import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round79/acceptance")
cases=["DS-013","DS-014","DS-015","DS-016","DS-017","DS-018","GSZ-028","GSZ-030","GSZ-031","GSZ-032","GSZ-033","QM-015","QM-016","QM-018","QM-019","QM-020","QM-204","QM-205","QM-304","QM-305","QM-306","ZCB-006","ZCB-007","ZCB-008","ZCB-009","ZCB-010","ZCB-011"]
# gold
gold={}
with open("/home/hatch/workspace/divination/benchmark/phase3/holdout23/test_gold.jsonl") as f:
    for line in f:
        if line.strip():
            o=json.loads(line)
            gold[o.get("case_id") or o.get("id")]=o
print("GOLD keys sample", list(gold)[:3])
for cid in cases:
    g=gold.get(cid)
    print("\n===GOLD",cid,"===")
    print(json.dumps(g,ensure_ascii=False)[:4000])
    p=base/"predictions"/f"{cid}.json"
    try:
        txt=p.read_text()
        print("---PRED",cid, txt[:4000])
    except Exception as e:
        print("PRED ERR",e)
for name in ["judgeO1","judgeO2","judgeM1","judgeM2"]:
    print(f"\n##### {name} #####")
    with open(base/"judging"/f"{name}.jsonl") as f:
        for line in f:
            if line.strip():
                print(line.strip()[:3000])
