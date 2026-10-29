# VALIDATION.md — 检验履历与打包说明

- 包名：divination（严肃占卜 · MastersDivination Benchmark 经检验的最终方法）
- 版本：1.0.0（status: validated-final）
- 打包日期：2026-10-29
- 正本定义：Round 17 冻结快照 `benchmark/runs/round17/kb-snapshot/MANIFEST.sha256` 所列哈希对应的 SKILL.md 与知识库正文状态。Round 18 留出集验收与双轴补评均使用这一版方法（R18 派发前已核验 KB 与 R17 快照逐字一致）。

## 一、正本与漂移核对（打包说明）

打包前以 `sha256sum -c` 对快照清单 27 个文件逐一核对，结果：**26 个一致、1 个漂移**。

| 类别 | 文件 | 结果 |
|---|---|---|
| 方法文件 | `~/workspace/custom-skills/divination/SKILL.md` | ✅ 与快照一致（880780b1…） |
| 知识库正文（9 篇） | README.md、MANIFEST.md、calibration.md、chinese-yijing.md、chinese-liuyao-meihua.md、chinese-bazi-ziwei.md、western-tarot.md、western-astro-numerology-runes.md、lifekline-method.md | ✅ 全部一致 |
| 工具脚本（3 个） | tools/cast_iching.py、tools/draw_tarot.py、tools/draw_runes.py | ✅ 全部一致 |
| 基准数据（13 个 jsonl） | masters-dataset 各卷 inputs/answers、data/dev、data/test_inputs、holdout/test_gold 等 | ✅ 全部一致（属基准数据，不属方法文件，未入本包，仍在原工作区证据链内） |
| 评测协议 | benchmark/PROTOCOL.md | ⚠️ **漂移 1 项，见下** |

**漂移登记（唯一一项）**：现行工作区 `benchmark/PROTOCOL.md` 哈希与 R17 快照不符。原因：双轴补评任务按预注册要求，在 PROTOCOL.md 末尾**追加**了「双轴评测补充协议」一节（属评测协议的追加登记，不改动占卜方法规则本身；该变更已随提交 413ae85 / 标签 dual-axis-v1 入链）。处置：本包 `references/PROTOCOL.md` 以快照为准，取自 git 标签 round17 的 PROTOCOL.md 原文，其 SHA-256 为 `f26a9531e6f93e9d0fbb11e18946e73110a5a8eeb2bd5e20d73bffd1994e17c9`，与快照清单逐字一致。工作区现行 PROTOCOL.md **未回退**（双轴追加是证据链的正当后续演进，git 历史完整保留两版）。除此项外无任何漂移；SKILL.md 与知识库正文零漂移，未做任何「恢复」动作。

## 二、检验履历（这版方法是怎么被验出来的）

评测设计：大师案例统一池 135 例（校准集 dev 94 / 留出集 test 41，一次冻结、从未因成绩挪动）；盲测由全新上下文 agent 只见题目作断，独立双评审打分（方向/断语/应验三项，满分 6，通过线 ≥4）、分歧仲裁；五角分离（数据/盲测/评审/修订/主持互不兼任）；每轮预注册、阴性结果照报。证据全程入本地 git 仓（只增不删、纠错只追加 errata）。

- **18 轮迭代（R1–R17 校准 + R18 验收）**：dev 均分自 R1 的 4.25 起，在 4.17–4.68 间震荡；最佳轮 **R15：均分 4.68（78.0%），通过 74/94**；**R17 为零改动纯复现轮：均分 4.37，通过 70/94**，实测噪声基线——零改动相邻轮总分差 +1.5pp、逐例深跌名单几乎完全换人，定论「均值可收敛、单例不可复现，此后只信聚合量」。
- **R18 留出集验收（决定性检验）**：test 41 例自始封存，2026-10-29 08:11 由评审角首次开封并留日志。结果：**逐例百分比均值 71.1%，通过 27/41，均分（原始）4.23**；与 dev 近三轮均值（约 74.0%）差 **2.9 个百分点 ≤ 预定 5pp 线**，收敛成立、无过拟合校准集的证据。著名例在未见数据上失手 1 例（MH-005），非著名例与 dev 同位——成绩主体不靠背题。
- **双轴补评（原始分数不动的补充评测）**：新增「实际应验轴」（预测 vs 独立客观结局），结局可得性分级后 **A 级可评 105/135 例**（dev 75、test 30；B 级 30 例只有大师自述结局，不可评）。最终系统同批 A 级实例双轴对照：dev 轴一 4.52 / 轴二 4.39（73.2%）；test 轴一 4.40 / 轴二 4.25（70.8%）。四象限（最终系统合并 n=105）：双高 69（65.7%）、只合大师 13（12.4%）、**只合现实即「超越大师例」7（6.7%）**、双低 16（15.2%）。评审一致性 kappa 0.912。
- **必须照实记录的阴性结论**：同批案例 R1→R17，轴一 4.39→4.52 上涨，轴二 4.49→4.39 在噪声内无可测变化——**十七轮以大师一致性为唯一目标函数的优化，没有给实际应验带来可测提升**；且有实例（AS-302 疫苗例）显示迭代把原本合现实的判断拉回大师错误一侧，另有已被现实证伪的大师预言被两轮完整复现（BZ-301，轴一 4.0→轴二 0.0）。两轴接近只因可核验案例里大师当年大多断对。本包方法即按此现状原样冻结，不粉饰；后续若再迭代，目标函数须双轴并行（须用户另行拍板）。
- **应期仍是两轴共同短板**：尺度压缩亚型经规则修订（SKILL 通则 (k)）基本解决；坐标错位亚型（年份/年月选错）无现成规则抓手，如实登记为未解决项。

## 三、冻结快照与证据链锚点

- 快照清单：`benchmark/runs/round17/kb-snapshot/MANIFEST.sha256`（仓内路径，下同）。
- 本包方法文件在快照中的哈希：SKILL.md `880780b1cf1ad3709e87b3c22362e81535629fc919269bc8bac934926d4ef46d`；PROTOCOL.md `f26a9531e6f93e9d0fbb11e18946e73110a5a8eeb2bd5e20d73bffd1994e17c9`（其余入包文件哈希见 VERIFY-LOG.txt 的逐项核验输出）。
- git 提交与标签：R17 冻结 `8886915` / 标签 `round17`；R18 验收 `95ee517` / 标签 `round18`（含最终总报告 benchmark/runs/round18/FINAL-REPORT.md）；双轴补评 `413ae85` / 标签 `dual-axis-v1`（报告 benchmark/dual-axis/DUAL-AXIS-REPORT.md）。本包提交后打标签 `final-skill-v1`。

## 四、包结构

```
final-skill/
├── SKILL.md            # 方法正本（路径已改指为包内相对路径，替换清单见第五节）
├── VALIDATION.md       # 本文件：检验履历 + 打包说明 + 替换清单 + 外部资产清单
├── VERIFY-LOG.txt      # 打包自验脚本输出
├── references/         # 知识库正文与评测协议（与快照哈希逐字一致，零改动）
│   ├── README.md  MANIFEST.md  calibration.md  PROTOCOL.md
│   ├── chinese-yijing.md  chinese-liuyao-meihua.md  chinese-bazi-ziwei.md
│   ├── western-tarot.md  western-astro-numerology-runes.md  lifekline-method.md
└── tools/              # 随机工具脚本（与快照哈希逐字一致，零改动）
    ├── cast_iching.py  draw_tarot.py  draw_runes.py
```

全包恰好一个 SKILL.md。references/ 与 tools/ 内文件为字节级原样拷贝，未润色、未删改。

## 五、SKILL.md 路径替换清单（逐项登记，规则语义零改动）

| # | 原引用 | 包内引用 | 说明 |
|---|---|---|---|
| 1 | frontmatter description 中 `~/workspace/divination/`（the local knowledge base at …） | `this skill's references/ directory`，并加注 validated final method of the MastersDivination Benchmark | 位置改指；另在 frontmatter 补 `version: 1.0.0` 与 `status: validated-final` 两行（原有字段 name、description 保留） |
| 2 | `` `~/workspace/divination/benchmark/PROTOCOL.md` ``（总目标节） | `` `references/PROTOCOL.md` `` | 绝对路径改包内相对路径 |
| 3 | 索引节标题「资料与工具索引（本地绝对位置，按来源类型组织）」 | 「资料与工具索引（按来源类型组织；包内正文用相对路径，外部资产见 VALIDATION.md 清单）」 | 标题随路径口径更正 |
| 4 | ``知识库根：`/home/hatch/workspace/divination/` `` | 改为本包根目录说明句（正文在 references/、工具在 tools/、外部资产见本文件清单） | 根路径改指包根 |
| 5 | `` `sources/chinese/` ``、`` `sources/western/` ``（类型1） | 去路径、改标「外部资产，见外部资产清单第 1 项」，原典名单文字保留 | 外部资产不在包内 |
| 6 | `` `tools/repos/` ``（类型2） | 改标「外部资产，见外部资产清单第 2 项」，仓库名单文字保留 | 同上 |
| 7 | `` `sources/academic/` ``（类型3） | 改标「外部资产，见外部资产清单第 3 项」 | 同上 |
| 8 | `` `tools/datasets/local/` ``、`` `tools/datasets/tarot-json/` ``、`` `tools/datasets/tarot-api/` ``、`` `tools/datasets/godcong-yi/` ``、`` `masters-dataset/` ``（类型6） | 改标「外部资产，见外部资产清单第 6 项」，数据集名单与 Schema 说明文字保留 | 同上 |
| 9 | `` `benchmark/PROTOCOL.md` ``、`` `benchmark/evaluation/evaluate.py` ``、`` `benchmark/cases/` ``、`` `benchmark/iterations.md` ``（评测行） | 协议改指 `` `references/PROTOCOL.md` ``；其余改标「外部资产，见外部资产清单第 7 项」 | 协议入包、其余外部 |
| 10 | 知识库正文裸文件名（共 19 处）：`README.md`×1、`MANIFEST.md`×1、`calibration.md`×2、`chinese-yijing.md`×1、`chinese-liuyao-meihua.md`×7、`chinese-bazi-ziwei.md`×3、`western-tarot.md`×1、`western-astro-numerology-runes.md`×1、`lifekline-method.md`×2 | 一律加前缀为 `` `references/<同名>` `` | 含正文中「细则见 …」等引用，语义不变 |
| 11 | 裸脚本名（共 2 处）：`` `cast_iching.py "原问"` ``、`` `draw_tarot.py` `` | `` `tools/cast_iching.py "原问"` ``、`` `tools/draw_tarot.py` `` | 索引行原有的 `tools/cast_iching.py`、`tools/draw_tarot.py`、`tools/draw_runes.py` 字符串不变，解析基准由知识库根改为包根 |
| 12 | `` `~/workspace/divination/readings/` ``（归档节） | 改为「原工作区知识库的 readings 目录（外部位置，见外部资产清单第 8 项）」 | 归档输出目录不在包内 |
| 13 | 盲测节散文路径 `masters-dataset`、`benchmark/cases`、`masters-dataset/holdout/` | 改为「大师验证集（外部资产，见外部资产清单第 6 项）」「种子题卡」「验证集 holdout 目录」 | 散文内路径同样改指 |
| 14 | 盲测节 `` `benchmark/iterations.md` `` | 改为「原工作区 benchmark 的 iterations.md（外部资产，见外部资产清单第 7 项）」 | 同上 |

未改动说明：类型4（参照源）一行原文无路径引用，未动；正文中对 MANIFEST（无扩展名）等名称性提及非路径，未动；除上列各处外，SKILL.md 全文（含作断通则 (a)–(k) 等全部规则条文）与正本逐字一致（打包时已做全文 diff 审查，差异仅为上表各行）。

## 六、外部资产清单（不在本包内，原位置）

| # | 资产 | 原位置（原工作区） |
|---|---|---|
| 1 | 类型1 原典全文（中文/西洋原典及 SOURCES.md 著录） | `~/workspace/divination/sources/chinese/`、`~/workspace/divination/sources/western/` |
| 2 | 类型2 开源代码仓（lunar-python、sxtwl_cpp、iztro、swisseph、pyswisseph、lifekline 两版；远端与提交号另见 EXTERNAL-REPOS.md） | `~/workspace/divination/tools/repos/` |
| 3 | 类型3 学术 OA 论文 5 篇 | `~/workspace/divination/sources/academic/` |
| 4 | 类型4 参照源（Swiss Ephemeris 数据、寿星天文历、6tail lunar 数据层） | 随第 2 项代码仓 |
| 5 | 类型5 现代整理 | 已入包：`references/lifekline-method.md` 及各篇知识库文末流派节 |
| 6 | 类型6 数据集（机器可读 JSON、tarot-json、tarot-api、godcong-yi、大师验证集 masters-dataset 含 holdout 与 splits.json） | `~/workspace/divination/tools/datasets/`、`~/workspace/divination/masters-dataset/` |
| 7 | 评测基础设施（evaluate.py、cases/ 种子题卡、iterations.md、PROTOCOL 现行版） | `~/workspace/divination/benchmark/`（其中 PROTOCOL 的 R17 冻结版已入包为 `references/PROTOCOL.md`） |
| 8 | 占卜归档输出目录 readings/（使用时自建） | `~/workspace/divination/readings/` |

许可提示：外部资产中 Swiss Ephemeris / pyswisseph 为 AGPL/商业双许可，只作研究参照；若将来做闭源商业产品不得直接嵌入（详见原工作区 LICENSES.md）。

## 七、自验

打包自验脚本逐项核验：① 包内 SKILL.md 引用的全部包内相对路径（references/、tools/、VALIDATION.md）真实存在；② references/ 与 tools/ 内每个文件与 R17 快照对应文件 SHA-256 一致（PROTOCOL.md 对照快照哈希）；③ 全包恰好一个 SKILL.md；④ 包内 SKILL.md 无残留绝对路径（`/home/hatch`、`~/workspace`）。核验输出见同目录 `VERIFY-LOG.txt`，结论须为全过方可交付。
