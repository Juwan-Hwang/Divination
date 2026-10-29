# liuren-seg5 评审简报（轴二：实际应验）

## 第一步：逐字读冻结评审提示
`benchmark/phase3/runs/calib-r17/JUDGE-PROMPT.txt`——逐字执行，不得改写、不得增删规则。

## 你的包
你评**全部两包**：`benchmark/phase3/runs/liuren-seg5/judging/packetA.json`（9 条）与 `packetB.json`（8 条），合起来是我方全部 17 例断语（匿名）。包内 prediction 结构化字段为 null 属既定形态——**断语正文经主持映射回读**：用 `benchmark/phase3/runs/liuren-seg5/judging/host-mapping.json`（anon_id → case_id）定位案例，再读 `benchmark/phase3/runs/liuren-seg5/predictions-frozen/<case_id>.json` 的 prediction_text 作为被评断语；包内 outcome_record 即该例结局。大师侧分数由主持以既有基线配对，不归你评。

## 评分口径（冻结提示细则）
- 三项各 0–2 分、0.5 步进：direction（方向）、claims（具体断言命中）、timing（应期）。total＝三项和（满分 6），pass＝total ≥ 4。
- 特殊口径：结局无可核时点 → timing 记 1 并在 reason 注明「结局无可核时点」；断语无应期 → timing 记 0 并注明「断语无应期」。
- claims 必须逐条回读 prediction_text 全文核验，未被结局记载的子断语不得给满分。
- 逐条独立评分，只对断语与结局的实际应验负责，不因文风加减分。

## 输出（只写指定文件，不做 git 提交）
评审 A 席写 `judging/judgeA-part1.jsonl`（packetA 9 行）与 `judging/judgeA-part2.jsonl`（packetB 8 行）；评审 B 席写 `judging/judgeB-part1.jsonl`（packetA 9 行）与 `judging/judgeB-part2.jsonl`（packetB 8 行）。JSONL，每行：{"anon_id","direction","claims","timing","total","pass","reason"}，reason 一句中文写明得分依据。包内每条一行，不得缺漏。
