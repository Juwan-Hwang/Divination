import json,sys
base="/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12"
ids=sys.argv[1].split(",")
for cid in ids:
    with open(f"{base}/{cid}.json",encoding="utf-8") as f:
        d=json.load(f)
    print("===",cid)
    print(json.dumps(d,ensure_ascii=False))
