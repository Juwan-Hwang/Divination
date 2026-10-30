#!/usr/bin/env python3
"""R49 host verification of blind predictions (B05 clause): per-batch,
per batches.json id list only (no glob over other batches' files beyond
the predictions dir listing for the total count). Checks: file exists,
JSON parses, fields complete, case_id matches filename, prediction_text
non-empty. Also recomputes trigger counts over liuyao cases.
Exit 0 iff all 487 pass.
"""
import json
import sys
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round49")
PRED = BASE / "predictions"
batches = json.loads((BASE / "batches.json").read_text(encoding="utf-8"))

need_fields = {"case_id", "prediction_text", "basis", "confidence", "trigger"}
trig_keys = {"changed_main", "reserve_used", "disputed", "reason"}

bad = []
total = 0
trig = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
for bname, ids in sorted(batches.items()):
    for cid in ids:
        total += 1
        p = PRED / f"{cid}.json"
        if not p.exists():
            bad.append((cid, "missing"))
            continue
        try:
            d = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            bad.append((cid, f"json error {e}"))
            continue
        if d.get("case_id") != cid:
            bad.append((cid, f"case_id mismatch {d.get('case_id')}"))
        if not need_fields.issubset(d.keys()):
            bad.append((cid, f"fields missing {need_fields - set(d.keys())}"))
        if not (d.get("prediction_text") or "").strip():
            bad.append((cid, "empty prediction_text"))
        t = d.get("trigger") or {}
        if not trig_keys.issubset(t.keys()):
            bad.append((cid, f"trigger keys missing {trig_keys - set(t.keys())}"))
        else:
            for k in ("changed_main", "reserve_used", "disputed"):
                if t.get(k) is True:
                    trig[k] += 1

on_disk = len(list(PRED.glob("*.json")))
print(f"batches total ids: {total}")
print(f"prediction files on disk: {on_disk}")
print(f"bad: {len(bad)}")
for cid, why in bad[:40]:
    print("BAD", cid, why)
print(f"trigger counts (all cases): {trig}")
sys.exit(0 if (not bad and total == 487 and on_disk == 487) else 1)
