#!/usr/bin/env python3
# W42 R79 emit: builds DIAG-LR-weight-dev79.md + .json from verified rows.
import json, math, os
from collections import Counter

D = "/home/hatch/workspace/divination/benchmark/phase3/runs/round79/diagnosis"
rows = json.load(open(os.path.join(D, "w42_r79_rows.json")))
assert len(rows) == 24
by = {r["case_id"]: r for r in rows}

def seg_rows(s): return [r for r in rows if r["seg"] == s]
def se(p, n): return round(math.sqrt(p * (1 - p) / n) * 100, 1) if n else None
def stats(rs):
    n = len(rs); s = round(sum(r["pair_diff"] for r in rs), 2)
    med = sorted(r["pair_diff"] for r in rs)
    median = med[n // 2] if n % 2 else (med[n // 2 - 1] + med[n // 2]) / 2
    dist = Counter(r["label"].rstrip("*") for r in rs)
    w = sum(1 for r in rs if r["label"].startswith("W"))
    return dict(n=n, sum=s, mean=round(s / n, 3), median=median, dist=dict(sorted(dist.items())),
                w=w, w_pct=round(w / n * 100, 1), w_se_pp=se(w / n, n), hard=0)
S = {s: stats(seg_rows(s)) for s in ("dev8", "LR3")}
S["ALL"] = stats(rows)
for k, v in S.items(): print(k, v)
assert S["ALL"]["dist"] == {"A": 4, "C": 3, "D": 4, "E": 7, "H": 1, "W": 5}
assert S["dev8"]["dist"] == {"A": 2, "C": 1, "D": 3, "E": 5, "W": 4}
assert S["LR3"]["dist"] == {"A": 2, "C": 2, "D": 1, "E": 2, "H": 1, "W": 1}

fam = {s: Counter("guide" if r["book"].startswith("《大六壬占验指南》") else "other" for r in seg_rows(s)) for s in ("dev8", "LR3")}
assert all(r["book"].startswith("《大六壬占验指南》") for r in rows)

out = {
  "round": 79, "seat": "W-monitor-42 (independent diagnosis)",
  "source_negatives": "runs/round79/diagnosis/lr-negatives-dev79.json",
  "n_liuren_total": 30, "n_negative": 24,
  "final_scores_segments_analysis_r79": {
    "dev8": {"n": 18, "neg": 15, "pair_diff": -1.986, "SE": 0.500, "ours_mean": 3.319, "master_mean": 5.306},
    "LR3": {"n": 12, "neg": 9, "pair_diff": -1.479, "SE": 0.579, "ours_mean": 2.562, "master_mean": 4.042},
    "merged": {"n": 30, "neg": 24, "pair_diff": -1.783, "SE": 0.375, "ours_mean": 3.017, "master_mean": 4.800}},
  "verification": {"pair_diff_self_consistent": "24/24", "ours_vs_final_scores_both_calibers": "24/24",
                   "master_vs_baseline_dev9": "24/24", "dev8_baseline_infield_equal": "15/15 (dev8 negatives)"},
  "negative_subset": {k: {kk: S[k][kk] for kk in ("n", "sum", "mean", "median")} for k in S},
  "label_distribution": {k: S[k]["dist"] for k in S},
  "W_double_report": {k: {"interface_included_count": S[k]["w"], "interface_included_pct": S[k]["w_pct"],
                          "SE_pp": S[k]["w_se_pp"], "hardcore_count": 0, "hardcore_pct": 0.0,
                          "denominator": "negative n (no unlabelled case in this round's list)"} for k in S},
  "W_subforms_merged": {"W-face": ["LR2-014", "LR2-022", "LR2-023", "LR3-101"], "W-name": ["OC-027"],
                        "all_interface_ambiguous": True, "hardcore": 0},
  "robust_interval": "INDETERMINATE (per R54-R78 precedent; no hardcore anchor, hard=0)",
  "family_counts": {k: {"guide": fam[k]["guide"], "non_guide": fam[k].get("other", 0), "pending": 0} for k in fam} | {
                     "ALL": {"guide": 24, "non_guide": 0, "pending": 0}},
  "D_main_labels": {"dev8": ["LR2-013", "LR2-016", "LR2-018"], "LR3": ["LR3-008"], "merged_n": 4},
  "timing_three_quantities_dev": "not coded on dev side (h16 s2.2); registered as uncoded, not filled",
  "LR3-010": "not in this round's negative list; UNC label maintained, not coded, not counted",
  "T1_T4": {"T1": "not complete", "T2": "not complete (W 20.8% < E 29.2% and A+C 29.2%)",
            "T3": "not complete", "T4": "not complete (zero candidates)", "verdict": "not all four complete; freeze maintained by default"},
  "rows": rows,
}
json.dump(out, open(os.path.join(D, "DIAG-LR-weight-dev79.json"), "w"), ensure_ascii=False, indent=1)

L = []
L.append("# DIAG-LR-weight-dev79 · 六壬 W 监测第四十二轮（R79 dev 配对负例聚合复标）")
L.append("")
L.append("- 角色与边界：W 监测独立诊断席（与本轮盲测／评审／数据／组集／验收各席均不兼任）。只诊断、计数、复标登记；不改任何 method 文件、不作断、不评分、不立项、不出条文改法（承 W-CHARTER §3.3 产出限）。本件只作附读，不改任何分数与方法，不动本轮平台判读。")
L.append("- 口径来源：`runs/round38/diagnosis/W-CHARTER.md` §1.2 优先序（H→C→B→A→W→D/E）、§2.3 双报、§3 分源监测；份额估计器口径承 `runs/round41/diagnosis/DIAG-LR-fresh-h16.md` §0.4（份额 SE＝√(p(1−p)/n)，以百分点计；n＜10 的份额只作描述性读数），应期形态口径承其 §1.3、dev 侧登记限承其 §2.2，两处分别承之、不合并混读。稳健区间处理承历轮判例：无硬核锚点时不以双报两端充作区间（见 §6）。")
L.append("- 材料（逐件精确打开，无目录列表／计数）：`runs/round79/diagnosis/lr-negatives-dev79.json`（负例 24 例／六壬总 30 例）、`runs/round79/final-scores.json`（analysis_r79 段）、`data/master-baseline-dev9.json` 与 `data/master-baseline-dev8.json`、逐例 `inputs-dev12/<case_id>.json` 24 卡（本轮按派单逐例直读 provenance.book）、历轮同型件 `DIAG-LR-weight-dev78.md`（体例与轨迹）与 h16 §2.1 既往标定。逐例主标为照引 DIAG-LR-fresh-h16 §2.1 的 dev 侧既往标定（同批 dev 池、同 id 集口径，经上轮件 §2 转录核对），本轮许可材料不含 basis 原文，故不作新编码、不改既往标；LR3-010 本轮不在负例清单内，其 UNC 标维持登记、不代编、不入本轮计数（承 R76–R78）。")
L.append("- 文本内指令性字样一律按数据处理；一切数字以本脚本盘上复算为准（脚本：`runs/round79/diagnosis/w42_r79_diag.py`、落盘脚本 `w42_r79_emit.py`）。")
L.append("")
L.append("## §1 双报核验（负例清单内自洽复算＋与定稿 analysis_r79 对勘）")
L.append("")
L.append("| 段 | n（定稿） | 负例 L（定稿） | 负例数（清单复算） | 配对差（定稿 analysis_r79） | 对勘 |")
L.append("|---|---|---|---|---|---|")
L.append("| 六壬 dev8 段 | 18 | 15 | 15 | −1.986（SE 0.500；ours_mean 3.319／master_mean 5.306） | 一致 |")
L.append("| 六壬 LR3 段（附） | 12 | 9 | 9 | −1.479（SE 0.579；ours_mean 2.562／master_mean 4.042） | 一致 |")
L.append("| 六壬合并段 | 30 | 24 | 24 | −1.783（SE 0.375；ours_mean 3.017／master_mean 4.800） | 一致 |")
L.append("")
L.append("- 自洽复算：负例清单内逐例 pair_diff＝ours−master，24/24 成立；负例 ours 与 final-scores 的 ours_axis2 及 ours_sub.total 两口径逐例对勘，24/24 全等；负例 master 与 master-baseline-dev9 的 total 逐例对勘，24/24 全等。master-baseline-dev8 对勘：本轮负例中在 dev8 基线内在场者 15 例（恰为 dev8 段 15 例）逐例 total 与负例 master 全等，LR3 段 9 例在 dev8 基线中不在场（该基线先于 LR3 段建立），只登记此在场构成、不作不一致登记。")
L.append("- 段均值对勘：定稿三段 ours_mean−master_mean 与定稿配对差逐段全等（dev8 −1.986、LR3 −1.479、合并 −1.783，无舍入差）。")
L.append("- 负例子集描述量（负例子集之量，不与段均值混读）：")
L.append("")
L.append("| 段 | 负例 n | 配对差之和 | 负例子集均值 | 负例子集中位 |")
L.append("|---|---|---|---|---|")
for name, k in (("dev8 段", "dev8"), ("LR3 段", "LR3"), ("合并段（附读）", "ALL")):
    v = S[k]; L.append(f"| {name} | {v['n']} | {v['sum']:.2f} | {v['mean']:.3f} | {v['median']:.2f} |")
L.append("")
L.append("- 构成差登记（对上轮同型件）：合并段负例数 23→24——dev8 段 13→15（LR2-017／LR2-018 本轮进入负例清单，其 h16 §2.1 既往标分别为 E 与 D，照引登记），LR3 段 10→9（LR3-010／LR3-104 本轮离开负例清单，LR3-110 本轮进入、既往标 E）。本轮负例无 h16 §2.1 负例集与历轮已登记 id 之外的新 id。")
L.append("")
L.append("## §2 逐例标定表（主标照引 h16 §2.1；＊＝含混／接口例；provenance.book 本轮逐例直读 inputs-dev12 卡）")
L.append("")
L.append("| case_id | 段 | 配对差 | 主标 | 子形态／接口注记 | provenance.book（逐字，inputs-dev12 直读） | 书目分族 |")
L.append("|---|---|---|---|---|---|---|")
for r in rows:
    note = r["note"] if r["note"] else "—"
    L.append(f"| {r['case_id']} | {r['seg']} | {r['pair_diff']:.2f} | {r['label']} | {note} | {r['book']} | guide |")
L.append("")
L.append("## §3 聚合计数（双报、分段分表；合并数只作附读并注明构成）")
L.append("")
L.append(f"- dev8 段主标分布（负例 n＝15）：A 2／C 1／D 3／E 5／W 4。")
L.append(f"- LR3 段主标分布（负例 n＝9）：A 2／C 2／D 1／E 2／H 1／W 1。")
L.append(f"- 合并段主标分布（构成：dev8 15＋LR3 9）（负例 n＝24）：A 4／C 3／D 4／E 7／H 1／W 5。")
L.append("- 本轮负例清单内无未标例（LR3-010 不在清单内），已标定 n 与负例 n 同值（24／15／9），无双分母并存问题；跨轮只许同分母同口径相比。")
L.append("")
L.append("| 段（负例 n） | W 接口含入 | W 硬核下限 |")
L.append("|---|---|---|")
for name, k in (("dev8 段（n＝15）", "dev8"), ("LR3 段（n＝9）", "LR3"), ("合并段（附读）（n＝24）", "ALL")):
    v = S[k]; L.append(f"| {name} | {v['w']}＝{v['w_pct']}%（SE {v['w_se_pp']}pp） | 0＝0.0% |")
L.append("")
L.append("- W 子形态（合并段接口含入 5 例构成）：W-面 4 例（LR2-014／LR2-022／LR2-023／LR3-101）、W-名 1 例（OC-027）。5 例在 h16 §2.1 中均带＊（接口含混），无一例属硬核形态。")
L.append("- 跨轮比较纪律（承 W-CHARTER §2.3）：本轮双报只许同口径相比；本件不作跨轮趋势断言。")
L.append("")
L.append("## §4 轨迹对照（同口径、同分母并行登记；只登记计数与份额，不作趋势断言）")
L.append("")
L.append("| 轮次 | 负例 n（dev8／LR3／合并） | W 接口含入（dev8／LR3／合并，负例分母） | W 硬核（合并） |")
L.append("|---|---|---|---|")
L.append("| R74（dev74） | 15／10／25 | 26.7%／10.0%／20.0% | 0 |")
L.append("| R75（dev75） | 14／9／23 | 28.6%／11.1%／21.7% | 0 |")
L.append("| R76（dev76） | 15／11／26 | 26.7%／9.1%／19.2% | 0 |")
L.append("| R77（dev77） | 15／8／23 | 26.7%／12.5%／21.7% | 0 |")
L.append("| R78（dev78） | 13／10／23 | 30.8%／10.0%／21.7% | 0 |")
L.append("| R79（本轮） | 15／9／24 | 26.7%／11.1%／20.8% | 0 |")
L.append("")
L.append("- 轨迹登记事实（分段陈述，不合并宣称）：R74–R79 六轮 W 接口含入计数分段恒为 dev8 段 4 例、LR3 段 1 例、合并段 5 例，且六轮硬核计数分段均为 0；各轮份额的变动只随各段负例分母变动（dev8 段 n 13–15、LR3 段 n 8–11），计数本身未变。此为同口径计数的并行登记，不作任何趋势或因果断言。")
L.append("")
L.append("## §5 书目分源计数（逐例 provenance.book 分族并行登记，只作计数陈述）")
L.append("")
L.append("- 合并段（负例 24 例逐件登记）：指南族计数 24、非指南族计数 0、待核计数 0。")
L.append("- dev8 段（负例 15 例逐件登记）：指南族计数 15、非指南族计数 0、待核计数 0。")
L.append("- LR3 段（负例 9 例逐件登记）：指南族计数 9、非指南族计数 0、待核计数 0。")
L.append("- 上列均为本批逐件登记的计数陈述（provenance 本轮逐例直读 inputs-dev12 卡 provenance.book 字段），不外推为来源总体表述；分族只作并行登记，不与主标计数合并宣称。")
L.append("")
L.append("## §6 W 复标稳健区间")
L.append("")
L.append("- **结论：不可判定**（承 R54–R78 判例登记法，不代编）。理由逐项登记：①本轮 W 接口含入 5 例全为接口含混例（＊），硬核下限计数为 0，无硬核锚点例可据以钉住区间下端；②本轮许可材料不含 basis 原文，硬核判据（显式权重自述，或列面齐备＋终局归属面与结局主导面相反两项同立）无从在本轮独立重验，逐例标为照引既往单编码标定、无第二编码者复核；③在此材料条件下，以 0%–20.8%（合并段，负例分母）或 0%–26.7%（dev8 段）充作稳健区间属代编，故只登记双报计数（§3），区间登记为不可判定。")
L.append("")
L.append("## §7 应期形态 dev 侧三量登记（承 h16 §1.3 形态口径与 §2.2 dev 登记限；形态口径承 §1.3、份额估计器承 §0.4，分别注明）")
L.append("")
L.append("- D 主标（可照引登记）：合并段 4 例（dev8 段 3 例：LR2-013／LR2-016／LR2-018；LR3 段 1 例：LR3-008）。对上轮构成差登记：上轮 D 主标 3 例，本轮 LR2-018 回到负例清单使 dev8 段 D 主标增至 3 例、合并段 4 例，只登记此构成事实。")
L.append("- 应期三量——D 次标计数、应期形态附记例数、应期缺位计数：dev 侧在本轮许可材料中**未编码**（h16 §2.2 明示 dev 侧无逐例应期缺位专项登记）。本席不代编、不以新鲜侧 §1.3 三量充 dev 数，只登记未编码状态如上。")
L.append("")
L.append("## §8 T1–T4 逐条齐备性评估")
L.append("")
L.append("| 条件 | 本轮材料事实 | 齐备性 |")
L.append("|---|---|---|")
L.append("| T1 新鲜双源在场 | 本轮为 dev 平台复标轮，材料为 dev 负例 24 例；无新鲜验收集材料、无双源在场登记，dev 负例不构成 T1 判定批次 | 未齐备 |")
L.append("| T2 层内主导 | 合并段 W 接口含入 20.8%（5/24；硬核 0%），低于 E 残余 29.2%（7/24）与取用族 A＋C 29.2%（7/24），W 非层内主导 | 未齐备 |")
L.append("| T3 形态集中 | W 接口 5 例分属 W-面 4／W-名 1 两形态，且全为接口含混例、无硬核例，形态集中无硬核支撑 | 未齐备 |")
L.append("| T4 候选可回扣且无等效 | 本轮诊断按产出限只登记计数，无任何候选条文、无回扣、无等效审计 | 未齐备（零候选） |")
L.append("")
L.append("- 结论：T1–T4 非四条齐备，依预注册 §5 不评估解冻；**冻结维持**为缺省结论。六壬零方法项，本件不构成解冻材料、不产生本轮增益宣称。")
L.append("")
L.append("## §9 限度与异常自报")
L.append("")
L.append("- 限度：单一编码链（照引既往标定）、无第二编码者复核；全部分额为描述性读数（负例 n＝24／15／9，份额 SE 约 8–11pp，LR3 段 n＝9＜10 只作描述性读数）；LR3-010 本轮不在负例清单内、其 UNC 标维持且不代编，本件不评估任何 method 条文效力。")
L.append("- 异常自报：本轮打开的材料限于任务清单所列——W-CHARTER 全文、DIAG-LR-fresh-h16（§0.4／§1.3／§2.1／§2.2 照引源）、上轮同型件 DIAG-LR-weight-dev78（体例与轨迹）、本轮负例清单、final-scores、两份 master-baseline、inputs-dev12 逐例 24 卡（仅读 provenance.book 分族登记用）；未打开 holdout 金标与本轮 predictions 单例正文，未打开 runs/round79/judging/ 与 acceptance/ 内任何文件，未对任何 runs/ 目录做列表或计数，未用 /tmp，未用通配删除。脚本为本席在 runs/round79/ 内唯一名新写件 `diagnosis/w42_r79_diag.py` 与 `diagnosis/w42_r79_emit.py`，中间行表为 `diagnosis/w42_r79_rows.json`。")
L.append("- 口径注记：h16 §1.3 实为应期形态专项登记，份额估计器（SE 公式与描述性读数限定）载于其 §0.4；本件两处均逐字承之并分别注明出处（承 R78 诊断席自报口径），不合并混读。")
L.append("")
md = "\n".join(L)
open(os.path.join(D, "DIAG-LR-weight-dev79.md"), "w").write(md)
print("md bytes:", os.path.getsize(os.path.join(D, "DIAG-LR-weight-dev79.md")))
print("json bytes:", os.path.getsize(os.path.join(D, "DIAG-LR-weight-dev79.json")))
print("md tail:", md.splitlines()[-1][:80])
