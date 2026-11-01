#!/usr/bin/env python3
# W58 (R95) 复算脚本：清单自洽、承登记聚合、分族双报、书目分源、逐例表行数断言。
# 承登记标定以 W56 件 (round93 DIAG-LR-weight-dev93.md) §2 为可核原件；
# W57 件 (round94 DIAG-LR-weight-dev94.md) 盘上截断于 §2 LR3-104 行中段，其 §2 前段与本表对勘一致。
import json, math, re, pathlib

BASE = pathlib.Path('/home/hatch/workspace/divination')
NEG = json.load(open(BASE/'benchmark/phase3/runs/round95/diagnosis/lr-negatives-dev95.json'))
NEG94 = json.load(open(BASE/'benchmark/phase3/runs/round94/diagnosis/lr-negatives-dev94.json'))

assert NEG['n_negative'] == 23 and len(NEG['negatives']) == 23
for x in NEG['negatives']:
    assert abs(x['ours'] - x['master'] - x['pair_diff']) < 1e-9, x
    assert x['pair_diff'] < 0
ids95 = [x['case_id'] for x in NEG['negatives']]
ids94 = {x['case_id'] for x in NEG94['negatives']}
assert sorted(set(ids95) - ids94) == ['LR3-010', 'LR3-114']
assert sorted(ids94 - set(ids95)) == ['LR-001', 'LR2-018', 'LR2-022', 'LR3-004', 'LR3-112']

# 承登记主标（W56 §2 原样；LR3-010/LR3-114/OC-029/LR3-008/LR3-104 为 UNC）
CODE = {
 'LR2-013': ('E', ''), 'LR2-014': ('D', ''), 'LR2-015': ('W', '硬核'),
 'LR2-016': ('D', ''), 'LR2-017': ('W', '硬核'), 'LR2-019': ('E', ''),
 'LR2-021': ('A', '＊'), 'LR2-023': ('C', '＊'), 'LR2-024': ('C', '＊'),
 'LR3-002': ('W', '硬核'), 'LR3-006': ('E', ''), 'LR3-008': ('UNC', ''),
 'LR3-010': ('UNC', ''), 'LR3-101': ('W', '＊'), 'LR3-104': ('UNC', ''),
 'LR3-107': ('A', ''), 'LR3-110': ('D', ''), 'LR3-114': ('UNC', ''),
 'LR3-116': ('A', ''), 'OC-026': ('E', ''), 'OC-027': ('C', '＊'),
 'OC-029': ('UNC', ''), 'OC-030': ('A', ''),
}
assert set(CODE) == set(ids95), (set(CODE) ^ set(ids95))

def se(p, n):
    return round(100 * math.sqrt(p * (1 - p) / n), 1) if n else None

def seg_stats(rows):
    d = [x['pair_diff'] for x in rows]
    return len(d), round(sum(d), 2), round(sum(d) / len(d), 3), sorted(d)[len(d) // 2] if len(d) % 2 else round((sorted(d)[len(d)//2-1] + sorted(d)[len(d)//2]) / 2, 3)

dev8 = [x for x in NEG['negatives'] if x['in_dev8']]
lr3 = [x for x in NEG['negatives'] if not x['in_dev8']]
print('dev8', seg_stats(dev8)); print('LR3', seg_stats(lr3)); print('all', seg_stats(NEG['negatives']))

coded = [c for c in ids95 if CODE[c][0] != 'UNC']
unc = [c for c in ids95 if CODE[c][0] == 'UNC']
print('coded n', len(coded), 'UNC', unc)
from collections import Counter
print('主标分布(已标定):', Counter(CODE[c][0] for c in coded))
for name, rows in [('dev8', dev8), ('LR3', lr3), ('all-coded', None)]:
    cids = [x['case_id'] for x in rows] if rows else coded
    cc = [c for c in cids if CODE[c][0] != 'UNC']
    w = [c for c in cc if CODE[c][0] == 'W']; wh = [c for c in w if CODE[c][1] == '硬核']
    n = len(cc)
    print(f'{name}: coded n={n} W接口 {len(w)}/{n}={100*len(w)/n:.1f}% SE {se(len(w)/n,n)}pp; 硬核 {len(wh)}/{n}={100*len(wh)/n:.1f}% SE {se(len(wh)/n,n)}pp')
for denom_name, denom in [('清单23', ids95), ('总例30', None)]:
    w = [c for c in coded if CODE[c][0] == 'W']; wh = [c for c in w if CODE[c][1] == '硬核']
    n = len(denom) if denom else 30
    print(f'{denom_name}: W接口 {len(w)}/{n}={100*len(w)/n:.1f}% SE {se(len(w)/n,n)}pp; 硬核 {len(wh)}/{n}={100*len(wh)/n:.1f}% SE {se(len(wh)/n,n)}pp')

# 书目分源：逐例回读 inputs-dev12 provenance.book
books = {}
for cid in ids95:
    d = json.load(open(BASE/f'benchmark/phase3/inputs-dev12/{cid}.json'))
    books[cid] = d['provenance']['book']
assert all('大六壬占验指南' in b for b in books.values())
print('书目：指南 23/23; 门类著录', sum('门' in b for b in books.values()), '; 课次著录', sum('门' not in b for b in books.values()))

# 含混（承登记 ＊ 例）
amb = [c for c in coded if CODE[c][1] == '＊' or CODE[c][0] in ('A','C') and c in ('LR2-021','LR2-023','LR2-024','OC-027')]
amb = ['LR2-021', 'LR2-023', 'LR2-024', 'LR3-101', 'OC-027']
print('含混', amb, f'{len(amb)}/{len(coded)}={100*len(amb)/len(coded):.1f}% SE {se(len(amb)/len(coded),len(coded))}pp')
print('ALL ASSERTIONS PASSED')
