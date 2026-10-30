#!/usr/bin/env python3
"""R35 analysis (analysis role only): merge double-judge scores, platform
reads per R35 PREREG s.2. No method files touched; no git operations.

Platform criteria (R35 PREREG s.2; line values restated from R33 s.2):
- (a) ALL pair_diff >= -1.371
- (b) bazi >= -0.449, bazi-natal >= +0.290, horary >= -0.760,
  liuren dev8 subset >= -2.593
- (c) liuyao dev8 (246): NEW-CALIBER single-round only (pooling reset at
  R35; R33/R34 pooled conclusions NOT invoked). Stands iff R35 single
  pair_diff >= -1.93. Single < -2.255 is recorded as a fuse fact for the
  new pooling pool (R35 = pool round 1); it voids nothing this round.
Outputs: runs/round35/final-scores.json + stdout.
Segment definitions verbatim from analyze_r34.py (host-meta traditions:
'bazi' = BZ 29, '八字' = natal 26, dev8 subsets via master-baseline-dev8).
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R35 = P3 / 'runs/round35'
JD = R35 / 'judging'


def load_jsonl(path):
    out = {}
    for line in open(path):
        line = line.strip()
        if line:
            r = json.loads(line)
            out[r['anon_id']] = r
    return out


def merge_views(jx, jy, arb, hmap):
    out, out_sub = {}, {}
    for anon in hmap:
        x, y = jx[anon], jy[anon]
        if abs(x['total'] - y['total']) >= 3:
            a = arb[anon]
            rec = {k: float(a[k]) for k in ('direction', 'claims', 'timing', 'total')}
        else:
            rec = {k: (x[k] + y[k]) / 2 for k in ('direction', 'claims', 'timing', 'total')}
        cid = hmap[anon]['case_id'] if isinstance(hmap[anon], dict) else hmap[anon]
        out[cid] = rec['total']
        out_sub[cid] = rec
    return out, out_sub


def seg(ids, scores, base):
    ids = sorted(c for c in ids if c in scores and c in base)
    pair = [scores[c] - base[c]['total'] for c in ids]
    n = len(pair)
    mean = sum(pair) / n
    se = (math.sqrt(sum((x - mean) ** 2 for x in pair) / (n - 1)) / math.sqrt(n)) if n > 1 else 0.0
    w = sum(1 for x in pair if x > 0); t = sum(1 for x in pair if x == 0); l = n - w - t
    return {'n': n, 'pair_diff': round(mean, 3), 'SE': round(se, 3),
            'ours_mean': round(sum(scores[c] for c in ids) / n, 3),
            'master_mean': round(sum(base[c]['total'] for c in ids) / n, 3),
            'W': w, 'T': t, 'L': l, 'W/T/L': f'{w}/{t}/{l}'}


def mean_se(vals):
    n = len(vals)
    m = sum(vals) / n
    se = (math.sqrt(sum((x - m) ** 2 for x in vals) / (n - 1)) / math.sqrt(n)) if n > 1 else 0.0
    return round(m, 3), round(se, 3)


# ---------------- platform ----------------
master = json.load(open(P3 / 'data/master-baseline-dev9.json'))
master8 = json.load(open(P3 / 'data/master-baseline-dev8.json'))
meta = json.load(open(JD / 'host-meta.json'))
hmap = json.load(open(JD / 'host-mapping.json'))
judgeX = json.load(open(JD / 'judgeX-merged.json'))
judgeY = json.load(open(JD / 'judgeY-merged.json'))
try:
    arbitration = load_jsonl(JD / 'arbitration.jsonl')
except FileNotFoundError:
    arbitration = {}
disputes = json.load(open(JD / 'disputes.json'))
computed = sorted(hmap[a] for a in hmap if abs(judgeX[a]['total'] - judgeY[a]['total']) >= 3)
assert computed == sorted(d['case_id'] for d in disputes), (computed, disputes)
if computed:
    assert set(arbitration) == {a for a in hmap if hmap[a] in computed}, 'arbitration coverage'
ours, ours_sub = merge_views(judgeX, judgeY, arbitration, hmap)
assert len(ours) == 487 and set(ours) == set(master) == set(meta)

all_ids = sorted(ours)
final = {'ours_axis2': {c: ours[c] for c in all_ids},
         'ours_sub': {c: ours_sub[c] for c in all_ids}}
json.dump(final, open(R35 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
print('final-scores.json written: n =', len(ours), '| disputes:', computed)


def by_trad(tr, pool=None):
    return [c for c in all_ids if meta[c]['tradition'] == tr and (pool is None or c in pool)]


dev8_set = set(c for c in all_ids if c in master8)
low_ids = [c for c in all_ids if meta[c]['contamination'] == 'low']
liuyao8 = by_trad('liuyao', dev8_set)
liuren_all = [c for c in all_ids if meta[c]['tradition'] in ('liuren', '六壬')]
liuren8 = [c for c in liuren_all if c in dev8_set]
lr3_ids = [c for c in liuren_all if c not in dev8_set]

print('\n== 1. headline ==')
s_all = seg(all_ids, ours, master)
print('ALL(487):', s_all, '| (a) >= -1.371 ->', s_all['pair_diff'] >= -1.371)
print('low-contamination:', seg(low_ids, ours, master))
print('ours pass:', sum(1 for c in all_ids if ours[c] >= 4), '/', len(all_ids))

print('\n== 2. platform (b) guardrails ==')
g_bazi = seg(by_trad('bazi'), ours, master)
g_natal = seg(by_trad('八字'), ours, master)
g_horary = seg(by_trad('horary'), ours, master)
g_liuren8 = seg(liuren8, ours, master)
print('(b) bazi:', g_bazi, '>= -0.449 ->', g_bazi['pair_diff'] >= -0.449)
print('(b) bazi-natal:', g_natal, '>= +0.290 ->', g_natal['pair_diff'] >= 0.290)
print('(b) horary:', g_horary, '>= -0.760 ->', g_horary['pair_diff'] >= -0.760)
print('(b) liuren dev8:', g_liuren8, '>= -2.593 ->', g_liuren8['pair_diff'] >= -2.593)
plat_b = (g_bazi['pair_diff'] >= -0.449 and g_natal['pair_diff'] >= 0.290
          and g_horary['pair_diff'] >= -0.760 and g_liuren8['pair_diff'] >= -2.593)

print('\n== 3. (c) liuyao dev8: R35 single-round (new-caliber pool round 1) ==')
c35 = seg(liuyao8, ours, master)
fuse_triggered = c35['pair_diff'] < -2.255
plat_c = c35['pair_diff'] >= -1.93
print('R35 single:', c35)
print(f'REGISTER: fuse fact (single < -2.255): {fuse_triggered} '
      f'(recorded for the new pooling pool; voids nothing this round)')
print('(c) STANDS (single >= -1.93):', plat_c)
r34 = json.load(open(P3 / 'runs/round34/final-scores.json'))['ours_axis2']
print('annex (report-only, NOT pooled, no verdict weight) R34 single:',
      seg(liuyao8, r34, master))

print('\n== 4. liuren family reads (platform run, report-only) ==')
print('dev8 clan(18):', seg(liuren8, ours, master), '| R34 -2.097; R33 -1.847; R32 -1.042')
print('LR3 clan(12):', seg(lr3_ids, ours, master), '| R34 -1.250; R33 -2.021')
print('merged(30):', seg(liuren_all, ours, master), '| R34 -1.758; R33 -1.917; R32 -1.100')

print('\n== 5. overlay 16 ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
print('overlay16 mean pair:', round(sum(ours[c] - master[c]['total'] for c in ov_ids) / 16, 3))

print('\n== 6. prediction meta ==')
sys_count, trig = Counter(), Counter()
for f in glob.glob(str(R35 / 'predictions/*.json')):
    p = json.load(open(f))
    for s in p.get('systems_used', []):
        sys_count[s] += 1
    for k in ('changed_main', 'reserve_used', 'disputed'):
        if p.get('trigger', {}).get(k):
            trig[k] += 1
print('systems_used:', dict(sys_count.most_common()))
print('trigger true counts:', {k: trig[k] for k in ('changed_main', 'reserve_used', 'disputed')})

plat_a = s_all['pair_diff'] >= -1.371
print('\n== PLATFORM ==')
print('(a)', plat_a, '| (b)', plat_b, '| (c)', plat_c, '| ALL STAND:', plat_a and plat_b and plat_c)

print('\n== SUMMARY ==')
print(json.dumps({'platform_a': plat_a, 'platform_b': plat_b, 'platform_c': plat_c,
                  'platform_all': plat_a and plat_b and plat_c,
                  'a_pair_diff': s_all['pair_diff'], 'c_single': c35['pair_diff'],
                  'c_fuse_triggered': fuse_triggered},
                 ensure_ascii=False))
