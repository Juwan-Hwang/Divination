# -*- coding: utf-8 -*-
import json, os
BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round77/predictions"
IDS = ["MP-017","MP-018","MP-019"] + ["OC-%03d" % i for i in range(1,31)] + ["WP-%03d" % i for i in range(1,8)]
assert len(IDS) == 40
cnt = {"changed_main":0, "reserve_used":0, "disputed":0}
total_bytes = 0
for cid in IDS:
    p = os.path.join(BASE, cid + ".json")
    sz = os.path.getsize(p)
    total_bytes += sz
    with open(p, encoding="utf-8") as f:
        o = json.load(f)
    assert o["case_id"] == cid, cid
    assert set(o.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}, (cid, o.keys())
    assert 0 <= o["confidence"] <= 1
    lines = o["basis"].split("\n")
    assert lines[0].startswith("tradition"), cid
    assert lines[1].startswith("systems_used"), cid
    for k in cnt:
        if o["trigger"][k]:
            cnt[k] += 1
    print(cid, sz)
print("files_ok=40 total_bytes=", total_bytes)
print("trigger_true_counts=", cnt)
