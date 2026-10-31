import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round82")
inp = [json.loads(l) for l in open(base/"judging/judgeX-block3.jsonl", encoding="utf-8")]
mapping = json.load(open(base/"judging/host-mapping.json", encoding="utf-8"))
out = open(base/"judging/judgeX3_r82_combined.txt","w",encoding="utf-8")
for i,row in enumerate(inp):
    anon=row["anon_id"]; case=mapping[anon]
    pred=json.load(open(base/"predictions"/f"{case}.json", encoding="utf-8"))
    out.write(f"\n===== {i+1} anon={anon} case={case} =====\n")
    out.write("OUTCOME: "+row.get("outcome_record","")+"\n")
    if row.get("carry_note"): out.write("CARRY: "+row["carry_note"][:300]+"\n")
    out.write("PREDICTION_TEXT:\n"+str(pred.get("prediction_text",""))+"\n")
    # also dump other keys for inspection
    for k,v in pred.items():
        if k!="prediction_text":
            out.write(f"[{k}] {v}\n")
out.close()
print("done", len(inp))
