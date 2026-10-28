# 西方卷 · 来源说明（SOURCES）

本目录为占卜盲测校准用的「西方大师原断」验证集。收录原则：只用公版原典、逐例可溯源、宁缺毋滥；现代占星师部分由另一分工负责（masters-dataset/modern-masters/），本卷不收。

## 文件

| 文件 | 内容 |
|---|---|
| `inputs.jsonl` | 每例的 subject（被算对象、背景、问题、问卜时刻）+ chart_data 附件（星盘数据，录自大师正文所述） |
| `answers.jsonl` | 与 inputs 同 id 配对：master_predictions（大师原断节录、出处、应验结果） |
| `waite-meanings-baseline.md` | Waite《Pictorial Key》78 张牌义基准集 + 书中示例牌局核查（牌义对齐基准，非案例集） |
| `existing-datasets.md` | 现成数据集盘点（合成型/客观结局型/大师原断型分类与可用性） |
| `pending.md` | 已定位但未能核到干净原文的待办，绝不以转述冒充原断 |
| `auxiliary/` | 原典全文与辅助数据（见下） |

## 主力来源：William Lilly《Christian Astrology》(1647)

- 本卷 15 例全部出自 Book II（卜卦问事卷），每例在 inputs/answers 中标注章节与 1647 年原书页码（按通行重印分页）。
- 全文底本：Internet Archive 馆藏合集 “Christian Astrology, Editions from 1647–2022”，identifier `christian-astrology-1647`：
  - `auxiliary/christian-astrology-vol1-3_djvu.txt` — 1647 年原版扫描 OCR（长 s 字形，个别字形有讹），本卷引文以此为准。
  - `auxiliary/christian-astrology-1647-original_djvu.txt` — 同馆藏 “White Page Edition” OCR，质量较差，仅备查。
  - 在线阅读：https://archive.org/details/christian-astrology-1647
- 交叉校对本：Lilly《An Introduction to Astrology》(1852, Zadkiel 修订本，即 Christian Astrology 前两卷的删节重排本)，本地已存于 `~/workspace/divination/sources/western/lilly-introduction-to-astrology-1852.pdf`。仅在 1647 OCR 字形残缺处用它核对措辞（如逃亡仆人例的结局句、盗窃少年例 Fig. 18 的完整断语），每例 source 字段已注明；断语内容归属 Lilly 本人。
- 版权：Lilly 原文 1647 年出版，早已进入公版（PD）。1852 Zadkiel 本同为公版。Deborah Houlding 的现代重排注释本（1999/2022）有编辑版权，本卷**未使用**。

## 其他原典的核查结论

- **托勒密《Tetrabiblos》（2 世纪）**：通篇为规则/断语体例（Books III–IV 按主题列断法），**不含任何带命主数据的完整本命成例**，无法从中抽取「输入—原断」配对。故本卷不收托勒密案例；其文本作规则基准用（本地：`~/workspace/divination/sources/western/tetrabiblos-ashmand-gutenberg70850.epub`，Ashmand 译，PD-US）。
- **Waite《The Pictorial Key to the Tarot》(1910/1911)**：书中没有「完整占例」，甚至没有一局填入具体牌面的示例牌阵——凯尔特十字一节只有操作程序、十个位置的位置义和一张无牌面的位置图（核查详情见 waite-meanings-baseline.md 第一节；凡声称引自本书的“Waite 示例牌局”均属后人编造或误传）。因此塔罗不进案例集，改以其 78 张牌义原文作「牌义基准集」。原文底本为 Sacred-Texts 公版全文，本地：`~/workspace/divination/sources/western/waite-pictorial-key-sacredtexts.txt`；注意同目录 Gutenberg #43548 是 de Laurence 1918 年影印本，本卷未用它作基准。
- **Lilly Book III 本命卷**：全书结尾附一商人本命盘的完整推断（1616 年 9 月 19 日生），但出生时刻只在盘图内、OCR 不可读，且其逐年推断（1646–1650 各年）在书中无应验记录，暂列 pending，不硬凑为验证例。

## 方法无关性与 cross_ref

按项目新原则：验证以「结论是否与大师一致」为准，与用什么方法算无关。已逐例检查本卷对象是否另有中方大师断过的线索：15 例均为 17 世纪英国本地人事（内战战事、伦敦市民、Lilly 本人），未发现同一对象被中方典籍/大师占断的记录，故各例 notes.cross_ref 均为 null；后续若发现跨体系同题案例，再补标。

## 数据质量说明

- chart_data 只录大师在正文中明言的星位/宫头/相位；盘图本身为图像，OCR 不可尽读，未明言者不推测补全，缺失项在 pending.md 注明。
- outcome 分两种并已在条目内区分：(a) Lilly 书中自记应验；(b) 外部史实核验（如剑桥未陷落、切里顿战役），条目中明标「historical record」，不冒充 Lilly 原文。
- 引文为节录：长断语以忠实转述加关键原句呈现，未改动大师的结论方向与时间判断。
