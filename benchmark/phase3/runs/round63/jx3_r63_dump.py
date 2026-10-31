import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round63")
inp = base/"judging/judgeX-block3.jsonl"
mapping = json.loads((base/"judging/host-mapping.json").read_text())
out = base/"jx3_r63_texts.jsonl"
rows=[]
for line in inp.read_text().splitlines():
    if not line.strip(): continue
    r=json.loads(line)
    anon=r["anon_id"]; case=mapping[anon]
    pred=json.loads((base/"predictions"/f"{case}.json").read_text())
    txt=pred.get("prediction_text","")
    rows.append({"anon_id":anon,"case_id":case,"prediction_text":txt,"outcome_record":r.get("outcome_record","")})
out.write_text("\n".join(json.dumps(x,ensure_ascii=False) for x in rows)+"\n")
print(len(rows))
