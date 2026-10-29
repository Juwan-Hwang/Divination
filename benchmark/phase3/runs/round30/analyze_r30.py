#!/usr/bin/env python3
"""R30 analysis (analysis role only): merge double-judge scores + preregistered reads.

Merge rule (same as R29): final = mean of judgeA/judgeB (total and the three
sub-scores direction/claims/timing); cases with |A.total - B.total| >= 3 are
replaced by the arbitration score. The computed dispute set is asserted equal
to judging/disputes.json before merging.

All paired diffs = ours_final - master baseline total
(data/master-baseline-dev9.json). Criteria per runs/round30/PREREG.md:
s.2 liuren merged segment (main), s.3 inputs10 DiD (registration only),
s.4 platform (a)/(b)/(c), s.5 holdout11 (<25 -> no seal, no opening).

Outputs: runs/round30/final-scores.json (same shape as round29) + stdout report
numbers. No method files are touched; no git operations.
"""
import json, math, glob
from collections import Counter
from pathlib import Path

P3 = Path('benchmark/phase3')
R30 = P3 / 'runs/round30'
JD = R30 / 'judging'

# ---------- load judging material ----------
def load_jsonl(path):
    out = {}
    for line in open(path):
        line = line.strip()
        if line:
            r = json.loads(line)
            out[r['anon_id']] = r
    return out

judgeA = {}
for f in ('judgeA-part1.jsonl', 'judgeA-part2.jsonl'):
    judgeA.update(load_jsonl(JD / f))
judgeB = {}
for f in ('judgeB-part1.jsonl', 'judgeB-part2.jsonl'):
    judgeB.update(load_jsonl(JD / f))
arbitration = load_jsonl(JD / 'arbitration.jsonl')
hmap = json.load(open(JD / 'host-mapping.json'))          # anon_id -> case_id
meta = json.load(open(JD / 'host-meta.json'))              # case_id -> tradition/contamination
disputes_file = json.load(open(JD / 'disputes.json'))
master = json.load(open(P3 / 'data/master-baseline-dev9.json'))
master8 = json.load(open(P3 / 'data/master-baseline-dev8.json'))

assert len(judgeA) == 487 and len(judgeB) == 487, (len(judgeA), len(judgeB))
assert set(judgeA) == set(hmap) == set(judgeB), 'anon_id sets differ across judge files / mapping'

# ---------- verify dispute set equals disputes.json ----------
computed_disputes = sorted(
    hmap[a] for a in hmap if abs(judgeA[a]['total'] - judgeB[a]['total']) >= 3)
file_disputes = sorted(d['case_id'] for d in disputes_file)
assert computed_disputes == file_disputes, (computed_disputes, file_disputes)
print('dispute set self-check: computed |dTotal|>=3 set == disputes.json ->', computed_disputes)

# ---------- merge ----------
ours, ours_sub = {}, {}
for anon, cid in hmap.items():
    a, b = judgeA[anon], judgeB[anon]
    if abs(a['total'] - b['total']) >= 3:
        arb = arbitration[anon]
        rec = {k: float(arb[k]) for k in ('direction', 'claims', 'timing', 'total')}
    else:
        rec = {k: (a[k] + b[k]) / 2 for k in ('direction', 'claims', 'timing', 'total')}
    ours[cid] = rec['total']
    ours_sub[cid] = rec
assert len(ours) == 487 and set(ours) == set(master) == set(meta)

# ---------- stats block (same shape/keys as round29 final-scores) ----------
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
json.dump(final, open(R30 / 'final-scores.json', 'w'), ensure_ascii=False, indent=1)
print('final-scores.json written: n =', len(final['ours_axis2']))

# ---------- segment helper (n + SE) ----------
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
low_ids = [c for c in all_ids if meta[c]['contamination'] == 'low']
liuyao8 = by_trad('liuyao', set(dev8_ids))
liuren_all = [c for c in all_ids if meta[c]['tradition'] in ('liuren', '六壬')]
liuren8 = [c for c in liuren_all if c in set(dev8_ids)]
lr3_ids = [c for c in liuren_all if c not in set(dev8_ids)]

print('\n== 1. headline ==')
print('ALL(487):', seg(all_ids))
print('low-contamination:', seg(low_ids))
print('ours pass:', stats['ALL']['ours_pass'], '/', len(all_ids))

print('\n== 2. same-subset reads ==')
print('dev8 subset(412):', seg(dev8_ids))
print('liuyao dev8(246):', seg(liuyao8))
print('guardrail bazi(29):', seg(by_trad('bazi')))
print('guardrail bazi-natal 八字(26):', seg(by_trad('八字')))
print('guardrail horary(25):', seg(by_trad('horary')))
print('guardrail liuren dev8(18):', seg(liuren8))
print('YY-label liuyao dev8 (六爻, attached):', seg(by_trad('六爻', set(dev8_ids))))
print('liuyao246+YY16 union (attached):', seg(sorted(set(liuyao8) | set(by_trad('六爻', set(dev8_ids))))))

print('\n== 3. MAIN CRITERION (PREREG s.2): liuren merged segment ==')
m = seg(liuren_all)
print('liuren merged(30):', m, '| R29 anchor -1.917 W/T/L 5/2/23; R28 -2.241')
print('liuren dev8 subset(18):', seg(liuren8), '| R29 anchor -1.750')
print('LR3 subset(12):', seg(lr3_ids), '| R29 anchor -2.167')
print('positive-gain: pair_diff >= -1.30 ->', m['pair_diff'] >= -1.30, '; W > 5 ->', m['W'] > 5)
print('falsify: pair_diff <= -2.10 ->', m['pair_diff'] <= -2.10)

print('\n== 4. inputs10 DiD (PREREG s.3) ==')
fs28 = json.load(open(P3 / 'runs/round28/final-scores.json'))
ours28 = {c: v['total'] if isinstance(v, dict) else v for c, v in fs28['ours_axis2'].items()}
fs29 = json.load(open(P3 / 'runs/round29/final-scores.json'))
ours29 = {c: v['total'] if isinstance(v, dict) else v for c, v in fs29['ours_axis2'].items()}
did_sets = json.load(open(P3 / 'data/DID-ANCHORS-R30.json'))['did']['sets']
S44 = did_sets['S_inputs10']
C_ids = did_sets['C_control']
S43 = [c for c in S44 if c != 'LY-036']
assert len(S44) == 44 and len(S43) == 43 and len(C_ids) == 396
print('R28 C anchor recomputed:', seg(C_ids, ours28), '| DID doc value -1.174 (SE 0.114)')
print('R28 S43 anchor recomputed:', seg(S43, ours28))
print('R30 S43:', seg(S43))
print('R30 C:', seg(C_ids))

def did(ids_a, ids_b):
    # per-case cross-round delta d = ours30 - ours28 (master cancels); DiD = mean_A(d) - mean_B(d)
    def dstats(ids):
        d = [ours[c] - ours28[c] for c in ids]
        n = len(d); mean = sum(d) / n
        var = sum((x - mean) ** 2 for x in d) / (n - 1)
        return mean, var, n
    ma, va, na = dstats(ids_a)
    mb, vb, nb = dstats(ids_b)
    return ma - mb, math.sqrt(va / na + vb / nb), ma, mb

did_val, did_se, d_s, d_c = did(S43, C_ids)
print(f'DiD = (R30_S43-R28_S43) - (R30_C-R28_C) = ({d_s:+.3f}) - ({d_c:+.3f}) = {did_val:+.3f} (SE {did_se:.3f})')
print('DiD band: > +0.55 effective / < -0.55 harmful / |DiD| <= 0.55 undetermined')

print('\n== 5. overlay 13 cases (PREREG s.1 variable 3) ==')
overlay = json.load(open(P3 / 'data/outcome-errata-overlay.json'))
ov_ids = sorted(k for k in overlay if not k.startswith('_'))
assert len(ov_ids) == 13
rows = []
for c in ov_ids:
    rows.append((c, round(ours[c] - master[c]['total'], 3), round(ours29[c] - master[c]['total'], 3),
                 ours[c], ours29[c], master[c]['total']))
    print(f'{c}: R30 pair {rows[-1][1]:+.3f} (ours {ours[c]}) | R29 pair {rows[-1][2]:+.3f} (ours {ours29[c]}) | master {master[c]["total"]}')
print('overlay13 mean pair: R30', round(sum(r[1] for r in rows) / 13, 3),
      '| R29', round(sum(r[2] for r in rows) / 13, 3))

print('\n== 6. single case / prediction meta ==')
print('LR-001:', seg(['LR-001']), '| ours', ours['LR-001'], '| master', master['LR-001']['total'])
sys_count = Counter(); n_pred = 0
trig = Counter()
for f in glob.glob(str(R30 / 'predictions/*.json')):
    p = json.load(open(f)); n_pred += 1
    for s in p.get('systems_used', []):
        sys_count[s] += 1
    for k in ('changed_main', 'reserve_used', 'disputed'):
        if p.get('trigger', {}).get(k):
            trig[k] += 1
print('predictions:', n_pred)
print('systems_used distribution:', dict(sys_count.most_common()))
print('trigger true counts:', {k: trig[k] for k in ('changed_main', 'reserve_used', 'disputed')})
