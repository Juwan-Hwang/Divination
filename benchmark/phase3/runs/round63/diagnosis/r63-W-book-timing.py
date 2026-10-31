import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
neg = json.load(open(base/'runs/round63/diagnosis/lr-negatives-dev63.json'))
fs = json.load(open(base/'runs/round63/final-scores.json'))
ours_sub = fs['ours_sub']
rows=[]
for n in neg['negatives']:
    cid=n['case_id']
    card=json.load(open(base/f'inputs-dev12/{cid}.json'))
    book=card.get('provenance',{}).get('book')
    sub=ours_sub.get(cid, {})
    rows.append({**n, 'book':book, 'timing': sub.get('timing'), 'ours_total_sub': sub.get('total') if isinstance(sub,dict) else None, 'sub_keys': list(sub.keys()) if isinstance(sub,dict) else None})
    print(cid, '| dev8=',n['in_dev8'],'| diff=',n['pair_diff'],'| timing=',rows[-1]['timing'],'| book=',book)
def mean(xs): return sum(xs)/len(xs) if xs else None
all_d=[r['pair_diff'] for r in rows]
d8=[r['pair_diff'] for r in rows if r['in_dev8']]
nd8=[r['pair_diff'] for r in rows if not r['in_dev8']]
print('neg mean all', round(mean(all_d),4), len(all_d))
print('neg mean dev8', round(mean(d8),4), len(d8))
print('neg mean nondev8', round(mean(nd8),4), len(nd8))
for label, subset in [('all',rows),('dev8',[r for r in rows if r['in_dev8']]),('nondev8',[r for r in rows if not r['in_dev8']])]:
    ts=[r['timing'] for r in subset if r['timing'] is not None]
    print(label,'timing mean', round(mean(ts),4) if ts else None, 'n_t',len(ts))
    print(label,'timing==0',[r['case_id'] for r in subset if r['timing']==0])
    print(label,'0<t<1',[(r['case_id'],r['timing']) for r in subset if r['timing'] is not None and 0<r['timing']<1])
    print(label,'t==1',[r['case_id'] for r in subset if r['timing']==1.0])
    print(label,'t>1',[(r['case_id'],r['timing']) for r in subset if r['timing'] is not None and r['timing']>1])
print('guide count', sum(1 for r in rows if r['book'] and '大六壬占验指南' in r['book']))
print('nonguide', [r['case_id'] for r in rows if not (r['book'] and '大六壬占验指南' in r['book'])])
