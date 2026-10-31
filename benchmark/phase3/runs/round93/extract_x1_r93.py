import json
base='/home/hatch/workspace/divination/benchmark/phase3/runs/round93'
mapping=json.load(open(f'{base}/judging/host-mapping.json'))
rows=[json.loads(l) for l in open(f'{base}/judging/judgeX-block1.jsonl') if l.strip()]
print('rows',len(rows))
with open(f'{base}/x1-combined-r93.txt','w') as out:
    for r in rows:
        cid=mapping[r['anon_id']]
        pred=json.load(open(f'{base}/predictions/{cid}.json'))
        out.write(f"===== {r['anon_id']} | {cid} =====\nOUTCOME: {r['outcome_record']}\nPREDICTION_TEXT:\n{pred.get('prediction_text','')}\n\n")
print('done')
