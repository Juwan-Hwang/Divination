import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round65")
block=base/"judging/judgeX-block2.jsonl"
mapping=json.loads((base/"judging/host-mapping.json").read_text())
out=[]
for line in block.read_text().splitlines():
    if not line.strip(): continue
    r=json.loads(line)
    anon=r["anon_id"]; case=mapping[anon]
    pred=json.loads((base/f"predictions/{case}.json").read_text())
    # find prediction_text field recursively?
    pt=pred.get("prediction_text") or pred.get("prediction") or ""
    if isinstance(pt, dict): pt=json.dumps(pt,ensure_ascii=False)
    out.append(f"=== {anon} | {case} ===\nOUTCOME: {r['outcome_record']}\nPREDICTION_TEXT:\n{pt}\n---FULLKEYS: {list(pred.keys())}\n")
    if not pred.get("prediction_text"):
        out.append(json.dumps(pred,ensure_ascii=False)[:4000]+"\n")
(base/"jx2_dump_r65.txt").write_text("\n".join(out))
print(len(out))
