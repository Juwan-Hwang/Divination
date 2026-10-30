#!/usr/bin/env python3
# R48 数据席（测字普查）盘上汇总脚本：ZC/CZ 判级集 + 已用集对勘 + 字触全新版 OCR 页位定位
# 只读既有登记件（data-verify/digestion/expansion 台账）；禁止触碰任何 runs/*/predictions、judging、final-scores。
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path("/home/hatch/workspace/divination")
WORK = ROOT / "benchmark/phase3/runs/round48/digestion/work-cezi-r48"
WORK.mkdir(parents=True, exist_ok=True)

ZC_FILES = [
    ("r38", ROOT / "benchmark/phase3/runs/round38/data-verify/zichu-cases-r38.jsonl", 98),
    ("r39", ROOT / "benchmark/phase3/runs/round39/data-verify/zichu-j3-cases-r39.jsonl", 35),
    ("r41", ROOT / "benchmark/phase3/runs/round41/data-verify/zc-candidates-r41.jsonl", 29),
    ("r42", ROOT / "benchmark/phase3/runs/round42/data-verify/zc-candidates-r42.jsonl", 3),
]
CZ_FILE = ROOT / "benchmark/phase3/expansion12/online-routes/cases.jsonl"

def num(i): return int(i.split("-")[1])

zc = {}
for tag, path, expect in ZC_FILES:
    rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    assert len(rows) == expect, f"{tag} 行数 {len(rows)} != {expect}"
    for r in rows:
        rid = r["id"]
        assert rid not in zc, f"重复 id {rid}"
        comp = r.get("compliance") or {}
        grade = r.get("outcome_grade") or comp.get("outcome_grade")
        contam = r.get("contamination") or comp.get("contamination")
        elig = r.get("holdout_eligible")
        if elig is None: elig = comp.get("holdout_eligible")
        prov = r.get("provenance") or {}
        ctx = r.get("context") or {}
        inp = r.get("input_material") or {}
        char = (ctx.get("attachments") or {}).get("character_written") or inp.get("character_or_omen") or ""
        subj = (r.get("subject") or {}).get("name_or_desc") or inp.get("subject") or ""
        ques = ctx.get("question") or inp.get("question") or ""
        zc[rid] = dict(id=rid, src=tag, grade=grade, contamination=contam, eligible=elig,
                       book=prov.get("book", ""), page=prov.get("page", ""),
                       char=str(char)[:60], subject=str(subj)[:80], question=str(ques)[:80])
assert sorted(zc, key=num) == [f"ZC-{i:03d}" for i in range(1, 166)], "ZC 编号非 001-165 连续"
print(f"[assert ok] ZC 判级集 165 条连续 ZC-001..165")

cz_rows = [json.loads(l) for l in CZ_FILE.read_text(encoding="utf-8").splitlines() if l.strip()]
assert len(cz_rows) == 33
cz = {}
for r in cz_rows:
    ctx = r.get("context") or {}
    cz[r["id"]] = dict(id=r["id"], grade=r.get("outcome_grade"), contamination=r.get("contamination"),
                       char=str((ctx.get("attachments") or {}).get("character_written", ""))[:40],
                       question=str(ctx.get("question", ""))[:60],
                       subject=str((r.get("subject") or {}).get("name_or_desc", ""))[:60])
assert sorted(cz, key=num) == [f"CZ-{i:03d}" for i in range(1, 34)]
print("[assert ok] CZ 判级集 33 条连续 CZ-001..033")

# 已用集（承 SUPPLY-R43 §二.1 金标实算逐 id 清单）
USED = {
 "h15": "006 014 016 017 022 023 024 025 028 030 036 039 049 054 061 062 064 066 068 069",
 "h16": "070 071 075 077 079 081 082 083 084 085 090 091 092 093 097 108 118 123 125 133",
 "h17": "072 073 130 134 135 136 137 138 140 141 142 147 148 151 152 153 155 159 161 162",
 "h18": "139 143 144 145 146 149 150 154 156 157 158 160 163 164 165",
}
used = set()
for k, v in USED.items():
    s = {f"ZC-{x}" for x in v.split()}
    assert len(s) == (20 if k != "h18" else 15), k
    used |= s
assert len(used) == 75, len(used)
print("[assert ok] ZC 已用集 75（h15 20+h16 20+h17 20+h18 15，无交叠外溢）")

compliant = {i for i, r in zc.items() if r["grade"] in ("A", "A-low") and r["contamination"] == "low" and r["eligible"] is True}
print(f"文件口径合规（A/A-low+low+eligible）: {len(compliant)} 条 -> {sorted(compliant - used, key=num)}")
assert compliant - used == {"ZC-122"}, f"合规未用差集异常: {sorted(compliant-used, key=num)}"
assert used <= compliant
print("[assert ok] 合规 76（含旗标 ZC-122）- ZC-122 旗标排除 = 已用 75，差集为空 → 新鲜合规 0 与 R43 定案一致")

from collections import Counter
dist = Counter((r["grade"], r["contamination"]) for r in zc.values())
print("ZC 判级分布(grade,contamination):", dict(dist))
noncomp = {i: zc[i] for i in zc if i not in compliant}
print(f"ZC 已判级不合格/旗标: {len(noncomp)} 条（含 ZC-122 旗标 1）")

# ---------- 字触全（进步书局本）OCR 索引 ----------
PAGES = ROOT / "benchmark/phase3/runs/round46/digestion/work-cezi/zichu-pages"
OCRDIR = WORK / "zichu-ocr"
OCRDIR.mkdir(exist_ok=True)
imgs = sorted(PAGES.glob("p-*.jpg"))
assert len(imgs) == 133, len(imgs)
for img in imgs:
    out = OCRDIR / (img.stem + ".txt")
    if out.exists() and out.stat().st_size > 0:
        continue
    subprocess.run(["tesseract", str(img), str(OCRDIR / img.stem), "-l", "chi_tra_vert", "--psm", "5"],
                   check=True, capture_output=True)
print("[ok] OCR 133 页毕（chi_tra_vert/psm5，仅作定位索引）")

ocr = {}
for img in imgs:
    pno = int(img.stem.split("-")[1])
    ocr[pno] = (OCRDIR / (img.stem + ".txt")).read_text(encoding="utf-8", errors="replace").replace(" ", "").replace("\n", "")

VOL_RANGE = {"卷一": (12, 37), "卷二": (38, 65), "卷三": (66, 79), "卷四": (80, 97), "卷五": (98, 117), "卷六": (118, 127)}
def vol_of(book):
    for v in VOL_RANGE:
        if v in book: return v
    return ""

hits, misses = {}, []
for rid, r in sorted(zc.items(), key=lambda kv: num(kv[0])):
    v = vol_of(r["book"])
    lo, hi = VOL_RANGE.get(v, (1, 133))
    # 检索键：所测字首字 + 事主姓氏首字（繁简差异时退化为仅所测字）
    key = r["char"].strip()[:1]
    found = []
    if key:
        found = [p for p in range(lo, hi + 1) if key in ocr.get(p, "")]
    hits[rid] = dict(vol=v, key=key, pages=found[:12], n=len(found))
    if not found: misses.append(rid)
print(f"OCR 字键定位: 命中 {165-len(misses)}/165，未命中 {len(misses)}: {misses[:20]}")

(WORK / "zc-judged-set-r48.json").write_text(json.dumps(
    dict(zc=zc, cz=cz, used=sorted(used, key=num), compliant_file_view=sorted(compliant, key=num),
         ocr_hits=hits, ocr_misses=misses), ensure_ascii=False, indent=1), encoding="utf-8")
print("[ok] 汇总落盘 work-cezi-r48/zc-judged-set-r48.json")
