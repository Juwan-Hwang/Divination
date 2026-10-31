import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
ids = []
b = json.loads((base/'runs/round77/batches.json').read_text())
for k in ['B01','B02','B03']:
    ids += b[k]
assert len(ids)==60, len(ids)
out=[]
for cid in ids:
    d=json.loads((base/'inputs-dev12'/f'{cid}.json').read_text())
    out.append(d)
p = base/'runs/round77/s1_inputs_compact.json'
p.write_text(json.dumps(out, ensure_ascii=False, indent=1))
print('wrote', len(out), p.stat().st_size)
