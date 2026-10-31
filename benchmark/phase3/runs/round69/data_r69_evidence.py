#!/usr/bin/env python3
"""R69 数据席证据脚本：只读核查，打印证据，不写任何产出件。
核查：① R68 counts 双路复算；② R69/R68 cases 487/487 全等；
③ R68 部分成立 58 件 vs R69 manifest _r69_carryover_notes_addendum 对勘；
④ R69 旗标行解析（126 行/90 anon）与 host-mapping 逐件对位（anon 后紧随括号 case 全等）；
⑤ tradition 7 件原卡无 tradition 字样 + prediction basis 首行逐字；
⑥ 指令性字样全量扫描（基线四例 + LR2-016 editor_note 分列 + 宽扫甄别）；
⑦ 新立/新旨件引文逐字核对。
"""
import json, re, pathlib
from collections import Counter, defaultdict

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")

def load(p):
    return json.loads(pathlib.Path(p).read_text(encoding="utf-8"))

r68 = load(BASE / "data/case-annotations-r68.json")
m69 = load(BASE / "runs/round69/judging/outcome-manifest.json")
m68 = load(BASE / "runs/round68/judging/outcome-manifest.json")
hm = load(BASE / "runs/round69/judging/host-mapping.json")
flags_text = (BASE / "runs/round69/judging/FLAGS-selfreported-r69.md").read_text(encoding="utf-8")

# ① counts
calc = Counter(a["disposition"] for a in r68["annotations"])
assert calc == Counter(r68["counts"]["verdicts"]), (calc, r68["counts"]["verdicts"])
print("① R68 counts 双路复算一致:", dict(calc), "总", len(r68["annotations"]))
partials = [a for a in r68["annotations"] if a["disposition"] == "部分成立"]
assert len(partials) == 58 and all(a["manifest_carry_suggestion"] for a in partials)
print("   部分成立 58 件，manifest_carry_suggestion 全非空")

# ② cases 全等
assert set(m69["cases"]) == set(m68["cases"]) and len(m69["cases"]) == 487
uneq = [k for k in m69["cases"] if m69["cases"][k] != m68["cases"][k]]
assert not uneq, uneq
print("② R69 cases 与 R68 逐件全等 487/487")

# ③ 对勘
add = m69["_r69_carryover_notes_addendum"]
assert set(add) == {a["case_id"] for a in partials}, "键集合差异"
diffs = [a["case_id"] for a in partials if add[a["case_id"]] != a["manifest_carry_suggestion"]]
print("③ 附则对勘：键集合全等，逐字差异", len(diffs), "件 ->", "58/58 全等" if not diffs else diffs)
assert not diffs

# ④ 旗标解析与对位
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
seat_rows = Counter(s for s, _, _ in rows if s != "HOST")
anons = sorted({a for _, a, _ in rows})
cases = {hm[a] for a in anons}
print("④ 旗标行", len(rows), "（八席）:", dict(seat_rows), "| anon", len(anons), "| 例", len(cases))
# anon 后紧随括号 case 全等（形近串号逐件对位：不用计数代判，逐行核）
bad = []
for _, a, ln in rows:
    m = re.match(r".*?" + re.escape(a) + r"\s*[（\(]([A-Z]+\d*-\d+)[）\)]", ln)
    if m and m.group(1) != hm[a]:
        bad.append((a, m.group(1), hm[a]))
assert not bad, bad
print("   anon 紧随括号 case 与 host-mapping 逐件全等，错配 0")
# 同首缀（P3-+4 hex）组逐组列示复核
g = defaultdict(list)
for a in anons: g[a[:7]].append(a)
print("   同首缀组（>1）:", {k: [(x, hm[x]) for x in v] for k, v in g.items() if len(v) > 1} or "无")
# LY-030 行内 LY-612 为同条参照、非本例标签
assert hm["P3-ba74d717"] == "LY-030"
print("   P3-ba74d717 映射 LY-030（行内 LY-612 系同条全文参照，非标签）已核")
# 待核四件未被触及
for cid in ["BZ-029", "BZ-040", "LY-537", "YM-070"]:
    assert cid not in cases, cid
print("   待核维持四件 BZ-029/BZ-040/LY-537/YM-070 本轮旗标均未触及")

# ⑤ tradition 7 件
trad = ["LY-017", "LY-019", "LY-021", "LY-022", "LY-034", "LY-103", "LY-105"]
for cid in trad:
    card_raw = (BASE / f"inputs-dev12/{cid}.json").read_text(encoding="utf-8")
    assert "tradition" not in card_raw and '"system"' not in card_raw, cid
    pred = load(BASE / f"runs/round69/predictions/{cid}.json")
    assert pred["basis"].startswith("卡面 tradition＝liuyao，與卡面一致"), cid
print("⑤ tradition 7 件：原卡全卡无 tradition/system 字样，basis 首行逐字为「卡面 tradition＝liuyao，與卡面一致」")

# ⑥ 指令性字样扫描
pats = ["请按", "請按", "须注", "須注", "评分时", "評分時", "比对时", "比對時",
        "使用时须", "使用時須", "分开统计", "分開統計", "勿以此斷"]
hits = {cid for cid, t in m69["cases"].items() if any(p in t for p in pats)}
assert hits == {"BZ-036", "BZ-042", "BZ-105", "LY-204"}, hits
assert "盲测比对须注" in m69["cases"]["BZ-036"]
assert "（盲测比对时以格局大富一项为主）" in m69["cases"]["BZ-042"]
assert "使用时须分开统计" in m69["cases"]["BZ-105"]
assert "勿以此斷" in m69["cases"]["LY-204"]
split = m69["_r56_lr2016_split"]
assert "评分时该细项请按未完全复核处理" in split["editor_note"]
assert "评分时" not in m69["cases"]["LR2-016"]
broad = {}
for cid, t in m69["cases"].items():
    f = [p for p in ["请", "請", "须", "須", "切不"] if p in t]
    if f: broad[cid] = f
print("⑥ 本体指令性字样恰为基线四例 {BZ-036,BZ-042,BZ-105,LY-204}；LR2-016 之句只存分列 editor_note")
print("   宽扫命中:", broad, "（叙事/通则/按语甄别见定案 special_checks③）")

# ⑦ 新立/新旨引文逐字
def pred(cid): return load(BASE / f"runs/round69/predictions/{cid}.json")
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
assert "雪止放晴" in pred("LY-025")["prediction_text"] and "negative" not in pred("LY-025")["prediction_text"] + pred("LY-025")["basis"]
assert "欄位與爻位出入已在此註明" in pred("LY-322")["basis"]
assert "卡面无附盘，依据不足" in pred("AS-307")["basis"]
print("⑦ 新立/新旨/注记层引文逐字断言全过（AS-215/LY-246/LY-329/LY-613/LY-628/LY-207/LY-520/LY-025/LY-322/AS-307）")
print("EVIDENCE OK")
