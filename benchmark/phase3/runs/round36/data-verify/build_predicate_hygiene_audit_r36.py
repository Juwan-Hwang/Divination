#!/usr/bin/env python3
"""R36 data-verify task1 generator: build PREDICATE-HYGIENE-AUDIT.md.

Classification below is the data-role manual adjudication (each hit read
in full against its outcome text; see audit header for criteria).
Excerpts are pulled mechanically from the R35 manifest (tail of the
outcome string) so no excerpt is hand-transcribed.
Reads: scan_predicate_hygiene_r36_hits.json + R35 outcome-manifest.json.
Writes: PREDICATE-HYGIENE-AUDIT.md in this directory. Modifies nothing else.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE.parent.parent / "round35" / "judging" / "outcome-manifest.json"

A_VERDICT = ["AS-002","AS-015","AS-204","AS-211","AS-302","AS-305","BQ-001",
 "BZ-021","BZ-022","BZ-023","BZ-024","BZ-026","BZ-028","BZ-031","BZ-032",
 "BZ-033","BZ-034","BZ-037","BZ-038","BZ-039","BZ-040","BZ-104","BZ-302",
 "BZ-303","LR2-016","LR2-019","LR2-020","LR3-002","LR3-010","LR3-101",
 "LR3-104","LR3-110","LR3-114","LR3-116","OC-001","OC-004","OC-006","OC-007",
 "OC-008","OC-010","OC-012","OC-013","OC-015","OC-016","OC-017","OC-018",
 "OC-019","OC-020","OC-021","OC-022","OC-023","OC-025"]
A_META = ["LR2-013","LR2-014","LR2-015","LR2-017","LR2-018","LR2-021","LR2-022",
 "LR2-023","LR2-024","LR3-004","LR3-006","LR3-008","LR3-107","MH-001",
 "OC-024","OC-026","OC-027","OC-028","OC-029","OC-030"]
B_NOTE = ["AS-001","AS-003","AS-004","AS-005","AS-007","AS-008","AS-009","AS-010",
 "AS-011","AS-012","AS-013","AS-014","AS-206","BZ-020","BZ-027","BZ-035",
 "BZ-036","BZ-041","BZ-042","BZ-105","DT-004","LR3-112","LY-102"]
C_CLEAR = ["AS-205","AS-215","AS-304","BQ-013","BQ-017","BQ-019","DT-005","DT-006",
 "LY-035","LY-103","LY-212","LY-220","LY-237","LY-250","LY-254","LY-259","LY-413",
 "LY-425","LY-457","LY-512","LY-524","LY-613","LY-618","LY-629","MH-007","MH-009",
 "MP-010","YY-022","YY-023"]

NOTES = {
 "OC-023": "锚例：尾段兼 (a)(b) 两型——「与断语逐项相合」＋「应验段在原文中独立成句……与断语可分离」",
 "OC-014": "锚例对照：现行 manifest 中该例尾句已由 overlay 16 条版剥离（仅余事件句），本轮扫描不再命中——同型处置已生效例，不计入现行计数",
 "OC-006": "与 §6② 回源对象重合：尾句即 cases.jsonl 原 outcome 描述自带判语，基线低分另有裁决（见 VERDICTS.md）",
 "LR3-112": "现行文本为 overlay 16 条版；残留为覆盖注记（细项未逐项复核／病断原文未载后续），非相合裁决",
 "AS-004": "整条为抽例者来源核验注记（「Marked as externally verified, not Lilly-stated」），事件仅居其间",
 "BZ-105": "尾句为抽例者「按：」方法注记（回溯断验、须分开统计），非事件叙述",
 "BZ-042": "尾句含给盲测比对的操作指示（「以格局大富一项为主」），属注记型",
 "LR2-016": "兼 B 型成分：尾含「评分时该细项请按未完全复核处理」的评分指示",
 "LR2-020": "兼 B 型成分：尾含「评分请按未复核处理」的评分指示",
 "LR3-110": "兼 B 型成分：括号内未复核／评分处理注记",
 "LR3-114": "兼 B 型成分：尾句「应期与人数两项按部分合处理」为抽例者评分处理注记",
 "LR3-116": "兼 B 型成分：括号内异文注记（牛黄／石黄）",
 "OC-022": "兼 B 型成分：尾「本例不取卒年断言」为抽例者取舍注记",
 "BZ-037": "兼 B 型成分：括号内已知偏差点注记（「本数据集如实标为已知偏差点」）",
 "BZ-021": "兼 B 型成分：括号内已知偏差点＋「盲测比对时须注明」指示",
 "LY-102": "括号尾为抽例者评价（「本卷可证伪性最强的占例之一」），非相合裁决，入 B",
}

def excerpt(text, limit=160):
    text = text.replace("|", "｜").replace("\n", " ")
    if len(text) <= limit:
        return text
    return text[:80] + " … " + text[-75:]

def table(ids, cases):
    rows = []
    for cid in ids:
        note = NOTES.get(cid, "")
        rows.append(f"| {cid} | {excerpt(cases[cid])} | {note} |")
    return "\n".join(rows)

def main():
    cases = json.loads(MANIFEST.read_text(encoding="utf-8"))["cases"]
    hits = json.loads((HERE / "scan_predicate_hygiene_r36_hits.json").read_text(encoding="utf-8"))
    all_classified = A_VERDICT + A_META + B_NOTE + C_CLEAR
    assert sorted(all_classified) == sorted(hits["hits"].keys()), (
        set(all_classified) ^ set(hits["hits"].keys()))
    assert len(all_classified) == len(set(all_classified)) == 124
    md = f"""# R36 判语卫生审计（PREREG §6①）：R35 结局清单 OC-023 型污染全量审计

- 性质：**数据角审计登记**（不作断、不评分、不改建包底本）。依据 `benchmark/phase3/runs/round36/PREREG.md` §6①。
- 审计对象：`benchmark/phase3/runs/round35/judging/outcome-manifest.json` 全部 **487 例**结局文本（`cases.<id>` 字符串，即 R35 评审建包所用现行结局清单）。
- 已知锚例：OC-023（尾段「与断语逐项相合」＋「应验段在原文中独立成句……与断语可分离」，见 `runs/round35/data-verify/VERDICTS.md` 第十六节）、OC-014（同型，见 `expansion12/pending-verify/VERDICTS.md` 第五节）。**OC-014 在现行 manifest 中尾句已被 overlay 16 条版剥离、仅余事件句，本轮扫描不再命中**，属同型处置已生效例，不计入现行计数；OC-023 仍带尾段，计入 A 类。
- 方法：标记模式全量扫描（脚本 `scan_predicate_hygiene_r36.py`，九组模式：相合裁决／断语指称／文本元注记／断曰类自指／英文裁决框架／部分相合／原书指称／对应／残余人工发现短语；命中原始文件 `scan_predicate_hygiene_r36_hits.json`）＋未命中例中抽例撰写型族群（OC/MP/BZ/AS/WP/ZY/DT/MH/BQ/YY2/LR/LR3 残余例）全读复核。候选共 **124 例**，逐一回读结局全文定性；其余 363 例无任何标记命中且非抽例撰写型文本（原书转录结局），未逐例定性，此限度如实登记。
- 出处字段口径：manifest 的 `cases` 为纯字符串、无逐例出处字段；每例出处即该文件 `cases.<id>` 本身，下表「原文摘录」为脚本自 manifest 机械截取（短例全文、长例首 80 字＋尾 75 字），非手抄；判语所在位置（尾段／首段框架／句中）以逐例回读定性为准。

## 定性口径（写死于本审计）

- **A 类·严格同型（OC-023 型）**：结局文本尾段（或收束段）混入**抽例者撰写的非事件句**，二子型：(a) **相合度裁决句**——对大师断语与结局是否相合下判语（相合／逐项对应／仅部分相合／不合／被证伪／按部分合处理等），指称对象（大师断语）不在结局文本内；(b) **应验段出处／可分离元注记**——注记应验文字在原书中的位置或可分离性（「均载原文应验段」「应验段独立载于原文」等）。两子型均为评审读面上的判语污染：评审只见结局时，该句或替评审预判相合度、或与计分无关。
- **B 类·邻类注记型（同处置建议、另行计数）**：抽例者注记混入结局文本，但非相合裁决——来源核验注记、覆盖／未复核注记、评分处理指示、「按：」方法注记、英文「Confirmed in the text:」类确认框架前缀等。
- **C 类·非同型（命中但排除）**：标记词出自**原书本文自身**——原书结局句自带的「果然／果驗／已而果然」短承、原书叙事内的「予曰」对话、原书自载的徵驗／应验解释句、作者（Lilly）自述的 postscript 引文等；此类文字是原书结局的组成部分，不是抽例判语。另 MP-010 为「独立参选」政党政治术语的假阳性。

## 计数汇总

| 类别 | 计数 | 说明 |
|---|---|---|
| A(a) 相合度裁决句型 | **52** | 见 §一 |
| A(b) 应验段出处／可分离元注记型 | **20** | 见 §二 |
| **A 类合计（严格同型）** | **72** | 占 487 例的 14.8% |
| B 类·邻类注记型 | **23** | 见 §三；另有 8 例 A 类例兼含 B 型成分，已在逐例注记标明、不重复计数 |
| C 类·非同型（扫描命中后排除） | 29 | 见 §四 |
| 候选合计 | 124 | ＝扫描命中 124 例（A72＋B23＋C29） |

同型构成观察（只登记）：A 类高度集中于抽例撰写型族群——OC 族 24/30 例、BZ 族 17/31 例、LR2/LR3 族 23/24 例、AS 族 6 例；原书转录型族群（LY/YM/YY 等）结局尾句无一例 A 类。OC-023 所在的 OC 族为重灾区（30 例中 24 例 A 类、另 OC-014 已剥离）。

## 一、A(a) 相合度裁决句型（52 例）

| id | 原文摘录（manifest `cases.<id>`，尾段） | 注记 |
|---|---|---|
{table(A_VERDICT, cases)}

## 二、A(b) 应验段出处／可分离元注记型（20 例）

| id | 原文摘录（manifest `cases.<id>`，尾段） | 注记 |
|---|---|---|
{table(A_META, cases)}

## 三、B 类·邻类注记型（23 例）

| id | 原文摘录（manifest `cases.<id>`，尾段；AS 前缀型摘录含首段者以全文短例为准） | 注记 |
|---|---|---|
{table(B_NOTE, cases)}

## 四、C 类·非同型（29 例，扫描命中后逐例排除）

| id | 原文摘录（manifest `cases.<id>`，尾段） | 注记 |
|---|---|---|
{table(C_CLEAR, cases)}

排除理由总述：LY/YM/DT/BQ/MH诸例的「果／果然／果驗」为原书结局句原文短承（如 LY-413「果然如是。」、YY-022「后果然。」整条即原书结局）；LY-212/220/250/254/259/524/629 的「予曰／彼曰」在原书叙事段内、属事件经过；LY-237/512/613/618 的理据／徵驗句为原书本文自带（非抽例者笔）；AS-205/215 的 proved/true 出自 Lilly 自述引文；AS-304 的「公开承认错误」是占者本人选后行为、属事件；BQ-013/017/019 为原书结局句的现代转述、裁决语出原书；MP-010 为术语假阳性。

## 五、口径注记（照 PREREG §6① 写死）

1. **本轮只审计登记，不改建包底本**：R36 建包仍以 R35 manifest 为底（保与 R35 可比），上表 A/B 类尾句在本轮 manifest 副本中原样保留；剥离修正留下一输入／清单卫生轮执行，届时建议口径：A(a) 裁决句整句剥离、A(b) 元注记整句剥离、B 类注记移出结局文本（评分指示与覆盖注记可移入建包侧元数据），事件句一字不动。
2. **既有各轮分数一概不回改**：本审计不构成任何一轮重评理由；A 类尾句对既往评审的实际影响未作量化（不在本项口径内），只登记存在性与分布。
3. holdout 侧同型防范已由 PREREG §6①(2) 另行写死（holdout14 金标建包逐例核 outcome、判语尾句剥离至 `extractor_verdict_tail` 并登记 BUILD-LOG），与本 dev 侧审计互不替代。
4. 锚例复核：OC-023 尾段两子型俱全、仍在现行清单（A 类）；OC-014 已剥离、不再命中。两锚与本审计定性口径一致，口径无外溢修正。
"""
    (HERE / "PREDICATE-HYGIENE-AUDIT.md").write_text(md, encoding="utf-8")
    print("written", len(md))

if __name__ == "__main__":
    main()
