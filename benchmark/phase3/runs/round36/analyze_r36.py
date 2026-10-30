#!/usr/bin/env python3
"""R36 analysis (analysis role only): merge double-judge scores, platform
reads per R36 PREREG s.2. No method files touched; no git operations.

Platform criteria (R36 PREREG s.2):
- (a) ALL pair_diff >= -1.371
- (b) bazi >= -0.449, bazi-natal >= +0.290, horary >= -0.760,
  liuren dev8 subset >= -2.593
- (c) liuyao dev8 (246): POOLED with R35 (pool round 2, declared in
  advance). Preconditions verified at freeze time: inputs-dev11 identical
  to R35; chinese-liuyao-meihua.md identical between R36 and R35 kb
  snapshots (hash 4675c3e2...). Stands iff pooled pair_diff (246 ids x 2
  rounds of paired diffs) >= -1.93 AND both single rounds >= -2.255
  (fuse line). R35 single was -1.758.
Attribution guardrails (PREREG s.2, separate from platform verdict;
rollback affects live method in later rounds only, never this round's
reads): liuren merged (dev8+LR3, n=30) pair_diff < -2.19 -> LR-QY items
falsified/rollback; bazi-all pair_diff < -0.514 -> CGM merge
falsified/rollback.
Segment definitions verbatim from analyze_r35.py (host-meta traditions:
'bazi' = BZ 29, '八字' = natal 26, dev8 subsets via master-baseline-dev8).
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R36 = P3 / 'runs/round36'
JD = R36 / 'judging'


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


def pooled_seg(ids, scores_list, base):
    pair = []
    for scores in scores_list:
        pair += [scores[c] - base[c]['total'] for c in sorted(ids)]
    n = len(pair)
    mean = sum(pair) / n
    se = (math.sqrt(sum((x - mean) ** 2 for x in pair) / (n - 1)) / math.sqrt(n)) if n > 1 else 0.0
    w = sum(1 for x in pair if x > 0); t = sum(1 for x in pair if x == 0); l = n - w - t
    return {'n_reads': n, 'pair_diff': round(mean, 3), 'SE': round(se, 3),
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
json.dump(final, open(R36 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
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

print('\n== 3. (c) liuyao dev8: pooled R35+R36 (pool round 2, PREREG s.2) ==')
c36 = seg(liuyao8, ours, master)
r35 = json.load(open(P3 / 'runs/round35/final-scores.json'))['ours_axis2']
c35 = seg(liuyao8, r35, master)
cpool = pooled_seg(liuyao8, [r35, ours], master)
fuse_ok = (c35['pair_diff'] >= -2.255) and (c36['pair_diff'] >= -2.255)
plat_c = (cpool['pair_diff'] >= -1.93) and fuse_ok
print('R35 single:', c35)
print('R36 single:', c36)
print('pooled (492 reads):', cpool)
print(f'fuse check (both singles >= -2.255): {fuse_ok}')
print('(c) STANDS (pooled >= -1.93 and fuse ok):', plat_c)

print('\n== 4. liuren family reads (platform run, report-only) ==')
print('dev8 clan(18):', seg(liuren8, ours, master))
print('LR3 clan(12):', seg(lr3_ids, ours, master))
print('merged(30):', seg(liuren_all, ours, master), '| R35 merged was -1.842')

print('\n== 5. overlay 16 ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
print('overlay16 mean pair:', round(sum(ours[c] - master[c]['total'] for c in ov_ids) / 16, 3))

print('\n== 6. prediction meta ==')
sys_count, trig = Counter(), Counter()
for f in glob.glob(str(R36 / 'predictions/*.json')):
    p = json.load(open(f))
    for s in p.get('systems_used', []):
        sys_count[s] += 1
    for k in ('changed_main', 'reserve_used', 'disputed'):
        if p.get('trigger', {}).get(k):
            trig[k] += 1
print('systems_used:', dict(sys_count.most_common()))
print('trigger true counts:', {k: trig[k] for k in ('changed_main', 'reserve_used', 'disputed')})

print('\n== 7. attribution guardrails (PREREG s.2; later-round rollback only) ==')
lr_merged = seg(liuren_all, ours, master)
lr_guard_fail = lr_merged['pair_diff'] < -2.19
cgm_guard_fail = g_bazi['pair_diff'] < -0.514
print('liuren merged:', lr_merged['pair_diff'], '< -2.19 -> LR-QY falsified/rollback:', lr_guard_fail)
print('bazi all:', g_bazi['pair_diff'], '< -0.514 -> CGM falsified/rollback:', cgm_guard_fail)

plat_a = s_all['pair_diff'] >= -1.371
print('\n== PLATFORM ==')
print('(a)', plat_a, '| (b)', plat_b, '| (c)', plat_c, '| ALL STAND:', plat_a and plat_b and plat_c)

print('\n== SUMMARY ==')
print(json.dumps({'platform_a': plat_a, 'platform_b': plat_b, 'platform_c': plat_c,
                  'platform_all': plat_a and plat_b and plat_c,
                  'a_pair_diff': s_all['pair_diff'], 'c_single_r36': c36['pair_diff'],
                  'c_pooled': cpool['pair_diff'], 'c_fuse_ok': fuse_ok,
                  'guardrail_lr_rollback': lr_guard_fail,
                  'guardrail_cgm_rollback': cgm_guard_fail},
                 ensure_ascii=False))
