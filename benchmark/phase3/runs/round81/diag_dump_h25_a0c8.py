import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
ids=["DS-025","DS-026","DS-027","DS-028","DS-029","DS-030","GSZ-049","GSZ-050","GSZ-052","GSZ-053","GSZ-054","GSZ-055","GSZ-058","GSZ-059","GSZ-060","GSZ-061","GSZ-068","QM-027","QM-028","QM-029","QM-030","QM-031","QM-032","QM-208","QM-209","QM-310","QM-311"]
gold={}
for line in (base/"holdout25/test_gold.jsonl").read_text().splitlines():
    d=json.loads(line); gold[d["id"]]=d
final=json.loads((base/"runs/round81/acceptance/judging/final-scores-h25.json").read_text())
mapping=json.loads((base/"runs/round81/acceptance/judging/host-mapping.json").read_text())
print("MAPPING", mapping)
def load_jsonl(p):
    out={}
    for line in pathlib.Path(p).read_text().splitlines():
        if line.strip():
            d=json.loads(line); out[d["anon_id"]]=d
    return out
# mapping structure unknown, print above; attempt resolve
# packet ours/master map anon-> outcome ; judges keyed by anon
jo1=load_jsonl(base/"runs/round81/acceptance/judging/judgeO1.jsonl")
jo2=load_jsonl(base/"runs/round81/acceptance/judging/judgeO2.jsonl")
jm1=load_jsonl(base/"runs/round81/acceptance/judging/judgeM1.jsonl")
jm2=load_jsonl(base/"runs/round81/acceptance/judging/judgeM2.jsonl")
# Build anon->real via mapping if dict
print(json.dumps(mapping, ensure_ascii=False, indent=1)[:6000])
out=[]
for cid in ids:
    pred=json.loads((base/f"runs/round81/acceptance/predictions/{cid}.json").read_text())
    inp=json.loads((base/f"holdout25/inputs/{cid}.json").read_text())
    out.append((cid,pred,inp))
for cid,pred,inp in out:
    print("\n"+"="*100)
    print(cid, "final ours/master/diff", final["per_case"][cid])
    print("PRED:", json.dumps(pred, ensure_ascii=False)[:4000])
    print("INPUT:", json.dumps(inp, ensure_ascii=False)[:2500])
    print("GOLD master:", gold[cid]["master_prediction"])
    print("GOLD outcome:", gold[cid]["outcome_record"])
    print("GOLD grade_note:", gold[cid]["grade_note"][:600])
