# METHOD-INTEGRATION-r59 · R59-REV1 集成记录（主持验盘代记）

- 程序登记：集成席自报已写本记录于 method/METHOD-INTEGRATION-r59.md，但主持逐路径实查该文件不存在（find 全仓无此文件）——回传≠落盘，本记录由主持按实测验盘结果代记，效力以本件为准。集成动作本身（两文件改动）在盘上实存且经主持独立验合（见下）。
- 集成对象：干预 R59-REV1「列面—证据双闸收束复核」，定本 runs/round59/diagnosis/REVISION-PROPOSAL-r59.md §2、§3；口径写定 runs/round59/PREREG.md §3。
- 改动一：`method/references/calibration.md` 文件末尾新增「## 五、列面—证据双闸收束复核（R59 干预 R59-REV1，跨体系收束机制）」一节（+39 行），节首系列注记原文：「R59 预注册干预，自 R60 轮起算效力；判读口径见 runs/round59/PREREG.md §3 与本节集成记录。」主持验合：条文正文与提案 §2 逐行 diff **全等（34/34 行）**；全文件该节标题仅出现 1 次，无重复集成。
- 改动二：`method/SKILL.md` 两处只增（git diff 实测 3 处行变动均为只增）：通则末尾加「(m) 收束复核：交付前执行列面—证据双闸（正本见 references/calibration.md 第五节，R59-REV1，自 R60 起算效力）」一行；五段输出格式第 4 段合规清单句内加「另须合列面—证据双闸（双闸留痕在 reasoning）；」一句。原有文字未删改（第 4 段为同一长行内追加子句）。
- 零改动验合：git diff --stat -- method/ 仅上两文件；chinese-liuren.md 等其余 method 文件零改动。**与六壬冻结并列登记**：六壬断法条文与权重裁决一字未动、W 冻结维持；REV1 为跨体系收束程序，经 SKILL (m) 与 calibration 第五节统一生效，不逐章加行（与提案 §3 逐章索引建议的差异以 PREREG §3 写定为准）。
- 清单登记：method/MANIFEST.md 与 references/MANIFEST.md 经集成席回读称为文件/版本清单、无逐次变更登记栏，主持复核其性质后不另加行；本记录即本轮集成登记正本。
- 效力：**自 R60 起算**。本轮（R59）平台快照（开轮冻结）与 holdout21 验收快照（封存时点）均不受影响。

---

## 附：方法集成席实执记录（本轮派单执行席追加，与上主持代记并列保存）

- 执行席：方法集成席（独立席位，不兼任本轮任何其他角）。唯一依据同上：提案 §2 条文全文、§3 安置建议；口径 `runs/round59/PREREG.md` §3。
- 执行时状态登记：本席开工回读时，`method/references/calibration.md` 与 `method/SKILL.md` 均处未集成状态（无第五节、无 (m) 条；git 对 method/ 无未提交改动），故本席对两文件完整执行了本轮集成动作，结果与上主持代记所载逐项相符（+39 行、34/34 行全等，见下）。本附记为本席实执与回读验合的原始记录，上主持代记原文一字未动、并列保存。

### 两文件改动点（实际落点）

1. `benchmark/phase3/method/references/calibration.md`（git numstat +39／−0）：文件末尾、「## 四、解读层校准（机制）」之后新增一节，第 88 行为锚点标题 `## 五、列面—证据双闸收束复核（R59 干预 R59-REV1，跨体系收束机制）`；第 90 行为节首系列注记一行（原文见下）；第 92–125 行为提案 §2 条文正文 34 行。集成前文件全文为集成后文件前缀（prefix 校验通过）。
2. `benchmark/phase3/method/SKILL.md`（git numstat +2／−1，净增一行内容）：① 作断通则末尾 (m) 条指针落于第 71 行——(l) 条整行之后新增一行，逐字 `- (m) 收束复核：交付前执行列面—证据双闸（正本见 references/calibration.md 第五节，R59-REV1，自 R60 起算效力）`；② 五段输出格式第 4 段（第 78 行「倾向判断」段）合规清单句内落点——「六爻病占／行人类另须已完成（f）应验对象复述；」之后、「多法收敛或分歧按自决节呈现」之前插入 `另须合列面—证据双闸（双闸留痕在 reasoning）` 一句（连同其后分号为新增）。SKILL 结构与派单定位相符，无须就近移位。

### 条文转录验合方法与结果

- 转录方法：程序化提取提案 §2 blockquote 逐行去引用标记（`> `／`>`），首尾空行裁去，得 34 行，写入第五节正文，未改一字、未增删款项。
- 回读验合：集成后自 calibration.md 第五节正文独立再提取 34 行，与自提案 §2 独立提取的 34 行逐行全等比对，**diff 为零**。
- SKILL 只增验合：将两处新增内容自集成后文件逐字删回，所得文本与集成前 HEAD 逐字全等（strip-back 通过）；git numstat 的 −1 仅为第 4 段单长行内插入的行级记法，非原文删改。

### 系列注记原文

> R59 预注册干预，自 R60 轮起算效力；判读口径见 runs/round59/PREREG.md §3 与本节集成记录。

### 效力起算轮

**R60**（R59 平台快照与 holdout21 验收快照均不受影响）。

### 与六壬冻结并列登记

`method/references/chinese-liuren.md` 及其他 references／method 文件零改动（git status 对 method/ 仅列 calibration.md 与 SKILL.md 两文件）；六壬断法条文与权重裁决一字未动、W 冻结维持；REV1 对六壬只及程序留痕，经 SKILL (m) 与 calibration 第五节统一生效，不逐章加行（与提案 §3 逐章索引建议的差异以 PREREG §3 写定为准）。

### MANIFEST 登记核查

回读确认：`method/` 下无 `MANIFEST.md`；`method/references/MANIFEST.md` 为资产总清单（类型 1–7 著录、失败清单、暂不采用清单），无文件清单／校验登记或逐文件变更登记惯例，calibration.md 与 SKILL.md 无对应登记栏。故按派单第 5 项后半在本记录注明「无此惯例」，不改任何 MANIFEST 文件。

### 改动行数汇总

| 文件 | git numstat | 备注 |
|---|---|---|
| `method/references/calibration.md` | +39 / −0 | 第五节整节新增，条文 34 行与提案 §2 diff 为零 |
| `method/SKILL.md` | +2 / −1 | (m) 条 +1 行；第 4 段长行内加一句，strip-back 验合原文零删改 |
| 其余 method 文件（含 chinese-liuren.md） | 0 / 0 | 零改动 |

- 纪律：未做 git 提交（主持统一提交）；未打开任何 predictions／judging／金标。
