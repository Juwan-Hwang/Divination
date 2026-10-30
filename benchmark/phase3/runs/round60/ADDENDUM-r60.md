# ADDENDUM-r60（R60 主持附记，随开轮落盘）

## 一、股票章六神列锚点口径疑点——主持裁定（承 ADDENDUM-r59 §四提请）

- **疑点原文**（runs/round59/digestion/build_recheck_r59.py 内 `anchor_standard_note`）：台账 rules 所列锚点五要素（卦名、动爻、世应、六亲纳支、月建日辰）不含六神，但 WHY 一轮对股票章（王虎应《六爻卦例说真》股票占章）16 例以「六神列未辨出」判 partial；复核席读图实测股票章卦盘版式本就未印六神列（非扫描辨认问题），且同章被判 present 的 WHY-045–049、052 卦盘同样未印六神列——原判 present/partial 划分与六神列可见性并不一一对应。
- **主持裁定**：锚点在场口径以**五要素（卦名、动爻、世应、六亲纳支、月建日辰）为唯一标准，六神列不属锚点要件**。理由三条：① 台账 rules 定义本就不含六神，以定义外要件判 partial 属口径执行越界；② 六神配卦由占日日干机械决定（青龙起例），日辰已在五要素之内，六神属可推导信息而非缺载锚点，缺印不构成锚点缺载；③ 同章 present 例同样未印六神列，原划分与六神可见性不对应，维持旧判将使同版式两判并存。
- **效力与边界**：自 R60 起**前瞻适用**于一切后续开采与复核；**不追溯已判例**——股票章 16 例本轮不逐例改判（其污染 mid 阻断独立成立，改判对可选集增量为零，承复核件自记）；WHY-001/002（变卦爻列缺）、WHY-029（动爻缺）属五要素内缺项，与本裁定无关、维持 partial。此后任何席位不得再以六神列缺印判锚点 partial；五要素内任一缺项仍照旧判 partial、升 present 须原文实据。

## 二、开轮核验登记（主持盘上实测）

- **holdout21 金标**：`holdout21/test_gold.jsonl` 独立 sha256sum 实测＝ea4d9315bfffd2f02fc7aed8f9e6a2ac04924bfa89d4545e08830287e447fb72，与封存日志定版值全文一致；输入卡 25 张在盘实测。
- **批次**：runs/round60/batches.json 与 round59 件 SHA 全等（006c4905195ab997874d5c90961c635eedda755f5151c31dd55b7da094251e5e）。
- **平台快照**：runs/round60/kb-snapshot 自现行活 method/ 生成（21 文件）；与 round59 快照逐文件 diff 仅 SKILL.md、references/calibration.md 两件不同（恰为 REV1 集成面），余 19 件全等——R60 平台为 REV1 接入后新系列第 1 点的事实基础在案。
- **冻结提示**：runs/round60/prompts/BLIND-PROMPT-verbatim.txt、JUDGE-PROMPT-verbatim.txt 与 runs/calib-r17/ 原件 diff 全等。
- **manifest**：runs/round60/build_manifest_r60.py 断言全过（487 例载荷逐字承接、层 A 14/14 交叉验合、层 B counts 与 R59 REPORT §四断言全等），产物 SHA-256＝c175fa0ab334a4127d7c80ddce6d98c9ed04c1653919c3a93e5c5e7e8478299b。
- **到货核查**：incoming 无新到货。wanted-books-4 五件（王虎应《六爻卦例说真》《六爻分类占验技法》、张志春《神奇之门》、杜新会《奇门遁甲现代实例精解》、曲炜《详批命例精解》）已于 R56–R58 开采毕；~/workspace/user/files/ 中 2026-10-30 19:02 的四个 Book.7z 分卷（.001–.004）即该包分卷、已由主会话拼合归档为 incoming/wanted-books-4/Book.7z，非本轮新到货。第四批第 2/6/8 条仍未到，只登记（PREREG §8）。
