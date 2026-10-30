#!/usr/bin/env python3
"""R38 analysis (analysis role only): merge double-judge scores, platform
reads per R38 PREREG s.2. No method files touched; no git operations.

Platform criteria (R38 PREREG s.2; line values re-declared in R38 PREREG s.3 (not inherited),
re-declared in R38 PREREG):
- (a) ALL pair_diff >= -1.371
- (b) bazi >= -0.449, bazi-natal >= +0.290, horary >= -0.760,
  liuren dev8 subset >= -2.600
- (c) liuyao dev8 (246): SINGLE round this round (PREREG s.2/s.6 declared
  in advance: the s.6 outcome-hygiene change voids the pooling
  precondition). Stands iff single pair_diff >= -1.93; < -2.255 registers
  a fuse fact (report only).
Attribution guardrails (PREREG s.2, separate from platform verdict;
rollback affects later rounds only, never this round's reads):
- bazi-all pair_diff < -0.617 -> BZ-YN items (s.7) falsified/rollback
- liuren merged (dev8+LR3, n=30) pair_diff < -2.375 -> register LR-QY
  cumulative-deterioration fact (no rollback object this round; R38 must
  respond head-on)
s.7 side reads: bazi-all / bazi-natal timing sub-item means R38 vs R37
(same merge logic both rounds), and bazi per-case paired diffs (in seg).
Segment definitions verbatim from analyze_r36.py (host-meta traditions:
'bazi' = BZ 29, '八字' = natal 26, dev8 subsets via master-baseline-dev8).
Outcome source: R38 judging/outcome-manifest.json (s.6 hygiene applied).
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R38 = P3 / 'runs/round38'
R37 = P3 / 'runs/round37'
JD = R38 / 'judging'


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
json.dump(final, open(R38 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
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

print('\n== 3. (c) liuyao dev8: SINGLE round (PREREG s.2; pooling voided by s.6) ==')
c37 = seg(liuyao8, ours, master)
plat_c = c37['pair_diff'] >= -1.93
fuse_fact = c37['pair_diff'] < -2.255
print('R38 single:', c37)
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
sys_count, trig = Counter(), Counter()
for f in glob.glob(str(R38 / 'predictions/*.json')):
    p = json.load(open(f))
    for s in p.get('systems_used', []):
        sys_count[s] += 1
    for k in ('changed_main', 'reserve_used', 'disputed'):
        if p.get('trigger', {}).get(k):
            trig[k] += 1
print('systems_used:', dict(sys_count.most_common()))
print('trigger true counts:', {k: trig[k] for k in ('changed_main', 'reserve_used', 'disputed')})

print('\n== 7. attribution guardrails (PREREG s.2; later rounds only) ==')
lr_merged = seg(liuren_all, ours, master)
bz_guard_fail = g_bazi['pair_diff'] < -0.816
lr_guard_fact = lr_merged['pair_diff'] < -2.183
print('bazi all:', g_bazi['pair_diff'], '< -0.816 -> BZ-FY falsified/rollback:', bz_guard_fail)
print('liuren merged:', lr_merged['pair_diff'], '< -2.183 -> liuren continued-deterioration fact:', lr_guard_fact)

print('\n== 8. s.7 side reads: bazi timing movement R37 -> R38 ==')
JD36 = R37 / 'judging'  # comparison baseline: R37 (PREREG s.5)
hmap36 = json.load(open(JD36 / 'host-mapping.json'))
jx36 = json.load(open(JD36 / 'judgeX-merged.json'))
jy36 = json.load(open(JD36 / 'judgeY-merged.json'))
try:
    arb36 = load_jsonl(JD36 / 'arbitration.jsonl')
except FileNotFoundError:
    arb36 = {}
_, sub36 = merge_views(jx36, jy36, arb36, hmap36)
for label, ids in (('bazi-all(29)', by_trad('bazi')), ('bazi-natal(26)', by_trad('八字'))):
    t37 = sum(ours_sub[c]['timing'] for c in ids) / len(ids)
    t36 = sum(sub36[c]['timing'] for c in ids) / len(ids)
    print(f'{label}: timing mean R38 {t37:.3f} vs R37 {t36:.3f} | delta {t37 - t36:+.3f} '
          f'(paired total diff this round in seg reads above)')

plat_a = s_all['pair_diff'] >= -1.371
print('\n== PLATFORM ==')
print('(a)', plat_a, '| (b)', plat_b, '| (c)', plat_c, '| ALL STAND:', plat_a and plat_b and plat_c)
print('NOTE: no sealed set exists to open this round (PREREG s.3); platform verdict is registration-only.')

print('\n== SUMMARY ==')
print(json.dumps({'platform_a': plat_a, 'platform_b': plat_b, 'platform_c': plat_c,
                  'platform_all': plat_a and plat_b and plat_c,
                  'a_pair_diff': s_all['pair_diff'], 'c_single_r38': c37['pair_diff'],
                  'c_fuse_fact': fuse_fact,
                  'guardrail_bz_rollback': bz_guard_fail,
                  'guardrail_lr_deterioration_fact': lr_guard_fact},
                 ensure_ascii=False))
