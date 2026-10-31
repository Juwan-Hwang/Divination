import json, pathlib, sys
BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
batches = json.loads((BASE/'runs/round78/batches.json').read_text())
ids = batches['B10']+batches['B11']+batches['B12']
which = sys.argv[1] if len(sys.argv)>1 else 'B10'
for cid in batches[which]:
    p = BASE/'inputs-dev12'/f'{cid}.json'
    d = json.loads(p.read_text())
    print('===', cid)
    print(json.dumps(d, ensure_ascii=False))
