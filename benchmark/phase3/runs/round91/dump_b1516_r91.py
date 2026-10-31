import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
batches = json.loads((base/'runs/round91/batches.json').read_text())
ids = batches['B15'] + batches['B16']
out = []
for cid in ids:
    d = json.loads((base/f'inputs-dev12/{cid}.json').read_text())
    out.append(f"===== {cid} =====")
    out.append(json.dumps(d, ensure_ascii=False))
    out.append('')
pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round91/cards_b1516_r91.txt').write_text('\n'.join(out))
print(len(ids))
