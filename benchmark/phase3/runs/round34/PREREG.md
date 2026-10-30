# Phase 3 · Round 34 预注册（零改动复现＋六壬回落诊断轮＋holdout12 验收前置）

登记：STAGE-SUMMARY-17 §三.1（R34 预注册）、§三.2（数据卫生三项，与方法轮分离立项，见 §6）。本文件写定后本轮内不得更改口径。

## §0 池与冻结

- 池 dev9＝487 例不变；输入 inputs-dev10 逐字不变（input-audit 的 CORRECTIONS 6 例本轮不落改，inputs-dev11 切换为 §6.③ 的独立卫生立项，于本轮分析定稿后执行，不影响本轮任何读数与 §2(c) 合读资格）。
- 大师基线 data/master-baseline-dev9.json（均值 4.662）不变；结局勘误 overlay 现行 16 条版不变，与 R33 同口径。
- 方法冻结：runs/round34/kb-snapshot 与 runs/round33/kb-snapshot **逐字一致**（主持 diff 验＋两轮 EVIDENCE.sha256 逐行全等）——本轮平台轮为 R33 方法的**零改动复现**。活 method/ 本轮冻结不动；消化支线产出只入暂存（§7），不并入活 method。

## §1 六壬回落诊断（第一优先；诊断轮，不动 §2 平台判据）

背景：R33 六壬两族同落（dev8 族 −1.847、LR3 族 −2.021、合并 −1.917；R32 合并 −1.100），与六壬章消化增补（434→1091 行、增 287 条级）同轮出现，性质未定。本诊断先定成因（条目稀释／冲突干扰／抽样），再谈处置；**未诊断先删条禁止，本轮不增删六壬章任何条目**。

- 对象：dev9 六壬 30 例（dev8 源出族 18＋LR3 迁移族 12，名单见 batches-diag.json）。
- 两快照：FULL＝runs/round34/kb-snapshot（六壬章 1091 行增补全章版）；CORE＝runs/round34/kb-diag-core，与 FULL **仅 references/chinese-liuren.md 一文件不同**——替换为 runs/round32/kb-snapshot 同名文件（434 行，即 R30–R32 诸轮读数所据、消化增补前的指南核心条文版；主持 diff 验仅此一文件、双快照哈希清单存 EVIDENCE-kb-snapshot.sha256／EVIDENCE-kb-diag-core.sha256）。
- 设计：30 例按族内排序 stride-3 分 3 块（每块 dev8 6＋LR3 4，见 batches-diag.json）；每块由两名不同盲测席分别在 FULL／CORE 快照下各读一遍（共 6 席，席内只接触一种快照、不得改读另一快照或活 method），每例得两臂各一条预测。盲测提示逐字冻结（轮次 R34-diag），输入同 inputs-dev10，方法自选口径不变（六壬案例仍照 SKILL 路由、不得指定主法之外的任何限制）。
- 评审：60 条预测匿名混编为一包（臂别不示），独立双评审＋|Δtotal|≥3 仲裁，量表与评审提示逐字冻结（runs/calib-r17/JUDGE-PROMPT.txt）；结局只取自 §4 显式清单。
- 主对照（事前写死）：逐例 Δ＝配对差_FULL − 配对差_CORE（配对差均对 master-baseline-dev9 同例总分）；主读数 Δ_merged（n=30），分族读数 Δ_dev8（n=18）、Δ_LR3（n=12），一律带 n 与 SE。
- 判读带（事前写死）：Δ_merged ≤ −0.50 且两族 Δ 同号为负 → 「增补致回落（条目稀释／冲突干扰）」成立，处置（条目精选／回滚候选）由修订角只据聚合另行提议、留 R35 预注册决定；Δ_merged ≥ +0.50 → 增补有益，R33 回落归席位／抽样方差；|Δ_merged| < 0.50 → 本分辨力下未定，抽样方差不排除，章维持现状。两族 Δ 符号相左 → 只报分族、不作合并结论。稀释与冲突干扰的细分只许据两臂 basis 的聚合形态（如冲突条文援引计数）作旁证登记，不单独成立结论。
- 附读（只报告，不判读）：诊断 FULL 臂 30 例读数 vs R33 平台同例读数（同方法异席，席位方差标尺）；诊断 CORE 臂 vs R32 平台同例读数（同章异轮，其他篇目代差在案）。
- 诊断结论不改变 §2 判据、不回改 R33 定稿；natal 子集本轮只作 §2(b) 护栏读数与附读，不单独设轮。

## §2 平台判据（沿用 R33 §2 线值，于本文件重述为本轮唯一判据）

- (a) 全集配对差 ≥ −1.371。
- (b) 分科护栏（任一破即不立）：八字全集 ≥ −0.449、八字 natal 子集 ≥ +0.290、西占 horary ≥ −0.760、六壬 dev8 子集 ≥ −2.593（平台轮读数，FULL 方法）。
- (c) 六爻 dev8 子集（246 例）**合读资格事前声明**：inputs-dev10 与 R33 逐字不变、六爻方法血统自 R33 快照起算且本轮快照与之逐字一致（§0 哈希全等为据），故 (c) 以 R33＋R34 合读判——492 个例轮观测合并配对差 ≥ −1.93 → 立。**熔断**：R34 单轮 (c) 配对差 < −2.255 → 合读资格作废，(c) 只按 R34 单轮判（≥ −1.93 才立）。R34 单轮 (c) 读数照例并列报告。本声明只确立 R34 的判读口径，不追改 R33 定稿（R33「平台不全立」结论照旧、不追认）。
- 三项全立 → §3 开封 holdout12；任一不立 → holdout12 保持封存、转诊断续链，判据变更只能自下一轮预注册起。

## §3 holdout12 开封与验收（照 R33 PREREG §3 体例，轮次改 R34）

- 开封前先验金标 SHA-256 与封存值 490679552b5bcbff08df369046f977750900f7396857714a51aa438e16b30c90 逐字一致并记 data/holdout12-seal-log.md；不一致即硬阻塞上报。
- 构成注记：holdout12＝49 例（六壬 27、八字 13、测字 8、六爻 1），全 A/A-low、全 low；低污染子集＝全集。成色限度（粹言 9 例仅干支级课式）与资格准据见 holdout12/SEALED.md、HOST-RULINGS-3/4，验收报告须连同引用；结论只对本集构成所及口径发言。
- 送验 artifact＝runs/round34/kb-snapshot（与 round33 快照逐字一致，SHA 清单验后送验）。
- 盲测：只给 benchmark/phase3/holdout12-inputs/ 输入卡，3 批混编（来源构成对席位不言明），照冻结盲测提示（轮次 R34-acceptance）作断。
- 评审：我方包与大师基线包各独立双评审＋|Δtotal|≥3 仲裁；大师基线由独立评审席按金标 master_predictions 对 outcome 打分建立（照 holdout9/10/11 体例）；结局与大师断语只许来自 holdout12/test_gold.jsonl 本文件，不经任何全树检索。
- 达标三判据：(i) 全集我方均分＞大师均分；(ii) 配对我方胜例多于负例；(iii) 配对差＞0 且差/SE≥1。
- 达标 → 打包 final-skill-v2（version 2.0.0，扁平根目录、恰一个 SKILL.md、仿 v1，以 round34 kb-snapshot 为正本）＋benchmark/phase3/FINAL-REPORT-v2.md 收官；未达标 → holdout12 标已用、转诊断、继续循环。

## §4 执行体例

- 平台盲测：runs/calib-r17/BLIND-PROMPT.txt 逐字套用（轮次 R34、输入 inputs-dev10、方法 runs/round34/kb-snapshot）；批次＝round33/batches.json 逐字复制（25 批，保同口径可比）；五角分离、修订只看聚合、阴性照报、分数带 n 与 SE。
- 建包（卫生①落地）：评审包结局**只许**来自显式源清单 runs/round34/judging/outcome-manifest.json（由 R33 官方评审包 packetA/packetB＋packetMP 纠正包经 round33 host-mapping 还原，overlay 16 例逐字自验通过、MP 抽查与 natal-batch2 文本零重合；构建脚本 build_outcome_manifest_r34.py 在案）。本轮建包脚本禁用 rglob／全树检索，违者作废重建。全树编号唯一性审计 audit_ids_r34.py 已跑（audit-ids-report.json）：全树结局冲突仅 MP-001…022 一族（expansion12/natal-batch2 与 expansion6/modern-cn 撞号），dev9 内即 MP-001…019，与 ADDENDUM-mp-collision 定案一致；其余 468 例 dev9 结局全树唯一。
- anon_id：种子 20261034，体例同 R33；host-meta 复制 round33 并验 487 键集全等。
- 评审席用冻结快照 predictions，先验 anon 集与 host-mapping 一致后开评；claims 须经 host-mapping 回读 prediction_text 全文（冻结评审提示原文）。
- 分析：round34 目录内新写唯一名脚本，产 final-scores.json 与全部读数（含分族、分科护栏、(c) 单轮与合读、诊断对照表）。

## §5 派单卫生（强制，承 R33 §5）

- 每份盲测派工文随单附：(1) 冻结盲测提示中的 trigger 条款原文：「trigger（六爻：changed_main、reserve_used、disputed 三布尔＋reason；非六爻三项全 false、reason 空串）」；(2) 主持注记原文：「trigger 三布尔在方法文本中无成文定义（定义债挂账、本轮不处理）；本轮唯一依据＝随单所附冻结提示原文，按各例 reason 如实留痕即可；禁止为查定义 grep 全仓；禁止打开任何 runs/ 下的 predictions/judging/final-scores/splits 与旧轮 basis——曾有席位为查定义 grep 误触旧轮 predictions 而自报隔离，本轮此为硬规。」
- 诊断席另附硬规：所读快照路径以派工文为准（FULL 席只读 runs/round34/kb-snapshot、CORE 席只读 runs/round34/kb-diag-core），不得改读活 method/ 或另一快照；两快照差异属实验设计，席内不言明。
- 一切脚本只许在 runs/round34/ 内新写唯一名文件；禁用 /tmp 残留脚本与通用脚本名；一切以盘上文件验收、回传文本不作转录源。
- 隔离自报：任何席位若意外接触禁读内容，须在回传中自报（所见内容、涉例范围），主持照 R31 补遗体例落 ADDENDUM 并核算影响；诚实自报不另罚。

## §6 数据卫生（与方法轮分离立项；不改本轮任何输入、预测与判据）

- ① 建包器显式源清单＋全树编号唯一性审计：已于本轮建包前落地，见 §4 与 audit-ids-report.json；此后各轮沿用显式清单体例。
- ② natal-batch2 编号重编：expansion12/natal-batch2/cases.jsonl 与 cases-reviewed.jsonl 内 QM-001…035 → QL-001…035（与 holdout12 既用映射同号对齐：QM-005→QL-001、QM-007→QL-002、QM-010→QL-003、QM-020→QL-004、QM-023→QL-005、QM-027→QL-006、QM-029→QL-007、QM-031→QL-008，其余按原序续编 QL-009…035）；MP-001…056 → 新前缀 PU-001…056（PU 前缀经全树审计未占用，见 STAGE-SUMMARY-18 登记）。映射落 expansion12/natal-batch2/RENUMBER-MAP.json（旧→新全表）；两数据文件 id 字段实改并留改前哈希；expansion12 内文档类引用不回改原文，另立 RENUMBER-NOTE.md 指引映射（证据只增不删）；holdout12 金标与 SEALED 的 source_id 保持原文、经映射可解。本项与 dev9 池无涉（natal-batch2 不在 dev9），与本轮盲测/评审并行执行互不污染。
- ③ inputs-dev11 口径切换：本轮分析定稿后执行——以 inputs-dev10 为底，按 input-audit/CORRECTIONS.md 6 例（LY-006、LY-010、LY-105、YY2-001、YY2-002、YY2-005）逐字落改建 inputs-dev11/，逐例 diff 登记；自 R35 起输入口径为 inputs-dev11、一切合读池资格重置（R33/R34 合读关系终止于 R34）。只作卫生立项，不包装增益（收益上限约 +0.10 且存疑，在案）。

## §7 消化续轮（支线，不阻塞主链）

- 辨疑正文卷二三、预测学三至五七章、粹言未提约 154 叶、紫微续编（ZZ-M90 起）、穷通宝鉴评注 3 处挂起回页复核、CGM-01…35 并入八字章——均属知识完备动作；本轮产出只入 method-extraction/ 暂存并登记，**不并入活 method/**（保 §0 零改动冻结），是否并入由 R35 预注册裁决。

## §8 待用户项（只登记）

- 命理探源 1997 重印本印 114–270 续借（已降备核：仅余八卷原貌直证意义），只登记不催办。
