#!/usr/bin/env python3
"""R29 preregistered analysis: main criterion (liuyao dev8 subset) + platform.
Reads runs/round29/final-scores.json (merge_scores output), host-meta,
master-baseline-dev9.json. Criteria per runs/round29/PREREG.md s.3.
"""
import json, math, glob
from pathlib import Path

P3 = Path('benchmark/phase3')
fs = json.load(open(P3 / 'runs/round29/final-scores.json'))
meta = json.load(open(P3 / 'runs/round29/judging/host-meta.json'))
master = json.load(open(P3 / 'data/master-baseline-dev9.json'))
ours = {c: v['total'] if isinstance(v, dict) else v for c, v in fs['ours_axis2'].items()}

def seg(ids):
    ids = [c for c in ids if c in ours and c in master]
    pair = [ours[c] - master[c]['total'] for c in ids]
    n = len(pair)
    mean = sum(pair) / n
    se = (math.sqrt(sum((x - mean) ** 2 for x in pair) / (n - 1)) / math.sqrt(n)) if n > 1 else 0.0
    w = sum(1 for x in pair if x > 0); t = sum(1 for x in pair if x == 0); l = sum(1 for x in pair if x < 0)
    return {'n': n, 'pair_diff': round(mean, 3), 'SE': round(se, 3),
            'ours_mean': round(sum(ours[c] for c in ids) / n, 3),
            'master_mean': round(sum(master[c]['total'] for c in ids) / n, 3),
            'W': w, 'W/T/L': f'{w}/{t}/{l}'}

def by_trad(tr, pool=None):
    return [c for c in ours if meta[c]['tradition'] == tr and (pool is None or c in pool)]

all_ids = sorted(ours)
dev8_ids = sorted(c for c in all_ids if c in json.load(open(P3 / 'data/master-baseline-dev8.json')))
new_ids = sorted(set(all_ids) - set(dev8_ids))
liuyao8 = by_trad('liuyao', set(dev8_ids))

print('== headline ==')
print('ALL(487):', seg(all_ids))
print('dev8 subset(412):', seg(dev8_ids))
print('ours pass:', sum(1 for c in all_ids if ours[c] >= 4), '/', len(all_ids))

print('== MAIN CRITERION (PREREG s.3): liuyao dev8 subset ==')
m = seg(liuyao8)
print('liuyao dev8:', m, '| anchors R28 -1.859 / R27 -1.845 / R26 -2.123 / R25 -1.929 / R24 -1.707')
print('positive-gain test: pair_diff >= -1.45 ->', m['pair_diff'] >= -1.45, '; W >= 46 ->', m['W'] >= 46)
print('falsify test: pair_diff <= -1.82 ->', m['pair_diff'] <= -1.82, '; W <= 44 ->', m['W'] <= 44)

print('== platform (PREREG s.3) ==')
a = seg(all_ids)
print('(a) ALL thr -1.371:', a['pair_diff'], a['pair_diff'] >= -1.371)
print('(b) bazi (n=29) thr -0.449:', seg(by_trad('bazi')))
print('(b) bazi-natal label (n=26) thr +0.290:', seg(by_trad('八字')))
print('(b) horary (n=25) thr -0.760:', seg(by_trad('horary')))
liuren_all = [c for c in all_ids if meta[c]['tradition'] in ('liuren', '六壬')]
liuren8 = [c for c in liuren_all if c in set(dev8_ids)]
print('(b) liuren dev8 (liuren+ labels):', seg(liuren8), 'thr -2.031')
print('(c) liuyao dev8 thr -1.93:', m['pair_diff'], m['pair_diff'] >= -1.93)

print('== attached reads ==')
cn6 = [c for c in dev8_ids if meta[c]['tradition'] == '六爻']
print('dev8 cases labeled (YY系):', seg(cn6))
print('liuyao246 + 16 union (262):', seg(sorted(set(liuyao8) | set(cn6))))
print('liuren merged (dev9, both labels):', seg(liuren_all))
print('liuren merged minus LR-001:', seg([c for c in liuren_all if c != 'LR-001']))
print('LR-001 single:', seg(['LR-001']))
low = [c for c in all_ids if meta[c]['contamination'] == 'low']
print('low-contamination subset:', seg(low))
ym = [c for c in new_ids if c.startswith('YM-')]
dt = [c for c in new_ids if c.startswith('DT-')]
lr3 = [c for c in new_ids if c.startswith('LR3-')]
print('new75: YM(yimao):', seg(ym), '| DT(dty, medium):', seg(dt), '| LR3:', seg(lr3))
print('new75 all:', seg(new_ids))
# R29 adjudication-entry actual invocations in blind predictions
inv = 0; inv_ids = []
for f in glob.glob(str(P3 / 'runs/round29/predictions/*.json')):
    p = json.load(open(f))
    blob = ' '.join(p.get('sources_used', [])) + p.get('basis', '')
    if '裁决（R29）' in blob or '分工条件裁决' in blob:
        inv += 1; inv_ids.append(p['case_id'])
print('predictions invoking R29 adjudication entries (sources_used/basis mention):', inv)
print('traditions dev9:', {t: seg(by_trad(t)) for t in sorted({meta[c]['tradition'] for c in all_ids})})
