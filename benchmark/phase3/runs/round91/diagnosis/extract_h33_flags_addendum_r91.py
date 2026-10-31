import json, glob, os, re
base = os.path.expanduser('~/workspace/divination/benchmark/phase3')
preds = sorted(glob.glob(base+'/runs/round91/acceptance/predictions/*.json'))
for p in preds:
    d = json.load(open(p))
    cid = os.path.basename(p)
    print('='*20, cid, 'keys:', list(d.keys()))
    # print basis-like fields fully
    for k, v in d.items():
        if isinstance(v, str) and ('basis' in k or 'flag' in k or 'note' in k):
            print(f'--{k}--')
            print(v)
        elif k in ('basis',):
            print(json.dumps(v, ensure_ascii=False, indent=1))
    # if basis is nested
    s = json.dumps(d, ensure_ascii=False)
    # find flag keywords contexts
    for kw in ['未载','未直载','推导','残损','底本未载','自注','不合','旬空','化神','病程','病位','同日']:
        for m in re.finditer(kw, s):
            a=max(0,m.start()-120); b=min(len(s), m.end()+120)
            print(f'  [{kw}] ...{s[a:b]}...')
            break
