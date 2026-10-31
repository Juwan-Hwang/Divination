#!/usr/bin/env python3
"""R69 数据席落盘脚本（唯一落盘脚本）。
产出一：benchmark/phase3/data/manifest-carryover-r69-addendum.md（R68 部分成立 58 件汇编 + R69 manifest 对勘）
产出二：benchmark/phase3/data/case-annotations-r69.json（R69 旗标定案：八席自报 126 行/90 anon/90 例
        + 主持 tradition 复核 7 件，其中 5 例新立、2 例为附加层；合计 annotations 95 件）
纪律：落笔前逐件回读本例结局原文；引文逐字断言内置（断言失败不落盘）；
anon 形近串号逐件以 host-mapping 核定 case_id，不以计数代判。只标注，不改分、不改结局原文。
"""
import json, re, pathlib
from collections import Counter, defaultdict

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")

def load(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def pred(cid):
    return load(BASE / f"runs/round69/predictions/{cid}.json")

r68 = load(BASE / "data/case-annotations-r68.json")
m69 = load(BASE / "runs/round69/judging/outcome-manifest.json")
m68 = load(BASE / "runs/round68/judging/outcome-manifest.json")
hm = load(BASE / "runs/round69/judging/host-mapping.json")
flags_text = (BASE / "runs/round69/judging/FLAGS-selfreported-r69.md").read_text(encoding="utf-8")

# ---------- 全局断言（失败即不落盘） ----------
calc68 = Counter(a["disposition"] for a in r68["annotations"])
assert calc68 == Counter(r68["counts"]["verdicts"]) == Counter({"部分成立": 58, "成立": 12, "不成立": 4, "未核": 2})
assert set(m69["cases"]) == set(m68["cases"]) and len(m69["cases"]) == 487
assert all(m69["cases"][k] == m68["cases"][k] for k in m69["cases"]), "cases 与 R68 不全等"
partials68 = [a for a in r68["annotations"] if a["disposition"] == "部分成立"]
assert len(partials68) == 58 and all(a["manifest_carry_suggestion"] for a in partials68)
add69 = m69["_r69_carryover_notes_addendum"]
assert set(add69) == {a["case_id"] for a in partials68}
diffs = [a["case_id"] for a in partials68 if add69[a["case_id"]] != a["manifest_carry_suggestion"]]
assert not diffs, diffs  # 58/58 全等

# ---------- 旗标解析 ----------
rows = []
cur = None
for ln in flags_text.splitlines():
    m = re.match(r"===== (FLAGS-([XY]\d))", ln)
    if m:
        cur = m.group(2); continue
    if "主持复核" in ln and "=====" in ln:
        cur = "HOST"; continue
    for a in re.findall(r"P3-[0-9a-f]{8}", ln):
        rows.append((cur, a, ln.strip()))
assert len(rows) == 126 and Counter(s for s, _, _ in rows) == Counter(
    {"X1": 15, "X2": 14, "X3": 23, "X4": 10, "Y1": 12, "Y2": 9, "Y3": 13, "Y4": 30})
# anon 逐件对位：紧随括号 case 与 host-mapping 全等（形近串号逐件复核，不以计数代判）
for _, a, ln in rows:
    mm = re.match(r".*?" + re.escape(a) + r"\s*[（\(]([A-Z]+\d*-\d+)[）\)]", ln)
    assert not mm or mm.group(1) == hm[a], (a, ln)
assert hm["P3-ba74d717"] == "LY-030"  # 行内 LY-612 为同条全文参照、非标签

def clean_flag(seat, line, anon):
    s = line
    s = re.sub(r"^[-*#\d\.\s]+", "", s)
    s = s.replace(anon, "").strip()
    s = re.sub(r"^[（\(][A-Z]+\d*-\d+[）\)][：:、]?\s*", "", s)
    s = re.sub(r"^[｜:：]\s*", "", s)
    return f"{seat}：{s}" if s else f"{seat}：（原文行见汇编）"

by_case = defaultdict(list)   # case_id -> [(seat, anon, line)]
for seat, a, ln in rows:
    if seat == "HOST":
        continue
    by_case[hm[a]].append((seat, a, ln))
assert len(by_case) == 90

# ---------- 历轮定案索引 ----------
hist = defaultdict(list)  # case_id -> [(round, annotation)]
for rnd in range(49, 69):
    p = BASE / f"data/case-annotations-r{rnd}.json"
    if not p.exists():
        continue
    for a in load(p).get("annotations", []):
        hist[a["case_id"]].append((rnd, a))

def sources_for(cid, latest_rnd=None):
    src = [f"benchmark/phase3/inputs-dev12/{cid}.json",
           "benchmark/phase3/runs/round69/judging/FLAGS-selfreported-r69.md",
           f"benchmark/phase3/runs/round69/judging/outcome-manifest.json cases[{cid}]",
           f"benchmark/phase3/runs/round69/predictions/{cid}.json"]
    for rnd, _ in hist.get(cid, []):
        src.append(f"benchmark/phase3/data/case-annotations-r{rnd}.json {cid} 条")
    return src

# ---------- 引文逐字断言（新立/新旨/附加层） ----------
assert "having onely Quarter for his Souldiers' —" in m69["cases"]["AS-215"]
assert "the Lostwithiel surrender, 2 September 1644" in m69["cases"]["AS-215"]
assert "果於壬申日生女﹐產母平安。" in m69["cases"]["LY-246"]
assert "切不可以男女而斷" in m69["cases"]["LY-246"]
assert m69["cases"]["LY-329"] == "果俗底伙计有事而止．"
assert "冲?子水值日" in pred("LY-613")["prediction_text"]
assert "静伏?官现" in pred("LY-628")["prediction_text"]
assert "終身功名有續" in pred("LY-207")["prediction_text"]
assert "病向負斷" not in pred("LY-207")["prediction_text"] + pred("LY-207")["basis"]
assert "?" not in pred("LY-520")["prediction_text"] + pred("LY-520")["basis"]
assert "雪止放晴" in pred("LY-025")["prediction_text"]
assert "negative" not in pred("LY-025")["prediction_text"] + pred("LY-025")["basis"]
assert "欄位與爻位出入已在此註明" in pred("LY-322")["basis"]
assert "卡面无附盘，依据不足" in pred("AS-307")["basis"]
TRAD = ["LY-017", "LY-019", "LY-021", "LY-022", "LY-034", "LY-103", "LY-105"]
TRAD_ANON = {}
for cid in TRAD:
    card_raw = (BASE / f"inputs-dev12/{cid}.json").read_text(encoding="utf-8")
    assert "tradition" not in card_raw and '"system"' not in card_raw, cid
    assert pred(cid)["basis"].startswith("卡面 tradition＝liuyao，與卡面一致"), cid
    inv = [a for a, c in hm.items() if c == cid]
    assert len(inv) == 1, cid
    TRAD_ANON[cid] = inv[0]
# 指令性字样断言
assert "盲测比对须注" in m69["cases"]["BZ-036"] and "使用时须分开统计" in m69["cases"]["BZ-105"]
assert "（盲测比对时以格局大富一项为主）" in m69["cases"]["BZ-042"] and "勿以此斷" in m69["cases"]["LY-204"]
assert "评分时该细项请按未完全复核处理" in m69["_r56_lr2016_split"]["editor_note"]
assert "评分时" not in m69["cases"]["LR2-016"]

# ---------- 分类 ----------
NEW = {"AS-215", "LY-246", "LY-329", "LY-613", "LY-628"}
NEWGIST = {"LY-207"}
TRAD_ONLY = {"LY-017", "LY-019", "LY-021", "LY-022", "LY-034"}
TRAD_EXTRA = {"LY-103", "LY-105"}
TRAD_FLAG = ("主持复核（tradition）：卡面确无 tradition/system 字段而 basis 首行作「卡面 tradition＝liuyao，與卡面一致」，"
             "BZ-021/ZY-003 型措辞不实；主持裁定登记不重测，值本身与体裁一致、无 value 误标")

NEW_FINDINGS = {
 "AS-215": ("新旗标（R69 新立）：回原卡——所问 Essex 伯爵西征之成败荣名；R69 manifest 结局载其先盛后败、"
            "「the second of September this worthy man had surrendered all his Ammunition to his Majesty」投降败局明载，"
            "但所引原话以「having onely Quarter for his Souldiers' —」中途截断、其后径接编者注「the Lostwithiel surrender, 2 September 1644」"
            "——引文截断一层属实；主结局（投降以败收）完整可核。故部分成立（同逗号收尾截断口径：截断在引文层、主结局明载）。"),
 "LY-246": ("新旗标（R69 新立）：回原卡——所问占孕男女兼问妻孕平安；R69 manifest 结局「果於壬申日生女﹐產母平安。」"
            "生女与母平安两面明载；其后尾段「覺子曰﹕占妻平安及占男女﹐原宜分占……若在臨產危急時而問者﹐切不可以男女而斷。」"
            "为原书按语（占法戒语）混入结局尾部一层属实；但该按语系原书对占者之诫、非结局缺载、非对评分者之指令。故部分成立（同解释层混载口径）。"),
 "LY-329": ("新旗标（R69 新立）：回原卡——所问占开店得利否；R69 manifest 结局仅「果俗底伙计有事而止．」十字——"
            "店止一面有载，但「有事」为何事、停业原因细目与盈亏面均未明载，语义含混一层属实；结局亦非他事。故部分成立（同 YM-030 语义未明口径）。"),
 "LY-613": ("新旗标（R69 新立）：回本例 R69 prediction 全文逐字核——prediction_text 载「主坐标子日（伏神逢值/冲?子水值日）」"
            "确含半角问号「?」字样一处（basis 另有同式字样）；但主体断语（难产有险、须借冲飞之期方产、母险小于胎险）完整可读。"
            "故部分成立（同 LY-520／LY-628 字样口径）。"),
 "LY-628": ("新旗标（R69 新立）：回本例 R69 prediction 全文逐字核——prediction_text 载「官鬼寅木休囚静伏?官现二爻静而无力兴讼」"
            "确含半角问号「?」字样一处；但主体断语（讼事可解、对占者有利）完整可读。故部分成立（同 LY-520／LY-613 字样口径）。"),
}
NEW_CARRY_GIST = {
 "AS-215": "结局引文句中途截断（主结局投降败局明载）",
 "LY-246": "结局尾部混入原书按语戒语层（生女与母平安主面明载）",
 "LY-329": "结局仅「果俗底伙计有事而止」十字，停业原因与盈亏面未明载、语义含混",
 "LY-613": "prediction 爻位处含「?」占位字样一处、主体断语完整可读",
 "LY-628": "prediction 爻位处含「?」占位字样一处、主体断语完整可读",
}

# ---------- 逐件定案 ----------
annotations = []
for cid, seat_rows_ in sorted(by_case.items(), key=lambda kv: sorted(a for _, a, _ in kv[1])[0]):
    anon = sorted({a for _, a, _ in seat_rows_})[0]
    assert len({a for _, a, _ in seat_rows_}) == 1
    seats = sorted({s for s, _, _ in seat_rows_})
    flag_txt = "；".join(clean_flag(s, ln, a) for s, a, ln in sorted(seat_rows_))
    if cid in NEW:
        disp = "部分成立"
        finding = NEW_FINDINGS[cid]
        relation = "新旗标（R69 新立）"
        carry = (f"同旨新立：自 R70 起承接本 R69 标注：按「{NEW_CARRY_GIST[cid]}」登记；结局原文照录不改。")
    elif cid in NEWGIST:
        disp = "部分成立"
        finding = ("同例新旨（R64 旧旨『prediction 病向负断模板与功名问面错位』定案部分成立、R65 复述旧旨定案不成立，"
                   "两旨照旧登记、本轮新旨与之各旨独立）：回原卡——所问「占終身功名有無」；逐字核 R69 prediction 全文——"
                   "prediction_text 作「終局：終身功名有續、病退後仍可起用（單一終局：有）」通篇功名向，并无病向负断表述；"
                   "X1 旗标所指 carry_note 仍登记「prediction 为病向负断模板、与终身功名问面错位」，与本轮 prediction_text 口径不合属实"
                   "（同 LY-025 R63 注记过时口径）；R69 manifest 结局载援例加纳、官至府佐、未年出仕、戌年升任之功名历程，与问面直接对应、无结局数据缺口。"
                   "所指注记层不合一层属实，故部分成立。")
        relation = "同例新旨（R64／R65 旧旨并行、本轮新旨另立）"
        carry = ("同例新旨：自 R70 起承接本 R69 标注（与 R64／R65 旧旨定案并行、各旨独立）："
                 "按「carry_note 所称 prediction 病向负断模板与 R69 prediction_text 功名向口径不合」登记；结局原文照录不改。")
    else:
        lr, lp = hist[cid][-1]
        disp = lp["disposition"]
        finding = (f"承接既有定案不重裁（历轮最近定案 R{lr} {disp}）：{lp['finding']} "
                   f"本轮（R69）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。")
        relation = f"同旨续接（R{lr}）"
        if cid == "LY-520":
            finding += ("另注记层核明：逐字核 R69 prediction 全文（prediction_text 与 basis）并无「?」字样，Y4 旗标所据为 carry 旧注——"
                        "旧注与本轮 prediction 口径不合一层属实（同 LY-025 注记过时口径），与本旨并行登记、档位不变。")
        if cid == "LY-322":
            finding += "另 R69 prediction basis 已自注「欄位與爻位出入已在此註明」，与本旨同面、档位不变。"
        if cid == "LY-025":
            finding += ("另逐字核 R69 prediction_text 作「終局：雪止放晴」晴向终局、全无 negative 表述，"
                        "Y4 旗标所指 carry 旧注口径不合一层与 R63 新旨同旨、并行承接、档位不变。")
        if cid in TRAD_EXTRA:
            finding += ("另本轮主持 tradition 复核同及本例：卡面确无 tradition/system 字段而 basis 首行作「與卡面一致」，"
                        "措辞不实一层与本旨并行登记（tradition 值六爻与体裁一致、无 value 误标，主持裁定不重测）、档位不变。")
            flag_txt += "；" + TRAD_FLAG
            seats = seats + ["主持复核"]
        if disp == "部分成立":
            carry = f"同旨续接：自 R70 起承接 R{lr}＋本 R69 标注；结局原文照录不改。"
        else:
            carry = (f"不入附则：本 R69 同旨续接定案（{disp}），自 R70 起承接本 R69 标注，不加承接注记；结局原文照录不改。")
    annotations.append({
        "anon_id": anon, "case_id": cid, "disposition": disp, "finding": finding,
        "flag": flag_txt, "manifest_carry_suggestion": carry, "relation": relation,
        "registered_round": 69, "sources_checked": sources_for(cid), "source_seats": seats,
    })

# tradition 独立 5 件
TRAD_GIST = "卡面无 tradition/system 字段、basis 首行『與卡面一致』措辞不实，tradition 值六爻与体裁一致、无 value 误标"
for cid in sorted(TRAD_ONLY):
    annotations.append({
        "anon_id": TRAD_ANON[cid], "case_id": cid, "disposition": "部分成立",
        "finding": ("新旗标（R69 主持 tradition 复核新立）：主持复核并经本席回源逐件核——原卡（inputs-dev12/"
                    f"{cid}.json）全卡无 tradition/system 字段（结构化直读断言），而 R69 prediction basis 首行作"
                    "「卡面 tradition＝liuyao，與卡面一致」——『與卡面一致』之卡面归属措辞不实一层属实；但所用 tradition 值（六爻）"
                    "与卡面体裁实质一致、无 value 误标，断语与结局对应完整，主持裁定不重测（承 R67 BZ-021/ZY-003 型判例登记处置）。故部分成立。"),
        "flag": TRAD_FLAG,
        "manifest_carry_suggestion": f"同旨新立：自 R70 起承接本 R69 标注：按「{TRAD_GIST}」登记；结局原文照录不改。",
        "relation": "新旗标（R69 主持复核新立）", "registered_round": 69,
        "sources_checked": [f"benchmark/phase3/inputs-dev12/{cid}.json",
                            "benchmark/phase3/runs/round69/FREEZE-r69.md §二",
                            "benchmark/phase3/runs/round69/judging/FLAGS-selfreported-r69.md 主持复核旗标",
                            f"benchmark/phase3/runs/round69/judging/outcome-manifest.json cases[{cid}]",
                            f"benchmark/phase3/runs/round69/predictions/{cid}.json"],
        "source_seats": ["主持复核"],
    })
annotations.sort(key=lambda a: a["anon_id"])
assert len(annotations) == 95 and len({a["case_id"] for a in annotations}) == 95
verdicts = Counter(a["disposition"] for a in annotations)
n_cont = sum(1 for a in annotations if a["relation"].startswith("同旨续接"))
print("定案分布:", dict(verdicts), "总", len(annotations), "| 同旨续接", n_cont)

flags_arr = []
for a in annotations:
    seats = a["source_seats"]
    views = sorted({s[0] for s in seats if s[0] in "XY"})
    flags_arr.append({
        "anon_id": a["anon_id"], "case_id": a["case_id"], "verdict": a["disposition"],
        "disposition": a["disposition"], "basis": a["finding"],
        "carry_suggestion": a["manifest_carry_suggestion"],
        "manifest_carry_suggestion": a["manifest_carry_suggestion"],
        "flag": a["flag"],
        "category": a["relation"] if not a["relation"].startswith("同旨续接") else "同旨续接（详见核查事实）",
        "views": views, "dual_view": len(views) > 1,
        "relation": a["relation"], "registered_round": 69,
        "sources_checked": a["sources_checked"],
    })

special_checks = [
 {"item": "特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记",
  "conclusion": "四件本轮均未被任何旗标触及（八席自报 90 例与主持复核 7 例集合均不含四件），依任务口径不入 annotations、维持各自原登记：BZ-029 维持 R55 卒年待核（未核）；BZ-040 维持 R55 原登记（许世英享年异说待盘外独立史源）；LY-537 维持未核（『申予日』措辞待核、无盘外独立史源不裁）；YM-070 维持未核（『都下』语义未明＋『甲寅旬』出处待核并列、无盘外独立史源不裁）。",
  "evidence": "据 runs/round69/judging/host-mapping.json 与 FLAGS-selfreported-r69.md 逐件比对：95 件 case_id 集合不含 BZ-029／BZ-040／LY-537／YM-070（证据脚本断言通过）。",
  "scope_note": "本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。"},
 {"item": "特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）",
  "conclusion": "引文层错配 0 件：126 条旗标行经 host-mapping.json 逐件回到 case_id，anon 后紧随括号 case 逐行核对全等；X3 旗标 P3-ba74d717（host-mapping 指 LY-030）行内所提 LY-612 系同条全文参照（『相对同条全文（LY-612）缺落点』）、非本例标签，已逐件对位复核、不作错配论。同首缀（P3-＋4 hex）组无多 anon 组，逐件对位后无串号。主张层不合 2 件，均已并行登记、档位照各自主旨：(一) LY-520 Y4 旗标所据 carry 旧注称 prediction 含『?』字样两处，逐字核 R69 prediction 全文无『?』——旧注与本轮 prediction 口径不合一层已入本例定案附注；(二) LY-207 X1 旗标本身即登记 carry_note 与本轮 prediction 口径不合，经核属实、已按同例新旨定案。其余各件旗标引文经逐件回读本例 R69 结局原文／prediction 原文核对均在本例内（引文逐字断言内置于落盘脚本）。",
  "evidence": "落盘脚本与证据脚本双脚本断言：括号对位全等、LY-520『?』不存在断言、LY-207『終身功名有續』在文与『病向負斷』不在文断言、LY-025『雪止放晴』在文与 negative 不在文断言均通过。",
  "scope_note": "本核查只登记错配与不合事实，不改分数、不改 manifest、不改旗标原文。"},
 {"item": "特别核查③：结局文本内嵌指令性字样之例——按数据处理登记（本体基线对勘＋本轮旗标所涉与新发现归属）",
  "conclusion": "承既有登记口径全量复扫 R69 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计／勿以此斷等，并以『请／請／须／須／切不』宽扫人工甄别）：cases 本体内指令性字样仍为基线本体四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。本轮新发现本体例（对评分者之指令）0 件：宽扫另命中 BZ-302／LR2-022／LR3-004／LR3-006／LR3-010／LY-416 均为叙事用字（请同乡说情／请吕纯阳下降／请告归里／所请准），LY-227『須再占』为原书断法通则叙事，均不入指令性登记；LY-246『切不可以男女而斷』为本轮 Y3 旗标新指、逐件归属为原书按语对占者之诫（已在本件按新立定案登记），非对评分者之指令、不入基线四例。本轮旗标所涉归属逐处定案：（一）X1 旗标 P3-2ea362f6（LR2-016）所指 editor_note 字样——归属分列 editor_note，非 cases 本体，已按同旨续接定案；（二）X2/Y2 旗标 P3-406738a9（BZ-105）所涉尾注即基线本体例 BZ-105 本身（回溯断验注＋『使用时须分开统计』同条并存），非新增本体例，已按同旨续接定案；（三）Y4 旗标 P3-e36202d9（BZ-036）主旨为系狱年数出入、其结局含基线字样『盲测比对须注』，归属本体基线例本身，已按同旨续接定案。各席均按数据处理未服从：X1 旗标原文自载『本席按数据处理未采入评分』、Y3 旗标原文自载『属原书按语、非对本席指令，仅登记』、Y2 席块末自载通读后未作量表外加减分依据，本席亦只按数据处理、未服从任何一处之指示，事实照录。",
  "evidence": "证据脚本 data_r69_evidence.py 全量扫描输出：关键词命中集合恰为 {BZ-036, BZ-042, BZ-105, LY-204}，与基线本体四例全等；宽扫候选 10 例逐件回读甄别如上；LR2-016 editor_note 以 manifest _r56_lr2016_split 分列字段结构化直读核对（editor_note 含该句、cases[LR2-016] 不含『评分时』，落盘脚本断言通过）。",
  "scope_note": "本核查只登记字样出处与处理事实，不改分数、不改 manifest、不改结局原文。"},
 {"item": "特别核查④：同例新旨、主持复核附加层与新立件登记（LY-207／LY-103／LY-105／LY-520）",
  "conclusion": "同例新旨 1 件：LY-207（R64 旧旨部分成立、R65 复述旧旨不成立照旧登记；本轮新旨为 carry_note 与 R69 prediction_text 功名向口径不合，核后部分成立），与旧旨各旨独立、并行不悖。主持 tradition 复核 7 件：5 件独立新立（LY-017／LY-019／LY-021／LY-022／LY-034，均部分成立），2 件为附加层（LY-103／LY-105——两例本轮自报主旨均为同旨续接，tradition 措辞不实一层并行登记、档位不变）。注记口径层 1 件：LY-520（carry 旧注『?』字样与 R69 prediction 不合，并行登记、档位不变）。新立件共 10 件：自报新立 5 件（AS-215／LY-246／LY-329／LY-613／LY-628，均核后部分成立）＋主持复核新立 5 件。",
  "evidence": "逐件回 R69 prediction 全文、原卡与结局原文，断言见落盘脚本；历轮定案档 case-annotations-r64.json／-r65.json LY-207 条、FREEZE-r69.md §二主持裁定。",
  "scope_note": "本登记只记关系，不改任何一轮分数。"},
 {"item": "特别核查⑤：汇编一致性与结局文本一致性",
  "conclusion": "汇编 FLAGS-selfreported-r69.md 八席自报共 126 条旗标行、90 anon、90 例（单席 54 例、双席 36 例），与主持复核 7 件合并后定案 95 例；R69 各例结局文本经脚本断言与 R68 manifest 逐件全等（487/487），续接类定案的『结局与历轮所核文本一致』前提全数成立。本轮配对异常 0 件（见特别核查②）。",
  "evidence": "证据脚本 data_r69_evidence.py 与落盘脚本 data_r69_build.py 双脚本断言输出。",
  "scope_note": "本核查只登记一致性事实。"},
]

counts = {
 "selfreport_flag_rows_total": 126,
 "selfreport_anons_total": 90,
 "selfreport_cases_total": 90,
 "host_tradition_flags_total": 7,
 "host_tradition_only_cases": 5,
 "cases_total": len(annotations),
 "continuation_cases": n_cont,
 "same_case_new_gist_cases": 1,
 "new_flag_cases": 10,
 "verdicts": dict(verdicts),
}
provenance = (
 "R69 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）逐件回源核查 R69 八席自报旗标 "
 "126 条旗标行（runs/round69/judging/FLAGS-selfreported-r69.md 汇编）、去重为 90 anon／90 例（同例多席同旨合并 36 例），"
 "另主持 tradition 复核旗标 7 件（FREEZE-r69 §二）中 5 例为独立新立、2 例（LY-103／LY-105）为既有定案例之附加层，合计定案 95 例。"
 "逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round69/predictions/<case_id>.json 预测原文、"
 "runs/round69/judging/outcome-manifest.json cases 载荷（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），"
 "并与历轮定案档（data/case-annotations-r49.json 至 -r68.json）核对承接关系："
 f"{n_cont} 件为同旨续接（只承接不重裁），1 件为同例新旨（LY-207，另裁部分成立），10 件为 R69 新立"
 "（自报新立 5 件 AS-215／LY-246／LY-329／LY-613／LY-628 与主持复核新立 5 件 LY-017／LY-019／LY-021／LY-022／LY-034，均核后部分成立）。"
 "R69 各例结局文本经脚本断言与 R68 manifest 逐件全等（487/487）。本轮 anon 内容错配 0 件；注记层口径不合 2 件（LY-207／LY-520）已并行登记。"
 "指令性字样特别核查：cases 本体仍为基线四例（BZ-036／BZ-042／BZ-105／LY-204），LR2-016 之句只存分列 editor_note，本轮新发现本体例 0 件；"
 "本轮旗标所涉三处（LR2-016 editor_note、BZ-105 本体基线、BZ-036 本体基线）与新指一处（LY-246 原书按语）归属已逐处定案登记于特别核查③，各席均按数据处理未服从。"
 "待核维持四件（BZ-029／BZ-040／LY-537／YM-070）本轮均未被旗标触及，不入本件、维持原登记（见特别核查①）。"
 "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。"
)
out = {"_provenance": provenance, "round": 69, "flags": flags_arr, "annotations": annotations,
       "special_checks": special_checks, "counts": counts}
out_path = BASE / "data/case-annotations-r69.json"
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("WROTE", out_path)

# ---------- 产出一：承接附则（分段 append、逐段验尾） ----------
add_path = BASE / "data/manifest-carryover-r69-addendum.md"
non = {d: [a["case_id"] for a in r68["annotations"] if a["disposition"] == d] for d in ["成立", "不成立", "未核"]}
head = f"""# Manifest 承接册附则（R69）——R68 定案承接建议汇编

## 卷首说明

- 本附则为 Phase 3 Round 69（R69）数据席（任务一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r68.json`（R68 定案正本：annotations 76 件，定案分布成立 12／部分成立 58／不成立 4／未核 2）。
- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 12／部分成立 58／不成立 4／未核 2、总 76，与任务给定分布逐项一致；部分成立 58 件每件 `manifest_carry_suggestion` 非空断言亦通过。
- 对勘结果：58/58 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round69/judging/outcome-manifest.json` 的 `_r69_carryover_notes_addendum` 层（本席只读该层与 `cases` 键名集），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 0 件）。
- **本附则自 R70 manifest 起落实**；本轮（R69）manifest 不据本附则改动。
- **本件只汇编与对勘，不改任何分数与结局原文。**
- 汇编范围：R68 定案中部分成立 58 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r68.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R69 起」等表述为原档原文，落实轮次按卷首上一条读作自 R70 起，不回溯改动 R69）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。
- 成立 12／不成立 4／未核 2 共 18 件不入正文逐件节，只在文末列 case_id 清单。
- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。

---

## 一、部分成立件承接汇编（定案档位：部分成立，58 件，逐件全列）
"""
chunks = [head]
for i, a in enumerate(partials68, 1):
    chunks.append(f"""
### A{i}. {a['case_id']}

- case_id：{a['case_id']}
- anon_id：{a['anon_id']}
- 定案（部分成立）：{a['finding']}
- 原旗标要旨（照原档 `flag` 字段）：{a['flag']}
- 承接注记建议文本（照原档 `manifest_carry_suggestion` 原文）：「{a['manifest_carry_suggestion']}」
- 与既有承接册／附则条目的关系（照原档 `relation` 字段）：{a['relation']}
""")
detail = "、".join(f"{a['case_id']}＝一致" for a in partials68)
tail = f"""
---

## 对勘记录

- 对勘对象：本汇编第一节 58 件承接注记建议文本（源：`case-annotations-r68.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round69/judging/outcome-manifest.json` 的 `_r69_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。
- 对勘结果：58 件逐字一致，差异 0 件（对勘明细：{detail}）。
- 键集合差异：无（manifest 层 58 键与部分成立 58 件 case_id 集合全等）。
- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。勘误结论：无须勘误；本附则结论自 R70 manifest 起落实。

---

## 自验

- 原档（case-annotations-r68.json）条目数：76；档位分布成立 12／部分成立 58／不成立 4／未核 2，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。
- 本附则正文条目数：58（第一节部分成立 58 件），与原档部分成立件数对齐；文末不入附则清单 18 件（成立 12＋不成立 4＋未核 2），58＋18＝76 与原档总数对齐。
- 承接注记建议文本：58 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R69 manifest `_r69_carryover_notes_addendum` 逐件逐字一致（58／58）。
- 回读断言：本附则写出后由生成脚本回读，断言第一节条目数＝58、每件承接注记建议文本与原档字段逐字一致（结果见产出时回读记录：通过）。
- 纪律自报：本席只汇编与对勘，未改任何分数、未改 manifest、未改 annotations、未改原卡；outcome-manifest 只读 `_r69_carryover_notes_addendum` 层与 `cases` 键名集（另为续接前提核对 cases 与 R68 逐件全等 487/487，只读）。

---

## 文末清单：不入附则 18 件（成立 12＋不成立 4＋未核 2，仅列 case_id）

### 成立 12 件

{chr(10).join('- ' + c for c in non['成立'])}

### 不成立 4 件

{chr(10).join('- ' + c for c in non['不成立'])}

### 未核 2 件

{chr(10).join('- ' + c for c in non['未核'])}
"""
chunks.append(tail)
with open(add_path, "w", encoding="utf-8") as f:
    for i, ch in enumerate(chunks):
        f.write(ch)
        f.flush()
        back = add_path.read_text(encoding="utf-8")
        assert back.endswith(ch[-80:]), f"段 {i} 验尾失败"
print("WROTE", add_path, "segments", len(chunks))

# 回读断言
back = add_path.read_text(encoding="utf-8")
assert back.count("\n### A") == 58
for a in partials68:
    assert f"「{a['manifest_carry_suggestion']}」" in back, a["case_id"]
backj = load(BASE / "data/case-annotations-r69.json")
assert backj["round"] == 69 and len(backj["annotations"]) == 95
assert Counter(x["disposition"] for x in backj["annotations"]) == verdicts
assert all(x["manifest_carry_suggestion"] for x in backj["annotations"] if x["disposition"] == "部分成立")
print("回读断言全过：附则 58 条逐字一致；定案档 95 件、分布", dict(verdicts))
print("BUILD OK")
