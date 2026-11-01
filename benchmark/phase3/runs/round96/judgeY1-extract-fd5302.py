import json, pathlib
base=pathlib.Path("benchmark/phase3/runs/round96")
# cwd is ~ ; adjust
import os
root=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round96")
mapping=json.loads((root/"judging/host-mapping.json").read_text())
rows=[]
for line in (root/"judging/judgeY-block1.jsonl").read_text().splitlines():
    if line.strip():
        rows.append(json.loads(line))
out=[]
for i,r in enumerate(rows,1):
    anon=r["anon_id"]; case=mapping[anon]
    pred=json.loads((root/"predictions"/f"{case}.json").read_text())
    pt=pred.get("prediction_text","")
    out.append(f"=== #{i} {anon} -> {case}\nOUTCOME: {r['outcome_record']}\nPRED: {pt}\n")
(root/"judgeY1-combined-fd5302.txt").write_text("\n".join(out))
print(len(rows), sum(len(x) for x in out))
