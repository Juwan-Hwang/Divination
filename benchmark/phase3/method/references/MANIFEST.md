# MANIFEST — 占卜知识库资产总清单

根目录：`/home/hatch/workspace/divination/`。下载/克隆日期：2026-10-29。调研依据：`~/workspace/research_notes/divination-metaphysics-survey-20261028-1713/`（下称「调研报告」）。
口径：来源分级 A 原典 / B 权威注本 / C 现代学术 / D 现代整理 / E 民间说法——**只作标注、不作收录门槛**（最终定调）；唯一验收是与大师结果的一致性（benchmark/）。
内部/公开口径：现阶段内部全量使用；`redistributable` 只决定未来公开发布版的导出过滤，与内部收录、划分、评分无关。

## 类型 1｜传统经典原典与古籍全文（实际下载）
| 资产 | 本地位置 | 来源 | 许可/等级 | 用途 |
|---|---|---|---|---|
| 《周易》经文+文言 | sources/chinese/zhouyi-wikisource.txt | 维基文库 | PD / A | 文本占底本 |
| 《增删卜易》 | sources/chinese/zengshan-buyi-wikisource.txt | 维基文库 | PD / B | 六爻基准+成例源 |
| 《渊海子平》 | sources/chinese/yuanhai-ziping-wikisource.txt | 维基文库 | PD / B | 八字源流 |
| 《梅花易数》卷一至三 | sources/chinese/meihua-yishu-wikisource.txt | 维基文库 | PD / B（托名存疑） | 梅花基准+成例源 |
| 《三命通会》12 卷 | sources/chinese/sanming-tonghui/ | GitHub 镜像（四库本） | 原文 PD、转录 CC BY-SA 4.0 / B | 八字通例 |
| 《大六壬指南》（陈公献） | **未落盘**（在线核读：维基文库分卷子页，2026-10-29 逐卷核对） | 维基文库 | PD / B | 六壬基准：卷一心印赋注/卷二指掌赋注/卷三会纂指南/卷四占验指南，断法章节 references/chinese-liuren.md 出处 |
| 《六壬大全》（四库本） | **未落盘**（在线核读：维基文库，2026-10-29） | 维基文库 | PD / B | 六壬参校：卷一入手法九宗、课目、课经、十二将释 |
| Waite《Pictorial Key》1911 | sources/western/waite-pictorial-key-sacredtexts.txt | Sacred-Texts | PD-US / B | 塔罗唯一对标底本 |
| Waite 文本 de Laurence 1918 影印本 | sources/western/waite-illustrated-key-delaurence1918-gutenberg43548.txt | Gutenberg #43548 | PD-US | 版本对照（按影印本著录） |
| Legge 译《I Ching》1882 | sources/western/iching-legge-sacredtexts.txt | Sacred-Texts | PD / B | 英译对读 |
| 《诗体埃达》Bellows 译（txt+PDF） | sources/western/poetic-edda-bellows-gutenberg.txt、poetic-edda-bellows-gitenberg.pdf | Gutenberg #73533 / GITenberg | PD-US / A | 卢恩 lore 底本 |
| 符文诗 | sources/western/rune-poems-wikisource.txt | 英文维基文库 | PD / A | 符名训诂 |
| 托勒密《Tetrabiblos》Ashmand 译 EPUB | sources/western/tetrabiblos-ashmand-gutenberg70850.epub | Gutenberg #70850 | PD-US / A | 占星规则原典 |
| Lilly《Introduction to Astrology》1852 PDF | sources/western/lilly-introduction-to-astrology-1852.pdf | Internet Archive | PD / B | 卜卦占星 |
| Cheiro《Book of Numbers》 | sources/western/cheiro-book-of-numbers-archive.txt | Internet Archive DLI | 许可存疑从严 / D（史料） | 数字命理史料 |
| ctext.org《周易》 | **未下载**（只在线读） | https://ctext.org/book-of-changes/xi-ci-shang | ToS 禁批量抓取 | 在线查读 |

## 类型 2｜GitHub 开源（实际克隆，tools/repos/ 与 tools/datasets/）
stars/forks 为 2026-10-29 gh api 实测；HEAD 为本地克隆短哈希。
| 仓库 | 位置 | stars/forks | 许可证 | HEAD | 用途 |
|---|---|---|---|---|---|
| 6tail/lunar-python | tools/repos/lunar-python | 685/169 | MIT | 448f397 | 八字/历算主库（EightChar） |
| yuangu/sxtwl_cpp | tools/repos/sxtwl_cpp | 258/— | BSD-3-Clause | —（克隆时未记） | 寿星天文历，节气交叉核对 |
| SylarLong/iztro | tools/repos/iztro | 4272/690 | MIT | 163606d | 紫微排盘事实标准 |
| aloistr/swisseph | tools/repos/swisseph（稀疏检出 src/doc/contrib，26 MB） | 737/265 | **AGPL / 商业双许可（CHF 700）** | 94621ab | 星历引擎与 .se1 数据（仓库完整版含 ephe，本机只取核心并注明） |
| astrorigin/pyswisseph | tools/repos/pyswisseph | 404/106 | AGPL-3.0 | 91ec656 | Swiss Ephemeris Python 绑定 |
| Harry-commit/lifekline | tools/repos/lifekline-harry | 35/52 | **无 LICENSE（默认版权）** | 33693c7 | 方法研究对照（只提炼，见 lifekline-method.md） |
| curionox/lifekline | tools/repos/lifekline-curionox | 776/566 | **无 LICENSE** | b9a27a7 | 同上（增强重打包版） |
| ekelen/tarot-api | tools/datasets/tarot-api | 412/— | 未声明 | — | RWS 牌义 JSON（源出 Waite） |
| metabismuth/tarot-json | tools/datasets/tarot-json | 81/23 | MIT | — | 塔罗数据集 |
| godcong/yi | tools/datasets/godcong-yi | 34/— | MIT | — | 易经 JSON 数据（gua/wenyan 等） |
| FENGTING2025/iching-64-hexagrams-json | tools/datasets/iching-64-hexagrams-json | 1/0 | 未声明 | — | 64 卦 JSON 比对（低权重） |
| mikkokotila/Sanming-Tongshui | sources/chinese/sanming-tonghui | 0/— | PD/CC BY-SA 4.0 | — | 见类型 1 |
未克隆（生态登记）：PyPI `qimendunjia`（奇门）、`kinliuren`（六壬）、`kerykeion`（占星上层）、tarot/bazi MCP servers——见调研报告 02 卷；六爻装卦库与梅花体用库为**生态空白**（无公认开源实现）。awesome-divination 类清单仓未发现有影响力者（负结果）。

## 类型 3｜学术与严肃研究（实际下载 sources/academic/，著录见该目录 SOURCES.md）
已下 5 篇 OA：Kotyk 印度天文学入华（Religions 2024, CC BY）、Picatrix 占卜实践（Religions 2024, CC BY）、Silva 篮占民族志（Religions 2014, CC BY）、Adler 朱熹占卜观章节（大学主页公开）、Hao 评 Shaughnessy 周易起源研究书（Dao 2024, OA）。
只记 DOI 未下：Dummett 10.1017/S1062798700000478（塔罗史，非 OA）；Raphals 2013 中希占卜比较（©）；Shaughnessy 2019 DOI 10.1515/9781501516948（OA，本轮未取文件）；低层级期刊塔罗计量文 DOI 10.35629/5252-0702551583 只作弱文献样本，不引为权威。

## 类型 4｜权威数据库与工具站（参照源，多为在线/库内数据）
- Swiss Ephemeris（Astrodienst）：星历金标准，数据文件 .se1 随类型 2 swisseph 仓分发（AGPL/商业双许可已注明）；官方说明页见调研报告。
- 寿星天文历 sxtwl/sxwnl：中国历算参照（已克隆 sxtwl_cpp + pip 版实测）。
- 6tail lunar 数据层：万年历/节气/干支结构化数据（已克隆）。
- astro.com 在线排盘、jadealmanac 约定对照页：仅作交叉核对参照（在线，未下载）。

## 类型 5｜现代权威整理本与教程
- `references/chinese-liuren.md` 大六壬断法章节（2026-10-29 补建）：据《大六壬指南》卷一至卷四与《六壬大全》卷一/课目/课经在线核读整理——起课与九宗取传、课格、十二天将、类神总表、分类占断十二门、应期推法，末附盘面不全作断规矩（本库衔接项）与精通检查表。
- `references/chinese-qimen.md` 奇门遁甲断法章节（R57 接入，效力自 R58 起算）：据张志春《神奇之门》为主干、杜新会《奇门遁甲现代实例精解》为补编（两书同源不作双重互证）；排局默认拆补法。
- Adler 易学书目与朱熹研究（已下，类型 3）。
- bookofchanges.academy《梅花易数》转录+托名考证（D，在线参照，未下载——维基文库本已覆盖原文）。
- iztro 官方文档（随类型 2 仓库）：紫微安星现代标准整理（D）。
- lifekline 两仓（类型 2）：现代 AI 应用样本，方法提炼见 lifekline-method.md。
- mingming3 紫微版本史专页（D/C，在线参照）：化科分歧依据。

## 类型 6｜数据集类（机器可读）
| 数据集 | 位置 | 内容 | 许可/来源 |
|---|---|---|---|
| hexagrams-64.json | tools/datasets/local/ | 64 卦序/上下卦/爻位二进制（程序自洽校验） | 自建（据 A 级结构） |
| tarot-78.json | tools/datasets/local/ | 78 牌名+正逆位关键词（逆位通则处已注明） | 自建整理（D），牌义基准仍为 Waite 原文 |
| runes-24.json | tools/datasets/local/ | 24 符名/音/训诂 | 自建（据 A 级材料重构名） |
| ganzhi-jieqi.json | tools/datasets/local/ | 干支/六十甲子/节气表 | 自建（历算规则） |
| tarot-api card_data.json | tools/datasets/tarot-api/static/ | 78 牌义 JSON | 未声明许可，源出 Waite |
| tarot-json | tools/datasets/tarot-json/ | 塔罗 JSON 数据集 | MIT |
| godcong/yi data/*.json | tools/datasets/godcong-yi/data/ | 卦/文言/甲子等 JSON | MIT |
| **MastersDivination Benchmark** | masters-dataset/（data/dev.jsonl、data/test_inputs.jsonl、holdout/test_gold.jsonl、splits.json）+ 分卷 chinese-natal/(45 例)、western/(15 例)、modern-masters/(predictions 12 + 占例 10) | 大师成例验证集：subject+context+master_predictions+outcome | 逐条 license_status/redistributable（内部全量，见 masters-dataset/SCHEMA.md） |

## 类型 7｜多媒体（链接清单，未下载大文件）
- 调研报告所引公开课/讲座以在线链接形式存于报告各卷（如 Adler 课程书目页、DeepWiki 各仓文档）；本轮未单独建多媒体清单文件，优先级最低，后续按需补 `sources/media-links.md`。

## 失败/部分清单（不静默跳过）
| 条目 | 结果 | 原因 |
|---|---|---|
| ctext 全文下载 | 未下（合规决定） | 站方明令禁批量抓取、对爬虫返回污染数据；只在线读 |
| 《周易》十翼（系辞/说卦/序卦/杂卦/彖/象） | 未取得 | 维基文库「周易/繫辭上」等标题 404；仅得文言 |
| 《滴天髓》全文 | 仅得目录篇 2,559 B | 维基文库该条目仅目录/首篇 |
| 《卜筮正宗》《子平真诠》《紫微斗数全书/全集》《京氏易传》全文 | 未取得 | 调研报告亦未核实到逐字直链，不杜撰路径；待 masters-dataset/后续轮次补 |
| 《梅花易数》首抓 | 先只得主页 3,865 字，后补卷一至三子页达全三卷 | 已修复，见类型 1 |
| Cheiro djvu /stream/ 路径 | 返回 HTML 页（假成功） | 改 /download/ 路径取得正文，已修复并在 SOURCES 注明 |
| Gutendex（Gutenberg API 镜像） | 503 | 改走 Gutenberg 站内检索+直链，已取得 |
| OpenAlex 学术检索 | HTTP 429 | 按规矩硬停，未重试；改用出版社 OA 直链与机构仓储 |
| arXiv 检索（I Ching/tarot） | 无结果返回 | 该库无相关条目，如实记负结果 |
| swisseph 全量克隆 | 中断（229 MB 未检出） | 改稀疏克隆（src/doc/contrib，26 MB）；ephe 数据文件未全量取，注明 |
| iztro-py 紫微对标 | 接口与文档不一致（by_solar_date 不存在） | 校准未完成项，见 calibration.md 2.8 |
| 左传占例（陈完观之否等） | 未取得原文 | 维基文库分卷标题多次试取未命中；benchmark 待补 |
| 塔罗大师实占成例 | 无 | Waite 书中无完整实占成例；benchmark 待补，不拿现代营销书冒充 |

## 暂不采用清单（原「已剔除」，按最终定调改口径）
收录原则：无大师背书 **且** 明显让结果偏离大师者才入此单；若盲测迭代证明某条反而提升一致性，可移回收录并在 benchmark/iterations.md 记明。入单条目只作避坑记录，解卦时不得引用为依据。
| 条目 | 理由 | 等级 |
|---|---|---|
| 卢恩空白符文（Wyrd） | 1982 年 Ralph Blum 发明，无任何古典/大师传统背书 | E（现代发明） |
| 卢恩现代抽符正逆位断法体系（merkstave 断语全套） | 20 世纪建构；符文诗只有训诂、无断语；与 Tacitus 唯一记载不合 | E |
| 塔罗「古埃及起源」叙事 | 无证据，Waite 本人否认；学术共识为意大利纸牌起源 | E（伪史） |
| BTB 黑帽风水 | 20 世纪西方发明，与形势/理气两传统大师体系均不合 | E |
| 数字命理「毕达哥拉斯起源」说法 | 毕氏无著作传世、古代无此法；品牌攀附（算法本身保留为民俗，起源说不用） | E |
| lifekline「禁止平滑、强造波动」提示词手法 | 为视觉效果编数据，直接拉低与大师依据链的一致性 | 现代产品手法 |
| 各类「AI 直编排盘/分数」无计算层应用 | 无可复核计算，与本库计算基准冲突 | — |

## 转录规矩（全库适用）
扫描件/影印中 OCR 不可读处（盘图、speculum、题头、手写字）用多模态视觉读图转录，标注 transcription=visual + 置信度，关键数据（出生时刻、干支、度数）须与上下文规则交叉验证；不许因 OCR 失败放弃或臆补（详见 README.md）。
