import json, pathlib
base = pathlib.Path(__file__).parent
block = [json.loads(l) for l in open(base/"judging/judgeY-block3.jsonl", encoding="utf-8") if l.strip()]
mapping = json.load(open(base/"judging/host-mapping.json", encoding="utf-8"))
print(f"COUNT {len(block)}")
for row in block:
    anon=row["anon_id"]; cid=mapping[anon]
    pred=json.load(open(base/"predictions"/f"{cid}.json", encoding="utf-8"))
    txt=pred.get("prediction_text","")
    print(f"\n=== {anon} | {cid} ===")
    print("OUTCOME:", row["outcome_record"])
    print("PREDICTION:", txt)
