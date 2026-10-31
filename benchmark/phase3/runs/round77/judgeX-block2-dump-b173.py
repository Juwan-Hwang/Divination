import json, pathlib, sys
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round77")
mapping = json.loads((base/"judging/host-mapping.json").read_text(encoding="utf-8"))
rows=[]
for line in (base/"judging/judgeX-block2.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        rows.append(json.loads(line))
start=int(sys.argv[1]); end=int(sys.argv[2])
for i,r in enumerate(rows[start:end], start=start):
    cid=mapping[r["anon_id"]]
    pred=json.loads((base/f"predictions/{cid}.json").read_text(encoding="utf-8"))
    pt=pred.get("prediction_text","")
    print(f"=== [{i}] {r['anon_id']} -> {cid} ===")
    print("PRED:", pt)
    print("OUTCOME:", r.get("outcome_record",""))
    print()
print(f"total rows={len(rows)}")
