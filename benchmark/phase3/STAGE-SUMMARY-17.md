# Phase 3 阶段小结 17（R33 任定稿，2026-10-30）

## 一、本任完成

1. **抽例开闸全数完成**（消化闸门已满足）：da-scratch 全量归档入 expansion12/liuren-duanan/scratch-archive/（coding.md 哈希验合）；断案系抽例 167 例（A 92＋B 75，可封存 162）；粹言慕农实 61 例头（更正 CENSUS 原称 35）、卷五对勘后净新 75（粹言可封存合计 119）；G 复核 126 例（seal 111）、H 复核 92 例（seal 18，QM 入池改编 QL 前缀）；主持更正（粹言计数）已追加 CENSUS.md 与 CENSUS-REPORT.md。
2. **holdout12 已建成并封存**（5fc4ac0）：49 例（六壬 27＝DA9/BY9/CY5/CYJ4、八字 13＝QL8/NL5、测字 CZ 8、六爻 HZ 1），单源最大 18.4%、非测字他源 41、全 A/A-low、全 low 污染；金标 SHA-256 490679552b5bcbff08df369046f977750900f7396857714a51aa438e16b30c90（SEALED.md、data/holdout12-seal-log.md、data/splits11.json）。资格准据链：HOST-RULINGS-3（测字路由补齐＋CZ 资格）、HOST-RULINGS-4（NL 改判 addendum 准据＋输入体例字样核准）。成色限度：粹言 9 例课式仅干支级，已登记于 SEALED。
3. **命理探原诸本核定（支线）**：四本存 incoming/mingli-tanyuan-editions/（SHA 清单在内）。定案：新校本与既持 #16 同版异扫、润德堂丛书本与 #16 正文同版，均无新增信息；存稿普查更正定稿（CENSUS-CUNGAO.md）——三系并集 47 则＋贱造附 1 全 B 级、成例供给终局阴性，断法 35 条登记（METHOD-EXTRACTION-cungao.md）；MT-011 误植定案（ERRATA-MT-011.md）；44 vs 42 之差收窄至壬五 1 则组属挂起。真本续借（印 114–270）降为备核、只登记不催办。
4. **R33 全程定稿**（75bb617，标签 phase3-round33-done）：预注册 e389254（消化后方法首读、判据事前声明不继承合读）；盲测 487 例 25 席全齐验数、双评审争议 0；平台 **(a) 立（−1.252）、(c) 立（六爻 dev8 单轮 −1.806 首过 −1.93 线）、(b) 仅八字 natal 未立（+0.173 vs +0.290）** → 平台不全立，**holdout12 保持封存未开封**。轮内缺陷 MP 撞号已定案处置（ADDENDUM-mp-collision：9 例重评替换，未纠正全集 −1.330 并列披露）。

## 二、R33 判读要点（供下任）

- 六爻 (c) 单轮过线是真信号候选：同口径下 R30 −1.632、R31/R32 −1.955、R33 −1.806，波动带约 ±0.16；是否与 R33 构成合读，须由 R34 预注册**事前**声明，不追认。
- 六壬两族同落（dev8 族 −1.847、LR3 族 −2.021、合并 −1.917，R32 合并 −1.100）：与六壬章消化增补同轮，性质未定（条文增密执行漂移 vs 席位方差），是 R34 第一诊断对象。
- natal 回落幅度（0.117，约 0.35 SE）不足以立结构假设；(b) 其余三项均立且有余量（horary −0.720 对线 −0.760 余量最薄，0.04）。
- 低污染子集 −1.765 仍显著深于全集，大师在低污染例上基线更高（4.891），验收口径的主战场不变。

## 三、续跑清单（下任按序）

1. **R34 预注册**：候选设计——(i) 六壬诊断：同 30 例六壬上以「指南核心条文版」与「增补全章版」两快照对照读数（诊断轮、不动平台判据），分族判读；(ii) natal 附读不单独设轮；(iii) 平台判据若沿用 §2 线值须在预注册重述，并事前声明 (c) 与 R33 的合读资格（inputs-dev10 不变、六爻方法血统自 R33 快照起算）；(iv) 平台全立才开封 holdout12（验 SHA 后按 R33 PREREG §3 执行）。
2. **数据卫生立项（与方法轮分离）**：① 建包器改显式源清单＋全树编号唯一性审计（禁 rglob 首命中）；② expansion12/natal-batch2 的 QM/MP 编号与 dev 池冲突，按 QL 改编先例重编并留映射（动此文件须同步其 cases-reviewed 与 expansion12 内引用）；③ inputs-dev11 口径切换（input-audit CORRECTIONS 6 例＋合读资格重置），收益上限约 +0.10 且存疑，只作卫生、不包装增益。
3. **消化续轮（支线）**：辨疑正文卷二三、预测学三至五七章、粹言未提约 154 叶、紫微续编（ZZ-M90 起）、穷通宝鉴评注 3 处挂起回页复核、CGM-01…35 并入八字章 references（知识完备动作）。
4. **待用户项（只登记）**：命理探源 1997 重印本印 114–270 续借（已降备核：仅余八卷原貌直证意义）。

## 四、提交与标签索引（本任）

- 检查点：98a2143（da-scratch 归档）→ 26ea9ad → 580d440 → b106bc3 → f2acf0c（裁定三）→ d08b7d3（存稿普查更正）→ 5fc4ac0（holdout12 封存）→ e389254（R33 预注册，标签 phase3-round33-prereg）→ a3cc690（盲测与建包）→ e0e0fc2/b6e611d（双评审与 MP 纠正）→ 75bb617（R33 定稿，标签 phase3-round33-done）。
- 本任关键文件：expansion12/{HOST-RULINGS-3.md, HOST-RULINGS-4.md, HOLDOUT12-BUILD-LOG.md, POOL-IDS.txt}、holdout12/SEALED.md、runs/round33/{PREREG.md, REPORT.md, ADDENDUM-mp-collision.md, ADDENDUM-isolation-disclosures.md, final-scores.json}。
