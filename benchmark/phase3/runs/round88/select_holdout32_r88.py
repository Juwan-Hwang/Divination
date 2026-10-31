# -*- coding: utf-8 -*-
"""holdout32 选例复算（R88 组集封存席，检查点 1）。

口径：PREREG-ADDENDUM-r88.md 构成句＋PREREG.md §4——T=28=六壬 14+六爻 14；
六壬轮取读法 B 自 DA 重启、DA/BY 交替逐源按台账序取未用（CY 常规 0 无取、
YX 不入）；六爻 WHY 台账序 WHY-070、WHY-071（§7 余）居前＋§8 序续取 12；
已用并集 used-ids-r88.json（1248）逐 id 零复用；LY-015/LY-320 逐 id 明核排除。
本脚本只落选例件，不建卡。
"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R88 = os.path.join(BASE, 'runs/round88')
OUT = os.path.join(R88, 'holdout32-selection-r88.json')

used = json.load(open(os.path.join(R88, 'used-ids-r88.json'), encoding='utf-8'))
assert isinstance(used, list) and len(used) == 1248, len(used)
used_set = set(used)
assert len(used_set) == 1248

ledger = json.load(open(os.path.join(BASE, 'runs/round85/lr-eligible-ledger-r85.json'), encoding='utf-8'))
da_all = ledger['六壬/《大六壬断案》']
by_all = ledger['六壬/《六壬辨疑·毕法案录》']
yx_all = ledger['六壬/《大六壬预测学》']
cy_all = ledger['六壬/《六壬粹言》卷六慕农占验附存']
cyj_all = ledger['六壬/《六壬粹言》卷五占验']

da_seq = [i for i in da_all if i not in used_set]
by_seq = [i for i in by_all if i not in used_set]
assert len(da_seq) == 80 and len(by_seq) == 73, (len(da_seq), len(by_seq))
yx_unused = [i for i in yx_all if i not in used_set]
assert yx_unused == ['YX-001', 'YX-003', 'YX-004']
cy_unused = [i for i in cy_all if i not in used_set]
cyj_unused = [i for i in cyj_all if i not in used_set]
# CY/CYJ 常规 eligible=0（裁定乙，盘体不在场仅式头）：未用 46 只登记不入轮取
assert len(cy_unused) + len(cyj_unused) == 46, (len(cy_unused), len(cyj_unused))
regular_remaining_before = len(da_seq) + len(by_seq) + len(yx_unused)
assert regular_remaining_before == 156, regular_remaining_before

# 轮取读法 B：自 DA 重启、DA/BY 交替各取一至 14 足额
LR_SEL, di, bi = [], 0, 0
while len(LR_SEL) < 14:
    LR_SEL.append(da_seq[di]); di += 1
    if len(LR_SEL) >= 14:
        break
    LR_SEL.append(by_seq[bi]); bi += 1
DA_SEL = [c for c in LR_SEL if c.startswith('DA-')]
BY_SEL = [c for c in LR_SEL if c.startswith('BY-')]
assert DA_SEL == ['DA-059', 'DA-060', 'DA-061', 'DA-062', 'DA-063', 'DA-064', 'DA-065'], DA_SEL
assert BY_SEL == ['BY-031', 'BY-032', 'BY-033', 'BY-034', 'BY-036', 'BY-037', 'BY-038'], BY_SEL
DA_FALLBACK = da_seq[di:di + 5]
BY_FALLBACK = by_seq[bi:bi + 5]

# WHY：§7 余序（STOCK-RECOUNT-h28 §7 eligible 未用 27，扣 h28 取 5、h30 取 10、
# h31 取 10 后余 2）＋§8 序（同件 §8 eligible 未用 30 全余）
why56 = json.load(open(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json'), encoding='utf-8'))
why57 = json.load(open(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json'), encoding='utf-8'))
net7 = why56['counts']['net_eligible_A_low_present']
net8 = why57['counts']['net_eligible_A_low_present']
assert len(net7) == 40 and len(net8) == 36
s7_remaining = [i for i in net7 if i not in used_set]
s8_remaining = [i for i in net8 if i not in used_set]
# §7 台账序以 net 名单序为准：h31 取用后余序须为 WHY-070、WHY-071 居前；
# net7 名单序中 068/069 在 070/071 前且已用，过滤后恰余此二例
assert s7_remaining == ['WHY-070', 'WHY-071'], s7_remaining
# §8 序：STOCK-RECOUNT-h28 §8 eligible 未用序（net8 名单序过滤已用后须与该序全等）
S8_ORDER_H28 = ['WHY-080', 'WHY-081', 'WHY-082', 'WHY-083', 'WHY-084', 'WHY-085',
                'WHY-086', 'WHY-087', 'WHY-088', 'WHY-089', 'WHY-090', 'WHY-091',
                'WHY-092', 'WHY-093', 'WHY-095', 'WHY-096', 'WHY-098', 'WHY-099',
                'WHY-100', 'WHY-103', 'WHY-104', 'WHY-106', 'WHY-107', 'WHY-108',
                'WHY-109', 'WHY-110', 'WHY-111', 'WHY-112', 'WHY-114', 'WHY-115']
assert s8_remaining == S8_ORDER_H28, s8_remaining
why_remaining_before = s7_remaining + s8_remaining
assert len(why_remaining_before) == 32
WHY_SEL = why_remaining_before[:14]
assert WHY_SEL == ['WHY-070', 'WHY-071', 'WHY-080', 'WHY-081', 'WHY-082', 'WHY-083',
                   'WHY-084', 'WHY-085', 'WHY-086', 'WHY-087', 'WHY-088', 'WHY-089',
                   'WHY-090', 'WHY-091'], WHY_SEL
WHY_FALLBACK = why_remaining_before[14:14 + 5]

ORDER = LR_SEL + WHY_SEL
assert len(ORDER) == 28 and len(set(ORDER)) == 28

# 前置核查：零复用／排除对／限度
overlap = [c for c in ORDER if c in used_set]
assert overlap == [], overlap
excl = {'LY-015': 'LY-015' in ORDER, 'LY-320': 'LY-320' in ORDER}
assert excl == {'LY-015': False, 'LY-320': False}
assert 'LY-015' in used_set and 'LY-320' in used_set  # 排除对本已在并集内、双重保险
src_counts = {'DA': len(DA_SEL), 'BY': len(BY_SEL), 'WHY': len(WHY_SEL)}
assert all(v <= 14 for v in src_counts.values())
assert len(LR_SEL) == 14 and len(WHY_SEL) == 14  # 单体系各 50.0%、非六爻 14>=13、非夷坚 28>=13

sel = {
 'set': 'holdout32', 'round': 88,
 'ruling': 'PREREG-ADDENDUM-r88.md 构成句＋PREREG.md §4（T=28=六壬14+六爻14）',
 'order': ORDER,
 'liuren_wheel': LR_SEL,
 'source_counts': src_counts,
 'da': {'ledger_total': len(da_all), 'unused_before': len(da_seq),
        'selected': DA_SEL, 'fallback_next': DA_FALLBACK,
        'unused_after': len(da_seq) - len(DA_SEL)},
 'by': {'ledger_total': len(by_all), 'unused_before': len(by_seq),
        'selected': BY_SEL, 'fallback_next': BY_FALLBACK,
        'unused_after': len(by_seq) - len(BY_SEL)},
 'cy': {'regular_eligible': 0, 'note': 'CY/CYJ 常规 eligible=0（裁定乙），轮取自动无取',
        'fidelity_unused': {'CY': cy_unused, 'CYJ': cyj_unused},
        'fidelity_unused_total': len(cy_unused) + len(cyj_unused)},
 'yx': {'in_wheel': False, 'unused': yx_unused, 'note': 'YX 3 例不入轮取源序、只登记'},
 'lr_regular_remaining_before': regular_remaining_before,
 'lr_regular_remaining_after': regular_remaining_before - 14,
 'why': {'s7_remaining_before': s7_remaining, 's8_remaining_before': s8_remaining,
         'remaining_before_total': len(why_remaining_before),
         'selected': WHY_SEL, 'fallback_next': WHY_FALLBACK,
         'remaining_after': why_remaining_before[14:],
         'remaining_after_total': len(why_remaining_before) - 14},
 'zero_reuse_check': {'used_union_size': len(used_set), 'overlap': overlap},
 'exclusion_pair_check': {'pair': ['LY-015', 'LY-320'], 'in_selection': excl,
                          'in_used_union': {'LY-015': 'LY-015' in used_set, 'LY-320': 'LY-320' in used_set}},
 'limits': {'T': 28, 'liuren_share': 0.5, 'liuyao_share': 0.5,
            'source_share_max': 0.5, 'non_yiji': 28, 'non_liuyao': 14,
            'pollution': 'low only（资格断言于建卡脚本逐例执行）'},
 'union_after_seal_expected': len(used_set) + 28,
}
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(sel, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'order': ORDER, 'source_counts': src_counts,
                  'lr_regular_after': sel['lr_regular_remaining_after'],
                  'why_after': sel['why']['remaining_after_total'],
                  'union_after': sel['union_after_seal_expected'],
                  'bytes': os.path.getsize(OUT)}, ensure_ascii=False))
