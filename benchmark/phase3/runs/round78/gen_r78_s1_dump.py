import json,sys
base="/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12/"
ids=sys.argv[1:]
for cid in ids:
    with open(base+cid+".json",encoding="utf-8") as f:
        d=json.load(f)
    print("="*20, cid)
    print(json.dumps(d,ensure_ascii=False,indent=1))
