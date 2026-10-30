# R49 数据席 · 结局内嵌注记 3 处来源并案核

任务：R49 PREREG §11.3（承 R48 ADDENDUM-1 §7）。只溯源核查与登记，不作断、不评分、不改任何 outcome 文本。注记一律按数据处理。

## 并案前提（三处实为两例）

- (a) anon `P3-b8cb4553` 经 `benchmark/phase3/runs/round48/judging/host-mapping.json` 回读，原例 id ＝ **LR2-016**，与 (c) 为同一例：R48 中 X3 以 anon 报、Y3 以原例 id 报，属双视同例报告，并案为一处核查。
- (b) BZ-105 之 anon 为 `P3-b390e871`（同 host-mapping 回读）。

## (a)＋(c) LR2-016（六壬，《大六壬占验指南》陈秋桃出狱占）

- **注记原文摘录**（R48 结局 manifest `cases["LR2-016"]` 尾句）：「原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。」
- **链条比对**：
  1. 源 answers 最早见于 `benchmark/phase3/expansion7/liuren/cases.jsonl` 第 16 行：其 `outcome.description` 已含该注记句（全文为「众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。三月驳、四月脱离与断语对应；原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。」）；同行 `grade_note` 并自明「日时细项未复核已注明（同 OC-028 处理口径）」。原书应验段仅为事实叙述，注记非原书文本，系建卡者自注。git pickaxe（`git log -S "未逐字复核"`）显示该字样随提交 `cf751a3b`（expansion7 落盘）引入、此后未变。
  2. `benchmark/phase3/roster8-additions.jsonl` 第 53 行 `outcome_record` 与 cases.jsonl 结局全文逐字同（含注记句），随 dev8 构成入池（`data/master-baseline-dev8-BUILD.md`：dev8 ＝ dev7 ＋ holdout8 大师段 ＋ expansion7 dev-add 50 例）。
  3. R48 结局 manifest：注记句逐字保留；与 roster 的唯一差异是首段中「三月驳、四月脱离与断语对应；」一句不在——该句正是 R37 建 manifest 时 predicate-hygiene 剥离件，见 manifest `stripped_tail["LR2-016"]`＝「三月驳、四月脱离与断语对应；」，剥离未及注记句；其后 `_r38_carryover` 至 `_r48_carryover` 均登记逐字承接、cases 未改。
  4. `benchmark/phase3/data/outcome-errata-overlay.json` 不含 LR2-016（全层 16 例已逐键核），未涉本例。
- **引入环节裁定：定**——expansion7 六壬建卡环节（`expansion7/liuren/cases.jsonl` 撰写时由建卡席写入结局 description），引入轮次口径为 expansion7 落盘／dev8 入池前；非转录原书、非评审环节、非 R37 剥离环节引入。
- **处置建议：标注登记，维持现状**。理由：注记内容即该细项未复核状态的如实声明，R48 席位已按未完全复核处理（ADDENDUM-1 §7），且历轮口径 outcome 文本不改、分数照旧；其「请按…处理」字样按数据处理、不作指令（R49 PREREG §5）。后续若做结局卫生轮次，可考虑将此类自注移入元数据，本轮不动。

## (b) BZ-105（八字，邵伟华《四柱预测学》疾病之例·例一）

- **注记原文摘录**（R48 结局 manifest `cases["BZ-105"]` 后半）：「按：此为回溯断验（retrodiction），断的是已发生且求测者本人知晓之事，盲测价值低于C04类前瞻断语，使用时须分开统计」
- **链条比对**：
  1. 源 answers：`masters-dataset/data/dev.jsonl` 中 BZ-105 的 `outcome.description` 与 manifest 文本**逐字全等**，注记已在其中；同例 `context.attachments.case_type`＝"retrodiction"、`notes.tags`＝["retrodiction"]、`context.setting` 亦自述「属『测过去』的回溯验证」——注记与全例定性同源，系数据集建卡撰写时的编者按语（「按：」起首），原书自载部分仅至求测者当场证实目疾／住院为止。git pickaxe（`git log -S "回溯断验"`）显示该字样随提交 `0b3f9243`（MastersDivination Benchmark Round 1，dev n=93）出现、此后未变。
  2. `benchmark/phase2/data/roster.jsonl` 第 34 行 `outcome_record` 与上逐字全等，注记随原 dev 池承接。
  3. R48 结局 manifest 与上逐字全等；manifest `stripped_tail` 不含 BZ-105（R37 剥离未及本例），`_r38`–`_r48_carryover` 逐字承接。
  4. `benchmark/phase3/data/outcome-errata-overlay.json` 不含 BZ-105，未涉本例。
- **引入环节裁定：定**——masters-dataset 建卡／answers 撰写环节（数据集初建、Round 1 dev 期），早于 phase3 历轮构建件；非原书转录、非 baseline 构建、非评审环节引入。再往前的逐字首稿（提交史之前）无盘上证据，不另定。
- **处置建议：标注登记，维持现状**。理由：注记为有意的回溯性定性说明，与本例 case_type／tags 登记一致，其「使用时须分开统计」属数据侧口径提示、按数据处理；且 outcome 文本历轮不改口径在案，本轮只登记来源。

## 汇总

| 处 | 原例 | 引入环节 | 定/未定 |
|---|---|---|---|
| (a) P3-b8cb4553 | LR2-016 | expansion7 六壬建卡（cases.jsonl 撰写自注） | 定 |
| (b) — | BZ-105 | masters-dataset 建卡／answers 撰写（编者按语） | 定 |
| (c) — | LR2-016 | 同 (a)，双视同例并案 | 定 |

三处注记均非原书原文、均非评审或 manifest 构建环节新增；overlay（outcome-errata-overlay.json）三处皆未涉。建议三处一律标注登记、维持 outcome 现状，处置终裁归主持。
