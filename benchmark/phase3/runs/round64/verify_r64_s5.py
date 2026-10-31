import json, os
BASE='/home/hatch/workspace/divination/benchmark/phase3'
b=json.load(open(f'{BASE}/runs/round64/batches.json'))
ids=b['B13']+b['B14']+b['B15']
cm=ru=di=0; total=0; lines=[]
for cid in ids:
    p=f'{BASE}/runs/round64/predictions/{cid}.json'
    d=json.load(open(p))
    assert d['case_id']==cid
    assert set(d.keys())=={'case_id','prediction_text','basis','confidence','trigger'}, d.keys()
    assert 0<d['confidence']<=1
    assert set(d['trigger'].keys())=={'changed_main','reserve_used','disputed','reason'}
    assert 'tradition' in d['basis'].split('\n')[0] and 'systems_used' in d['basis']
    assert 'R61-REV1-2' in d['basis'] and 'R61-REV1-4' in d['basis']
    assert '動化方向' in d['basis'] and '反轉條件' in d['basis']
    cm+=d['trigger']['changed_main']; ru+=d['trigger']['reserve_used']; di+=d['trigger']['disputed']
    sz=os.path.getsize(p); total+=sz
    lines.append(f'{cid}.json {sz}')
print('files ok:', len(ids), 'total bytes:', total)
print('trigger counts: changed_main=%d reserve_used=%d disputed=%d'%(cm,ru,di))
print('\n'.join(lines))
