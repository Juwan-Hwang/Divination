import json, pathlib
P=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
b=json.loads((P/'runs/round89/batches.json').read_text())
ids=b['B09']+b['B10']
import sys
sel=sys.argv[1] if len(sys.argv)>1 else 'B09'
lst=b[sel]
for cid in lst:
    d=json.loads((P/f'inputs-dev12/{cid}.json').read_text())
    print('='*20, cid)
    print(json.dumps(d, ensure_ascii=False, indent=1))
