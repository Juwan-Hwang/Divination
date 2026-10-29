#!/usr/bin/env python3
"""R28 preregistered analysis: DiD for inputs9 effect + platform criteria.
Reads runs/round28/final-scores.json (merge_scores output), host-meta,
master-baseline-dev9.json. Anchors per PREREG.md (R24/R25 same-method means).
"""
import json, math
from pathlib import Path

P3 = Path('benchmark/phase3')
fs = json.load(open(P3 / 'runs/round28/final-scores.json'))
meta = json.load(open(P3 / 'runs/round28/judging/host-meta.json'))
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
            'W/T/L': f'{w}/{t}/{l}'}

def by_trad(tr, pool=None):
    return [c for c in ours if meta[c]['tradition'] == tr and (pool is None or c in pool)]

all_ids = sorted(ours)
dev8_ids = sorted(c for c in all_ids if c in json.load(open(P3 / 'data/master-baseline-dev8.json')))
new_ids = sorted(set(all_ids) - set(dev8_ids))
switched = sorted(p.stem for p in (P3 / 'inputs9').glob('*.json'))
liuyao8 = by_trad('liuyao', set(dev8_ids))
ctl = sorted(c for c in liuyao8 if c not in switched)

print('== headline ==')
print('ALL(487):', seg(all_ids))
print('dev8 subset(412):', seg(dev8_ids))
print('== DiD (PREREG s.2) ==')
s_sw = seg(switched); s_ctl = seg(ctl)
print('switched47 R28:', s_sw, '| anchor -1.774 -> delta_sw = %.3f' % (s_sw['pair_diff'] + 1.774))
print('control199 R28:', s_ctl, '| anchor -1.829 -> delta_ctl = %.3f' % (s_ctl['pair_diff'] + 1.829))
print('INPUT EFFECT (DiD) = %.3f' % ((s_sw['pair_diff'] + 1.774) - (s_ctl['pair_diff'] + 1.829)))
import re
rep = open(P3 / 'inputs9/BUILD-REPORT.md', encoding='utf-8').read()
sec = rep.split('## 任务一')[1].split('\n## ')[0]
core14 = sorted(set(re.findall(r'\b(?:LY|YY2|YY|WP|MP)-\d+\b', sec)))
print('C-core (inputs9 BUILD-REPORT task-1 section, n=%d):' % len(core14), seg([c for c in core14 if c in switched]))
print('== platform (PREREG s.3) ==')
print('(a) ALL >= -1.371:', seg(all_ids)['pair_diff'])
print('(b) bazi (n=29) thr -0.449:', seg(by_trad('bazi')))
print('(b) bazi-natal label 八字 (n=26) thr +0.290:', seg(by_trad('八字')))
print('(b) horary (n=25) thr -0.760:', seg(by_trad('horary')))
liuren_all = [c for c in all_ids if meta[c]['tradition'] in ('liuren', '六壬')]
liuren8 = [c for c in liuren_all if c in set(dev8_ids)]
print('(b) liuren dev8 (liuren+六壬 labels):', seg(liuren8), 'thr -2.031')
print('(c) liuyao dev8 (tradition==liuyao, n should be 246):', seg(liuyao8), 'thr -1.93')
cn6 = [c for c in dev8_ids if meta[c]['tradition'] == '六爻']
print('attached: dev8 cases labeled 六爻 (not in the 246):', seg(cn6))
print('attached: liuyao246 + 六爻16 union:', seg(sorted(set(liuyao8) | set(cn6))))
print('== attached reads ==')
print('liuren merged (dev9):', seg(by_trad('liuren')))
print('liuren merged minus LR-001:', seg([c for c in by_trad('liuren') if c != 'LR-001']))
src = {}
for c in new_ids:
    src.setdefault(meta[c].get('source') or '?', []).append(c)
print('new75 by meta source:', {k: len(v) for k, v in src.items()})
ym = [c for c in new_ids if c.startswith('YM-')]
dt = [c for c in new_ids if c.startswith('DT-')]
lr3 = [c for c in new_ids if c.startswith('LR3-')]
print('YM new:', seg(ym)); print('DT new (medium):', seg(dt)); print('LR3 new:', seg(lr3))
print('traditions dev9:', {t: seg(by_trad(t)) for t in sorted({meta[c]['tradition'] for c in all_ids})})
low = [c for c in all_ids if meta[c]['contamination'] == 'low']
print('low-contamination subset:', seg(low))
