import json, os, sys
base="/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12"
ids=sys.argv[1:]
for cid in ids:
    d=json.load(open(os.path.join(base,cid+".json")))
    # strip notes completion verbose
    copy={k:v for k,v in d.items() if k!='notes'}
    print("===",cid)
    print(json.dumps(copy,ensure_ascii=False))
    print()
