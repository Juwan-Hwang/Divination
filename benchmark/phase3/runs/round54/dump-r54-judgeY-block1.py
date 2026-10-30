import json, sys
base="benchmark/phase3/runs/round54"
mapping=json.load(open(f"{base}/judging/host-mapping.json"))
rows=[json.loads(l) for l in open(f"{base}/judging/judgeY-block1.jsonl") if l.strip()]
start=int(sys.argv[1]); end=int(sys.argv[2])
for i,r in enumerate(rows[start:end], start=start):
    cid=mapping[r["anon_id"]]
    pred=json.load(open(f"{base}/predictions/{cid}.json"))
    print(f"=== {i} {r['anon_id']} {cid}")
    print("OUTCOME:", r["outcome_record"])
    print("PRED:", pred.get("prediction_text"))
