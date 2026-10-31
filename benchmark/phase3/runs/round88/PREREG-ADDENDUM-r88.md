# PREREG-ADDENDUM-r88 — holdout32 组集构成写定（R88 主持，封存前落盘）

承 PREREG-r88 §4 框架，本增补件写定 holdout32 构成句与封存锚点事实，组集派单逐字引用本件。

## 一、封存时点 method 状态（快照锚点）

- R87-REV1 已于本轮判读**未达未证伪**并处置完毕：第十二节自 R89 起失效存档（失效登记已入活 method，METHOD-DISPOSAL-r87rev1-r88.md；SKILL (t) 指针保留、SKILL.md 零改动）。
- 本轮修订**不立项**（runs/round88/revision/PROPOSAL-R88-REV1.md 不立项登记）：无第十三节集成、无 (u) 指针。
- 故 holdout32 快照＝封存时点活 method（处置后形态：现行干预仅第八节；第十二节存档条文在册、(t) 指针在册），自 benchmark/phase3/method/ 复制为 runs/round88/kb-snapshot-holdout32，与活 method 逐件全等登记。
- **判读归属：空缺登记**——本集不判读任何干预（无待判读节）；下一实际立项提案的判读集归属自其集成后首个新鲜封存集起算，不追溯本集（承 h30 空缺登记与 R88 不立项登记）。

## 二、构成句（写定）

- T＝28＝六壬 14＋六爻 14。
- 六壬 14：轮取读法 B 自 DA 重启、DA/BY 交替逐源按台账序取未用（台账 runs/round85/lr-eligible-ledger-r85.json）；CY 常规 eligible＝0 自动无取（CYJ/CY 名单不入轮取）、YX 3 例不入轮取源序；逐源取数与逐 id 以组集席对 used-ids-r88.json（并集 1248）的盘上复算为准并逐源登记；单源不足额时由另一源续足并登记。
- 六爻 14：WHY 台账序——WHY-070、WHY-071（§7 余）居前，其后续 §8 序（台账 runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json 与 data/holdout28-seal-log.md 所载 STOCK-RECOUNT-h28 §7/§8 序）；GSZ 已尽、无 GSZ 取数。
- 排除与限度照 PREREG §4：与并集 1248 逐 id 零复用； LY-015／LY-320 排除对逐 id 明核不在集内；T≥25、单体系 ≤50%、单源 ≤50%、非夷坚 ≥13、非六爻 ≥13；仅锚点在场（六壬以盘体实载为准）；全例 low（现有供给形态）。

## 三、金标编例（统一口径，承 PREREG §4）

- 结局以案验正文为限：复玩/复盘文尾、附议、问答、编注一律不入；断语以正议/原断全文为限。复玩与案验正文同段连写无分界者，整段照录并在 grade_note 逐例登记。DA 例金标回底本全文逐字照录（expansion12/liuren-duanan/scratch-archive/cases_raw.json）；BY 例课盘回原书页图逐字复原（承 h31 工法）；WHY 例照 r56 台账源文本逐字编例。缺口先逐字补录后封，不臆补。

## 四、封存体例

- 字段白名单照 h31 卡面形态；三道扫描（禁用键／泄漏标记／白名单偏离）组集席自扫＋主持独立复扫；金标 SHA-256 组集席双读＋主持第三读定版；封存日志 data/holdout32-seal-log.md（构成、限度复核、逐例文尾处置登记、余量与可行性登记：封存后并集预期 1276、六壬常规余量与 WHY 余量逐项登记、h33/h34 可行性预告照 PREREG §4）；主持验封后提交＋标签 phase3-round88-holdout32-sealed。
- 开封条件：封存后首个平台全立轮当轮开封，照第二版三判据（R42 PREREG §8）。
