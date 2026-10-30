#!/usr/bin/env python3
"""R61 数据席：自报旗标定案（任务二）。只做标注与承接建议，不改任何分数。
逐件回源：原卡 inputs-dev12/<case>.json、R61 predictions/<case>.json、
R61 outcome-manifest.json 的 cases 载荷（结构化直读）、历轮定案档与承接关系。
注记文本一律结构化直读，不用正则截断抽取。
"""
import json
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3")
FLAGS = BASE / "runs/round61/judging/FLAGS-selfreported-r61.md"
MAPPING = BASE / "runs/round61/judging/host-mapping.json"
MANIFEST61 = BASE / "runs/round61/judging/outcome-manifest.json"
MANIFEST60 = BASE / "runs/round60/judging/outcome-manifest.json"
OUT = BASE / "data/case-annotations-r61.json"
STD = {"成立", "部分成立", "不成立", "未核"}

# ---------- 读旗标汇编（按行解析，不用正则） ----------
mapping = json.loads(MAPPING.read_text(encoding="utf-8"))
seat = None
per_anon = {}  # anon -> list[(seat, text)]
order = []
for ln in FLAGS.read_text(encoding="utf-8").splitlines():
    if ln.startswith("## FLAGS-"):
        seat = ln[len("## FLAGS-"):].split(".")[0].strip()  # X1..Y4
    elif ln.startswith("- P3-") and seat:
        body = ln[2:]
        anon, _, text = body.partition("：")
        anon = anon.strip()
        if anon not in per_anon:
            per_anon[anon] = []
            order.append(anon)
        per_anon[anon].append((seat, text.strip()))
assert len(order) == 81, len(order)

cases61 = json.loads(MANIFEST61.read_text(encoding="utf-8"))["cases"]
cases60 = json.loads(MANIFEST60.read_text(encoding="utf-8"))["cases"]

# ---------- 历轮定案（结构化直读 r49-r60） ----------
prior = {}  # case_id -> list[(round, disposition_or_None, finding, relation, filename)]
for f in sorted((BASE / "data").glob("case-annotations-r*.json")):
    rnd = int(f.stem.rsplit("-r", 1)[1])
    if rnd >= 61:
        continue
    d = json.loads(f.read_text(encoding="utf-8"))
    seen = set()
    for e in d.get("annotations", []) or []:
        cid = e.get("case_id")
        if cid in seen:
            continue
        seen.add(cid)
        prior.setdefault(cid, []).append(
            (rnd, e.get("disposition"), e.get("finding") or "", e.get("relation") or "", f.name))

def latest_std(cid):
    cands = [p for p in prior.get(cid, []) if p[1] in STD]
    return cands[-1] if cands else None

# ---------- R61 新立件（逐件回原卡/预测/结局三方核对后手裁） ----------
NEW = {
 "AS-209": ("部分成立", "结局疑误记（已自注）",
   "新旗标（R61 新立）：回原卡——双问国王借爱尔兰兵与王后北军南下会合；R61 manifest 结局载王后会合日期作「14. of July 1443 [sic — misprint for 1643]」——年份误印属实，但结局文本内已自注为 1643 之误印，非未注明误记。故部分成立（同 AS-008／BZ-036 自注类口径）。",
   "同旨新立：自 R62 起承接本 R61 标注：按「结局年份『1443』系 1643 误印、结局内已自注」登记；结局原文照录不改。"),
 "BZ-019": ("部分成立", "prediction 称谓出入（传主身分）",
   "新旗标（R61 新立）：回原卡——setting 明载与 ren-016 同一命造（乾隆帝）、盲测不得给身分；R61 prediction 断语作「位极人臣，贵寿双全」——『人臣』称谓与传主帝王身分出入一层属实；但 prediction 贵寿主线（权位极盛、寿过八旬）与结局史实（在位 60 年、享寿 87 岁）对位，且身分系卡面按盲测设计 withheld，非输入/结局数据缺损。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「prediction『位极人臣』称谓与传主帝王身分出入、贵寿主线对位、身分系盲测 withheld」登记；结局原文照录不改。"),
 "BZ-104": ("部分成立", "结局成色（口头反馈、已自述）",
   "新旗标（R61 新立）：回原卡——邵伟华四柱断子未来病伤；R61 manifest 结局载 1990 年肝炎住院与骑摩托撞伤，并自注「（书内自述，求测方口头反馈，无第三方记录）」——口头反馈、无第三方记录属实，但来源性质已在结局内自述，非未注明问题。故部分成立（同 LY-105 二手来源例口径）。",
   "同旨新立：自 R62 起承接本 R61 标注：按「结局系求测方口头反馈、无第三方记录（结局内已自述）」登记；结局原文照录不改。"),
 "LY-004": ("部分成立", "结局双段（近愈远绝、分段载）",
   "新旗标（R61 新立）：回原卡——四度占父病；R61 manifest 结局为双段文本「目下果愈（壽姓醫者治之）；果絕於亥月（冬季）」——近段愈、远段亥月绝两段并载属实，成色为分段混合；但两段系时序分段（先愈后绝）而非同点自相矛盾，终局段（亥月绝）明载。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「结局双段分载：目下果愈、果绝于亥月，须分段读」登记；结局原文照录不改。"),
 "LY-025": ("部分成立", "prediction 终局单判与问目错位（模板化）",
   "新旗标（R61 新立）：回原卡——所问「何日晴」为时点问；R61 prediction 正文作「倾向不成/不得/凶……终局单判：negative」——以成败单判套时点问，问目错位、模板化一层属实；但 prediction 另载应期结构（巳日候选），且结局「果於次日卯時，雲開日出」时点明载、无数据缺口。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「prediction 终局单判 negative 与『何日晴』时点问错位（prediction 文本面）、结局时点明载」登记；结局原文照录不改。"),
 "LY-103": ("部分成立", "结局成色（书内自述）＋应期尺度出入",
   "新旗标（R61 新立）：回原卡——所问当晚雨停否，数小时内可验；R61 manifest 结局「当晚雨停，音乐会得以举办（书内自述，无气象记录佐证）」——无气象佐证属实且结局内已自注；另 R61 prediction 应期作一旬窗口、午日主坐标，与当晚问事尺度出入一层属实（prediction 面）。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「结局为书内自述、无气象记录佐证（已自注）；prediction 应期尺度与当晚问事出入」登记；结局原文照录不改。"),
 "LY-211": ("成立", "prediction 内部矛盾（倾向与终局单判）",
   "新旗标（R61 新立）：逐字核 R61 prediction——正文作「成败参半偏不成（克害居多）」，终局单判却作「positive」，两处同文自相矛盾，自报属实。属 prediction 文本面，不涉结局原文（结局「果卒於卯年」明载）。故成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「prediction 正文倾向『偏不成』与终局单判 positive 自相矛盾（prediction 文本面）」登记；结局原文照录不改。"),
 "LY-216": ("部分成立", "prediction 终局单判与问目对应含混",
   "新旗标（R61 新立）：回原卡——所问「占僕人為禍否」；R61 prediction 作「倾向成/得/吉……终局单判：positive」——positive 究指『为祸成真』抑或『事成/吉』，与问目对应含混一层属实；但 prediction 正文用神论述完整、结局亦载二人原欲害主而逃、不能相害之结果，非整例无据。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「prediction 终局单判 positive 与『仆人为祸否』问目对应含混」登记；结局原文照录不改。"),
 "LY-228": ("成立", "prediction 内部矛盾（倾向与终局单判）",
   "新旗标（R61 新立）：逐字核 R61 prediction——正文作「成败参半偏成（待填实出空方应）」，终局单判却作「negative」，两处同文自相矛盾，自报属实（X4/Y4 双席同报）。属 prediction 文本面，不涉结局原文。故成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「prediction 正文倾向『偏成』与终局单判 negative 自相矛盾（prediction 文本面）」登记；结局原文照录不改。"),
 "LY-231": ("成立", "prediction 内部矛盾（倾向与终局单判）",
   "新旗标（R61 新立）：逐字核 R61 prediction——正文作「成败参半偏成（待填实出空方应）」，终局单判却作「negative」，两处同文自相矛盾，自报属实。属 prediction 文本面，不涉结局原文（结局「果於八月丁艱」明载）。故成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「prediction 正文倾向『偏成』与终局单判 negative 自相矛盾（prediction 文本面）」登记；结局原文照录不改。"),
 "LY-237": ("成立", "prediction 内部矛盾（倾向与终局单判）",
   "新旗标（R61 新立）：逐字核 R61 prediction——正文作「成败参半偏成（待填实出空方应）」，终局单判却作「negative」，两处同文自相矛盾，自报属实（X4/Y4 双席同报）。属 prediction 文本面，不涉结局原文。故成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「prediction 正文倾向『偏成』与终局单判 negative 自相矛盾（prediction 文本面）」登记；结局原文照录不改。"),
 "LY-416": ("部分成立", "结局疑似截断（逗号收尾）",
   "新旗标（R61 新立）：回原卡——所问迎请父王灵柩允否；R61 manifest 结局「後應申月所請準，酉歲迎靈而歸，」以逗号收尾——疑似截断之表面属实；但所请准与酉岁迎灵而归两项主结局均已明载，盘内无据裁定尚有缺失后文。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「结局以逗号收尾、疑似截断，主结局（申月准、酉岁迎灵而归）明载」登记；结局原文照录不改、不补字。"),
 "LY-516": ("部分成立", "结局混入断法通则（个案结局仅四字）",
   "新旗标（R61 新立）：回原卡——所问升迁得何地（山东/真定两缺）；R61 manifest 结局个案结果仅「果得眞定」四字，后半为『以初爻为内地、以五六爻为边缺』等断法通则陈述——通则混入属实，个案结局成色受限；但得真定之终局本身明载。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「个案结局仅『果得真定』、后半混入断法通则」登记；结局原文照录不改。"),
 "MP-014": ("不成立", "旗标与本例 prediction 文本不合",
   "新旗标核查后不成立（历轮定案档无本 case_id 条目）：逐字核 R61 prediction——全文为专断文本『特朗普病情可愈而选情不利、连任失败（negative，就选情论）』，并无『成败参半偏成』一语，终局单判与正文一致；自报 X2 所指内部矛盾在本例文本中不存在。结局（败于拜登、10 月 5 日出院康复）与问面直接对位。故不成立。",
   "不入附则：prediction 正文与终局单判一致、结局与问面直接对位，不加承接注记；结局原文照录不改。"),
 "OC-009": ("部分成立", "prediction 残损降格（四柱未给出、已自陈）",
   "新旗标（R61 新立）：回原卡——卡面仅注『原书应运篇下论造，四柱以原书为准，转录本个别字待校』，四柱未实际给出；R61 prediction 自陈『无盘可排……不断具体运程』、置信低（0.20），属残损降格断——所指属实，但残损状态已在卡面与 prediction 双处明示。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「四柱未实际给出、prediction 为残损降格断（卡面与 prediction 已双示）」登记；结局原文照录不改。"),
 "YM-038": ("不成立", "旗标与本例 prediction／结局文本不合",
   "新旗标核查后不成立（历轮定案档无本 case_id 条目）：逐字核 R61 prediction——全文为专断文本『子病可愈，不至死……终局按可愈单判』，无『成败参半偏成』、无 negative 单判；R61 manifest 结局仅「后其疾不死，未半年溺水而亡。」两句，无通用断例规则文本。自报 X2 两层所指在本例文本中均不存在。故不成立。",
   "不入附则：旗标所指文本在本例 prediction 与结局中均不存在，不加承接注记；结局原文照录不改。"),
 "YY-023": ("部分成立", "断语式结局（总承式）",
   "新旗标（R61 新立）：回原卡——所问占讼能否说情脱罪；R61 manifest 结局仅「后果然。」二字总承——断面未分载属实；但总承所指即本问讼事本身（同 YY-022 体例）。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「结局为总承式『后果然』、断面未分载」登记；结局原文照录不改。"),
 "YY2-002": ("部分成立", "结局含断理解释层（终局明载）",
   "新旗标（R61 新立）：回原卡——所问妻寿；R61 manifest 结局首句明载终局『直至丙子年丙申月庚辰日故』，后半『财虽不值岁旬空亡……所以终命也』为本例断理解释层——解释层并载属实，但系本例个案释义、非通则混入，且终局本身明载。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「结局终局明载、后半为本例断理解释层」登记；结局原文照录不改。"),
 "YY2-004": ("部分成立", "prediction 残损降格（盘面残损、已自陈）",
   "新旗标（R61 新立）：回原卡——卡面自注本卦名原书缺字、六爻与动爻不录；R61 prediction 自述『本例盘面残损，本卦名原书缺字、六爻盘面与动爻均不可补……无据定断』——残损降格属实，但残损状态已在卡面与 prediction 双处明示。故部分成立。",
   "同旨新立：自 R62 起承接本 R61 标注：按「盘面残损、prediction 为无据不报之降格断（卡面与 prediction 已双示）」登记；结局原文照录不改。"),
}

# 承接件中需附加注记的特例
EXTRA_BASIS = {
 "LY-205": "另本轮 X2 新报一层经逐字核 R61 prediction 属实：正文作『成败参半偏成』、终局单判作 negative，同文自相矛盾（prediction 文本面），与既有禄/财断面定案并行登记、不改既有 disposition。",
 "LY-629": "另本轮 Y4 所报『改向之后大发与 prediction 平顺小吉量级出入』一层，属 prediction 与结局的评分面落差，不构成数据缺口，随本条并行登记。",
 "LY-537": "与『待核维持』登记并行不悖：本轮照实核、照实给 disposition 为未核，与待核维持口径一致、无差异；差异仅在出处——本件系 R61 自报旗标定案产出，待核维持系另行登记，两者并行。",
 "YM-070": "与『待核维持』登记并行不悖：本轮旗标仅及结局『都下』语义一层，照实核、照实给 disposition 为未核（挂起），与既有『甲寅旬』出处待核项并存合并登记；本件定案口径与待核维持一致、无差异，两者并行。",
}
EXTRA_CARRY = {
 "LY-537": "挂起维持：自 R62 起承接 R56＋R57＋本 R61 登记：按「结局『果于申予日归』字样疑衍字、无原书页文本可裁」登记；结局原文照录不改、不补字；无盘外独立史源前不另裁。",
 "YM-070": "挂起维持（注记合并）：自 R62 起承接 R51＋R55＋R56＋R57＋R58＋R59＋R60＋本 R61 登记：按「结局措辞待核（『都下』语义未明）」与卡面 asked_at「甲寅旬」出处待核两项合并登记、并列承接；结局原文照录不改、不补字；无盘外独立史源前不另裁。",
}

annotations = []
flags_full = []
continuation = 0
new_cases = 0
for anon in order:
    cid = mapping[anon]
    inp = json.loads((BASE / f"inputs-dev12/{cid}.json").read_text(encoding="utf-8"))
    pred = json.loads((BASE / f"runs/round61/predictions/{cid}.json").read_text(encoding="utf-8"))
    assert cid in cases61 and cases61[cid], cid
    assert cid in cases60 and cases60[cid] == cases61[cid], f"outcome differs from R60: {cid}"
    flag_text = "；".join(f"{s}：{t}" for s, t in per_anon[anon])
    seats = sorted({s for s, _ in per_anon[anon]})
    sources = [f"benchmark/phase3/inputs-dev12/{cid}.json",
               "benchmark/phase3/runs/round61/judging/FLAGS-selfreported-r61.md",
               f"benchmark/phase3/runs/round61/judging/outcome-manifest.json cases[{cid}]",
               f"benchmark/phase3/runs/round61/predictions/{cid}.json"]
    lat = latest_std(cid)
    if cid in NEW:
        disp, cat, finding, carry = NEW[cid]
        relation = "新旗标（R61 新立）" + ("，核后不成立" if disp == "不成立" else "")
        new_cases += 1
    elif cid == "LY-629":
        disp, cat = "部分成立", "对话体总承式结局（改向后总承）"
        r54 = [p for p in prior[cid] if p[0] == 54][0]
        finding = ("承接既有定案不重裁（R54 部分成立）：回原卡——所问「占墳地風水」，R61 manifest 结局"
                   "「彼曰：一一果然，葬可好否？予曰：依予取水作朝，棄山作向，許必大發，彼果依斷，葬後即如所言．」"
                   "——前断以『一一果然』总承、后段转入改向建议与『葬后即如所言』总承，原问坟地吉凶未以独立实绩分载，"
                   "旗标部分成立；本轮（R61）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。")
        carry = "同旨续接：自 R62 起承接 R54＋本 R61 标注：按「结局为总承式且系改向之后应验、原问坟地吉凶未独立分载」登记；结局原文照录不改。"
        relation = "同旨续接（R54）"
        sources += [f"benchmark/phase3/data/case-annotations-r54.json {cid} 条"]
        continuation += 1
    elif cid == "LY-425":
        disp, cat = "部分成立", "问面名目与结局名目有别（得缺／中榜）"
        r53 = [p for p in prior[cid] if p[0] == 53][0]
        finding = ("承接既有定案不重裁（R53 弱口径）：回原卡——所问「占候選何時得缺」，"
                   "R61 manifest 结局仅「果然在第二年寅月沒有中榜，」——结局对应大师功名总断，"
                   "但事件名目为中榜而非得缺、断面不完全对应一层属实；本轮 X1 自报与 R53 定案同旨。"
                   "本轮（R61）manifest 该例结局与历轮所核文本一致。")
        carry = "同旨续接：自 R62 起承接 R53＋本 R61 标注：按「问面名目（得缺）与结局名目（中榜）有别、结局对应功名总断」登记；结局原文照录不改。"
        relation = "同旨续接（R53）"
        sources += [f"benchmark/phase3/data/case-annotations-r53.json {cid} 条"]
        continuation += 1
    else:
        assert lat is not None, cid
        rnd, disp, pfind, prel, pfname = lat
        rounds = sorted({p[0] for p in prior[cid] if p[1] in STD})
        rtxt = "／".join(f"R{r}" for r in rounds)
        finding = (f"承接既有定案不重裁（历轮最近定案 R{rnd} {disp}）：{pfind} "
                   f"本轮（R61）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。")
        if disp in ("成立", "部分成立"):
            carry = f"同旨续接：自 R62 起承接 {rtxt}＋本 R61 标注；结局原文照录不改。"
        elif disp == "不成立":
            carry = "不入附则：承既有定案口径，不加承接注记；结局原文照录不改。"
        else:  # 未核
            carry = "挂起维持：承既有未核定案；结局原文照录不改、无盘外独立史源前不另裁。"
        relation = f"同旨续接（{rtxt}）"
        cat = "同旨续接（详见核查事实）"
        for p in prior[cid]:
            if p[1] in STD:
                sources.append(f"benchmark/phase3/data/{p[4]} {cid} 条")
        continuation += 1
    if cid in EXTRA_BASIS:
        finding = finding + EXTRA_BASIS[cid]
    if cid in EXTRA_CARRY:
        carry = EXTRA_CARRY[cid]
    entry = {"anon_id": anon, "case_id": cid, "disposition": disp, "finding": finding,
             "flag": flag_text, "manifest_carry_suggestion": carry, "relation": relation,
             "registered_round": 61, "sources_checked": sources, "source_seats": seats}
    annotations.append(entry)
    flags_full.append({"anon_id": anon, "case_id": cid, "verdict": disp, "disposition": disp,
                       "basis": finding, "carry_suggestion": carry,
                       "manifest_carry_suggestion": carry, "flag": flag_text, "category": cat,
                       "views": sorted({s[0] for s in seats}), "dual_view": len(seats) > 1,
                       "relation": relation, "registered_round": 61, "sources_checked": sources})

verdicts = {k: sum(1 for a in annotations if a["disposition"] == k) for k in ("成立", "部分成立", "不成立", "未核")}
counts = {"selfreport_anons_total": len(order), "cases_total": len({a['case_id'] for a in annotations}),
          "continuation_cases": continuation, "new_flag_cases": new_cases, "verdicts": verdicts}
# 脚本断言：counts 与 annotations 逐件复算全等
assert counts["selfreport_anons_total"] == len(annotations) == 81
assert counts["cases_total"] == 81
assert continuation + new_cases == 81, (continuation, new_cases)
assert sum(verdicts.values()) == 81
assert "BZ-029" not in {a["case_id"] for a in annotations}
assert "BZ-040" not in {a["case_id"] for a in annotations}

doc = {
 "_provenance": ("R61 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）"
   "逐件回源核查 R61 八席自报旗标 81 anon（runs/round61/judging/FLAGS-selfreported-r61.md，去重后；"
   "同一 anon 多席重复报者合并为一件、注明来源席位）。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、"
   "runs/round61/predictions/<case_id>.json 预测原文、runs/round61/judging/outcome-manifest.json cases 载荷，"
   "并与历轮定案档（data/case-annotations-r49.json 至 -r60.json）核对承接关系：62 件为同旨续接（只承接不重裁），"
   "19 件为 R61 新立。R61 各例结局文本经脚本断言与 R60 manifest 逐件全等。"
   "待核维持项：BZ-029／BZ-040 本轮未出现在旗标中，不在本件范围；LY-537 与 YM-070 出现在本轮旗标中，"
   "已照实核、照实给 disposition（均为未核），与『待核维持』登记并行不悖、口径一致无差异，差异仅在出处（本件为定案产出），已在各该条注明。"
   "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。"),
 "round": 61,
 "flags": flags_full,
 "annotations": annotations,
 "special_checks": [
   {"item": "特别核查①：P3-ec8e108e（LY-537）与 P3-f44f8a28（YM-070）出现在本轮旗标——与『待核维持』登记的关系",
    "conclusion": "两件均照实核、照实给 disposition 为未核（挂起），与待核维持口径一致、无差异；本定案产出与待核维持登记并行不悖。BZ-029／BZ-040 本轮未出现在旗标中，不在本件范围、维持原登记。",
    "evidence": "LY-537：R61 manifest 结局「果于申予日归」，『申予日』疑衍字，盘内无《卜筮正宗》原书页文本可裁（承 R56／R57 未核）。YM-070：R61 manifest 结局「后果同行都下。」中『都下』语义未明（R51–R60 历轮登记），另卡面 asked_at『甲寅旬』出处待核为并存挂起项，两项合并登记。",
    "scope_note": "本核查只登记关系，不改分数、不改 manifest；待核口径照旧。"},
   {"item": "特别核查②：P3-5a0975c5（MP-014）与 P3-790233fc（YM-038）自报『内部矛盾』文本核查",
    "conclusion": "两件旗标均不成立：所指『成败参半偏成』与终局单判矛盾在本例 R61 prediction 全文中不存在（均为专断文本、正文与单判一致）；YM-038 结局亦无通用断例规则文本。",
    "evidence": "MP-014 prediction 全文作『病情可愈而选情不利、连任失败（negative，就选情论）』，无『参半偏成』一语。YM-038 prediction 全文作『子病可愈，不至死……终局按可愈单判』，无 negative 单判；结局仅「后其疾不死，未半年溺水而亡。」。",
    "scope_note": "本核查只裁旗标与本例文本的对应关系，不改分数、不改 manifest。"},
 ],
 "counts": counts,
}
OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

# 复算断言（重读产出件逐件复算）
chk = json.loads(OUT.read_text(encoding="utf-8"))
re_v = {k: sum(1 for a in chk["annotations"] if a["disposition"] == k) for k in ("成立", "部分成立", "不成立", "未核")}
assert chk["counts"]["verdicts"] == re_v
assert chk["counts"]["selfreport_anons_total"] == len(chk["annotations"])
assert chk["counts"]["cases_total"] == len({a["case_id"] for a in chk["annotations"]})
assert chk["counts"]["continuation_cases"] + chk["counts"]["new_flag_cases"] == len(chk["annotations"])
print(json.dumps(counts, ensure_ascii=False))
print("bytes:", OUT.stat().st_size)
