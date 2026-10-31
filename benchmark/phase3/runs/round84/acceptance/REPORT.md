# R84 验收报告（holdout28 开封验收）

主持：R84 主持角。开封时点：R84 平台三项全立（全立计 31）后当轮开封，照 PREREG.md 写定。本件为验收定稿汇总；逐件证据见本目录 OPENING.md、final-scores-h28.json、DIAG-H28.md、JUDGMENT-R83-REV1-r84.md 与封存日志 §十（benchmark/phase3/data/holdout28-seal-log.md）。

## 一、开封前置复验（三项全过）

1. 金标 SHA-256 再测 e985d5d1552a8583e22297e4e9ee08cc47c3fb797056ec1f8819489d481e3675（42,736 字节、27 行），与封存定版全等；
2. 输入卡 27 张在盘（benchmark/phase3/holdout28/inputs/，金标在 holdout28/test_gold.jsonl）；
3. 主持开封复扫（host_opening_scan_h28_r84.py）零命中，预测在开封后方生成。复验追记封存日志 §十。

## 二、验收定稿（未达标）

- 我方均分 **2.685** vs 大师均分 **4.491**；配对差 **−1.806**（SE 0.378，n＝27）；W/T/L **3／3／21**。
- 三判据（R42 PREREG §8）全不立：(i) 我方均分＞大师均分——不立；(ii) 低污染子集配对胜多于负——不立；(iii) 低污染子集配对差＞0——不立。
- holdout28 标已用；holdout2–holdout28 全部开封用毕。**不打包 final-skill-v2**，链条续行（见 STAGE-SUMMARY-69）。
- 双视分歧 0 件（我方 max |Δ| 1.0、大师 max |Δ| 1.5），无仲裁。
- 分段配对差：bazi_DS −1.962（2/0/11）、qimen_QM −2.333（0/0/3，n 小仅附读）、liuyao_GSZ −1.167（1/1/4）、liuyao_WHY −1.850（0/2/3）；non_liuyao 合计 −2.031。

## 三、诊断（DIAG-H28）

- 27 例主码全 E5（席位判断）；子类 DIR 7／CLAIM 10／TIM 6（全实质）／OMIT 4；次码 E4 4 例。
- 构成面清白连续：IN＝0/27（输入构成缺载零例）——败因不在输入构成，在判断本身，与 h22 以来共识一致。

## 四、R83-REV1 判读（JUDGMENT-R83-REV1-r84.md）

- 结论三态之 ② **未达未证伪**：段 DIR 主码 1≤1 达（恰压线）、TIM 主码 1≤1 达（恰压线）、护栏甲 OMIT 0 守、乙 CLAIM 1 守（恰压线）、丁执行面四行留痕 3/3 例 12/12 行守；**护栏丙全集总差 −1.806 破线（线 ≥−1.722，差 0.084）为落 ② 唯一原因**。证伪三线全未触。
- 处置：第十一节标失效存档、SKILL (s) 指针照未达体例保留（先例 R82 处置第九节 (q)），由处置席执行、登记件 method/METHOD-DISPOSAL-r83rev1-r84.md。处置后现行干预仅第八节（唯一判读成立现行节）。

## 五、平台侧（同轮）

平台三项全立、全立计 31：(a) −1.084、(b) 四护栏全立、(c) −1.821（熔断线 −2.255 未触）；归因护栏：八字全集 0.078（BZ-FY 证伪 False）、六壬合并 −1.650（继续恶化 False）。详见 runs/round84/REPORT.md 与 final-scores.json。
