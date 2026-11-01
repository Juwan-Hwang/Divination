# R96 数据席收尾验合（只读）
import json
from collections import Counter
BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ann = json.load(open(f'{BASE}/data/case-annotations-r96.json'))
add = open(f'{BASE}/data/manifest-carryover-r96-addendum.md', encoding='utf-8').read()
assert ann['round'] == 96
assert len(ann['annotations']) == 555
assert Counter(a['disposition'] for a in ann['annotations']) == {'成立': 15, '部分成立': 452, '不成立': 85, '未核': 3}
assert len(ann['special_checks']) == 107
new = ann['annotations'][541:]
assert len(new) == 14 and all(a['registered_round'] == 96 for a in new)
# §三.1 三条逐例建议全文在附则内逐字在场
for cid in ('LY-615', 'MH-010', 'LY-342'):
    b = [a for a in new if a['case_id'] == cid]
    assert len(b) == 1 and b[0]['manifest_carry_suggestion'] in add, cid
# §三.2 轮级候选三条承接建议句在附则内在场
for frag in ('第八节执行面监测（只监测、不判读）：平台面全集 487／487 三项 100%',
             'holdout35 组集封存成立（封存执行中）：T＝28＝紫微 14＋六壬 14',
             'R96 B25 派单批注事故：主持误批注波及 YY2-003／004／005 之 trigger'):
    assert frag in add, frag
# §三.3 续接 39 件 id 全在附则 §三.3 段内
import re
sec33 = add.split('### 3.3')[1].split('### 3.4')[0]
for cid in ann['counts']['r96_judge_flags']['同旨续接_不重复立条']:
    assert cid in sec33, cid
# §五定版构成逐 id 在附则内
for zid in ('ZW-036', 'ZW-044', 'ZW-045', 'ZW-046', 'DA-082', 'DA-090', 'BY-054', 'BY-061'):
    assert zid in add, zid
print('VERIFY OK')
