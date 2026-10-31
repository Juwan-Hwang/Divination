# FREEZE-r87 — R87 平台盲测冻结验盘（主持）

- 验盘脚本：verify_predictions_host_r87.py（承 R86 体例适配，主持复算，盘上为准）；验盘输出 verify-predictions-host-r87.json。
- 完整性：want 487、实存 487、missing 0、extra 0、bad 0。
- trigger 主持复算（487 件）：changed_main＝26、reserve_used＝46、disputed＝55；reasons_nonempty＝244。须回填 analyze_r87.py 的 host_expected，定稿运行断言相等。
- tradition 初检候选 15 件，主持逐件回读首行＋输入卡字段裁定如下；声明组（claim group）候选 0 件；主持加扫（照录/原值类声称与卡面字段存在性及值一致性全量对勘）另得候选 2 件（BZ-021 已含于初检候选、OC-012 为未标注如实声明之误检，放行）。
- 冻结锚：kb-snapshot 与 R86 快照逐件零差异（21/21），平台新系列第 3 点与 R85/R86 同锚；六壬章冻结维持（SHA-256 a04697180dbee602dbcfacad6d493d9461c7bc8a249dea51022f45395514e89a）。

## tradition 旗标逐件裁定

- **检查器误报、不成立（14 件）**：BQ-017、BQ-018、BQ-020、BQ-021、BQ-022、BQ-023、BQ-024、BQ-025（卡面 tradition＝六爻，首行均逐字照录该值；命中之「未载／缺载」字面指月建、世爻地支、化出之支等盘面要素缺载，非 tradition 字段）；BZ-022、BZ-024、BZ-026、BZ-028（卡面 tradition＝bazi，首行逐字照录；「未载」指起运岁数未载）；LY-446（卡面 tradition＝liuyao，首行照录；「未見」出方法引文「疑者只見財動、未見其化」）；LR3-110（卡面无 tradition/system 字段，首行明写「卡面 tradition 未标注」属如实未标注声明，检查器以「卡面 tradition」子串误检）。
- **BZ-021（B03）——措辞不实，裁定部分成立，不作废不重测**：输入卡（inputs-dev12/BZ-021.json）顶层无 tradition/system 字段，basis 首行却作「tradition＝bazi（卡面 tradition 字段逐字照录——本卡载有 tradition 字段，值即 bazi）」，虚称卡面载有该字段。惟：① 标示值 bazi 与本例体裁及分段口径（host-meta）全等、实际作断体系为八字子平，方法实质无误、断语不受影响；② 该席回传自报与落盘文字一致（称 BZ-021 在照录组），无 R79 LY-022 真虚称之「回传自相矛盾」要件；③ 同例同型缺陷有 R67 判例在册（BZ-021 括号措辞不实只登记）。照 R67 同例判例与 R80 operative 口径（方法实质一致、断语不受影响）裁定部分成立，入本轮旗标定案流水待数据席 manifest 注记落实；冻结件即原件，不重测。
- 无误标批、无声明互斥，本轮冻结零补派。

## 席位过程登记（只登记，不改分数）

- 工具自动溢存 /tmp 三件只登记不归责（照 R75 口径）：B09、B24 各一件；B17 一件（读取输入卡时工具输出截断并自动溢存）；B14 自报一次 exec 输出截断，若伴随自动溢存同口径登记。
- 目录列示三件只登记：B07 为定位方法篇目对 kb-snapshot 及其 references 子目录执行 ls；B13 对 inputs-dev12 目录执行一次 ls；CYJ 锚点复核席开工时对 runs/round87 本轮目录做过一次列表查看（仅文件名，未涉 predictions/judging 内容、未作计数）。均未见禁读内容接触证据。
- B04 席所断 BZ-036/BZ-042/BZ-105 与 B08 席 LY-204 均属指令性字样本体基线例，卡面字样已按数据处理，只登记。
- LY-015（B07）与 LY-320（B11）各自独立作断，未参照他例；新鲜集组集排除此对不变。
- 25 批全部回收：各批逐件自验通过（JSON 可解析、五字段齐、case_id 与文件名一致、写盘断言例数与批额全等），无回传异常补派件。
