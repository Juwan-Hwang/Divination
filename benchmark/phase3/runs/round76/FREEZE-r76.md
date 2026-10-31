# FREEZE-r76 — R76 盲测冻结记录

（主持角，2026-10-31。预注册：runs/round76/PREREG.md；匿名种子 20261082。本件冻结后方许构建评审包。）

## 一、验盘（主持盘上复算）

- verify_predictions_host_r76.py：487/487 全在盘，缺失 0、额外 0、结构坏件 0（case_id/prediction_text/basis/confidence/trigger 结构全检通过）。
- 六爻 trigger 主持复算：changed_main＝29、reserve_used＝52、disputed＝87；与十席回传分项和逐值全等（29/52/87）。
- 方法零改动：kb-snapshot 21 件与 round75 快照 diff 空集（开轮已验，见 PREREG §0）。

## 二、tradition 检查与裁定（承 R69 模板首行判例与 R74/R75 覆盖缺口判例）

- check_tradition_host_r76.py 初检：direct 365、none-labelled 100、flags 22；声明组数加扫：声明组 0、冲突组 0。
- flags 22 件逐件裁定分两类：
  - **不成立 16 件**（MP-019、OC-001/006/009/011/014/017/020/023/025/026/029、WP-001/003/004/007）：首行均明写卡面未见/未载 tradition 字段（如实注明），检查器关键词表未含「未见／未载」变体，属覆盖缺口；不作废不重测，实效归 none-labelled。检查器变体补集（未见／未载）登记入 ADDENDUM，自 R77 起补。
  - **部分成立 6 件**（BZ-032/035/036/037/038/041）：主持逐件回读卡面（全部 inputs 副本对勘）——卡面确无 tradition/system 字段，basis 首行却统一写「卡面 tradition＝bazi」，属 R69 型全批统一首行模板虚称卡面字段；所用方法实质为八字、断语不受影响，裁定部分成立，不作废不重测，入旗标定案流水待数据席 manifest 注记落实（承 R75 部分成立 48 件同型处置）。
- 实效分布：direct 365 / none-labelled 116 / 部分成立 6。

## 三、本轮隔离与自报事项登记（详见 ADDENDUM-r76）

- S1：AS-301–307 卡面 attachments 为空、无盘面数据，席位已注明残损并降置信；BQ 全批 chart_complete=false，只据卡面自述状态判读。
- S5：reserve_used＝20 为十席最高，系该批伏神取用逐例留痕所致，trigger 语义内事项，只登记。
- S6：MP-001–016 卡面无盘面字段，席位未臆造盘面、如实注明并降置信；LY-626 盘面 OCR 还原不可靠，未臆取伏神。
- S9：YY2-004 本卦名原书缺字、盘面字段 null，席位照实注明残损、confidence 0.05，未臆补。
- 十席均自报未读 judging/final-scores/金标/他席预测，中间件只写本轮目录内，未写 /tmp，无通配删除事件。

## 四、冻结

- 本件落盘＋冻结提交后打标签 phase3-round76-blind-frozen；此后方许 build_judge_packets_r76.py 构建评审包并派评审席。
