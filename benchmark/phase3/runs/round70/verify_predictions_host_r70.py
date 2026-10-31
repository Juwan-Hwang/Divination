import json, os, sys
BASE="/home/hatch/workspace/divination/benchmark/phase3"
b=json.load(open(f"{BASE}/runs/round70/batches.json"))
want=[]
for k,v in b.items(): want+=v
assert len(want)==487 and len(set(want))==487
P=f"{BASE}/runs/round70/predictions"
files=set(fn[:-5] for fn in os.listdir(P) if fn.endswith(".json"))
missing=[c for c in want if c not in files]
extra=[c for c in files if c not in set(want)]
bad=[]
trig={"changed_main":0,"reserve_used":0,"disputed":0}
for c in want:
    try:
        d=json.load(open(f"{P}/{c}.json"))
        assert d["case_id"]==c, "case_id mismatch"
        for f in ("prediction_text","basis","confidence","trigger"):
            assert f in d and d[f] not in (None,""), f"missing {f}"
        assert isinstance(d["confidence"],(int,float)) and 0<=d["confidence"]<=1
        t=d["trigger"]
        for f in ("changed_main","reserve_used","disputed","reason"):
            assert f in t, f"trigger missing {f}"
        for f in ("changed_main","reserve_used","disputed"):
            assert isinstance(t[f],bool)
            if t[f]: trig[f]+=1
    except Exception as e:
        bad.append((c,str(e)))
print("want",len(want),"files",len(files),"missing",missing,"extra",extra,"bad",bad)
print("trigger recount:",trig)
assert not missing and not extra and not bad
print("HOST VERIFY OK 487/487")
