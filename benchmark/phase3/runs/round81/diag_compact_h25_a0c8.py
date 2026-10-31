import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
ids=["DS-025","DS-026","DS-027","DS-028","DS-029","DS-030","GSZ-049","GSZ-050","GSZ-052","GSZ-053","GSZ-054","GSZ-055","GSZ-058","GSZ-059","GSZ-060","GSZ-061","GSZ-068","QM-027","QM-028","QM-029","QM-030","QM-031","QM-032","QM-208","QM-209","QM-310","QM-311"]
gold={}
for line in (base/"holdout25/test_gold.jsonl").read_text().splitlines():
    d=json.loads(line); gold[d["id"]]=d
final=json.loads((base/"runs/round81/acceptance/judging/final-scores-h25.json").read_text())
mapping=json.loads((base/"runs/round81/acceptance/judging/host-mapping.json").read_text())
rev_o={v:k for k,v in mapping["ours"].items()}
def load(p):
    out={}
    for line in pathlib.Path(p).read_text().splitlines():
        if line.strip():
            d=json.loads(line); out[d["anon_id"]]=d
    return out
jo1=load(base/"runs/round81/acceptance/judging/judgeO1.jsonl")
jo2=load(base/"runs/round81/acceptance/judging/judgeO2.jsonl")
lines=[]
for cid in ids:
    pred=json.loads((base/f"runs/round81/acceptance/predictions/{cid}.json").read_text())
    inp=json.loads((base/f"holdout25/inputs/{cid}.json").read_text())
    anon=rev_o[cid]
    j1=jo1.get(anon,{}); j2=jo2.get(anon,{})
    lines.append(f"### {cid} ours={final['per_case'][cid]['ours']} master={final['per_case'][cid]['master']} diff={final['per_case'][cid]['diff']}")
    lines.append(f"Q: {inp.get('question','')} | anchors: {json.dumps(inp.get('anchors',{}),ensure_ascii=False)[:700]}")
    lines.append(f"PRED: {pred.get('prediction_text','')}")
    lines.append(f"BASIS_HEAD: {pred.get('basis','')[:900]}")
    lines.append(f"MASTER: {gold[cid]['master_prediction']}")
    lines.append(f"OUTCOME: {gold[cid]['outcome_record']}")
    lines.append(f"O1 dir={j1.get('direction')} claims={j1.get('claims')} timing={j1.get('timing')} total={j1.get('total')} reason={j1.get('reason','')}")
    lines.append(f"O2 dir={j2.get('direction')} claims={j2.get('claims')} timing={j2.get('timing')} total={j2.get('total')} reason={j2.get('reason','')}")
    lines.append("")
pathlib.Path(base/"runs/round81/diag_compact_h25_a0c8.txt").write_text("\n".join(lines))
print(len("\n".join(lines)))
