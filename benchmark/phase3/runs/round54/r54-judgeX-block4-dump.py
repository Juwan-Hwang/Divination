import json, pathlib
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3/runs/round54"
block_path = base / "judging/judgeX-block4.jsonl"
map_path = base / "judging/host-mapping.json"
with open(map_path, encoding="utf-8") as f:
    mapping = json.load(f)
rows=[]
with open(block_path, encoding="utf-8") as f:
    for line in f:
        line=line.strip()
        if line:
            rows.append(json.loads(line))
out_path = base / "r54-judgeX-block4-preddump.txt"
with open(out_path, "w", encoding="utf-8") as out:
    out.write(f"count={len(rows)}\n")
    for r in rows:
        anon=r["anon_id"]
        case=mapping.get(anon, "?MISSING?")
        out.write(f"\n===== {anon} -> {case} =====\n")
        out.write(f"OUTCOME: {r.get('outcome_record','')}\n")
        pred_path = base / "predictions" / f"{case}.json"
        try:
            with open(pred_path, encoding="utf-8") as pf:
                pj=json.load(pf)
            # dump full json keys for inspection
            out.write(f"PRED_KEYS: {list(pj.keys())}\n")
            pt = pj.get("prediction_text","")
            out.write(f"PREDICTION_TEXT:\n{pt}\n")
            # also dump other fields if present
            for k,v in pj.items():
                if k!="prediction_text":
                    out.write(f"FIELD {k}: {v}\n")
        except Exception as e:
            out.write(f"ERROR reading {pred_path}: {e}\n")
print(f"wrote {out_path} rows={len(rows)}")
