import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round63")
block=[json.loads(l) for l in open(base/"judging/judgeX-block4.jsonl",encoding="utf-8") if l.strip()]
mp=json.load(open(base/"judging/host-mapping.json",encoding="utf-8"))
out=[]
for r in block:
    anon=r["anon_id"]; cid=mp[anon]
    p=json.load(open(base/f"predictions/{cid}.json",encoding="utf-8"))
    pt=p.get("prediction_text") or p.get("prediction") or ""
    if isinstance(pt,dict): pt=json.dumps(pt,ensure_ascii=False)
    out.append({"anon":anon,"case":cid,"prediction_text":pt,"outcome":r["outcome_record"],"carry":r.get("carry_note"),"editor":r.get("editor_note")})
with open(base/"jx4_r63_texts.json","w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=1)
print(len(out))
for o in out:
    print("="*80)
    print(o["anon"], o["case"])
    print("PRED:", o["prediction_text"][:3000])
    print("OUT:", o["outcome"][:800])
