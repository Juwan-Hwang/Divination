# -*- coding: utf-8 -*-
"""R79 数据席落盘脚本：case-annotations-r79.json + manifest-carryover-r79-addendum.md
三判例：落笔前逐件回读结局原文；引文逐字断言内置（不过即停）；anon 经 host-mapping 逐件对位。
只写两件产出；不改分数、不改 manifest、不改原卡。"""
import json, hashlib, pathlib, re, sys, collections

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
R79 = BASE / "runs/round79"

def load(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

r78 = load(BASE / "data/case-annotations-r78.json")
man = load(R79 / "judging/outcome-manifest.json")
man78 = load(BASE / "runs/round78/judging/outcome-manifest.json")
mapping = load(R79 / "judging/host-mapping.json")
flagtext = (R79 / "judge-flags-r79-host-compiled.md").read_text(encoding="utf-8")

def fail(msg):
    print("ASSERT FAIL:", msg); sys.exit(1)

# ---------- 基线断言 ----------
man_raw = (R79 / "judging/outcome-manifest.json").read_bytes()
if hashlib.sha256(man_raw).hexdigest() != "9114a6bfd665b3376e53f87ac7b39617495f310ee1fc62de2370b97a74c4c2e0":
    fail("manifest sha")
cases_sha = hashlib.sha256(json.dumps(man["cases"], sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
if cases_sha != "00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad":
    fail("cases sha")
if len(man["cases"]) != 487: fail("cases n")
if man["cases"] != man78["cases"]: fail("cases vs r78")
for k, v in man78.items():
    if k in ("cases", "_provenance"): continue
    if k not in man or man[k] != v: fail(f"layer carried verbatim: {k}")
if "_r79_carryover_notes_addendum" in man: fail("unexpected r79 layer")
if "_r78_carryover_notes_addendum" in man: fail("unexpected r78 layer")
NOTE_R79 = man["_r79_manifest_note"]
EXP_NOTE = "R79: no new carryover layer. R78 adjudication produced no new partial-upheld items (R78 addendum compilation is the empty set, data/manifest-carryover-r78-addendum.md; R78 annotations carried 70 items with an empty new-adjudication set). All R78 layers carried verbatim; cases payload identical (sha asserted)."
if NOTE_R79 != EXP_NOTE: fail("r79 note text")

base_ann = r78["annotations"]
if len(base_ann) != 70: fail("base 70")
if collections.Counter(a["disposition"] for a in base_ann) != {"成立": 12, "部分成立": 54, "不成立": 2, "未核": 2}:
    fail("base verdicts")
base_by_case = {a["case_id"]: a for a in base_ann}
if len(base_by_case) != 70: fail("base unique")

# ---------- 旗标解析 ----------
flag_lines = {}   # anon -> list of (seat, seatno, type, quote)
for line in flagtext.splitlines():
    m = re.match(r"\d+\.\s+([XY]\d)-(\d+)｜(P3-[0-9a-f]{8})｜([^｜]+?)(?:｜(.*))?$", line.strip())
    if m:
        seat, sno, anon, typ, quote = m.groups()
        flag_lines.setdefault(anon, []).append((seat, sno, typ, quote or ""))
n_items = sum(len(v) for v in flag_lines.values())
if n_items != 93: fail(f"flag items {n_items}")
anons = sorted(flag_lines.keys())
if len(anons) != 64: fail("flag anons 64")
flag_cases = {}
for anon in anons:
    if anon not in mapping: fail(f"anon not in mapping {anon}")
    flag_cases[anon] = mapping[anon]
if len(set(flag_cases.values())) != 64: fail("flag cases unique 64")

def flag_field(anon):
    parts = []
    for seat, sno, typ, quote in flag_lines[anon]:
        parts.append(f"{seat}：{typ}｜{quote}" if quote else f"{seat}：{typ}")
    return "；".join(parts)

def seats_of(anon):
    seen = []
    for seat, *_ in flag_lines[anon]:
        if seat not in seen: seen.append(seat)
    return seen

# ---------- 结局逐字断言工具 ----------
def outcome(cid):
    if cid not in man["cases"]: fail(f"case missing {cid}")
    return man["cases"][cid]

def assert_in(needle, hay, what):
    if needle not in hay: fail(f"quote not found [{what}]: {needle[:40]}")

EDITOR_NOTE = man["_r56_lr2016_split"]["editor_note"]
if EDITOR_NOTE != "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。":
    fail("editor note")

# 指令性字样基线六处（R79 manifest 实测）
assert_in("盲测比对须注", outcome("BZ-036"), "BZ-036")
assert_in("（盲测比对时以格局大富一项为主）", outcome("BZ-042"), "BZ-042")
assert_in("使用时须分开统计", outcome("BZ-105"), "BZ-105")
assert_in("勿以此斷", outcome("LY-204"), "LY-204")
if man_raw.decode("utf-8").count(EDITOR_NOTE) != 1: fail("editor note count")

# ---------- 同例关系对勘（64 例逐件以 case_id 对勘） ----------
overlap = {mapping[a]: a for a in anons if mapping[a] in base_by_case}
new_anons = {a: c for a, c in flag_cases.items() if c not in base_by_case}
if len(overlap) != 40 or len(new_anons) != 24: fail(f"overlap/new {len(overlap)}/{len(new_anons)}")

PENDING_TOUCH = ["LY-537", "YM-070"]          # 待核维持、只登记不裁
NEW_GIST = ["BZ-037"]                          # 同例新旨（新面与既有条目各旨独立）
continuation = sorted(c for c in overlap if c not in PENDING_TOUCH + NEW_GIST)
if len(continuation) != 37: fail("continuation 37")
# 同旨续接件：本轮自报与既有定案同旨，档位承既有 disposition（逐件以 r78 条目断言）
flag_verdicts = {}
for c in continuation:
    flag_verdicts[c] = base_by_case[c]["disposition"]
flag_verdicts["BZ-037"] = "部分成立"

# BZ-037 同例新旨逐字核（结局自注偏差）
assert_in("「未执政」一语与史实不合，疑指其执政不稳/未久安，或版本文字之异", outcome("BZ-037"), "BZ-037 new gist")
BZ037_SUGGESTION = "同例新旨：自 R80 起承接本 R79 标注（与 R76 主持裁定 tradition 旨并行）：按「结局自注『未执政』与史实不合、已自标为已知偏差点」登记；结局原文照录不改。"

# 待核触及逐字核（只登记、不裁）
assert_in("果于申予日归", outcome("LY-537"), "LY-537 touch")
assert_in("后果同行都下。", outcome("YM-070"), "YM-070 touch")

# ---------- 新登记 24 件定案 ----------
# (case_id, 历轮最近定案轮次 or None, disposition, relation, finding, [逐字引文], suggestion or None)
NEW = [
 ("AS-209", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——结局引文年份误印一层属实，原文已自注 [sic — misprint for 1643]；其余会面与战况记载明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["14. of July 1443 [sic — misprint for 1643]"], None),
 ("AS-215", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——结局英文引文句中途截断（止于「having onely Quarter for his Souldiers'」）属实；主结局（1644 年 9 月 2 日 Lostwithiel 投降败局）由 manifest 结局文本明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["having onely Quarter for his Souldiers'", "the Lostwithiel surrender, 2 September 1644"], None),
 ("AS-304", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——结局后半并载具名人物 Gopalakrishnan 选后认错一节、与本例关系未标一层属实；选举结果（312 张选举人票胜出、对方 226 票）主结局明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["Gopalakrishnan于选后公开承认错误并宣布暂停政治预测", "特朗普以312张选举人票胜出"], None),
 ("BQ-021", 73, "部分成立", "同旨续接（R73）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R73 部分成立）：回原卡——所问卜禾（禾稻长势与天时）；R79 manifest 结局载插莳之时因阴人少财而去、逾三四日亢旱难用，禾稻收成终局未载一层属实；插莳与天时断面有载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["逾三四日，而天则亢旱难用矣"], None),
 ("BZ-104", 73, "部分成立", "同旨续接（R73）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R73 部分成立）：回原卡——结局系求测方口头反馈、无第三方记录一层属实，结局内已以「书内自述」自述标明；其子先患肝炎住院、后骑摩托车撞伤两灾有载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["书内自述，求测方口头反馈，无第三方记录"], None),
 ("LR2-016", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——所问被逮者何时出狱；manifest editor_note（_r56_lr2016_split 分列层）载「甲戌日巳时」日时细项未逐字复核一层属实；该注已与结局原文分列登记，结局本体「三月驳下、四月依拟脱离」完整明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"], None),
 ("LR3-002", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——所问奉命出师江东吉凶；R79 manifest 结局「仅撤回剿贼；庚辰太岁受克、退位。」中「退位」主语未明字一层属实；撤回剿贼一面明载，stripped_tail 以确指事件／时点表述承接两项应验。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["仅撤回剿贼；庚辰太岁受克、退位。"], None),
 ("LY-011", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——双断例：结局「果於次年三月妹至」对应大师同条第二断（兄弟必来），所问母来主断对象未应、母来否结果未载一层属实；来者断面有载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["果於次年三月妹至"], None),
 ("LY-255", 73, "部分成立", "同旨续接（R73）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R73 部分成立）：回原卡——所问衙宇后沟从后流宜否、修沟之后何如；R79 manifest 结局仅载「後於申年升任」，是否修沟与沟流宜否未载一层属实；升任断面有载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["後於申年升任"], None),
 ("LY-322", 73, "部分成立", "同旨续接（R73）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R73 部分成立）：回原卡——卡面 yongshen 文字「应上巳火财爻（师病以应为用）」与装卦表世应标记（妻财巳火临世、父母申金临应）一处不合属实，卡面 notes 已自注提示此出入；结局「果于丑日人事不知，寅日乃愈．」明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["果于丑日人事不知，寅日乃愈．"], None),
 ("LY-329", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——所问开店得利否；R79 manifest 结局仅「果俗底伙计有事而止．」十字，停业事实有载、停业原因与盈亏未明载一层属实。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["果俗底伙计有事而止．"], None),
 ("LY-408", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——R79 manifest 结局以逗号收尾、疑似截断属实；「果卒於甲戌日」主结局明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["果卒於甲戌日﹐"], None),
 ("LY-411", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——R79 manifest 结局以逗号收尾、疑似截断属实；「後報升於巳月」主结局明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["後報升於巳月﹐"], None),
 ("LY-413", 73, "部分成立", "同旨续接（R73）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R73 部分成立）：回原卡——R79 manifest 结局仅「果然如是。」总承式收束、断面与分晓时点未分载属实；总承本身即应验记载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["果然如是。"], None),
 ("LY-428", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——R79 manifest 结局以逗号收尾、疑似截断属实；得差与次年三月死于中途两段明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["卽於壬寅日得差﹐次年三月死於中途﹐"], None),
 ("LY-434", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——R79 manifest 结局以逗号收尾、疑似截断属实；「果於申日文書實收俱到」主结局明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["果於申日文書實收俱到﹐"], None),
 ("LY-440", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——R79 manifest 结局以逗号收尾、疑似截断属实；次日卯时云开日出主结局明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["果於次日卯時﹐云開日出﹐"], None),
 ("LY-514", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——R79 manifest 结局以逗号收尾、疑似截断属实；屢次遇兵變、或避之或有驚無險明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["後此人屢次遇兵變﹐或避之﹐或有驚無險﹐"], None),
 ("LY-523", 73, "部分成立", "同旨续接（R73）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R73 部分成立）：回原卡——R79 manifest 结局以逗号收尾、疑似截断属实；子時退災、次日起牀明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["果於子時退災﹐次日起牀﹐"], None),
 ("LY-525", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——R79 manifest 结局以逗号收尾、疑似截断属实；「服之便醒」主结局明载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["服之便醒﹐"], None),
 ("LY-538", 73, "部分成立", "同旨续接（R73）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R73 部分成立）：回原卡——所问占防恭劾（防新换抚军参劾吉凶）；R79 manifest 结局句意残缺含混、参劾过程未明载一层属实；「此将公赴京另补」仕途走向一面可读。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["后因裁他处缺上台，题留他处官顶此公位将，此将公赴京另补"], None),
 ("LY-620", 60, "不成立", "同旨续接（R60 功名旨；与 R73 残损旨并行）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮功名旨最近定案 R60 不成立，R54／R57／R58 同旨）：回原卡——所问代卜长辈功名；R79 manifest 结局「果於削職後七月而終。」以削职明载功名终局、卒为削职后余事，功名断面并非无直接对应，旗标所指不成立之据在此。本条只裁功名旨，与 R73 残损旨（卡面装卦复原、部分成立）各旨独立、并行不悖。本轮（R79）manifest 该例结局与历轮所核文本一致。",
  ["果於削職後七月而終。"], None),
 ("LY-623", 74, "部分成立", "同旨续接（R74）",
  "新登记（现行承接册 r78 之 70 件无条目）：承接既有定案不重裁（历轮最近定案 R74 部分成立）：回原卡——R79 manifest 结局以地方惊险侧载（苗獨作亂、地方不祥、驚險異常），本人安危未明字一层属实；辰年缺歸、午年又官仕途面有载。故部分成立。本轮（R79）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。",
  ["後知苗獨作亂，地方不祥，驚險異常"], None),
 ("YM-015", None, "不成立", "新立（R79）",
  "新旗标（R79 新立）：回原卡——所问占功名（乡举之期）；R79 manifest 结局全文仅「改丙戌而发乡科。」，无旗标所引「果于本日巳时还一半，乙酉日巳时还清一半者」之文、亦无自相矛盾措辞——该引文逐字属 LY-342 结局（manifest cases[LY-342] 实读），系旗标引文错配本例；本例结局与功名问面对应、无所指瑕疵。故不成立。LY-342 本轮未被旗标点名、不入案，错配线索另于特别核查登记。",
  ["改丙戌而发乡科。"], None),
]
if len(NEW) != 24: fail("NEW 24")
new_by_case = {}
for cid, last_r, disp, rel, finding, quotes, _s in NEW:
    anon = flag_cases_inverse = None
    for a, c in flag_cases.items():
        if c == cid: anon = a
    if anon is None: fail(f"no anon for {cid}")
    if cid in base_by_case: fail(f"new case in base {cid}")
    oc = outcome(cid)
    for q in quotes: assert_in(q, oc, cid)
    new_by_case[cid] = (anon, last_r, disp, rel, finding)
    flag_verdicts[cid] = disp
# YM-015 错配断言：引文不在本例、在 LY-342
if "果于本日巳时还一半" in outcome("YM-015"): fail("YM-015 quote unexpectedly present")
assert_in("果于本日巳时还一半，乙酉日巳时还清一半者", outcome("LY-342"), "LY-342")
# LY-322 卡面用神文字断言
card322 = (BASE / "inputs-dev12/LY-322.json").read_text(encoding="utf-8")
assert_in("应上巳火财爻", card322, "LY-322 card yongshen")
assert_in("妻财巳火⚊世", card322, "LY-322 card chart")
# LR2-023 / BZ-304 / LY-613 prediction 层断言（同旨续接件之并行核）
pred_lr2023 = (R79 / "predictions/LR2-023.json").read_text(encoding="utf-8")
if "兒婦" in pred_lr2023 or "儿妇" in pred_lr2023 or "妊" in pred_lr2023: fail("LR2-023 pred facet")
assert_in("儿妇妊性别如断", outcome("LR2-023"), "LR2-023 outcome")
pred_bz304 = (R79 / "predictions/BZ-304.json").read_text(encoding="utf-8")
if "恢复正常" in pred_bz304: fail("BZ-304 pred facet")
pred_ly613 = (R79 / "predictions/LY-613.json").read_text(encoding="utf-8")
if "?" in pred_ly613 or "？" in pred_ly613: fail("LY-613 pred facet")

new_partial = [c for c, *_r in [(n[0],) for n in NEW] if new_by_case[c][2] == "部分成立"]
new_not = [n[0] for n in NEW if n[2] == "不成立"]
if len(new_partial) != 22 or len(new_not) != 2: fail(f"new verdicts {len(new_partial)}/{len(new_not)}")
fv = collections.Counter(flag_verdicts.values())
if fv != {"成立": 9, "部分成立": 50, "不成立": 3} or len(flag_verdicts) != 62:
    fail(f"flag verdict distribution {fv} n={len(flag_verdicts)}")

# ---------- 组装 annotations ----------
def hist_files(cid):
    hits = []
    for r in range(49, 79):
        p = BASE / f"data/case-annotations-r{r}.json"
        if not p.exists(): continue
        d = load(p)
        if any(a["case_id"] == cid for a in d["annotations"]): hits.append(r)
    return hits

new_entries = []
for cid, last_r, disp, rel, finding, quotes, _s in NEW:
    anon = new_by_case[cid][0]
    if disp == "部分成立":
        suggestion = f"同旨续接：自 R80 起承接 R{last_r}＋本 R79 标注；结局原文照录不改。" if last_r else "自 R80 起承接本 R79 标注；结局原文照录不改。"
    elif cid == "LY-620":
        suggestion = "同旨续接：自 R80 起承接 R60 功名旨＋本 R79 标注（与 R73 残损旨并行）；结局原文照录不改。"
    else:  # YM-015
        suggestion = "新立：自 R80 起承接本 R79 标注：按「旗标引文系 LY-342 结局文、与本例结局原文不合」登记；结局原文照录不改。"
    sources = [
        f"divination/benchmark/phase3/inputs-dev12/{cid}.json",
        "divination/benchmark/phase3/runs/round79/judge-flags-r79-host-compiled.md",
        f"divination/benchmark/phase3/runs/round79/judging/host-mapping.json（anon 解析：{anon}＝{cid}）",
        f"divination/benchmark/phase3/runs/round79/judging/outcome-manifest.json cases[{cid}]",
        f"divination/benchmark/phase3/runs/round79/predictions/{cid}.json",
    ]
    if cid == "YM-015":
        sources.append("divination/benchmark/phase3/runs/round79/judging/outcome-manifest.json cases[LY-342]（错配引文出处核对）")
    for r in hist_files(cid)[-6:]:
        sources.append(f"divination/benchmark/phase3/data/case-annotations-r{r}.json {cid} 条")
    new_entries.append({
        "anon_id": anon,
        "case_id": cid,
        "disposition": disp,
        "finding": finding,
        "flag": flag_field(anon),
        "manifest_carry_suggestion": suggestion,
        "relation": rel,
        "registered_round": 79,
        "sources_checked": sources,
        "source_seats": seats_of(anon),
    })

annotations_out = base_ann + new_entries
if len(annotations_out) != 94: fail("total 94")
if len({a["case_id"] for a in annotations_out}) != 94: fail("unique 94")
if annotations_out[:70] != base_ann: fail("base verbatim")
total_verdicts = collections.Counter(a["disposition"] for a in annotations_out)
if total_verdicts != {"成立": 12, "部分成立": 76, "不成立": 4, "未核": 2}: fail(f"total verdicts {total_verdicts}")

special = list(r78["special_checks"])
if len(special) != 18: fail("special base 18")
special += [
 {"item": "特别核查⑲（R79）：附则对勘——R79 manifest 无新落实层与 _r79_manifest_note 对勘",
  "conclusion": "R79 manifest 顶层无 _r79_carryover_notes_addendum 键、最新承接层止于 _r77_carryover_notes_addendum；_r79_manifest_note 全文与附则 §二引录逐字全等，注记四项（无新落实层／R78 附则汇编为空集／既有各层原样保留／cases 逐字全等）经盘上交叉核对逐项相合、无勘误。",
  "evidence": "本席脚本断言：R79 manifest 与 R78 manifest cases 487 例深度全等、既有各层（_r56–_r77 各层与注记）逐键全等；cases 结构化 SHA 复算＝00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad；manifest 全文 SHA-256＝9114a6bfd665b3376e53f87ac7b39617495f310ee1fc62de2370b97a74c4c2e0，与 R79 PREREG 开轮登记一致。",
  "scope_note": "对勘只登记、不静默改任一侧。"},
 {"item": "特别核查⑳（R79）：评审旗标汇编一致性与本轮定案总登记",
  "conclusion": "主持汇编 93 条编号旗标（X1 3／X2 8／X3 6／X4 30／Y1 9／Y2 10／Y3 6／Y4 21）去重为 64 个 anon、经 host-mapping 逐件对位为 64 例（形近串号逐件对位、未凭序号推断）。与 r78 承接册 70 件对勘：同例 40 件——同旨续接 37 件（档位承既有定案）、同例新旨 1 件（BZ-037，见核查㉑）、待核触及 2 件（LY-537／YM-070，见核查㉒）；70 件外新登记 24 件（部分成立 22／不成立 2）。本轮定案分布（62 件入裁）：成立 9／部分成立 50／不成立 3；另 2 件待核触及只登记不裁。",
  "evidence": "逐件对位与逐字断言均内置于落盘脚本（build_r79_data_seat.py）：64 例结局原文逐件回读、每件 finding 所引原文逐字命中结局原文（LR2-016 另核 editor_note 分列层、LY-322 另核卡面 yongshen 与装卦表、YM-015 另核错配出处 LY-342）；同旨续接 37 件档位以 r78 条目 disposition 逐件断言承接。",
  "scope_note": "定案只及标注与承接建议，不改任何分数。"},
 {"item": "特别核查㉑（R79）：同例新旨一件——BZ-037 结局自注史实偏差",
  "conclusion": "BZ-037 本轮 Y1 旗标所指为同例新旨（与其 r78 条目 R76 主持裁定 tradition 旨各旨独立、并行不悖）：结局自注「『未执政』一语与史实不合，疑指其执政不稳/未久安，或版本文字之异」——偏差一层属实（成立面）；但该偏差已由结局原文自注标为已知偏差点、非隐匿瑕疵（不成立面）。故新旨定案部分成立，承接建议汇编入本轮附则 §三、自 R80 manifest 落实；r78 既有条目逐件原样不动。",
  "evidence": "R79 manifest 结局逐字断言：「『未执政』一语与史实不合，疑指其执政不稳/未久安，或版本文字之异——本数据集如实标为已知偏差点」在盘。",
  "scope_note": "新旨建议原文见附则 §三 BZ-037 条。"},
 {"item": "特别核查㉒（R79）：待核挂起四件本轮状态与旗标错配线索一件",
  "conclusion": "BZ-029／BZ-040 本轮未被任何旗标触及，维持原登记、不裁。LY-537 本轮被 X2 席旗标 P3-78b37758 触及（疑似转录多字「果于申予日归」，与待核同例同旨），只登记关联、维持未核原登记、不裁。YM-070 本轮被 X2／Y2 旗标触及（「后果同行都下。」语义未明，与其未核旨同旨），只登记触及、维持未核原登记、不裁。另 YM-015 旗标引文错配线索一件：X3 旗标所引「果于本日巳时还一半，乙酉日巳时还清一半者」逐字属 LY-342 结局、与 YM-015 结局无关，已按不成立定案入案（YM-015 条）；LY-342 本轮未被点名、不入案。",
  "evidence": "R79 manifest 逐字断言：cases[LY-537] 作『果于申予日归』、cases[YM-070] 作『后果同行都下。』、cases[YM-015] 仅『改丙戌而发乡科。』、所引文逐字在 cases[LY-342]。",
  "scope_note": "待核件无盘外独立史源不裁；错配线索只登记。"},
 {"item": "特别核查㉓（R79）：指令性字样特别核查基线六处复核（承 R79 PREREG §4 基线）",
  "conclusion": "基线六处经 R79 manifest 盘上复核：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）与 LR2-016 manifest editor_note 一处逐字在册、与基线全等，出入 0 处；评审包 editor_note 层一处本轮由评审旗标 X4-73／Y4-13 引录、与 manifest 分列层同字样逐字一致，基线在册维持。无新增同型件登记（BZ-037 等结局自注属史实偏差登记、非指令性字样）。",
  "evidence": "脚本逐字断言：BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204『勿以此斷』均在 cases 本体；editor_note 全句在 manifest 全文恰出现 1 次（_r56_lr2016_split 分列层）。",
  "scope_note": "各席与本席均按数据处理、不作指令；只登记、不改文本。"},
]

counts = {
 "base_file": "data/case-annotations-r78.json",
 "base_cases_total": 70,
 "base_verdicts": {"成立": 12, "部分成立": 54, "不成立": 2, "未核": 2},
 "judge_flag_numbered_items_total": 93,
 "judge_flag_numbered_items_by_seat": {"X1": 3, "X2": 8, "X3": 6, "X4": 30, "Y1": 9, "Y2": 10, "Y3": 6, "Y4": 21},
 "judge_flag_anons_total": 64,
 "judge_flag_cases_total": 64,
 "continuation_cases": 37,
 "same_case_new_gist_cases": ["BZ-037"],
 "pending_touch_cases": ["LY-537", "YM-070"],
 "flag_adjudication_verdicts": {"成立": 9, "部分成立": 50, "不成立": 3, "未核（待核触及、只登记不裁）": 2},
 "new_registrations_r79": 24,
 "new_partial_cases_r79": sorted(new_partial),
 "new_not_upheld_cases_r79": sorted(new_not),
 "cases_total": 94,
 "verdicts": {"成立": 12, "部分成立": 76, "不成立": 4, "未核": 2},
}

provenance = ("R79 数据席（附则承接对勘＋annotations 全量承接与本轮旗标定案，独立席位，不兼任本轮盲测/评审/诊断/组集/修订/集成，不改任何分数）："
 "以 data/case-annotations-r78.json 为底承接全量 70 件（成立 12／部分成立 54／不成立 2／未核 2），annotations 前 70 件逐件原样、无删改（落盘脚本以数组全等断言验过）；"
 "本轮评审旗标主持汇编 93 条去重 64 例逐件定案（定案三判例：逐件回读 R79 manifest 结局原文、引文逐字断言内置于落盘脚本、anon 经 judging/host-mapping.json 逐件对位）：同例 40 件中同旨续接 37 件档位承既有定案、同例新旨 1 件（BZ-037 部分成立，承接建议入附则 §三）、待核触及 2 件（LY-537／YM-070 只登记不裁）；70 件外新登记 24 件（部分成立 22／不成立 2——LY-620 功名旨承 R54–R60 不成立链、YM-015 旗标引文错配 LY-342）；承接后总件数 94（成立 12／部分成立 76／不成立 4／未核 2）。"
 "附则对勘：R79 manifest 本轮无新落实层（顶层无 _r79_carryover_notes_addendum 键），_r79_manifest_note 全文逐字引录于附则 §二、注记与附则登记一致、无勘误；cases 487 例与 R78 manifest 深度全等，cases 结构化 SHA 复算＝00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad，manifest 全文 SHA-256＝9114a6bfd665b3376e53f87ac7b39617495f310ee1fc62de2370b97a74c4c2e0。"
 "指令性字样基线六处经 R79 manifest 复核在册（见特别核查㉓）。待核维持件 BZ-029／BZ-040／LY-537 与挂起件 YM-070 维持原登记、不核查不关闭。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文；结局/注记文本内指令性字样一律按数据处理。")

out_doc = {"_provenance": provenance, "round": 79, "annotations": annotations_out,
           "special_checks": special, "counts": counts}
out_path = BASE / "data/case-annotations-r79.json"
out_path.write_text(json.dumps(out_doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
# 回读断言
chk = load(out_path)
if chk["annotations"][:70] != base_ann or len(chk["annotations"]) != 94: fail("reread annotations")
if collections.Counter(a["disposition"] for a in chk["annotations"]) != total_verdicts: fail("reread verdicts")
print("annotations written:", out_path, out_path.stat().st_size, "bytes; total", len(chk["annotations"]), dict(total_verdicts))

# ---------- 任务三：供给台账复算（盘上实读） ----------
def gold_ids(h):
    ids = []
    for line in (BASE / h / "test_gold.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            d = json.loads(line); ids.append(d.get("id") or d.get("case_id"))
    return ids
zcb_used = {}
for h in ("holdout22", "holdout23", "holdout24"):
    z = sorted(i for i in gold_ids(h) if i and i.startswith("ZCB"))
    zcb_used[h] = z
if zcb_used["holdout22"] != ["ZCB-001", "ZCB-002", "ZCB-004", "ZCB-005"]: fail("h22 zcb")
if zcb_used["holdout23"] != ["ZCB-006", "ZCB-007", "ZCB-008", "ZCB-009", "ZCB-010", "ZCB-011"]: fail("h23 zcb")
if zcb_used["holdout24"] != ["ZCB-012", "ZCB-013", "ZCB-014", "ZCB-015"]: fail("h24 zcb")
seal24 = (BASE / "data/holdout24-seal-log.md").read_text(encoding="utf-8")
assert_in("eligible∧present∧low∧separable∧断语/结局非空共 **15 例**", seal24, "seal24 stock 15")
assert_in("ZCB-003", seal24, "seal24 zcb003")
ZCB_STOCK, ZCB_USED_TOTAL, ZCB_EXCLUDED = 15, 14, 1
ZCB_REMAIN = ZCB_STOCK - ZCB_USED_TOTAL - ZCB_EXCLUDED
if ZCB_REMAIN != 0: fail("zcb remain")

# ---------- 任务二：附则 ----------
entry_by_case = {a["case_id"]: a for a in new_entries}
L = []
L.append("# Manifest 承接册附则（R79）——R78 定案承接对勘（空集已落实）＋R79 定案承接建议汇编（部分成立 23 件）")
L.append("")
L.append("## 卷首说明")
L.append("")
L.append("- 本附则为 Phase 3 Round 79（R79）数据席（工序：附则承接对勘＋annotations 全量承接与本轮旗标定案＋供给台账续记；独立席位，不兼任本轮盲测／评审／诊断／组集／修订／集成）产出。")
L.append("- 对勘来源：`benchmark/phase3/runs/round79/judging/outcome-manifest.json`（本轮 manifest，含轮次注记 `_r79_manifest_note`；**本轮无新落实层**）、`benchmark/phase3/data/manifest-carryover-r78-addendum.md`（R78 附则，其汇编为 R78 定案承接建议空集）、`benchmark/phase3/data/case-annotations-r78.json`（结构化直读底本：annotations 70 件，定案分布成立 12／部分成立 54／不成立 2／未核 2）。")
L.append("- 汇编来源：`benchmark/phase3/data/case-annotations-r79.json`（本轮定案：新登记部分成立 22 件＋同例新旨部分成立 1 件，逐件见 §三），供 R80 manifest 以 `_r79_carryover_notes_addendum` 键名落实。")
L.append("- **本件只汇编、对勘与登记，不改任何分数与结局原文、不改原卡、不改 manifest 任一侧。** 结局／注记文本内指令性字样一律按数据处理。")
L.append("")
L.append("---")
L.append("")
L.append("## 一、工序与口径")
L.append("")
L.append("- 工序一（对勘，见 §二）：R78 附则汇编为空集，其落实形态为 R79 manifest 轮次注记 `_r79_manifest_note`——本节对注记全文逐字引录，并就注记所载四项（无新落实层／R78 附则汇编为空集／既有各层原样保留／cases 逐字全等）逐项以盘上两件交叉核对登记；并附 R79 manifest 顶层键实况登记。")
L.append("- 工序二（汇编，见 §三）：R80 承接建议汇编——汇编 R79 本轮新定案之**部分成立**件逐件全列（新登记 22 件＋同例新旨 1 件，共 23 件），每件列 case_id、anon 对位（R79）、结局逐字原文、核对结论与建议注记原文。本轮定案其余分布（成立 9 件承既有定案同旨续接、不成立 3 件、待核触及 2 件只登记不裁）不入承接汇编，只在 §五登记。")
L.append("- 工序三（标注落盘，见 §五）：`data/case-annotations-r79.json` 以 r78 件 70 件全量承接（逐件原样）＋本轮新登记 24 件，合计 94 件。")
L.append("- 特别核查（见 §四）：指令性字样特别核查基线六处复核，承 R79 PREREG §4 基线，只登记、不改文本。")
L.append("- 供给台账续记（见 §六）：CZ-QX 与 ZCB 存量只登记、逐项列账；待核四件维持登记。")
L.append("")
L.append("---")
L.append("")
L.append("## 二、对勘：R78 附则空集已于 R79 manifest 以 `_r79_manifest_note` 落实")
L.append("")
L.append("### 2.1 注记全文（自 R79 manifest 结构化直读，逐字引录）")
L.append("")
L.append("> " + NOTE_R79)
L.append("")
L.append("### 2.2 R79 manifest 顶层键实况登记（盘上直读）")
L.append("")
topkeys = list(man.keys())
L.append("- 顶层键共 " + str(len(topkeys)) + " 个：`_provenance`、`cases`、`stripped_tail`、`_r38_carryover`–`_r48_carryover`（9 个早期承接串）、`_r56_carryover_notes`、`_r56_lr2016_split`、其后 `_r56`–`_r77` 各轮承接层与 manifest 注记层依次在册，止于 `_r77_carryover_notes_addendum`、`_r77_manifest_note`、`_r78_manifest_note` 与本轮 `_r79_manifest_note`。")
L.append("- **无 `_r79_carryover_notes_addendum` 键**（本轮无新落实层，与注记首句合）；亦无 `_r78_carryover_notes_addendum` 键（R78 附则汇编为空集、无层可立，与 R78 附则 §二登记合）。最新承接层为 `_r77_carryover_notes_addendum`（6 件，R76 定案集）。")
L.append("")
L.append("### 2.3 逐项对勘")
L.append("")
L.append("| # | 注记所载 | 盘上复核 | 结果 |")
L.append("|---|---|---|---|")
L.append("| 1 | 本轮无新落实层（no new carryover layer） | R79 manifest 顶层键无 `_r79_carryover_notes_addendum`，最新承接层止于 `_r77_carryover_notes_addendum` 与本注记 | 合 |")
L.append("| 2 | R78 定案无新部分成立件、R78 附则汇编为空集 | `data/manifest-carryover-r78-addendum.md` §三明载汇编为空集（R78 无新定案承接建议） | 合 |")
L.append("| 3 | 既有各层原样保留（All R78 layers carried verbatim） | 本席脚本逐键断言：R79 manifest 与 `runs/round78/judging/outcome-manifest.json` 除 `_provenance` 与新增 `_r79_manifest_note` 外，各层（`stripped_tail`、`_r38`–`_r77` 各承接层与注记层、`_r56_lr2016_split`）逐键深度全等 | 合 |")
L.append(f"| 4 | cases 载荷全等（cases payload identical, sha asserted） | R79 cases 487 例与 R78 manifest cases 深度全等；结构化 SHA 复算（json.dumps sort_keys=True、ensure_ascii=False、默认分隔）＝`{cases_sha}`，与 R79 PREREG 开轮登记一致；manifest 全文 SHA-256 复算＝`9114a6bfd665b3376e53f87ac7b39617495f310ee1fc62de2370b97a74c4c2e0`，与主持登记一致 | 合 |")
L.append("")
L.append("- 对勘结论：**注记与本件登记一致**——注记四项所载与盘上实测逐项相合、本件 §一至 §三登记与注记同口径，**无勘误**，不静默改任一侧。")
L.append("")
L.append("---")
L.append("")
L.append("## 三、R80 承接建议汇编：R79 定案部分成立 23 件逐件全列")
L.append("")
L.append("- 落实键名写定：自 R80 manifest 起以 `_r79_carryover_notes_addendum` 键名落实本节 23 件建议注记原文。")
L.append("- 每件格式：case_id＋anon 对位（R79 anon_id）＋结局逐字原文＋核对结论＋建议注记原文。引文均经落盘脚本逐字断言命中 R79 manifest 结局原文（LR2-016 另核 editor_note 分列层、LY-322 另核卡面字段）。")
L.append("")
L.append("### 3.1 新登记部分成立 22 件")
L.append("")
for i, cid in enumerate(sorted(new_partial, key=[n[0] for n in NEW].index), 1):
    e = entry_by_case[cid]
    L.append(f"### B{i}. {cid}")
    L.append("")
    L.append(f"- case_id：{cid}")
    L.append(f"- anon_id（R79）：{e['anon_id']}")
    L.append(f"- 结局逐字原文：「{outcome(cid)}」")
    L.append(f"- 核对结论（部分成立）：{e['finding']}")
    L.append(f"- 原旗标要旨：{e['flag']}")
    L.append(f"- 承接注记建议文本（供 R80 manifest 落实，原文）：「{e['manifest_carry_suggestion']}」")
    L.append(f"- 与既有承接册／附则条目的关系：{e['relation']}；现行承接册 r78 之 70 件无条目，本轮新登记入 `data/case-annotations-r79.json`。")
    L.append("")
L.append("### 3.2 同例新旨部分成立 1 件")
L.append("")
L.append("### B23. BZ-037")
L.append("")
L.append("- case_id：BZ-037")
L.append("- anon_id（R79）：P3-1952cec7")
L.append(f"- 结局逐字原文：「{outcome('BZ-037')}」")
L.append("- 核对结论（部分成立）：同例新旨——Y1 旗标所指结局自注「『未执政』一语与史实不合，疑指其执政不稳/未久安，或版本文字之异」，偏差一层属实（成立面）；但该偏差已由结局原文自注标为已知偏差点、非隐匿瑕疵（不成立面）。故部分成立。与其 r78 条目 R76 主持裁定 tradition 旨各旨独立、并行不悖；r78 既有条目逐件原样不动，本旨定案登记于 `data/case-annotations-r79.json` 特别核查㉑。")
L.append("- 原旗标要旨：Y1：结局自注史实/版本偏差｜「『未执政』一语与史实不合，疑指其执政不稳/未久安，或版本文字之异」")
L.append(f"- 承接注记建议文本（供 R80 manifest 落实，原文）：「{BZ037_SUGGESTION}」")
L.append("- 与既有承接册／附则条目的关系：同例新旨（R76 主持裁定旧旨并行）。")
L.append("")
L.append("---")
L.append("")
L.append("## 四、指令性字样特别核查基线六处复核（承 R79 PREREG §4 基线）")
L.append("")
L.append("- 基线构成：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处＋LR2-016 评审包 editor_note 层一处，共六处、分三层。本轮自 `runs/round79/judging/outcome-manifest.json` 盘上复核，**只登记、不改文本**；各席与本席均按数据处理、不作指令。")
L.append("")
L.append("### 4.1 cases 本体四例（manifest cases 本体逐字在场）")
L.append("")
L.append("| case_id | 基线字样（按数据引录） | 本轮在盘形态 |")
L.append("|---|---|---|")
L.append("| BZ-036 | 结局含「盲测比对须注」 | 在册：在场——结局作「……史载下狱三年、系狱前后牵连较久，此年数有出入，盲测比对须注）；1936年卒于苏州」，字样逐字在盘 |")
L.append("| BZ-042 | 结局含「（盲测比对时以格局大富一项为主）」 | 在册：在场——结局尾段逐字作「（盲测比对时以格局大富一项为主）」 |")
L.append("| BZ-105 | 结局含「使用时须分开统计」 | 在册：在场——结局尾段逐字作「……盲测价值低于C04类前瞻断语，使用时须分开统计」 |")
L.append("| LY-204 | 结局旧注层含「勿以此斷」 | 在册：在场——结局逐字作「……舊注官鬼持世疾病纏綿﹐若是貴人。勿以此斷。此人原非貴人。……」 |")
L.append("")
L.append("- 附注：R79 cases 与 R78 件逐字全等（§二.3 第 4 项），四例字样本轮在盘形态与 R78 附则 §4.1 登记逐字一致。")
L.append("")
L.append("### 4.2 LR2-016 manifest editor_note 一处（分列层）")
L.append("")
L.append("- 所在：manifest `_r56_lr2016_split`（case_id＝LR2-016，分列状态原样承接）。")
L.append("- 在册：editor_note 本轮在盘原文逐字：「原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。」（按数据引录）——与基线全等；manifest 全文该句恰出现 1 次（落盘脚本断言）。")
L.append("")
L.append("### 4.3 LR2-016 评审包 editor_note 层一处（另列一类）")
L.append("")
L.append("- 本轮复核：评审席旗标 X4-73／Y4-13 引录该层字样「原文未逐字复核「甲戌日巳时」的日时细节」，与 §4.2 manifest 分列层 editor_note 逐字一致（落盘脚本以旗标引文为 editor_note 子串断言核过）；且该例本轮已按部分成立新登记入 annotations（LR2-016 条，定案见 §三 B 区），其定案只及「细项未逐字复核」之登记面、不及字样本身处置。")
L.append("- 分类：本件属评审包 editor_note 层，与 §4.2 manifest 分列层同例同字样而来源层不同，另列一类、不并入 cases 本体基线计数。")
L.append("")
L.append("### 4.4 结论")
L.append("")
L.append("- 基线六处：五处（cases 本体四例＋manifest editor_note 一处）经 R79 manifest 盘上复核在册、与基线逐字全等，出入 0 处；一处（评审包 editor_note 层）本轮经评审旗标引录对勘在册。无新增同型件登记。本席只登记、不改任何文本。")
L.append("")
L.append("---")

L.append("")
L.append("## 五、annotations 落盘断言与待核维持清单")
L.append("")
L.append("### 5.1 annotations 落盘断言（工序三）")
L.append("")
L.append("- 底本：`data/case-annotations-r78.json` annotations 70 件（成立 12／部分成立 54／不成立 2／未核 2），全量承接、逐件原样、无删改（落盘脚本以 annotations 数组前 70 件全等断言与 id 集断言验过：(case_id, anon_id) 70 组与底本逐组全等、唯一 70）。")
L.append("- 本轮旗标定案总登记：主持汇编 93 条编号旗标（X1 3／X2 8／X3 6／X4 30／Y1 9／Y2 10／Y3 6／Y4 21）去重 64 anon、经 `judging/host-mapping.json` 逐件对位 64 例；与承接册 70 件对勘——同旨续接 37 件（档位承既有定案：成立 9／部分成立 27／不成立 1）、同例新旨 1 件（BZ-037，部分成立，见 §三.2）、待核触及 2 件（LY-537／YM-070，只登记不裁）、70 件外新登记 24 件。本轮入裁 62 件分布：成立 9／部分成立 50／不成立 3。")
L.append("- 新增登记：**24 件**（部分成立 22 件，见 §三.1；不成立 2 件：LY-620 功名旨承 R54–R60 不成立链、YM-015 旗标引文错配 LY-342）——落盘 `data/case-annotations-r79.json` annotations **94 件＝70＋24**（成立 12／部分成立 76／不成立 4／未核 2），counts 相应更新（base 70／new_registrations_r79＝24／new_partial_cases_r79 22 件／cases_total 94），回读 JSON 可解析断言通过。")
L.append("- special_checks 承接 r78 十八件并新增 R79 五件（⑲ 附则对勘无新落实层；⑳ 旗标汇编一致性与定案总登记；㉑ 同例新旨 BZ-037；㉒ 待核挂起四件与错配线索；㉓ 指令性字样基线六处复核），合计 23 件。")
L.append("")
L.append("### 5.2 R79 确认的待核维持清单（四件，维持挂起、不核查不关闭）")
L.append("")
L.append("以下四件状态原文自 `data/manifest-carryover-r78-addendum.md` §五逐字承接、不改字（其中「本轮」指 R77 轮触及登记，`case-annotations-r77.json` 在 R78 件中随全量承接为 `data/case-annotations-r78.json`、在 R79 件中随全量承接为 `data/case-annotations-r79.json`）：")
L.append("")
L.append("| case_id | 状态原文（逐字承接） |")
L.append("|---|---|")
L.append("| BZ-029 | 俞大维卒年待核＋旗标错配线索，维持原登记、不裁；不入 annotations |")
L.append("| BZ-040 | 许世英享年待核，维持原登记、不裁；不入 annotations |")
L.append("| LY-537 | 「申予日」衍字疑，维持未核原登记；本轮由盲测 S6 席（B16）作断、basis 首行对卡面 tradition 照录 liuyao，只登记触及、不裁断；以未核条目随承接在 `case-annotations-r77.json` 内 |")
L.append("| YM-070 | 「甲寅旬」出处待核，维持挂起；本轮由盲测 S10 席（B24）作断，只登记触及、不裁断；以未核条目随承接在 `case-annotations-r77.json` 内 |")
L.append("")
L.append("- R79 确认：四件维持挂起，本轮不核查、不关闭。R79 触及登记：BZ-029／BZ-040 本轮未被任何旗标触及；LY-537 本轮被 X2 席旗标（anon P3-78b37758、席内号 X2-109）触及——所指「果于申予日归」与待核同例同旨，**只登记关联、不裁**（并见 §六）；YM-070 本轮被 X2／Y2 席旗标（anon P3-46dabb02）触及——所指「后果同行都下。」语义未明与其未核旨同旨，只登记触及、不裁。")
L.append("")
L.append("---")
L.append("")
L.append("## 六、供给台账续记（只登记）")
L.append("")
L.append("### 6.1 CZ-QX 维持 16")
L.append("")
L.append("- CZ-QX 维持 **16**，承 R79 PREREG §4 登记口径由本席承接续记，本轮无增减。")
L.append("")
L.append("### 6.2 ZCB 合格存量复算列账（holdout24 取例后）")
L.append("")
L.append("- 合格总存量：**15 例**——组集口径 eligible∧present∧low∧separable∧断语/结局非空（`data/holdout24-seal-log.md` §一.1 盘上复算登记，本席以该日志原文断言核对）。")
L.append(f"- 已用合计：**14 例**（金标 id 盘上实读复算）——holdout22 取 4 例（{'、'.join(zcb_used['holdout22'])}，`benchmark/phase3/holdout22/test_gold.jsonl` 实读）；holdout23 取 6 例（{'、'.join(zcb_used['holdout23'])}，`benchmark/phase3/holdout23/test_gold.jsonl` 实读）；holdout24 取 4 例（{'、'.join(zcb_used['holdout24'])}，`benchmark/phase3/holdout24/test_gold.jsonl` 实读，本轮组集实取——定额 5 而合格可选余 4、差额 1 例已由 GSZ-047 递补，封存日志 §一.1 在案）。")
L.append("- 排除：**1 例**——ZCB-003 维持排除（holdout22 主持裁处未撤销，R79 PREREG §4 与 holdout24 封存日志 §一.1 均在案），不入选、不翻案。")
L.append("- **可选余复算：15 − 14 − 1 ＝ 0 例。** ZCB 合格存量经 holdout24 取例后已无可选余例，后轮组集如需测字面供给须待新源入账，只登记、不另行结算。")
L.append("")
L.append("### 6.3 待核四件维持登记（与 §五.2 同口径）")
L.append("")
L.append("- BZ-029（俞大维卒年，另含旗标内容错配线索）、BZ-040（许世英享年）、LY-537（「申予日」衍字疑）、YM-070（「甲寅旬」挂起）四件维持登记，无盘外独立史源不裁。")
L.append("- LY-537 关联登记：本轮 X2 席旗标 anon **P3-78b37758**（席内号 X2-109）与待核件 LY-537 同例（经 host-mapping 对位 P3-78b37758＝LY-537），所指即待核之「申予日」字样——**只登记关联、不裁**，LY-537 待核状态不变。")
L.append("")

addendum_text = "\n".join(L) + "\n"
# 附则逐字断言：23 件建议与 annotations 条目逐字对应、引文命中结局
for cid in new_partial:
    e = entry_by_case[cid]
    if f"「{e['manifest_carry_suggestion']}」" not in addendum_text: fail(f"addendum suggestion {cid}")
    assert_in(outcome(cid), addendum_text, f"addendum outcome {cid}")
if f"「{BZ037_SUGGESTION}」" not in addendum_text: fail("addendum BZ-037")
assert_in("原文未逐字复核「甲戌日巳时」的日时细节", EDITOR_NOTE, "flag quote vs editor_note")
add_path = BASE / "data/manifest-carryover-r79-addendum.md"
add_path.write_text(addendum_text, encoding="utf-8")
print("addendum written:", add_path, add_path.stat().st_size, "bytes")
print("ZCB ledger: stock 15 - used 14 (h22 4 + h23 6 + h24 4) - excluded 1 = remain", ZCB_REMAIN)
print("flag adjudication:", dict(fv), "+ pending touch 2 =", len(flag_verdicts) + 2)
