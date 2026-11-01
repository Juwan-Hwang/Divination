# R96 数据席探查（只读）
import json
from collections import Counter
BASE='/home/hatch/workspace/divination/benchmark/phase3'
r95=json.load(open(f'{BASE}/data/case-annotations-r95.json'))
print('r95 keys', list(r95.keys()))
print('round', r95.get('round'))
ann=r95['annotations']
print('len', len(ann), Counter(a['disposition'] for a in ann))
print('special', len(r95['special_checks']))
print('counts verdicts', r95['counts'].get('verdicts'), r95['counts'].get('cases_total'))
man=json.load(open(f'{BASE}/runs/round96/judging/outcome-manifest.json'))
print('manifest top keys', [k for k in man.keys()])
lay=man.get('_r95_carryover_notes_addendum')
print('layer type', type(lay), list(lay.keys()) if isinstance(lay,dict) else lay)
for k,v in (lay.items() if isinstance(lay,dict) else []):
    print('---LAYER',k)
    print(v)
# flags mapping
import re
flags=open(f'{BASE}/runs/round96/judging/judge-flags-r96.md',encoding='utf-8').read()
bullets=[ln.strip() for ln in flags.splitlines() if ln.strip().startswith('- P3-')]
print('bullets',len(bullets))
anons=[re.search(r'P3-[0-9a-f]{8}',ln).group(0) for ln in bullets]
print('unique anons',len(set(anons)))
hm=json.load(open(f'{BASE}/runs/round96/judging/host-mapping.json'))
for a in anons:
    print(a, hm.get(a))
print('--- annotations for flag cases ---')
for a in anons:
    cid=hm[a]
    bars=[x for x in ann if x['case_id']==cid]
    print(f"== {a} {cid} bars={len(bars)}")
    for b in bars:
        print('  round',b.get('registered_round'),'disp',b['disposition'],'anon',b.get('anon_id'))
        print('  finding:',b.get('finding','')[:400])
        print('  flag:',b.get('flag','')[:200])
        print('  carry:',b.get('manifest_carry_suggestion','')[:300])
        print('  relation:',b.get('relation'))
print('--- cases outcomes for flag cases ---')
cases=man['cases']
for a in anons:
    cid=hm[a]
    print(f"== {cid} outcome: {cases.get(cid)!r}")
    # stripped tail if exists
    st=man.get('stripped_tail',{})
    if cid in st:
        print(f"   stripped_tail: {st[cid]!r}")
print('--- OC-019, YY2 ---')
for cid in ('OC-019','YY2-003','YY2-004','YY2-005','OC-012','LY-615'):
    print(cid, 'outcome', cases.get(cid))
    try:
        inp=json.load(open(f'{BASE}/inputs-dev12/{cid}.json'))
        print(' inp keys', list(inp.keys()), 'tradition', inp.get('tradition'), 'system', inp.get('system'))
        print(' context', json.dumps(inp.get('context'),ensure_ascii=False)[:600])
        print(' provenance', inp.get('provenance'))
    except Exception as e:
        print(' inp err', e)
