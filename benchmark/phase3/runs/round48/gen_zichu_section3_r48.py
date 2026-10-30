#!/usr/bin/env python3
# R48 数据席（测字普查·乙）§3 总清单生成：165 条逐则（题旨/旧书页/新版页推定/状态）
# 只读 work-cezi-r48 两件汇总 JSON；新版页为逐卷锚点线性推定，实测条以 OVERRIDE 标注。
import json, re
from pathlib import Path

ROOT = Path("/home/hatch/workspace/divination")
WORK = ROOT / "benchmark/phase3/runs/round48/digestion/work-cezi-r48"
rows = json.loads((WORK / "zc-entries-summary-r48.json").read_text(encoding="utf-8"))
assert len(rows) == 165

def old_page(page_str):
    m = re.search(r"书页\s*(\d+)", page_str or "")
    if m:
        return int(m.group(1))
    m = re.search(r"書頁\s*(\d+)", page_str or "")
    return int(m.group(1)) if m else None

def vol_of(book):
    for v in ("卷一", "卷二", "卷三", "卷四", "卷五", "卷六"):
        if v in (book or ""):
            return v
    return ""

# 逐卷线性对位（旧书页 -> 新版 PDF 页），锚点见 CENSUS-zichuquan-r48 §1/§5 与 R46 §3
MAPS = {
    "卷一": lambda o: round(13 + (o - 1) * 23 / 19),   # 旧12->26 实测锚 (ZC-135)
    "卷二": lambda o: round(39 + (o - 21) * 26 / 22),  # 旧39->60、旧42/43->65 实测锚
    "卷三": lambda o: round(66 + (o - 45) * 12 / 10),  # 旧45->66 实测锚 (ZC-099/100)
    "卷四": lambda o: round(80.3 + (o - 57) * 1.19),   # 旧58->81/82、旧66->91 实测锚
    "卷五": lambda o: round(98 + (o - 72) * 18 / 15),
    "卷六": lambda o: round(118 + (o - 89) * 8 / 6),   # 旧95->126 推定
}
MEASURED = {  # 本席或 R46 视觉实测的新版页（优先于推定）
    "ZC-135": "26（实测）", "ZC-139": "81–82（实测）", "ZC-140": "82（实测）",
    "ZC-153": "91（实测）", "ZC-072": "60（实测）",
    "ZC-084": "65（实测）", "ZC-085": "65（实测）",
    "ZC-099": "66（实测）", "ZC-100": "66（实测）",
}
VOL_ORDER = ["卷一", "卷二", "卷三", "卷四", "卷五", "卷六"]
rows.sort(key=lambda r: (VOL_ORDER.index(vol_of(r["book"])) if vol_of(r["book"]) in VOL_ORDER else 9,
                         old_page(r["page"]) or 999, int(r["id"].split("-")[1])))
out = []
cur = None
for r in rows:
    v = vol_of(r["book"])
    if v != cur:
        cur = v
        out.append(f"\n### {v}（{'廋部' if v=='卷一' else '外部' if v=='卷二' else '晰部' if v=='卷三' else '几部' if v=='卷四' else '谐部' if v=='卷五' else '说部'}）\n")
        out.append("| ZC | 题旨（所测字·事主/所问） | 旧书页 | 新版页 | 状态（原判） |")
        out.append("|---|---|---|---|---|")
    o = old_page(r["page"])
    newp = MEASURED.get(r["id"]) or (str(MAPS[v](o)) if (v in MAPS and o) else "—")
    gist = (r["char"] or "—").replace("\n", " ")[:26]
    subj = (r["subject"] or "").replace("\n", " ")[:30]
    ques = (r["question"] or "").replace("\n", " ")[:30]
    topic = "·".join(x for x in [subj, ques] if x)[:44]
    if r["id"] == "ZC-122":
        status = "已判级·旗标排除（A·low 形态，身份未定，未用）"
    elif r["used"]:
        status = "已判级已用（合规 A/A-low·low）"
    else:
        status = f"已判级不合格（{r['grade']}·{r['contamination']}）"
    out.append(f"| {r['id']} | {gist}·{topic} | {o if o else '—'} | {newp} | {status} |")

txt = "\n".join(out) + "\n"
(WORK / "section3-table-r48.md").write_text(txt, encoding="utf-8")
n_meas = sum(1 for r in rows if r["id"] in MEASURED)
print(f"[ok] §3 表生成：165 行（实测页位 {n_meas} 条，其余逐卷推定） -> work-cezi-r48/section3-table-r48.md")
