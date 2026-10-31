import json
base='/home/hatch/workspace/divination/benchmark/phase3/'
b=json.load(open(base+'runs/round64/batches.json'))
ids=[]
for k in ('B16','B17','B18'): ids+=b[k]
assert len(ids)==60, len(ids)
out=[]
for cid in ids:
    d=json.load(open(base+f'inputs-dev12/{cid}.json'))
    out.append('====='+cid)
    out.append(json.dumps({k:v for k,v in d.items() if k not in ('provenance','notes')},ensure_ascii=False))
    nt=d.get('notes')
    if nt:
        s=json.dumps(nt,ensure_ascii=False)
        out.append('NOTES(len %d): %s'%(len(s), s[:600]))
print('\n'.join(out))
