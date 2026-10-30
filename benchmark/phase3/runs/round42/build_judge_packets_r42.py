#!/usr/bin/env python3
"""Round 42 judging packet builder (host tooling, build-only; no scoring).

Hygiene-1 implementation (carried from R35 PREREG s.4): outcomes come
ONLY from the explicit source manifest runs/round42/judging/
outcome-manifest.json (itself a verbatim carry-over of R41 per R42
PREREG). No rglob / tree search anywhere in this script.

Packet shape mirrors R41: items {"anon_id", "prediction": {direction,
assertions, timing, summary} (pred.get(k), null by design),
"outcome_record"}, json.dump(ensure_ascii=False, indent=1).
anon seed 20261042. host-meta copied from round41 judging and verified
against the 487 id set. Per-view JSONL copies judgeX/judgeY-block1..4
emitted as in R41 (one shared anonymisation mapping; views differ only
at judging time).
"""
import json
import random
import shutil
import sys
from pathlib import Path

SEED = 20261042

ROUND_DIR = Path(__file__).resolve().parent
PRED_DIR = ROUND_DIR / "predictions"
JUDGING = ROUND_DIR / "judging"
MANIFEST = JUDGING / "outcome-manifest.json"
R41_META = ROUND_DIR.parent / "round41" / "judging" / "host-meta.json"
OVERLAY_PATH = ROUND_DIR.parents[1] / "data" / "outcome-errata-overlay.json"
BATCHES = ROUND_DIR / "batches.json"


def main():
    JUDGING.mkdir(parents=True, exist_ok=True)
    pred_files = sorted(PRED_DIR.glob("*.json"))
    case_ids = [p.stem for p in pred_files]
    if len(case_ids) != 487 or len(set(case_ids)) != 487:
        print(f"FATAL: predictions = {len(case_ids)} (unique {len(set(case_ids))}), expected 487")
        return 1
    need = set(case_ids)

    batches = json.loads(BATCHES.read_text(encoding="utf-8"))
    batch_ids = {cid for ids in batches.values() for cid in ids}
    if batch_ids != need or len(batch_ids) != 487:
        print(f"FATAL: batches.json id set != prediction id set "
              f"({len(batch_ids)} vs {len(need)})")
        return 1
    print("batches.json id set == prediction id set (487)")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    outcomes = manifest["cases"]
    if set(outcomes) != need:
        print(f"FATAL: manifest keys != prediction ids; "
              f"missing {sorted(need - set(outcomes))[:5]} extra {sorted(set(outcomes) - need)[:5]}")
        return 1

    overlay_raw = json.loads(OVERLAY_PATH.read_text(encoding="utf-8"))
    overlay = {k: (v["corrected_outcome"] if isinstance(v, dict) else v)
               for k, v in overlay_raw.items() if k != "_comment"}
    if len(overlay) != 16:
        print(f"FATAL: overlay entries = {len(overlay)}, expected 16")
        return 1
    ok = sum(1 for cid, corr in overlay.items() if outcomes.get(cid) == corr)
    if ok != 16:
        print(f"FATAL: overlay verbatim check {ok}/16 against manifest")
        return 1
    print("overlay 16/16 verbatim in manifest outcomes")

    rng = random.Random(SEED)
    mapping, used = {}, set()
    for cid in case_ids:
        while True:
            anon = "P3-%08x" % rng.getrandbits(32)
            if anon not in used:
                used.add(anon)
                break
        mapping[anon] = cid

    items = []
    for anon, cid in mapping.items():
        pred = json.loads((PRED_DIR / f"{cid}.json").read_text(encoding="utf-8"))
        items.append({
            "anon_id": anon,
            "prediction": {k: pred.get(k) for k in ("direction", "assertions", "timing", "summary")},
            "outcome_record": outcomes[cid],
        })
    items.sort(key=lambda x: x["anon_id"])

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

    # Per-view JSONL copies of the same four blocks (as R41).
    for view in ("judgeX", "judgeY"):
        total, seen = 0, set()
        for i, block in enumerate(blocks, start=1):
            with open(JUDGING / f"{view}-block{i}.jsonl", "w", encoding="utf-8") as fh:
                for e in block:
                    fh.write(json.dumps(e, ensure_ascii=False) + "\n")
            total += len(block)
            seen.update(e["anon_id"] for e in block)
        if total != 487 or len(seen) != 487:
            print(f"FATAL: {view} JSONL total {total}, unique anon {len(seen)}, expected 487/487")
            return 1
        print(f"{view} JSONL blocks: {[len(b) for b in blocks]}, total {total}, anon unique {len(seen)}/487")

    shutil.copyfile(R41_META, JUDGING / "host-meta.json")
    meta = json.loads((JUDGING / "host-meta.json").read_text(encoding="utf-8"))
    if set(meta.keys()) != need:
        print("FATAL: host-meta key set != case id set")
        return 1
    if set(meta.keys()) != batch_ids:
        print("FATAL: host-meta key set != batches.json id set")
        return 1

    (JUDGING / "anon-seed.txt").write_text(
        f"anon_id random seed: {SEED}\n"
        "method: random.Random(SEED); for case_id in sorted(case_ids): "
        "anon = 'P3-%08x' % rng.getrandbits(32), redraw on collision.\n"
        "outcome source: judging/outcome-manifest.json ONLY (explicit manifest, "
        "R42 PREREG hygiene rule carried from R35).\n",
        encoding="utf-8")

    anons = [e["anon_id"] for e in items]
    nonempty = sum(1 for e in items if isinstance(e["outcome_record"], str) and e["outcome_record"].strip())
    print(f"predictions: {len(case_ids)}")
    print(f"packetA: {len(packet_a)}, packetB: {len(packet_b)}, total: {len(items)}")
    print(f"blocks packet1-4: {[len(b) for b in blocks]}")
    print(f"anon unique: {len(set(anons))}/{len(anons)}")
    print(f"outcome non-empty: {nonempty}/{len(items)}")
    print(f"host-meta keys: {len(meta)} == case set: {set(meta.keys()) == need}")
    print(f"host-mapping entries: {len(mapping)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
