import json, sys, pathlib
base = pathlib.Path(__file__).resolve().parent
root = base.parent.parent.parent.parent  # divination? let's compute: judging->round41->runs->phase3->benchmark->divination
# Actually predictions are in benchmark/phase3/runs/round41/predictions
pred_dir = base.parent / "predictions"
inp = base / "judgeX-block1.jsonl"
mapping = json.loads((base / "host-mapping.json").read_text(encoding="utf-8"))
rows = [json.loads(l) for l in inp.read_text(encoding="utf-8").splitlines() if l.strip()]
start = int(sys.argv[1]) if len(sys.argv)>1 else 0
end = int(sys.argv[2]) if len(sys.argv)>2 else len(rows)
for i, r in enumerate(rows[start:end], start=start):
    anon = r["anon_id"]
    case = mapping.get(anon)
    pfile = pred_dir / f"{case}.json"
    try:
        pj = json.loads(pfile.read_text(encoding="utf-8"))
        ptext = pj.get("prediction_text") or pj.get("prediction") or str(pj)
    except Exception as e:
        ptext = f"<ERR {e}>"
    print(f"\n=== {i} {anon} case={case} ===")
    print("OUTCOME:", r.get("outcome_record"))
    print("PREDICTION_TEXT:", ptext)
