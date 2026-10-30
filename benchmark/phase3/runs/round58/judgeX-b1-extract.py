import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round58')
mapping=json.loads((base/'judging/host-mapping.json').read_text())
lines=(base/'judging/judgeX-block1.jsonl').read_text().splitlines()
out=[]
for ln in lines:
    o=json.loads(ln)
    anon=o['anon_id']; cid=mapping[anon]
    pred=json.loads((base/'predictions'/f'{cid}.json').read_text())
    out.append({'anon_id':anon,'case_id':cid,'prediction_text':pred.get('prediction_text'),'outcome':o['outcome_record']})
with open(base/'judgeX-b1-combined.json','w') as f:
    json.dump(out,f,ensure_ascii=False,indent=1)
print(len(out))
