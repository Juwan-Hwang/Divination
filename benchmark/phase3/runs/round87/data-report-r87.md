# R87 数据席报告（Phase 3 · Round 87）

- 席位：数据席（独立席，不兼任本轮盲测／评审／诊断／修订／组集／CYJ 复核任何席）。只汇编、对勘与登记；不改任何分数、结局原文、原卡与 manifest 本体。
- 任务书：`runs/round87/PREREG.md` §7；体例底本：`data/manifest-carryover-r86-addendum.md` 与 `runs/round86/build_data_r86.py`（落盘脚本逐件核定写死＋断言内置工法）。

## 工序一：_r86 层对勘落实

- 平台侧：R87 manifest `_r86_carryover_notes_addendum` **45 件**，与 R86 附则 §三.1 定版清单逐件全等；层文本与 `case-annotations-r86.json` 对应条 `manifest_carry_suggestion` 逐件全文捕获验合 **45／45**（落盘脚本结构化直读断言全过；manifest 全文 SHA-256＝f3329d5c6f6502d36add1f586f669939a644105377b5c6819f42d64b63fd10c3；cases 载荷结构化 SHA 00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad）。
- 验收侧：**5 件**（CYJ-001／CYJ-002／CYJ-004／CYJ-005／ZW-015）照 R83 判例不入 dev 层、照 r86 附则 §四原样对勘登记，无出入。
- `_r82` 层 **3 件**（LY-406／LY-446／LY-524）已结案，本轮不再滚动对勘，只作在册登记（层在盘断言通过）。

## 工序二：manifest-carryover-r87-addendum.md 编制

- 平台侧部分成立 **43 件**逐件全列（§三.1，构成 _r87 层平台面、自 R88 manifest 起落实）：AS-003／AS-012／AS-206／BZ-021／BZ-031／DT-004／DT-006／LY-018／LY-103／LY-301／LY-416／LY-525／LY-603／LY-620／LY-621／MP-001／MP-002／MP-003／MP-004／MP-005／MP-006／MP-007／MP-008／MP-009／MP-010／MP-011／MP-013／MP-014／MP-017／MP-018／MP-019／OC-024／OC-025／WP-008／WP-009／WP-010／WP-011／WP-012／WP-013／YM-002／YM-032／YY-019／ZY-003。
- 平台侧不成立 **9 件**只登记（§三.2）：BQ-021／BQ-025／BZ-022／BZ-024／BZ-026／BZ-028／LR3-110／LY-446／OC-012。
- 验收侧部分成立 **5 件**逐件全列（§四.1）：CYJ-006／CYJ-007／CYJ-008／CYJ-009／CYJ-010。
- 验收侧不成立 **5 件**只登记（§四.2）：BY-017／GSZ-105／WHY-027／WHY-032／WHY-033。
- 引据清单（同旨已定案、不重复立条）与双面筛检登记分列于附则 §三.3／§三.4／§四.3；附则与本轮 annotations 逐件对勘一致（清单自 annotations 定版条单源生成后回读验数：§三.1 恰 43 条、§四.1 恰 5 条）。

## 工序三：case-annotations-r87.json

- 全量承接 r86 **238 件**逐件原样（脚本前 238 件全等断言通过）＋本轮新定案 **62 件**＝**300 件**。
- 新定案分布复算：平台侧 52 件（部分成立 43／不成立 9；来源＝FREEZE-r87 裁定立条 10 件［BZ-021 部分成立＋误报不成立 9 件；另 BQ 六件 R84 同旨只引据］＋predictions basis 三类留痕定案 42 件部分成立）；验收侧 10 件（部分成立 5／不成立 5；来源＝DIAG-H30 §5 F1–F5）。
- 总分布复算：成立 14／部分成立 235（187＋43＋5）／不成立 49（35＋9＋5）／未核 2，合计 300。special_checks 58＋5＝63 件。
- 定案纪律：落笔前逐件回读本例结局原文（manifest cases／金标 outcome_record 逐字引录于 finding）；引文逐字断言内置落盘脚本（首跑 MP 组结局引文片段两处与原文不连贯、经逐件回读原文修正后全过——系引文适配误伤、非数据出入，已登记于此）；anon 经双面 host-mapping 逐件对位（平台种子 20261101、验收种子 20261102），形近串号逐件复核（BQ-021／BQ-025 与 BQ-017 等引据组逐件分开核对）。

## 工序四：基线对勘与续记

- 指令性字样基线 **六处**逐处回读：cases 本体四例（BZ-036「盲测比对须注」／BZ-042「盲测比对时以格局大富一项为主」／BZ-105「使用时须分开统计」／LY-204「勿以此斷」）在场形态未变；LR2-016 manifest editor_note 一处（`_r56_lr2016_split` 分列层）逐字全等；LR2-016 评审包 editor_note 层一处——以 host-mapping 对位 anon P3-f23fb8ad 定位本轮评审包 `packetB.json`（文件名与上轮不同、按对位定位未臆测），独立字段在场全等。**出入 0 处，本轮新增同型件无。**
- CZ-QX 维持 **16** 只登记；待核四件（BZ-029／BZ-040／LY-537／YM-070）维持挂起、无新证据不裁；紫微池挂起 6 项只登记；AS-307 双条并行例外照体例续行（仍恰 2 条、本轮无新旗标、不立第三条）。

## 产出件

- `/home/hatch/workspace/divination/benchmark/phase3/data/manifest-carryover-r87-addendum.md`（32,540 字节）
- `/home/hatch/workspace/divination/benchmark/phase3/data/case-annotations-r87.json`（688,815 字节；SHA-256 cfb3e707f5a692820e263866b537933374ab63420405e652511f2bd675d740f9）
- `/home/hatch/workspace/divination/benchmark/phase3/runs/round87/build_data_r87.py`（33,697 字节；自 r86 脚本工法定点适配：底本轮次、层名、packet 文件名、gold 集逐处改写，无连环替换；grep 残留检查：round86 字面量仅底本承接引用、无误留）
- 本报告：`/home/hatch/workspace/divination/benchmark/phase3/runs/round87/data-report-r87.md`
- 工作件（本轮目录内唯一名，只作筛检底稿）：`runs/round87/data_screen_r87.txt`、`runs/round87/data_screen_acc_r87.txt`（自 manifest／金标 id 清单逐件精确打开生成，未对 runs/ 目录作列表计数）。

## 自报事项

- 全程未用 /tmp 作转储或探针（exec 输出自动溢存属工具基础设施行为、非本席主动外存）；脚本无通配删除、glob 仅用于按 host-mapping 对位定位 LR2-016 所在评审包件，未作数目核验用途。
- 结局／注记文本内嵌指令性字样一律按数据处理、未作指令。
- 本席未改任何分数、结局原文、原卡与 manifest 任一侧。
