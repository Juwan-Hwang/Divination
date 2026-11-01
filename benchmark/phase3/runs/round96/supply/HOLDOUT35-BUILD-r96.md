# HOLDOUT35-BUILD-r96 — holdout35 封存建卡报告（R96 建卡席）

- 席位：R96 holdout35 封存建卡席（独立封存角，不兼任盲测/评审/诊断/数据/修订/供给）。
- 产出：`benchmark/phase3/holdout35/`（inputs 28 卡＋test_gold.jsonl 28 行＋kb-snapshot 21 件＋kb-snapshot-sha256.txt 21 行）。
- 构建脚本：`benchmark/phase3/runs/round96/build_h35_r96.py`（本轮唯一名；中间件同目录：`holdout35-build-frag-r96.json`、页图 `h35-by-pages-r96/`、裁切 `h35-by-crops-r96/`、盘图回读 `h35-xzs-pages-r96/`）。未用 /tmp；未做 git；脚本无通配删除。
- 体例：卡字段白名单恰为 id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors（28/28 键序断言全过）；金标字段序承 h34 §六：id, master_prediction, outcome_record, tradition, pollution, grade, grade_note, provenance, license_status, redistributable（28/28）。卡内不含结局/大师断语原文（脚本断言 outcome 全文不入卡＋12 字分片泄漏粗扫 0 命中）。

## 一、构成与 id 集断言（全过）

- T＝28＝紫微 14＋六壬 14（DA 7＋BY 7），与主持定版逐 id 全等：
  - 紫微：ZW-024、ZW-025、ZW-026、ZW-027、ZW-033、ZW-034、ZW-035（reserve）；ZW-036（＝CM-11）、ZW-037（＝CM-12）、ZW-038（＝CM-13）、ZW-039（＝CM-18）、ZW-044（＝CM-73）（蔡明宏批）；ZW-045（＝ZJ-10）、ZW-046（＝ZJ-11）（《正解》解锁批）。
  - 六壬 DA：《大六壬断案》DA-082、DA-083、DA-085、DA-086、DA-087、DA-088、DA-090。
  - 六壬 BY：《六壬辨疑·毕法案录》BY-054、BY-055、BY-056、BY-057、BY-058、BY-060、BY-061。
- 零复用断言：28 id 对 `runs/round96/used-ids-r96.json`（1333 件、互异 1333）逐 id 对撞，交集为空（脚本硬断言通过）。
- 台账续位复算断言：`runs/round85/lr-eligible-ledger-r85.json` 自 DA-081／BY-053 后按登记序续取、跳过已用，得 DA 7／BY 7 与定版逐 id 全等（DA-084、BY-059 等不在台账列内，自然跳过；台账序≠连续段，逐 id 列明如上）。
- 排除对 LY-015／LY-320：28/28 零命中。
- 限度复核：单体系紫微 14/28＝50%、六壬 14/28＝50%（均 ≤50%）；单源最大 DA、BY 各 7/28＝25%；非夷坚 28；非六爻 28；pollution＝low 28/28；redistributable＝false 28/28；grade A-low 28/28。

## 二、逐例来源与资格断言

资格通则：六壬池卡 holdout_eligible=true、contamination=low、outcome_grade=A-low、master_predictions 与 outcome 非空（脚本逐例硬断言全过）；BY 另 review.verdict=seal、grade_final=A-low、contamination_final=low（以台账/池件为准，断言全过）。紫微逐例登记件载 A-low／low／redistributable=false、锚点在场。

| id | 来源件与页/条目 | 资格与锚点 |
|---|---|---|
| DA-082 | expansion12/liuren-duanan/scratch-archive/cases_raw.json n=82；池卡 cases-a/b.jsonl | eligible/low/A-low；课盘三件（方阵/四课格/三传栏）程序化转录断言在场 |
| DA-083 | cases_raw.json n=83 | 同上 |
| DA-085 | cases_raw.json n=85 | 同上 |
| DA-086 | cases_raw.json n=86 | 同上 |
| DA-087 | cases_raw.json n=87（池卡 subject「毛主簿」、底本作「毛主薄」，卡面从池卡） | 同上 |
| DA-088 | cases_raw.json n=88 | 同上 |
| DA-090 | cases_raw.json n=90 | 同上 |
| BY-054 | 原书页图 PDF p197（书p185）课例六十五；池件 cases-reviewed.jsonl | eligible/low/A-low、review seal；课盘三件读图通读＋裁切放大复核 |
| BY-055 | PDF pp197–198（书pp185–186）课例六十六 | 同上 |
| BY-056 | PDF p198（书p186）课例六十七 | 同上 |
| BY-057 | PDF p200（书p188）课例七十 | 同上 |
| BY-058 | PDF pp200–201（书pp188–189）课例七十一 | 同上 |
| BY-060 | PDF p202（书p190）课例七十四 | 同上 |
| BY-061 | PDF pp202–203（书pp190–191）课例七十五 | 同上 |
| ZW-024 | runs/round93/supply/ZIWEI-REVIEW-XZS7-r93.md §三.4（XZS-14）；BATCH2-XZS XZS-14 条；DIGEST-5 D5-29-16；本席回原书页图 PDF151 | 复评通过 A-low/low；盘图回读 |
| ZW-025 | REVIEW-XZS7 §三.5（XZS-17）；DIGEST-5 D5-29-21；原书页图 PDF156 | 复评通过 A-low/low；H-1 盘图回读（命宫申、紫微未） |
| ZW-026 | REVIEW-XZS7 §三.6（XZS-19）；DIGEST-5 D5-30-08；原书页图 PDF162 | 复评通过 A-low/low；图三盘宫干校验读定（命宫午、紫微卯） |
| ZW-027 | REVIEW-XZS7 §三.7（XZS-25）；DIGEST-5 附项/D5-32-13；原书页图 PDF176–177 | 复评通过 A-low/low；300dpi 附项复核；联系栏不转录 |
| ZW-033 | ZIWEI-SUPPLY-BATCH3-ZJ-r93.md ZJ-07 条；BATCH3-SUMMARY §三续编 ZJ-07→ZW-033 | 四滤全过 A-low/low；全盘锚点（登记件裁剪复核） |
| ZW-034 | BATCH3-ZJ ZJ-08 条；SUMMARY 续编 ZJ-08→ZW-034 | 同上 |
| ZW-035 | BATCH3-ZJ ZJ-09 条；SUMMARY 续编 ZJ-09→ZW-035 | 同上 |
| ZW-036 | ZIWEI-SUPPLY-BATCH5-CM-r96.md CM-11 行（定版 PDF p189）；rate-chunk-3-r96.md CM-11 节逐字转录；SUMMARY-r96 编号 CM-11→ZW-036 | 四滤全过 A-low/low；局部锚点（标字5格、4星，逐例标明、空白宫不补）；无特殊注 |
| ZW-037 | BATCH5 CM-12 行（PDF p201）；rate-chunk-3 CM-12 节；CM-12→ZW-037 | 局部锚点（标字4格、4星） |
| ZW-038 | BATCH5 CM-13 行（PDF p202上）；rate-chunk-3 CM-13 节；CM-13→ZW-038 | 局部锚点（标字4格、4星） |
| ZW-039 | BATCH5 CM-18 行（PDF p223）；rate-chunk-4-r96.md CM-18 节；CM-18→ZW-039 | 局部锚点（标字3格） |
| ZW-044 | BATCH5 CM-73 行（PDF pp535–540）；rate-chunk-15-r96.md CM-73 节逐字转录；CM-73→ZW-044 | 全盘锚点（十二宫齐备） |
| ZW-045 | BATCH3-ZJ ZJ-10 条；ZIWEI-SUPPLY-BATCH6-ZJ-UNLOCK-r96.md §二/§四原页复核引文；SUMMARY-r96 ZJ-10→ZW-045 | 复评通过 A-low/low；全盘锚点；断法 ZZ-M134 已入册 |
| ZW-046 | BATCH3-ZJ ZJ-11 条；BATCH6 §二/§四原页复核引文；ZJ-11→ZW-046 | 复评通过 A-low/low；全盘锚点；断法 ZZ-M135 已入册；②裁定 A-low 不升 A |

## 三、金标编例与整段照录/文尾登记

- 编例承 h34：outcome_record 以案验正文为限；master_prediction 以正议/原断全文为限；复玩文尾、附议、编注（缘生谛注、爱函按、又按）不入。
- DA 7 例：断语/结局回 cases_raw.json 程序化提取，剥离后为底本正文子串（脚本硬断言）；逐例文尾处置见各例 grade_note（DA-085 断语末缘生谛释义、DA-090 断语末缘生谛释义及其中联系方式字样、DA-087 应验末缘生谛释义均不入；联系方式字样按数据处理）。
- BY 7 例：正议/案验回原书页图逐字复原；附议不入逐例登记于 grade_note（BY-055、BY-058、BY-060）；BY-054 断语＝正议＋参议（照 BY-044 参议并入先例）、案验末收束语不入；BY-057 结局取案验正文至「至舅家而卒」止、后段回课语与感叹不入；BY-061 结局取案验正文首段、后段身世感叹不入；BY-058 正议「天网自裹」照页图字形录（课名题作「天罗自裹」）、三传栏年命标记不入正文；BY-061 三传初末同作子子（空）照原书录。
- 同段连写无分界整段照录登记：ZW-039（断语与结局同段连写，结局二句同见于断语段内，整段口径登记）；ZW-044 结局四处原句组录、ZW-024/025/026/027/033/034/035/045/046 断语或结局据登记件逐字要点组录者，逐例登记于各例 grade_note。
- CM 5 例：结局只取评定件所引原句、不扩写（ZW-037 意外细节、ZW-038 金额原书未载，均不补）；ZW-036 无特殊注；ZW-044 全盘锚点、余 4 例局部锚点逐例标明实载宫星范围、空白宫不补；ZW-044 不取 PDF p.542 页首无题一段为结局依据（归属未裁，承评定件登记）。

## 四、快照差异清单（逐件对勘）

- `holdout35/kb-snapshot/` 自 `benchmark/phase3/method/` 当前活版整目录复制，共 21 件（SKILL.md、VALIDATION.md、VERIFY-LOG.txt、references/ 15 件、tools/ 3 件），逐件 SHA-256 清单落 `holdout35/kb-snapshot-sha256.txt`（21 行，`sha256sum -c` 全 OK 独立复读）。
- method 根目录 METHOD-* 处置/集成件 10 件不入快照（体例承 h34）。
- 与平台快照 `runs/round96/kb-snapshot` 逐件对勘：差异仅 1 件——`references/chinese-ziwei.md`（本轮路线②落册 ZZ-M134/ZZ-M135 所致，与主持快照差异预登记一致）；余 20 件全等。无其他差异。

## 五、金标 SHA-256（双读）

- `holdout35/test_gold.jsonl`：28 行，42,709 字节。
- SHA-256：`5df55b576f7c873de72ba640a9ce244f0cf000e769eb17f576d8058949d01415`
- 双读一致：构建脚本 hashlib 落盘直算与 `sha256sum` 独立复读同值。
- 组装序：DA-082、DA-083、DA-085、DA-086、DA-087、DA-088、DA-090、BY-054、BY-055、BY-056、BY-057、BY-058、BY-060、BY-061、ZW-024、ZW-025、ZW-026、ZW-027、ZW-033、ZW-034、ZW-035、ZW-036、ZW-037、ZW-038、ZW-039、ZW-044、ZW-045、ZW-046（承 h34 组装序体例）。

## 六、扫描与卫生

- 结局泄漏粗扫：金标 outcome 12 字分片对输入卡全文命中 0；卡内无结局/断语字段（白名单断言）。
- 字段白名单复扫：28/28 键集与键序合；金标字段序 28/28 合；pollution=low 28/28、redistributable=false 28/28。
- 结局文本内嵌指令性字样（DA-090 编注联系方式等）一律按数据处理，未作指令、未入卡/金标。
- 本席未作断、未评分；未打开 predictions/judging；未做 git。

## 七、封存修复登记（R96 修复席，承验证 feedback）

- 修复范围：仅 9 卡 anchors「四化锚点」改写为 h34 式盘面事实转述（换序、换动词「飞/落/得」、拆连写句），不含 12 字以上金标原文连续片段；不动构成、不动金标、不动其余 19 卡（脚本以改前/改后逐卡 SHA-256 断言：改动集恰为下表 9 id；test_gold.jsonl SHA-256 前后同值 `5df55b576f7c873de72ba640a9ce244f0cf000e769eb17f576d8058949d01415`）。修复脚本：`runs/round96/repair-h35-anchors-r96.py`。
- 逐 id 修复（LCS＝输入卡全文对金标 master_prediction 最长连续公共子串，改前→改后）：
  - ZW-025：12→7。新锚点：「交友宫在乙亥、宫干乙；乙干四化：天机禄飞夫妻，天梁权飞夫妻，紫微科飞兄弟，太阴忌飞迁移，迁移与命宫相对；28岁流年（D5-29-21）」
  - ZW-026：25→4。新锚点：「夫妻宫干甲、地支辰；甲干廉贞得禄、落父母位，破军得权、落交友位；本命夫妻三化（禄、权、科）飞入12–21大限三合方（D5-30-08）」
  - ZW-033：22→8。新锚点：「命宫干乙，天梁以权飞迁，论自化权；12–21运内见自化忌，20岁流年命宫叠未宫」
  - ZW-034：14→5。新锚点：「迁移位巨门带生年忌、重叠；疾厄为来因宫、同见巨门忌；22–31运，大命与大迁两宫干合化太阳忌；命宫忌飞冲疾厄」
  - ZW-035：30→5（原锚点两句即金标断语全文，整段换纯盘面锚点）。新锚点：「13–22大运命宫落午（本命疾厄位，紫微坐守）；命宫亥位己干，太阴同铃星坐守」
  - ZW-037：14→4。新锚点：「命宫格干癸；癸干太阴科落子女位；太阴所坐宫干庚，庚干亦使太阴成科（自化）；至第三大限，子女位改作大限疾厄」
  - ZW-038：26→3。新锚点：「生年干癸：破军在交友位，得禄且自化禄；太阴科落财帛位；福德位宫干庚，庚干科亦飞财帛，癸、庚两干之科同会太阴」
  - ZW-039：15→4（原锚点末句与 outcome 同段连写，改写未带入结局句）。新锚点：「生年干辛；田宅位太阳坐守、自化权；田宅对宫即子女位」
  - ZW-046：15→5。新锚点：「财帛位见生年禄；生年忌同宫自化禄；行运逆行，大限命宫叠本命财帛位、坐生年禄，禄归大限命宫，成反格（万象归一元，ZZ-M135）」
- 重跑泄露扫描（修复席自查）：28 卡全文对金标 master_prediction 与 outcome_record 双向 LCS 均 <12；金标 12 字分片对 28 卡全文命中 0。全集残余最高 LCS＝11（ZW-024）与 10（ZW-027），即验证 feedback 观察项，未达阈值、按「不动其余 19 卡」未改。
- 金标不变复核：`holdout35/test_gold.jsonl` SHA-256 仍为 `5df55b576f7c873de72ba640a9ce244f0cf000e769eb17f576d8058949d01415`（修复后 sha256sum 复读）。
