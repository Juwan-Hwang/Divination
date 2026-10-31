import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12")
ids=["MP-017","MP-018","MP-019"]+[f"OC-{i:03d}" for i in range(1,31)]+[f"WP-{i:03d}" for i in range(1,8)]
for cid in ids:
    p=base/f"{cid}.json"
    try:
        d=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(cid,"ERR",e); continue
    print("===",cid)
    print(json.dumps(d,ensure_ascii=False)[:2500])
