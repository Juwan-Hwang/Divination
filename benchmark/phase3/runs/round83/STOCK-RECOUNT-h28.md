# STOCK-RECOUNT-h28 —— holdout28 供给存量盘上全口径复算（R83 组集席开工复算）

本件为 R83 组集封存席开工复算产出：只复算登记，不改构成。复算脚本 `runs/round83/recount_stock_h28_r83.py`（唯一名，盘上实算），中间结果 `runs/round83/recount_stock_h28_r83_out.json`；本件由 `runs/round83/render_recount_h28_r83.py` 直读复算 JSON 渲染，数字与 id 未经手工转录。台账/结局文本一律按数据处理。

## 口径（写定依据）

- 依据：`runs/round83/PREREG.md` §4（并集与资格口径写定）、`runs/round83/PREREG-ADDENDUM-r83.md`（holdout28 构成写定）与 `runs/round82/STOCK-RECOUNT-h27.md`（复算方法承接）。
- 已用并集：盘上逐 id 实算 **1139**（dev 488＋phase2 splits2 holdout2 29＋holdout3–27 金标 id 727＋holdout inputs 卡 id 568＋顶层 inputs6–10 卡 id 412，五源并集去重；与主持开轮实算 1139 一致，复算脚本内断言 1139 通过）。零复用＝台账 id 与该并集逐 id 零命中；**同名即剔**。金标文件只按 id 字段计并集，未读金标正文。
- 资格口径（eligible）：A 级、污染 low、锚点在场（六爻面五要素：卦名、动爻、世应、六亲纳支、月建日辰，六神不属要件；他体系以各台账 anchor 字段口径）、未用、四滤（逐字原文、独立结局、可分离、非 high 污染）。各台账资格字段读法以历轮构建脚本为准，无 eligible_net/grade 字段之台账按构建脚本实际采用的字段组合判定，逐件注记。
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

- 资格全过（qualified）：62；其中已用（与已用并集逐 id 命中）：48——DS-001、DS-002、DS-003、DS-004、DS-005、DS-006、DS-007、DS-008、DS-009、DS-010、DS-011、DS-012、DS-013、DS-014、DS-015、DS-016、DS-017、DS-018、DS-019、DS-020、DS-021、DS-022、DS-023、DS-024、DS-025、DS-026、DS-027、DS-028、DS-029、DS-030、DS-031、DS-032、DS-033、DS-034、DS-035、DS-036、DS-037、DS-038、DS-039、DS-040、DS-041、DS-042、DS-043、DS-044、DS-045、DS-046、DS-048、DS-049。
- **eligible 未用：14**——DS-050、DS-051、DS-052、DS-053、DS-054、DS-055、DS-056、DS-057、DS-058、DS-059、DS-060、DS-061、DS-062、DS-063。

注记：DS-047 contamination medium 于 low 级淘汰，与历轮一致。已用较 h27 复算增 9（holdout27 取 DS-040–046、048、049），未用由 23 降至 14。
### 2. 张志春《开悟之门》QM 开悟（r76）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round76/digestion/SUPPLY-MINING-kaiwu-r76.json`；体系：qimen（奇门）；台账总例数：**52**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present | 0 | （无） | 52 |
| contamination low | 0 | （无） | 52 |
| separable=true | 0 | （无） | 52 |
| stem_check天地盘双ok | 14 | QM-017、QM-026、QM-033、QM-041、QM-050、QM-051、QM-053、QM-054、QM-056、QM-057、QM-059、QM-060、QM-061、QM-062 | 38 |
| 断语/结局非空 | 0 | （无） | 38 |

- 资格全过（qualified）：38；其中已用（与已用并集逐 id 命中）：38——QM-011、QM-012、QM-013、QM-014、QM-015、QM-016、QM-018、QM-019、QM-020、QM-021、QM-022、QM-023、QM-024、QM-025、QM-027、QM-028、QM-029、QM-030、QM-031、QM-032、QM-034、QM-035、QM-036、QM-037、QM-038、QM-039、QM-040、QM-042、QM-043、QM-044、QM-045、QM-046、QM-047、QM-048、QM-049、QM-052、QM-055、QM-058。
- **eligible 未用：0**——（无）。

注记：本台账无 grade/eligible_net/filters 字段，资格读法承构建脚本：present∧low∧separable∧stem_check 天地盘双 ok（全合）∧断语/结局非空。未用较 h27 复算减 9（holdout27 取全 9 例），**未用归 0**。
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

注记：资格读法承构建脚本：present∧low∧separable∧断语/结局非空（本台账无 stem_check/grade/eligible_net 字段）。未用 2 例与 h27 复算一致。
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

注记：资格读法同启悟。11 例已全部用尽，未用 0，与 h27 复算一致。
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
- **eligible 未用：1**——ZCB-003。

注记：资格全过 15－已用 14＝未用 1 例，即 ZCB-003；ZCB-003 经主持裁处维持排除（§四单独登记），**可选 eligible 未用＝0**，与历轮复算一致。
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

- 资格全过（qualified）：63；其中已用：43——GSZ-003、GSZ-005、GSZ-009、GSZ-015、GSZ-016、GSZ-017、GSZ-022、GSZ-023、GSZ-024、GSZ-026、GSZ-028、GSZ-030、GSZ-031、GSZ-032、GSZ-033、GSZ-034、GSZ-038、GSZ-041、GSZ-042、GSZ-043、GSZ-046、GSZ-047、GSZ-049、GSZ-050、GSZ-052、GSZ-053、GSZ-054、GSZ-055、GSZ-058、GSZ-059、GSZ-060、GSZ-061、GSZ-068、GSZ-069、GSZ-074、GSZ-075、GSZ-077、GSZ-078、GSZ-079、GSZ-081、GSZ-084、GSZ-086、GSZ-088。
- **eligible 未用（台账净资格口径）：20**——GSZ-020、GSZ-080、GSZ-082、GSZ-089、GSZ-091、GSZ-092、GSZ-093、GSZ-094、GSZ-098、GSZ-099、GSZ-100、GSZ-101、GSZ-103、GSZ-104、GSZ-105、GSZ-107、GSZ-108、GSZ-109、GSZ-110、GSZ-111。
- 注记：资格全过集与台账 counts.net_eligible_A_low_present 名单逐 id 相等（复算脚本断言通过）。建卡口径五要素复核（逐例回原书文字层 `runs/round76/gsz-book-r76.txt` 以构建脚本同一 five_elements 函数复核）：未用 20 例中五要素全在场 **14** 例——GSZ-091、GSZ-092、GSZ-093、GSZ-098、GSZ-099、GSZ-100、GSZ-101、GSZ-103、GSZ-104、GSZ-105、GSZ-107、GSZ-108、GSZ-109、GSZ-110；五要素不过 **6** 例——GSZ-020、GSZ-080、GSZ-082、GSZ-089、GSZ-094、GSZ-111，均仅「动爻」一要素缺如（静卦、变卦空，逐例 elements 明细在复算 JSON）。故 GSZ 按台账净资格未用 20、按建卡口径 eligible 未用 14，两数并列登记。已用较 h27 复算增 5（holdout27 取 GSZ-079、081、084、086、088），建卡口径未用由 19 降至 14。
### 7. 王虎应《六爻分类占验技法》一轮 WHY-001–071（r56）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json`；体系：liuyao（六爻）；台账总例数：**71**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| anchor present | 19 | WHY-001、WHY-002、WHY-029、WHY-050、WHY-051、WHY-053、WHY-054、WHY-055、WHY-056、WHY-057、WHY-058、WHY-059、WHY-060、WHY-061、WHY-062、WHY-063、WHY-064、WHY-065、WHY-066 | 52 |
| pollution low | 12 | WHY-013、WHY-014、WHY-017、WHY-018、WHY-019、WHY-020、WHY-045、WHY-046、WHY-047、WHY-048、WHY-049、WHY-052 | 40 |
| counts净入账名单成员 | 0 | （无） | 40 |

- 资格全过（qualified）：40；其中已用（与已用并集逐 id 命中）：13——WHY-003、WHY-004、WHY-005、WHY-006、WHY-007、WHY-008、WHY-009、WHY-010、WHY-011、WHY-015、WHY-021、WHY-030、WHY-067。
- **eligible 未用：27**——WHY-012、WHY-016、WHY-022、WHY-023、WHY-024、WHY-025、WHY-026、WHY-027、WHY-028、WHY-031、WHY-032、WHY-033、WHY-034、WHY-035、WHY-036、WHY-037、WHY-038、WHY-039、WHY-040、WHY-041、WHY-042、WHY-043、WHY-044、WHY-068、WHY-069、WHY-070、WHY-071。

注记：本台账 entries 无 grade/filters/eligible_net 字段，净入账以台账 counts.net_eligible_A_low_present 名单（40）为准；漏斗以 anchor_presence∧pollution∧名单成员三级复算，资格全过集与名单逐 id 相等（断言通过）。已用较 h27 复算增 4（holdout27 取 WHY-008–011），未用由 31 降至 27。
### 8. 王虎应《六爻分类占验技法》二轮 WHY-072–117（r57-r2）

- 台账路径：`/home/hatch/workspace/divination/benchmark/phase3/runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json`；体系：liuyao（六爻）；台账总例数：**46**。

| 滤级（顺序漏斗） | 淘汰数 | 淘汰 id | 余 |
|---|---|---|---|
| grade A | 5 | WHY-076、WHY-094、WHY-113、WHY-116、WHY-117 | 41 |
| pollution low | 0 | （无） | 41 |
| anchor present | 1 | WHY-102 | 40 |
| eligible_net=true | 4 | WHY-077、WHY-097、WHY-101、WHY-105 | 36 |
| 四滤全true | 0 | （无） | 36 |
| 断语/结局非空(字段口径见注) | 0 | （无） | 36 |

- 资格全过（qualified）：36；其中已用（与已用并集逐 id 命中）：6——WHY-072、WHY-073、WHY-074、WHY-075、WHY-078、WHY-079。
- **eligible 未用：30**——WHY-080、WHY-081、WHY-082、WHY-083、WHY-084、WHY-085、WHY-086、WHY-087、WHY-088、WHY-089、WHY-090、WHY-091、WHY-092、WHY-093、WHY-095、WHY-096、WHY-098、WHY-099、WHY-100、WHY-103、WHY-104、WHY-106、WHY-107、WHY-108、WHY-109、WHY-110、WHY-111、WHY-112、WHY-114、WHY-115。

注记：资格全过数与台账 counts.net_eligible_A_low_present（36）相等（断言通过）。未用 30 与 h27 复算一致。台账另有 registered_only 2 件不在 entries 46 内、不入账。
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

注记：本台账无 grade/eligible_net 字段，资格读法：anchor present∧pollution low∧四滤全 pass∧结局非空，present 集 17 例已全部用尽，未用 0。partial 17 例（QW-018–034）经 SUPPLY-RECHECK-qwpartial-r57 复核升格 0、维持 partial，不入资格集。
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

注记：4 例锚点皆 partial，资格 0、可选增量 0，与台账 count 口径一致。
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

注记：资格承 QM-REVIEW-r58 复核（`runs/round58/digestion/QM-REVIEW-r58.json`）：eligible_optional 9 例（QM-001–008、QM-010），QM-009 pollution＝mid 只建池不入可选。已用 8（holdout21），未用 1＝QM-010，与 h27 复算一致。
## 二、主台账汇总（逐体系）

| 体系 | eligible 未用（台账净资格口径） | eligible 未用（建卡口径，GSZ 过五要素复核） | 构成 id |
|---|---|---|---|
| bazi（八字） | 14 | 14 | DS 14＋QW 0 |
| qimen（奇门） | 3 | 3 | 开悟 0＋启悟 2＋石建国 0＋旧池 1 |
| liuyao（六爻） | 77 | 71 | GSZ 20（建卡口径 14）＋WHY 一轮 27＋WHY 二轮 30 |
| cezi（测字） | 0 | 0 | ZCB 可选 0（ZCB-003 裁处排除，§四） |
| **合计** | **94** | **88** | |

以下 §五可达性核算以建卡口径 88 为基数（GSZ 五要素不过 6 例单列、不入基数）。非六爻 eligible 未用 **17**（DS 14＋QM 3），与 PREREG §4 写定口径（非六爻 17＝DS 14＋QM 3）逐项一致。

## 三、全体系口径普查——旧面台账（承 h27 复算 §三，逐面状态不变登记）

- supply-ledger r46–r50 诸面、cards-mining r46–r53 诸面、旧测字池 ZC/CZ：eligible 未用＝0（逐面定性承 `runs/round82/STOCK-RECOUNT-h27.md` §三全量复算登记；holdout27 取用例为 DS/开悟/GSZ/WHY 四源，未触旧面任何 id，本轮复算的已用并集 1139 与资格漏斗结果与该定性相容，本席未重复逐面重开）。
- expansion–expansion12 池层未用 id 共 691（承 h27 复算 §3.4），逐例资格从未按 holdout 供给口径全量落台账，按现行口径可计 eligible 未用＝0、状态**未核**；PREREG §5 已裁决自 R84 起开设逐例资格核查工序，本轮不抢跑核查、不计入存量。

## 四、单独登记（不计 eligible）

1. **ZCB-003**（《字触补》台账，资格全过、未入已用并集）：经 holdout22 主持裁处维持排除，裁处未撤销。可选计数中剔除，ZCB 可选 eligible 未用因此为 0。
2. **ZC-122**（旧测字池）：身份未定旗标排除自 R39 起一贯在案，不计 eligible（承 h27 复算 §四）。
3. **GSZ 五要素不过 6 例**（GSZ-020、GSZ-080、GSZ-082、GSZ-089、GSZ-094、GSZ-111）：台账净资格在册，但建卡口径五要素复核动爻缺如；只登记、不计建卡口径 eligible。
4. **WHY 去重 8 例**（WHY-076/077/094/097/101/105/113/116）：与 GSZ 同案、归属说真席，只登记异文，不入 WHY 资格集。
5. 在途未到面（紫微两本、梅花两条、《奇门遁甲解真》正本、《盲师断命轶例集之壹》等）：未到不入选、不计存量，只登记。

## 五、holdout28 组集可行性核算与增补件构成对勘（限度：T≥25、单体系 ≤50%、单源 ≤50%、非夷坚 ≥13、非六爻 ≥13）

基数：建卡口径 eligible 未用 **88**（八字 14／奇门 3／六爻 71／测字 0）；非六爻存量 17；旧面 eligible 未用 0（§三）。

**增补件写定构成对勘（PREREG-ADDENDUM-r83 §一，T＝27）**：DS 13（DS-050–062）⊆ DS 未用 14 例（DS-050–063）✓；QM 启悟 2（QM-210、QM-211）＝启悟未用全集 ✓；QM 旧池 1（QM-010）＝旧池未用全集 ✓；GSZ 6（GSZ-091、092、093、098、099、100）⊆ GSZ 建卡口径未用 14 例 ✓；WHY 5（WHY-012、016、022、023、024）⊆ WHY 一轮未用 27 例 ✓。写定 27 id 与已用并集 1139 逐 id 对勘（复算脚本资格集与并集关系）零命中预期由构建脚本再断言。**复算与增补件构成写定逐项相合，无不合项，不提请改构成。**

限度逐项（按写定构成）：T＝27 ≥25 ✓；单体系最大 bazi 13/27＝48.1% ≤50% ✓；单源最大 DS 13/27＝48.1% ≤50% ✓；非夷坚 27 ≥13 ✓；非六爻 16 ≥13 ✓；仅锚点在场（构建脚本资格断言）✓。

**取用后余量（按写定构成实算）**：DS 1（DS-063）／QM 0／GSZ 建卡口径 8／WHY 52（一轮 22＋二轮 30）／非六爻合计 1／六爻建卡口径余 60／总余 61。非六爻余 1＜13——**holdout28 为存量内最后一集**（承 PREREG §4 存量见底定案），其后组集系于 §5 expansion 工序产出或待用户书目。

## 六、对照登记——holdout27 封存后口径 vs 本席复算（逐面）

holdout27 封存日志 §一.1 取用后余量口径：DS 14／QM 3（启悟 2＋旧池 1，开悟 0）／GSZ 建卡口径 14／WHY 57／非六爻 17／合计（建卡口径）88。

| 面 | h27 封存后口径 | 本席复算（建卡口径） | 差异 |
|---|---|---|---|
| DS 段氏 | 14 | 14 | 0 |
| QM 开悟 | 0 | 0 | 0 |
| QM 启悟 | 2 | 2 | 0 |
| QM 石建国 | 0 | 0 | 0 |
| QM 旧池 | 1 | 1 | 0 |
| 奇门小计 | 3 | 3 | 0 |
| GSZ（建卡口径） | 14 | 14 | 0 |
| WHY 一轮 | 27 | 27 | 0 |
| WHY 二轮 | 30 | 30 | 0 |
| 六爻小计（建卡口径） | 71 | 71 | 0 |
| 测字 ZCB 可选 | 0 | 0 | 0 |
| 旧面（§三诸面） | 0 | 0 | 0 |
| **合计（建卡口径）** | **88** | **88** | **0** |

出入原因（只登记事实）：逐面差异全为 0，无出入项。存量自 h27 复算建卡口径 115 降至 88，减少 27，恰为 holdout27 实成 27 例逐 id 命中已用并集所致。

## 七、产出与卫生登记

- 复算脚本：`runs/round83/recount_stock_h28_r83.py`；复算结果 JSON：`runs/round83/recount_stock_h28_r83_out.json`；本件由 `runs/round83/render_recount_h28_r83.py` 直读复算 JSON 渲染。
- 本席本件工序未建卡、未组集、未封存、未作断、未评分、未做 git 操作；未打开任何 holdout 的 test_gold.jsonl 正文（已用并集仅取各集金标 id 字段与 inputs 卡文件名）；未打开任何 predictions/judging/final-scores。
- 隔离自报：无。复算脚本按 PREREG §4 写定口径对 phase3 非 runs 目录（inputs-dev*/inputs/inputs6–10 与各 holdout inputs 目录）枚举文件名计并集，承历轮构建/复算脚本同口径，非目录列表式探查；本席未对任何 runs/ 目录执行列表/计数操作。
