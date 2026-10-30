import json, pathlib
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
neg = json.loads((base/'runs/round60/diagnosis/lr-negatives-dev60.json').read_text())
fs = json.loads((base/'runs/round60/final-scores.json').read_text())
rows=[]
for n in neg['negatives']:
    cid=n['case_id']
    card=json.loads((base/f'inputs-dev12/{cid}.json').read_text())
    book=card.get('provenance',{}).get('book')
    timing=fs['ours_sub'][cid]['timing']
    rows.append({**n,'book':book,'timing':timing})
for r in rows: print(json.dumps(r,ensure_ascii=False))
def mean(xs): return sum(xs)/len(xs)
for name,sub in [('all',rows),('dev8',[r for r in rows if r['in_dev8']]),('nondev8',[r for r in rows if not r['in_dev8']])]:
    print(name,'n',len(sub),'pair_mean',round(mean([r['pair_diff'] for r in sub]),3),'timing_mean',round(mean([r['timing'] for r in sub]),3))
    print(' timing=0',[r['case_id'] for r in sub if r['timing']==0])
    print(' 0<t<1',[(r['case_id'],r['timing']) for r in sub if 0<r['timing']<1])
    print(' t=1',[r['case_id'] for r in sub if r['timing']==1.0])
    print(' t>1',[(r['case_id'],r['timing']) for r in sub if r['timing']>1])
print('guide',sum(1 for r in rows if '大六壬占验指南' in (r['book'] or '')),'nonguide',sum(1 for r in rows if '大六壬占验指南' not in (r['book'] or '')))
