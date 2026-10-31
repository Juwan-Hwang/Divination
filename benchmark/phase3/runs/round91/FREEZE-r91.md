# FREEZE-r91 — R91 平台盲测冻结登记

日期：2026-11-01（Asia/Shanghai）。主持全量验盘（runs/round91/verify_predictions_host_r91.py）实测：

- 完整性：want 487／files 487／missing 0／extra 0／bad 0（字段齐全、JSON 可解析、confidence 全在 0–1、trigger 三布尔类型全合）。
- trigger 主持复算：changed_main **36**、reserve_used **39**、disputed **53**（reason 非空 195）。analyze 的 host_expected 回填为此三值。
- tradition 初检：候选旗标 **38 件**（见下裁定）；声明互斥组加扫（CLAIM declaration groups）**0 件**。

## tradition 旗标裁定（38 件）

- **LY-007**（检查器类：card_has_field_but_first_line_unmarked）：主持回读原卡与 prediction 首行裁定——原卡顶层实载 `tradition: 'liuyao'`（卡键集 context／provenance／subject／tradition／uid），R91 prediction basis 首行作「卡面未标注 tradition/system 字段，按题面体裁自决」，**与卡面实载不符、措辞不实成立**；但该例实际作断体系为六爻纳甲（首行自注「六爻纳甲卦盘俱全，用六爻」，与卡面 tradition 一致），无体系误标、无虚构卡面值。裁定：**部分成立**——不作废、不重测（与 R90 AS-009 同型同裁），登记入本轮数据议程（平台面新定案候选：部分成立），manifest 承接建议由数据席按体例编制。
- **余 37 件全数裁定检查器语境误报、不成立**：形态分三类——(i) 首行逐字照录卡面值后另述他字段未载（LY-402–425 等 17 件之「未载 yongshen 与空亡字段」指 attachments 字段、非 tradition；BQ-024、LY-503、YM-004、YM-055、YM-063、YY-006、YY2-005 同型）；(ii) tradition 字段实缺、system 字段实载且首行如实分述两字段状态（LY-010、LY-011、LY-014、LY-016、LY-024、LY-025、LY-031、LY-033、LY-036、MH-001、MH-003 共 11 件，首行明载「卡面另载 system＝…」）；(iii) 卡面实无 tradition/system 而首行明述核过无值（BZ-021，检查器「卡面 tradition」字面模式误命中否定句）。逐件经主持回读首行＋卡面字段核实，承 R78 判例口径。

## 席位卫生登记

- 13 席回传均无意外接触禁读内容自报；无 /tmp 使用自报。紫微供给首批第一席（非平台线）曾自报 grep 副带命中金标文件两行（与其三例无关、未用作判定），登记于 ADDENDUM-r91，不涉平台冻结件。
- 各席数据面旗标（卡面残损/自注类）汇总转数据席定案流水（编号条目在各席回传中，数据席逐件回原卡核对）。

冻结提交后打标签 `phase3-round91-blind-frozen`。冻结后 predictions 不再改动；评审建包（build_judge_packets_r91.py，种子 20261109）只读冻结件。
