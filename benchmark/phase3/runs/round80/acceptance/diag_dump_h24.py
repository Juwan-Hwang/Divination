import json, os
BASE="/home/hatch/workspace/divination/benchmark/phase3"
ACC=f"{BASE}/runs/round80/acceptance"
gold={}
for line in open(f"{BASE}/holdout24/test_gold.jsonl"):
    line=line.strip()
    if line:
        g=json.loads(line); gold[g.get("case_id") or g.get("id")]=g
hm=json.load(open(f"{ACC}/judging/host-mapping.json"))
rev=hm["ours"]
jo={}
for f in ("judgeO1","judgeO2"):
    for line in open(f"{ACC}/judging/{f}.jsonl"):
        line=line.strip()
        if not line: continue
        r=json.loads(line)
        aid=r.get("anon_id") or r.get("id")
        cid=rev.get(aid)
        if cid: jo.setdefault(cid,{})[f]=r
fs=json.load(open(f"{ACC}/judging/final-scores-h24.json"))
out=[]
for cid in sorted(fs["per_case"]):
    pred=json.load(open(f"{ACC}/predictions/{cid}.json"))
    inp=json.load(open(f"{BASE}/holdout24/inputs/{cid}.json"))
    out.append(f"\n===== {cid} ours={fs['per_case'][cid]['ours']} master={fs['per_case'][cid]['master']} diff={fs['per_case'][cid]['diff']} =====")
    out.append("-- INPUT --"); out.append(json.dumps(inp,ensure_ascii=False)[:2500])
    out.append("-- PREDICTION --"); out.append(json.dumps(pred,ensure_ascii=False)[:6000])
    out.append("-- GOLD --"); out.append(json.dumps(gold.get(cid),ensure_ascii=False)[:6000])
    for f in ("judgeO1","judgeO2"):
        r=jo.get(cid,{}).get(f)
        out.append(f"-- {f} --"); out.append(json.dumps(r,ensure_ascii=False)[:2500] if r else "MISSING")
open(f"{ACC}/diag-dump-h24.txt","w").write("\n".join(out))
print("cases:",len(fs["per_case"]),"gold:",len(gold),"jo:",len(jo))
