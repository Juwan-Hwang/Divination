# -*- coding: utf-8 -*-
"""R88 数据席产出独立复核：回读两件产出，复算一切数字，逐段验尾。"""
import json, collections, pathlib
BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
a88 = json.load(open(BASE/'data/case-annotations-r88.json', encoding='utf-8'))
a87 = json.load(open(BASE/'data/case-annotations-r87.json', encoding='utf-8'))
assert a88['round'] == 88
assert len(a88['annotations']) == 309
assert a88['annotations'][:300] == a87['annotations']
print('dist', dict(collections.Counter(x['disposition'] for x in a88['annotations'])))
assert collections.Counter(x['disposition'] for x in a88['annotations']) == {'成立':14,'部分成立':238,'不成立':55,'未核':2}
new = a88['annotations'][300:]
assert len(new) == 9 and all(x['registered_round']==88 for x in new)
assert collections.Counter(x['disposition'] for x in new) == {'部分成立':3,'不成立':6}
print('new ids', [(x['case_id'], x['disposition'], x['flag'].split('：')[0]) for x in new])
for x in new:
    for k in ['anon_id','case_id','disposition','finding','flag','manifest_carry_suggestion','registered_round','relation','source_seats','sources_checked']:
        assert x.get(k), (x['case_id'], k)
assert sum(1 for x in a88['annotations'] if x['case_id']=='AS-307') == 2
assert len(a88['special_checks']) == 68 and a88['special_checks'][:63] == a87['special_checks']
assert a88['counts']['cases_total'] == 309
md = open(BASE/'data/manifest-carryover-r88-addendum.md', encoding='utf-8').read()
for marker in ['（§一毕）','（§二毕）','（§三毕）','（§四毕）','（§五毕）','（全文毕）']:
    assert marker in md, marker
assert md.count('：落实——层注记逐字全等') == 43
for s in ['落实 43／维持 0／订正 0','CYJ-006','309 件＝300＋9','基线六处经 R88 盘上','CZ-QX 维持 **16**','fidelity 例外 **46 件**','紫微池挂起 **6 项**']:
    assert s in md, s
print('addendum segment tails OK; 43-case lines OK')
for p in ['data/case-annotations-r88.json','data/manifest-carryover-r88-addendum.md']:
    fp = BASE/p; print(p, fp.stat().st_size, 'bytes')
print('VERIFY ALL OK')
