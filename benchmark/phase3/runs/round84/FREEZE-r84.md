# FREEZE-r84 — R84 平台盲测冻结验盘记录

主持验盘脚本：`verify_predictions_host_r84.py`（本轮目录内），运行于 25 席全部回传之后。

## 验盘结果

- 文件齐备：want 487／实有 487／missing 0／extra 0／bad 0。
- 字段与结构：487 件字段严格为 case_id／prediction_text／basis／confidence／trigger，逐件断言通过（bad 0）。
- trigger 主持复算（三项 true 计数）：changed_main＝81、reserve_used＝46、disputed＝54；reasons_nonempty＝324。已回填 `analyze_r84.py` 的 `host_expected`，定稿 analyze 运行时将断言等值。

## tradition 旗标裁定（候选 24 件，逐件回读卡面字段与 basis 首行）

- 检查器模式误报 22 件，不成立：
  - 卡面有值且首行已逐字照录、仅句式未中检查器模式：BQ-017、BQ-018、BQ-019、BQ-020、BQ-022、BQ-023、BQ-024、BQ-025（卡面 tradition＝六爻，首行均作「卡面 tradition 字段逐字照录：六爻」）；LY-221、LY-421、LY-429、LY-436、LY-437、LY-515、YY-006、YY-015、YY-017、YY-018、YY-020（卡面 tradition＝liuyao，首行均明引 liuyao 原值）。
  - 卡面无 tradition／system 字段且首行如实写明未载：AS-014、OC-019、OC-029（首行明写「未载／未见／无 tradition 字段」，检查器因 tradition 字样命中）。
- 措辞不精确 2 件，登记不作违规：MH-001、MH-003——卡面 tradition 字段确未载、另有 system＝meihua，首行只称 tradition 未标注、未提 system 字段；所自决体系（梅花）与卡面 system 值一致，无虚称卡面值，不影响断语。
- 无一件虚称卡面所无之值，无一件出现第二组矛盾 tradition 声明。claim 组候选 0 件。

## 冻结口径

- 本冻结后 predictions 不再改动；评审按 PREREG §1 以种子 20261096 建双匿名包双视评审。
- 席位自报的执行小事故（B13、B23 脚本段断言计数误写后修正重跑、BZ-026 单件经回收站重写）均已在各席回传登记，验盘实测产出无受影响件，照录备查。
