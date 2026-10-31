#!/usr/bin/env python3
# R93 数据席落盘脚本：承接对勘 + 本轮新定案汇编 + case-annotations-r93.json 生成。
# 纪律：只读 data/、runs/round93/ 点名件；禁读 predictions/judging 分数件
# （outcome-manifest.json 与 final-scores 之 analysis_r93 节不在此列，本脚本只读
# outcome-manifest 的 _r92 层与 cases 结局、host-mapping 对位）；不读封存集金标；不做 git。
import json, pathlib, collections, copy

BASE = pathlib.Path.home() / "workspace/divination/benchmark/phase3"
R92 = json.loads((BASE / "data/case-annotations-r92.json").read_text())
MAN93 = json.loads((BASE / "runs/round93/judging/outcome-manifest.json").read_text())
HM = json.loads((BASE / "runs/round93/judging/host-mapping.json").read_text())
INV = {v: k for k, v in HM.items()}
SEAL = (BASE / "data/holdout34-seal-log.md").read_text()
FREEZE = (BASE / "runs/round93/FREEZE-r93.md").read_text()

def card(cid):
    return json.loads((BASE / f"inputs-dev12/{cid}.json").read_text())

def pred(cid):
    return json.loads((BASE / f"runs/round93/predictions/{cid}.json").read_text())

def outcome(cid):
    return MAN93["cases"][cid]

# ---------- 工序一：承接对勘（_r92 层 12 件 vs r92 条 suggestion 逐字全等） ----------
addendum_layer = MAN93["_r92_carryover_notes_addendum"]
assert len(addendum_layer) == 12, len(addendum_layer)
assert set(addendum_layer) == {"AS-009", "DT-002", "DT-003", "DT-004", "DT-005", "DT-006",
                               "DT-007", "MP-015", "MP-016", "BZ-038", "LY-202", "LY-234"}
by_case_r92 = collections.defaultdict(list)
for a in R92["annotations"]:
    by_case_r92[a["case_id"]].append(a)
carry_match, carry_diff = [], []
for cid, txt in addendum_layer.items():
    pool = [a for a in by_case_r92[cid] if a.get("registered_round") == 92]
    assert pool, cid
    if any(a["manifest_carry_suggestion"] == txt for a in pool):
        carry_match.append(cid)
    else:
        carry_diff.append(cid)
assert len(carry_match) == 12 and not carry_diff, carry_diff
print(f"工序一对勘：全等 {len(carry_match)}／出入 {len(carry_diff)}")

# ---------- 工序二：本轮新定案逐件回源核对 ----------
# (a) OC-019：卡面无 tradition/system；basis 首行如实写明未标注、「卡面所载」指四柱
c = card("OC-019")
assert "tradition" not in c and set(c.keys()) == {"id", "subject", "context", "provenance", "language"}
assert pred("OC-019")["basis"].startswith("卡面未标注 tradition 字段，按题面体裁自决")
assert "以卡面所载徐乐吾书四柱为准" in pred("OC-019")["basis"]
assert outcome("OC-019") == "杨杏佛于1933年6月18日在上海中央研究院门前遇刺身亡。"
assert "OC-019 不成立" in FREEZE and "检查器语境误报" in FREEZE
# (a) YY2-004：卡面 tradition=liuyao 在场；basis 首行照录；未载字面指缺字与 null 残损
c = card("YY2-004")
assert c["tradition"] == "liuyao"
assert pred("YY2-004")["basis"].startswith("卡面 tradition 字段＝liuyao")
assert "本卦名原书版面即缺字" in pred("YY2-004")["basis"]
assert pred("YY2-004")["confidence"] == 0.18
assert outcome("YY2-004").startswith("直至戊寅年戊午月壬戌日故。")
assert "YY2-004 不成立" in FREEZE
# (b) WHY-112：封存日志 §七台账 2000 年／原书二〇〇一年、金标从原书；§十一与主持追认在册
assert "WHY-112：结局年份台账作「2000 年」、原书應驗情況（印刷 p196）作「二〇〇一年」" in SEAL
assert "金标结局改从原书" in SEAL and "主持追认" in SEAL
assert "530ab1250dfd6b57931d4d9e07ca1b3cbf8d566edf98fa4cfd85f792a66d54b0" in SEAL
assert "已用并集：1304＋29＝1333" in SEAL
# 指令性字样基线：manifest 侧五处在场、无新增同型件（cases 本体扫描）
for cid, phrase in [("BZ-036", "盲测比对须注"), ("BZ-042", "（盲测比对时以格局大富一项为主）"),
                    ("BZ-105", "使用时须分开统计"), ("LY-204", "勿以此斷")]:
    assert phrase in outcome(cid), cid
assert MAN93["_r56_lr2016_split"]["editor_note"] == "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
pats = ["盲测", "评分时", "请按", "须注", "勿以", "分开统计", "比对时"]
hits = {cid for cid, txt in MAN93["cases"].items() if any(p in txt for p in pats)}
assert hits == {"BZ-036", "BZ-042", "BZ-105", "LY-204"}, hits
print("工序二回源核对：OC-019／YY2-004／WHY-112／基线五处全过、无新增同型件")

# ---------- 新定案条目（3 条） ----------
def entry(cid, anon, disp, flag, finding, sugg, relation, seats, sources):
    return {
        "anon_id": anon, "case_id": cid, "disposition": disp,
        "finding": finding, "flag": flag, "manifest_carry_suggestion": sugg,
        "relation": relation, "registered_round": 93,
        "sources_checked": sources, "source_seats": seats,
    }

new_entries = []

new_entries.append(entry(
    "OC-019", INV["OC-019"], "不成立",
    "主持裁定（FREEZE-r93）：tradition 旗标候选——检查器命中「卡面所载」字面（实指四柱、非 tradition 值宣称）",
    "主持裁定不成立（FREEZE-r93 §2 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面键集为 id／subject／context／provenance／language，无 tradition／system 字段；R93 prediction basis 首行逐字作「卡面未标注 tradition 字段，按题面体裁自决：四柱子平合参，本例以卡面所载徐乐吾书四柱为准（卡面已注韦书另载全异、未取）」，首行未标注之声明与卡面实况相符，检查器命中之「卡面所载」指向四柱（盘面数据）、非 tradition 值宣称，系检查器语境误报。照 R92 余 37 件同型裁例：不成立、不作废、不重测。R93 manifest 结局逐字载「杨杏佛于1933年6月18日在上海中央研究院门前遇刺身亡。」，主问终局明载可核。与在册 R84 条、R89 条（同例 tradition 面检查器误报、不成立）及 R91 条（两书四柱全异面、部分成立）各轮／各旨独立、并行不悖。",
    "只登记不入层：自 R94 起承接本 R93 标注（不成立＝检查器语境误报，不入 _r93_carryover_notes_addendum 承接层）；结局原文照录不改。",
    "同例新轮同型并行（在册 R84／R89 不成立条与 R91 部分成立条各旨独立、互不覆盖）",
    ["主持检查器＋FREEZE-r93 裁定", "R93 数据席回读原卡"],
    ["divination/benchmark/phase3/inputs-dev12/OC-019.json",
     "divination/benchmark/phase3/runs/round93/predictions/OC-019.json",
     "divination/benchmark/phase3/runs/round93/judging/outcome-manifest.json cases[OC-019]",
     "divination/benchmark/phase3/runs/round93/judging/host-mapping.json（anon 解析：P3-5698e3de＝OC-019）",
     "divination/benchmark/phase3/runs/round93/FREEZE-r93.md"],
))

new_entries.append(entry(
    "YY2-004", INV["YY2-004"], "不成立",
    "主持裁定（FREEZE-r93）：tradition 旗标候选——检查器命中未载类字面（实指本卦名版面缺字与盘面／动爻 null 残损注记、非 tradition 未标注宣称）",
    "主持裁定不成立（FREEZE-r93 §2 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面逐字载 tradition＝'liuyao' 在场；R93 prediction basis 首行逐字作「卡面 tradition 字段＝liuyao」，照录无误；检查器命中之未载类字面指向本卦名版面缺字（得□之大壮）与 chart_lines_top_to_bottom／moving_lines 均为 null 之残损注记，该例输入残损已照实在 basis 注明、置信 0.18，非 tradition 未标注宣称。照 R78 判例口径：不成立、不作废、不重测。R93 manifest 结局逐字首句作「直至戊寅年戊午月壬戌日故。」，终局明载可核。该例残损面已在册 R75 条（部分成立），本条只裁 tradition 面、与之各旨独立、并行不悖。",
    "只登记不入层：自 R94 起承接本 R93 标注（不成立＝检查器语境误报，不入 _r93_carryover_notes_addendum 承接层）；结局原文照录不改。",
    "同例新旨并行（在册 R75 条残损面部分成立，各旨独立、互不覆盖）",
    ["主持检查器＋FREEZE-r93 裁定", "R93 数据席回读原卡"],
    ["divination/benchmark/phase3/inputs-dev12/YY2-004.json",
     "divination/benchmark/phase3/runs/round93/predictions/YY2-004.json",
     "divination/benchmark/phase3/runs/round93/judging/outcome-manifest.json cases[YY2-004]",
     "divination/benchmark/phase3/runs/round93/judging/host-mapping.json（anon 解析：P3-680cfa10＝YY2-004）",
     "divination/benchmark/phase3/runs/round93/FREEZE-r93.md"],
))

new_entries.append(entry(
    "WHY-112", None, "未核",
    "holdout34 封存席补录／更正登记：结局年份台账与原书不合（台账 outcome_record 作 2000 年、原书應驗情況作二〇〇一年；errata 候选）",
    "待核新登记（errata 候选，本席只转录封存席处置、不重裁）：holdout34 封存日志 §七逐字登记——该例结局年份，六爻分类占验台账 outcome_record 作「2000 年」、原书應驗情況（印刷 p196）作「二〇〇一年」，封存席经放大页图定字从原书，holdout34 金标结局已改从原书（二〇〇一年），其余从台账简体通例，异文已登记于该例 grade_note；R93 主持验封追认此处置（封存日志 §十二）。台账转录误差一层属实、金标侧已正，台账侧异文未改（本席不改台账、不读封存金标），列新待核／errata 候选挂起，待后续台账订正轮处置。该例首条；anon 编号无（holdout34 封存例，未入平台／验收 anon 体系，anon_id 记 null）。",
    "待核维持：自 R94 起承接本 R93 登记：按「结局年份台账转录作 2000 年、原书作二〇〇一年，金标已从原书；台账异文列 errata 候选、待台账订正轮处置」登记；金标原文照录不改。",
    "新登记（该例首条；holdout34 封存面 errata 候选、待核）",
    ["holdout34 封存席（R93 组集封存席）更正登记", "R93 主持验封追认", "R93 数据席转录登记"],
    ["divination/benchmark/phase3/data/holdout34-seal-log.md §七／§十一／§十二",
     "divination/benchmark/phase3/runs/round93/holdout34-build-report-r93.json（gold_corrections_r93 含 WHY-112）"],
))

assert len(new_entries) == 3
assert [e["case_id"] for e in new_entries] == ["OC-019", "YY2-004", "WHY-112"]
print("新定案条目：3 条（不成立 2／未核 1）")

# ---------- 落盘 ----------
out = copy.deepcopy(R92)
out["round"] = 93
out["annotations"] = R92["annotations"] + new_entries
assert out["annotations"][:529] == R92["annotations"]
verdicts = collections.Counter(a["disposition"] for a in out["annotations"])
assert verdicts == {"成立": 14, "部分成立": 442, "不成立": 73, "未核": 3}, verdicts
assert len(out["annotations"]) == 532

out["_provenance"] = (
    "R93 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／组集／修订，不改方法、不动分数）："
    "以 data/case-annotations-r92.json 为底承接全量 529 件（成立 14／部分成立 442／不成立 71／未核 2），前 529 件逐件原样、无删改（落盘脚本全等断言验过）；"
    "承接对勘：R93 manifest 新层 _r92_carryover_notes_addendum 12 件逐件与 r92 条（registered_round＝92 平台面条）manifest_carry_suggestion 全文逐字全等、出入 0 件；"
    "本轮新定案 3 条：FREEZE-r93 tradition 旗标裁定 2 件不成立（OC-019 检查器语境误报——「卡面所载」实指四柱；YY2-004 检查器语境误报——卡面 tradition＝liuyao 照录无误、未载字面实指本卦名缺字与盘面 null 残损注记），逐件回原卡与 R93 manifest 结局原文核对，只登记不入承接层；声明互斥组候选 0；"
    "WHY-112 结局年份台账与原书不合（台账 2000 年／原书二〇〇一年、金标已从原书、主持验封追认）新登记为待核／errata 候选 1 条（未核）；"
    "评审席旗标 id 对位失败现象级登记 1 件（special_checks 第 96 件；内容线索不可逐例入账、不编造逐例条目；与 BZ-040 享年待核重合之线索已并入附则 BZ-040 待核行作交叉注记）；"
    "合计 532 件（成立 14／部分成立 442／不成立 73／未核 3）。"
    "holdout34 封存事实转录登记（T＝29＝紫微 12＋六壬 13＋WHY 4、金标 SHA-256 530ab1250dfd6b57…、已用并集 1333、六壬台账余面 DA 59／BY 53、紫微 reserve 7）；"
    "紫微第三批进度转录（DIGEST-5 提炼 79 条、徐曾生挂起复评 7/7 通过、ZJ 通过 8、未用 eligible 累计 19、h34 组集取 12）；"
    "第八节执行面监测计数已转录附则（FREEZE-r93 §3：节名明引 480／487、六爻标目 325／325、主线认定行 451／487）；"
    "W56 结论转录（不可判定、W-T 悬置＋W-ID 现行、LR3-010 UNC 维持）；"
    "CZ-QX 维持 16；待核清单五件（BZ-029／BZ-040／LY-537／YM-070 维持＋WHY-112 新增待核）；指令性字样基线六处 manifest 侧五处在场、形态未变、本轮新增同型件无（评审包层一处禁读未复核、承接登记）；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留、不合并；已用并集 1333。"
)

out["special_checks"] = R92["special_checks"] + [
    {
        "item": "（R93）特别核查93：R92 附则承接对勘（_r92 层 12 件）",
        "conclusion": "R93 manifest 新层 _r92_carryover_notes_addendum 12 件（AS-009、DT-002–DT-007、MP-015／MP-016、BZ-038、LY-202、LY-234）逐件与 annotations-r92 对应条（registered_round＝92 平台面条）manifest_carry_suggestion 全文逐字全等，落实 12／出入 0。",
        "evidence": "runs/round93/judging/outcome-manifest.json _r92_carryover_notes_addendum；data/case-annotations-r92.json；data/manifest-carryover-r92-addendum.md §三。",
        "scope_note": "对勘只报不改史；manifest 与 annotations 两侧文本均不改动。",
    },
    {
        "item": "（R93）特别核查94：tradition 旗标定案总登记（FREEZE-r93 裁定 2 件不成立）",
        "conclusion": "本轮 tradition 旗标候选 2 件经 FREEZE-r93 §2 裁定全数不成立（检查器语境误报）：OC-019（卡面无 tradition/system 字段、首行如实写明未标注，检查器命中之「卡面所载」指向四柱）；YY2-004（卡面 tradition＝liuyao 在场、首行逐字照录无误，命中之未载类字面指向本卦名版面缺字与盘面／动爻 null 残损注记，该例残损面已在册 R75 条）。两件均已逐件回原卡、R93 prediction basis 与 manifest 结局原文复核后以不成立条入册，只登记不入承接层、不作废不重测。声明互斥组候选 0、无对应定案。本轮无成立件、无部分成立件（平台面）。",
        "evidence": "runs/round93/FREEZE-r93.md §2；inputs-dev12/OC-019.json、YY2-004.json；runs/round93/predictions/OC-019.json、YY2-004.json；runs/round93/judging/outcome-manifest.json cases[OC-019／YY2-004]；runs/round93/judging/host-mapping.json。",
        "scope_note": "同例多旨并行不悖、不合并；不成立条不入 _r93_carryover_notes_addendum 承接层。",
    },
    {
        "item": "（R93）特别核查95：WHY-112 errata 待核新登记与 holdout34 封存事实转录",
        "conclusion": "WHY-112 结局年份台账与原书不合：台账 outcome_record 作 2000 年、原书應驗情況（印刷 p196）作二〇〇一年，封存席经放大页图定字从原书、holdout34 金标结局已改从原书，R93 主持验封追认；台账侧异文列 errata 候选、以未核条入册挂起（待核清单由四件增至五件）。holdout34 封存事实（封存日志盘上登记、主持验封成立）：T＝29（紫微 12＋六壬 13＝DA 7＋BY 6＋WHY 4），金标 29 行 52765 字节、SHA-256＝530ab1250dfd6b57931d4d9e07ca1b3cbf8d566edf98fa4cfd85f792a66d54b0；已用并集 1304＋29＝1333；六壬台账余面 DA 59（下位 DA-082 起）／BY 53（下位 BY-054 起）；WHY 合格余面 0；紫微 reserve 7（ZW-024–027、ZW-033–035）。",
        "evidence": "data/holdout34-seal-log.md §一／§七／§八／§十一／§十二；runs/round93/holdout34-build-report-r93.json。",
        "scope_note": "只转录封存席与主持验封登记，不读封存金标、不改台账与金标任一侧。",
    },
    {
        "item": "（R93）特别核查96：评审席旗标 id 对位失败现象登记（现象级一条）",
        "conclusion": "本轮各评审席回传旗标所载 anon_id 经主持抽核，多数与本轮 host-mapping 对位失败——旗标内容线索不可逐例入账，本席只作现象级登记一条、不编造逐例条目、不据失败对位之 id 立任何逐例定案。其中一条内容线索与 BZ-040 享年待核事项重合，该线索已并入附则 BZ-040 既有待核行作交叉注记（BZ-040 不入 annotations、待核维持不变）；余线索不入账。后续轮次旗标回传须以当轮 host-mapping 重新对位后方可逐例处置。",
        "evidence": "runs/round93/judging/host-mapping.json（对位基准）；R93 主持抽核登记（本轮评审席回传旗标）。",
        "scope_note": "现象级登记，不含任何逐例旗标内容；BZ-040 交叉注记只登记重合事实、不裁享年。",
    },
    {
        "item": "（R93）特别核查97：紫微第三批进度、第八节监测计数与 W56 结论转录",
        "conclusion": "紫微第三批（SUMMARY-r93 主持汇编）：DIGEST-5 徐曾生特有断法提炼登记 79 条（第 19 章 12＋第 26＋27 章 10＋第 28 章 11＋第 29 章 22＋第 30 章 9＋第 32 章 15），残余挂起 11 项；徐曾生挂起 7 件复评通过 7/7（XZS-05／10／13／14／17／19／25→ZW-021–ZW-027）；许铨仁《正解》抽例通过 8（ZJ-01／02／04／05／06／07／08／09→ZW-028–ZW-035），不通过 1（ZJ-03 与 ZW-018 同例跨书重复）、挂起 1（ZJ-10）；未用 eligible 累计 19，h34 组集取 12、reserve 余 7。第八节执行面监测（FREEZE-r93 §3，只监测不判读）：全集 487 件节名明引 480（98.6%）、功量核标目段 480、主线认定行 451（92.6%）；六爻 325 件节名明引／标目 325（100%）、主线认定行 321；六壬 30 件节名明引 30、主线认定行 5；其余 132 件节名明引 125、主线认定行 125。W56（DIAG-LR-weight-dev93）：结论不可判定（T2／T3／T4 未齐备），W-T 悬置、W-ID 现行口径维持，LR3-010 UNC 维持（本轮另有 UNC 3 例：LR3-004／LR3-104／LR3-114，成因不同、分开登记）。",
        "evidence": "runs/round93/supply/ZIWEI-SUPPLY-BATCH3-SUMMARY-r93.md；runs/round93/FREEZE-r93.md §3；runs/round93/diagnosis/DIAG-LR-weight-dev93.md §6／§7。",
        "scope_note": "只转录登记，不增删各席结论；第八节成立状态现行不变、W56 不改任何分数与方法。",
    },
    {
        "item": "（R93）特别核查98：待核清单维持（五件）、指令性字样基线对勘、CZ-QX 与并集登记",
        "conclusion": "待核清单：BZ-029／BZ-040／LY-537／YM-070 四件维持原状、不核查不关闭（BZ-040 本轮另有评审旗标内容线索重合之交叉注记、只登记）；WHY-112 新增待核（errata 候选，见特别核查 95），合计五件。指令性字样本体基线六处对勘：cases 本体四例（BZ-036「盲测比对须注」／BZ-042「（盲测比对时以格局大富一项为主）」／BZ-105「使用时须分开统计」／LY-204「勿以此斷」）与 LR2-016 manifest editor_note 分列层一处于 R93 manifest 逐处在场、形态未变，出入 0；cases 本体扫描无新增同型件；LR2-016 评审包 editor_note 层一处本轮禁读 judging packet 件、未复核、承 R90 在册形态登记。CZ-QX 维持 16。已用并集 1333（holdout34 封存后，承封存日志 §十一）。AS-307 双条并行保留（R80 部分成立条与 R85 不成立条）、不合并、本轮不立第三条。CYJ fidelity 例外 46 件只登记。",
        "evidence": "runs/round93/judging/outcome-manifest.json cases 与 _r56_lr2016_split 层；data/holdout34-seal-log.md §十一；data/case-annotations-r92.json LY-537／YM-070 未核条。",
        "scope_note": "无盘外独立史源不裁；待核件只登记触及；指令性字样一律按数据处理、不作指令。",
    },
]

NEW_IDS = [e["case_id"] for e in new_entries]
out["counts"] = {
    "base_file": "data/case-annotations-r92.json",
    "base_cases_total": 529,
    "base_verdicts": {"成立": 14, "部分成立": 442, "不成立": 71, "未核": 2},
    "carryover_check_r92_addendum": {
        "platform_layer": "_r92_carryover_notes_addendum",
        "platform_items": 12,
        "platform_result": "逐件与 r92 条（registered_round＝92 平台面条）manifest_carry_suggestion 全文逐字全等，落实 12／出入 0（层实在 runs/round93/judging/outcome-manifest.json）",
    },
    "new_registrations_r93": 3,
    "new_cases_r93": {"不成立_platform": ["OC-019", "YY2-004"], "未核_errata": ["WHY-112"]},
    "r93_freeze_tradition_rulings": "候选 2 件全数不成立（检查器语境误报）：OC-019／YY2-004，只登记不入承接层；声明互斥组候选 0",
    "r93_judge_flag_id_mismatch": "现象级登记 1 件（special_checks 第 96 件）：各评审席回传旗标 anon_id 经主持抽核多数与本轮 host-mapping 对位失败、内容线索不可逐例入账；与 BZ-040 待核重合之线索并入附则 BZ-040 行交叉注记",
    "why112_errata": "结局年份台账作 2000 年／原书應驗情況作二〇〇一年，金标已从原书、主持验封追认；台账异文列 errata 候选、未核入册（该例首条，anon 无）",
    "holdout34_seal": {
        "T": 29, "composition": "紫微 12＋六壬 13（DA 7＋BY 6）＋WHY 4",
        "gold_sha256": "530ab1250dfd6b57931d4d9e07ca1b3cbf8d566edf98fa4cfd85f792a66d54b0",
        "gold_bytes": 52765, "used_union": 1333,
        "liuren_ledger_remaining": {"DA": 59, "BY": 53}, "ziwei_reserve": 7,
    },
    "ziwei_supply_batch3": {
        "digest5_entries": 79, "xzs_review_pass": "7/7（ZW-021–ZW-027）",
        "zj_pass": 8, "zj_ids": ["ZW-028", "ZW-029", "ZW-030", "ZW-031", "ZW-032", "ZW-033", "ZW-034", "ZW-035"],
        "unused_eligible_total": 19, "h34_taken": 12, "reserve_after_h34": 7,
    },
    "section8_monitoring_r93": {
        "source": "FREEZE-r93 §3（只监测、不判读）",
        "all": {"n": 487, "节名明引": 480, "节名明引率": "98.6%", "编号R80明引": 47, "机制全称明引": 0, "功量核标目段": 480, "主线认定行": 451, "主线认定行率": "92.6%"},
        "liuyao": {"n": 325, "节名明引": 325, "功量核标目段": 325, "主线认定行": 321},
        "liuren": {"n": 30, "节名明引": 30, "功量核标目段": 30, "主线认定行": 5},
        "other": {"n": 132, "节名明引": 125, "功量核标目段": 125, "主线认定行": 125},
    },
    "w56_conclusion": "不可判定（T2／T3／T4 未齐备）；W-T 悬置＋W-ID 现行；LR3-010 UNC 维持；本轮另 UNC 3 例（LR3-004／LR3-104／LR3-114）成因不同、分开登记",
    "instructional_baseline_six": "manifest 侧五处（BZ-036／BZ-042／BZ-105／LY-204 cases 本体＋LR2-016 分列 editor_note）逐处在场、形态未变、出入 0；评审包层一处禁读未复核、承接登记；本轮新增同型件无",
    "czqx_same_tier_count": 16,
    "as307_double_entry": "R80 部分成立条与 R85 不成立条并行保留、不合并；本轮不立第三条",
    "pending_five": "BZ-029／BZ-040／LY-537／YM-070 维持原状＋WHY-112 新增待核（errata 候选）；BZ-040 另有评审旗标线索重合交叉注记、只登记",
    "used_union": 1333,
    "cases_total": 532,
    "verdicts": {"成立": 14, "部分成立": 442, "不成立": 73, "未核": 3},
}

target = BASE / "data/case-annotations-r93.json"
target.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
back = json.loads(target.read_text())
assert back["annotations"][:529] == R92["annotations"]
assert len(back["annotations"]) == 532
assert collections.Counter(a["disposition"] for a in back["annotations"]) == verdicts
assert len(back["special_checks"]) == 98
print("落盘完成：", target, "annotations =", len(back["annotations"]), dict(verdicts),
      "special_checks =", len(back["special_checks"]))
print("NEW:", NEW_IDS)
