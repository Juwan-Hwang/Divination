import json, pathlib
base=pathlib.Path(__file__).parent
judge=base/"judging"/"judgeY-block1.jsonl"
mapping=json.loads((base/"judging"/"host-mapping.json").read_text())
rows=[json.loads(l) for l in judge.read_text().splitlines() if l.strip()]
print(f"COUNT {len(rows)}")
for r in rows:
    anon=r["anon_id"]; case=mapping[anon]
    pred=json.loads((base/"predictions"/f"{case}.json").read_text())
    txt=pred.get("prediction_text","")
    print(f"\n=== {anon} -> {case} ===")
    print(f"OUTCOME: {r['outcome_record']}")
    print(f"PREDICTION: {txt}")
