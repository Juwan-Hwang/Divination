import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round57')
rows = [json.loads(l) for l in open(base/'judging/judgeX-block1.jsonl', encoding='utf-8') if l.strip()]
mapping = json.load(open(base/'judging/host-mapping.json', encoding='utf-8'))
out=[]
for r in rows:
    anon=r['anon_id']; case=mapping.get(anon)
    pfile=base/'predictions'/f'{case}.json'
    try:
        p=json.load(open(pfile, encoding='utf-8'))
        txt=p.get('prediction_text','')
        keys=list(p.keys())
    except Exception as e:
        txt=f'ERROR {e}'; keys=[]
    out.append({'anon_id':anon,'case_id':case,'outcome_record':r.get('outcome_record',''),'carry_note':r.get('carry_note',''),'prediction_text':txt,'keys':keys})
with open(base/'x1_dump.json','w',encoding='utf-8') as f:
    json.dump(out,f,ensure_ascii=False,indent=1)
print(len(out))
for o in out:
    print(o['anon_id'], o['case_id'], len(o['prediction_text']))
