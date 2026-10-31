#!/usr/bin/env python3
"""R84 supply seat E3: expansion12 pool qualification audit (front-half subpools).

Scope (absolute paths only, no /tmp):
  /home/hatch/workspace/divination/benchmark/phase3/expansion12/{bushi-quanshu-beixuan,
  cezi-zichu, density-checks, huangjince-huozhulin, liuren-bianyi-yuce,
  liuren-cuiyan, liuren-duanan}

Steps:
  1) Recompute used-id union (1166) per R84 PREREG opening method:
     dev (master-baseline-dev9 keys + inputs-dev9/10/11/12 + inputs card ids)
     + phase2 splits2 holdout2 + holdout3-28 test_gold.jsonl id fields only
     + holdout2-28 inputs card ids + top-level inputs6-10 card ids.
     Gold files are read for the id field ONLY; gold body text is never used.
  2) Pool id totals per subpool = union of ids in all *.jsonl under the subpool dir.
  3) For every unused id, adjudicate: four filters (verbatim / independent
     outcome / separable / non-high pollution) + A-grade / low pollution +
     anchor presence, per the standards documented in the output file.
Output: EXPANSION-AUDIT-expansion12a-r84.md in this directory, appended in
segments with assertions after each segment.
"""
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
BM = P3.parent
EXP12 = P3 / "expansion12"
OUT = P3 / "runs/round84/supply/EXPANSION-AUDIT-expansion12a-r84.md"

SUBPOOLS = [
    "bushi-quanshu-beixuan",
    "cezi-zichu",
    "density-checks",
    "huangjince-huozhulin",
    "liuren-bianyi-yuce",
    "liuren-cuiyan",
    "liuren-duanan",
]

# ---------------------------------------------------------------- used union
def card_ids(d: Path):
    out = set()
    if d.is_dir():
        for f in d.glob("*.json"):
            out.add(f.stem)
    return out

def gold_ids(p: Path):
    out = set()
    if p.is_file():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                out.add(json.loads(line)["id"])  # id field only
    return out

def build_used():
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

# ---------------------------------------------------------------- pool records
def load_jsonl(fp: Path):
    rows = []
    for line in fp.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows

def pool_records(subpool: str):
    """Return (ids set, {id: (record, relpath)}) with reviewed files taking
    precedence over plain files for the same id."""
    d = EXP12 / subpool
    ids = set()
    recs = {}
    files = sorted(d.rglob("*.jsonl"))
    # plain first, reviewed last so reviewed wins
    files.sort(key=lambda f: ("reviewed" in f.name, f.name))
    for fp in files:
        for r in load_jsonl(fp):
            rid = r.get("id") or r.get("case_id") or r.get("provisional_id")
            if rid:
                ids.add(rid)
                recs[rid] = (r, str(fp.relative_to(P3)))
    return ids, recs, [str(f.relative_to(P3)) for f in files]

# ---------------------------------------------------------------- anchor (liuren)
GAN = "甲乙丙丁戊己庚辛壬癸"
ZHI = "子丑寅卯辰巳午未申酉戌亥"
def anchor_liuren(asked_at: str):
    a = asked_at or ""
    year_ok = bool(re.search(rf"[{GAN}][{ZHI}]年", a)) or bool(re.search(r"民国\d+年", a))
    # regnal-year form: era name + numeral year (e.g. 宣和三年)
    if re.search(r"(宣和|大观|崇宁|靖康|建炎|绍兴|咸丰|同治|道光|光绪|乾隆|嘉庆)", a) and re.search(r"[一二三四五六七八九十\d]+年", a):
        year_ok = True
    # era-name + stem-branch year + branch month (e.g. 咸丰甲寅午月丁丑日):
    # a stem-branch pair directly followed by a branch month is the year
    if re.search(rf"[{GAN}][{ZHI}][{ZHI}]月", a):
        year_ok = True
    # shorthand form: leading stem-branch pair directly followed by a month
    # expression is the year stem-branch with 年 omitted (e.g. 己酉八月癸酉日)
    stripped = a.strip()
    if len(stripped) >= 3 and stripped[0] in GAN and stripped[1] in ZHI and stripped[2] in "一二三四五六七八九十正闰冬腊秋春夏":
        if re.search(rf"[{GAN}已][{ZHI}]日", a):
            year_ok = True
    if a.strip().startswith("□年"):
        year_ok = False
    month_ok = bool(re.search(r"(正月|闰?[一二三四五六七八九十冬腊]月|\d+月|秋月|春月|夏月)", a)) or bool(re.search(rf"[{ZHI}]月", a))
    if "□月" in a:
        month_ok = False
    day_ok = bool(re.search(rf"[{GAN}已][{ZHI}]日", a))
    # day stem-branch written without 日 suffix, directly followed by 将/时
    if re.search(rf"[{GAN}][{ZHI}][{ZHI}]将", a) or re.search(rf"日[{GAN}][{ZHI}]", a):
        day_ok = True
    if "□日" in a or "日干支佚" in a:
        day_ok = False
    hour_ok = bool(re.search(rf"[{ZHI}]时", a))
    elems = {"年": year_ok, "月": month_ok, "日": day_ok, "时": hour_ok}
    n_ok = sum(elems.values())
    if n_ok == 4:
        return "present", elems
    if n_ok == 0:
        return "absent", elems
    return "partial", elems

def anchor_liuyao(rec):
    """Five elements: 卦名 / 动爻 / 世应 / 六亲纳支 / 月建日辰 (六神 not required)."""
    hx = rec.get("hexagram") or {}
    name_ok = bool(hx.get("original_name"))
    chart = str(hx.get("chart_lines") or "")
    dong_ok = ("动" in chart) or bool(hx.get("changed_name"))
    shiying_ok = ("世" in chart and "应" in chart)
    liuqin_ok = any(q in chart for q in ["父母", "兄弟", "官鬼", "妻财", "子孙"]) and bool(re.search(rf"[{GAN}][{ZHI}]", chart))
    asked = rec.get("asked_at") or ""
    yue_ok = bool(re.search(r"(正月|闰?[一二三四五六七八九十冬腊]月|\d+月)", asked))
    ri_ok = bool(re.search(rf"[{GAN}][{ZHI}]日", asked))
    monthday_ok = yue_ok and ri_ok
    elems = {"卦名": name_ok, "动爻": dong_ok, "世应": shiying_ok, "六亲纳支": liuqin_ok, "月建日辰": monthday_ok}
    if rec.get("chart_complete") and rec.get("month_day_complete"):
        return "present", elems
    if all(elems.values()):
        return "present", elems
    if not any(elems.values()):
        return "absent", elems
    return "partial", elems

# ---------------------------------------------------------------- filters
TAOYU = re.compile(r"(如所占|如所断|全如所占|事俱验|果应$|晓果)")
def outcome_is_taoyu_only(text: str):
    t = (text or "").strip()
    if not t:
        return True
    if "（验语简）" in t and len(t) <= 10:
        return True
    clauses = [c for c in re.split(r"[，。；、]", t) if c.strip()]
    if not clauses:
        return True
    return all(TAOYU.search(c) for c in clauses)

NO_OUTCOME_MARKERS = ["未载后验", "未立后验段", "未见独立结局", "仅以断语回指", "揭晓物名未独立", "未能全读", "无结局段", "无后验"]

def adjudicate(subpool: str, rec: dict):
    """Return dict of filter results. Standards documented in output header."""
    rid = rec["id"]
    trad = rec.get("tradition", "")
    is_liuyao = trad in ("六爻", "liuyao")
    review = rec.get("review")
    pred_txt = " ".join(p.get("statement_excerpt", "") for p in rec.get("master_predictions", []))
    out_txt = (rec.get("outcome") or {}).get("description", "")
    grade_note = rec.get("grade_note", "") or ""

    f1 = f2 = f3 = f4 = True
    notes = []

    if review is not None:
        # liuren-bianyi-yuce: REVIEW-G adjudication supersedes original grading
        gf = review.get("grade_final", "")
        cf = review.get("contamination_final", "")
        grade_ok = gf in ("A", "A-low")
        contam = cf
        if gf == "待回源核":
            f2 = False
            notes.append("复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三）")
        if rid == "YX-006":
            f3 = False
            notes.append("复核判断/验分离度不足（REVIEW-G §三(四)）")
        if cf == "high":
            f4 = False
            notes.append("复核污染改判 high（REVIEW-G §三）")
        if review.get("verdict") == "dev-only" and gf == "A-low" and cf != "high":
            notes.append("复核 verdict=dev-only（污染改判出封）")
    else:
        grade_ok = rec.get("outcome_grade") in ("A", "A-low")
        contam = rec.get("contamination", "")
        # F1 verbatim: fail only where the record itself flags outcome text unreadable
        if rid == "CY-048":
            f1 = False
            notes.append("验语尾字漫漶未能全读（原卡 grade_note）")
        # F2 independent outcome
        if outcome_is_taoyu_only(out_txt):
            f2 = False
            notes.append("结局仅套语回声（果如所占/后果如所占类）、无独立事件记述")
        if any(m in out_txt for m in NO_OUTCOME_MARKERS):
            f2 = False
            notes.append("原卡自载无独立结局/后验段")
        # F3 separable
        if ("不可分离" in grade_note) or ("不可分离" in out_txt):
            f3 = False
            notes.append("原卡自载断/验交缠不可分离")
        if rid == "CY-018":
            notes.append("结局尾语与断交缠（原卡自载）、主体事件（生后累年余而殇）可分离，按原卡 A-low 口径计可分离 pass、限度登记于此")
        if rid == "DA-142":
            f3 = False
            notes.append("应验嵌于断语段内（抽例注记 §特别处置）")
        if contam == "high":
            f4 = False
            notes.append("原卡 contamination=high")
        if not grade_ok:
            notes.append(f"原卡 outcome_grade={rec.get('outcome_grade')}（非 A 级）")

    if is_liuyao:
        anchor, elems = anchor_liuyao(rec)
        anchor_str = anchor + "(" + "".join(k for k, v in elems.items() if v) + ")"
        if rec.get("chart_complete") is False:
            notes.append("原卡 chart_complete=false、无全盘")
    else:
        anchor, elems = anchor_liuren(rec.get("asked_at", ""))
        missing = [k for k, v in elems.items() if not v]
        anchor_str = anchor if not missing else anchor + "(缺" + "".join(missing) + ")"
        if anchor != "present":
            notes.append("课式头要素缺项：" + "".join(missing))

    low_ok = contam == "low"
    eligible = all([f1, f2, f3, f4, grade_ok, low_ok, anchor == "present"])
    fails = []
    if not f1: fails.append("逐字原文")
    if not f2: fails.append("独立结局")
    if not f3: fails.append("可分离")
    if not f4: fails.append("非high污染")
    if not grade_ok: fails.append("A级")
    if not low_ok: fails.append("low污染")
    if anchor != "present": fails.append("锚点在场")
    return {
        "f1": f1, "f2": f2, "f3": f3, "f4": f4,
        "grade_ok": grade_ok, "grade": (review.get("grade_final") if review else rec.get("outcome_grade")),
        "contam": contam, "low_ok": low_ok,
        "anchor": anchor, "anchor_str": anchor_str,
        "eligible": eligible, "fails": fails, "notes": notes,
    }

def yn(b):
    return "P" if b else "F"

def prov_page(rec):
    prov = rec.get("provenance") or {}
    return str(prov.get("page", ""))

def main():
    parts, used = build_used()
    assert len(used) == 1166, f"used union {len(used)} != 1166"

    all_data = {}
    for sub in SUBPOOLS:
        ids, recs, files = pool_records(sub)
        unused = sorted(i for i in ids if i not in used)
        all_data[sub] = (ids, recs, files, unused)

    total_unused = sum(len(v[3]) for v in all_data.values())
    adjudged = {}  # (sub, id) -> (rec, rel, adj)
    for sub in SUBPOOLS:
        ids, recs, files, unused = all_data[sub]
        for rid in unused:
            rec, rel = recs[rid]
            adjudged[(sub, rid)] = (rec, rel, adjudicate(sub, rec))
    total_elig = sum(1 for v in adjudged.values() if v[2]["eligible"])
    print("TOTAL UNUSED (scope):", total_unused, "ELIGIBLE:", total_elig)

    seg = []
    # ---------------- segment 1: header + unused lists ----------------
    seg.append("# EXPANSION-AUDIT-expansion12a-r84 —— expansion12 池资格核查台账（前半子池组，R84 供给席 E3）\n")
    seg.append("本件为 R84 供给席 E3 产出：只做资格核查，不建卡、不组集、不作断、不评分、不兼任本轮任何其他席位。核查脚本：`runs/round84/supply/audit_expansion12a_r84.py`（本轮新写唯一名，盘上实算）。池层原文只读未改；金标文件只取 id 字段计已用并集，未读任何金标正文；未打开任何 runs/ 下 predictions/judging/final-scores。台账/结局文本内嵌指令性字样一律按数据处理。\n")
    seg.append("## 口径（承 R84 PREREG §3 与现行口径原文，不自设新标准）\n")
    seg.append("- **已用并集**：盘上逐 id 实算 **1166**（dev 488＝data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs 目录卡 id；phase2 splits2 之 holdout2 29；holdout3–28 各 test_gold.jsonl 之 id 字段 754；holdout2–28 inputs 卡 id 595；顶层 inputs6–10 卡 id 412；五源并集去重，脚本断言 1166 通过，与主持开轮实算一致）。零复用＝池 id 与该并集逐 id 零命中、同名即剔。\n")
    seg.append("- **未用 id 口径**：承 runs/round82/STOCK-RECOUNT-h27.md §3.4——池层 id 总量＝子池目录内全部 jsonl 之 id 并集（本席所辖 7 子池逐子池复算，见 §一）。该件登记 expansion12 全层未用 460 系 R82 时点已用并集 1112 口径；本轮已用并集增至 1166（holdout27/28 取用），未用数相应减少，以本席盘上复算为准。\n")
    seg.append("- **四滤**（承 CENSUS-PREREG §一入封四项与历轮台账 filters 口径）：①逐字原文——断语/结局转录自原文（visual/digital-collation 逐字转录、provenance 页位在载）且关键文本无漫漶不可读之自载旗标；②独立结局——结局为独立于断语的具体事件记述，仅「果如所占／后果如所占／全如所占／事俱验／果应」类套语回声、无事件落文者判不成立（承 liuren-bianyi-yuce/REVIEW-G §三同型判例：仅凭记录内文本核断、摘录过薄无法确认双全者不合格；短而具体的事件句不以字数计、照 BQ-027 主持复核先例）；③可分离——断语与结局分载可分离，原卡自载交缠不可分离者判不成立；④非 high 污染——污染级非 high。\n")
    seg.append("- **A 级／low**：结局可得性 A 级（含 A-low，主持口径：断语与应验俱在书内、具体可分离、断先于验）且污染 low。liuren-bianyi-yuce 以 cases-reviewed.jsonl 之 review 字段（grade_final/contamination_final/verdict）为终裁口径（REVIEW-G 明示「结论以本报告为准」），原 cases.jsonl 分级被复核改判者从复核。\n")
    seg.append("- **锚点在场**：六爻面以五要素（卦名、动爻、世应、六亲纳支、月建日辰）为唯一标准、六神不属要件（承 ADDENDUM-r60 §一裁定）；他体系以原卡/台账 anchor 字段口径为准——本组六壬各池原卡无独立 anchor 字段，课式锚点载于原卡 asked_at 课式头，以其四要素（年、月、日、时，干支/纪年载记）为要素集：四要素俱载判 present、任一缺项（□/佚/未载）判 partial、升 present 须原文实据（asked_at 逐字为据，年干支省「年」字而直承月名、纪年年号＋年数、日干支省「日」字直承月将等原书体例载记法照原文认定并逐例可回查）。盘面本体（四课三传/天地盘）不在池卡内、属组集建卡时回原文复原工序（holdout12 建集先例），不作本轮锚点要素；粹言池卡盘字未录一节照实登记于 §三异常说明。\n")
    seg.append("- **eligible**：未用 ∧ 四滤全 pass ∧ A 级 ∧ low ∧ 锚点 present，缺一不可；不合格逐例注明所卡滤项。\n")
    seg.append("\n## 一、未用 id 清单（逐 id，按子池分组）\n")
    for sub in SUBPOOLS:
        ids, recs, files, unused = all_data[sub]
        seg.append(f"\n### {sub}\n")
        seg.append(f"- 池层 id 总量 {len(ids)}；已用命中 {len(ids) - len(unused)}；**未用 {len(unused)}**。jsonl 文件：{('、'.join(files) if files else '（无 jsonl 文件）')}\n")
        if unused:
            seg.append("- 未用 id：" + "、".join(unused) + "\n")
        else:
            seg.append("- 未用 id：（无）\n")
    OUT.write_text("".join(seg), encoding="utf-8")
    written = OUT.read_text(encoding="utf-8")
    for sub in SUBPOOLS:
        for rid in all_data[sub][3]:
            assert rid in written, f"seg1 missing {rid}"
    print("segment 1 written:", OUT.stat().st_size, "bytes")

    # ---------------- segment 2: per-case ledger, per subpool ----------------
    hdr = "\n## 二、逐例资格核查台账（逐例一行）\n"
    hdr += "\n列：id｜子池｜体系/来源｜逐字｜独立结局｜可分离｜非high｜A级｜污染｜锚点｜结论｜原文定位（文件＋provenance 页位）｜备注。四滤/A级以 P=pass、F=fail 记。\n"
    with OUT.open("a", encoding="utf-8") as fh:
        fh.write(hdr)
    for sub in SUBPOOLS:
        ids, recs, files, unused = all_data[sub]
        lines = [f"\n### {sub}（未用 {len(unused)} 例）\n"]
        if not unused:
            lines.append("\n（本子池未用例 0，无逐例行。）\n")
        else:
            lines.append("\n| id | 子池 | 体系/来源 | 逐字 | 独立结局 | 可分离 | 非high | A级 | 污染 | 锚点 | 结论 | 原文定位 | 备注 |\n")
            lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
            for rid in unused:
                rec, rel, adj = adjudged[(sub, rid)]
                src = str(rec.get("source_work", "")).replace("|", "｜")
                trad = str(rec.get("tradition", ""))
                concl = "eligible" if adj["eligible"] else "不合格（卡：" + "、".join(adj["fails"]) + "）"
                notes = "；".join(adj["notes"])
                lines.append(
                    f"| {rid} | {sub} | {trad}/{src} | {yn(adj['f1'])} | {yn(adj['f2'])} | {yn(adj['f3'])} | {yn(adj['f4'])} "
                    f"| {yn(adj['grade_ok'])}({adj['grade']}) | {adj['contam']} | {adj['anchor_str']} | {concl} "
                    f"| {rel}；{prov_page(rec)} | {notes} |\n"
                )
        with OUT.open("a", encoding="utf-8") as fh:
            fh.write("".join(lines))
        written = OUT.read_text(encoding="utf-8")
        for rid in unused:
            assert f"| {rid} |" in written, f"seg2 missing row {rid}"
        print(f"segment 2 [{sub}] appended; file now", OUT.stat().st_size, "bytes")

    # ---------------- segment 3: counts + anomalies ----------------
    from collections import Counter
    per_sub = {}
    for sub in SUBPOOLS:
        ids, recs, files, unused = all_data[sub]
        el = sum(1 for rid in unused if adjudged[(sub, rid)][2]["eligible"])
        per_sub[sub] = (len(ids), len(ids) - len(unused), len(unused), el)
    fail_counter = Counter()
    anchor_counter = Counter()
    for (sub, rid), (rec, rel, adj) in adjudged.items():
        for f in adj["fails"]:
            fail_counter[f] += 1
        anchor_counter[adj["anchor"]] += 1
    liuyao_unused = sum(1 for (sub, rid), (rec, rel, adj) in adjudged.items() if rec.get("tradition") in ("六爻", "liuyao"))
    liuyao_elig = sum(1 for (sub, rid), (rec, rel, adj) in adjudged.items() if adj["eligible"] and rec.get("tradition") in ("六爻", "liuyao"))

    s3 = ["\n## 三、分面计数\n"]
    s3.append("\n| 子池 | 池层 id 总量 | 已用命中 | 未用 | eligible | 不合格 |\n|---|---|---|---|---|---|\n")
    for sub in SUBPOOLS:
        t, u, un, el = per_sub[sub]
        s3.append(f"| {sub} | {t} | {u} | {un} | {el} | {un - el} |\n")
    s3.append(f"| **合计** | **{sum(v[0] for v in per_sub.values())}** | **{sum(v[1] for v in per_sub.values())}** | **{total_unused}** | **{total_elig}** | **{total_unused - total_elig}** |\n")
    s3.append(f"\n- 按体系：六壬 eligible {total_elig - liuyao_elig}（未用 {total_unused - liuyao_unused}）；六爻 eligible {liuyao_elig}（未用 {liuyao_unused}）。\n")
    s3.append(f"- **非六爻 eligible 合计 {total_elig - liuyao_elig}**；六爻 eligible 合计 {liuyao_elig}。（本组子池体系构成：六壬＋六爻，无八字/奇门/测字/紫微例。）\n")
    s3.append(f"- 锚点分布（未用 {total_unused} 例）：present {anchor_counter.get('present', 0)}、partial {anchor_counter.get('partial', 0)}、absent {anchor_counter.get('absent', 0)}。\n")
    s3.append("- 不合格所卡滤项计数（一例可卡多项）：\n")
    for k in ["逐字原文", "独立结局", "可分离", "非high污染", "A级", "low污染", "锚点在场"]:
        s3.append(f"  - {k}：{fail_counter.get(k, 0)}\n")
    s3.append("\n## 四、异常与限度说明\n")
    s3.append("\n1. **cezi-zichu、density-checks 两子池无 jsonl 文件**（盘上实况：cezi-zichu 仅 CHAPTER-DRAFT.md、EXTRACTION-NOTES.md、work-ocr/、work-pages/；density-checks 仅 CENSUS-NOTES.md），池层 id 总量 0、未用 0、无逐例可核——《字触》成例从未抽例建池（提炼件自载「未逐条全录、后续抽例建池另行处理」）、density-checks 为密度普查件（定案 NO-GO、不产 cases），与盘上登记一致，只登记不另断。\n")
    s3.append("2. **bushi-quanshu-beixuan（BQ-026–034，9 例）与 huangjince-huozhulin（HZ-001）未用均为 0**：9＋1 例 id 全部命中已用并集（BQ 系经 holdout14 inputs 卡、HZ-001 经 holdout12 inputs 卡），本轮无逐例核查对象；其资格状态以既往封存集登记为准、本席不重判。\n")
    s3.append("3. **六壬锚点口径限度**：本组六壬池卡无独立 anchor 字段，锚点以原卡 asked_at 课式头四要素（年月日时）判定（口径与实据见卷首口径节）；盘面本体（四课三传/天地盘）未载于池卡——断案系底本全文（liuren-duanan/scratch-archive/cases_raw.json）在盘、辨疑系原书课盘体例经 holdout12 建集日志登记、粹言系原书有课盘列而池卡未录盘字（holdout12 建集日志逐例 fidelity 登记在案），组集建卡时仍须逐例回原文复核盘面，本台账之 present 不替代建卡复核。\n")
    s3.append("4. **粹言慕农套语结局 30 余例**：cases-munong.jsonl 中多例 outcome 仅载「后果如所占」类套语（转录底稿 TRANSCRIPTION-NOTES.md 同型），原抽例席按 A-low 收录；本席承 REVIEW-G 同型判例（仅凭记录内文本核断）判独立结局不成立。此为本组最大不合格来源之一；若主持日后回原书页图核得案验全文更完整者，可逐例升回，本台账只按盘上记录现状判定。\n")
    s3.append("5. **断案系课式头无年份 20 余例**：cases-a/b 部分例 asked_at 未载年份（底本同段年份未逐例明载、抽例注记自载「个别案底本课式头无年份照原样保留」），按「升 present 须原文实据」判 partial；其余四滤与分级多全过，卡点仅在锚点一项，逐例已于台账备注注明缺项。\n")
    s3.append("6. 本席未打开任何已封存集金标正文（已用并集只取金标 id 字段）、未打开 runs/ 下 predictions/judging/final-scores；对 runs/ 目录未做列表/计数操作（本轮 runs/round84/supply 内本席文件除外）；池层原文只读未改。回传数字以主持复算为准。\n")
    with OUT.open("a", encoding="utf-8") as fh:
        fh.write("".join(s3))

    # ---------------- final assertions ----------------
    text = OUT.read_text(encoding="utf-8")
    rows = re.findall(r"^\| ((?:BY|YX|CY|CYJ|DA|BQ|HZ)-[0-9]+) \|", text, flags=re.M)
    assert len(rows) == total_unused, f"ledger rows {len(rows)} != unused {total_unused}"
    assert set(rows) == {rid for (sub, rid) in adjudged}, "ledger id set mismatch"
    elig_rows = len(re.findall(r"^\| (?:BY|YX|CY|CYJ|DA|BQ|HZ)-[0-9]+ \|.*\| eligible \|", text, flags=re.M))
    assert elig_rows == total_elig, f"eligible rows {elig_rows} != {total_elig}"
    print("FINAL OK:", OUT, OUT.stat().st_size, "bytes; rows", len(rows), "eligible", total_elig)

if __name__ == "__main__":
    main()
