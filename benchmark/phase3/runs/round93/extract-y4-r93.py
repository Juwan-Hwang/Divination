import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round93')
block = [json.loads(l) for l in open(base/'judging/judgeY-block4.jsonl', encoding='utf-8') if l.strip()]
mapping = json.load(open(base/'judging/host-mapping.json', encoding='utf-8'))
out = []
for i, row in enumerate(block, 1):
    anon = row['anon_id']
    case = mapping[anon]
    pred = json.load(open(base/'predictions'/f'{case}.json', encoding='utf-8'))
    out.append(f"=== {i} | {anon} | {case} ===\nOUTCOME: {row['outcome_record']}\nPRED: {pred['prediction_text']}\n")
open(base/'y4-dump-r93.txt', 'w', encoding='utf-8').write('\n'.join(out))
print('written', len(out))
