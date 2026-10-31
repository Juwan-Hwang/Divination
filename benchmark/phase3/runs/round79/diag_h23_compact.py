import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round79/acceptance")
cases=["DS-013","DS-014","DS-015","DS-016","DS-017","DS-018","GSZ-028","GSZ-030","GSZ-031","GSZ-032","GSZ-033","QM-015","QM-016","QM-018","QM-019","QM-020","QM-204","QM-205","QM-304","QM-305","QM-306","ZCB-006","ZCB-007","ZCB-008","ZCB-009","ZCB-010","ZCB-011"]
gold={}
with open("/home/hatch/workspace/divination/benchmark/phase3/holdout23/test_gold.jsonl") as f:
    for line in f:
        if line.strip():
            o=json.loads(line); gold[o["id"]]=o
judges={}
for name in ["judgeO1","judgeO2","judgeM1","judgeM2"]:
    d={}
    with open(base/"judging"/f"{name}.jsonl") as f:
        for line in f:
            if line.strip():
                o=json.loads(line); d[o.get("case_id") or o.get("id")]=o
    judges[name]=d
    print(name, "sample keys", list(list(d.values())[0].keys()) if d else [])
for cid in cases:
    print(f"\n=== {cid} ===")
    g=gold[cid]
    print("GOLD_MASTER:", g.get("master_prediction"))
    print("GOLD_OUTCOME:", g.get("outcome_record"))
    pred=json.loads((base/"predictions"/f"{cid}.json").read_text())
    print("OURS_PRED:", pred.get("prediction_text","")[:900])
    for name in ["judgeO1","judgeO2"]:
        o=judges[name].get(cid,{})
        print(name, json.dumps(o,ensure_ascii=False)[:1800])
