# holdout34 封存日志（R93 组集封存席）

封存对象：`benchmark/phase3/holdout34/`（inputs 29 卡＋test_gold.jsonl 29 行＋kb-snapshot 21 件＋kb-snapshot-sha256.txt）。
本席只建卡封存，不作断、不评分。构成与口径以 `runs/round93/PREREG-ADDENDUM-r93.md` 定版为准；体例承 holdout33 封存日志。

## 一、构成与口径

- T＝29＝紫微 12＋六壬 13（读法 B：DA 7＋BY 6）＋六爻（WHY）4。
- 紫微 12：ZW-017、ZW-018、ZW-019、ZW-020、ZW-021、ZW-022、ZW-023、ZW-028、ZW-029、ZW-030、ZW-031、ZW-032（reserve ZW-024–027、ZW-033–035 不取）。
- 六壬 13：自 holdout33 取用位 DA-074／BY-046 后，按 R84 核查台账（`runs/round85/lr-eligible-ledger-r85.json`）登记序续取、跳过已用，复算定版：DA 7＝DA-075、DA-076、DA-077、DA-078、DA-079、DA-080、DA-081；BY 6＝BY-047、BY-048、BY-049、BY-050、BY-051、BY-053（BY-052 不在台账列内，自然跳过；台账原始序其后无已用例、无跳例）。
- WHY 4：WHY-111、WHY-112、WHY-114、WHY-115。
- 金标编例（承 h33）：结局以案验正文为限、断语以正议/原断全文为限；复玩文尾、附议、编注（缘生谛注、爱函按）不入；同段连写无分界者整段照录并逐例登记（§七）。

## 二、限度逐项复核（封存后盘上复算）

- 紫微占比 12/29＝41.4%；六壬占比 13/29＝44.8%；六爻占比 4/29＝13.8%。
- 单源最大：DA 7/29＝24.1%（次 BY 6/29＝20.7%）。
- 非六爻 25/29；pollution＝low 29/29；redistributable＝false 29/29。
- 排除对 LY-015／LY-320：29/29 零命中。

## 三、前置核查逐项结果（脚本 `runs/round93/precheck_h34_r93.py`，全过）

- (i) 排除对逐 id 对撞：零命中。
- (ii) 零复用对撞：29 id 对 `runs/round93/used-ids-r93.json`（1304 件、互异 1304）逐 id 对撞，交集为空（已用 ZW 仅 ZW-004–016）。
- (iii) 六壬续位台账复算：台账中 DA-074 序位 30、BY-046 序位 28；续位定版如 §一，无递补、无自换例。
- (iv-a) 六壬 13 例池卡资格断言全过：holdout_eligible=true、contamination=low、outcome_grade∈{A, A-low}、master_predictions 与 outcome.description 非空；BY 另 review.verdict=seal、grade_final=A-low、contamination_final=low。
- (iv-b) DA 7 例底本（`expansion12/liuren-duanan/scratch-archive/cases_raw.json`）在册：n=75–81，raw 长 615–833，三传栏标记在场。
- (v) WHY 4 例台账资格全过：pollution=low、anchor_presence=present、anchor_missing 为假、outcome_record 非空、chart.ben_gua 与 chart_lines_top_to_bottom 非空。
- (vi) 紫微登记件 5 件在场（BATCH1、BATCH2-XZS、REVIEW-XZS7、BATCH3-ZJ、SUMMARY）。
- 停工/递补登记：无。

## 四、取用清单（29）

- DA（《大六壬断案》，邵彦和）：DA-075、DA-076、DA-077、DA-078、DA-079、DA-080、DA-081（grade 均 A-low）。
- BY（《六壬辨疑·毕法案录》，张官德）：BY-047、BY-048、BY-049、BY-050、BY-051、BY-053（课例五十六–六十、六十三；grade 均 A-low）。
- WHY（《六爻分类占验技法》，王虎应）：WHY-111（病因例三）、WHY-112（病因例四）、WHY-114（综合例二）、WHY-115（综合例三）（grade 均 A）。
- ZW：ZW-017、ZW-018（许铨仁《钦天四化紫微斗数命理学》）；ZW-019、ZW-020、ZW-021、ZW-022、ZW-023（徐曾生《紫微斗数命运分析》，原例 XZS-08、12、05、10、13）；ZW-028、ZW-029、ZW-030、ZW-031、ZW-032（许铨仁《紫微斗数命理学正解》，原例 ZJ-01、02、04、05、06）（grade 均 A-low）。

## 五、资格断言结果

- 六壬 13 例、WHY 4 例资格断言见 §三 (iv)(v)，全过。
- 紫微 12 例：登记件载 A-low／low／redistributable=false，与金标行逐例一致；盘面锚点（命宫、局、四化）在登记件有据，其中 ZW-020 十二宫从 BATCH2 登记件（封存席半页速读有出入处从登记件），ZW-021 十二宫经 REVIEW-XZS7 复评回读。

## 六、字段映射口径

- 输入卡字段白名单（序）：id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors。29/29 键序一致（封存脚本断言）。
- 金标字段序：id, master_prediction, outcome_record, tradition, pollution, grade, grade_note, provenance, license_status, redistributable。29/29 一致。
- 许可字面：古籍文本＝「古籍文本，内部研究用」；现代版权文本＝「现代版权文本，内部研究用」。
- 六壬天将省字「元」＝玄武，原书省字照录并在卡内注标；课盘方阵/四课/三传照原式转录（DA 从底本数字文本、BY 从原书页图直录）。

## 七、逐例文尾处置与补录/更正登记

- DA 七例：断语录「邵先生曰」段全文（DA-075 含退而告门人、门人问其故两段，同属原断）；段中/段末缘生谛注（词语释义）不入，爱函按不入，逐例同例。DA-077 金标分片一度在终端复核输出中呈乱码，经盘上字节复读证实分片原文完好（「墓遂得出也。又是夜贵人」），系显示伪影，未作改动、登记备查。
- BY-047：正议首词原书作「课传五贵」、课名题作「俱贵」，异文以正议为准，金标从正议。
- BY-048：案验后附议（书 p181 页首「凡幕贵加年命为林下贵人…故以升官论」）不入，已登记于该例 grade_note。
- BY-049：断语「考必攻诘」经 300dpi 原书页图定字（分片原作「攻讦」，封存席更正）。
- BY-050：断语为正议问答两段全文；案验后附议不入，已登记。
- WHY-112：结局年份台账作「2000 年」、原书應驗情況（印刷 p196）作「二〇〇一年」，经放大页图定字从原书，金标结局改从原书（其余从台账简体通例）；异文已登记于该例 grade_note。
- WHY-114：断语回原书补录全文，含台账所无肠炎段（「丑為財庫，才為屎尿，墓庫臨子孫為腸，生殖器，世臨朱雀主炎症，斷其有腸炎」）。
- WHY-115：原书无独立應驗段，结局以判断内对话核实语逐项摘录（含省略号照原式）。
- ZW-019/020/022/023/028/029/030/031/032：金标分片断语原为要旨摘录/转述，封存席回原书页图逐字补录全文后替换（脚本 `runs/round93/fix_gold_h34_r93.py`，逐例登记于各例 grade_note）；ZW-019 结局后段（七十六年癌症句）改从原书繁体原文。ZW-022 断语中原书一处同句复沓（排印重出）从简照录一句，义无出入。ZW-030 断语取书 p.247 析文（1）（2）与 p.248 本案例总结句，理则页（p.246）不入。ZW-031 断语取书 p.258 ※条与命宫丁干条、p.259 大运命宫丙干条（含释义句）。
- ZW-017/018/021：断语/结局从登记件逐字转录（BATCH1 整页转录＋双席复核；ZW-021 从 REVIEW-XZS7 复评件），未再改动。

## 八、金标 SHA-256

- `holdout34/test_gold.jsonl`：29 行，52765 字节。
- SHA-256：`530ab1250dfd6b57931d4d9e07ca1b3cbf8d566edf98fa4cfd85f792a66d54b0`（封存脚本 hashlib 计算与 `sha256sum` 独立复读一致，双读验讫）。
- 组装序：DA-075–081、BY-047–053、WHY-111/112/114/115、ZW-017–032（承 h33 组装序体例）。

## 九、三道扫描结果（脚本 `runs/round93/scan_h34_r93.py`，结果件 `runs/round93/holdout34-scan-r93.json`）

- 扫描一（结局泄漏）：禁用键递归命中 0；一级＋二级＋泄漏标记集全文命中 0。
- 扫描二（大师姓名）：命中 51 处，逐处回读裁记——全部落在 setting/provenance 的书目署名（《大六壬断案》邵彦和、《六壬辨疑·毕法案录》张官德、《六爻分类占验技法》王虎应、《紫微斗数命运分析》徐曾生、许铨仁两书），与 holdout33 同体例：书目信息、非断语/结局内容，不构成泄漏，照录不删。
- 扫描三（字段白名单）：偏离 0（29/29 键集与白名单全等；键序另经封存脚本断言）。
- id 唯一性/零复用：29 id 互异；与已用并集 1304 交集为空（封存脚本断言复核）。

## 十、快照 diff

- `holdout34/kb-snapshot/` 21 件（SKILL.md、VALIDATION.md、VERIFY-LOG.txt、references/ 15 件、tools/ 3 件），与 `runs/round93/kb-snapshot` 逐件全等，且逐件与活 `benchmark/phase3/method/` 源文件哈希一致：diff 无。
- method/ 根目录 METHOD-* 处置/集成件 10 件不入快照（体例同 h33），清单见构建报告 `method_root_not_in_snapshot`。
- SHA 清单：`holdout34/kb-snapshot-sha256.txt`（21 行）。

## 十一、供给面登记（封存后）

- 已用并集：1304＋29＝1333。
- 六壬台账余面：DA 59（下位 DA-082 起）、BY 53（下位 BY-054 起）。
- WHY 合格余面 0：台账未用条目（WHY-113、WHY-116、WHY-117 等）均 grade B，不合 A 级资格。
- 紫微 reserve 7：ZW-024–027、ZW-033–035（本轮不取）。

## 十二、卫生与验封留位

- 本轮脚本均新写于 `runs/round93/` 内唯一名（precheck_h34_r93.py、fix_gold_h34_r93.py、seal_h34_r93.py、scan_h34_r93.py 及各建卡席脚本），grep 残留 h33/r89 字面量逐处查毕（仅注释中体例出处提及，无路径/构成残留）；页图只入 `runs/round93/` 内新目录（lr-pages-h34-seat、why-pages-h34-seat、xzs-pages-h34-seat、zj-pages-h34-seat）；未用 /tmp；未用通配删除；未读 `runs/round93/predictions` 与 judging 分数件；未做 git。
- 构建报告：`runs/round93/holdout34-build-report-r93.json`。
- 主持验封（R93 主持，2026-10-31）：盘上复算全合——inputs 29 卡 id 集与 PREREG-ADDENDUM-r93 构成逐 id 全等、字段白名单 29/29 键集与键序合；金标 29 行、字段序 29/29 合、pollution=low 29/29、redistributable=false 29/29；金标 SHA-256 主持直算 530ab1250dfd6b57931d4d9e07ca1b3cbf8d566edf98fa4cfd85f792a66d54b0，与封存脚本及构建报告双读一致；限度复算：T=29、紫微 41.4%、六壬 44.8%、六爻 13.8%、单源最大 DA 24.1%、非夷坚 29、非六爻 25，全合；快照与 runs/round93/kb-snapshot 主持 diff 零差异。WHY-112 结局年份从原书（二〇〇一年）之处置**主持追认**：金标以原书为准、台账转录误差登记入数据流水待核（见 R93 数据议程）。**holdout34 封存成立**，开封条件照 §8 与 PREREG-ADDENDUM-r93 §4（封存后首个平台全立轮、最早 R94）。

## 十三、开封追记（R94 主持，2026-11-01）

- 开封轮：R94（封存后首个平台全立轮：(a) −0.918、(b) 四护栏全过、(c) −1.547，全立计 40）。开封前置复验四项全过（金标 SHA 三读一致 530ab125…d54b0、inputs 29 id 与 §一逐 id 全等、快照 diff 零差异、输入卡白名单复扫违规 0），登记于 `runs/round94/acceptance/FREEZE-h34.md`。
- 验收结果：**未达标**。我方均分 3.603 vs 大师 5.397，配对差 **−1.793**（SE 0.314），W/T/L 2/4/23；第二版三判据（R42 PREREG §8）①②③全不成立（主口径 low 29 全集与封存口径同值）。分段：紫微 −1.083、六壬 −2.538（DA −3.643／BY −1.250）、WHY −1.500。双视争议 0、无仲裁。明细在 `runs/round94/acceptance/judging/final-scores-h34.json` 与 R94 REPORT。
- 附读：验收面第八节明引率 29/29＝100%（h33 验收面为 3.6%），执行缺口堵上而总差未实质收窄（历集口径：h31 −1.652、h32 −1.929、h33 −1.982、本集 −1.793，构成不同只作并列登记）。
- 本集自此标已用，纳入已用并集（1333 不变——封存时已计入；开封不新增 id）。后续诊断 DIAG-H34 与修订裁定见 R94 REPORT/ADDENDUM。
