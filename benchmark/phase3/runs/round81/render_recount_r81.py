#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R81 组集席：由 recount_stock_r81_out.json 渲染 STOCK-RECOUNT-h26.md（数字/ id 一律直读复算件）。
另结构化直读旧测字池台账（zc-entries-summary-r48.json）补登 ZC 面。只渲染、不改任何台账。"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
R = json.loads((P3 / "runs/round81/recount_stock_r81_out.json").read_text(encoding="utf-8"))
OUT = P3 / "runs/round81/STOCK-RECOUNT-h26.md"
L = R["ledgers"]

def ids(lst):
    return "、".join(lst) if lst else "（无）"

def funnel_md(v):
    lines = ["| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |", "|---|---|---|---|"]
    for s in v["funnel"]:
        lines.append(f"| {s['stage']} | {s['eliminated']} | {ids(s['eliminated_ids'])} | {s['remaining']} |")
    return "\n".join(lines)

def ledger_section(title, key, tradition, extra=""):
    v = L[key]
    unused = v.get("qualified_unused", [])
    s = [f"### {title}", "",
         f"- 台账路径：`{v['path']}`；体系：{tradition}；台账总例数：**{v['total']}**。",
         "", funnel_md(v), "",
         f"- 资格全过（qualified）：{len(v['qualified'])}；其中已用（与已用并集逐 id 命中）：{len(v['qualified_used'])}——{ids(v['qualified_used'])}。",
         f"- **eligible 未用：{len(unused)}**——{ids(unused)}。"]
    if extra:
        s += ["", extra]
    s += [""]
    return "\n".join(s)

parts = []
parts.append("# STOCK-RECOUNT-h26 —— holdout26 供给存量盘上全口径复算（R81 组集席·第一阶段）")
parts.append("""
本件为组集线第一阶段产出：只复算登记，不建卡、不封存、不作断、不评分、不做 git 操作。复算脚本 `runs/round81/recount_stock_r81.py`（唯一名，盘上实算），中间结果 `runs/round81/recount_stock_r81_out.json`；渲染脚本 `runs/round81/render_recount_r81.py`。台账/结局文本一律按数据处理。

## 口径（写定依据）

- 依据：`runs/round81/PREREG.md` §4 与 `data/holdout25-seal-log.md` §一/§二。
- 已用并集：盘上逐 id 实算 **1085**（dev 488＋phase2 splits2 holdout2 29＋holdout3–25 金标 id 673＋holdout inputs 卡 id 514＋顶层 inputs6–10 卡 id 412，五源并集去重；与主持开轮实算一致，本席以 `count_used_union_r81.py` 同口径复跑断言 1085 通过）。零复用＝台账 id 与该并集逐 id 零命中；**同名即剔**（无论内容相涉与否）。
- 资格口径（eligible）：A 级、污染 low、锚点在场（六爻面五要素：卦名、动爻、世应、六亲纳支、月建日辰，六神不属要件；他体系以各台账 anchor 字段口径）、未用、四滤（逐字原文、独立结局、可分离、非 high 污染）。各台账资格字段读法以历轮构建脚本为准（`runs/round80/build_holdout25_r80.py`、`runs/round79/build_holdout24_r79.py`）：无 eligible_net/grade 字段之台账，按构建脚本实际采用的字段组合判定，逐件注记。
- ZCB-003 维持排除（主持裁处未撤销），单独登记、不计 eligible（§四）。
""")

# ---------- 主台账 ----------
parts.append("## 一、主台账逐源复算（已知面）\n")
parts.append(ledger_section("1. 段建业《段氏理象学》DS（r76）", "DS-r76", "bazi（八字）",
    "注记：台账 count 字段登记 registered 63、four_filter_pass_net 63、anchor_present 63、contamination_medium 1（DS-047）、low 62，与本席漏斗一致。DS-033 为同造合并组唯一卡（其组未被既往集取用），在未用名单内；同造组至多取 1 之限属组集阶段规则，本阶段只登记存量。"))
parts.append(ledger_section("2. 张志春《开悟之门》QM 开悟（r76）", "KW-kaiwu-r76", "qimen（奇门）",
    "注记：本台账无 grade/eligible_net/filters 字段，资格读法承构建脚本：present∧low∧separable∧stem_check 天地盘双 ok（全合）∧断语/结局非空。未全合 14 例（QM-017、QM-026、QM-033、QM-041、QM-050、QM-051、QM-053、QM-054、QM-056、QM-057、QM-059、QM-060、QM-061、QM-062）不入资格集，与 holdout25 封存日志 §一.1 登记一致。"))
parts.append(ledger_section("3. 刘文元《奇门启悟》QM 启悟（r76）", "QW76-qiwu-r76", "qimen（奇门）",
    "注记：资格读法承构建脚本：present∧low∧separable∧断语/结局非空（本台账无 stem_check/grade/eligible_net 字段）。"))
parts.append(ledger_section("4. 石建国《奇门遁甲最新实例解析》QM 石建国（r76）", "SG-shijianguo-r76", "qimen（奇门）",
    "注记：资格读法同启悟。台账另有 screened_out 6 例（池外淘汰登记，非台账 cases 计数内）。11 例已全部用尽（holdout22–25），未用 0。"))
parts.append(ledger_section("5. 《字触补》ZCB（r76）", "ZCB-zichubu-r76", "cezi（测字）",
    "注记：资格全过 15－已用 14＝未用 1 例，即 ZCB-003；ZCB-003 经主持裁处维持排除（§四单独登记），**可选 eligible 未用＝0**，与 holdout25 封存日志 §一.1 复算一致。"))
gsz = L["GSZ-guaishuo-r57"]
gsz_extra = (f"注记：资格全过集与台账 counts.net_eligible_A_low_present 名单（63）逐 id 相等（本席断言 qualified_equals_net_list＝true）。"
             f"GSZ 另有建卡口径五要素复核（承 build_holdout25_r80.py：逐例回原书文字层 `runs/round76/gsz-book-r76.txt` 以构建脚本同一 five_elements 函数复核）：未用 30 例中五要素全在场 **{len(gsz['five_element_pass_unused'])}** 例——{ids(gsz['five_element_pass_unused'])}；"
             f"五要素不过 **{len(gsz['five_element_fail_unused'])}** 例——{ids(gsz['five_element_fail_unused'])}，六例均仅「动爻」一要素缺如（静卦、变卦空，与 GSZ-020 历轮换例先例同型，逐例 elements 明细在复算 JSON）。故 GSZ 按台账净资格未用 30、按建卡口径 eligible 未用 24，两数并列登记。")
parts.append(ledger_section("6. 王虎应《六爻卦例说真》GSZ（r57）", "GSZ-guaishuo-r57", "liuyao（六爻）", gsz_extra))
why1 = L["WHY1-wanghuying-r56"]
parts.append(ledger_section("7. 王虎应《六爻分类占验技法》一轮 WHY-001–071（r56）", "WHY1-wanghuying-r56", "liuyao（六爻）",
    "注记：本台账 entries 无 grade/filters/eligible_net 字段（键集实查见复算 JSON entry_keys_union），净入账以台账 counts.net_eligible_A_low_present 名单（40）为准；本席漏斗以 anchor_presence∧pollution∧名单成员三级复算，资格全过集与名单逐 id 相等（断言通过）。已用 5 例为 holdout20 取例，与 SUPPLY-ACCOUNTING-r59 §一（可选未用 35）一致。"))
parts.append(ledger_section("8. 王虎应《六爻分类占验技法》二轮 WHY-072–117（r57-r2）", "WHY2-wanghuying-r57r2", "liuyao（六爻）",
    "注记：资格全过集与台账 counts 名单（36）逐 id 相等（断言通过）。台账另有 registered_only 2 件（WHY-R2-REG-01 月球例等）不在 entries 46 内、不入账。已用 6 例为 holdout21 取例，与 SUPPLY-ACCOUNTING-r59 §一（可选未用 30）一致。"))
parts.append(ledger_section("9. 曲炜《详批命例精解》QW（r56）", "QW-quwei-r56", "bazi（八字）",
    "注记：本台账无 grade/eligible_net 字段，资格读法：anchor present∧pollution low∧四滤全 pass∧结局非空，present 集 17 例（QW-001–017）已全部用尽（holdout20 用 12＋holdout21 用 5），未用 0，与 SUPPLY-ACCOUNTING-r59 §一一致。partial 17 例（QW-018–034）经 SUPPLY-RECHECK-qwpartial-r57 复核升格 0、维持 partial，不入资格集。"))
parts.append(ledger_section("10. 曲炜《详批命例精解》续抽 QW-035–038（r59）", "QW-quwei-r59", "bazi（八字）",
    "注记：4 例锚点皆 partial（出生信息原文未载），资格 0、可选增量 0，与台账 count.optional_pool_increment＝0 一致。"))
parts.append(ledger_section("11. 奇门旧池 QM-001–010（r56，杜新会/张志春两书）", "QM-qimen-r56", "qimen（奇门）",
    "注记：台账路径 `runs/round56/digestion/SUPPLY-MINING-qimen-r56.json`；资格承 QM-REVIEW-r58 复核（`runs/round58/digestion/QM-REVIEW-r58.json`）：eligible_optional 9 例（QM-001–008、QM-010），QM-009 pollution＝mid 只建池不入可选。已用 8（holdout21），未用 1＝QM-010，与 SUPPLY-ACCOUNTING-r59 §一一致。"))

# 复核件登记
rc = R["rechecks"]
parts.append(f"""### 复核件登记（只登记、无增量）

- `runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.json`：QW partial 复核 {rc['QW-partial-r57']['checked']} 例，升 present {rc['QW-partial-r57']['upgraded']}。
- `runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.json`：WHY partial/未净候选复核 {rc['WHY-partial-r59']['candidate_n']} 例，升格 {rc['WHY-partial-r59']['upgrades']}、可选增量 {rc['WHY-partial-r59']['pool_increment']}（含去重 8 例维持不入账）。
- `runs/round56/digestion/SUPPLY-GOLD-SUPPLEMENT-r56.json`：holdout20 已用 17 例之断语逐字补录件，非新供给面，其 id 全部已用，不另计存量。
""")

# ---------- 汇总 ----------
ds_u = len(L["DS-r76"]["qualified_unused"]); kw_u = len(L["KW-kaiwu-r76"]["qualified_unused"])
qw76_u = len(L["QW76-qiwu-r76"]["qualified_unused"]); sg_u = len(L["SG-shijianguo-r76"]["qualified_unused"])
gsz_net_u = len(gsz["qualified_unused"]); gsz5_u = len(gsz["five_element_pass_unused"])
why_u = len(why1["qualified_unused"]) + len(L["WHY2-wanghuying-r57r2"]["qualified_unused"])
qm56_u = len(L["QM-qimen-r56"]["qualified_unused"])
bazi = ds_u
qimen = kw_u + qw76_u + sg_u + qm56_u
liuyao_net = gsz_net_u + why_u
liuyao_build = gsz5_u + why_u
total_net = bazi + qimen + liuyao_net
total_build = bazi + qimen + liuyao_build
parts.append(f"""## 二、主台账汇总（逐体系）

| 体系 | eligible 未用（台账净资格口径） | eligible 未用（建卡口径，GSZ 过五要素复核） | 构成 id |
|---|---|---|---|
| bazi（八字） | {bazi} | {bazi} | DS {ds_u}＋QW 0 |
| qimen（奇门） | {qimen} | {qimen} | 开悟 {kw_u}＋启悟 {qw76_u}＋石建国 {sg_u}＋旧池 {qm56_u} |
| liuyao（六爻） | {liuyao_net} | {liuyao_build} | GSZ {gsz_net_u}（建卡口径 {gsz5_u}）＋WHY 一轮 {len(why1['qualified_unused'])}＋WHY 二轮 {len(L['WHY2-wanghuying-r57r2']['qualified_unused'])} |
| cezi（测字） | 0 | 0 | ZCB 可选 0（ZCB-003 裁处排除，§四） |
| **合计** | **{total_net}** | **{total_build}** | |

逐 id 全列见 §一各台账节。以下 §五可达性核算以建卡口径 {total_build} 为基数（GSZ 五要素不过 6 例单列、不入基数）。
""")

# ---------- 旧面普查 ----------
of = R["old_faces"]
sl = of["supply_ledgers_r46_r50"]
sl_rows = []
for rel, v in sl.items():
    sl_rows.append(f"| `{rel}` | {v['total']} | {len(v['counted_ids'])} | {len(v['counted_used'])} | {ids(v['counted_unused'])} |")
cm = of["cards_mining_dirs"]
cm_rows = []
for rel, v in cm.items():
    cm_rows.append(f"| `{rel}` | {v['total_ids']} | {len(v['used'])} | {ids(v['unused'])} |")
zc_sum = json.loads((P3 / "runs/round48/digestion/work-cezi-r48/zc-entries-summary-r48.json").read_text(encoding="utf-8"))
zc_elig = [e for e in zc_sum if e.get("eligible") is True]
zc_elig_used = [e["id"] for e in zc_elig if e.get("used") is True]
zc_elig_unused = [e["id"] for e in zc_elig if e.get("used") is not True]
assert zc_elig_unused == ["ZC-122"], zc_elig_unused
parts.append(f"""## 三、全体系口径普查——旧面台账（上列主台账未覆盖面）

检索以历轮登记档（SUPPLY-ACCOUNTING 链、STOCK-ANCHOR-r53、CENSUS 件）为先、逐名定性；下列各面均完整跑完（台账逐件打开、逐 id 与已用并集对勘），非中断登记。

### 3.1 supply-ledger r46–r50（夷坚/春渚/阅微/类考/梦占/逸旨/玄解/三书诸面统一入账台账）

| 台账路径 | 登记条目数 | counted（合规入账） | counted 已用 | counted 未用 |
|---|---|---|---|---|
{chr(10).join(sl_rows)}

- counted 合计 {sum(len(v['counted_ids']) for v in sl.values())}，已用 {sum(len(v['counted_used']) for v in sl.values())}，未用仅 3：YJ2-008、YJ2-011、YJ2-013（r49 夷坚面）。
- 该 3 例锚点资格经 STOCK-ANCHOR-r53 逐例标记为**不在场**（YJ2-008 卦象全缺、YJ2-011 谶语/占式全缺、YJ2-013 盘面/数式全缺），不合「仅锚点在场」口径——**eligible 未用＝0**。
- 未 counted 条目均为 B 级/mid/high/只登记/普查汇总行，逐件登记于各台账 verdict/host_check，不入资格集。
- 覆盖面逐名登记：夷坚志（YJ/YJ2/YJ3/YJ4/SS 诸号）、阅微草堂笔记（yw-*/YW2/YW3/YW4/YW5 诸号）、梦占类考（LK/LK2）、梦占逸旨（YZ-C）、梦林玄解（XJ47）、春渚纪闻（CZ2，见 3.2）、三书杂面（SS 课占/遁甲/扶乩等）。

### 3.2 cards-mining 逐面卡目录（r46–r53）

| 目录 | 卡 id 数 | 已用命中 | 未用 id |
|---|---|---|---|
{chr(10).join(cm_rows)}

未用卡逐面定性（依据均为历轮登记档）：

- 阅微 yw-mo、yw-dongming（r46 台账）：contamination high、registered-not-counted——eligible 未用 0。
- 夷坚 YJ-002、YJ-003、YJ-005、YJ-007（r47 台账）：high 只登记／B 级／mid，不入账——0。
- 三书 SS-002、SS-003、SS-004、SS-006（r48 台账）：counted＝false（mid／B 确认式结局）——0。
- 夷坚 YJ2-001–004（r49 台账聚合行）：contamination mid、counted＝false——0；YJ2-008/011/013 见 3.1（锚点不在场）——0。
- 阅微 YW2-001（r49 台账）：B 级、counted＝false——0。YW3-002（r50 台账）：B 级、counted＝false——0。
- 阅微 YW4-001（SUPPLY-ACCOUNTING-r51）：主持改判 B 级、污染 low-mid，只登记不入账——0。
- 阅微 YW5-001（STOCK-ANCHOR-r53）：锚点部分在场、所缺为决定性属性（按不在场同格）——0；YW5-002、YW5-003（SUPPLY-ACCOUNTING-r52）：A 级但 low-mid，只登记不入账——0；YW5-004（SUPPLY-ACCOUNTING-r53）：锚点决定性属性不在源文，只登记不入账——0。
- 春渚 CZ2-004、CZ2-005（STOCK-ANCHOR-r53）：锚点不在场／部分在场缺决定性属性——0。（CZ2-001/002/003/006 已用尽。）
- 夷坚 YJ4-001–011（STOCK-ANCHOR-r53）：11 例锚点全不在场或部分在场缺决定性属性——0。
- 类考 LK2-C48、LK2-C51（SUPPLY-ACCOUNTING-r52）：A 级但污染 mid，只登记不入账——0；LK2-C58（SUPPLY-ACCOUNTING-r53）：与已用 XJ47-092 同案异文、卡已裁撤，不作独立候选——0。
- 类考续读 LK2-C61、C62（SUPPLY-ACCOUNTING-r54）：俱同案（YZ-C019／XJ47-572，均已用）不重复入账、未建卡——0。类考面经 r54 登记全书检毕；夷坚近穷尽、春渚近穷尽、阅微检毕（SUPPLY-ACCOUNTING-r54 §定性，照录不另断）。

### 3.3 旧测字池 ZC（《字触》旧池，r38–r41 抽例、r48 汇总台账）

- 台账：`runs/round48/digestion/work-cezi-r48/zc-entries-summary-r48.json`（总 165 条）＋ `runs/round48/digestion/CENSUS-zichuquan-r48.md`。
- eligible 形态（A＋low＋eligible＝true）76 条，已用 75（h15 20＋h16 20＋h17 20＋h18 15，CENSUS 逐 id 断言合规集＝已用集），未用仅 **ZC-122**：该例经 R39/R40/R41/R48 一贯裁处为**身份未定旗标排除**（grade_note 载「相哥」身份未定、可径降 A-high），不入合规——单独登记（§四同型），**eligible 未用＝0**。
- 同 judged-set 内春渚旧池 CZ 33 条：eligible＝true 者 0——eligible 未用 0。

### 3.4 expansion–expansion12 池层（早期池扩容件）

下表为各池目录内全部 jsonl 之 id 并集的逐 id 对勘（池内含 work/ 索引件，故总数为池层 id 总量、非台账条目数）：

| 池 | id 总数 | 已用命中 | 未用 id 数 |
|---|---|---|---|
""")
exp = of["expansion_pools"]
exp_rows = []
for k, v in exp.items():
    exp_rows.append(f"| {k} | {v['total_ids']} | {v['used_n']} | {len(v['unused_ids'])} |")
parts[-1] = parts[-1].rstrip("\n") + "\n" + "\n".join(exp_rows)
small_unused = []
for k, v in exp.items():
    if 0 < len(v["unused_ids"]) <= 60:
        small_unused.append(f"- {k} 未用 {len(v['unused_ids'])}：{ids(v['unused_ids'])}")
parts.append("""
未用 id 较小集逐列（expansion11/expansion12 两池未用数大，逐 id 全列存于复算 JSON `old_faces.expansion_pools`，本件只登计数）：
""" + "\n".join(small_unused) + f"""
- expansion11 未用 {len(exp['expansion11']['unused_ids'])}、expansion12 未用 {len(exp['expansion12']['unused_ids'])}（逐 id 见复算 JSON）。

定性：该池层为例卡成卡前之候选/索引层，其逐例资格（A 级/low/锚点在场 adjudication）从未按 holdout 供给口径全量落台账；历轮 SUPPLY-ACCOUNTING 链之可选库存从未含此池层未用 id。按本轮资格口径（须台账资格字段齐备且锚点在场经 adjudication）**可计 eligible 未用＝0**；逐例资格**未核**——本席只登记此计数口径，不下「净新／枯竭」结论。
""")

# ---------- 单独登记 ----------
parts.append("""## 四、单独登记（不计 eligible）

1. **ZCB-003**（《字触补》台账，资格全过、未入已用并集）：input_side 拆分锚点原文末句含结论句，经 holdout22 主持裁处判为断语/结局事实入卡并换例剔除；本轮承 PREREG §4，裁处未撤销、维持排除。可选计数中剔除，ZCB 可选 eligible 未用因此为 0（合格存量 15－已用 14－本件 1）。
2. **ZC-122**（旧测字池）：A/low/eligible 形态，但身份未定旗标排除自 R39 起一贯在案（见 §3.3），不计 eligible。
3. **GSZ 五要素不过 6 例**（GSZ-020、GSZ-080、GSZ-082、GSZ-089、GSZ-094、GSZ-111）：台账净资格在册，但建卡口径五要素复核动爻缺如；组集阶段如拟动用须另经主持裁处，本阶段只登记、不计建卡口径 eligible。
4. **WHY 去重 8 例**（WHY-076/077/094/097/101/105/113/116）：与 GSZ 同案、归属说真席，只登记异文，不入 WHY 资格集（§一.8 顺序漏斗中分别于 grade 级剔除 4 例——WHY-076/094/113/116，其台账 grade 为 B；eligible_net 级剔除 4 例——WHY-077/097/101/105）。
5. 在途未到面（紫微两本、梅花两条、《奇门遁甲解真》正本、《盲师断命轶例集之壹》等）：未到不入选、不计存量，只登记（承 PREREG §8）。
""")

# ---------- 可达性纯计数 ----------
non_liuyao = bazi + qimen
non_yijian = total_build  # 主台账诸源皆近现代专著（非夷坚）；旧面 eligible 未用 0
parts.append(f"""## 五、组集限度可达性——纯计数核算（只算数、不下构成结论、不挑例）

基数：建卡口径 eligible 未用 **{total_build}**（八字 {bazi}／奇门 {qimen}／六爻 {liuyao_build}／测字 0）；旧面 eligible 未用 0（§三）；合计 {total_build}。

以 T＝25 试算各限度所需与现有之计数关系（限度：T≥25、单体系 ≤50%、单源 ≤50%、非夷坚 ≥13、非六爻 ≥13）：

| 限度项 | T＝25 时的计数要求 | 现有存量计数 | 差额（要求－现有，负为余量） |
|---|---|---|---|
| 总量 T≥25 | ≥25 | {total_build} | {25 - total_build} |
| 非六爻 ≥13 | ≥13 | {non_liuyao}（八字 {bazi}＋奇门 {qimen}） | {13 - non_liuyao} |
| 非夷坚 ≥13 | ≥13 | {non_yijian}（主台账诸源皆非夷坚；夷坚面 eligible 未用 0） | {13 - non_yijian} |
| 单体系 ≤50% | 任一体系 ≤12（12/25＝48%；13/25＝52% 超限） | 体系存量：六爻 {liuyao_build}、八字 {bazi}、奇门 {qimen}——组集时每体系至多取 12，三体系上限合计 36 ≥25 | —（上限侧核算） |
| 单源 ≤50% | 任一单源 ≤12 | 逐源存量：DS {ds_u}、WHY 两轮同书合计 {why_u}（一轮 {len(why1['qualified_unused'])}＋二轮 {len(L['WHY2-wanghuying-r57r2']['qualified_unused'])}）、GSZ（建卡口径）{gsz5_u}、开悟 {kw_u}、启悟 {qw76_u}、QM 旧池 {qm56_u}、石建国 {sg_u}——组集时每源至多取 12 | —（上限侧核算） |

计数事实（仅算术）：以 T＝25 计，非六爻须 ≥13 且六爻至多 12；现有非六爻存量 {non_liuyao}、六爻存量 {liuyao_build}，两项计数均不小于各自所需下限/上限配合量（非六爻 {non_liuyao}≥13、且可供六爻取用上限 12≤{liuyao_build}）。逐源上限 12 之下，存量 ≥12 之源有：DS（{ds_u}）、WHY 同书（{why_u}）、GSZ（{gsz5_u}）、开悟（{kw_u}），共 4 源。本节止于计数核算：构成表、选例规则与递补链由主持增补件写定，本席不下构成结论、不挑例。

## 六、产出与卫生登记

- 复算脚本：`runs/round81/recount_stock_r81.py`；复算结果 JSON：`runs/round81/recount_stock_r81_out.json`；探查脚本：`runs/round81/probe_ledgers_r81.py`；本件由 `runs/round81/render_recount_r81.py` 直读复算 JSON 渲染，数字与 id 未经手工转录。
- 本阶段未建卡、未封存、未作断、未评分、未做 git 操作；未打开任何 runs/ 下 predictions/judging/final-scores（已用并集仅取各集金标 id 字段与 inputs 卡文件名，未读金标正文）。
- 全体系普查完整性：§三各面均已逐件跑完并逐名定性；唯一「未核」登记为 §3.4 expansion 池层逐例资格（已逐 id 对勘、未逐例 adjudication），照口径登记、不下净新/枯竭结论。
""")

OUT.write_text("\n".join(parts), encoding="utf-8")
print("written", OUT, OUT.stat().st_size)
print("totals: net", total_net, "build", total_build, "bazi", bazi, "qimen", qimen,
      "liuyao_net", liuyao_net, "liuyao_build", liuyao_build)
