# -*- coding: utf-8 -*-
"""R91 h33 blind seat self-verify: read back each prediction by exact id."""
import json, os

IDS = ["DA-066","DA-067","DA-068","DA-070","DA-072","DA-073","DA-074",
       "BY-039","BY-041","BY-042","BY-043","BY-044","BY-045","BY-046",
       "WHY-092","WHY-093","WHY-095","WHY-096","WHY-098","WHY-099","WHY-100",
       "WHY-103","WHY-104","WHY-106","WHY-107","WHY-108","WHY-109","WHY-110"]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "predictions")
ok = 0; cm = ru = di = 0; problems = []
for cid in IDS:
    p = os.path.join(OUT, cid + ".json")
    try:
        with open(p, encoding="utf-8") as f:
            o = json.load(f)
    except Exception as e:
        problems.append((cid, "unreadable: %s" % e)); continue
    if o.get("case_id") != cid: problems.append((cid, "case_id mismatch"))
    if not o.get("prediction_text"): problems.append((cid, "empty prediction_text"))
    if not o.get("basis"): problems.append((cid, "empty basis"))
    c = o.get("confidence")
    if not (isinstance(c, (int, float)) and 0 <= c <= 1): problems.append((cid, "confidence out of range"))
    t = o.get("trigger") or {}
    for k in ("changed_main", "reserve_used", "disputed"):
        if not isinstance(t.get(k), bool): problems.append((cid, "trigger %s not bool" % k))
    if not isinstance(t.get("reason"), str): problems.append((cid, "trigger reason not str"))
    cm += bool(t.get("changed_main")); ru += bool(t.get("reserve_used")); di += bool(t.get("disputed"))
    ok += 1
print("verified_ok", ok, "of", len(IDS))
print("trigger_counts changed_main=%d reserve_used=%d disputed=%d" % (cm, ru, di))
print("problems", problems)
