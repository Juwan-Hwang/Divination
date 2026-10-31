# holdout31 封存日志（R87 组集封存席）

## 一、构成与口径

- 定版口径（主持增补件 `runs/round87/PREREG-ADDENDUM-r87.md` 逐字引）：「**holdout31 共 28 例：六壬 14（源序 DA→CY→BY 轮取、读法 B 自 DA 起重启，CY 源常规 eligible 为 0 自动无取，逐源按台账序轮取至 14 足额，源别分额由组集席按 h30 封存日志轮取口径执行并在封存日志逐源登记）＋六爻 14（WHY 台账序续取 10＋GSZ-107、GSZ-108、GSZ-109、GSZ-110 四例尽取）。**」组集写死口径承 `runs/round87/PREREG.md` §5；锚点以盘体实载为准承 CYJ 专项复核主持裁定（乙·收紧，`runs/round87/supply/CYJ-ANCHOR-REVIEW-r87.md` §5）。
- **判读归属：本集为 R87-REV1（calibration 第十二节）判读集**——集成先于封存、本集快照含集成集（见 §九）；开封条件＝封存后首个平台全立轮（最早 R88）。
- 六壬轮取（读法 B）：轮取起点自 DA 起重启，源序 DA→CY→BY；CY 源（粹言卷五/卷六）经常规 eligible 为 0（裁定乙）于轮取中自动无取（不占轮次产出、仅登记）；DA 与 BY 交替各取一，至 14 足额止，实成 **DA 7＋BY 7**。轮取结果（按取用序）：DA-047 → BY-022 → DA-048 → BY-023 → DA-050 → BY-024 → DA-051 → BY-025 → DA-054 → BY-027 → DA-055 → BY-028 → DA-057 → BY-030。
- 六爻：WHY 按台账序（一轮 §7 序在前）续取 10＝WHY-037、038、039、040、041、042、043、044、068、069；GSZ 建卡口径名单尽取 4＝GSZ-107、108、109、110。
- 产物：`benchmark/phase3/holdout31/inputs/<id>.json` ×28＋`benchmark/phase3/holdout31/test_gold.jsonl`（28 行）。

## 二、限度逐项复核（组集席自核）

| 限度项 | 要求 | 本集实况 | 判定 |
|---|---|---|---|
| T | ＝28 | 28 | ✔ |
| 单体系占比 | 各 ≤50.0% | 六壬 14／28＝50.0%、六爻 14／28＝50.0% | ✔ |
| 单源占比 | 任一源 ≤50% | DA 7（25.0%）、BY 7（25.0%）、WHY 10（35.7%）、GSZ 4（14.3%） | ✔ |
| 非夷坚源 | ≥13 | 夷坚源 0 例、非夷坚 28 | ✔ |
| 非六爻 | ≥13 | 非六爻＝六壬 14 | ✔ |
| 锚点 | 仅锚点在场者 | 六壬 14 例课式头四要素在场（R84 台账 present 面内取用、课盘回原文实载复原）；WHY 10 例 anchor present；GSZ 4 例 anchor present＋建卡口径五要素复核全过 | ✔ |
| pollution | low 全集 | 28／28 low | ✔ |
| redistributable | false 全集 | 28／28 false | ✔ |

## 三、前置核查（件：`runs/round87/precheck-holdout31-seat-r87.json`，脚本 `runs/round87/precheck_holdout31_r87.py` 全断言通过）

1. **排除对**：候选 28 例逐 id 对 LY-015／LY-320 明核，两 id 均不在候选内（候选 id 空间 DA-／BY-／WHY-／GSZ-，与 LY- 不交叠），逐 id 执行登记。
2. **零复用**：候选逐 id 对已用并集 1220（`runs/round87/used-ids-r87.json`，distinct 1220）对勘，交集为空集。
3. **六壬余面复算**：台账（`runs/round85/lr-eligible-ledger-r85.json`）未用总量 216（DA 87、BY 80、CYJ 40、CY 6、YX 3）；CYJ／CY 两源未用 46 例经常规 eligible 归 0（裁定乙，转 fidelity 例外登记）；常规 eligible 余面＝216－46＝**170**（＝DA 87＋BY 80＋YX 3，YX 承历轮不在轮取源序内、只登记），与增补件登记订正值 170 逐值相符。DA／BY 两源可取面 167 ≥14，足额，不触发停工回主持。
4. **WHY 余面复算**：STOCK-RECOUNT-h28 §7 未用 27＋§8 未用 30（基点 57），扣已用（h28 已取 5＋h30 已取 10＝WHY-025、026、027、028、031、032、033、034、035、036 等，逐 id 对并集核）后余 **42**（§7 余 12＋§8 余 30），与增补件登记值逐值相符；按台账序续取前 10。
5. **id 号段占用**：28 id 逐一对全部已封集 `holdout*/inputs/` 文件名核对，零冲突。

## 四、取用清单（逐源登记，按轮取／台账取用序）

- **DA（《大六壬断案》，7 例）**：DA-047、DA-048、DA-050、DA-051、DA-054、DA-055、DA-057。台账序后续递补链（未触发）：DA-059、DA-060、DA-061、DA-062、DA-063…
- **BY（《六壬辨疑·毕法案录》，7 例）**：BY-022、BY-023、BY-024、BY-025、BY-027、BY-028、BY-030。台账序后续递补链（未触发）：BY-031、BY-032、BY-033…
- **CY（《六壬粹言》卷五/卷六）**：轮取中自动无取（常规 eligible 为 0，裁定乙）；fidelity 例外未用余面 46 例只登记、不入选（不以 fidelity 降级形态凑数）。
- **WHY（《六爻分类占验技法》，10 例）**：WHY-037、WHY-038、WHY-039、WHY-040、WHY-041、WHY-042、WHY-043、WHY-044、WHY-068、WHY-069。一轮余序递补链（未触发）：WHY-070、WHY-071、二轮 §8 序。
- **GSZ（《六爻卦例说真》，4 例尽取）**：GSZ-107、GSZ-108、GSZ-109、GSZ-110。建卡口径名单（STOCK-RECOUNT-h28 §6 共 14 例）至此尽取、同源无递补余位（GSZ-111 不在建卡口径名单、五要素不过）——本轮四例五要素复核全过，未触发递补；登记在案备后轮口径。
- **递补触发登记：全程未触发**（28 例建卡与资格断言一次全过，无同名剔除、无建卡不过）。

## 五、资格断言集（承 h30 §三、按本集源面适配，构建脚本逐例硬断言全过）

- 六壬（DA／BY）：池卡 `holdout_eligible=true`、`contamination='low'`、`outcome_grade∈{A, A-low}`、`master_predictions[0].statement_excerpt` 非空、`outcome.description` 非空、id ∉ 已用并集 1220；BY 另断 `review.verdict='seal'`、`review.grade_final∈{A, A-low}`、`review.contamination_final='low'`。课式头四要素在场以 R84 核查台账（`runs/round84/supply/LR-ANCHOR-CHECK-r84.md` §4/§5/§7）为准据，课盘回原文实载复原（DA 回底本全文原式、BY 回原书页图）。
- WHY：id ∈ 台账 `net_eligible_A_low_present`（＝资格全过名单 §7/§8 面内）、`pollution='low'`、`anchor_presence='present'` 且 `anchor_missing` 为假、`outcome_record` 非空、断语补录件齐备（十例全命中）。
- GSZ：`grade='A'`、`pollution='low'`、`anchor_presence='present'`、`eligible_net=true`、id ∈ 建卡口径名单、断语与结局非空；**建卡口径五要素复核**（回原书文字层 `runs/round76/gsz-book-r76.txt`，函数与 h30 同源）：卦名／动爻（卦象行含「动」或有变卦）／世应／六亲纳支（六行六亲齐备）／月建日辰（asked_at 含月与日）＋本卦名与占时在书内在册——四例七项全 True（逐例结果见构建报告 `eligibility`）。

## 六、字段白名单、剔除与字段映射（体例承 h30 §四）

- 输入卡字段白名单（对齐 holdout30 卡实读）：`id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors`；金标字段序：`id, master_prediction, outcome_record, tradition, pollution, grade, grade_note, provenance, license_status, redistributable`。逐卡剔除登记与字段映射见构建报告 `strip_register`／`field_mapping_notes`。
- WHY 卡：`anchors` 全列＝台账 `input_fields.chart`（asked_at／ben_gua／bian_gua／moving_lines／chart_lines_top_to_bottom 逐字）；`subject` 台账为空、原书未具名，组写为「求测者（台账 subject 为空、原书未具名）」；`context`＝asked_at＋question＋原书章节定位组写。WHY-044 台账 ben_gua 字段含乱码字，经台账 chart_lines（父母戌土×／动爻结构）与原书核定为「山地剥」入卡（登记）。
- GSZ 卡：`anchors`＝台账 chart 全列（无 moving_lines 键、承 h30 体例）；subject／context 组写同 WHY 体例。
- 六壬卡剔除口径（承 h30 §四）：占者问句段、编注（缘生谛注等）与案验续释不入断语——DA 七例断语＝邵先生曰全文、结局＝应验段正文，尾部「缘生谛：…」编注逐例剔除（DA-047、048、054、057 等）；BY 断语＝正议全文、结局＝案验正文。

## 七、补录、剔除与转录登记（全程）

- **DA 金标全录**：池卡摘录为节录，本轮金标断语／结局回底本全文（`expansion12/liuren-duanan/scratch-archive/cases_raw.json`，经 `runs/round87/dump-da-raw-h31-r87.txt` 转储核读）逐字照录，课盘自 raw 原式（天盘方阵／四课格／三传栏）转录入 anchors。DA-051 结局底本作「工部待郎」，逐字照录不改作「侍郎」（登记）。DA-054 结局中续占段（堪舆人言葬地、知丞再占）为应验叙事正文，照录。
- **BY 金标全录**：池卡无课盘字段，本轮课盘与正议／案验全文回原书扫描本页图逐字复原（140dpi 渲染读图、课盘 250dpi 裁切复核，页图存 `runs/round87/lr-pages-h31-seat/`）。课名以原书课例题署为准（BY-022「上下皆合・闭口卦体」、BY-023「自支传干・闭口卦体」等）。原书天将省字「元」（＝玄武）照录并注记；BY-022 与 BY-023 天盘原式经裁切复核确为同式（原书如此，照录）。BY-030 四课格天将行末另标「关」字、三传旁标「游」「都」，照录注记。**剔除差异登记**：BY-022 案验段含复玩分析文尾（「果信不能通…而原断宜为久远者则误矣」以下），本轮照录入结局（承 h30 DA-038 复盘分析照录先例）；BY-027 案验后复玩分析段与附议问答段不入结局（承 h30 BY-017/018 剔除先例）——两例处置口径不一，逐例登记在此，备验封裁处。
- **WHY 断语补录**：台账未单列断语字段，十例回原书《六爻分类占验技法》〔判斷〕段逐字补录（繁体照录，页图存 `runs/round87/why-pages-h31-seat/`；定位以印刷页脚为准，扫描本 PDF 内页序错乱已逐例核对）。结局自台账 `outcome_record` 逐字照录，并逐例与原书應驗情況核对相合。**字形登记三处**：WHY-037「本卦」一字扫描字形近「丙」，按文义取「本卦」；WHY-039／040「墓庫」扫描字形近「基庫」，按术语取「墓庫」——均逐字断言内置、登记备核。
- **GSZ**：断语与结局自台账逐字照录，无补录。

## 八、扫描三道与金标 SHA-256

- 标记集逐字承 R42 PREREG §5（一级 13 词＋二级 9 词）＋封存日志泄漏标记集（字段名污染词 11 词）＋禁用键集（28 键）。
- 构建道（`runs/round87/build_holdout31_r87.py`）：28 卡内容标记／字段名／禁用键／金标片段子串扫描，四项命中全 0。
- 落盘回读道（同脚本落盘后回读）：四项命中全 0，卡面与内存构建逐字相等、字段白名单与字段序断言全过。
- 独立复扫道（`runs/round87/scan_holdout31_r87.py`，不 import 构建脚本、按 id 清单逐件精确打开）：五项扫描全 0、`all_pass=true`，件 `runs/round87/scan-holdout31-rescan-r87.json`。
- 卡面逐卡通读转储：`runs/round87/dump-holdout31-cards-r87.txt`。
- **金标 SHA-256 双读**：构建脚本 hashlib＝`4b4312147f6657b66fc21fe56207f7ba76857fdd7340ab0a5c5e6728a9210e9d`；落盘后独立 `sha256sum`＝`4b4312147f6657b66fc21fe56207f7ba76857fdd7340ab0a5c5e6728a9210e9d`——两读全等。金标 37,104 字节、28 行。主持第三读：`4b4312147f6657b66fc21fe56207f7ba76857fdd7340ab0a5c5e6728a9210e9d`（见第十二节，三读定版）。

## 九、封存快照

- 自封存时点活 `method/` 生成 `runs/round87/kb-snapshot-holdout31`（21 文件，method/ 根 `METHOD-*` 登记件不入快照）＋SHA 清单 `runs/round87/kb-snapshot-holdout31-sha256.txt`。
- 与平台快照 `runs/round87/kb-snapshot` 逐件对勘：文件集相同（21＝21），哈希差异**恰为 {SKILL.md, references/calibration.md} 两文件**——即本轮 R87-REV1 集成（calibration 第十二节＋SKILL (t) 指针），与派单预判逐件相符；本集快照含集成集，承 §一判读归属。

## 十、供给面登记（照实）

- **「本集为存量内最后一集」口径不适用**——本集系 expansion 池台账存量（六壬）＋r56/r57 台账存量（六爻）组集，非封存存量末集口径。
- 封存后供给面：六壬常规 eligible 余面 156（＝170－14，含 YX 3 不入轮取源序）；CYJ／CY fidelity 例外未用余面 46 例（盘体不在场、仅式头）；WHY 资格余面 32（42－10，§7 余 2＋§8 余 30）；GSZ 建卡口径名单已尽取（同源无余）；测字段（ZCB）eligible 已枯竭（承 h30 登记，本轮无测字例）。

## 十一、卫生与执行环境

- 页图与转储只入 `runs/round87/` 内（`lr-pages-h31-seat/`、`why-pages-h31-seat/` 及各转储件），未用 /tmp；构建 glob 未用通配删除；数目按自有 id 清单逐件核验（28 卡逐件精确打开复扫）。
- WHY 定位探针件（`why-pages-h31-seat/ocrprobe/` 与 loc-* 探针图）为定位过程件，只登记、不入产物。
- 本席未做任何 git 操作（验封、提交、打标签由主持执行）。

## 十二、主持验封（R87 续任主持，组集席交卷后独立执行）

- **金标 SHA-256 主持第三读**：`4b4312147f6657b66fc21fe56207f7ba76857fdd7340ab0a5c5e6728a9210e9d`（37,104 字节、28 行）——与组集席双读逐字一致，**三读定版**。
- **主持独立复核**（`runs/round87/host_verify_holdout31_r87.py`，不 import 组集席脚本）：输入卡 28 张按金标 id 清单逐件精确打开、id 集与金标全等；与已用并集 1220 逐 id 零复用；排除对 LY-015／LY-320 明核不在集内；卡面禁用键递归扫描零命中；快照 `kb-snapshot-holdout31` 与平台快照文件集相同（21＝21）、哈希差异恰为 {SKILL.md, references/calibration.md} 两文件（R87-REV1 集成集）。**全过**。
- **构成与限度主持复核**：28 例＝六壬 14（DA 7／BY 7，轮取读法 B 自 DA 重启、CY 常规 0 自动无取，逐源登记与增补件构成句相符）＋六爻 14（WHY 10 台账序续取／GSZ 4 尽取）；单体系各 50.0% 不逾、单源最大 WHY 35.7%、非夷坚 28、非六爻 14、仅锚点在场（盘体实载口径）、low 28/28；递补链零触发。封存后并集＝1220＋28＝**1248**。
- **裁处（BY-022／BY-027 结局剔除口径并存）**：两例各承 h30 在册先例（BY-022 案验复玩文尾照录承 DA-038 型、BY-027 复玩段与附议不入承 BY-017/018 型），属案验编例口径之并存、无泄漏与断语污染（三道扫描零命中复核在案），**登记并存、验封不改**；R88 预注册宜将「案验复玩文尾」取舍统一成文，避免后续集再现两口径。
- **裁处（WHY 转录字形三处与 DA-051 照录）**：WHY-037「本卦」、WHY-039/040「墓庫」与 DA-051 底本「工部待郎」均系原书/底本形态照录，已逐例登记，照录不改成立。
- **验封结论：通过。** 快照锚定 runs/round87/kb-snapshot-holdout31（含第十二节集成集）；**本集为 R87-REV1 判读集**（判读口径见 runs/round87/revision/PROPOSAL-R87-REV1.md：TIM 实质主码率 ≤0.120 为主指标、护栏五项、证伪线写死）；开封＝封存后首个平台全立轮（最早 R88），照第二版三判据。

## 开封（R88 主持）

- 开封条件成就：R88 平台三项全立（R87-REV1 接入后系列第 1 点、全立计 35；(a) 全集 −1.160（SE 0.102）／(b) 四护栏全立（八字全集 ＋0.284、natal ＋0.827、horary −0.160、六壬 dev8 −1.889）／(c) 六爻 dev8 −1.870、熔断未触（>−2.255），归因护栏无触发，analyze_r88 定稿），照本日志写死条件「封存后首个平台全立轮当轮开封」于 R88 开封。
- 开封前置复验（R88 开轮已行、开封时点复核）：金标 SHA-256 主持复读 `4b4312147f6657b66fc21fe56207f7ba76857fdd7340ab0a5c5e6728a9210e9d`（37,104 字节、28 行）与三读定版全等；输入卡 28 张在盘；主持独立第三道复扫（runs/round88/host_scan_holdout31_r88.py）28 卡禁用键与泄漏标记零命中。前置复验三项全过。
- 盲测快照：封存时点快照 `runs/round87/kb-snapshot-holdout31`（含第十二节，与 R87 平台快照差异恰集成两文件）；本集为 R87-REV1 判读集，验收后照写死口径判读（N＝28 不顺延）。
- 验收执行细节见 `runs/round88/acceptance/OPENING.md`；评审 anon 种子 20261104、前缀 H31O-／H31M-。

## 验收结果（R88，已用）

- 验收执行：runs/round88/acceptance/（OPENING.md、REPORT.md、final-scores-h31.json）。双视无分歧（我方 max |Δ|＝1.0、大师 max |Δ|＝1.0，仲裁集为空）。
- 三判据（主口径＝全 low 28）：我方均分 2.509 vs 大师 4.161，配对差 **−1.652**（SE 0.376，n＝28），W/T/L 5/0/23——(i)(ii)(iii) 三判据全不成立，**未达标**。本集自此标已用，并集不变（28 id 本已计入 1248）。
- 分段附读（只作诊断）：六壬 −2.071（DA −3.536，0/0/7，我方均分 1.107 为最深段；BY −0.607）；六爻 −1.232（WHY −1.300、GSZ −1.062）。
- 独立诊断 DIAG-H31 随 R88 执行；本集为 R87-REV1 判读集，判读照写死口径随 R88 执行（见 runs/round88/acceptance/JUDGMENT-R87-REV1-r88.md）。
