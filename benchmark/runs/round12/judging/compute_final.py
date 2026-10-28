#!/usr/bin/env python3
"""Round 4 最终分合成与分项统计（口径：非分歧例取双评审均值，分歧例取仲裁分）。"""
import json
from collections import defaultdict

BASE = '/home/hatch/workspace/divination/benchmark/runs/round12/judging'
DEV = '/home/hatch/workspace/divination/masters-dataset/data/dev.jsonl'
FAMOUS = {'MH-001', 'MH-002', 'MH-006', 'ZY-001', 'ZY-002', 'ZY-004'}

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
        final[i] = {'id': i,
                    'direction_score': (a['direction_score'] + b['direction_score']) / 2,
                    'assertions_score': (a['assertions_score'] + b['assertions_score']) / 2,
                    'outcome_score': (a['outcome_score'] + b['outcome_score']) / 2,
                    'total': tot, 'pass': tot >= 4, 'source': 'mean(A,B)'}

with open(f'{BASE}/final-scores.json', 'w') as f:
    json.dump(final, f, ensure_ascii=False, indent=1)

trad = {}
with open(DEV) as f:
    for line in f:
        d = json.loads(line)
        trad[d['id']] = d['master_predictions'][0]['tradition']

n = len(final)
tot = [v['total'] for v in final.values()]
print(f'n={n} pass={sum(1 for v in final.values() if v["pass"])}/{n} '
      f'({sum(1 for v in final.values() if v["pass"])/n:.1%}) mean={sum(tot)/n:.2f} ({sum(tot)/n/6:.1%})')
print(f'dir={sum(v["direction_score"] for v in final.values())/n:.2f} '
      f'assert={sum(v["assertions_score"] for v in final.values())/n:.2f} '
      f'outcome={sum(v["outcome_score"] for v in final.values())/n:.2f}')
print(f'cross_system: A={sum(1 for v in A.values() if v.get("cross_system"))} '
      f'B={sum(1 for v in B.values() if v.get("cross_system"))}')

by = defaultdict(list)
for i, v in final.items():
    by[trad[i]].append(v['total'])
print('\nper-tradition:')
for t in sorted(by, key=lambda t: -sum(by[t]) / len(by[t])):
    v = by[t]
    print(f'  {t}: n={len(v)} mean={sum(v)/len(v):.2f} pass={sum(1 for x in v if x >= 4)}/{len(v)}')

for label, group in (('famous', FAMOUS), ('non-famous', set(final) - FAMOUS)):
    v = [final[i]['total'] for i in group if i in final]
    print(f'{label}: n={len(v)} mean={sum(v)/len(v):.2f} pass={sum(1 for x in v if x >= 4)}/{len(v)}')

low = sorted(final.items(), key=lambda kv: kv[1]['total'])
print('\nlowest 12:', [(i, v['total']) for i, v in low[:12]])
print('full marks (6.0):', sum(1 for v in final.values() if v['total'] == 6))
print('exactly 3.0:', [i for i, v in final.items() if v['total'] == 3.0])
ly = {i: v['total'] for i, v in final.items() if trad[i] == 'liuyao'}
print(f'liuyao <=1: {[i for i, x in ly.items() if x <= 1]}')
bz = {i: v['total'] for i, v in final.items() if trad[i] == 'bazi'}
print(f'bazi exactly 3.0 count: {sum(1 for x in bz.values() if x == 3.0)}')
