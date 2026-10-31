# EXPANSION-AUDIT-SUMMARY-r84 — expansion 池资格核查汇总（R84 主持复算）

核查面：expansion 池层全部未用 id（四席分工：E1 小池组 expansion/expansion6/expansion8/expansion9、E2 expansion11、E3 expansion12 前半七子池、E4 expansion12 后半五子池＋根散件）。标准照 R83 PREREG §5 裁决：四滤（逐字原文／独立结局／可分离／非 high 污染）＋A 或 A-low＋low＋锚点在场，逐例登记，标准未改。

## 一、并集与未用复算

- 已用并集：四席各自盘上复算均为 **1166**（dev 488＋holdout2 29＋holdout3–28 金标 id 754＋holdout2–28 inputs 595＋顶层 inputs6–10 412），与主持开轮实算一致。
- 池层未用合计 **691**，与 STOCK-RECOUNT-h27 §3.4 登记逐层全等：expansion 2／expansion6 15／expansion8 31／expansion9 3／expansion11 180／expansion12 460。

## 二、eligible 分面计数（主持裁定后）

| 池层 | 未用 | eligible | 构成 |
|---|---|---|---|
| expansion | 2 | 0 | LY-302/303 为 B 级不可分离 |
| expansion6 | 15 | 0 | 全 B 级（holdout_eligible=false），MP 三例另 high 污染 |
| expansion8 | 31 | 0 | MT 全 B、无 outcome、inputs 为空 |
| expansion9 | 3 | 0 | LR3-103/106/108 照 HOST-ADJUDICATION 终裁不入池（见 §三） |
| expansion11 | 180 | 0 | 索引条目资格证据回源卡读取后无一全过；其声称 2 例经 §三裁定归 expansion9 层且不 eligible |
| expansion12 前半 | 340 | **243** | 全六壬：六壬断案 97／六壬粹言 55／六壬变易预测 91 |
| expansion12 后半 | 120 | 0 | natal 两子池资格全过集均已在已用并集内 |
| **合计** | **691** | **243** | **非六爻 243（全六壬）／六爻 0／其他体系 0** |

## 三、跨席冲突裁定（LR3-106／LR3-108）

- E1（expansion9 层）照 HOST-ADJUDICATION（2026-10-30 主持裁决）判 LR3-103/106/108 不入池/降 B；E2（expansion11 层）照原卡台账字段（A 级、low、holdout_eligible=true）判 LR3-106/108 eligible，并注明系经本层 pool-index 计入、与 expansion9 为同一批 id。
- **主持裁定**：HOST-ADJUDICATION 为针对该批 id 的在后专项终裁，优先于原卡台账字段——LR3-106/108 **不 eligible**，归 expansion9 层计、只计一次；expansion11 层 eligible 相应为 0。此裁定同时消除跨池重复计入面。
- 连带登记：expansion9 三例 cases 自标与 HOST-ADJUDICATION 的冲突已在 E1 台账登记，池层原文未改。

## 四、门槛与构成可行性（供 PREREG-ADDENDUM-r84 裁定）

- PREREG §5 量门槛「非六爻 eligible ≥13」：实得 243，**达限**。
- 构成限度（照旧）：T≥25、单体系 ≤50%、单源 ≤50%、非夷坚 ≥13、非六爻 ≥13、仅锚点在场、逐 id 零复用。eligible 全部集中于六壬单一体系：任一合规构成中六壬至多占半数，须有 ≥（六壬入选数）的非六壬 eligible 配平；非六壬 eligible 实得 **0**。以最小构成计（六壬 13＋他系 13＝26），他系缺口 **13**。
- 附注：E3 台账锚点 present 系按池卡课式头四要素判定、盘面本体不在池卡内，组集建卡时仍须回原文复原——本轮因构成不可行未进入该工序，仅登记。
