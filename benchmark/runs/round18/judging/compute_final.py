#!/usr/bin/env python3
"""Round 18 最终分合成与分项统计（口径：非分歧例取双评审均值，分歧例取仲裁分）。
merchant 例满分 4（应验不计），其余满分 6；全轮均分百分比 = 逐例百分比平均。
分体系 tradition 取自金标元数据字段（仅用于分组统计，主持角汇总，不改分）。"""
import json
from collections import defaultdict

BASE = '/home/hatch/workspace/divination/benchmark/runs/round18/judging'
GOLD = '/home/hatch/workspace/divination/masters-dataset/holdout/test_gold.jsonl'
MERCHANT = 'lilly-nativity-1616-merchant'
FAMOUS = {'MH-003', 'MH-005', 'ZY-003'}

def maxscore(i):
    return 4 if i == MERCHANT else 6

def load(name):
    out = {}
    with open(f'{BASE}/{name}') as f:
        for line in f:
            line = line.strip()
            if line:
                d = json.loads(line)
                out[d['id']] = d
    return out

A = load('judgeA-scores.jsonl')
B = load('judgeB-scores.jsonl')
try:
    ARB = load('arbiter-scores.jsonl')
except FileNotFoundError:
    ARB = {}
div = set(json.load(open(f'{BASE}/divergent-cases.json')))

final = {}
for i in sorted(set(A) & set(B)):
    if i in div:
        assert i in ARB, f'divergent case missing arbitration: {i}'
        r = ARB[i]
        final[i] = {'id': i, 'direction_score': r['direction_score'],
                    'assertions_score': r['assertions_score'],
                    'outcome_score': r['outcome_score'],
                    'total': r['total'], 'pass': r['pass'], 'source': 'arbiter'}
    else:
        a, b = A[i], B[i]
        tot = (a['total'] + b['total']) / 2
        ms = maxscore(i)
        final[i] = {'id': i,
                    'direction_score': (a['direction_score'] + b['direction_score']) / 2,
                    'assertions_score': (a['assertions_score'] + b['assertions_score']) / 2,
                    'outcome_score': None if (a['outcome_score'] is None or b['outcome_score'] is None)
                        else (a['outcome_score'] + b['outcome_score']) / 2,
                    'total': tot, 'pass': tot >= (4 if ms == 6 else 8 / 3), 'source': 'mean(A,B)'}

with open(f'{BASE}/final-scores.json', 'w') as f:
    json.dump(final, f, ensure_ascii=False, indent=1)

trad = {}
with open(GOLD) as f:
    for line in f:
        d = json.loads(line)
        trad[d['id']] = d['master_predictions'][0]['tradition']

n = len(final)
pct = [v['total'] / maxscore(i) for i, v in final.items()]
raw = [v['total'] for v in final.values()]
print(f'n={n} pass={sum(1 for v in final.values() if v["pass"])}/{n} '
      f'({sum(1 for v in final.values() if v["pass"])/n:.1%})')
print(f'mean raw total = {sum(raw)/n:.2f}; mean per-case pct = {sum(pct)/n:.1%}')
oc = [v['outcome_score'] for v in final.values() if v['outcome_score'] is not None]
print(f'dir={sum(v["direction_score"] for v in final.values())/n:.2f} '
      f'assert={sum(v["assertions_score"] for v in final.values())/n:.2f} '
      f'outcome={sum(oc)/len(oc):.2f} (n={len(oc)})')

by = defaultdict(list)
for i, v in final.items():
    by[trad[i]].append(v)
print('\nper-tradition (sorted by mean pct):')
for t in sorted(by, key=lambda t: -sum(x['total'] / maxscore(x['id']) for x in by[t]) / len(by[t])):
    v = by[t]
    mp = sum(x['total'] / maxscore(x['id']) for x in v) / len(v)
    print(f'  {t}: n={len(v)} mean={sum(x["total"] for x in v)/len(v):.2f} meanpct={mp:.1%} '
          f'pass={sum(1 for x in v if x["pass"])}/{len(v)}')

for label, group in (('famous', FAMOUS), ('non-famous', set(final) - FAMOUS)):
    v = [final[i] for i in group if i in final]
    mp = sum(x['total'] / maxscore(x['id']) for x in v) / len(v)
    print(f'{label}: n={len(v)} mean={sum(x["total"] for x in v)/len(v):.2f} meanpct={mp:.1%} '
          f'pass={sum(1 for x in v if x["pass"])}/{len(v)}')

low = sorted(final.items(), key=lambda kv: kv[1]['total'] / maxscore(kv[0]))
print('\nlowest 15:', [(i, v['total'], v['source']) for i, v in low[:15]])
print('full marks:', [i for i, v in final.items() if v['total'] == maxscore(i)])
print('zero:', [i for i, v in final.items() if v['total'] == 0])
print('cross_system both-judge agreed: LR-001 (see consistency output)')
