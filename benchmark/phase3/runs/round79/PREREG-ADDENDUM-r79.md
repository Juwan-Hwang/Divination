# PREREG-ADDENDUM-r79（holdout24 组集封存写定，R79 主持）

本件为 holdout24 组集封存的唯一授权文本（承 PREREG §4）。体例承 PREREG-ADDENDUM-r78（holdout23 组集）与 data/holdout22-seal-log.md、data/holdout23-seal-log.md。组集封存席只建卡与封存：不作断、不评分、不开封验收、不做 git 操作（提交与标签由主持执行）。**本集为 R78-REV1 判读集**（PREREG §2 写死）：封存快照锚定封存时点活 method（含 calibration 第七节），开封条件为封存后首个平台全立轮（最早 R80），判读随其开封验收之同口径诊断执行、口径照 PREREG §2 写死值，本件不另改写。

## §一 构成写定（T＝27）

| 来源 | 例数 | 台账（绝对路径） |
|---|---|---|
| 段建业《段氏理象学》(DS) | 6 | /home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json |
| 张志春《开悟之门》(QM 开悟） | 5 | /home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-kaiwu-r76.json |
| 刘文元《奇门启悟》(QM 启悟） | 2 | /home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-qiwu-r76.json |
| 石建国《奇门遁甲最新实例解析》(QM 石建国） | 3 | /home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-shijianguo-r76.json |
| 《字触补》（四库未收书辑刊陆辑拾捌册）(ZCB) | 5 | /home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json |
| 王虎应《六爻卦例说真》(GSZ) | 6 | /home/hatch/workspace/divination/benchmark/phase3/runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json（原书文字层：runs/round76/gsz-book-r76.txt） |
| 合计 | 27 | 非夷坚 27、非六爻 21 |

体系构成：八字 6（22.2%）、奇门 10（37.0%）、测字 5（18.5%）、六爻 6（22.2%）。
构成限度逐项（封存席逐项断言、主持复核）：总量 T＝27 ≥25；单体系 ≤50%（最大奇门 37.0%）；单源 ≤50%（最大 DS／GSZ 各 6/27＝22.2%）；非夷坚 ≥13（27）；非六爻 ≥13（21）；仅锚点在场例入选（§二资格断言）；与已用并集逐 id 零复用（§二）。
构成登记（只登记、不作选例依据）：构成与 holdout23 同型（六源并存、奇门三源并存），ZCB 定额自 6 降至 5（present∧low 存量扣减 holdout23 取例后之台账实算为准，见 §二.5）、GSZ 自 5 增至 6 相应补足。选例一律按 §二规则，**不按题材、分数或任何验收结果挑例**——奇门段有害信号所涉题材（病占、婚/胎产等）不作入选或剔除依据。

## §二 选例规则与资格断言（逐例，缺一不可、不过即换）

通用顺序：各源先按本节资格滤＋已用并集逐 id 滤，再按**台账登记序**取足本源定额；任一例资格断言不过 → 按登记序换下一例（换例逐件登记于封存日志）；定额内换尽仍不足 → 按下列跨源递补规则处理，规则外不足立即停建并报主持裁处（不得擅自跨源递补）。**跨源递补规则（本轮写定）**：① ZCB 定额不足 → 差额由 GSZ 按登记序递补（GSZ 定额相应增加，逐件登记）；② GSZ 定额（含递补增额）不足 → 差额由 QM 开悟全合余例递补（逐件登记）；③ DS／QM 任一源不足 → 停建报主持裁处，不自动递补。递补后构成限度复断言（单源 ≤50% 等逐项重算并登记）。

1. **已用并集（逐 id，盘上实算）**：dev 池 id＝data/master-baseline-dev9.json 键集 ∪ inputs-dev9/10/11/12 与 inputs 目录卡 id；holdout 侧＝holdout2–23 各 test_gold.jsonl 的 id 字段 ∪ 各集 inputs/ 目录卡 id。并集去重，选例逐 id 对此并集零命中。只取 id 字段建集，不得打开已封存集金标正文做内容比对。并集实算规模与逐源计数写入构建报告（开轮主持附读实算 1031 id，构建时复算为准）。**同名即剔**：台账 id 与并集任一 id 同名者，无论内容相涉与否，剔除递补并登记（holdout22 DS 撞号教训）。
2. **DS**：台账逐例 eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、master_assertion/outcome 逐字非空；DS-047（medium）排除；**同造合并组至多取 1**（承 holdout22 §一.1 核验口径，合并组构成以台账登记为准、逐组登记；holdout23 已取之合并组唯一卡所在组别本轮同组他卡仍受「至多取 1」之限——以台账合并组登记为准逐组核）。
3. **QM 开悟**：台账逐例 anchor_status＝present、contamination_pre＝low、separable＝true、stem_check 天盘与地盘**双 ok（全合）**、断语/结局非空。未全合者本轮不入选（不做建卡精核升格）。
4. **QM 启悟／石建国**：台账逐例 anchor_status＝present、contamination_pre＝low、separable＝true、断语/结局非空。石建国例若入选例含台账已登记之转录疑字注记（如 QM-308 型），逐例在封存日志单列注记。
5. **ZCB**：台账逐例 eligible＝true、anchor_status＝present、contamination_pre＝low、separable＝true、断语/结局非空；mid 例不取；**ZCB-003 维持排除**（承 PREREG §4 主持裁处：holdout22 裁处未撤销、本轮不入选，登记序跳过并登记）。已用 ZCB id 以 holdout22／holdout23 test_gold.jsonl 盘上实读为准（封存日志与诊断件编号出入时以金标文件为准、差异登记）。ZCB 合格存量盘上复算计数写入构建报告（与 STAGE-SUMMARY-63 §4「present∧low 余 5」口径之出入逐项登记、以盘上复算为准）。
6. **GSZ**：台账逐例 grade＝A、pollution＝low、anchor_presence＝present、eligible_net＝true、断语/结局非空，且属可选未用池成员；并逐例回原书文字层（runs/round76/gsz-book-r76.txt）复核锚点五要素（卦名、动爻、世应、六亲纳支、月建日辰）全在场，缺一即换下一例（holdout22 GSZ-020 换例先例）。

## §三 建卡与金标规格（输入侧卫生，承 holdout22/23 体例）

- 输入卡字段白名单：{id, tradition, subject, context, question, setting, provenance, anchors}＋{redistributable, license_status}（以 holdout23 卡实读字段集为准，封存席开工先回读 holdout23 任一卡字段集对齐后写定）。构建脚本以禁用键集对全部输入卡全字段递归扫描，管理/断语/结局/判级/污染字段零残留断言；落盘后复扫亦零。
- input_side 一律取台账 input_side 逐字；台账无 context/question 字段者按 holdout22/23 组写口径组写并逐例登记于构建报告。provenance 全卡含「用户经学校图书馆提供」口径（六爻例照其台账 source 逐字承接），redistributable 全 false。
- **泄题处置**：输入卡题面/节题/篇名若含结局事实或内容级断语字样，封存席不得自改——逐件列单报主持裁处；主持裁处（中性化改写或附条件删除）后入卡，金标与台账不动，裁处全文入封存日志（holdout22 DS-011／QM-301／ZCB-004、holdout23 DS-013/014/015 先例）。书目信息性字样（篇名含一级标记字）承 holdout22 处置口径：卡面略去、金标 provenance 载全，逐例登记。
- 金标：test_gold.jsonl 逐例载台账 gold_side 之 master_assertion 与 outcome **逐字原文**；断语仅要旨/有缺口者，封存席回原书逐字补录后入标（补录逐例登记：原台账文本与补录后文本并列），无补录不得封存。金标 SHA-256 以构建脚本 hashlib 输出与脚本外独立 sha256sum 实测**双读一致**为定版候选，主持再以独立 sha256sum 第三读复核一致后方为封存定版（写入封存日志并标注三读）。

## §四 三道断语扫描与快照锚定

- 内容级断语扫描（标记集承 runs/round42/PREREG.md §5）三道：① 构建脚本内扫描断言；② 封存席落盘后独立复扫（独立脚本、唯一名）；③ 主持封存复验时复扫。三道均对全部输入卡执行、命中逐件处置登记，零命中方合封存。开封轮主持复扫留位照 ADDENDUM-r77 §三办理（结论追记本日志、不另立新档）。
- 快照锚定：封存时点自现行活 method/ 生成 runs/round79/kb-snapshot-holdout24（21 文件）＋SHA-256 清单；封存时点活 method 含 calibration 第七节（R78-REV1），快照即封存时点方法、与 runs/round79/kb-snapshot 逐件比对登记（预期全等，差异逐件登记）。验收盲测读此快照原件。
- 封存日志：data/holdout24-seal-log.md，体例承 holdout23 封存日志（构成表、零复用核算、资格断言逐例、剥离登记、裁处登记、扫描结论、金标 SHA 三读、开封条件重述）。
- 产物路径：holdout24/inputs/ 输入卡、holdout24/test_gold.jsonl 金标、构建脚本与构建报告置 runs/round79/（唯一名）。
