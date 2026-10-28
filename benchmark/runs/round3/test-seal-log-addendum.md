# Round 3 封存日志追加（test-seal-log-addendum）

- 日期：2026-10-29。角色：数据角（只管数据整理与封存，不作断、不评分）。
- 依据：Round 3 预注册（benchmark/iterations.md 末节）——候选池两例正式启用；冻结的原 133 例划分一例未动，本次全部写操作均为追加。
- 本文件只记启用与封存动作、去向与计分口径，不载任何金标内容。

## 一、wei-023（吴子深造，源 chinese-natal 分卷）

- 来源：masters-dataset/chinese-natal/inputs.jsonl 与 answers.jsonl 中 id=wei-023 条目（视觉补核已补齐月柱，源条目标 disputed，统一记录保留 disputed 标注与订正说明）。
- 动作：映射为统一 schema 记录（id=wei-023，split=dev），追加至 masters-dataset/data/dev.jsonl 末尾（93 → 94 行，既有 93 行未改动）。
- 划分登记：masters-dataset/splits.json 追加 "wei-023": "dev"（既有 133 条未改动）。
- 盲测输入：生成 benchmark/runs/round3/inputs/wei-023.json（格式同 round3 既有输入文件，仅含输入面字段）。自检：grep 该文件 "master_predictions"、"outcome"、"direction" 三词均为 0 命中，无例外字段需说明。
- 计分口径：常规计分（量表三项，口径同 Round 3 预注册）。

## 二、lilly-nativity-1616-merchant（源 western 分卷）

- 来源：masters-dataset/western/inputs.jsonl 与 answers.jsonl 中 id=lilly-nativity-1616-merchant 条目。
- 动作：映射为统一 schema 记录（id=lilly-nativity-1616-merchant，split=test）——
  - 输入面（不含答案）追加至 masters-dataset/data/test_inputs.jsonl 末尾（40 → 41 行）；
  - 完整记录（含金标）由数据角追加封存至 masters-dataset/holdout/test_gold.jsonl 末尾（40 → 41 行，既有 40 行未改动）；金标内容未复制到任何其他文件。
- 划分登记：masters-dataset/splits.json 追加 "lilly-nativity-1616-merchant": "test"。
- 计分口径注记：应验项不计分——outcome 为 book_internal_only、只作断法示范（该注记已随条目写入统一记录 notes）。本轮（Round 3）仍不跑 test，本例仅完成封存登记。

## 三、校验（2026-10-29，数据角执行）

- 行数：dev.jsonl 94 行、test_inputs.jsonl 41 行、test_gold.jsonl 41 行、splits.json 135 条。
- 交叉一致：splits.json 与三个数据文件的 id/split 逐条对齐；两例新 id 在各自去向文件中有且仅有一条，split 字段与 splits.json 一致。
- 池总数：133 → 135（dev 93 → 94、test 40 → 41），已同步追加记录于 benchmark/pool-manifest.md 末节。
