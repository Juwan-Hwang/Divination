#!/usr/bin/env python3
"""R32 analysis (analysis role only): merge double-judge scores + preregistered reads.

Merge rule (same as R29/R30/R31): final = mean of the two judge views (total
and sub-scores); cases with |X.total - Y.total| >= 3 are replaced by the
arbitration score. The computed dispute set is asserted equal to
judging/disputes.json before merging. Judge views were merged by the host
(merge_judge_views_r32.py) after verifying both views cover the identical
487 anon set as host-mapping.json.

Criteria per runs/round32/PREREG.md:
- No variable this round (zero-change replication). Liuren reads are
  report-only by clan: dev8 clan = upper-bound read, LR3 clan = migration
  read, merged = report-only; LR-001 listed singly.
- s.3 platform (a) ALL >= -1.371; (b) bazi >= -0.449, bazi-natal >= +0.290,
  horary >= -0.760, liuren dev8 subset >= -2.593.
- s.2 platform (c) POOLED rule: pool = rounds with liuyao inputs identical
  to inputs-dev10 and liuyao method of the R29-snapshot lineage =
  {R30, R31, R32}. For each of the 246 (c)-subset cases take the mean of the
  per-round pair diffs (round final ours - dev8 master baseline total),
  then average over the 246. Pooled >= -1.93 -> (c) stands. Circuit breaker:
  if R32 single-round (c) < -2.255 the pooled standing is void.
  R31's own single-round verdict is not altered by this rule.
- s.0/s.5 overlay 13 listed singly (R32/R31/R30 trio).

Outputs: runs/round32/final-scores.json (same shape as round29/30/31) + stdout.
No method files are touched; no git operations.
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R32 = P3 / 'runs/round32'
JD = R32 / 'judging'

def load_jsonl(path):
    out = {}
    for line in open(path):
        line = line.strip()
        if line:
            r = json.loads(line)
            out[r['anon_id']] = r
    return out

judgeX = json.load(open(JD / 'judgeX-merged.json'))
judgeY = json.load(open(JD / 'judgeY-merged.json'))
arbitration = load_jsonl(JD / 'arbitration.jsonl')
hmap = json.load(open(JD / 'host-mapping.json'))
meta = json.load(open(JD / 'host-meta.json'))
disputes_file = json.load(open(JD / 'disputes.json'))
master = json.load(open(P3 / 'data/master-baseline-dev9.json'))
master8 = json.load(open(P3 / 'data/master-baseline-dev8.json'))

assert len(judgeX) == 487 and len(judgeY) == 487, (len(judgeX), len(judgeY))
assert set(judgeX) == set(hmap) == set(judgeY), 'anon_id sets differ'

computed_disputes = sorted(
    hmap[a] for a in hmap if abs(judgeX[a]['total'] - judgeY[a]['total']) >= 3)
file_disputes = sorted(d['case_id'] for d in disputes_file)
assert computed_disputes == file_disputes, (computed_disputes, file_disputes)
assert set(arbitration) == {a for a, c in hmap.items() if c in computed_disputes}
print('dispute set self-check: computed == disputes.json ->', computed_disputes)

ours, ours_sub = {}, {}
for anon, cid in hmap.items():
    x, y = judgeX[anon], judgeY[anon]
    if abs(x['total'] - y['total']) >= 3:
        arb = arbitration[anon]
        rec = {k: float(arb[k]) for k in ('direction', 'claims', 'timing', 'total')}
    else:
        rec = {k: (x[k] + y[k]) / 2 for k in ('direction', 'claims', 'timing', 'total')}
    ours[cid] = rec['total']
    ours_sub[cid] = rec
assert len(ours) == 487 and set(ours) == set(master) == set(meta)

def block(ids):
    ids = sorted(ids)
    n = len(ids)
    om = sum(ours[c] for c in ids) / n
    mm = sum(master[c]['total'] for c in ids) / n
    pair = [ours[c] - master[c]['total'] for c in ids]
    w = sum(1 for x in pair if x > 0); t = sum(1 for x in pair if x == 0); l = n - w - t
    return {'n': n, 'ours_mean': round(om, 3), 'ours_pct': round(om / 6 * 100, 1),
            'ours_pass': sum(1 for c in ids if ours[c] >= 4),
            'master_mean': round(mm, 3), 'pair_diff': round(sum(pair) / n, 3),
            'W/T/L': f'{w}/{t}/{l}',
            'timing_ours': round(sum(ours_sub[c]['timing'] for c in ids) / n, 3),
            'dir_ours': round(sum(ours_sub[c]['direction'] for c in ids) / n, 3),
            'claims_ours': round(sum(ours_sub[c]['claims'] for c in ids) / n, 3)}

all_ids = sorted(ours)
stats = {'ALL': block(all_ids),
         'by_tradition': {t: block([c for c in all_ids if meta[c]['tradition'] == t])
                          for t in sorted({meta[c]['tradition'] for c in all_ids})},
         'by_contamination': {k: block([c for c in all_ids if meta[c]['contamination'] == k])
                              for k in sorted({meta[c]['contamination'] for c in all_ids})}}
final = {'ours_axis2': {c: ours[c] for c in all_ids},
         'ours_sub': {c: ours_sub[c] for c in all_ids},
         'stats': stats}
json.dump(final, open(R32 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
print('final-scores.json written: n =', len(final['ours_axis2']))

def seg(ids, scores=None, base=None):
    scores = ours if scores is None else scores
    base = master if base is None else base
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

def by_trad(tr, pool=None):
    return [c for c in all_ids if meta[c]['tradition'] == tr and (pool is None or c in pool)]

dev8_ids = sorted(c for c in all_ids if c in master8)
dev8_set = set(dev8_ids)
low_ids = [c for c in all_ids if meta[c]['contamination'] == 'low']
liuyao8 = by_trad('liuyao', dev8_set)
liuren_all = [c for c in all_ids if meta[c]['tradition'] in ('liuren', '六壬')]
liuren8 = [c for c in liuren_all if c in dev8_set]
lr3_ids = [c for c in liuren_all if c not in dev8_set]
liuren8_no_lr001 = [c for c in liuren8 if c != 'LR-001']

def load_final(rnd):
    fs = json.load(open(P3 / f'runs/{rnd}/final-scores.json'))
    return {c: (v['total'] if isinstance(v, dict) else v) for c, v in fs['ours_axis2'].items()}

ours31 = load_final('round31')
ours30 = load_final('round30')

print('\n== 1. headline ==')
print('ALL(487):', seg(all_ids), '| platform (a) >= -1.371 ->', seg(all_ids)['pair_diff'] >= -1.371)
print('low-contamination:', seg(low_ids))
print('ours pass:', stats['ALL']['ours_pass'], '/', len(all_ids))

print('\n== 2. liuren family reads (report-only, PREREG s.1) ==')
print('dev8 clan(18) upper-bound read:', seg(liuren8), '| R31 -0.569; R30 -2.236; R29 -1.750')
print('LR3 clan(12) migration read:', seg(lr3_ids), '| R31 -1.896; R30 -0.021 (alt packet); R29 -2.167')
print('liuren merged(30) report-only:', seg(liuren_all), '| R31 -1.100; R30 -1.350; R29 -1.917')
print('dev8 clan excl LR-001(17) reference:', seg(liuren8_no_lr001))
print('LR-001 single:', seg(['LR-001']), '| ours', ours['LR-001'], '| master', master['LR-001']['total'])

print('\n== 3. platform (PREREG s.3 + s.2) ==')
print('(b) bazi(29):', seg(by_trad('bazi')), '>= -0.449 ->', seg(by_trad('bazi'))['pair_diff'] >= -0.449)
print('(b) bazi-natal(26):', seg(by_trad('八字')), '>= +0.290 ->', seg(by_trad('八字'))['pair_diff'] >= 0.290)
print('(b) horary(25):', seg(by_trad('horary')), '>= -0.760 ->', seg(by_trad('horary'))['pair_diff'] >= -0.760)
print('(b) liuren dev8(18): >= -2.593 ->', seg(liuren8)['pair_diff'] >= -2.593)
c_single = seg(liuyao8)
print('(c) R32 single-round liuyao dev8(246):', c_single, '| R31 -1.955; R30 -1.632')
print('(c) YY-label liuyao dev8 attached:', seg(by_trad('六爻', dev8_set)))
print('(c) liuyao246+YY union attached:', seg(sorted(set(liuyao8) | set(by_trad('六爻', dev8_set)))))

# pooled (c): case-level mean of per-round pair diffs over {R30, R31, R32}
pool_rounds = {'R30': ours30, 'R31': ours31, 'R32': ours}
per_case = {}
for c in liuyao8:
    diffs = [pool_rounds[r][c] - master8[c]['total'] for r in ('R30', 'R31', 'R32')]
    per_case[c] = sum(diffs) / 3
pv = [per_case[c] for c in liuyao8]
pn = len(pv); pmean = sum(pv) / pn
pse = math.sqrt(sum((x - pmean) ** 2 for x in pv) / (pn - 1)) / math.sqrt(pn)
print(f'(c) POOLED over R30/R31/R32: n={pn} pooled pair_diff={round(pmean, 3)} SE(case-mean)={round(pse, 3)}')
print('(c) circuit breaker: R32 single >= -2.255 ->', c_single['pair_diff'] >= -2.255)
pooled_stands = pmean >= -1.93 and c_single['pair_diff'] >= -2.255
print('(c) pooled >= -1.93 and breaker intact -> (c) STANDS:', pooled_stands)

print('\n== 4. overlay 13 cases ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
assert len(ov_ids) == 13
rows = []
for c in ov_ids:
    rows.append((c, round(ours[c] - master[c]['total'], 3),
                 round(ours31[c] - master[c]['total'], 3),
                 round(ours30[c] - master[c]['total'], 3)))
    print(f'{c}: R32 pair {rows[-1][1]:+.3f} (ours {ours[c]}) | R31 pair {rows[-1][2]:+.3f} | R30 pair {rows[-1][3]:+.3f} | master {master[c]["total"]}')
print('overlay13 mean pair: R32', round(sum(r[1] for r in rows) / 13, 3),
      '| R31', round(sum(r[2] for r in rows) / 13, 3),
      '| R30', round(sum(r[3] for r in rows) / 13, 3))

print('\n== 5. prediction meta ==')
sys_count = Counter(); trig = Counter(); n_pred = 0
for f in glob.glob(str(R32 / 'predictions/*.json')):
    p = json.load(open(f)); n_pred += 1
    for s in p.get('systems_used', []):
        sys_count[s] += 1
    for k in ('changed_main', 'reserve_used', 'disputed'):
        if p.get('trigger', {}).get(k):
            trig[k] += 1
print('predictions:', n_pred)
print('systems_used distribution:', dict(sys_count.most_common()))
print('trigger true counts:', {k: trig[k] for k in ('changed_main', 'reserve_used', 'disputed')})

plat_a = seg(all_ids)['pair_diff'] >= -1.371
plat_b = (seg(by_trad('bazi'))['pair_diff'] >= -0.449 and seg(by_trad('八字'))['pair_diff'] >= 0.290
          and seg(by_trad('horary'))['pair_diff'] >= -0.760 and seg(liuren8)['pair_diff'] >= -2.593)
print('\n== PLATFORM ==')
print('(a)', plat_a, '| (b)', plat_b, '| (c pooled)', pooled_stands, '| ALL STAND:', plat_a and plat_b and pooled_stands)
