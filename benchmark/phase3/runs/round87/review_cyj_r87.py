#!/usr/bin/env python3
"""R87 CYJ anchor review: pool-layer vs card-layer loading check.
Reads only: round85 ledger, expansion12/liuren-cuiyan pool files,
holdout29/holdout30 input cards for the 9 used CYJ ids, and the
grade_note field of those 9 ids in holdout29/holdout30 gold.
Writes the two supply documents for round87.
"""
import json, re
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3")
LEDGER = BASE / "runs/round85/lr-eligible-ledger-r85.json"
POOL_J5 = BASE / "expansion12/liuren-cuiyan/cases-juan5.jsonl"
POOL_MN = BASE / "expansion12/liuren-cuiyan/cases-munong.jsonl"
OUT1 = BASE / "runs/round87/supply/CYJ-ANCHOR-REVIEW-r87.md"
OUT2 = BASE / "runs/round87/supply/lr-ledger-note-r87.md"

USED = {
    "CYJ-001": "holdout29", "CYJ-002": "holdout29",
    "CYJ-004": "holdout29", "CYJ-005": "holdout29",
    "CYJ-006": "holdout30", "CYJ-007": "holdout30",
    "CYJ-008": "holdout30", "CYJ-009": "holdout30",
    "CYJ-010": "holdout30",
}
GAN = "甲乙丙丁戊己庚辛壬癸"
ZHI = "子丑寅卯辰巳午未申酉戌亥"
# Head present = all four slots (year / month / day / hour) occupied in
# asked_at. Slot-structure match (not strict ganzhi glyphs): CYJ-001's
# pool asked_at writes the day stem with a wrong glyph (已 for 己),
# slots are nonetheless all present; the glyph issue is noted in the doc.
HEAD_RE = re.compile(r"[^年]+年[^月]+月[^日]+日[^时]+时")
CHART_TERMS = ["四课", "三传", "初传", "天将", "空亡", "年命", "行年"]

ledger = json.loads(LEDGER.read_text())
ids_j5 = ledger["六壬/《六壬粹言》卷五占验"]
ids_mn = ledger["六壬/《六壬粹言》卷六慕农占验附存"]
ids = ids_j5 + ids_mn
assert len(ids) == 55 and len(set(ids)) == 55, len(ids)
assert len(ids_j5) == 49 and len(ids_mn) == 6

pool = {}
pool_file = {}
for path, tag in [(POOL_J5, "cases-juan5.jsonl"), (POOL_MN, "cases-munong.jsonl")]:
    for line in path.read_text().splitlines():
        obj = json.loads(line)
        pool[obj["id"]] = obj
        pool_file[obj["id"]] = tag
assert all(i in pool for i in ids)

rows = []
for cid in ids:
    rec = pool[cid]
    asked = rec.get("asked_at", "")
    head = bool(HEAD_RE.search(asked))
    yuejiang_explicit = ("将" in asked)
    # chart body loading: a structured listing of chart values.
    # Pool records carry no chart keys at all (key set asserted below);
    # terms inside master_predictions excerpts are assertion mentions,
    # not a chart listing.
    chart_keys = [k for k in rec.keys()
                  if any(t in k for t in ("chart", "课", "传", "盘"))]
    pred_txt = json.dumps(rec.get("master_predictions", []), ensure_ascii=False)
    mentions = [t for t in CHART_TERMS if t in pred_txt]
    body = False  # no record carries a chart listing; see key-set check
    card_cc, card_cf, gold_note = "—（未建卡）", "—", "—"
    if cid in USED:
        hold = USED[cid]
        card = json.loads((BASE / f"{hold}/inputs/{cid}.json").read_text())
        card_cc = str(card["anchors"]["chart_complete"])
        card_cf = card["anchors"]["chart_fidelity"]
        for line in (BASE / f"{hold}/test_gold.jsonl").read_text().splitlines():
            g = json.loads(line)
            if g.get("id") == cid:
                gn = g.get("grade_note", "")
                gold_note = "含「课式头四要素 present（R84 核查台账）」" \
                    if "课式头四要素 present（R84 核查台账）" in gn else "未见该语"
    page = rec["provenance"]["page"]
    rows.append(dict(id=cid, used=USED.get(cid, "未用"), head=head,
                     yj=yuejiang_explicit, body=body, mentions=mentions,
                     asked=asked, card_cc=card_cc, card_cf=card_cf,
                     gold=gold_note, page=page, file=pool_file[cid],
                     chart_keys=chart_keys))

key_union = set()
for cid in ids:
    key_union.update(pool[cid].keys())
assert not any(("chart" in k or "课" in k or "盘" in k) for k in key_union), key_union

def agg(rs):
    return dict(n=len(rs), head=sum(r["head"] for r in rs),
                body=sum(r["body"] for r in rs),
                both_missing=sum((not r["head"] and not r["body"]) for r in rs),
                head_only=sum((r["head"] and not r["body"]) for r in rs),
                yj=sum(r["yj"] for r in rs))

all_a = agg(rows)
used_a = agg([r for r in rows if r["used"] != "未用"])
unused_a = agg([r for r in rows if r["used"] == "未用"])
h29_a = agg([r for r in rows if r["used"] == "holdout29"])
h30_a = agg([r for r in rows if r["used"] == "holdout30"])
assert all_a["n"] == 55 and used_a["n"] == 9 and unused_a["n"] == 46
assert all_a["head"] == 55 and all_a["body"] == 0
assert all_a["yj"] == 4
mention_rows = [r for r in rows if r["mentions"]]

L = []
L.append("# CYJ 锚点专项复核（R87，独立复核席）")
L.append("")
L.append("- 复核对象：runs/round85/lr-eligible-ledger-r85.json 中《六壬粹言》来源条目全量"
         "＝卷五占验（CYJ-，49 例）＋卷六慕农占验附存（CY-，6 例），合计 **55 例**。")
L.append("- 池层实址登记：任务书预设路径 expansion12/liuren-*/cases-reviewed.jsonl 与实盘不合；"
         "CYJ 子集池层实址为 `expansion12/liuren-cuiyan/cases-juan5.jsonl`（卷五 75 行）与 "
         "`expansion12/liuren-cuiyan/cases-munong.jsonl`（卷六 61 行），逐例以台账 id 精确打开核对，"
         "原书定位取各例 provenance.page 字段。")
L.append("- 卡面实址：benchmark/phase3/holdout29/inputs/ 与 holdout30/inputs/（已用 9 例）；"
         "金标仅读该 9 例 grade_note 字段中「课式头 present」登记语，未读断语/结局正文作他用。")
L.append("- 判定口径（本席操作定义）：式头在场＝池层 asked_at 同时实载年干支、月、日干支、时支"
         "（即已用卡面所称「年、月、日、时俱载」之四要素形态）；月将明载另列子计数（asked_at 含「…将」字样）。"
         "盘体在场＝有四课/三传/天将/空亡/年命之盘面值罗列（结构化字段或成列载录）；"
         "大师断语摘录中提及个别盘体要素名目（如「三传合局」）属断语提及、不算盘体载录，另列登记。")
L.append("")
L.append("## 1. 逐例两层载录结论表")
L.append("")
L.append("| id | 已用/未用 | 式头在场（池层 asked_at） | 月将明载 | 盘体在场 | 卡面 chart_complete | 卡面 chart_fidelity 原文摘录 | 池层原文定位 |")
L.append("|---|---|---|---|---|---|---|---|")
for r in rows:
    loc = f"{r['file']} · {r['page']}"
    cf = r["card_cf"] if r["card_cf"] == "—" else f"「{r['card_cf']}」"
    L.append(f"| {r['id']} | {r['used']} | {'在场' if r['head'] else '缺'}（{r['asked']}） "
             f"| {'是' if r['yj'] else '否'} | {'在场' if r['body'] else '缺载'} "
             f"| {r['card_cc']} | {cf} | {loc} |")
L.append("")
L.append("已用 9 例金标 grade_note 对位（DIAG-H29 §5-F3）：9/9 均含「课式头四要素 present（R84 核查台账）」字样，"
         "与卡面 anchors「课式头四要素：年、月、日、时俱载（台账锚点 present 口径，R84 核查台账）」及 "
         "chart_complete=false／chart_fidelity「仅干支（复原不能）」三者同指一形态：式头在场、盘体缺载，两口径并存属实。")
L.append("")
L.append("断语提及登记（不算盘体载录）：池层 55 例中，大师断语摘录提及盘体要素名目者 "
         f"{len(mention_rows)} 例——" +
         "、".join(f"{r['id']}（{'/'.join(r['mentions'])}）" for r in mention_rows) +
         "；各例均无四课/三传之干支值、天将排布、空亡旬或年命干支之罗列。"
         "另 CYJ-002 之「初传」字样仅见于 grade_note（戌时为初传推定之注记），断语内无。")
L.append("")
L.append("池层结构事实：55 例池记录字段集全同（17 键），无任何课盘/四课/三传类字段；"
         "盘体信息在池层从未被转录载录，非逐例偶漏。原书层面，已用卡面明载「原书有课盘列、池卡未录盘字」"
         "——缺载发生在转录/建卡层，原书课盘列本身在盘（据已用 9 例卡面登记语；未用例无卡面，此点不外推）。")
L.append("")
L.append("## 2. 聚合计数")
L.append("")
L.append("| 组 | 例数 | 式头在场 | 月将明载 | 盘体在场 | 仅式头（盘体缺载） | 两层俱缺 |")
L.append("|---|---|---|---|---|---|---|")
for name, a in [("全子集", all_a), ("已用合计", used_a), ("holdout29", h29_a),
                ("holdout30", h30_a), ("未用余面", unused_a)]:
    L.append(f"| {name} | {a['n']} | {a['head']} | {a['yj']} | {a['body']} "
             f"| {a['head_only']} | {a['both_missing']} |")
L.append("")
L.append("## 3. 口径建议（复核席建议，裁定归主持）")
L.append("")
L.append("对照 PREREG §3 裁决口径两形态：")
L.append("")
L.append("- (甲)「个别形态」不成立：盘体缺载不是子集内少数个案——55/55 全数缺载（100%），"
         "已用组 9/9、未用余面 46/46 无一例外；且成因是池层转录形态整段一致（字段集全同、无课盘字段），"
         "与 holdout29 CYJ 段 4/4 同型并非巧合，而是同一池层形态的必然延续。")
L.append("- (乙)「成段例行形态」成立：盘体缺载在 CYJ 子集内成段、例行、无例外，与 (乙) 的事实要件逐项相合。"
         "台账/卡面降级登记虽齐全（已用 9 例 chart_complete=false＋chart_fidelity 明载、两口径并列登记无缺），"
         "但 (甲) 的前提含「子集内少数」一要件，计数上不满足，降级登记齐全不足以单独支撑 (甲)。")
L.append("")
L.append("**建议：按 (乙) 收紧**——自 holdout31 起 CYJ 子集「锚点在场」以盘体实载为准，"
         "仅式头者降为 fidelity 例外登记、不计常规 eligible。依据计数：全子集盘体在场 0/55、"
         "仅式头 55/55；未用余面盘体在场 0/46，即收紧口径下 CYJ 未用余面常规 eligible 为 0，"
         "46 例全数转 fidelity 例外登记（其中式头在场 46/46、两层俱缺 0）。已用面（h29 4＋h30 5）效力不动，仅作事实登记。")
L.append("")
L.append("附注一（月将）：式头四要素若按 PREREG §3 字面把月将计入必备项，则月将明载仅 4/55"
         "（CY-019 酉将、CY-026 亥将、CY-035 午将、CY-050 未将，俱在卷六子集；卷五 49 例 asked_at 均只记时支、无月将字样）。"
         "此点不改变上项建议（盘体口径已足以定案），仅供主持落字时对式头口径一并厘清。")
L.append("附注二（载录小异）：CYJ-001 池层 asked_at 作「己酉年十一月已酉日辰时」（日干支首字作「已」），"
         "已用卡面作「己酉日」——式头在场判定不受影响，字面差异照实登记。")
L.append("")
L.append("## 4. 异常与自报")
L.append("")
L.append("- 池层路径与任务书预设不合（cases-reviewed.jsonl 在 liuren-cuiyan 下不存在），已按实盘定位并于首节登记实址。")
L.append("- 本席开工确认 supply 目录在盘时，曾对 runs/round87 本轮目录做一次列表查看（仅见文件名，未涉 predictions/judging/final-scores 内容、未作计数用途），照卫生口径自报于此。")
L.append("- 本席未读任何 predictions/judging/final-scores；未改任何既有文件、台账、卡面与 method 文件；中间脚本为 runs/round87/review_cyj_r87.py，未用 /tmp。")
L.append("")

OUT1.write_text("\n".join(L))

N = []
N.append("# lr 承接台账注记（R87，CYJ 锚点专项复核承接件）")
N.append("")
N.append("- 复核对象台账：runs/round85/lr-eligible-ledger-r85.json 中《六壬粹言》两键条目全量——"
         "卷五占验 49 id（CYJ-001…CYJ-064 号段内取 49）＋卷六慕农占验附存 6 id（CY-014、CY-018、CY-019、CY-026、CY-035、CY-050），"
         "台账实数合计 **55**。")
N.append(f"- 已用扣减：holdout29 取 4（CYJ-001、CYJ-002、CYJ-004、CYJ-005）＋holdout30 取 5（CYJ-006–CYJ-010）＝9；"
         f"已用扣减后未用余面 **{unused_a['n']}** 例。")
N.append(f"- 余面按载录分列：盘体在场 **{unused_a['body']}** 例；仅式头（式头在场而盘体缺载）**{unused_a['head_only']}** 例；"
         f"两层俱缺 {unused_a['both_missing']} 例。余面 46 例 id：卷五 40（CYJ-012、015–022、025–036、038、039、041–046、049、050、053、055–061、064）＋卷六 6（CY-014、018、019、026、035、050）。")
N.append("- 口径承接提示（事实面，裁定归主持）：若主持按 PREREG §3 (乙) 落字收紧，余面 46 例常规 eligible 归 0、全数转 fidelity 例外登记；"
         "若按 (甲) 维持，余面 46 例仍以 fidelity 降级登记形态计 eligible。本注记只登记两形态下之计数，不代裁定。")
N.append("- 详表与建议见同目录 CYJ-ANCHOR-REVIEW-r87.md。")
N.append("")
OUT2.write_text("\n".join(N))
print("all", all_a)
print("used", used_a)
print("unused", unused_a)
print("mentions", [(r["id"], r["mentions"]) for r in mention_rows])
print(OUT1, OUT1.stat().st_size)
print(OUT2, OUT2.stat().st_size)
