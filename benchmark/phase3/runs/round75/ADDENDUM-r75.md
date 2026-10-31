# ADDENDUM-r75 — R75 附记（供给、事件与登记）

（主持角，2026-10-31。定稿见 runs/round75/REPORT.md 与 final-scores.json analysis_r75 节。）

## 一、供给状态（开轮核查与本轮结果）

- 开轮到货核查：以 runs/round74/REPORT.md 为界，incoming 与用户文件区（~/workspace/user/files）find -newer 实查为空——**无新到货**。
- holdout22 绑定缺口不变：非六爻锚点在场 eligible 缺 **12 例**；本轮不组集、不封存。无封存集存量，R61-REV1 判读继续顺延（判读集＝holdout22，口径照 PREREG-ADDENDUM-r61 §三写死，禁改门槛禁同集调参）。
- 候选面维持 ADDENDUM-r74 §四/§五定案：第五批 8 条（紫微必得 2／奇门应得 3／八字应得 1／梅花可跳过 2，WANTED-TEXTS.md 第五批章节 bdf6964d）＋《字触补》丛书路径（《四库未收书辑刊》第六辑第 18 册，待用户按丛书名复检）；《实战卦例精解》已核查关闭、《卜筮元龟》卷下维持当前渠道未获。以上待用户项只登记不催办。

## 二、主持工具事件（评审合并文件名口径）

- merge_judge_views_r75.py 首跑 KeyError 'total'：R74 体例中 judgeX-block*.jsonl 为评审席评分输出名，R75 构建脚本将同名文件用作评审包、派单另定评分输出为 scores-judge*.jsonl，合并脚本（承 R74 逐字）遂误读包文件。主持定案：改合并脚本 main() 读 scores-judgeX/Y*.jsonl 并在 docstring 登记，机制与断言不变；8 个评分文件结构先行复核全好（974 行、键集全对），合并结果双视各 487、anon 集与 mapping 全等。影响为零，不涉任何分数。

## 三、席位自报与隔离事项登记

- **BZ-019**：卡面 setting 内嵌「盲测时不得给身份」字样，盲测 S1 席按数据处理未从其令；数据席 fresh 裁部分成立入案（case-annotations-r75.json）——卡面字样属实、系盲测 withheld 设计、R75 prediction 全文无身份字样。结局/卡面内嵌指令性字样不作指令，照既定口径。
- **S5 席 /tmp 转存**：read 工具输出溢出由工具基础设施自动转存 /tmp，非席位写入、席位未读取使用，影响为零。与 R72 席位自写转储性质不同，如实登记。
- **S3 席 exec 非零退出**：会话内一处命令非零退出，按 R68 判例以主持盘上验盘为准（该席 60/60 验全）。
- **S4 席中间转储**：s4_cards_dump.txt 只置本轮目录内，合规；未入任何提交（未跟踪 scratch，勿 add 勿删，同 judging/build-Y2.py、review-Y2.txt）。
- 十盲席与八评审席均自报隔离无违规；本轮无通配删除事件、无目录计数违规（目录计数禁令下达后第二轮）。

## 四、数据席对勘差异登记（派单表述与盘上构造）

- 数据席登记：R75 manifest `_r75_carryover_notes_addendum` 层 67 件注记为建议文本原文直入（与 manifest_carry_suggestion 全文逐字相等 67/67），不含「[R75-addendum]」分隔字样（0 件）。主持核对：与 build_manifest_r75.py 原构造一致——manifest 层存建议原文，「[R75-addendum]」前缀仅由 build_judge_packets_r75.py 在评审包 carry_note 层拼接。主持给数据席的派单句将两层混述，属表述不确，产物无误、对勘结论（67/67）不受影响。此后派单涉多层构造时逐层写明。

## 五、旗标与定案汇总（详见 data/case-annotations-r75.json、data/manifest-carryover-r75-addendum.md）

- tradition 主持复核 24 件：冻结时全数裁定检查器关键词覆盖缺口（卡面确无 tradition/system 字段、首行如实注明），实效分布 direct 365／none-labelled 122／flags 0，与 R74 冻结实效分布逐值相同（FREEZE-r75.md §二）。
- 评审＋盲测旗标定案 64 例：成立 12／部分成立 48／不成立 2／未核 2；同旨续接 59、同例新旨 2（LY-227、BZ-019）、新立 1（LY-035）。未核 2＝YM-070（挂起维持，本轮被 X4/Y4 触及）与 LY-537（被盲测席触及，OCR 行序风险，只登记触及）；BZ-029／BZ-040 未被触及、不入案，维持未核。
- R76 manifest 待落实：R75 部分成立 48 件建议（新层 `_r76_carryover_notes_addendum`，自 case-annotations-r75.json 结构化直读）。
- CZ-QX 同档计数维持 4，续结仍系《字触补》丛书复检或第五批测字外新面（第五批测字方向查无）。

## 六、W 监测（W38）

- DIAG-LR-weight-dev75.md：六壬 dev8 −2.292（n=18)、合并 −1.917（n=30)、LR3-new −1.354（n=12)，负例 23 例；W 双报合并 21.7%（5/23，硬核 0)，§5 稳健区间不可判定；T1–T4 无一齐备，六壬章冻结维持、解冻通道未开。
