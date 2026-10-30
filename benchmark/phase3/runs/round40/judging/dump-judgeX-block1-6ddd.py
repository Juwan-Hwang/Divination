import json, pathlib
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3/runs/round40"
packet = json.loads((base/"judging/packet1.json").read_text(encoding="utf-8"))
mapping = json.loads((base/"judging/host-mapping.json").read_text(encoding="utf-8"))
out = []
for i, row in enumerate(packet, 1):
    anon = row["anon_id"]
    case = mapping[anon]
    pred = json.loads((base/"predictions"/f"{case}.json").read_text(encoding="utf-8"))
    text = pred.get("prediction_text") or json.dumps(pred, ensure_ascii=False)
    out.append(f"=== {i} {anon} -> {case} ===\n[PREDICTION]\n{text}\n[OUTCOME]\n{row['outcome_record']}\n")
path = base/"judging/review-judgeX-block1-6ddd.txt"
path.write_text("\n".join(out), encoding="utf-8")
print(len(packet), path)
