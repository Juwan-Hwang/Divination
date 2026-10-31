# -*- coding: utf-8 -*-
"""R89 holdout33 封存席前置核查（工序1）：
(i) 28 id 逐 id 对 LY-015/LY-320 核对（零命中）；
(ii) 28 id 对 used-ids-r89.json（1276）逐 id 对撞（零交集），
    并复核 DA-069/BY-040 不在构成内；
(iii-a) DA 7 例回底本全文 cases_raw.json 核式盘四课三传实载
    （BY 7 例由页图直核，另件登记）。
构成以 PREREG-ADDENDUM-r89.md（更正版）为准。"""
import json

B = '/home/hatch/workspace/divination/benchmark/phase3'
DA = ['DA-066', 'DA-067', 'DA-068', 'DA-070', 'DA-072', 'DA-073', 'DA-074']
BY = ['BY-039', 'BY-041', 'BY-042', 'BY-043', 'BY-044', 'BY-045', 'BY-046']
WHY = ['WHY-092', 'WHY-093', 'WHY-095', 'WHY-096', 'WHY-098', 'WHY-099',
       'WHY-100', 'WHY-103', 'WHY-104', 'WHY-106', 'WHY-107', 'WHY-108',
       'WHY-109', 'WHY-110']
IDS = DA + BY + WHY
assert len(IDS) == 28 and len(set(IDS)) == 28

# (i) 排除对逐 id 核对
excl = {}
for cid in IDS:
    excl[cid] = {'LY-015': cid == 'LY-015', 'LY-320': cid == 'LY-320'}
assert not any(v['LY-015'] or v['LY-320'] for v in excl.values())
print('(i) LY-015/LY-320 逐 id 核对：28/28 零命中')

# (ii) 零复用对撞
used = json.load(open(B + '/runs/round89/used-ids-r89.json', encoding='utf-8'))
assert isinstance(used, list) and len(used) == 1276 and len(set(used)) == 1276
used_set = set(used)
inter = [cid for cid in IDS if cid in used_set]
assert not inter, inter
assert 'DA-069' not in IDS and 'BY-040' not in IDS
assert 'DA-069' in used_set and 'BY-040' in used_set  # 二者确属已用（h12）
print('(ii) used-ids-r89 1276 件逐 id 对撞：交集为空；DA-069/BY-040 不在构成内（且确在已用并集内）')

# (iii-a) DA 原卡（底本全文）式盘实载核查
raw = json.load(open(B + '/expansion12/liuren-duanan/scratch-archive/cases_raw.json',
                     encoding='utf-8'))
print('cases_raw type:', type(raw), 'len:', len(raw))
sample = raw[0] if isinstance(raw, list) else list(raw.values())[0]
print('sample keys:', list(sample.keys()) if isinstance(sample, dict) else sample)
