# 数据角任务原文（Round 1，主持角分发，留档）

你担任 MastersDivination Benchmark Round 1 的：只管统一汇总、去重、划分、封存与清单，不作断、不评分。严格按 ~/workspace/divination/benchmark/PROTOCOL.md（含论文级五角分离修订）与 ~/workspace/divination/masters-dataset/SCHEMA.md 执行。主持角已完成预注册（benchmark/iterations.md 的 Round 1 预注册节）与知识库哈希冻结（benchmark/runs/round1/kb-snapshot/MANIFEST.sha256），你不要改这两处。

## 数据源（ masters-dataset/ 下）
- chinese-divination/inputs.jsonl + answers.jsonl（50 例，已是统一结构，direction/key_assertions/outcome 齐全；system: liuyao36/meihua10/yijing4；famous 标记在 inputs 的 notes.tags：MH-001/002/003/005/006、ZY-001..004）
- chinese-natal/（45 例，旧结构：inputs 有 native/pillars/life_context/master/system，answers 有 master_verdict/reasoning_points/outcome(字符串)）
- western/（15 例，answers 的 master_predictions[0] 只有 master/system/verdict 长文本，无 direction/key_assertions/outcome 独立字段，应验信息含在 verdict 或原书自述里）
- modern-masters/inputs+answers（10 例 C：master_verdict/reasoning_points/outcome 字符串）与 predictions.jsonl（12 条 P：顶层 master/tradition/subject{含 context_at_prediction}/master_predictions[{statement,published_at}]/outcome(字符串)/outcome_verdict/cross_system）
- benchmark/cases/ 种子 6 例（input/*.md、answer/*.md、holdout-answer/*.md）与 masters-dataset/data/dev.jsonl（4 例种子 dev）、holdout/test_gold.jsonl（2 例种子 test）现状

## 去重（已由主持角对账确认，按此执行并记入 manifest）
- 种子 LY-02 ≡ chinese-divination LY-001；MH-01 ≡ MH-001；MH-02 ≡ MH-002；MH-03 ≡ MH-003 —— 重复只计一例，以分卷版为正本，种子版仅记 alias。
- 种子 LY-01（候文书·贲静卦）、LY-03（占官升迁·困之兑）经全文检索在分卷中无同例，作为独立例保留（金标分别在 benchmark/cases/answer/LY-01.md 与 holdout-answer/LY-03.md，你负责转成统一结构）。
- 预期统一池总数 = 50+45+15+10+12+2 = 134 例。若你的对账数不符，停下并在汇报中说明差异，不要自行凑数。

## UID 映射（统一 id，原分卷 id 存入 source_id 字段）
- chinese-divination：保持原 id（LY-001…、MH-001…、ZY-001…）。
- 种子：LY-01、LY-03 保持。
- chinese-natal：八字按文件原序 → BZ-001…BZ-042；紫微 → ZW-001…ZW-003。
- western：按文件原序 → AS-001…AS-015。
- modern C：按各例 tradition，八字 → BZ-101 起顺编，六爻 → LY-101 起顺编。
- modern P：P01→BZ-301、P02→LR-001、P03→BZ-302、P04→BZ-303、P05→AS-301、P06→AS-302、P07→BZ-304、P08→AS-303、P09→AS-304、P10→AS-305、P11→AS-306、P12→AS-307。

## 金标结构化（旧结构卷）
- key_assertions：natal 与 modern C 取 reasoning_points；western 由你从 verdict 原文提炼 1–3 条具体断语（只提炼、不改写关键信息）；modern P 取 statement 中的具体主张（1–3 条）。
- outcome：字符串转 {description, verified_by}（verified_by 据来源填「原书自载」等，western 从 verdict 中应验自述提炼，没有明确应验记载的如实写「原书未另载应验，以断语为准」）。
- direction：主持角在旧口径下草拟的编码如下，你必须逐条对照原文 verdict 复核，复核不一致的以原文为准改掉并在 manifest 的「编码复核更正」节逐条记录（这是数据整理，不是评分）：
  - natal: ren-001 +、ren-002 +、ren-003 +、ren-004 +、ren-005 +、ren-006 −、ren-007 +、ren-008 −、ren-009 −、ren-010 +、ren-011 −、ren-012 +、ren-013 +、ren-014 mixed、ren-015 mixed、ren-016 +、xu-001 +、xu-002 −、xu-003 +、sanming-001 mixed、wei-001 +、wei-002 mixed、wei-003 mixed、wei-004 +、wei-005 +、wei-006 +、wei-007 +、wei-008 +、wei-009 +、wei-010 +、wei-011 +、wei-012 +、wei-013 +、wei-014 −、wei-015 +、wei-016 mixed、wei-017 mixed、wei-018 mixed、wei-019 +、wei-020 +、wei-021 +、wei-022 mixed、ziwei-001 −、ziwei-002 +、ziwei-003 −（+ = positive，− = negative）
  - western（按文件序即 AS-001..015）: +、+、+、−、+、−、+、+、+、+、+、−、mixed、+、mixed
  - modern C（C01..C10）: +、+、+、−、−、−、+、+、−、−（C05 另在 notes.tags 加 retrodiction）
  - modern P（P01..P12，方向=大师预测对对象而言的方向）: −、+、−、−、−、−、+、−、+、+、+、+
- ziwei 3 例 outcome 原笔记未载结局：description 如实写「原笔记未载结局」，并在 notes.comment 注明 outcome 项只能按格局断法对齐评。

## 划分（一次冻结，随机种子 20261029，写明在 manifest）
- 按 tradition 分层约 70/30 抽 dev/test（tradition 分组：liuyao、meihua、yijing、bazi、ziwei、horary、modern-prediction（P 类整体一组）、六爻-modern 已并入 liuyao 组、八字-modern 并入 bazi 组——即按统一 tradition 字段分组，P 类以其 source 卷单独成组以便分项统计，tradition 字段写原体系、notes.tags 加 modern_prediction）。
- 强制指定（覆盖随机）：LY-01→dev、LY-03→test、LY-001→dev、MH-001→dev、MH-002→dev、MH-003→test。
- famous 9 例按比例分两边（MH-003 已强制 test），不得全在一边。

## 产出文件
1. masters-dataset/data/dev.jsonl：dev 全量统一记录（含 master_predictions/outcome，split 字段填 dev）。
2. masters-dataset/data/test_inputs.jsonl：test 的输入面（只含 id/subject/context/provenance 公开部分，无金标）。
3. masters-dataset/holdout/test_gold.jsonl：test 全量金标（替换旧的仅 2 例版本；旧种子金标内容并入对应统一记录）。
4. masters-dataset/splits.json：全部 134 个 uid → dev/test 单一事实源。
5. benchmark/pool-manifest.md：总数、分 tradition counts、dev/test counts、去重日志、uid↔source 映射表、编码复核更正记录、随机种子、ziwei/retrodiction 特别标注。
6. benchmark/runs/round1/inputs/<uid>.json：每个 dev 例一份盲测输入文件，只含 uid、tradition、subject、context（含 attachments）、provenance.book（可含书名，不得含断语/结局）；严禁出现 master_predictions、outcome、direction、key_assertions、分卷 answers 的任何内容。写完后自检：grep 这些文件不得出现「outcome」字段名与各例 outcome 的关键句（抽查即可，方法写进 manifest）。
7. benchmark/runs/round1/test-seal-log.md：一行封存日志（日期、test 例数、封存位置、本轮不打开声明）。

全部 JSONL 写完逐行解析校验 + 用 masters-dataset/schema.json 的必填字段做一次人工抽查（至少每卷抽 2 例）。完成后汇报：总数与分项 counts、dev/test 数、更正过的 direction 编码清单、自检结果。
