#!/usr/bin/env python3
"""Merge dev9 baseline judging (host tooling). Mirrors dev8 build rules:
dual judges; divergence = pass mismatch or |(claims+timing)A-(claims+timing)B|>=2
-> arbitration; else item means. Writes disputes.json on first pass; after
arbitration.jsonl exists, writes part-new.jsonl + master-baseline-dev9.json.
"""
import json, os

P3 = 'benchmark/phase3'
D = f'{P3}/data/dev9-baseline-build'

def load_jsonl(p):
    d = {}
    if os.path.exists(p):
        for l in open(p, encoding='utf-8'):
            if l.strip():
                r = json.loads(l); d[r['anon_id']] = r
    return d

key = json.load(open(f'{D}/host-key.json', encoding='utf-8'))
A, B = {}, {}
for part in ('part1', 'part2'):
    A.update(load_jsonl(f'{D}/judgeA-{part}.jsonl'))
    B.update(load_jsonl(f'{D}/judgeB-{part}.jsonl'))
ARB = load_jsonl(f'{D}/arbitration.jsonl')

disputes, final = [], {}
for anon, cid in key.items():
    if anon not in A or anon not in B:
        print('MISSING', anon, cid); continue
    a, b = A[anon], B[anon]
    need = abs((a['claims'] + a['timing']) - (b['claims'] + b['timing'])) >= 2 or a['pass'] != b['pass']
    if need and anon not in ARB:
        disputes.append(anon); continue
    if anon in ARB:
        r = ARB[anon]
        final[cid] = {k: float(r[k]) for k in ('direction', 'claims', 'timing', 'total')}
    else:
        final[cid] = {k: (a[k] + b[k]) / 2 for k in ('direction', 'claims', 'timing', 'total')}

if disputes:
    json.dump(disputes, open(f'{D}/disputes.json', 'w', encoding='utf-8'))
    print('DISPUTES:', len(disputes), disputes); raise SystemExit

with open(f'{D}/part-new.jsonl', 'w', encoding='utf-8') as f:
    for cid in sorted(final):
        f.write(json.dumps({'id': cid, **final[cid]}, ensure_ascii=False) + '\n')
base = json.load(open(f'{P3}/data/master-baseline-dev8.json', encoding='utf-8'))
for cid, v in final.items():
    base[cid] = {'src': 'dev9-baseline-build', 'total': v['total']}
json.dump(base, open(f'{P3}/data/master-baseline-dev9.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = [v['total'] for v in final.values()]
print('new baselines:', len(final), 'master mean %.3f' % (sum(tot) / len(tot)),
      'pass', sum(1 for t in tot if t >= 4), '/', len(tot),
      '| dev9 baseline total entries:', len(base))
