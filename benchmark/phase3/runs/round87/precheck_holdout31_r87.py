# -*- coding: utf-8 -*-
"""holdout31 前置核查（R87 组集封存席，开工第一步）。

口径：runs/round87/PREREG.md §5＋PREREG-ADDENDUM-r87.md 构成定版＋
runs/round87/supply/CYJ-ANCHOR-REVIEW-r87.md §5 主持裁定（乙·收紧）。
产出：runs/round87/precheck-holdout31-seat-r87.json。
"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R87 = os.path.join(BASE, 'runs/round87')
OUT = os.path.join(R87, 'precheck-holdout31-seat-r87.json')

used = json.load(open(os.path.join(R87, 'used-ids-r87.json'), encoding='utf-8'))
assert isinstance(used, list) and len(used) == 1220, len(used)
used_set = set(used)
assert len(used_set) == 1220

ledger = json.load(open(os.path.join(BASE, 'runs/round85/lr-eligible-ledger-r85.json'), encoding='utf-8'))
DA_LED = ledger['六壬/《大六壬断案》']
BY_LED = ledger['六壬/《六壬辨疑·毕法案录》']
CYJ_LED = ledger['六壬/《六壬粹言》卷五占验']
CY_LED = ledger['六壬/《六壬粹言》卷六慕农占验附存']
YX_LED = ledger['六壬/《大六壬预测学》']

def unused(seq):
    return [i for i in seq if i not in used_set]

da_rest, by_rest = unused(DA_LED), unused(BY_LED)
cyj_rest, cy_rest, yx_rest = unused(CYJ_LED), unused(CY_LED), unused(YX_LED)
lr_unused_total = len(da_rest) + len(by_rest) + len(cyj_rest) + len(cy_rest) + len(yx_rest)
cy_fidelity = len(cyj_rest) + len(cy_rest)          # 裁定乙：常规 eligible 归 0，转 fidelity 例外登记
regular_eligible = lr_unused_total - cy_fidelity    # 含 YX 3（只登记、不在轮取源序内）
assert lr_unused_total == 216, lr_unused_total
assert cy_fidelity == 46, cy_fidelity
assert regular_eligible == 170, regular_eligible
assert len(da_rest) + len(by_rest) >= 14            # DA/BY 两源可取面足额（不足则停工回主持，本断言即停工点）

# 轮取（读法 B 自 DA 起重启；源序 DA→CY→BY，CY 常规 eligible 为 0 自动无取）
LR_SEL, di, bi = [], 0, 0
while len(LR_SEL) < 14:
    LR_SEL.append(da_rest[di]); di += 1
    if len(LR_SEL) >= 14:
        break
    LR_SEL.append(by_rest[bi]); bi += 1
LR_EXPECTED = ['DA-047', 'BY-022', 'DA-048', 'BY-023', 'DA-050', 'BY-024', 'DA-051',
               'BY-025', 'DA-054', 'BY-027', 'DA-055', 'BY-028', 'DA-057', 'BY-030']
assert LR_SEL == LR_EXPECTED, LR_SEL

# WHY 余面复算：STOCK-RECOUNT-h28 §7 未用 27＋§8 未用 30，扣已用后续取
WHY_S7 = ['WHY-012', 'WHY-016', 'WHY-022', 'WHY-023', 'WHY-024', 'WHY-025', 'WHY-026',
          'WHY-027', 'WHY-028', 'WHY-031', 'WHY-032', 'WHY-033', 'WHY-034', 'WHY-035',
          'WHY-036', 'WHY-037', 'WHY-038', 'WHY-039', 'WHY-040', 'WHY-041', 'WHY-042',
          'WHY-043', 'WHY-044', 'WHY-068', 'WHY-069', 'WHY-070', 'WHY-071']
WHY_S8 = ['WHY-080', 'WHY-081', 'WHY-082', 'WHY-083', 'WHY-084', 'WHY-085', 'WHY-086',
          'WHY-087', 'WHY-088', 'WHY-089', 'WHY-090', 'WHY-091', 'WHY-092', 'WHY-093',
          'WHY-095', 'WHY-096', 'WHY-098', 'WHY-099', 'WHY-100', 'WHY-103', 'WHY-104',
          'WHY-106', 'WHY-107', 'WHY-108', 'WHY-109', 'WHY-110', 'WHY-111', 'WHY-112',
          'WHY-114', 'WHY-115']
H30_WHY = ['WHY-025', 'WHY-026', 'WHY-027', 'WHY-028', 'WHY-031',
           'WHY-032', 'WHY-033', 'WHY-034', 'WHY-035', 'WHY-036']
assert all(i in used_set for i in H30_WHY)
why_s7_rest = [i for i in WHY_S7 if i not in used_set]
why_s8_rest = [i for i in WHY_S8 if i not in used_set]
why_rest_total = len(why_s7_rest) + len(why_s8_rest)
assert why_rest_total == 42, why_rest_total
WHY_SEL = why_s7_rest[:10]
assert WHY_SEL == ['WHY-037', 'WHY-038', 'WHY-039', 'WHY-040', 'WHY-041',
                   'WHY-042', 'WHY-043', 'WHY-044', 'WHY-068', 'WHY-069'], WHY_SEL

GSZ_SEL = ['GSZ-107', 'GSZ-108', 'GSZ-109', 'GSZ-110']
ORDER = LR_SEL + WHY_SEL + GSZ_SEL
assert len(ORDER) == 28 and len(set(ORDER)) == 28

# 1. 排除对逐 id 明核
ly_check = {x: (x in ORDER) for x in ('LY-015', 'LY-320')}
assert not any(ly_check.values())
# 2. 零复用逐 id 对勘并集 1220
overlap = [c for c in ORDER if c in used_set]
assert overlap == [], overlap
# 5. id 号段占用：对全部已封集 holdout*/inputs/ 文件名核对
existing = set()
for d in os.listdir(BASE):
    idir = os.path.join(BASE, d, 'inputs')
    if d.startswith('holdout') and os.path.isdir(idir):
        existing |= {fn[:-5] for fn in os.listdir(idir) if fn.endswith('.json')}
conflicts = [c for c in ORDER if c in existing]
assert conflicts == [], conflicts

precheck = {
    'seat': 'R87 holdout31 组集封存席（前置核查）',
    'ruling': 'runs/round87/PREREG.md §5＋PREREG-ADDENDUM-r87.md＋CYJ-ANCHOR-REVIEW-r87.md §5 主持裁定（乙·收紧）',
    'selection': {'liuren_wheel': LR_SEL, 'why': WHY_SEL, 'gsz': GSZ_SEL, 'order': ORDER},
    'exclusion_pair_check': {'checked': ['LY-015', 'LY-320'], 'in_selection': ly_check,
                             'conclusion': '两 id 均不在候选 28 例内，逐 id 明核（候选 id 空间 DA-/BY-/WHY-/GSZ-，与 LY- 不交叠）'},
    'zero_reuse_check': {'basis': 'runs/round87/used-ids-r87.json（1220 条、distinct 1220）',
                         'candidates': ORDER, 'overlap': overlap, 'conclusion': '交集为空集'},
    'lr_remaining_recount': {
        'ledger_unused_total': lr_unused_total,
        'by_source_unused': {'DA': len(da_rest), 'BY': len(by_rest), 'CYJ': len(cyj_rest),
                             'CY': len(cy_rest), 'YX': len(yx_rest)},
        'cy_regular_eligible_zero': {'fidelity_exception_unused': cy_fidelity,
                                     'basis': 'CYJ 专项复核裁定乙：CYJ/CY 两源盘体在场 0/55，仅式头者不计常规 eligible'},
        'regular_eligible_total': regular_eligible,
        'regular_eligible_note': '170＝DA 87＋BY 80＋YX 3（YX 承历轮不在轮取源序内、只登记）；与增补件登记订正值 170 逐值相符',
        'da_by_takeable': len(da_rest) + len(by_rest),
        'conclusion': 'DA/BY 两源可取面 167 ≥14，足额，不触发停工回主持'},
    'why_remaining_recount': {
        'stock_s7_unused': 27, 'stock_s8_unused': 30,
        's7_rest_after_used': why_s7_rest, 's8_rest_count': len(why_s8_rest),
        'h30_taken': H30_WHY, 'remaining_total': why_rest_total,
        'conclusion': '余面 42 与增补件登记值逐值相符；按台账序（一轮 §7 序在前）续取前 10＝WHY-037…044、068、069'},
    'id_occupancy_check': {'existing_sealed_input_ids_count': len(existing), 'conflicts': conflicts,
                           'conclusion': '28 id 逐一对全部已封集 holdout*/inputs/ 文件名核对零冲突'},
}
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(precheck, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'out': OUT, 'order': ORDER}, ensure_ascii=False))
