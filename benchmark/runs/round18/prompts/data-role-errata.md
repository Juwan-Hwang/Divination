# 数据角旁线任务（Round 18，不阻塞验收）

你是 MastersDivination Benchmark 的数据角，只管数据核对与登记，不作断、不评分、不改任何既有数据文件。

## 任务 1：LY-018 输入自洽性 errata 核对
背景：多轮报告登记 LY-018 输入存在「卦名/爻位不自洽」疑点（见 benchmark/iterations.md 与 runs/round16、round17 报告的口径登记）。请回 chinese-divination 源头核对：
- 读 masters-dataset/chinese-divination/inputs.jsonl 与 answers.jsonl 中 LY-018 条目，找出卦名、爻位、动爻等字段之间不自洽的具体位置；
- 回源头出处核对原文：该例源自《增删卜易》（维基文库全文已下载在 ~/workspace/divination/sources/ 下，自行定位对应章节），逐字比对输入字段与原文；
- 给出结论：不自洽属实与否、错在哪个字段、正确值应为是什麼、证据引文（原文逐字摘录＋出处位置）。
结论写入 ~/workspace/divination/benchmark/runs/round18/errata/LY-018-errata.md（含核对过程、引文、结论、建议处置）。严禁直接修改 inputs.jsonl/answers.jsonl/dev.jsonl 等任何既有数据文件——纠错只追加 errata，改不改数据等主持角与主会话裁定。

## 任务 2：schema id 正则修订建议（只登记不擅改）
读 masters-dataset/schema.json 中 id 字段的正则/pattern 现状，结合现行 id 形态（LY-01、LY-03 这类短 id 与 LY-001 并存、lilly-nativity-1616-merchant 这类长 id 已入集），写一份修订建议（现正则为何不匹配、建议改成什麼、影响哪些既有 id）写入 ~/workspace/divination/benchmark/runs/round18/errata/schema-id-pattern-proposal.md。严禁直接修改 schema.json。

两件办完后汇报每件的结论一句话与文件路径。
