# Phase 3 · Round 33 预注册（消化后方法首读轮＋holdout12 验收前置）

登记：STAGE-SUMMARY-16 §三.3。本轮方法版本＝消化批次并入后的活 method/（723 条提炼＋测字新章＋SKILL 测字路由补齐，见 HOST-RULINGS-2/3），与 R29–R32 的方法血统不同，故本轮为**新方法首读**：平台判据在本文件事前声明，不继承 R32 合读池、不回溯放宽。

## §0 池与冻结

- 池 dev9＝487 例不变；输入 inputs-dev10 逐字不变（input-audit 的 CORRECTIONS 6 例本轮不落改，待 inputs-dev11 口径切换程序，声明在案）。
- 大师基线 data/master-baseline-dev9.json（均值 4.662）不变。
- 结局勘误 overlay 采用现行 16 条版（data/outcome-errata-overlay.json：原 13 条＋HOST-RULINGS-1 并入 3 条）；R30–R32 用 13 条版，本轮差异在此声明，建包时评审包按 16 条叠加。
- 方法冻结快照 runs/round33/kb-snapshot/（与活 method/ 逐字一致，主持已 diff 验）＋EVIDENCE.sha256（19 文件）。

## §1 变量声明

- 唯一变量＝方法版本（消化并入＋测字路由）。盲测席照冻结提示自由选法/混用、每例记 systems_used、不得按来源指定主法。
- 六壬只读数：按分族常例报告 dev8 源出例族上限读数、非源出例族迁移读数、合并读数只报告；断案/辨疑/粹言诸新源未入 dev9，不在本轮读数范围。
- 新体系：测字在 dev9 无案例，本轮无测字读数；其成色只由 holdout12 验收回答（如开封）。

## §2 平台判据（本轮唯一判据，事前写死；线值与 R31/R32 线集相同、不放宽）

- (a) 全集配对差 ≥ −1.371。
- (b) 分科护栏（任一破即不立）：八字全集 ≥ −0.449、八字 natal 子集 ≥ +0.290、西占 horary ≥ −0.760、六壬 dev8 子集 ≥ −2.593。
- (c) 六爻 dev8 子集（246 例）**单轮**配对差 ≥ −1.93。
- 合读声明：本轮不构成任何合读池资格（新方法首读、无同口径前轮）；(c) 不许以合读补救。若三项全立 → §3 开封 holdout12；任一不立 → holdout12 保持封存、转诊断续链，判据变更只能自下一轮预注册起。

## §3 holdout12 开封与验收（照 R32 PREREG §4 体例）

- 开封前先验金标 SHA-256 与封存值 490679552b5bcbff08df369046f977750900f7396857714a51aa438e16b30c90 逐字一致并记 data/holdout12-seal-log.md；不一致即硬阻塞上报。
- 构成注记：holdout12＝49 例（六壬 27、八字 13、测字 8、六爻 1），全 A/A-low、全 low；低污染子集＝全集。成色限度（粹言 9 例仅干支级课式）与资格准据见 holdout12/SEALED.md、HOST-RULINGS-3/4，验收报告须连同引用；结论只对本集构成所及口径发言。
- 送验 artifact＝runs/round33/kb-snapshot（SHA 清单验后送验）。
- 盲测：只给 benchmark/phase3/holdout12-inputs/ 输入卡，3 批混编（来源构成对席位不言明），照冻结盲测提示（轮次 R33-acceptance）作断。
- 评审：我方包与大师基线包各独立双评审＋|Δtotal|≥3 仲裁；大师基线由独立评审席按金标 master_predictions 对 outcome 打分建立（照 holdout9/10/11 体例）。
- 达标三判据：(i) 全集我方均分＞大师均分；(ii) 配对我方胜例多于负例；(iii) 配对差＞0 且差/SE≥1。
- 达标 → 打包 final-skill-v2（version 2.0.0，扁平根目录、恰一个 SKILL.md、仿 v1，以 round33 kb-snapshot 为正本）＋benchmark/phase3/FINAL-REPORT-v2.md 收官；未达标 → holdout12 标已用、转诊断、继续循环。

## §4 执行体例

- 盲测：runs/calib-r17/BLIND-PROMPT.txt 逐字套用（轮次 R33、输入 inputs-dev10）；批次＝round31/batches.json 逐字复制（25 批，保同口径可比）；五角分离、修订只看聚合、阴性照报、分数带 n 与 SE。
- 建包：round33 目录内新写唯一名脚本（种子 20261033）；host-mapping/host-meta 照 R32 体例（host-meta 复制 round32 并验 487 键集全等）；评审席用冻结快照 predictions 先验 anon 集一致后开评；双评审＋|Δtotal|≥3 仲裁照旧。
- 分析：round33 目录内新写唯一名脚本，产 final-scores.json 与全部读数（含分族与分科护栏子集）。

## §5 派单卫生（强制，承 R32 §6）

- 每份盲测派工文随单附：(1) 冻结盲测提示中的 trigger 条款原文；(2) 主持注记原文：「trigger 三布尔在方法文本中无成文定义（定义债挂账、本轮不处理）；本轮唯一依据＝随单所附冻结提示原文，按各例 reason 如实留痕即可；禁止为查定义 grep 全仓；禁止打开任何 runs/ 下的 predictions/judging/final-scores/splits 与旧轮 basis——曾有席位为查定义 grep 误触旧轮 predictions 而自报隔离，本轮此为硬规。」
- 一切脚本只许在 runs/round33/ 内新写唯一名文件；禁用 /tmp 残留脚本与通用脚本名；一切以盘上文件验收、回传文本不作转录源。
- 隔离自报：任何席位若意外接触禁读内容，须在回传中自报（所见内容、涉例范围），主持照 R31 补遗体例落 ADDENDUM 并核算影响；诚实自报不另罚。
