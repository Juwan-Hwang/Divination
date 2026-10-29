任务：担任 MastersDivination Benchmark Phase 3 Round 1 的盲测角，对分配给你的案例逐例作断。工作区 ~/workspace/divination/。

方法：先通读 benchmark/phase3/method/SKILL.md 并按需查阅 benchmark/phase3/method/references/ 与 tools/（本轮唯一方法来源，含「应期双层表达」通则，务必执行）。方法不拘、可混用体系、可运用概率与基础率推理，以断准实际结果为唯一目标。

逐例流程：读 benchmark/phase3/inputs/<id>.json（只有对象与背景，无答案）→ 作断 → 写 benchmark/phase3/runs/round1/predictions/<id>.json，字段：
{"id", "direction": "positive|negative|mixed", "assertions": [具体断语，对象/时间/部位级别，逐条可证伪], "timing": "应期/时点判断：事件型占断按双层表达——先写窗口（尺度与边界写清），再写窗口内主坐标；命造类写运档；实在无从判断写『无从判断』", "summary": "一句话结论", "method": "所用方法", "reasoning": "依据链简述（含窗口推出依据）"}

铁律：严禁看任何含结局的材料——不许读 masters-dataset 的完整记录（dev.jsonl/test_gold.jsonl）、dual-axis 目录、phase2/data/roster.jsonl、phase3/data/roster3.jsonl、phase3/expansion 的 answers.jsonl、phase3/holdout3/、任何轮次的 judging/final-scores、iterations.md 的结果节、历轮 predictions；严禁联网搜案例；不许与其他盲测角交流。只许读：phase3/method/ 全部、phase3/inputs/ 中分配给你的案例。

交付回传：完成例数、每例 direction 一行清单、写入文件数校验（ls 计数）。
