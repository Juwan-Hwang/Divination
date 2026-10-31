import json, glob, collections, re, os
base='/home/hatch/workspace/divination/benchmark/phase3'
jd=f'{base}/runs/round64/judging'
# raw flags files
seats=['X1','X2','X3','X4','Y1','Y2','Y3','Y4']
raw={}
total=0
for s in seats:
    p=f'{jd}/FLAGS-{s}.md'
    t=open(p).read()
    lines=[l for l in t.splitlines() if 'P3-' in l]
    raw[s]=t
    total+=len(lines)
    print(s, 'exists', os.path.exists(p), 'P3 lines', len(lines), 'first:', lines[0][:120] if lines else None)
print('raw total P3 lines', total)
# compiled
txt=open(f'{jd}/FLAGS-selfreported-r64.md').read()
cur=None; compiled={}
for l in txt.splitlines():
    m=re.match(r'## (X[1-4]|Y[1-4])（(\d+) 条）', l)
    if m: cur=m.group(1); print('section',cur,m.group(2))
    m2=re.match(r'- (P3-[0-9a-f]+)：(.*)', l)
    if m2 and cur:
        compiled.setdefault(m2.group(1), []).append((cur, m2.group(2)))
print('compiled unique', len(compiled), 'lines', sum(len(v) for v in compiled.values()))
hm=json.load(open(f'{jd}/host-mapping.json'))
cases=collections.defaultdict(list)
for a in compiled: cases[hm[a]].append(a)
print('cases', len(cases))
# prior coverage
prior=collections.defaultdict(list)
for f in sorted(glob.glob(f'{base}/data/case-annotations-*.json')):
    d=json.load(open(f))
    rnd=re.search(r'r(\d+)\.json', f).group(1)
    for a in d['annotations']:
        prior[a['case_id']].append((int(rnd), a.get('disposition') or a.get('type_label'), a.get('relation','')))
noprior=[]; 
for c in sorted(cases):
    hist=prior.get(c,[])
    if not hist: noprior.append(c)
    else: print(c, cases[c], 'hist', hist)
print('NO PRIOR:', noprior)
# manifest equality r63 vs r64 cases for flagged
m64=json.load(open(f'{jd}/outcome-manifest.json'))
m63=json.load(open(f'{base}/runs/round63/judging/outcome-manifest.json'))
diff=[]
for c in cases:
    if m64['cases'].get(c)!=m63['cases'].get(c): diff.append(c)
print('outcome diff vs r63:', diff)
print('cases payload type sample', type(m64['cases']['LY-623']), str(m64['cases']['LY-623'])[:200])
