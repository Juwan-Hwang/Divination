import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round77")
mapping = json.loads((base/"judging/host-mapping.json").read_text())
rows = [json.loads(l) for l in (base/"judging/judgeY-block2.jsonl").read_text().splitlines() if l.strip()]
out=[]
for r in rows:
    anon=r["anon_id"]; case=mapping[anon]
    pred=json.loads((base/"predictions"/f"{case}.json").read_text())
    pt = pred.get("prediction_text") or pred.get("prediction") or ""
    if not isinstance(pt,str): pt=json.dumps(pt,ensure_ascii=False)
    out.append(f"===== {anon} | {case} =====\nPRED: {pt}\nOUTCOME: {r.get('outcome_record','')}\n")
(base/"judgeY-block2-combined.txt").write_text("\n".join(out))
print(len(rows), sum(len(x) for x in out))
