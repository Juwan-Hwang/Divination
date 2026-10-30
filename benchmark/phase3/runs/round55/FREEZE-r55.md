# FREEZE-r55（Round 55 盲测冻结记录）

冻结时点：2026-10-31（+08:00）。冻结范围：`runs/round55/predictions/` 487 件。

## 验盘（主持亲跑，盘上实测）

- `verify_predictions_host_r55.py` 输出：`want 487 files 487 missing [] extra [] bad []`；trigger 主持复算 changed_main＝68、reserve_used＝43、disputed＝77；`HOST VERIFY OK 487/487`（字段全齐、confidence 全在 0–1）。
- tradition 逐批复核（`check_tradition_host_r55.py`）：direct 365、none-labelled 114、flags 8。flags 8 件主持逐件裁定**全为格式变体、实质合规、不触发重测**：LY-002 卡面 system=liuyao、席位中文自述「卡面 system=liuyao；实际所用体系：六爻纳甲」与卡面一致（检查器以句式未命中计旗标）；WP-001–WP-007 卡面无 tradition/system 字段、席位以英文句「Card face carries no tradition/system field; system actually used: …」如实标注无标注并写明实际体系（检查器以中文定式未命中计旗标）。误标批为零。

## 路径误写事件与处置（本轮重大程序事项，全文入 ADDENDUM-r55，此处为冻结口径摘要）

- 本轮派单沿用相对路径 `runs/round55/`（实路径 `benchmark/phase3/runs/round55/`，PREREG §0 已注）。18 席自行定位实路径无误；7 席（B08、B11、B16、B18、B19、B25 及 B20）将相对路径误解为仓根 `~/workspace/divination/runs/round55/` 并在该处建目录写盘，共误写 127 件预测＋6 件写盘脚本；B20 另在正本目录有 20 件与误写件逐字节相同的同名件（写盘机制不予认定）。
- 主持发现后即发路径纠正令至全部在跑席位；未写错的席位（B06、B07、B10、B12、B13、B14、B15、B17、B21、B22、B23、B24 等）经自报与盘上双证未向误写目录写件，其正本件验收有效（B15 自报其脚本初稿曾含双目录写法但未运行、误写目录无 B15 件，盘上复核一致）。
- 处置口径（照 R42 误标先例「全新席全盲重测覆盖、原作废件移存留痕」）：误写七批（B08、B11、B16、B18、B19、B20、B25）**全批作废**，由七名全新席以绝对路径派单全盲重测，正本 487 件即重测后构成；冻结验盘以本记录为准。
- 作废件移存：误写树全件复制归档于 `runs/round55/voided-pathmixup-outside/round55/`（127 预测＋6 脚本，与原树 133/133 逐字节双读一致后，原树删除）；B20 正本作废 20 件移存 `runs/round55/voided-pathmixup-b20/`。全量 SHA-256 清单 `runs/round55/voided-sha256.txt`（153 行）随冻结提交存档。作废件不入评审、不计分，仅作程序留痕。

## 冻结后工序

冻结提交后建评审包（anon 种子 20261057）、派双视评审 8 席、分歧仲裁、平台定稿；W 监测第十八轮与数据议程并行，照 PREREG。
