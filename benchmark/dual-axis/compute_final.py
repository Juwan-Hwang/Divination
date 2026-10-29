#!/usr/bin/env python3
"""主持角合成：轴二最终分（分歧例取仲裁、其余取双评审均值）＋与轴一交叉统计。
只读既有分数文件，不改动任何分数；产出 dual-axis/final-axis2-scores.json 与 stats.json。"""
import json, os
from collections import Counter, defaultdict

ROOT = os.path.expanduser('~/workspace/divination')
DA = f'{ROOT}/benchmark/dual-axis'

def load_jsonl(p):
    if not os.path.exists(p):
        return {}
    return {json.loads(l)['anon_id']: json.loads(l) for l in open(p) if l.strip()}

A = load_jsonl(f'{DA}/judging/judgeA-scores.jsonl')
B = load_jsonl(f'{DA}/judging/judgeB-scores.jsonl')
ARB = load_jsonl(f'{DA}/judging/arbiter-scores.jsonl')
mapping = json.load(open(f'{DA}/host-mapping.json'))

AXIS1_FILES = {
    'round17_dev': 'benchmark/runs/round17/judging/final-scores.json',
    'round18_test': 'benchmark/runs/round18/judging/final-scores.json',
    'round1_dev': 'benchmark/runs/round1/judging/final-scores.json',
}
axis1 = {}
for g, rel in AXIS1_FILES.items():
    d = json.load(open(f'{ROOT}/{rel}'))
    axis1[g] = {cid: v for cid, v in d.items()}

GROUP_TOTAL = {'round17_dev': 94, 'round18_test': 41, 'round1_dev': 93}

final = {}
for anon, m in mapping.items():
    if anon in ARB:
        r = ARB[anon]
        final[anon] = {'direction_reality': r['direction_reality'],
                       'assertions_reality': r['assertions_reality'],
                       'timing_reality': r['timing_reality'],
                       'total': r['total'], 'pass': r['pass'], 'source': 'arbiter'}
    else:
        a, b = A[anon], B[anon]
        tot = round((a['total'] + b['total']) / 2, 3)
        final[anon] = {'direction_reality': (a['direction_reality'] + b['direction_reality']) / 2,
                       'assertions_reality': (a['assertions_reality'] + b['assertions_reality']) / 2,
                       'timing_reality': (a['timing_reality'] + b['timing_reality']) / 2,
                       'total': tot, 'pass': tot >= 4, 'source': 'mean(A,B)'}

with open(f'{DA}/final-axis2-scores.json', 'w') as f:
    json.dump(final, f, ensure_ascii=False, indent=1)

# 双评审一致性（轴二）
agree_pass = sum(1 for anon in A if A[anon]['pass'] == B[anon]['pass'])
tot_ids = list(A)
n = len(tot_ids)
pa = sum(1 for anon in tot_ids if A[anon]['pass']) / n
pb = sum(1 for anon in tot_ids if B[anon]['pass']) / n
po = agree_pass / n
pe = pa * pb + (1 - pa) * (1 - pb)
kappa = (po - pe) / (1 - pe) if pe < 1 else 1.0
exact = sum(1 for anon in tot_ids if A[anon]['total'] == B[anon]['total'])

stats = {'consistency': {'n': n, 'pass_agree': agree_pass, 'pass_agree_rate': round(po, 4),
                         'kappa': round(kappa, 3), 'total_exact_agree': exact,
                         'A_pass': sum(1 for anon in tot_ids if A[anon]['pass']),
                         'B_pass': sum(1 for anon in tot_ids if B[anon]['pass']),
                         'arbitrated': len(ARB)},
         'groups': {}, 'quadrants': {}, 'exceed_master': [], 'replicate_error': []}

for g in GROUP_TOTAL:
    rows = [(anon, m) for anon, m in mapping.items() if m['group'] == g]
    vals = [final[anon] for anon, _ in rows]
    stats['groups'][g] = {
        'n_rated': len(rows), 'n_unrated_B': GROUP_TOTAL[g] - len(rows),
        'axis2_pass': sum(1 for v in vals if v['pass']),
        'axis2_mean': round(sum(v['total'] for v in vals) / len(vals), 3) if vals else None,
        'axis2_mean_pct': round(100 * sum(v['total'] for v in vals) / len(vals) / 6, 1) if vals else None,
    }
    q = Counter()
    for anon, m in rows:
        a1 = axis1[g][m['case_id']]
        a1_pass = a1['pass']
        a2_pass = final[anon]['pass']
        key = ('both_high' if a1_pass and a2_pass else
               'master_only' if a1_pass else
               'reality_only' if a2_pass else 'both_low')
        q[key] += 1
        rec = {'group': g, 'case_id': m['case_id'], 'axis1_total': a1['total'],
               'axis2_total': final[anon]['total']}
        if not a1_pass and a2_pass:
            stats['exceed_master'].append(rec)
        if a1_pass and not a2_pass:
            stats['replicate_error'].append(rec)
    stats['quadrants'][g] = dict(q)

# 最终系统口径（R17 dev + R18 test 合并的四象限）
q = Counter()
for g in ('round17_dev', 'round18_test'):
    q.update(stats['quadrants'][g])
stats['quadrants']['final_system_pooled'] = dict(q)

with open(f'{DA}/stats.json', 'w') as f:
    json.dump(stats, f, ensure_ascii=False, indent=1)
print(json.dumps(stats, ensure_ascii=False, indent=1))
