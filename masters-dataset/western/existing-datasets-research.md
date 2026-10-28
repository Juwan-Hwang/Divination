# 现成「算命/占卜大师案例」数据集盘点：真伪与用途

- 核实日期：2026-10-29（Asia/Shanghai）
- 核实方式：GitHub API（本地 gh CLI v2.102.0，账号 Juwan-Hwang）、Hugging Face 数据集页面、arXiv 论文原文、仓库文件树与 Release 资产清单、下载文件本地实数。凡只来自项目自述而未独立复算的数字，都标注「自述」；搜不到的如实写搜不到，不编造。
- 本目录说明：任务目录名为 `western/`，但清单本身以八字/紫微等东方术数为主、兼及塔罗与西方占星，按任务清单原样盘点，未改范围。

## 分类口径

| 类别 | 定义 |
|---|---|
| 大师原断型 | 真人命理师针对真实命主写下/出示的题目与断语，答案不是整理者编的 |
| 客观结局型 | 题目答案锚定命主真实人生事件（可客观对错），但题目本身可由他人/LLM 事后编制 |
| 合成生成型 | 由算法、排盘引擎或 LLM 批量生成，没有真实命主与真实结局作锚 |
| 经典文本/牌义库（附加类） | 古籍原文、牌义、卦辞等工具书数据；不含任何案例，先单列以免混入上面三类 |

## 总览

| # | 数据集 | 规模（实查） | 生成方式 | 许可 | 分类 | 能否作盲测验证集 |
|---|---|---|---|---|---|---|
| 1 | HF `viveriveniversumvivusvici/bazi_comprehensive_dataset` | 1,000 条（HF 页面） | custom algorithm 系统生成 | **未标注** | 合成生成型 | ❌ 无真实结局，且样本含非法干支组合 |
| 2 | GitHub `MirrorAI-Lab/BaZi-Persona`（Celebrity50） | 50 人 / 488 题（下载实数） | 真人传记（astro.com 出生资料）+ Qwen LLM 生成题目 | **仓库无 LICENSE** | 客观结局型（题目为 LLM 合成） | ⚠️ 有条件可用：须剥离身份信息、且答案分布严重偏斜（B 占 62.5%） |
| 3 | GitHub `ChenJiangxi/BaziQA`（本次新发现） | 555 道真题 / 117 命主（逐文件实数） | 全球算命师大赛 2010–2026 历届真题转写 | 代码/转写 MIT；题目著作权属主办方与出题人、仅供研究 | **大师原断型＋客观结局型** | ✅ 本批最佳：命主匿名、官方答案、有人类冠军基线 |
| 4 | GitHub `Renhuai123/ziwei-doushu` | 仓库本体约 2.7 MB；Release 数据集 v3 518,400 条、v4 674,976 盘（自述＋资产清单核对） | 排盘引擎＋**闭源断语库**确定性批量生成 | 代码 MIT；数据集 CC BY 4.0（须署名）；倪海厦原话 CC BY-NC-SA 4.0 | 合成生成型（另含 1,848 条倪海厦原话语料） | ❌ 穷举日期网格、无真人结局，无法评分对错 |
| 5 | GitHub `ekelen/tarot-api` | 78 张牌（文件实数） | 解析 A. E. Waite《The Pictorial Key to the Tarot》 | **仓库无 LICENSE** | 经典文本/牌义库 | ❌ 只有牌义、无案例无结局 |
| 6 | Kaggle `lsind18/tarot-json`（Tarot Deck） | 78 张牌＋牌图 7.37 MB（Kaggle 页面自述，未本地下载核验） | Rider-Waite 牌义＋扫描图整理 | Kaggle 页面称 MIT | 经典文本/牌义库 | ❌ 同上 |
| 7 | Astro-Databank（Astrodienst） | 公开人物 74,000 条＋研究数据 6,629 条（官网主页） | 人工编辑收集出生资料、传记与人生事件，带 Rodden Rating 来源评级 | 浏览免费；XML 全量导出须签许可协议换密码，免费子集仅 4,000 余条 | 客观结局型**原料**（无大师断语、非成品数据集） | ⚠️ 只能自建题库（Celebrity50 即以 astro.com 为源），不能直接拿来测 |
| 8 | 易经类（`godcong/yi` 等） | 64 卦及卦爻辞（库自述） | 古籍文本结构化 | MIT（`godcong/yi`，据 pkg.go.dev 页） | 经典文本/牌义库 | ❌ 无案例型易经数据集被找到 |

---

## 1. Hugging Face：viveriveniversumvivusvici/bazi_comprehensive_dataset

- 链接：https://huggingface.co/datasets/viveriveniversumvivusvici/bazi_comprehensive_dataset （作者 BENIDO，为 AstroAlchemy Web3 dApp 微调 Mistral 而作）
- 规模：**1,000 条**。HF 查看器显示 subset `default · 1k rows`，README「Dataset Statistics」亦称 Total Samples: 1,000。文件字节数页面未给出，未实查到，不填。
  - 注：本次读取的是 HF 镜像站缓存页（页面标注爬取于 2026-06-10），行数与 README 口径互相一致；若后续引用精确文件大小，需再走 HF 官方 API 复核。
- 字段：JSONL，每行仅两字段——`input`（字符串：年/月/日/时四柱、五行计数、藏干、当前流年；长度 130–154 字符）、`output`（字符串：财富/感情/事业/健康/日常五域建议＋幸运方位＋风险警告；长度 766–1,210 字符）。
- 生成方式：**合成**。README「Generation Methodology」原文：*Each entry was created using a custom algorithm that ensures diversity while maintaining BaZi principles*，与任务给定的已知自述一致。
- 数据质量红旗（页面样本直接可见）：多条样本出现「乙子」「己子」等**不在六十甲子内**的干支组合（如 `Year: 乙子`、`Day: 乙子`），说明其算法连干支合法配对都未约束——不只是「合成」，而且合成得不正确。
- 许可：**未标注**。在 HF 页面与 README 全文中检索不到 license 字样；上月下载量 9。未标注许可不等于可自由使用，商用/再分发前须另行取得授权。
- 分类：合成生成型。
- 盲测可用性：❌。没有任何真实人物、真实事件或可核对的答案，output 是模板化建议文本，无对错可言；加上干支合法性错误，连作「排盘规则一致性」样本都不合格。至多当反面教材：识别「AI 批量造命理语料」的典型形态。

## 2. GitHub：MirrorAI-Lab/BaZi-Persona（Celebrity50）＋论文 arXiv 2510.23337

- 链接：https://github.com/MirrorAI-Lab/BaZi-Persona ；论文 https://arxiv.org/abs/2510.23337（*BaZi-Based Character Simulation Benchmark*）
- 仓库实况（gh API，2026-10-29）：仓库仅 **2 个文件**——`Celebrity50_zh.json`（500,716 字节）与一行说明的 `README.md`（104 字节）；仓库大小 162 KB；**license 字段为 null、仓内无 LICENSE 文件**（任务要求注明：此仓无 LICENSE 记录，使用/再分发无法务依据，引用时只能按学术引用惯例并注明来源）。
- 论文口径：50 位名人、29 个国家、488 道人生事件选择题（人均 9.76 题），男 37 / 女 13；出生资料经 astro.com 收集核验；五维分类：财富、健康、六亲、事业、感情。
- 生成方式（论文 §3 及 Limitations 自述）：先取真实出生时间 → 用 **Qwen API** 检索/汇总人物传记叙事 → **同一个 LLM 据此生成选择题** → 脚本拼装 JSON，作者人工清洗过滤。论文明说局限：*many narratives and questions are LLM-generated (by Qwen), introducing potential hallucination, bias, and factual errors*。
- 下载核对（已下载，见文末）：本地文件 500,716 字节，与 GitHub 记录逐字一致。实数结果：
  - 顶层为数组，**50 人**；`questions` 合计 **488 道**（每人 8–10 道，均值 9.76），与论文一致。
  - 每人字段：`person_id`、`name`、`profile{birth{year,month,day,hour,minute,place,raw,raw_candidates,approximate}, gender}`、`categories{感情,财富,六亲,事业,健康}`（传记事件条目）、`questions[{question_id, question, options, answer}]`、`source_file`。
  - 选项数：487 题为 5 选 1、1 题为 4 选 1。
  - **答案分布严重偏斜（实数）：A 41、B 305、C 120、D 20、E 2——B 占 62.5%。** 不做平衡处理时，「全选 B」即可得 62.5%，原始准确率数字没有意义。
  - 出生年份跨度实测 1881–1997，与论文「born around 1940」的筛选表述对不上（论文口径与文件实况有出入，引用时以文件为准）。
  - 另注意：`ChenJiangxi/BaziQA` 仓内也有一份 `data/celebrity50_zh.json`（491,767 字节），实数同为 50 人 / 488 题，但字节数与本仓版本不同（字段有增删），两份不要混用、引用须注明出处仓。
- 分类：客观结局型——答案锚定真实人生事件；但题面由 LLM 合成，非大师原断。
- 盲测可用性：⚠️ 有条件可用。理由与前置处理：
  1. 命主全是名人，`name`、`categories` 直接写明身份与生平——盲测前必须只保留出生信息＋题目，剥离 `name/categories/source_file`，否则模型靠记忆/检索即可作答，测的不是命理推理；
  2. 必须处理答案偏斜（重排选项顺序并同步改答案键，或按选项位置分层报告），否则成绩虚高；
  3. 题目由 Qwen 按传记反向生成，题干常带「命主感情宫显示……」式的事后叙事，且论文自认可能有幻觉与事实错误，小样本（50 人）下个别错题对结论影响大。

## 3. GitHub：ChenJiangxi/BaziQA（本次新发现，本批价值最高）

- 链接：https://github.com/ChenJiangxi/BaziQA ；论文 https://arxiv.org/abs/2602.12889
- 来源：香港青年術數家協會「全球算命師大賽」2010–2026 年共 17 届真题。每道题由专业命理师（约 70 位出题人）以一位**真实命主**出题，正确答案即命主真实经历；主办方逐年公布答案与冠军成绩。
- 规模实数（浅克隆后逐文件数）：`data/` 下 17 个比赛文件合计 **555 道题、117 位命主**，与仓库 README 的「555 道 / 117 命主」一致；另附 Celebrity50 副本一份（见 §2）。仓库大小约 8.6 MB（gh API size 8,591 KB），含 `sources/` 原题图片与官方答案表存档、`charts/` 八字/紫微排盘、评分脚本。
- 口径差异（须分清）：**论文**（arXiv 2602.12889）只用了其中 2021–2025 年的 **200 题**（每年 8 命例 × 5 题）做实验；**仓库现版**已扩展到 2010–2026 全量 555 题，且 v2 对 v1 转写错误做过逐字校正（README 列明 32 处改变题意的文字错误等）。新实验应使用仓库现版，不要拿论文的 200 题口径当全量。
- 答案可靠性分层：555 题中 **365 题为官方公布答案，190 题为转载站答案**（官方原档已佚；仓库称转载与可比对的官方答案 283 题逐题一致）。使用时可按文件内 `answer_source` 字段一键排除转载部分。
- 人类基线：历届冠军正确率 43%–78%（随机猜测 25%，个别早期年份为 5 选 1 即 20%），可直接把模型成绩放入人类排名对照——这是其他数据集都没有的。
- 生成方式：人工转写＋逐题对源核对，非生成。命主多为普通人、已匿名化（`name` 形如「1940年台湾出生女性」），不存在 Celebrity50 的名人记忆泄漏问题。
- 许可：仓库 LICENSE 为 MIT，但文件末尾有附加说明：**比赛题目著作权属香港青年術數家協會与各出题人，本仓 MIT 只覆盖其转写、元数据与代码，题目仅供研究使用并逐题署名**。GitHub API 因此将该仓许可识别为 `Other / NOASSERTION`。按「研究可用、勿商用再分发题目原文」理解最稳妥。
- 分类：大师原断型＋客观结局型（本批唯一兼具两者）。
- 盲测可用性：✅ 可直接用作盲测验证集。理由：真实命主、匿名、官方答案键、客观可评分、有人类冠军基线、附排盘与评分脚本。注意事项：①190 道转载答案题建议单独标注或排除后做敏感性分析；②个别特殊题（如 2013 年第 16 题是反推出生时辰、命主 `hour` 为 null）在仓库 README 已逐一列明，跑测前先读；③题目含八字/紫微/奇门混合构成，`setter.method` 字段可按术数过滤，只测八字时不要混入紫微题。

## 4. GitHub：Renhuai123/ziwei-doushu——排盘引擎与「56.6 GB 数据集」的实况区分

- 链接：https://github.com/Renhuai123/ziwei-doushu （代码 MIT，8,889 stars / 1,784 forks，gh API 2026-10-29）
- **仓库本体不是数据集**：gh API 仓库大小 2,689 KB，文件树共 149 项，主体是 Next.js 排盘应用——排盘引擎 `lib/ziwei/`（algorithm.ts、sihua.ts、patterns.ts 等）、页面与组件、古籍原文数据 `lib/classics/data/`（骨髓赋、全集、全书的摘录 TS 文件，单文件仅数 KB）。
- 仓内真实数据只有两小块：
  1. `docs/tianji-ziwei/`：倪海厦《天纪》紫微部分**原话语料 1,848 条**（`entries.jsonl` 739,532 字节，本地实数 1,848 行，与其 README 一致），每条带 B 站视频时间码出处。这是本仓唯一接近「大师原话」的部分，但它是讲课断语摘录、**不是命例原断**；许可 CC BY-NC-SA 4.0（非商业）。
  2. `lib/ziwei/famous.ts` 等少量名人示例盘，仅供演示。
- **所谓数据集在 Releases，不在仓库**（此前调研口径需按此修正）：
  - v3.0 样本数据集（Release `v3.0-samples`，2026-05-07）：自述 518,400 条；资产为 3 个分卷 zip，实查合计 5,878,229,556 字节（约 5.88 GB），README 称解压后 33.1 GB。覆盖为 1924–1983 × 每月 1–30 日 × 12 时辰 × 男女的**穷举网格**；自认约 2,520 条是 2 月 30 日等不存在的日期（已在 README 明示过滤方法）。
  - v4.0 解读数据集（Release `v4.0-13d`，2026-10-15）：自述 674,976 张命盘（1950–2026 真实日期 × 12 时辰 × 男女）× 13 维 = 8,774,688 段解读，**解压后 56.6 GB**——「56.6 GB」是解压后体积，不是下载体积：实查 Release 资产为 77 个按年 `.jsonl.zst`（每个约 2 MB）＋全量 tar 包 161,490,432 字节，资产总计 322,920,204 字节。字段每盘一行 JSONL：`k/y/m/d/h/g/ms/t/c`（c 为 13 维解读全文）。
- 生成方式：**排盘引擎＋断语库确定性批量生成，不经 AI**（README 原文：「排盘引擎 + 断语库确定性生成，不经 AI，同一输入恒得同一输出」；DATASET-LICENSE 亦自述「本数据集由排盘引擎批量生成」）。
- **判词/断语库闭源——属实**：README 第七章「开源边界」明说断语库不开源，仓内 `lib/ziwei/db-analysis.ts` 只是 2,124 字节的占位文件，线上是「上万行的 13 主题断语」；AI 解读 prompt、后端 API 同样不开源。也就是说：数据集是这套闭源断语库的**输出快照**，生成规则本身拿不到、无法审计。
- 许可：代码 MIT；v3/v4 数据集按仓内 `DATASET-LICENSE` 以 **CC BY 4.0** 口径发布（可商用，唯一要求署名「紫微斗数开源样本/解读数据集，来源 github.com/Renhuai123/ziwei-doushu，作者 王多鱼AI」）；但解读中引用的倪海厦原话被明确排除在该授权之外（按 CC BY-NC-SA 4.0 处理），古籍原文为公有领域。
- 分类：合成生成型（引擎批量演绎文本；输入是穷举的日期网格，不是真实命主个案）。
- 盲测可用性：❌。没有任何真实人物的结局标签，解读对错无从评分；它能验证的只有「你的引擎输出与它的引擎输出是否一致」。适合的用途是：微调/RAG 语料、排盘口径对照基线、《天纪》断语风格参考。另 1,848 条倪海厦原话可作大师断语风格语料，但规模小且非命例形式，同样不能作验证集。

## 5. GitHub：ekelen/tarot-api（塔罗牌义）

- 链接：https://github.com/ekelen/tarot-api （412 stars，gh API 2026-10-29）
- 规模实数：数据源 `static/card_data.json` 80,041 字节，本地解析实数 **78 张牌**（Rider-Waite-Smith 全套）；字段：`name, name_short, type, suit, value, value_int, meaning_up, meaning_rev, desc`。
- 生成方式：整理/解析型——README 自述内容 parsed from A. E. Waite's *The Pictorial Key to the Tarot*（1910 年，公有领域文本），仓内 `scraper/` 还留有原始抓取文本（maj_text.json / min_text.json）。
- 许可：**仓库无 LICENSE**（gh API license 为 null，文件树无 LICENSE 文件）。底层 Waite 文本已进入公有领域，但这份 JSON 编纂本身的授权未声明，商用前需注意。
- 分类：经典文本/牌义库。
- 盲测可用性：❌。只有单牌牌义，没有牌阵案例、没有问卜者结局，无法构成验证集；用途是给解读生成提供牌义检索源。

## 6. Kaggle：lsind18/tarot-json（Tarot Deck）

- 链接：https://www.kaggle.com/datasets/lsind18/tarot-json （作者 Daria Chemkaeva，约 7 年前更新）
- 规模（Kaggle 页面自述，**未本地下载核验**——Kaggle 下载需登录，本次只核页面）：`tarot-images.json` 含 **78 张牌**（字段：name、number、arcana、suit、img、fortune_telling、keywords、meanings{light, shadow}、Questions to Ask 等），另附 `cards` 文件夹 Rider-Waite 扫描图 350×600px、合计 7.37 MB。
- 生成方式：人工整理牌义＋牌图扫描。
- 许可：Kaggle 页面称「available as open source under the terms of the MIT License」，并注明原版 Rider-Waite 在作者去世 70 年以内版权期国家属公有领域（牌图在更长版权期法域的状态需自行判断）。
- 分类：经典文本/牌义库。
- 盲测可用性：❌。同 §5，只有牌义与牌图，无案例无结局。

## 7. Astro-Databank（Astrodienst，astro.com）

- 链接：https://www.astro.com/astro-databank/ ；导出说明 https://www.astro.com/astro-databank/Help:XML_export_format
- 规模（官网主页本次检索所见，数字逐日增）：Public Figures and mundane data **74,000** 条、Research data **6,629** 条、Private data 2,649 条（仅工作人员）。（站外常引的「20,000 名人」是其旧标题，已过时。）
- 内容与生成方式：人工编辑收集的**出生资料（日期/时间/地点，带 Rodden Rating 出生时间可信度评级）、传记与人生事件、关系数据**；Astrodienst 2009 年收购，编辑团队持续更新。它是西方占星研究界事实标准的出生数据库——Celebrity50 的出生资料正是取自 astro.com。
- 可下载性（实查其 XML 导出帮助页）：**不是点开即下的开放数据集**。帮助页写明：全量 XML 导出须先下载许可文件、签字扫描后发邮件申请，收到密码才能解压，且「only serious researchers will be accepted」；下载页另有一个**免费子集（4,000 余条，以字母 C 开头的条目）**供研究者先行开发工具。网页端逐条浏览则免费。
- 许可：按其导出许可协议（研究用途），非开源许可；再分发受限。
- 分类：客观结局型**原料**——有真实出生＋真实事件，但没有大师断语、没有现成题目。
- 盲测可用性：⚠️ 不能直接用，须自建：从中抽取人物 → 把人生事件改写为题目/标签 → 剥离身份信息，才能得到一个 Celebrity50 式验证集（且名人子集同样有记忆泄漏问题，宜优先用其非名人的 Research data 并做匿名化）。它的价值在于规模与出生时间评级，是自建西方占星验证集时最可信的原料来源。

## 8. 易经 / 其他方向的检索结果（多为否定结论）

- 易经：多轮检索只找到**经典文本结构化**项目，如 GitHub `godcong/yi`（Go 库，`data/` 下 64 卦及彖/象/文言/解卦 JSON，MIT，据 pkg.go.dev 页面）、Rust crate `i-ching`（基于 adamblvck 整理的 Wilhelm-Baynes 译本数据：64 卦、384 爻辞，MIT，据 lib.rs 页面）。**没有找到任何「占卜案例＋真实结局」形态的易经数据集**，故无条目可列；这类库只能作卦辞检索源，不能作验证集。
- Hugging Face `pokkoa/positive-interpretation`：自称易经卦象问答集，但原文本已做 tokenize＋hash 处理、**不可逆还原**（其页面 Privacy Notice 明示），实际内容读不出来，不能用；其行数在检索结果中未显示，未核实，不填报数。
- Kaggle：在 Kaggle 站内以 tarot / horoscope / iching / bazi 检索，除 §6 的塔罗牌义集外，**没有搜到**命理案例型或结局型数据集（命中的多为无关的预测类数据集与 Notebook，如用出生日期做星座预测演示的 Notebook，其输入数据并非独立发布的占星数据集）。如实记录为：Kaggle 上暂无可用的大师案例/结局数据集。
- 另有一条线索未独立核实、不计入正式清单：dev.to 文章称某 78 张塔罗牌义集同步发布于 Kaggle（Complete Tarot Card Meanings）与 Hugging Face（tarot-card-meanings-78），本次未打开其 HF/Kaggle 页面核对规模与许可，仅作待查线索。

---

## 结论：哪套能用、怎么用

1. **要「大师原断＋客观答案」的盲测集，现成里只有 BaziQA（§3）真正达标**：比赛真题、真实匿名命主、官方答案、人类冠军基线齐全，且已下载通道与评分脚本俱全。本项目的盲测验证应以它为第一选择（建议主用 365 道官方答案题，190 道转载题作敏感性对照）。
2. **Celebrity50（§2）是次选的客观结局型**：已下载到本地（见下）。用之前必须做两件事——剥离姓名与传记字段防记忆泄漏、重排选项消除 B 选项 62.5% 的偏斜；且要记得题目是 Qwen 按传记反向生成的，测的是「据八字信息反推人生」而非大师断法本身。
3. **其余全部不是验证集**：HF bazi_comprehensive 与紫微 v3/v4 都是合成生成型（前者算法粗糙到出现非法干支，后者是闭源断语库的引擎输出快照），只能当训练/风格语料；塔罗与易经的现成数据全是牌义/卦辞工具书；Astro-Databank 是需要申请许可、自建题目的原料库。
4. 一句话真伪总结：市面上自称「命理数据集」的大体量产品（千条、五十万盘、56.6 GB）无一例外是机器合成；凡有真实命主与真实答案的，规模都很小（488 题、555 题）——这正是自建大师案例集的机会所在。

## 附：Celebrity50_zh.json 下载核对记录

- 下载位置：`~/workspace/divination/masters-dataset/western/auxiliary/Celebrity50_zh.json`
- 下载方式：gh CLI 调 GitHub API 取 `MirrorAI-Lab/BaZi-Persona` 仓 `Celebrity50_zh.json` 内容解码落盘（2026-10-29）。
- 文件大小：500,716 字节（与 GitHub 记录一致）；SHA-256：`e87e6493929f8ec00a9584d2d5a89adab3d39b292f179f33866b8a801e5ebeef`
- 实数：50 人、488 道题（每人 8–10 道）；结构与字段见 §2。许可状态：源仓无 LICENSE，本地副本仅作研究盘点用。
