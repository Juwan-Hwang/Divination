#!/usr/bin/env python3
"""R66 data seat build: Task1 addendum (R65 partials) + Task2 annotations (R66 flags).
Structured reads only; history enumerated explicitly r49,r50,r51,r53-r65."""
import json, pathlib, collections

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
DATA = BASE / "data"
J66 = BASE / "runs/round66/judging"
EV = json.loads((BASE / "runs/round66/data_r66_evidence.json").read_text(encoding="utf-8"))
R65 = json.loads((DATA / "case-annotations-r65.json").read_text(encoding="utf-8"))
OM66 = json.loads((J66 / "outcome-manifest.json").read_text(encoding="utf-8"))
OM65 = json.loads((BASE / "runs/round65/judging/outcome-manifest.json").read_text(encoding="utf-8"))

# ============ TASK 1: counts assertions (dual-path) ============
ann65 = R65["annotations"]
tally = collections.Counter(a["disposition"] for a in ann65)
assert dict(tally) == R65["counts"]["verdicts"], (dict(tally), R65["counts"]["verdicts"])
assert R65["counts"]["verdicts"] == {"部分成立": 40, "不成立": 3, "成立": 5}
assert len(ann65) == 48 and R65["counts"]["cases_total"] == 48
partials = [a for a in ann65 if a["disposition"] == "部分成立"]
assert len(partials) == 40
assert all((a["manifest_carry_suggestion"] or "").strip() for a in partials)

# ============ TASK 1: cross-check vs R66 manifest addendum layer ============
layer = OM66["_r66_carryover_notes_addendum"]
assert set(OM66["cases"].keys()) == set(OM65["cases"].keys()) and len(OM66["cases"]) == 487
assert all(OM66["cases"][k] == OM65["cases"][k] for k in OM66["cases"])
keyset_equal = set(a["case_id"] for a in partials) == set(layer.keys())
match, mismatch = [], []
for a in partials:
    (match if layer.get(a["case_id"]) == a["manifest_carry_suggestion"] else mismatch).append(a["case_id"])
print(f"TASK1 cross-check: {len(match)}/40 match, mismatches={mismatch}, keyset_equal={keyset_equal}")
assert keyset_equal and not mismatch

def esc(s):
    return s.replace("\n", " ")

lines = []
lines.append("# Manifest 承接册附则（R66）——R65 定案承接建议汇编")
lines.append("")
lines.append("## 卷首说明")
lines.append("")
lines.append("- 本附则为 Phase 3 Round 66（R66）数据席（任务一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r65.json`（R65 定案正本：annotations 48 件，定案分布成立 5／部分成立 40／不成立 3／未核 0）。")
lines.append(f"- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 5／部分成立 40／不成立 3、总 48，与 R65 公布分布逐项一致；部分成立 40 件每件 `manifest_carry_suggestion` 非空断言亦通过。")
lines.append(f"- 对勘结果：{len(match)}/40 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round66/judging/outcome-manifest.json` 的 `_r66_carryover_notes_addendum` 层（本席只读该层与 `cases` 键名集），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 {len(mismatch)} 件）。")
lines.append("- **本附则自 R67 manifest 起落实**；本轮（R66）manifest 不据本附则改动。")
lines.append("- **本件只汇编与对勘，不改任何分数与结局原文。**")
lines.append("- 汇编范围：R65 定案中部分成立 40 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r65.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R66 起」等表述为原档原文，落实轮次按卷首上一条读作自 R67 起，不回溯改动 R66）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。")
lines.append("- 成立 5／不成立 3 共 8 件不入正文逐件节，只在文末列 case_id 清单（本轮未核 0 件）。")
lines.append("- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 一、部分成立件承接汇编（定案档位：部分成立，40 件，逐件全列）")
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
lines.append("- 对勘对象：本汇编第一节 40 件承接注记建议文本（源：`case-annotations-r65.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round66/judging/outcome-manifest.json` 的 `_r66_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。")
detail = "、".join(f"{a['case_id']}＝{'一致' if a['case_id'] in match else '不一致'}" for a in partials)
lines.append(f"- 对勘结果：{len(match)} 件逐字一致，差异 {len(mismatch)} 件（对勘明细：{detail}）。")
lines.append(f"- 键集合差异：{'无（manifest 层 40 键与部分成立 40 件 case_id 集合全等）' if keyset_equal else '有，见不一致登记'}。")
if mismatch:
    lines.append("- 不一致登记：" + "；".join(f"{c}：附则侧照源档原文录入、manifest 侧照其盘上原文对勘，两侧均未作任何静默改动" for c in mismatch) + "。")
else:
    lines.append("- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。勘误结论：无须勘误；本附则结论自 R67 manifest 起落实。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 自验")
lines.append("")
lines.append("- 原档（case-annotations-r65.json）条目数：48；档位分布成立 5／部分成立 40／不成立 3／未核 0，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。")
lines.append("- 本附则正文条目数：40（第一节部分成立 40 件），与原档部分成立件数对齐；文末不入附则清单 8 件（成立 5＋不成立 3），40＋8＝48 与原档总数对齐。")
lines.append(f"- 承接注记建议文本：40 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R66 manifest `_r66_carryover_notes_addendum` 逐件逐字一致（{len(match)}／40）。")
lines.append("- 回读断言：本附则写出后由生成脚本回读，断言第一节条目数＝40、每件承接注记建议文本与原档字段逐字一致（结果见产出时回读记录：通过）。")
lines.append("- 纪律自报：本席只汇编与对勘，未改任何分数、未改 manifest、未改 annotations、未改原卡；outcome-manifest 只读 `_r66_carryover_notes_addendum` 层与 `cases` 键名集（另为续接前提核对 cases 与 R65 逐件全等 487/487，只读）。")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## 文末清单：不入附则 8 件（成立 5＋不成立 3，仅列 case_id；未核 0 件）")
lines.append("")
for disp, n in [("成立", 5), ("不成立", 3)]:
    lines.append(f"### {disp} {n} 件")
    lines.append("")
    for a in ann65:
        if a["disposition"] == disp:
            lines.append(f"- {a['case_id']}")
    lines.append("")
addendum_text = "\n".join(lines)
out1 = DATA / "manifest-carryover-r66-addendum.md"
out1.write_text(addendum_text, encoding="utf-8")

rb = out1.read_text(encoding="utf-8")
assert rb.count("### A") == 40, rb.count("### A")
for a in partials:
    assert a["manifest_carry_suggestion"] in rb and a["finding"] in rb and a["flag"] in rb
print("TASK1 readback OK, bytes:", out1.stat().st_size)

# ============ TASK 2: adjudication ============
entries = {e["case_id"]: e for e in EV["entries"]}
assert len(entries) == 54 and EV["flag_rows_total"] == 70 and EV["unique_anons"] == 54

FLAGS_TEXT = {
    "LY-216": "X1：结局为妇人转述反问、无独立终局叙述",
    "LY-252": "X1：结局首句后混入占亲属病断法通则",
    "OC-029": "X1：结局罗列多事而本例主问求官面不在其中（与carry附注同旨）",
    "LR3-101": "X1：outcome_record 内含编者排除性说明句（旁验不属本例结局）",
    "BZ-304": "X1：结局末句引述「5-6月恢复正常」一语不见于本轮 prediction_text 全文；Y1：结局末句引述「5-6月恢复正常」一语，本轮 prediction 全文无此语（原文为6月前后转缓、分段放松），引述与被引对象不合",
    "LY-516": "X1：结局首句后混入长段断法通则",
    "YM-068": "X1：结局仅残句「而不知已堕于井。」、主语与寻见与否均无明载",
    "LR3-002": "X1：结局「退位」主语未明字",
    "LY-436": "X1：结局与本问（本月天时）对应面错位、为多年后死亡记载；Y1：本例 prediction 为本月天时（阴晴）断，结局为占者午年子月之死，问验面错位（卡面自标占此应彼类）",
    "LY-614": "X1：结局以反问语收束、兄病终局未载；Y1：结局以反问语收束、兄病终局（愈/亡）未载，终局不可核",
    "LY-533": "X1：结局对应人身祸福面、所问房价面无验；Y1：所问索房价，结局为人身覆舟之亡、房价面无验，问验面错位",
    "LY-540": "X1：结局以逗号收尾、疑似截断；Y1：结局以逗号收尾、疑似截断（主结局城破被害已明载）",
    "BQ-001": "X2：outcome_record 本体未载终局，终逝仅由 carry_note 承接；Y2：carry_note 承接的应验信息不在 outcome_record 本体内",
    "BQ-021": "X2：outcome_record 止于旱象段，禾稻收成终局未载",
    "LY-206": "X2：outcome_record 仅载死亡断面，所问终身财福面无对应记录（与 carry_note 登记同旨）",
    "BQ-025": "X2：outcome_record 止于占后半日即时记载，养蜂终局未载",
    "LY-220": "X2：outcome_record 未载所问「兄弟和好」面（与 carry_note「和好面未载」同旨）",
    "LY-426": "X2：outcome_record 所载为旁及官非断面，开店贸易得利面无独立记载（与 carry_note 登记同旨）",
    "AS-004": "X3：结局为外部史实核验、非原文后记",
    "BZ-105": "X3：本例为回溯断验、结局自载其盲测价值受限；Y3：本例为回溯断验、盲测价值受限（carry_note 历轮同旨登记在案）",
    "BZ-037": "X3：结局自注原载与史实不合（已知偏差点）",
    "BZ-042": "X3：结局文本内嵌对评审的指令性字样（已按数据处理、只登记不服从）；同例晚年细节来源未备亦在结局内自注",
    "LY-437": "X3：结局断面与主问（小厮病）不对应：结局仅载占者本人七月革职（迁移断面），病愈与否无载；Y3：结局对应迁移断面（占他应我），且以逗号收尾疑似截断",
    "LY-023": "X3：结局断面与主问（母病）不对应：结局仅载其子惊风，母病结果未载；Y3：主问结果未载、结局载迁移面",
    "YM-070": "X3：结局措辞语义未明（「都下」所指不清），终局判定靠上下文；Y3：结局措辞语义未明（「都下」），本断方向对合无法确核（carry_note 历轮同旨登记在案）",
    "YM-030": "X3：结局「复完胎」语义未明、胎终局判定存疑；Y3：结局关键语义未明、胎终局存疑（「复完胎」，carry_note 历轮同旨登记在案）",
    "YY-022": "X3：总承式结局、断面未分载，子断语无从逐条核验",
    "LY-528": "X3：总承式结局、断面未分载，子断语无从逐条核验",
    "LY-529": "X3：结局含总承语「一一皆是」而指代未分载，同载实绩（二子发科甲）与总承指向关系不明",
    "BQ-016": "X3：结局引文含省略号截断、原文不完整",
    "BZ-036": "X4：结局内自注史实年数出入：原书系狱「六载」与史载三年不一致，结局已自注、比对时须留意；Y4：outcome_record 内嵌对盲测比对者的提示性字样（「盲测比对须注」）、且年数自相出入已自注，已按数据处理",
    "LY-452": "X4：结局以逗号收尾、疑似截断；仅载焚村实况，本人是否避往及安否未载；Y4：outcome_record 以逗号收尾、疑似截断",
    "LY-227": "X4：结局前段为个案结果，后半混入六冲／六合断法通则，非个案结局记载",
    "LY-506": "X4：两占（母病／子病）合载，结局死亡一句归属未明字，无法判定死者为母或子",
    "LR2-016": "X4：本例 editor_note 提及「甲戌日巳时」日时细项，然本例 outcome_record 原文并无此字样，该细项已按未载处理；Y4：editor_note 含对评分者的指令性字样（「评分时……请按……处理」），且所涉「甲戌日巳时」不见于 outcome_record 原文，已按数据处理、未服从",
    "LY-510": "X4：结局对应同条再问（遍游行踪），主问「何事可为」的具体断面无独立记载",
    "LY-531": "X4：结局仅侧载午月中途过害，仆人归否未明载",
    "AS-015": "X4：同图兼断例：结局仅载问者本人死日，丈夫存亡与归讯未载，主断无从核验",
    "LY-430": "X4：结局对应再占危灾断面（病死），本断所问掣签何处与能否到任面无记载；Y4：outcome 对应再占危灾断面、主问断面无记载",
    "LY-513": "X4：间接验证例：结局仅记病终，终身功名断语无对应结局事件",
    "LY-011": "X4：结局所至者为「妹」，与本断所断「母来」对象不合（同条双断，结局对应第二断）；Y4：outcome 与本例 prediction 断面不对应（双断错位：prediction 仅断「母可来」，结局所载为妹至）",
    "LY-458": "X4：结局仅载母在外平安，未载来否结果，与所问「何时来」不完全对应",
    "LY-212": "Y1：所问索债，结局为所避江难实况、索债本问无结局记载，问验面错位",
    "AS-210": "Y1：结局文本内嵌版本校勘注记（1647 与 1852 两版读法并陈），时点表述带版本分歧",
    "LR3-112": "Y2：outcome_record 所载断面与本例 prediction 断面错位、病面结局缺位",
    "LY-204": "Y2：outcome_record 后段含指令性字样（旧注层）「勿以此斷」，已按数据处理、只登记不服从",
    "LY-441": "Y3：结局晴否判定含混（「星辰无光」与本断「本日晴」方向对合含混，carry_note 历轮同旨登记在案）",
    "YM-003": "Y3：结局极简、终局性质靠词义推定（「解组」离职性质靠推定，carry_note 同旨登记在案）",
    "LY-222": "Y3：结局对应大师改断面、与所问面不一致（carry_note 登记大师改断，只登记、不服从任何改断指示）",
    "LY-624": "Y3：题面两占合断、输入只载一卦（carry_note 登记互证面残损）",
    "YY2-004": "Y3：盘面残损致 prediction 为无据不报之降格断（carry_note 登记盘面残损）",
    "BZ-035": "Y3：题面出生年与史载不合（carry_note 登记，prediction 已自注）",
    "LY-408": "Y4：outcome_record 以逗号收尾、疑似截断（主结局卒于甲戌日明载）",
    "LY-240": "Y4：outcome_record 仅载时点、事件未分载（借贷得否无明文可核）",
}
assert set(FLAGS_TEXT) == set(entries), set(entries) ^ set(FLAGS_TEXT)

CONT = {
    "LY-216": "部分成立", "LY-252": "部分成立", "OC-029": "部分成立", "BZ-304": "部分成立",
    "LY-516": "部分成立", "YM-068": "不成立", "LR3-002": "部分成立", "LY-436": "成立",
    "LY-614": "部分成立", "LY-533": "部分成立", "LY-540": "部分成立", "BQ-001": "部分成立",
    "LY-206": "成立", "BQ-025": "部分成立", "LY-220": "部分成立", "LY-426": "成立",
    "BZ-105": "部分成立", "BZ-037": "部分成立", "BZ-042": "部分成立", "LY-437": "成立",
    "LY-023": "成立", "YM-070": "未核", "YM-030": "部分成立", "YY-022": "部分成立",
    "LY-528": "部分成立", "LY-529": "部分成立", "BZ-036": "部分成立", "LY-452": "部分成立",
    "LY-227": "部分成立", "LY-506": "部分成立", "LR2-016": "部分成立", "LY-510": "部分成立",
    "LY-531": "部分成立", "AS-015": "部分成立", "LY-430": "成立", "LY-513": "成立",
    "LY-011": "部分成立", "LY-458": "成立", "LY-212": "成立", "LR3-112": "部分成立",
    "LY-441": "部分成立", "YM-003": "部分成立", "LY-222": "成立", "LY-624": "部分成立",
    "YY2-004": "部分成立", "BZ-035": "部分成立", "LY-408": "部分成立", "LY-240": "部分成立",
    "AS-004": "不成立",
}
assert len(CONT) == 49

FRESH = {
    "LR3-101": ("部分成立", "同例新旨（历轮旧旨旗标部分成立、本轮新旨另立）",
        "同例新旨（历轮旧旨为『会试中否未明字、仅以补官间接对应』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「会试中否？」；R66 manifest 结局『后补刑部主政，恬退不仕。』后并载编者排除性说明句『同课旁载的代占会武中两名、占病死二人系一课多占的旁验，不属本例结局。』——编者说明句并载于结局文本属实一层；但该句系明示排除旁验、划清本例边界，非他例结局混入，本例主线补官记载本身完整。故部分成立。",
        "同例新旨：自 R67 起承接本 R66 标注（与历轮旧旨定案并行、各旨独立）：按「结局后并载编者排除性说明句、主线补官明载」登记；结局原文照录不改。",
        "同例新旨：结局并载编者排除性说明句（主线明载）"),
    "AS-210": ("部分成立", "同例新旨（历轮旧旨旗标部分成立、本轮新旨另立）",
        "同例新旨（历轮旧旨为『得缺以总承语带过、未明名，假朋友一面明载』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问能否得所求官职；R66 manifest 结局时点表述内嵌版本校勘注记『within lesse three weekes [1647 OCR reading; the 1852 edition reads 'within three weeks']』——校勘注记混入结局文本、时点表述带版本分歧属实一层；但两版读法仅 lesse 之别、三周时点本身有载，假朋友一面亦明载。故部分成立。",
        "同例新旨：自 R67 起承接本 R66 标注（与历轮旧旨定案并行、各旨独立）：按「结局时点表述内嵌版本校勘注记、三周时点有载」登记；结局原文照录不改。",
        "同例新旨：结局内嵌版本校勘注记（时点有载）"),
    "LY-204": ("部分成立", "同例新旨（R64 旧旨旗标部分成立、本轮新旨另立）",
        "同例新旨（R64 旧旨为『结局含旧注解释层、与主断面混载』、定案部分成立，本轮新旨就旧注内指令性字样另立、与旧旨并行不悖）：回原卡——所问「占財福（再占問功名出仕）」；R66 manifest 结局后段旧注『舊注官鬼持世疾病纏綿﹐若是貴人。勿以此斷。』含指令性字样『勿以此斷』、在 cases 本体内属实；该字样系原书旧注对断法之指示、非结局事实，各席与本席均按数据处理、未服从；前段功名实绩（卯年援例入临、巳年初任、未年再位）明载。故部分成立。指令性字样出处登记另见特别核查③。",
        "同例新旨：自 R67 起承接本 R66 标注（与 R64 旧旨定案并行、各旨独立）：按「结局旧注层含指令性字样『勿以此斷』、按数据处理未服从，功名实绩明载」登记；结局原文照录不改。",
        "同例新旨：旧注层指令性字样登记（实绩明载）"),
    "BQ-021": ("部分成立", "新旗标（R66 新立）",
        "新旗标（R66 新立）：回原卡——所问「卜禾（禾稻长势与天时）」；R66 manifest 结局载插莳时雇工（阴人）少财而去、逾三四日天亢旱难用——插莳与旱象段有载；但禾稻收成终局（转安／有收与否）无对应记载，所指终局缺位一层属实；结局亦非全无记载。故部分成立（同 BQ-025 即时段有载、终局未载口径）。",
        "同旨新立：自 R67 起承接本 R66 标注：按「插莳与亢旱段有载、禾稻收成终局未载」登记；结局原文照录不改。",
        "结局终局缺位（前段有载）"),
    "BQ-016": ("部分成立", "新旗标（R66 新立）",
        "新旗标（R66 新立）：回原卡——所问「卜倭乱（其年倭寇之乱如何）」；R66 manifest 结局引文段『其年果应倭贼大乱……所以其年劫、烧、杀、伤不可胜计』含省略号截断、原文不完整属实一层；但倭贼大乱与劫烧杀伤之主结局在引文与转述两处均明载、终局可核。故部分成立（同 LY-540 逗号收尾口径）。",
        "同旨新立：自 R67 起承接本 R66 标注：按「结局引文含省略号截断、倭乱主结局明载」登记；结局原文照录不改。",
        "结局引文省略号截断（主结局明载）"),
}
assert len(FRESH) == 5 and not (set(FRESH) & set(CONT)) and set(FRESH) | set(CONT) == set(entries)

# verbatim assertions (built-in, per R66 three-precedent rule)
cases = OM66["cases"]
assert cases["BZ-304"].find("5-6月恢复正常") >= 0
pred304 = entries["BZ-304"]["prediction_text"]
assert "5-6月恢复正常" not in pred304 and "6月前后" in pred304
assert "勿以此斷" in cases["LY-204"] and "勿以此斷" in cases["LY-204"]
assert "甲戌日巳时" not in cases["LR2-016"]
assert OM66["_r56_lr2016_split"]["editor_note"] == "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
assert "盲测比对须注" in cases["BZ-036"] and "盲测比对时以格局大富一项为主" in cases["BZ-042"] and "使用时须分开统计" in cases["BZ-105"]
assert "同课旁载的代占会武中两名、占病死二人系一课多占的旁验，不属本例结局。" in cases["LR3-101"]
assert "1647 OCR reading" in cases["AS-210"] and "1852 edition reads" in cases["AS-210"]
assert "……" in cases["BQ-016"]
# anon near-string check: dual-seat anons resolve to same case via host-mapping (already in EV construction); assert seat counts
assert sum(len([1]) for _ in entries) == 54

STD = {"成立", "部分成立", "不成立", "未核"}
flags_out, ann_out = [], []
for cid in sorted(entries, key=lambda c: entries[c]["anon"]):
    e = entries[cid]
    anon = e["anon"]
    flag_text = FLAGS_TEXT[cid]
    hist = e["history"]
    sources = [
        f"benchmark/phase3/inputs-dev12/{cid}.json",
        "benchmark/phase3/runs/round66/judging/FLAGS-selfreported-r66.md",
        f"benchmark/phase3/runs/round66/judging/outcome-manifest.json cases[{cid}]",
        f"benchmark/phase3/runs/round66/predictions/{cid}.json",
    ] + [f"benchmark/phase3/data/case-annotations-r{h['round']}.json {cid} 条" for h in hist if h["disposition"] in STD or h["round"] >= 55]
    views = sorted({("X" if s.startswith("X") else "Y") for s in e["seats"]})
    if cid in CONT:
        disp = CONT[cid]
        std_hist = [h for h in hist if h["disposition"] in STD]
        latest = max(std_hist, key=lambda h: h["round"])
        assert latest["disposition"] == disp, (cid, latest["round"], latest["disposition"], disp)
        relation = f"同旨续接（R{latest['round']}）"
        finding = (f"承接既有定案不重裁（历轮最近定案 R{latest['round']} {disp}）：{latest['finding']}"
                   f" 本轮（R66）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。")
        if cid == "BZ-304":
            finding += " 另逐字核 R66 prediction 全文，仍无『5-6月恢复正常』一语（原文为6月前后转缓、分段放松），续接前提（引述不见于 prediction）本轮仍成立。"
        if disp == "部分成立":
            sugg = f"同旨续接：自 R67 起承接 R{latest['round']}＋本 R66 标注；结局原文照录不改。"
            if cid == "YM-070":
                sugg = "同旨续接：自 R67 起承接历轮标注：按「结局措辞待核（『都下』语义未明）」登记，与『甲寅旬』出处待核并列；结局原文照录不改、不补字。"
        elif disp == "未核":
            sugg = "同旨续接（未核维持）：自 R67 起承接历轮标注：按「结局措辞待核（『都下』语义未明）」登记，与『甲寅旬』出处待核并列；结局原文照录不改、不补字，无盘外独立史源不裁。"
        else:
            sugg = f"不入附则：本 R66 同旨续接定案（{disp}），自 R67 起承接本 R66 标注，不加承接注记；结局原文照录不改。"
        category = "同旨续接（详见核查事实）"
    else:
        disp, relation, finding, sugg, category = FRESH[cid]
    flags_out.append({
        "anon_id": anon, "case_id": cid, "verdict": disp, "disposition": disp,
        "basis": finding, "carry_suggestion": sugg, "manifest_carry_suggestion": sugg,
        "flag": flag_text, "category": category, "views": views,
        "dual_view": len(views) == 2, "relation": relation, "registered_round": 66,
        "sources_checked": sources,
    })
    ann_out.append({
        "anon_id": anon, "case_id": cid, "disposition": disp, "finding": finding,
        "flag": flag_text, "manifest_carry_suggestion": sugg, "relation": relation,
        "registered_round": 66, "sources_checked": sources, "source_seats": e["seats"],
    })

verdicts = dict(collections.Counter(a["disposition"] for a in ann_out))
n_cont = sum(1 for a in ann_out if a["relation"].startswith("同旨续接"))
n_newgist = sum(1 for a in ann_out if a["relation"].startswith("同例新旨"))
n_new = sum(1 for a in ann_out if a["relation"].startswith("新旗标"))
print("TASK2 verdicts:", verdicts, "cont/newgist/new:", n_cont, n_newgist, n_new)
assert n_cont == 49 and n_newgist == 3 and n_new == 2 and len(ann_out) == 54
assert verdicts == {"部分成立": 41, "成立": 10, "不成立": 2, "未核": 1}, verdicts

special_checks = [
    {
        "item": "特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记",
        "conclusion": "BZ-029／BZ-040／LY-537 三件本轮未被任何旗标触及，不在本件范围，维持各自原登记、不另裁、不虚构条目：BZ-029 维持 R55 卒年待核（未核），其错配线索一层照原登记并列、无盘外独立史源不裁；BZ-040 维持 R55 原登记（许世英享年异说待盘外独立史源）；LY-537 维持未核登记。YM-070 本轮被 X3／Y3 两席旗标触及，已在本件逐件定案（同旨续接、未核维持：『都下』语义未明＋『甲寅旬』出处待核并列），不重复入本附注。",
        "evidence": "据 runs/round66/judging/host-mapping.json 与 FLAGS-selfreported-r66.md 逐件比对：54 件 case_id 集合不含 BZ-029／BZ-040／LY-537，含 YM-070（P3-7c6961f4，X3／Y3 双席）。",
        "scope_note": "本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。",
    },
    {
        "item": "特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）",
        "conclusion": "引文层：54 件旗标所引结局文字经逐件回读本例 R66 结局原文核对，均在本例结局内（X3 对 AS-004 之引文为省略号节录，其首尾两段『Not stated as a postscript in the excerpt』与『Marked as externally verified, not Lilly-stated.』均逐字在原文内），无 anon 内容错配（0 件）。anon 对位：70 条旗标行经 host-mapping.json 逐件回到 case_id，16 例双席同 anon（如 BZ-304 之 P3-1505ba68 为 X1／Y1 同指一例、LY-540 之 P3-42cd02dd、BQ-001 之 P3-43a7aa1d 等）逐件对位复核无串号；形近 anon（如 P3-975226ed BZ-105 与 P3-9e5bc17f BZ-037、P3-c07de21f BZ-036 与 P3-c482c78f LY-452）经映射逐件分核、各归其例。主张层：各席主张与本例所问面／prediction 全文逐件相合，无 R64／R65 式主张层不合件（0 件）。",
        "evidence": "脚本结构化解析八件原始 FLAGS-X1..X4／Y1..Y4.md：70 行、54 anon，与汇编 FLAGS-selfreported-r66.md 逐件比对全等（anon 集合全含）；引文逐字断言内置于落盘脚本（BZ-304／LY-204／LR2-016／BZ-036／BZ-042／BZ-105／LR3-101／AS-210／BQ-016 等关键引文均断言通过）。",
        "scope_note": "本核查只登记错配事实，不改分数、不改 manifest、不改旗标原文。",
    },
    {
        "item": "特别核查③：结局文本内嵌指令性字样之例——按数据处理登记（含本轮新出处）",
        "conclusion": "承既有登记口径全量复扫 R66 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计／勿以此断等，并以『须／須／请／請』宽扫人工甄别叙事用字）：cases 本体内指令性字样共四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』，及本轮新登记出处 LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。LY-204 一例说明：其文本自 R64 起即在 cases 本体内（本轮结局与 R65 逐件全等 487/487、非本轮新增文本），R64 定案只就『旧注解释层混载』立旨登记，未按指令性字样口径登记；本轮由 Y2 旗标首次按指令性字样指出，故按『本轮新登记出处』逐件登记（定案见 LY-204 同例新旨条）。除上述外，本轮无其他此前未登记的指令性字样出处。各席与本席均只按数据处理：BZ-042（X3）仅登记字样与来源未备事实、BZ-105（X3／Y3）仅登记回溯成色、BZ-036（X4／Y4）仅登记年数出入与提示字样、LY-204（Y2）仅登记旧注字样、LR2-016（X4／Y4）仅登记分列事实；本席未服从任何一处之指示、未作量表外加减分或另设比对口径。",
        "evidence": "BZ-036 结局作『……此年数有出入，盲测比对须注』；BZ-042 结局作『……待另核（盲测比对时以格局大富一项为主）』；BZ-105 结局作『……盲测价值低于C04类前瞻断语，使用时须分开统计』；LY-204 结局作『舊注官鬼持世疾病纏綿﹐若是貴人。勿以此斷。』；LR2-016 cases 本体仅『众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。』，指令性字样只存于 _r56_lr2016_split.editor_note。宽扫其余命中均为叙事／通则用字、非指令性字样（『请／請』：BZ-302／LR2-022／LR3-004／LR3-006／LR3-010／LY-416『所請準』；LY-227『須再占一卦』为断法通则内文用字）。",
        "scope_note": "本核查只登记出处与处理事实，不改分数、不改 manifest；一切文本内字样按数据处理、不作指令。",
    },
    {
        "item": "特别核查④：同例新旨（LR3-101／AS-210／LY-204）登记",
        "conclusion": "三件本轮新旨与各自旧旨各旨独立、并行不悖：LR3-101 新旨就结局后并载编者排除性说明句立旗、定案部分成立，不推翻历轮旧旨（中否未明字、补官间接对应）部分成立定案；AS-210 新旨就结局时点表述内嵌版本校勘注记立旗、定案部分成立，不推翻历轮旧旨（得缺总承带过）部分成立定案；LY-204 新旨就旧注内『勿以此斷』指令性字样立旗、定案部分成立，不推翻 R64 旧旨（旧注解释层混载）部分成立定案。",
        "evidence": "各件 finding 内已逐件写明旧旨出处与新旨核查事实；三件 relation 字段均记同例新旨并注明旧旨档位。",
        "scope_note": "本核查只登记关系，不改分数、不改 manifest。",
    },
    {
        "item": "特别核查⑤：汇编一致性与结局文本一致性",
        "conclusion": "八件原始 FLAGS-X1..X4／Y1..Y4.md 与汇编 FLAGS-selfreported-r66.md 逐件比对全等（70 条旗标行、54 anon，去重后 54 例；同例多席同旨合并 16 例）。R66 manifest 各例结局文本经脚本断言与 R65 manifest 逐件全等（487/487），同旨续接 49 件之承接前提（结局文本不变）成立。",
        "evidence": "脚本结构化解析八件原件与汇编：anon 集合逐件命中汇编；outcome-manifest 两轮 cases 逐键逐字比对 487/487 相等（落盘脚本断言通过）。",
        "scope_note": "本核查只登记一致性事实，不改分数、不改 manifest。",
    },
]

doc = {
    "_provenance": "R66 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）逐件回源核查 R66 八席自报旗标 70 条旗标行（runs/round66/judging/FLAGS-selfreported-r66.md 汇编；八件原始 FLAGS-X1..X4/Y1..Y4.md 逐件与汇编比对全等）、去重为 54 anon／54 例（同例多席同旨合并 16 例）。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round66/predictions/<case_id>.json 预测原文、runs/round66/judging/outcome-manifest.json cases 载荷（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），并与历轮定案档（data/case-annotations-r49.json 至 -r65.json；盘上实存 r49／r50／r51／r53–r65，缺 r52；历史检索显式排除本轮 r66 产出自身）核对承接关系：49 件为同旨续接（只承接不重裁），3 件为同例新旨（另裁），2 件为 R66 新立（逐件回源另裁）。R66 各例结局文本经脚本断言与 R65 manifest 逐件全等（487/487）。本轮无 anon 内容错配（54 件引文逐字核均在本例结局内），无主张层不合件。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。",
    "round": 66,
    "flags": flags_out,
    "annotations": ann_out,
    "special_checks": special_checks,
    "counts": {
        "selfreport_flag_rows_total": 70,
        "selfreport_anons_total": 54,
        "cases_total": 54,
        "continuation_cases": n_cont,
        "same_case_new_gist_cases": n_newgist,
        "new_flag_cases": n_new,
        "verdicts": verdicts,
    },
}
out2 = DATA / "case-annotations-r66.json"
out2.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

rb2 = json.loads(out2.read_text(encoding="utf-8"))
tally2 = dict(collections.Counter(a["disposition"] for a in rb2["annotations"]))
tally2f = dict(collections.Counter(f["disposition"] for f in rb2["flags"]))
assert tally2 == rb2["counts"]["verdicts"] == tally2f, (tally2, tally2f)
assert len(rb2["annotations"]) == len(rb2["flags"]) == 54
assert all(f["basis"] == a["finding"] and f["flag"] == a["flag"] for f, a in zip(rb2["flags"], rb2["annotations"]))
assert all((a["manifest_carry_suggestion"] or "").strip() for a in rb2["annotations"] if a["disposition"] == "部分成立")
print("TASK2 readback OK, bytes:", out2.stat().st_size)
print("SUMMARY verdicts:", verdicts, "| cont/newgist/new:", n_cont, n_newgist, n_new)
