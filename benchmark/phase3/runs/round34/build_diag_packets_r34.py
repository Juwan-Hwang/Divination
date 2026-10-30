#!/usr/bin/env python3
"""Round 34 liuren-diagnostic packet builder (host tooling, build-only).

60 diagnostic predictions (30 cases x FULL/CORE arms) are anonymized into
one packet. Outcomes come ONLY from judging/outcome-manifest.json.
Arm membership must stay invisible to judge seats: the full prediction
texts are copied verbatim to judging/diag-texts/<anon_id>.json (judges read
those), while judging/host-diag-mapping.json (anon -> {case_id, arm}) is
host-only and judge seats are forbidden to open it.
anon seed 20261035, prefix D34-.
"""
import json
import random
import shutil
import sys
from pathlib import Path

SEED = 20261035

ROUND_DIR = Path(__file__).resolve().parent
JUDGING = ROUND_DIR / "judging"
MANIFEST = JUDGING / "outcome-manifest.json"


def main():
    batches = json.loads((ROUND_DIR / "batches-diag.json").read_text(encoding="utf-8"))
    case_ids = sorted(c for k in ("D1", "D2", "D3") for c in batches[k])
    if len(case_ids) != 30 or len(set(case_ids)) != 30:
        print(f"FATAL: diag case ids = {len(case_ids)} unique {len(set(case_ids))}")
        return 1
    outcomes = json.loads(MANIFEST.read_text(encoding="utf-8"))["cases"]

    entries = []  # (case_id, arm, pred dict)
    for arm, sub in (("full", "full"), ("core", "core")):
        for cid in case_ids:
            p = ROUND_DIR / "diag-predictions" / sub / f"{cid}.json"
            if not p.is_file():
                print(f"FATAL: missing diag prediction {p}")
                return 1
            entries.append((cid, arm, json.loads(p.read_text(encoding="utf-8"))))
    if len(entries) != 60:
        print(f"FATAL: diag entries = {len(entries)}, expected 60")
        return 1

    rng = random.Random(SEED)
    mapping, used = {}, set()
    for cid, arm, _ in sorted(entries, key=lambda e: (e[0], e[1])):
        while True:
            anon = "D34-%08x" % rng.getrandbits(32)
            if anon not in used:
                used.add(anon)
                break
        mapping[anon] = {"case_id": cid, "arm": arm}

    texts_dir = JUDGING / "diag-texts"
    texts_dir.mkdir(parents=True, exist_ok=True)
    items = []
    for anon, ref in mapping.items():
        cid, arm = ref["case_id"], ref["arm"]
        src = ROUND_DIR / "diag-predictions" / arm / f"{cid}.json"
        shutil.copyfile(src, texts_dir / f"{anon}.json")
        pred = json.loads(src.read_text(encoding="utf-8"))
        items.append({
            "anon_id": anon,
            "prediction": {k: pred.get(k) for k in ("direction", "assertions", "timing", "summary")},
            "outcome_record": outcomes[cid],
        })
    items.sort(key=lambda x: x["anon_id"])

    with open(JUDGING / "packet-diag.json", "w", encoding="utf-8") as fh:
        json.dump(items, fh, ensure_ascii=False, indent=1)
    with open(JUDGING / "host-diag-mapping.json", "w", encoding="utf-8") as fh:
        json.dump(mapping, fh, ensure_ascii=False, indent=1)
    (JUDGING / "anon-seed-diag.txt").write_text(
        f"diag anon_id random seed: {SEED}\n"
        "method: random.Random(SEED) over entries sorted by (case_id, arm); "
        "anon = 'D34-%08x' % rng.getrandbits(32), redraw on collision.\n",
        encoding="utf-8")
    print(f"diag packet: {len(items)} items; texts copied: {len(list(texts_dir.glob('*.json')))}")
    print(f"arms in mapping: full={sum(1 for v in mapping.values() if v['arm']=='full')}, "
          f"core={sum(1 for v in mapping.values() if v['arm']=='core')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
