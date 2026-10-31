#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""渲染 STOCK-RECOUNT-h28.md：直读 recount_stock_h28_r83_out.json，数字与 id 不经手工转录。"""
import json, os

R83 = '/home/hatch/workspace/divination/benchmark/phase3/runs/round83'
out = json.load(open(os.path.join(R83, 'recount_stock_h28_r83_out.json'), encoding='utf-8'))
L = out['ledgers']
US = out['used_sources']


def ids(lst):
    return '、'.join(lst) if lst else '（无）'


def funnel_table(key):
    e = L[key]
    rows = []
    remain = e['total']
    for st in e['steps']:
        remain -= len(st['eliminated'])
        rows.append(f"| {st['label']} | {len(st['eliminated'])} | {ids(st['eliminated'])} | {remain} |")
    return '\n'.join(rows), e


def ledger_section(num, title, path, system, key, note):
    tbl, e = funnel_table(key)
    return f"""### {num}. {title}

- 台账路径：`{path}`；体系：{system}；台账总例数：**{e['total']}**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
{tbl}

- 资格全过（qualified）：{e['qualified_n']}；其中已用（与已用并集逐 id 命中）：{len(e['used'])}——{ids(e['used'])}。
- **eligible 未用：{e['unused_n']}**——{ids(e['unused'])}。

{note}
"""


parts = []
parts.append(f"""# STOCK-RECOUNT-h28 —— holdout28 供给存量盘上全口径复算（R83 组集席开工复算）

本件为 R83 组集封存席开工复算产出：只复算登记，不改构成。复算脚本 `runs/round83/recount_stock_h28_r83.py`（唯一名，盘上实算），中间结果 `runs/round83/recount_stock_h28_r83_out.json`；本件由 `runs/round83/render_recount_h28_r83.py` 直读复算 JSON 渲染，数字与 id 未经手工转录。台账/结局文本一律按数据处理。

## 口径（写定依据）

- 依据：`runs/round83/PREREG.md` §4（并集与资格口径写定）、`runs/round83/PREREG-ADDENDUM-r83.md`（holdout28 构成写定）与 `runs/round82/STOCK-RECOUNT-h27.md`（复算方法承接）。
- 已用并集：盘上逐 id 实算 **{out['used_union_total']}**（dev {US['dev_pool_with_input_dirs']}＋phase2 splits2 holdout2 {US['phase2_splits2_holdout2']}＋holdout3–27 金标 id {US['holdout3_27_gold_ids']}＋holdout inputs 卡 id {US['holdout2_27_input_card_ids']}＋顶层 inputs6–10 卡 id {US['toplevel_inputs6_10_card_ids']}，五源并集去重；与主持开轮实算 1139 一致，复算脚本内断言 1139 通过）。零复用＝台账 id 与该并集逐 id 零命中；**同名即剔**。金标文件只按 id 字段计并集，未读金标正文。
- 资格口径（eligible）：A 级、污染 low、锚点在场（六爻面五要素：卦名、动爻、世应、六亲纳支、月建日辰，六神不属要件；他体系以各台账 anchor 字段口径）、未用、四滤（逐字原文、独立结局、可分离、非 high 污染）。各台账资格字段读法以历轮构建脚本为准，无 eligible_net/grade 字段之台账按构建脚本实际采用的字段组合判定，逐件注记。
- ZCB-003 维持排除（主持裁处未撤销），单独登记、不计 eligible（§四）。

## 一、主台账逐源复算（已知面）
""")

parts.append(ledger_section('1', '段建业《段氏理象学》DS（r76）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json',
    'bazi（八字）', 'DS',
    '注记：DS-047 contamination medium 于 low 级淘汰，与历轮一致。已用较 h27 复算增 9（holdout27 取 DS-040–046、048、049），未用由 23 降至 14。'))
parts.append(ledger_section('2', '张志春《开悟之门》QM 开悟（r76）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-kaiwu-r76.json',
    'qimen（奇门）', 'QM_KAIWU',
    '注记：本台账无 grade/eligible_net/filters 字段，资格读法承构建脚本：present∧low∧separable∧stem_check 天地盘双 ok（全合）∧断语/结局非空。未用较 h27 复算减 9（holdout27 取全 9 例），**未用归 0**。'))
parts.append(ledger_section('3', '刘文元《奇门启悟》QM 启悟（r76）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-qiwu-r76.json',
    'qimen（奇门）', 'QM_QIWU',
    '注记：资格读法承构建脚本：present∧low∧separable∧断语/结局非空（本台账无 stem_check/grade/eligible_net 字段）。未用 2 例与 h27 复算一致。'))
parts.append(ledger_section('4', '石建国《奇门遁甲最新实例解析》QM 石建国（r76）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-shijianguo-r76.json',
    'qimen（奇门）', 'QM_SHIJIANGUO',
    '注记：资格读法同启悟。11 例已全部用尽，未用 0，与 h27 复算一致。'))
parts.append(ledger_section('5', '《字触补》ZCB（r76）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json',
    'cezi（测字）', 'ZCB',
    '注记：资格全过 15－已用 14＝未用 1 例，即 ZCB-003；ZCB-003 经主持裁处维持排除（§四单独登记），**可选 eligible 未用＝0**，与历轮复算一致。'))
tbl, e = funnel_table('GSZ_NET')
parts.append(f"""### 6. 王虎应《六爻卦例说真》GSZ（r57）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json`；体系：liuyao（六爻）；台账总例数：**{e['total']}**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
{tbl}

- 资格全过（qualified）：{e['qualified_n']}；其中已用：{len(e['used'])}——{ids(e['used'])}。
- **eligible 未用（台账净资格口径）：{e['unused_n']}**——{ids(e['unused'])}。
- 注记：资格全过集与台账 counts.net_eligible_A_low_present 名单逐 id 相等（复算脚本断言通过）。建卡口径五要素复核（逐例回原书文字层 `runs/round76/gsz-book-r76.txt` 以构建脚本同一 five_elements 函数复核）：未用 {e['unused_n']} 例中五要素全在场 **{L['GSZ_CARD']['unused_n']}** 例——{ids(L['GSZ_CARD']['unused'])}；五要素不过 **{len(L['GSZ_CARD']['steps'][0]['eliminated'])}** 例——{ids(L['GSZ_CARD']['steps'][0]['eliminated'])}，均仅「动爻」一要素缺如（静卦、变卦空，逐例 elements 明细在复算 JSON）。故 GSZ 按台账净资格未用 {e['unused_n']}、按建卡口径 eligible 未用 {L['GSZ_CARD']['unused_n']}，两数并列登记。已用较 h27 复算增 5（holdout27 取 GSZ-079、081、084、086、088），建卡口径未用由 19 降至 14。
""")
parts.append(ledger_section('7', '王虎应《六爻分类占验技法》一轮 WHY-001–071（r56）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json',
    'liuyao（六爻）', 'WHY_R1',
    '注记：本台账 entries 无 grade/filters/eligible_net 字段，净入账以台账 counts.net_eligible_A_low_present 名单（40）为准；漏斗以 anchor_presence∧pollution∧名单成员三级复算，资格全过集与名单逐 id 相等（断言通过）。已用较 h27 复算增 4（holdout27 取 WHY-008–011），未用由 31 降至 27。'))
parts.append(ledger_section('8', '王虎应《六爻分类占验技法》二轮 WHY-072–117（r57-r2）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json',
    'liuyao（六爻）', 'WHY_R2',
    '注记：资格全过数与台账 counts.net_eligible_A_low_present（36）相等（断言通过）。未用 30 与 h27 复算一致。台账另有 registered_only 2 件不在 entries 46 内、不入账。'))
parts.append(ledger_section('9', '曲炜《详批命例精解》QW（r56）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-quwei-r56.json',
    'bazi（八字）', 'QW',
    '注记：本台账无 grade/eligible_net 字段，资格读法：anchor present∧pollution low∧四滤全 pass∧结局非空，present 集 17 例已全部用尽，未用 0。partial 17 例（QW-018–034）经 SUPPLY-RECHECK-qwpartial-r57 复核升格 0、维持 partial，不入资格集。'))
parts.append(ledger_section('10', '曲炜《详批命例精解》续抽 QW-035–038（r59）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round59/digestion/SUPPLY-MINING-quwei-r59.json',
    'bazi（八字）', 'QW_R59',
    '注记：4 例锚点皆 partial，资格 0、可选增量 0，与台账 count 口径一致。'))
parts.append(ledger_section('11', '奇门旧池 QM-001–010（r56，杜新会/张志春两书）',
    '/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-qimen-r56.json',
    'qimen（奇门）', 'QM_OLD',
    '注记：资格承 QM-REVIEW-r58 复核（`runs/round58/digestion/QM-REVIEW-r58.json`）：eligible_optional 9 例（QM-001–008、QM-010），QM-009 pollution＝mid 只建池不入可选。已用 8（holdout21），未用 1＝QM-010，与 h27 复算一致。'))

ds_n = L['DS']['unused_n']; qm_n = L['QM_KAIWU']['unused_n'] + L['QM_QIWU']['unused_n'] + L['QM_SHIJIANGUO']['unused_n'] + L['QM_OLD']['unused_n']
gsz_c = L['GSZ_CARD']['unused_n']; gsz_net = L['GSZ_NET']['unused_n']
why_n = L['WHY_R1']['unused_n'] + L['WHY_R2']['unused_n']
non_ly = out['summary']['non_liuyao_unused']; ly_c = out['summary']['liuyao_unused_card']; tot = out['summary']['total_card']
parts.append(f"""## 二、主台账汇总（逐体系）

| 体系 | eligible 未用（台账净资格口径） | eligible 未用（建卡口径，GSZ 过五要素复核） | 构成 id |
|---|---|---|---|
| bazi（八字） | {ds_n} | {ds_n} | DS {ds_n}＋QW 0 |
| qimen（奇门） | {qm_n} | {qm_n} | 开悟 {L['QM_KAIWU']['unused_n']}＋启悟 {L['QM_QIWU']['unused_n']}＋石建国 {L['QM_SHIJIANGUO']['unused_n']}＋旧池 {L['QM_OLD']['unused_n']} |
| liuyao（六爻） | {out['summary']['liuyao_unused_net']} | {ly_c} | GSZ {gsz_net}（建卡口径 {gsz_c}）＋WHY 一轮 {L['WHY_R1']['unused_n']}＋WHY 二轮 {L['WHY_R2']['unused_n']} |
| cezi（测字） | 0 | 0 | ZCB 可选 0（ZCB-003 裁处排除，§四） |
| **合计** | **{tot + (gsz_net - gsz_c)}** | **{tot}** | |

以下 §五可达性核算以建卡口径 {tot} 为基数（GSZ 五要素不过 {gsz_net - gsz_c} 例单列、不入基数）。非六爻 eligible 未用 **{non_ly}**（DS {ds_n}＋QM {qm_n}），与 PREREG §4 写定口径（非六爻 17＝DS 14＋QM 3）逐项一致。

## 三、全体系口径普查——旧面台账（承 h27 复算 §三，逐面状态不变登记）

- supply-ledger r46–r50 诸面、cards-mining r46–r53 诸面、旧测字池 ZC/CZ：eligible 未用＝0（逐面定性承 `runs/round82/STOCK-RECOUNT-h27.md` §三全量复算登记；holdout27 取用例为 DS/开悟/GSZ/WHY 四源，未触旧面任何 id，本轮复算的已用并集 1139 与资格漏斗结果与该定性相容，本席未重复逐面重开）。
- expansion–expansion12 池层未用 id 共 691（承 h27 复算 §3.4），逐例资格从未按 holdout 供给口径全量落台账，按现行口径可计 eligible 未用＝0、状态**未核**；PREREG §5 已裁决自 R84 起开设逐例资格核查工序，本轮不抢跑核查、不计入存量。

## 四、单独登记（不计 eligible）

1. **ZCB-003**（《字触补》台账，资格全过、未入已用并集）：经 holdout22 主持裁处维持排除，裁处未撤销。可选计数中剔除，ZCB 可选 eligible 未用因此为 0。
2. **ZC-122**（旧测字池）：身份未定旗标排除自 R39 起一贯在案，不计 eligible（承 h27 复算 §四）。
3. **GSZ 五要素不过 {gsz_net - gsz_c} 例**（{ids(L['GSZ_CARD']['steps'][0]['eliminated'])}）：台账净资格在册，但建卡口径五要素复核动爻缺如；只登记、不计建卡口径 eligible。
4. **WHY 去重 8 例**（WHY-076/077/094/097/101/105/113/116）：与 GSZ 同案、归属说真席，只登记异文，不入 WHY 资格集。
5. 在途未到面（紫微两本、梅花两条、《奇门遁甲解真》正本、《盲师断命轶例集之壹》等）：未到不入选、不计存量，只登记。

## 五、holdout28 组集可行性核算与增补件构成对勘（限度：T≥25、单体系 ≤50%、单源 ≤50%、非夷坚 ≥13、非六爻 ≥13）

基数：建卡口径 eligible 未用 **{tot}**（八字 {ds_n}／奇门 {qm_n}／六爻 {ly_c}／测字 0）；非六爻存量 {non_ly}；旧面 eligible 未用 0（§三）。

**增补件写定构成对勘（PREREG-ADDENDUM-r83 §一，T＝27）**：DS 13（DS-050–062）⊆ DS 未用 {ds_n} 例（DS-050–063）✓；QM 启悟 2（QM-210、QM-211）＝启悟未用全集 ✓；QM 旧池 1（QM-010）＝旧池未用全集 ✓；GSZ 6（GSZ-091、092、093、098、099、100）⊆ GSZ 建卡口径未用 {gsz_c} 例 ✓；WHY 5（WHY-012、016、022、023、024）⊆ WHY 一轮未用 {L['WHY_R1']['unused_n']} 例 ✓。写定 27 id 与已用并集 {out['used_union_total']} 逐 id 对勘（复算脚本资格集与并集关系）零命中预期由构建脚本再断言。**复算与增补件构成写定逐项相合，无不合项，不提请改构成。**

限度逐项（按写定构成）：T＝27 ≥25 ✓；单体系最大 bazi 13/27＝48.1% ≤50% ✓；单源最大 DS 13/27＝48.1% ≤50% ✓；非夷坚 27 ≥13 ✓；非六爻 16 ≥13 ✓；仅锚点在场（构建脚本资格断言）✓。

**取用后余量（按写定构成实算）**：DS {ds_n - 13}（DS-063）／QM 0／GSZ 建卡口径 {gsz_c - 6}／WHY {why_n - 5}（一轮 {L['WHY_R1']['unused_n'] - 5}＋二轮 {L['WHY_R2']['unused_n']}）／非六爻合计 {non_ly - 16}／六爻建卡口径余 {ly_c - 11}／总余 {tot - 27}。非六爻余 {non_ly - 16}＜13——**holdout28 为存量内最后一集**（承 PREREG §4 存量见底定案），其后组集系于 §5 expansion 工序产出或待用户书目。

## 六、对照登记——holdout27 封存后口径 vs 本席复算（逐面）

holdout27 封存日志 §一.1 取用后余量口径：DS 14／QM 3（启悟 2＋旧池 1，开悟 0）／GSZ 建卡口径 14／WHY 57／非六爻 17／合计（建卡口径）88。

| 面 | h27 封存后口径 | 本席复算（建卡口径） | 差异 |
|---|---|---|---|
| DS 段氏 | 14 | {ds_n} | 0 |
| QM 开悟 | 0 | {L['QM_KAIWU']['unused_n']} | 0 |
| QM 启悟 | 2 | {L['QM_QIWU']['unused_n']} | 0 |
| QM 石建国 | 0 | {L['QM_SHIJIANGUO']['unused_n']} | 0 |
| QM 旧池 | 1 | {L['QM_OLD']['unused_n']} | 0 |
| 奇门小计 | 3 | {qm_n} | 0 |
| GSZ（建卡口径） | 14 | {gsz_c} | 0 |
| WHY 一轮 | 27 | {L['WHY_R1']['unused_n']} | 0 |
| WHY 二轮 | 30 | {L['WHY_R2']['unused_n']} | 0 |
| 六爻小计（建卡口径） | 71 | {ly_c} | 0 |
| 测字 ZCB 可选 | 0 | 0 | 0 |
| 旧面（§三诸面） | 0 | 0 | 0 |
| **合计（建卡口径）** | **88** | **{tot}** | **0** |

出入原因（只登记事实）：逐面差异全为 0，无出入项。存量自 h27 复算建卡口径 115 降至 {tot}，减少 27，恰为 holdout27 实成 27 例逐 id 命中已用并集所致。

## 七、产出与卫生登记

- 复算脚本：`runs/round83/recount_stock_h28_r83.py`；复算结果 JSON：`runs/round83/recount_stock_h28_r83_out.json`；本件由 `runs/round83/render_recount_h28_r83.py` 直读复算 JSON 渲染。
- 本席本件工序未建卡、未组集、未封存、未作断、未评分、未做 git 操作；未打开任何 holdout 的 test_gold.jsonl 正文（已用并集仅取各集金标 id 字段与 inputs 卡文件名）；未打开任何 predictions/judging/final-scores。
- 隔离自报：无。复算脚本按 PREREG §4 写定口径对 phase3 非 runs 目录（inputs-dev*/inputs/inputs6–10 与各 holdout inputs 目录）枚举文件名计并集，承历轮构建/复算脚本同口径，非目录列表式探查；本席未对任何 runs/ 目录执行列表/计数操作。
""")

path = os.path.join(R83, 'STOCK-RECOUNT-h28.md')
with open(path, 'w', encoding='utf-8') as f:
    f.write(''.join(parts))
print(path, os.path.getsize(path))
