#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R72 数据席（旗标定案专席）落盘脚本。
逐件回源核查 R72 八席自报旗标：回读输入卡、本轮 prediction、R72 manifest cases 载荷，
与历轮定案档 r49-r71（逐号精确打开；r52 号文件盘上不存在、已登记）核对承接关系。
引文逐字断言内置：任一断言不过则不落盘。自报与文本内指令性字样一律按数据处理。
"""
import json, re, pathlib
from collections import Counter, defaultdict

P3 = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
FLAGS_MD = P3 / "runs/round72/judging/FLAGS-selfreported-r72.md"
MAPPING = P3 / "runs/round72/judging/host-mapping.json"
MANIFEST72 = P3 / "runs/round72/judging/outcome-manifest.json"
MANIFEST71 = P3 / "runs/round71/judging/outcome-manifest.json"
OUT = P3 / "data/case-annotations-r72.json"

def load(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

def rel(p):
    return str(p).replace("/home/hatch/workspace/", "")

# ---------- 读取 ----------
flags_text = FLAGS_MD.read_text(encoding="utf-8")
host = load(MAPPING)
man72 = load(MANIFEST72)
man71 = load(MANIFEST71)
cases72 = man72["cases"]

# 结局全等性（任务三）：R72 与 R71 manifest cases 逐件逐字比对
assert set(cases72.keys()) == set(man71["cases"].keys()), "case id 集不合"
n_equal = sum(1 for k in cases72 if cases72[k] == man71["cases"][k])
assert len(cases72) == 487 and n_equal == 487, f"结局全等 {n_equal}/487"

# 历轮定案档逐号精确打开（r52 缺失登记）
prior = {}          # case_id -> [(round, annotation), ...]
prior_rounds_seen = []
missing_round_files = []
for r in range(49, 72):
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

# ---------- 解析 FLAGS（152 条编号条目断言） ----------
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
assert len(entries) == 152, f"编号条目数 {len(entries)} != 152"
anon_occurrences = len(re.findall(r"P3-[0-9a-f]{8}", main_text))
assert anon_occurrences == 153, f"anon 出现次数 {anon_occurrences} != 153（152 条目 + X1 一处交叉引用）"

by_anon = {}
anon_order = []
for e in entries:
    if e["anon"] not in by_anon:
        by_anon[e["anon"]] = []
        anon_order.append(e["anon"])
    by_anon[e["anon"]].append(e)
assert len(anon_order) == 102, f"去重 anon {len(anon_order)} != 102"
case_ids = [host[a] for a in anon_order]
assert len(set(case_ids)) == 102, "anon->case 非一一对应"

# ---------- 分类 ----------
NEW_CASES = {"YM-049", "LY-405", "BQ-024", "LY-306", "LY-530", "AS-301",
             "YM-058", "ZY-004", "LY-335", "YM-045", "AS-205", "LY-418"}
NEW_GIST = {"LY-231", "YM-014", "LY-628", "LR3-107", "LY-620"}
PENDING = {"LY-537"}
for cid in NEW_CASES:
    assert cid not in prior, f"新立件 {cid} 竟有历轮条目"
for cid in NEW_GIST:
    assert cid in prior, f"新旨件 {cid} 无历轮条目"
assert "LY-537" in prior and prior["LY-537"][-1][1]["disposition"] == "未核"

# ---------- 引文断言工具 ----------
def corpus_of(cid):
    inp = load(P3 / f"inputs-dev12/{cid}.json")
    pred = load(P3 / f"runs/round72/predictions/{cid}.json")
    parts = [cases72[cid], pred["prediction_text"], pred.get("basis", ""),
             json.dumps(inp, ensure_ascii=False)]
    for layer in man72.values():
        if isinstance(layer, dict) and cid in layer and isinstance(layer[cid], str):
            parts.append(layer[cid])
    if cid in man72.get("stripped_tail", {}):
        parts.append(man72["stripped_tail"][cid])
    for (_r, a) in prior.get(cid, []):
        parts.append(a.get("flag") or "")
        parts.append(a.get("finding") or "")
    return "\n".join(parts)

def assert_quote(cid, quote, where="corpus"):
    if where == "outcome":
        src = cases72[cid]
    elif where == "prediction":
        src = load(P3 / f"runs/round72/predictions/{cid}.json")["prediction_text"]
    elif where == "basis":
        src = load(P3 / f"runs/round72/predictions/{cid}.json").get("basis", "")
    elif where == "input":
        src = json.dumps(load(P3 / f"inputs-dev12/{cid}.json"), ensure_ascii=False)
    else:
        src = corpus_of(cid)
    assert quote in src, f"引文断言失败 {cid} [{where}]: {quote[:60]}"

def assert_no_fffd(cid):
    raw = (P3 / f"runs/round72/predictions/{cid}.json").read_bytes()
    assert b"\xef\xbf\xbd" not in raw, f"{cid} prediction 原始文件竟含 U+FFFD"

# ---------- 新立 / 新旨 / 待核：逐件定案 ----------
CUSTOM = {}
CUSTOM["YM-049"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：回原卡——所问「占自身（自占病吉凶）」；R72 manifest 结局仅「是夕遂卒。」——自占病终局（是夕卒）明载、与问面直接对位；prediction 断「自病可愈（吉向，先危后安、险中得救）」与结局方向相反，属 prediction 与结局的评分落差，非题目—结局数据不对位（同 LY-627／YM-068 评分面口径）。故旗标不成立。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、方向相左属评分面登记）；结局原文照录不改。",
    quotes=[("input", "占自身（自占病吉凶）"), ("outcome", "是夕遂卒。"),
            ("prediction", "自病可愈（吉向，先危后安、险中得救）")])
CUSTOM["LY-405"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：回原卡——所问「占病」；R72 manifest 结局仅「果卒於丑月。」——病终局（丑月卒）明载、与问面直接对位；prediction 断「病可愈」与结局方向相反，属 prediction 与结局的评分落差，非题目—结局数据不对位（同 LY-627／YM-068 评分面口径）。故旗标不成立。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、方向相左属评分面登记）；结局原文照录不改。",
    quotes=[("input", "占病"), ("outcome", "果卒於丑月。"), ("prediction", "病可愈")])
CUSTOM["BQ-024"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：回原卡——所问「因鸡瘟卜（瘟中之鸡生死）」；R72 manifest 结局「果应不死，后因夜啼而妻病作」并自带转述句「鸡果不死」——鸡生死一面即问面本身、终局明载；prediction 断「多数将死于瘟」与结局方向相反，属 prediction 与结局的评分落差，非题目—结局数据不对位（同 YM-068 评分面口径）。故旗标不成立。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、方向相左属评分面登记）；结局原文照录不改。",
    quotes=[("input", "因鸡瘟卜（瘟中之鸡生死）"), ("outcome", "果应不死，后因夜啼而妻病作"),
            ("prediction", "多数将死于瘟")])
CUSTOM["LY-306"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：回原卡——所问「一人占弟死太湖，尸首可見否」；R72 manifest 结局「後至庚申日不見，直至丑月甲子旬內，壬申日尸首浮起得見」——尸首得见与否即问面本身、终局明载；prediction 将所问读作「行人可歸」（生还而归）与结局性质相反，属 prediction 对问面的读法与评分落差，非题目—结局数据不对位（同 YM-068 评分面口径）。故旗标不成立。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、方向相左属评分面登记）；结局原文照录不改。",
    quotes=[("input", "一人占弟死太湖，尸首可見否"), ("outcome", "壬申日尸首浮起得見"),
            ("prediction", "行人可歸")])
CUSTOM["LY-530"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：回原卡——所问「占家宅人口平安否」；R72 manifest 结局「一家数口回禄俱死」——家宅人口安否即问面本身、终局明载；prediction 断「家宅人口大體平安、有小驚無大害」与结局方向相反，属 prediction 与结局的评分落差，非题目—结局数据不对位（同 LY-627 评分面口径）。故旗标不成立。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、方向相左属评分面登记）；结局原文照录不改。",
    quotes=[("input", "占家宅人口平安否"), ("outcome", "一家数口回禄俱死"),
            ("prediction", "家宅人口大體平安、有小驚無大害")])
CUSTOM["AS-301"] = dict(
    verdict="部分成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：回原卡——所问「公开预测：2020年世界局势（逐月）」；R72 manifest 结局仅「2020年3月上旬新冠在欧美急剧扩散，世卫组织于2020年3月11日宣布大流行；3月8-9日前后全球市场与交通陷入混乱」一段——三月段明载可核；但 prediction 所断「下半年疫苗研发传来决定性好消息」与美国大选等下半年子断语在本结局中无任何对应记载，覆盖不全一层属实；结局亦非全无记载。故部分成立。",
    carry="同旨新立：自 R73 起承接本 R72 标注：按「结局仅载三月段、下半年疫苗与美国大选等子断语无对应记载」登记；结局原文照录不改。",
    quotes=[("input", "公开预测：2020年世界局势（逐月）"),
            ("outcome", "世卫组织于2020年3月11日宣布大流行"),
            ("prediction", "下半年疫苗研发传来决定性好消息"), ("prediction", "美国大选")])
CUSTOM["YM-058"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：乱码主张盘上无据——逐字回读 R72 prediction 原始文件，全文无 U+FFFD 替换字符（原始字节断言通过），旗标所引「未土戌月得月���（同土气）而旺」之乱码在盘上作「未土戌月得月扶（同土气）而旺」、文义完整。故旗标不成立（同 R71 YM-037／YM-048 乱码无据口径）。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。",
    quotes=[("prediction", "未土戌月得月扶（同土气）而旺")], no_fffd=True)
CUSTOM["ZY-004"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：乱码主张盘上无据——逐字回读 R72 prediction 原始文件，全文无 U+FFFD 替换字符（原始字节断言通过），旗标所引「卫国嗣位��元定」之乱码在盘上作「卫国嗣位以元定」、文义完整。故旗标不成立（同 R71 YM-037／YM-048 乱码无据口径）。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。",
    quotes=[("prediction", "卫国嗣位以元定")], no_fffd=True)
CUSTOM["YM-045"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：乱码主张盘上无据——逐字回读 R72 prediction 原始文件，全文无 U+FFFD 替换字符（原始字节断言通过），旗标所引「四爻官鬼壬��火应动化父母癸丑土」之乱码在盘上作「四爻官鬼壬午火应动化父母癸丑土」、文义完整。故旗标不成立（同 R71 YM-037／YM-048 乱码无据口径）。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。",
    quotes=[("prediction", "四爻官鬼壬午火应动化父母癸丑土")], no_fffd=True)
CUSTOM["AS-205"] = dict(
    verdict="不成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：乱码主张盘上无据——逐字回读 R72 prediction 原始文件，全文无 U+FFFD 替换字符（原始字节断言通过），旗标所引「月亮近南交点（龙尾）且在上升受克—���存活所需之光体与生命指示俱伤」之乱码在盘上文义完整（「存活所需之光体与生命指示俱伤」逐字在场）。故旗标不成立（同 R71 YM-037／YM-048 乱码无据口径）。",
    carry="新立定案：自 R73 起承接本 R72 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。",
    quotes=[("prediction", "月亮近南交点（龙尾）且在上升受克"), ("prediction", "存活所需之光体与生命指示俱伤")], no_fffd=True)
CUSTOM["LY-335"] = dict(
    verdict="部分成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：回原卡——所问「占廷师训子」、setting 明载「占延请教师训子可久否」；R72 prediction_text 首句仅作「所問之事可成：用神有氣、助力在，終局主成。」——泛指所问之事、未在 prediction_text 内指名廷师训子之具体断面，所指属实一层；但其 basis 已对回占题、结局「后至午月子水逄月破，其子病故，即辞师矣．」对可久否有明载对应（辞师即不久），数据本身无缺口。故部分成立。",
    carry="同旨新立：自 R73 起承接本 R72 标注：按「prediction_text 泛指所问之事、无具体断面，basis 已对回占题、结局对可久否有明载对应」登记；结局原文照录不改。",
    quotes=[("input", "占延请教师训子可久否"), ("prediction", "所問之事可成：用神有氣、助力在，終局主成。"),
            ("outcome", "后至午月子水逄月破，其子病故，即辞师矣．")])
CUSTOM["LY-418"] = dict(
    verdict="部分成立", relation="新旗标（R72 新立）",
    finding="新旗标（R72 新立）：回原卡——所问「占求財」；R72 manifest 结局仅「卻得於辰土出空之日﹐」以逗号收尾——疑似截断之表面属实；但得财时点（辰土出空之日）已明载，盘内无据裁定尚有缺失后文。故部分成立（同 LY-416／LY-540 逗号收尾口径）。",
    carry="同旨新立：自 R73 起承接本 R72 标注：按「结局以逗号收尾、疑似截断，得财时点明载」登记；结局原文照录不改。",
    quotes=[("input", "占求財"), ("outcome", "卻得於辰土出空之日﹐")])
CUSTOM["LY-231"] = dict(
    verdict="不成立", relation="同例新旨（R61 旧旨为『prediction 正文与终局单判自相矛盾』、定案成立，本轮新旨与之各旨独立）",
    finding="同例新旨（R61 旧旨为『prediction 正文与终局单判自相矛盾』、定案成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「占在任平安否（流年）」；R72 manifest 结局「果於八月丁艱。」——流年内丁艰明载、与问面直接对位；prediction 断「在任流年平安為主，無大災」与结局方向相反，属 prediction 与结局的评分落差，非题目—结局数据不对位（同 LY-627 评分面口径）。故本轮新旨不成立。",
    carry="同例新旨：自 R73 起承接本 R72 标注：按「丁艰明载、方向相左属评分面，本轮新旨不成立」登记；结局原文照录不改。",
    quotes=[("input", "占在任平安否（流年）"), ("outcome", "果於八月丁艱。"),
            ("prediction", "在任流年平安為主，無大災")])
CUSTOM["YM-014"] = dict(
    verdict="不成立", relation="同例新旨（R65 旧旨为『结局尾句为应验解释层并载』、定案部分成立，本轮新旨与之各旨独立）",
    finding="同例新旨（R65 旧旨为『结局尾句为应验解释层并载』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「占家宅（火灾之虞）」；R72 manifest 结局「至甲午日而回禄，以夏至后先壬而后甲也。」——回禄成灾即家宅火灾问面本身、终局明载；prediction 断「家宅不至发生火灾成灾」与结局方向相反，属 prediction 与结局的评分落差，非题目—结局数据不对位（同 LY-627 评分面口径）。故本轮新旨不成立。",
    carry="同例新旨：自 R73 起承接本 R72 标注：按「回禄明载、方向相左属评分面，本轮新旨不成立」登记；结局原文照录不改。",
    quotes=[("input", "占家宅（火灾之虞）"), ("outcome", "至甲午日而回禄，以夏至后先壬而后甲也。"),
            ("prediction", "家宅不至发生火灾成灾")])
CUSTOM["LY-628"] = dict(
    verdict="部分成立", relation="同例新旨（R69 旧旨为『prediction 含「?」占位字样』、定案部分成立，本轮新旨与之各旨独立）",
    finding="同例新旨（R69 旧旨为『prediction 含「?」占位字样』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：回原卡——所问「占訟事」；R72 manifest 结局仅「果被杖責，此應日克月破故耳．」——杖责事件明载，但受杖责主体（占者抑或对方）未以明字分载，胜负方向读法受此影响，所指含混一层属实；结局亦非他事。故部分成立（同 LR2-022 终句主语未明口径）。",
    carry="同例新旨：自 R73 起承接本 R72 标注：按「结局受杖责主体未明字、胜负方向读法受影响」登记；结局原文照录不改。",
    quotes=[("input", "占訟事"), ("outcome", "果被杖責，此應日克月破故耳．")])
CUSTOM["LR3-107"] = dict(
    verdict="部分成立", relation="同例新旨（R54／R57 旧旨为『结局与何等样人／吉凶问面对位疑』、定案不成立，本轮新旨与之各旨独立）",
    finding="同例新旨（R54／R57 旧旨为『结局与何等样人／吉凶问面对位疑』、定案不成立，本轮新旨与之各旨独立、并行不悖）：回原卡——卡面 attachments 课式条自注「退茹（原书课体首字作「鬼」，疑残泐[存疑]）」，课式名字残泐存疑在卡面已注；R72 prediction 亦自载「课式名字残泐存疑卡面已注，置信降档。」——残损一层属实，但已在卡面与 prediction 双处明示。故部分成立（同 LR3-116 残损双示口径）。",
    carry="同例新旨：自 R73 起承接本 R72 标注：按「卡面课式名字残泐存疑、已于卡面与 prediction 双示」登记；结局原文照录不改。",
    quotes=[("input", "疑残泐[存疑]"), ("prediction", "课式名字残泐存疑卡面已注，置信降档。")])
CUSTOM["LY-620"] = dict(
    verdict="部分成立", relation="同例新旨（R54／R57／R58／R60 旧旨为『结局断面偏移疑』、定案不成立，本轮新旨与之各旨独立）",
    finding="同例新旨（R54／R57／R58／R60 旧旨为『结局断面偏移疑』、定案不成立，本轮新旨与之各旨独立、并行不悖）：回原卡——卡面 chart_note 自注「原文僅記月日與卦名、未列逐爻裝卦表」，notes 载逐爻与动爻为推算复原；R72 prediction 自注「卡面明言原文未列逐爻裝卦表、動爻為復原」并降置信——盘面为复原件一层属实，但残损状态已在卡面明载、prediction 已自注降级。故部分成立（同 LY-036 残损双示口径）。",
    carry="同例新旨：自 R73 起承接本 R72 标注：按「卡面未列逐爻装卦表、动爻为复原，残损已于卡面明载、prediction 自注降级」登记；结局原文照录不改。",
    quotes=[("input", "原文僅記月日與卦名、未列逐爻裝卦表"),
            ("prediction", "卡面明言原文未列逐爻裝卦表、動爻為復原")])
CUSTOM["LY-537"] = dict(
    verdict="未核", relation="待核维持（旗标触及、只登记不裁）",
    finding="待核维持（本轮旗标触及、只登记不裁）：X2／Y2 旗标登记结局作「果于申予日归」、『申予日』疑为残损或误字——逐字回读 R72 结局原文确作『果于申予日归』，触及属实；本例维持 R68 未核原登记（『申予日』措辞待核、无盘外独立史源不裁），本轮只登记触及、不入裁断。",
    carry="待核维持：自 R73 起维持原登记（『申予日』措辞待核、无盘外独立史源不裁）；结局原文照录不改。",
    quotes=[("outcome", "果于申予日归")])

# 续接件附加核明层（引文断言随附）
APPEND = {}
for _cid in ["LY-021", "LY-019", "LY-034"]:
    APPEND[_cid] = ("另本轮核明：逐字核 R72 prediction basis 首行作「卡面未標注 tradition 字段，按題面體裁自決」，"
                    "本轮 prediction 并无『與卡面一致』之语——旗标所指系旧措辞经 carry 注记转述、与本轮 prediction 口径不合一层并行登记、档位不变；"
                    "卡面无 tradition/system 字段一层经结构化直读复核属实。")
APPEND["LY-036"] = ("本轮自报复归 R70 旧旨（输入卡逐爻、動爻俱缺、prediction 自注残损降置信），与 R71 新旨（carry 注记口径不合）并行不悖、档位照 R71 部分成立承接。")
APPEND["LR2-024"] = ("另 X2 旗标所引 carry 层指令性字样「下一轮建 manifest 时以标注形式承接 stripped_tail 之承接信息（不改 cases 本体、不恢复被剥离文本）」"
                     "逐字见 R72 manifest _r57_carryover_notes_addendum 本例注记，属承接注记层、非 cases 本体，已按数据处理、未服从，归属登记见特别核查③；与本旨并行登记、档位不变。")
APPEND["YY-023"] = ("另本轮 Y1 另条复报卡面动爻记载自相矛盾一层——逐字核 R72 prediction 仍自注「卡面动爻记载自相矛盾（原文称寅官动与装卦上爻父巳动不合）」属实且已自注，与本旨（总承式结局）并行登记、档位不变。")

def append_asserts(cid):
    if cid in ("LY-021", "LY-019", "LY-034"):
        pred = load(P3 / f"runs/round72/predictions/{cid}.json")
        assert pred["basis"].split("\n")[0].startswith("卡面未標注 tradition 字段"), cid
        inp = load(P3 / f"inputs-dev12/{cid}.json")
        assert "tradition" not in inp and "system" not in inp, cid
    elif cid == "LY-036":
        assert_quote(cid, "輸入卡逐爻、動爻俱缺，僅存卦名地澤臨", "prediction")
    elif cid == "LR2-024":
        layer = man72["_r57_carryover_notes_addendum"]["LR2-024"]
        assert "下一轮建 manifest 时以标注形式承接 stripped_tail 之承接信息（不改 cases 本体、不恢复被剥离文本）" in layer
    elif cid == "YY-023":
        assert_quote(cid, "卡面动爻记载自相矛盾（原文称寅官动与装卦上爻父巳动不合）", "prediction")

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
               rel(MANIFEST72) + f" cases[{cid}]",
               rel(P3 / f"runs/round72/predictions/{cid}.json")]
    for (r, _a) in prior.get(cid, []):
        sources.append(rel(P3 / f"data/case-annotations-r{r}.json") + f" {cid} 条")
    if cid in CUSTOM:
        c = CUSTOM[cid]
        verdict, finding, relation, carry = c["verdict"], c["finding"], c["relation"], c["carry"]
        for (where, q) in c["quotes"]:
            assert_quote(cid, q, where)
        if c.get("no_fffd"):
            assert_no_fffd(cid)
        category = "待核维持（详见核查事实）" if cid in PENDING else (
            "同例新旨（详见核查事实）" if cid in NEW_GIST else "新旗标（详见核查事实）")
    else:
        hist = prior[cid]
        lr, la = hist[-1]
        verdict = la["disposition"]
        finding = f"承接既有定案不重裁（历轮最近定案 R{lr} {verdict}）：" + (la.get("finding") or "")
        if cid in APPEND:
            append_asserts(cid)
            finding += " " + APPEND[cid]
        finding += " 本轮（R72）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。"
        relation = f"同旨续接（R{lr}）"
        carry = f"同旨续接：自 R73 起承接 R{lr}＋本 R72 标注；结局原文照录不改。"
        category = "同旨续接（详见核查事实）"
    if verdict == "部分成立":
        assert carry.strip(), f"{cid} 部分成立件 carry 为空"
    flags_out.append({
        "anon_id": anon, "case_id": cid, "verdict": verdict, "disposition": verdict,
        "basis": finding, "carry_suggestion": carry, "manifest_carry_suggestion": carry,
        "flag": flag_summary, "category": category, "views": views,
        "dual_view": len(views) > 1, "relation": relation, "registered_round": 72,
        "sources_checked": sources})
    ann_out.append({
        "anon_id": anon, "case_id": cid, "disposition": verdict, "finding": finding,
        "flag": flag_summary, "manifest_carry_suggestion": carry, "relation": relation,
        "registered_round": 72, "sources_checked": sources, "source_seats": seats})

verdicts = Counter(a["disposition"] for a in ann_out)
assert sum(verdicts.values()) == 102
n_cont = sum(1 for a in ann_out if a["relation"].startswith("同旨续接"))
n_gist = sum(1 for a in ann_out if a["relation"].startswith("同例新旨"))
n_new = sum(1 for a in ann_out if a["relation"].startswith("新旗标"))
n_pend = sum(1 for a in ann_out if a["relation"].startswith("待核维持"))
assert (n_cont, n_gist, n_new, n_pend) == (84, 5, 12, 1), (n_cont, n_gist, n_new, n_pend)
seat_case_counts = Counter()
for anon in anon_order:
    ss = set(e["seat"] for e in by_anon[anon])
    seat_case_counts[len(ss)] += 1

# ---------- 特别核查③：指令性字样复扫 ----------
kws = ["请按", "须注", "須注", "评分时", "評分時", "比对时", "比對時", "使用时须", "使用時須",
       "分开统计", "分開統計", "勿以此斷", "不可以", "不得"]
kw_hits = sorted(cid for cid, t in cases72.items() if any(k in t for k in kws))
assert kw_hits == ["BZ-036", "BZ-042", "BZ-105", "LY-204", "LY-246", "YM-009", "YM-029", "YY-014"], kw_hits
wide_hits = sorted(cid for cid, t in cases72.items() if any(c in t for c in ["请", "請", "须", "須", "勿"]))
assert wide_hits == ["BZ-036", "BZ-105", "BZ-302", "LR2-022", "LR3-004", "LR3-006", "LR3-010", "LY-204", "LY-227", "LY-416"], wide_hits
assert "评分时" not in cases72["LR2-016"]
assert "评分时该细项请按未完全复核处理" in man72["_r56_lr2016_split"]["editor_note"]
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
assert fail_keys == [("X1", "YY-023"), ("X3", "AS-210"), ("Y1", "YY2-004"), ("Y3", "AS-205"),
                     ("Y3", "LR2-023"), ("Y3", "LY-335"), ("Y3", "YM-045"), ("Y3", "YM-058"),
                     ("Y3", "ZY-004"), ("Y4", "BZ-304")], fail_keys

special_checks = [
    {
        "item": "特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记",
        "conclusion": "LY-537 本轮被旗标触及（X2／Y2 两条同旨：结局「果于申予日归」之『申予日』疑残损或误字），依任务口径只登记触及、维持 R68 未核原登记、不入裁断，以未核入本轮 annotations。BZ-029／BZ-040／YM-070 本轮未被任何旗标触及，不入 annotations、维持各自原登记（BZ-029 维持 R55 卒年待核（未核）；BZ-040 维持 R55 原登记（许世英享年异说待盘外独立史源）；YM-070 维持既有未核原登记）。",
        "evidence": "据 runs/round72/judging/host-mapping.json 与 FLAGS-selfreported-r72.md 逐件比对：102 件 case_id 集合含 LY-537（anon P3-720d8523）、不含 BZ-029／BZ-040／YM-070（落盘脚本断言通过）；LY-537 结局原文逐字断言（「果于申予日归」）通过。",
        "scope_note": "本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。",
    },
    {
        "item": "特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）",
        "conclusion": "括号对位错配 0 件、内容错配 0 件：本轮旗标正文内出现的 case_id 字样仅 LY-024 两处，均系 LY-023 例结局原文内交叉引用（「其後復占子病，見 LY-024」），host-mapping 对 LY-023（P3-d808d916）对位正确，非串号。引文逐字复核有 10 处未在盘上原文逐字命中，逐件定性如下：（一）繁简／字形转写 3 件——YY-023 之 X1 引「後果然。」（盘上作「后果然。」）、LR2-023 之 Y3 引「後果然（兒婦妊性别如斷）」（盘上作「后果然（儿妇妊性别如断）」）、LY-335 之 Y3 引「後至午月……即辞师矣」（盘上作「后至午月……即辞师矣」），均同例同句、仅字形转写，非内容错配；（二）引号体例转写 1 件——BZ-304 之 Y4 引「与『5-6月恢复正常』相反」，盘上原文作「与「5-6月恢复正常」相反」，内层引文逐字在场；（三）释义性标签 2 件——AS-210 之 X3「得官职/晋升」、YY2-004 之 Y1「预测断语本身无应期」均为评审自拟概括语、非自称逐字引文；（四）乱码主张 4 件（YM-058／ZY-004／YM-045／AS-205）——盘上 prediction 原始文件均无 U+FFFD、对应文句文义完整，已逐件定案不成立。另 anon 出现次数 153 中有 1 次为 X1 旗标 P3-249b0a4b 条内对 P3-20e3d6d7 的交叉引用提及，非独立条目，已在 counts 中分列。主张层口径不合 3 件（LY-019／LY-021／LY-034 tradition 措辞）：R72 prediction basis 首行均作「卡面未標注 tradition 字段，按題面體裁自決」，旗标所指『與卡面一致』系旧措辞经 carry 注记转述，已逐件并行登记于各该例定案、档位不变；卡面无 tradition/system 字段一层经结构化直读复核属实。其余各件旗标引文经逐件回读本例 R72 结局原文／prediction 原文／卡面／承接层核对均在本例内（引文逐字断言内置于落盘脚本）。",
        "evidence": "落盘脚本断言：引文未命中清单恰为上述 10 处（座位×case 集合断言通过）；LY-023 结局交叉引用逐字断言、TRAD3 三例卡面无 tradition/system 键与 basis 首行断言、四件乱码例 prediction 原始字节无 U+FFFD 断言均通过。",
        "scope_note": "本核查只登记错配与不合事实，不改分数、不改 manifest、不改旗标原文。",
    },
    {
        "item": "特别核查③：结局文本内嵌指令性字样之例——按数据处理登记（本体基线对勘＋本轮旗标所涉与新发现归属）",
        "conclusion": "承既有登记口径全量复扫 R72 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计／勿以此斷等，并以『请／請／须／須／勿』宽扫人工甄别）：cases 本体内指令性字样仍为基线本体四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。本轮新发现本体例 0 件：关键词另命中 LY-246『切不可以男女而斷』（原书按语对占者之诫，R69 已定案登记、非对评分者之指令、不入基线四例）、YM-009『反不得』／YM-029『本岁不得』／YY-014『求之不得』均为叙事用字；宽扫另命中 BZ-302／LR2-022／LR3-004／LR3-006／LR3-010（请字叙事）与 LY-227『須再占』（原书断法通则叙事）及 LY-416（请字叙事），均不入指令性登记。本轮旗标所涉归属逐处定案：（一）X1／Y1 旗标 P3-09567035（BZ-105）主旨为回溯断验、其结局含基线字样『使用时须分开统计』同条并存，归属本体基线例本身，已按同旨续接定案；（二）Y4 旗标 P3-f8ad6b33（LY-204）所涉即基线字样『勿以此斷』本身，归属本体基线例本身，已按同旨续接定案；（三）X3／Y3 旗标 P3-9746bb89（LR2-016）所引 editor_note 句分列于 editor_note 及承接注记层、非 cases 本体，已按同旨续接定案；（四）X2 旗标 P3-3aa0e904（LR2-024）所引『下一轮建 manifest 时以标注形式承接……』逐字见 manifest _r57_carryover_notes_addendum 本例承接注记，属承接注记层、非 cases 本体，已并行登记于该例定案。BZ-036／BZ-042 本轮未被旗标触及、基线登记照旧。各席均按数据处理未服从，本席亦只按数据处理、未服从任何一处之指示，事实照录。",
        "evidence": "落盘脚本全量扫描断言：关键词命中集合恰为 {BZ-036, BZ-042, BZ-105, LY-204, LY-246, YM-009, YM-029, YY-014}，宽扫集合恰为 {BZ-036, BZ-105, BZ-302, LR2-022, LR3-004, LR3-006, LR3-010, LY-204, LY-227, LY-416}，与 R71 核查集合逐件相同（R72 与 R71 cases 载荷 487/487 全等为其前提）；LR2-016 editor_note 含该句、cases[LR2-016] 不含『评分时』，断言通过。",
        "scope_note": "本核查只登记字样出处与处理事实，不改分数、不改 manifest、不改结局原文。",
    },
    {
        "item": "特别核查④：同例新旨、主持复核附加层与新立件登记",
        "conclusion": "同例新旨 5 件：LY-231（方向相左属评分面、新旨不成立；R61 旧旨 prediction 自相矛盾定案成立并行不悖）、YM-014（方向相左属评分面、新旨不成立；R65 旧旨解释层并载定案部分成立并行不悖）、LY-628（结局受杖责主体未明字、新旨部分成立）、LR3-107（卡面课式名字残泐存疑双示、新旨部分成立）、LY-620（卡面未列逐爻表、动爻为复原、新旨部分成立）。主持 tradition 复核本轮无旗标交定案（FREEZE-r72 §二：初检 flags 0 件、措辞不实型旗标连续第二轮归零），无主持附加层件。新立 12 件：AS-301（结局仅载三月段、覆盖不全，部分成立）、LY-335（prediction_text 泛指无具体断面，部分成立）、LY-418（结局逗号收尾疑截断、得财时点明载，部分成立）、YM-049／LY-405／BQ-024／LY-306／LY-530（结局明载问面终局、所指仅为 prediction 方向相左属评分面，不成立）、YM-058／ZY-004／YM-045／AS-205（乱码主张盘上无据，不成立）。待核触及 1 件（LY-537）见特别核查①。另登记：历轮定案档逐号精确打开时 r52 号文件盘上不存在（r49-r51、r53-r71 均在），承接核对以盘上实存各号为准、该缺失已在本件 _provenance 与本项登记，不影响本轮 102 件承接判定（各件最近定案均出自实存号）。",
        "evidence": "据 FLAGS-selfreported-r72.md 主持复核节、data/case-annotations-r61.json LY-231 条、-r65.json YM-014 条、-r69.json LY-628 条、-r54/-r57.json LR3-107 条、-r54/-r60.json LY-620 条与本轮逐件回源核查；r52 缺失由落盘脚本逐号打开断言记录（missing_round_files == [52]）。",
        "scope_note": "本核查只登记构成事实，不改分数、不改 manifest。",
    },
    {
        "item": "特别核查⑤：汇编一致性与结局文本一致性",
        "conclusion": "汇编 FLAGS-selfreported-r72.md 八席自报共 152 条编号条目、153 次 anon 出现（含 X1 条内交叉引用提及 1 次）、102 anon、102 例（单席 53 例、双席 49 例；X 侧独有 14 例、Y 侧独有 39 例、双侧同报 49 例），主持 tradition 复核交定案 0 件，合计定案 102 例；R72 各例结局文本经脚本断言与 R71 manifest 逐件全等（487/487），续接类定案的『结局与历轮所核文本一致』前提全数成立。本轮括号对位异常 0 件、内容错配 0 件（见特别核查②）。承接附则对勘：R71 定案部分成立 83 件与 R72 manifest _r72_carryover_notes_addendum 逐件对勘结论见 data/manifest-carryover-r72-addendum.md（由 data_r72_addendum.py 编制）。",
        "evidence": "落盘脚本 data_r72_build.py 断言输出：entries=152、anon_occurrences=153、anons=102、cases_equal_r71=487/487、verdicts 与 annotations 逐件复算一致。",
        "scope_note": "本核查只登记一致性事实。",
    },
]

counts = {
    "selfreport_flag_rows_total": 152,
    "selfreport_numbered_items_total": 152,
    "selfreport_anons_total": 102,
    "selfreport_cases_total": 102,
    "host_tradition_flags_total": 0,
    "host_tradition_only_cases": 0,
    "cases_total": 102,
    "continuation_cases": n_cont,
    "same_case_new_gist_cases": n_gist,
    "new_flag_cases": n_new,
    "pending_touch_cases": n_pend,
    "verdicts": {"成立": verdicts.get("成立", 0), "部分成立": verdicts.get("部分成立", 0),
                 "不成立": verdicts.get("不成立", 0), "未核": verdicts.get("未核", 0)},
}
provenance = (
    "R72 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断，不改任何分数）逐件回源核查 R72 八席自报旗标 "
    "152 条编号条目／153 次 anon 出现（含 X1 旗标 P3-249b0a4b 条内对 P3-20e3d6d7 的交叉引用提及 1 次）、去重为 102 anon／102 例，"
    "主持 tradition 复核本轮无旗标交定案。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、"
    "runs/round72/predictions/<case_id>.json 预测原文、runs/round72/judging/outcome-manifest.json cases 载荷"
    "（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），并与历轮定案档（data/case-annotations-r49.json 至 -r71.json 逐号精确打开；"
    "r52 号文件盘上不存在、已登记）核对承接关系：84 件为同旨续接（只承接不重裁），5 件为同例新旨"
    "（LY-231／YM-014 方向相左属评分面不成立；LY-628 结局主体未明、LR3-107 课式残泐双示、LY-620 盘面复原双示均部分成立），"
    "12 件为 R72 新立（AS-301／LY-335／LY-418 部分成立；YM-049／LY-405／BQ-024／LY-306／LY-530 方向相左属评分面不成立；"
    "YM-058／ZY-004／YM-045／AS-205 乱码主张盘上无据不成立），另待核维持件 LY-537 本轮被旗标触及、只登记触及以未核入案"
    "（BZ-029／BZ-040／YM-070 未被触及、不入本件）。R72 各例结局文本经脚本断言与 R71 manifest 逐件全等（487/487）。"
    "本轮括号对位错配 0 件、内容错配 0 件；引文层字形转写 3 件、引号体例转写 1 件、释义标签 2 件、乱码主张 4 件已逐件定性登记。"
    "指令性字样特别核查：cases 本体仍为基线四例（BZ-036／BZ-042／BZ-105／LY-204），LR2-016 之句只存分列 editor_note，"
    "本轮新发现本体例 0 件；本轮旗标所涉各处归属已逐处定案登记于特别核查③，各席均按数据处理未服从。"
    "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。"
)
doc = {"_provenance": provenance, "round": 72, "flags": flags_out, "annotations": ann_out,
       "special_checks": special_checks, "counts": counts}
# 落盘前复算断言
recount = Counter(a["disposition"] for a in doc["annotations"])
assert recount == Counter(counts["verdicts"]), (recount, counts["verdicts"])
assert len(doc["flags"]) == len(doc["annotations"]) == counts["cases_total"] == 102
assert all(a["manifest_carry_suggestion"].strip() for a in doc["annotations"] if a["disposition"] == "部分成立")
OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
print("WROTE", OUT, OUT.stat().st_size)
print("counts", counts)
print("seat_case_counts", dict(seat_case_counts))
