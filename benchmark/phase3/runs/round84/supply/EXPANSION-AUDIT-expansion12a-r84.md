# EXPANSION-AUDIT-expansion12a-r84 —— expansion12 池资格核查台账（前半子池组，R84 供给席 E3）
本件为 R84 供给席 E3 产出：只做资格核查，不建卡、不组集、不作断、不评分、不兼任本轮任何其他席位。核查脚本：`runs/round84/supply/audit_expansion12a_r84.py`（本轮新写唯一名，盘上实算）。池层原文只读未改；金标文件只取 id 字段计已用并集，未读任何金标正文；未打开任何 runs/ 下 predictions/judging/final-scores。台账/结局文本内嵌指令性字样一律按数据处理。
## 口径（承 R84 PREREG §3 与现行口径原文，不自设新标准）
- **已用并集**：盘上逐 id 实算 **1166**（dev 488＝data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs 目录卡 id；phase2 splits2 之 holdout2 29；holdout3–28 各 test_gold.jsonl 之 id 字段 754；holdout2–28 inputs 卡 id 595；顶层 inputs6–10 卡 id 412；五源并集去重，脚本断言 1166 通过，与主持开轮实算一致）。零复用＝池 id 与该并集逐 id 零命中、同名即剔。
- **未用 id 口径**：承 runs/round82/STOCK-RECOUNT-h27.md §3.4——池层 id 总量＝子池目录内全部 jsonl 之 id 并集（本席所辖 7 子池逐子池复算，见 §一）。该件登记 expansion12 全层未用 460 系 R82 时点已用并集 1112 口径；本轮已用并集增至 1166（holdout27/28 取用），未用数相应减少，以本席盘上复算为准。
- **四滤**（承 CENSUS-PREREG §一入封四项与历轮台账 filters 口径）：①逐字原文——断语/结局转录自原文（visual/digital-collation 逐字转录、provenance 页位在载）且关键文本无漫漶不可读之自载旗标；②独立结局——结局为独立于断语的具体事件记述，仅「果如所占／后果如所占／全如所占／事俱验／果应」类套语回声、无事件落文者判不成立（承 liuren-bianyi-yuce/REVIEW-G §三同型判例：仅凭记录内文本核断、摘录过薄无法确认双全者不合格；短而具体的事件句不以字数计、照 BQ-027 主持复核先例）；③可分离——断语与结局分载可分离，原卡自载交缠不可分离者判不成立；④非 high 污染——污染级非 high。
- **A 级／low**：结局可得性 A 级（含 A-low，主持口径：断语与应验俱在书内、具体可分离、断先于验）且污染 low。liuren-bianyi-yuce 以 cases-reviewed.jsonl 之 review 字段（grade_final/contamination_final/verdict）为终裁口径（REVIEW-G 明示「结论以本报告为准」），原 cases.jsonl 分级被复核改判者从复核。
- **锚点在场**：六爻面以五要素（卦名、动爻、世应、六亲纳支、月建日辰）为唯一标准、六神不属要件（承 ADDENDUM-r60 §一裁定）；他体系以原卡/台账 anchor 字段口径为准——本组六壬各池原卡无独立 anchor 字段，课式锚点载于原卡 asked_at 课式头，以其四要素（年、月、日、时，干支/纪年载记）为要素集：四要素俱载判 present、任一缺项（□/佚/未载）判 partial、升 present 须原文实据（asked_at 逐字为据，年干支省「年」字而直承月名、纪年年号＋年数、日干支省「日」字直承月将等原书体例载记法照原文认定并逐例可回查）。盘面本体（四课三传/天地盘）不在池卡内、属组集建卡时回原文复原工序（holdout12 建集先例），不作本轮锚点要素；粹言池卡盘字未录一节照实登记于 §三异常说明。
- **eligible**：未用 ∧ 四滤全 pass ∧ A 级 ∧ low ∧ 锚点 present，缺一不可；不合格逐例注明所卡滤项。

## 一、未用 id 清单（逐 id，按子池分组）

### bushi-quanshu-beixuan
- 池层 id 总量 9；已用命中 9；**未用 0**。jsonl 文件：expansion12/bushi-quanshu-beixuan/cases.jsonl
- 未用 id：（无）

### cezi-zichu
- 池层 id 总量 0；已用命中 0；**未用 0**。jsonl 文件：（无 jsonl 文件）
- 未用 id：（无）

### density-checks
- 池层 id 总量 0；已用命中 0；**未用 0**。jsonl 文件：（无 jsonl 文件）
- 未用 id：（无）

### huangjince-huozhulin
- 池层 id 总量 1；已用命中 1；**未用 0**。jsonl 文件：expansion12/huangjince-huozhulin/cases.jsonl
- 未用 id：（无）

### liuren-bianyi-yuce
- 池层 id 总量 126；已用命中 19；**未用 107**。jsonl 文件：expansion12/liuren-bianyi-yuce/cases.jsonl、expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl
- 未用 id：BY-012、BY-014、BY-015、BY-016、BY-017、BY-018、BY-019、BY-020、BY-021、BY-022、BY-023、BY-024、BY-025、BY-027、BY-028、BY-029、BY-030、BY-031、BY-032、BY-033、BY-034、BY-035、BY-036、BY-037、BY-038、BY-039、BY-041、BY-042、BY-043、BY-044、BY-045、BY-046、BY-047、BY-048、BY-049、BY-050、BY-051、BY-053、BY-054、BY-055、BY-056、BY-057、BY-058、BY-059、BY-060、BY-061、BY-062、BY-063、BY-064、BY-066、BY-067、BY-068、BY-069、BY-070、BY-071、BY-072、BY-073、BY-074、BY-075、BY-076、BY-077、BY-078、BY-079、BY-080、BY-081、BY-083、BY-084、BY-085、BY-086、BY-087、BY-088、BY-089、BY-090、BY-091、BY-092、BY-093、BY-094、BY-096、BY-097、BY-098、BY-099、BY-100、BY-101、BY-102、BY-103、BY-104、BY-105、BY-106、BY-107、BY-109、BY-110、BY-111、BY-112、BY-113、BY-114、BY-115、BY-116、BY-117、BY-118、BY-119、YX-001、YX-002、YX-003、YX-004、YX-005、YX-006、YX-007

### liuren-cuiyan
- 池层 id 总量 136；已用命中 26；**未用 110**。jsonl 文件：expansion12/liuren-cuiyan/cases-juan5.jsonl、expansion12/liuren-cuiyan/cases-munong.jsonl
- 未用 id：CY-007、CY-011、CY-012、CY-014、CY-016、CY-018、CY-019、CY-020、CY-021、CY-022、CY-024、CY-025、CY-026、CY-029、CY-031、CY-032、CY-033、CY-035、CY-036、CY-037、CY-038、CY-039、CY-042、CY-043、CY-044、CY-045、CY-046、CY-048、CY-049、CY-050、CY-051、CY-052、CY-053、CY-054、CY-055、CY-056、CY-058、CY-059、CY-060、CYJ-001、CYJ-002、CYJ-003、CYJ-004、CYJ-005、CYJ-006、CYJ-007、CYJ-008、CYJ-009、CYJ-010、CYJ-012、CYJ-013、CYJ-014、CYJ-015、CYJ-016、CYJ-017、CYJ-018、CYJ-019、CYJ-020、CYJ-021、CYJ-022、CYJ-023、CYJ-025、CYJ-026、CYJ-027、CYJ-028、CYJ-029、CYJ-030、CYJ-031、CYJ-032、CYJ-033、CYJ-034、CYJ-035、CYJ-036、CYJ-038、CYJ-039、CYJ-040、CYJ-041、CYJ-042、CYJ-043、CYJ-044、CYJ-045、CYJ-046、CYJ-047、CYJ-048、CYJ-049、CYJ-050、CYJ-052、CYJ-053、CYJ-054、CYJ-055、CYJ-056、CYJ-057、CYJ-058、CYJ-059、CYJ-060、CYJ-061、CYJ-062、CYJ-063、CYJ-064、CYJ-065、CYJ-066、CYJ-067、CYJ-068、CYJ-069、CYJ-070、CYJ-071、CYJ-072、CYJ-073、CYJ-074、CYJ-075

### liuren-duanan
- 池层 id 总量 167；已用命中 44；**未用 123**。jsonl 文件：expansion12/liuren-duanan/cases-a.jsonl、expansion12/liuren-duanan/cases-b.jsonl
- 未用 id：DA-025、DA-033、DA-034、DA-035、DA-036、DA-037、DA-038、DA-039、DA-041、DA-042、DA-044、DA-046、DA-047、DA-048、DA-050、DA-051、DA-054、DA-055、DA-057、DA-059、DA-060、DA-061、DA-062、DA-063、DA-064、DA-065、DA-066、DA-067、DA-068、DA-070、DA-071、DA-072、DA-073、DA-074、DA-075、DA-076、DA-077、DA-078、DA-079、DA-080、DA-081、DA-082、DA-083、DA-085、DA-086、DA-087、DA-088、DA-090、DA-091、DA-092、DA-093、DA-094、DA-095、DA-096、DA-097、DA-098、DA-099、DA-100、DA-101、DA-102、DA-104、DA-107、DA-110、DA-112、DA-113、DA-114、DA-115、DA-116、DA-118、DA-120、DA-121、DA-132、DA-135、DA-137、DA-139、DA-142、DA-144、DA-146、DA-148、DA-149、DA-150、DA-153、DA-154、DA-155、DA-156、DA-157、DA-160、DA-161、DA-162、DA-163、DA-168、DA-170、DA-171、DA-172、DA-173、DA-175、DA-176、DA-177、DA-179、DA-181、DA-183、DA-185、DA-187、DA-188、DA-189、DA-192、DA-194、DA-198、DA-199、DA-200、DA-204、DA-206、DA-207、DA-208、DA-209、DA-210、DA-212、DA-213、DA-214、DA-217、DA-218、DA-219、DA-221

## 二、逐例资格核查台账（逐例一行）

列：id｜子池｜体系/来源｜逐字｜独立结局｜可分离｜非high｜A级｜污染｜锚点｜结论｜原文定位（文件＋provenance 页位）｜备注。四滤/A级以 P=pass、F=fail 记。

### bushi-quanshu-beixuan（未用 0 例）

（本子池未用例 0，无逐例行。）

### cezi-zichu（未用 0 例）

（本子池未用例 0，无逐例行。）

### density-checks（未用 0 例）

（本子池未用例 0，无逐例行。）

### huangjince-huozhulin（未用 0 例）

（本子池未用例 0，无逐例行。）

### liuren-bianyi-yuce（未用 107 例）

| id | 子池 | 体系/来源 | 逐字 | 独立结局 | 可分离 | 非high | A级 | 污染 | 锚点 | 结论 | 原文定位 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BY-012 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例十四，书p157（PDF p169） |  |
| BY-014 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例十六，书p158（PDF p170） |  |
| BY-015 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例十七，书p159（PDF p171） |  |
| BY-016 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例十八，书p159-160（PDF p171-172） |  |
| BY-017 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例十九，书p160（PDF p172） |  |
| BY-018 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例二十，书p160-161（PDF p172-173） |  |
| BY-019 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例二十一，书p161（PDF p173） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-020 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例二十二，书p161-162（PDF p173-174） |  |
| BY-021 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例二十三，书p162（PDF p174） |  |
| BY-022 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例二十四，书p162-163（PDF p174-175） |  |
| BY-023 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例二十五，书p163（PDF p175） |  |
| BY-024 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例二十七，书p164（PDF p176） |  |
| BY-025 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例二十八，书p165（PDF p177） |  |
| BY-027 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例三十，书p166（PDF p178） |  |
| BY-028 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例三十一，书p166-167（PDF p178-179） |  |
| BY-029 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例三十二，书p167（PDF p179） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-030 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例三十四，书p168（PDF p180） |  |
| BY-031 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例三十五，书p168（PDF p180） |  |
| BY-032 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例三十六，书p169（PDF p181） |  |
| BY-033 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例三十八，书p170（PDF p182） |  |
| BY-034 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例四十，书p171（PDF p183） |  |
| BY-035 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例四十一，书p171-172（PDF p183-184） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-036 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例四十二，书p172（PDF p184） |  |
| BY-037 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例四十三，书p172-173（PDF p184-185） |  |
| BY-038 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例四十五，书p173-174（PDF p185-186） |  |
| BY-039 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例四十六，书p174（PDF p186） |  |
| BY-041 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例四十八，书p175（PDF p187） |  |
| BY-042 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例四十九，书p175-176（PDF p187-188） |  |
| BY-043 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例五十一，书p177（PDF p189） |  |
| BY-044 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例五十二，书p177-178（PDF p189-190） |  |
| BY-045 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例五十三，书p178（PDF p190） |  |
| BY-046 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例五十四，书p179（PDF p191） |  |
| BY-047 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例五十六，书p180（PDF p192） |  |
| BY-048 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例五十七，书p180（PDF p192） |  |
| BY-049 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例五十八，书p181（PDF p193） |  |
| BY-050 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例五十九，书p181-182（PDF p193-194） |  |
| BY-051 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例六十，书p182（PDF p194） |  |
| BY-053 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例六十三，书p184（PDF p196） |  |
| BY-054 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例六十五，书p185（PDF p197） |  |
| BY-055 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例六十六，书p185-186（PDF p197-198） |  |
| BY-056 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例六十七，书p186（PDF p198） |  |
| BY-057 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例七十，书p188（PDF p200） |  |
| BY-058 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例七十一，书p188-189（PDF p200-201） |  |
| BY-059 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例七十三，书p189-190（PDF p201-202） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-060 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例七十四，书p190（PDF p202） |  |
| BY-061 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例七十五，书p190-191（PDF p202-203） |  |
| BY-062 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例七十六，书p191（PDF p203） |  |
| BY-063 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例七十七，书p191-192（PDF p203-204） |  |
| BY-064 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例七十八，书p192-193（PDF p204-205） |  |
| BY-066 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例八十，书p194（PDF p206） |  |
| BY-067 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例八十一，书p194（PDF p206） |  |
| BY-068 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例八十三，书p195-196（PDF p207-208） |  |
| BY-069 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例八十四，书p196（PDF p208） |  |
| BY-070 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例八十五，书p196-197（PDF p208-209） |  |
| BY-071 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例八十六，书p197（PDF p209） |  |
| BY-072 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例八十七，书p197-198（PDF p209-210） |  |
| BY-073 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例八十九，书p199（PDF p211） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-074 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例九十，书p199（PDF p211） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-075 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例九十一，书p200（PDF p212） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-076 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例九十二，书p200（PDF p212） |  |
| BY-077 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例九十三，书p201（PDF p213） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-078 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例九十四，书p201（PDF p213） |  |
| BY-079 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例九十六，书p202（PDF p214） |  |
| BY-080 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例九十七，书p203（PDF p215） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-081 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例九十八，书p203-204（PDF p215-216） |  |
| BY-083 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百，书p204-205（PDF p216-217） |  |
| BY-084 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇一，书p205（PDF p217） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-085 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | partial(缺月日) | 不合格（卡：锚点在场） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇二，书p206（PDF p218） | 课式头要素缺项：月日 |
| BY-086 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇三，书p206（PDF p218） |  |
| BY-087 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇四，书p207（PDF p219） |  |
| BY-088 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇六，书p208（PDF p220） |  |
| BY-089 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇七，书p208-209（PDF p220-221） |  |
| BY-090 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇八，书p209（PDF p221） |  |
| BY-091 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇九（其一），书p209-210（PDF p221-222） |  |
| BY-092 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百〇九（其二），书p210（PDF p222） |  |
| BY-093 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十，书p211（PDF p223） |  |
| BY-094 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十一，书p212（PDF p224） |  |
| BY-096 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十三，书p213（PDF p225） |  |
| BY-097 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十四，书p213-214（PDF p225-226） |  |
| BY-098 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十五，书p214（PDF p226） |  |
| BY-099 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十六，书p214-215（PDF p226-227） |  |
| BY-100 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十七，书p215（PDF p227） |  |
| BY-101 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十八，书p215-216（PDF p227-228） |  |
| BY-102 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百一十九，书p216（PDF p228） |  |
| BY-103 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百二十，书p216-217（PDF p228-229） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |
| BY-104 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百二十一，书p217（PDF p229） |  |
| BY-105 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百二十二，书p218（PDF p230） |  |
| BY-106 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百二十三，书p218-219（PDF p230-231） |  |
| BY-107 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百二十四，书p219（PDF p231） |  |
| BY-109 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；毕法案录课例一百二十六，书p220（PDF p232） |  |
| BY-110 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十，书p136-137（PDF p148-149） |  |
| BY-111 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十一，书p137（PDF p149） |  |
| BY-112 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十二，书p137-138（PDF p149-150） |  |
| BY-113 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十三，书p138（PDF p150） |  |
| BY-114 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十四，书p138-139（PDF p150-151） |  |
| BY-115 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十五，书p139（PDF p151） |  |
| BY-116 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十六，书p139（PDF p151） |  |
| BY-117 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十七，书p140（PDF p152） |  |
| BY-118 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十八，书p141（PDF p153） |  |
| BY-119 | liuren-bianyi-yuce | 六壬/《六壬辨疑·毕法案录》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；辨疑卷五占验一百二十九，书p141-142（PDF p153-154） |  |
| YX-001 | liuren-bianyi-yuce | 六壬/《大六壬预测学》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；第二章例一，书p22-25（PDF p12-13） |  |
| YX-002 | liuren-bianyi-yuce | 六壬/《大六壬预测学》 | P | P | P | F | P(A-low) | high | present | 不合格（卡：非high污染、low污染） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；第二章例二，书p26-28（PDF p14-15） | 复核污染改判 high（REVIEW-G §三） |
| YX-003 | liuren-bianyi-yuce | 六壬/《大六壬预测学》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；第二章例三，书p29-32（PDF p15-17） |  |
| YX-004 | liuren-bianyi-yuce | 六壬/《大六壬预测学》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；第二章例四，书p32-36（PDF p17-19） |  |
| YX-005 | liuren-bianyi-yuce | 六壬/《大六壬预测学》 | P | P | P | F | P(A-low) | high | present | 不合格（卡：非high污染、low污染） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；第二章例五，书p37-41（PDF p19-21） | 复核污染改判 high（REVIEW-G §三） |
| YX-006 | liuren-bianyi-yuce | 六壬/YX | P | F | F | F | F(待回源核) | high | present | 不合格（卡：独立结局、可分离、非high污染、A级、low污染） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；第六章第一节占婚姻例一，书p391-394（PDF p196-198） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三）；复核判断/验分离度不足（REVIEW-G §三(四)）；复核污染改判 high（REVIEW-G §三） |
| YX-007 | liuren-bianyi-yuce | 六壬/YX | P | F | P | P | F(待回源核) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl；第六章第一节占胎产例一，书p401-402（PDF p201-202） | 复核判待回源核：记录内结局不可确认独立具体（REVIEW-G §三） |

### liuren-cuiyan（未用 110 例）

| id | 子池 | 体系/来源 | 逐字 | 独立结局 | 可分离 | 非high | A级 | 污染 | 锚点 | 结论 | 原文定位 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CY-007 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验四叶，PDF p.154（丛刊页246） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CY-011 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验六叶，PDF p.155（丛刊页247） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-012 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验六叶，PDF p.155（丛刊页247） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-014 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验七叶，PDF p.156（丛刊页248） |  |
| CY-016 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验九叶，PDF p.157（丛刊页249） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-018 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十叶，PDF p.157（丛刊页249） | 结局尾语与断交缠（原卡自载）、主体事件（生后累年余而殇）可分离，按原卡 A-low 口径计可分离 pass、限度登记于此 |
| CY-019 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十一叶，PDF p.158（丛刊页250） |  |
| CY-020 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：独立结局、锚点在场） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十二叶，PDF p.158（丛刊页250） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述；课式头要素缺项：年 |
| CY-021 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：独立结局、锚点在场） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十二叶，PDF p.158（丛刊页250） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述；课式头要素缺项：年 |
| CY-022 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十三叶，PDF p.159（丛刊页251） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-024 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十四叶，PDF p.159（丛刊页251） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-025 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十四叶，PDF p.159（丛刊页251） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-026 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十五叶，PDF p.160（丛刊页252） |  |
| CY-029 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十六叶，PDF p.160（丛刊页252） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-031 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十七叶，PDF p.161（丛刊页253） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-032 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十八叶，PDF p.161（丛刊页253） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-033 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十八叶，PDF p.161（丛刊页253） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-035 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验十九叶，PDF p.162（丛刊页254） |  |
| CY-036 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验二十叶，PDF p.162（丛刊页254） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-037 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验二十叶，PDF p.162（丛刊页254） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-038 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：独立结局、锚点在场） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿一叶，PDF p.163（丛刊页255） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述；课式头要素缺项：年 |
| CY-039 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿一叶，PDF p.163（丛刊页255） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-042 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿三叶，PDF p.164（丛刊页256） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-043 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿三叶，PDF p.164（丛刊页256） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-044 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿四叶，PDF p.164（丛刊页256） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-045 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿四叶，PDF p.164（丛刊页256） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-046 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿五叶，PDF p.165（丛刊页257） | 课式头要素缺项：年 |
| CY-048 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | F | F | F | P | F(B) | low | present | 不合格（卡：逐字原文、独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿六叶，PDF p.165（丛刊页257） | 验语尾字漫漶未能全读（原卡 grade_note）；原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CY-049 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：独立结局、锚点在场） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿七叶，PDF p.166（丛刊页258） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述；课式头要素缺项：年 |
| CY-050 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿七叶，PDF p.166（丛刊页258） |  |
| CY-051 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿八叶，PDF p.166（丛刊页258） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-052 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿九叶，PDF p.167（丛刊页259） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CY-053 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | F(B) | low | present | 不合格（卡：独立结局、A级） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验廿九叶，PDF p.167（丛刊页259） | 原卡自载无独立结局/后验段；原卡 outcome_grade=B（非 A 级） |
| CY-054 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验三十叶，PDF p.167（丛刊页259） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-055 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验三十叶，PDF p.167（丛刊页259） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-056 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：独立结局、锚点在场） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验卅一叶，PDF p.168（丛刊页260） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述；课式头要素缺项：年 |
| CY-058 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验卅二叶，PDF p.168（丛刊页260） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-059 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验卅二叶，PDF p.168（丛刊页260） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CY-060 | liuren-cuiyan | 六壬/《六壬粹言》卷六慕农占验附存 | P | F | P | P | F(B) | low | partial(缺日) | 不合格（卡：独立结局、A级、锚点在场） | expansion12/liuren-cuiyan/cases-munong.jsonl；卷六验卅三叶，PDF p.169（丛刊页261） | 原卡自载无独立结局/后验段；原卡 outcome_grade=B（非 A 级）；课式头要素缺项：日 |
| CYJ-001 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占一叶，PDF p.128（丛刊页220） |  |
| CYJ-002 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占一叶，PDF p.128（丛刊页220） |  |
| CYJ-003 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占二叶，PDF p.128（丛刊页220） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CYJ-004 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占二叶，PDF p.128（丛刊页220） |  |
| CYJ-005 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占三叶，PDF p.129（丛刊页221） |  |
| CYJ-006 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四叶，PDF p.129（丛刊页221） |  |
| CYJ-007 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四叶，PDF p.129（丛刊页221） |  |
| CYJ-008 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占五叶，PDF p.130（丛刊页222） |  |
| CYJ-009 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占六叶，PDF p.130（丛刊页222） |  |
| CYJ-010 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占七叶，PDF p.131（丛刊页223） |  |
| CYJ-012 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占八叶，PDF p.131（丛刊页223） |  |
| CYJ-013 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占八叶，PDF p.131（丛刊页223） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CYJ-014 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占九叶，PDF p.132（丛刊页224） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CYJ-015 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占九叶，PDF p.132（丛刊页224） |  |
| CYJ-016 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十叶，PDF p.132（丛刊页224） |  |
| CYJ-017 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十一叶，PDF p.133（丛刊页225） |  |
| CYJ-018 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十二叶，PDF p.133（丛刊页225） |  |
| CYJ-019 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十二叶，PDF p.133（丛刊页225） |  |
| CYJ-020 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十三叶，PDF p.134（丛刊页226） |  |
| CYJ-021 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十三叶，PDF p.134（丛刊页226） |  |
| CYJ-022 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十四叶，PDF p.134（丛刊页226） |  |
| CYJ-023 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十五叶，PDF p.135（丛刊页227） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CYJ-025 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十七叶，PDF p.136（丛刊页228） |  |
| CYJ-026 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十九叶，PDF p.137（丛刊页229） |  |
| CYJ-027 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十九叶，PDF p.137（丛刊页229） |  |
| CYJ-028 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占二十叶，PDF p.137（丛刊页229） |  |
| CYJ-029 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿一叶，PDF p.138（丛刊页230） |  |
| CYJ-030 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿一叶，PDF p.138（丛刊页230） |  |
| CYJ-031 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿二叶，PDF p.138（丛刊页230） |  |
| CYJ-032 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿三叶，PDF p.139（丛刊页231） |  |
| CYJ-033 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿三叶，PDF p.139（丛刊页231） |  |
| CYJ-034 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿四叶，PDF p.139（丛刊页231） |  |
| CYJ-035 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿五叶，PDF p.140（丛刊页232） |  |
| CYJ-036 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿六叶，PDF p.140（丛刊页232） |  |
| CYJ-038 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿九叶，PDF p.141（丛刊页233） |  |
| CYJ-039 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅一叶，PDF p.142（丛刊页234） |  |
| CYJ-040 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅二叶，PDF p.143（丛刊页235） | 课式头要素缺项：年 |
| CYJ-041 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅二叶，PDF p.143（丛刊页235） |  |
| CYJ-042 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅三叶，PDF p.143（丛刊页235） |  |
| CYJ-043 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅四叶，PDF p.144（丛刊页236） |  |
| CYJ-044 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅五叶，PDF p.144（丛刊页236） |  |
| CYJ-045 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅六叶，PDF p.145（丛刊页237） |  |
| CYJ-046 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅六叶，PDF p.145（丛刊页237） |  |
| CYJ-047 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅八叶，PDF p.146（丛刊页238） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-048 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅九叶，PDF p.146（丛刊页238） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CYJ-049 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占卅九叶，PDF p.146（丛刊页238） |  |
| CYJ-050 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十二叶，PDF p.148（丛刊页240） |  |
| CYJ-052 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | partial(缺年月) | 不合格（卡：锚点在场） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十三叶，PDF p.148（丛刊页240） | 课式头要素缺项：年月 |
| CYJ-053 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十四叶，PDF p.149（丛刊页241） |  |
| CYJ-054 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十五叶，PDF p.149（丛刊页241） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CYJ-055 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十五叶，PDF p.149（丛刊页241） |  |
| CYJ-056 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十六叶，PDF p.150（丛刊页242） |  |
| CYJ-057 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十六叶，PDF p.150（丛刊页242） |  |
| CYJ-058 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十七叶，PDF p.150（丛刊页242） |  |
| CYJ-059 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十七叶，PDF p.150（丛刊页242） |  |
| CYJ-060 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十八叶，PDF p.151（丛刊页243） |  |
| CYJ-061 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十八叶，PDF p.151（丛刊页243） |  |
| CYJ-062 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | partial(缺年月日) | 不合格（卡：锚点在场） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十九叶，PDF p.151（丛刊页243） | 课式头要素缺项：年月日 |
| CYJ-063 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | P | P | P(A-low) | low | present | 不合格（卡：独立结局） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十九叶，PDF p.151（丛刊页243） | 结局仅套语回声（果如所占/后果如所占类）、无独立事件记述 |
| CYJ-064 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占五十叶，PDF p.152（丛刊页244） |  |
| CYJ-065 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十五叶，PDF p.135（丛刊页227） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-066 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占十七叶，PDF p.136（丛刊页228） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-067 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占二十叶，PDF p.137（丛刊页229） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-068 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿二叶，PDF p.138（丛刊页230） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-069 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | partial(缺月) | 不合格（卡：独立结局、可分离、A级、锚点在场） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿六叶，PDF p.140（丛刊页232） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级）；课式头要素缺项：月 |
| CYJ-070 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占廿八叶，PDF p.141（丛刊页233） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-071 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十叶，PDF p.147（丛刊页239） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-072 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十叶，PDF p.147（丛刊页239） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-073 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十一叶，PDF p.147（丛刊页239） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-074 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十一叶，PDF p.147（丛刊页239） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |
| CYJ-075 | liuren-cuiyan | 六壬/《六壬粹言》卷五占验 | P | F | F | P | F(B) | low | present | 不合格（卡：独立结局、可分离、A级） | expansion12/liuren-cuiyan/cases-juan5.jsonl；卷五占四十三叶，PDF p.148（丛刊页240） | 原卡自载无独立结局/后验段；原卡自载断/验交缠不可分离；原卡 outcome_grade=B（非 A 级） |

### liuren-duanan（未用 123 例）

| id | 子池 | 体系/来源 | 逐字 | 独立结局 | 可分离 | 非high | A级 | 污染 | 锚点 | 结论 | 原文定位 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DA-025 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案025（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-033 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案033（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-034 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案034（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-035 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案035（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-036 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-a.jsonl；案036（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） | 课式头要素缺项：年 |
| DA-037 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案037（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-038 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案038（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-039 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-a.jsonl；案039（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） | 课式头要素缺项：年 |
| DA-041 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案041（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-042 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案042（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-044 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案044（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-046 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案046（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-047 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案047（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-048 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案048（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-050 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案050（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-051 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案051（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-054 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案054（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-055 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案055（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-057 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案057（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-059 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案059（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-060 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案060（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-061 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案061（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-062 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案062（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-063 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案063（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-064 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案064（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-065 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案065（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-066 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案066（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-067 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案067（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-068 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案068（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-070 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案070（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-071 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | F | P(A-low) | high | present | 不合格（卡：非high污染、low污染） | expansion12/liuren-duanan/cases-a.jsonl；案071（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） | 原卡 contamination=high |
| DA-072 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案072（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-073 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案073（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-074 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案074（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-075 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案075（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-076 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案076（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-077 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案077（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-078 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案078（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-079 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案079（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-080 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案080（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-081 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案081（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-082 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案082（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-083 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案083（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-085 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案085（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-086 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案086（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-087 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案087（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-088 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案088（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-090 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案090（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-091 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案091（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-092 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案092（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-093 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案093（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-094 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案094（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-095 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案095（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-096 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案096（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-097 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案097（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-098 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | F | P(A-low) | high | partial(缺月) | 不合格（卡：非high污染、low污染、锚点在场） | expansion12/liuren-duanan/cases-a.jsonl；案098（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） | 原卡 contamination=high；课式头要素缺项：月 |
| DA-099 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案099（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-100 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案100（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-101 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案101（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-102 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案102（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-104 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案104（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-107 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案107（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-110 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-a.jsonl；案110（底本数字文本；疏正/新编互校页图备于scratch-archive/mutual，本例底本断验文字可读、未触发定点查阅） |  |
| DA-112 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案112 |  |
| DA-113 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案113 |  |
| DA-114 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案114 |  |
| DA-115 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案115 |  |
| DA-116 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案116 |  |
| DA-118 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案118 |  |
| DA-120 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案120 |  |
| DA-121 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案121 |  |
| DA-132 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案132 |  |
| DA-135 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案135 |  |
| DA-137 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案137 |  |
| DA-139 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案139 |  |
| DA-142 | liuren-duanan | 六壬/《大六壬断案》 | P | P | F | F | P(A-low) | high | present | 不合格（卡：可分离、非high污染、low污染） | expansion12/liuren-duanan/cases-b.jsonl；案142 | 应验嵌于断语段内（抽例注记 §特别处置）；原卡 contamination=high |
| DA-144 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案144 |  |
| DA-146 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案146 |  |
| DA-148 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案148 |  |
| DA-149 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案149 |  |
| DA-150 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案150 |  |
| DA-153 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案153 | 课式头要素缺项：年 |
| DA-154 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案154 |  |
| DA-155 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案155 | 课式头要素缺项：年 |
| DA-156 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | F | P(A) | high | present | 不合格（卡：非high污染、low污染） | expansion12/liuren-duanan/cases-b.jsonl；案156 | 原卡 contamination=high |
| DA-157 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案157 |  |
| DA-160 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案160 |  |
| DA-161 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案161 |  |
| DA-162 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案162 | 课式头要素缺项：年 |
| DA-163 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案163 | 课式头要素缺项：年 |
| DA-168 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案168 |  |
| DA-170 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案170 |  |
| DA-171 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案171 |  |
| DA-172 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案172 |  |
| DA-173 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案173 |  |
| DA-175 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案175 |  |
| DA-176 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案176 |  |
| DA-177 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案177 |  |
| DA-179 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案179 | 课式头要素缺项：年 |
| DA-181 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案181 | 课式头要素缺项：年 |
| DA-183 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案183 | 课式头要素缺项：年 |
| DA-185 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案185 |  |
| DA-187 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案187 | 课式头要素缺项：年 |
| DA-188 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案188 | 课式头要素缺项：年 |
| DA-189 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案189 | 课式头要素缺项：年 |
| DA-192 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案192 |  |
| DA-194 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案194 | 课式头要素缺项：年 |
| DA-198 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案198 | 课式头要素缺项：年 |
| DA-199 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案199 | 课式头要素缺项：年 |
| DA-200 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案200 | 课式头要素缺项：年 |
| DA-204 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案204 | 课式头要素缺项：年 |
| DA-206 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案206 |  |
| DA-207 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案207 |  |
| DA-208 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案208 |  |
| DA-209 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案209 |  |
| DA-210 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案210 |  |
| DA-212 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案212 | 课式头要素缺项：年 |
| DA-213 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案213 | 课式头要素缺项：年 |
| DA-214 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案214 | 课式头要素缺项：年 |
| DA-217 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案217 |  |
| DA-218 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | partial(缺年) | 不合格（卡：锚点在场） | expansion12/liuren-duanan/cases-b.jsonl；案218 | 课式头要素缺项：年 |
| DA-219 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | P | P(A-low) | low | present | eligible | expansion12/liuren-duanan/cases-b.jsonl；案219 |  |
| DA-221 | liuren-duanan | 六壬/《大六壬断案》 | P | P | P | F | P(A) | high | present | 不合格（卡：非high污染、low污染） | expansion12/liuren-duanan/cases-b.jsonl；案221 | 原卡 contamination=high |

## 三、分面计数

| 子池 | 池层 id 总量 | 已用命中 | 未用 | eligible | 不合格 |
|---|---|---|---|---|---|
| bushi-quanshu-beixuan | 9 | 9 | 0 | 0 | 0 |
| cezi-zichu | 0 | 0 | 0 | 0 | 0 |
| density-checks | 0 | 0 | 0 | 0 | 0 |
| huangjince-huozhulin | 1 | 1 | 0 | 0 | 0 |
| liuren-bianyi-yuce | 126 | 19 | 107 | 91 | 16 |
| liuren-cuiyan | 136 | 26 | 110 | 55 | 55 |
| liuren-duanan | 167 | 44 | 123 | 97 | 26 |
| **合计** | **439** | **99** | **340** | **243** | **97** |

- 按体系：六壬 eligible 243（未用 340）；六爻 eligible 0（未用 0）。
- **非六爻 eligible 合计 243**；六爻 eligible 合计 0。（本组子池体系构成：六壬＋六爻，无八字/奇门/测字/紫微例。）
- 锚点分布（未用 340 例）：present 306、partial 34、absent 0。
- 不合格所卡滤项计数（一例可卡多项）：
  - 逐字原文：1
  - 独立结局：64
  - 可分离：17
  - 非high污染：8
  - A级：30
  - low污染：8
  - 锚点在场：34

## 四、异常与限度说明

1. **cezi-zichu、density-checks 两子池无 jsonl 文件**（盘上实况：cezi-zichu 仅 CHAPTER-DRAFT.md、EXTRACTION-NOTES.md、work-ocr/、work-pages/；density-checks 仅 CENSUS-NOTES.md），池层 id 总量 0、未用 0、无逐例可核——《字触》成例从未抽例建池（提炼件自载「未逐条全录、后续抽例建池另行处理」）、density-checks 为密度普查件（定案 NO-GO、不产 cases），与盘上登记一致，只登记不另断。
2. **bushi-quanshu-beixuan（BQ-026–034，9 例）与 huangjince-huozhulin（HZ-001）未用均为 0**：9＋1 例 id 全部命中已用并集（BQ 系经 holdout14 inputs 卡、HZ-001 经 holdout12 inputs 卡），本轮无逐例核查对象；其资格状态以既往封存集登记为准、本席不重判。
3. **六壬锚点口径限度**：本组六壬池卡无独立 anchor 字段，锚点以原卡 asked_at 课式头四要素（年月日时）判定（口径与实据见卷首口径节）；盘面本体（四课三传/天地盘）未载于池卡——断案系底本全文（liuren-duanan/scratch-archive/cases_raw.json）在盘、辨疑系原书课盘体例经 holdout12 建集日志登记、粹言系原书有课盘列而池卡未录盘字（holdout12 建集日志逐例 fidelity 登记在案），组集建卡时仍须逐例回原文复核盘面，本台账之 present 不替代建卡复核。
4. **粹言慕农套语结局 30 余例**：cases-munong.jsonl 中多例 outcome 仅载「后果如所占」类套语（转录底稿 TRANSCRIPTION-NOTES.md 同型），原抽例席按 A-low 收录；本席承 REVIEW-G 同型判例（仅凭记录内文本核断）判独立结局不成立。此为本组最大不合格来源之一；若主持日后回原书页图核得案验全文更完整者，可逐例升回，本台账只按盘上记录现状判定。
5. **断案系课式头无年份 20 余例**：cases-a/b 部分例 asked_at 未载年份（底本同段年份未逐例明载、抽例注记自载「个别案底本课式头无年份照原样保留」），按「升 present 须原文实据」判 partial；其余四滤与分级多全过，卡点仅在锚点一项，逐例已于台账备注注明缺项。
6. 本席未打开任何已封存集金标正文（已用并集只取金标 id 字段）、未打开 runs/ 下 predictions/judging/final-scores；对 runs/ 目录未做列表/计数操作（本轮 runs/round84/supply 内本席文件除外）；池层原文只读未改。回传数字以主持复算为准。
