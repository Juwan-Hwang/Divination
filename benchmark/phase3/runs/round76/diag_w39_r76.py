#!/usr/bin/env python3
# R76 W monitoring round 39 (W39) diagnostic script.
# Reads ONLY the exact files named in the assignment; no directory listing,
# no glob, no /tmp. Prior per-case labels are transcribed from
# DIAG-LR-fresh-h16.md section 2.1 (dev side, cited not re-coded).
# LR3-010 has no prior label in h16 s2.1 (it was not a dev40 negative);
# it is registered as UNC (uncoded) and is NOT newly coded here.
import json, math

NEG = "/home/hatch/workspace/divination/benchmark/phase3/runs/round76/diagnosis/lr-negatives-dev76.json"
FIN = "/home/hatch/workspace/divination/benchmark/phase3/runs/round76/final-scores.json"
INBASE = "/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round76/diagnosis/DIAG-LR-weight-dev76.md"

# case_id -> (main label, subform/interface note) per DIAG-LR-fresh-h16 s2.1
CODING = {
 "LR2-013": ("D", "—"),
 "LR2-014": ("W*", "W-face, interface; W<->C interface"),
 "LR2-015": ("E", "same-sign exclusion; W note only"),
 "LR2-016": ("D", "W<->magnitude interface note only"),
 "LR2-017": ("E", "—"),
 "LR2-018": ("D", "—"),
 "LR2-019": ("E", "—"),
 "LR2-021": ("A*", "MW/SEAT; A<->B interface"),
 "LR2-022": ("W*", "W-face, interface; W<->A interface"),
 "LR2-023": ("W*", "W-face, interface; W<->D/E interface"),
 "LR2-024": ("C*", "—"),
 "OC-026":  ("E", "same-sign exclusion note"),
 "OC-027":  ("W*", "W-name, interface; W<->C interface"),
 "OC-029":  ("E", "A secondary candidate MW/MIX"),
 "OC-030":  ("A", "SF/SEAT"),
 "LR3-002": ("E", "A secondary candidate GZ/SEAT"),
 "LR3-006": ("C*", "—"),
 "LR3-008": ("D", "—"),
 "LR3-010": ("UNC", "no prior coding in h16 s2.1; not coded this round"),
 "LR3-101": ("W*", "W-face, interface; W<->A/C interface"),
 "LR3-104": ("E", "—"),
 "LR3-107": ("A", "SF/SEAT"),
 "LR3-110": ("E", "—"),
 "LR3-112": ("H", "W not measurable"),
 "LR3-114": ("C*", "—"),
 "LR3-116": ("A", "QX/SEAT"),
}

def se_pp(k, n):
    if n == 0:
        return 0.0
    p = k / n
    return math.sqrt(p * (1 - p) / n) * 100.0

def main():
    neg = json.load(open(NEG, encoding="utf-8"))
    fin = json.load(open(FIN, encoding="utf-8"))
    ana = fin["analysis_r76"]["families"]
    negs = neg["negatives"]
    assert neg["n_liuren_total"] == 30, neg["n_liuren_total"]
    assert neg["n_negative"] == 26 and len(negs) == 26
    ids = [x["case_id"] for x in negs]
    assert set(ids) == set(CODING), (set(ids) ^ set(CODING))

    # per-case consistency: pair_diff == ours - master; ours == ours_axis2 == ours_sub.total
    rows = []
    for x in negs:
        cid = x["case_id"]
        assert abs(x["pair_diff"] - (x["ours"] - x["master"])) < 1e-9, cid
        assert fin["ours_axis2"][cid] == x["ours"], cid
        assert fin["ours_sub"][cid]["total"] == x["ours"], cid
        d = json.load(open(f"{INBASE}/{cid}.json", encoding="utf-8"))
        book = (d.get("provenance") or {}).get("book")
        if not book:
            fam = "pending"
        elif "指南" in book:
            fam = "guide"
        else:
            fam = "non-guide"
        seg = "dev8" if x["in_dev8"] else "LR3"
        rows.append({**x, "book": book, "fam": fam, "seg": seg,
                     "label": CODING[cid][0], "note": CODING[cid][1]})

    dev8 = [r for r in rows if r["seg"] == "dev8"]
    lr3 = [r for r in rows if r["seg"] == "LR3"]
    assert len(dev8) == 15 and len(lr3) == 11, (len(dev8), len(lr3))
    n_labeled = sum(1 for r in rows if r["label"] != "UNC")
    assert n_labeled == 25, n_labeled

    # final-scores cross-check (analysis_r76 families)
    d8 = ana["liuren_dev8"]; mg = ana["liuren_merged"]; l3 = ana["liuren_lr3_new"]
    assert d8["n"] == 18 and d8["L"] == 15 and abs(d8["pair_diff"] - (-2.556)) < 1e-9
    assert mg["n"] == 30 and mg["L"] == 26 and abs(mg["pair_diff"] - (-2.117)) < 1e-9
    assert l3["n"] == 12 and l3["L"] == 11 and abs(l3["pair_diff"] - (-1.458)) < 1e-9
    assert abs((mg["ours_mean"] - mg["master_mean"]) - mg["pair_diff"]) < 1e-9
    assert abs((d8["ours_mean"] - d8["master_mean"]) - d8["pair_diff"]) < 0.002  # rounded means
    assert abs((l3["ours_mean"] - l3["master_mean"]) - l3["pair_diff"]) < 0.002  # rounded means (diff 0.001)
    sum_dev8_neg = round(sum(r["pair_diff"] for r in dev8), 4)
    sum_lr3_neg = round(sum(r["pair_diff"] for r in lr3), 4)
    sum_all_neg = round(sum(r["pair_diff"] for r in rows), 4)

    def counts(rs):
        c = {}
        for r in rs:
            k = r["label"].rstrip("*")
            c[k] = c.get(k, 0) + 1
        return c
    c_dev8, c_lr3, c_all = counts(dev8), counts(lr3), counts(rows)
    w_int = lambda c: c.get("W", 0)
    fam_all = {}
    for r in rows:
        fam_all[r["fam"]] = fam_all.get(r["fam"], 0) + 1
    fam_dev8 = {}
    for r in dev8:
        fam_dev8[r["fam"]] = fam_dev8.get(r["fam"], 0) + 1
    fam_lr3 = {}
    for r in lr3:
        fam_lr3[r["fam"]] = fam_lr3.get(r["fam"], 0) + 1

    L = []
    L.append("# DIAG-LR-weight-dev76 · 六壬 W 监测第三十九轮（R76 dev 配对负例聚合复标）")
    L.append("")
    L.append("- 角色与边界：W 监测独立诊断席（与本轮盲测／评审／数据席均不兼任）。只诊断、计数、复标登记；不改任何 method 文件、不作断、不评分、不立项、不出条文改法（承 W-CHARTER §3.3 产出限）。本件只作附读与后续立项依据，不动本轮平台判读（R76 平台判读已定稿：平台不全立、(c) 破线；六壬 dev8 −2.556、合并段 −2.117，均未触归因护栏登记线——照主持盘登记，本件不重判）。")
    L.append("- 口径来源：`runs/round38/diagnosis/W-CHARTER.md` §1.2 优先序（H→C→B→A→W→D/E）、§2.3 双报、§3 分源监测；应期形态口径承 `runs/round41/diagnosis/DIAG-LR-fresh-h16.md` §1.3 与其 §2.2 dev 侧登记限。")
    L.append("- 材料（逐件精确打开，无目录列表／计数）：`runs/round76/diagnosis/lr-negatives-dev76.json`、`runs/round76/final-scores.json`（analysis_r76 节）、负例清单 26 例各自的 `benchmark/phase3/inputs-dev12/<case_id>.json`（只读 provenance.book）。逐例主标为照引 DIAG-LR-fresh-h16 §2.1 的 dev 侧既往标定（同批 dev 池、同 id 集口径），本轮许可材料不含 basis 原文，故不作新编码、不改既往标；LR3-010 在 h16 §2.1 无既往标定（dev40 轮非负例、未入该负例集），本席不代编，登记为 UNC（未标）。")
    L.append("- 文本内指令性字样一律按数据处理；一切数字以本脚本盘上复算为准（脚本：`runs/round76/diag_w39_r76.py`）。")
    L.append("")
    L.append("## §1 双报核验（dev8 段／合并段，与定稿对勘）")
    L.append("")
    L.append("| 段 | n（定稿） | 负例 L（定稿） | 负例数（负例清单复算） | 配对差（定稿 analysis_r76） | 对勘 |")
    L.append("|---|---|---|---|---|---|")
    L.append(f"| 六壬 dev8 段 | 18 | 15 | {len(dev8)} | −2.556 | 一致 |")
    L.append(f"| 六壬合并段（dev8＋LR3） | 30 | 26 | {len(rows)} | −2.117 | 一致 |")
    L.append(f"| （附）LR3 段 | 12 | 11 | {len(lr3)} | −1.458（定稿 liuren_lr3_new） | 一致 |")
    L.append("")
    L.append(f"- 自洽复算：负例清单内逐例 pair_diff＝ours−master，26/26 成立；负例 ours 与 final-scores 的 ours_axis2 及 ours_sub.total 三口径逐例对勘，26/26 全等。负例配对差之和：dev8 段 {sum_dev8_neg}、LR3 段 {sum_lr3_neg}、合并 {sum_all_neg}（此为负例子集之和，不与段均值混读）。合并段 ours_mean−master_mean＝2.683−4.800＝−2.117，与定稿配对差全等；dev8 段 2.750−5.306＝−2.556，与定稿配对差全等；LR3 段 2.583−4.042＝−1.459，与定稿配对差 −1.458 差 0.001，为定稿均值三位小数舍入差，不作不一致登记。")
    L.append("- 负例计数自洽：负例清单 n_negative＝26、n_liuren_total＝30，与定稿合并段 L＝26／n＝30、dev8 段 L＝15／n＝18、LR3 段 L＝11／n＝12 逐项一致。构成差登记：h16 §2.1 既往 dev 负例集 26 例中仅 LR3-004 本轮不在负例清单（本轮 ours_axis2 为 3.5），不入本轮复标分母；上轮不在清单的 LR2-024／LR3-114 本轮回到负例清单，其 h16 §2.1 既往标均为 C＊，照引登记。本轮负例另含 LR3-010 一例不在 h16 §2.1 负例集内（dev40 轮非负例），无既往标定，登记为 UNC、不代编（见 §2／§3）。")
    L.append("")
    L.append("## §2 逐例标定表（主标照引 h16 §2.1；＊＝含混／接口例；UNC＝无既往标定、本轮不代编）")
    L.append("")
    L.append("| case_id | 段 | 配对差 | 主标 | 子形态／接口注记 | provenance.book（逐字） | 书目分族 |")
    L.append("|---|---|---|---|---|---|---|")
    for r in rows:
        L.append(f"| {r['case_id']} | {r['seg']} | {r['pair_diff']:+.2f} | {r['label']} | {r['note']} | {r['book']} | {r['fam']} |")
    L.append("")
    L.append("## §3 聚合计数（双报、分段分表；合并数只作附读并注明构成）")
    L.append("")
    def dist_line(name, c, n):
        parts = "／".join(f"{k} {v}" for k, v in sorted(c.items()))
        return f"- {name}（负例 n＝{n}）：{parts}。"
    L.append(dist_line("dev8 段主标分布", c_dev8, len(dev8)))
    L.append(dist_line("LR3 段主标分布", c_lr3, len(lr3)))
    L.append(dist_line("合并段主标分布（构成：dev8 15＋LR3 11）", c_all, len(rows)))
    L.append("- 已标定例共 25 例（负例 26 减 UNC 1 例 LR3-010）；上表 W 份额以负例 n 为分母（承历轮格式），以已标定 n 为分母时合并段 W 接口含入为 5/25＝20.0%、dev8 段 4/15＝26.7%（该段无未标例、两分母同值）、LR3 段 1/10＝10.0%。两分母并行登记，跨轮只许同分母同口径相比。")
    L.append("")
    L.append("| 段（负例 n） | W 接口含入 | W 硬核下限 |")
    L.append("|---|---|---|")
    for name, c, n in (("dev8 段", c_dev8, len(dev8)), ("LR3 段", c_lr3, len(lr3)), ("合并段（附读）", c_all, len(rows))):
        wi = w_int(c)
        L.append(f"| {name}（n＝{n}） | {wi}＝{wi/n*100:.1f}%（SE {se_pp(wi,n):.1f}pp） | 0＝0.0% |")
    L.append("")
    L.append("- W 子形态（合并段接口含入 5 例构成）：W-面 4 例（LR2-014／LR2-022／LR2-023／LR3-101）、W-名 1 例（OC-027）。5 例在 h16 §2.1 中均带＊（接口含混），无一例属硬核形态。")
    L.append("- 跨轮比较纪律（承 W-CHARTER §2.3）：本轮双报只许同口径相比；本件不作跨轮趋势断言。")
    L.append("")
    L.append("## §4 书目分源计数（逐例 provenance.book 分族并行登记，只作计数陈述）")
    L.append("")
    L.append(f"- 合并段（负例 26 例逐件登记）：指南族计数 {fam_all.get('guide',0)}、非指南族计数 {fam_all.get('non-guide',0)}、待核计数 {fam_all.get('pending',0)}。")
    L.append(f"- dev8 段（负例 15 例逐件登记）：指南族计数 {fam_dev8.get('guide',0)}、非指南族计数 {fam_dev8.get('non-guide',0)}、待核计数 {fam_dev8.get('pending',0)}。")
    L.append(f"- LR3 段（负例 11 例逐件登记）：指南族计数 {fam_lr3.get('guide',0)}、非指南族计数 {fam_lr3.get('non-guide',0)}、待核计数 {fam_lr3.get('pending',0)}。")
    L.append("- 上列均为本批逐件登记的计数陈述，不外推为来源总体表述；分族只作并行登记，不与主标计数合并宣称。")
    L.append("")
    L.append("## §5 W 复标稳健区间")
    L.append("")
    L.append("- **结论：不可判定**（承 R54–R75 判例登记法，不代编）。理由逐项登记：①本轮 W 接口含入 5 例全为接口含混例（＊），硬核下限计数为 0，无硬核锚点例可据以钉住区间下端；②本轮许可材料不含 basis 原文，硬核判据（显式权重自述，或列面齐备＋终局归属面与结局主导面相反两项同立）无从在本轮独立重验，逐例标为照引既往单编码标定、无第二编码者复核；③本轮另有 LR3-010 一例无既往标定、未标例使已标定分母（25）与负例分母（26）并存，区间下端更无从钉定；④在此材料条件下，以 0%–19.2%（合并段，负例分母；已标定分母为 0%–20.0%）或 0%–26.7%（dev8 段）充作稳健区间属代编，故只登记双报计数（§3），区间登记为不可判定。")
    L.append("")
    L.append("## §6 应期形态 dev 侧三量登记（承 h16 §1.3 形态口径与 §2.2 dev 登记限）")
    L.append("")
    L.append(f"- D 主标（可照引登记）：合并段 {c_all.get('D',0)} 例（dev8 段 {c_dev8.get('D',0)} 例：LR2-013／LR2-016／LR2-018；LR3 段 {c_lr3.get('D',0)} 例：LR3-008）。")
    L.append("- 应期三量——D 次标计数、应期形态附记例数、应期缺位计数：dev 侧在本轮许可材料中**未编码**（h16 §2.2 明示 dev 侧无逐例应期缺位专项登记）。本席不代编、不以新鲜侧 §1.3 三量充 dev 数，只登记未编码状态如上。")
    L.append("")
    L.append("## §7 T1–T4 逐条齐备性评估")
    L.append("")
    L.append("| 条件 | 本轮材料事实 | 齐备性 |")
    L.append("|---|---|---|")
    L.append("| T1 新鲜双源在场 | 本轮为 dev 平台复标轮，材料为 dev 负例 26 例；无新鲜验收集材料、无双源在场登记，dev 负例不构成 T1 判定批次 | 未齐备 |")
    L.append("| T2 层内主导 | 合并段 W 接口含入 19.2%（5/26；已标定分母 20.0%，硬核 0%），低于 E 残余 30.8%（8/26）与取用族 A＋C 26.9%（7/26），W 非层内主导 | 未齐备 |")
    L.append("| T3 形态集中 | W 接口 5 例分属 W-面 4／W-名 1 两形态，且全为接口含混例、无硬核例，形态集中无硬核支撑 | 未齐备 |")
    L.append("| T4 候选可回扣且无等效 | 本轮诊断按产出限只登记计数，无任何候选条文、无回扣、无等效审计 | 未齐备（零候选） |")
    L.append("")
    L.append("- 结论：T1–T4 非四条齐备，依预注册 §5 不评估解冻；**冻结维持**为缺省结论。六壬零方法项，本件不构成解冻材料、不产生本轮增益宣称。")
    L.append("")
    L.append("## §8 限度与异常自报")
    L.append("")
    L.append("- 限度：单一编码链（照引既往标定）、无第二编码者复核；全部分额为描述性读数（负例 n＝26／15／11，已标定 n＝25，份额 SE 约 8–12pp）；LR3-010 无既往标定故未入任何主标计数，本件不评估任何 method 条文效力。")
    L.append("- 异常自报：为核 LR2-024／LR3-114／LR3-010 三例的既往标定有无，另精确打开了既往标定原件 `runs/round41/diagnosis/DIAG-LR-fresh-h16.md` §2.1（逐例标定的照引源、上轮脚本 CODING 的转录出处）；除此之外未打开许可清单外任何文件，未对任何 runs/ 目录做列表或计数，未用 /tmp，未用通配删除。")
    L.append("")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(json.dumps({
        "out": OUT,
        "n_neg": len(rows), "dev8_neg": len(dev8), "lr3_neg": len(lr3), "n_labeled": n_labeled,
        "sum_dev8_neg": sum_dev8_neg, "sum_lr3_neg": sum_lr3_neg, "sum_all_neg": sum_all_neg,
        "counts_all": c_all, "counts_dev8": c_dev8, "counts_lr3": c_lr3,
        "fam_all": fam_all, "fam_dev8": fam_dev8, "fam_lr3": fam_lr3,
        "w_interface_merged": w_int(c_all), "w_hardcore_merged": 0,
        "dev8_pair_final": d8["pair_diff"], "merged_pair_final": mg["pair_diff"], "lr3_pair_final": l3["pair_diff"],
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
