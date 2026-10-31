import json, glob, collections, re
base='/home/hatch/workspace/divination/benchmark/phase3'
jd=f'{base}/runs/round64/judging'
txt=open(f'{jd}/FLAGS-selfreported-r64.md').read()
cur=None; compiled=collections.OrderedDict()
for l in txt.splitlines():
    m=re.match(r'## (X[1-4]|Y[1-4])（', l)
    if m: cur=m.group(1)
    m2=re.match(r'- (P3-[0-9a-f]+)：(.*)', l)
    if m2 and cur: compiled.setdefault(m2.group(1), []).append((cur, m2.group(2)))
hm=json.load(open(f'{jd}/host-mapping.json'))
m64=json.load(open(f'{jd}/outcome-manifest.json'))
# BZ-029 check
for a in ['P3-0fe6c7e3','P3-0fdbcca1']:
    print(a, '->', hm[a], 'flags', compiled[a])
for cid in ['BZ-029','BZ-040','LY-531']:
    print(cid, 'outcome:', m64['cases'].get(cid))
    card=json.load(open(f'{base}/inputs-dev12/{cid}.json'))
    print(cid, 'card keys:', list(card.keys()))
    print(cid, 'card:', json.dumps(card, ensure_ascii=False)[:900])
    print()
# LY-537, YM-070
for cid in ['LY-537','YM-070']:
    print(cid, 'outcome:', m64['cases'].get(cid))
print('BZ-040 in compiled cases?', 'BZ-040' in [hm[a] for a in compiled])
import os
print('round64 predictions exists:', os.path.isdir(f'{base}/runs/round64/predictions'))
if os.path.isdir(f'{base}/runs/round64/predictions'):
    print('BZ-304 pred:', json.dumps(json.load(open(f'{base}/runs/round64/predictions/BZ-304.json')), ensure_ascii=False)[:600])
