import json
BASE="/home/hatch/workspace/divination/benchmark/phase3"
ACC=f"{BASE}/runs/round80/acceptance"
gold={}
for line in open(f"{BASE}/holdout24/test_gold.jsonl"):
    if line.strip():
        g=json.loads(line); gold[g["id"]]=g
hm=json.load(open(f"{ACC}/judging/host-mapping.json")); rev=hm["ours"]
jo={}
for f in ("judgeO1","judgeO2"):
    for line in open(f"{ACC}/judging/{f}.jsonl"):
        if line.strip():
            r=json.loads(line); jo.setdefault(rev[r["anon_id"]],{})[f]=r
fs=json.load(open(f"{ACC}/judging/final-scores-h24.json"))
out=[]
for cid in sorted(fs["per_case"]):
    pred=json.load(open(f"{ACC}/predictions/{cid}.json"))
    inp=json.load(open(f"{BASE}/holdout24/inputs/{cid}.json"))
    g=gold[cid]
    pc=fs["per_case"][cid]
    out.append(f"\n===== {cid} ours={pc['ours']} master={pc['master']} diff={pc['diff']} =====")
    out.append("ANCHORS: "+json.dumps(inp.get("anchors"),ensure_ascii=False)[:700])
    out.append("PRED: "+pred.get("prediction_text","")[:2200])
    out.append("MASTER: "+g.get("master_prediction",""))
    out.append("OUTCOME: "+g.get("outcome_record",""))
    gn=g.get("grade_note","")
    out.append("GRADE_NOTE_ANCHOR: "+("present" if "present" in gn else gn[:200]))
    for f in ("judgeO1","judgeO2"):
        r=jo[cid][f]
        out.append(f"{f} d={r['direction']} c={r['claims']} t={r['timing']} tot={r['total']}: {r['reason']}")
open(f"{ACC}/diag-compact-h24.txt","w").write("\n".join(out))
print("ok")
