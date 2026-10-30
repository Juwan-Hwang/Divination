import json, sys
base = "/home/hatch/workspace/divination/benchmark/phase3/runs/round54"
with open(base+"/judging/judgeX-block2.jsonl", encoding="utf-8") as f:
    rows=[json.loads(l) for l in f if l.strip()]
with open(base+"/judging/host-mapping.json", encoding="utf-8") as f:
    mp=json.load(f)
start=int(sys.argv[1]); end=int(sys.argv[2])
for i,row in enumerate(rows[start:end], start=start+1):
    anon=row["anon_id"]; case=mp[anon]
    with open(f"{base}/predictions/{case}.json", encoding="utf-8") as pf:
        pred=json.load(pf)
    print(f"=== {i} {anon} {case}")
    print("OUTCOME:", row["outcome_record"])
    print("PRED:", pred.get("prediction_text",""))
    print()
