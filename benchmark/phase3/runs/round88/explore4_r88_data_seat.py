import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
ids=['WHY-043','DA-051','DA-048','DA-055','WHY-068','WHY-069','GSZ-107','BY-030']
gold={}
for line in open(base/'holdout31/test_gold.jsonl', encoding='utf-8'):
    line=line.strip()
    if not line: continue
    o=json.loads(line)
    gold[o.get('case_id') or o.get('id')]=o
print('gold keys sample', list(gold)[:5], 'n', len(gold))
hm=json.load(open(base/'runs/round88/acceptance/judging/host-mapping.json'))
print('acc host-mapping sample', str(hm)[:400])
inv={}
def walk(o):
    if isinstance(o,dict):
        for k,v in o.items():
            if isinstance(v,str) and v in ids: inv[v]=k
            walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
walk(hm); print('anon inv', inv)
for cid in ids:
    print('='*20, cid, 'anon', inv.get(cid))
    card=json.load(open(base/f'holdout31/inputs/{cid}.json'))
    print('CARD:', json.dumps(card, ensure_ascii=False)[:1800])
    g=gold.get(cid)
    print('GOLD:', json.dumps(g, ensure_ascii=False)[:1800] if g else None)
    pred=json.load(open(base/f'runs/round88/acceptance/predictions/{cid}.json'))
    print('PRED keys:', list(pred.keys()))
    print('PRED:', json.dumps(pred, ensure_ascii=False)[:1800])
    print()
