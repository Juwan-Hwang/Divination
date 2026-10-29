# SEALED — holdout8 测试集金标（未开封）

- 封存时间：2026-10-29T19:58:07.918110+08:00（Asia/Shanghai）
- 来源轮次：Phase 3 第六轮扩数（expansion6），全新收集 A 级案例
- 例数：28（modern-cn 7、modern-west 4、classical-other 17；low 污染 10、high 污染 18）
- 选择规则：全新 A 级中 low 污染全取（10 例），余位按来源分层、sha256("phase3-expansion6-holdout8:<id>") 定序补 high 污染例；规则与名单见 splits7.json 与 build_dev7.py
- 金标文件：benchmark/phase3/holdout8/test_gold.jsonl
- 金标 SHA-256：6db901c23b5e0e51f7c361f85ff7783b19e0563e74899a94347ba21596815c77
- 盲测 inputs：分散于 benchmark/phase3/expansion6/*/inputs/（holdout8 例不入 inputs7）
- 状态：**未开封**。开封须按 PROTOCOL 预注册后由评审角执行，并在此文件与 benchmark/phase3/holdout8-seal-log.md 追加开封记录。
- 纪律：数据角、修订角、盲测角不得读取 test_gold.jsonl 内容。
