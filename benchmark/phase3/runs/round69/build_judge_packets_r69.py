#!/usr/bin/env python3
"""Round 69 judging packet builder (host tooling, build-only; no scoring).

Hygiene-1 implementation (carried from R35 PREREG s.4): outcomes come
ONLY from the explicit source manifest this round's judging/outcome-manifest.json (R69 build per PREREG s.0: 487 cases verbatim, LR2-016 editor note split-registered, fifteen carryover note layers attached as separate packet fields). No rglob / tree search anywhere in this script.

Packet shape mirrors R50: items {"anon_id", "prediction": {direction,
assertions, timing, summary} (pred.get(k), null by design),
"outcome_record"}, json.dump(ensure_ascii=False, indent=1).
anon seed 20261075. host-meta copied forward (round68 judging copy) and verified
against the 487 id set. Per-view JSONL copies judgeX/judgeY-block1..4
emitted as in R50 (one shared anonymisation mapping; views differ only
at judging time).
"""
import json
import random
import shutil
import sys
from pathlib import Path

SEED = 20261075

ROUND_DIR = Path(__file__).resolve().parent
PRED_DIR = ROUND_DIR / "predictions"
JUDGING = ROUND_DIR / "judging"
MANIFEST = JUDGING / "outcome-manifest.json"
META_SRC = ROUND_DIR.parent / "round68" / "judging" / "host-meta.json"
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

    carry56 = manifest.get("_r56_carryover_notes", {})
    carry57 = manifest.get("_r57_carryover_notes_addendum", {})
    carry58 = manifest.get("_r58_carryover_notes_addendum", {})
    carry59 = manifest.get("_r59_carryover_notes_addendum", {})
    carry60a = manifest.get("_r60_carryover_notes_addendum_a", {})
    carry60b = manifest.get("_r60_carryover_notes_addendum_b", {})
    carry61 = manifest.get("_r61_carryover_notes_addendum", {})
    carry62 = manifest.get("_r62_carryover_notes_addendum", {})
    carry63 = manifest.get("_r63_carryover_notes_addendum", {})
    carry64 = manifest.get("_r64_carryover_notes_addendum", {})
    carry65 = manifest.get("_r65_carryover_notes_addendum", {})
    carry66 = manifest.get("_r66_carryover_notes_addendum", {})
    carry67 = manifest.get("_r67_carryover_notes_addendum", {})
    carry68 = manifest.get("_r68_carryover_notes_addendum", {})
    carry69 = manifest.get("_r69_carryover_notes_addendum", {})
    assert len(carry56) == 29 and len(carry57) == 21 and len(carry58) == 17 and len(carry59) == 29 and len(carry60a) == 14 and len(carry60b) == 20 and len(carry61) == 34 and len(carry62) == 58 and len(carry63) == 65 and len(carry64) == 72 and len(carry65) == 99 and len(carry66) == 40 and len(carry67) == 41 and len(carry68) == 35 and len(carry69) == 58, (
        len(carry56), len(carry57), len(carry58), len(carry59), len(carry60a), len(carry60b), len(carry61), len(carry62), len(carry63), len(carry64), len(carry65), len(carry66), len(carry67), len(carry68), len(carry69))
    carry_notes = {}
    for cid in set(carry56) | set(carry57) | set(carry58) | set(carry59) | set(carry60a) | set(carry60b) | set(carry61) | set(carry62) | set(carry63) | set(carry64) | set(carry65) | set(carry66) | set(carry67) | set(carry68) | set(carry69):
        parts = []
        if cid in carry56:
            parts.append("[R56-carryover] " + carry56[cid])
        if cid in carry57:
            parts.append("[R57-addendum] " + carry57[cid])
        if cid in carry58:
            parts.append("[R58-addendum] " + carry58[cid])
        if cid in carry59:
            parts.append("[R59-addendum] " + carry59[cid])
        if cid in carry60a:
            parts.append("[R60-addendum-a] " + carry60a[cid])
        if cid in carry60b:
            parts.append("[R60-addendum-b] " + carry60b[cid])
        if cid in carry61:
            parts.append("[R61-addendum] " + carry61[cid])
        if cid in carry62:
            parts.append("[R62-addendum] " + carry62[cid])
        if cid in carry63:
            parts.append("[R63-addendum] " + carry63[cid])
        if cid in carry64:
            parts.append("[R64-addendum] " + carry64[cid])
        if cid in carry65:
            parts.append("[R65-addendum] " + carry65[cid])
        if cid in carry66:
            parts.append("[R66-addendum] " + carry66[cid])
        if cid in carry67:
            parts.append("[R67-addendum] " + carry67[cid])
        if cid in carry68:
            parts.append("[R68-addendum] " + carry68[cid])
        if cid in carry69:
            parts.append("[R69-addendum] " + carry69[cid])
        carry_notes[cid] = "\n".join(parts)
    lr_split = manifest.get("_r56_lr2016_split", {})
    items = []
    for anon, cid in mapping.items():
        pred = json.loads((PRED_DIR / f"{cid}.json").read_text(encoding="utf-8"))
        item = {
            "anon_id": anon,
            "prediction": {k: pred.get(k) for k in ("direction", "assertions", "timing", "summary")},
            "outcome_record": outcomes[cid],
        }
        if cid in carry_notes:
            item["carry_note"] = carry_notes[cid]
        if lr_split.get("case_id") == cid:
            item["editor_note"] = lr_split["editor_note"]
        items.append(item)
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

    # Per-view JSONL copies of the same four blocks (as R48).
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

    shutil.copyfile(META_SRC, JUDGING / "host-meta.json")
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
        "R56 PREREG hygiene rule carried from R35).\n",
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
