#!/usr/bin/env python3
"""主持角分歧筛查：按预注册口径找出轴二双评审分歧例并组仲裁包。
分歧定义：（断语+应期两项之和两评审相差 ≥2）或轴二通过判定不一致。"""
import json, os

ROOT = os.path.expanduser('~/workspace/divination')
DA = f'{ROOT}/benchmark/dual-axis'

def load_jsonl(p):
    return {json.loads(l)['anon_id']: json.loads(l) for l in open(p) if l.strip()}

A = load_jsonl(f'{DA}/judging/judgeA-scores.jsonl')
B = load_jsonl(f'{DA}/judging/judgeB-scores.jsonl')
assert set(A) == set(B), '两评审 anon_id 集合不一致'
packet = {p['anon_id']: p for p in json.load(open(f'{DA}/packets/judge-packet.json'))}
assert set(A) == set(packet), '评审与包 anon_id 集合不一致'

divergent = []
for anon in sorted(A):
    a, b = A[anon], B[anon]
    s_a = a['assertions_reality'] + a['timing_reality']
    s_b = b['assertions_reality'] + b['timing_reality']
    if abs(s_a - s_b) >= 2 or a['pass'] != b['pass']:
        divergent.append({
            'anon_id': anon,
            'prediction': packet[anon]['prediction'],
            'outcome_record': packet[anon]['outcome_record'],
            'judgeA': {k: a[k] for k in ('direction_reality', 'assertions_reality', 'timing_reality', 'total', 'pass', 'note')},
            'judgeB': {k: b[k] for k in ('direction_reality', 'assertions_reality', 'timing_reality', 'total', 'pass', 'note')},
        })

with open(f'{DA}/judging/arbiter-packet.json', 'w') as f:
    json.dump(divergent, f, ensure_ascii=False, indent=1)
with open(f'{DA}/judging/divergent-cases.json', 'w') as f:
    json.dump([d['anon_id'] for d in divergent], f, ensure_ascii=False)
print(f'双评审各 {len(A)} 条；分歧 {len(divergent)} 例：', [d['anon_id'] for d in divergent])
