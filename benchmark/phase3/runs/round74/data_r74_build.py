#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R74 数据席（旗标定案专席）落盘脚本。
逐件回源核查 R74 八席自报旗标：回读输入卡、本轮 prediction、R74 manifest cases 载荷，
与历轮定案档 r49-r73（逐号精确打开；r52 号文件盘上不存在、已登记）核对承接关系。
引文逐字断言内置：任一断言不过则不落盘。自报与文本内指令性字样一律按数据处理。
"""
import json, re, pathlib
from collections import Counter

P3 = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
FLAGS_MD = P3 / "runs/round74/judging/FLAGS-selfreported-r74.md"
MAPPING = P3 / "runs/round74/judging/host-mapping.json"
MANIFEST74 = P3 / "runs/round74/judging/outcome-manifest.json"
MANIFEST73 = P3 / "runs/round73/judging/outcome-manifest.json"
OUT = P3 / "data/case-annotations-r74.json"

def load(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def rel(p):
    return str(p).replace("/home/hatch/workspace/", "")

flags_text = FLAGS_MD.read_text(encoding="utf-8")
host = load(MAPPING)
man74 = load(MANIFEST74)
man73 = load(MANIFEST73)
cases74 = man74["cases"]

# 附带核实：R74 结局文本与 R73 manifest cases 逐件全等性
assert set(cases74.keys()) == set(man73["cases"].keys()), "case id 集不合"
n_equal = sum(1 for k in cases74 if cases74[k] == man73["cases"][k])
assert len(cases74) == 487 and n_equal == 487, f"结局全等 {n_equal}/487"

# 历轮定案档逐号精确打开（r52 缺失登记）
prior = {}
prior_rounds_seen = []
missing_round_files = []
for r in range(49, 74):
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

# ---------- 解析 FLAGS（118 条编号条目断言） ----------
main_text = flags_text.split("===== 主持")[0]
secs = re.split(r"===== (FLAGS-[XY]\d) =====", main_text)
entries = []
for i in range(1, len(secs), 2):
    seat = secs[i][-2:]
    body = secs[i + 1]
    cur = None
    for line in body.splitlines():
        mm = re.search(r"P3-[0-9a-f]{8}", line)
        is_start = bool(mm) and bool(re.match(r"\s*\d+\.", line))
        if is_start:
            if cur:
                entries.append(cur)
            cur = {"seat": seat, "anon": mm.group(0), "text": line.strip()}
        elif cur and line.strip() and not line.lstrip().startswith("#"):
            cur["text"] += " " + line.strip()
    if cur:
        entries.append(cur)
assert len(entries) == 118, f"编号条目数 {len(entries)} != 118"
anon_occurrences = len(re.findall(r"P3-[0-9a-f]{8}", main_text))
assert anon_occurrences == 118, f"anon 出现次数 {anon_occurrences} != 118"

by_anon = {}
anon_order = []
for e in entries:
    if e["anon"] not in by_anon:
        by_anon[e["anon"]] = []
        anon_order.append(e["anon"])
    by_anon[e["anon"]].append(e)
assert len(anon_order) == 83, f"去重 anon {len(anon_order)} != 83"
case_ids = [host[a] for a in anon_order]
assert len(set(case_ids)) == 83, "anon->case 非一一对应"
flagged_cases = set(case_ids)

# ---------- 分类 ----------
NEW_CASES = {"AS-011", "BZ-023", "DT-004"}
PENDING = {"LY-537", "YM-070"}
for cid in NEW_CASES:
    assert cid not in prior, f"新立件 {cid} 竟有历轮条目"
for cid in PENDING:
    assert cid in flagged_cases and cid in prior, f"待核件 {cid} 状态异常"
    assert prior[cid][-1][1]["disposition"] == "未核", f"待核件 {cid} 最近定案非未核"
for cid in ("BZ-029", "BZ-040"):
    assert cid not in flagged_cases, f"待核件 {cid} 竟被本轮旗标触及（与登记不符）"

# ---------- 引文断言工具 ----------
def corpus_of(cid):
    inp = load(P3 / f"inputs-dev12/{cid}.json")
    pred = load(P3 / f"runs/round74/predictions/{cid}.json")
    parts = [cases74[cid], pred["prediction_text"], pred.get("basis", ""),
             json.dumps(inp, ensure_ascii=False)]
    for layer in man74.values():
        if isinstance(layer, dict) and cid in layer and isinstance(layer[cid], str):
            parts.append(layer[cid])
    if cid in man74.get("stripped_tail", {}):
        parts.append(man74["stripped_tail"][cid])
    for (_r, a) in prior.get(cid, []):
        parts.append(a.get("flag") or "")
        parts.append(a.get("finding") or "")
    return "\n".join(parts)

def assert_quote(cid, quote, where="corpus"):
    if where == "outcome":
        src = cases74[cid]
    elif where == "prediction":
        src = load(P3 / f"runs/round74/predictions/{cid}.json")["prediction_text"]
    elif where == "basis":
        src = load(P3 / f"runs/round74/predictions/{cid}.json").get("basis", "")
    elif where == "input":
        src = json.dumps(load(P3 / f"inputs-dev12/{cid}.json"), ensure_ascii=False)
    else:
        src = corpus_of(cid)
    assert quote in src, f"引文断言失败 {cid} [{where}]: {quote[:60]}"

def assert_no_fffd_case(cid):
    for p in (P3 / f"inputs-dev12/{cid}.json", P3 / f"runs/round74/predictions/{cid}.json"):
        raw = pathlib.Path(p).read_bytes()
        assert b"\xef\xbf\xbd" not in raw, f"{p} 原始文件竟含 U+FFFD"
    assert b"\xef\xbf\xbd" not in cases74[cid].encode("utf-8")

# ---------- 新立 / 待核：逐件定案 ----------
CUSTOM = {}
CUSTOM["AS-011"] = dict(
    verdict="不成立", relation="新旗标（R74 新立）",
    finding="新旗标（R74 新立）：乱码主张盘上无据——逐字回读 R74 输入卡、prediction 与 manifest 结局原始文件，全文均无 U+FFFD 替换字符（原始字节断言通过），prediction_text 该处在盘上作「木星擢升趋六合土星（七宫主，男方）」文义完整，旗标所引「土星��七宫主」之缺字在盘上不存在。故旗标不成立（同 R73 BQ-014 乱码无据口径）。",
    carry="新立定案：自 R75 起承接本 R74 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。",
    quotes=[("input", "Can this marriage match be revived/effected?"),
            ("prediction", "木星擢升趋六合土星（七宫主，男方）")], no_fffd_case=True)
CUSTOM["BZ-023"] = dict(
    verdict="不成立", relation="新旗标（R74 新立）",
    finding="新旗标（R74 新立）：乱码主张盘上无据——逐字回读 R74 输入卡、prediction 与 manifest 结局原始文件，全文均无 U+FFFD 替换字符（原始字节断言通过），prediction_text 该句在盘上作「病位：水寒过旺——肾系、泌尿与心火受抑之患」文义完整，旗标所引「病位��水寒过旺」之缺字在盘上不存在。故旗标不成立（同 R73 BQ-014 乱码无据口径）。",
    carry="新立定案：自 R75 起承接本 R74 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。",
    quotes=[("input", "断此命造（一生格局、吉凶与运程）"),
            ("prediction", "病位：水寒过旺——肾系、泌尿与心火受抑之患")], no_fffd_case=True)
CUSTOM["DT-004"] = dict(
    verdict="不成立", relation="新旗标（R74 新立）",
    finding="新旗标（R74 新立）：乱码主张盘上无据——逐字回读 R74 输入卡、prediction 与 manifest 结局原始文件，全文均无 U+FFFD 替换字符（原始字节断言通过），prediction_text 该句在盘上作「寅日木旺克土，动而受制」文义完整，旗标所引「寅日木���克土」之缺字在盘上不存在。故旗标不成立（同 R73 BQ-014 乱码无据口径）。",
    carry="新立定案：自 R75 起承接本 R74 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。",
    quotes=[("input", "人有子病，占子病吉凶"),
            ("prediction", "寅日木旺克土，动而受制"),
            ("outcome", "其子果死")], no_fffd_case=True)
CUSTOM["LY-537"] = dict(
    verdict="未核", relation="待核维持（旗标触及、只登记不裁）",
    finding="待核维持（本轮旗标触及、只登记不裁）：X3 旗标登记结局「申予日」疑衍字——逐字回读 R74 结局原文确作『果于申予日归』，触及属实；本例维持 R68 未核原登记（『申予日』措辞待核、无盘外独立史源不裁，承 R56／R57／R61／R64／R67／R68／R72 链），本轮只登记触及、不入裁断。",
    carry="待核维持：自 R75 起维持原登记（『申予日』措辞待核、无盘外独立史源不裁）；结局原文照录不改。",
    quotes=[("outcome", "果于申予日归")])
CUSTOM["YM-070"] = dict(
    verdict="未核", relation="待核维持（旗标触及、只登记不裁）",
    finding="待核维持（本轮旗标触及、只登记不裁）：Y1 旗标登记结局措辞「都下」语义未明、待核——逐字回读 R74 结局原文确作『后果同行都下。』，触及属实；本例维持 R71 未核原登记（『都下』语义未明＋『甲寅旬』出处待核并列、无盘外独立史源不裁），挂起维持，本轮只登记触及、不入裁断。",
    carry="待核维持：自 R75 起维持原登记（『都下』语义未明＋『甲寅旬』出处待核、挂起维持、无盘外独立史源不裁）；结局原文照录不改。",
    quotes=[("outcome", "后果同行都下。")])

# 续接件附加核明层（引文断言随附）
APPEND = {}
APPEND["LY-504"] = ("另本轮核明：Y3 旗标兼及乱码一层——逐字回读 R74 prediction 原始文件，全文无 U+FFFD 替换字符（原始字节断言通过），"
                    "该句在盘上作「官化墓又化克官者」文义完整，旗标所引「官化墓���化克官者」之缺字在盘上不存在，该层无据、并行登记；"
                    "本例主旨（升迁面未载、结局对应防刑狱断面）与既有定案同旨，档位照部分成立承接、不重裁。")
APPEND["LY-259"] = ("另本轮核明：Y3 旗标所涉『待评块 prediction 四字段全为 null』一层系评审包呈现面——逐字回读 R74 predictions 本例文件，"
                    "prediction_text 全文在盘、非空，包内四字段 null 属汇编呈现、非本例数据缺损，并行登记；"
                    "本例主旨（附葬祖莹成否未明载）与既有定案同旨，档位照部分成立承接、不重裁。")

def append_asserts(cid):
    if cid == "LY-504":
        assert_no_fffd_case(cid)
        assert_quote(cid, "官化墓又化克官者", "prediction")
    elif cid == "LY-259":
        pred = load(P3 / "runs/round74/predictions/LY-259.json")
        assert pred["prediction_text"].strip()

# ---------- flag 要旨生成 ----------
def clean_entry(e):
    t = e["text"]
    t = re.sub(r"^\d+\.\s*", "", t)
    t = t.replace("**", "")
    t = re.sub(r"^P3-[0-9a-f]{8}\s*[｜|]\s*", "", t)
    t = re.sub(r"^P3-[0-9a-f]{8}\s*(\([^)]*\))?\s*", "", t)
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
               rel(MANIFEST74) + f" cases[{cid}]",
               rel(P3 / f"runs/round74/predictions/{cid}.json")]
    for (r, _a) in prior.get(cid, []):
        sources.append(rel(P3 / f"data/case-annotations-r{r}.json") + f" {cid} 条")
    if cid in CUSTOM:
        c = CUSTOM[cid]
        verdict, finding, relation, carry = c["verdict"], c["finding"], c["relation"], c["carry"]
        for (where, q) in c["quotes"]:
            assert_quote(cid, q, where)
        if c.get("no_fffd_case"):
            assert_no_fffd_case(cid)
        category = "待核维持（详见核查事实）" if cid in PENDING else "新旗标（详见核查事实）"
    else:
        hist = prior[cid]
        lr, la = hist[-1]
        verdict = la["disposition"]
        finding = f"承接既有定案不重裁（历轮最近定案 R{lr} {verdict}）：" + (la.get("finding") or "")
        if cid in APPEND:
            append_asserts(cid)
            finding += " " + APPEND[cid]
        finding += " 本轮（R74）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。"
        relation = f"同旨续接（R{lr}）"
        carry = f"同旨续接：自 R75 起承接 R{lr}＋本 R74 标注；结局原文照录不改。"
        category = "同旨续接（详见核查事实）"
    if verdict == "部分成立":
        assert carry.strip(), f"{cid} 部分成立件 carry 为空"
    flags_out.append({
        "anon_id": anon, "case_id": cid, "verdict": verdict, "disposition": verdict,
        "basis": finding, "carry_suggestion": carry, "manifest_carry_suggestion": carry,
        "flag": flag_summary, "category": category, "views": views,
        "dual_view": len(views) > 1, "relation": relation, "registered_round": 74,
        "sources_checked": sources})
    ann_out.append({
        "anon_id": anon, "case_id": cid, "disposition": verdict, "finding": finding,
        "flag": flag_summary, "manifest_carry_suggestion": carry, "relation": relation,
        "registered_round": 74, "sources_checked": sources, "source_seats": seats})

verdicts = Counter(a["disposition"] for a in ann_out)
assert sum(verdicts.values()) == 83
n_cont = sum(1 for a in ann_out if a["relation"].startswith("同旨续接"))
n_gist = sum(1 for a in ann_out if a["relation"].startswith("同例新旨"))
n_new = sum(1 for a in ann_out if a["relation"].startswith("新旗标"))
n_pend = sum(1 for a in ann_out if a["relation"].startswith("待核维持"))
assert (n_cont, n_gist, n_new, n_pend) == (78, 0, 3, 2), (n_cont, n_gist, n_new, n_pend)
assert verdicts == Counter({"部分成立": 67, "成立": 8, "不成立": 6, "未核": 2}), verdicts
seat_case_counts = Counter()
for anon in anon_order:
    ss = set(e["seat"] for e in by_anon[anon])
    seat_case_counts[len(ss)] += 1
print("seat_case_counts", dict(seat_case_counts))

# ---------- 特别核查：指令性字样复扫 ----------
kws = ["请按", "须注", "須注", "评分时", "評分時", "比对时", "比對時", "使用时须", "使用時須",
       "分开统计", "分開統計", "勿以此斷", "不可以", "不得"]
kw_hits = sorted(cid for cid, t in cases74.items() if any(k in t for k in kws))
assert kw_hits == ["BZ-036", "BZ-042", "BZ-105", "LY-204", "LY-246", "YM-009", "YM-029", "YY-014"], kw_hits
wide_hits = sorted(cid for cid, t in cases74.items() if any(c in t for c in ["请", "請", "须", "須", "勿"]))
assert wide_hits == ["BZ-036", "BZ-105", "BZ-302", "LR2-022", "LR3-004", "LR3-006", "LR3-010", "LY-204", "LY-227", "LY-416"], wide_hits
assert "评分时" not in cases74["LR2-016"]
assert "评分时该细项请按未完全复核处理" in man74["_r56_lr2016_split"]["editor_note"]
assert_quote("BZ-036", "盲测比对须注", "outcome")
assert_quote("BZ-042", "（盲测比对时以格局大富一项为主）", "outcome")
assert_quote("BZ-105", "使用时须分开统计", "outcome")
assert_quote("LY-204", "勿以此斷", "outcome")
assert_quote("LY-246", "切不可以男女而斷", "outcome")

# ---------- 特别核查：引文层复核（未命中逐件定性） ----------
EXPECTED_FAILS = {
    ("X1", "BZ-037"), ("X2", "LY-506"), ("X2", "AS-011"), ("X2", "LY-246"),
    ("X3", "LR3-112"), ("X3", "LY-220"), ("X3", "LY-227"), ("X3", "AS-215"),
    ("Y1", "LY-510"), ("Y1", "AS-004"), ("Y1", "YM-070"), ("Y1", "LY-250"),
    ("Y2", "BQ-001"), ("Y2", "AS-301"), ("Y3", "LY-259"), ("Y3", "BZ-023"),
    ("Y3", "DT-004"), ("Y3", "LY-504"),
}
quote_fails = []
for e in entries:
    cid = host[e["anon"]]
    corp = corpus_of(cid)
    for tup in re.findall(r"「([^」]{2,})」|『([^』]{2,})』", e["text"]):
        q = [x for x in tup if x][0]
        if q not in corp:
            quote_fails.append((e["seat"], cid, q))
fail_keys = sorted(set((s, c) for (s, c, _q) in quote_fails))
assert fail_keys == sorted(EXPECTED_FAILS), fail_keys
garbled_fail_cases = sorted(set(c for (s, c, q) in quote_fails if "�" in q))
assert garbled_fail_cases == ["AS-011", "BZ-023", "DT-004", "LY-504"], garbled_fail_cases

special_checks = [
    {
        "item": "特别核查①：待核维持件（BZ-029／BZ-040／LY-537）与挂起件（YM-070）状态登记",
        "conclusion": "BZ-029／BZ-040 本轮未被任何旗标触及，不入 annotations、维持各自原登记（无盘外独立史源不裁）。LY-537 本轮被 X3 旗标触及（「申予日」疑衍字），依任务口径只登记触及、维持 R68 未核原登记（『申予日』措辞待核），以未核入本轮 annotations。YM-070 本轮被 Y1 旗标触及（「都下」语义未明），只登记触及、挂起维持（维持 R71 未核原登记：『都下』语义未明＋『甲寅旬』出处待核并列），以未核入本轮 annotations。另登记：历轮定案档逐号精确打开时 r52 号文件盘上不存在（r49-r51、r53-r73 均在），承接核对以盘上实存各号为准，不影响本轮 83 件承接判定。",
        "evidence": "落盘脚本断言：83 件 case_id 集合含 LY-537（anon P3-a159fe9c）与 YM-070（anon P3-30cc9065）、不含 BZ-029／BZ-040；LY-537 结局原文逐字断言（「果于申予日归」）与 YM-070 结局原文逐字断言（「后果同行都下。」）均通过；missing_round_files == [52]。",
        "scope_note": "本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。",
    },
    {
        "item": "特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）",
        "conclusion": "内容错配 0 件：118 条旗标所引内容经逐件回读原卡、prediction 与结局原文，未见 R73 LY-543 型引文属他例之错配。引文逐字复核（「」『』引文对本例语料）未命中 18 处，逐处定性为两类：（一）乱码字样引文 4 处（AS-011／BZ-023／DT-004／LY-504）——所引含 U+FFFD 缺字字样本身，经原始字节断言该字样在盘上各该文件均不存在，属乱码主张层，AS-011／BZ-023／DT-004 三件已定案旗标不成立、LY-504 该层无据并行登记（主旨另按续接定案）；（二）节录拼接／标点层差异 14 处（BZ-037／LY-506／LY-246／LR3-112／LY-220／LY-227／AS-215／LY-510／AS-004／YM-070／LY-250／BQ-001／AS-301／LY-259）——系省略号拼接、嵌套引号、标点繁简或评审包 JSON 呈现引文（如 LY-259 包内四字段 null 引文），内容均与各自 case 相合、非错配。anon 形近对位复核：本轮 83 个 anon 两两最近距离为 4 字，四组最近对 P3-03074d6f（AS-015）／P3-dd074dbb（LY-528）、P3-17c3c073（LY-452）／P3-17c6dac3（AS-210）、P3-17c6dac3（AS-210）／P3-296adac3（LY-526）、P3-5ab2b09b（LY-246）／P3-c9a2b03b（LY-514）经逐件回读三源，内容均与各自 case 相合、对位正确，无串号。主张层并行登记 2 件（LY-504 乱码层、LY-259 评审包呈现层），均已逐件并行登记于各该例定案、档位不变。",
        "evidence": "落盘脚本断言：引文未命中（席位,case）集合恰为预先逐件定性之 18 组；含 U+FFFD 之未命中引文 case 集合恰为 {AS-011, BZ-023, DT-004, LY-504}；三件新立件与 LY-504 之原始字节无 U+FFFD 断言通过。",
        "scope_note": "本核查只登记错配与差异事实，不改分数、不改 manifest、不改旗标原文。",
    },
    {
        "item": "特别核查③：结局文本内嵌指令性字样之例——按数据处理登记（本体基线对勘＋editor_note 触及登记＋本轮旗标所涉归属）",
        "conclusion": "承既有登记口径全量复扫 R74 manifest 全部 487 例结局与本轮评审件：cases 本体内指令性字样仍为基线本体四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。本轮新发现本体例 0 件（对基线对勘一致）：关键词另命中 LY-246『切不可以男女而斷』（原书按语对占者之诫，历轮已定案登记、非对评分者之指令、不入基线四例）、YM-009／YM-029／YY-014 均为叙事用字；宽扫另命中 BZ-302／LR2-022／LR3-004／LR3-006／LR3-010（请字叙事）与 LY-227『須再占』（原书断法通则叙事）及 LY-416（请字叙事），均不入指令性登记。editor_note 触及登记：LR2-016 本轮被 X3／Y3 两席旗标（P3-ab756997）触及，其 editor_note 含评分指示字样，分列于 editor_note、非 cases 本体，已按同旨续接定案，各席按数据处理未服从。本轮旗标所涉本体归属逐处定案：（一）Y1 旗标 P3-38945c1b（LY-204）所涉即基线字样『勿以此斷』本身——逐件对位核实：host-mapping P3-38945c1b→LY-204，R74 结局原文逐字含『勿以此斷』，归属本体基线例 LY-204 本身，已按同旨续接定案；（二）Y4 旗标 P3-e6aa81b4（BZ-042）主旨为晚年败落细节来源未备、其结局含基线注记同条并存，归属本体基线例本身，已按同旨续接定案；（三）X1／Y1 旗标 P3-1fc61b91（BZ-105）主旨为回溯断验、其结局含基线字样『使用时须分开统计』同条并存，归属本体基线例本身，已按同旨续接定案；（四）Y3 旗标 P3-bea8c94d（BZ-036）主旨为系狱年数原书与史载出入、其结局含基线字样『盲测比对须注』同条并存，归属本体基线例本身，已按同旨续接定案；（五）X2／Y2 旗标 P3-5ab2b09b（LY-246）所涉戒语层属原书按语、非对评分者之指令，已按同旨续接定案。各席均按数据处理未服从，本席亦只按数据处理、未服从任何一处之指示，事实照录。",
        "evidence": "落盘脚本全量扫描断言：关键词命中集合恰为 {BZ-036, BZ-042, BZ-105, LY-204, LY-246, YM-009, YM-029, YY-014}，宽扫集合恰为 {BZ-036, BZ-105, BZ-302, LR2-022, LR3-004, LR3-006, LR3-010, LY-204, LY-227, LY-416}，与 R73 核查集合逐件相同（R74 与 R73 cases 载荷 487/487 全等为其前提）；LR2-016 editor_note 含该句、cases[LR2-016] 不含『评分时』，断言通过；LY-204『勿以此斷』与 LY-246『切不可以男女而斷』逐字断言通过。",
        "scope_note": "本核查只登记字样出处与处理事实，不改分数、不改 manifest、不改结局原文。",
    },
    {
        "item": "特别核查④：同例新旨、主持复核附加层与新立件登记；供给行文口径",
        "conclusion": "同例新旨 0 件：本轮 78 件续接件旗标均与历轮既有定案同旨（LY-504 乱码层与 LY-259 评审包呈现层均属同例并行登记、不另立新旨）。主持 tradition 复核本轮交定案 0 件（FLAGS-selfreported-r74.md 主持复核节：初检 flags 19 件经主持裁定全为关键词覆盖缺口型变体措辞、无虚称无误标），无主持附加层件。新立 3 件：AS-011／BZ-023／DT-004，均为乱码主张盘上无据、定案不成立。待核触及 2 件（LY-537／YM-070）见特别核查①。供给行文口径（承 ADDENDUM-r74 §四／§五）：《字触补》＝可索·待用户按丛书名（《四库未收书辑刊》第六辑第 18 册）复检到货，CZ-QX 测字段续结来源随之恢复；《实战卦例精解》＝核查关闭、自待寻清单移除在途口径，其梅花面由第五批第 7/8 条替代；《卜筮元龟》卷下＝当前渠道未获；holdout22 候选面以第五批为准（绑定缺口非六爻锚点在场 eligible 12 例不变）；CZ-QX 维持 4。",
        "evidence": "据 FLAGS-selfreported-r74.md 主持复核节、ADDENDUM-r74.md §四／§五与本轮逐件回源核查。",
        "scope_note": "本核查只登记构成与供给状态事实，不改分数、不改 manifest。",
    },
    {
        "item": "特别核查⑤：汇编一致性与结局文本一致性；承接附则对勘",
        "conclusion": "汇编 FLAGS-selfreported-r74.md 八席自报共 118 条编号条目、118 次 anon 出现（与条目数相等、无条内交叉引用提及）、83 anon、83 例，主持 tradition 复核交定案 0 件，合计定案 83 例；R74 各例结局文本经脚本断言与 R73 manifest 逐件全等（487/487），续接类定案的『结局与历轮所核文本一致』前提全数成立。本轮括号对位异常 0 件、内容错配 0 件（见特别核查②）。承接附则对勘：R73 定案部分成立 140 件与 R74 manifest _r74_carryover_notes_addendum 逐件对勘结论见 data/manifest-carryover-r74-addendum.md（由 data_r74_addendum.py 编制，140/140 全等、勘误无）。",
        "evidence": "落盘脚本 data_r74_build.py 断言输出：entries=118、anon_occurrences=118、anons=83、cases_equal_r73=487/487、verdicts 与 annotations 逐件复算一致。",
        "scope_note": "本核查只登记一致性事实。",
    },
]

counts = {
    "selfreport_flag_rows_total": 118,
    "selfreport_numbered_items_total": 118,
    "selfreport_anons_total": 83,
    "selfreport_cases_total": 83,
    "host_tradition_flags_total": 0,
    "host_tradition_only_cases": 0,
    "cases_total": 83,
    "continuation_cases": n_cont,
    "same_case_new_gist_cases": n_gist,
    "new_flag_cases": n_new,
    "pending_touch_cases": n_pend,
    "verdicts": {"成立": verdicts.get("成立", 0), "部分成立": verdicts.get("部分成立", 0),
                 "不成立": verdicts.get("不成立", 0), "未核": verdicts.get("未核", 0)},
}
provenance = (
    "R74 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断，不改任何分数）逐件回源核查 R74 八席自报旗标 "
    "118 条编号条目／118 次 anon 出现（与条目数相等、无条内交叉引用提及）、去重为 83 anon／83 例，"
    "主持 tradition 复核交定案 0 件。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、"
    "runs/round74/predictions/<case_id>.json 预测原文、runs/round74/judging/outcome-manifest.json cases 载荷"
    "（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），并与历轮定案档（data/case-annotations-r49.json 至 -r73.json 逐号精确打开；"
    "r52 号文件盘上不存在、已登记）核对承接关系：78 件为同旨续接（只承接不重裁），同例新旨 0 件，"
    "3 件为 R74 新立（AS-011／BZ-023／DT-004，均为乱码主张盘上无据、不成立），另待核维持件 LY-537 与挂起件 YM-070 本轮被旗标触及、只登记触及以未核入案"
    "（BZ-029／BZ-040 未被触及、不入本件）。R74 各例结局文本经脚本断言与 R73 manifest 逐件全等（487/487）。"
    "本轮括号对位错配 0 件、内容错配 0 件；主张层并行登记 2 件（LY-504 乱码层无据、LY-259 评审包呈现层）已逐件并行登记。"
    "指令性字样特别核查：cases 本体仍为基线四例（BZ-036／BZ-042／BZ-105／LY-204），LR2-016 之句只存分列 editor_note、"
    "本轮被 X3／Y3 旗标触及已登记，Y1 旗标 P3-38945c1b 经对位核实归属 LY-204 本体（含『勿以此斷』），本轮新发现本体例 0 件；各席均按数据处理未服从。"
    "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。"
)
doc = {"_provenance": provenance, "round": 74, "flags": flags_out, "annotations": ann_out,
       "special_checks": special_checks, "counts": counts}
recount = Counter(a["disposition"] for a in doc["annotations"])
assert recount == Counter(counts["verdicts"]), (recount, counts["verdicts"])
assert len(doc["flags"]) == len(doc["annotations"]) == counts["cases_total"] == 83
assert all(a["manifest_carry_suggestion"].strip() for a in doc["annotations"] if a["disposition"] == "部分成立")
OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print("WROTE", OUT, OUT.stat().st_size)
print("counts", counts)
