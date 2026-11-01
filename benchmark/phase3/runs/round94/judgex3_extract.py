import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round94")
jud=base/"judging"
block=[json.loads(l) for l in (jud/"judgeX-block3.jsonl").read_text(encoding="utf-8").strip().splitlines()]
mp=json.loads((jud/"host-mapping.json").read_text(encoding="utf-8"))
out=[]
missing=[]
for i,row in enumerate(block,1):
    anon=row["anon_id"]
    cid=mp.get(anon)
    ptext=""
    if cid:
        pf=base/"predictions"/f"{cid}.json"
        if pf.exists():
            data=json.loads(pf.read_text(encoding="utf-8"))
            ptext=data.get("prediction_text","") or ""
        else:
            missing.append((anon,cid,"file_missing"))
    else:
        missing.append((anon,None,"no_mapping"))
    if not ptext:
        missing.append((anon,cid,"empty_prediction"))
    out.append({"n":i,"anon_id":anon,"case_id":cid,"outcome_record":row.get("outcome_record",""),"prediction_text":ptext})
pathlib.Path(base/"judgex3_work.json").write_text(json.dumps({"items":out,"missing":missing},ensure_ascii=False,indent=1),encoding="utf-8")
print(f"total {len(out)} missing {missing}")
for it in out[:2]:
    print(it["n"], it["anon_id"], it["case_id"], it["prediction_text"][:500], "|| OUT:", it["outcome_record"][:200])
