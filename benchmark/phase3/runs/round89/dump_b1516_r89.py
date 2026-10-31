import json, pathlib
P3 = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
batches = json.loads((P3/'runs/round89/batches.json').read_text())
ids = batches['B15'] + batches['B16']
out = []
for cid in ids:
    card = json.loads((P3/f'inputs-dev12/{cid}.json').read_text())
    out.append(json.dumps(card, ensure_ascii=False))
(P3/'runs/round89/cards_b1516_r89.txt').write_text('\n@@@\n'.join(out), encoding='utf-8')
print(len(ids), 'cards written')
