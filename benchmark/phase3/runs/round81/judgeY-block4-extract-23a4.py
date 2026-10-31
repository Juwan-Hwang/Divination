import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round81')
block = base/'judging'/'judgeY-block4.jsonl'
mapping = json.loads((base/'judging'/'host-mapping.json').read_text(encoding='utf-8'))
out = base/'judging'/'judgeY-block4-extract-23a4.txt'
lines=[]
with block.open(encoding='utf-8') as f:
    rows=[json.loads(l) for l in f if l.strip()]
for i,row in enumerate(rows,1):
    anon=row['anon_id']; case=mapping[anon]
    pred=json.loads((base/'predictions'/f'{case}.json').read_text(encoding='utf-8'))
    lines.append(f"=== {i} {anon} {case}\nOUT: {row.get('outcome_record','')}\nPRED: {pred.get('prediction_text','')}\n")
out.write_text('\n'.join(lines),encoding='utf-8')
print(len(rows), out.stat().st_size)
