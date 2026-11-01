import json, pathlib, sys
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round94")
rows=[json.loads(l) for l in (base/"judging/judgeX-block4.jsonl").read_text().splitlines() if l.strip()]
mapping=json.loads((base/"judging/host-mapping.json").read_text())
start=int(sys.argv[1]); end=int(sys.argv[2])
for i,r in enumerate(rows[start:end], start=start+1):
    anon=r["anon_id"]; case=mapping[anon]
    p=json.loads((base/f"predictions/{case}.json").read_text())
    txt=p.get("prediction_text")
    print(f"\n=== {i} {anon} {case} ===")
    print("OUTCOME:", r.get("outcome_record"))
    print("PRED:", txt)
