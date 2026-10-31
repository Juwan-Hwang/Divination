import json, glob, collections, re, sys
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
man=json.load(open(f'{jd}/outcome-manifest.json'))
prior=collections.defaultdict(list)
for f in sorted(glob.glob(f'{base}/data/case-annotations-*.json')):
    d=json.load(open(f)); rnd=int(re.search(r'r(\d+)\.json', f).group(1))
    for a in d['annotations']: prior[a['case_id']].append((rnd, a))
out=[]
for anon, fl in compiled.items():
    cid=hm[anon]
    out.append(f'=== {cid} {anon} seats={[s for s,_ in fl]}')
    for s,t in fl: out.append(f'  R64FLAG {s}：{t}')
    out.append(f'  OUTCOME: {man["cases"][cid]}')
    hist=prior.get(cid,[])
    if hist:
        rnd, a = hist[-1]
        out.append(f'  LATEST PRIOR R{rnd} disp={a.get("disposition") or a.get("type_label")} rel={a.get("relation","")}')
        out.append(f'  PRIORFLAG: {a.get("flag","")}')
        out.append(f'  PRIORFINDING: {a.get("finding") or a.get("basis","")}')
        out.append(f'  PRIORHIST: {[(r, x.get("disposition") or x.get("type_label")) for r,x in hist]}')
    else:
        out.append('  NO PRIOR')
open(f'{base}/runs/round64/digestion/dat-dump2.txt','w').write('\n'.join(out))
print('written', len(out))
# no-prior list with flags
np=[hm[a] for a in compiled if hm[a] not in prior]
print('no prior count', len(np), np)
