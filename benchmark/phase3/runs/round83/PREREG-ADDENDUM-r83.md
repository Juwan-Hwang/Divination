# PREREG-ADDENDUM-r83 —— holdout28 组集构成写定（存量内最后一集）

承主预注册 `runs/round83/PREREG.md` §4。存量口径以 `runs/round82/STOCK-RECOUNT-h27.md` 全口径复算与 `data/holdout27-seal-log.md` §一.1 取用后余量为准（组集席开工仍须盘上复算核对，落 runs/round83/STOCK-RECOUNT-h28.md）；本增补件写定构成、选例规则与递补链，组集席不得自改。**序首提示（承 R80 判例）**：下列存量数字已经主持开轮以 STOCK-RECOUNT-h27 与 holdout27 封存日志逐项对勘，组集席以盘上复算复核后为准，复算与本件不合者先回主持、不径自组集。

## 一、写定构成（T＝27，台账登记序选例，不按任何分数挑例）

| 来源 | 例数 | 入选 id（台账序） |
|---|---|---|
| 段建业《段氏理象学》DS | 13 | DS-050、DS-051、DS-052、DS-053、DS-054、DS-055、DS-056、DS-057、DS-058、DS-059、DS-060、DS-061、DS-062 |
| 刘文元《奇门启悟》QM 启悟 | 2 | QM-210、QM-211 |
| 奇门旧池（r56，杜新会/张志春两书） | 1 | QM-010 |
| 王虎应《六爻卦例说真》GSZ | 6 | GSZ-091、GSZ-092、GSZ-093、GSZ-098、GSZ-099、GSZ-100 |
| 王虎应《六爻分类占验技法》WHY（一轮台账序） | 5 | WHY-012、WHY-016、WHY-022、WHY-023、WHY-024 |
| 合计 | 27 | 非夷坚 27；非六爻 16 |

体系计数：bazi 13（48.1%）、qimen 3（11.1%）、liuyao 11（40.7%）、cezi 0。单源最大 DS 13（48.1%）≤50%（计数 ≤13）；单体系最大 bazi 13 ≤13。限度逐项：T＝27 ≥25；非夷坚 27 ≥13；非六爻 16 ≥13；仅锚点在场（资格断言见 §三）；与已用并集 1139 逐 id 零复用（写定名单已经主持开轮对勘：DS-050–062、QM-210、QM-211、QM-010、GSZ 六例、WHY 五例均不在 1139 并集内，组集席构建时以盘上复算再断言）。

## 二、递补链（逐段写定，触发时按序取用并逐件登记）

- DS 段：DS-063（仅 1 例）。DS 段递补竭后若仍缺额，跨段递补顺序为 GSZ 段→WHY 段（六爻面），但**非六爻计数不得低于 13**：DS 实成 <10 时（非六爻 <13）组集不成立，停建回主持登记（存量内组集失败定案），不得以六爻填充破非六爻下限。
- QM 段：无递补（启悟与旧池存量至此为全部）。QM 任一例资格断言不过时，先查同例可否以原文实据补正（锚点升格须原文实据，承 §4 锚点口径）；不可者该例退出、T 相应减 1 并登记，不得跨段以六爻或八字填充奇门段额（奇门段额非限度项，T≥25 与各限度仍须全合）。
- GSZ 段：GSZ-101、GSZ-103、GSZ-104、GSZ-105、GSZ-107、GSZ-108、GSZ-109、GSZ-110（台账序）。
- WHY 段：WHY-025、WHY-026、WHY-027、WHY-028、WHY-031、WHY-032、WHY-033、WHY-034（台账序，其后一轮余例顺延，再竭入二轮台账序 WHY-080 起）。
- 跨段总结：任何递补后仍须全限度复断言；T 最低 25。

## 三、资格断言口径（逐例，缺一不可，承历轮构建脚本读法）

- DS：台账 `runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json` 逐例 eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、master_assertion/outcome 逐字非空；入选例四柱（pillars_verbatim）互异、无同造重复（断言）。
- QM 启悟：台账 `runs/round76/digestion/SUPPLY-MINING-qiwu-r76.json` 逐例 anchor present、contamination low、separable＝true、断语/结局非空。
- QM-010（旧池）：台账 `runs/round56/digestion/SUPPLY-MINING-qimen-r56.json`＋复核件 `runs/round58/digestion/QM-REVIEW-r58.json` eligible_optional＝true、anchor present、pollution low、断语/结局非空。
- GSZ：台账 `runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json` 逐例 grade＝A、pollution＝low、anchor_presence＝present、eligible_net＝true、断语/结局非空，且属建卡口径名单（五要素复核通过集）成员；并逐例回原书文字层（`runs/round76/gsz-book-r76.txt`）以构建脚本同一 five_elements 函数复核锚点五要素全在场。
- WHY：台账 `runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json` 逐例属 counts 净入账名单（net_eligible_A_low_present）成员、pollution＝low、anchor_presence＝present、anchor_missing 为空、outcome_record 非空；断语台账未单列字段者（缺口整段）回原书逐字补录后封（体例承 holdout27 WHY 四例：回原书扫描本读图转录、transcription=visual 口径登记，页图件只许存 runs/round83/ 内、**不得提交入仓**——版权扫描件照 R82 why-pages 判例只留盘上未跟踪）。

## 四、封存体例（照 holdout27 定式）

- 输入卡字段白名单与剥离登记、节题/问题中性化核查、删除/改写清单逐字登记，体例承 holdout27 封存日志 §三。
- 三道断语扫描：第一道构建脚本内（逐字片段＋内容级标记集逐字承 R42 PREREG §5＋字段名黑名单＋禁用键集）；第二道封存席独立复扫脚本（不 import 构建脚本）＋逐卡语义通读；第三道主持独立复扫。逐道结果落封存日志。
- 金标：断语缺口先逐字补录后封；金标 SHA-256 构建双读＋主持第三读定版。
- 快照：封存时点自活 method/ 生成 runs/round83/kb-snapshot-holdout28（21 文件口径，排除 METHOD-*.md 登记件），与 runs/round83/kb-snapshot 之差异逐件登记（预期：奇门集成（若成立）文件集；无集成则零差异）；快照 calibration/SKILL 哈希与届时活 method 逐字对勘。
- 封存日志 data/holdout28-seal-log.md 须明记：**本集为存量内最后一集**、取用后余量逐项（预期 DS 1／QM 0／GSZ 建卡口径 8／WHY 52／非六爻合计 1）、其后组集系于 §5 expansion 工序产出或待用户书目；开封条件＝封存后首个平台全立轮（最早 R84）；若 R83-REV1 集成成立，本集为其判读集（判读口径以 method/METHOD-INTEGRATION-r83.md 写死为准，封存日志 §七逐字转录登记）。
- 验封：主持第三读＋第三道复扫＋构成与快照复核后追记封存日志，主持统一提交并打标签 `phase3-round83-holdout28-sealed`（组集席不做 git 操作）。

## 五、时序（写死）

组集封存于本轮奇门集成（若成立）落盘**之后**、第十节处置（若 §2 判读触发）**之前**。本轮不开封 holdout28。
