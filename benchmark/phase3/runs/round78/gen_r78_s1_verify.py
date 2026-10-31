# -*- coding: utf-8 -*-
import json, os
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round78/predictions"
ids = (["AS-001","AS-002","AS-003","AS-004","AS-005","AS-007","AS-008","AS-009","AS-010","AS-011","AS-012","AS-013","AS-014","AS-015","AS-204","AS-205","AS-206","AS-207","AS-208","AS-209"]
 + ["AS-210","AS-211","AS-212","AS-213","AS-215","AS-301","AS-302","AS-303","AS-304","AS-305","AS-306","AS-307","BQ-001","BQ-010","BQ-011","BQ-012","BQ-013","BQ-014","BQ-015","BQ-016"]
 + ["BQ-017","BQ-018","BQ-019","BQ-020","BQ-021","BQ-022","BQ-023","BQ-024","BQ-025","BZ-016","BZ-019","BZ-020","BZ-021","BZ-022","BZ-023","BZ-024","BZ-025","BZ-026","BZ-027","BZ-028"])
assert len(ids) == 60 and len(set(ids)) == 60
cm = ru = di = 0; liuyao_n = 0
for cid in ids:
    with open(os.path.join(OUT, cid + ".json"), encoding="utf-8") as f:
        r = json.load(f)
    assert r["case_id"] == cid, cid
    assert set(r.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}, (cid, r.keys())
    assert r["prediction_text"].strip() and r["basis"].strip()
    assert 0.0 <= r["confidence"] <= 1.0
    t = r["trigger"]
    assert set(t.keys()) == {"changed_main","reserve_used","disputed","reason"}
    if cid.startswith("BQ-") and cid != "BQ-001":
        liuyao_n += 1
        cm += t["changed_main"]; ru += t["reserve_used"]; di += t["disputed"]
    else:
        assert t == {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}, (cid, t)
print("TOTAL verified files: 60 / 60")
print("六爻例数 (BQ-010..025):", liuyao_n)
print("trigger counts: changed_main=%d reserve_used=%d disputed=%d" % (cm, ru, di))
