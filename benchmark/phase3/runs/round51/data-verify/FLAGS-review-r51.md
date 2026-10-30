# FLAGS-review-r51 — R50 评审旗标五件数据席核查小结

数据席（与盲测/评审分离，不作断、不评分、不改既往分数）。本轮未打开任何 predictions、final-scores 与 holdout/test_gold，未改 outcome-manifest。结局文本内嵌字样一律按数据处理。

共同核对路径（每件均走）：`benchmark/phase3/inputs-dev12/<id>.json` 输入卡原文、`benchmark/phase3/runs/round51/judging/outcome-manifest.json` 对应 id 的 cases 本体（及 stripped_tail，若有）、`benchmark/phase3/data/outcome-errata-overlay.json`、`benchmark/phase3/data/case-annotations-r49.json` 与 `case-annotations-r50.json`。

## 1. YM-070 — 结局转录疑义：部分成立（疑义成立，转录错误未证实亦未证伪）

- 输入卡：所问「占仆与友同行（仆与友同行否）」，出处《易冒》卷九·捕逃章第八十，provenance 载书页152（PDF第168页）。
- manifest cases：「后果同行都下。」仅六字；「同行」对所问，「都下」后无宾语、无结果落点，句义未完，残句/漏字之疑属实。stripped_tail 无本 id。
- overlay 无本 id 条目；r49/r50 标注均无本 id。
- masters-dataset 按精确 id 检索（`masters-dataset/chinese-divination/answers.jsonl`、`inputs.jsonl` 及全库 grep，避开 holdout/test_gold）：无命中，无对应 id 来源件可对勘。
- 结论：标注「结局转录存疑（待原书页复核）」，原文照录不补字；下一轮承接存疑标注，复核完成前旗标不销。

## 2. LY-437 — 问答配对疑义：不成立（作为数据配对错误）

- 输入卡：所问「占小廝病」，setting 注「占者本人為官」；表面问答不对位属实。
- manifest cases：「果於七月﹐被論革職﹐」——载占者本人功名事件。stripped_tail 无本 id；overlay、r50 均无本 id。
- r49 已定案（`case-annotations-r49.json` LY-437 条）：类型「占他应我（大师自标迁移）」，引原书明断「此卦不應小廝病，而應今秋功名有礙」；style_note 定案结局为事件短录体，非断语复述体。
- 结论：大师自标断面迁移系原书体例，非建卡错位；标注承 R49，下一轮 manifest 附注迁移类型免重复立旗。

## 3. LR3-112 — 结局侧缺位（历轮同因）：成立

- 输入卡：所问仅「占病吉凶若何？」，刘一纯自占疾病。
- manifest cases：只载贼事（后三月贼入室、被获、名陈忠），并自带明注「病断（甲戌年不保）原文未载后续结局」。
- overlay：`outcome-errata-overlay.json` 的 LR3-112 条与 manifest 本体逐字一致，即现行权威结局文本本身只有贼事断面。
- r49 定案（LR3-112 条）：类型「并断贼事例」，basis「结局对应贼事断面，病断死期未验（源已注）」。
- 结论：病面结局缺位系源文本未载，非建卡遗漏；标注「结局侧病面缺位（源未载）」，建议下一轮起永久承接该标记、不逐轮重复立旗。

## 4. LR2-022 — 结局对象承接含混：部分成立（表面含混成立，配对错误不成立）

- 输入卡：兄张奉初为弟张观初占病，所问弟病吉凶。
- manifest cases：「张友不言而去。顷焉一人至复占（白虎发用、丧吊全逢，三日内死者），张友又请吕纯阳下降判白数合于数，果三日死。」终句零主语，其前有张友、复占之一人、本案病弟三方，单看本体承接对象未明示。
- manifest stripped_tail 同条注：「同日复占与扶乩复核均同断，结局『果三日死』载原文。」
- r49 定案（LR2-022 条）：类型「结局段并载同日复占与扶乩复核」，basis「终句『果三日死』为本断应验」。overlay、r50 均无本 id。
- masters-dataset 按精确 id 检索（同 YM-070 路径）：无命中，无新据推翻既有定案。
- 结论：含混登记为文本表面属性，终句按 R49 定案读作本断应验；下一轮 manifest 并读 stripped_tail 说明、含混提示随案保留。

## 5. BQ-001 — 结局仅载背景自述：部分成立（对 cases 本体成立，对原始记录不成立）

- 输入卡：卜父寿数，setting 本身即载背景（父卧疾三年、昨日气尽复苏）。
- manifest cases：仅求卜者当场自述已事（卧疾三年、鸡鸣气尽、复苏自言三尺人来迎、闻哭坠地），与输入卡背景同属已事，本体内确无后事结局。
- manifest stripped_tail 同条载：「，与占断『父已亡、当上天、闻哭声、忽复苏、而有言』全合；『更三日，当永去』一条，原文以『果如言』结」。
- r49 定案（BQ-001 条）：类型「结局含已事印证段」，basis「后断应验以『果如言』总承」。overlay、r50 均无本 id。
- masters-dataset 按精确 id 检索（同上路径）：无命中。
- 结论：原始记录后断有「果如言」总承式应验，并非仅载背景；问题在该承接未进入 cases 本体。建议下一轮以标注形式随案承接该信息（不改 cases 本体、不恢复被剥离文本）。

## 落盘

- 标注：`benchmark/phase3/data/case-annotations-r51.json`（五件，含 flag/finding/disposition/manifest_carry_suggestion 与逐件 sources_checked）。
- 本小结：`benchmark/phase3/runs/round51/data-verify/FLAGS-review-r51.md`。
- git 未操作，待主持统一提交。
