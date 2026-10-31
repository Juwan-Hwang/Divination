import json, pathlib, math, statistics
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
neg = json.loads((base/'runs/round81/diagnosis/lr-negatives-dev81.json').read_text())
fs = json.loads((base/'runs/round81/final-scores.json').read_text())
ana = fs.get('analysis_r81', {})
print(json.dumps(ana, ensure_ascii=False, indent=1)[:12000])
print('---NEG CHECK---')
negs = neg['negatives']
print('n_negative field', neg['n_negative'], 'len', len(negs), 'total', neg['n_liuren_total'])
for seg_name, filt in [('dev8', lambda x: x['in_dev8']), ('LR3', lambda x: not x['in_dev8']), ('combined', lambda x: True)]:
    s=[x for x in negs if filt(x)]
    diffs=[x['pair_diff'] for x in s]
    print(seg_name, len(s), 'sum', sum(diffs), 'mean_neg', sum(diffs)/len(diffs) if diffs else None, 'median_neg', statistics.median(diffs) if diffs else None)
    # self-consistency
    bad=[x['case_id'] for x in s if abs(x['ours']-x['master']-x['pair_diff'])>1e-9]
    print('  pair_diff inconsistent', bad)
    bad2=[x['case_id'] for x in s if fs['ours_axis2'].get(x['case_id'])!=x['ours']]
    print('  ours_axis2 mismatch', bad2)
    bad3=[x['case_id'] for x in s if fs['ours_sub'].get(x['case_id'],{}).get('total')!=x['ours']]
    print('  ours_sub mismatch', bad3)
print('---BOOKS---')
for x in negs:
    cid=x['case_id']
    p=base/f'inputs-dev12/{cid}.json'
    d=json.loads(p.read_text())
    print(cid, '|', d.get('provenance',{}).get('book'))
print('---ALL LIUREN OURS for segment means (need master baseline? not allowed)---')
# segment info from analysis: print families/per_tradition
