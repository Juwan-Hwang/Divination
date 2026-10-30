import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round58")
mapping = json.loads((base/"judging/host-mapping.json").read_text())
rows = [json.loads(l) for l in (base/"judging/judgeX-block3.jsonl").read_text().splitlines() if l.strip()]
out=[]
for i,r in enumerate(rows):
    anon=r["anon_id"]
    cid=mapping.get(anon)
    pred=""
    if cid:
        p=json.loads((base/"predictions"/f"{cid}.json").read_text())
        pred=p.get("prediction_text","")
    out.append(f"=== {i} {anon} case={cid} ===\nSUMMARY: {json.dumps(r,ensure_ascii=False)}\nFULL_PREDICTION:\n{pred}\n")
(base/"dump-judgeX-block3-a235.txt").write_text("\n".join(out))
print(len(rows))
