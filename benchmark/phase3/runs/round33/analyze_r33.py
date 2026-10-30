#!/usr/bin/env python3
"""R33 analysis (analysis role only): merge double-judge scores + preregistered reads.

Merge rule (same as R29-R32): final = mean of the two judge views; cases with
|X.total - Y.total| >= 3 are replaced by the arbitration score (R33 original
dispute set is empty, verified against judging/disputes.json).

MP correction (ADDENDUM-mp-collision.md): the 9 mismatched MP rows in both
views are replaced by the re-judged rows (judgeX-mp.jsonl / judgeY-mp.jsonl,
same anon ids, correct outcomes) before merging; the uncorrected headline is
also computed and printed for disclosure. If a corrected row pair disputes
(|dTotal| >= 3) this script stops and reports it for arbitration.

Criteria per runs/round33/PREREG.md s.2 (single-round, no pooling):
- (a) ALL pair_diff >= -1.371
- (b) bazi >= -0.449, bazi-natal >= +0.290, horary >= -0.760,
  liuren dev8 subset >= -2.593
- (c) liuyao dev8 subset (246) single-round pair_diff >= -1.93
Liuren family reads report-only by clan; overlay 16 listed singly.

Outputs: runs/round33/final-scores.json (same shape as round29-32) + stdout.
No method files are touched; no git operations.
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R33 = P3 / 'runs/round33'
JD = R33 / 'judging'

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
try:
    arbitration = load_jsonl(JD / 'arbitration.jsonl')
except FileNotFoundError:
    arbitration = {}
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
print('original dispute set self-check: computed == disputes.json ->', computed_disputes)

def merge_views(jx, jy, arb):
    out, out_sub = {}, {}
    for anon, cid in hmap.items():
        x, y = jx[anon], jy[anon]
        if abs(x['total'] - y['total']) >= 3:
            a = arb[anon]
            rec = {k: float(a[k]) for k in ('direction', 'claims', 'timing', 'total')}
        else:
            rec = {k: (x[k] + y[k]) / 2 for k in ('direction', 'claims', 'timing', 'total')}
        out[cid] = rec['total']
        out_sub[cid] = rec
    return out, out_sub

ours_raw, _ = merge_views(judgeX, judgeY, arbitration)

# ---- MP correction ----
mpX = load_jsonl(JD / 'judgeX-mp.jsonl')
mpY = load_jsonl(JD / 'judgeY-mp.jsonl')
assert len(mpX) == 9 and len(mpY) == 9 and set(mpX) == set(mpY)
assert set(mpX) <= set(judgeX), 'mp anon ids not in views'
mp_disputes = sorted(hmap[a] for a in mpX if abs(mpX[a]['total'] - mpY[a]['total']) >= 3)
print('MP corrected rows: 9; corrected dispute set:', mp_disputes)
if mp_disputes:
    raise SystemExit('MP corrected rows need arbitration first: ' + str(mp_disputes))
for a in mpX:
    judgeX[a] = mpX[a]
    judgeY[a] = mpY[a]
ours, ours_sub = merge_views(judgeX, judgeY, arbitration)
assert len(ours) == 487 and set(ours) == set(master) == set(meta)

def block(ids, scores):
    ids = sorted(ids)
    n = len(ids)
    om = sum(scores[c] for c in ids) / n
    mm = sum(master[c]['total'] for c in ids) / n
    pair = [scores[c] - master[c]['total'] for c in ids]
    w = sum(1 for x in pair if x > 0); t = sum(1 for x in pair if x == 0); l = n - w - t
    return {'n': n, 'ours_mean': round(om, 3), 'ours_pct': round(om / 6 * 100, 1),
            'ours_pass': sum(1 for c in ids if scores[c] >= 4),
            'master_mean': round(mm, 3), 'pair_diff': round(sum(pair) / n, 3),
            'W/T/L': f'{w}/{t}/{l}',
            'timing_ours': round(sum(ours_sub[c]['timing'] for c in ids) / n, 3),
            'dir_ours': round(sum(ours_sub[c]['direction'] for c in ids) / n, 3),
            'claims_ours': round(sum(ours_sub[c]['claims'] for c in ids) / n, 3)}

all_ids = sorted(ours)
stats = {'ALL': block(all_ids, ours),
         'by_tradition': {t: block([c for c in all_ids if meta[c]['tradition'] == t], ours)
                          for t in sorted({meta[c]['tradition'] for c in all_ids})},
         'by_contamination': {k: block([c for c in all_ids if meta[c]['contamination'] == k], ours)
                              for k in sorted({meta[c]['contamination'] for c in all_ids})}}
final = {'ours_axis2': {c: ours[c] for c in all_ids},
         'ours_sub': {c: ours_sub[c] for c in all_ids},
         'stats': stats}
json.dump(final, open(R33 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
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
mp_ids = sorted(hmap[a] for a in mpX)

print('\n== 1. headline ==')
print('ALL(487) corrected:', seg(all_ids), '| platform (a) >= -1.371 ->', seg(all_ids)['pair_diff'] >= -1.371)
print('ALL(487) UNCORRECTED (disclosure only):', seg(all_ids, scores=ours_raw))
print('MP corrected 9:', seg(mp_ids), '| uncorrected:', seg(mp_ids, scores=ours_raw))
print('low-contamination:', seg(low_ids))
print('ours pass:', stats['ALL']['ours_pass'], '/', len(all_ids))

print('\n== 2. liuren family reads (report-only, PREREG s.1) ==')
print('dev8 clan(18) upper-bound read:', seg(liuren8), '| R32 -1.042; R31 -0.569')
print('LR3 clan(12) migration read:', seg(lr3_ids), '| R32 -1.896(merged-only); R31 -1.896')
print('liuren merged(30) report-only:', seg(liuren_all), '| R32 -1.100; R31 -1.100')
print('dev8 clan excl LR-001(17) reference:', seg(liuren8_no_lr001))
print('LR-001 single:', seg(['LR-001']), '| ours', ours['LR-001'], '| master', master['LR-001']['total'])

print('\n== 3. platform (PREREG s.2) ==')
print('(a) ALL >= -1.371 ->', seg(all_ids)['pair_diff'] >= -1.371)
print('(b) bazi(29):', seg(by_trad('bazi')), '>= -0.449 ->', seg(by_trad('bazi'))['pair_diff'] >= -0.449)
print('(b) bazi-natal(26):', seg(by_trad('八字')), '>= +0.290 ->', seg(by_trad('八字'))['pair_diff'] >= 0.290)
print('(b) horary(25):', seg(by_trad('horary')), '>= -0.760 ->', seg(by_trad('horary'))['pair_diff'] >= -0.760)
print('(b) liuren dev8(18):', seg(liuren8), '>= -2.593 ->', seg(liuren8)['pair_diff'] >= -2.593)
c_single = seg(liuyao8)
print('(c) R33 single-round liuyao dev8(246):', c_single, '| >= -1.93 ->', c_single['pair_diff'] >= -1.93, '| R32 single -1.955; R31 -1.955; R30 -1.632')
print('(c) YY-label liuyao dev8 attached:', seg(by_trad('六爻', dev8_set)))
print('(c) liuyao246+YY union attached:', seg(sorted(set(liuyao8) | set(by_trad('六爻', dev8_set)))))

print('\n== 4. overlay 16 cases ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
assert len(ov_ids) == 16
rows = []
for c in ov_ids:
    rows.append((c, round(ours[c] - master[c]['total'], 3)))
    print(f'{c}: R33 pair {rows[-1][1]:+.3f} (ours {ours[c]}) | master {master[c]["total"]}')
print('overlay16 mean pair: R33', round(sum(r[1] for r in rows) / 16, 3))

print('\n== 5. prediction meta ==')
sys_count = Counter(); trig = Counter(); n_pred = 0
for f in glob.glob(str(R33 / 'predictions/*.json')):
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
plat_c = c_single['pair_diff'] >= -1.93
print('\n== PLATFORM ==')
print('(a)', plat_a, '| (b)', plat_b, '| (c)', plat_c, '| ALL STAND:', plat_a and plat_b and plat_c)
