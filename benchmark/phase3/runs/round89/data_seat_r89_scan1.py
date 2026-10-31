import json, re, os
base="/home/hatch/workspace/divination/benchmark/phase3"
hm=json.load(open(f"{base}/runs/round89/judging/host-mapping.json",encoding="utf-8"))
# judge merged files
for name in ["judgeX-merged.json","judgeY-merged.json"]:
    p=f"{base}/runs/round89/judging/{name}"
    d=json.load(open(p,encoding="utf-8"))
    print(name, type(d), list(d.keys())[:10] if isinstance(d,dict) else len(d))
    # sample one entry
    if isinstance(d,dict):
        k0=list(d.keys())[0]
        print(" sample key",k0, json.dumps(d[k0],ensure_ascii=False)[:1500])
    elif isinstance(d,list):
        print(json.dumps(d[0],ensure_ascii=False)[:1500])
