# FREEZE-r89 — R89 平台盲测冻结登记

## 冻结事实

- 盲测 13 席（B01+B02、B03+B04、B05+B06、B07+B08、B09+B10、B11+B12、B13+B14、B15+B16、B17+B18、B19+B20、B21+B22、B23+B24、B25）全回，主持全量验盘（verify_predictions_host_r89.py）通过：want 487、files 487、missing 0、extra 0、bad 0。
- trigger 主持复算：changed_main **36**、reserve_used **41**、disputed **56**；reason 非空 248 件。已回填 analyze_r89.py 之 host_expected，定稿 analyze 运行时须逐值相符。
- 声明组数加扫：claim group candidates **0**（无同文件互斥 tradition 声明）。

## tradition 旗标裁定（1 件）

- **OC-019**（检查器候选 kind=card_no_field_but_first_line_claims_card_value）：主持回读原卡与首行裁定——输入卡无 tradition/system 字段，basis 首行明写「卡面未标注 tradition 字段，本例据卡面四柱以八字自决」，检查器命中之「卡面所载」字面系指卡面所载四柱（癸巳丙辰壬申癸卯），非 tradition 值声称。**裁定：检查器误报，旗标不成立，不作废、不重测**（承 R74/R78 检查器误报判例：初检 flags 逐件回读核实后裁定）。

## 席位卫生自报裁记（2 件，均只登记）

1. **B09+B10 席**：曾对 inputs-dev12 目录执行一次 `ls | head`（非 runs/ 目录、非禁读内容，仅见文件名，未读清单外案例内容）。不触目录禁令（禁令对象为 runs/ 下目录），只登记备查，影响为零。
2. **B15+B16 席**：开工时对 round89 根目录执行过一次 `ls`（仅见顶层条目名，未打开、未读取 predictions/judging/final-scores/splits 中任何内容）。形式上触「禁止对任何 runs/ 目录列表」之规，实质未接触任何禁读内容，影响为零；照 R88 DIAG 席定位性目录列举判例只登记、不作废本批产出（本批 40 件经主持全量验盘格式与 id 集无误）。

## 方法状态

- 盲测读 runs/round89/kb-snapshot（与现行活 method 逐件全等）；现行干预仅 calibration 第八节（R80-REV1），各席 basis 留痕由诊断/附读面后续核查，本冻结不作执行面结论。

冻结后进入评审建包（build_judge_packets_r89.py）。
