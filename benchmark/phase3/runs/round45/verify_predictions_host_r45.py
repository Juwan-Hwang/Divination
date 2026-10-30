#!/usr/bin/env python3
"""R45 host B05 verification (PREREG s.10 B05 clause): disk-first check of
all platform predictions before freezing / packet building.
Hard assertions (any failure aborts):
  1. prediction file set == batches.json id set (487, unique);
  2. every file parses, case_id matches filename, required fields present
     (case_id / prediction_text / basis / confidence / trigger with the
     three booleans + reason), confidence numeric in [0,1];
  3. B07 provenance cross-check: disk trigger sums for batch B07 are
     recomputed and printed (host compares against the final-seat
     read-back record in ADDENDUM-1).
Host tooling, verify-only; no scoring."""
import json
import sys
from pathlib import Path

R45 = Path(__file__).resolve().parent
P3 = R45.parents[1]
BATCHES = R45 / "batches.json"
PRED = R45 / "predictions"
REQ = {"case_id", "prediction_text", "basis", "confidence", "trigger"}


def main():
    batches = json.loads(BATCHES.read_text(encoding="utf-8"))
    batch_ids = {cid for ids in batches.values() for cid in ids}
    files = {p.stem for p in PRED.glob("*.json")}
    if files != batch_ids or len(files) != 487:
        print(f"FATAL: prediction files {len(files)} vs batches ids {len(batch_ids)}; "
              f"missing {sorted(batch_ids - files)[:8]} extra {sorted(files - batch_ids)[:8]}")
        return 1
    bad = []
    for cid in sorted(files):
        try:
            p = json.loads((PRED / f"{cid}.json").read_text(encoding="utf-8"))
        except Exception as e:
            bad.append((cid, f"parse: {e}"))
            continue
        if p.get("case_id") != cid or not REQ.issubset(p.keys()):
            bad.append((cid, "schema"))
            continue
        t = p.get("trigger") or {}
        if not all(k in t for k in ("changed_main", "reserve_used", "disputed", "reason")):
            bad.append((cid, "trigger"))
        c = p.get("confidence")
        if not isinstance(c, (int, float)) or not (0 <= c <= 1):
            bad.append((cid, "confidence"))
        if not str(p.get("prediction_text") or "").strip():
            bad.append((cid, "empty prediction_text"))
    if bad:
        print(f"FATAL: {len(bad)} bad files: {bad[:10]}")
        return 1
    sums = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
    for cid in batches["B07"]:
        t = json.loads((PRED / f"{cid}.json").read_text(encoding="utf-8"))["trigger"]
        for k in sums:
            sums[k] += 1 if t.get(k) else 0
    print(f"OK: 487/487 prediction files present, schema-valid, case_id aligned.")
    print(f"B07 disk trigger sums (host recompute): {sums}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
