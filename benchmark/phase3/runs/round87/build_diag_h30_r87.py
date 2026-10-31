import json, os
base="/home/hatch/workspace/divination/benchmark/phase3"
ids=["BY-017","BY-018","BY-020","BY-021","CYJ-006","CYJ-007","CYJ-008","CYJ-009","CYJ-010","DA-038","DA-041","DA-042","DA-044","DA-046","GSZ-101","GSZ-103","GSZ-104","GSZ-105","WHY-025","WHY-026","WHY-027","WHY-028","WHY-031","WHY-032","WHY-033","WHY-034","WHY-035","WHY-036"]
assert len(ids)==28 and len(set(ids))==28
# gold
gold={}
with open(f"{base}/holdout30/test_gold.jsonl",encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if not line: continue
        o=json.loads(line)
        gid=o.get("id") or o.get("case_id") or o.get("case")
        gold[gid]=o
print("gold ids", sorted(gold.keys()))
assert set(gold.keys())==set(ids), (set(ids)-set(gold.keys()), set(gold.keys())-set(ids))
# host mapping
with open(f"{base}/runs/round87/acceptance/judging/host-mapping.json",encoding="utf-8") as f:
    hm=json.load(f)
print("host-mapping", json.dumps(hm,ensure_ascii=False)[:2000])
# judges
def load_jsonl(p):
    out=[]
    with open(p,encoding="utf-8") as f:
        for line in f:
            if line.strip(): out.append(json.loads(line))
    return out
judges={}
for name in ["judgeO1","judgeO2","judgeM1","judgeM2"]:
    judges[name]=load_jsonl(f"{base}/runs/round87/acceptance/judging/{name}.jsonl")
    print(name, len(judges[name]), json.dumps(judges[name][0],ensure_ascii=False)[:1200])
# snapshot scandir only (necessary to locate chapter files, will self-report)
snap=f"{base}/runs/round86/kb-snapshot-holdout30"
for root,dirs,files in os.walk(snap):
    level=root.replace(snap,'')
    print("SNAP", level, sorted(files), sorted(dirs))
