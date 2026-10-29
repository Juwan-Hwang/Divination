任务：担任 MastersDivination Benchmark Phase 2 的数据角（只做数据，不作断、不评分、不改方法）。工作区 ~/workspace/divination/。

产出（全部落盘 benchmark/phase2/ 下）：
1. data/roster.jsonl（105 行）：取双轴分级表 benchmark/dual-axis/grading/outcome-availability.jsonl 中 grade=A 的全部 105 例。逐例字段：id、tradition（从 masters-dataset/data/dev.jsonl 与 masters-dataset/holdout/test_gold.jsonl 的完整记录取）、phase1_split（dev/test）、outcome_record（照抄分级表）、contamination（high/low）+ contamination_reason（一句话）。污染判定口径：结局属著名历史事件、名人结局或广为人知的现代事件（大概率在模型训练知识内）→ high；冷门案例的局部结局、或现代带时间戳预测所涉非著名事件 → low；拿不准从严标 high。判定依据只许看 subject/context/outcome_record 的公开事实属性，不许参考任何预测或分数。
2. inputs/<id>.json（105 个）：盲测用 inputs，逐字取自 benchmark/runs/round17/inputs/ 与 benchmark/runs/round18/inputs/ 中同名文件（已验证为盲安全版本：只有 subject/context，不含大师断语与结局）。逐个核对文件内不出现 master_predictions/outcome 字段，核对记录写进 data/input-check.txt。
3. splits2.json：dev2/holdout2 划分。算法（严格执行）：在每个 tradition × contamination 分层内，按 sha256("phase2-20261029:"+id) 的十六进制串升序排序，每 10 例取排序后第 3、6、9 位（即约 30%）入 holdout2，其余入 dev2；分层内不足 3 例的分层全入 dev2。写完后统计各分层与总计 n（目标 holdout2 约 28–34 例），写入 data/splits2-summary.md，含算法复述与逐分层计数。划分一经落盘即冻结，你不得再改。
4. data/master-baseline-dev2-packet.json：dev2 全部案例的大师基线评审包：逐例 {anon_id（用 DB-001…顺序号，与案例 id 的映射只存 data/master-baseline-mapping.json，主持留存）、master_statements（完整记录里 master_predictions 的 statement_excerpt 全文拼接，注明大师与体系）、outcome_record}。此包供评审角给大师断语打轴二分，包内不得出现我方任何预测。

纪律：只许读分级表、完整记录与既有 inputs；不许打开任何 predictions/final-scores 文件；不许改 splits.json 等 Phase 1 文件。交付回传：roster 行数校验、污染 high/low 计数、splits2 各分层计数、inputs 核对结论、基线包例数。
