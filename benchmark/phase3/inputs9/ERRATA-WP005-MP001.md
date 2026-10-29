# Errata 候选：WP-005、MP-001 结局文本（outcome_record）尾注矛盾

- 性质：**候选建议，未落盘修改**。本文件由 phase3 数据角（C 轨）于 2026-10-30 提出；roster 任何文件未改、历轮分数未动。
- 缘起：phase3 runs/round26/REPORT.md 第 56 行——「WP-005、MP-001 两例 outcome_record 尾注与其所载事件/数字自相矛盾；两席评审均以事件与数字为准计分并在 reason 注明。列为 roster 结局文本 errata 候选，待数据角核原书后以 errata 形式处理，历轮分数不回改。」

---

## 一、WP-005

### 所在文件
- `benchmark/phase3/roster7-additions.jsonl` 第 15 行（id = WP-005）。
- 同文另见金标源：`benchmark/phase3/expansion6/modern-west/cases.jsonl` 第 5 行 outcome.description（roster 条即由此压缩而来）。

### outcome_record 原文（roster 全文）
> "Donald Trump won the 2016 election in the Electoral College and became president. The prediction failed."

### 尾注原文摘录
> "The prediction failed."

### 矛盾描述
- 同条前半所载事件明确无误：特朗普赢得 2016 年大选（选举人团）并成为总统——此为公开选举记录，本地来源（cases.jsonl 同条 outcome.source 作 "Official US election results / universal public record"）与常识一致，无误。
- 尾注 "The prediction failed"（该预测落空）**在 roster 条内没有指称对象**：该条不载任何预测文本，读者（及按 roster 计分的评审席）无从知道「该预测」指谁。按条内唯一可读的语境——紧随「特朗普获胜」之后——尾注只能被读作对「特朗普获胜」这一事件命题的否定，与前半事件直接冲突。
- 尾注的真实出处与原意：cases.jsonl 同条 master_predictions 载明，大师 Aleksandar Imsiragic 在 ISAR 座谈上的表态是「Trump 前景不妙」（即克林顿将胜）；尾注本是对**大师该预测**的判语，随 outcome.description 压缩进 roster 时丢失了指称对象，于是与同条事件形成表面自相矛盾。
- R26 两席评审的处理（已按事件计分，分数不回改）：
  - 评审 A（judgeA-packetA1.jsonl，anon P3-3c5c45eb）：「特朗普胜选合（结局注文案与事件矛盾，以胜选事件为准）；11月8日合」
  - 评审 B（judgeB-packetA1.jsonl，同 anon）：「本预测断特朗普胜与实际胜合」（即按我方预测与事件相合计分，未采尾注）

### 建议更正文本（仅建议）
将尾注改为带指称对象的表述，二选一：
- （a）删尾注，全文作："Donald Trump won the 2016 election in the Electoral College and became president."
- （b）保留判语但明示对象："Donald Trump won the 2016 election in the Electoral College and became president. The ISAR panel's favoured outcome — a Clinton win, per Imsiragic's on-record statement that Trump's outlook was 'gloom' — did not occur."

### 证据来源
- `benchmark/phase3/expansion6/modern-west/cases.jsonl` 第 5 行：master_predictions（Imsiragic 原话节录 "It doesn't bode well for Donald Trump" 及 key_assertions）、outcome、grade_note（方向编码约定说明）。
- `benchmark/phase3/expansion6/modern-west/BUILD-REPORT.md` 第 18 行：同例摘要（「Trump 前景不妙」／Trump 胜（落空））。
- R26 评审 reason：`benchmark/phase3/runs/round26/judging/judgeA-packetA1.jsonl`、`judgeB-packetA1.jsonl`（anon_id P3-3c5c45eb）；`benchmark/phase3/runs/round26/REPORT.md` 第 56 行。

---

## 二、MP-001

### 所在文件
- `benchmark/phase3/roster8-additions.jsonl` 第 1 行（id = MP-001）。
- 同文另见金标源：`benchmark/phase3/holdout8/test_gold.jsonl` 第 1 行 outcome.description。

### outcome_record 原文（roster 全文）
> "蔡英文以817万票大胜韩国瑜552万票，差距约265万票连任；立委选举民进党单独取得61席过半，国民党38席。三项断言全反"

### 尾注原文摘录
> "三项断言全反"

### 矛盾描述
- 同条所载事件/数字经核实**全部准确**：蔡英文 8,170,231 票（约 817 万）、韩国瑜 5,522,119 票（约 552 万）、票差 2,648,112（约 265 万）；立委民进党 61 席、国民党 38 席。核证：金标源同条 outcome.source 引中选会公布结果与自由时报选后盘点；另经公开记录复核（2020 年台湾大选公开结果：蔡 57.13%、韩 38.61%、票差约 264.8 万，立委民进党 61 席、国民党 38 席）一致。
- 尾注「三项断言全反」在 roster 条内同样**没有指称对象**：该条只载结局事件与数字，不载任何「断言」。R26 中被计分的我方预测恰与该条数字相合（评审语：「与票差约250万、约60对40以下三断皆合」——我方三项断言皆合），尾注的「全反」与我方三断、与同条数字三者互相冲突，按 roster 字面读即自相矛盾。
- 尾注的真实出处与原意：金标源同条 master_predictions 载明大师詹惟中三项断言为——①韩国瑜当选 2020 总统；②韩胜蔡 30 万至 60 万票；③国民党立委获胜、民进党立委不过半。三项与结局逐项相反，「全反」本是对**大师三项断言**的判语；压缩进 roster 时丢失指称对象，遂成本条矛盾。
- R26 两席评审的处理（已按数字计分，分数不回改）：
  - 评审 A（judgeA-packetB2.jsonl，anon P3-e4eedf3e）：「按结局数字核：蔡817万胜韩552万差265万、立委61对38席，与票差约250万、约60对40以下三断皆合；结局无可核时点」
  - 评审 B（judgeB-packetB2.jsonl，同 anon）：「蔡胜265万票差民进党61席国民党38席全合；结局无可核时点」

### 建议更正文本（仅建议）
将尾注改为带指称对象的表述：
> "蔡英文以817万票大胜韩国瑜552万票，差距约265万票连任；立委选举民进党单独取得61席过半，国民党38席。（大师詹惟中三项断言——韩国瑜当选、韩胜蔡30万至60万票、国民党立委获胜且民进党不过半——全反。）"

或径删尾注「三项断言全反」四字，判语留待金标源条内。

### 证据来源
- `benchmark/phase3/holdout8/test_gold.jsonl` 第 1 行：master_predictions.key_assertions（三项断言原文）、outcome（含中选会/自由时报出处链接）。
- 公开选举记录复核（2026-10-30 数据角查证）：2020 年台湾总统选举蔡英文 8,170,231 票、韩国瑜 5,522,119 票；立委民进党 61 席、国民党 38 席，与 roster 数字一致。
- R26 评审 reason：`benchmark/phase3/runs/round26/judging/judgeA-packetB2.jsonl`、`judgeB-packetB2.jsonl`（anon_id P3-e4eedf3e）；`benchmark/phase3/runs/round26/REPORT.md` 第 56 行。

---

## 三、共性机理与处置建议（供主持角）

1. 两例同型：金标源 outcome.description 末句本是**对大师预测的判语**，其指称对象（大师断言）只存在于同条 master_predictions 字段；roster 的 outcome_record 只摘 outcome 一字段单独流通，判语遂失去对象，与同条事件/数字、与被计分的我方预测形成矛盾。
2. 建议处置（任一）：(a) 按上列建议文本修正 roster7-additions / roster8-additions 两行尾注（并同步金标源 outcome.description 的表述习惯）；(b) 立一条 roster 编纂规矩：outcome_record 只载事件与数字，成败判语必须自带指称对象（如「大师断言全反」）。
3. 本候选不要求回改任何历轮分数：R26 两席已按事件/数字计分并在 reason 中注明，REPORT.md 亦已定「历轮分数不回改」。
