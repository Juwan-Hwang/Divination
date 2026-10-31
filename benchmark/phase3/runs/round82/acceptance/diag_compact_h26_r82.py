import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
A=base/"runs/round82/acceptance"
ids=["DS-031","DS-032","DS-033","DS-034","DS-035","DS-036","DS-037","DS-038","DS-039","GSZ-069","GSZ-074","GSZ-075","GSZ-077","GSZ-078","QM-034","QM-035","QM-036","QM-037","QM-038","QM-039","QM-040","QM-042","QM-043","WHY-004","WHY-005","WHY-006","WHY-007"]
gold={}
for line in (base/"holdout26/test_gold.jsonl").read_text().splitlines():
    d=json.loads(line); gold[d["id"]]=d
final=json.loads((A/"judging/final-scores-h26.json").read_text())
mapping=json.loads((A/"judging/host-mapping.json").read_text())
rev_o={v:k for k,v in mapping["ours"].items()}
rev_m={v:k for k,v in mapping["master"].items()}
def load(p):
    out={}
    for line in pathlib.Path(p).read_text().splitlines():
        if line.strip():
            d=json.loads(line); out[d["anon_id"]]=d
    return out
jo1=load(A/"judging/judgeO1.jsonl"); jo2=load(A/"judging/judgeO2.jsonl")
jm1=load(A/"judging/judgeM1.jsonl"); jm2=load(A/"judging/judgeM2.jsonl")
lines=[]
for cid in ids:
    pred=json.loads((A/f"predictions/{cid}.json").read_text())
    inp=json.loads((base/f"holdout26/inputs/{cid}.json").read_text())
    ao=rev_o[cid]; am=rev_m[cid]
    j1=jo1.get(ao,{}); j2=jo2.get(ao,{}); m1=jm1.get(am,{}); m2=jm2.get(am,{})
    lines.append(f"### {cid} ours={final['per_case'][cid]['ours']} master={final['per_case'][cid]['master']} diff={final['per_case'][cid]['diff']}")
    lines.append(f"SUBJ: {inp.get('subject','')} | Q: {inp.get('question','')} | CTX: {inp.get('context','')[:300]}")
    lines.append(f"ANCH: {json.dumps(inp.get('anchors',{}),ensure_ascii=False)[:900]}")
    lines.append(f"PRED: {pred.get('prediction_text','')}")
    lines.append(f"BASIS: {pred.get('basis','')}")
    lines.append(f"MASTER: {gold[cid]['master_prediction']}")
    lines.append(f"OUTCOME: {gold[cid]['outcome_record']}")
    lines.append(f"GN: {gold[cid].get('grade_note','')}")
    if gold[cid].get('editor_note'): lines.append(f"EN: {gold[cid]['editor_note']}")
    lines.append(f"O1 d={j1.get('direction')} c={j1.get('claims')} t={j1.get('timing')} tot={j1.get('total')} :: {j1.get('reason','')}")
    lines.append(f"O2 d={j2.get('direction')} c={j2.get('claims')} t={j2.get('timing')} tot={j2.get('total')} :: {j2.get('reason','')}")
    lines.append(f"M1 d={m1.get('direction')} c={m1.get('claims')} t={m1.get('timing')} tot={m1.get('total')} :: {m1.get('reason','')}")
    lines.append(f"M2 d={m2.get('direction')} c={m2.get('claims')} t={m2.get('timing')} tot={m2.get('total')} :: {m2.get('reason','')}")
    lines.append("")
out="\n".join(lines)
(A/"diag_compact_h26_r82.txt").write_text(out)
print(len(out), out.count("\n"))
