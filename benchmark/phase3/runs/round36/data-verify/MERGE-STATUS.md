# R36 库存合并状态表（§7(iii) 数据角产出）

- 任务：逐件核查 expansion12 暂存件与 method-extraction 旧批四组对现行活 method（`benchmark/phase3/method/references/`）的合并状态。本表只核查登记，不作断、不评分、不改 method、不裁决并入与否（裁决归主持角 STAGING-RULINGS）。
- 核查方法：① 编号全量对照——脚本 `runs/round36/data-verify/merge_check_r36_data.py` 抽取各暂存件全部条目编号，在活章 references 全部文件内逐号检索，结果存 `runs/round36/data-verify/merge-check-r36-output.txt`；② 段长比对——活章各「增补编」段行数与暂存件行数逐段核对（各段均＝暂存件全文＋约 6 行增补编题头，系主持角逐字并入形态）；③ 抽样条目逐条定位（每件 ≥3 条，下列行号均为活章文件行号）。
- 总体事实：expansion12 各件已于 2026-10-30「第二批消化」由主持角逐字并入活章增补编（各增补编题头原文均载此语）；method-extraction 旧批四组已于断法提炼批次（R28 前入账，EXTRACTION-REPORT 登记）合并。故各件结论多为「已并入」，差异只在**入章层级**（正文／增补编／候选层／附编登记层／索引层）与个别附属文件的未入部分，逐件注记如下。

---

## 1. expansion12/liuren-duanan/METHOD-EXTRACTION.md（《大六壬断案》系）

- 条目总数：**27 条**（DA-M01–M27）
- 结论：**已并入**
- 证据（活章＝`chinese-liuren.md`，增补编·甲，题头在 :439，段 :439–657，暂存件 213 行）：
  - DA-M01 取用纠正（弹射）→ `chinese-liuren.md:462`
  - DA-M02 同课异断 → `chinese-liuren.md:466`
  - DA-M14 占官：须见官星 → `chinese-liuren.md:534`
  - DA-M27 → `chinese-liuren.md:609`（全量对照 27/27 命中，缺号 0）
- 未并入部分：条目无未并入者。暂存件卷首「互校定点结论／覆盖限度」等说明文字亦随全文一并入段（段内可见）；疏正评疏全帙、详解其余按语、新编《直指析义》本非本件提炼范围，暂存件原文已自记「不在本席任务范围」，不属未并入条目。

## 2. expansion12/liuren-bianyi-yuce/METHOD-EXTRACTION.md（《六壬辨疑·毕法案录》＋《大六壬预测学》）

- 条目总数：**234 条＋对照长表 1 组**（辨疑 127 条＝毕法正文 100 法全录〔无 G 编号、序号列表〕＋纲领 G-BY-M1–M5＋抽读 G-BY-S/K/L/T 共 19 条＋另 3 条抽读，总数以暂存件 §五复核注为准；预测学 G-YX-H/T/C/D 共 107 条＋病症对照长表 1 组）
- 结论：**已并入**
- 证据（活章＝`chinese-liuren.md`，增补编·乙，题头在 :658，段 :658–916，暂存件 253 行）：
  - 毕法一百法序号全录 → `chinese-liuren.md:678`（「1. 前后引从，升迁吉。…100. 已灾凶逃，返无疑。」整段在段内）
  - G-BY-M1 条例纲领 → `chinese-liuren.md:684`；G-BY-S7 三刑定向 → 段内 S 组（全量对照 G-BY 编号 24/24 命中）
  - G-YX-T12 → `chinese-liuren.md:789`；G-YX-D7 → `chinese-liuren.md:880`（全量对照 G-YX 编号 107/107 命中）
- 未并入部分：条目无未并入者。注意同源注记（暂存件 §四、段内同载）：辨疑毕法与现章《六壬大全》系同源、预测学例源含粹言／指南系，分族判读口径随文入段，非未并入事项。

## 3. expansion12/liuren-cuiyan/METHOD-EXTRACTION.md（《六壬粹言》）

- 条目总数：**26 条**（CX-M01–M26；另冲突并列登记 C1–C4）
- 结论：**已并入**
- 证据（活章＝`chinese-liuren.md`，增补编·丙，题头在 :917，段 :917–1091〔章末〕，暂存件 173 行）：
  - CX-M01 月将以中气为准 → `chinese-liuren.md:932`
  - CX-M14 五虎格 → `chinese-liuren.md:988`
  - CX-M26 疾病·死煞乘鬼断死例式 → `chinese-liuren.md:1044`（全量对照 26/26 命中）
- 未并入部分：条目无未并入者。族别注记随文入段：本件全条归「指南族」，只作同族完备细化、不作独立新源（暂存件 §一原文，段内 :926 一带同载）。粹言未提约 154 叶系**原书未提炼**（PREREG §8 支线），非本件未并入。

## 4. expansion12/natal-batch2/METHOD-EXTRACTION.md（《千里命稿》＋《袁氏命谱》）

- 条目总数：**97 条**（千里 QM-M01–M73 共 73 条，条目在暂存件与活章中均以行首简号 M01–M73 行文、QM-M 为其全称；命谱 MP-P01–P24 共 24 条）
- 结论：**已并入**
- 证据（活章＝`chinese-bazi-ziwei.md`，增补编·乙，题头在 :818，段 :818–1027，暂存件 204 行）：
  - M01 推年法（QM-M01）→ `chinese-bazi-ziwei.md:835`
  - M37 外格逐格「构成＋用神」（QM-M37）→ `chinese-bazi-ziwei.md:879`
  - M72「精神饱满」判读（QM-M72）→ `chinese-bazi-ziwei.md:923`；M73 → :924
  - MP-P04 论命纲领：中和 → `chinese-bazi-ziwei.md:940`；MP-P12 化气格读法 → :958；MP-P24 → :980（MP-P 编号全量对照 24/24 命中）
- 未并入部分：条目无未并入者。暂存件自记限度（查表型内容以结构＋代表条登记、未逐字复录全表）系**提炼限度**、非合并缺失，随文入段。

## 5. expansion12/mingli-tanyuan-zhenben/METHOD-EXTRACTION.md（《新命理探原》甲本，XMT 系）

- 条目总数：**79 条**（XMT-01–79；含版本／体例登记条 6 条、纯议论存档条 3 条，暂存件文末自记）
- 结论：**已并入**
- 证据（活章＝`chinese-bazi-ziwei.md`，增补编·丙，题头在 :1028，段 :1028–1522〔章末〕，暂存件 493 行）：
  - XMT-02 纳音生成数 → `chinese-bazi-ziwei.md:1052` 一带（XMT-01 首见于题头 :1028）
  - XMT-35 → `chinese-bazi-ziwei.md:1234`
  - XMT-79 朱文公赠徐端叔命序 → `chinese-bazi-ziwei.md:1479`（全量对照 79/79 命中）
- 未并入部分：本件条目无未并入者（版本／议论类登记条亦照原样入段）。范围声明：同目
...[truncated 5829 chars]