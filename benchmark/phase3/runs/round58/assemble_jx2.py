import json, os
base='/home/hatch/workspace/divination/benchmark/phase3/runs/round58'
rows=[json.loads(l) for l in open(f'{base}/judging/judgeX-block2.jsonl')]
mp=json.load(open(f'{base}/judging/host-mapping.json'))
out=open(f'{base}/assemble-judgeX-block2.txt','w')
for i,r in enumerate(rows):
    cid=mp[r['anon_id']]
    pj=json.load(open(f'{base}/predictions/{cid}.json'))
    pt=pj.get('prediction_text') or pj.get('prediction') or ''
    if not isinstance(pt,str): pt=json.dumps(pt,ensure_ascii=False)
    out.write(f"=== {i+1} {r['anon_id']} case={cid} ===\n")
    out.write("PREDICTION_TEXT:\n"+pt+"\n")
    out.write("OUTCOME:\n"+json.dumps(r.get('outcome_record'),ensure_ascii=False)+"\n")
    for k in ('carry_note','editor_note'):
        if r.get(k): out.write(f"{k}: "+json.dumps(r[k],ensure_ascii=False)+"\n")
    out.write("\n")
out.close()
print('done', len(rows))
