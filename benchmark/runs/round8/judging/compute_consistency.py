#!/usr/bin/env python3
"""Round 4 双评审一致性与分歧清单计算（主持角汇总用，不改分）。"""
import json, sys
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/runs/round8/judging'

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
ids = sorted(set(A) & set(B))
print(f'A={len(A)} B={len(B)} common={len(ids)}')
only_a = sorted(set(A) - set(B)); only_b = sorted(set(B) - set(A))
if only_a: print('only in A:', only_a)
if only_b: print('only in B:', only_b)

exact = sum(1 for i in ids if A[i]['total'] == B[i]['total'])
pass_agree = sum(1 for i in ids if A[i]['pass'] == B[i]['pass'])
print(f'total exact agreement: {exact}/{len(ids)} = {exact/len(ids):.3f}')
print(f'pass agreement: {pass_agree}/{len(ids)} = {pass_agree/len(ids):.3f}')

# Cohen's kappa on pass/fail
n = len(ids)
po = pass_agree / n
pa = sum(1 for i in ids if A[i]['pass']) / n
pb = sum(1 for i in ids if B[i]['pass']) / n
pe = pa * pb + (1 - pa) * (1 - pb)
kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0
print(f'Cohen kappa (pass): {kappa:.3f}  (A pass={int(pa*n)}, B pass={int(pb*n)})')
for name, J in (('A', A), ('B', B)):
    tot = [J[i]['total'] for i in ids]
    print(f'Judge {name}: pass={sum(1 for i in ids if J[i]["pass"])}, mean total={sum(tot)/n:.2f}, '
          f'dir={sum(J[i]["direction_score"] for i in ids)/n:.2f}, '
          f'assert={sum(J[i]["assertions_score"] for i in ids)/n:.2f}, '
          f'outcome={sum(J[i]["outcome_score"] for i in ids)/n:.2f}, '
          f'cross_system={sum(1 for i in ids if J[i].get("cross_system"))}')

div = []
for i in ids:
    a, b = A[i], B[i]
    ao = a['assertions_score'] + a['outcome_score']
    bo = b['assertions_score'] + b['outcome_score']
    if a['pass'] != b['pass'] or abs(ao - bo) >= 2 or abs(a['total'] - b['total']) >= 2:
        div.append(i)
print(f'divergent cases ({len(div)}): {div}')
with open(f'{BASE}/divergent-cases.json', 'w') as f:
    json.dump(div, f, ensure_ascii=False, indent=1)
