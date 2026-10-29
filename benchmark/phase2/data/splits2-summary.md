# Phase 2 splits2 划分汇总（数据角，落盘即冻结）

算法（严格按任务书执行）：在每个 tradition × contamination 分层内，按 sha256("phase2-20261029:"+id) 的十六进制串升序排序，每 10 例取排序后第 3、6、9 位（即位置序号 mod 10 ∈ {3,6,9}，约 30%）入 holdout2，其余入 dev2；分层内不足 3 例的分层全入 dev2。

| tradition | contamination | n | dev2 | holdout2 |
|---|---|---|---|---|
| astrology | high | 4 | 3 | 1 |
| bazi | high | 27 | 19 | 8 |
| bazi | low | 2 | 2 | 0 |
| fengshui | high | 2 | 2 | 0 |
| horary | high | 3 | 2 | 1 |
| horary | low | 11 | 8 | 3 |
| liuren | high | 1 | 1 | 0 |
| liuyao | low | 40 | 28 | 12 |
| meihua | low | 8 | 6 | 2 |
| vedic-astrology | high | 3 | 2 | 1 |
| yijing | high | 4 | 3 | 1 |
| **合计** |  | **105** | **76** | **29** |
