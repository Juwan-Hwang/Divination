任务：担任 MastersDivination Benchmark Phase 3 Round 1 的评审角（独立），给匿名预测打「实际应验轴」（轴二）分数。工作区 ~/workspace/divination/。

对象：指定 packet 文件（benchmark/phase3/runs/round1/judging/packetA.json 或 packetB.json），每条 {anon_id, prediction{direction, assertions, timing, summary}, outcome_record（客观结局记录）}。你只评预测与现实结局的吻合，与任何大师断语无关，也不得去查找案例身份或其他分数。

量表（三项各 0–2）：
1. 方向对现实：2=预测方向与实际结局同向同级；1=同向不同级/含糊；0=反向或不敢断。
2. 关键断语对现实：2=具体断语（对象/时间/部位级别）被结局证实；1=部分证实或错位；0=被证伪或只有空泛吉凶。
3. 应期/时点对现实：2=应期与实际时点对齐；1=部分对齐（尺度对坐标偏、窗口含实应时点而主坐标偏等）；0=不对齐。预测未给应期或结局无时点可核 → 本项记 1 并标注「无时点可核（中性记 1）」。

输出 JSONL 到指定文件，每行：{"anon_id","direction","claims","timing","total","pass"(>=4),"gap_note":"失分形态一句话（全对写『无』）"}。交付回传：条数、均分、通过数。与其他评审互不可见，不得交流；不许读 predictions 原始文件、answers 或任何既有分数文件。
