import json, sys
base='/home/hatch/workspace/divination/benchmark/phase3/runs/round93'
rows=[json.loads(l) for l in open(base+'/judging/judgeX-block3.jsonl',encoding='utf-8') if l.strip()]
mapping=json.load(open(base+'/judging/host-mapping.json',encoding='utf-8'))
lo,hi=int(sys.argv[1]),int(sys.argv[2])
for i,r in enumerate(rows[lo:hi],start=lo):
    cid=mapping[r['anon_id']]
    pred=json.load(open(base+f'/predictions/{cid}.json',encoding='utf-8'))
    print(f"=== [{i}] {r['anon_id']} -> {cid}")
    print(pred.get('prediction_text',''))
    print()
