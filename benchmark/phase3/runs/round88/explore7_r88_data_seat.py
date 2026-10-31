import json, pathlib
base=pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
ann=json.load(open(base/'data/case-annotations-r87.json'))
for cid in ['DS-034','DS-040']:
    for a in ann['annotations']:
        if a['case_id']==cid:
            print(cid, json.dumps(a, ensure_ascii=False)[:1600]); print()
# check R87 manifest cases sha vs R88
import hashlib
for r in ['round87','round88']:
    m=json.load(open(base/f'runs/{r}/judging/outcome-manifest.json'))
    cs=json.dumps(m['cases'], ensure_ascii=False, sort_keys=True)
    print(r, 'cases sha', hashlib.sha256(cs.encode()).hexdigest(), 'ncases', len(m['cases']))
    print(r, '_r82 layer', len(m.get('_r82_carryover_notes_addendum',{})), list(m.get('_r82_carryover_notes_addendum',{}).keys()))
# pending: BZ-029/BZ-040 in annotations?
ids=[a['case_id'] for a in ann['annotations']]
print('BZ-029 in ann?', 'BZ-029' in ids, 'BZ-040?', 'BZ-040' in ids, '未核 ids', [a['case_id'] for a in ann['annotations'] if a['disposition']=='未核'])
# acceptance entries sample full for GSZ-105 (不成立 acceptance) to copy field structure
for a in ann['annotations']:
    if a['case_id'] in ('GSZ-105','WHY-027') and a.get('registered_round')==87:
        print(a['case_id'], json.dumps(a, ensure_ascii=False)[:1400]); print()
