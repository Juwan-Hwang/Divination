import json, pathlib
base=pathlib.Path(__file__).parent
rows=[json.loads(l) for l in open(base/"judgeX-block2.jsonl",encoding="utf-8") if l.strip()]
mp=json.load(open(base/"host-mapping.json",encoding="utf-8"))
out=[]
for r in rows:
    cid=mp[r["anon_id"]]
    p=json.load(open(base.parent/"predictions"/f"{cid}.json",encoding="utf-8"))
    out.append({"anon_id":r["anon_id"],"case_id":cid,"outcome":r["outcome_record"],"prediction_text":p.get("prediction_text")})
print(json.dumps(out,ensure_ascii=False,indent=1))
