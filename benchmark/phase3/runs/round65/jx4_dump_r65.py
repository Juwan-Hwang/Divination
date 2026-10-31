import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round65")
rows=[json.loads(l) for l in open(base/"judging/judgeX-block4.jsonl",encoding="utf-8")]
hm=json.load(open(base/"judging/host-mapping.json",encoding="utf-8"))
out=[]
for i,r in enumerate(rows):
    anon=r["anon_id"]; case=hm.get(anon)
    ppath=base/"predictions"/f"{case}.json"
    try:
        pj=json.loads(ppath.read_text(encoding="utf-8"))
        ptext=pj.get("prediction_text") or pj.get("prediction") or str(pj)
        if not isinstance(ptext,str): ptext=json.dumps(ptext,ensure_ascii=False)
    except Exception as e:
        ptext=f"<ERR {e}>"; pj={}
    out.append({"idx":i+1,"anon_id":anon,"case_id":case,"outcome_record":r.get("outcome_record",""),"carry_note":r.get("carry_note"),"editor_note":r.get("editor_note"),"prediction_text":ptext})
pathlib.Path(base/"jx4_view_r65.json").write_text(json.dumps(out,ensure_ascii=False,indent=1),encoding="utf-8")
print(f"wrote {len(out)} cases")
for o in out[:2]:
    print(o["idx"],o["anon_id"],o["case_id"], o["prediction_text"][:300])
