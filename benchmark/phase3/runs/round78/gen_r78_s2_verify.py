import json
BASE="/home/hatch/workspace/divination/benchmark/phase3"
# fix one stray english word in LR2-016
p=f"{BASE}/runs/round78/predictions/LR2-016.json"
d=json.load(open(p,encoding="utf-8"))
d["prediction_text"]=d["prediction_text"].replace("阴私文书之 slow 审","阴私文书之迟审")
json.dump(d,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)

batches=json.load(open(f"{BASE}/runs/round78/batches.json",encoding="utf-8"))
ids=batches["B04"]+batches["B05"]+batches["B06"]
assert len(ids)==60
trig={"changed_main":0,"reserve_used":0,"disputed":0}
liuyao_ids=[]
problems=[]
for cid in ids:
    card=json.load(open(f"{BASE}/inputs-dev12/{cid}.json",encoding="utf-8"))
    d=json.load(open(f"{BASE}/runs/round78/predictions/{cid}.json",encoding="utf-8"))
    assert set(d)=={"case_id","prediction_text","basis","confidence","trigger"}, cid
    assert d["case_id"]==cid
    assert isinstance(d["confidence"],(int,float)) and 0<=d["confidence"]<=1
    assert d["prediction_text"].strip() and d["basis"].strip()
    assert "systems_used" in d["basis"], cid
    first=d["basis"].splitlines()[0]
    val=card.get("tradition", card.get("system"))
    if val is not None:
        assert first==val, (cid, first, val)
    else:
        assert first.startswith("卡面未标注 tradition"), (cid, first)
    is_ly = val=="liuyao"
    if is_ly: liuyao_ids.append(cid)
    t=d["trigger"]
    assert set(t)=={"changed_main","reserve_used","disputed","reason"}
    if is_ly:
        for k in trig:
            if t[k]: trig[k]+=1
        if not any(t[k] for k in trig):
            assert t["reason"]=="", cid
    else:
        assert t=={"changed_main":False,"reserve_used":False,"disputed":False,"reason":""}, (cid,t)
print("ALL 60 VERIFIED")
print("liuyao cases:", len(liuyao_ids), liuyao_ids)
print("liuyao trigger counts:", trig)
for cid in ids:
    d=json.load(open(f"{BASE}/runs/round78/predictions/{cid}.json",encoding="utf-8"))
    if d["trigger"]["disputed"]:
        print("disputed:", cid, d["trigger"]["reason"][:40])
