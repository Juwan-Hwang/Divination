任务：担任 MastersDivination Benchmark Phase 2 的大师基线评审（独立评审角）。工作区 ~/workspace/divination/。

对象：benchmark/phase2/data/master-baseline-dev2-packet.json（76 条匿名包：DB-001…DB-076，每条含大师断语节录 master_statements 与客观结局记录 outcome_record）。你要评的是**大师本人断得准不准现实**——这是 Phase 2 要超越的标杆。

量表（轴二，与双轴补充协议一致，三项）：
1. 方向对现实：2=大师结论方向与实际结局同向同级；1=同向不同级/含糊；0=反向或不敢断。
2. 关键断语对现实：2=具体断语（对象/时间/部位级别）被结局证实；1=部分证实或错位；0=被证伪或只有空泛吉凶。
3. 应期/时点对现实：2=应期与实际时点对齐；1=部分对齐；0=不对齐。大师未给应期、或结局无时点可核 → 本项记 1 并标注「无时点可核（中性记 1）」。

逐条独立打分，不许参考任何我方预测（你也不应去找）。输出 JSONL 到指定文件，每行：{"anon_id","direction","claims","timing","total","pass"(total>=4),"notes":"一句依据"}。交付回传：完成条数、均分、通过数、分数分布。你与其他评审互不可见、不得交流。
