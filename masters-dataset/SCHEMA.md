# SCHEMA — MastersDivination Benchmark 数据规范（四个收集 agent 对齐用）

版本：v0.1（2026-10-29）。机器可读版：同目录 `schema.json`（JSON Schema draft 2020-12）。

## 核心结构（每例一条 JSON，JSONL 一行一条）
必填主结构只有两样：**被算对象 + 当时背景** 与 **大师们的预测**。各体系特有的盘面/卦象一律降为可选附件字段，不得作为必填。

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | string | 稳定编号，前缀区分卷：`LY-` 六爻、`MH-` 梅花、`ZY-` 周易文本占、`BZ-` 八字、`ZW-` 紫微、`TR-` 塔罗、`AS-` 占星、`RN-` 卢恩、`NM-` 数字命理、`QM-` 奇门、`LR-` 六壬。编号一经发布不得复用/更改 |
| `subject` | object | 被算对象基本信息：`name_or_desc`（可匿名化描述）、`birth`（可选：date/time/place，命盘类才有）、`gender`（可选） |
| `context` | object | 当时背景：`question`（所问之事原文）、`asked_at`（占时，含干支或公历）、`setting`（场景/外应等当时可知信息）、`attachments`（可选：卦象/牌面/盘面等体系特有数据，自由结构） |
| `master_predictions` | array | 每位大师一条：`master`（姓名）、`tradition`（体系）、`date`（占断/发表时间，可注「不详」）、`statement_excerpt`（预测原文节录，不得改写关键信息）、`source`（出处指针）、`direction`（结构化方向：`positive`/`negative`/`mixed`/`neutral`，供自动评分）、`key_assertions`（关键具体断语列表：对象/时间/部位级） |
| `outcome` | object | `description`（实际应验）、`verified_by`（应验的记录来源，如书中自述/史载） |
| `provenance` | object | `book`、`edition`、`url`（可空）、`page`（卷/页/章） |
| `license_status` | string | 如 `public-domain`、`cc-by-sa-4.0`、`copyrighted-excerpt-only`、`unknown` |
| `redistributable` | bool | 保守口径：公版与自有整理可 true；现代版权作品只许元数据+短节录，拿不准一律 false 并在 notes 注明 |
| `split` | enum | `dev`（校准集，答案开放）或 `test`（留出集，答案封存）；**由基准统一划分（约七三），收集 agent 不得自行指定 test 的答案去向** |
| `language` | string | 原文语言，如 `zh-Hant`、`en` |
| `notes` | object | `tags`：可含 `cross_system`（多体系同断）、`famous`（名例，污染风险高）、`disputed`（源流/归属存疑，如托名）、`excerpted`（有节录）等；`comment` 自由备注 |

## 存放与封存
- `data/dev.jsonl`：dev 全量（含 master_predictions 与 outcome，开放）。
- `data/test_inputs.jsonl`：test 的输入面（只含 id/subject/context/provenance 的公开部分），**不含** master_predictions.statement_excerpt 与 outcome。
- `holdout/test_gold.jsonl`：test 的完整金标，**封存**：只在阶段验收时由评测方开封跑一次；收集 agent 只写不读回给盲测方。
- 划分清单：`splits.json`（id → split 的单一事实源，与各行 split 字段冲突时以 splits.json 为准并回改数据）。

## 收集纪律
1. 只收真实可核的大师成例：出处到书名卷次；原文节录不改写关键信息，节录注明。
2. 宁少而真：找不到合格成例的体系留空并登记，不凑数、不编造。
3. 现代建构/伪托照收（大师实际奉行即可），但 notes.tags 标 `disputed` 并在 comment 写明真伪情况。
4. 每条必须有 license_status 与 redistributable；版权作品只存元数据+短节录+出处指针。

## 内部版与公开发布版（2026-10-29 用户口径，最高优先）
- **现阶段为内部使用：内部版 = 全量。** 收录、split 划分、评分与 `redistributable` 完全无关；现代版权内容全量进内部测试集，不因版权或可否再分发而剔除、降级或限制使用范围（内部）。
- `redistributable` 只决定将来**公开发布版**导出时的过滤：发布导出 = 仅 redistributable=true 的条目 + 版权条目的「元数据+短节录+出处指针」形态。内部全量版与公开过滤版是同一数据集的两种导出，不是两个数据集。
- `license_status` 仍须逐条如实填写（为将来过滤与合规留据），但不影响内部任何环节。

## 分卷旧结构映射（已按 inputs/answers 写的分卷不推倒，按此映射进统一核心）
| 分卷字段 | 统一核心字段 |
|---|---|
| subject.name / subject.basic_info | subject.name_or_desc（basic_info 并入 context 或 subject 的扩展键保留） |
| subject.context_at_prediction | context.setting |
| casting / 盘面对象 | context.attachments |
| master_verdict / master_predictions[].statement | master_predictions[].statement_excerpt |
| reasoning_points | master_predictions[].key_assertions 的参考（整理者据此编码，原文断语优先） |
| 应验字段（outcome/verification 等） | outcome.description / outcome.verified_by |
分卷目录（chinese-natal/、western/、modern-masters/）为收集层；基准层（data/、holdout/、splits.json）由 benchmark 统一划分与登记。modern-masters 的 predictions（公开预测类）与 inputs/answers（占例类）全部进入候选池参与 dev/test 划分。
