# R96 数据席探查2：manifest 各层与 predictions
import json, re
BASE='/home/hatch/workspace/divination/benchmark/phase3'
man=json.load(open(f'{BASE}/runs/round96/judging/outcome-manifest.json'))
hm=json.load(open(f'{BASE}/runs/round96/judging/host-mapping.json'))
flags=open(f'{BASE}/runs/round96/judging/judge-flags-r96.md',encoding='utf-8').read()
bullets=[ln.strip() for ln in flags.splitlines() if ln.strip().startswith('- P3-')]
anons=[re.search(r'P3-[0-9a-f]{8}',ln).group(0) for ln in bullets]
cids=[hm[a] for a in anons]
for cid in cids:
    print(f"== {cid}")
    for k,v in man.items():
        if isinstance(v,dict) and cid in v:
            txt=v[cid] if isinstance(v[cid],str) else json.dumps(v[cid],ensure_ascii=False)
            print(f"  LAYER {k}: {txt[:500]}")
    # check _r38 etc maybe key different? also search in whole manifest text for cid in carry layers values
    for k,v in man.items():
        if k.startswith('_r') and isinstance(v,dict):
            for kk,vv in v.items():
                if isinstance(vv,str) and cid in vv and kk!=cid:
                    print(f"  MENTION {k}[{kk}]: {vv[:400]}")
for cid in ('LY-615','YM-053','MH-010','LY-517','OC-025','LR3-116'):
    print(f"==== PRED {cid}")
    try:
        p=json.load(open(f'{BASE}/runs/round96/predictions/{cid}.json'))
        print(json.dumps(p,ensure_ascii=False)[:2000])
    except Exception as e:
        print(e)
    inp=json.load(open(f'{BASE}/inputs-dev12/{cid}.json'))
    print('INP', json.dumps(inp,ensure_ascii=False)[:1200])
