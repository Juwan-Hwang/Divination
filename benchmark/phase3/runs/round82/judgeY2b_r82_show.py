import json, pathlib, sys
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round82')
rows=[json.loads(l) for l in open(base/'judging/judgeY-block2.jsonl')]
mp=json.load(open(base/'judging/host-mapping.json'))
s=int(sys.argv[1]); e=int(sys.argv[2])
for i,r in enumerate(rows[s:e], start=s):
    cid=mp[r['anon_id']]
    p=json.load(open(base/'predictions'/f'{cid}.json'))
    pt=p.get('prediction_text') or p.get('prediction') or str(p)
    if not isinstance(pt,str): pt=json.dumps(pt,ensure_ascii=False)
    print(f"=== {i} {r['anon_id']} {cid} ===")
    print("OUT:", r['outcome_record'])
    print("PRED:", pt)
    print()
