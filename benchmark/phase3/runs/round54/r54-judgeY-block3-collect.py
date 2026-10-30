import json, pathlib
base = pathlib.Path(__file__).parent
block = base/"judging"/"judgeY-block3.jsonl"
mapping = json.loads((base/"judging"/"host-mapping.json").read_text(encoding="utf-8"))
out_lines=[]
rows=[json.loads(l) for l in block.read_text(encoding="utf-8").splitlines() if l.strip()]
print(f"rows={len(rows)}")
for i,r in enumerate(rows,1):
    anon=r["anon_id"]; case=mapping.get(anon,"?MISSING?")
    pfile=base/"predictions"/f"{case}.json"
    try:
        pj=json.loads(pfile.read_text(encoding="utf-8"))
        pt=pj.get("prediction_text") or json.dumps(pj,ensure_ascii=False)
    except Exception as e:
        pt=f"!!READ_ERR {e}"
    out_lines.append(f"=== {i} {anon} -> {case} ===")
    out_lines.append(f"OUTCOME: {r.get('outcome_record')}")
    out_lines.append(f"PRED: {pt}")
    out_lines.append("")
(base/"r54-judgeY-block3-preds.txt").write_text("\n".join(out_lines),encoding="utf-8")
print("written")
