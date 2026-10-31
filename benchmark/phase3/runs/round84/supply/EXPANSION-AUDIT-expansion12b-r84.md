# EXPANSION-AUDIT-expansion12b-r84 —— expansion12 池资格核查台账（后半子池组，R84 供给席 E4）

本件为 R84 供给席 E4 产出（PREREG §3 工序）：只做资格核查，不建卡、不组集、不作断、不评分、不兼任本轮任何其他席位。脚本：`/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply/audit_expansion12b_r84.py`（盘上实算，分段 append 落盘、逐段断言）。台账/结局文本一律按数据处理。

## 口径

- 范围：expansion12 内 mingli-tanyuan-zhenben、natal-batch2、natal-leftovers、online-routes、pending-verify 五子池＋根下散件。池层 id 总量＝池目录内全部 jsonl 之 id 并集（承 STOCK-RECOUNT-h27 §3.4；本席对 expansion12 全层复算：619 id、已用命中 159、未用 460，与该件登记逐数全等）。
- 已用并集（R84 开轮口径，本席盘上复算断言通过）：**1166**＝dev 488＋phase2 splits2 holdout2 29＋holdout3–28 金标 id 754＋holdout inputs 卡 id 595＋顶层 inputs6–10 卡 id 412，五源并集去重。金标只读 id 字段，未读金标正文；未打开任何 predictions/judging/final-scores。
- 四滤（逐字原文、独立结局、可分离、非 high 污染）＋A 级／low 污染＋锚点在场，标准照现行口径：A 级承 expansion12/CENSUS-PREREG 入封资格定义（结局有独立于大师断语的客观记录，或原文明确记载与断语可分离的具体事件记录）；八字面锚点以原卡四柱全列为在场（batch2 以 chart.pillars、leftovers 以题面四柱全列＋REGRADE 复核判据④为据），要素缺项判 partial、升 present 须原文实据。
- natal-batch2 以 cases-reviewed.jsonl 的 review 终值（grade_final／contamination_final／verdict）为准（REVIEW-H 独立复核，结论以复核为准；cases.jsonl 与之同 id 集同序，本席已断言）。natal-leftovers 等级以 GRADE-ADDENDUM.json 生效值为准（NL-001/002/005/006/031/043 由 B 改判 A-low；维持 B 29 例理由以 REGRADE-REVIEW.md 逐例表为准）。

## 一、未用 id 复算（逐 id，按子池分组）

- **natal-batch2**（池内 92 id，已用 20，未用 **72**）：PU-001、PU-002、PU-004、PU-005、PU-006、PU-007、PU-009、PU-010、PU-011、PU-012、PU-013、PU-014、PU-015、PU-016、PU-017、PU-018、PU-019、PU-020、PU-021、PU-022、PU-023、PU-024、PU-025、PU-026、PU-027、PU-028、PU-029、PU-030、PU-031、PU-032、PU-033、PU-034、PU-035、PU-036、PU-037、PU-038、PU-039、PU-040、PU-041、PU-042、PU-043、PU-044、PU-045、PU-046、PU-047、PU-048、PU-049、PU-050、PU-051、PU-052、PU-053、PU-054、PU-055、PU-056、PU-057、QL-009、QL-010、QL-011、QL-012、QL-015、QL-016、QL-017、QL-018、QL-019、QL-020、QL-021、QL-022、QL-024、QL-028、QL-029、QL-033、QL-034
- **natal-leftovers**（池内 55 id，已用 7，未用 **48**）：NL-003、NL-004、NL-007、NL-008、NL-009、NL-010、NL-011、NL-012、NL-013、NL-014、NL-015、NL-016、NL-017、NL-018、NL-019、NL-020、NL-021、NL-022、NL-023、NL-024、NL-025、NL-026、NL-027、NL-028、NL-029、NL-030、NL-032、NL-033、NL-034、NL-035、NL-036、NL-037、NL-038、NL-039、NL-040、NL-041、NL-042、NL-044、NL-045、NL-046、NL-047、NL-048、NL-050、NL-051、NL-052、NL-053、NL-054、NL-055
- **online-routes**（池内 33 id，已用 33，未用 **0**）：CZ-001…CZ-033 全部命中已用并集，无未用例（同名即剔口径下不作逐例核查；该文件内 holdout_eligible 亦全为 false）。
- **mingli-tanyuan-zhenben**（未用 **0**）：子池内无任何 jsonl（仅 CENSUS／METHOD／校勘类 md 与页图），池层 id 并集贡献 0；文中 MT 编号系跨池校勘引用，其案例记录不在本子池。
- **pending-verify**（未用 **0**）：子池内无 jsonl，仅 VERDICTS.md 与 overlay-proposals.json；overlay 草案所涉 6 id（LY-430、LR3-112、LY-437、LY-533、OC-014、YM-019）经本席逐 id 核对全部已在已用并集内，属既有例的结局处置草案、非新供给。
- **expansion12 根散件**（未用 **0**）：根下无 jsonl（仅 CENSUS／HOST-RULINGS 类 md 与 POOL-IDS.txt 全池清单文本），池层 id 并集贡献 0。
- **所辖未用合计：120**（natal-batch2 72＋natal-leftovers 48）。以下逐例核查即此 120 例。

## 二、逐例资格核查 —— natal-batch2（72 例，体系：八字）

来源：袁树珊《袁氏命谱》（PU）／韦千里《千里命稿》（QL），转录＝逐页视觉读图（transcription=visual）。原文定位＝cases-reviewed.jsonl 行号＋provenance 页。

| id | 子池 | 体系/来源 | 逐字原文 | 独立结局 | 可分离 | 非high | 锚点 | 污染 | 等级 | 结论 | 原文定位 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PU-001 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含两说成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:1；PDF p39–41（书卷一 p1–3，命式 p2） |
| PU-002 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含考定、两说成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:2；PDF p47–49（书卷一 p9–11，命式 p10） |
| PU-004 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含推定成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:4；PDF p63–65（书卷一 p25–27，命式 p26） |
| PU-005 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:5；PDF p73–75（书卷一 p35–37，命式 p36） |
| PU-006 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含推定成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:6；PDF p77–78（书卷一 p39–40，命式 p40） |
| PU-007 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含推定、考定成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:7；PDF p81–83（书卷一 p43–45，命式 p44） |
| PU-009 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:9；PDF p97–99（书卷二 p59–61，命式 p60） |
| PU-010 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:10；PDF p103–105（书卷二 p65–67，命式 p66） |
| PU-011 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:11；PDF p109–110（书卷二 p71–72，命式 p71） |
| PU-012 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含考定成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:12；PDF p117–119（书卷二 p79–81，命式 p80） |
| PU-013 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:13；PDF p124–126（书卷二 p86–88，命式 p87） |
| PU-014 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:14；PDF p128–131（书卷二 p90–93，命式 p91） |
| PU-015 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:15；PDF p140–141（书卷二 p102–103，命式 p103） |
| PU-016 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:16；PDF p147–148（书卷三 p109–110，命式 p109） |
| PU-017 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:17；PDF p151–153（书卷三 p113–115，命式 p114） |
| PU-018 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:18；PDF p159–160（书卷三 p121–122，命式 p122） |
| PU-019 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:19；PDF p165–166（书卷三 p127–128，命式 p128） |
| PU-020 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:20；PDF p172–173（书卷三 p134–135，命式 p135） |
| PU-021 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:21；PDF p177–179（书卷三 p139–141，命式 p140） |
| PU-022 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:22；PDF p182–183（书卷三 p144–145，命式 p145） |
| PU-023 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:23；PDF p189–191（书卷三 p151–153，命式 p152） |
| PU-024 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:24；PDF p193–195（书卷四 p155–157，命式 p156） |
| PU-025 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含推定、拟作成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:25；PDF p197–199（书卷四 p159–161，命式 p160） |
| PU-026 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:26；PDF p203–207（书卷四 p165–169，命式 p167） |
| PU-027 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:27；PDF p215–216（书卷四 p177–178，命式 p178） |
| PU-028 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:28；PDF p219–221（书卷四 p181–183，命式 p182） |
| PU-029 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:29；PDF p225–226（书卷四 p187–188，命式 p188） |
| PU-030 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:30；PDF p229–230（书卷四 p191–192，命式 p192） |
| PU-031 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:31；PDF p233–235（书卷四 p195–197，命式 p196） |
| PU-032 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:32；PDF p241–242（书卷五 p203–204，命式 p203） |
| PU-033 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:33；PDF p252–253（书卷五 p214–215，命式 p215） |
| PU-034 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:34；PDF p258–261（书卷五 p220–223，命式 p221） |
| PU-035 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:35；PDF p263–264（书卷五 p225–226，命式 p226） |
| PU-036 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:36；PDF p267–268（书卷五 p229–230，命式 p229） |
| PU-037 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含推定、测之成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:37；PDF p275–276（书卷五 p237–238，命式 p237） |
| PU-038 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:38；PDF p279–280（书卷五 p241–242，命式 p241） |
| PU-039 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:39；PDF p283–285（书卷六 p245–247，命式 p246） |
| PU-040 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含推定、测之成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:40；PDF p293–295（书卷六 p255–257，命式 p256） |
| PU-041 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:41；PDF p307–308（书卷六 p269–270，命式 p269） |
| PU-042 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:42；PDF p309–310（书卷六 p271–272，命式 p271） |
| PU-043 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:43；PDF p315–316（书卷六 p277–278，命式 p278） |
| PU-044 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:44；PDF p320–321（书卷六 p282–283，命式见 p282） |
| PU-045 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:45；PDF p326–327（书卷六 p288–289，命式 p289） |
| PU-046 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:46；PDF p329–330（书卷七 p291–292，命式 p292） |
| PU-047 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:47；PDF p333–334（书卷七 p295–296，命式 p295） |
| PU-048 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:48；PDF p337–338（书卷七 p299–300，命式 p299） |
| PU-049 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:49；PDF p343–344（书卷七 p305–306，命式 p305） |
| PU-050 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:50；PDF p360–361（书卷七 p322–323，命式 p322） |
| PU-051 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:51；PDF p375–376（书卷八 p337–338，命式 p338） |
| PU-052 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:52；PDF p383–384（书卷八 p345–346，命式 p345） |
| PU-053 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:53；PDF p385–386（书卷八 p347–348，命式 p348） |
| PU-054 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:54；PDF p390–391（书卷八 p352–353，命式见 p352） |
| PU-055 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present（锚点注：四柱书内单一采用，含转述、疑信参半成分，入池须知） | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:55；PDF p396–397（书卷八 p358–359，命式 p359） |
| PU-056 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:56；PDF p399–400（书卷八 p361–362，命式 p361） |
| PU-057 | natal-batch2 | 八字/袁树珊《袁氏命谱》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:57；PDF p406–407（书卷八 p368–369，命式 p369） |
| QL-009 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:58；PDF p241–242（书应运篇 p241–242） |
| QL-010 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:59；PDF p242（书应运篇 p242） |
| QL-011 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:60；PDF p243（书应运篇 p243） |
| QL-012 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present（锚点注：四柱书内单一采用，含转述成分，入池须知） | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:61；PDF p244–245（书应运篇 p244–245） |
| QL-015 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:66；PDF p249（书应运篇 p249） |
| QL-016 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:68；PDF p254（书应运篇 p254） |
| QL-017 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:69；PDF p255（书应运篇 p255） |
| QL-018 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:70；PDF p259（书应运篇 p259） |
| QL-019 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✗ | present | high | B | 不合格（卡：独立结局、可分离、非high污染、A级、low污染） | natal-batch2/cases-reviewed.jsonl:71；PDF p259（书应运篇 p259） |
| QL-020 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:72；PDF p260（书应运篇 p260） |
| QL-021 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✓ | ✓ | ✗ | partial（锚点注：四柱系互证重构、非整造直载） | high | A | 不合格（卡：非high污染、low污染、锚点在场） | natal-batch2/cases-reviewed.jsonl:73；PDF p261（书应运篇 p261） |
| QL-022 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:74；PDF p263（书应运篇 p263） |
| QL-024 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present（锚点注：四柱书内单一采用，含转述成分，入池须知） | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:76；PDF p267（书应运篇 p267） |
| QL-028 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-batch2/cases-reviewed.jsonl:82；PDF p278（书应运篇 p276） |
| QL-029 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✓ | ✓ | ✗ | partial（锚点注：四柱系互证重构、非整造直载） | high | A | 不合格（卡：非high污染、low污染、锚点在场） | natal-batch2/cases-reviewed.jsonl:83；PDF p283（书应运篇 p281） |
| QL-033 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级） | natal-batch2/cases-reviewed.jsonl:90；PDF p280（书应运篇 p278） |
| QL-034 | natal-batch2 | 八字/韦千里《千里命稿》 | ✓ | ✗ | ✗ | ✗ | present（锚点注：四柱书内单一采用，含两说成分，入池须知） | high | B | 不合格（卡：独立结局、可分离、非high污染、A级、low污染） | natal-batch2/cases-reviewed.jsonl:91；PDF p229（书应运篇 p227） |

## 三、逐例资格核查 —— natal-leftovers（48 例，体系：八字）

来源：韦千里《呱呱集》（NL-001…045）／徐乐吾评注《子平真诠评注》（NL-046…055）。原文定位＝cases.jsonl 行号＋provenance 页。维持 B 例的卡项主因承 REGRADE-REVIEW §三分布（回顾性解盘／无具体断语／结局即断语本身），其逐例表②③两项皆不备。

| id | 子池 | 体系/来源 | 逐字原文 | 独立结局 | 可分离 | 非high | 锚点 | 污染 | 等级 | 结论 | 原文定位 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| NL-003 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:3；主本PDF p8；原版书p36 |
| NL-004 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:4；主本PDF p7-8 |
| NL-007 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:7；主本PDF p7 |
| NL-008 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:8；主本PDF p7 |
| NL-009 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:9；主本PDF p6 |
| NL-010 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:10；主本PDF p3；原版书p9 |
| NL-011 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:11；主本PDF p3；原版书p9 |
| NL-012 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:12；主本PDF p2 |
| NL-013 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:13；主本PDF p2 |
| NL-014 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:14；主本PDF p4-5；原版书p17 |
| NL-015 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:15；主本PDF p10；原版书p44 |
| NL-016 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:16；主本PDF p10；原版书p45 |
| NL-017 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:17；主本PDF p10；原版书p46 |
| NL-018 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:18；主本PDF p11；原版书p49 |
| NL-019 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:19；主本PDF p11；原版书p49 |
| NL-020 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:20；主本PDF p11；原版书p49 |
| NL-021 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✗ | present | high | B | 不合格（卡：独立结局、可分离、非high污染、A级、low污染）（注：grade_note 载命造本身不可核） | natal-leftovers/cases.jsonl:21；主本PDF p11；原版书p50 |
| NL-022 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：无具体断语） | natal-leftovers/cases.jsonl:22；主本PDF p11；原版书p50 |
| NL-023 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:23；主本PDF p11；原版书p48 |
| NL-024 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✗ | present | high | B | 不合格（卡：独立结局、可分离、非high污染、A级、low污染） | natal-leftovers/cases.jsonl:24；主本PDF p9 |
| NL-025 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:25；主本PDF p9-10；原版书p42 |
| NL-026 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✗ | present | high | B | 不合格（卡：独立结局、可分离、非high污染、A级、low污染） | natal-leftovers/cases.jsonl:26；主本PDF p9-10；原版书p42 |
| NL-027 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✗ | present | high | B | 不合格（卡：独立结局、可分离、非high污染、A级、low污染） | natal-leftovers/cases.jsonl:27；主本PDF p10；原版书p47 |
| NL-028 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:28；主本PDF p4；原版书p16 |
| NL-029 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:29；主本PDF p4；原版书p16 |
| NL-030 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:30；主本PDF p4；原版书p14-15 |
| NL-032 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：无具体断语） | natal-leftovers/cases.jsonl:32；主本PDF p5；原版书p19 |
| NL-033 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:33；主本PDF p3；原版书p8 |
| NL-034 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:34；主本PDF p3-4；原版书p12 |
| NL-035 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：结局即断语本身/仅状态语） | natal-leftovers/cases.jsonl:35；主本PDF p11-12；原版书p52 |
| NL-036 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:36；主本PDF p11-12；原版书p52 |
| NL-037 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：无具体断语） | natal-leftovers/cases.jsonl:37；主本PDF p11-12；原版书p52 |
| NL-038 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:38；主本PDF p12；原版书p53 |
| NL-039 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:39；主本PDF p12；原版书p53 |
| NL-040 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:40；主本PDF p12 |
| NL-041 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:41；主本PDF p12；原版书p54 |
| NL-042 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:42；主本PDF p12；原版书p53 |
| NL-044 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✗ | present | high | B | 不合格（卡：独立结局、可分离、非high污染、A级、low污染）（注：命主名一字待核，见 CENSUS 勘误） | natal-leftovers/cases.jsonl:44；主本PDF p36（下集，答卢百泉君函中） |
| NL-045 | natal-leftovers | 八字/韦千里《呱呱集》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:45；主本PDF p39（下集，答谭林君） |
| NL-046 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:46；第二十一章 论星辰无关格局（评注txt约L1785） |
| NL-047 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:47；第二十一章 论星辰无关格局（评注txt约L1800） |
| NL-048 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:48；第二十一章 论星辰无关格局（评注txt约L1806） |
| NL-050 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✓ | ✓ | ✗ | present | high | A | 不合格（卡：非high污染、low污染） | natal-leftovers/cases.jsonl:50；第二十七章 论喜忌干支有别（评注txt约L1955） |
| NL-051 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:51；第二十八章 论支中喜忌逢运透清（评注txt约L1985） |
| NL-052 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:52；第二十七章 论喜忌干支有别（评注txt约L1970） |
| NL-053 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：结局即断语本身/仅状态语） | natal-leftovers/cases.jsonl:53；第十四章 论用神配气候得失（评注txt约L1486） |
| NL-054 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：回顾性解盘） | natal-leftovers/cases.jsonl:54；第四章（论用神）性情相关段（评注txt约L347；第二十二章L500互见） |
| NL-055 | natal-leftovers | 八字/徐乐吾《子平真诠评注》 | ✓ | ✗ | ✗ | ✓ | present | low | B | 不合格（卡：独立结局、可分离、A级）（主缺项：结局即断语本身/仅状态语） | natal-leftovers/cases.jsonl:55；第九章 论用神成败救应（评注txt约L1158；第八章L760互见作「浙江盐商」） |

## 四、分面计数（所辖未用 120 例）

| 面 | 未用 | eligible | 不合格 |
|---|---|---|---|
| natal-batch2（八字） | 72 | 0 | 72 |
| natal-leftovers（八字） | 48 | 0 | 48 |
| online-routes（测字） | 0 | 0 | 0 |
| mingli-tanyuan-zhenben | 0 | 0 | 0 |
| pending-verify | 0 | 0 | 0 |
| 根散件 | 0 | 0 | 0 |
| **合计** | **120** | **0** | **120** |

- 逐体系 eligible：八字 **0**；六爻 0；奇门 0；测字 0；其余体系 0。所辖五子池＋根散件未用 120 例逐例核查后 eligible 为 **0**。
- 非六爻 eligible 合计 **0**；六爻 eligible 合计 **0**。（本席所辖范围对 PREREG §5 门槛的贡献为 0；其余子池组不在本席范围。）
- 不合格主因分布（可重叠）：污染 high 80 例（natal-batch2 61＋natal-leftovers 19，逐例见台账行）；等级非 A／独立结局与可分离不备 47 例；锚点 partial 2 例（QL-021、QL-029，四柱互证重构、非整造直载，两例另因 high 污染不合格，锚点不改变其结论）。逐字原文一项 120 例全过（断语摘录与结局描述俱非空、转录来源在册）。
- 交叉核对（资格全过集与已用并集的关系）：natal-batch2 复核 seal 18 例（＝holdout_eligible=true 集）全部已在已用并集内；natal-leftovers 资格全过集恰 7 例（改判 A-low 6 例 NL-001、NL-002、NL-005、NL-006、NL-031、NL-043＋原 A＋low 的 NL-049），亦全部已在已用并集内（脚本逐 id 断言通过）。即所辖两子池凡资格全过者皆已被取用，未用 120 例无一全过，与逐例核查结论 eligible=0 互证一致。

## 五、异常与注记

1. **编号映射**：natal-batch2 盘上现行号 PU/QL 系 RENUMBER-MAP.json 重编结果（旧 MP→PU 同号、旧 QM→QL 非同号映射）；REVIEW-H 与 CENSUS-NOTES 正文仍用旧号，引用时须经映射表换算，本台账一律用现行号。
2. **锚点 partial 2 例**：QL-021（页上仅残行见一柱、余柱互证重构）、QL-029（干支序列与造式互证复原），原文未整造直载，按口径判 partial、不升 present；两例同时 high 污染，结论均为不合格。另 PU 诸例中时柱含推定/考定/拟作/转述成分者（PU-001、002、004、006、007、012、025、031、037、040、055 及 QL-034 造式两说）四柱仍为书内单一采用、全列在册，判 present 并逐行注记，入池使用不得作史载生辰直录引用。
3. **online-routes 同名占用**：CZ-001…CZ-033 与既有 CZ 号段（dev 侧）同名，33 例全部命中已用并集；按同名即剔，本子池对未用集贡献 0。此为 id 层占用事实，不涉该 33 例内容资格（其文件内 holdout_eligible 亦全 false）。
4. **mingli-tanyuan-zhenben 无例可核**：该子池为《命理探源》版本/存稿校勘面，只有文档与页图、无案例 jsonl；如主持认定其 CENSUS 文档内述及的命例应另册建账，须另行派单抽例，不在本席核查范围内推定。
5. **NL-044**：命主名一字（微/维）待核、CENSUS 已登记，本例另因 B 级＋high 污染不合格，待核事项不影响结论。**NL-021**：grade_note 载命造本身不可核，本例因 B 级＋high 污染不合格，锚点形式全列但附注于台账行。
6. 本席未打开任何已封存集金标正文（已用并集只取金标 id 字段）、未打开 runs/ 下 predictions/judging/final-scores；池层原文只读未改；脚本仅本件同目录唯一名文件。

