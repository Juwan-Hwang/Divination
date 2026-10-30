import json, pathlib
root = pathlib.Path(__file__).parent
block_path = root / "judging" / "judgeY-block2.jsonl"
mapping = json.loads((root / "judging" / "host-mapping.json").read_text(encoding="utf-8"))
rows = [json.loads(l) for l in block_path.read_text(encoding="utf-8").splitlines() if l.strip()]
out = []
for i, r in enumerate(rows, 1):
    anon = r["anon_id"]
    case = mapping.get(anon, "?")
    pred_path = root / "predictions" / f"{case}.json"
    try:
        pred = json.loads(pred_path.read_text(encoding="utf-8"))
        ptext = pred.get("prediction_text", pred)
        if not isinstance(ptext, str):
            ptext = json.dumps(ptext, ensure_ascii=False)
    except Exception as e:
        ptext = f"[ERR {e}]"
    out.append(f"=== {i} {anon} -> {case} ===\nOUTCOME: {r.get('outcome_record')}\nPREDICTION: {ptext}\n")
print("\n".join(out))
