#!/usr/bin/env python3
"""R39 analysis (analysis role only): merge double-judge scores, platform
reads per R39 PREREG s.3. No method files touched; no git operations.

Platform criteria (R39 PREREG s.3; line values declared in R39 PREREG,
not inherited from R38 verdicts):
- (a) ALL pair_diff >= -1.371
- (b) bazi >= -0.449, bazi-natal >= +0.290, horary >= -0.760,
  liuren dev8 subset >= -2.600 (any break fails (b))
- (c) liuyao dev8 (246): SINGLE round this round. Stands iff single
  pair_diff >= -1.93; < -2.255 registers a fuse fact (report only).
Attribution guardrails (PREREG s.3, separate from platform verdict;
effects apply to later rounds only, never this round's reads):
- bazi-all pair_diff < -0.816 -> BZ-FY falsified/rollback
- liuren merged (dev8+LR3, n=30) pair_diff < -2.550 -> register liuren
  continued-deterioration fact (forces R40 A-layer aggregate diagnosis
  before its preregistration)
Side reads (PREREG s.5): bazi-all / bazi-natal timing sub-item means
R39 vs R38 (same merge logic both rounds).
Segment definitions verbatim from analyze_r38.py (host-meta traditions:
'bazi' = BZ 29, '八字' = natal 26, dev8 subsets via master-baseline-dev8).
Outcome source: R39 judging/outcome-manifest.json (verbatim carry-over
of R38 per PREREG s.0).
Note: R39 predictions carry no systems_used field (fields are case_id /
prediction_text / basis / confidence / trigger); the systems_used count
from analyze_r38.py is therefore omitted by design, trigger counts kept.
holdout16 was not built (PREREG s.4.2 count gate failed by 1 case), so
per PREREG s.3 the platform verdict is registration-only this round.
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R39 = P3 / 'runs/round39'
R38 = P3 / 'runs/round38'
JD = R39 / 'judging'


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
json.dump(final, open(R39 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
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
print('(b) liuren dev8:', g_liuren8, '>= -2.600 ->', g_liuren8['pair_diff'] >= -2.600)
plat_b = (g_bazi['pair_diff'] >= -0.449 and g_natal['pair_diff'] >= 0.290
          and g_horary['pair_diff'] >= -0.760 and g_liuren8['pair_diff'] >= -2.600)

print('\n== 3. (c) liuyao dev8: SINGLE round (PREREG s.3) ==')
c39 = seg(liuyao8, ours, master)
plat_c = c39['pair_diff'] >= -1.93
fuse_fact = c39['pair_diff'] < -2.255
print('R39 single:', c39)
print('(c) STANDS (single >= -1.93):', plat_c, '| fuse fact (< -2.255):', fuse_fact)

print('\n== 4. liuren family reads (platform run, report-only) ==')
print('dev8 clan(18):', seg(liuren8, ours, master))
print('LR3 clan(12):', seg(lr3_ids, ours, master))
print('merged(30):', seg(liuren_all, ours, master))

print('\n== 5. overlay 16 ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
print('overlay16 mean pair:', round(sum(ours[c] - master[c]['total'] for c in ov_ids) / 16, 3))

print('\n== 6. prediction meta ==')
trig = Counter()
npred = 0
for f in glob.glob(str(R39 / 'predictions/*.json')):
    p = json.load(open(f))
    npred += 1
    for k in ('changed_main', 'reserve_used', 'disputed'):
        if p.get('trigger', {}).get(k):
            trig[k] += 1
print('predictions read:', npred, '(no systems_used field this round; count omitted by design)')
print('trigger true counts:', {k: trig[k] for k in ('changed_main', 'reserve_used', 'disputed')})

print('\n== 7. attribution guardrails (PREREG s.3; later rounds only) ==')
lr_merged = seg(liuren_all, ours, master)
bz_guard_fail = g_bazi['pair_diff'] < -0.816
lr_guard_fact = lr_merged['pair_diff'] < -2.550
print('bazi all:', g_bazi['pair_diff'], '< -0.816 -> BZ-FY falsified/rollback:', bz_guard_fail)
print('liuren merged:', lr_merged['pair_diff'], '< -2.550 -> liuren continued-deterioration fact:', lr_guard_fact)

print('\n== 8. side reads: bazi timing movement R38 -> R39 ==')
JD38 = R38 / 'judging'
hmap38 = json.load(open(JD38 / 'host-mapping.json'))
jx38 = json.load(open(JD38 / 'judgeX-merged.json'))
jy38 = json.load(open(JD38 / 'judgeY-merged.json'))
try:
    arb38 = load_jsonl(JD38 / 'arbitration.jsonl')
except FileNotFoundError:
    arb38 = {}
_, sub38 = merge_views(jx38, jy38, arb38, hmap38)
for label, ids in (('bazi-all(29)', by_trad('bazi')), ('bazi-natal(26)', by_trad('八字'))):
    t39 = sum(ours_sub[c]['timing'] for c in ids) / len(ids)
    t38 = sum(sub38[c]['timing'] for c in ids) / len(ids)
    print(f'{label}: timing mean R39 {t39:.3f} vs R38 {t38:.3f} | delta {t39 - t38:+.3f} '
          f'(paired total diff this round in seg reads above)')

plat_a = s_all['pair_diff'] >= -1.371
print('\n== PLATFORM ==')
print('(a)', plat_a, '| (b)', plat_b, '| (c)', plat_c, '| ALL STAND:', plat_a and plat_b and plat_c)
print('NOTE: holdout16 was not built (PREREG s.4.2 count gate); platform verdict is registration-only, no opening (PREREG s.3).')

print('\n== SUMMARY ==')
print(json.dumps({'platform_a': plat_a, 'platform_b': plat_b, 'platform_c': plat_c,
                  'platform_all': plat_a and plat_b and plat_c,
                  'a_pair_diff': s_all['pair_diff'], 'c_single_r39': c39['pair_diff'],
                  'c_fuse_fact': fuse_fact,
                  'guardrail_bz_rollback': bz_guard_fail,
                  'guardrail_lr_deterioration_fact': lr_guard_fact},
                 ensure_ascii=False))
