# FREEZE-r81（R81 平台盲测冻结登记）

- 冻结时点：R81 平台盲测 25 批全回后，续任主持验盘（verify_predictions_host_r81.py 全量复跑）通过：**want 487／files 487／missing 0／extra 0／bad 0**，字段与 trigger 子字段逐件齐全、confidence 均在 0–1。前任主持已验 7 批（B01/B02/B05/B12/B18/B19/B25，127 件）由本任以全量验盘复核覆盖；B13 以盘上订正版终件为准（验盘对象即盘上终件）。
- trigger 主持复算：changed_main **51**／reserve_used **50**／disputed **69**；trigger reason 非空 324 件。analyze_r81.py 之 host_expected 已由本任回填为 {changed_main: 51, reserve_used: 50, disputed: 69}，定稿以 analyze 复算对勘为准。
- 快照口径：本轮平台盲测读 runs/round81/kb-snapshot（R80-REV1 接入后系列第 1 点，与 holdout25 封存快照差异恰两文件，见 PREREG 开轮登记）。

## 一、tradition 首行核查（主持检查器＋逐件回读裁定）

检查器初检 flags **33 件**（全为 card_has_field_but_first_line_unmarked 型），逐件回读原卡与 basis 首行后裁定：

1. **LY 32 件（LY-211、215、216、217、219、220、221、222、227、228、230、231、232、234、235、237、240、241、455、457、501、502、503、507、508、509、510、511、512、513、514、515）——不成立（检查器误报）**：32 例卡面均载 tradition＝liuyao，basis 首行逐字作「卡面 tradition＝liuyao；…卡面值照录于此行」或「tradition: liuyao（卡面原值照录）」，systems_used 行均作六爻纳甲（liuyao），与卡面值逐字相符——检查器未标注关键词命中系行内他处字面误触（承 R78 同型判例：初检 flags 逐件回读后裁定）。不作废不重测。
2. **AS-307（B02）——部分成立，不作废不重测**：卡面顶层明载 tradition＝astrology，basis 首行作「卡面未标注 tradition 字段，按题面体裁自决」，属对卡面字段之误读误述；但本例实际所用方法为 astrology（systems_used 行明载「astrology（选举占星，自决采用）」），与卡面值实质一致。与 R80 同例旗标同型，照 FREEZE-r80 §一.1 operative 口径裁定部分成立，不作废不重测，入本轮旗标定案流水（registered_round＝81，随 manifest 新层落实）。
- 声明互斥加扫（全 basis CLAIM 声明组数）：**0 例**。

## 二、隔离与卫生（两件席位自报，本任裁记）

1. **B11 席 /tmp 语法探针自报**：该席调试时曾在 /tmp 短暂生成语法探针文件（脚本头部副本、**无任何案例数据**），发现后自删、其后校验全改本轮目录内。裁记：形式触犯 PREREG §7「禁 /tmp」明文（禁令涵盖探针与转储，R72 起判例在册），但内容不涉案例/金标/他批产出、自报及时且当场清除、验盘 487/487 全过，**实质影响为零——只登记、不作废不重测**；后续派单明文重申探针类临时件亦只许本轮目录内。
2. **B22 席列示 kb-snapshot 目录自报**：该席曾列示 runs/round81/kb-snapshot 目录以定位方法篇目，称未触禁读内容。本任对勘：所列目录为该席本轮**授权必读**之方法快照本体，非 judging/predictions/他轮目录，未涉计数核验捷径、未触金标与他批产出。裁记：与「目录计数禁令」（防对 predictions/judging 列表计数）之规范目的不侔，**不构成违规，只登记备查**；后续派单宜明文豁免「为定位篇目列示本轮方法快照目录」一格，以免席位无所适从。
- 其余各席回传均声明未触金标/judging/final-scores/splits/旧轮 basis；无其他隔离自报。

## 三、冻结结论

487 件冻结成立；其后只许评审与分析，预测件不得再改。冻结件随本登记提交、标签 phase3-round81-blind-frozen。
