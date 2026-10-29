# BUILD-REPORT — expansion11/modern2（NM 系：现代大师时间戳公开预测，第三路）

批次目录：`benchmark/phase3/expansion11/modern2/`
构建脚本：`build_modern2_nm_v1.py`（本批次唯一脚本，运行产出 `cases.jsonl` 与 `inputs/`）
数据角职责：搜集、分级、去重、写文件；不作断、不评分、不改 method、不提交 git。

## 1. 任务与标准

为 holdout11 封存备料补全新 A-low（现有《易林补遗》YB 22 例，下限 25，缺口 ≥3）。本路按预注册标准逐字执行：具名大师/职业预测者、结果揭晓前公开发表、带可核原始时间戳（一手载体）、断语具体可证伪（方向＋具体断言）、结局有独立于预测者的客观记录、断验可分离。污染从严分级：著名事件/名人＝high；有一定知名度＝medium；冷门对象/事件（模型先验大概率不知结局）＝low。**只有 A-low 计入 holdout11 备料**，A-medium/A-high 单独计数入储备。

收录/排除口径继承 `masters-dataset/modern-masters/excluded.md` 与 expansion6 两批（modern-cn MP 系、modern-west WP 系）BUILD-REPORT；已排除条目与同人同题重复一律不收。

## 2. 搜集路径

- 先通读 excluded.md、masters-roster、expansion6 两批 BUILD-REPORT 与 STAGE-SUMMARY-13 / INVENTORY-R30，确认现代大师路历来低产、A 级储备已用尽。
- 检索面（browser.search / browser.open 只读查证）：印度邦级与全国选举占星断语（Telangana、Karnataka、Sri Lanka 两届）、美国地方选举（Chicago 2019）、体育赛事（IPL、Ashes、板球世界杯、Euro 2024）、娱乐赛事与奖项（Eurovision 2011、I'm a Celebrity 2024、奥斯卡 2024）、华人占星师回顾性自称（杨登嵙等）。
- 每例均回查一手载体与发表时间戳，并以独立来源（官方记录/EBU/选委会数据报道/主流新闻）核结局。

## 3. 过筛漏斗

| 关口 | 通过数 | 本关剔除 |
|---|---|---|
| 初筛（逐项 examined 的断语条目） | 31 | — |
| 过时间戳核（含具名/一手出处核） | 24 | 7（E3、E4、E5、E6、E7、E8、E9） |
| 过可证伪核 | 20 | 4（E1、E2、E10、E11） |
| 过结局独立核 | 19 | 1（E12） |
| 三键去重后 A 级收录 | **17** | 2（D1、D2） |

收录 17 例分级：**A-low 1 例、A-medium 8 例、A-high 8 例**。排除/剔除共 14 项（未过筛 12＋去重 2），逐条见 §5。

## 4. 收录清单（NM-001 – NM-017）

| id | 预测者 | 事项 | 发表（载体） | 污染 | holdout 备料 |
|---|---|---|---|---|---|
| NM-001 | Andrew Bevan | Eurovision 2011 冠军（首选英国） | 2010-10-16（本人站点/Skyscript） | **low** | **是** |
| NM-002 | Inbaal Honigman | I'm a Celebrity 2024 冠亚军 | 2024-12-06（What's The Jam） | medium | 否（储备） |
| NM-003 | Jayashankarr Sistlaa | Telangana 2023：KCR 连任 | 2023-12-01（Deccan Chronicle） | medium | 否（储备） |
| NM-004 | Krothapally Suresh Sharma | Telangana 2023：国大党 70 席 | 2023-12-01（Deccan Chronicle） | medium | 否（储备） |
| NM-005 | S. N. Murthy Sidhanthi | Telangana 2023：悬峙议会 | 2023-12-01（Deccan Chronicle） | medium | 否（储备） |
| NM-006 | Susan Abbott Gidel | Chicago 市长 2019：Daley 当选 | 2019-02-20（本人站点） | medium | 否（储备） |
| NM-007 | Sumanadasa Abeygunawardena | 斯里兰卡总统 2015：Rajapaksa 连任 | 2014-12-30 / 2015-01-06（IBTimes / NYT 等） | medium | 否（储备） |
| NM-008 | Pandit Jagannath Guruji | IPL 2024 决赛：KKR 夺冠 | 2024-05-23（Economic Times） | medium | 否（储备） |
| NM-009 | Greenstone Lobo | Ashes 2017–18 系列赛 | 2017-11-22（CricTracker 报其专栏） | medium | 否（储备） |
| NM-010 | Inbaal Honigman | Euro 2024：德国冠军/英格兰止步四强 | 2024-01 上旬（Betfair Casino） | high | 否（储备） |
| NM-011 | Greenstone Lobo | 板球世界杯 2023：印度夺冠 | 2023-10（Asianet Newsable） | high | 否（储备） |
| NM-012 | Inbaal Honigman | 奥斯卡 2024 最佳女主角 | 2024-01-25（CheatSheet） | high | 否（储备） |
| NM-013 | Inbaal Honigman | 奥斯卡 2024 最佳男主角 | 2024-01-25（CheatSheet） | high | 否（储备） |
| NM-014 | Inbaal Honigman | 奥斯卡 2024 最佳男配角 | 2024-01-25（CheatSheet） | high | 否（储备） |
| NM-015 | Inbaal Honigman | 奥斯卡 2024 最佳女配角 | 2024-01-25（CheatSheet） | high | 否（储备） |
| NM-016 | Inbaal Honigman | 奥斯卡 2024 最佳导演 | 2024-01-25（CheatSheet） | high | 否（储备） |
| NM-017 | Inbaal Honigman | 奥斯卡 2024 最佳影片 | 2024-01-25（CheatSheet） | high | 否（储备） |

三键去重已比对：masters-dataset/modern-masters 全部（P01–P12、C01–C10）、expansion6 的 MP/WP/OC 全系、splits9 dev9 清单（487 例）、holdout9 / holdout10 已用例——无命中。同载体多例（NM-003–005、NM-012–017）均为不同预测者或不同所测事项，三键互不重复，与 expansion6 先例一致。

## 5. 排除登记（逐条理由）

未过筛 12 项：

- **E1** Venuswamy（Venu Swamy）IPL 2024 决赛倾向 SRH：原文为 “possibly clinch the title” 的含糊表述，未达可证伪门槛（B 级），不收。载体 Mykhel 2024-05-26。
- **E2** Inbaal Honigman《Celebrity Big Brother 2024》（indy100，2024-03-22）：标题称其断 Louis Walsh 夺冠，正文引语只有 “fire cards / really want to win” 类表述、无单一胜者断语，不可证伪，不收。
- **E3** Inbaal Honigman Grand National 2025 选马：仅见内容农场转载、无可核原始日期，且为多匹马 “best chance” 的概率性表述；时间戳核不过，不收。
- **E4** Lisa Simmi《The Traitors India》第二季：决赛后自宣文，断语为约 6 人名单中的 “potential winners” 之一，Instagram 原始时间戳/内容不可核；时间戳核不过，不收。
- **E5** 杨登嵙 “2018 六都全中” 说：仅见 2026 年选举报道中的回顾性自称，未检得 2018 年原始发表；无一手时间戳，不收。
- **E6** 杨登嵙 “2020 年预言 2022 台北名次（蒋万安 1、陈时中 2、黄珊珊 3）” 说：同上，仅回顾文自称，无 2020 年原始发表，不收。
- **E7** 斯里兰卡 2019 总统选举占星师群（含 Kalyani Menike）：仅有选后盘点文（Sunday Times 2019-12-01），选前原始发表与时间戳未检得，不收。（同国 2015 年 Abeygunawardena 有三家选前一手载体，已收为 NM-007，不重复。）
- **E8** Andrew Bevan 自称 2009（Rybak）、2010（Lena）Eurovision 断中：仅其 2011 年页面回顾提及，原始发表未检得，不收。
- **E9** astrologicalmusings.com《Planets and Karnataka Assembly Elections 2023》（2023-03-14）断 BJP 大败、国大党全多数：断语本身合格且结局可核，但**站点作者无法确证**——“Astrological Musings” 名下有多个不同站点/作者（Sachin Malhotra、Lynn Hayes 等）混杂，原文页面无署名，本轮查证未能落实具名，未过具名/一手核，不收。
- **E10** Mangalore Today 载 Harsh Mehta 2019 相关文：所检文本无针对目标选举的明确胜负断语，不可证伪，不收。
- **E11** GaneshaSpeaks 关于 Mayawati 文：同上，无明确可证伪断语，不收。
- **E12** 台湾 2026 市长选举预测群（杨登嵙、周映君等，2026-10 报道）：选举为 2026-11-28，任务时点（2026-10-30）尚无结局，结局独立核不过，不收。

去重剔除 2 项：

- **D1** Greenstone Lobo “印度不会赢 2019 世界杯”（Deccan Chronicle 2019-07 赛后反思文）：与既有 WP-009 同人、同对象、同事项，三键重复，剔除。
- **D2** Greenstone Lobo 2023 世界杯决赛前 Asianet 文：与 NM-011 同大师、同事项，择赛前文收录，决赛前文剔除（仅计一例）。

另：excluded.md 既有登记（唐绮阳/麦玲玲/宋韶光流年泛谈、李居明同题、Athos Salomé 类、Abhigya Anand、Allan Lichtman、无名 “民间大师” 等）本轮未重收任何一条。

## 6. 题面与泄漏自检登记

`inputs/<id>.json` 逐例生成（17/17），规则：只含对象背景＋预测时点情境；剔除 `master_predictions` 与 `outcome` 本体；`provenance` 中性化（只记载体类型与日期，标题/链接可能指向断语者一律不入题面）；`grade_note`（含中误讨论）不入题面。脚本化自检：扫描全部题面，无 `master_predictions`/`outcome` 键，无断语与结局词面（唯一命中为 NM-008 疑问句 “谁将夺冠？” 属题面设问本身，非泄漏）。各题面 `notes.leak_check` 已逐例登记。

## 7. holdout11 备料结论（照实报）

- 本路新增 **A-low 仅 1 例（NM-001）**。YB 22＋NM 1＝**23 例，仍低于 25 例下限，缺口 2 例，本路未能补足**。未降标准凑数：I'm a Celebrity 2024（NM-002）具体名次虽冷，但节目与参赛者知名度高、且断中对象为赔率热门，按从严口径判 medium，不升格 low。
- A-medium 8 例、A-high 8 例已单独登记入储备（`holdout_eligible=false`），不计入封存备料。

## 8. 请主持角复核事项

1. **NM-001**：断语形态为 “短名单＋首选（first bet）”，较单点断语弱；污染判 low 的依据是 “2011 届冠军为冷门具体结局”，若主持角以赛事知名度改判 medium，本批 A-low 归零、备料缺口回到 3。
2. **NM-006**：本人站点页面存选后 “Updated 2019-10-23” 戳；核心断语以选前发表元数据（2019-02-20）为据，若从严可降 B。
3. **NM-009**：污染介于 medium/high 边界（灰烬杯为著名系列赛，单届细节非通识），本批取 medium 并已在 grade_note 明示，主持角可上调 high（不影响备料计数）。
4. **NM-012–017**：六例同篇发表、奖项各异；若主持角认为同篇应合并计数，储备数相应减少（不影响 A-low 与备料结论）。
