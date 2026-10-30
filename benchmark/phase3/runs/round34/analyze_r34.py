#!/usr/bin/env python3
"""R34 analysis (analysis role only): merge double-judge scores, platform
reads per PREREG s.2, pooled (c) with R33, and the liuren diagnostic
contrast per PREREG s.1. No method files touched; no git operations.

Platform criteria (PREREG s.2, restated R33 lines):
- (a) ALL pair_diff >= -1.371
- (b) bazi >= -0.449, bazi-natal >= +0.290, horary >= -0.760,
  liuren dev8 subset >= -2.593
- (c) liuyao dev8 (246): pooled R33+R34 pair_diff >= -1.93, fuse: R34
  single-round < -2.255 voids pooling (then single-round >= -1.93 only).

Diagnostic (PREREG s.1): per case Delta = pair_FULL - pair_CORE vs the
same master baseline; bands at +/-0.50 on Delta_merged with clan signs.
Outputs: runs/round34/final-scores.json + diag-scores.json + stdout.
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R34 = P3 / 'runs/round34'
JD = R34 / 'judging'


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
json.dump(final, open(R34 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
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

print('\n== 3. (c) liuyao dev8: single + pooled with R33 ==')
r33 = json.load(open(P3 / 'runs/round33/final-scores.json'))['ours_axis2']
c34 = seg(liuyao8, ours, master)
c33 = seg(liuyao8, r33, master)
pooled_vals = ([ours[c] - master[c]['total'] for c in liuyao8]
               + [r33[c] - master[c]['total'] for c in liuyao8])
pm, pse = mean_se(pooled_vals)
fuse_ok = c34['pair_diff'] >= -2.255
pooled_stand = fuse_ok and pm >= -1.93
single_stand = c34['pair_diff'] >= -1.93
plat_c = pooled_stand if fuse_ok else single_stand
print('R34 single:', c34)
print('R33 single (recorded):', c33)
print(f'pooled R33+R34: mean {pm} SE {pse} (n=492 obs) | fuse ok: {fuse_ok} '
      f'| pooled >= -1.93 -> {pm >= -1.93} | (c) STANDS: {plat_c}')

print('\n== 4. liuren family reads (platform run, report-only) ==')
print('dev8 clan(18):', seg(liuren8, ours, master), '| R33 -1.847; R32 -1.042')
print('LR3 clan(12):', seg(lr3_ids, ours, master), '| R33 -2.021')
print('merged(30):', seg(liuren_all, ours, master), '| R33 -1.917; R32 -1.100')

print('\n== 5. overlay 16 ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
print('overlay16 mean pair:', round(sum(ours[c] - master[c]['total'] for c in ov_ids) / 16, 3))

print('\n== 6. prediction meta ==')
sys_count, trig = Counter(), Counter()
for f in glob.glob(str(R34 / 'predictions/*.json')):
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

# ---------------- liuren diagnostic ----------------
print('\n== 7. liuren diagnostic (PREREG s.1) ==')
dmap = json.load(open(JD / 'host-diag-mapping.json'))
dX = json.load(open(JD / 'judgeX-merged-diag.json'))
dY = json.load(open(JD / 'judgeY-merged-diag.json'))
try:
    darb = load_jsonl(JD / 'arbitration-diag.jsonl')
except FileNotFoundError:
    darb = {}
ddisputes = json.load(open(JD / 'disputes-diag.json'))
dcomputed = sorted(a for a in dmap if abs(dX[a]['total'] - dY[a]['total']) >= 3)
assert dcomputed == sorted(d['anon_id'] for d in ddisputes), (dcomputed, ddisputes)
if dcomputed:
    assert set(darb) == set(dcomputed), 'diag arbitration coverage'
scores = {}  # (case, arm) -> total, merged per anon (arms share case_id: key by anon first)
for anon, ref in dmap.items():
    x, y = dX[anon], dY[anon]
    if abs(x['total'] - y['total']) >= 3:
        total = float(darb[anon]['total'])
    else:
        total = (x['total'] + y['total']) / 2
    scores[(ref['case_id'], ref['arm'])] = total
batches = json.load(open(R34 / 'batches-diag.json'))
clans = batches['_clans']
rows = []
for cid in sorted({c for c, _ in scores}):
    pf = scores[(cid, 'full')] - master[cid]['total']
    pc = scores[(cid, 'core')] - master[cid]['total']
    clan = 'dev8' if cid in clans['dev8'] else 'lr3'
    rows.append({'case_id': cid, 'clan': clan, 'full': scores[(cid, 'full')],
                 'core': scores[(cid, 'core')], 'master': master[cid]['total'],
                 'pair_full': round(pf, 3), 'pair_core': round(pc, 3),
                 'delta': round(pf - pc, 3)})
json.dump(rows, open(R34 / 'diag-scores.json', 'w'), ensure_ascii=False, indent=1)


def dstats(sub):
    dm, dse = mean_se([r['delta'] for r in sub])
    fm, fse = mean_se([r['pair_full'] for r in sub])
    cm, cse = mean_se([r['pair_core'] for r in sub])
    return {'n': len(sub), 'pair_full': fm, 'pair_full_SE': fse,
            'pair_core': cm, 'pair_core_SE': cse, 'delta': dm, 'delta_SE': dse}


d_all = dstats(rows)
d_dev8 = dstats([r for r in rows if r['clan'] == 'dev8'])
d_lr3 = dstats([r for r in rows if r['clan'] == 'lr3'])
print('merged(30):', d_all)
print('dev8 clan(18):', d_dev8)
print('LR3 clan(12):', d_lr3)
dm = d_all['delta']
same_sign_neg = d_dev8['delta'] < 0 and d_lr3['delta'] < 0
same_sign_pos = d_dev8['delta'] > 0 and d_lr3['delta'] > 0
if d_dev8['delta'] * d_lr3['delta'] < 0:
    verdict = 'CLAN SIGNS DIVERGE: report by clan only, no merged conclusion'
elif dm <= -0.50 and same_sign_neg:
    verdict = 'EXPANSION-CAUSED DROP SUPPORTED (dilution/conflict): disposition to R35 prereg via revision role'
elif dm >= 0.50 and same_sign_pos:
    verdict = 'EXPANSION BENEFICIAL: R33 drop attributed to seat/sampling variance'
elif abs(dm) < 0.50:
    verdict = 'UNRESOLVED at this resolution: sampling variance not excluded; chapter unchanged'
else:
    verdict = 'MIXED: merged band crossed but clan signs not aligned; report only'
print('DIAGNOSTIC VERDICT (PREREG s.1 bands):', verdict)

r32 = json.load(open(P3 / 'runs/round32/final-scores.json'))['ours_axis2']
diag30 = sorted({c for c, _ in scores})
print('annex FULL arm vs R33 platform same cases:',
      seg(diag30, {c: scores[(c, 'full')] for c in diag30}, master),
      '| R33 platform:', seg(diag30, r33, master))
print('annex CORE arm vs R32 platform same cases:',
      seg(diag30, {c: scores[(c, 'core')] for c in diag30}, master),
      '| R32 platform:', seg(diag30, r32, master))

print('\n== SUMMARY ==')
print(json.dumps({'platform_a': plat_a, 'platform_b': plat_b, 'platform_c': plat_c,
                  'platform_all': plat_a and plat_b and plat_c,
                  'c_single': c34['pair_diff'], 'c_pooled': pm, 'c_fuse_ok': fuse_ok,
                  'diag_delta_merged': d_all['delta'], 'diag_verdict': verdict},
                 ensure_ascii=False))
