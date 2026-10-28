# 现成数据集盘点（existing-datasets）

核实日期 2026-10-29，逐项实查（GitHub API / HF 页面 / arXiv 论文 / 下载文件本地实数）。详细核查过程见同目录 `existing-datasets-research.md`，本文件是结论版。

分类口径：**大师原断型**（真人命理师对真实命主的题目与断语）／**客观结局型**（答案锚定真实人生事件，但题目可由他人或 LLM 事后编制）／**合成生成型**（算法/引擎/LLM 批量生成，无真实命主与结局锚）。只有前两类可进验证体系。

## 总表

| 数据集 | 规模（实查） | 许可 | 分类 | 验证集可用性 |
|---|---|---|---|---|
| GitHub `ChenJiangxi/BaziQA` | 555 题 / 117 命主（2010–2026 全球算命师大赛 17 届真题） | 转写与代码 MIT；题目著作权属主办方与出题人，仅供研究 | **大师原断型＋客观结局型** | ✅ **最佳**：真实匿名命主、官方答案、人类冠军基线（43%–78%） |
| GitHub `MirrorAI-Lab/BaZi-Persona`（Celebrity50） | 50 人 / 488 题（下载实数） | 仓库无 LICENSE | 客观结局型（题目由 Qwen 按传记生成） | ⚠️ 有条件：须剥离姓名/传记防记忆泄漏，且答案 B 占 62.5% 须重排选项 |
| Hugging Face `viveriveniversumvivusvici/bazi_comprehensive_dataset` | 1,000 条 | 未标注 | 合成生成型（custom algorithm 自述） | ❌ 且质量差：样本含「乙子」等非法干支组合；只能当反例 |
| GitHub `Renhuai123/ziwei-doushu` 的 Release 数据集 | v3 518,400 条 / v4 674,976 盘（解压 56.6 GB） | 数据集 CC BY 4.0；代码 MIT；断语库**闭源** | 合成生成型（排盘引擎＋闭源断语库确定性生成） | ❌ 穷举日期网格、无真人结局；仅作排盘口径对照/风格语料。仓内另有倪海厦《天纪》原话 1,848 条（CC BY-NC-SA），是讲课断语摘录，非命例原断 |
| GitHub `ekelen/tarot-api` | 78 张牌牌义 | 仓库无 LICENSE（底层 Waite 文本公版） | 经典文本/牌义库 | ❌ 无案例无结局；作牌义检索源 |
| Kaggle `lsind18/tarot-json` | 78 张牌＋牌图 7.37 MB（页面自述，未下载核验） | 页面称 MIT | 经典文本/牌义库 | ❌ 同上 |
| Astro-Databank（Astrodienst） | 公开人物 74,000＋研究数据 6,629（官网） | 全量 XML 导出须签许可申请；免费子集 4,000 余条 | 客观结局型**原料**（出生资料＋事件，带 Rodden 评级，无大师断语） | ⚠️ 不能直接用；是自建西方占星验证集最可信的原料（Celebrity50 即源于此） |
| 易经类（`godcong/yi` 等） | 64 卦卦爻辞结构化数据 | MIT | 经典文本库 | ❌ 未找到任何「占例＋真实结局」型易经数据集 |

## 关键结论

1. **现成可用的验证集只有 BaziQA 完全达标**，Celebrity50 改造后次选。BaziQA 细节：555 题中 365 题为官方公布答案、190 题为转载站答案（可用 `answer_source` 字段排除）；命主已匿名，无名人记忆泄漏；附排盘与评分脚本；跑测前先读其 README 的特殊题说明，混合题按 `setter.method` 过滤。
2. **大体量「命理数据集」无一例外是机器合成**：HF 的 1,000 条、紫微的 518,400/674,976 盘，都没有真实命主与真实结局，无法评分对错。紫微数据集此前调研所称「56.6 GB」是 v4 解压体积（下载资产约 323 MB），且其断语库闭源、不可审计——生成规则拿不到。
3. **凡有真实命主与真实答案的，规模都很小**（488 题、555 题量级）。这正是本项目自建大师案例集（见 inputs.jsonl/answers.jsonl）的价值所在。
4. Kaggle 除塔罗牌义集外未搜到命理案例/结局型数据集；HF 上另有易经问答集（pokkoa/positive-interpretation）因原文已哈希不可逆，实际不可用。

## 再分发条件（按 benchmark 发布规范逐项标注）

| 数据集 | 原始许可 | redistributable | 说明 |
|---|---|---|---|
| 本卷 Lilly 案例集（inputs/answers） | Lilly 原文 1647 年出版，公版（PD） | ✅ true | 节录与转述为本项目新作，发布时注明底本为 Internet Archive `christian-astrology-1647` 扫描本 |
| Waite 牌义基准集 | 《Pictorial Key》1910/11，公版（PD-US） | ✅ true | 逐字摘录自 Sacred-Texts 公版全文 |
| BaziQA（未下载，仅盘点） | 转写/代码 MIT；**题目著作权属香港青年術數家協會与出题人** | ❌ false（题目原文） | 仅供研究、须逐题署名；公开发布时不得整包转载题目原文，只能引用结论与统计 |
| Celebrity50_zh.json（已下载） | **源仓无 LICENSE** | ❌ false | 无再分发授权依据；本地仅作研究与辅助验证，公开发布版本必须剔除该文件或另行取得授权 |
| HF bazi_comprehensive_dataset | 未标注许可 | ❌ false | 未标注不等于无权利；且内容为合成数据，本项目亦不采用 |
| 紫微 v3/v4 数据集 | CC BY 4.0（须署名） | ✅ true（带条件） | 署名口径见其 DATASET-LICENSE；其中倪海厦原话部分为 CC BY-NC-SA 4.0，非商业且同许可分享，须分开标注 |
| ekelen/tarot-api | 仓库无 LICENSE（底层 Waite 文本公版） | ❌ false（该 JSON 编纂） | 牌义内容本身出自公版 Waite，应引用原文而非转载其 JSON |
| Kaggle tarot-json | 页面称 MIT | ⚠️ 未核（未下载） | 以 Kaggle 页面条款为准，下载核验后再定 |
| Astro-Databank | Astrodienst 导出许可协议（研究用途） | ❌ false | 全量导出须签约申请；免费子集亦受其条款约束，不得整包转载 |

## 已下载的辅助数据

| 文件 | 来源 | 核对 |
|---|---|---|
| `auxiliary/Celebrity50_zh.json`（500,716 字节） | GitHub MirrorAI-Lab/BaZi-Persona（gh API 下载） | 实数 50 人 / 488 题；SHA-256 `e87e6493929f8ec00a9584d2d5a89adab3d39b292f179f33866b8a801e5ebeef`；源仓无 LICENSE，仅作研究用。用作八字辅助验证集时：输入只给出生信息（年月日时、性别、出生地），答案为真实生平事件选择题；须先剥离 name/categories 并重排选项 |
| `auxiliary/christian-astrology-vol1-3_djvu.txt` | Internet Archive `christian-astrology-1647`（1647 原版 OCR） | 本卷 15 例 Lilly 案例的原文底本 |
| `auxiliary/christian-astrology-1647-original_djvu.txt` | 同上（White Page Edition OCR） | 备查，质量较差 |
