# natal-batch2 编号重编说明（R34 数据卫生 §6.②）

执行日期：2026-10-30。依据：`benchmark/phase3/runs/round34/PREREG.md` §6.②。

## 缘由

R33 评审建包时发现编号撞号并经定案（`runs/round34/audit-ids-report.json`、R33 ADDENDUM-mp-collision）：全树结局冲突仅 MP 一族——本目录 `cases.jsonl`／`cases-reviewed.jsonl` 的 MP 号（《袁氏命谱》命造）与 `expansion6/modern-cn` 的 MP-001…（现代案例，属 dev9 池）同号异例，曾致 R33 出现 9 例错配。本次重编把本目录的 MP 号整体改换为未占用前缀 PU，从源头消除撞号；同批《千里命稿》QM 号亦按 QL 改编先例重编，并与 holdout12 已封存使用的 QL 编号同号对齐，避免同一批案例两套编号并存。

## 改了什么

仅本目录两数据文件的 `id` 字段实改，其余字段逐字不动（逐行字节差异仅落在 id 值内、文件总字节数不变，校验见映射文件的 verification 记述与复验脚本）：

- QM-001…035（《千里命稿》）→ QL-001…035：其中 QL-001…008 与 holdout12 既用映射同号对齐（QM-005→QL-001、QM-007→QL-002、QM-010→QL-003、QM-020→QL-004、QM-023→QL-005、QM-027→QL-006、QM-029→QL-007、QM-031→QL-008），其余 27 例按原编号升序续编 QL-009…035。
- MP-001…057（《袁氏命谱》）→ PU-001…057，同号对应。注：预注册 §6.② 写 MP-001…056，盘上实有 57 例（本目录 CENSUS-NOTES.md 记「57 例（MP-001…MP-057）」，两文件总记录 92＝57＋35），MP-057（端方）同属《袁氏命谱》，一并同号重编为 PU-057，未留旧前缀残号；此出入已登记于映射文件 anomalies，主持如有异裁仅此一例可按映射回退。

两文件改前／改后 SHA-256、旧→新全表（QM→QL 35 条、MP→PU 57 条）见同目录映射文件 **`RENUMBER-MAP.json`**；执行脚本 `renumber_nb2_r34.py`、独立复验脚本 `verify_renumber_nb2_r34.py` 同目录在案。

## 查阅口径（证据只增不删，旧文不回改）

- **holdout12 金标与 SEALED.md 保持原文**：`benchmark/phase3/holdout12/test_gold.jsonl` 中 QL-001…008 行的 `source_id` 仍为原文 QM 号（QM-005 等），`holdout12/SEALED.md` 的 QL 改编映射记述亦不改动；经 `RENUMBER-MAP.json` 的 QM→QL 表可逐条解回本目录新号。
- **expansion12 其余文档内的旧号引用不回改原文**：本目录 `REVIEW-H.md`、`CENSUS-NOTES.md`、`METHOD-EXTRACTION.md` 及上级 `HOLDOUT12-BUILD-LOG.md`、`POOL-IDS.txt` 等文档中出现的 QM-／MP- 号均为重编前原文，查阅时一律以 `RENUMBER-MAP.json` 映射为准换算为 QL-／PU- 新号。
- 本目录两数据文件内部的自由文本互引同理：`cases-reviewed.jsonl` 中原 QM-008（现 QL-014）与原 QM-023（现 QL-005）两例 `review.notes` 内各有一处对对方的旧号互引（同姓不同人辨异注记），按「只改 id 字段」口径未动原文，以映射换算。
