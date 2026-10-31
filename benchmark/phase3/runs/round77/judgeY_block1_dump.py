import json, sys
base="/home/hatch/workspace/divination/benchmark/phase3/runs/round77"
rows=[json.loads(l) for l in open(f"{base}/judging/judgeY-block1.jsonl",encoding="utf-8")]
mp=json.load(open(f"{base}/judging/host-mapping.json",encoding="utf-8"))
start=int(sys.argv[1]); end=int(sys.argv[2])
for i,r in enumerate(rows[start:end], start=start):
    cid=mp[r["anon_id"]]
    try:
        p=json.load(open(f"{base}/predictions/{cid}.json",encoding="utf-8"))
        pt=p.get("prediction_text") or p.get("prediction") or str(p)
        if not isinstance(pt,str): pt=json.dumps(pt,ensure_ascii=False)
    except Exception as e:
        pt=f"<ERR {e}>"
    print(f"\n=== #{i} {r['anon_id']} -> {cid} ===")
    print("PRED:", pt)
    print("OUTCOME:", r["outcome_record"])
    for k in ("carry_note","editor_note"):
        if k in r: print(k.upper()+":", r[k][:400])
