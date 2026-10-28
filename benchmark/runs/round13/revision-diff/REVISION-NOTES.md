# Round 13 修订说明（修订角）

## 性质

单变量回滚验证轮。依据仅为 Round 12 REPORT 第二节（H12 判定与主持诊断）与第五节（Round 13 诊断方向），以及 `benchmark/iterations.md` 中「Round 13 预注册」一节。本轮不引入任何新规则，只执行一处删除。

## 回滚对象

- 文件：`chinese-liuyao-meihua.md`
- 删除对象：Round 12 新增的独立小节「### 空破伏待出判读（必经，用神空破伏时的终局合成）」全文。
- 删除位置（删除前行号）：原第 106–121 行，位于伏神判读清单（伏神五步清单，第 5 步「按四项满足数定三档结论」）之后、「### 真空／假空成文判别（知识补强）」之前。
- 删除内容构成：小节标题 1 行、通则出处引言、触发（强制启用）、两段式强制（现态段／待出段）、两段关系与终局归属、病占特则、与既有规则的衔接，以及段间空行与小节末尾空行。
- 删除行数：**16 行**（`git diff --numstat`：0 insertions、16 deletions；文件总行数 340 → 324）。

## 删除后与 Round 11 形态的核验结论

**结论：一致，无差异，无需标红停下。**

- 删除后哈希（实测）：
  `3e7bbc9b117ff4e7eba93b1d7403fb010fdf632c2f861a8130861384984d6113  chinese-liuyao-meihua.md`
- Round 11 快照清单（`benchmark/runs/round11/kb-snapshot/MANIFEST.sha256`）中该文件哈希：
  `3e7bbc9b117ff4e7eba93b1d7403fb010fdf632c2f861a8130861384984d6113`
- 两者**逐字（逐字节）一致**。哈希一致即证明删除后文件与 Round 11 快照为同一字节序列，因此下列保留项与 Round 12 版本中除被删小节外的部分逐字一致、无一字连带改动：
  - 六爻判定序（空、墓、伏、化进退取舍决策序；化进/化退与动化复核；空墓伏冲起判定序与化退终局权重合流）
  - 动化定性裁决表与执行留痕
  - 伏神五步清单（伏神待出成文判别，五步与四项判据三档）
  - 病位取象核对清单（病位取象复核、病占原神有根／源绝成文判别）
  - 类别条件读法
  - 双动／终局反转信号扫查（完整判据链门槛）
  - 对象对齐表
  - 两段式通则（原文未动；被删的只是其在空破伏情形下的专用强制形态）
  - 梅花全部内容（先天数与起卦、体用断法、爻辞取象核对与事实优先序、梅花具体断语作断前自检表、对象同类核对、六爻与梅花分工等）
  - 真空／假空成文判别、应期三步等其余小节

## 其余文件

- 八字文件 `chinese-bazi-ziwei.md` 本轮一字不动，Round 12 的合绊否决保留。实测其 sha256 删除前后均为 `8353fcab503aaa40819387e01799e9fcf453b59bec2a1855a7b6425d5f296fd0`，且 `git status` 中该文件无修改标记。
- `git diff --stat` 全仓仅 `chinese-liuyao-meihua.md | 16 ----------------` 一项；diff 中除该小节删除外无任何其他增删（见同目录 `kb-changes.diff`）。

## 产出

- `benchmark/runs/round13/revision-diff/kb-changes.diff`（由 `git -C ~/workspace/divination diff -- chinese-liuyao-meihua.md` 生成）
- 本文件 `benchmark/runs/round13/revision-diff/REVISION-NOTES.md`
