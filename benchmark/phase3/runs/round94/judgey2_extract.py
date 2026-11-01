import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round94')
block = [json.loads(l) for l in open(base/'judging/judgeY-block2.jsonl', encoding='utf-8') if l.strip()]
mapping = json.load(open(base/'judging/host-mapping.json', encoding='utf-8'))
out = open(base/'judging/judgey2-work.txt','w',encoding='utf-8')
missing=[]
for i,row in enumerate(block):
    anon=row['anon_id']; cid=mapping.get(anon)
    ptext=None
    if cid:
        p=json.load(open(base/'predictions'/f'{cid}.json',encoding='utf-8'))
        ptext=p.get('prediction_text')
    if not ptext: missing.append(anon)
    out.write(f"=== {i+1} | {anon} | {cid} ===\nOUTCOME: {row.get('outcome_record')}\nCARRY: {row.get('carry_note')}\nPRED: {ptext}\n\n")
out.close()
print('rows',len(block),'missing',missing)
