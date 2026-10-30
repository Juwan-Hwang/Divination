#!/usr/bin/env python3
"""R35 DIAG-BZ exposure stratification (diagnosis role only, no method change).

Populations (per runs/round34/analyze_r34.py tradition coding):
  MAIN  : tradition == 'bazi'  (29 cases, R34 report '八字全集', pair -0.078)
  CTRL  : tradition == '八字'  (26 cases, R34 'natal' subset, pair +0.788)
          + 3 mixed-tradition cases containing 八字 (MP-014/015/018) = 29
Exposure layer = first dev pool the case appears in:
  early  : Phase1/2 or dev<=6  (splits3/4/5 dev lists, dev6-roster, roster<=6)
  mid    : dev7 / dev8 entry   (splits7/splits8 first appearance, roster7/8)
  recent : dev9 entry          (splits9 first appearance, roster9)
Contamination: runs/round34/judging/host-meta.json (consolidated per-case
label; master-baseline-dev9.json itself stores only {src,total}).
Scores: R34 (main) / R33 (secondary) final-scores.json ours_axis2 minus
master-baseline-dev9.json total. Fresh anchor: holdout12-acceptance
judging/final-scores.json per_case QL/NL.
"""
import json, math
from pathlib import Path

P3 = Path('benchmark/phase3')
OUT = P3 / 'runs/round35/diagnosis/diag_bz_exposure_r35_out.json'

def jl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

def mean_se(vals):
    n = len(vals)
    if n == 0:
        return None, None
    m = sum(vals) / n
    se = (math.sqrt(sum((x - m) ** 2 for x in vals) / (n - 1)) / math.sqrt(n)) if n > 1 else 0.0
    return round(m, 3), round(se, 3)

# ---- pool chronology evidence ----
splits = {}
for name, key in [('splits3.json', 'dev3'), ('splits4.json', 'dev4'),
                  ('splits5.json', 'dev5'), ('splits7.json', 'dev7'),
                  ('splits8.json', 'dev8'), ('splits9.json', 'dev9')]:
    d = json.load(open(P3 / name, encoding='utf-8'))
    splits[key] = set(d[key])
dev6 = set(json.load(open(P3 / 'data/dev6-roster.json', encoding='utf-8')).keys())
rosters = {}
for n in (4, 5, 6, 7, 8, 9):
    p = P3 / f'roster{n}-additions.jsonl'
    if p.exists():
        rosters[n] = {r['id']: r for r in jl(p)}

def first_pool(cid):
    """return (layer, evidence_str)"""
    if cid in splits['dev3']:
        return 'early', 'benchmark/phase3/splits3.json dev3'
    if cid in splits['dev4']:
        return 'early', 'benchmark/phase3/splits4.json dev4 (first in dev4)'
    if cid in splits['dev5']:
        return 'early', 'benchmark/phase3/splits5.json dev5 (first in dev5)'
    if cid in dev6:
        return 'early', 'benchmark/phase3/data/dev6-roster.json (dev6)'
    if cid in splits['dev7']:
        src = rosters.get(7, {}).get(cid, {})
        tier = src.get('source_tier', '') if isinstance(src, dict) else ''
        return 'mid', f'benchmark/phase3/splits7.json dev7 + roster7-additions.jsonl ({tier})'
    if cid in splits['dev8']:
        src = rosters.get(8, {}).get(cid, {})
        tier = src.get('source_tier', '') if isinstance(src, dict) else ''
        return 'mid', f'benchmark/phase3/splits8.json dev8 + roster8-additions.jsonl ({tier})'
    if cid in splits['dev9']:
        return 'recent', 'benchmark/phase3/splits9.json dev9 + roster9-additions.jsonl'
    return 'unknown', 'not found in splits3/4/5/7/8/9 or dev6-roster'

# ---- scores ----
master = json.load(open(P3 / 'data/master-baseline-dev9.json', encoding='utf-8'))
r34 = json.load(open(P3 / 'runs/round34/final-scores.json', encoding='utf-8'))['ours_axis2']
r33 = json.load(open(P3 / 'runs/round33/final-scores.json', encoding='utf-8'))['ours_axis2']
meta = json.load(open(P3 / 'runs/round34/judging/host-meta.json', encoding='utf-8'))

main_ids = sorted(c for c in meta if meta[c]['tradition'] == 'bazi')
natal_ids = sorted(c for c in meta if meta[c]['tradition'] == '八字')
mixed_ids = sorted(c for c in meta if '八字' in meta[c]['tradition'] and meta[c]['tradition'] != '八字')
assert len(main_ids) == 29, main_ids
assert len(natal_ids) == 26 and len(mixed_ids) == 3, (natal_ids, mixed_ids)
ctrl_ids = sorted(natal_ids + mixed_ids)

def rows_for(ids, pop):
    rows = []
    for cid in ids:
        layer, ev = first_pool(cid)
        # roster contamination cross-check
        rc = None
        for n in (4, 5, 6, 7, 8, 9):
            if cid in rosters.get(n, {}):
                rc = rosters[n][cid].get('contamination')
        rows.append({
            'pop': pop, 'id': cid, 'tradition': meta[cid]['tradition'],
            'contamination_hostmeta': meta[cid]['contamination'],
            'contamination_roster': rc,
            'layer': layer, 'evidence': ev,
            'ours_r34': r34[cid], 'ours_r33': r33[cid], 'master': master[cid]['total'],
            'pair_r34': round(r34[cid] - master[cid]['total'], 3),
            'pair_r33': round(r33[cid] - master[cid]['total'], 3),
        })
    return rows

def layer_stats(rows, key):
    out = {}
    for layer in ('early', 'mid', 'recent', 'unknown'):
        vals = [r[key] for r in rows if r['layer'] == layer]
        if vals:
            m, se = mean_se(vals)
            out[layer] = {'n': len(vals), 'mean': m, 'SE': se}
    # contamination split (all layers)
    for cont in ('high', 'low'):
        vals = [r[key] for r in rows if r['contamination_hostmeta'] == cont]
        if vals:
            m, se = mean_se(vals)
            out[f'cont_{cont}'] = {'n': len(vals), 'mean': m, 'SE': se}
    vals = [r[key] for r in rows]
    m, se = mean_se(vals)
    out['ALL'] = {'n': len(vals), 'mean': m, 'SE': se}
    return out

result = {}
for pop, ids in [('MAIN-bazi29', main_ids), ('CTRL-natal26+3', ctrl_ids)]:
    rows = rows_for(ids, pop)
    result[pop] = {'rows': rows,
                   'stats_r34': layer_stats(rows, 'pair_r34'),
                   'stats_r33': layer_stats(rows, 'pair_r33')}

# ---- fresh anchor ----
acc = json.load(open(P3 / 'runs/holdout12-acceptance/judging/final-scores.json', encoding='utf-8'))
anchor = {}
for segname, pref in [('QL', 'QL-'), ('NL', 'NL-')]:
    vals = [v['diff'] for c, v in acc['per_case'].items() if c.startswith(pref)]
    m, se = mean_se(vals)
    anchor[segname] = {'n': len(vals), 'mean': m, 'SE': se,
                       'ids': sorted(c for c in acc['per_case'] if c.startswith(pref))}
allf = [v['diff'] for c, v in acc['per_case'].items() if c.startswith(('QL-', 'NL-'))]
m, se = mean_se(allf)
anchor['QL+NL'] = {'n': len(allf), 'mean': m, 'SE': se}
result['anchor'] = anchor

# ---- layer contrasts (R34) for MAIN ----
def contrast(a, b):
    if a is None or b is None or a['n'] < 3 or b['n'] < 3:
        return None
    diff = round(a['mean'] - b['mean'], 3)
    se = round(math.sqrt(a['SE'] ** 2 + b['SE'] ** 2), 3)
    return {'diff': diff, 'SE_combined': se, 'diff_gt_SE': abs(diff) > se,
            'ratio': round(abs(diff) / se, 3) if se else None}

for pop in ('MAIN-bazi29', 'CTRL-natal26+3'):
    s = result[pop]['stats_r34']
    a_stats = {'n': anchor['QL+NL']['n'], 'mean': anchor['QL+NL']['mean'], 'SE': anchor['QL+NL']['SE']}
    result[pop]['contrasts_r34'] = {
        'early_vs_mid': contrast(s.get('early'), s.get('mid')),
        'early_vs_anchorQLNL': contrast(s.get('early'), a_stats),
        'mid_vs_anchorQLNL': contrast(s.get('mid'), a_stats),
        'recent_vs_anchorQLNL': contrast(s.get('recent'), a_stats),
        'all_vs_anchorQLNL': contrast(s.get('ALL'), a_stats),
    }

# ---- supplementary (report-only, not in preregistered bands) ----
s7, s8 = splits['dev7'], splits['dev8']
supp = {}
for label, ours in [('r34', r34), ('r33', r33)]:
    bz = result['MAIN-bazi29']['rows']
    eh = [r['pair_' + label] for r in bz if r['layer'] == 'early' and r['contamination_hostmeta'] == 'high']
    m, se = mean_se(eh)
    supp[f'BZ_early_high_only_{label}'] = {'n': len(eh), 'mean': m, 'SE': se}
    nat = [r for r in result['CTRL-natal26+3']['rows'] if r['tradition'] == '八字']
    for sub, pred in [('dev7entry', lambda c: c in s7), ('dev8entry', lambda c: c in s8 and c not in s7)]:
        vals = [r['pair_' + label] for r in nat if pred(r['id'])]
        m, se = mean_se(vals)
        supp[f'natal_{sub}_{label}'] = {'n': len(vals), 'mean': m, 'SE': se}
result['supplementary'] = supp

json.dump(result, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('supplementary:', json.dumps(supp, ensure_ascii=False))
print(json.dumps({k: (v if k in ('anchor', 'supplementary') else {'stats_r34': v['stats_r34'], 'stats_r33': v['stats_r33'], 'contrasts_r34': v['contrasts_r34']})
                  for k, v in result.items()}, ensure_ascii=False, indent=1))
for pop in ('MAIN-bazi29', 'CTRL-natal26+3'):
    print('\n', pop)
    for r in result[pop]['rows']:
        print(r['id'], r['tradition'], r['layer'], r['contamination_hostmeta'], '/', r['contamination_roster'], r['pair_r34'], r['pair_r33'], '|', r['evidence'])
