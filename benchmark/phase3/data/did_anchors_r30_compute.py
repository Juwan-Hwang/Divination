#!/usr/bin/env python3
"""R30 data-corner compute: inventory counts + inputs10 DiD same-method double anchors.
Reads only on-disk files under benchmark/phase3 (+ masters-dataset/modern-masters counts).
Writes benchmark/phase3/data/DID-ANCHORS-R30.json. No scoring, no edits to originals.
"""
import json, math
from pathlib import Path
from collections import Counter

P3 = Path(__file__).resolve().parents[1]  # benchmark/phase3
ROOT = P3.parents[1]  # ~/workspace/divination

def mean_se(xs):
    n = len(xs)
    m = sum(xs) / n if n else float('nan')
    if n > 1:
        sd = math.sqrt(sum((x - m) ** 2 for x in xs) / (n - 1))
        se = sd / math.sqrt(n)
    else:
        sd = se = float('nan')
    return m, sd, se

def seg_stats(ids, ours, master):
    pair = [ours[c] - master[c] for c in ids]
    m, sd, se = mean_se(pair)
    w = sum(1 for x in pair if x > 0); t = sum(1 for x in pair if x == 0); l = sum(1 for x in pair if x < 0)
    return {'n': len(ids), 'pair_diff': round(m, 4), 'SE': round(se, 4), 'SD': round(sd, 4),
            'ours_mean': round(sum(ours[c] for c in ids) / len(ids), 4),
            'master_mean': round(sum(master[c] for c in ids) / len(ids), 4),
            'W/T/L': f'{w}/{t}/{l}'}

def delta_stats(ids, o28, o29):
    d = [o29[c] - o28[c] for c in ids]
    m, sd, se = mean_se(d)
    dist = Counter(round(x, 2) for x in d)
    return {'n': len(ids), 'delta_mean': round(m, 4), 'SE': round(se, 4), 'SD': round(sd, 4),
            'min': min(d), 'max': max(d),
            'n_pos': sum(1 for x in d if x > 0), 'n_zero': sum(1 for x in d if x == 0),
            'n_neg': sum(1 for x in d if x < 0),
            'hist': {str(k): dist[k] for k in sorted(dist)}}

# ---------- inventory ----------
splits = json.loads((P3 / 'splits9.json').read_text())
dev9 = splits['dev9']; hold10 = splits['holdout10']
dev9s, hold10s = set(dev9), set(hold10)
gold10 = [json.loads(l) for l in (P3 / 'holdout10/test_gold.jsonl').read_text().splitlines() if l.strip()]
gold10_ids = sorted(g['id'] for g in gold10)
assert gold10_ids == sorted(hold10), 'splits9 holdout10 != gold file ids'

def cases_ids(rel):
    p = P3 / rel
    if not p.exists() or p.stat().st_size == 0:
        return []
    return sorted(json.loads(l)['id'] for l in p.read_text().splitlines() if l.strip())

def cases_rows(rel):
    p = P3 / rel
    if not p.exists() or p.stat().st_size == 0:
        return []
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]

ym_all = cases_ids('expansion8/yimao/cases.jsonl')
ym_dev = sorted(set(ym_all) & dev9s); ym_hold = sorted(set(ym_all) & hold10s)
ym_unused = sorted(set(ym_all) - dev9s - hold10s)

lr3_rows = cases_rows('expansion9/liuren-chen1/cases.jsonl') + cases_rows('expansion9/liuren-chen2/cases.jsonl')
lr3_all = sorted(r['id'] for r in lr3_rows)
lr3_contam = {r['id']: r.get('contamination') for r in lr3_rows}
excluded_lr3 = ['LR3-103', 'LR3-106', 'LR3-108']  # HOST-ADJUDICATION: B / not-in-pool
lr3_eligible = sorted(set(lr3_all) - set(excluded_lr3))
lr3_dev = sorted(set(lr3_eligible) & dev9s); lr3_hold = sorted(set(lr3_eligible) & hold10s)
lr3_unused = sorted(set(lr3_eligible) - dev9s - hold10s)

dt_rows = cases_rows('expansion8/duanyi-tianji/cases.jsonl')
ds_rows = cases_rows('expansion8/ditian-sui/cases.jsonl')
mt_rows = cases_rows('expansion8/mingli-tanyuan/cases.jsonl')
zw_rows = cases_rows('expansion8/ziwei/cases.jsonl')

inv = {
 'yimao': {'total': len(ym_all), 'in_dev9': len(ym_dev), 'in_holdout10': len(ym_hold),
           'unused': len(ym_unused), 'unused_ids': ym_unused,
           'dev_ids': ym_dev, 'holdout_ids': ym_hold},
 'lr3': {'total_raw': len(lr3_all), 'all_ids': lr3_all,
         'excluded_by_adjudication': excluded_lr3,
         'eligible_A_low_plus_devonly': len(lr3_eligible),
         'in_dev9': len(lr3_dev), 'in_holdout10': len(lr3_hold),
         'unused_eligible': len(lr3_unused), 'unused_ids': lr3_unused,
         'dev_ids': lr3_dev, 'holdout_ids': lr3_hold,
         'dev_only': ['LR3-010'], 'contamination': lr3_contam},
 'duanyi_tianji': {'total_A': len(dt_rows), 'ids': sorted(r['id'] for r in dt_rows),
                   'in_dev9': len(set(r['id'] for r in dt_rows) & dev9s),
                   'in_holdout10': len(set(r['id'] for r in dt_rows) & hold10s),
                   'unused': len(set(r['id'] for r in dt_rows) - dev9s - hold10s),
                   'contamination': {r['id']: r.get('contamination') for r in dt_rows}},
 'ditian_sui': {'total_A': len(ds_rows), 'ids': sorted(r['id'] for r in ds_rows),
                'in_dev9': len(set(r['id'] for r in ds_rows) & dev9s),
                'in_holdout10': len(set(r['id'] for r in ds_rows) & hold10s),
                'unused': len(set(r['id'] for r in ds_rows) - dev9s - hold10s)},
 'mingli_tanyuan': {'cases_rows_B': len(mt_rows),
                    'holdout_eligible_true': sum(1 for r in mt_rows if r.get('holdout_eligible')),
                    'A_new': 0, 'inputs_files': len(list((P3 / 'expansion8/mingli-tanyuan/inputs').glob('*')))},
 'ziwei': {'cases_rows': len(zw_rows), 'inputs_files': len(list((P3 / 'expansion8/ziwei/inputs').glob('*')))},
 'dev9_n': len(dev9), 'holdout10_n': len(hold10),
}

# ---------- DiD anchors ----------
master_raw = json.loads((P3 / 'data/master-baseline-dev9.json').read_text())
master = {c: (v['total'] if isinstance(v, dict) else v) for c, v in master_raw.items()}
def load_ours(rnd):
    fs = json.loads((P3 / f'runs/{rnd}/final-scores.json').read_text())
    return {c: (v['total'] if isinstance(v, dict) else v) for c, v in fs['ours_axis2'].items()}, fs['stats']['ALL']
o28, st28 = load_ours('round28'); o29, st29 = load_ours('round29')

S = sorted(p.stem for p in (P3 / 'inputs10').glob('*.json'))
I9 = sorted(p.stem for p in (P3 / 'inputs9').glob('*.json'))
noncase10 = sorted(p.name for p in (P3 / 'inputs10').iterdir() if p.suffix != '.json')
noncase9 = sorted(p.name for p in (P3 / 'inputs9').iterdir() if p.suffix != '.json')
C = sorted(set(dev9) - set(S) - set(I9))
assert len(S) == 44 and len(I9) == 47 and len(C) == 396 and not (set(S) & set(I9))

# master consistency: final-scores.json carries no per-case master; both rounds' analyze
# scripts read the same data/master-baseline-dev9.json; headline master_mean must match.
master_check = {'r28_headline_master_mean': st28['master_mean'], 'r29_headline_master_mean': st29['master_mean'],
                'percase_master_source': 'data/master-baseline-dev9.json (single file, both rounds)',
                'inconsistent_cases': 0}

did = {
 'sets': {'S_inputs10': S, 'inputs9_switch': I9, 'C_control': C,
          'noncase_files_inputs10': noncase10, 'noncase_files_inputs9': noncase9},
 'master_check': master_check,
 'S_r28': seg_stats(S, o28, master), 'S_r29': seg_stats(S, o29, master),
 'C_r28': seg_stats(C, o28, master), 'C_r29': seg_stats(C, o29, master),
 'ALL_r28': seg_stats(sorted(dev9), o28, master), 'ALL_r29': seg_stats(sorted(dev9), o29, master),
 'S_delta_R29minusR28': delta_stats(S, o28, o29),
 'C_delta_R29minusR28': delta_stats(C, o28, o29),
 'S_percase': [{'id': c, 'ours_r28': o28[c], 'ours_r29': o29[c], 'master': master[c],
                'pair_r28': round(o28[c] - master[c], 4), 'pair_r29': round(o29[c] - master[c], 4),
                'delta': round(o29[c] - o28[c], 4)} for c in S],
}
out = {'inventory': inv, 'did': did}
(P3 / 'data/DID-ANCHORS-R30.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(json.dumps(inv, ensure_ascii=False, indent=1))
print('---DID---')
for k in ['S_r28', 'S_r29', 'C_r28', 'C_r29', 'ALL_r28', 'ALL_r29', 'S_delta_R29minusR28', 'C_delta_R29minusR28']:
    print(k, did[k] if 'delta' not in k else {kk: vv for kk, vv in did[k].items() if kk != 'hist'})
print('S delta hist', did['S_delta_R29minusR28']['hist'])
print('C delta hist', did['C_delta_R29minusR28']['hist'])
