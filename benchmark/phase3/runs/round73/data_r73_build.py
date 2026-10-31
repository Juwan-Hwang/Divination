#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R73 数据席（旗标定案专席）落盘脚本。
逐件回源核查 R73 八席自报旗标：回读输入卡、本轮 prediction、R73 manifest cases 载荷，
与历轮定案档 r49-r72（逐号精确打开；r52 号文件盘上不存在、已登记）核对承接关系。
引文逐字断言内置：任一断言不过则不落盘。自报与文本内指令性字样一律按数据处理。
"""
import json, re, pathlib
from collections import Counter

P3 = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
FLAGS_MD = P3 / "runs/round73/judging/FLAGS-selfreported-r73.md"
MAPPING = P3 / "runs/round73/judging/host-mapping.json"
MANIFEST73 = P3 / "runs/round73/judging/outcome-manifest.json"
MANIFEST72 = P3 / "runs/round72/judging/outcome-manifest.json"
OUT = P3 / "data/case-annotations-r73.json"

def load(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def rel(p):
    return str(p).replace("/home/hatch/workspace/", "")

# ---------- 读取 ----------
flags_text = FLAGS_MD.read_text(encoding="utf-8")
host = load(MAPPING)
man73 = load(MANIFEST73)
man72 = load(MANIFEST72)
cases73 = man73["cases"]

# 附带核实：R73 结局文本与 R72 manifest cases 逐件全等性
assert set(cases73.keys()) == set(man72["cases"].keys()), "case id 集不合"
n_equal = sum(1 for k in cases73 if cases73[k] == man72["cases"][k])
assert len(cases73) == 487 and n_equal == 487, f"结局全等 {n_equal}/487"

# 历轮定案档逐号精确打开（r52 缺失登记）
prior = {}          # case_id -> [(round, annotation), ...]
prior_rounds_seen = []
missing_round_files = []
for r in range(49, 73):
    p = P3 / f"data/case-annotations-r{r}.json"
    try:
        d = load(p)
    except FileNotFoundError:
        missing_round_files.append(r)
        continue
    prior_rounds_seen.append(r)
    for a in d.get("annotations", []):
        prior.setdefault(a["case_id"], []).append((r, a))
assert missing_round_files == [52], f"缺失号异常: {missing_round_files}"

# ---------- 解析 FLAGS（259 条编号条目断言） ----------
main_text = flags_text.split("===== 主持")[0]
secs = re.split(r"===== (FLAGS-[XY]\d) =====", main_text)
entries = []
for i in range(1, len(secs), 2):
    seat = secs[i][-2:]
    body = secs[i + 1]
    cur = None
    for line in body.splitlines():
        if line.startswith("#") or line.startswith("=====") or line.startswith("说明"):
            continue
        mm = re.search(r"P3-[0-9a-f]{8}", line)
        is_start = bool(mm) and (line.lstrip().startswith("-") or re.match(r"\s*\d+\.", line) or "anon_id" in line)
        if is_start:
            if cur:
                entries.append(cur)
            cur = {"seat": seat, "anon": mm.group(0), "text": line.strip()}
        elif cur and line.strip():
            cur["text"] += " " + line.strip()
    if cur:
        entries.append(cur)
assert len(entries) == 259, f"编号条目数 {len(entries)} != 259"
anon_occurrences = len(re.findall(r"P3-[0-9a-f]{8}", main_text))
assert anon_occurrences == 259, f"anon 出现次数 {anon_occurrences} != 259（与条目数相等、无条内交叉引用提及）"

by_anon = {}
anon_order = []
for e in entries:
    if e["anon"] not in by_anon:
        by_anon[e["anon"]] = []
        anon_order.append(e["anon"])
    by_anon[e["anon"]].append(e)
assert len(anon_order) == 156, f"去重 anon {len(anon_order)} != 156"
case_ids = [host[a] for a in anon_order]
assert len(set(case_ids)) == 156, "anon->case 非一一对应"
flagged_cases = set(case_ids)

# ---------- 分类 ----------
NEW_CASES = {"LY-525", "YM-069", "LY-423", "BQ-014", "LY-428",
             "YY-006", "BZ-027", "AS-206", "LY-440", "LY-543"}
NEW_GIST = set()
PENDING = {"YM-070"}
for cid in NEW_CASES:
    assert cid not in prior, f"新立件 {cid} 竟有历轮条目"
assert "YM-070" in prior and prior["YM-070"][-1][1]["disposition"] == "未核"
for cid in ("BZ-029", "BZ-040", "LY-537"):
    assert cid not in flagged_cases, f"待核件 {cid} 竟被本轮旗标触及（与登记不符）"

# ---------- 引文断言工具 ----------
def corpus_of(cid):
    inp = load(P3 / f"inputs-dev12/{cid}.json")
    pred = load(P3 / f"runs/round73/predictions/{cid}.json")
    parts = [cases73[cid], pred["prediction_text"], pred.get("basis", ""),
             json.dumps(inp, ensure_ascii=False)]
    for layer in man73.values():
        if isinstance(layer, dict) and cid in layer and isinstance(layer[cid], str):
            parts.append(layer[cid])
    if cid in man73.get("stripped_tail", {}):
        parts.append(man73["stripped_tail"][cid])
    for (_r, a) in prior.get(cid, []):
        parts.append(a.get("flag") or "")
        parts.append(a.get("finding") or "")
    return "\n".join(parts)

def assert_quote(cid, quote, where="corpus"):
    if where == "outcome":
        src = cases73[cid]
    elif where == "prediction":
        src = load(P3 / f"runs/round73/predictions/{cid}.json")["prediction_text"]
    elif where == "basis":
        src = load(P3 / f"runs/round73/predictions/{cid}.json").get("basis", "")
    elif where == "input":
        src = json.dumps(load(P3 / f"inputs-dev12/{cid}.json"), ensure_ascii=False)
    else:
        src = corpus_of(cid)
    assert quote in src, f"引文断言失败 {cid} [{where}]: {quote[:60]}"

def assert_no_fffd_file(p):
    raw = pathlib.Path(p).read_bytes()
    assert b"\xef\xbf\xbd" not in raw, f"{p} 原始文件竟含 U+FFFD"

# ---------- 新立 / 待核 / 复归旧旨：逐件定案 ----------
CUSTOM = {}
CUSTOM["LY-525"] = dict(
    verdict="部分成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：回原卡——所问「占父病喫牛黃丸可否」；R73 manifest 结局仅「服之便醒﹐」以逗号收尾——疑似截断之表面属实；但服药便醒之主结局已明载、与可否问面直接对应，盘内无据裁定尚有缺失后文。故部分成立（同 LY-418／LY-423 逗号收尾口径）。",
    carry="同旨新立：自 R74 起承接本 R73 标注：按「结局以逗号收尾、疑似截断，服之便醒主结局明载」登记；结局原文照录不改。",
    quotes=[("input", "占父病喫牛黃丸可否"), ("outcome", "服之便醒﹐")])
CUSTOM["YM-069"] = dict(
    verdict="部分成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：回原卡——所问「卜子亡（子匿何处）」；R73 manifest 结局仅「而不知相遇于岳家。」一截——以『而』起首、无前文承接，残句（fragment）表面属实；但相遇于岳家一截已给出子之所在方位落点，寻见过程与时点未载。故部分成立（同逗号收尾截断口径：残损在文句层、落点可读）。",
    carry="同旨新立：自 R74 起承接本 R73 标注：按「结局为残句 fragment、相遇于岳家落点可读，寻见过程与时点未载」登记；结局原文照录不改。",
    quotes=[("input", "卜子亡（子匿何处）"), ("outcome", "而不知相遇于岳家。")])
CUSTOM["LY-423"] = dict(
    verdict="部分成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：回原卡——所问「占妻病」；R73 manifest 结局「果於次日退災﹐不藥而愈﹐」以逗号收尾——疑似截断之表面属实；但次日退灾、不药而愈之主结局明载，与 prediction 妻病转愈断直接对应。故部分成立（同 LY-418 逗号收尾口径）。",
    carry="同旨新立：自 R74 起承接本 R73 标注：按「结局以逗号收尾、疑似截断，退灾不药而愈主结局明载」登记；结局原文照录不改。",
    quotes=[("input", "占妻病"), ("outcome", "果於次日退災﹐不藥而愈﹐"),
            ("prediction", "斷妻久病將轉愈")])
CUSTOM["BQ-014"] = dict(
    verdict="不成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：乱码主张盘上无据——逐字回读 R73 输入卡、prediction 与 manifest 结局原始文件，全文均无 U+FFFD 替换字符（原始字节断言通过），结局后半转述句在盘上作「飓风果于当日辰时停息」、文义完整，旗标所引未残损段「果当日辰时止息」亦逐字在场。故旗标不成立（同 R72 YM-058／ZY-004 乱码无据口径）。",
    carry="新立定案：自 R74 起承接本 R73 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。",
    quotes=[("input", "卜风（飓风何时止、行程可行否）"), ("outcome", "飓风果于当日辰时停息"),
            ("outcome", "果当日辰时止息")], no_fffd_case=True)
CUSTOM["LY-428"] = dict(
    verdict="部分成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：回原卡——所问「占關差得否」；R73 manifest 结局「卽於壬寅日得差﹐次年三月死於中途﹐」以逗号收尾——疑似截断之表面属实；但得差与次年三月死于中途两段均明载。故部分成立（同 LY-418 逗号收尾口径）。",
    carry="同旨新立：自 R74 起承接本 R73 标注：按「结局以逗号收尾、疑似截断，得差与死于中途两段明载」登记；结局原文照录不改。",
    quotes=[("input", "占關差得否"), ("outcome", "卽於壬寅日得差﹐次年三月死於中途﹐")])
CUSTOM["YY-006"] = dict(
    verdict="部分成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：回原卡——所问英宗北狩车驾何时旋归、归后处境、能否复辟；R73 manifest 结局「后英宗南旋，及锢南内，最后夺门复辟，年月日悉符其占。」——南旋、锢南内、夺门复辟三事均明载；但三事之具体年月日仅以末句『悉符其占』总承收束、无逐项年月日可核，所指属实一层。故部分成立（同总承式结局口径）。",
    carry="同旨新立：自 R74 起承接本 R73 标注：按「结局三事明载、具体年月日以『悉符其占』总承收束无逐项可核」登记；结局原文照录不改。",
    quotes=[("input", "车驾何时旋归"), ("outcome", "后英宗南旋，及锢南内，最后夺门复辟，年月日悉符其占。")])
CUSTOM["BZ-027"] = dict(
    verdict="部分成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：回原卡——所问「断此命造（一生格局、吉凶与运程）」（命主荀慧生）；R73 manifest 结局载创荀派、四大名旦之一与 1972 年卒之史实主线，并自注『确曾一度息影务农而无所获（原书已自注此节为既验之事）』——结局含占前既验一节属实，但已在结局文本内逐字自注、非未注明问题，史实主线明载。故部分成立（同 BZ-105 回溯／BZ-036 自注口径）。",
    carry="同旨新立：自 R74 起承接本 R73 标注：按「结局含占前既验一节、已在结局内自注，史实主线明载」登记；结局原文照录不改。",
    quotes=[("input", "断此命造（一生格局、吉凶与运程）"),
            ("outcome", "确曾一度息影务农而无所获（原书已自注此节为既验之事）"), ("outcome", "1972年卒")])
CUSTOM["AS-206"] = dict(
    verdict="部分成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：回原卡——所问「If she should marry the man desired?」；R73 manifest 结局作『Recorded within the judgment passage itself: that person at last, with a little difficulty, produced the Marriage to effect, to the content of both parties.』——婚成事实有载，但系编者转述、录于原书断语段内、无独立后记与时点，所指成色一层属实。故部分成立。",
    carry="同旨新立：自 R74 起承接本 R73 标注：按「结局录于原书断语段内、系编者转述，婚成事实有载、无独立时点」登记；结局原文照录不改。",
    quotes=[("input", "If she should marry the man desired?"),
            ("outcome", "produced the Marriage to effect, to the content of both parties")])
CUSTOM["LY-440"] = dict(
    verdict="部分成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：回原卡——所问「因連日雪占何日晴」；R73 manifest 结局「果於次日卯時﹐云開日出﹐」以逗号收尾——疑似截断之表面属实；但次日卯时云开日出之主结局明载、与何日晴问面直接对应。故部分成立（同 LY-418 逗号收尾口径）。",
    carry="同旨新立：自 R74 起承接本 R73 标注：按「结局以逗号收尾、疑似截断，次日卯时云开日出主结局明载」登记；结局原文照录不改。",
    quotes=[("input", "因連日雪占何日晴"), ("outcome", "果於次日卯時﹐云開日出﹐")])
CUSTOM["LY-543"] = dict(
    verdict="不成立", relation="新旗标（R73 新立）",
    finding="新旗标（R73 新立）：内容错配——Y4 旗标所引结局『後果於寅年醫好富翁，厚贈讀書』逐字属 LY-202 结局（落盘脚本断言：在 LY-202 结局在场、在本例结局不在场），与本例问面、prediction、结局全不相涉；回原卡——本例所问「占兵到一家當避何處」，R73 manifest 结局「彼回即领家眷往东去，后来覆我曰平安，惟其弟牵念父母往探之，行至半途遭害矣．」载一家东避覆平安、与 prediction『一家有可避之處、避得過去可保平安』直接对应，弟往探遭害系旁及一节、非问面错位。故旗标不成立，错配事实另登记于特别核查②。",
    carry="新立定案：自 R74 起承接本 R73 标注（旗标不成立、所引结局系 LY-202 文本之内容错配登记）；结局原文照录不改。",
    quotes=[("input", "占兵到一家當避何處"), ("outcome", "彼回即领家眷往东去，后来覆我曰平安"),
            ("prediction", "一家有可避之處、避得過去可保平安")], ly202_check=True)
CUSTOM["YM-014"] = dict(
    verdict="部分成立", relation="同旨续接（R65）",
    finding="承接既有定案不重裁（历轮最近同旨定案 R65 部分成立）：本轮 X2 旗标复归 R65 旧旨——R73 manifest 结局「至甲午日而回禄，以夏至后先壬而后甲也。」中回禄终局明载、尾句『以夏至后先壬而后甲也』为应验解释层并载，与 R65 定案（解释层并载、部分成立）同旨；R72 新旨（方向相左属评分面、不成立）与本旨各旨独立、并行不悖，照旧登记。本轮（R73）manifest 该例结局与历轮所核文本一致。",
    carry="同旨续接：自 R74 起承接 R65＋本 R73 标注；结局原文照录不改。",
    quotes=[("input", "占家宅（火灾之虞）"), ("outcome", "至甲午日而回禄，以夏至后先壬而后甲也。")])
CUSTOM["YM-070"] = dict(
    verdict="未核", relation="待核维持（旗标触及、只登记不裁）",
    finding="待核维持（本轮旗标触及、只登记不裁）：X3／Y3 旗标登记结局措辞「后果同行都下」语义未明待核——逐字回读 R73 结局原文确作『后果同行都下。』，触及属实；本例维持 R71 未核原登记（『都下』语义未明＋『甲寅旬』出处待核并列、无盘外独立史源不裁），本轮只登记触及、不入裁断。",
    carry="待核维持：自 R74 起维持原登记（『都下』语义未明＋『甲寅旬』出处待核、无盘外独立史源不裁）；结局原文照录不改。",
    quotes=[("outcome", "后果同行都下。")])

# 续接件附加核明层（引文断言随附）
APPEND = {}
APPEND["LY-335"] = ("另本轮核明：逐字核 R73 prediction_text，首句即具体断语『斷教師可聘而不可久（negative，就可久一問不成立）』，"
                    "R72 定案所据『所問之事可成』泛指句在本轮 prediction_text 不在场——Y2 旗标所指 carry 登记与本轮 prediction 全文口径不合一层属实、并行登记；"
                    "R72 泛指一层系旧轮 prediction 文本面之登记，档位照 R72 部分成立承接、不重裁。")
APPEND["BZ-019"] = ("另本轮核明：逐字核 R73 prediction_text，全文无『位极人臣』一语，本轮作『故格局等级断至极贵：下限封疆卿相、上限人君，落点取上限侧』——"
                    "Y2 旗标所指 carry 所引称谓与本轮 prediction_text 口径不合一层属实、并行登记；称谓出入系旧轮 prediction 登记，档位不变。")
APPEND["LY-036"] = ("另本轮核明：X4 所指无据降格一层在本轮 prediction 仍在场（『用神四源（现卦同亲、变爻、日月、伏神）俱无可定主者，盘面不足以定主用神，终局按无据降格取不利向』）；"
                    "Y4 所指 carry_note 称 prediction 不报方向一层，经逐字核 R73 prediction_text 明载『终局（单一方向，negative）：官事难成』、方向断在场，"
                    "该 carry 措辞与本轮 prediction 口径不合一层并行登记、档位不变。")
APPEND["LY-218"] = ("另本轮 Y2 旗标兼及结局首段框架一层——逐字核 R73 结局，首段即『癸酉年占至乙巳年三十餘載，復遇其人而問曰：尊翁健否？答曰：甚健。』，"
                    "父寿终局系三十余载后复遇追问所载属实，与本旨（双占分载＋古法解释层）同例并行登记、档位不变。")

def append_asserts(cid):
    if cid == "LY-335":
        pred = load(P3 / "runs/round73/predictions/LY-335.json")
        assert "所問之事可成：用神有氣、助力在，終局主成。" not in pred["prediction_text"]
        assert_quote(cid, "斷教師可聘而不可久", "prediction")
    elif cid == "BZ-019":
        pred = load(P3 / "runs/round73/predictions/BZ-019.json")
        assert "位极人臣" not in pred["prediction_text"]
        assert_quote(cid, "故格局等级断至极贵：下限封疆卿相、上限人君，落点取上限侧", "prediction")
    elif cid == "LY-036":
        assert_quote(cid, "用神四源（现卦同亲、变爻、日月、伏神）俱无可定主者，盘面不足以定主用神，终局按无据降格取不利向", "prediction")
        assert_quote(cid, "终局（单一方向，negative）：官事难成", "prediction")
    elif cid == "LY-218":
        assert_quote(cid, "三十餘載", "outcome")
        assert_quote(cid, "尊翁健否", "outcome")

# ---------- flag 要旨生成 ----------
def clean_entry(e):
    t = e["text"]
    t = re.sub(r"^-+\s*", "", t)
    t = re.sub(r"^\d+\.\s*", "", t)
    t = t.replace("**", "")
    t = re.sub(r"^anon_id[:=]\s*", "", t)
    t = re.sub(r"^anon_id:\s*", "", t)
    t = re.sub(r"^P3-[0-9a-f]{8}\s*[｜|]\s*", "", t)
    t = re.sub(r"^P3-[0-9a-f]{8}\s+", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t[:240]

# ---------- 组装 ----------
flags_out, ann_out = [], []
for anon in anon_order:
    cid = host[anon]
    ents = by_anon[anon]
    seats = [e["seat"] for e in ents]
    views = sorted(set(s[0] for s in seats))
    flag_summary = "；".join(f"{e['seat']}：{clean_entry(e)}" for e in ents)
    sources = [rel(P3 / f"inputs-dev12/{cid}.json"),
               rel(FLAGS_MD),
               rel(MANIFEST73) + f" cases[{cid}]",
               rel(P3 / f"runs/round73/predictions/{cid}.json")]
    for (r, _a) in prior.get(cid, []):
        sources.append(rel(P3 / f"data/case-annotations-r{r}.json") + f" {cid} 条")
    if cid in CUSTOM:
        c = CUSTOM[cid]
        verdict, finding, relation, carry = c["verdict"], c["finding"], c["relation"], c["carry"]
        for (where, q) in c["quotes"]:
            assert_quote(cid, q, where)
        if c.get("no_fffd_case"):
            assert_no_fffd_file(P3 / f"inputs-dev12/{cid}.json")
            assert_no_fffd_file(P3 / f"runs/round73/predictions/{cid}.json")
            assert b"\xef\xbf\xbd" not in cases73[cid].encode("utf-8")
        if c.get("ly202_check"):
            assert "醫好富翁" in cases73["LY-202"] and "醫好富翁" not in cases73["LY-543"]
            assert "厚贈讀書" in cases73["LY-202"]
        category = "待核维持（详见核查事实）" if cid in PENDING else (
            "同旨续接（详见核查事实）" if cid == "YM-014" else "新旗标（详见核查事实）")
    else:
        hist = prior[cid]
        lr, la = hist[-1]
        verdict = la["disposition"]
        finding = f"承接既有定案不重裁（历轮最近定案 R{lr} {verdict}）：" + (la.get("finding") or "")
        if cid in APPEND:
            append_asserts(cid)
            finding += " " + APPEND[cid]
        finding += " 本轮（R73）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。"
        relation = f"同旨续接（R{lr}）"
        carry = f"同旨续接：自 R74 起承接 R{lr}＋本 R73 标注；结局原文照录不改。"
        category = "同旨续接（详见核查事实）"
    if verdict == "部分成立":
        assert carry.strip(), f"{cid} 部分成立件 carry 为空"
    flags_out.append({
        "anon_id": anon, "case_id": cid, "verdict": verdict, "disposition": verdict,
        "basis": finding, "carry_suggestion": carry, "manifest_carry_suggestion": carry,
        "flag": flag_summary, "category": category, "views": views,
        "dual_view": len(views) > 1, "relation": relation, "registered_round": 73,
        "sources_checked": sources})
    ann_out.append({
        "anon_id": anon, "case_id": cid, "disposition": verdict, "finding": finding,
        "flag": flag_summary, "manifest_carry_suggestion": carry, "relation": relation,
        "registered_round": 73, "sources_checked": sources, "source_seats": seats})

verdicts = Counter(a["disposition"] for a in ann_out)
assert sum(verdicts.values()) == 156
n_cont = sum(1 for a in ann_out if a["relation"].startswith("同旨续接"))
n_gist = sum(1 for a in ann_out if a["relation"].startswith("同例新旨"))
n_new = sum(1 for a in ann_out if a["relation"].startswith("新旗标"))
n_pend = sum(1 for a in ann_out if a["relation"].startswith("待核维持"))
assert (n_cont, n_gist, n_new, n_pend) == (145, 0, 10, 1), (n_cont, n_gist, n_new, n_pend)
assert verdicts == Counter({"部分成立": 140, "成立": 11, "不成立": 4, "未核": 1}), verdicts
seat_case_counts = Counter()
for anon in anon_order:
    ss = set(e["seat"] for e in by_anon[anon])
    seat_case_counts[len(ss)] += 1
assert seat_case_counts == Counter({2: 103, 1: 53}), seat_case_counts

# ---------- 特别核查③：指令性字样复扫 ----------
kws = ["请按", "须注", "須注", "评分时", "評分時", "比对时", "比對時", "使用时须", "使用時須",
       "分开统计", "分開統計", "勿以此斷", "不可以", "不得"]
kw_hits = sorted(cid for cid, t in cases73.items() if any(k in t for k in kws))
assert kw_hits == ["BZ-036", "BZ-042", "BZ-105", "LY-204", "LY-246", "YM-009", "YM-029", "YY-014"], kw_hits
wide_hits = sorted(cid for cid, t in cases73.items() if any(c in t for c in ["请", "請", "须", "須", "勿"]))
assert wide_hits == ["BZ-036", "BZ-105", "BZ-302", "LR2-022", "LR3-004", "LR3-006", "LR3-010", "LY-204", "LY-227", "LY-416"], wide_hits
assert "评分时" not in cases73["LR2-016"]
assert "评分时该细项请按未完全复核处理" in man73["_r56_lr2016_split"]["editor_note"]
assert_quote("BZ-036", "盲测比对须注", "outcome")
assert_quote("BZ-042", "（盲测比对时以格局大富一项为主）", "outcome")
assert_quote("BZ-105", "使用时须分开统计", "outcome")
assert_quote("LY-204", "勿以此斷", "outcome")

# ---------- 特别核查②：引文层复核（失败清单逐件定性） ----------
quote_fails = []
for e in entries:
    cid = host[e["anon"]]
    corp = corpus_of(cid)
    for tup in re.findall(r"「([^」]{2,})」|『([^』]{2,})』", e["text"]):
        q = [x for x in tup if x][0]
        if q not in corp:
            quote_fails.append((e["seat"], e["anon"], cid, q))
fail_keys = sorted(set((s, c) for (s, _a, c, _q) in quote_fails))
assert fail_keys == [], fail_keys
# LY-543 内容错配专项断言（旗标引文属 LY-202）
assert "醫好富翁" in cases73["LY-202"] and "醫好富翁" not in cases73["LY-543"]
assert "後果於寅年醫好富翁" in cases73["LY-202"]

special_checks = [
    {
        "item": "特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记",
        "conclusion": "YM-070 本轮被旗标触及（X3／Y3 两条同旨：结局措辞「后果同行都下」之『都下』语义未明待核），依任务口径只登记触及、维持 R71 未核原登记（『都下』语义未明＋『甲寅旬』出处待核并列）、不入裁断，以未核入本轮 annotations。BZ-029／BZ-040／LY-537 本轮未被任何旗标触及，不入 annotations、维持各自原登记。",
        "evidence": "据 runs/round73/judging/host-mapping.json 与 FLAGS-selfreported-r73.md 逐件比对：156 件 case_id 集合含 YM-070（anon P3-9c155020）、不含 BZ-029／BZ-040／LY-537（落盘脚本断言通过）；YM-070 结局原文逐字断言（「后果同行都下。」）通过。",
        "scope_note": "本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。",
    },
    {
        "item": "特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）",
        "conclusion": "内容错配 1 件：LY-543（anon P3-ec970d58，Y4 单席）——旗标所引结局『後果於寅年醫好富翁，厚贈讀書』逐字属 LY-202 结局（LY-202 本轮另有 X4 旗标 P3-ecf83ba2、自洽在案），与 LY-543 问面（占兵到一家當避何處）、prediction、结局全不相涉，已定案旗标不成立；host-mapping 对 P3-ec970d58→LY-543 之对位经回读本例三源确认无误，错配在旗标引文层、非映射层。括号对位错配 0 件：旗标正文内出现的他人 case_id 字样仅 LY-030 两处 LY-612，均系『相对同条全文（LY-612）』之同条对勘引用、历轮已登记，非串号。引文逐字复核（「」『』引文对本例语料）：未命中 0 处。anon 形近对位复核：P3-2bb4587d（LY-413）／P3-2bbf2044（LY-105）、P3-5e62e501（LY-426）／P3-5e67a1bc（YM-014）、P3-6184cfc2（LY-434）／P3-618671c0（BQ-001）、P3-86240c9f（LY-514）／P3-86244110（AS-210）四组形近 anon 经逐件回读三源，内容均与各自 case 相合、对位正确。主张层口径不合 3 件（LY-335／BZ-019／LY-036）：R73 prediction_text 与 carry 旧登记措辞不合（LY-335 泛指句不在场而具体断语在场、BZ-019『位极人臣』不在场、LY-036 方向断在场），均已逐件并行登记于各该例定案、档位不变；LY-218 之 Y2 兼及结局首段复遇框架一层，同例并行登记。乱码主张 1 件（BQ-014）盘上无据，见特别核查④。",
        "evidence": "落盘脚本断言：「」『』引文未命中集合为空；LY-202 结局含『後果於寅年醫好富翁』且 LY-543 结局不含该语；LY-335／BZ-019／LY-036 三件口径核明断言（不在场／在场逐字断言）与 LY-218 结局首段断言均通过。",
        "scope_note": "本核查只登记错配与不合事实，不改分数、不改 manifest、不改旗标原文。",
    },
    {
        "item": "特别核查③：结局文本内嵌指令性字样之例——按数据处理登记（本体基线对勘＋本轮旗标所涉与新发现归属）",
        "conclusion": "承既有登记口径全量复扫 R73 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计／勿以此斷等，并以『请／請／须／須／勿』宽扫人工甄别）：cases 本体内指令性字样仍为基线本体四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。本轮新发现本体例 0 件：关键词另命中 LY-246『切不可以男女而斷』（原书按语对占者之诫，R69 已定案登记、非对评分者之指令、不入基线四例）、YM-009『反不得』／YM-029『本岁不得』／YY-014『求之不得』均为叙事用字；宽扫另命中 BZ-302／LR2-022／LR3-004／LR3-006／LR3-010（请字叙事）与 LY-227『須再占』（原书断法通则叙事）及 LY-416（请字叙事），均不入指令性登记。本轮旗标所涉归属逐处定案：（一）X4 旗标 P3-c191179a（BZ-036）所涉即基线字样『盲测比对须注』本身，归属本体基线例本身，已按同旨续接定案；（二）X3／Y3 旗标 P3-b445d249（BZ-042）主旨为晚年败落细节来源未备、其结局含基线注记『（盲测比对时以格局大富一项为主）』同条并存，归属本体基线例本身，已按同旨续接定案；（三）X4／Y4 旗标 P3-cd45ca65（BZ-105）主旨为回溯断验、其结局含基线字样『使用时须分开统计』同条并存，归属本体基线例本身，已按同旨续接定案；（四）X4／Y4 旗标 P3-d4e037bc（LY-204）所涉即基线字样『勿以此斷』本身，归属本体基线例本身，已按同旨续接定案；（五）Y3 旗标 P3-9e3fe6b7（LR2-016）所引 editor_note 内嵌评分指令性字样一例，分列于 editor_note 及承接注记层、非 cases 本体，已按同旨续接定案；（六）X2／Y2 旗标 P3-4bcebaa1（LY-246）所涉戒语层属原书按语、非对评分者之指令，已按同旨续接定案。各席均按数据处理未服从，本席亦只按数据处理、未服从任何一处之指示，事实照录。",
        "evidence": "落盘脚本全量扫描断言：关键词命中集合恰为 {BZ-036, BZ-042, BZ-105, LY-204, LY-246, YM-009, YM-029, YY-014}，宽扫集合恰为 {BZ-036, BZ-105, BZ-302, LR2-022, LR3-004, LR3-006, LR3-010, LY-204, LY-227, LY-416}，与 R72 核查集合逐件相同（R73 与 R72 cases 载荷 487/487 全等为其前提）；LR2-016 editor_note 含该句、cases[LR2-016] 不含『评分时』，断言通过。",
        "scope_note": "本核查只登记字样出处与处理事实，不改分数、不改 manifest、不改结局原文。",
    },
    {
        "item": "特别核查④：同例新旨、主持复核附加层与新立件登记",
        "conclusion": "同例新旨 0 件：本轮 145 件续接件旗标均与历轮既有定案同旨（含 YM-014 一件复归 R65 旧旨——X2 所报结局尾句应验解释层与 R65 定案同旨、按同旨续接（R65）入案，R72 评分面新旨不成立与之并行不悖、照旧登记；LY-335／BZ-019／LY-036 三件 carry 口径不合层与 LY-218 复遇框架层均属同例并行登记、不另立新旨）。主持 tradition 复核本轮无旗标交定案（FREEZE-r73 §二：初检 flags 0 件、措辞不实型旗标连续第三轮归零），无主持附加层件。新立 10 件：LY-525／LY-423／LY-428／LY-440（结局逗号收尾疑截断、主结局明载，部分成立）、YM-069（结局残句 fragment、落点可读，部分成立）、YY-006（结局三事明载、年月日以总承收束，部分成立）、BZ-027（结局含占前既验一节、已自注，部分成立）、AS-206（结局录于断语段内、系编者转述，部分成立）、BQ-014（乱码主张盘上无据，不成立）、LY-543（旗标引文系 LY-202 文本之内容错配，不成立）。待核触及 1 件（YM-070）见特别核查①。另登记：历轮定案档逐号精确打开时 r52 号文件盘上不存在（r49-r51、r53-r72 均在），承接核对以盘上实存各号为准、该缺失已在本件 _provenance 与本项登记，不影响本轮 156 件承接判定（各件最近定案均出自实存号）。",
        "evidence": "据 FLAGS-selfreported-r73.md 主持复核节、data/case-annotations-r65.json YM-014 条与本轮逐件回源核查；r52 缺失由落盘脚本逐号打开断言记录（missing_round_files == [52]）。",
        "scope_note": "本核查只登记构成事实，不改分数、不改 manifest。",
    },
    {
        "item": "特别核查⑤：汇编一致性与结局文本一致性",
        "conclusion": "汇编 FLAGS-selfreported-r73.md 八席自报共 259 条编号条目、259 次 anon 出现（与条目数相等、无条内交叉引用提及）、156 anon、156 例（单席 53 例、双席 103 例；X 侧独有 20 例、Y 侧独有 33 例、双侧同报 103 例），主持 tradition 复核交定案 0 件，合计定案 156 例；R73 各例结局文本经脚本断言与 R72 manifest 逐件全等（487/487），续接类定案的『结局与历轮所核文本一致』前提全数成立。本轮括号对位异常 0 件、内容错配 1 件（LY-543，见特别核查②）。承接附则对勘：R72 定案部分成立 77 件与 R73 manifest _r73_carryover_notes_addendum 逐件对勘结论见 data/manifest-carryover-r73-addendum.md（由 data_r73_addendum.py 编制）。",
        "evidence": "落盘脚本 data_r73_build.py 断言输出：entries=259、anon_occurrences=259、anons=156、cases_equal_r72=487/487、verdicts 与 annotations 逐件复算一致。",
        "scope_note": "本核查只登记一致性事实。",
    },
]

counts = {
    "selfreport_flag_rows_total": 259,
    "selfreport_numbered_items_total": 259,
    "selfreport_anons_total": 156,
    "selfreport_cases_total": 156,
    "host_tradition_flags_total": 0,
    "host_tradition_only_cases": 0,
    "cases_total": 156,
    "continuation_cases": n_cont,
    "same_case_new_gist_cases": n_gist,
    "new_flag_cases": n_new,
    "pending_touch_cases": n_pend,
    "verdicts": {"成立": verdicts.get("成立", 0), "部分成立": verdicts.get("部分成立", 0),
                 "不成立": verdicts.get("不成立", 0), "未核": verdicts.get("未核", 0)},
}
provenance = (
    "R73 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断，不改任何分数）逐件回源核查 R73 八席自报旗标 "
    "259 条编号条目／259 次 anon 出现（与条目数相等、无条内交叉引用提及）、去重为 156 anon／156 例，"
    "主持 tradition 复核交定案 0 件。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、"
    "runs/round73/predictions/<case_id>.json 预测原文、runs/round73/judging/outcome-manifest.json cases 载荷"
    "（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），并与历轮定案档（data/case-annotations-r49.json 至 -r72.json 逐号精确打开；"
    "r52 号文件盘上不存在、已登记）核对承接关系：145 件为同旨续接（只承接不重裁；含 YM-014 复归 R65 旧旨一件、按同旨续接（R65）入案），"
    "同例新旨 0 件，10 件为 R73 新立（LY-525／YM-069／LY-423／LY-428／YY-006／BZ-027／AS-206／LY-440 部分成立；"
    "BQ-014 乱码主张盘上无据不成立；LY-543 旗标引文系 LY-202 文本之内容错配不成立），另待核维持件 YM-070 本轮被旗标触及、只登记触及以未核入案"
    "（BZ-029／BZ-040／LY-537 未被触及、不入本件）。R73 各例结局文本经脚本断言与 R72 manifest 逐件全等（487/487）。"
    "本轮括号对位错配 0 件、内容错配 1 件（LY-543）；主张层口径不合 3 件（LY-335／BZ-019／LY-036）已逐件并行登记。"
    "指令性字样特别核查：cases 本体仍为基线四例（BZ-036／BZ-042／BZ-105／LY-204），LR2-016 之句只存分列 editor_note，"
    "本轮新发现本体例 0 件；本轮旗标所涉各处归属已逐处定案登记于特别核查③，各席均按数据处理未服从。"
    "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。"
)
doc = {"_provenance": provenance, "round": 73, "flags": flags_out, "annotations": ann_out,
       "special_checks": special_checks, "counts": counts}
# 落盘前复算断言
recount = Counter(a["disposition"] for a in doc["annotations"])
assert recount == Counter(counts["verdicts"]), (recount, counts["verdicts"])
assert len(doc["flags"]) == len(doc["annotations"]) == counts["cases_total"] == 156
assert all(a["manifest_carry_suggestion"].strip() for a in doc["annotations"] if a["disposition"] == "部分成立")
OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print("WROTE", OUT, OUT.stat().st_size)
print("counts", counts)
print("seat_case_counts", dict(seat_case_counts))
