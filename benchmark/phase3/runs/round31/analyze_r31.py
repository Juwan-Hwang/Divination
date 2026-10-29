#!/usr/bin/env python3
"""R31 analysis (analysis role only): merge double-judge scores + preregistered reads.

Seat layout this round (documented deviation in seat assignment only; the
double-judge + arbitration protocol is unchanged): judge view X =
judgeA (packetA) + judgeA2 (packetB); judge view Y = judgeB (packetB) +
judgeB2 (packetA). Merged views were written by the host to
judging/judgeX-merged.json / judgeY-merged.json after verifying both views
cover the identical 487 anon set as host-mapping.json.

Merge rule (same as R29/R30): final = mean of the two judge views (total and
sub-scores); cases with |X.total - Y.total| >= 3 are replaced by the
arbitration score. The computed dispute set is asserted equal to
judging/disputes.json before merging.

Criteria per runs/round31/PREREG.md:
- s.2 MAIN = LR3 clan migration read (pair_diff >= -1.567 positive gain;
  <= -2.717 falsified; between = undetermined). dev8 clan is an upper-bound
  read with guardrail >= -2.593 (breach joins the falsify disposition).
  Merged liuren segment is report-only.
- s.4 platform (a) ALL >= -1.371; (b) bazi >= -0.449, bazi-natal >= +0.290,
  horary >= -0.760, liuren dev8 subset >= -2.593; (c) liuyao dev8 subset
  >= -1.93. All three stand -> open holdout11 (host step, not here).
- s.5 overlay 13 listed singly; LR-001 listed singly; dev8 clan excluding
  LR-001 (n=17) as reference.

Outputs: runs/round31/final-scores.json (same shape as round29/30) + stdout.
No method files are touched; no git operations.
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R31 = P3 / 'runs/round31'
JD = R31 / 'judging'

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
json.dump(final, open(R31 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
print('final-scores.json written: n =', len(final['ours_axis2']))

def seg(ids, scores=None):
    scores = ours if scores is None else scores
    ids = sorted(c for c in ids if c in scores and c in master)
    pair = [scores[c] - master[c]['total'] for c in ids]
    n = len(pair)
    mean = sum(pair) / n
    se = (math.sqrt(sum((x - mean) ** 2 for x in pair) / (n - 1)) / math.sqrt(n)) if n > 1 else 0.0
    w = sum(1 for x in pair if x > 0); t = sum(1 for x in pair if x == 0); l = n - w - t
    return {'n': n, 'pair_diff': round(mean, 3), 'SE': round(se, 3),
            'ours_mean': round(sum(scores[c] for c in ids) / n, 3),
            'master_mean': round(sum(master[c]['total'] for c in ids) / n, 3),
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

fs29 = json.load(open(P3 / 'runs/round29/final-scores.json'))
ours29 = {c: (v['total'] if isinstance(v, dict) else v) for c, v in fs29['ours_axis2'].items()}
fs30 = json.load(open(P3 / 'runs/round30/final-scores.json'))
ours30 = {c: (v['total'] if isinstance(v, dict) else v) for c, v in fs30['ours_axis2'].items()}

print('\n== 1. headline ==')
print('ALL(487):', seg(all_ids), '| platform (a) >= -1.371 ->', seg(all_ids)['pair_diff'] >= -1.371)
print('low-contamination:', seg(low_ids))
print('ours pass:', stats['ALL']['ours_pass'], '/', len(all_ids))

print('\n== 2. MAIN CRITERION (PREREG s.2): LR3 clan migration read ==')
m_lr3 = seg(lr3_ids)
print('LR3 clan(12):', m_lr3, '| R29 anchor -2.167; R30 alt-pack read -0.021 (reference only)')
print('positive-gain: pair_diff >= -1.567 ->', m_lr3['pair_diff'] >= -1.567)
print('falsify: pair_diff <= -2.717 ->', m_lr3['pair_diff'] <= -2.717)
m_d8 = seg(liuren8)
print('dev8 clan(18) upper-bound read:', m_d8, '| R29 anchor -1.750; R30 read -2.236')
print('guardrail: pair_diff >= -2.593 ->', m_d8['pair_diff'] >= -2.593)
print('dev8 clan excl LR-001(17) reference:', seg(liuren8_no_lr001))
print('liuren merged(30) report-only:', seg(liuren_all), '| R29 anchor -1.917; R30 -1.350')
print('LR3 R31 vs R29 same-subset:', seg(lr3_ids, ours29))
print('dev8 clan R31 vs R29 same-subset:', seg(liuren8, ours29))
print('LR-001 single:', seg(['LR-001']), '| ours', ours['LR-001'], '| master', master['LR-001']['total'])

print('\n== 3. platform (PREREG s.4) ==')
print('(b) bazi(29):', seg(by_trad('bazi')), '>= -0.449 ->', seg(by_trad('bazi'))['pair_diff'] >= -0.449)
print('(b) bazi-natal(26):', seg(by_trad('八字')), '>= +0.290 ->', seg(by_trad('八字'))['pair_diff'] >= 0.290)
print('(b) horary(25):', seg(by_trad('horary')), '>= -0.760 ->', seg(by_trad('horary'))['pair_diff'] >= -0.760)
print('(b) liuren dev8(18): >= -2.593 ->', m_d8['pair_diff'] >= -2.593)
print('(c) liuyao dev8(246):', seg(liuyao8), '>= -1.93 ->', seg(liuyao8)['pair_diff'] >= -1.93)
print('(c) YY-label liuyao dev8 attached:', seg(by_trad('六爻', dev8_set)))
print('(c) liuyao246+YY union attached:', seg(sorted(set(liuyao8) | set(by_trad('六爻', dev8_set)))))

print('\n== 4. overlay 13 cases (PREREG s.5) ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
assert len(ov_ids) == 13
rows = []
for c in ov_ids:
    rows.append((c, round(ours[c] - master[c]['total'], 3),
                 round(ours30[c] - master[c]['total'], 3),
                 round(ours29[c] - master[c]['total'], 3)))
    print(f'{c}: R31 pair {rows[-1][1]:+.3f} (ours {ours[c]}) | R30 pair {rows[-1][2]:+.3f} | R29 pair {rows[-1][3]:+.3f} | master {master[c]["total"]}')
print('overlay13 mean pair: R31', round(sum(r[1] for r in rows) / 13, 3),
      '| R30', round(sum(r[2] for r in rows) / 13, 3),
      '| R29', round(sum(r[3] for r in rows) / 13, 3))

print('\n== 5. prediction meta ==')
sys_count = Counter(); trig = Counter(); n_pred = 0
for f in glob.glob(str(R31 / 'predictions/*.json')):
    p = json.load(open(f)); n_pred += 1
    for s in p.get('systems_used', []):
        sys_count[s] += 1
    for k in ('changed_main', 'reserve_used', 'disputed'):
        if p.get('trigger', {}).get(k):
            trig[k] += 1
print('predictions:', n_pred)
print('systems_used distribution:', dict(sys_count.most_common()))
print('trigger true counts:', {k: trig[k] for k in ('changed_main', 'reserve_used', 'disputed')})
