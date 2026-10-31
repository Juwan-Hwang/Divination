#!/usr/bin/env python3
"""R89 analysis (analysis role only): merge double-judge scores, platform
reads per R89 PREREG s.1. No method files touched; no score changed;
no git operations. Merge/seg logic copied verbatim in method from
analyze_r49.py (same merge_views / seg formulas and segment definitions).

Platform criteria (R89 PREREG s.1, line values carried verbatim from
R64 PREREG s.1 via R65-R88 execution, numerically identical):
- (a) ALL pair_diff >= -1.371
- (b) bazi >= -0.449, bazi-natal >= +0.290, horary >= -0.760,
  liuren dev8 subset >= -2.600 (any break fails (b))
- (c) liuyao dev8 (246): SINGLE round this round. Stands iff single
  pair_diff >= -1.93; < -2.255 registers a fuse fact (report only).
Attribution guardrails (R89 PREREG s.1, separate from platform verdict):
- bazi-all pair_diff < -0.816 -> BZ-FY falsified
- liuren merged (dev8+LR3, n=30) pair_diff < -2.550 -> register liuren
  continued-deterioration fact
Arbitration rule: per analyze_r39.py merge_views code rule, when
|X.total - Y.total| >= 3 the arbitration record REPLACES the
double-view mean (all four sub-scores). Applied as in R40.
Segment definitions verbatim from analyze_r39/r40 (host-meta
traditions: 'bazi' = BZ 29, '八字' = natal 26, dev8 subsets via
master-baseline-dev8; liuren family = traditions 'liuren' + '六壬').
Side reads: bazi-all / bazi-natal timing sub-item means R89 vs R88
(R88 baseline taken from runs/round88/final-scores.json side-read
values; no other-round judging/predictions opened), overlay-16 mean
pair diff, trigger counts recomputed from runs/round89/predictions/,
double-view |Delta| distribution, mengzhan chapter variable footprint
recomputed on round89 predictions (s.9b mechanism of R49), and the
liuren negative-case list for the W-monitoring seat
(diagnosis/lr-negatives-dev89.json).
final-scores.json keeps the R39 structure (ours_axis2 / ours_sub) and
adds an analysis_r89 section carrying every read with n and SE.
Assertions: 487-case full coverage, double-view key sets equal,
trigger recount equals host_expected.
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R88D = P3 / 'runs/round89'
PREV_FINAL = P3 / 'runs/round88/final-scores.json'
JD = R88D / 'judging'


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
assert set(judgeX) == set(judgeY) == set(hmap), 'double-view / host-mapping key sets differ'
assert len(judgeX) == 487, 'judge coverage != 487'
try:
    arbitration = load_jsonl(JD / 'arbitration-scores.jsonl')
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


def by_trad(tr, pool=None):
    return [c for c in all_ids if meta[c]['tradition'] == tr and (pool is None or c in pool)]


dev8_set = set(c for c in all_ids if c in master8)
low_ids = [c for c in all_ids if meta[c]['contamination'] == 'low']
liuyao8 = by_trad('liuyao', dev8_set)
liuren_all = [c for c in all_ids if meta[c]['tradition'] in ('liuren', '六壬')]
liuren8 = [c for c in liuren_all if c in dev8_set]
lr3_ids = [c for c in liuren_all if c not in dev8_set]

print('== 0. merge ==')
print('disputes (|dTotal|>=3):', computed, '| arbitration applied (replaces mean):',
      {c: arbitration[[a for a in hmap if hmap[a] == c][0]]['total'] for c in computed})

print('\n== 1. headline ==')
s_all = seg(all_ids, ours, master)
s_low = seg(low_ids, ours, master)
print('ALL(487):', s_all, '| (a) >= -1.371 ->', s_all['pair_diff'] >= -1.371)
print('low-contamination:', s_low)
print('ours pass:', sum(1 for c in all_ids if ours[c] >= 4), '/', len(all_ids))

print('\n== 2. platform (b) guardrails ==')
g_bazi = seg(by_trad('bazi'), ours, master)
g_natal = seg(by_trad('八字'), ours, master)
g_horary = seg(by_trad('horary'), ours, master)
g_liuren8 = seg(liuren8, ours, master)
print('(b) bazi:', g_bazi, '>= -0.449 ->', g_bazi['pair_diff'] >= -0.449,
      '| margin', round(g_bazi['pair_diff'] - (-0.449), 3))
print('(b) bazi-natal:', g_natal, '>= +0.290 ->', g_natal['pair_diff'] >= 0.290,
      '| margin', round(g_natal['pair_diff'] - 0.290, 3))
print('(b) horary:', g_horary, '>= -0.760 ->', g_horary['pair_diff'] >= -0.760,
      '| margin', round(g_horary['pair_diff'] - (-0.760), 3))
print('(b) liuren dev8:', g_liuren8, '>= -2.600 ->', g_liuren8['pair_diff'] >= -2.600,
      '| margin', round(g_liuren8['pair_diff'] - (-2.600), 3))
plat_b = (g_bazi['pair_diff'] >= -0.449 and g_natal['pair_diff'] >= 0.290
          and g_horary['pair_diff'] >= -0.760 and g_liuren8['pair_diff'] >= -2.600)

print('\n== 3. (c) liuyao dev8: SINGLE round (PREREG s.1) ==')
c44 = seg(liuyao8, ours, master)
plat_c = c44['pair_diff'] >= -1.93
fuse_fact = c44['pair_diff'] < -2.255
print('R89 single:', c44)
print('(c) STANDS (single >= -1.93):', plat_c, '| fuse fact (< -2.255):', fuse_fact)

print('\n== 4. family reads ==')
fam = {}
fam['liuyao_dev8_c_segment'] = c44
fam['liuyao_all'] = seg(by_trad('liuyao'), ours, master)
fam['liuyao_zh'] = seg(by_trad('六爻'), ours, master)
fam['liuyao_combined'] = seg([c for c in all_ids if meta[c]['tradition'] in ('liuyao', '六爻')], ours, master)
fam['liuren_dev8'] = g_liuren8
fam['liuren_lr3_new'] = seg(lr3_ids, ours, master)
fam['liuren_merged'] = seg(liuren_all, ours, master)
fam['liuren_en'] = seg(by_trad('liuren'), ours, master)
fam['liuren_zh'] = seg(by_trad('六壬'), ours, master)
fam['bazi_all'] = g_bazi
fam['bazi_natal'] = g_natal
fam['horary'] = g_horary
fam['meihua_en'] = seg(by_trad('meihua'), ours, master)
fam['meihua_zh'] = seg(by_trad('梅花'), ours, master)
fam['meihua_merged'] = seg([c for c in all_ids if meta[c]['tradition'] in ('meihua', '梅花')], ours, master)
cezi_ids = [c for c in all_ids if '测字' in meta[c]['tradition']]
fam['cezi_dev'] = seg(cezi_ids, ours, master) if cezi_ids else None
for k, v in fam.items():
    print(k, ':', v, ('| ids ' + str(cezi_ids)) if k == 'cezi_dev' else '')
per_trad = {}
for tr in sorted(set(meta[c]['tradition'] for c in all_ids)):
    per_trad[tr] = seg(by_trad(tr), ours, master)
print('per-tradition (all):')
for tr, v in per_trad.items():
    print(' ', tr, v)

print('\n== 5. overlay 16 ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
ov_mean = round(sum(ours[c] - master[c]['total'] for c in ov_ids) / 16, 3)
print('overlay16 mean pair:', ov_mean)

print('\n== 6. prediction meta: trigger recount ==')
trig = Counter()
npred = 0
for f in glob.glob(str(R88D / 'predictions/*.json')):
    p = json.load(open(f))
    npred += 1
    for k in ('changed_main', 'reserve_used', 'disputed'):
        if p.get('trigger', {}).get(k):
            trig[k] += 1
trig_counts = {k: trig[k] for k in ('changed_main', 'reserve_used', 'disputed')}
host_expected = {'changed_main': 36, 'reserve_used': 41, 'disputed': 56}  # host freeze verify recount (verify_predictions_host_r89.py, FREEZE-r89); filled by R89 host after freeze verify, before the definitive analyze run
assert host_expected is None or trig_counts == host_expected, (trig_counts, host_expected)
print('predictions read:', npred)
print('trigger true counts:', trig_counts, '| host final check:', host_expected,
      '| match:', (trig_counts == host_expected) if host_expected else 'n/a (host fills host_expected after freeze verify)')

print('\n== 7. double-view consistency ==')
inv = {v: k for k, v in hmap.items()}
deltas = {c: abs(judgeX[inv[c]]['total'] - judgeY[inv[c]]['total']) for c in all_ids}
dist_exact = dict(sorted(Counter(deltas.values()).items()))
dist_bins = {'==0': sum(1 for d in deltas.values() if d == 0),
             '(0,1)': sum(1 for d in deltas.values() if 0 < d < 1),
             '[1,2)': sum(1 for d in deltas.values() if 1 <= d < 2),
             '[2,3)': sum(1 for d in deltas.values() if 2 <= d < 3),
             '>=3 (disputed)': sum(1 for d in deltas.values() if d >= 3)}
print('|dTotal| exact distribution:', dist_exact)
print('|dTotal| bins:', dist_bins)
arb_detail = []
for c in computed:
    a = inv[c]
    arb_detail.append({'case_id': c, 'anon_id': a,
                       'judgeX_total': judgeX[a]['total'], 'judgeY_total': judgeY[a]['total'],
                       'abs_delta': abs(judgeX[a]['total'] - judgeY[a]['total']),
                       'double_view_mean_total': (judgeX[a]['total'] + judgeY[a]['total']) / 2,
                       'arbitration_total': float(arbitration[a]['total']),
                       'final_total': ours[c],
                       'rule': 'arbitration replaces double-view mean (analyze_r39 merge_views code rule)'})
print('arbitration detail:', arb_detail)

print('\n== 8. attribution guardrails (PREREG s.1) ==')
lr_merged = fam['liuren_merged']
bz_guard_fail = g_bazi['pair_diff'] < -0.816
lr_guard_fact = lr_merged['pair_diff'] < -2.550
print('bazi all:', g_bazi['pair_diff'], '< -0.816 -> BZ-FY falsified:', bz_guard_fail)
print('liuren merged:', lr_merged['pair_diff'], '< -2.550 -> liuren continued-deterioration fact:', lr_guard_fact)

print('\n== 9. side reads: bazi timing movement R88 -> R89 ==')
prev_final = json.load(open(PREV_FINAL))
prev_timing = prev_final['analysis_r88']['appendix']['bazi_timing_side_read_vs_r87']
timing_reads = {}
for label, ids in (('bazi-all(29)', by_trad('bazi')), ('bazi-natal(26)', by_trad('八字'))):
    t77 = sum(ours_sub[c]['timing'] for c in ids) / len(ids)
    t76v = prev_timing[label]['timing_mean_r88']
    timing_reads[label] = {'timing_mean_r89': round(t77, 3), 'timing_mean_r88': round(t76v, 3),
                           'delta': round(t77 - t76v, 3), 'n': len(ids)}
    print(f'{label}: timing mean R89 {t77:.3f} vs R88 {t76v:.3f} | delta {t77 - t76v:+.3f}')

print('\n== 9b. side read: mengzhan chapter variable footprint (R49 s.9b mechanism) ==')
mz_cases = []
for f in glob.glob(str(R88D / 'predictions/*.json')):
    p = json.load(open(f))
    blob = (p.get('basis') or '') + '\n' + (p.get('prediction_text') or '')
    if ('梦占' in blob) or ('mengzhan' in blob.lower()):
        mz_cases.append(p['case_id'])
mz_cases.sort()
dream_trad = {tr: sum(1 for c in all_ids if meta[c]['tradition'] == tr)
              for tr in sorted(set(meta[c]['tradition'] for c in all_ids)) if '梦' in tr}
mengzhan_read = {'predictions_citing_mengzhan': mz_cases,
                 'n_citing': len(mz_cases),
                 'dev_traditions_containing_dream_char': dream_trad,
                 'note': ('Footprint side read only; R89 is the first platform point of the post-section-12-disposal series (snapshot differs from the R88 platform snapshot exactly in references/calibration.md, the section-12 disposal registration; section 8 is the only live intervention); holdout32 carries no judgment attribution this round; footprint is a side read only and carries no verdict; the mengzhan chapter effectiveness test still awaits fresh dream cases at acceptance.')}
print('predictions citing mengzhan chapter:', len(mz_cases), mz_cases)
print('dev traditions containing dream char:', dream_trad)

plat_a = s_all['pair_diff'] >= -1.371
print('\n== PLATFORM ==')
print('(a)', plat_a, '| (b)', plat_b, '| (c)', plat_c, '| ALL STAND:', plat_a and plat_b and plat_c)

# ---------------- write final-scores.json (R39 structure + analysis section) ----------------
analysis = {
    'round': 89,
    'prereg_source': 'runs/round89/PREREG.md s.1 (platform lines and attribution guardrails)',
    'arbitration_rule': ('Per analyze_r39.py merge_views code rule, when |X-Y|>=3 the '
                         'arbitration record replaces the double-view mean. Applied per '
                         'judging/arbitration-scores.jsonl when disputes exist.'),
    'headline': {'all': s_all, 'low_contamination': s_low,
                 'ours_pass_ge4': sum(1 for c in all_ids if ours[c] >= 4), 'n': len(all_ids)},
    'families': fam,
    'per_tradition_all': per_trad,
    'platform': {
        'a_all': {'seg': s_all, 'line': -1.371, 'stands': plat_a,
                  'margin': round(s_all['pair_diff'] - (-1.371), 3)},
        'b_guardrails': {
            'bazi_all': {'seg': g_bazi, 'line': -0.449, 'stands': g_bazi['pair_diff'] >= -0.449,
                         'margin': round(g_bazi['pair_diff'] - (-0.449), 3)},
            'bazi_natal': {'seg': g_natal, 'line': 0.290, 'stands': g_natal['pair_diff'] >= 0.290,
                           'margin': round(g_natal['pair_diff'] - 0.290, 3)},
            'horary': {'seg': g_horary, 'line': -0.760, 'stands': g_horary['pair_diff'] >= -0.760,
                       'margin': round(g_horary['pair_diff'] - (-0.760), 3)},
            'liuren_dev8': {'seg': g_liuren8, 'line': -2.600, 'stands': g_liuren8['pair_diff'] >= -2.600,
                            'margin': round(g_liuren8['pair_diff'] - (-2.600), 3)},
            'stands_all': plat_b},
        'c_liuyao_dev8_single': {'seg': c44, 'line': -1.93, 'stands': plat_c,
                                 'margin': round(c44['pair_diff'] - (-1.93), 3),
                                 'fuse_line': -2.255, 'fuse_triggered': fuse_fact},
        'all_stand': plat_a and plat_b and plat_c},
    'guardrails_attribution': {
        'note': 'Separate from platform verdict (R89 PREREG s.1).',
        'bazi_bzfy_falsification': {'seg': g_bazi, 'threshold': -0.816,
                                    'condition': 'pair_diff < -0.816',
                                    'triggered': bz_guard_fail},
        'liuren_continued_deterioration': {'seg': lr_merged, 'threshold': -2.550,
                                           'condition': 'pair_diff < -2.550',
                                           'triggered': lr_guard_fact}},
    'appendix': {
        'trigger_recount': {'n_predictions': npred, 'counts': trig_counts,
                            'host_final_check': host_expected,
                            'match_host': (trig_counts == host_expected) if host_expected else None},
        'double_view_consistency': {'abs_delta_exact_distribution': {str(k): v for k, v in dist_exact.items()},
                                    'abs_delta_bins': dist_bins,
                                    'n_disputed_ge3': len(computed),
                                    'disputed_cases': computed,
                                    'arbitration_detail': arb_detail},
        'overlay16_mean_pair_diff': ov_mean,
        'mengzhan_variable_side_read': mengzhan_read,
        'bazi_timing_side_read_vs_r88': timing_reads},
}
final = {'ours_axis2': {c: ours[c] for c in all_ids},
         'ours_sub': {c: ours_sub[c] for c in all_ids},
         'analysis_r89': analysis}
json.dump(final, open(R88D / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
print('\nfinal-scores.json written: n =', len(ours), '| disputes:', computed)

# ---------------- liuren negatives for W-monitoring seat ----------------
neg = []
for c in liuren_all:
    d = round(ours[c] - master[c]['total'], 3)
    if d < 0:
        neg.append({'case_id': c, 'tradition': meta[c]['tradition'],
                    'in_dev8': c in dev8_set,
                    'ours': ours[c], 'master': master[c]['total'], 'pair_diff': d})
neg.sort(key=lambda r: r['case_id'])
lr_doc = {'round': 89,
          'definition': ("host-meta tradition in ('liuren','六壬'); pair_diff = final ours "
                         "(arbitration-merged) - master-baseline-dev9 total; listed iff < 0"),
          'n_liuren_total': len(liuren_all), 'n_negative': len(neg),
          'negatives': neg}
(R88D / 'diagnosis').mkdir(exist_ok=True)
json.dump(lr_doc, open(R88D / 'diagnosis/lr-negatives-dev89.json', 'w'), ensure_ascii=False, indent=1)
print('lr-negatives-dev89.json written: negatives', len(neg), '/', len(liuren_all))

print('\n== SUMMARY ==')
print(json.dumps({'platform_a': plat_a, 'platform_b': plat_b, 'platform_c': plat_c,
                  'platform_all': plat_a and plat_b and plat_c,
                  'a_pair_diff': s_all['pair_diff'], 'c_single_r89': c44['pair_diff'],
                  'c_fuse_fact': fuse_fact,
                  'guardrail_bz_falsified': bz_guard_fail,
                  'guardrail_lr_deterioration_fact': lr_guard_fact},
                 ensure_ascii=False))
