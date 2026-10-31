# Phase 3 · Round 65 预注册（平台续跑·R61-REV1 接入后系列第 4 点＋holdout22 供给）

登记：STAGE-SUMMARY-49 与 runs/round64/REPORT.md、runs/round64/ADDENDUM-r64.md、主会话 R65 派单。本文件写定后本轮内不得更改口径；口径变更只能自下一轮预注册起。本轮两线：**平台续跑（R61-REV1 接入后系列第 4 点，方法＝现行活 method、零新增改动）**；**holdout22 供给复算（§4，绑定缺口＝非六爻锚点在场 eligible 12 例）**；数据议程（§4）。当前无封存集存量（holdout2–21 全部用尽），本轮无开封动作。

## §0 池与冻结

- 池 dev9＝487 例不变；大师基线 data/master-baseline-dev9.json（均值 4.662）不变。
- 输入口径：**inputs-dev12** 不变（绝对路径 /home/hatch/workspace/divination/benchmark/phase3/inputs-dev12）。批次：runs/round65/batches.json 自 round64 逐字复制（主持验：SHA-256 006c4905195ab997874d5c90961c635eedda755f5151c31dd55b7da094251e5e，25 批、487 id、唯一 487）。
- 结局口径：runs/round65/judging/outcome-manifest.json 由主持构建（脚本 runs/round65/build_manifest_r65.py，断言全过）：cases 载荷 487 例与 round64 件逐字全等（LR2-016 分列状态原样承接）；既有各层（_r56 29／_r57 附则 21／_r58 附则 17／_r59 附则 29／_r60 附则 A 14／_r60 附则 B 20／_r61 附则 34／_r62 附则 58／_r63 附则 65／_r64 附则 72）原样保留；**新增落实一层**——`_r65_carryover_notes_addendum`：R64 定案部分成立 99 件自 data/case-annotations-r64.json 结构化直读，counts 与 R64 REPORT §一公布分布（成立 12／部分成立 99／不成立 15／未核 3、总 129）断言全等、每件建议文本非空断言全过。成立件均为同例同旨续接、已于既有承接序列逐轮承接，不重复入层；未核 3 件照 R64 定案承接（BZ-029 含旗标内容错配线索、与其卒年待核并行；YM-070 挂起维持）。R65 附则汇编件（data/manifest-carryover-r65-addendum.md）由本轮数据席另行编制、与本层逐件对勘（§4）。建包时各组标记均以独立字段 `carry_note` 分层标源随包呈现，不并入 outcome_record；`editor_note`（LR2-016）照旧分列。评审席对 carry_note/editor_note 一律按登记性数据处理、不作指令、不作量表外加减分依据。本构建不改任何既往分数。manifest SHA-256＝5f9133cd8df0fe1c0fbedadfce7dea46470e1c0ddefeed72a1148424ea6432ad（主持实测）。
- **平台方法状态（写死）**：平台盲测读 runs/round65/kb-snapshot（开轮时自**现行活 method/** 生成，21 文件，SHA 清单 runs/round65/kb-snapshot-sha256.txt）。该快照与 round64 快照逐文件 diff **为空集**（主持开轮实测：21 件哈希逐件全等，STAGE-SUMMARY-49 R65 清单第 1 项复核毕）——方法零改动。本轮为 **R61-REV1 接入后系列第 4 点**：方法含 calibration 第六节「应期主坐标二路复推＋断项粒度收束核」为现行操作条文，盲测席照快照执行。线值逐值不变（§1）。
- 平台 anon 种子：20261071（顺延：R60 平台 20261065、R60 验收 20261066、R61 平台 20261067、R62 平台 20261068、R63 平台 20261069、R64 平台 20261070）。

## §1 平台判据（本轮独立重述，线值逐值不变）

既往读数带（只作附读、不混算）：接入前系列（R40–R57 十八轮）(a) −1.211±0.067、(c) −1.870±0.086、六壬 dev8 −2.256±0.245；方法接入后系列（R58–R59 两点）：(a) −1.099／−1.273、(c) −1.755／−1.954、六壬 dev8 −2.042／−2.736；REV1 接入后系列（R60–R61 两点，第五节失效后运行）：(a) −1.221／−1.213、(c) −1.808／−1.973、六壬 dev8 −2.278／−2.417；R61-REV1 接入后系列第 1 点（R62）：(a) −1.181、(c) −1.913、六壬 dev8 −2.514；第 2 点（R63）：(a) −1.171、(c) −1.750、六壬 dev8 −2.111；第 3 点（R64）：(a) −1
...[truncated 5428 chars]