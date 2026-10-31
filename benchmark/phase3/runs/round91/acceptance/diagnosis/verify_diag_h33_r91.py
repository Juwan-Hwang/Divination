import json, pathlib, re
from collections import Counter
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
acc = base/'runs/round91/acceptance'
ids = sorted([p.stem for p in (acc/'predictions').glob('*.json')])
seg = lambda c: c.split('-')[0]
cnt = Counter(); changed=[]; reserve=[]; disputed=[]; reasons=Counter()
for cid in ids:
    p=json.load(open(acc/'predictions'/f'{cid}.json')); b=p.get('basis',''); s=seg(cid)
    for key,pat in [('节名第八节','第八节'),('R80','R80'),('做功主线','做功主线'),('主线','主线'),('功量核','功量核'),('功量','功量'),('量级','量级')]:
        if pat in b: cnt[(key,'ALL')]+=1; cnt[(key,s)]+=1
    t=p.get('trigger',{})
    if t.get('changed_main'): changed.append(cid)
    if t.get('reserve_used'): reserve.append(cid)
    if t.get('disputed'): disputed.append(cid)
    reasons[t.get('reason','')]+=1
for k in sorted(cnt): print(k, cnt[k])
print('changed', len(changed), changed)
print('reserve', len(reserve), reserve)
print('disputed', len(disputed), disputed)
print('reason distinct', len(reasons), 'empty reason n=', reasons.get('',0))
# input field check for WHY cases: fu_shen presence and chart relatives
for cid in ids:
    if cid.startswith('WHY'):
        inp=json.load(open(base/'holdout33/inputs'/f'{cid}.json')); a=inp.get('anchors',{})
        print(cid, 'fu_shen=', repr(a.get('fu_shen','<no field>')), '| bian=', a.get('bian_gua'))
    else:
        inp=json.load(open(base/'holdout33/inputs'/f'{cid}.json')); a=inp.get('anchors',{})
        print(cid, 'anchors keys=', sorted(a.keys()))
