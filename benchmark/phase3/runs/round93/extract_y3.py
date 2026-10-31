import json, os
base='/home/hatch/workspace/divination/benchmark/phase3/runs/round93'
with open(f'{base}/judging/judgeY-block3.jsonl') as f:
    rows=[json.loads(l) for l in f if l.strip()]
with open(f'{base}/judging/host-mapping.json') as f:
    mp=json.load(f)
out=[]
for i,r in enumerate(rows):
    cid=mp[r['anon_id']]
    with open(f'{base}/predictions/{cid}.json') as f:
        p=json.load(f)
    pt=p.get('prediction_text','')
    out.append(f"=== {i} {r['anon_id']} case={cid}\nOUTCOME: {r['outcome_record']}\nPREDICTION:\n{pt}\n")
with open(f'{base}/review_y3_dump.txt','w') as f:
    f.write('\n'.join(out))
print(len(rows), 'written', sum(len(x) for x in out))
