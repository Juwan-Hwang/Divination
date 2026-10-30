# holdout13 封存说明（2026-10-30，R35 数据角封存）

- 构成：40 例，全新、从未入任何 dev/holdout，全 low 污染（低污染子集＝全集）。来源与体系：六壬 16（《大六壬断案》DA 8、《六壬辨疑》BY 5、《六壬粹言》卷六慕农占验 CY 3）、八字 12（《千里命稿》QL 10、《呱呱集/子平真诠评注》NL 2）、测字 12（《测字秘牒》CZ）、六爻 0（本轮有界普查实得 0，缺位如实登记，见 BUILD-LOG §四）。
- 构成验算（PREREG §6.② 写死口径逐条）：总量 40（≥40 ✔）；单一来源最大 CZ 12/40＝30.0%（≤50% ✔）；单体系最大六壬 16/40＝40.0%（≤40% ✔，恰在上限）；粹言干支级课式例 3/40＝7.5%（≤20% ✔）；六壬内部全课式原文直载来源（断案＋辨疑）13 例优先、粹言 3 例（≤8 ✔）。
- 选择规则：各源合格集内按源文件既有顺序取足配额、跳过已排除 id，无按难度/结局/预期分数挑选（防挑题规则与逐源入选清单见 BUILD-LOG §五）。资格准据：DA 以 cases-a/b 的 holdout_eligible 为准；BY 以 REVIEW-G 的 review.verdict=seal／grade_final 为准；CY 以 cases-munong 的 holdout_eligible 为准；QL 以 REVIEW-H 的 review.verdict=seal／grade_final 为准；NL 以 GRADE-ADDENDUM 改判为准（NL-006 改判 A-low、NL-049 原 A 且 addendum 确认资格不变）；CZ 以 HOST-RULINGS-3 资格生效口径（33 例全合格）为准。
- 等级（以准据计）：A 19、A-low 21。注记：金标中 NL-006 行的 outcome_grade 字段照源文件逐字保留为 B，其封存等级以 GRADE-ADDENDUM 改判 A-low 为准（与 holdout12 的 NL 例同一体例）；QL 10 例 review.grade_final 为 A（REVIEW-H 注明按 A-low 口径保 A）。
- QL 编号注记：本批 QL 例的 id 即 natal-batch2/cases-reviewed.jsonl 现行 QL 号，与 holdout12 已用 QL-001…008 为同一编号空间内的不同例（内容逐例不同，审计已核，见 BUILD-LOG §六）；holdout12 建集时的 QM→QL 改编 source_id 映射未在盘上留存逐例对应，本批金标不带 source_id，金标行与 cases-reviewed 源行逐字一致。
- 课式完整度逐例登记：
  - 全课式原文直载（13）：DA-002、DA-004、DA-005、DA-008、DA-010、DA-011、DA-012、DA-013（课盘原文自断案 scratch-archive/cases_raw.json 直录）；BY-002、BY-003、BY-004、BY-005、BY-006（课式/三传/四课/天地盘自原书排印本 PDF 页图直录）。BY-003 天地盘末行天将行第三字排印本作「无」，照原字录入（他例玄武省作「元」，此字经 400dpi 放大核读为「无」，只登记不改字）。
  - 干支级（3）：CY-002、CY-003、CY-004（原书有课盘列、转录底稿未录盘字、页图盘字漫漶，输入卡仅录干支/月将/占时，盲测按六壬章起课程序自起；验收结论引用时须连同此限度）。
  - 非六壬课式（24）：QL 10＋NL 2 四柱全载直录（源行 chart 字段／题面括注）；CZ 12 所测字直载。
- 成色注记：DA-008 三传中传干支原盘仅作「申」（单支），照盘转录为「兄申（蛇）」，旬空标记◎⊙只保留于课盘原文、三传串不带。QL-030 输入卡删后事身份词「中储蓄会头奖者」（金标不动，照 holdout12 QL-006 卡卫生先例）。
- 输入卫生：建卡剥离 grade_note／review／method_hint 类字段并逐例登记（BUILD-LOG §八）；40 卡全数通过禁键扫描（grade_note／outcome／master_predictions／review／method_hint／contamination 零命中）。QL/NL 输入卡 asked_at 的体例性回顾框架语（含「应验追记」字样）为全批一致的通用语、无本例结局，照 holdout12 先例保留。
- 封存前编号唯一性审计：runs/round35/audit_ids_holdout13_r35.py（只查 id 冲突）已跑，40 例无一命中 dev9（inputs-dev11 文件名集）、POOL-IDS、splits 清单或任何其他 holdout 金标；15 例的同 id 出现仅为同源复核孪生文件（BY 的 cases.jsonl 原件、QL 的 cases.jsonl 原件），经输入侧字段逐一核对为同一例，处置见 BUILD-LOG §六。
- 金标：holdout13/test_gold.jsonl，SHA-256 `75c5349d6184d5cace454dadb790433eabac731f38884b889cd1f9bd67aab483`，登记于 data/holdout13-seal-log.md 与 data/splits12.json。输入卡在 benchmark/phase3/holdout13-inputs/（40 张）。
- 开封条件：R35 于 dev9 平台判据全立后按其预注册 §3 开封；开封前验金标 SHA 与封存值逐字一致。验收结论只对本集构成所及口径发言（六壬/八字/测字为主、六爻 0 例不作六爻结论）。
