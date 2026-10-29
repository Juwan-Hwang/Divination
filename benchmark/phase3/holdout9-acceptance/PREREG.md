# holdout9 验收预注册（2026-10-30，平台成立后开封）

- 前提：R27 全池正式轮平台三判据全立（(a) 全集 −1.061 ≥ −1.371；(b) 护栏逐项未触发；(c) 六爻段 −1.845 ≥ −1.93），见 runs/round27/REPORT.md。H-R27 本身判未定、增补已回滚活 skill；本验收送验 artifact 为**产出平台证据的 R27 冻结快照**（runs/round27/kb-snapshot，含对立面裁决增补），口径解释见 R27 REPORT。
- 对象：holdout9 封存 28 例（expansion7 全新 A 级、全 low 污染：六壬 LR2-001–012 共 12、易隐 YY 8、卜筮全书 BQ 8），金标封存 SHA-256 be970fda5c4774bc11b45f855656efa2c5c1e9c8af2cb454804512413e8e61dc。开封前实测金标 SHA-256 与封存值逐字一致（2026-10-30 实测），并在 holdout9-seal-log.md 追加开封笔。
- 方法：R27 冻结快照（runs/round27/kb-snapshot/SKILL.md＋references/）。盲测只读各例 inputs（expansion7/{liuren,yiyin,bushi-quanshu}/inputs/<id>.json），方法自选/混用、不按来源指定主法，每例记 systems_used；盲测提示用冻结模板（runs/calib-r17/BLIND-PROMPT.txt 体例，路径按本验收替换）。
- 评审：混编匿名包 56 条（我方 28＋大师原断 28，大师侧以金标 master_predictions 的 statement_excerpt 拼接为 prediction_text；来源匿名、随机序），冻结量表（runs/calib-r17/JUDGE-PROMPT.txt 逐字）双评审＋分歧仲裁（分歧定义同各轮：|两席 claims+timing 差|≥2 或 pass 不一致），主持角持 host-key 解盲配对。
- 达标三判据（同前，且本集全 low，低污染子集＝全集 28 例）：(i) 全集我方均分＞大师；(ii) 低污染子集配对胜多于负；(iii) 低污染子集配对差为正且超噪声。三项全立 → 达标，以 R27 冻结快照为方法源打包 final-skill-v2（version 2.0.0）＋FINAL-REPORT-v2；任一不立 → holdout9 标已用、转诊断续链。
- 六壬终判附记：本集六壬 12 例为新鲜例，其配对差即六壬段终判读数（取代 dev 复用读数 −1.486 的上限口径），无论总判据成败均在验收 REPORT 中单列。

*主持角，2026-10-30*
