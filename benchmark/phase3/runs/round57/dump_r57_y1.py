import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round57")
judging = base/"judging"
rows = [json.loads(l) for l in open(judging/"judgeY-block1.jsonl", encoding="utf-8") if l.strip()]
mapping = json.load(open(judging/"host-mapping.json", encoding="utf-8"))
out=[]
for r in rows:
    anon=r["anon_id"]
    cid=mapping.get(anon)
    pred_path = base/"predictions"/f"{cid}.json"
    ptxt=""
    extra=""
    if pred_path.exists():
        pj=json.load(open(pred_path, encoding="utf-8"))
        ptxt=pj.get("prediction_text","")
        # capture other keys for context
        extra={k:v for k,v in pj.items() if k!="prediction_text"}
    else:
        ptxt=f"[MISSING {cid}]"
    out.append({"anon_id":anon,"case_id":cid,"outcome_record":r.get("outcome_record"),"carry_note":r.get("carry_note"),"editor_note":r.get("editor_note"),"prediction_text":ptxt,"pred_extra":extra})
with open(base/"dump_r57_y1.json","w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False,indent=1)
print(len(out))
for o in out:
    print(o["anon_id"], o["case_id"], "carry" if o["carry_note"] else "", "editor" if o["editor_note"] else "", len(o["prediction_text"] or ""))
