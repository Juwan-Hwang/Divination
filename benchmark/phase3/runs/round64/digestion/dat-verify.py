# -*- coding: utf-8 -*-
import json, collections, re
base='/home/hatch/workspace/divination/benchmark/phase3'
d=json.load(open(f'{base}/data/case-annotations-r64.json'))
print('top keys', list(d.keys()), 'round', d['round'])
print('counts', d['counts'])
ann=d['annotations']; fl=d['flags']
assert len(ann)==129 and len(fl)==129
assert collections.Counter(a['disposition'] for a in ann)==collections.Counter(d['counts']['verdicts'])
assert all(fl[i]['case_id']==ann[i]['case_id'] and fl[i]['basis']==ann[i]['finding'] and fl[i]['manifest_carry_suggestion']==ann[i]['manifest_carry_suggestion'] for i in range(129))
need={'anon_id','case_id','disposition','finding','flag','manifest_carry_suggestion','relation','registered_round','sources_checked','source_seats'}
for a in ann:
    assert need<=set(a), a['case_id']
    assert a['registered_round']==64
    if a['disposition']=='部分成立': assert a['manifest_carry_suggestion']
print('relations:', collections.Counter(a['relation'].split('（')[0] for a in ann))
for a in ann:
    if a['relation'].startswith('新旗标') or a['relation'].startswith('同例新旨'):
        print(a['case_id'], a['disposition'], '|', a['relation'])
# addendum re-read
md=open(f'{base}/data/manifest-carryover-r64-addendum.md').read()
r63=json.load(open(f'{base}/data/case-annotations-r63.json'))
part=[a for a in r63['annotations'] if a['disposition']=='部分成立']
sec=md.split('## 一、')[1].split('## 对勘记录')[0]
assert sec.count('### A')==72
for a in part:
    assert a['finding'] in md and a['flag'] in md and f'「{a["manifest_carry_suggestion"]}」' in md
for disp in ('成立','不成立','未核'):
    ids=[a['case_id'] for a in r63['annotations'] if a['disposition']==disp]
    for cid in ids: assert f'- {cid}' in md, cid
print('addendum OK, bytes', len(md.encode()))
import os
print('json bytes', os.path.getsize(f'{base}/data/case-annotations-r64.json'))
print('special items', [s['item'] for s in d['special_checks']])
