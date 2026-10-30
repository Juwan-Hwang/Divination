import json, pathlib
base = pathlib.Path(__file__).resolve().parent
root = base.parent.parent  # runs/round41? check: judging is runs/round41/judging, parent=round41
# Actually base.parent is round41
round_dir = base.parent
inp = base / "judgeX-block3.jsonl"
rows = [json.loads(l) for l in inp.read_text(encoding="utf-8").splitlines() if l.strip()]
mapping = json.loads((base / "host-mapping.json").read_text(encoding="utf-8"))
start = int(__import__("sys").argv[1]) if len(__import__("sys").argv)>1 else 0
end = int(__import__("sys").argv[2]) if len(__import__("sys").argv)>2 else len(rows)
for i, r in enumerate(rows[start:end], start=start):
    cid = mapping[r["anon_id"]]
    pred = json.loads((round_dir / "predictions" / f"{cid}.json").read_text(encoding="utf-8"))
    txt = pred.get("prediction_text","")
    print(f"=== {i} {r['anon_id']} {cid} ===")
    print("OUTCOME:", r["outcome_record"])
    print("PRED:", txt)
    print()
