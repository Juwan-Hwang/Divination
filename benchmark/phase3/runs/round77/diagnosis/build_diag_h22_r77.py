import json, math, os
BASE="/home/hatch/workspace/divination/benchmark/phase3"
DIAG=f"{BASE}/runs/round77/diagnosis"
IDS=["DS-004","DS-005","DS-006","DS-007","DS-008","DS-009","DS-010","DS-011","DS-012",
"GSZ-022","GSZ-023","GSZ-024","GSZ-026",
"QM-011","QM-012","QM-013","QM-014","QM-201","QM-202","QM-203","QM-301","QM-302","QM-303",
"ZCB-001","ZCB-002","ZCB-004","ZCB-005"]
assert len(IDS)==27
fs=json.load(open(f"{BASE}/runs/round77/acceptance/judging/final-scores.json"))
hm=json.load(open(f"{BASE}/runs/round77/acceptance/judging/host-mapping.json"))
def load_j(fn):
    d={}
    for line in open(f"{BASE}/runs/round77/acceptance/judging/{fn}"):
        line=line.strip()
        if line:
            r=json.loads(line); d[r["anon_id"]]=r
    return d
JO1,JO2,JM1,JM2=[load_j(f) for f in ["judgeO1.jsonl","judgeO2.jsonl","judgeM1.jsonl","judgeM2.jsonl"]]
gold={}
for line in open(f"{BASE}/holdout22/test_gold.jsonl"):
    r=json.loads(line); gold[r["id"]]=r
assert set(gold)==set(IDS)
inv_o={v:k for k,v in hm["ours"].items()}; inv_m={v:k for k,v in hm["master"].items()}
sub={}
for cid in IDS:
    o1,o2=JO1[inv_o[cid]],JO2[inv_o[cid]]; m1,m2=JM1[inv_m[cid]],JM2[inv_m[cid]]
    ours={k:round((o1[k]+o2[k])/2,4) for k in ["direction","claims","timing"]}
    ours["total"]=round(sum(ours.values()),4)
    mast={k:round((m1[k]+m2[k])/2,4) for k in ["direction","claims","timing"]}
    mast["total"]=round(sum(mast.values()),4)
    assert abs(ours["total"]-fs["ours"][cid])<1e-9,(cid,ours,fs["ours"][cid])
    assert abs(mast["total"]-fs["master"][cid])<1e-9,(cid,mast)
    sub[cid]={"ours":ours,"master":mast,"diff":fs["per_case"][cid]["diff"],
              "O_reasons":[o1["reason"],o2["reason"]],"M_reasons":[m1["reason"],m2["reason"]]}
# digest for coding
with open(f"{DIAG}/digest_h22_r77.txt","w") as f:
    for cid in IDS:
        pred=json.load(open(f"{BASE}/runs/round77/acceptance/predictions/{cid}.json"))
        inp=json.load(open(f"{BASE}/holdout22/inputs/{cid}.json"))
        f.write(f"\n===== {cid} =====\n")
        f.write(f"SUB ours dir/claims/tim {sub[cid]['ours']['direction']}/{sub[cid]['ours']['claims']}/{sub[cid]['ours']['timing']} tot {sub[cid]['ours']['total']} | master {sub[cid]['master']['direction']}/{sub[cid]['master']['claims']}/{sub[cid]['master']['timing']} tot {sub[cid]['master']['total']} | diff {sub[cid]['diff']}\n")
        f.write(f"O reasons: {sub[cid]['O_reasons'][0]} || {sub[cid]['O_reasons'][1]}\n")
        f.write(f"M reasons: {sub[cid]['M_reasons'][0]} || {sub[cid]['M_reasons'][1]}\n")
        f.write(f"INPUT subject={inp.get('subject')} question={inp.get('question')} context={inp.get('context')}\n")
        f.write(f"INPUT anchors={json.dumps(inp.get('anchors'),ensure_ascii=False)[:1200]}\n")
        f.write(f"PRED: {pred['prediction_text']}\n")
        f.write(f"BASIS: {pred['basis'][:1500]}\n")
        f.write(f"GOLD master: {gold[cid]['master_prediction']}\n")
        f.write(f"GOLD outcome: {gold[cid]['outcome_record']}\n")
json.dump(sub,open(f"{DIAG}/subscores_h22_r77.json","w"),ensure_ascii=False,indent=1)
print("OK asserts passed; digest bytes",os.path.getsize(f"{DIAG}/digest_h22_r77.txt"))
