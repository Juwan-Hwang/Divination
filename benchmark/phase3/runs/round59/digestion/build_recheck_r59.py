#!/usr/bin/env python3
"""R59 数据席补件构建：SUPPLY-RECHECK-why-partial-r59 (.md/.json) + SUPPLY-ACCOUNTING-r59.md
依据：两台账机械导出候选 41 例 + 本席对扫描源 PDF 的 150dpi 渲染逐页读图复核（49 印刷页 + p161）。
不打开任何 predictions/judging；不读已封存集金标正文（仅 id 集/台账字段）。
"""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
OUT = f"{BASE}/runs/round59/digestion"
r56 = json.load(open(f"{BASE}/runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json"))
r57 = json.load(open(f"{BASE}/runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json"))
r56map = {e["provisional_id"]: e for e in r56["entries"]}
r57map = {e["provisional_id"]: e for e in r57["entries"]}
net56 = set(r56["counts"]["net_eligible_A_low_present"])
net57 = set(r57["counts"]["net_eligible_A_low_present"])

# ---- 机械导出候选集 ----
cand57 = [e["provisional_id"] for e in r57["entries"]
          if e["anchor_presence"] != "present" or e["eligible_net"] is not True or not all(e["filters"].values())]
cand56 = [e["provisional_id"] for e in r56["entries"] if e["provisional_id"] not in net56]
assert len(cand57) == 10 and len(cand56) == 31, (len(cand57), len(cand56))

# ---- 本席逐例复核判词：id -> (锚点复核判, 阻断点, 依据与原文定位) ----
V = {
 # R56 partial+low
 "WHY-001": ("partial", "锚点不全（变卦爻列不可辨）",
   "印刷p10 卦盘放大复核：本卦六亲纳支/世应/六神略字可辨，变卦爻列被黑色斑驳带整列覆盖、不可辨，正文亦未载变卦名；变出爻列无原文实据，维持 partial。应验段（p11）为具体叙事，滤二 pass。"),
 "WHY-002": ("partial", "锚点不全（变卦爻列不可辨）",
   "印刷p11 卦盘：本卦全列可辨（螣蛇妻财子水应/勾陈兄弟戌土/朱雀子孙申金×/青龙官鬼卯木世/玄武父母巳火/白虎兄弟未土），但变卦爻列被黑带整列覆盖、不可辨；缺失点较原判收窄至变卦爻列，仍无原文实据可升 present，维持 partial。"),
 "WHY-029": ("partial", "锚点不全（动爻原书未载）",
   "印刷p57 卦盘六爻全列与台账转录逐行一致，但盘上无任何动爻标记（○/×皆无）、判断文亦未明言何爻动；动爻要素系原书未载而非扫描问题，维持 partial。应验「蛇没有出现」具体，滤二 pass。"),
 # R56 present+mid（锚点抽核在场，阻断为污染 mid）
 "WHY-013": ("present", "污染 mid（地震名案从严，承 R56 口径）",
   "印刷p29–30 卦盘全列在场（含六神略字与变卦列），p30 应验段逐项具体（地点/日期/震级）；台账 present 判属实。阻断仅在污染 mid，维持不可选。"),
 "WHY-014": ("present", "污染 mid（地震名案从严）",
   "印刷p31 卦盘全列在场，p31–32 应验具体（堪察加半岛 7.3 级等）；维持不可选，阻断为污染 mid。"),
 "WHY-017": ("present", "污染 mid（地震名案从严）",
   "印刷p35 卦盘在场，p36 应验具体；维持不可选，阻断为污染 mid。"),
 "WHY-018": ("present", "污染 mid（地震名案从严）",
   "印刷p36 卦盘在场，p37 应验（太原有感）具体；维持不可选，阻断为污染 mid。"),
 "WHY-019": ("present", "污染 mid（地震名案从严）",
   "印刷p37 卦盘在场，p38 应验（日本鹿儿岛 6.3 级等）具体；维持不可选，阻断为污染 mid。"),
 "WHY-020": ("present", "污染 mid（地震名案从严）",
   "印刷p38 卦盘在场，p40 应验具体；维持不可选，阻断为污染 mid。"),
 "WHY-045": ("present", "污染 mid（股票名案从严）",
   "印刷p145 卦盘在场（六神略字全列），应验载明 345→339 日元；维持不可选，阻断为污染 mid。"),
 "WHY-046": ("present", "污染 mid（股票名案从严）",
   "印刷p146 例三卦盘在场，应验 339→338 日元；维持不可选，阻断为污染 mid。"),
 "WHY-047": ("present", "污染 mid（股票名案从严）",
   "印刷p146 例四卦盘在场（含变卦列），p147 应验 338→335 日元；维持不可选，阻断为污染 mid。"),
 "WHY-048": ("present", "污染 mid（股票名案从严）；锚点口径疑点登记（见总注）",
   "印刷p147 例五卦盘本卦列在场，但六神列在本席 150dpi 渲染下未见印载，与股票章 partial 群同形态——原判 present 与 partial 群的划分口径不一致，登记待主持裁；本例阻断为污染 mid，锚点升降不影响可选结论，维持不可选。"),
 "WHY-049": ("present", "污染 mid（股票名案从严）；锚点口径疑点登记（见总注）",
   "印刷p148 例六卦盘与 WHY-048 同形态（六神列未见印载）；维持不可选，阻断为污染 mid，口径疑点并案登记。"),
 "WHY-052": ("present", "污染 mid（股票名案从严）；锚点口径疑点登记（见总注）",
   "印刷p149 例九卦盘与 partial 群同形态（六神列未见印载），p150 应验 335→327 日元；维持不可选，阻断为污染 mid，口径疑点并案登记。"),
 # R56 partial+mid（股票章：六神列原书未印载 + 污染 mid 双阻断）
 "WHY-050": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p148–149 例七卦盘：六亲纳支/世应全列，六神列原书未印载（股票章卦盘版式通例，非扫描辨认问题）；维持 partial。"),
 "WHY-051": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p149 例八卦盘同 WHY-050 形态；维持 partial。"),
 "WHY-053": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p150 例十：变卦名「震为雷」实载于正文题句（台账 anchor_missing 称变卦名一字未全辨，与原文不合，登记）；六神列未印载，维持 partial。"),
 "WHY-054": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p151 例十一卦盘六神列未印载；应验 312→307 日元具体；维持 partial。"),
 "WHY-055": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p151 例十二卦盘同上；p152 应验 1410→1408 日元；维持 partial。"),
 "WHY-056": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p152 例十三卦盘同上；p153 应验 1368→1399 日元；维持 partial。"),
 "WHY-057": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p152 例十四卦盘同上；p153 应验 1408→1368 日元；维持 partial。"),
 "WHY-058": ("partial", "锚点不全（六神列原书未印载）＋污染 mid；滤二成色薄",
   "印刷p153 例十五卦盘同上；结局仅「下跌五日元」无基价（台账登记属实），滤二薄 pass；维持 partial。"),
 "WHY-059": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p154 一周例一卦盘同上；p155 应验逐日数字具体；维持 partial。"),
 "WHY-060": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p155 一周例二卦盘同上；p156 应验逐日数字可辨（台账「两处数字辨认置信度中」不影响滤二 pass）；维持 partial。"),
 "WHY-061": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p156 一周例三卦盘同上；p157 应验逐日数字具体；维持 partial。"),
 "WHY-062": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p157 一周例四卦盘同上；p158 应验逐日数字具体；维持 partial。"),
 "WHY-063": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p158–159 买卖例一卦盘同上；结局为方向性记录（承台账 outcome_record，成色薄、滤二薄 pass）；维持 partial。"),
 "WHY-064": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p159 买卖例二卦盘同上；应验「从第二天开始股票出现下跌，一路走低」方向性记录；维持 partial。"),
 "WHY-065": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p160 买卖例三卦盘同上；结局实载价格（当日以 5.40 元卖出、此后下跌到 4 元多）——台账 anchor_missing 附注「结局为方向性记录」与原文不合，登记；维持 partial。"),
 "WHY-066": ("partial", "锚点不全（六神列原书未印载）＋污染 mid",
   "印刷p160 买卖例四卦盘同上；p161 应验载明甲申日以 6.6 元卖出获利、丙戌日后下跌不再升到 6 元以上，具体；维持 partial。"),
 # R57 二轮
 "WHY-076": ("present", "去重滤（跨书同案归属 GSZ-095）",
   "印刷p91–92 三键（戊寅年丙辰月丁亥日／地山谦变雷火丰／测夫妻缘分）与台账转录合，卦盘在场、应验具体、四滤全过属实；阻断仅为同案归属说真席（先完成转录者），维持只登记、不入 WHY 可选集。"),
 "WHY-077": ("present", "去重滤（跨书同案归属 GSZ-054）",
   "印刷p92–93 三键（丁丑年壬子月壬辰日／天泽履变天水讼／测妻怀孕）与台账转录合，卦盘在场、应验具体；维持只登记，归属 GSZ-054。"),
 "WHY-094": ("present", "去重滤（跨书同案归属 GSZ-106）",
   "印刷p127 三键（戊寅年丙辰月癸巳日／地天泰变水雷屯／86 岁老妇测流年）与台账转录合，卦盘在场、应验具体；维持只登记，归属 GSZ-106。"),
 "WHY-097": ("present", "去重滤（跨书同案归属 GSZ-053）",
   "印刷p167–168 三键（亥月丙寅日／风泽中孚变巽为风／测住房风水）与台账转录合，p168 应验具体；维持只登记，归属 GSZ-053。"),
 "WHY-101": ("present", "去重滤（跨书同案归属 GSZ-049）",
   "印刷p171–172 三键（亥月辛酉日／水地比变坤为地／测叔家风水）与台账转录合，应验具体；维持只登记，归属 GSZ-049。"),
 "WHY-102": ("partial", "锚点不全（月建日辰原书未载）",
   "印刷p172 例六题句仅「某男测店中风水得火天大有变离为火卦」，全例无月建日辰；卦盘本体（六神/世应/六亲纳支全列）在场，p173 应验具体。占时系原书未载、不许推定补锚，维持 partial——此为二轮 10 例中唯一锚点 partial 例。"),
 "WHY-105": ("present", "去重滤（跨书同案归属 GSZ-058）",
   "印刷p175–176 三键（未月庚辰日／风泽中孚变天水讼／焦炭厂测风水）与台账转录合，应验两段具体；维持只登记，归属 GSZ-058。"),
 "WHY-113": ("present", "去重滤（跨书同案归属 GSZ-029）",
   "印刷p196–197 三键（庚辰年甲申月丁酉日／泽天夬变泽火革／医院老妇测病）与台账转录合，p197 有事实复述段（浮肿消退、拔管出院）；维持只登记，归属 GSZ-029。"),
 "WHY-116": ("present", "去重滤（跨书同案归属 GSZ-011）；台账 asked_at 勘误登记",
   "印刷p200 例四题句实载「己卯年丁卯月甲子日」——台账 input_fields.asked_at 作「甲申日」系转录之误（台账 fail_reason 与 counts 三键作甲子日，与原文合），在此勘误登记、原台账不动；三键（甲子日／泽天夬变雷天大壮）与原文合，p201 应验具体；维持只登记，归属 GSZ-011。"),
 "WHY-117": ("present", "独立结局滤（滤二 fail）",
   "印刷p202 卦盘在场；p203 应验情况仅「以上推断果然应验」一句总括，无任何具体事实复述——滤二 fail 与台账判一致，维持只登记。此例阻断点与锚点无关。"),
}
assert set(V) == set(cand56) | set(cand57), (set(V) ^ (set(cand56) | set(cand57)))

entries = []
for cid in cand56:
    e = r56map[cid]
    a, blocker, basis = V[cid]
    entries.append({
        "id": cid, "round": "R56一轮", "ledger": "runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json",
        "source_location": e["source"],
        "original": {"anchor_presence": e["anchor_presence"], "anchor_missing": e.get("anchor_missing", ""),
                     "pollution": e["pollution"], "in_net_eligible_list": cid in net56,
                     "note": "R56 台账 JSON 无 filters/grade/eligible_net 字段；净入账口径为 counts.net_eligible_A_low_present（A 级＋low＋锚点 present），71 例均为四滤淘汰 33 例后的过筛入账例（承台账摘要）"},
        "recheck": {
            "filters": {"verbatim_transcribable": "pass（正文为印刷体，断语/结局段落可逐字转录；本席逐页读图核对）",
                        "independent_outcome": "pass（应验段独立成文且具体，逐例定位见 basis；WHY-058/063/064 为薄 pass，见 basis）" if cid != "WHY-117" else "fail",
                        "separable_prediction_outcome": "pass（原书〔判断〕与应验情况分段成文）",
                        "not_high_pollution": f"pass（{e['pollution']}，非 high）"},
            "anchor_presence": a, "pollution": e["pollution"],
            "verdict": "维持（不升格、不入可选集）", "blocker": blocker, "basis": basis},
    })
for cid in cand57:
    e = r57map[cid]
    a, blocker, basis = V[cid]
    entries.append({
        "id": cid, "round": "R57二轮", "ledger": "runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json",
        "source_location": e["source"],
        "original": {"anchor_presence": e["anchor_presence"], "anchor_missing": e.get("anchor_missing", ""),
                     "pollution": e["pollution"], "grade": e["grade"], "eligible_net": e["eligible_net"],
                     "filters": e["filters"], "fail_reason": e.get("fail_reason", "")},
        "recheck": {
            "filters": {"verbatim_transcribable": "pass", "independent_outcome": "fail（仅总括句，无具体事实复述）" if cid == "WHY-117" else "pass",
                        "separable_prediction_outcome": "pass", "not_high_pollution": "pass（low）"},
            "anchor_presence": a, "pollution": e["pollution"],
            "verdict": "维持（不升格、不入可选集）", "blocker": blocker, "basis": basis},
    })

doc = {
    "batch": "R59 数据席（补件）·WHY partial 面续采复核",
    "seat": "data (supplement, independent)",
    "candidate_derivation": {
        "rule": "anchor_presence≠present 或 eligible_net≠true 或 filters 未全 pass（三者取并集），自两台账 JSON 机械导出",
        "r57_r2": {"n": len(cand57), "ids": cand57,
                   "note": "二轮台账字段齐全（filters/grade/eligible_net），机械导出恰为 registered_only 10 例"},
        "r56_r1": {"n": len(cand56), "ids": cand56,
                   "note": "一轮台账 JSON 无 eligible_net/filters/grade 字段；以台账自身 counts.net_eligible_A_low_present（40 例）为净入账判据，非净入账 31 例＝锚点 partial 19＋锚点 present 但污染 mid 12"},
        "total": 41,
        "vs_predecessor_claim": "前任自报候选 19 例（二轮 10＋一轮 9）：二轮 10 与本席机械导出一致；一轮 9 在两台账中无任何口径可复现（一轮 partial 为 19、非净入账为 31，均非 9），差异登记于此，以本席机械导出 41 例为准",
    },
    "source_verification": {
        "file": "/home/hatch/workspace/divination/incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf",
        "finding": "盘上实测为扫描本（Pdg2Pic 制作、104 页、无文字层，pdftotext 输出为空），与两台账 provenance 登记「扫描本 transcription=visual」一致；派单所述「文字版 PDF/TXT」在该目录内未核到。复核方法：150dpi 渲染 32 个 PDF sheet（印刷页→PDF 页映射经 sheet6 实测：sheet N 含印刷 p(2N−2) 右、p(2N−1) 左）、逐页读图，覆盖全部 41 例所在 49 个印刷页＋p161（WHY-066 结局）",
        "render_script": "runs/round59/digestion/render_recheck_r59.py",
    },
    "summary": {
        "checked": 41, "upgraded_to_present": 0, "newly_eligible": 0,
        "anchor_partial_maintained": 20, "anchor_present_maintained": 21,
        "blocker_breakdown": {
            "跨书同案去重归属（GSZ 侧已入账）": 8, "污染 mid（地震/股票名案从严）": 28,
            "锚点不全·变卦爻列黑带覆盖": 2, "锚点不全·动爻原书未载": 1,
            "锚点不全·月建日辰原书未载": 1, "独立结局滤 fail": 1,
            "note": "计数按主阻断计：股票 partial 16 例兼具锚点不全与污染 mid，已计入污染 mid 之外另计——实际分布：partial+mid 16 例双阻断计入「污染 mid」行时该行为 28（12 present-mid＋16 partial-mid）；锚点不全单阻断为 001/002/029/102 共 4 例。两行合计 8+28+4+1=41"},
        "vs_predecessor_conclusion": "前任自报「19 例全部维持 partial、阻断为占时干支仅部分载录（15 例级）与占地未载」——与盘面不符之处：①候选集应为 41 例而非 19；②41 例中锚点 present 者 21 例（去重 8＋结局滤 1＋present-mid 12），并非「全部 partial」；③「占地」不在本链锚点定义（卦名/动爻/世应/六亲纳支/月建日辰）之内、两台账 anchor_missing 亦无此项；④「占时干支部分载录」仅 WHY-102 一例属占时缺失（全缺而非部分载录），余者缺失点为变卦爻列（2 例）、动爻标记（1 例）、六神列未印载（16 例）。本席结论：升格 0 例、新增可选 0 例——可选集增量与前任自报相同（0），但候选构成与阻断归因以本件为准",
        "anchor_standard_note": "口径疑点（提请主持裁，不自行改判）：台账 rules 所列锚点五要素（卦名、动爻、世应、六亲纳支、月建日辰）不含六神，但一轮对股票章 16 例以「六神列未辨出」判 partial；本席读图实测股票章卦盘版式本就未印六神列（非扫描辨认问题），且同章被判 present 的 WHY-045–049、052 卦盘同样未印六神列——原席对股票章的 present/partial 划分与六神列可见性并不一一对应。本席承链上既行口径（六神列缺失维持 partial）不擅改门槛；若主持改以五要素为准，股票 partial 16 例的锚点判将翻转（其污染 mid 仍阻断可选，故对可选集增量无影响，惟 WHY-001/002 的变卦爻列与 WHY-029 的动爻仍缺）",
        "ledger_errata": ["WHY-116 台账 input_fields.asked_at「甲申日」与原书题句「甲子日」不合（详见该例 basis），勘误登记、原台账未动",
                          "WHY-053 台账 anchor_missing「变卦名一字未全辨」与原文题句实载「震为雷」不合，登记",
                          "WHY-065 台账 anchor_missing 附注「结局为方向性记录」与原文实载价格（5.40 元卖出、跌至 4 元多）不合，登记"],
        "dedup_scope": "只对 id 集与三键（本变卦＋占月日＋问事）核对，未打开任何已封存集金标正文；未打开 runs/round59/predictions 或 judging 内容，judging 目录未列表；未做 git 操作",
    },
    "entries": entries,
}
with open(f"{OUT}/SUPPLY-RECHECK-why-partial-r59.json", "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)

# ---- MD ----
lines = []
lines.append("# SUPPLY-RECHECK-why-partial-r59 —— WHY partial 面续采复核（R59 数据席·补件）\n")
lines.append("- 复核席：数据席（补件，独立席位）。数据件：同目录 `SUPPLY-RECHECK-why-partial-r59.json`（逐例全字段）。")
lines.append("- 候选集机械导出：`anchor_presence≠present 或 eligible_net≠true 或 filters 未全 pass` 并集——R57 二轮台账（字段齐全）导出 **10 例**；R56 一轮台账 JSON 无 eligible_net/filters/grade 字段，以其 counts 净入账名单（40 例）为判据导出非净入账 **31 例**（锚点 partial 19＋present 但污染 mid 12）。合计 **n=41**。")
lines.append("- 与前任自报差异登记：前任称候选 19 例（一轮 9），一轮「9」在两台账中无口径可复现（partial 为 19、非净入账为 31），以本席机械导出为准。")
lines.append("- 源文本核对：派单称「分类占验技法文字版」，盘上实测 `incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf` 为**扫描本无文字层**（与台账 provenance 一致）；复核以 150dpi 渲染逐页读图行之，覆盖 41 例所在 49 个印刷页＋p161，渲染脚本 `render_recheck_r59.py`（同目录）。")
lines.append("")
lines.append("## 结论（n=41）")
lines.append("")
lines.append("- **升 present 0 例、新增可选 0 例。** 41 例全部维持不入可选集。")
lines.append("- 锚点复核：partial 维持 **20** 例（R56 partial 19＋WHY-102）；present 维持 **21** 例（present-mid 12＋去重 8＋WHY-117）。")
lines.append("- 阻断构成：跨书同案去重归属 8（076/077/094/097/101/105/113/116，GSZ 侧已入账）；污染 mid 28（地震 6＋股票 22，其中股票 partial 16 例兼锚点不全）；锚点单阻断 4（001 变卦爻列黑带、002 变卦爻列黑带、029 动爻原书未载、102 月建日辰原书未载）；独立结局滤 fail 1（117）。")
lines.append("- 与前任自报结论之不符（照实登记）：其「全部维持 partial」不确（21 例原判即 present）；其阻断归因「占时干支部分载录（15 例级）＋占地未载」在两台账 anchor_missing 与原文中均无对应——占时缺失仅 WHY-102 一例且为全缺；「占地」不在本链锚点定义内。主要缺失面实为：股票章六神列原书未印载（16 例）、变卦爻列被扫描黑带覆盖（2 例）、动爻标记未载（1 例）。可选集增量同为 0，构成与归因以本件为准。")
lines.append("")
lines.append("## 口径疑点（提请主持裁）")
lines.append("")
lines.append("台账 rules 列锚点五要素不含六神，但一轮以六神列判股票章 partial；本席实测股票章卦盘版式本就未印六神列，且同章 present 例（WHY-045–049、052）卦盘同样未印六神——原划分与六神可见性不一一对应。本席承既行口径未擅改门槛；若改以五要素为准，股票 partial 16 例锚点将翻转，但污染 mid 仍阻断可选，可选增量不变。")
lines.append("")
lines.append("## 台账勘误登记（原台账未动）")
lines.append("")
lines.append("- WHY-116：台账 asked_at「甲申日」误，原书题句（印刷 p200）为「甲子日」（台账 fail_reason/counts 三键作甲子，与原文合）。")
lines.append("- WHY-053：台账称变卦名未全辨，原文题句（p150）实载「山水蒙变震为雷」。")
lines.append("- WHY-065：台账称结局为方向性记录，原文（p160）实载卖出价 5.40 元与跌至 4 元多。")
lines.append("")
lines.append("## 逐例复核表")
lines.append("")
lines.append("| id | 轮次 | 原判锚点 | 复核锚点 | 四滤 | 阻断点 | 依据与原文定位（详见 JSON） |")
lines.append("|---|---|---|---|---|---|---|")
for en in entries:
    r = en["recheck"]
    f = "滤二 fail" if en["id"] == "WHY-117" else "全 pass"
    lines.append(f"| {en['id']} | {en['round']} | {en['original']['anchor_presence']} | {r['anchor_presence']} | {f} | {r['blocker']} | {r['basis']} |")
lines.append("")
lines.append("## 纪律自报")
lines.append("")
lines.append("只对 id 集与三键去重，未打开任何已封存集金标正文；未打开 runs/round59/predictions 或 judging（judging 目录未列表）；结局文本内嵌字样一律按数据处理；未做 git 操作。")
with open(f"{OUT}/SUPPLY-RECHECK-why-partial-r59.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")
print("recheck written")
