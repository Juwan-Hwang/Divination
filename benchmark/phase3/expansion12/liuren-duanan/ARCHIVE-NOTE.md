# 断案系 F 席草稿验盘入库存档（2026-10-30，本任主持角）

承 STAGE-SUMMARY-16 §三.1 与 HOST-RULINGS-2 §三：F 席断案系编码草稿原在工作区外 ~/da-scratch/，本件将其全量复制入 expansion12/liuren-duanan/scratch-archive/ 存档，并验盘如下。

## 验盘结果

- coding.md 两处 SHA-256 一致：`b9988ce422bbf39f6926b56b747925aeced8080eb95c218a545090206a51387e`（归档副本与 ~/da-scratch 原件逐字相同）。
- coding.md 编码 221 案（001–221）：**Y（A-low 合格候选）167、N 52、N?（待核全文）2**（006、191；另 156 例注记污染 high、221 例注记 A/污染 high、142 例 disputed 注记、027/130 疑伪托已编 N）。
- 原料文件同批存档：cases_raw.json（221 案全文，缘生谛校注版底本抽取）、meta.json（题名/课式头）、base.txt / narr.txt（底本与叙事文本）、toc.json / casepage.json（目录与页位）、mutual/（疏正/新编互校页图）、an.py / show.py（F 席脚本）。

## 入库口径

- 本归档中仅 coding.md 与本件入 git（F 席分析成果与主持验盘记录）；cases_raw.json、base.txt、narr.txt、mutual/ 页图等系现代校注本（redistributable=false）全文转录与页图，只存盘、不入 git，续抽席位在本机盘上取用。
- 续抽口径：以 coding.md 的 Y 为抽例范围（N? 两例先核全文定 Y/N），底本缘生谛校注版、三版互校定点补强；成例落盘格式与 expansion12 既有 cases.jsonl 同构（见 liuren-bianyi-yuce/cases.jsonl），编号 DA-001…与案号 n 对齐。
- 全池去重索引：expansion12/POOL-IDS.txt（masters-dataset 四分卷 data 目录清单＋inputs-dev10 全 487 id），各抽例/复核席三键去重时以此为 id 全集，对象/时间/事项核对回各源文件原文。
