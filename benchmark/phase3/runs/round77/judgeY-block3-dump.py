import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round77")
mapping=json.loads((base/"judging/host-mapping.json").read_text())
rows=[json.loads(l) for l in (base/"judging/judgeY-block3.jsonl").read_text().splitlines() if l.strip()]
rows.sort(key=lambda r:r["anon_id"])
for idx,row in enumerate(rows):
    cid=mapping[row["anon_id"]]
    pred=json.loads((base/f"predictions/{cid}.json").read_text())
    ptext=pred.get("prediction_text") or pred.get("prediction") or str(pred)
    if not isinstance(ptext,str): ptext=json.dumps(ptext,ensure_ascii=False)
    chunk=idx//20
    out=base/f"judgeY-block3-chunk{chunk}.txt"
    with out.open("a",encoding="utf-8") as f:
        f.write(f"\n=== {idx} {row['anon_id']} -> {cid} ===\nPRED: {ptext}\nOUTCOME: {row.get('outcome_record','')}\n")
print(len(rows))
