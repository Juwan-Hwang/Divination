#!/usr/bin/env python3
# R92 数据席落盘脚本：承接对勘 + 平台面新定案汇编 + case-annotations-r92.json 与附则生成。
# 纪律：只读 data/、runs/round92/、inputs-dev12/、runs/round91/ 承接件；不读封存集金标；不做 git。
import json, pathlib, re, collections, copy

BASE = pathlib.Path.home() / "workspace/divination/benchmark/phase3"
R91 = json.loads((BASE / "data/case-annotations-r91.json").read_text())
MAN92 = json.loads((BASE / "runs/round92/judging/outcome-manifest.json").read_text())
HM = json.loads((BASE / "runs/round92/judging/host-mapping.json").read_text())
INV = {v: k for k, v in HM.items()}

def pred(cid, rnd=92):
    return json.loads((BASE / f"runs/round{rnd}/predictions/{cid}.json").read_text())

def card(cid):
    return json.loads((BASE / f"inputs-dev12/{cid}.json").read_text())

def outcome(cid):
    return MAN92["cases"][cid]

# ---------- 工序一：承接对勘 ----------
addendum_layer = MAN92["_r91_carryover_notes_addendum"]
assert len(addendum_layer) == 103, len(addendum_layer)
by_case_r91 = collections.defaultdict(list)
for a in R91["annotations"]:
    by_case_r91[a["case_id"]].append(a)
carry_match, carry_diff = [], []
for cid, txt in addendum_layer.items():
    pool = [a for a in by_case_r91[cid] if a.get("registered_round") == 91]
    assert pool, cid
    if any(a["manifest_carry_suggestion"] == txt for a in pool):
        carry_match.append(cid)
    else:
        carry_diff.append(cid)
assert len(carry_match) == 103 and not carry_diff, carry_diff
print(f"工序一对勘：全等 {len(carry_match)}／出入 {len(carry_diff)}")

# ---------- 工序二.2 候选扫描与分类 ----------
MARKERS = ["残损", "未载", "不合", "订正", "无盘面", "原文误", "缺载", "存疑",
           "推算复原", "不可补", "未给", "未录", "未附", "缺字", "残泐", "未直载"]
candidates = []
for p in sorted((BASE / "runs/round92/predictions").glob("*.json")):
    d = json.loads(p.read_text())
    if any(m in d.get("basis", "") for m in MARKERS):
        candidates.append(d["case_id"])
NEW_BASIS = ["DT-002", "DT-003", "DT-004", "DT-005", "DT-006", "DT-007",
             "MP-015", "MP-016", "BZ-038", "LY-202", "LY-234"]
CAT_B = ["LY-009", "LY-010", "LY-013", "LY-016", "LY-029", "LY-031", "LY-216", "LY-218",
         "LY-220", "LY-221", "LY-228", "LY-235", "LY-237", "LY-240", "LY-243", "LY-244",
         "LY-254", "LY-315", "LY-329", "LY-336", "LY-342", "LY-403", "LY-404", "LY-405",
         "LY-407", "LY-408", "LY-411", "LY-428", "LY-432", "LY-504", "LY-515", "LY-517",
         "LY-605", "LY-614", "LY-617", "LY-625", "YM-049"]
CAT_C = ["AS-001", "AS-002", "AS-004", "AS-005", "AS-007", "AS-010", "AS-011", "AS-013",
         "AS-014", "AS-204", "AS-208", "AS-209", "AS-211", "AS-213", "AS-215",
         "LR2-013", "LR3-010", "LY-205", "LY-429", "LY-437", "LY-506"]
CAT_D = ["OC-001"]
CAT_PENDING = ["LY-537"]
assert len(CAT_B) == 37 and len(CAT_C) == 21 and len(CAT_D) == 1 and len(CAT_PENDING) == 1
CAT_A = [c for c in candidates if c not in NEW_BASIS + CAT_B + CAT_C + CAT_D + CAT_PENDING]
assert len(candidates) == 174, len(candidates)
assert len(CAT_A) == 103, (len(CAT_A), CAT_A)
# A 类每件须有在册条目或 R91 §3.5 复触口径可据（OC-023／YY-023／YY2-003 三件承 R91 附则 §3.5 登记口径）
for c in CAT_A:
    assert by_case_r91.get(c) or c in ("OC-023", "YY-023", "YY2-003"), c
print(f"工序二候选：{len(candidates)} 件；入册 {len(NEW_BASIS)}；复触 {len(CAT_A)}；推断 {len(CAT_B)}；设计 {len(CAT_C)}；tradition {len(CAT_D)}；待核同旨 {len(CAT_PENDING)}")

# ---------- 新定案条目 ----------
SRC = lambda cid, extra=None: [
    f"divination/benchmark/phase3/inputs-dev12/{cid}.json",
    f"divination/benchmark/phase3/runs/round92/judging/outcome-manifest.json cases[{cid}]",
    f"divination/benchmark/phase3/runs/round92/predictions/{cid}.json",
] + (extra or [])
SEATS_BASIS = ["R92 平台盲测席 basis 自报", "R92 数据席回读原卡"]

def entry(cid, flag, finding, sugg, relation, seats, sources):
    return {
        "anon_id": INV[cid], "case_id": cid, "disposition": "部分成立",
        "finding": finding, "flag": flag, "manifest_carry_suggestion": sugg,
        "relation": relation, "registered_round": 92,
        "sources_checked": sources, "source_seats": seats,
    }

new_entries = []

# §三.1 FREEZE 首件 AS-009
cid = "AS-009"
assert card(cid)["tradition"] == "horary"
assert "卡面未标注 tradition" in pred(cid)["basis"]
assert "systems_used：horary" in pred(cid)["basis"] or "systems_used: horary" in pred(cid)["basis"] or "horary" in pred(cid)["basis"]
assert "found the dog tied up under a table" in outcome(cid)
new_entries.append(entry(
    cid,
    "主持裁定（FREEZE-r92）：卡面实载 tradition='horary'，R92 prediction basis 首行误称「卡面未标注 tradition」（三度重现）",
    "主持裁定部分成立（FREEZE-r92 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面顶层逐字载 tradition＝'horary'（卡键集 uid／tradition／subject／context／provenance）；R92 prediction basis 首行逐字作「卡面未标注 tradition」，与卡面实载不符、措辞不实一层成立，且系该例三度重现（R85 轮同型措辞不精确附注、R90 轮同旨部分成立）。但该例实际作断体系为 horary（basis 首行自注 systems_used 为 horary、与卡面 tradition 一致），无体系误标、无虚构卡面值，不作废不重测（照 R90／R91 同例裁例）。R92 manifest 结局逐字载狗于 Long Acre 桌下被寻回送还，主问终局明载可核。故部分成立。与在册 R85 条（不成立＋措辞不精确附注）、R86 条（OCR 残损旨）及 R90 条（R90 轮同旨部分成立）各轮／各旨独立、并行不悖。",
    "平台侧新登记：自 R93 起承接本 R92 标注：按「卡面实载 tradition＝horary、R92 首行误称未标注属措辞不实（三度重现），注记须以卡面实载值 horary 为准回写；实际作断体系与卡面一致、无体系误标，部分成立」登记；结局原文照录不改。",
    "同例新轮新旨（R92 主持裁定；与 R85／R86／R90 在册条并行）",
    ["主持检查器＋FREEZE-r92 裁定", "R92 数据席回读原卡"],
    SRC(cid, ["divination/benchmark/phase3/runs/round92/FREEZE-r92.md"]),
))

# §三.2 DT 组：化神未载 6 件
DT_INFO = {
    "DT-002": ("山水蒙", "寅、午动爻化神卡面未直载", "后果于九月己卯日巳时生男，母子俱得平安。",
               "同例新旨并行（在册 1 条各旨独立、互不覆盖）", "与在册 R91 条（动爻原文飞伏语叙述、读法有歧旨）各旨独立、并行不悖。"),
    "DT-003": ("艮为山（八纯艮）", "午火动化神未载", "其人果死不还。",
               "新登记（该例首条）", ""),
    "DT-004": ("天火同人", "两动化神未载", "其子果死（原文作『其子果死不救』）。",
               "同例新旨并行（在册 1 条各旨独立、互不覆盖）", "与在册 R87 条（动爻组飞伏交错旨）各旨独立、并行不悖。"),
    "DT-005": ("泽水困", "酉金动化神未载", "果然无事（子病无事）。",
               "新登记（该例首条）", ""),
    "DT-006": ("山风蛊", "动爻化神未载", "果然无事（子病无事）。",
               "同例新旨并行（在册 1 条各旨独立、互不覆盖）", "与在册 R87 条（动爻飞伏语含混旨）各旨独立、并行不悖。"),
    "DT-007": ("火水未济", "酉金动化神未载", "后果二月壬辰日，贼果来偷其家财。",
               "新登记（该例首条）", ""),
}
for cid in ["DT-002", "DT-003", "DT-004", "DT-005", "DT-006", "DT-007"]:
    hexa, phrase, oc, relation, tail = DT_INFO[cid]
    att = card(cid)["context"]["attachments"]
    assert att["hexagram"] == hexa, (cid, att["hexagram"])
    assert len(att["chart_lines_top_to_bottom"]) == 6
    assert phrase in pred(cid)["basis"], cid
    assert outcome(cid) == oc, (cid, outcome(cid))
    finding = (f"回原卡——卡面 attachments 只载本卦「{hexa}」逐爻六行与 moving_lines，未载变卦全盘与动爻化神，缺载一层属实；"
               f"R92 basis 逐字照实登记「{phrase}」、动化方向只按本卦爻位定性并降置信；"
               f"R92 manifest 结局逐字载「{oc}」，终局明载可核。故部分成立。{tail}")
    new_entries.append(entry(
        cid,
        "R92 平台 basis 留痕：卡面未载动爻化神与变卦全盘（残损类）",
        finding,
        "平台侧新登记：自 R93 起承接本 R92 标注：按「卡面未载动爻化神与变卦全盘、已照实登记按本卦爻位定性；终局明载，部分成立」登记；结局原文照录不改。",
        relation, SEATS_BASIS, SRC(cid),
    ))

# §三.2 MP 组：无盘面 2 件
MP_INFO = {
    "MP-015": "拜登因辩论表现与选情压力于2024-07-21宣布退选，未能竞选连任；特朗普于2024-11-05胜选当选第47任总统",
    "MP-016": "特朗普当选第47任总统，选举人票312张",
}
for cid in ["MP-015", "MP-016"]:
    c = card(cid)
    assert "attachments" not in (c.get("context") or {}) and set(c.keys()) == {"id", "subject", "context", "provenance", "language"}
    assert "输入残损注明：无占具/盘面字段" in pred(cid)["basis"], cid
    assert outcome(cid) == MP_INFO[cid]
    extra = ""
    sugg = "平台侧新登记：自 R93 起承接本 R92 标注：按「卡面无任何占具／盘面字段、已照实登记只据题面事实作断；终局明载，部分成立」登记；结局原文照录不改。"
    if cid == "MP-016":
        assert "字占残损：仅一字无完整拆字盘面" in pred(cid)["basis"]
        extra = "兼字占一面：所问以『相』字问卜，R92 basis 逐字登记「字占残损：仅一字无完整拆字盘面，不以字象充数」，此面并载；"
        sugg = "平台侧新登记：自 R93 起承接本 R92 标注：按「卡面无任何占具／盘面字段、已照实登记只据题面事实作断；兼字占仅一字、无完整拆字盘面已照实登记；终局明载，部分成立」登记；结局原文照录不改。"
    finding = (f"回原卡——卡面只有 subject／context／provenance，未载任何卦盘、出生时刻或排盘数据，缺载一层属实；"
               f"R92 basis 逐字照实登记「输入残损注明：无占具/盘面字段」、只据题面已载事实与选情结构作断并降置信；{extra}"
               f"R92 manifest 结局逐字载「{MP_INFO[cid]}」，终局明载可核。故部分成立。该例首条。"
               f"与在册 R87 MP 组各条（MP-001–MP-014／MP-017／MP-018 无盘面旨）同型、各自独立。")
    new_entries.append(entry(
        cid,
        "R92 平台 basis 留痕：输入残损——无占具／盘面字段（残损类）",
        finding, sugg, "新登记（该例首条）", SEATS_BASIS, SRC(cid),
    ))

# §三.3 singles
cid = "BZ-038"
assert "系他人将其生辰译成八字" in json.dumps(card(cid), ensure_ascii=False)
assert "转译残损" in pred(cid)["basis"]
assert "1931年卒于上海" in outcome(cid)
new_entries.append(entry(
    cid,
    "R92 平台 basis 留痕：卡面仅存四柱、生辰系他人转译八字（自注类）",
    "回原卡——卡面 birth.date 逐字自注「原书仅存四柱（原书注明系他人将其生辰译成八字）」，生辰经他人转译一层属实且卡面自注，attachments 只载四柱；R92 basis 逐字照实登记此转译残损、置信下调；四柱实载，R92 manifest 结局逐字载哈同白手起家成为上海地产大王、1931年卒于上海等事，终局明载可核。故部分成立（与在册 R91 OC-015 条二手传略面同型）。与在册 R76 条（tradition 首行旨）各旨独立、并行不悖。",
    "平台侧新登记：自 R93 起承接本 R92 标注：按「卡面仅存四柱、生辰系他人转译八字卡面已自注、已照实登记并降置信；终局明载，部分成立」登记；结局原文照录不改。",
    "同例新旨并行（在册 1 条各旨独立、互不覆盖）", SEATS_BASIS, SRC(cid),
))

cid = "LY-202"
att = card(cid)["context"]["attachments"]
assert set(att.keys()) == {"casting_method", "hexagram", "moving_lines", "chart_lines_top_to_bottom"}
assert "卡面未载空亡，按乙巳日甲辰旬空寅卯" in pred(cid)["basis"]
assert "後果於寅年醫好富翁" in outcome(cid)
new_entries.append(entry(
    cid,
    "R92 平台 basis 留痕：卡面未载空亡、按日干支推得（残损类）",
    "回原卡——卡面 attachments 逐项核未载空亡字段（只有 casting_method／hexagram／moving_lines／chart_lines_top_to_bottom），空亡未载属实；R92 basis 逐字照实登记「卡面未载空亡，按乙巳日甲辰旬空寅卯」推得并注明，所涉官鬼寅木 basis 自注「终身功名非所问，只记」、不涉本问（终身财福）主用；逐爻盘面实载，R92 manifest 结局为长文实载（寅年医好富翁、午年一榜、援例县令等事），终局明载可核。故部分成立。该例首条。",
    "平台侧新登记：自 R93 起承接本 R92 标注：按「卡面未载空亡字段、按日干支推得已照实注明（所涉官鬼一爻非本问主用、只记）；终局明载，部分成立」登记；结局原文照录不改。",
    "新登记（该例首条）", SEATS_BASIS, SRC(cid),
))

cid = "LY-234"
att = card(cid)["context"]["attachments"]
assert set(att.keys()) == {"casting_method", "hexagram", "moving_lines", "chart_lines_top_to_bottom"}
lines = att["chart_lines_top_to_bottom"]
ben = [ln.split("　")[0] for ln in lines]
assert not any("官鬼" in x for x in ben), ben
assert any("官鬼亥水" in ln for ln in lines) and any("官鬼子水" in ln for ln in lines)
assert "卡面未载官鬼爻与伏神栏" in pred(cid)["basis"]
assert "果應於寅年。後終於未年" in outcome(cid)
new_entries.append(entry(
    cid,
    "R92 平台 basis 留痕：卡面未载伏神栏、本卦无官鬼、伏神规则推得（残损类）；basis 兼称变爻亦无官鬼一层与卡面不合并载",
    "回原卡——卡面 attachments 逐项核未载伏神／hidden_lines 栏，本卦逐爻六亲（父母／兄弟／子孙）无官鬼一层属实；R92 basis 逐字照实登记伏神午火按本宫首卦同位规则推得、属推算复原并降置信。另 basis 兼称「变爻亦无官鬼」一层与卡面不合：卡面变卦盘四爻（子孙未土动）化官鬼亥水、初爻（父母寅木动）化官鬼子水，官鬼于变卦盘两见——此层并载、不据以改缺载面定案。R92 manifest 结局逐字载「果應於寅年。後終於未年」等，终局明载可核。故部分成立。该例首条。",
    "平台侧新登记：自 R93 起承接本 R92 标注：按「卡面未载伏神栏、本卦六亲无官鬼，伏神按本宫首卦规则推得已照实注明；basis 称变爻亦无官鬼一层与卡面变卦盘官鬼两见不合并载；终局明载，部分成立」登记；结局原文照录不改。",
    "新登记（该例首条）", SEATS_BASIS, SRC(cid),
))

assert len(new_entries) == 12
assert all(e["anon_id"] for e in new_entries)
assert len({e["anon_id"] for e in new_entries}) == 12

# ---------- 落盘 ----------
out = copy.deepcopy(R91)
out["round"] = 92
out["annotations"] = R91["annotations"] + new_entries
# 前 517 件全等断言
assert out["annotations"][:517] == R91["annotations"]
verdicts = collections.Counter(a["disposition"] for a in out["annotations"])
assert verdicts == {"成立": 14, "部分成立": 442, "不成立": 71, "未核": 2}, verdicts
assert len(out["annotations"]) == 529

out["_provenance"] = (
    "R92 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／组集／修订，不改方法、不动分数）："
    "以 data/case-annotations-r91.json 为底承接全量 517 件（平台面 465＋验收面补编 52；成立 14／部分成立 430／不成立 71／未核 2），前 517 件逐件原样、无删改（落盘脚本全等断言验过）；"
    "承接对勘：R92 manifest 新层 _r91_carryover_notes_addendum 103 件逐件与 r91 条（registered_round＝91 平台面条）manifest_carry_suggestion 全文逐字全等、出入 0 件；"
    "本轮平台面新定案 12 条全部分成立（FREEZE-r92 裁定 AS-009 部分成立为平台面新定案第一件；盲测席 basis 自报定案 11 件：DT 组化神未载 6＋MP 组无盘面 2＋singles 3，逐件回原卡与 R92 manifest 结局原文核对）；"
    "tradition 旗标余 37 件 FREEZE-r92 裁定不成立、只登记不入 annotations；声明互斥组候选 0；"
    "盲测席 basis 自报候选 174 件中未入册 163 件分因登记（同旨复触 103／推断性读法注记 37／卡面设计形态与组通式 21／tradition 首行注记 1／待核同旨 1）；"
    "合计 529 件（成立 14／部分成立 442／不成立 71／未核 2）。"
    "紫微供给次批转录登记（次批 #3 徐曾生新增 ZW-019／ZW-020 均 A-low eligible、#4 陆在田通过 0；未用 eligible 累计 4＝ZW-017／ZW-018／ZW-019／ZW-020，距 h34 判据 ≥9 差 5）；"
    "第八节执行面监测计数已转录附则（FREEZE-r92 §3：节名明引 440／487＝90.3%、主线认定行 480／487＝98.6%）；"
    "CZ-QX 维持 16；待核四件（BZ-029／BZ-040／LY-537／YM-070）维持挂起；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留、不合并、本轮不立第三条；已用并集 1304。"
)

out["special_checks"] = R91["special_checks"] + [
    {
        "item": "（R92）特别核查88：R91 附则承接对勘与 AS-009 三度重现定案登记",
        "conclusion": "R92 manifest 新层 _r91_carryover_notes_addendum 103 件逐件与 annotations-r91 对应条（registered_round＝91 平台面条）manifest_carry_suggestion 全文逐字全等，落实 103／出入 0。AS-009 经 FREEZE-r92 裁定部分成立（措辞不实、三度重现）入册为本轮平台面新定案第一件，承接建议承 R90／R91 同例注记口径续写（以卡面实载值 horary 回写）。",
        "evidence": "runs/round92/judging/outcome-manifest.json _r91_carryover_notes_addendum；data/case-annotations-r91.json；runs/round92/FREEZE-r92.md §2；inputs-dev12/AS-009.json；runs/round92/predictions/AS-009.json。",
        "scope_note": "对勘只报不改史；manifest 与 annotations 两侧文本均不改动。",
    },
    {
        "item": "（R92）特别核查89：平台面旗标定案总登记（新定案 12 条）与承接筛检（候选 174 件分类）",
        "conclusion": "本轮平台面新定案 12 条全部分成立：FREEZE 裁定 1（AS-009）＋盲测席 basis 自报 11（DT 组卡面未载动爻化神 6：DT-002–DT-007；MP 组无盘面 2：MP-015／MP-016；singles 3：BZ-038 转译自注、LY-202 空亡未载、LY-234 伏神栏未载）。basis 自报候选 174 件（标记词：残损／未载／未直载／不合／订正／无盘面／原文误／缺载／存疑／推算复原／不可补／未给／未录／未附／缺字／残泐）中未入册 163 件分因：同旨已在册复触 103（照在册条承接、不重复立条；AS-009 OCR 残损面计入此类、其 tradition 面另经 FREEZE 入册）、纯推断性／读法注记 37（门类对表不合、应期三路取舍、取用存疑、两占分断读法等，非卡面缺陷主张）、卡面设计形态与组通式 21（Lilly 散文述位组 15 经 R87 筛检定为设计形态；LR2-013 天盘全图与 LR3-010 代占未具名各 1 为组设计／题面设定；LY-429／LY-437／LY-506 病位复核六神旁记 3 与 LY-205 伏位旁记 1）、tradition 首行如实注记 1（OC-001，非盘面缺陷）、待核同旨 1（LY-537，归待核维持）。tradition 旗标余 37 件 FREEZE-r92 裁定不成立、只登记；声明互斥组候选 0、无对应定案。本轮无成立件、无新增待核件。",
        "evidence": "runs/round92/predictions 全部 487 件 basis 扫描；inputs-dev12 逐件回读；runs/round92/judging/outcome-manifest.json 结局原文；runs/round92/FREEZE-r92.md §2；data/case-annotations-r91.json 在册条目。",
        "scope_note": "同例多旨并行不悖、不合并；与在册同旨者不重复立条。",
    },
    {
        "item": "（R92）特别核查90：紫微供给面次批登记",
        "conclusion": "次批 #3 徐曾生《紫微斗数命运分析》续评：候选 25 例（XZS-01–25），通过 2 例新增 ZW-019（XZS-08，第 25 章例解主例，A-low）／ZW-020（XZS-12，第 28 章借钱被倒案、取自楚皇著作，A-low），不通过 16（无独立结局 12／high 污染 3／锚不成立 1），挂起待提炼 7。次批 #4 陆在田《紫微斗数股票战略》定点推进：LD-01–LD-03 全不通过、通过 0。紫微面未用 eligible 累计＝4（ZW-017／ZW-018／ZW-019／ZW-020），池 eligible 累计 17（ZW-004–ZW-020），距 h34 组集判据 ≥9 差 5。",
        "evidence": "runs/round92/supply/ZIWEI-SUPPLY-BATCH2-XZS-r92.md；runs/round92/supply/ZIWEI-SUPPLY-BATCH2-LZT-r92.md。",
        "scope_note": "只转录登记，不增删供给席结论；挂起例不计 eligible、不预支例数。",
    },
    {
        "item": "（R92）特别核查91：第八节执行面监测计数转录（FREEZE-r92 §3，只监测、不判读）",
        "conclusion": "全集 487 件：节名明引 440（90.3%）、编号 R80 明引 247、机制全称明引 234、功量核标目段 440（90.3%）、主线认定行 480（98.6%）。分组：六爻 325 件节名明引 285（87.7%）／主线认定行 325（100%）；六壬 30 件节名明引 30（100%）／主线认定行 30（100%）；其余 132 件节名明引 125（94.7%）／主线认定行 125（94.7%）。与 holdout33 验收面对照（节名明引 1／28＝3.6%）平台面缺口大幅收窄之登记照 FREEZE 原文转录；第八节成立状态现行不变、不外推验收面。",
        "evidence": "runs/round92/FREEZE-r92.md §3 表。",
        "scope_note": "只转录计数，不判读、不改第八节成立状态。",
    },
    {
        "item": "（R92）特别核查92：待核四件维持、CZ-QX 维持 16 与并集登记",
        "conclusion": "待核四件维持原状、不核查不关闭：BZ-029（俞大维卒年待核＋旗标错配线索；本轮 basis 无新证据）、BZ-040（许世英享年待核；本轮 basis 为格局断语、无分歧自注新旨）、LY-537（「申予日」衍字疑，以未核条目随承接在册；本轮 basis 输入残损注记与该例十八问答组形态同域、只登记触及、维持未核）、YM-070（「甲寅旬」出处待核并「同行都下」语义未明，以未核条目随承接在册；本轮 basis 无残损自报、无新证据）。CZ-QX 维持 16。已用并集 1304（runs/round92/used-ids-r92.json 实测）。AS-307 双条并行保留（R80 部分成立条与 R85 不成立条），本轮 basis 输入残损面与在册 R86 条同旨、不另立第三条。CYJ fidelity 例外 46 件只登记。",
        "evidence": "data/case-annotations-r91.json LY-537／YM-070 未核条；runs/round92/predictions BZ-029／BZ-040／LY-537／YM-070 basis；runs/round92/used-ids-r92.json。",
        "scope_note": "无盘外独立史源不裁；待核件只登记触及。",
    },
]

NEW_IDS = [e["case_id"] for e in new_entries]
out["counts"] = {
    "base_file": "data/case-annotations-r91.json",
    "base_cases_total": 517,
    "base_verdicts": {"成立": 14, "部分成立": 430, "不成立": 71, "未核": 2},
    "carryover_check_r91_addendum": {
        "platform_layer": "_r91_carryover_notes_addendum",
        "platform_items": 103,
        "platform_result": "逐件与 r91 条（registered_round＝91 平台面条）manifest_carry_suggestion 全文逐字全等，落实 103／出入 0（层实在 runs/round92/judging/outcome-manifest.json）",
    },
    "new_registrations_r92": 12,
    "new_cases_r92": {"部分成立_platform": NEW_IDS},
    "r92_partial_upheld_platform": NEW_IDS,
    "r92_freeze_first": "AS-009（FREEZE-r92 tradition 裁定部分成立，措辞不实三度重现）",
    "r92_basis_groups": {
        "DT化神未载组": ["DT-002", "DT-003", "DT-004", "DT-005", "DT-006", "DT-007"],
        "MP无盘面组": ["MP-015", "MP-016"],
        "singles": ["BZ-038", "LY-202", "LY-234"],
    },
    "r92_candidate_scan": {
        "candidates": 174, "upheld_new_basis": 11, "not_upheld": 163,
        "breakdown": {"同旨已在册复触": 103, "纯推断性／读法注记": 37, "卡面设计形态与组通式": 21,
                      "tradition首行如实注记": 1, "待核同旨（LY-537）": 1},
        "note": "AS-009 计入复触 103 之 OCR 残损面；其 tradition 面另经 FREEZE-r92 入册，不在 basis 通道 11 件内。",
    },
    "r92_not_upheld_platform_registered_only": "tradition 旗标候选余 37 件（FREEZE-r92 裁定不成立：LY-221／LY-234／LY-429／LY-437／LY-503／LY-506／LY-626 共 7 件首行照录无误、触发词指向他字段；MP-019 与 OC-002–OC-030 共 30 件卡面确无 tradition/system、首行如实写明未标注）＋声明互斥组候选 0，只登记不入 annotations",
    "ziwei_supply_batch2": {
        "eligible_new": ["ZW-019", "ZW-020"], "grades": "A-low",
        "sources": "次批 #3 徐曾生：ZW-019＝XZS-08（第 25 章例解主例）、ZW-020＝XZS-12（第 28 章借钱被倒案，取自楚皇著作）；候选 25、不通过 16、挂起 7",
        "lzt_batch2_4": "陆在田《紫微斗数股票战略》LD-01–LD-03 全不通过、通过 0",
        "unused_eligible": 4, "unused_ids": ["ZW-017", "ZW-018", "ZW-019", "ZW-020"],
        "pool_eligible_total": 17, "h34_gap": 5,
    },
    "section8_monitoring_r92": {
        "source": "FREEZE-r92 §3（只监测、不判读）",
        "all": {"n": 487, "节名明引": 440, "节名明引率": "90.3%", "编号R80明引": 247, "机制全称明引": 234, "功量核标目段": 440, "主线认定行": 480, "主线认定行率": "98.6%"},
        "liuyao": {"n": 325, "节名明引": 285, "功量核标目段": 285, "主线认定行": 325},
        "liuren": {"n": 30, "节名明引": 30, "功量核标目段": 30, "主线认定行": 30},
        "other": {"n": 132, "节名明引": 125, "功量核标目段": 125, "主线认定行": 125},
    },
    "czqx_same_tier_count": 16,
    "as307_double_entry": "R80 部分成立条与 R85 不成立条并行保留、不合并；R92 basis 输入残损面与在册 R86 条同旨，无新旗标旨、不另立第三条",
    "pending_four": "BZ-029／BZ-040／LY-537／YM-070 维持原状；LY-537 本轮 basis 输入残损注记只登记触及、余三件本轮无新证据，均维持未核",
    "used_union": 1304,
    "cases_total": 529,
    "verdicts": {"成立": 14, "部分成立": 442, "不成立": 71, "未核": 2},
}

target = BASE / "data/case-annotations-r92.json"
target.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
# 回读断言
back = json.loads(target.read_text())
assert back["annotations"][:517] == R91["annotations"]
assert len(back["annotations"]) == 529
assert collections.Counter(a["disposition"] for a in back["annotations"]) == verdicts
print("落盘完成：", target, "annotations =", len(back["annotations"]), dict(verdicts))
print("CAT_A:", CAT_A)
print("NEW:", NEW_IDS)
