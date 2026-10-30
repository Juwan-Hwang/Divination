import json, pathlib, sys
base = pathlib.Path(__file__).parent
rows = [json.loads(l) for l in (base/"judgeY-block1.jsonl").read_text().splitlines() if l.strip()]
mp = json.loads((base/"host-mapping.json").read_text())
pred_dir = base.parent/"predictions"
start = int(sys.argv[1]); end = int(sys.argv[2])
for i, r in enumerate(rows[start:end], start=start):
    cid = mp[r["anon_id"]]
    p = json.loads((pred_dir/f"{cid}.json").read_text())
    pt = p.get("prediction_text","")
    print(f"=== {i} {r['anon_id']} {cid} ===")
    print("PRED:", pt)
    print("OUTCOME:", r["outcome_record"])
