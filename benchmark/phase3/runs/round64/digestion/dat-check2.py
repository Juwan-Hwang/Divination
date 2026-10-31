import json, collections, re, difflib
base='/home/hatch/workspace/divination/benchmark/phase3'
man=json.load(open(f'{base}/runs/round64/judging/outcome-manifest.json'))
for cid in ['LY-207','LY-021','LY-026','LY-522']:
    p=json.load(open(f'{base}/runs/round64/predictions/{cid}.json'))
    print(cid,'PRED:', p['prediction_text'][:420]); print()
for cid in ['AS-303','AS-307','LY-253']:
    card=json.load(open(f'{base}/inputs-dev12/{cid}.json'))
    print(cid,'CARD:', json.dumps(card, ensure_ascii=False)[:700]); print()
print('LY-253 outcome repr:', repr(man['cases']['LY-253']))
print('AS-208 outcome full:', repr(man['cases']['AS-208']))
# similarity scan: R64 flag combined vs latest prior flag
import glob
jd=f'{base}/runs/round64/judging'
txt=open(f'{jd}/FLAGS-selfreported-r64.md').read()
cur=None; compiled=collections.OrderedDict()
for l in txt.splitlines():
    m=re.match(r'## (X[1-4]|Y[1-4])（', l)
    if m: cur=m.group(1)
    m2=re.match(r'- (P3-[0-9a-f]+)：(.*)', l)
    if m2 and cur: compiled.setdefault(m2.group(1), []).append((cur, m2.group(2)))
hm=json.load(open(f'{jd}/host-mapping.json'))
prior=collections.defaultdict(list)
for f in sorted(glob.glob(f'{base}/data/case-annotations-*.json')):
    d=json.load(open(f)); rnd=int(re.search(r'r(\d+)\.json', f).group(1))
    for a in d['annotations']: prior[a['case_id']].append((rnd,a))
def norm(s):
    return re.sub(r'[^一-鿿a-zA-Z0-9]','', s or '')
for anon, fl in compiled.items():
    cid=hm[anon]
    if cid not in prior: continue
    rnd,a=prior[cid][-1]
    pf=norm(a.get('flag',''))
    nf=norm(''.join(t for _,t in fl))
    sim=difflib.SequenceMatcher(None, pf, nf).ratio()
    # also check containment of key phrases
    if sim < 0.45:
        print(f'LOW SIM {cid} R{rnd} sim={sim:.2f}')
        print('  prior:', (a.get('flag','') or '')[:150])
        print('  new  :', ' | '.join(t for _,t in fl)[:200])
