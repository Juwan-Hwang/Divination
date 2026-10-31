import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round77")
mapping = json.loads((base/"judging/host-mapping.json").read_text())
rows = [json.loads(l) for l in (base/"judging/judgeX-block4.jsonl").read_text().splitlines() if l.strip()]
out=[]
for i,r in enumerate(rows,1):
    anon=r["anon_id"]; cid=mapping[anon]
    pred=json.loads((base/"predictions"/f"{cid}.json").read_text())
    ptext = pred.get("prediction_text") or pred.get("prediction") or json.dumps(pred, ensure_ascii=False)
    if isinstance(ptext, dict): ptext=json.dumps(ptext, ensure_ascii=False)
    out.append(f"=== {i} {anon} {cid} ===\nPRED: {ptext}\nOUTCOME: {r.get('outcome_record','')}\n")
(base/"judging/judgeX-block4-merged.txt").write_text("\n".join(out))
print(len(rows), "merged bytes", (base/"judging/judgeX-block4-merged.txt").stat().st_size)
# also show pred file keys sample
import collections
print(rows[0].keys())
