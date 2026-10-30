# inputs-dev11 · BUILD-MANIFEST（R34 §6.③ 数据卫生·口径切换，数据角交付 2026-10-30）

- 底本：`benchmark/phase3/inputs-dev10/`（487 件 `.json`）；产出：本目录 487 件 `.json`＋本清单。
- 组集脚本：`benchmark/phase3/build_inputs_dev11_r34.py`（本批唯一新脚本，保留在案）。
- 立项依据：`benchmark/phase3/runs/round34/PREREG.md` §6.③（与方法轮分离的数据卫生立项，R34 分析定稿后执行）；纠正准绳：`benchmark/phase3/input-audit/CORRECTIONS.md`（6 例 A 类定案）；字段级证据：`input-audit/verify-V1.json`（LY-006、LY-010、LY-105）、`verify-V2.json`（YY2-001、YY2-002）、`verify-V3.json`（YY2-005）。构建前已断言 CORRECTIONS 与三份 verify 证据值逐项一致、无冲突。
- 落改方式：逐字复制底本后，仅对下 6 例作原文文本级替换（每处旧文本在文件内恰出现 1 次才许替换）；6 个改动文件内未改字段逐字不变，其余 481 件与底本逐字（SHA-256）一致。
- diff（vs inputs-dev10）：**6 例**，全部落在 CORRECTIONS 声明集内；其余 **481 例**逐字一致。

## 6 例逐例 diff（字段 · 旧值 · 新值 · 证据文件）

- LY-006 · 字段 `context.attachments.moving_lines` · 旧值「初爻父母子水○、四爻官鬼酉金○、五爻妻財未土ㄨ（世）動」· 新值「初爻父母子水○、四爻官鬼酉金○、五爻妻財未土ㄨ（世）動、上爻子孫巳火○動」· 补「上爻子孫巳火○動」、动位 [1,4,5]→[1,4,5,6] · 证据：CORRECTIONS.md 表 LY-006 行＋verify-V1.json（源本盘面与断语「巳火子動而生世」互证）· 改后 SHA-256 前 12 位 6900d4fbb352（底本 064900875b65）。
- LY-010 · 字段 `context.attachments.moving_lines` · 旧值「初爻官鬼巳火○、五爻父母未土ㄨ（世）動」· 新值「初爻官鬼巳火○、上爻父母未土ㄨ（世）動」· 动位 [1,5]→[1,6] · 证据：CORRECTIONS.md 表 LY-010 行＋verify-V1.json（源本盘面未土ㄨ世在上爻）· 改后 SHA-256 前 12 位 feac260a9e5e（底本 3f30c6fc3623）。
- LY-105 · 字段 `context.attachments.空亡` · 旧值「寅卯」· 新值「子丑」· 证据：CORRECTIONS.md 表 LY-105 行＋verify-V1.json（卡面 setting 自载「壬戌日（子丑空）」、壬戌属甲寅旬空子丑）· 改后 SHA-256 前 12 位 91a3cd35097c（底本 a84a7abf9c94）。范围注记：本次仅改 `attachments.空亡` 值字段；`notes.completion_grade` 中关于该字段补录依据的历史记录文字未改（属补录过程记录、非输入字段）。
- YY2-001 · 字段 `context.attachments.chart_lines_top_to_bottom`（全 6 爻，自上而下）· 旧值 官鬼丁丑土／父母丁酉金／妻财丁巳火 应／父母戊申金／官鬼戊辰土／子孙戊寅木 世 · 新值 兄弟戊子水／官鬼戊戌土／父母戊申金 应／官鬼丁丑土／子孙丁卯木／妻财丁巳火 世 · 按水澤節（坎宫一世）标准装卦逐爻改 · 证据：CORRECTIONS.md 表 YY2-001 行（纠正值见 V2）＋verify-V2.json `corrected_chart_top_to_bottom`（与新值逐字相等、脚本已断言）· 改后 SHA-256 前 12 位 c9c1828ebfc5（底本 694df2f96573）。
- YY2-002 · 字段 `context.attachments.chart_lines_top_to_bottom`（全 6 爻，自上而下）· 旧值 妻财戊午火 应／官鬼戊戌土／兄弟戊子水／子孙乙卯木 世／妻财乙巳火／官鬼乙未土 · 新值 父母癸酉金 应／兄弟癸亥水／官鬼癸丑土／妻财戊午火 世／官鬼戊辰土／子孙戊寅木 · 按地水師（坎宫歸魂）标准装卦逐爻改 · 证据：CORRECTIONS.md 表 YY2-002 行（纠正值见 V2）＋verify-V2.json `corrected_chart_top_to_bottom`（与新值逐字相等、脚本已断言）· 改后 SHA-256 前 12 位 dc609d743aca（底本 8bac61b65ee3）。
- YY2-005 · 字段 `context.attachments.chart_lines_top_to_bottom`（仅上三爻，自上而下为六爻／五爻／四爻）· 旧值 兄弟乙卯木／子孙乙巳火／妻财乙未土 世 · 新值 官鬼癸酉金／父母癸亥水／妻财癸丑土 世（下三爻 官鬼辛酉金／父母辛亥水／妻财辛丑土 应 不变）· 上卦坤误按内卦序装、改按外卦序癸酉亥丑 · 证据：CORRECTIONS.md 表 YY2-005 行＋verify-V3.json 三条 discrepancies（四爻妻财癸丑土 世、五爻父母癸亥水、六爻官鬼癸酉金）· 改后 SHA-256 前 12 位 5f4b40d6f348（底本 0f26003f5da1）。

## 口径切换登记

- 自 **R35** 起，输入口径为 **inputs-dev11**（本目录）；inputs-dev10 口径终止于 R34。
- **一切合读池资格重置**：R33/R34 依「inputs-dev10 与前轮逐字不变」成立的合读关系**终止于 R34**，不延伸至 inputs-dev11；R35 起任何合读资格须按新口径另行预注册声明。
- 本切换**只作数据卫生、不包装增益**：6 例均为输入转录/复原错误的勘误落改，非方法改进；其收益上限约 +0.10 且存疑（R34 PREREG §6.③ 在案），不得引作方法增益证据。
- 本立项与方法轮分离：未改动 `method/` 与任何 `runs/` 目录，未改动 inputs-dev10 任何文件；本轮（R34）一切读数与判据不受本切换影响。

## 自验

- 文件数：inputs-dev11 内 `.json` **487** 件＋本清单 `BUILD-MANIFEST.md` 1 件；文件名集与 inputs-dev10 逐一相等。
- 逐文件比对方法：对 inputs-dev10 与 inputs-dev11 同名 `.json` 逐一计算 SHA-256 全等判定（脚本 `build_inputs_dev11_r34.py` 自验 2）。结果：**恰 6 件不同**（即上 6 例）、**其余 481 件逐字一致**。
- 字段级核对：6 件改后经 JSON 深比对，差异路径恰落在声明字段内（LY-006/LY-010 为 `moving_lines`、LY-105 为 `空亡`、YY2 三例为 `chart_lines_top_to_bottom`），无越界改动；改后值与 CORRECTIONS/verify 证据值逐项相等（构建前两源一致性断言＋构建后语义断言均通过）。
- 与 CORRECTIONS.md 逐条对应：6 行表格（LY-006、LY-010、LY-105、YY2-001、YY2-002、YY2-005）与上 diff 登记一一对应，无遗漏、无额外例。

