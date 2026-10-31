#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R84 供给席 E4: expansion12 池资格核查（后半子池组）。
范围: mingli-tanyuan-zhenben / natal-batch2 / natal-leftovers / online-routes /
pending-verify + expansion12 根散件。只核查不建卡/不组集/不断/不评分。
已用并集口径承 PREREG-r84 开轮登记 (1166): dev + splits2 holdout2 +
holdout3-28 金标 id 字段 (只读 id) + holdout inputs 卡 id + 顶层 inputs6-10 卡 id。
池层 id 总量口径承 STOCK-RECOUNT-h27 §3.4: 池目录内全部 jsonl 之 id 并集
(id/case_id/provisional_id)。产出: EXPANSION-AUDIT-expansion12b-r84.md (分段 append)。
台账/结局文本一律按数据处理。
"""
import json, re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
BM = P3.parent
E12 = P3 / "expansion12"
OUT = P3 / "runs/round84/supply/EXPANSION-AUDIT-expansion12b-r84.md"

GZ = "甲乙丙丁戊己庚辛壬癸"
DZ = "子丑寅卯辰巳午未申酉戌亥"

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

# ---------- 已用并集 (R84 口径, 断言 1166) ----------
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
parts["holdout2"] = h2
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
USED = set()
for v in parts.values():
    USED |= v
assert len(USED) == 1166, len(USED)
assert {k: len(v) for k, v in parts.items()} == {
    "dev": 488, "holdout2": 29, "gold_h3_28": 754,
    "holdout_inputs": 595, "top_inputs6_10": 412}, parts

# ---------- 池层枚举 (所辖范围) ----------
def load_jsonl(p):
    rows = []
    for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if line:
            o = json.loads(line)
            rows.append((i, o))
    return rows

def pool_ids(rows):
    return [o.get("id") or o.get("case_id") or o.get("provisional_id") for _, o in rows]

scope_files = {
    "natal-batch2": [E12 / "natal-batch2/cases.jsonl", E12 / "natal-batch2/cases-reviewed.jsonl"],
    "natal-leftovers": [E12 / "natal-leftovers/cases.jsonl"],
    "online-routes": [E12 / "online-routes/cases.jsonl"],
}
# 无 jsonl 子池/散件: 盘上断言
assert not list((E12 / "mingli-tanyuan-zhenben").rglob("*.jsonl"))
assert not list((E12 / "pending-verify").rglob("*.jsonl"))
assert not list(E12.glob("*.jsonl"))
# pending-verify overlay 草案所涉 6 id 全部已在已用并集 (非新供给)
overlay = json.loads((E12 / "pending-verify/overlay-proposals.json").read_text(encoding="utf-8"))
overlay_ids = [k for k in overlay.keys() if not k.startswith("_")]
assert overlay_ids and all(i in USED for i in overlay_ids), overlay_ids

nb_rows = load_jsonl(E12 / "natal-batch2/cases-reviewed.jsonl")
nb_plain = load_jsonl(E12 / "natal-batch2/cases.jsonl")
assert pool_ids(nb_rows) == pool_ids(nb_plain)  # 两文件同 id 集同序, 以 reviewed 为核查面
nl_rows = load_jsonl(E12 / "natal-leftovers/cases.jsonl")
on_rows = load_jsonl(E12 / "online-routes/cases.jsonl")

def unused(rows):
    return [(ln, o) for ln, o in rows if (o.get("id") or o.get("case_id") or o.get("provisional_id")) not in USED]

nb_unused = unused(nb_rows)
nl_unused = unused(nl_rows)
on_unused = unused(on_rows)
assert len(pool_ids(nb_rows)) == 92 and len(nb_unused) == 72, (len(nb_unused),)
assert len(pool_ids(nl_rows)) == 55 and len(nl_unused) == 48, (len(nl_unused),)
assert len(pool_ids(on_rows)) == 33 and len(on_unused) == 0
TOTAL_UNUSED = len(nb_unused) + len(nl_unused) + len(on_unused)
assert TOTAL_UNUSED == 120, TOTAL_UNUSED

# expansion12 全层交叉核对 (只计 id 集, 与 STOCK-RECOUNT §3.4 对勘)
all12 = set()
for fp in E12.rglob("*.jsonl"):
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
            all12.add(v)
assert len(all12) == 619 and len([i for i in all12 if i not in USED]) == 460, len(all12)

def pillars_ok(s):
    toks = (s or "").split()
    return len(toks) == 4 and all(len(t) == 2 and t[0] in GZ and t[1] in DZ for t in toks)

def excerpt_ok(o):
    mp = o.get("master_predictions") or []
    return bool(mp) and bool((mp[0].get("statement_excerpt") or "").strip())

def outcome_ok(o):
    oc = o.get("outcome") or {}
    return bool((oc.get("description") or "").strip())

CAVEAT_WORDS = ["推定", "拟作", "测之", "考定", "两说", "转述", "疑信参半"]

def caveats(txt):
    return [w for w in CAVEAT_WORDS if w in txt]

# ---------- natal-batch2 逐例判定 (以 cases-reviewed 的 review 终值为准) ----------
# 四滤读法 (承 REVIEW-H 四项核 + CENSUS-PREREG A 级定义):
#  逐字原文: statement_excerpt 非空且 transcription=visual (逐页视觉读图转录)
#  独立结局: grade_final=A (复核标准2: 结局有独立于断语的客观记录/分载可分离); B 即不备
#  可分离: 同上 A 口径 (grade_note/review.notes 于 A 例明载可分离; B 例明载交织/仅总评)
#  非high污染: contamination_final=low
# 锚点 (八字面, 原卡 chart 口径): chart.pillars 四柱全列且干支合法 = present;
#  review.notes 明载互证重构/非整造直载者 = partial (原文未整造直载, 升 present 无原文实据)
nb_audit = []
for ln, o in nb_unused:
    rv = o["review"]
    grade = rv["grade_final"]
    cont = rv["contamination_final"]
    f1 = excerpt_ok(o) and o.get("transcription") == "visual" and outcome_ok(o)
    f2 = grade == "A"
    f3 = grade == "A"
    f4 = cont == "low"
    notes_txt = (o.get("grade_note") or "") + (rv.get("notes") or "")
    if "重构" in notes_txt or "非整造直载" in notes_txt:
        anchor = "partial"
    elif pillars_ok((o.get("chart") or {}).get("pillars")):
        anchor = "present"
    else:
        anchor = "absent"
    cav = caveats(notes_txt)
    eligible = f1 and f2 and f3 and f4 and grade in ("A", "A-low") and cont == "low" and anchor == "present"
    nb_audit.append(dict(ln=ln, o=o, grade=grade, cont=cont, f1=f1, f2=f2, f3=f3, f4=f4,
                         anchor=anchor, cav=cav, eligible=eligible))
assert not any(a["eligible"] for a in nb_audit)  # seal 18 例全已用, 未用中 eligible=0
seal_ids = [o["id"] for _, o in nb_rows if o["review"]["verdict"] == "seal"]
assert len(seal_ids) == 18 and all(i in USED for i in seal_ids)

# ---------- natal-leftovers 逐例判定 ----------
add = json.loads((E12 / "natal-leftovers/GRADE-ADDENDUM.json").read_text(encoding="utf-8"))
REGRADED = set(add["regraded_to_A_low"])
assert REGRADED == {"NL-001", "NL-002", "NL-005", "NL-006", "NL-031", "NL-043"}
# REGRADE-REVIEW §二/§三维持 B 29 例 (逐例表 2/3 两项皆不备), 主缺项分组承 §三分布表
MAINTAINED_B = ["NL-004", "NL-007", "NL-008", "NL-009", "NL-010", "NL-012", "NL-013",
                "NL-022", "NL-028", "NL-029", "NL-030", "NL-032", "NL-033", "NL-034",
                "NL-035", "NL-036", "NL-037", "NL-038", "NL-039", "NL-040", "NL-041",
                "NL-045", "NL-047", "NL-048", "NL-051", "NL-052", "NL-053", "NL-054", "NL-055"]
assert len(MAINTAINED_B) == 29
MAIN_DEFECT = {}
for i in ["NL-004", "NL-007", "NL-008", "NL-009", "NL-010", "NL-012", "NL-013", "NL-028",
          "NL-029", "NL-030", "NL-033", "NL-034", "NL-036", "NL-038", "NL-039", "NL-040",
          "NL-041", "NL-045", "NL-047", "NL-048", "NL-051", "NL-052", "NL-054"]:
    MAIN_DEFECT[i] = "回顾性解盘"
for i in ["NL-022", "NL-032", "NL-037"]:
    MAIN_DEFECT[i] = "无具体断语"
for i in ["NL-035", "NL-053", "NL-055"]:
    MAIN_DEFECT[i] = "结局即断语本身/仅状态语"
assert set(MAIN_DEFECT) == set(MAINTAINED_B)

nl_audit = []
for ln, o in nl_unused:
    grade = "A-low" if o["id"] in REGRADED else o["outcome_grade"]
    cont = o["contamination"]
    f1 = excerpt_ok(o) and outcome_ok(o) and bool((o.get("transcription") or "").strip())
    if o["id"] in MAINTAINED_B:
        f2 = False  # REGRADE 逐例表: 结局具体可分离项不备
        f3 = False  # 同上, 且非回顾性项亦不备
    else:
        f2 = grade in ("A", "A-low")  # CENSUS §四 A 口径: 独立客观记录可互核/原文明确记载可分离
        f3 = grade in ("A", "A-low")
    f4 = cont == "low"
    m = re.search(r"四柱（(.+?)）", o.get("question_or_topic") or "")
    anchor = "present" if (m and pillars_ok(m.group(1))) else "absent"
    eligible = f1 and f2 and f3 and f4 and grade in ("A", "A-low") and cont == "low" and anchor == "present"
    nl_audit.append(dict(ln=ln, o=o, grade=grade, cont=cont, f1=f1, f2=f2, f3=f3, f4=f4,
                         anchor=anchor, eligible=eligible))
elig_ids = sorted(a["o"]["id"] for a in nl_audit if a["eligible"])
# A/A-low+low 全集 (改判 6 例 + NL-049) 逐 id 核对: 7 例全部已在已用并集内, 故未用 eligible=0
alow_low = sorted(o["id"] for _, o in nl_rows
                  if ("A-low" if o["id"] in REGRADED else o["outcome_grade"]) in ("A", "A-low")
                  and o["contamination"] == "low")
assert alow_low == ["NL-001", "NL-002", "NL-005", "NL-006", "NL-031", "NL-043", "NL-049"], alow_low
assert all(i in USED for i in alow_low)
assert elig_ids == [], elig_ids

def yn(b):
    return "✓" if b else "✗"

def verdict(a):
    if a["eligible"]:
        return "eligible"
    bad = []
    if not a["f1"]:
        bad.append("逐字原文")
    if not a["f2"]:
        bad.append("独立结局")
    if not a["f3"]:
        bad.append("可分离")
    if not a["f4"]:
        bad.append("非high污染")
    if a["grade"] not in ("A", "A-low"):
        bad.append("A级")
    if a["cont"] != "low":
        bad.append("low污染")
    if a["anchor"] != "present":
        bad.append("锚点在场")
    return "不合格（卡：" + "、".join(dict.fromkeys(bad)) + "）"

segs = []
# ===== 段 1: 头 + 复算 =====
s = []
s.append("# EXPANSION-AUDIT-expansion12b-r84 —— expansion12 池资格核查台账（后半子池组，R84 供给席 E4）")
s.append("")
s.append("本件为 R84 供给席 E4 产出（PREREG §3 工序）：只做资格核查，不建卡、不组集、不作断、不评分、不兼任本轮任何其他席位。脚本：`/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply/audit_expansion12b_r84.py`（盘上实算，分段 append 落盘、逐段断言）。台账/结局文本一律按数据处理。")
s.append("")
s.append("## 口径")
s.append("")
s.append("- 范围：expansion12 内 mingli-tanyuan-zhenben、natal-batch2、natal-leftovers、online-routes、pending-verify 五子池＋根下散件。池层 id 总量＝池目录内全部 jsonl 之 id 并集（承 STOCK-RECOUNT-h27 §3.4；本席对 expansion12 全层复算：619 id、已用命中 159、未用 460，与该件登记逐数全等）。")
s.append("- 已用并集（R84 开轮口径，本席盘上复算断言通过）：**1166**＝dev 488＋phase2 splits2 holdout2 29＋holdout3–28 金标 id 754＋holdout inputs 卡 id 595＋顶层 inputs6–10 卡 id 412，五源并集去重。金标只读 id 字段，未读金标正文；未打开任何 predictions/judging/final-scores。")
s.append("- 四滤（逐字原文、独立结局、可分离、非 high 污染）＋A 级／low 污染＋锚点在场，标准照现行口径：A 级承 expansion12/CENSUS-PREREG 入封资格定义（结局有独立于大师断语的客观记录，或原文明确记载与断语可分离的具体事件记录）；八字面锚点以原卡四柱全列为在场（batch2 以 chart.pillars、leftovers 以题面四柱全列＋REGRADE 复核判据④为据），要素缺项判 partial、升 present 须原文实据。")
s.append("- natal-batch2 以 cases-reviewed.jsonl 的 review 终值（grade_final／contamination_final／verdict）为准（REVIEW-H 独立复核，结论以复核为准；cases.jsonl 与之同 id 集同序，本席已断言）。natal-leftovers 等级以 GRADE-ADDENDUM.json 生效值为准（NL-001/002/005/006/031/043 由 B 改判 A-low；维持 B 29 例理由以 REGRADE-REVIEW.md 逐例表为准）。")
s.append("")
s.append("## 一、未用 id 复算（逐 id，按子池分组）")
s.append("")
s.append(f"- **natal-batch2**（池内 92 id，已用 20，未用 **72**）：{'、'.join(a['o']['id'] for a in nb_audit)}")
s.append(f"- **natal-leftovers**（池内 55 id，已用 7，未用 **48**）：{'、'.join(a['o']['id'] for a in nl_audit)}")
s.append("- **online-routes**（池内 33 id，已用 33，未用 **0**）：CZ-001…CZ-033 全部命中已用并集，无未用例（同名即剔口径下不作逐例核查；该文件内 holdout_eligible 亦全为 false）。")
s.append("- **mingli-tanyuan-zhenben**（未用 **0**）：子池内无任何 jsonl（仅 CENSUS／METHOD／校勘类 md 与页图），池层 id 并集贡献 0；文中 MT 编号系跨池校勘引用，其案例记录不在本子池。")
s.append("- **pending-verify**（未用 **0**）：子池内无 jsonl，仅 VERDICTS.md 与 overlay-proposals.json；overlay 草案所涉 6 id（LY-430、LR3-112、LY-437、LY-533、OC-014、YM-019）经本席逐 id 核对全部已在已用并集内，属既有例的结局处置草案、非新供给。")
s.append("- **expansion12 根散件**（未用 **0**）：根下无 jsonl（仅 CENSUS／HOST-RULINGS 类 md 与 POOL-IDS.txt 全池清单文本），池层 id 并集贡献 0。")
s.append(f"- **所辖未用合计：120**（natal-batch2 72＋natal-leftovers 48）。以下逐例核查即此 120 例。")
s.append("")
segs.append("\n".join(s) + "\n")

# ===== 段 2: natal-batch2 逐例 =====
s = []
s.append("## 二、逐例资格核查 —— natal-batch2（72 例，体系：八字）")
s.append("")
s.append("来源：袁树珊《袁氏命谱》（PU）／韦千里《千里命稿》（QL），转录＝逐页视觉读图（transcription=visual）。原文定位＝cases-reviewed.jsonl 行号＋provenance 页。")
s.append("")
s.append("| id | 子池 | 体系/来源 | 逐字原文 | 独立结局 | 可分离 | 非high | 锚点 | 污染 | 等级 | 结论 | 原文定位 |")
s.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
for a in nb_audit:
    o = a["o"]
    src = f"八字/{o['master']}《{o['source_work'].strip('《》')}》"
    loc = f"natal-batch2/cases-reviewed.jsonl:{a['ln']}；{o['provenance']['page']}"
    note = ""
    if a["anchor"] == "partial":
        note = "（锚点注：四柱系互证重构、非整造直载）"
    elif a["cav"]:
        note = "（锚点注：四柱书内单一采用，含" + "、".join(a["cav"]) + "成分，入池须知）"
    s.append(f"| {o['id']} | natal-batch2 | {src} | {yn(a['f1'])} | {yn(a['f2'])} | {yn(a['f3'])} | {yn(a['f4'])} | {a['anchor']}{note} | {a['cont']} | {a['grade']} | {verdict(a)} | {loc} |")
s.append("")
segs.append("\n".join(s) + "\n")

# ===== 段 3: natal-leftovers 逐例 =====
s = []
s.append("## 三、逐例资格核查 —— natal-leftovers（48 例，体系：八字）")
s.append("")
s.append("来源：韦千里《呱呱集》（NL-001…045）／徐乐吾评注《子平真诠评注》（NL-046…055）。原文定位＝cases.jsonl 行号＋provenance 页。维持 B 例的卡项主因承 REGRADE-REVIEW §三分布（回顾性解盘／无具体断语／结局即断语本身），其逐例表②③两项皆不备。")
s.append("")
s.append("| id | 子池 | 体系/来源 | 逐字原文 | 独立结局 | 可分离 | 非high | 锚点 | 污染 | 等级 | 结论 | 原文定位 |")
s.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
for a in nl_audit:
    o = a["o"]
    src = f"八字/{o['master']}《{o['source_work'].strip('《》')}》"
    loc = f"natal-leftovers/cases.jsonl:{a['ln']}；{o['provenance']['page']}"
    extra = ""
    if o["id"] in MAIN_DEFECT:
        extra = f"（主缺项：{MAIN_DEFECT[o['id']]}）"
    if o["id"] in REGRADED:
        extra = "（GRADE-ADDENDUM 改判 A-low）"
    if o["id"] == "NL-044":
        extra = "（注：命主名一字待核，见 CENSUS 勘误）"
    if o["id"] == "NL-021":
        extra = "（注：grade_note 载命造本身不可核）"
    s.append(f"| {o['id']} | natal-leftovers | {src} | {yn(a['f1'])} | {yn(a['f2'])} | {yn(a['f3'])} | {yn(a['f4'])} | {a['anchor']} | {a['cont']} | {a['grade']} | {verdict(a)}{extra} | {loc} |")
s.append("")
segs.append("\n".join(s) + "\n")

# ===== 段 4: 计数 + 异常 =====
all_a = nb_audit + nl_audit
elig = [a for a in all_a if a["eligible"]]
fail_high = [a for a in all_a if not a["f4"]]
fail_grade = [a for a in all_a if a["grade"] not in ("A", "A-low")]
fail_anchor_partial = [a for a in all_a if a["anchor"] == "partial"]
s = []
s.append("## 四、分面计数（所辖未用 120 例）")
s.append("")
s.append("| 面 | 未用 | eligible | 不合格 |")
s.append("|---|---|---|---|")
s.append(f"| natal-batch2（八字） | 72 | 0 | 72 |")
s.append(f"| natal-leftovers（八字） | 48 | 0 | 48 |")
s.append("| online-routes（测字） | 0 | 0 | 0 |")
s.append("| mingli-tanyuan-zhenben | 0 | 0 | 0 |")
s.append("| pending-verify | 0 | 0 | 0 |")
s.append("| 根散件 | 0 | 0 | 0 |")
s.append(f"| **合计** | **120** | **0** | **120** |")
s.append("")
s.append("- 逐体系 eligible：八字 **0**；六爻 0；奇门 0；测字 0；其余体系 0。所辖五子池＋根散件未用 120 例逐例核查后 eligible 为 **0**。")
s.append("- 非六爻 eligible 合计 **0**；六爻 eligible 合计 **0**。（本席所辖范围对 PREREG §5 门槛的贡献为 0；其余子池组不在本席范围。）")
fh_nb = len([a for a in nb_audit if not a['f4']]); fh_nl = len([a for a in nl_audit if not a['f4']])
s.append(f"- 不合格主因分布（可重叠）：污染 high {len(fail_high)} 例（natal-batch2 {fh_nb}＋natal-leftovers {fh_nl}，逐例见台账行）；等级非 A／独立结局与可分离不备 {len(fail_grade)} 例；锚点 partial {len(fail_anchor_partial)} 例（QL-021、QL-029，四柱互证重构、非整造直载，两例另因 high 污染不合格，锚点不改变其结论）。逐字原文一项 120 例全过（断语摘录与结局描述俱非空、转录来源在册）。")
s.append("- 交叉核对（资格全过集与已用并集的关系）：natal-batch2 复核 seal 18 例（＝holdout_eligible=true 集）全部已在已用并集内；natal-leftovers 资格全过集恰 7 例（改判 A-low 6 例 NL-001、NL-002、NL-005、NL-006、NL-031、NL-043＋原 A＋low 的 NL-049），亦全部已在已用并集内（脚本逐 id 断言通过）。即所辖两子池凡资格全过者皆已被取用，未用 120 例无一全过，与逐例核查结论 eligible=0 互证一致。")
s.append("")
s.append("## 五、异常与注记")
s.append("")
s.append("1. **编号映射**：natal-batch2 盘上现行号 PU/QL 系 RENUMBER-MAP.json 重编结果（旧 MP→PU 同号、旧 QM→QL 非同号映射）；REVIEW-H 与 CENSUS-NOTES 正文仍用旧号，引用时须经映射表换算，本台账一律用现行号。")
s.append("2. **锚点 partial 2 例**：QL-021（页上仅残行见一柱、余柱互证重构）、QL-029（干支序列与造式互证复原），原文未整造直载，按口径判 partial、不升 present；两例同时 high 污染，结论均为不合格。另 PU 诸例中时柱含推定/考定/拟作/转述成分者（PU-001、002、004、006、007、012、025、031、037、040、055 及 QL-034 造式两说）四柱仍为书内单一采用、全列在册，判 present 并逐行注记，入池使用不得作史载生辰直录引用。")
s.append("3. **online-routes 同名占用**：CZ-001…CZ-033 与既有 CZ 号段（dev 侧）同名，33 例全部命中已用并集；按同名即剔，本子池对未用集贡献 0。此为 id 层占用事实，不涉该 33 例内容资格（其文件内 holdout_eligible 亦全 false）。")
s.append("4. **mingli-tanyuan-zhenben 无例可核**：该子池为《命理探源》版本/存稿校勘面，只有文档与页图、无案例 jsonl；如主持认定其 CENSUS 文档内述及的命例应另册建账，须另行派单抽例，不在本席核查范围内推定。")
s.append("5. **NL-044**：命主名一字（微/维）待核、CENSUS 已登记，本例另因 B 级＋high 污染不合格，待核事项不影响结论。**NL-021**：grade_note 载命造本身不可核，本例因 B 级＋high 污染不合格，锚点形式全列但附注于台账行。")
s.append("6. 本席未打开任何已封存集金标正文（已用并集只取金标 id 字段）、未打开 runs/ 下 predictions/judging/final-scores；池层原文只读未改；脚本仅本件同目录唯一名文件。")
s.append("")
segs.append("\n".join(s) + "\n")

# ---------- 分段 append 落盘, 逐段断言 ----------
OUT.write_text("", encoding="utf-8")
total = 0
for i, seg in enumerate(segs, 1):
    with OUT.open("a", encoding="utf-8") as f:
        f.write(seg)
    total += len(seg.encode("utf-8"))
    actual = OUT.stat().st_size
    assert actual == total, (i, actual, total)
    print(f"segment {i} appended, bytes={actual}")
print("DONE unused=120 eligible=0 bytes=", OUT.stat().st_size)
