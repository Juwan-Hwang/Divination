import json,sys
base='/home/hatch/workspace/divination/benchmark/phase3/runs/round63'
rows=[json.loads(l) for l in open(base+'/judging/judgeY-block2.jsonl')]
mp=json.load(open(base+'/judging/host-mapping.json'))
lo=int(sys.argv[1]); hi=int(sys.argv[2])
for i,r in enumerate(rows[lo:hi], start=lo):
    cid=mp[r['anon_id']]
    pred=json.load(open(f"{base}/predictions/{cid}.json"))
    pt=pred.get('prediction_text','')
    print(f"=== {i} {r['anon_id']} {cid} ===")
    print("PRED:", pt)
    print("OUTCOME:", r['outcome_record'])
    for k in ('carry_note','editor_note'):
        if k in r: print(k.upper()+":", r[k])
    print()
