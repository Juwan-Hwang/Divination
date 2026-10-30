# inputs-dev12 · BUILD-MANIFEST（R39 §4.1 输入卫生剥离，数据角交付 2026-10-30）

- 底本：`benchmark/phase3/inputs-dev11/`（487 件 `.json`）；产出：本目录 487 件 `.json`＋本清单。
- 立项依据：`benchmark/phase3/runs/round39/PREREG.md` §4.1（输入卫生剥离，承 R38 盲测席自报 AS-304/AS-306 输入卡 provenance 自带断语线索）；逐字段准绳：`runs/round39/data-verify/INPUT-HYGIENE-SCAN.md` 强命中清单（15 卡／20 字段，形态 F1–F5）。
- 构建脚本：`runs/round39/data-verify/build_inputs_dev12_strip_r39.py`；逐字段原文→替换文登记：`runs/round39/data-verify/STRIP-LOG.md`；校验脚本：`runs/round39/data-verify/verify_inputs_dev12_strip_r39.py`。
- 落改方式：逐字复制底本后，仅对强命中 15 卡的 20 个命名字段作原文文本级替换（每处旧文本在文件内恰出现 1 次才许替换）；替换以中性出处著录保留纯著录信息（书名／作者／来源类型／页位编号本身），删除断语内容、结局事实、断语时点与结局日期；URL slug 直载断语者，url 字段改为中性占位注记「（链接略，标题含断语已剥离）」。题面字段零改动。其余 472 卡与底本逐字（SHA-256）一致。
- 弱命中 25 卡一律未动（保留理由见 PREREG §4.1 写死登记：主形态 W2 为 asked_at 日期反推注记，所引多为干支生克片段、不含吉凶断语，剥离反损题面）。
- diff（vs inputs-dev11）：**15 卡／20 字段**，全部落在扫描件强命中声明集内（F1 出处标题／URL 9 卡 13 字段、F2 页位条目 1 卡 1 字段、F3 setting 断语 3 卡 3 字段、F4 setting 结局 1 卡 1 字段、F5 asked_at／note 时点与日期 1 卡 2 字段）；逐卡清单见 STRIP-LOG.md。

## 口径切换登记

- 自 **R39** 起，输入口径为 **inputs-dev12**（PREREG §0 登记）；inputs-dev11 口径终止于 R38。
- 与 R38 读数的跨轮比较只作带宽内参考，输入变更事实已在 R39 PREREG §0 登记。
- 本切换**只作数据卫生、不包装增益**：剥离的是输入卡非题面字段内的断语／结局承载文本，非方法改进。

## 自验

- 文件数：inputs-dev12 内 `.json` **487** 件＋本清单 `BUILD-MANIFEST.md` 1 件；文件名集与 inputs-dev11 逐一相等（校验 (1) 通过）。
- 字段级核对：两目录 JSON 深比对，差异路径恰为 STRIP-LOG 登记的 20 个（卡，字段），无遗漏、无越界；字节级核查未登记 472 卡逐字一致、登记 15 卡均有差异（校验 (2) 通过）。
- 题面字段逐卡哈希不变（487/487）：题面字段集＝顶层标识键 id／uid／source_id＋subject 整树＋context.question＋context.attachments 课式本体（扣除 note／chart_note／source／secondhand／chart_excerpt）（校验 (3) 通过）。
- 剥离后字段断语残片复扫（25 个片段：胜方名、slug 关键词、断语原句、结局日期等）：命中 0（登记于 STRIP-LOG.md）。
