# STOCK-RECOUNT-h26 —— holdout26 供给存量盘上全口径复算（R81 组集席·第一阶段）

本件为组集线第一阶段产出：只复算登记，不建卡、不封存、不作断、不评分、不做 git 操作。复算脚本 `runs/round81/recount_stock_r81.py`（唯一名，盘上实算），中间结果 `runs/round81/recount_stock_r81_out.json`；渲染脚本 `runs/round81/render_recount_r81.py`。台账/结局文本一律按数据处理。

## 口径（写定依据）

- 依据：`runs/round81/PREREG.md` §4 与 `data/holdout25-seal-log.md` §一/§二。
- 已用并集：盘上逐 id 实算 **1085**（dev 488＋phase2 splits2 holdout2 29＋holdout3–25 金标 id 673＋holdout inputs 卡 id 514＋顶层 inputs6–10 卡 id 412，五源并集去重；与主持开轮实算一致，本席以 `count_used_union_r81.py` 同口径复跑断言 1085 通过）。零复用＝台账 id 与该并集逐 id 零命中；**同名即剔**（无论内容相涉与否）。
- 资格口径（eligible）：A 级、污染 low、锚点在场（六爻面五要素：卦名、动爻、世应、六亲纳支、月建日辰，六神不属要件；他体系以各台账 anchor 字段口径）、未用、四滤（逐字原文、独立结局、可分离、非 high 污染）。各台账资格字段读法以历轮构建脚本为准（`runs/round80/build_holdout25_r80.py`、`runs/round79/build_holdout24_r79.py`）：无 eligible_net/grade 字段之台账，按构建脚本实际采用的字段组合判定，逐件注记。
- ZCB-003 维持排除（主持裁处未撤销），单独登记、不计 eligible（§四）。

## 一、主台账逐源复算（已知面）

### 1. 段建业《段氏理象学》DS（r76）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json`；体系：bazi（八字）；台账总例数：**63**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| eligible_net=true | 0 | （无） | 63 |
| anchor present | 0 | （无） | 63 |
| contamination low | 1 | DS-047 | 62 |
| 四滤全pass | 0 | （无） | 62 |
| 断语/结局非空 | 0 | （无） | 62 |

- 资格全过（qualified）：62；其中已用（与已用并集逐 id 命中）：30——DS-001、DS-002、DS-003、DS-004、DS-005、DS-006、DS-007、DS-008、DS-009、DS-010、DS-011、DS-012、DS-013、DS-014、DS-015、DS-016、DS-017、DS-018、DS-019、DS-020、DS-021、DS-022、DS-023、DS-024、DS-025、DS-026、DS-027、DS-028、DS-029、DS-030。
- **eligible 未用：32**——DS-031、DS-032、DS-033、DS-034、DS-035、DS-036、DS-037、DS-038、DS-039、DS-040、DS-041、DS-042、DS-043、DS-044、DS-045、DS-046、DS-048、DS-049、DS-050、DS-051、DS-052、DS-053、DS-054、DS-055、DS-056、DS-057、DS-058、DS-059、DS-060、DS-061、DS-062、DS-063。

注记：台账 count 字段登记 registered 63、four_filter_pass_net 63、anchor_present 63、contamination_medium 1（DS-047）、low 62，与本席漏斗一致。DS-033 为同造合并组唯一卡（其组未被既往集取用），在未用名单内；同造组至多取 1 之限属组集阶段规则，本阶段只登记存量。

### 2. 张志春《开悟之门》QM 开悟（r76）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-kaiwu-r76.json`；体系：qimen（奇门）；台账总例数：**52**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present | 0 | （无） | 52 |
| contamination low | 0 | （无） | 52 |
| separable=true | 0 | （无） | 52 |
| stem_check天地盘双ok(全合) | 14 | QM-017、QM-026、QM-033、QM-041、QM-050、QM-051、QM-053、QM-054、QM-056、QM-057、QM-059、QM-060、QM-061、QM-062 | 38 |
| 断语/结局非空 | 0 | （无） | 38 |

- 资格全过（qualified）：38；其中已用（与已用并集逐 id 命中）：20——QM-011、QM-012、QM-013、QM-014、QM-015、QM-016、QM-018、QM-019、QM-020、QM-021、QM-022、QM-023、QM-024、QM-025、QM-027、QM-028、QM-029、QM-030、QM-031、QM-032。
- **eligible 未用：18**——QM-034、QM-035、QM-036、QM-037、QM-038、QM-039、QM-040、QM-042、QM-043、QM-044、QM-045、QM-046、QM-047、QM-048、QM-049、QM-052、QM-055、QM-058。

注记：本台账无 grade/eligible_net/filters 字段，资格读法承构建脚本：present∧low∧separable∧stem_check 天地盘双 ok（全合）∧断语/结局非空。未全合 14 例（QM-017、QM-026、QM-033、QM-041、QM-050、QM-051、QM-053、QM-054、QM-056、QM-057、QM-059、QM-060、QM-061、QM-062）不入资格集，与 holdout25 封存日志 §一.1 登记一致。

### 3. 刘文元《奇门启悟》QM 启悟（r76）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-qiwu-r76.json`；体系：qimen（奇门）；台账总例数：**11**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present | 0 | （无） | 11 |
| contamination low | 0 | （无） | 11 |
| separable=true | 0 | （无） | 11 |
| 断语/结局非空 | 0 | （无） | 11 |

- 资格全过（qualified）：11；其中已用（与已用并集逐 id 命中）：9——QM-201、QM-202、QM-203、QM-204、QM-205、QM-206、QM-207、QM-208、QM-209。
- **eligible 未用：2**——QM-210、QM-211。

注记：资格读法承构建脚本：present∧low∧separable∧断语/结局非空（本台账无 stem_check/grade/eligible_net 字段）。

### 4. 石建国《奇门遁甲最新实例解析》QM 石建国（r76）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-shijianguo-r76.json`；体系：qimen（奇门）；台账总例数：**11**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present | 0 | （无） | 11 |
| contamination low | 0 | （无） | 11 |
| separable=true | 0 | （无） | 11 |
| 断语/结局非空 | 0 | （无） | 11 |

- 资格全过（qualified）：11；其中已用（与已用并集逐 id 命中）：11——QM-301、QM-302、QM-303、QM-304、QM-305、QM-306、QM-307、QM-308、QM-309、QM-310、QM-311。
- **eligible 未用：0**——（无）。

注记：资格读法同启悟。台账另有 screened_out 6 例（池外淘汰登记，非台账 cases 计数内）。11 例已全部用尽（holdout22–25），未用 0。

### 5. 《字触补》ZCB（r76）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json`；体系：cezi（测字）；台账总例数：**36**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| eligible=true | 17 | ZCB-020、ZCB-021、ZCB-022、ZCB-023、ZCB-024、ZCB-025、ZCB-026、ZCB-027、ZCB-028、ZCB-029、ZCB-030、ZCB-031、ZCB-032、ZCB-033、ZCB-034、ZCB-035、ZCB-036 | 19 |
| anchor present | 0 | （无） | 19 |
| contamination low | 4 | ZCB-016、ZCB-017、ZCB-018、ZCB-019 | 15 |
| separable=true | 0 | （无） | 15 |
| 断语/结局非空 | 0 | （无） | 15 |

- 资格全过（qualified）：15；其中已用（与已用并集逐 id 命中）：14——ZCB-001、ZCB-002、ZCB-004、ZCB-005、ZCB-006、ZCB-007、ZCB-008、ZCB-009、ZCB-010、ZCB-011、ZCB-012、ZCB-013、ZCB-014、ZCB-015。
- **eligible 未用：0**——（无）。

注记：资格全过 15－已用 14＝未用 1 例，即 ZCB-003；ZCB-003 经主持裁处维持排除（§四单独登记），**可选 eligible 未用＝0**，与 holdout25 封存日志 §一.1 复算一致。

### 6. 王虎应《六爻卦例说真》GSZ（r57）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json`；体系：liuyao（六爻）；台账总例数：**113**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| grade A | 49 | GSZ-001、GSZ-002、GSZ-004、GSZ-006、GSZ-007、GSZ-008、GSZ-010、GSZ-011、GSZ-012、GSZ-013、GSZ-014、GSZ-018、GSZ-019、GSZ-021、GSZ-025、GSZ-029、GSZ-035、GSZ-036、GSZ-037、GSZ-039、GSZ-040、GSZ-044、GSZ-045、GSZ-048、GSZ-051、GSZ-056、GSZ-057、GSZ-062、GSZ-063、GSZ-064、GSZ-065、GSZ-066、GSZ-067、GSZ-070、GSZ-071、GSZ-072、GSZ-073、GSZ-076、GSZ-083、GSZ-085、GSZ-087、GSZ-090、GSZ-095、GSZ-096、GSZ-097、GSZ-102、GSZ-106、GSZ-112、GSZ-113 | 64 |
| pollution low | 0 | （无） | 64 |
| anchor present | 0 | （无） | 64 |
| eligible_net=true | 1 | GSZ-027 | 63 |
| 四滤全true | 0 | （无） | 63 |
| 断语/结局非空 | 0 | （无） | 63 |

- 资格全过（qualified）：63；其中已用（与已用并集逐 id 命中）：33——GSZ-003、GSZ-005、GSZ-009、GSZ-015、GSZ-016、GSZ-017、GSZ-022、GSZ-023、GSZ-024、GSZ-026、GSZ-028、GSZ-030、GSZ-031、GSZ-032、GSZ-033、GSZ-034、GSZ-038、GSZ-041、GSZ-042、GSZ-043、GSZ-046、GSZ-047、GSZ-049、GSZ-050、GSZ-052、GSZ-053、GSZ-054、GSZ-055、GSZ-058、GSZ-059、GSZ-060、GSZ-061、GSZ-068。
- **eligible 未用：30**——GSZ-020、GSZ-069、GSZ-074、GSZ-075、GSZ-077、GSZ-078、GSZ-079、GSZ-080、GSZ-081、GSZ-082、GSZ-084、GSZ-086、GSZ-088、GSZ-089、GSZ-091、GSZ-092、GSZ-093、GSZ-094、GSZ-098、GSZ-099、GSZ-100、GSZ-101、GSZ-103、GSZ-104、GSZ-105、GSZ-107、GSZ-108、GSZ-109、GSZ-110、GSZ-111。

注记：资格全过集与台账 counts.net_eligible_A_low_present 名单（63）逐 id 相等（本席断言 qualified_equals_net_list＝true）。GSZ 另有建卡口径五要素复核（承 build_holdout25_r80.py：逐例回原书文字层 `runs/round76/gsz-book-r76.txt` 以构建脚本同一 five_elements 函数复核）：未用 30 例中五要素全在场 **24** 例——GSZ-069、GSZ-074、GSZ-075、GSZ-077、GSZ-078、GSZ-079、GSZ-081、GSZ-084、GSZ-086、GSZ-088、GSZ-091、GSZ-092、GSZ-093、GSZ-098、GSZ-099、GSZ-100、GSZ-101、GSZ-103、GSZ-104、GSZ-105、GSZ-107、GSZ-108、GSZ-109、GSZ-110；五要素不过 **6** 例——GSZ-020、GSZ-080、GSZ-082、GSZ-089、GSZ-094、GSZ-111，六例均仅「动爻」一要素缺如（静卦、变卦空，与 GSZ-020 历轮换例先例同型，逐例 elements 明细在复算 JSON）。故 GSZ 按台账净资格未用 30、按建卡口径 eligible 未用 24，两数并列登记。

### 7. 王虎应《六爻分类占验技法》一轮 WHY-001–071（r56）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json`；体系：liuyao（六爻）；台账总例数：**71**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present | 19 | WHY-001、WHY-002、WHY-029、WHY-050、WHY-051、WHY-053、WHY-054、WHY-055、WHY-056、WHY-057、WHY-058、WHY-059、WHY-060、WHY-061、WHY-062、WHY-063、WHY-064、WHY-065、WHY-066 | 52 |
| pollution low | 12 | WHY-013、WHY-014、WHY-017、WHY-018、WHY-019、WHY-020、WHY-045、WHY-046、WHY-047、WHY-048、WHY-049、WHY-052 | 40 |
| counts净入账名单成员 | 0 | （无） | 40 |

- 资格全过（qualified）：40；其中已用（与已用并集逐 id 命中）：5——WHY-003、WHY-015、WHY-021、WHY-030、WHY-067。
- **eligible 未用：35**——WHY-004、WHY-005、WHY-006、WHY-007、WHY-008、WHY-009、WHY-010、WHY-011、WHY-012、WHY-016、WHY-022、WHY-023、WHY-024、WHY-025、WHY-026、WHY-027、WHY-028、WHY-031、WHY-032、WHY-033、WHY-034、WHY-035、WHY-036、WHY-037、WHY-038、WHY-039、WHY-040、WHY-041、WHY-042、WHY-043、WHY-044、WHY-068、WHY-069、WHY-070、WHY-071。

注记：本台账 entries 无 grade/filters/eligible_net 字段（键集实查见复算 JSON entry_keys_union），净入账以台账 counts.net_eligible_A_low_present 名单（40）为准；本席漏斗以 anchor_presence∧pollution∧名单成员三级复算，资格全过集与名单逐 id 相等（断言通过）。已用 5 例为 holdout20 取例，与 SUPPLY-ACCOUNTING-r59 §一（可选未用 35）一致。

### 8. 王虎应《六爻分类占验技法》二轮 WHY-072–117（r57-r2）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json`；体系：liuyao（六爻）；台账总例数：**46**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| grade A | 5 | WHY-076、WHY-094、WHY-113、WHY-116、WHY-117 | 41 |
| pollution low | 0 | （无） | 41 |
| anchor present | 1 | WHY-102 | 40 |
| eligible_net=true | 4 | WHY-077、WHY-097、WHY-101、WHY-105 | 36 |
| 四滤全true | 0 | （无） | 36 |
| 断语/结局非空 | 0 | （无） | 36 |

- 资格全过（qualified）：36；其中已用（与已用并集逐 id 命中）：6——WHY-072、WHY-073、WHY-074、WHY-075、WHY-078、WHY-079。
- **eligible 未用：30**——WHY-080、WHY-081、WHY-082、WHY-083、WHY-084、WHY-085、WHY-086、WHY-087、WHY-088、WHY-089、WHY-090、WHY-091、WHY-092、WHY-093、WHY-095、WHY-096、WHY-098、WHY-099、WHY-100、WHY-103、WHY-104、WHY-106、WHY-107、WHY-108、WHY-109、WHY-110、WHY-111、WHY-112、WHY-114、WHY-115。

注记：资格全过集与台账 counts 名单（36）逐 id 相等（断言通过）。台账另有 registered_only 2 件（WHY-R2-REG-01 月球例等）不在 entries 46 内、不入账。已用 6 例为 holdout21 取例，与 SUPPLY-ACCOUNTING-r59 §一（可选未用 30）一致。

### 9. 曲炜《详批命例精解》QW（r56）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-quwei-r56.json`；体系：bazi（八字）；台账总例数：**34**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present | 17 | QW-018、QW-019、QW-020、QW-021、QW-022、QW-023、QW-024、QW-025、QW-026、QW-027、QW-028、QW-029、QW-030、QW-031、QW-032、QW-033、QW-034 | 17 |
| pollution low | 0 | （无） | 17 |
| 四滤全pass | 0 | （无） | 17 |
| 结局非空 | 0 | （无） | 17 |

- 资格全过（qualified）：17；其中已用（与已用并集逐 id 命中）：17——QW-001、QW-002、QW-003、QW-004、QW-005、QW-006、QW-007、QW-008、QW-009、QW-010、QW-011、QW-012、QW-013、QW-014、QW-015、QW-016、QW-017。
- **eligible 未用：0**——（无）。

注记：本台账无 grade/eligible_net 字段，资格读法：anchor present∧pollution low∧四滤全 pass∧结局非空，present 集 17 例（QW-001–017）已全部用尽（holdout20 用 12＋holdout21 用 5），未用 0，与 SUPPLY-ACCOUNTING-r59 §一一致。partial 17 例（QW-018–034）经 SUPPLY-RECHECK-qwpartial-r57 复核升格 0、维持 partial，不入资格集。

### 10. 曲炜《详批命例精解》续抽 QW-035–038（r59）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round59/digestion/SUPPLY-MINING-quwei-r59.json`；体系：bazi（八字）；台账总例数：**4**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present | 4 | QW-035、QW-036、QW-037、QW-038 | 0 |
| pollution low | 0 | （无） | 0 |
| 四滤全pass | 0 | （无） | 0 |
| eligible_net=true | 0 | （无） | 0 |
| 断语/结局非空 | 0 | （无） | 0 |

- 资格全过（qualified）：0；其中已用（与已用并集逐 id 命中）：0——（无）。
- **eligible 未用：0**——（无）。

注记：4 例锚点皆 partial（出生信息原文未载），资格 0、可选增量 0，与台账 count.optional_pool_increment＝0 一致。

### 11. 奇门旧池 QM-001–010（r56，杜新会/张志春两书）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-qimen-r56.json`；体系：qimen（奇门）；台账总例数：**10**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present(台账) | 0 | （无） | 10 |
| pollution low(台账) | 1 | QM-009 | 9 |
| R58复核 eligible_optional=true | 0 | （无） | 9 |
| 断语/结局非空 | 0 | （无） | 9 |

- 资格全过（qualified）：9；其中已用（与已用并集逐 id 命中）：8——QM-001、QM-002、QM-003、QM-004、QM-005、QM-006、QM-007、QM-008。
- **eligible 未用：1**——QM-010。

注记：台账路径 `runs/round56/digestion/SUPPLY-MINING-qimen-r56.json`；资格承 QM-REVIEW-r58 复核（`runs/round58/digestion/QM-REVIEW-r58.json`）：eligible_optional 9 例（QM-001–008、QM-010），QM-009 pollution＝mid 只建池不入可选。已用 8（holdout21），未用 1＝QM-010，与 SUPPLY-ACCOUNTING-r59 §一一致。

### 复核件登记（只登记、无增量）

- `runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.json`：QW partial 复核 17 例，升 present 0。
- `runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.json`：WHY partial/未净候选复核 41 例，升格 0、可选增量 0（含去重 8 例维持不入账）。
- `runs/round56/digestion/SUPPLY-GOLD-SUPPLEMENT-r56.json`：holdout20 已用 17 例之断语逐字补录件，非新供给面，其 id 全部已用，不另计存量。

## 二、主台账汇总（逐体系）

| 体系 | eligible 未用（台账净资格口径） | eligible 未用（建卡口径，GSZ 过五要素复核） | 构成 id |
|---|---|---|---|
| bazi（八字） | 32 | 32 | DS 32＋QW 0 |
| qimen（奇门） | 21 | 21 | 开悟 18＋启悟 2＋石建国 0＋旧池 1 |
| liuyao（六爻） | 95 | 89 | GSZ 30（建卡口径 24）＋WHY 一轮 35＋WHY 二轮 30 |
| cezi（测字） | 0 | 0 | ZCB 可选 0（ZCB-003 裁处排除，§四） |
| **合计** | **148** | **142** | |

逐 id 全列见 §一各台账节。以下 §五可达性核算以建卡口径 142 为基数（GSZ 五要素不过 6 例单列、不入基数）。

## 三、全体系口径普查——旧面台账（上列主台账未覆盖面）

检索以历轮登记档（SUPPLY-ACCOUNTING 链、STOCK-ANCHOR-r53、CENSUS 件）为先、逐名定性；下列各面均完整跑完（台账逐件打开、逐 id 与已用并集对勘），非中断登记。

### 3.1 supply-ledger r46–r50（夷坚/春渚/阅微/类考/梦占/逸旨/玄解/三书诸面统一入账台账）

| 台账路径 | 登记条目数 | counted（合规入账） | counted 已用 | counted 未用 |
|---|---|---|---|---|
| `runs/round46/digestion/supply-ledger-r46.jsonl` | 20 | 1 | 1 | （无） |
| `runs/round47/digestion/supply-ledger-r47.jsonl` | 42 | 15 | 15 | （无） |
| `runs/round48/digestion/supply-ledger-r48.jsonl` | 10 | 2 | 2 | （无） |
| `runs/round49/digestion/supply-ledger-r49.jsonl` | 14 | 9 | 6 | YJ2-008、YJ2-011、YJ2-013 |
| `runs/round50/digestion/supply-ledger-r50-rest.jsonl` | 6 | 1 | 1 | （无） |
| `runs/round50/digestion/supply-ledger-r50-yijian.jsonl` | 8 | 5 | 5 | （无） |

- counted 合计 33，已用 30，未用仅 3：YJ2-008、YJ2-011、YJ2-013（r49 夷坚面）。
- 该 3 例锚点资格经 STOCK-ANCHOR-r53 逐例标记为**不在场**（YJ2-008 卦象全缺、YJ2-011 谶语/占式全缺、YJ2-013 盘面/数式全缺），不合「仅锚点在场」口径——**eligible 未用＝0**。
- 未 counted 条目均为 B 级/mid/high/只登记/普查汇总行，逐件登记于各台账 verdict/host_check，不入资格集。
- 覆盖面逐名登记：夷坚志（YJ/YJ2/YJ3/YJ4/SS 诸号）、阅微草堂笔记（yw-*/YW2/YW3/YW4/YW5 诸号）、梦占类考（LK/LK2）、梦占逸旨（YZ-C）、梦林玄解（XJ47）、春渚纪闻（CZ2，见 3.2）、三书杂面（SS 课占/遁甲/扶乩等）。

### 3.2 cards-mining 逐面卡目录（r46–r53）

| 目录 | 卡 id 数 | 已用命中 | 未用 id |
|---|---|---|---|
| `runs/round46/digestion/cards-mining` | 2 | 0 | yw-dongming、yw-mo |
| `runs/round47/digestion/cards-mining-yijian` | 7 | 3 | YJ-002、YJ-003、YJ-005、YJ-007 |
| `runs/round48/digestion/cards-mining-sanshu` | 6 | 2 | SS-002、SS-003、SS-004、SS-006 |
| `runs/round49/digestion/cards-mining-yijian-r49` | 13 | 6 | YJ2-001、YJ2-002、YJ2-003、YJ2-004、YJ2-008、YJ2-011、YJ2-013 |
| `runs/round49/digestion/cards-mining-yuewei` | 1 | 0 | YW2-001 |
| `runs/round50/digestion/cards-mining-yijian-r50` | 5 | 5 | （无） |
| `runs/round50/digestion/cards-mining-yuewei-r50` | 2 | 1 | YW3-002 |
| `runs/round51/digestion/cards-mining-chunzhu-r51` | 5 | 3 | CZ2-004、CZ2-005 |
| `runs/round51/digestion/cards-mining-yijian-r51` | 11 | 0 | YJ4-001、YJ4-002、YJ4-003、YJ4-004、YJ4-005、YJ4-006、YJ4-007、YJ4-008、YJ4-009、YJ4-010、YJ4-011 |
| `runs/round51/digestion/cards-mining-yuewei-r51` | 1 | 0 | YW4-001 |
| `runs/round52/digestion/cards-mining-leikao-r52` | 2 | 0 | LK2-C48、LK2-C51 |
| `runs/round52/digestion/cards-mining-yuewei-r52` | 3 | 0 | YW5-001、YW5-002、YW5-003 |
| `runs/round53/digestion/cards-mining-chunzhu-r53` | 1 | 1 | （无） |
| `runs/round53/digestion/cards-mining-leikao-r53` | 1 | 0 | LK2-C58 |
| `runs/round53/digestion/cards-mining-yuewei-r53` | 1 | 0 | YW5-004 |

未用卡逐面定性（依据均为历轮登记档）：

- 阅微 yw-mo、yw-dongming（r46 台账）：contamination high、registered-not-counted——eligible 未用 0。
- 夷坚 YJ-002、YJ-003、YJ-005、YJ-007（r47 台账）：high 只登记／B 级／mid，不入账——0。
- 三书 SS-002、SS-003、SS-004、SS-006（r48 台账）：counted＝false（mid／B 确认式结局）——0。
- 夷坚 YJ2-001–004（r49 台账聚合行）：contamination mid、counted＝false——0；YJ2-008/011/013 见 3.1（锚点不在场）——0。
- 阅微 YW2-001（r49 台账）：B 级、counted＝false——0。YW3-002（r50 台账）：B 级、counted＝false——0。
- 阅微 YW4-001（SUPPLY-ACCOUNTING-r51）：主持改判 B 级、污染 low-mid，只登记不入账——0。
- 阅微 YW5-001（STOCK-ANCHOR-r53）：锚点部分在场、所缺为决定性属性（按不在场同格）——0；YW5-002、YW5-003（SUPPLY-ACCOUNTING-r52）：A 级但 low-mid，只登记不入账——0；YW5-004（SUPPLY-ACCOUNTING-r53）：锚点决定性属性不在源文，只登记不入账——0。
- 春渚 CZ2-004、CZ2-005（STOCK-ANCHOR-r53）：锚点不在场／部分在场缺决定性属性——0。（CZ2-001/002/003/006 已用尽。）
- 夷坚 YJ4-001–011（STOCK-ANCHOR-r53）：11 例锚点全不在场或部分在场缺决定性属性——0。
- 类考 LK2-C48、LK2-C51（SUPPLY-ACCOUNTING-r52）：A 级但污染 mid，只登记不入账——0；LK2-C58（SUPPLY-ACCOUNTING-r53）：与已用 XJ47-092 同案异文、卡已裁撤，不作独立候选——0。
- 类考续读 LK2-C61、C62（SUPPLY-ACCOUNTING-r54）：俱同案（YZ-C019／XJ47-572，均已用）不重复入账、未建卡——0。类考面经 r54 登记全书检毕；夷坚近穷尽、春渚近穷尽、阅微检毕（SUPPLY-ACCOUNTING-r54 §定性，照录不另断）。

### 3.3 旧测字池 ZC（《字触》旧池，r38–r41 抽例、r48 汇总台账）

- 台账：`runs/round48/digestion/work-cezi-r48/zc-entries-summary-r48.json`（总 165 条）＋ `runs/round48/digestion/CENSUS-zichuquan-r48.md`。
- eligible 形态（A＋low＋eligible＝true）76 条，已用 75（h15 20＋h16 20＋h17 20＋h18 15，CENSUS 逐 id 断言合规集＝已用集），未用仅 **ZC-122**：该例经 R39/R40/R41/R48 一贯裁处为**身份未定旗标排除**（grade_note 载「相哥」身份未定、可径降 A-high），不入合规——单独登记（§四同型），**eligible 未用＝0**。
- 同 judged-set 内春渚旧池 CZ 33 条：eligible＝true 者 0——eligible 未用 0。

### 3.4 expansion–expansion12 池层（早期池扩容件）

下表为各池目录内全部 jsonl 之 id 并集的逐 id 对勘（池内含 work/ 索引件，故总数为池层 id 总量、非台账条目数）：

| 池 | id 总数 | 已用命中 | 未用 id 数 |
|---|---|---|---|
| expansion | 94 | 92 | 2 |
| expansion2 | 84 | 84 | 0 |
| expansion3 | 43 | 43 | 0 |
| expansion4 | 29 | 29 | 0 |
| expansion5 | 1 | 1 | 0 |
| expansion6 | 106 | 91 | 15 |
| expansion7 | 78 | 78 | 0 |
| expansion8 | 111 | 80 | 31 |
| expansion9 | 27 | 24 | 3 |
| expansion10 | 22 | 22 | 0 |
| expansion11 | 803 | 623 | 180 |
| expansion12 | 619 | 159 | 460 |

未用 id 较小集逐列（expansion11/expansion12 两池未用数大，逐 id 全列存于复算 JSON `old_faces.expansion_pools`，本件只登计数）：
- expansion 未用 2：LY-302、LY-303
- expansion6 未用 15：MP-020、MP-021、MP-022、OC-031、OC-032、OC-033、OC-034、OC-035、OC-036、OC-037、OC-038、OC-039、WP-014、WP-015、WP-016
- expansion8 未用 31：MT-001、MT-002、MT-003、MT-004、MT-005、MT-006、MT-007、MT-008、MT-009、MT-010、MT-011、MT-012、MT-013、MT-014、MT-015、MT-016、MT-017、MT-018、MT-019、MT-020、MT-021、MT-022、MT-023、MT-024、MT-025、MT-026、MT-027、MT-028、MT-029、MT-030、MT-031
- expansion9 未用 3：LR3-103、LR3-106、LR3-108
- expansion11 未用 180、expansion12 未用 460（逐 id 见复算 JSON）。

定性：该池层为例卡成卡前之候选/索引层，其逐例资格（A 级/low/锚点在场 adjudication）从未按 holdout 供给口径全量落台账；历轮 SUPPLY-ACCOUNTING 链之可选库存从未含此池层未用 id。按本轮资格口径（须台账资格字段齐备且锚点在场经 adjudication）**可计 eligible 未用＝0**；逐例资格**未核**——本席只登记此计数口径，不下「净新／枯竭」结论。

## 四、单独登记（不计 eligible）

1. **ZCB-003**（《字触补》台账，资格全过、未入已用并集）：input_side 拆分锚点原文末句含结论句，经 holdout22 主持裁处判为断语/结局事实入卡并换例剔除；本轮承 PREREG §4，裁处未撤销、维持排除。可选计数中剔除，ZCB 可选 eligible 未用因此为 0（合格存量 15－已用 14－本件 1）。
2. **ZC-122**（旧测字池）：A/low/eligible 形态，但身份未定旗标排除自 R39 起一贯在案（见 §3.3），不计 eligible。
3. **GSZ 五要素不过 6 例**（GSZ-020、GSZ-080、GSZ-082、GSZ-089、GSZ-094、GSZ-111）：台账净资格在册，但建卡口径五要素复核动爻缺如；组集阶段如拟动用须另经主持裁处，本阶段只登记、不计建卡口径 eligible。
4. **WHY 去重 8 例**（WHY-076/077/094/097/101/105/113/116）：与 GSZ 同案、归属说真席，只登记异文，不入 WHY 资格集（§一.8 顺序漏斗中分别于 grade 级剔除 4 例——WHY-076/094/113/116，其台账 grade 为 B；eligible_net 级剔除 4 例——WHY-077/097/101/105）。
5. 在途未到面（紫微两本、梅花两条、《奇门遁甲解真》正本、《盲师断命轶例集之壹》等）：未到不入选、不计存量，只登记（承 PREREG §8）。

## 五、组集限度可达性——纯计数核算（只算数、不下构成结论、不挑例）

基数：建卡口径 eligible 未用 **142**（八字 32／奇门 21／六爻 89／测字 0）；旧面 eligible 未用 0（§三）；合计 142。

以 T＝25 试算各限度所需与现有之计数关系（限度：T≥25、单体系 ≤50%、单源 ≤50%、非夷坚 ≥13、非六爻 ≥13）：

| 限度项 | T＝25 时的计数要求 | 现有存量计数 | 差额（要求－现有，负为余量） |
|---|---|---|---|
| 总量 T≥25 | ≥25 | 142 | -117 |
| 非六爻 ≥13 | ≥13 | 53（八字 32＋奇门 21） | -40 |
| 非夷坚 ≥13 | ≥13 | 142（主台账诸源皆非夷坚；夷坚面 eligible 未用 0） | -129 |
| 单体系 ≤50% | 任一体系 ≤12（12/25＝48%；13/25＝52% 超限） | 体系存量：六爻 89、八字 32、奇门 21——组集时每体系至多取 12，三体系上限合计 36 ≥25 | —（上限侧核算） |
| 单源 ≤50% | 任一单源 ≤12 | 逐源存量：DS 32、WHY 两轮同书合计 65（一轮 35＋二轮 30）、GSZ（建卡口径）24、开悟 18、启悟 2、QM 旧池 1、石建国 0——组集时每源至多取 12 | —（上限侧核算） |

计数事实（仅算术）：以 T＝25 计，非六爻须 ≥13 且六爻至多 12；现有非六爻存量 53、六爻存量 89，两项计数均不小于各自所需下限/上限配合量（非六爻 53≥13、且可供六爻取用上限 12≤89）。逐源上限 12 之下，存量 ≥12 之源有：DS（32）、WHY 同书（65）、GSZ（24）、开悟（18），共 4 源。本节止于计数核算：构成表、选例规则与递补链由主持增补件写定，本席不下构成结论、不挑例。

## 六、产出与卫生登记

- 复算脚本：`runs/round81/recount_stock_r81.py`；复算结果 JSON：`runs/round81/recount_stock_r81_out.json`；探查脚本：`runs/round81/probe_ledgers_r81.py`；本件由 `runs/round81/render_recount_r81.py` 直读复算 JSON 渲染，数字与 id 未经手工转录。
- 本阶段未建卡、未封存、未作断、未评分、未做 git 操作；未打开任何 runs/ 下 predictions/judging/final-scores（已用并集仅取各集金标 id 字段与 inputs 卡文件名，未读金标正文）。
- 全体系普查完整性：§三各面均已逐件跑完并逐名定性；唯一「未核」登记为 §3.4 expansion 池层逐例资格（已逐 id 对勘、未逐例 adjudication），照口径登记、不下净新/枯竭结论。
