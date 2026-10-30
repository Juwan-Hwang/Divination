# holdout13 BUILD-LOG — 组建日志（R35 数据角，2026-10-30）

组建脚本：`runs/round35/build_holdout13_r35.py`（唯一名，盘上验收）；审计脚本：`runs/round35/audit_ids_holdout13_r35.py`＋`runs/round35/audit-ids-holdout13-report.json`；组建事实：`runs/round35/build_holdout13_facts_r35.json`。本轮未作断、未评分、未 git 提交。

## 一、储备账核对（盘上逐行解析实测，与任务单/STAGE-SUMMARY-17 §一逐项合）

| 源 | 文件 | 盘上实数 | 可封存口径 | 实测 |
|---|---|---|---|---|
| 断案 DA | expansion12/liuren-duanan/cases-a.jsonl（92）＋cases-b.jsonl（75） | 167 | holdout_eligible=true | **162** ✔ |
| 辨疑/预测学 BY/YX | expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl（126） | 126 | review.verdict=seal（REVIEW-G） | **111**（BY 108＋YX 3）✔ |
| 粹言 CY/CYJ | expansion12/liuren-cuiyan/cases-munong.jsonl（61）＋cases-juan5.jsonl（75） | 136 | holdout_eligible=true | **119**（56＋63）✔ |
| 千里命稿 QL | expansion12/natal-batch2/cases-reviewed.jsonl（92） | 92 | review.verdict=seal（REVIEW-H，全 QL） | **18** ✔ |
| NL | expansion12/natal-leftovers/cases.jsonl（55） | 55 | GRADE-ADDENDUM 改判 A-low 6＋NL-049 | **7** ✔ |
| 测字 CZ | expansion12/online-routes/cases.jsonl | 33 | HOST-RULINGS-3 资格生效（全 33；源文件 holdout_eligible=false 系抽例时点状态、不作过滤，同 holdout12 续建口径） | **33** ✔ |
| 六爻 HZ | expansion12/huangjince-huozhulin/cases.jsonl | 1 | holdout_eligible=true | 1（HZ-001，holdout12 已用）→ 余 **0** |

## 二、排除清单（入封前扣除，脚本硬断言）

- holdout12 已用 49 例：DA-001、DA-028、DA-049、DA-069、DA-089、DA-111、DA-143、DA-166、DA-193、BY-001、BY-013、BY-026、BY-040、BY-052、BY-065、BY-082、BY-095、BY-108、CY-001、CY-015、CY-028、CY-041、CY-057、CYJ-011、CYJ-024、CYJ-037、CYJ-051、QL-001…QL-008、NL-001、NL-002、NL-005、NL-031、NL-043、CZ-001、CZ-005、CZ-009、CZ-013、CZ-017、CZ-021、CZ-025、CZ-029、HZ-001。
- dev9 全部 487 例：以 benchmark/phase3/inputs-dev11/ 文件名集为准，入选 id 与之零交集（脚本断言＋审计复核）。
- 历次 holdout 已用 id：holdout3–holdout12 各 test_gold.jsonl 的 id 集（仅取 id 字段）并入排除集；入选 id 零命中。
- expansion12/POOL-IDS.txt 488 个 id 并入排除集；入选 id 零命中。

## 三、构成与配额推导

硬约束：总量 ≥40；单一来源 ≤50%；单体系 ≤40%；粹言干支级 ≤全集 20%；八字供给上限＝QL 余 10＋NL 余 2＝12（封顶，无更多合格八字例）；测字参考 10–12；六壬参考 16–17。取总量 40：六壬 16（40.0%，恰合 ≤40% 上限）、八字 12（30.0%）、测字 12（30.0%）、六爻 0。若六壬取 17 则总量须 ≥43、测字须扩至 14（超参考上限），故取 16。六壬内部：断案 8（全课式）＋辨疑 5（全课式）＋粹言 3（干支级，≤8 且占全集 7.5%≤20%）。

## 四、六爻有界普查（结论：实得 0）

- 范围：① expansion12 全目录 jsonl 清点——六爻 cases 文件仅 huangjince-huozhulin/cases.jsonl（1 例 HZ-001，holdout12 已用）；expansion12/yuangui 仅 METHOD-EXTRACTION.md（《卜筮元龟》卷上成例确数 0，全卷假令与通则，未抽例）。② 已知六爻源逐文件核（脚本计：tradition∈{liuyao,六爻,筮占}、outcome_grade 以 A 开头、contamination=low、且 id 不在 dev9∪历次 holdout 分配集者）：expansion3（LY 43）、expansion4（LY 29）、expansion5（LY-701）、expansion7/bushi-quanshu（BQ 25）、expansion7/yiyin（YY 24）、expansion7/yiyin2（YY2 5）、expansion8/duanyi-tianji（DS 7）、expansion8/yimao（YM 70）、expansion10/yilin-buyi（YB 13）、expansion10/yilin-buyi-zongduan（YB 9）、expansion11/bushi-zhengzong（ZG 3）——各文件未分配的新鲜 A/low 例数均为 **0**（全部已入 dev9 或历次 holdout）。
- 结论：六爻现账封存合格余量 **0**，本集六爻缺位如实登记，不以已用例、降级例或他体系例冒充。

## 五、选取规则与入选清单

规则（防挑题，写死）：每源在合格集内**按源文件既有顺序**依次取例，跳过 §二排除 id，取足配额即止；不看结局、不看预期分数、不作任何替换。

| 源 | 配额 | 入选（按选取序＝文件序） |
|---|---|---|
| DA | 8 | DA-002、DA-004、DA-005、DA-008、DA-010、DA-011、DA-012、DA-013 |
| BY | 5 | BY-002、BY-003、BY-004、BY-005、BY-006 |
| CY（慕农） | 3 | CY-002、CY-003、CY-004 |
| QL | 10 | QL-013、QL-014、QL-023、QL-025、QL-026、QL-027、QL-030、QL-031、QL-032、QL-035（seal 18 扣除已用 8 后的全部余量） |
| NL | 2 | NL-006、NL-049（可封存 7 扣除已用 5 后的全部余量） |
| CZ | 12 | CZ-002、CZ-003、CZ-004、CZ-006、CZ-007、CZ-008、CZ-010、CZ-011、CZ-012、CZ-014、CZ-015、CZ-016 |

替换登记：无替换。

## 六、封存前全树编号唯一性审计（结果与处置）

`audit_ids_holdout13_r35.py` 扫 benchmark/ 下 4302 个 json/jsonl 文件（排除 runs/ 与 holdout13 自身产出），只查 id 出现位置，不取结局作任何判定。结果：40 例入选 id 无一命中 inputs-dev11 文件名集、POOL-IDS、data/splits10/11 清单或任何其他 holdout 金标。15 例有「源文件外出现」标记，逐一处置如下（均为同源孪生、非冲突）：

- BY-002…006（5）：另一出现为 liuren-bianyi-yuce/cases.jsonl——即 cases-reviewed.jsonl 的复核前原件（REVIEW-G 明载：原记录全字段逐字未动＋review 字段），同一例。
- QL-013、QL-014、QL-023、QL-025、QL-026、QL-027、QL-030、QL-031、QL-032、QL-035（10）：另一出现为 natal-batch2/cases.jsonl——改号后原件；与 cases-reviewed 对应行逐字段比对（subject/question_or_topic/chart 及全部共有字段）零差异，同一例。
- 其余 25 例仅出现于各自唯一源文件。

另：三键（对象＋占时＋事项，归一化去空白）核对——入选 40 例两两 0 撞、与 holdout12 49 例三键 0 撞（脚本断言通过）。

## 七、构成验算表

| 维度 | 例数 | 占比 | 口径 | 判定 |
|---|---|---|---|---|
| 总量 | 40 | — | ≥40 | ✔ |
| 来源 DA《大六壬断案》 | 8 | 20.0% | 单源 ≤50% | ✔ |
| 来源 BY《六壬辨疑》 | 5 | 12.5% | 同上 | ✔ |
| 来源 CY《六壬粹言》卷六 | 3 | 7.5% | 同上 | ✔ |
| 来源 QL《千里命稿》 | 10 | 25.0% | 同上 | ✔ |
| 来源 NL《呱呱集/子平真诠评注》 | 2 | 5.0% | 同上 | ✔ |
| 来源 CZ《测字秘牒》 | 12 | 30.0% | 同上（最大单源） | ✔ |
| 体系 六壬 | 16 | 40.0% | 单体系 ≤40% | ✔（恰在上限） |
| 体系 八字 | 12 | 30.0% | 同上 | ✔ |
| 体系 测字 | 12 | 30.0% | 同上 | ✔ |
| 体系 六爻 | 0 | 0% | 实得为准 | 缺位登记（§四） |
| 粹言干支级课式例 | 3 | 7.5% | ≤20% | ✔ |
| 六壬全课式原文直载 | 13/16 | — | 断案/辨疑优先 | ✔ |
| 等级 A／A-low | 19／21 | — | 全例 A/A-low | ✔ |
| 污染 low | 40 | 100% | 全 low | ✔ |

## 八、逐例入封四项核验（①新鲜 ②A 级双全可分离 ③低污染 ④断语＋结局俱全）

准据：BY/QL 以 review 的 grade_final／contamination_final／verdict 为准；NL-006 以 GRADE-ADDENDUM 改判为准、NL-049 以源行 A 级＋addendum 确认为准；DA/CY/CZ 以源行 outcome_grade／contamination 为准（CZ 资格另据 HOST-RULINGS-3）。①由各源复核的去重结论＋§六审计＋三键核对共同成立；④由脚本逐例断言（master_predictions 首条 statement_excerpt 非空、outcome.description 非空）全数通过。

| id | 源 | 等级（准据） | 污染 | ① | ② | ③ | ④ |
|---|---|---|---|---|---|---|---|
| DA-002 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-004 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-005 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-008 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-010 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-011 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-012 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| DA-013 | 断案 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| BY-002 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| BY-003 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| BY-004 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| BY-005 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| BY-006 | 辨疑 | A-low（grade_final） | low | ✔ | ✔ | ✔ | ✔ |
| CY-002 | 粹言 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CY-003 | 粹言 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CY-004 | 粹言 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| QL-013 | 千里命稿 | A（grade_final，A-low 口径保 A） | low | ✔ | ✔ | ✔ | ✔ |
| QL-014 | 千里命稿 | A（同上） | low | ✔ | ✔ | ✔ | ✔ |
| QL-023 | 千里命稿 | A（同上） | low | ✔ | ✔ | ✔ | ✔ |
| QL-025 | 千里命稿 | A（同上） | low | ✔ | ✔ | ✔ | ✔ |
| QL-026 | 千里命稿 | A（同上） | low | ✔ | ✔ | ✔ | ✔ |
| QL-027 | 千里命稿 | A（同上） | low | ✔ | ✔ | ✔ | ✔ |
| QL-030 | 千里命稿 | A（同上） | low | ✔ | ✔ | ✔ | ✔ |
| QL-031 | 千里命稿 | A（同上） | low | ✔ | ✔ | ✔ | ✔ |
| QL-032 | 千里命稿 | A（同上；结局主体为命主之妻，REVIEW-H 已注记） | low | ✔ | ✔ | ✔ | ✔ |
| QL-035 | 千里命稿 | A（同上） | low | ✔ | ✔ | ✔ | ✔ |
| NL-006 | NL | A-low（GRADE-ADDENDUM 改判；金标行 grade 字段照源保留 B） | low | ✔ | ✔ | ✔ | ✔ |
| NL-049 | NL | A（addendum 确认资格不变） | low | ✔ | ✔ | ✔ | ✔ |
| CZ-002 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-003 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-004 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-006 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-007 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-008 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-010 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-011 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-012 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-014 | 测字 | A-low | low | ✔ | ✔ | ✔ | ✔ |
| CZ-015 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |
| CZ-016 | 测字 | A | low | ✔ | ✔ | ✔ | ✔ |

## 九、逐例课式 fidelity（六壬 16 例）

- DA 8 例：原文直载——课盘原文与三传自 liuren-duanan/scratch-archive/cases_raw.json 对应案号原文直录（案002/004/005/008/010/011/012/013；评注续行已滤除、只留盘列，◎⊙旬空标记保留于课盘原文）。DA-008 中传干支原盘仅作单支「申」，三传串照录「兄申（蛇）」。
- BY 5 例：原文直载——课式标题/三传/四课/天地盘自《六壬辨疑》排印本 PDF 页图逐字直录（数据角 2026-10-30 视觉转录，200dpi 渲染、疑字 400dpi 放大核读）：BY-002＝课例二（PDF p163）、BY-003＝课例四（p164）、BY-004＝课例六（p165）、BY-005＝课例七（p165）、BY-006＝课例八（p166）。排印本玄武省作「元」：三传天将按全称记、四课与天地盘天将行照原字（照 holdout12 BY 体例）。BY-003 天地盘末行第三字经放大核读为「无」（排印本原字），照原字录入、不改作「元」。
- CY 3 例：仅干支（复原不能）——原书有课盘列但转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录干支/月将/占时，例头月将已含于 asked_at。

## 十、逐例输入卫生处置（剥离登记）

建卡一律白名单字段组装：grade_note／review／contamination 类字段不入卡（40 卡禁键扫描零命中，脚本断言）。

- DA 8 例：context_at_prediction 原文为空，未填；课盘自 cases_raw 直录（见 §九）。
- BY 5 例：context_at_prediction 原文为空，未填；课式自页图直录（见 §九）。
- CY 3 例：context_at_prediction 原文为空，未填；干支级建卡、note 明示不臆录。
- QL 10 例：context_at_prediction 原文为空，未填；四柱/性别自源行 chart 入 attachments。QL-030：subject 与 question 中的后事身份词「中储蓄会头奖者」已删、改「某女（佚名）」（照 holdout12 QL-006 先例；金标不动）。asked_at 通用回顾框架语（全批一致、无本例结局）保留原文。
- NL 2 例：四柱自 question_or_topic 括注提取入 attachments；性别据 subject 明示记男（NL-006「李弘毅之弟」、NL-049「李鸿章长孙」）。NL-049 的 context_at_prediction 为徐氏凡例体例说明（无本例结局），原样用作 setting。
- CZ 12 例：沿原 context 建卡；attachments 原 method_hint 为大师拆字取象理据（断语侧信息），已剔除、仅留所测字；setting/question/asked_at 为占时信息，原文保留。

## 十一、产出（盘上实数）

- 金标 benchmark/phase3/holdout13/test_gold.jsonl：40 行，与各源文件原行逐字一致（脚本比对 0 不符；QL 无 source_id，理由见 SEALED 注记），SHA-256 `75c5349d6184d5cace454dadb790433eabac731f38884b889cd1f9bd67aab483`。
- 输入卡 benchmark/phase3/holdout13-inputs/：40 个 JSON，逐一解析合法。
- 登记：benchmark/phase3/holdout13/SEALED.md、data/holdout13-seal-log.md、data/splits12.json（dev9 487＋holdout13 40）。
- 缺口登记：六爻 0 例（§四）；八字已用尽全部合格余量（QL 余 10＋NL 余 2 全数入封，无进一步扩量空间）；总量 40 恰达下限，无降级凑数。
