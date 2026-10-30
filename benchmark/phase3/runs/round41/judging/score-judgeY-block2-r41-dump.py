import json
base = "/home/hatch/workspace/divination/benchmark/phase3/runs/round41"
with open(f"{base}/judging/judgeY-block2.jsonl") as f:
    rows=[json.loads(l) for l in f if l.strip()]
with open(f"{base}/judging/host-mapping.json") as f:
    mp=json.load(f)
for r in rows:
    cid=mp[r["anon_id"]]
    with open(f"{base}/predictions/{cid}.json") as f:
        p=json.load(f)
    print("="*80)
    print(r["anon_id"], cid)
    print("OUTCOME:", r["outcome_record"])
    print("PRED:", p.get("prediction_text"))
