import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round93')
block = [json.loads(l) for l in open(base/'judging/judgeX-block1.jsonl', encoding='utf-8')]
mapping = json.load(open(base/'judging/host-mapping.json', encoding='utf-8'))
out=[]
for i, item in enumerate(block):
    anon=item['anon_id']
    case=mapping[anon]
    pred=json.load(open(base/'predictions'/f'{case}.json', encoding='utf-8'))
    ptext=pred.get('prediction_text','')
    out.append(f"=== {i+1} {anon} case={case}\nOUTCOME: {item.get('outcome_record','')}\n")
    if 'carry_note' in item: out.append(f"CARRY: {item['carry_note']}\n")
    if 'editor_note' in item: out.append(f"EDITOR: {item['editor_note']}\n")
    out.append(f"PREDICTION:\n{ptext}\n")
open(base/'judgeX1-review.txt','w',encoding='utf-8').write('\n'.join(out))
print(len(block))
