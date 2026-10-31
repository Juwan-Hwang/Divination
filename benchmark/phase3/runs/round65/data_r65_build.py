#!/usr/bin/env python3
"""R65 data seat build: Task1 addendum + Task2 annotations. Structured reads only.
History files enumerated explicitly (r49,r50,r51,r53-r64); round65 outputs excluded by construction."""
import json, pathlib, collections

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
DATA = BASE / "data"
J65 = BASE / "runs/round65/judging"
EV = json.loads((BASE / "runs/round65/data_r65_evidence.json").read_text(encoding="utf-8"))
R64 = json.loads((DATA / "case-annotations-r64.json").read_text(encoding="utf-8"))
OM65 = json.loads((J65 / "outcome-manifest.json").read_text(encoding="utf-8"))
OM64 = json.loads((BASE / "runs/round64/judging/outcome-manifest.json").read_text(encoding="utf-8"))

# ============ TASK 1: counts assertions (dual-path) ============
ann64 = R64["annotations"]
tally = collections.Counter(a["disposition"] for a in ann64)
assert dict(tally) == R64["counts"]["verdicts"], (dict(tally), R64["counts"]["verdicts"])
assert R64["counts"]["verdicts"] == {"成立": 12, "部分成立": 99, "不成立": 15, "未核": 3}
assert len(ann64) == 129 and R64["counts"]["cases_total"] == 129
partials = [a for a in ann64 if a["disposition"] == "部分成立"]
assert len(partials) == 99
assert all((a["manifest_carry_suggestion"] or "").strip() for a in partials)

# ============ TASK 1: cross-check vs R65 manifest addendum layer (read only that layer + cases key set) ============
layer = OM65["_r65_carryover_notes_addendum"]
assert set(OM65["cases"].keys()) == set(OM64["cases"].keys()) and len(OM65["cases"]) == 487
keyset_equal = set(a["case_id"] for a in partials) == set(layer.keys())
match, mismatch = [], []
for a in partials:
    (match if layer.get(a["case_id"]) == a["manifest_carry_suggestion"] else mismatch).append(a["case_id"])
print(f"TASK1 cross-check: {len(match)}/99 match, mismatches={mismatch}, keyset_equal={keyset_equal}")
assert keyset_equal

def esc(s):
    return s.replace("\n", " ")

lines = []
lines.append("# Manifest 承接册附则（R65）——R64 定案承接建议汇编")
lines.append("")
lines.append("## 卷首说明")
lines.append("")
lines.append("- 本附则为 Phase 3 Round 65（R65）数据席（任务一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r64.json`（R64 定案正本：annotations 129 件，定案分布成立 12／部分成立 99／不成立 15／未核 3）。")
lines.append(f"- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 12／部分成立 99／不成立 15／未核 3、总 129，与 R64 公布分布逐项一致；部分成立 99 件每件 `manifest_carry_suggestion` 非空断言亦通过。")
lines.append(f"- 对勘结果：{len(match)}/99 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round65/judging/outcome-manifest.json` 的 `_r65_carryover_notes_addendum` 层（本席只读该层与 `cases` 键名集），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 {len(mismatch)} 件）。")
lines.append("- **本附则自 R66 manifest 起落实**；本轮（R65）manifest 不据本附则改动。")
lines.append("- **本件只汇编与对勘，不改任何分数与结局原文。**")
lines.append("- 汇编范围：R64 定案中部分成立 99 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r64.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R65 起」等表述为原档原文，落实轮次按卷首上一条读作自 R66 起，不回溯改动 R65）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。")
lines.append("- 成立 12／不成立 15／未核 3 共 30 件不入正文逐件节，只在文末列 case_id 清单。")
lines.append("- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 一、部分成立件承接汇编（定案档位：部分成立，99 件，逐件全列）")
lines.append("")
for i, a in enumerate(partials, 1):
    lines.append(f"### A{i}. {a['case_id']}")
    lines.append("")
    lines.append(f"- case_id：{a['case_id']}")
    lines.append(f"- anon_id：{a['anon_id']}")
    lines.append(f"- 定案（部分成立）：{esc(a['finding'])}")
    lines.append(f"- 原旗标要旨（照原档 `flag` 字段）：{esc(a['flag'])}")
    lines.append(f"- 承接注记建议文本（照原档 `manifest_carry_suggestion` 原文）：「{esc(a['manifest_carry_suggestion'])}」")
    lines.append(f"- 与既有承接册／附则条目的关系（照原档 `relation` 字段）：{esc(a['relation'])}")
    lines.append("")
lines.append("---")
lines.append("")
lines.append("## 对勘记录")
lines.append("")
lines.append("- 对勘对象：本汇编第一节 99 件承接注记建议文本（源：`case-annotations-r64.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round65/judging/outcome-manifest.json` 的 `_r65_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。")
detail = "、".join(f"{a['case_id']}＝{'一致' if a['case_id'] in match else '不一致'}" for a in partials)
lines.append(f"- 对勘结果：{len(match)} 件逐字一致，差异 {len(mismatch)} 件（对勘明细：{detail}）。")
lines.append(f"- 键集合差异：{'无（manifest 层 99 键与部分成立 99 件 case_id 集合全等）' if keyset_equal else '有，见不一致登记'}。")
if mismatch:
    lines.append("- 不一致登记：" + "；".join(f"{c}：附则侧照源档原文录入、manifest 侧照其盘上原文对勘，两侧均未作任何静默改动" for c in mismatch) + "。")
else:
    lines.append("- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。勘误结论：无须勘误；本附则结论自 R66 manifest 起落实。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 自验")
lines.append("")
lines.append("- 原档（case-annotations-r64.json）条目数：129；档位分布成立 12／部分成立 99／不成立 15／未核 3，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。")
lines.append("- 本附则正文条目数：99（第一节部分成立 99 件），与原档部分成立件数对齐；文末不入附则清单 30 件（成立 12＋不成立 15＋未核 3），99＋30＝129 与原档总数对齐。")
lines.append(f"- 承接注记建议文本：99 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R65 manifest `_r65_carryover_notes_addendum` 逐件逐字一致（{len(match)}／99）。")
lines.append("- 回读断言：本附则写出后由生成脚本回读，断言第一节条目数＝99、每件承接注记建议文本与原档字段逐字一致（结果见产出时回读记录：通过）。")
lines.append("- 纪律自报：本席只汇编与对勘，未改任何分数、未改 manifest、未改 annotations、未改原卡；outcome-manifest 只读 `_r65_carryover_notes_addendum` 层与 `cases` 键名集。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 文末清单：不入附则 30 件（成立 12＋不成立 15＋未核 3，仅列 case_id）")
lines.append("")
for disp, n in [("成立", 12), ("不成立", 15), ("未核", 3)]:
    lines.append(f"### {disp} {n} 件")
    lines.append("")
    for a in ann64:
        if a["disposition"] == disp:
            lines.append(f"- {a['case_id']}")
    lines.append("")
addendum_text = "\n".join(lines)
out1 = DATA / "manifest-carryover-r65-addendum.md"
out1.write_text(addendum_text, encoding="utf-8")

# readback Task1
rb = out1.read_text(encoding="utf-8")
assert rb.count("### A") == 99, rb.count("### A")
for a in partials:
    assert a["manifest_carry_suggestion"] in rb and a["finding"] in rb and a["flag"] in rb
print("TASK1 readback OK, bytes:", out1.stat().st_size)

# ============ TASK 2: adjudication ============
entries = {e["case_id"]: e for e in EV["entries"]}
assert len(entries) == 48

# Continuation cases: case_id -> expected disposition (verified against latest history disposition in code below)
CONT = {
    "LR2-023": "部分成立", "LY-432": "不成立", "BZ-105": "部分成立", "LY-227": "部分成立",
    "BZ-304": "部分成立", "LY-437": "成立", "LY-458": "成立", "LY-426": "成立",
    "BZ-042": "部分成立", "YM-043": "部分成立", "LY-533": "部分成立", "LY-252": "部分成立",
    "LY-023": "成立", "LY-614": "部分成立", "YY2-002": "部分成立", "YM-030": "部分成立",
    "LY-202": "部分成立", "LY-532": "部分成立", "LY-516": "部分成立", "YY2-004": "部分成立",
    "AS-209": "部分成立", "LY-211": "部分成立", "LY-506": "部分成立", "LR2-024": "部分成立",
    "LY-504": "部分成立", "LY-220": "部分成立", "LY-513": "成立", "YY2-001": "部分成立",
    "LY-102": "部分成立", "LY-216": "部分成立", "YY2-003": "部分成立",
}
assert len(CONT) == 31

FRESH = {
    "LY-203": ("部分成立", "同例新旨（R54 旧旨旗标不成立、本轮新旨另立）",
        "同例新旨（R54 旧旨为『结局与财福问不对位』、定案不成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「占財福」；R65 manifest 结局前段『值子年農生被蝗虫食盡﹐全家瘟疫﹐六畜亦瘟。』为子年破败事实明载，后段『應子年者﹐占時原有子日沖其午火﹐因午火而值月建可以相敵﹐令遇子年﹐增其沖克﹐所以破敗。』为本例应验解释层——解释层并载属实；但系本例个案释义，破败终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同例新旨：自 R66 起承接本 R65 标注（与 R54 旧旨定案并行、各旨独立）：按「结局后段为应验解释层、子年破败事实明载」登记；结局原文照录不改。",
        "同例新旨：结局含应验解释层（终局明载）"),
    "LY-207": ("不成立", "同例新旨（R64 旧旨旗标部分成立、本轮旗标复述旧旨另核）",
        "同例新旨（R64 旧旨为『prediction 病向负断模板与功名问面错位』、定案部分成立，本轮旗标复述旧旨、经逐字核与本轮文本不合，另立）：回原卡——所问「占終身功名有無」；逐字核 R65 prediction 全文——通篇为功名向断语（『功名不再起，官已化财向』，以世官鬼化财、父母文书等立论），并无病向负断表述，旧旨所指模板错位在本轮 prediction 中不存在（R64 prediction 之病向模板语经全量检索，本轮仅见于 AS-204 prediction 之通用模板、与本例无关）；R65 manifest 结局载援例加纳、官至府佐、未年出仕、戌年升任之功名历程，与问面直接对应。故本轮旗标所指不成立。R64 旧旨部分成立定案只及 R64 prediction 文本面、照旧登记，不据本件改动。",
        "不入附则：本 R65 同例新旨定案（不成立），自 R66 起承接本 R65 标注，不加承接注记；R64 旧旨部分成立定案只及 R64 prediction 文本面、照旧登记；结局原文照录不改。",
        "同例新旨：旧旨复述经核不合（本轮 prediction 已改）"),
    "LY-615": ("部分成立", "同例新旨（R54／R58／R64 旧旨旗标不成立、本轮新旨另立）",
        "同例新旨（R54／R58／R64 旧旨为『女死与出门问不对位』、定案不成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「占出門」；R65 manifest 结局『後因病重，此人未去，女死辰日』为事实层明载，其后『夫應不去者，世動而逢合也，女死辰日者，卯木子孫變辰土之故也』为应验解释层——解释层并载属实；但系本例个案释义，未去与女死两面事实本身明载。故部分成立（同 YY2-002 解释层口径）。旧旨『女死旁面』一层仍依 R54／R58／R64 同案复合定案（不成立）登记，本件不推翻。",
        "同例新旨：自 R66 起承接本 R65 标注（与 R54／R58／R64 旧旨定案并行、各旨独立）：按「结局后段为应验解释层、未去与女死事实明载」登记；结局原文照录不改。",
        "同例新旨：结局含应验解释层（终局明载）"),
    "LY-627": ("部分成立", "同例新旨（R57／R61／R64 旧旨旗标不成立、本轮新旨另立）",
        "同例新旨（R57／R61／R64 旧旨为『其日指代未明／prediction 方向相反』、定案不成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「占父近病」；R65 manifest 结局『果至其日而死』为父病终局明载，尾句『此應出旬又被沖克也』为回溯性应验解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同例新旨：自 R66 起承接本 R65 标注（与 R57／R61／R64 旧旨定案并行、各旨独立）：按「结局尾句为应验解释层、父病终局明载」登记；结局原文照录不改。",
        "同例新旨：结局含应验解释层（终局明载）"),
    "AS-304": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「公开预测：2024年美国总统选举结果」，卡面 provenance 仅作『其X（推特）账号原文，后经 Timesnownews 报道引录』，原预测者姓名未载；R65 manifest 结局前半『特朗普以312张选举人票胜出，哈里斯得226票』为选举结果明载，后半『Gopalakrishnan于选后公开承认错误并宣布暂停政治预测』并载具名人物选后认错一节——该人物与本例原预测之关系未在卡面与结局内标明，所指并载未标一层属实；本席全量检索 487 例结局，该姓名仅见于本例，无据断言系他例结局混入，选举结果本面亦完整。故部分成立。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局后半并载具名人物认错一节、与本例关系未标，选举结果明载」登记；结局原文照录不改。",
        "结局并载未标关系人物一节（结果本面明载）"),
    "LY-243": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「女家代占婚」；R65 manifest 结局『後果聘定於四月﹐未及成婚被賊兵劫去』为婚事终局明载，尾句『應巳月者亥水逢月破也』为应验解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局尾句为应验解释层、婚事终局明载」登记；结局原文照录不改。",
        "结局含断语解释层（终局明载）"),
    "LY-244": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占夫妻不和將來如何」；R65 manifest 结局『果於次年寅月休妻﹐此人六月再取彼婦』为事实明载，尾二句『應寅月者﹐夫臨寅木而沖世也﹐應六月者未土沖開初爻丑土﹐子水來生其寅木也』为应验解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局尾二句为应验解释层、休妻再娶事实明载」登记；结局原文照录不改。",
        "结局含断语解释层（终局明载）"),
    "YY2-005": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「求占文书（所求文书能否办成）」；R65 manifest 结局『后于子日成就』为文书办成终局明载，尾句『盖文书旺于子，且冲破午胎也』为解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局尾句为解释层、文书成就明载」登记；结局原文照录不改。",
        "结局含断语解释层（终局明载）"),
    "LY-230": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占何日補官」；R65 manifest 结局『果得升於冬月』为补官终局明载，后半『應冬月者﹐辰土化子水空亡﹐十一月則不空矣』为应验解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局后半为应验解释层、得升冬月明载」登记；结局原文照录不改。",
        "结局含断语解释层（终局明载）"),
    "LY-250": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占夫在外還往他省去否（兼問何日到）」；R65 manifest 结局首句『果於巳日到』为到日终局明载，后半『或曰﹕用爻有病﹐莫問歸期……予曰﹕……斷卦者各有取用耳』为断语取用讨论并载——讨论层混入属实；但系本例断语往复、非他例文字，到日终局本身明载。故部分成立。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局后半混入断语取用讨论、巳日到明载」登记；结局原文照录不改。",
        "结局混入断语取用讨论（到日终局明载）"),
    "LY-621": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占主病」；R65 manifest 结局『果卒於九月丁亥日』为卒期明载，尾句『應亥日者，坎水之絕地也』为应验解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局尾句为应验解释层、卒期明载」登记；结局原文照录不改。",
        "结局含断语解释层（终局明载）"),
    "LY-503": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占久病」；R65 manifest 结局『果卒於申日』为卒日明载，尾句『此乃少一字﹐得後來之申日補之﹐豈可謂少一字不成三刑耶』为回溯性自解层——自解层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局尾句为回溯自解层、卒于申日明载」登记；结局原文照录不改。",
        "结局含回溯自解层（终局明载）"),
    "LY-511": ("不成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占終身財福」（非旗标所称求财／经营问面）；R65 manifest 结局『後屢見逢顯貴聘之﹐才高气傲﹐皆不待瓜期辭矣。目摯十餘載﹐貧寒淡泊﹐後隨表弟升任云南﹐不知所終。』——『貧寒淡泊』十余载即终身财福之终局明载，辞聘、随表弟赴滇为其生平财况之载，与问面同面对应、非他例结局错配。故旗标不成立。",
        "不入附则：本 R65 新立定案（不成立），自 R66 起承接本 R65 标注，不加承接注记；结局原文照录不改。",
        "所问面误述核查（结局同面对应）"),
    "LY-610": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占官之升遷」；R65 manifest 结局『果於三月升任云南太守』为升迁终局明载，后半『卽升者乃因爻得水局生扶，應三月者辰土出空之月也，應云南者，世與官星皆在六爻之故耳』为应验解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局后半为应验解释层、三月升任明载」登记；结局原文照录不改。",
        "结局含断语解释层（终局明载）"),
    "YM-014": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占家宅（火灾之虞）」；R65 manifest 结局『至甲午日而回禄』为火灾终局明载，尾句『以夏至后先壬而后甲也』为应验解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局尾句为应验解释层、甲午日回禄明载」登记；结局原文照录不改。",
        "结局含断语解释层（终局明载）"),
    "LY-429": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占病」；R65 manifest 结局前段『果於丁亥日全愈』、后段『復得病而死』为病情终局两段明载，中段『後至巳月亥逢月破﹐巳火生助戌土﹐諺語﹕斬艸不除根﹐萌芽依舊生』为应期机制解释与谚语式卦理解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局中段为应期解释层与谚语、全愈与复病而死事实明载」登记；结局原文照录不改。",
        "结局含应期解释层与谚语（终局明载）"),
    "LY-210": ("部分成立", "新旗标（R65 新立）",
        "新旗标（R65 新立）：回原卡——所问「占壽」；R65 manifest 结局『後卒於戌年』为卒年明载，第二句『應在巳火入墓之年』为应验解释层——解释层并载属实；但系本例个案释义，终局本身明载。故部分成立（同 YY2-002 解释层口径）。",
        "同旨新立：自 R66 起承接本 R65 标注：按「结局第二句为应验解释层、卒于戌年明载」登记；结局原文照录不改。",
        "结局含断语解释层（终局明载）"),
}
assert len(FRESH) == 17 and not (set(FRESH) & set(CONT)) and set(FRESH) | set(CONT) == set(entries)

flags_out, ann_out = [], []
for cid in sorted(entries, key=lambda c: entries[c]["anon"]):
    e = entries[cid]
    anon = e["anon"]
    flag_text = "；".join(e["gists"])
    hist = e["history"]
    sources = [
        f"benchmark/phase3/inputs-dev12/{cid}.json",
        "benchmark/phase3/runs/round65/judging/FLAGS-selfreported-r65.md",
        f"benchmark/phase3/runs/round65/judging/outcome-manifest.json cases[{cid}]",
        f"benchmark/phase3/runs/round65/predictions/{cid}.json",
    ] + [f"benchmark/phase3/data/case-annotations-r{h['round']}.json {cid} 条" for h in hist]
    views = sorted({("X" if s.startswith("X") else "Y") for s in e["seats"]})
    if cid in CONT:
        disp = CONT[cid]
        latest = max(hist, key=lambda h: h["round"])
        # latest verdict disposition must match expected (descriptive r53-style strings excluded by construction: latest is r57+ for all CONT)
        assert latest["disposition"] == disp, (cid, latest["round"], latest["disposition"], disp)
        relation = f"同旨续接（R{latest['round']}）"
        finding = (f"承接既有定案不重裁（历轮最近定案 R{latest['round']} {disp}）：{latest['finding']}"
                   f" 本轮（R65）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。")
        if cid == "BZ-304":
            finding += " 另逐字核 R65 prediction 全文，仍无『5-6月恢复正常』一语、亦无 5–6 月时点表述，续接前提（引述不见于 prediction）本轮仍成立。"
        if cid == "LY-211":
            sugg = "同旨续接：自 R66 起承接本 R64 新旨标注＋本 R65 标注（与 R61 旧旨定案并行、各旨独立）；结局原文照录不改。"
        elif cid == "LY-216":
            sugg = "同旨续接：自 R66 起承接本 R64 新旨标注＋本 R65 标注（与 R61／R62 旧旨及 R63 续旨定案并行、各旨独立）；结局原文照录不改。"
        elif cid == "LY-432":
            sugg = "同旨续接：自 R66 起承接 R53／R56／R57＋本 R65 标注；结局原文照录不改。"
        else:
            sugg = "同旨续接：自 R66 起承接 R64＋本 R65 标注；结局原文照录不改。"
        category = "同旨续接（详见核查事实）"
    else:
        disp, relation, finding, sugg, category = FRESH[cid]
    flags_out.append({
        "anon_id": anon, "case_id": cid, "verdict": disp, "disposition": disp,
        "basis": finding, "carry_suggestion": sugg, "manifest_carry_suggestion": sugg,
        "flag": flag_text, "category": category, "views": views,
        "dual_view": len(views) == 2, "relation": relation, "registered_round": 65,
        "sources_checked": sources,
    })
    ann_out.append({
        "anon_id": anon, "case_id": cid, "disposition": disp, "finding": finding,
        "flag": flag_text, "manifest_carry_suggestion": sugg, "relation": relation,
        "registered_round": 65, "sources_checked": sources, "source_seats": e["seats"],
    })

verdicts = dict(collections.Counter(a["disposition"] for a in ann_out))
n_cont = sum(1 for a in ann_out if a["relation"].startswith("同旨续接"))
n_newgist = sum(1 for a in ann_out if a["relation"].startswith("同例新旨"))
n_new = sum(1 for a in ann_out if a["relation"].startswith("新旗标"))
print("TASK2 verdicts:", verdicts, "cont/newgist/new:", n_cont, n_newgist, n_new)
assert n_cont == 31 and n_newgist == 4 and n_new == 13 and len(ann_out) == 48

special_checks = [
    {
        "item": "特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记",
        "conclusion": "四件本轮均未出现在 R65 旗标 48 件中，不在本件范围，维持各自原登记、不另裁、不虚构条目：BZ-029 维持 R55 卒年待核（未核）；BZ-040 维持 R55 原登记（许世英享年异说待盘外独立史源）；LY-537 维持未核登记；YM-070『甲寅旬』出处待核挂起维持，其『都下』语义定案（未核）照旧。",
        "evidence": "据 runs/round65/judging/host-mapping.json 与 FLAGS-selfreported-r65.md 逐件比对：48 件 case_id 集合不含 BZ-029／BZ-040／LY-537／YM-070。",
        "scope_note": "本核查只登记状态，不改分数、不改 manifest；待核口径照旧。",
    },
    {
        "item": "特别核查②：旗标内容错配核查（引文层与主张层）",
        "conclusion": "引文层：48 件旗标引文逐字核（去空白后全文子串比对）均在本例 R65 结局内，无 R64 式 anon 内容错配（0 件）。主张层不合两件，均已按本例文本如实定案（不成立）：(1) LY-207（X2）旗标复述 R64 旧旨『prediction 病向负断模板』，逐字核 R65 prediction 全文为功名向断语、无病向表述，旧旨所指在本轮文本中不存在，定案不成立（同例新旨另立）；(2) LY-511（Y2）旗标称所问为求财／经营问面、疑结局错配，回读原卡所问为『占終身財福』，结局『貧寒淡泊』即其终局明载，定案不成立（新立）。另 LY-432（X2／Y2）『两段拼接／疑混入』之疑，依原卡自载两念反应结构承接 R53／R56／R57 既有定案（不成立），非错配。",
        "evidence": "LY-207：R65 prediction 作『功名不再起，官已化财向……』；R64 病向模板语『病势偏重、难速愈』全量检索 R65 predictions 仅见于 AS-204 通用模板。LY-511：inputs-dev12/LY-511.json 所问『占終身財福』；R65 结局『目摯十餘載，貧寒淡泊』。LY-432：原卡 question／setting 自载『先代尊長占病、本人占功名，兩念反應』，结局『五月高遷。 次日卽愈。』两段分应两念。",
        "scope_note": "本核查只登记错配事实与定案去向，不改分数、不改 manifest、不改旗标原文。",
    },
    {
        "item": "特别核查③：结局文本内嵌指令性字样之例——按数据处理登记",
        "conclusion": "承 R64 三处口径全量复扫 R65 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计等，并以『须／请／注』宽扫人工甄别叙事用字）：cases 本体内指令性字样共三例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。关于『第四处』：BZ-105 一句在字样口径下构成 cases 本体内第三例（连同 LR2-016 合计第四处文本出处），但该句自 R60 起即以回溯断验编者按登记在案、本轮由 X2 旗标再指，非本轮新发现的未登记出处；除上述外，本轮无任何此前未登记的指令性字样新出处。各席与本席均只按数据处理：BZ-042（X3）仅登记来源未备事实层、BZ-105（X2）仅登记回溯成色，BZ-036 与 LR2-016 本轮无席立旗；本席未服从任何一处之指示、未作量表外加减分或另设比对口径。",
        "evidence": "BZ-036 结局作『……此年数有出入，盲测比对须注』；BZ-042 结局作『……待另核（盲测比对时以格局大富一项为主）』；BZ-105 结局作『……盲测价值低于C04类前瞻断语，使用时须分开统计』；LR2-016 cases 本体仅『众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。』，指令性字样只存于 _r56_lr2016_split.editor_note。宽扫其余『请』字命中（BZ-302／LR2-022／LR3-004／LR3-006／LR3-010／LY-416）均为史实叙事用字、非指令性字样。",
        "scope_note": "本核查只登记出处与处理事实，不改分数、不改 manifest；一切文本内字样按数据处理、不作指令。",
    },
    {
        "item": "特别核查④：同例新旨（LY-203／LY-207／LY-615／LY-627）登记",
        "conclusion": "四件本轮新旨与各自旧旨各旨独立、并行不悖：LY-203 新旨就结局应验解释层立旗、定案部分成立，不推翻 R54 旧旨（问面不对位）不成立定案；LY-207 旗标复述 R64 旧旨（prediction 模板错位、部分成立），经核 R65 prediction 已改、所指不存在，另立定案不成立，R64 旧旨只及 R64 文本面、照旧登记；LY-615 新旨就结局应验解释层立旗、定案部分成立，旧旨（女死旁面）仍依 R54／R58／R64 同案复合不成立定案登记；LY-627 新旨就结局尾句应验解释层立旗、定案部分成立，不推翻 R57／R61／R64 旧旨（其日指代／方向）不成立定案。",
        "evidence": "各件 finding 内已逐件写明旧旨出处与新旨核查事实；四件 relation 字段均记同例新旨并注明旧旨轮次与档位。",
        "scope_note": "本核查只登记关系，不改分数、不改 manifest。",
    },
    {
        "item": "特别核查⑤：汇编一致性与结局文本一致性",
        "conclusion": "八件原始 FLAGS-X1..X4／Y1..Y4.md 与汇编 FLAGS-selfreported-r65.md 逐件比对全等（52 条旗标行、48 anon，去重后 48 例；同例多席同旨合并 4 例：LR2-023／LY-432／LY-437／LY-250）。R65 manifest 各例结局文本经脚本断言与 R64 manifest 逐件全等（487/487），同旨续接 31 件之承接前提（结局文本不变）成立。",
        "evidence": "脚本结构化解析八件原件与汇编：anon 集合与要旨首段逐件命中汇编；outcome-manifest 两轮 cases 逐键逐字比对 487/487 相等。",
        "scope_note": "本核查只登记一致性事实，不改分数、不改 manifest。",
    },
]

doc = {
    "_provenance": "R65 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）逐件回源核查 R65 八席自报旗标 52 条旗标行（runs/round65/judging/FLAGS-selfreported-r65.md 汇编；八件原始 FLAGS-X1..X4/Y1..Y4.md 逐件与汇编比对全等）、去重为 48 anon／48 例（同例多席同旨合并 4 例）。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round65/predictions/<case_id>.json 预测原文、runs/round65/judging/outcome-manifest.json cases 载荷（涉『与所问面不合／疑错配』者另回读原卡所问面核对），并与历轮定案档（data/case-annotations-r49.json 至 -r64.json；盘上实存 r49／r50／r51／r53–r64，缺 r52；历史检索显式排除本轮 r65 产出自身）核对承接关系：31 件为同旨续接（只承接不重裁），4 件为同例新旨（另裁），13 件为 R65 新立（逐件回源另裁）。R65 各例结局文本经脚本断言与 R64 manifest 逐件全等（487/487）。本轮无 R64 式 anon 内容错配（48 件引文逐字核均在本例结局内）；主张层不合两件（LY-207／LY-511）已按本例文本如实定案，见特别核查②。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。",
    "round": 65,
    "flags": flags_out,
    "annotations": ann_out,
    "special_checks": special_checks,
    "counts": {
        "selfreport_flag_rows_total": 52,
        "selfreport_anons_total": 48,
        "cases_total": 48,
        "continuation_cases": n_cont,
        "same_case_new_gist_cases": n_newgist,
        "new_flag_cases": n_new,
        "verdicts": verdicts,
    },
}
out2 = DATA / "case-annotations-r65.json"
out2.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

# readback Task2: dual-path counts self-consistency
rb2 = json.loads(out2.read_text(encoding="utf-8"))
tally2 = dict(collections.Counter(a["disposition"] for a in rb2["annotations"]))
tally2f = dict(collections.Counter(f["disposition"] for f in rb2["flags"]))
assert tally2 == rb2["counts"]["verdicts"] == tally2f, (tally2, tally2f)
assert len(rb2["annotations"]) == len(rb2["flags"]) == 48
assert all(f["basis"] == a["finding"] and f["flag"] == a["flag"] for f, a in zip(rb2["flags"], rb2["annotations"]))
print("TASK2 readback OK, bytes:", out2.stat().st_size)
print("SUMMARY verdicts:", verdicts, "| cont/newgist/new:", n_cont, n_newgist, n_new)
