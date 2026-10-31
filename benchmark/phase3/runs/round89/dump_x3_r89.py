import json
base='/home/hatch/workspace/divination/benchmark/phase3/runs/round89'
rows=[json.loads(l) for l in open(base+'/judging/judgeX-block3.jsonl') if l.strip()]
hm=json.load(open(base+'/judging/host-mapping.json'))
out=open(base+'/dump_x3_r89.txt','w')
missing=[]
for i,r in enumerate(rows):
    cid=hm.get(r['anon_id'])
    if not cid:
        missing.append(r['anon_id']); pt='<<NO MAPPING>>'
    else:
        try:
            pj=json.load(open(f"{base}/predictions/{cid}.json"))
            pt=pj.get('prediction_text','<<NO prediction_text FIELD>> keys='+str(list(pj.keys())))
        except Exception as e:
            pt=f'<<ERR {e}>>'; missing.append(r['anon_id'])
    out.write(f"### {i+1} {r['anon_id']} case={cid}\nOUTCOME: {r['outcome_record']}\nPRED: {pt}\n\n")
out.close()
print('rows',len(rows),'missing',missing)
