# holdout4 封存日志

- **组建时间**：2026-10-29T15:30:06+08:00（Asia/Shanghai）
- **组建角色**：数据角（Phase 3 第二轮扩数建池）
- **算法**：仅对 expansion2 新增 84 例 A 级案例按 tradition × contamination 分层（本轮仅 liuyao × low 一层），层内按 sha256("phase3-round2-20261029:"+id) 十六进制升序，每 10 例取第 3、6、9 位入 holdout4；划分详见 benchmark/phase3/splits4.json，落盘即冻结。
- **例数**：holdout4 共 25 例（LY-343、LY-321、LY-414、LY-431、LY-459、LY-327、LY-444、LY-409、LY-337、LY-447、LY-456、LY-420、LY-435、LY-448、LY-401、LY-438、LY-453、LY-419、LY-450、LY-410、LY-326、LY-334、LY-345、LY-422、LY-341）。
- **金标 SHA-256**：`4c5c989cb37c774ce78e3ecb8c2c96b6d4a333fdbd99a35c4d0105006219c147`
- **结局封存位置**：benchmark/phase3/holdout4/test_gold.jsonl（同目录 SEALED.md 注明只许评审角验收时开封）；holdout4 的盲测 inputs 单独置于 benchmark/phase3/holdout4-inputs/，不含任何答案字段（核对记录 benchmark/phase3/expansion2/input-check2.txt）。
- **状态**：**未开封**。自本笔落盘起，holdout4 结局不进入任何给盲测角／修订角的材料；开封须由评审角于验收轮在本日志追加一笔后进行。

## 开封记录（验收轮）

- **开封时间**：2026-10-29T16:28+08:00（Asia/Shanghai）
- **开封角色**：主持角（代评审侧建包角执行开封登记；建包脚本只建包不评分，评分由独立评审角执行）
- **依据**：holdout4 验收预注册（benchmark/iterations.md，提交 84862aa）；R13 平台裁定成立（提交 d4c9c13）；我方 25 例盲测预测已齐备并经主持角覆盖校验（25/25、七字段零错误，落 benchmark/phase3/holdout4-acceptance/predictions/），盲测全程未接触金标。
- **范围**：读取 benchmark/phase3/holdout4/test_gold.jsonl 建混编匿名评审包（anon 前缀 H4-）；建包脚本内嵌封存哈希校验（SHA-256 须与本日志登记值一致，不一致即中止）。
- **状态变更**：holdout4 自本笔起为「已开封·验收中」；验收完成后标「已用」。

## 验收完成记录

- **完成时间**：2026-10-29T16:33+08:00（Asia/Shanghai）
- **结果**：我方 3.210 vs 大师 4.820，配对差 −1.610（4/1/20），达标三判据全不成立，**未达标**。详见 benchmark/phase3/holdout4-acceptance/REPORT.md。
- **状态变更**：holdout4 自本笔起标「已用」，不得再作验收集。
