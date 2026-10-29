# Phase 3 · Round 32 预注册（零改动复现轮＋(c) 合读判据）

登记：STAGE-SUMMARY-14 §3 合读路径＋input-audit/PILOT-REPORT.md §5（六爻数据侧 NO-GO、维持观察）。本轮无任何方法/输入变量，目的＝为平台 (c) 提供第三轮同口径读数并按 §2 事前声明的合读判据裁决，同时复核平台 (a)(b)。

## §0 池与冻结

- 池 dev9＝487 例不变；输入 inputs-dev10 逐字不变。注：input-audit 定案的 6 例 A 类纠正值登记于 input-audit/CORRECTIONS.md，**本轮不落改**——合读池要求六爻输入与 R30/R31 逐字同口径，勘误待下一输入版本按口径切换程序采用（inputs-dev10 原件不动）。
- 大师基线 data/master-baseline-dev9.json（均值 4.662）不变；overlay 13 例常设叠加不变。
- 方法：活 method/（R31 六壬 22 条已 revert 后状态）。主持已验：method/ 与 round31 kb-snapshot 的 diff 仅 chinese-liuren.md 一文件（即 revert 本身）；六爻方法与 R29 快照血统一字未动。本轮冻结快照 runs/round32/kb-snapshot/（＋EVIDENCE.sha256）。
- 数据卫生照 R31 PREREG §6 单份登记：LY-036 旧版输入参跑、DT-002/004/006 已知瑕疵、LR-001 仅单列、overlay 13 例单列——原文照录不复述，本轮不处理；trigger 三布尔定义债仍挂账，本轮不搭车处理。

## §1 变量声明

- 无变量。盲测席照冻结提示自由选法/混用、每例记 systems_used、不得按来源指定主法。
- 六壬只读数：按分族常例报告 dev8 源出例族上限读数、非源出例族迁移读数、合并读数只报告；不立条目、不挂判据（平台 (b) 的 dev8 子集护栏除外，照 §3）。
- 六爻只观察：(c) 判据见 §2。

## §2 平台 (c) 合读判据（本轮新预注册，为本轮 (c) 唯一判据；不溯及既往）

- 立据：(c) 子集单轮读数 R30 −1.632、R31 −1.955（同口径，inputs-dev10；R29 −1.642 系 inputs-r28、不同口径，仅作旁证不入池）。轮 SE≈0.13，而门槛线 −1.93 距两轮读数之差（0.32）小于两轮间摆动本身——在此邻近区，单轮判读测的主要是盲测/评审重采样噪声而非段位水平。故本轮改以多轮合读裁决 (c)，公式与资格事前写死如下；R31 的单轮「不立」判读在其 REPORT 中原样保留、不因本节改动；本节只管 R32 这一轮的平台裁决。
- 资格池：六爻输入与 inputs-dev10 逐字相同、且六爻方法属 R29 快照血统未改的轮次＝{R30、R31、R32}（本轮）。
- 公式：对 (c) 子集 246 例逐例取三轮配对差（各轮定稿 final-scores 我方 total − dev8 大师基线 total）的均值，再对 246 例取平均（各轮 n 同为 246，与轮均值平均等价，逐例式为正典）。
- 判据：合读 (c) ≥ −1.93 → (c) 立。
- 熔断：若 R32 单轮 (c) < −2.255，则合读作废、(c) 不立（防以合读掩盖真实恶化；−2.255＝R31 证伪档线）。
- 报告义务：REPORT 须并列 R32 单轮 (c)、三轮逐轮读数与合读值，SE 照算。

## §3 平台其余判据（R32 当轮读数，线值与 R31 全同、不放宽）

- (a) 全集配对差 ≥ −1.371。
- (b) 分科护栏（任一破即不立）：八字全集 ≥ −0.449、八字 natal 子集 ≥ +0.290、西占 horary ≥ −0.760、六壬 dev8 子集 ≥ −2.593。
- 平台全立（(a)∧(b)∧§2）→ §4 开封 holdout11。

## §4 holdout11 开封与验收（照 R31 PREREG §4 体例）

- 开封前先验金标 SHA-256 与封存值 e0d43559b2f915dcbbd2b7275efbf8f5259f12fbd0985dd0f68a3749aac81d40 逐字一致并记 data/holdout11-seal-log.md；不一致即硬阻塞上报。
- 构成注记：holdout11＝25 例单一六爻（YB-001…022＋ZG-001…003，全 A-low）；验收结论只对六爻/全池口径发言；低污染子集＝全集（25 例全 low）。
- 送验 artifact＝runs/round32/kb-snapshot（SHA 清单验后送验）。
- 盲测：只给 inputs——YB 取 data/expansion10/ 两批 inputs、ZG 取 data/expansion11/bushi-zhengzong/inputs/，2 批混编，席位不知来源构成。
- 评审：我方包与大师基线包各独立双评审＋|Δtotal|≥3 仲裁；大师基线由独立评审席按大师原断对结局打分建立（照 holdout9/10 体例）。
- 达标三判据：(i) 全集我方均分＞大师均分；(ii) 配对我方胜例多于负例；(iii) 配对差＞0 且差/SE≥1。
- 达标 → 打包 final-skill-v2（version 2.0.0，扁平根目录、恰一个 SKILL.md、仿 v1）＋benchmark/phase3/FINAL-REPORT-v2.md 收官回报；未达标 → holdout11 标已用、转诊断、继续循环。

## §5 执行体例

- 盲测：runs/calib-r17/BLIND-PROMPT.txt 逐字套用（轮次 R32、输入 inputs-dev10）；批次＝round31/batches.json 逐字复制（25 批，保同口径可比）；五角分离、修订只看聚合、阴性照报、分数带 n 与 SE。
- 建包：round32 目录内新写唯一名脚本（种子 20261032）；host-mapping/host-meta 照 R31 体例（host-meta 复制 round31 并验 487 键集全等）；评审席用冻结快照 predictions 先验 anon 集一致后开评；双评审＋|Δtotal|≥3 仲裁照旧。
- 分析：round32 目录内新写唯一名脚本，产 final-scores.json 与全部读数（含 §2 合读，自 round30/31/32 三轮 final-scores 计算）。

## §6 派单卫生（强制，承 R31 隔离补遗 §6 增补）

- 每份盲测派工文随单附：(1) 冻结盲测提示中的 trigger 条款原文；(2) 主持注记原文：「trigger 三布尔在方法文本中无成文定义（定义债挂账、本轮不处理）；本轮唯一依据＝随单所附冻结提示原文，按各例 reason 如实留痕即可；禁止为查定义 grep 全仓；禁止打开任何 runs/ 下的 predictions/judging/final-scores/splits 与旧轮 basis——R31 曾有席位为查定义 grep 误触旧轮 predictions 而自报隔离，本轮此为硬规。」
- 一切脚本只许在 runs/round32/ 内新写唯一名文件；禁用 /tmp 残留脚本与通用脚本名；一切以盘上文件验收、回传文本不作转录源。
- 隔离自报：任何席位若意外接触禁读内容，须在回传中自报（所见内容、涉例范围），主持照 R31 补遗体例落 ADDENDUM 并核算影响；诚实自报不另罚。
