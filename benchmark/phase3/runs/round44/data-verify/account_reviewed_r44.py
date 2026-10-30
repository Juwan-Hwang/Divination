import json, collections
def load(p):
    return [json.loads(l) for l in open(p)]
used=set()
for l in open('runs/round43/data-verify/used-union-r43.jsonl'):
    d=json.loads(l); used.add(d.get('id') or d.get('case_id'))
dev9=set(json.load(open('runs/round43/batches.json')).keys())
allbatch=set()
for v in json.load(open('runs/round43/batches.json')).values(): allbatch.update(v)
print('used union:', len(used), 'dev9 batches ids:', len(allbatch))
for name, path in [('bianyi-yuce','expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl'),
                   ('natal-batch2','expansion12/natal-batch2/cases-reviewed.jsonl')]:
    rows=load(path)
    ids=[r['id'] for r in rows]
    print(f'== {name}: {len(rows)} rows, unique ids {len(set(ids))}')
    print('  prefixes:', collections.Counter(i.rsplit("-",1)[0] for i in ids))
    print('  holdout_eligible:', collections.Counter(str(r.get('holdout_eligible')) for r in rows))
    print('  contamination:', collections.Counter(str(r.get('contamination')) for r in rows))
    inused=[i for i in ids if i in used]; indev=[i for i in ids if i in allbatch]
    notused=[r for r in rows if r['id'] not in used]
    print(f'  in used-union: {len(inused)}; in dev9: {len(indev)}; NOT in used: {len(notused)}')
    nu_elig=[r for r in notused if r.get('holdout_eligible') is True]
    print(f'  NOT-used & holdout_eligible=True: {len(nu_elig)}')
    print('  NOT-used prefixes:', collections.Counter(r['id'].rsplit("-",1)[0] for r in notused))
    print('  NOT-used eligible prefixes:', collections.Counter(r['id'].rsplit("-",1)[0] for r in nu_elig))
    print('  NOT-used sample ids:', [r['id'] for r in notused[:8]])
    print('  eligible-but-used sample:', [r['id'] for r in rows if r.get('holdout_eligible') is True and r['id'] in used][:8])
# LR3 special
for lid in ['LR3-103','LR3-106','LR3-108']:
    print(lid, 'in used:', lid in used, 'in dev9:', lid in allbatch)
