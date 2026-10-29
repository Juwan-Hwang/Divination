任务：担任 MastersDivination Benchmark Phase 2 的评审角（独立），给匿名预测打「大师一致性轴」（轴一）分数（本阶段仅作旁报）。工作区 ~/workspace/divination/。

对象：指定 packet 文件，每条 {anon_id, prediction{direction, assertions, timing, summary}, master_statements（大师断语节录）, outcome（原载应验结果）}。

量表（PROTOCOL 原量表，三项）：
1. 结论方向：2=与大师同向同级；1=同向不同级/含糊；0=反向或不敢断。
2. 关键具体断语：2=与大师同等具体程度且命中其断语要点；1=有具体但错位；0=只有空泛吉凶。
3. 应验结果对齐：2=断语与实际应验事件对齐（与大师断语的应验口径一致）；1=部分对齐；0=不对齐。
另：预测所用方法与大师不同体系而三项对齐者，标 cross_system=true。

输出 JSONL 到指定文件，每行：{"anon_id","direction","claims","timing","total","pass"(>=4),"cross_system":bool,"gap_note":"一句话"}。交付回传：条数、均分、通过数。与另一位评审互不可见，不得交流。
