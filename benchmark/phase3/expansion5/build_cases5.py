#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MastersDivination Benchmark · Phase 3 第五輪擴數（expansion5）建檔腳本（數據角）

來源：
  《增刪卜易》卷之一·暗動章第二十二 —— 2026-10-29 經維基文库子頁
  https://zh.wikisource.org/wiki/增刪卜易/22 在線渲染讀取（本地 dump 卷一
  只有 {{/子頁}} 轉入標籤、無正文；expansion4 卷一普查未收此例、亦未列棄）。
  本輪對卷二至卷四本地全文另做「月日干支開口」全量普查（198 開口）與
  開口計數對池比對，除已收／歷輪已棄者外無新合格例，詳見 BUILD-REPORT.md。

去重：照 expansion4/build_cases4.py 原件的三鍵指紋法（月日干支＋全裝卦逐爻行
      ＋結局首句繁簡雙查）對全部既有記錄程序比對；另以「坤之師／女痘／暗動章」
      關鍵詞全倉 grep（排除 test_gold）覆核無命中。
劃分：合格池＝｛A 級 ∩ low ∩ 雙完整｝，按 sha256("phase3-round5-20261029:"+id)
      十六進制升序即 holdout7 順序。本輪合格池僅 1 例，遠不足目標 20–25，
      如實全取、未放寬標準湊數。
      金標只寫 benchmark/phase3/holdout7/test_gold.jsonl（封存，未開封）。
      本腳本絕不讀取任何 holdout 的 test_gold.jsonl。
冪等：可重跑，產物一致（時間戳除外）。
"""
import hashlib, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]          # ~/workspace/divination
P3 = ROOT / "benchmark" / "phase3"
OUTDIR = P3 / "expansion5"
H7DIR = P3 / "holdout7"
ROUND_TAG = "phase3-round5-20261029"

# ---------------------------------------------------------------- 卦象推導（照 expansion4/build_cases4.py 原件）
TRI = {(1,1,1):"乾",(1,1,0):"兌",(1,0,1):"離",(1,0,0):"震",
       (0,1,1):"巽",(0,1,0):"坎",(0,0,1):"艮",(0,0,0):"坤"}
_HEX_ROWS = {
"乾": {"乾":"乾爲天","坤":"天地否","震":"天雷无妄","巽":"天風姤","坎":"天水訟","離":"天火同人","艮":"天山遯","兌":"天澤履"},
"坤": {"乾":"地天泰","坤":"坤爲地","震":"地雷復","巽":"地風升","坎":"地水師","離":"地火明夷","艮":"地山謙","兌":"地澤臨"},
"震": {"乾":"雷天大壯","坤":"雷地豫","震":"震爲雷","巽":"雷風恆","坎":"雷水解","離":"雷火豐","艮":"雷山小過","兌":"雷澤歸妹"},
"巽": {"乾":"風天小畜","坤":"風地觀","震":"風雷益","巽":"巽爲風","坎":"風水渙","離":"風火家人","艮":"風山漸","兌":"風澤中孚"},
"坎": {"乾":"水天需","坤":"水地比","震":"水雷屯","巽":"水風井","坎":"坎爲水","離":"水火既濟","艮":"水山蹇","兌":"水澤節"},
"離": {"乾":"火天大有","坤":"火地晉","震":"火雷噬嗑","巽":"火風鼎","坎":"火水未濟","離":"離爲火","艮":"火山旅","兌":"火澤睽"},
"艮": {"乾":"山天大畜","坤":"山地剝","震":"山雷頤","巽":"山風蠱","坎":"山水蒙","離":"山火賁","艮":"艮爲山","兌":"山澤損"},
"兌": {"乾":"澤天夬","坤":"澤地萃","震":"澤雷隨","巽":"澤風大過","坎":"澤水困","離":"澤火革","艮":"澤山咸","兌":"兌爲澤"}}
HEX = {}
for _up, _row in _HEX_ROWS.items():
    for _lo, _nm in _row.items():
        HEX[(_up, _lo)] = _nm
def derive(chart_lines):
    names = []
    groups = [chart_lines[i:i+6] for i in range(0, len(chart_lines), 6)]
    for g in groups:
        if len(g) != 6:
            names.append(None); continue
        ben, bian, has_move = [], [], False
        for row in reversed(g):
            left = row.split("　")[0]
            y = 1 if ("⚊" in left or "○" in left) else 0
            ben.append(y)
            if "○" in left: bian.append(0); has_move = True
            elif "ㄨ" in left: bian.append(1); has_move = True
            else: bian.append(y)
        lo = TRI[tuple(ben[0:3])]; up = TRI[tuple(ben[3:6])]
        name = HEX[(up, lo)]
        if has_move:
            lo2 = TRI[tuple(bian[0:3])]; up2 = TRI[tuple(bian[3:6])]
            name = name + "之" + HEX[(up2, lo2)]
        names.append(name)
    return names

# ------------------------------------------------------------ 既有記錄載入（去重用，照 expansion4 原件）
def iter_jsonl(p):
    try:
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield json.loads(line)
    except FileNotFoundError:
        return

def load_existing():
    recs = {}
    pats = ["masters-dataset/**/inputs.jsonl", "masters-dataset/**/answers.jsonl",
            "benchmark/**/inputs.jsonl", "benchmark/**/answers.jsonl",
            "benchmark/**/cases.jsonl", "benchmark/**/roster.jsonl",
            "benchmark/phase3/data/*.jsonl"]
    for pat in pats:
        for p in sorted(ROOT.glob(pat)):
            if "expansion5" in str(p) or "holdout7" in str(p):
                continue                      # 不把本輪產物當既有
            assert "test_gold" not in p.name  # 紀律：不讀任何金標
            for r in iter_jsonl(p):
                rid = r.get("id")
                if rid and rid not in recs:
                    recs[rid] = r
    for d in [ROOT/"benchmark/phase3/expansion/inputs",
              ROOT/"benchmark/phase3/expansion2/inputs",
              ROOT/"benchmark/phase3/expansion3/inputs",
              ROOT/"benchmark/phase3/expansion4/inputs",
              ROOT/"benchmark/phase3/holdout3-inputs",
              ROOT/"benchmark/phase3/holdout4-inputs",
              ROOT/"benchmark/phase3/inputs"]:
        if d.is_dir():
            for p in sorted(d.glob("*.json")):
                r = json.loads(p.read_text(encoding="utf-8"))
                if r.get("id") and r["id"] not in recs:
                    recs[r["id"]] = r
    return recs

PUNC = "，。；：、．·…—「」『』（）()？！?! "
def norm(s):
    return "".join(c for c in (s or "") if c not in PUNC)
T2S = str.maketrans({"斷":"断","曰":"曰","果":"果","於":"于","後":"后","麼":"么",
                     "這":"这","裡":"里","醫":"医","時":"时","還":"还","來":"来",
                     "為":"为"})
def fp_chart(rec):
    hx = rec.get("hexagram") or {}
    rows = []
    for cast in [hx] + (rec.get("extra_casts") or []):
        for ln in (cast.get("chart_lines") or []):
            rows.append(ln.split("　")[0])
    return tuple(rows)

def outcome_head(rec):
    oc = rec.get("outcome") or {}
    txt = oc.get("description") or ""
    m = re.split(r"[。；]", txt)
    return norm(m[0])[:16] if m else ""

# ---------------------------------------------------------------- 本輪新例（增刪卷一·暗動章）
# 欄位: subj, caster, question, asked, chapter, category, direction,
#        gua_expected(原文所記), chart, stmt, out, gnote, comment
Z = []
def z(*a, **k):
    Z.append(a)

z("女痘吉凶","一人","占女痘","寅月己未日","暗動章第二十二","疾病","positive",
  "坤爲地之地水師",
  ["子孫酉金⚋世　子孫酉金⚋","妻財亥水⚋　　妻財亥水⚋","兄弟丑土⚋　　兄弟丑土⚋",
   "官鬼卯木⚋應　父母午火⚋","父母巳火ㄨ　　兄弟辰土⚊","兄弟未土⚋　　官鬼寅木⚋"],
  "酉金子孫，𨿽則春令休囚，得日辰生之，二爻巳火動而克金，得未日沖動丑土，土動生金，花𨿽密以全生。彼曰：目下甚危。予曰：不妨，今日未申時有救，",
  "果於申時遇明醫救治，何當緩也？",
  "原文占日作「寅月已未日」，「已」為「己」之形訛，asked_at 據干支常例作寅月己未日（前輪 LY-410/437 同例口徑）；斷語「今日未申時」之「未」字疑衍、照錄。斷語（申時有救）與結局（果於申時遇明醫救治）可分離，A 級。",
  "卷一暗動章第二十二；本地 dump 卷一僅存子頁轉入標籤無正文，本例經維基文库子頁 /22 在線讀取得。expansion4 卷一普查未收、棄例名單亦未列，本輪補收。")

CONTAM_Z = ("清初民間占例（野鶴老人自占及輯錄）；求測者多未具名、非著名歷史人物或事件，"
            "結局無從以常識先驗得知。")
Z_URL = "https://zh.wikisource.org/wiki/增刪卜易"
CAST = "六爻納甲（銅錢搖卦，原書只記月日與卦象）"

def build_z(cid, t):
    (subj, caster, question, asked, chapter, cat, direction, gua_exp,
     chart, stmt, out, gnote, comment) = t
    rec = {
        "id": cid, "tradition": "六爻",
        "master": "野鶴老人（《增刪卜易》）",
        "source_work": "增刪卜易",
        "subject": subj, "caster_or_relation": caster, "question": question,
        "category": cat, "asked_at": asked, "casting_method": CAST,
    }
    assert len(chart) % 6 == 0
    casts = [chart[i:i+6] for i in range(0, len(chart), 6)]
    derived = derive(chart)
    exps = gua_exp.split("＋")
    assert len(derived) == len(exps), (cid, derived, exps)
    hx = []
    for ci, cl in enumerate(casts):
        assert derived[ci] == exps[ci], (cid, derived[ci], exps[ci])
        nmov = sum(1 for ln in cl if "○" in ln.split("　")[0] or "ㄨ" in ln.split("　")[0])
        hx.append({"name": derived[ci], "chart_lines": cl, "moving": nmov})
    main = hx[0]
    names = main["name"].split("之")
    rec["hexagram"] = {
        "original_name": names[0],
        "changed_name": names[1] if len(names) > 1 else None,
        "chart_lines": casts[0]}
    if len(casts) > 1:
        rec["extra_casts"] = [{
            "original_name": h["name"].split("之")[0],
            "changed_name": h["name"].split("之")[1] if "之" in h["name"] else None,
            "chart_lines": c} for h, c in zip(hx[1:], casts[1:])]
    rec["chart_complete"] = True
    rec["completeness_basis"] = ("月日干支原文俱全（month_day_complete=true；占日「已未」為「己未」形訛、已註明）；裝卦表逐爻照錄線上渲染頁，"
                                 "卦名經推導與原文所記相符（chart_complete=true）。斷語、結局逐字照錄。")
    rec["month_day_complete"] = True
    rec["provenance"] = {"work": "增刪卜易", "edition": "維基文库本（錄入者整理本，未排版/未校對）",
                         "page": "卷之一·" + chapter, "url": Z_URL, "language": "zh-Hant"}
    rec["master_predictions"] = [{
        "statement_excerpt": stmt, "direction": direction,
        "key_assertions": [], "timing_claim": None, "source_language": "zh-Hant"}]
    rec["outcome"] = {"description": out, "direction": direction, "source_language": "zh-Hant"}
    rec["outcome_grade"] = "A"
    rec["contamination"] = "low"
    rec["contamination_rationale"] = CONTAM_Z
    rec["grade_note"] = gnote
    rec["comment"] = comment
    rec["holdout_eligible"] = bool(rec["chart_complete"])
    return rec

def main():
    now = __import__("subprocess").run(
        ["date", "+%Y-%m-%dT%H:%M:%S+08:00"], env={"TZ": "Asia/Shanghai", "PATH": "/usr/bin:/bin"},
        capture_output=True, text=True).stdout.strip()
    existing = load_existing()
    print(f"既有記錄（按 id 去重）: {len(existing)}")

    cases = []
    nid = 700
    for t in Z:
        nid += 1
        cases.append(build_z(f"LY-{nid}", t))
    print(f"新例: {len(cases)}")

    # ---- 去重斷言（照 expansion4）----
    exist_fp = {}
    for rid, r in existing.items():
        fp = (r.get("asked_at"), fp_chart(r))
        if fp[1]:
            exist_fp.setdefault(fp, rid)
    exist_out_heads = {}
    for rid, r in existing.items():
        h = outcome_head(r)
        if len(h) >= 6:
            exist_out_heads.setdefault(h, rid)
            exist_out_heads.setdefault(h.translate(T2S), rid)
    for c in cases:
        fp = (c["asked_at"], fp_chart(c))
        if fp[1]:
            assert fp not in exist_fp, f"去重碰撞（月日＋裝卦）: {c['id']} vs {exist_fp.get(fp)}"
        h = outcome_head(c)
        assert h not in exist_out_heads, f"去重碰撞（結局首句）: {c['id']} vs {exist_out_heads.get(h)}"
    print("去重斷言通過（月日＋裝卦指紋、結局首句繁簡雙查）。")

    # ---- 劃分 ----
    eligible = [c for c in cases if c["holdout_eligible"]]
    eligible.sort(key=lambda c: hashlib.sha256(f"{ROUND_TAG}:{c['id']}".encode()).hexdigest())
    holdout = eligible[:25]
    hids = {c["id"] for c in holdout}
    print(f"合格池 {len(eligible)} 例；holdout7 取 {len(holdout)} 例"
          + ("（遠不足 20–25，如實全取、不放寬標準）" if len(eligible) < 20 else ""))
    devadd = [c for c in cases if c["id"] not in hids]

    def inp(c):
        return {"id": c["id"], "tradition": c["tradition"], "subject": c["subject"],
                "context": {"caster_or_relation": c["caster_or_relation"],
                            "question": c["question"], "category": c["category"],
                            "asked_at": c["asked_at"], "casting_method": c["casting_method"],
                            "hexagram": c["hexagram"]},
                "provenance": c["provenance"], "language": c["provenance"]["language"]}

    def ans(c):
        return {"id": c["id"], "master": c["master"], "source_work": c["source_work"],
                "master_predictions": c["master_predictions"], "outcome": c["outcome"],
                "outcome_grade": c["outcome_grade"], "contamination": c["contamination"],
                "contamination_rationale": c["contamination_rationale"],
                "grade_note": c["grade_note"]}

    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR / "inputs").mkdir(exist_ok=True)
    with open(OUTDIR / "cases.jsonl", "w", encoding="utf-8") as f:
        for c in cases:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    for c in cases:
        (OUTDIR / "inputs" / f"{c['id']}.json").write_text(
            json.dumps(inp(c), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with open(OUTDIR / "dev-add-answers.jsonl", "w", encoding="utf-8") as f:
        for c in sorted(devadd, key=lambda x: x["id"]):
            f.write(json.dumps(ans(c), ensure_ascii=False) + "\n")

    H7DIR.mkdir(parents=True, exist_ok=True)
    gold_path = H7DIR / "test_gold.jsonl"
    with open(gold_path, "w", encoding="utf-8") as f:
        for c in holdout:
            f.write(json.dumps(ans(c), ensure_ascii=False) + "\n")
    gold_sha = hashlib.sha256(gold_path.read_bytes()).hexdigest()

    sealed = f"""# SEALED — holdout7 測試集金標（未開封）

- 封存時間：{now}（Asia/Shanghai）
- 來源輪次：Phase 3 第五輪擴數（expansion5），新例 LY-701
- 例數：{len(holdout)}（合格池 {{A 級 ∩ low ∩ 雙完整}} 共 {len(eligible)} 例，遠不足目標 20–25，如實全取、未放寬標準；
  按 sha256("{ROUND_TAG}:<id>") 十六進制升序取序——合格池全數入選）
- 金標文件：benchmark/phase3/holdout7/test_gold.jsonl
- 金標 SHA-256：{gold_sha}
- 盲測 inputs：benchmark/phase3/expansion5/inputs/（LY-7xx 逐例一檔）
- 狀態：**未開封**。開封須按 PROTOCOL 預註冊後由評分角執行，並在本文件與
  benchmark/phase3/holdout7-seal-log.md 追加開封記錄。
- 紀律：數據角、修訂角不得讀取 test_gold.jsonl 內容。
- 注意：本集僅 {len(holdout)} 例，統計功效近乎為零；是否用作留出驗收由主持角裁斷（見 expansion5/BUILD-REPORT.md 缺口說明）。
"""
    (H7DIR / "SEALED.md").write_text(sealed, encoding="utf-8")
    seal_log = f"""# holdout7 封存日誌

## {now} 封存（數據角，expansion5）
- 新例總數：{len(cases)}（《增刪卜易》卷一·暗動章第二十二 補收 1 例）
- 合格池（A∩low∩雙完整）：{len(eligible)} 例 → holdout7 {len(holdout)} 例（遠不足目標 20–25，全取，不放寬標準；缺口詳見 expansion5/BUILD-REPORT.md）
- dev-add：{len(devadd)} 例（答案存 expansion5/dev-add-answers.jsonl）
- 排序鍵：sha256("{ROUND_TAG}:<id>") 十六進制升序
- 金標：benchmark/phase3/holdout7/test_gold.jsonl
- 金標 SHA-256：{gold_sha}
- 狀態：未開封
"""
    (P3 / "holdout7-seal-log.md").write_text(seal_log, encoding="utf-8")

    # ---- inputs 泄漏自檢 ----
    bad = []
    for c in cases:
        p = OUTDIR / "inputs" / f"{c['id']}.json"
        t = p.read_text(encoding="utf-8")
        for kw in ["master_predictions", "outcome", "statement_excerpt", "key_assertions",
                   "果於", "果于", "後果", "后果", "斷曰", "断曰"]:
            if kw in t:
                bad.append((c["id"], kw))
    assert not bad, f"inputs 泄漏: {bad}"
    print("inputs 泄漏自檢: CLEAN")
    print(f"holdout7: {len(holdout)} 例，金標 SHA-256 = {gold_sha}")
    print(f"dev-add: {len(devadd)} 例: {[c['id'] for c in sorted(devadd, key=lambda x: x['id'])]}")

if __name__ == "__main__":
    main()
