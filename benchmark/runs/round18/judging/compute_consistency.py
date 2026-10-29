#!/usr/bin/env python3
"""Round 18 双评审一致性与分歧清单（主持角汇总用，不改分）。
分歧定义（预注册）：（断语+应验两项之和两评审相差 >=2）或通过判定不一致。
merchant 例 outcome=null：以断语单项差 >=2 或通过判定不一致为分歧。"""
import json

BASE = '/home/hatch/workspace/divination/benchmark/runs/round18/judging'

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

n = len(ids)
po = pass_agree / n
pa = sum(1 for i in ids if A[i]['pass']) / n
pb = sum(1 for i in ids if B[i]['pass']) / n
pe = pa * pb + (1 - pa) * (1 - pb)
kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0
print(f"Cohen's kappa (pass): {kappa:.3f}")

def subtotal(d):
    o = d['outcome_score']
    return d['assertions_score'] + (o if o is not None else 0)

div = []
for i in ids:
    if A[i]['pass'] != B[i]['pass'] or abs(subtotal(A[i]) - subtotal(B[i])) >= 2:
        div.append(i)
print('divergent:', div)
with open(f'{BASE}/divergent-cases.json', 'w') as f:
    json.dump(div, f, ensure_ascii=False, indent=1)
print('cross_system A:', [i for i in ids if A[i].get('cross_system')])
print('cross_system B:', [i for i in ids if B[i].get('cross_system')])
