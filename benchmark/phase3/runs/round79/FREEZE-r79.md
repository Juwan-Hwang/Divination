# FREEZE-r79（R79 平台盲测冻结记录，主持验盘）

- 核验脚本：runs/round79/verify_predictions_host_r79.py（主持开轮后适配，含 tradition 三口径检查＋声明互斥加扫）。
- 覆盖：batches.json 25 批 487 id 与 predictions/ 盘上文件集逐件对位——**487/487，missing 0、extra 0、bad 0**（字段 case_id/prediction_text/basis/confidence/trigger 齐、case_id 对位、confidence∈[0,1]、trigger 三布尔＋reason 齐，全数通过）。
- trigger 主持复算（冻结终值）：**changed_main 68、reserve_used 44、disputed 100**（analyze_r79.py host_expected 已按此填入）。
- tradition 复核：卡面载 tradition/system 365 例、未载 122 例。检查器首跑旗 17 件，主持逐件回读首行＋卡面字段裁定：
  - **LY-022（B07）——真虚称，作废重测**：卡面无 tradition/system 字段，basis 首行却作「卡面 tradition＝liuyao」，且与该席自报（称已写未标注声明）矛盾；按 PREREG §7 与 R66 逐例判例裁定该例作废（原件移存 runs/round79/voided/LY-022.json.voided-r79-falseclaim），由全新席全盲重测覆盖（新件首行如实写未标注、trigger 0/0/0，与原件同为 0/0/0，冻结复算不变）。重测后复跑核验：旗减为 16。
  - **OC-001/002/003/004/005/006/007/008/010/011/012/013/014/015/016/017（B19）16 件——声明形式简省，登记放行**：卡面未载 tradition/system，首行逐例以本例 provenance/四柱事实落笔并载 systems_used，未作任何「卡面 tradition＝…」式断言、无「与卡面一致」虚称、无误标（tradition 值从未被声称）；属声明措辞不合推荐句式，非虚称非误标，照 R78 旗标逐件裁定体例登记、不重测。
  - 声明互斥加扫（全 basis CLAIM 组数）：**0 例**。
  - 首行模板盘点：互异模板 259 种，无全批统一套话异常（最大组为卡面照录型 44 件，属卡面值同为 liuyao 之正常聚集）。
- 隔离与卫生：各席回传均声明未触金标/judging/旧轮 predictions；无席位自报隔离事件。席位生成脚本均在 runs/round79/ 内唯一名文件。
- 快照口径：本轮平台盲测读 runs/round79/kb-snapshot（含 calibration 第七节，R78-REV1 生效首轮）。
- 冻结结论：487 件冻结成立，标签 phase3-round79-blind-frozen；其后只许评审与分析，预测件不得再改（LY-022 重测件已在冻结前落盘并复核）。
