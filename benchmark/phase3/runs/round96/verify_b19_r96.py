# -*- coding: utf-8 -*-
"""R96 B19 verification: exact-id reads only, no directory enumeration."""
import json, os
BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round96/predictions"
IDS = ["MP-017","MP-018","MP-019","OC-001","OC-002","OC-003","OC-004","OC-005",
       "OC-006","OC-007","OC-008","OC-009","OC-010","OC-011","OC-012","OC-013",
       "OC-014","OC-015","OC-016","OC-017"]
total = 0
trig_counts = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
for cid in IDS:
    p = f"{BASE}/{cid}.json"
    with open(p, encoding="utf-8") as f:
        o = json.load(f)
    assert set(o.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}, cid
    assert o["case_id"] == cid
    assert isinstance(o["confidence"], (int,float)) and 0 <= o["confidence"] <= 1
    t = o["trigger"]
    assert set(t.keys()) == {"changed_main","reserve_used","disputed","reason"}, cid
    assert t["reason"] == "" and all(t[k] is False for k in trig_counts), cid
    b = o["basis"]
    lines = b.splitlines()
    assert lines[0].startswith("tradition"), cid
    assert lines[1].startswith("systems_used:"), cid
    assert "第八节" in b and "功量核" in b, cid
    assert "主线认定：" in b, cid
    total += os.path.getsize(p)
print("OK files:", len(IDS), "total_bytes:", total, "trigger_true_counts:", trig_counts)
