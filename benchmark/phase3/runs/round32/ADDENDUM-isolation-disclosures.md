# Round 32 隔离自报补遗（定稿后随席位回盘补齐，照 R31 补遗体例）

说明：REPORT.md 定稿时各盲测席回盘尚未齐，主持误记「未见隔离自报」；回盘齐后实有下列自报，本补遗逐项登记并核算影响，REPORT.md 与 STAGE-SUMMARY-15 已各追加勘误指向本文件。

## 一、元数据级接触（6 席，均为本批预测全部落盘定稿之后、校验脚本通配过宽所致）

| 席 | 接触方式 | 实际所见 | 未接触 |
|---|---|---|---|
| B02 | 校验脚本误用 predictions/*.json 全目录通配（当时目录共 205 份） | 他批文件的 case_id、confidence、systems_used、trigger 四元数据字段 | prediction_text、basis、judging、final-scores、金标、结局 |
| B08 | glob predictions/LY-*.json 打印字段 | 多批文件（LY-001～028、211 起及 3xx/4xx/5xx/6xx）的 case_id、confidence、trigger.reason | prediction_text、basis、判分、结局 |
| B10 | 校验 glob 解析全部 LY-*.json（98 份） | 仅断言顶层键集，未输出/未读取任何字段值 | 一切内容字段 |
| B15 | 通配 predictions/LY-5*.json | 他批（LY-501～516、537～543）的 case_id、confidence、systems_used、trigger 三布尔 | prediction_text、basis 正文、判分、结局 |
| B16 | glob 加载全部 LY-*.json（48 份） | 仅断言字段名集合，未读取/未输出内容 | 一切内容字段 |
| B23 | glob 加载全部 YM-*.json（34 份） | 仅断言顶层字段名与 trigger 字段名集合 | 一切内容字段 |

## 二、仅文件名列表（不构成内容接触，登记备查）

B11、B12、B14、B21、B24、B25 于开工/校验时对 predictions 目录执行过 ls 或文件名计数——所见仅案例 id 文件名，而案例 id 本就在公开的 batches.json 中，未打开任何文件。B18 仅对 round32 目录做过目录名列表（predictions 为空）。

## 三、主持影响核算

- 时序：六席接触均发生于各自批次预测**全部落盘定稿之后**，接触者自身断语不可能被回溯影响；接触均为只读，未改动任何他批文件。
- 内容性质：所见最深为他批的 confidence／systems_used／trigger（含个别 reason 文本）——这些是预测方的自报元数据，不含结局、判分、金标或他批断语正文（prediction_text、basis 全程无人接触）。由 confidence 数值无法反推任何案例的结局或分数。
- 结论：无任何一例预测可能因上述接触被污染，R32 全部读数与平台判读、holdout11 验收结果维持不变。本补遗只补记录、不改任何已定稿数字。
- 教训（登记给下一任）：校验脚本通配过宽是本轮六席同型事故，属派单卫生可改进项——下一任派单应明示「校验只许按本批文件名清单定点读取，禁止对 predictions 目录用通配 glob/ls 全量」。
