#!/usr/bin/env python3
"""R84 supply seat E1: expansion small-pool eligibility audit.

Scope (task order): pools expansion / expansion6 / expansion8 / expansion9 only.
Recomputes the used-id union (1166口径) and each pool's unused id set from disk,
then renders the per-case adjudication ledger EXPANSION-AUDIT-small-pools-r84.md.
Adjudication values below were determined by this seat by reading each unused
case's pool-layer original records (cases/answers/inputs/GRADING/BUILD-REPORT/
HOST-ADJUDICATION) directly; this script only recomputes id sets, asserts the
adjudication table covers exactly the unused sets, and renders the ledger.
Gold files are read for the "id" field only; no gold body text is opened.
No predictions/judging/final-scores under runs/ are opened.
"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
BM = P3.parent
OUT = P3 / "runs/round84/supply/EXPANSION-AUDIT-small-pools-r84.md"
POOLS = ["expansion", "expansion6", "expansion8", "expansion9"]


def card_ids(d):
    out = set()
    if d.is_dir():
        for f in d.glob("*.json"):
            out.add(f.stem)
    return out


def gold_ids(p):
    out = set()
    if p.is_file():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                out.add(json.loads(line)["id"])
    return out


def used_union():
    parts = {}
    dev = set(json.loads((P3 / "data/master-baseline-dev9.json").read_text(encoding="utf-8")).keys())
    for name in ["inputs-dev9", "inputs-dev10", "inputs-dev11", "inputs-dev12", "inputs"]:
        dev |= card_ids(P3 / name)
    parts["dev"] = dev
    sp2 = json.loads((BM / "phase2/splits2.json").read_text(encoding="utf-8"))
    h2 = set()

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "holdout2" and isinstance(v, list):
                    h2.update(x if isinstance(x, str) else x.get("id") for x in v)
                else:
                    walk(v)
        elif isinstance(o, list):
            for x in o:
                walk(x)

    walk(sp2)
    parts["holdout2_splits2"] = h2
    golds = set()
    for n in range(3, 29):
        golds |= gold_ids(P3 / f"holdout{n}" / "test_gold.jsonl")
    parts["gold_h3_28"] = golds
    hinputs = set()
    for n in range(2, 29):
        hinputs |= card_ids(P3 / f"holdout{n}" / "inputs")
        hinputs |= card_ids(P3 / f"holdout{n}-inputs")
    parts["holdout_inputs"] = hinputs
    top = set()
    for name in ["inputs6", "inputs7", "inputs8", "inputs9", "inputs10"]:
        top |= card_ids(P3 / name)
    parts["top_inputs6_10"] = top
    union = set()
    for v in parts.values():
        union |= v
    return parts, union


def pool_ids(name):
    ids = set()
    for fp in (P3 / name).rglob("*.jsonl"):
        for line in fp.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            v = o.get("id") or o.get("case_id") or o.get("provisional_id")
            if v:
                ids.add(v)
    return ids


# ---- adjudication table (seat's per-case reading of pool originals) ----
# fields: id, pool, tradition/source, F1 verbatim, F2 independent outcome,
# F3 separable, F4 non-high, anchor, contamination, grade, verdict, location
P_, F_ = "pass", "fail"
ROWS = [
    # expansion / bushi (GRADING.md: A=outcome separable & concrete; B=self-stated 果驗)
    ["LY-302", "expansion", "liuyao 六爻／《卜筮正宗》王洪緒（輯錄）·第七問占求財",
     P_, F_, F_, P_, "partial", "low", "B", "不合格：F2 独立结局（「本日即果驗」与断语同句、仅自述式应验）＋F3 可分离（GRADING 明载不可分离）＋非 A 级＋锚点 partial（卦名風雷益在；动爻缺——装卦表 OCR 错乱逐爻未录；世应仅用神持世一语、六亲纳支逐爻缺；月建原文未明记、日辰仅戌日）",
     "expansion/bushi/answers.jsonl＋inputs.jsonl；expansion/bushi/GRADING.md 逐例分级表 LY-302 行"],
    ["LY-303", "expansion", "liuyao 六爻／《卜筮正宗》王洪緒（輯錄）·第七問占仆何日回",
     P_, F_, F_, P_, "partial", "low", "B", "不合格：F2 独立结局（应验仅「後果驗」自述句）＋F3 可分离（应验与断语同句不可分离）＋非 A 级＋锚点 partial（卦名澤火革在；动爻/世应/六亲纳支逐爻缺；月日原文未明記）",
     "expansion/bushi/answers.jsonl＋inputs.jsonl；expansion/bushi/GRADING.md 逐例分级表 LY-303 行"],
    # expansion6 / classical-other (all B, holdout_eligible=false in cases)
    ["OC-031", "expansion6", "bazi 八字／韦千里《千里命稿》应运篇·夭折婴",
     P_, P_, P_, P_, "present", "low", "B", "不合格：非 A 级（未具名＋结局仅原书自载、无独立史料，台账 outcome_grade=B、holdout_eligible=false）",
     "expansion6/classical-other/cases.jsonl OC-031＋inputs/OC-031.json；classical-other/BUILD-REPORT.md B 级清单"],
    ["OC-032", "expansion6", "bazi 八字／韦千里《千里命稿》应运篇下·广东妓女",
     P_, P_, P_, P_, "present", "low", "B", "不合格：非 A 级（未具名＋结局书内自载，上限 B；holdout_eligible=false）",
     "expansion6/classical-other/cases.jsonl OC-032＋inputs/OC-032.json；classical-other/BUILD-REPORT.md B 级清单"],
    ["OC-033", "expansion6", "bazi 八字／韦千里《千里命稿》应运篇下·某军人",
     P_, P_, P_, P_, "present", "low", "B", "不合格：非 A 级（未具名＋结局书内自载，上限 B；应验段虽独立可分离，holdout_eligible=false）",
     "expansion6/classical-other/cases.jsonl OC-033＋inputs/OC-033.json；classical-other/BUILD-REPORT.md B 级清单"],
    ["OC-034", "expansion6", "meihua 梅花／《梅花易数》卷二·田姓起屋占",
     P_, F_, F_, P_, "present", "low", "B", "不合格：F2 独立结局（全段结局仅「遂斷之而皆驗」总述、无分例应验记载）＋F3 可分离（结局为三家总述、不可按例分离）＋非 A 级",
     "expansion6/classical-other/cases.jsonl OC-034＋inputs/OC-034.json（卦象：水风井变地风升）；classical-other/BUILD-REPORT.md B 级清单"],
    ["OC-035", "expansion6", "meihua 梅花／《梅花易数》卷二·韩姓起屋占",
     P_, F_, F_, P_, "present", "low", "B", "不合格：F2 独立结局（仅「遂斷之而皆驗」总述）＋F3 可分离（总述不可按例分离）＋非 A 级",
     "expansion6/classical-other/cases.jsonl OC-035＋inputs/OC-035.json（卦象：风益变风泽中孚）；classical-other/BUILD-REPORT.md B 级清单"],
    ["OC-036", "expansion6", "liuren 六壬／袁树珊《大六壬探原》占卜一斑录·从戎占",
     P_, F_, P_, P_, "absent", "low", "B", "不合格：F2 独立结局（结局仅当场决计买舟旋里之意向、非事后结局记载）＋非 A 级＋锚点不在场（inputs 卡无课式/四课/三传附件，仅占时与「甲午命年十八」注）",
     "expansion6/classical-other/cases.jsonl OC-036＋inputs/OC-036.json；classical-other/BUILD-REPORT.md B 级清单"],
    ["OC-037", "expansion6", "liuren 六壬／袁树珊《大六壬探原》占卜一斑录·争讼占",
     P_, F_, P_, P_, "absent", "low", "B", "不合格：F2 独立结局（断语为既往事实逆断、当场核对成立；前瞻部分（上诉）结局原文未载）＋非 A 级＋锚点不在场（inputs 卡无课式/四课/三传附件）",
     "expansion6/classical-other/cases.jsonl OC-037＋inputs/OC-037.json；classical-other/BUILD-REPORT.md B 级清单"],
    ["OC-038", "expansion6", "liuren 六壬／陈公献《大六壬占验指南》第61课·孙友进京占",
     P_, P_, P_, P_, "present", "low", "B", "不合格：非 A 级（占者未具全名、结局无外部独立记载，台账 B、holdout_eligible=false）",
     "expansion6/classical-other/cases.jsonl OC-038＋inputs/OC-038.json（课式/三传/月将附件）；classical-other/BUILD-REPORT.md B 级清单"],
    ["OC-039", "expansion6", "liuren 六壬／陈公献《大六壬占验指南》第62课·寇道台仕途占",
     P_, P_, P_, P_, "present", "low", "B", "不合格：非 A 级（主占者未具全名，台账 B、holdout_eligible=false）",
     "expansion6/classical-other/cases.jsonl OC-039＋inputs/OC-039.json（课式/三传/月将附件）；classical-other/BUILD-REPORT.md B 级清单"],
    # expansion6 / modern-cn (all B; road-level contamination high for public elections)
    ["MP-020", "expansion6", "姓名学／泓葆先生·2024 台湾大选（赖清德）",
     F_, P_, P_, F_, "partial", "high", "B", "不合格：F1 逐字原文（断语仅见选后翌日报道、无任何选前发表物，时间戳不可独立验证）＋F4 非 high 污染（high：2024 台湾大选著名选举）＋非 A 级＋非 low＋锚点 partial（inputs 卡仅题面/时点、无盘面锚点字段）",
     "expansion6/modern-cn/cases.jsonl MP-020＋inputs/MP-020.json；modern-cn/BUILD-REPORT.md B 级清单与普查账（三立 2024-01-14 行）"],
    ["MP-021", "expansion6", "bazi 八字（盲人算命）／陳寬利·2020 台湾大选当选人属相党籍",
     F_, P_, P_, F_, "partial", "high", "B", "不合格：F1 逐字原文（仅见选后汇编转录一行、无原始发表日期与出处）＋F4 非 high 污染（high）＋非 A 级＋非 low＋锚点 partial（inputs 卡 asked_at 仅记「选前（具体日期未载）」）",
     "expansion6/modern-cn/cases.jsonl MP-021＋inputs/MP-021.json；modern-cn/BUILD-REPORT.md B 级清单"],
    ["MP-022", "expansion6", "易经卜卦／鄭姓命理師·2024 美国大选（特朗普得票率）",
     P_, P_, P_, F_, "partial", "high", "B", "不合格：F4 非 high 污染（high：2024 美国大选全球著名事件）＋非 A 级（大师仅知姓氏、无全名与出版记录可核）＋非 low＋锚点 partial（inputs 卡无盘面锚点字段）",
     "expansion6/modern-cn/cases.jsonl MP-022＋inputs/MP-022.json；modern-cn/BUILD-REPORT.md B 级清单"],
    # expansion6 / modern-west (all B, holdout_eligible=false)
    ["WP-014", "expansion6", "horary 西方卜卦占星／Robert Zoller·1991 纽约楼宇工会罢工占",
     P_, P_, P_, P_, "present", "low", "B", "不合格：非 A 级（结局前时间戳仅靠作者自述见证/赌局、首刊 1993 年期刊，按该路口径从严定 B；holdout_eligible=false）",
     "expansion6/modern-west/cases.jsonl WP-014＋inputs/WP-014.json；modern-west/BUILD-REPORT.md B 级表 WP-014 行"],
    ["WP-015", "expansion6", "horary 西方卜卦占星／Sharon Knight·遗失钻石耳环占",
     P_, F_, P_, P_, "present", "low", "B", "不合格：F2 独立结局（断语与结局均只见于从业者本人发表的案例文、无外部印证）＋非 A 级",
     "expansion6/modern-west/cases.jsonl WP-015＋inputs/WP-015.json；modern-west/BUILD-REPORT.md B 级表 WP-015 行"],
    ["WP-016", "expansion6", "horary 西方卜卦占星／John Frawley·走失猫占（1998 伦敦）",
     F_, F_, P_, P_, "present", "low", "B", "不合格：F1 逐字原文（本轮可得文本为 2026 年二手转述、非 Frawley 原书逐字文本）＋F2 独立结局（结局仅从业者报告）＋非 A 级",
     "expansion6/modern-west/cases.jsonl WP-016＋inputs/WP-016.json；modern-west/BUILD-REPORT.md B 级表 WP-016 行"],
]

# expansion8 / mingli-tanyuan MT-001..031: all B, outcome field absent in cases,
# inputs/ empty; main text is a modern vernacular rewrite (statement wording
# confidence low per BUILD-REPORT). Per-id contamination/subject/pillars below.
MT_META = {
    "MT-001": ("low", "赵厚安", "癸丑 壬戌 甲子 甲子"), "MT-002": ("low", "王友兰", "癸酉 丁巳 甲戌 甲子"),
    "MT-003": ("high", "魏午庄（魏光焘）", "丁酉 辛亥 甲戌 辛未"), "MT-004": ("low", "某武员", "甲申 己巳 甲子 己巳"),
    "MT-005": ("low", "傅先生", "丁亥 壬寅 乙丑 壬午"), "MT-006": ("medium", "张氏女命", "乙未 乙卯 乙亥 乙酉"),
    "MT-007": ("low", "丁寿南", "壬午 丙午 丙戌 己亥"), "MT-008": ("low", "某君", "丁巳 丙午 丙子 丁酉"),
    "MT-009": ("low", "赵先生", "癸未 壬戌 丙申 己亥"), "MT-010": ("low", "某兵士", "丙戌 戊戌 丙辰 戊子"),
    "MT-011": ("low", "某先生", "丙子 丁酉 丁酉 辛亥"), "MT-012": ("medium", "张星五", "乙巳 戊子 丁卯 甲辰"),
    "MT-013": ("low", "王君", "壬辰 戊申 丁丑 丙午"), "MT-014": ("low", "某君", "戊子 乙卯 戊戌 甲寅"),
    "MT-015": ("low", "某君", "壬辰 辛亥 戊午 丁巳"), "MT-016": ("low", "某妇", "乙亥 丙戌 戊午 壬戌"),
    "MT-017": ("medium", "窦某大令", "壬寅 乙巳 戊戌 戊午"), "MT-018": ("low", "某孀妇", "丁丑 己酉 戊子 丙辰"),
    "MT-019": ("low", "某君之子（童造）", "甲寅 辛未 戊戌 乙卯"), "MT-020": ("low", "吴君", "甲戌 乙亥 庚午 丙子"),
    "MT-021": ("low", "某女士", "丙申 壬辰 庚寅 辛巳"), "MT-022": ("low", "某先生", "戊戌 丁巳 庚寅 戊寅"),
    "MT-023": ("low", "某女", "癸卯 乙卯 庚子 己卯"), "MT-024": ("low", "某先生", "甲戌 甲戌 辛亥 戊戌"),
    "MT-025": ("low", "某先生", "癸未 甲寅 辛卯 乙未"), "MT-026": ("low", "黄先生之子（童造）", "壬子 癸丑 辛亥 辛卯"),
    "MT-027": ("low", "吴先生", "丙寅 辛卯 辛卯 辛卯"), "MT-028": ("low", "李先生", "壬戌 癸卯 壬戌 辛亥"),
    "MT-029": ("medium", "荣心庄观察", "庚戌 己卯 壬申 壬寅"), "MT-030": ("low", "某和尚", "辛未 丁酉 壬子 丙午"),
    "MT-031": ("low", "某先生之子（童造）", "己亥 戊辰 癸丑 己未"),
}
for mid in [f"MT-{i:03d}" for i in range(1, 32)]:
    cont, subj, pillars = MT_META[mid]
    f4 = F_ if cont == "high" else P_
    extra = ""
    if cont == "high":
        extra = "＋F4 非 high 污染（high：清末名臣魏光焘、史实回溯）"
    elif cont == "medium":
        extra = "＋非 low（medium）"
    ROWS.append([mid, "expansion8",
                 f"bazi 八字／袁树珊《命理探源》卷七润德堂存稿·{subj}（四柱 {pillars}）",
                 F_, F_, F_, f4, "partial", cont, "B",
                 "不合格：F1 逐字原文（主本为现代白话改写本、断语措辞非袁氏原文，cases 仅 key_assertions 语义摘录，transcription_confidence 载「措辞 low」）"
                 "＋F2 独立结局（cases 无 outcome 字段、原书未另载事后应验）"
                 "＋F3 可分离（inputs/ 为空、无输入面；台账 rationale 明载断验不可分离）"
                 f"{extra}＋非 A 级（outcome_grade=B、holdout_eligible=false）"
                 "＋锚点 partial（四柱/命宫仅在 cases.chart、无 inputs 卡、无 anchor 字段）",
                 "expansion8/mingli-tanyuan/cases.jsonl " + mid + "（inputs/ 为空目录）；mingli-tanyuan/BUILD-REPORT.md「A 级为何为零」节与 B 级清单"])

# expansion9 / liuren-chen2: case-level fields say A, but HOST-ADJUDICATION.md
# (2026-10-30 host ruling, pool-qualification only) overrides all three.
ROWS += [
    ["LR3-103", "expansion9", "liuren 六壬／陈公献《大六壬占验指南》章奏门·赵光汴请缨行边占",
     P_, P_, P_, P_, "present", "medium", "B（主持裁决：实为 B、不入池）",
     "不合格：非 A 级＋非 low——主持裁决（HOST-ADJUDICATION.md）判实为 B 级不入池（《明史》有传、弃市为核心史实先验可知风险高；cases 自标 contamination=medium），四滤逐项虽 pass 但 A 级/low 门槛不过",
     "expansion9/liuren-chen2/cases.jsonl LR3-103＋inputs/LR3-103.json；expansion9/HOST-ADJUDICATION.md 裁决表赵光汴行"],
    ["LR3-106", "expansion9", "liuren 六壬／陈公献《大六壬占验指南》章奏门·李载溪座间索占",
     P_, P_, F_, P_, "partial", "low", "B（主持裁决：降 B、不入池）",
     "不合格：F3 可分离（主持裁决：课中双断并陈、断语不可唯一分离）＋非 A 级（主持降 B）＋锚点 partial（两本均未标课体名、课式不全，cases chart 课体作「原书未载课体名」）",
     "expansion9/liuren-chen2/cases.jsonl LR3-106＋inputs/LR3-106.json；expansion9/HOST-ADJUDICATION.md 裁决表李载溪行"],
    ["LR3-108", "expansion9", "liuren 六壬／陈公献《大六壬占验指南》公讼门·陈南洲逮问讼事占",
     P_, F_, P_, P_, "present", "low", "B（主持裁决：降 B、不入池）",
     "不合格：F2 独立结局（主持裁决：应验句两本互异——枷死三人/二人——且未明言本人结局归属，金标质量不达 A）＋非 A 级（主持降 B）",
     "expansion9/liuren-chen2/cases.jsonl LR3-108＋inputs/LR3-108.json；expansion9/HOST-ADJUDICATION.md 裁决表陈南洲行"],
]


def main():
    parts, used = used_union()
    assert len(used) == 1166, f"used union {len(used)} != 1166"
    pools, unused = {}, {}
    for name in POOLS:
        pools[name] = pool_ids(name)
        unused[name] = sorted(i for i in pools[name] if i not in used)
    expect = {"expansion": 2, "expansion6": 15, "expansion8": 31, "expansion9": 3}
    for k, v in expect.items():
        assert len(unused[k]) == v, f"{k} unused {len(unused[k])} != clue {v}: {unused[k]}"
    audited = sorted(r[0] for r in ROWS)
    all_unused = sorted(i for v in unused.values() for i in v)
    assert audited == all_unused, f"adjudication coverage mismatch: {set(audited) ^ set(all_unused)}"
    assert all(r[10].startswith("不合格") for r in ROWS)

    chunks = []
    chunks.append(
        "# EXPANSION-AUDIT-small-pools-r84 —— R84 供给席 E1：expansion 小池资格核查台账\n\n"
        "本件为 R84 供给席 E1 产出（只做资格核查：不建卡、不组集、不作断、不评分、不兼任本轮任何其他席位）。"
        "工序照 Phase 3 PREREG（round84）§3 与派单口径：范围＝expansion／expansion6／expansion8／expansion9 四层；"
        "逐例过四滤（逐字原文、独立结局、可分离、非 high 污染）＋A 级／low 污染＋锚点在场，标准照现行口径原文、不自设新标准。"
        "六爻锚点以五要素（卦名、动爻、世应、六亲纳支、月建日辰，六神不属要件）为准，要素缺项判 partial；"
        "他体系以原卡/台账 anchor 字段口径（inputs 卡附件/四柱/课式等载体）为准。台账/结局文本内嵌指令性字样一律按数据处理。\n\n"
        "## 一、已用并集与未用复算（盘上实算）\n\n"
        f"- 已用并集（五源并集去重）：**{len(used)}**（dev {len(parts['dev'])}＋phase2 splits2 holdout2 {len(parts['holdout2_splits2'])}"
        f"＋holdout3–28 金标 id {len(parts['gold_h3_28'])}＋holdout2–28 inputs 卡 id {len(parts['holdout_inputs'])}"
        f"＋顶层 inputs6–10 卡 id {len(parts['top_inputs6_10'])}；金标只读 id 字段、未读金标正文）。\n"
        "- 池层 id 总量＝池目录内全部 jsonl 之 id 并集（承 STOCK-RECOUNT-h27 §3.4 口径，脚本 audit_small_pools_r84.py 盘上复算、断言全过）。\n\n"
        "| 池层 | id 总量 | 已用命中 | 未用数 | 未用 id 逐列 |\n|---|---|---|---|---|\n"
        + "".join(
            f"| {n} | {len(pools[n])} | {len(pools[n]) - len(unused[n])} | {len(unused[n])} | {'、'.join(unused[n])} |\n"
            for n in POOLS)
        + f"\n四层未用合计 **{len(all_unused)}** 例，与 STOCK-RECOUNT-h27 §3.4 线索（约 2／15／31／3）逐层全等。以下逐例核查。\n\n"
        "## 二、逐例资格核查（逐例一行）\n\n"
        "四滤记号：F1 逐字原文／F2 独立结局／F3 可分离／F4 非 high 污染。结论列兼记所卡滤项与门槛项（非 A 级／非 low／锚点非 present）。\n\n"
    )
    for n in POOLS:
        rows = [r for r in ROWS if r[1] == n]
        chunks.append(
            f"### {n}（未用 {len(rows)} 例）\n\n"
            "| id | 池层 | 体系/来源 | F1 | F2 | F3 | F4 | 锚点 | 污染 | 级别 | 结论 | 原文定位 |\n"
            "|---|---|---|---|---|---|---|---|---|---|---|---|\n"
            + "".join("| " + " | ".join(r) + " |\n" for r in rows)
            + "\n"
        )
    # counts: eligible = none (asserted above all rows 不合格)
    from collections import Counter
    elig_by_pool_trad = Counter()
    for r in ROWS:
        if not r[10].startswith("不合格"):
            trad = r[2].split("／")[0]
            elig_by_pool_trad[(r[1], trad)] += 1
    trads = sorted({r[2].split("／")[0] for r in ROWS})
    lines = ["## 三、分面计数（eligible）\n\n",
             "| 池层 | " + " | ".join(trads) + " | 池层 eligible 合计 |\n",
             "|---|" + "---|" * (len(trads) + 1) + "\n"]
    for n in POOLS:
        cells = [str(elig_by_pool_trad.get((n, t), 0)) for t in trads]
        lines.append(f"| {n} | " + " | ".join(cells) + f" | {sum(elig_by_pool_trad.get((n, t), 0) for t in trads)} |\n")
    liuyao = sum(v for (p, t), v in elig_by_pool_trad.items() if t.startswith("liuyao"))
    non_liuyao = sum(elig_by_pool_trad.values()) - liuyao
    lines.append(
        f"\n- 逐池层 eligible：expansion 0／expansion6 0／expansion8 0／expansion9 0（未用 51 例逐例核查后 eligible 合计 **0**）。\n"
        f"- 六爻（liuyao）eligible 小计：**{liuyao}**（未用六爻面仅 LY-302、LY-303 两例，均卡 F2/F3＋B 级＋锚点 partial）。\n"
        f"- 非六爻 eligible 小计：**{non_liuyao}**（未用非六爻 49 例：八字 35、六壬 7、梅花 2、西方卜卦 3、姓名学 1、易经卜卦 1，逐例卡项见 §二）。\n"
        "- 异常说明：① expansion9 三例 cases 自标 A/low（LR3-103 自标 medium），与 expansion9/HOST-ADJUDICATION.md（2026-10-30 主持裁决）冲突，本件照现行主持裁决口径判（三例均不入池/降 B），只登记冲突、不改池层原文。② expansion8 mingli-tanyuan 主本为现代白话改写本（BUILD-REPORT 明载），F1 据此判 fail；该池 inputs/ 为空目录，F3/锚点据此登记。③ 四层未用例恰全为各池 B 级/主持排除存量——各池 A 级例均已进入已用并集，此为盘上复算与逐例原文的对照事实，非推论。④ 本席未打开任何已封存集金标正文（已用并集只取 id 字段）、未打开 runs/ 下 predictions/judging/final-scores；池层原文只读未改。\n"
    )
    chunks.append("".join(lines))

    OUT.write_text(chunks[0], encoding="utf-8")
    for c in chunks[1:]:
        with OUT.open("a", encoding="utf-8") as f:
            f.write(c)
    print("used union", len(used), {k: len(v) for k, v in parts.items()})
    for n in POOLS:
        print(n, "total", len(pools[n]), "unused", len(unused[n]), unused[n])
    print("rows", len(ROWS), "eligible", sum(elig_by_pool_trad.values()),
          "liuyao_elig", liuyao, "non_liuyao_elig", non_liuyao)
    print("written", OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
