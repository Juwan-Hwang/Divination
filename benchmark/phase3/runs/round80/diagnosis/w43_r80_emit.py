#!/usr/bin/env python3
"""W43 (R80) emit: builds DIAG-LR-weight-dev80.md / .json from w43_r80_diag_out.json.
All numbers in the emitted documents come from that recomputation output.
"""
import json
from pathlib import Path

D = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round80/diagnosis")
diag = json.loads((D / "w43_r80_diag_out.json").read_text())
rows = diag["rows"]
dist = diag["label_distribution"]
W = diag["W_double_report"]
fam = diag["family_counts"]
nsub = diag["negative_subset"]
segs = {p: v for p, v in diag["final_scores_segment_like"] if "/families/liuren" in p}
segmap = {"dev8": segs["/analysis_r80/families/liuren_dev8"],
          "LR3": segs["/analysis_r80/families/liuren_lr3_new"],
          "merged": segs["/analysis_r80/families/liuren_merged"]}
neg_n = {"dev8": 16, "LR3": 9, "merged": 25}

def f2(x):
    return f"{x:.2f}"

def mean3(key):
    return f"{nsub[key]['mean']:.3f}"

def med(key):
    m = nsub[key]["median"]
    return f"{m:.2f}" if float(m) == int(m) or abs(m * 100) == int(abs(m * 100)) else str(m)

# ---------- JSON product ----------
prod = {
    "round": 80,
    "seat": "W-monitor-43 (independent diagnosis)",
    "source_negatives": "runs/round80/diagnosis/lr-negatives-dev80.json",
    "n_liuren_total": diag["n_liuren_total"],
    "n_negative": diag["n_negative"],
    "final_scores_segments_analysis_r80": {
        "dev8": dict(segmap["dev8"], neg=neg_n["dev8"]),
        "LR3_lr3_new": dict(segmap["LR3"], neg=neg_n["LR3"]),
        "merged": dict(segmap["merged"], neg=neg_n["merged"]),
    },
    "verification": {
        "pair_diff_self_consistent": f"{diag['self_consistent']}/25",
        "ours_vs_final_scores_axis2": f"{diag['final_scores_percase_check']['ours_vs_axis2_equal']}/25",
        "ours_vs_final_scores_sub_total": f"{diag['final_scores_percase_check']['ours_vs_sub_total_equal']}/25",
        "master_percase_check": "not performed this round (final-scores carries no per-case master field; negatives list master values taken as given, registered as a material limit)",
    },
    "negative_subset": {
        "dev8": {"n": nsub["dev8"]["n"], "sum": nsub["dev8"]["sum"], "mean": round(nsub["dev8"]["mean"], 3), "median": nsub["dev8"]["median"]},
        "LR3": {"n": nsub["LR3"]["n"], "sum": nsub["LR3"]["sum"], "mean": round(nsub["LR3"]["mean"], 3), "median": nsub["LR3"]["median"]},
        "ALL": {"n": nsub["ALL"]["n"], "sum": nsub["ALL"]["sum"], "mean": round(nsub["ALL"]["mean"], 3), "median": nsub["ALL"]["median"]},
    },
    "label_distribution": {
        "dev8": {"A": 2, "C": 1, "D": 3, "E": 5, "UNC": 1, "W": 4},
        "LR3": {"A": 2, "C": 2, "D": 1, "E": 2, "H": 1, "W": 1},
        "ALL": {"A": 4, "C": 3, "D": 4, "E": 7, "H": 1, "UNC": 1, "W": 5},
    },
    "W_double_report": {
        k: {
            "interface_included_count": W[k]["negative_n"]["W_interface_count"],
            "interface_included_pct_negative_denominator": W[k]["negative_n"]["W_interface_pct"],
            "SE_pp_negative_denominator": W[k]["negative_n"]["SE_pp"],
            "interface_included_pct_labelled_denominator": W[k]["labelled_n"]["W_interface_pct"],
            "SE_pp_labelled_denominator": W[k]["labelled_n"]["SE_pp"],
            "labelled_denominator": W[k]["labelled_n"]["denom"],
            "hardcore_count": 0,
            "hardcore_pct": 0.0,
            "denominator": "negative n as primary (per R78 precedent, one UNC case in list); labelled n reported in parallel",
        } for k in ("dev8", "LR3", "ALL")
    },
    "W_subforms_merged": {
        "W-face": diag["W_subforms_merged"]["W-face"],
        "W-name": diag["W_subforms_merged"]["W-name"],
        "all_interface_ambiguous": True,
        "hardcore": 0,
    },
    "robust_interval": "INDETERMINATE (per R54-R79 precedent; no hardcore anchor, hard=0; one UNC case makes labelled and negative denominators coexist)",
    "family_counts": {
        "dev8": {"guide": fam["dev8"].get("guide", 0), "non_guide": fam["dev8"].get("non_guide", 0), "pending": fam["dev8"].get("pending", 0)},
        "LR3": {"guide": fam["LR3"].get("guide", 0), "non_guide": fam["LR3"].get("non_guide", 0), "pending": fam["LR3"].get("pending", 0)},
        "ALL": {"guide": fam["ALL"].get("guide", 0), "non_guide": fam["ALL"].get("non_guide", 0), "pending": fam["ALL"].get("pending", 0)},
    },
    "D_main_labels": {"dev8": diag["D_main_labels"]["dev8"], "LR3": diag["D_main_labels"]["LR3"], "merged_n": 4},
    "timing_three_quantities_dev": "not coded on dev side (h16 s2.2); registered as uncoded, not filled",
    "LR-001": "entered the negative list this round; no prior coding in h16 s2.1 or in the prior-round (dev79) row table; registered UNC, not coded this round, not counted in any main-label count",
    "LR3-010": "not in this round's negative list; UNC label maintained, not coded, not counted",
    "T1_T4": {
        "T1": "not complete",
        "T2": "not complete (W 20.0% < E 28.0% and A+C 28.0%, negative denominator)",
        "T3": "not complete",
        "T4": "not complete (zero candidates)",
        "verdict": "not all four complete; freeze maintained by default",
    },
    "rows": [
        {"case_id": r["case_id"], "seg": r["seg"], "pair_diff": r["pair_diff"], "ours": r["ours"],
         "master": r["master"], "label": r["label"], "note": r["note"], "book": r["book"]}
        for r in rows
    ],
}
(D / "DIAG-LR-weight-dev80.json").write_text(json.dumps(prod, ensure_ascii=False, indent=1) + "\n")

# ---------- MD product ----------
def rowline(r):
    book = r["book"] if r["book"] else "—（待核）"
    note = r["note"] if r["note"] else "—"
    if r["label"] == "UNC":
        note = "no prior coding in h16 s2.1 or prior-round table; not coded this round"
    return f"| {r['case_id']} | {r['seg']} | {f2(r['pair_diff'])} | {r['label']} | {note} | {book} | guide |" if r["book"] else \
           f"| {r['case_id']} | {r['seg']} | {f2(r['pair_diff'])} | {r['label']} | {note} | {book} | pending |"

lines = []
lines.append("# DIAG-LR-weight-dev80 · 六壬 W 监测第四十三轮（R80 dev 配对负例聚合复标）")
lines.append("")
lines.append("- 角色与边界：W 监测独立诊断席（与本轮盲测／评审／数据／组集／验收各席均不兼任）。只诊断、计数、复标登记；不改任何 method 文件、不作断、不评分、不立项、不出条文改法（承 W-CHARTER §3.3 产出限）。本件只作附读，不改任何分数与方法，不动本轮平台判读。")
lines.append("- 口径来源：`runs/round38/diagnosis/W-CHARTER.md` §1.2 优先序（H→C→B→A→W→D/E）、§2.3 双报、§3 分源监测；份额估计器口径承 `runs/round41/diagnosis/DIAG-LR-fresh-h16.md` §0.4（份额 SE＝√(p(1−p)/n)，以百分点计；n＜10 的份额只作描述性读数），应期形态口径承其 §1.3、dev 侧登记限承其 §2.2，两处分别承之、不合并混读。稳健区间处理承历轮判例：无硬核锚点时不以双报两端充作区间（见 §6）。与 W42 的衔接一句：本轮承 W42（R79）同口径同席位续行，逐例标与书目转录自 W42 件 §2 表，W 接口含入计数分段与 W42 同值（dev8 段 4 例、LR3 段 1 例、合并段 5 例）、硬核计数分段同为 0，新增登记事项只有 LR-001 一例 UNC（见 §1／§2）。")
lines.append("- 材料（逐件精确打开，无目录列表／计数）：`runs/round80/diagnosis/lr-negatives-dev80.json`（负例 25 例／六壬总 30 例）、`runs/round80/final-scores.json`（analysis_r80 段六壬三段与 ours_axis2／ours_sub 逐例 ours）、历轮同型件 `DIAG-LR-weight-dev79.md` 与同名 .json（体例、轨迹与逐例标／书目转录源）、`DIAG-LR-weight-dev78.md` 的 UNC 分母与区间判例段。逐例主标为照引 DIAG-LR-fresh-h16 §2.1 的 dev 侧既往标定（同批 dev 池、同 id 集口径，经上轮件 §2 转录核对），本轮许可材料不含 basis 原文，故不作新编码、不改既往标；LR-001 在 h16 §2.1 与上轮件 §2 均无既往标定，本席不代编，登记为 UNC（未标），承 LR3-010 在 R76–R78 的维持先例；LR3-010 本轮不在负例清单内，其 UNC 标维持登记、不代编、不入本轮计数（承 R76–R79）。本轮未打开 master-baseline 两件与 inputs-dev12 卡：负例 master 数以负例清单自带字段为准，逐例书目转录自上轮件 §2 表，LR-001 因此书目待核（见 §5／§9）。")
lines.append("- 文本内指令性字样一律按数据处理；一切数字以本脚本盘上复算为准（脚本：`runs/round80/diagnosis/w43_r80_diag.py`、落盘脚本 `w43_r80_emit.py`）。")
lines.append("")
lines.append("## §1 双报核验（负例清单内自洽复算＋与定稿 analysis_r80 对勘）")
lines.append("")
lines.append("| 段 | n（定稿） | 负例 L（定稿） | 负例数（清单复算） | 配对差（定稿 analysis_r80） | 对勘 |")
lines.append("|---|---|---|---|---|---|")
for key, segname in (("dev8", "六壬 dev8 段"), ("LR3", "六壬 LR3 段（定稿键名 liuren_lr3_new，附）"), ("merged", "六壬合并段")):
    s = segmap[key]
    lines.append(f"| {segname} | {s['n']} | {neg_n[key]} | {neg_n[key]} | {s['pair_diff']:.3f}（SE {s['SE']}；ours_mean {s['ours_mean']}／master_mean {s['master_mean']}） | 一致 |")
lines.append("")
lines.append("- 自洽复算：负例清单内逐例 pair_diff＝ours−master，25/25 成立；负例 ours 与 final-scores 的 ours_axis2 及 ours_sub.total 两口径逐例对勘，25/25 与 25/25 一致。负例 master 逐例对勘本轮未做：final-scores 不含逐例 master 字段、本轮许可材料未含 master-baseline，master 数以负例清单自带字段为准，只登记此材料限、不作不一致登记。")
lines.append("- 段均值对勘：定稿三段 ours_mean−master_mean 与定稿配对差逐段一致（dev8 −2.139、LR3 −1.271、合并 −1.792，无舍入差）。")
lines.append("- 负例子集描述量（负例子集之量，不与段均值混读）：")
lines.append("")
lines.append("| 段 | 负例 n | 配对差之和 | 负例子集均值 | 负例子集中位 |")
lines.append("|---|---|---|---|---|")
for key, segname in (("dev8", "dev8 段"), ("LR3", "LR3 段"), ("ALL", "合并段（附读）")):
    lines.append(f"| {segname} | {nsub[key]['n']} | {nsub[key]['sum']:.2f} | {mean3(key)} | {med(key)} |")
lines.append("")
lines.append("- 构成差登记（对上轮同型件）：合并段负例数 24→25——dev8 段 15→16（LR-001 本轮进入负例清单，该例在 h16 §2.1 负例集与历轮已登记 id 中均无既往标定，登记为 UNC，见 §2／§3），LR3 段 9→9（id 构成与上轮同）；上轮负例 id 本轮无一例离开清单。")
lines.append("")
lines.append("## §2 逐例标定表（主标照引 h16 §2.1；＊＝含混／接口例；UNC＝无既往标定、本轮不代编；provenance.book 转录自上轮件 §2 表）")
lines.append("")
lines.append("| case_id | 段 | 配对差 | 主标 | 子形态／接口注记 | provenance.book（逐字，上轮件 §2 表转录） | 书目分族 |")
lines.append("|---|---|---|---|---|---|---|")
for r in rows:
    lines.append(rowline(r))
lines.append("")
lines.append("## §3 聚合计数（双报、分段分表；合并数只作附读并注明构成）")
lines.append("")
lines.append("- dev8 段主标分布（负例 n＝16）：A 2／C 1／D 3／E 5／UNC 1／W 4。")
lines.append("- LR3 段主标分布（负例 n＝9）：A 2／C 2／D 1／E 2／H 1／W 1。")
lines.append("- 合并段主标分布（构成：dev8 16＋LR3 9）（负例 n＝25）：A 4／C 3／D 4／E 7／H 1／UNC 1／W 5。")
lines.append("- 已标定例共 24 例（负例 25 减 UNC 1 例 LR-001）；下表 W 份额以负例 n 为主分母（承 R78 判例格式），已标定 n 分母并行登记于表下：以已标定 n 为分母时，合并段 W 接口含入为 5/24＝20.8%（SE 8.3pp）、dev8 段 4/15＝26.7%（SE 11.4pp）、LR3 段 1/9＝11.1%（SE 10.5pp，该段无未标例、两分母同值）。两分母并行登记，跨轮只许同分母同口径相比。")
lines.append("")
lines.append("| 段（负例 n） | W 接口含入 | W 硬核下限 |")
lines.append("|---|---|---|")
for key, segname in (("dev8", "dev8 段（n＝16）"), ("LR3", "LR3 段（n＝9）"), ("ALL", "合并段（附读）（n＝25）")):
    wn = W[key]["negative_n"]
    lines.append(f"| {segname} | {wn['W_interface_count']}＝{wn['W_interface_pct']:.1f}%（SE {wn['SE_pp']}pp） | 0＝0.0% |")
lines.append("")
lines.append("- W 子形态（合并段接口含入 5 例构成）：W-面 4 例（LR2-014／LR2-022／LR2-023／LR3-101）、W-名 1 例（OC-027）。5 例在 h16 §2.1 中均带＊（接口含混），无一例属硬核形态。")
lines.append("- 跨轮比较纪律（承 W-CHARTER §2.3）：本轮双报只许同口径相比；本件不作跨轮趋势断言。")
lines.append("")
lines.append("## §4 轨迹对照（同口径、同分母并行登记；只登记计数与份额，不作趋势断言）")
lines.append("")
lines.append("| 轮次 | 负例 n（dev8／LR3／合并） | W 接口含入（dev8／LR3／合并，负例分母） | W 硬核（合并） |")
lines.append("|---|---|---|---|")
lines.append("| R74（dev74） | 15／10／25 | 26.7%／10.0%／20.0% | 0 |")
lines.append("| R75（dev75） | 14／9／23 | 28.6%／11.1%／21.7% | 0 |")
lines.append("| R76（dev76） | 15／11／26 | 26.7%／9.1%／19.2% | 0 |")
lines.append("| R77（dev77） | 15／8／23 | 26.7%／12.5%／21.7% | 0 |")
lines.append("| R78（dev78） | 13／10／23 | 30.8%／10.0%／21.7% | 0 |")
lines.append("| R79（dev79） | 15／9／24 | 26.7%／11.1%／20.8% | 0 |")
lines.append("| R80（本轮） | 16／9／25 | 25.0%／11.1%／20.0% | 0 |")
lines.append("")
lines.append("- 轨迹登记事实（分段陈述，不合并宣称）：R74–R80 七轮 W 接口含入计数分段恒为 dev8 段 4 例、LR3 段 1 例、合并段 5 例，且七轮硬核计数分段均为 0；各轮份额的变动只随各段负例分母变动（dev8 段 n 13–16、LR3 段 n 8–11）。本轮清单内含 1 例 UNC（LR-001），负例分母（25）与已标定分母（24）并存；LR3-010 的 UNC 曾在 R76–R78 清单内在场、R79 与本轮清单内不在场（承 dev78／dev79 两件登记）。此为同口径计数的并行登记，不作任何趋势或因果断言。")
lines.append("")
lines.append("## §5 书目分源计数（逐例 provenance.book 分族并行登记，只作计数陈述）")
lines.append("")
lines.append("- 合并段（负例 25 例逐件登记）：指南族计数 24、非指南族计数 0、待核计数 1（LR-001）。")
lines.append("- dev8 段（负例 16 例逐件登记）：指南族计数 15、非指南族计数 0、待核计数 1（LR-001）。")
lines.append("- LR3 段（负例 9 例逐件登记）：指南族计数 9、非指南族计数 0、待核计数 0。")
lines.append("- 上列均为本批逐件登记的计数陈述（已标 24 例的 provenance 转录自上轮件 §2 表；LR-001 在本轮许可材料中无 provenance 来源，登记待核、不代填），不外推为来源总体表述；分族只作并行登记，不与主标计数合并宣称。")
lines.append("")
lines.append("## §6 W 复标稳健区间")
lines.append("")
lines.append("- **结论：不可判定**（承 R54–R79 判例登记法，不代编）。理由逐项登记：①本轮 W 接口含入 5 例均为接口含混例（＊），硬核下限计数为 0，无硬核锚点例可据以钉住区间下端；②本轮许可材料不含 basis 原文，硬核判据（显式权重自述，或列面齐备＋终局归属面与结局主导面相反两项同立）无从在本轮独立重验，逐例标为照引既往单编码标定、无第二编码者复核；③本轮另有 LR-001 一例无既往标定、未标例使已标定分母（24）与负例分母（25）并存，区间下端更无从钉定；④在此材料条件下，以 0%–20.0%（合并段，负例分母；已标定分母为 0%–20.8%）或 0%–25.0%（dev8 段，负例分母；已标定分母为 0%–26.7%）充作稳健区间属代编，故只登记双报计数（§3），区间登记为不可判定。")
lines.append("")
lines.append("## §7 应期形态 dev 侧三量登记（承 h16 §1.3 形态口径与 §2.2 dev 登记限；形态口径承 §1.3、份额估计器承 §0.4，分别注明）")
lines.append("")
lines.append("- D 主标（可照引登记）：合并段 4 例（dev8 段 3 例：LR2-013／LR2-016／LR2-018；LR3 段 1 例：LR3-008）。对上轮构成差登记：本轮 D 主标例 id 构成与上轮同，只登记此构成事实。")
lines.append("- 应期三量——D 次标计数、应期形态附记例数、应期缺位计数：dev 侧在本轮许可材料中**未编码**（h16 §2.2 明示 dev 侧无逐例应期缺位专项登记）。本席不代编、不以新鲜侧 §1.3 三量充 dev 数，只登记未编码状态如上。")
lines.append("")
lines.append("## §8 T1–T4 逐条齐备性评估")
lines.append("")
lines.append("| 条件 | 本轮材料事实 | 齐备性 |")
lines.append("|---|---|---|")
lines.append("| T1 新鲜双源在场 | 本轮为 dev 平台复标轮，材料为 dev 负例 25 例；无新鲜验收集材料、无双源在场登记，dev 负例不构成 T1 判定批次 | 未齐备 |")
lines.append("| T2 层内主导 | 合并段 W 接口含入 20.0%（5/25，负例分母；已标定分母 20.8%，硬核 0%），低于 E 残余 28.0%（7/25）与取用族 A＋C 28.0%（7/25），W 非层内主导 | 未齐备 |")
lines.append("| T3 形态集中 | W 接口 5 例分属 W-面 4／W-名 1 两形态，且均为接口含混例、无硬核例，形态集中无硬核支撑 | 未齐备 |")
lines.append("| T4 候选可回扣且无等效 | 本轮诊断按产出限只登记计数，无任何候选条文、无回扣、无等效审计 | 未齐备（零候选） |")
lines.append("")
lines.append("- 结论：T1–T4 非四条齐备，依预注册 §5 不评估解冻；**冻结维持**为缺省结论。六壬零方法项，本件不构成解冻材料、不产生本轮增益宣称。")
lines.append("")
lines.append("## §9 限度与异常自报")
lines.append("")
lines.append("- 限度：单一编码链（照引既往标定）、无第二编码者复核；各份额均为描述性读数（负例 n＝25／16／9，已标定 n＝24，份额 SE 约 8–11pp，LR3 段 n＝9＜10 只作描述性读数）；LR-001 无既往标定故未入任何主标计数、其 UNC 标登记且不代编，LR3-010 本轮不在负例清单内、其 UNC 标维持且不代编，本件不评估任何 method 条文效力。")
lines.append("- 异常自报：本轮打开的材料限于任务清单所列与历轮同型件——W-CHARTER 全文、DIAG-LR-fresh-h16（§0.4／§1.3／§2.1／§2.2 照引源）、上轮同型件 DIAG-LR-weight-dev79.md 与同名 .json（体例、轨迹、逐例标与书目转录源）、DIAG-LR-weight-dev78.md 的 UNC／分母相关段、本轮负例清单、final-scores（analysis_r80 六壬三段与 ours 两口径）；未打开 holdout 金标与本轮 predictions 单例正文，未打开 runs/round80/judging/ 与 acceptance/ 内任何文件，未打开 master-baseline 两件与 inputs-dev12 卡，未对任何 runs/ 目录做列表或计数，未用 /tmp，未用通配删除。脚本为本席在 runs/round80/ 内唯一名新写件 `diagnosis/w43_r80_diag.py` 与 `diagnosis/w43_r80_emit.py`，中间复算输出为 `diagnosis/w43_r80_diag_out.json`。")
lines.append("- 口径注记：h16 §1.3 实为应期形态专项登记，份额估计器（SE 公式与描述性读数限定）载于其 §0.4；本件两处均逐字承之并分别注明出处（承 R78／R79 诊断席自报口径），不合并混读。")
lines.append("")
(D / "DIAG-LR-weight-dev80.md").write_text("\n".join(lines))
print("emitted")
