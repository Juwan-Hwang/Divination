# FREEZE-r61（R61 平台盲测冻结登记，主持盘上验盘）

## 一、验盘结果

- 主持验盘脚本 runs/round61/verify_predictions_host_r61.py 输出：want 487、files 487、missing []、extra []、bad []——**487/487 全过**（case_id 一致、五字段齐、confidence ∈[0,1]、trigger 四键结构齐且三布尔为 bool）。
- trigger 主持复算：changed_main **59**／reserve_used **54**／disputed **71**（已填入 analyze_r61.py 的 host_expected，定稿时断言对勘）。
- 席位构成：S1–S3、S5–S9 九席原派 427 例＋S4 补派三席（S4b/c/d）60 例。S4 事件见 ADDENDUM-r61 §一。

## 二、tradition 复核（主持裁定）

- check_tradition_host_r61.py 输出：direct 365／none-labelled 36／flags 86。86 件 flags 全部为「输入卡无 tradition 字段」例（inputs-dev12 卡无该字段，承前轮卡面事实），席位按派单写定口径据题面体裁自决并在 basis 首行注明。
- 主持另以 host-meta 体系逐件交叉核对（455/487 标签相符）；余 32 件逐件定性均为同族/变体标签：AS-303/304 以 astrology 泛称 vedic-astrology（卡无盘面、席位已注残损）、BQ-001 以「筮占」称 liuyao（同族称谓）、MP-001–019 共 19 例以 modern-political／现代事件占断伞标签（该组卡面无任何盘面/生辰材料、原大师体系各异，席位逐例注明残损并作事件级断）、WP 组以 western mundane/political 称谓对 mundane-astrology（同义变体）。
- **裁定：误标批为零，不重测。** 依据：被旗标各例均无卡载 tradition 可供违背；分段口径以 host-meta 为准、不以席位 basis 标签计分；伞标签各例的残损与自决理由均已逐例留痕。此裁定与 R44/R55/R60「旗标全为格式变体」判例同式。

## 三、冻结状态

- 预测集自本件提交起冻结；评审包以种子 20261067 由 build_judge_packets_r61.py 构建（anon 集与本冻结集全等由构建脚本断言）。
- 方法快照：runs/round61/kb-snapshot（与活 method 开轮时全等；与 round60 快照仅 calibration.md 失效注记一件差异，见 PREREG §0）。
