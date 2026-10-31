import json, collections, re
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
cases=man['cases']; tails=man.get('stripped_tail',{})
def variants(s):
    # traditional/simplified rough: just return as-is plus a few swaps
    return [s]
for anon, fl in compiled.items():
    cid=hm[anon]
    card=json.dumps(json.load(open(f'{base}/inputs-dev12/{cid}.json')), ensure_ascii=False)
    try:
        pred=json.dumps(json.load(open(f'{base}/runs/round64/predictions/{cid}.json')), ensure_ascii=False)
    except Exception:
        pred=''
    hay=cases.get(cid,'')+' '+tails.get(cid,'')+' '+card+' '+pred
    for seat, ftext in fl:
        quotes=re.findall(r'[「『]([^」』]{2,})[」』]', ftext)
        bad=[]
        for q in quotes:
            if q not in hay:
                # try ignoring punctuation variants
                bad.append(q)
        if bad:
            print(f'{cid} {anon} {seat}: MISS quotes={bad} | flag={ftext[:90]} | outcome={cases.get(cid,"")[:90]}')
print('done')
# LY-013 full
print('LY-013 outcome:', repr(cases['LY-013']), 'tail:', repr(tails.get('LY-013')))
print('LY-013 pred:', open(f'{base}/runs/round64/predictions/LY-013.json').read()[:800])
