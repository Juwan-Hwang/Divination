import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round81")
mapping = json.loads((base/"judging/host-mapping.json").read_text(encoding="utf-8"))
rows=[]
for line in (base/"judging/judgeY-block3.jsonl").read_text(encoding="utf-8").splitlines():
    if not line.strip(): continue
    r=json.loads(line)
    anon=r["anon_id"]; case=mapping[anon]
    pred=json.loads((base/"predictions"/f"{case}.json").read_text(encoding="utf-8"))
    rows.append({"n":len(rows)+1,"anon_id":anon,"case_id":case,"prediction_text":pred.get("prediction_text",""),"outcome_record":r.get("outcome_record","")})
with open(base/"judging/judgeY-b3-compact-81.jsonl","w",encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r,ensure_ascii=False)+"\n")
print(len(rows))
