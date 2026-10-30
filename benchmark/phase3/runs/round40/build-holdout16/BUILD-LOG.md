# holdout16 BUILD-LOG（R40 数据角，2026-10-30）

## 产物
- 输入卡：`benchmark/phase3/holdout16/inputs/` 40 张（ZC 20＋BYZ 10＋YXS 3＋DA 7）。
- 金标：`benchmark/phase3/holdout16/test_gold.jsonl` 40 行。
- **金标 SHA-256：`2040c63e3d3ba6481a84507880eba27a2aae6b7e8b8f78c1327a84c4c35f3e10`**（构建脚本输出与封存后 sha256sum 双读一致）。金标建成后未再打开其内容。
- 封存日志：`data/holdout16-seal-log.md`。选取清单：`runs/round40/build-holdout16/SELECTION.md`（建卡前落盘，含建卡期对勘补记）。
- 构建脚本（唯一名、新写于 runs/round40/ 内）：`runs/round40/build_holdout16_r40.py`；六壬 enrich 数据：`runs/round40/build-holdout16/liuren-enrich-r40.jsonl`；构建报告：`runs/round40/build-holdout16/build-report-r40.json`。

## 构建过程与校验
1. 选取：按 PREREG §5.2 写死构成自 SUPPLY-VERIFY 合规清单内按题材选取（测字合规 23 取 20、余 ZC-072/073/130 留库存；辨疑合规未用 88 取 10；预测学 3 全取；断案新鲜合规 137 取底本课式完备 7），SELECTION.md 先行落盘。
2. 回源对勘（逐例）：测字 20 例回字触原页图（expansion12/cezi-zichu/work-pages 与 runs/round39 work-pages-j3）核测字/事主/所问；辨疑 10 例回原书 PDF 页图（本轮 pdftoppm 200dpi 渲染至 work-bianyi/，含 BYZ-106 因卷五偏移 +14 改渲染 PDF139–140）核题面/课式/正议/案验，并自原页转录课式全式与正议摘录；预测学 3 例回原书页图（R39 核查图 yucechk-181…188）核题面/图式/推论/验证并转录；断案 7 例回 cases_raw.json 全文，课盘/三传/月将/旬空/年命由脚本逐例解析补录，并断言台账断语摘录（去标点）连续 6 字窗口命中底本、解析三传恰 3 条。
   结果：**对勘不合 0 例、无替补、无降格**。
3. 断言全过：构成 20/10/3/7＝40；全例 outcome_grade=A-low、contamination=low；40 张输入卡递归禁用键扫描 17 类命中 0；三键去重（对象＋时间＋事项，参照＝dev 487 卡＋holdout15 40 卡＋holdout3–14 金标三键，去重后参照 663 条）命中 0、弱键（对象＋事项）命中 0、id 冲突 0、集内三键互异。
4. 异常/注记登记（2 件，均不影响入选）：
   - DA-136 底本谛注「课同169」：DA-169 未入选；本例对象/时间/事项三键自足，登记备查。
   - BYZ-106 台账 provenance 的 PDF 页注记 137 有误：实测占验一〇六在 PDF139（书页 125 无误；卷五区域 PDF 偏移由 +12 变 +14）。金标 page 按实测作「书页125（PDF139）」；edition 字段沿台账原文。
5. 构建中脚本两处解析规则当场修正并重跑（均为解析器问题、非数据问题）：断案课盘行过滤漏无天将地盘行→放宽规则；三传正则跨列误命中→改按每行末三 token 提取；断语对勘窗口改去标点后滑动 6 字。终版一次通过（输出：OK cards=40 gold=40）。

## 格式承继
输入卡体例承 holdout15（测字卡 attachments.character_written；六壬卡 attachments.课式原文＋chart_complete；断案卡承 holdout12 DA 卡 attachments 课盘原文/三传/月将/旬空/年命）。金标 schema 承既有 holdout 金标（测字行/六壬行两式）。holdout16 输入卡置于 `holdout16/inputs/`（与 holdout15 的同级 `holdout15-inputs/` 布局不同，按本轮任务书指定路径）。
