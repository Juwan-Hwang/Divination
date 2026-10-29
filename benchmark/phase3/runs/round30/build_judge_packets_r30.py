#!/usr/bin/env python3
"""Round 30 judging packet builder (host tooling, build-only; no scoring).

体例参照 runs/round29/judging/packetA.json 与 host-meta.json（只学结构）：
每条 {"anon_id", "prediction": {"direction","assertions","timing","summary"},
"outcome_record"}，json.dump(ensure_ascii=False, indent=1)。

- 我方预测：runs/round30/predictions/<case_id>.json，prediction 四键以
  p.get(k) 取值（与 phase3/build_packets.py 原建包器逐字同法；本轮预测
  文件无此四键，故为 null，与 round29 包逐字同构）。
- 结局金标：按 case_id 全域检索池内病例记录的 outcome 字段，首命中为准。
  检索域（按优先级）：benchmark/ 下各 cases.jsonl ->
  benchmark/data/ 与 benchmark/phase3/data/ 的 roster/cases 文件 ->
  benchmark/phase2/data/roster.jsonl -> 其余 benchmark/ 下 roster*.jsonl。
  outcome 取值：outcome_record(str) | outcome(str) | outcome.description。
- 勘误 overlay：benchmark/phase3/data/outcome-errata-overlay.json（13 例，
  键为 case_id，值为更正后 outcome 文本字符串；若值为 dict 则取其
  corrected_outcome 字段）。命中 id 一律替换，并逐例自验逐字一致。
- anon_id：P3-<8 位十六进制>，随机分配，种子 SEED = 20261030
  （random.Random(SEED)，按 case_id 排序序逐例 getrandbits(32) 生成，
  撞号重抽）；种子另记于 judging/anon-seed.txt。
- host-meta：池与 round29 相同，直接复制 round29 的 host-meta.json
  并验键集与本轮 487 id 集全等。
"""
import collections
import json
import random
import shutil
import sys
from pathlib import Path

SEED = 20261030

ROUND_DIR = Path(__file__).resolve().parent          # runs/round30
BENCH = ROUND_DIR.parents[2]                          # benchmark/
DIV_ROOT = BENCH.parent                               # divination/
PRED_DIR = ROUND_DIR / "predictions"
JUDGING = ROUND_DIR / "judging"
R29_META = BENCH / "phase3" / "runs" / "round29" / "judging" / "host-meta.json"
OVERLAY_PATH = BENCH / "phase3" / "data" / "outcome-errata-overlay.json"


def extract_outcome(rec):
    """从一条病例记录里取 outcome 文本；取不到返回 None。"""
    v = rec.get("outcome_record")
    if isinstance(v, str) and v.strip():
        return v
    o = rec.get("outcome")
    if isinstance(o, str) and o.strip():
        return o
    if isinstance(o, dict):
        for key in ("description", "outcome_record", "text"):
            d = o.get(key)
            if isinstance(d, str) and d.strip():
                return d
    return None


def iter_records(path):
    if path.suffix == ".jsonl":
        with open(path, encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(rec, dict):
                    yield rec
    elif path.suffix == ".json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return
        if isinstance(data, list):
            for rec in data:
                if isinstance(rec, dict):
                    yield rec
        elif isinstance(data, dict):
            for key, val in data.items():
                if isinstance(val, dict):
                    rec = dict(val)
                    rec.setdefault("id", key)
                    yield rec


def candidate_files():
    ordered, seen = [], set()

    def add(path):
        if path.is_file() and path not in seen:
            seen.add(path)
            ordered.append(path)

    # 1) benchmark/ 下各 expansion 的 cases.jsonl
    for p in sorted(BENCH.rglob("cases.jsonl")):
        add(p)
    # 2) benchmark/data/ 与 benchmark/phase3/data/ 的 roster/cases 文件
    for base in (BENCH / "data", BENCH / "phase3" / "data"):
        if base.is_dir():
            for p in sorted(base.iterdir()):
                if p.is_file() and ("roster" in p.name or "cases" in p.name):
                    add(p)
    # 3) phase2 roster
    add(BENCH / "phase2" / "data" / "roster.jsonl")
    # 4) 其余 roster*.jsonl
    for p in sorted(BENCH.rglob("roster*.jsonl")):
        add(p)
    return ordered


def main():
    pred_files = sorted(PRED_DIR.glob("*.json"))
    case_ids = [p.stem for p in pred_files]
    if len(case_ids) != 487 or len(set(case_ids)) != 487:
        print(f"FATAL: predictions = {len(case_ids)} (unique {len(set(case_ids))}), expected 487")
        return 1
    need = set(case_ids)

    # ---- 结局全域检索（首命中） ----
    outcomes, sources = {}, {}
    for path in candidate_files():
        rel = str(path.relative_to(DIV_ROOT))
        for rec in iter_records(path):
            cid = rec.get("id") or rec.get("case_id")
            if cid in need and cid not in outcomes:
                oc = extract_outcome(rec)
                if oc is not None:
                    outcomes[cid] = oc
                    sources[cid] = rel
    missing = sorted(need - set(outcomes))
    if missing:
        print(f"FATAL: outcome not found for {len(missing)} cases: {missing}")
        return 1
    source_counts = collections.Counter(sources[cid] for cid in case_ids)

    # ---- overlay 替换 ----
    overlay_raw = json.loads(OVERLAY_PATH.read_text(encoding="utf-8"))
    overlay = {}
    for key, val in overlay_raw.items():
        if key == "_comment":
            continue
        overlay[key] = val["corrected_outcome"] if isinstance(val, dict) else val
    if len(overlay) != 13:
        print(f"FATAL: overlay entries = {len(overlay)}, expected 13")
        return 1
    for cid, corrected in overlay.items():
        if cid not in outcomes:
            print(f"FATAL: overlay id {cid} not in pool")
            return 1
        outcomes[cid] = corrected

    # ---- anon 随机分配（种子见文件头与 judging/anon-seed.txt） ----
    rng = random.Random(SEED)
    mapping, used = {}, set()
    for cid in case_ids:  # case_ids 已按文件名排序
        while True:
            anon = "P3-%08x" % rng.getrandbits(32)
            if anon not in used:
                used.add(anon)
                break
        mapping[anon] = cid

    # ---- 组包 ----
    items = []
    for anon, cid in mapping.items():
        pred = json.loads((PRED_DIR / f"{cid}.json").read_text(encoding="utf-8"))
        items.append({
            "anon_id": anon,
            "prediction": {k: pred.get(k) for k in ("direction", "assertions", "timing", "summary")},
            "outcome_record": outcomes[cid],
        })
    items.sort(key=lambda x: x["anon_id"])

    # overlay 逐例自验：包内文本与 corrected 逐字一致
    by_case = {mapping[e["anon_id"]]: e["outcome_record"] for e in items}
    overlay_ok = sum(1 for cid, corr in overlay.items() if by_case.get(cid) == corr)
    if overlay_ok != 13:
        print(f"FATAL: overlay verification {overlay_ok}/13")
        return 1

    JUDGING.mkdir(parents=True, exist_ok=True)

    def dump(obj, name):
        with open(JUDGING / name, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)

    packet_a, packet_b = items[:244], items[244:]
    dump(packet_a, "packetA.json")
    dump(packet_b, "packetB.json")
    blocks = [items[0:122], items[122:244], items[244:366], items[366:487]]
    for i, block in enumerate(blocks, start=1):
        dump(block, f"packet{i}.json")
    dump(mapping, "host-mapping.json")

    # host-meta：以 round29 为底复制并验键集全等
    shutil.copyfile(R29_META, JUDGING / "host-meta.json")
    meta = json.loads((JUDGING / "host-meta.json").read_text(encoding="utf-8"))
    if set(meta.keys()) != need:
        print("FATAL: host-meta key set != round30 case id set")
        return 1

    (JUDGING / "anon-seed.txt").write_text(
        f"anon_id random seed: {SEED}\n"
        "method: random.Random(SEED); for case_id in sorted(case_ids): "
        "anon = 'P3-%08x' % rng.getrandbits(32), redraw on collision.\n",
        encoding="utf-8")

    # ---- 自报核对 ----
    anons = [e["anon_id"] for e in items]
    nonempty = sum(1 for e in items if isinstance(e["outcome_record"], str) and e["outcome_record"].strip())
    print(f"predictions: {len(case_ids)}")
    print(f"outcomes found: {len(outcomes)}/487")
    for src, cnt in sorted(source_counts.items()):
        print(f"  source {src}: {cnt}")
    print(f"overlay replaced & verified: {overlay_ok}/13")
    print(f"packetA: {len(packet_a)}, packetB: {len(packet_b)}, total: {len(items)}")
    print(f"blocks packet1-4: {[len(b) for b in blocks]}")
    print(f"anon unique: {len(set(anons))}/{len(anons)}, A/B overlap: {len(set(e['anon_id'] for e in packet_a) & set(e['anon_id'] for e in packet_b))}")
    print(f"outcome non-empty: {nonempty}/{len(items)}")
    print(f"host-meta keys: {len(meta)} == case set: {set(meta.keys()) == need}")
    print(f"host-mapping entries: {len(mapping)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
