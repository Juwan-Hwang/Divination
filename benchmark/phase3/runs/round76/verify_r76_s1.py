import json, os
BASE="/home/hatch/workspace/divination/benchmark/phase3/runs/round76"
b=json.load(open(f"{BASE}/batches.json"))
ids=b["B01"]+b["B02"]+b["B03"]
cm=ru=di=0; tot=0
for cid in ids:
    p=f"{BASE}/predictions/{cid}.json"
    d=json.load(open(p))
    assert d["case_id"]==cid and set(d)== {"case_id","prediction_text","basis","confidence","trigger"}, cid
    assert 0<=d["confidence"]<=1
    t=d["trigger"]; assert set(t)=={"changed_main","reserve_used","disputed","reason"}
    cm+=t["changed_main"]; ru+=t["reserve_used"]; di+=t["disputed"]
    s=os.path.getsize(p); tot+=s
    print(cid, s, t["changed_main"], t["reserve_used"], t["disputed"])
print("TOTAL", len(ids), "bytes", tot, "changed_main", cm, "reserve_used", ru, "disputed", di)
