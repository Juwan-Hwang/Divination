import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round66")
block = [json.loads(l) for l in open(base/"judging/judgeY-block1.jsonl", encoding="utf-8")]
mapping = json.load(open(base/"judging/host-mapping.json", encoding="utf-8"))
print("block count", len(block))
for i, row in enumerate(block):
    anon = row["anon_id"]
    cid = mapping[anon]
    pred = json.load(open(base/"predictions"/f"{cid}.json", encoding="utf-8"))
    if i == 0:
        print("pred keys:", list(pred.keys()))
    pt = pred.get("prediction_text", "")
    print(f"\n===== #{i+1} {anon} -> {cid} =====")
    print("PREDICTION_TEXT:", pt)
    print("OUTCOME:", row.get("outcome_record",""))
    for k in ("carry_note","editor_note"):
        if k in row:
            print(k.upper()+":", row[k][:300])
