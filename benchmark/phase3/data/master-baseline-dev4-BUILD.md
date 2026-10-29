# master-baseline-dev4 建构记录（评审侧基线建构角）

## 任务与产物
- 为 splits4.json 的 `dev_add_new` 59 例（LY-322…LY-458，六爻）建立大师基线（轴二＝实际应验口径），与 dev3 基线 141 例合并为 `master-baseline-dev4.json`，共 **200 例**。
- dev3 的 141 例条目原样并入，未改动任何既有分数；新 59 例条目结构与 dev3 后段条目一致：`{direction, claims, timing, total, src}`，`src` 为 `meanAB`（非分歧取双评均值）或 `arbitration`（分歧例取仲裁分）。
- 本任务只评大师断语，未打开任何 `runs/round*/predictions` 或 `final-scores`。

## 口径（沿用 dev3 基线建构流程）
- 输入格式、匿名包字段、评审输出字段、分歧定义均照 dev3 基线一组文件（`master-baseline-newdev-packet.json`、`baseline-judgeA/B.jsonl`、`baseline-arbitration.jsonl`、`baseline-arbitration-packet.json`）的实际结构执行。
- 量表：direction / claims / timing 各 0–2（0.5 步进），total＝三项和，pass＝total≥4。
- direction：2＝与实际结局同向同级；1＝同向不同级或含糊；0＝反向或未下结论。
- claims：2＝具体断语被结局证实；1（及 1.5）＝部分证实或错位；0＝被证伪或只有空泛吉凶。
- timing：2＝所给应期与实际时点对齐；1＝部分对齐；0＝明确给出且不对齐。
- 分歧定义（与主持角既有筛查脚本同口径）：claims+timing 两项之和双评相差 ≥2，或 pass 判定不一致 → 第三方仲裁定分；其余取双评均值。

### 本任务书对 timing 的两点细化（与双轴补评 judge-role 的「一律中性记 1」不同，按任务书执行）
1. 结局无可核时点（而断语有时点尺度可参）→ timing 记 1，notes 注明「无时点可核（中性记 1）」。
2. 断语本身无任何应期信息 → timing 记 0，notes 注明「断语无应期」。
- 新 59 例最终 timing＝0 共 21 例，其中绝大多数属此类（六爻短断语只断吉凶成败、不给应期者甚多）；这是新例 timing 均分偏低的主因，引用时须知此口径。

## 匿名包构成
- 每例一条：`prediction_text`＝大师断语（`statement_excerpt` 原文＋`key_assertions` 以「」拼接）；`outcome_record`＝`outcome.description` 原文。源文件：`benchmark/phase3/expansion2/dev-add-answers.jsonl`（59 例与 dev_add_new 名单恰合，无缺漏、无多预测条目）。
- anon id：`MB-`＋`sha256('dev4-master-base:'+case_id)` 十六进制前 8 位。
- 映射与全部评审原始文件只留本建构目录 `benchmark/phase3/data/dev4-baseline-build/`：`packet.json`、`mapping.json`、`judgeA.jsonl`（含 `judgeA.sha256`）、`judgeB.jsonl`（含 `judgeB.sha256`）、`arbitration-packet.json`、`arbitration.jsonl`。

## 执行方式（独立性说明，如实记录）
- 建包、评审 A、评审 B、仲裁由同一执行角在**分开的顺序步骤**中完成：先建包；评审 A 只读匿名包逐条打分，落盘后即以 SHA-256 封存（`0cf783ee…`）；评审 B 重新只读匿名包独立打分、全程未查阅 A 的分数，落盘封存（`5135b1b0…`）；分歧由机械脚本按上列定义筛出后，仲裁步骤才首次同时见到双评分数与理由并逐例裁定。两份初评之间无互相迁就的通道；分歧的产生与分布（见下）可作旁证。

## 双评与仲裁统计（新 59 例）
- 评审 A：均分 4.847，pass 44/59。评审 B：均分 5.051，pass 52/59。
- 分歧 **8 例**，全部为 pass 判定不一致（claims+timing 差 ≥2 者 0 例），已全部仲裁：MB-36d244ff、MB-45ab6132、MB-999e26ea、MB-9b73f1a6、MB-da554fe8、MB-dabfa02a、MB-f9a59d81、MB-fe3de0a4。
- 分歧焦点集中在一处口径读法：断语只有一句针对所问的结论性断语且被结局全幅证实时，claims 记 2（B）还是因其简短记 1.5（A）。仲裁原则：量表 claims 2 的定义是「具体断语被证实」，简短不等于部分证实——单断全中记 2（7 例采此）；唯 MB-45ab6132 的断语只有凶级（「大凶之兆」）而无具体内容，维持 1.5、该例最终不通过。MB-36d244ff 另涉「立凶危」的即时性读法，仲裁 timing 记 1、claims 记 1.5，合计 4.5 通过。
- 最终构成：meanAB 51 例、arbitration 8 例。

## 新 59 例大师基线（最终分）
- **total 均分 4.975 / 6**；direction 均分 **1.932**；claims 均分 **1.835**；timing 均分 **1.208**。
- **pass 51 / 59**（total≥4）。
- 不通过 8 例（case_id / total）：LY-428 / 1.25（断语未下结论）、LY-333 / 1.75（断今日不死而本日死）、LY-429 / 2.25（愈后复发而死）、LY-424 / 2.75、LY-411 / 3.25（升迁应期错位）、LY-452 / 3.25、LY-457 / 3.25、LY-402 / 3.5（仲裁定分）。完整逐条分数以 `master-baseline-dev4.json` 为准。

## 口径疑难（如实记录，供主持角知悉）
1. **MB-96b6484b**：源数据 `statement_excerpt` 本身含「世辰年占卦，在午年子月而死」一类与结局同文的句子，断语与应验在源头即同句；本轮仍按包面文字评分（timing 全合），未擅自剔除。此例分数宜谨慎引用。
2. **MB-9529b8f1**：断语摘录只陈述卦象并质疑旧法、无明确吉凶结论（疑似摘录截断），双评 direction 均低（A 0 / B 1，均值 0.5），最终 total 1.25 为全组最低；属源数据形态问题，非大师断错可比。
3. **MB-938269da**：结局「果俗底伙计有事而止」之「俗底」时点含义不明，双评均按「结局无明确时点可核（中性记 1）」处理。
4. 若干例的 key_assertions 括号内含数据角的应验按语（如「实际本日午时死」），属源文件既有形态，与 dev-new-answers 第一轮同构，本轮照原样入包、评分只据断语本体与结局原文，未据按语加分。
