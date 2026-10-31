import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
A=base/"runs/round83/acceptance"
ids=["DS-040","DS-041","DS-042","DS-043","DS-044","DS-045","DS-046","DS-048","DS-049","GSZ-079","GSZ-081","GSZ-084","GSZ-086","GSZ-088","QM-044","QM-045","QM-046","QM-047","QM-048","QM-049","QM-052","QM-055","QM-058","WHY-008","WHY-009","WHY-010","WHY-011"]
gold={}
for line in (base/"holdout27/test_gold.jsonl").read_text().splitlines():
    d=json.loads(line); gold[d["id"]]=d
final=json.loads((A/"judging/final-scores-h27.json").read_text())
assert set(ids)==set(final["per_case"]), "id set mismatch vs final-scores"
assert set(ids)==set(gold), "id set mismatch vs gold"
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
    inp=json.loads((base/f"holdout27/inputs/{cid}.json").read_text())
    ao=rev_o[cid]; am=rev_m[cid]
    j1=jo1.get(ao,{}); j2=jo2.get(ao,{}); m1=jm1.get(am,{}); m2=jm2.get(am,{})
    assert float(j1.get("total",-1))>=0 and float(m1.get("total",-1))>=0, cid
    lines.append(f"### {cid} ours={final['per_case'][cid]['ours']} master={final['per_case'][cid]['master']} diff={final['per_case'][cid]['diff']}")
    lines.append(f"SUBJ: {inp.get('subject','')} | Q: {inp.get('question','')} | CTX: {inp.get('context','')[:400]}")
    lines.append(f"ANCH: {json.dumps(inp.get('anchors',{}),ensure_ascii=False)[:1200]}")
    lines.append(f"PRED: {pred.get('prediction_text','')}")
    lines.append(f"BASIS: {pred.get('basis','')}")
    lines.append(f"TRIGGER: {pred.get('trigger','')}")
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
dest=base/"runs/round83/diag_compact_h27_r83.txt"
dest.write_text(out)
print("bytes", len(out.encode()), "lines", out.count("\n"), "cases", out.count("### "))
