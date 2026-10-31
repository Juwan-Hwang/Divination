#!/usr/bin/env python3
"""R88 host verification of holdout31 acceptance blind predictions.
Checks the 28 expected files under acceptance/predictions: JSON parses,
five fields present, case_id matches filename, confidence in [0,1],
trigger booleans are bool; recounts trigger totals. Writes
acceptance/verify-acc-predictions-host-r88.json.
"""
import json
from pathlib import Path

ACC = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round88/acceptance")
IDS = ["DA-047", "DA-048", "DA-050", "DA-051", "DA-054", "DA-055", "DA-057",
       "BY-022", "BY-023", "BY-024", "BY-025", "BY-027", "BY-028", "BY-030",
       "WHY-037", "WHY-038", "WHY-039", "WHY-040", "WHY-041", "WHY-042",
       "WHY-043", "WHY-044", "WHY-068", "WHY-069",
       "GSZ-107", "GSZ-108", "GSZ-109", "GSZ-110"]
FIELDS = {"case_id", "prediction_text", "basis", "confidence", "trigger"}

missing, bad, trig = [], {}, {"changed_main": 0, "reserve_used": 0, "disputed": 0}
for cid in IDS:
    p = ACC / "predictions" / f"{cid}.json"
    if not p.exists():
        missing.append(cid)
        continue
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
        assert FIELDS <= set(d), sorted(set(d))
        assert d["case_id"] == cid
        assert isinstance(d["confidence"], (int, float)) and 0 <= d["confidence"] <= 1
        t = d["trigger"]
        for k in trig:
            assert isinstance(t[k], bool), (cid, k)
            trig[k] += int(t[k])
    except Exception as e:  # noqa: BLE001
        bad[cid] = repr(e)
extra = sorted(f.stem for f in (ACC / "predictions").glob("*.json") if f.stem not in IDS)
out = {"want": len(IDS), "missing": missing, "extra": extra, "bad": bad, "trigger": trig}
(ACC / "verify-acc-predictions-host-r88.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(out)
assert not missing and not extra and not bad
