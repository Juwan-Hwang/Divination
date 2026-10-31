import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
r90=base/"runs/round90/acceptance"
final=json.loads((r90/"judging/final-scores-h32.json").read_text())
ids=list(final["per_case"].keys())
gold={}
for line in (base/"holdout32/test_gold.jsonl").read_text().splitlines():
    g=json.loads(line); gold[g["id"]]=g
preds={cid: json.loads((r90/f"predictions/{cid}.json").read_text()) for cid in ids}
# map anon via packet-ours prediction_text exact match
packet=json.loads((r90/"judging/packet-ours.json").read_text())
anon2case={}
for e in packet:
    for cid,p in preds.items():
        if p["prediction_text"]==e["prediction_text"]:
            anon2case[e["anon_id"]]=cid
print("mapped ours packet", len(anon2case))
packetM=json.loads((r90/"judging/packet-master.json").read_text())
anon2caseM={}
for e in packetM:
    for cid,g in gold.items():
        if g["master_prediction"]==e["prediction_text"]:
            anon2caseM[e["anon_id"]]=cid
print("mapped master packet", len(anon2caseM))
def load_j(name, mapping):
    d={}
    for line in (r90/f"judging/{name}").read_text().splitlines():
        if line.strip():
            j=json.loads(line); cid=mapping.get(j["anon_id"]); 
            if cid: d[cid]=j
    return d
O1=load_j("judgeO1.jsonl", anon2case); O2=load_j("judgeO2.jsonl", anon2case)
M1=load_j("judgeM1.jsonl", anon2caseM); M2=load_j("judgeM2.jsonl", anon2caseM)
print("judge counts", len(O1), len(O2), len(M1), len(M2))
# verify totals vs final
bad=[]
for cid in ids:
    o=(O1[cid]["total"]+O2[cid]["total"])/2; m=(M1[cid]["total"]+M2[cid]["total"])/2
    if abs(o-final["per_case"][cid]["ours"])>0.26 or abs(m-final["per_case"][cid]["master"])>0.26:
        bad.append((cid,o,final["per_case"][cid]["ours"],m,final["per_case"][cid]["master"]))
print("mismatches", bad)
out=[]
for cid in ids:
    pred=preds[cid]
    inp=""
    idir=base/"holdout32/inputs"
    for p in idir.iterdir():
        if p.stem==cid: inp=p.read_text(); break
    out.append(f"\n===== {cid} ours={final['per_case'][cid]['ours']} master={final['per_case'][cid]['master']} diff={final['per_case'][cid]['diff']} =====\nPRED: {pred.get('prediction_text')}\nBASIS: {pred.get('basis')}\nTRIGGER: {json.dumps(pred.get('trigger'),ensure_ascii=False)}\nO1: {json.dumps(O1.get(cid),ensure_ascii=False)}\nO2: {json.dumps(O2.get(cid),ensure_ascii=False)}\nM1: {json.dumps(M1.get(cid),ensure_ascii=False)}\nM2: {json.dumps(M2.get(cid),ensure_ascii=False)}\nGOLD_MASTER: {gold[cid].get('master_prediction')}\nGOLD_OUTCOME: {gold[cid].get('outcome_record')}\nGRADE {gold[cid].get('grade')} NOTE {gold[cid].get('grade_note')}\nINPUT: {inp}\n")
(r90/"diag_compact_h32_r90.txt").write_text("\n".join(out))
for cid in ids:
    b=preds[cid].get('basis','')
    s8=[k for k in ["第八节","R80-REV1","R80","功量核算","做功主线","功量"] if k in b]
    s12=[k for k in ["第十二节","R87-REV1","R87","坐标对位","对位纪律","落点对位"] if k in b]
    t=preds[cid]['trigger']
    print(cid, "S8:", s8, "| S12:", s12, "| trig:", t['changed_main'], t['reserve_used'], t['disputed'], "| reason:", t.get('reason','')[:60])
