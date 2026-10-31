# PREREG-ADDENDUM-r89 — R89 预注册增补（holdout33 构成写定）

## 勘误登记（先于正文）

本件第一稿构成句（仅经封存派单文本流转、未落盘、未被任何封存产物采用）将台账序误写为连续编号段（DA-066–072、BY-039–045）。封存席前置核查 (ii) 零复用对撞查出其中 DA-069、BY-040 已在已用并集 1276（holdout12 已用）、DA-071 不在 R85 台账，停工回传；主持按台账原件（runs/round85/lr-eligible-ledger-r85.json，按书分键序列表）复算与封存席独立复算全等。本件以复算构成定版；封存未发生、无产物受影响。构成句自此以本件为准，派单引用不得再用连续段写法。

## 一、构成句（写定，组集派单逐字引用本节）

holdout33：T＝28＝六壬 14（DA 7＋BY 7）＋WHY 14。

- DA 7＝台账序 DA-066、DA-067、DA-068、DA-070、DA-072、DA-073、DA-074（《大六壬断案》未用序前 7；该源未用共 73）。
- BY 7＝台账序 BY-039、BY-041、BY-042、BY-043、BY-044、BY-045、BY-046（《六壬辨疑·毕法案录》未用序前 7；该源未用共 66）。
- WHY 14＝WHY-092、093、095、096、098、099、100、103、104、106、107、108、109、110（h32 封存日志 §十 §8 台账序余面清单前 14 序，逐 id 已核 ∉ 已用并集）。
- 轮取读法 B 沿用：本集六壬面只取 DA 与 BY 两源；YX 3 不入轮取；CY 常规（卷六附存 6）本集自动无取；CYJ 卷五 40 属 fidelity 例外面、不充常规 eligible。

## 二、产物定式（从 h32 实物）

- 输入卡：benchmark/phase3/holdout33/inputs/<id>.json（28 件），字段体例与 holdout32/inputs/ 同构。
- 金标：benchmark/phase3/holdout33/test_gold.jsonl（28 行），字段序照 h32：id, master_prediction, outcome_record, tradition, pollution, grade, grade_note, provenance, license_status, redistributable。金标文本照「案验复玩文尾」统一口径（h32 起算）：master_prediction 取原卡大师断语全文，outcome_record 取案验/复玩文尾全文。
- 快照：runs/round89/kb-snapshot-holdout33/，源＝benchmark/phase3/method/ 活树的方法文件 21 件（METHOD-INTEGRATION-*/METHOD-DISPOSAL-* 记录件不入快照，照历轮快照构成），逐件 SHA-256 与源全等。
- 封存日志：benchmark/phase3/data/holdout33-seal-log.md；三道扫描标记集出处＝holdout32-seal-log.md §八（源出 R42 PREREG §5）。

## 三、封存后账目

- 已用并集 1276＋28＝**1304**。
- 余量：六壬常规（DA＋BY＋YX 口径）余 **128**（DA 66、BY 59、YX 3）；WHY 余 **4**（WHY-111、112、114、115）；CY 卷六附存 6 与 CYJ 40 例外面分列不入常规余量。
- h34 起现限度下不可组集（六壬 14＋WHY 4＝18＜25）的面对项结论不变，出路登记照 PREREG §7。
