# FREEZE-r80（R80 平台盲测冻结登记）

- 冻结时点：R80 平台盲测 25 批全回后，主持验盘（verify_predictions_host_r80.py）通过：**want 487／files 487／missing 0／extra 0／bad 0**，字段与 trigger 子字段逐件齐全、confidence 均在 0–1。
- trigger 主持复算：changed_main **118**／reserve_used **50**／disputed **69**（各席回传计数为主持复算之附读，定稿以 analyze 复算为准）。
- 快照口径：本轮平台盲测读 runs/round80/kb-snapshot（与 round79 平台快照逐件零差异，含 calibration 第七节，R78-REV1 接入后系列第 2 点）。

## 一、tradition 首行核查（主持检查器＋逐件回读裁定）

检查器初检 flags 3 件，逐件回读原卡与 basis 首行后裁定：

1. **AS-307（B02）——部分成立，不作废不重测**：卡面顶层明载 tradition＝astrology，basis 首行却作「卡面未标注 tradition 字段——此卡无 tradition 行」，属对卡面字段之误读误述；但本例实际所用方法为西洋占星（systems_used 行明载），与卡面 tradition 值实质一致、断语方向不受影响；且该席回传自报与落盘文字一致（误读而非自相矛盾）。照 R76 BZ 六件判例之 operative 口径（方法实质一致、断语不受影响）裁定部分成立，不作废不重测，入本轮旗标定案流水待数据席 manifest 注记落实。与 R79 LY-022 真虚称（声称卡面值以自证＋回传自相矛盾）之区别在此登记。
2. **LR3-004、LR3-104（B06）——不成立（检查器误报）**：两例卡面确无 tradition/system 字段，basis 首行已以散文逐字写明「本例卡面没有 tradition／system 两字段……自决作断」，属未标注声明之完整表述；检查器未标注关键词集未含「没有」变体，属覆盖缺口（承 R78/R79 同型判例）。不作废不重测；「没有」变体补集登记入 ADDENDUM-r80，自 R81 起检查器口径补入。
- 声明互斥加扫（全 basis CLAIM 声明组数）：**0 例**。
- 首行模板盘点：互异模板 295 种，无全批统一套话异常（最大组 33 件为卡面照录型，属卡面值同为 liuyao/horary 之正常聚集）。
- 卡面载 tradition/system 字段 365 例、未载 122 例。

## 二、隔离与卫生

- 各席回传均声明未触金标/judging/final-scores/splits/旧轮 basis；无席位自报隔离事件。数件会话内 exec 非零退出（B03/B08/B14）经主持盘上逐件复验产出完整有效，照 R68 登记口径记完成、只登记。
- 席位生成脚本均在 runs/round80/ 内唯一名文件（write_b01–b25_r80.py）；B04 自报首跑缩进落盘丢失已自修复重跑、产出经复验完整，只登记。

## 三、冻结结论

487 件冻结成立；其后只许评审与分析，预测件不得再改。冻结件随本登记提交、标签 phase3-round80-blind-frozen。
