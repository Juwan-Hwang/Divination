# FREEZE-r85（R85 平台盲测冻结登记）

冻结时点：25 批盲测席（B01–B25）回传齐备后，主持全量验盘毕。方法快照＝runs/round85/kb-snapshot（新系列第 1 点，注记见 PREREG §1）。

## 验盘（verify_predictions_host_r85.py 盘上复算）

- 文件：want 487／实到 487／missing 0／extra 0／bad 0（字段、confidence 区间、trigger 结构、六爻限定、reason 非空规则全过）。
- trigger 主持复算（权威口径，席位自报数不采用）：changed_main **26**／reserve_used **44**／disputed **57**；reasons_nonempty 306。analyze_r85.py 的 host_expected 已按此回填。

## tradition 旗标初检与主持裁定（11 件候选）

检查器关键词集（繁简＋英文＋未见/未载＋「没有」变体）初检候选 11 件，逐件回读原卡（inputs-dev12）与 basis 首行裁定：

- **不成立（检查器误报）9 件**：BZ-104、BZ-105、BZ-301、BZ-302、BZ-303、LY-626——首行明载「卡面 tradition＝值」且与卡面逐字相符，仅措辞未中检查器型式；OC-003、OC-011、OC-014——卡面确无 tradition 字段，席位如实记阙如并按四柱题面自决八字，与卡面内容一致。
- **不成立（旗标不成立＋措辞不精确附注）2 件**：AS-009（卡面 tradition＝horary，席位误称「未见 tradition 字段」后自决 horary，与卡面一致）、AS-307（卡面 tradition＝astrology，席位误称「未标注 tradition 字段」后按题面自决占星向，与卡面一致）——与 R84 MH-001/003 同型：对卡面的陈述不精确，但方法自决结果与卡面值一致、无分数影响；交数据席按 PREREG §5.3 正式立条（类别承 ADDENDUM-r84 §八裁定）。
- tradition 真虚称：**0 件**，无作废重测。

## 声明组数加扫

basis 内 tradition 声明组数一致性加扫（claim group candidates）：**0**——无「通篇只用一组声明冒充逐例」件。

## 席位卫生登记

- B08、B11 两席自报：工具自动溢存把工具结果转储写入 /tmp（席位未主动使用 /tmp）——照 PREREG §6 只登记不归责席位，产物在盘核验无误。
- B25 席回传含对他批（B24）个例的旁注一条：不影响本轮数据（主持验盘覆盖全 487 件且全过），只登记不处置。
- 其余各席自报均无 /tmp 使用、无通配删除、无目录计数违规。

## 冻结结论

487 件预测冻结，进入评审建包（build_judge_packets_r85.py，种子 20261098）。
