任务：担任 MastersDivination Benchmark Phase 2 Round 2 的盲测角，对分配给你的案例逐例作断。工作区 ~/workspace/divination/。

方法：先通读 benchmark/phase2/method/SKILL.md 并按需查阅 benchmark/phase2/method/references/ 与 tools/（这是本轮唯一方法来源，v1 冻结版，零改动轮）。方法不拘、可混用体系、可运用概率与基础率推理，以断准实际结果为唯一目标。

逐例流程：读 benchmark/phase2/inputs/<id>.json（只有对象与背景，无答案）→ 作断 → 写 benchmark/phase2/runs/round2/predictions/<id>.json，字段：
{"id", "direction": "positive|negative|mixed", "assertions": [具体断语，对象/时间/部位级别，逐条可证伪], "timing": "明确的应期/时点判断（尺度与坐标都写清；实在无从判断写『无从判断』）", "summary": "一句话结论", "method": "所用方法", "reasoning": "依据链简述"}

铁律：严禁看任何含结局的材料——不许读 masters-dataset 的完整记录（dev.jsonl/test_gold.jsonl）、dual-axis 目录、phase2/data/roster.jsonl、runs/round17、round18 的 judging/final-scores、iterations.md 的结果节；严禁联网搜案例；不许与其他盲测角交流。只许读：phase2/method/ 全部、phase2/inputs/ 中分配给你的案例。

交付回传：完成例数、每例 direction 一行清单、写入文件数校验（ls 计数）。
