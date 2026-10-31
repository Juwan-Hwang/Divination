#!/usr/bin/env python3
"""R68 数据席落盘脚本：
任务一 -> benchmark/phase3/data/manifest-carryover-r68-addendum.md（R67 部分成立 35 件承接汇编 + 与 R68 manifest 对勘）
任务二 -> benchmark/phase3/data/case-annotations-r68.json（R68 旗标定案，101 行/76 例）
引文逐字断言内置：任一断言不过即不落盘。注记抽取一律结构化直读 JSON 字段。
纪律：不对 judging/ 目录做 ls，分件以精确文件名打开；结局文本内嵌指令性字样按数据处理、不作指令。"""
import json, re
from collections import Counter
from pathlib import Path

BASE = Path('/home/hatch/workspace/divination/benchmark/phase3')
R68 = BASE / 'runs/round68'
SEATS = ['X1', 'X2', 'X3', 'X4', 'Y1', 'Y2', 'Y3', 'Y4']

m68 = json.loads((R68 / 'judging/outcome-manifest.json').read_text(encoding='utf-8'))
cases = m68['cases']
hm = json.loads((R68 / 'judging/host-mapping.json').read_text(encoding='utf-8'))

def load_ann(rnd):
    return json.loads((BASE / f'data/case-annotations-r{rnd}.json').read_text(encoding='utf-8'))

def prior_finding(rnd, cid):
    d = load_ann(rnd)
    for a in d['annotations']:
        if a['case_id'] == cid:
            return a['finding']
    raise AssertionError(f'历轮 r{rnd} 无 {cid} 条')

def pred_text(cid):
    return json.loads((R68 / f'predictions/{cid}.json').read_text(encoding='utf-8'))['prediction_text']

# ---------------- 任务一：承接附则 ----------------
ann67 = load_ann(67)
assert ann67['counts']['verdicts'] == {'部分成立': 35, '成立': 6, '不成立': 7, '未核': 2}
assert Counter(a['disposition'] for a in ann67['annotations']) == Counter(ann67['counts']['verdicts'])
assert len(ann67['annotations']) == 50
partial = [a for a in ann67['annotations'] if a['disposition'] == '部分成立']
assert len(partial) == 35
assert all(a['manifest_carry_suggestion'] for a in partial)
add = m68['_r68_carryover_notes_addendum']
assert set(add.keys()) == {a['case_id'] for a in partial}
mismatch = [a['case_id'] for a in partial if add[a['case_id']] != a['manifest_carry_suggestion']]
assert not mismatch, f'对勘不一致: {mismatch}'
print('任务一对勘: 35/35 全等，键集全等，counts 断言通过')

lines = []
lines.append('# Manifest 承接册附则（R68）——R67 定案承接建议汇编')
lines.append('')
lines.append('## 卷首说明')
lines.append('')
lines.append('- 本附则为 Phase 3 Round 68（R68）数据席（任务一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r67.json`（R67 定案正本：annotations 50 件，定案分布成立 6／部分成立 35／不成立 7／未核 2）。')
lines.append('- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 6／部分成立 35／不成立 7／未核 2、总 50，与任务给定分布逐项一致；部分成立 35 件每件 `manifest_carry_suggestion` 非空断言亦通过。')
lines.append('- 对勘结果：35/35 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round68/judging/outcome-manifest.json` 的 `_r68_carryover_notes_addendum` 层（本席只读该层与 `cases` 键名集），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 0 件）。')
lines.append('- **本附则自 R69 manifest 起落实**；本轮（R68）manifest 不据本附则改动。')
lines.append('- **本件只汇编与对勘，不改任何分数与结局原文。**')
lines.append('- 汇编范围：R67 定案中部分成立 35 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r67.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R68 起」等表述为原档原文，落实轮次按卷首上一条读作自 R69 起，不回溯改动 R68）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。')
lines.append('- 成立 6／不成立 7／未核 2 共 15 件不入正文逐件节，只在文末列 case_id 清单。')
lines.append('- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 一、部分成立件承接汇编（定案档位：部分成立，35 件，逐件全列）')
lines.append('')
for i, a in enumerate(partial, 1):
    assert a['manifest_carry_suggestion']
    lines.append(f"### A{i}. {a['case_id']}")
    lines.append('')
    lines.append(f"- case_id：{a['case_id']}")
    lines.append(f"- anon_id：{a['anon_id']}")
    lines.append(f"- 定案（部分成立）：{a['finding']}")
    lines.append(f"- 原旗标要旨（照原档 `flag` 字段）：{a['flag']}")
    lines.append(f"- 承接注记建议文本（照原档 `manifest_carry_suggestion` 原文）：「{a['manifest_carry_suggestion']}」")
    lines.append(f"- 与既有承接册／附则条目的关系（照原档 `relation` 字段）：{a['relation']}")
    lines.append('')
lines.append('---')
lines.append('')
lines.append('## 对勘记录')
lines.append('')
lines.append('- 对勘对象：本汇编第一节 35 件承接注记建议文本（源：`case-annotations-r67.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round68/judging/outcome-manifest.json` 的 `_r68_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。')
detail = '、'.join(f"{a['case_id']}＝一致" for a in partial)
lines.append(f'- 对勘结果：35 件逐字一致，差异 0 件（对勘明细：{detail}）。')
lines.append('- 键集合差异：无（manifest 层 35 键与部分成立 35 件 case_id 集合全等）。')
lines.append('- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。勘误结论：无须勘误；本附则结论自 R69 manifest 起落实。')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 自验')
lines.append('')
lines.append('- 原档（case-annotations-r67.json）条目数：50；档位分布成立 6／部分成立 35／不成立 7／未核 2，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。')
lines.append('- 本附则正文条目数：35（第一节部分成立 35 件），与原档部分成立件数对齐；文末不入附则清单 15 件（成立 6＋不成立 7＋未核 2），35＋15＝50 与原档总数对齐。')
lines.append('- 承接注记建议文本：35 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R68 manifest `_r68_carryover_notes_addendum` 逐件逐字一致（35／35）。')
lines.append('- 回读断言：本附则写出后由生成脚本回读，断言第一节条目数＝35、每件承接注记建议文本与原档字段逐字一致（结果见产出时回读记录：通过）。')
lines.append('- 纪律自报：本席只汇编与对勘，未改任何分数、未改 manifest、未改 annotations、未改原卡；outcome-manifest 只读 `_r68_carryover_notes_addendum` 层与 `cases` 键名集（另为续接前提核对 cases 与 R67 逐件全等 487/487，只读）。')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 文末清单：不入附则 15 件（成立 6＋不成立 7＋未核 2，仅列 case_id）')
lines.append('')
for verdict in ['成立', '不成立', '未核']:
    ids = [a['case_id'] for a in ann67['annotations'] if a['disposition'] == verdict]
    lines.append(f"### {verdict} {len(ids)} 件")
    lines.append('')
    for cid in ids:
        lines.append(f'- {cid}')
    lines.append('')
addendum_text = '\n'.join(lines)
out_add = BASE / 'data/manifest-carryover-r68-addendum.md'
out_add.write_text(addendum_text, encoding='utf-8')
back = out_add.read_text(encoding='utf-8')
assert back.count('### A') == 35
for a in partial:
    assert f"「{a['manifest_carry_suggestion']}」" in back
print('任务一落盘 + 回读断言通过:', out_add)

# ---------------- 任务二：R68 旗标定案 ----------------
def parse_flags_text(text):
    rows = []
    for line in text.splitlines():
        mm = re.match(r'- (P3-[0-9a-f]+)：(.*)$', line)
        if mm:
            rows.append((mm.group(1), mm.group(2)))
    return rows

per_seat = {}
for s in SEATS:
    per_seat[s] = parse_flags_text((R68 / f'judging/FLAGS-{s}.md').read_text(encoding='utf-8'))
flag_rows = [(s, anon, flag) for s in SEATS for anon, flag in per_seat[s]]
assert len(flag_rows) == 101
uniq = {}
for s, anon, flag in flag_rows:
    uniq.setdefault(anon, []).append((s, flag))
assert len(uniq) == 76

# 定案规格（续接类）：anon -> (verdict, recent_round, outcome_quote)
SPEC = {
 'P3-13d0ce5e': ('部分成立', 67, '一一皆是'),
 'P3-16f31ce8': ('成立', 67, '盡覆沒'),
 'P3-2974ed8f': ('部分成立', 67, '我死，有三尺人来迎'),
 'P3-3238a1bf': ('部分成立', 67, '儿妇妊性别如断'),
 'P3-3da58e61': ('部分成立', 67, '直至戊寅年甲子月癸卯日故'),
 'P3-3e54858e': ('部分成立', 67, '驚險異常'),
 'P3-438bfa0e': ('不成立', 67, '次日卽愈'),
 'P3-46bac0c5': ('成立', 67, '被論革職'),
 'P3-4b59db5a': ('部分成立', 66, '天则亢旱难用矣'),
 'P3-515a56d5': ('部分成立', 67, '城破与官府一同被害，'),
 'P3-57245a7a': ('未核', 67, '果于申予日归'),
 'P3-57ea57c3': ('部分成立', 67, '老友夫妇告知'),
 'P3-5cb016ce': ('部分成立', 64, '果三日死'),
 'P3-6504c747': ('部分成立', 66, '不能相害'),
 'P3-6c42ee65': ('成立', 64, '死於丑年'),
 'P3-6dd0d159': ('部分成立', 67, 'within lesse three weekes'),
 'P3-72ec80da': ('部分成立', 67, '後於申年升任'),
 'P3-738eb626': ('部分成立', 67, '文書實收俱到'),
 'P3-749b93ce': ('部分成立', 67, '沈屙復起'),
 'P3-7814bf5d': ('部分成立', 64, '卒年不详于本数据集所据来源'),
 'P3-79327e4c': ('成立', 66, '後果在外平安'),
 'P3-7efa8d14': ('部分成立', 64, '果於午年保舉'),
 'P3-82adec1f': ('不成立', 67, 'a matter of historical record'),
 'P3-858dacd7': ('部分成立', 66, '后逢亥令解组'),
 'P3-87debd57': ('部分成立', 66, '中途过害'),
 'P3-9b8fffca': ('部分成立', 67, '直至戊寅年戊午月壬戌日故'),
 'P3-9d997362': ('部分成立', 67, '果有金弟屬猴'),
 'P3-a0b0c16a': ('部分成立', 67, '放火燒村而去'),
 'P3-a3f17d63': ('部分成立', 67, 'she died the eighth of October'),
 'P3-a55c8b05': ('部分成立', 64, '接受手术'),
 'P3-ae1875a1': ('部分成立', 67, '果死於卯日'),
 'P3-aeba44f1': ('成立', 67, '在午年子月而死'),
 'P3-bcde8edc': ('部分成立', 67, '病断（甲戌年不保）原文未载后续结局'),
 'P3-c2ef12d8': ('部分成立', 67, '沒有中榜'),
 'P3-c3d45b6a': ('部分成立', 67, '報出行文拿問'),
 'P3-c3d6b6e1': ('部分成立', 67, '后果然'),
 'P3-e9042f3c': ('成立', 66, '丑年得蠱病而終'),
 'P3-ea1accd8': ('成立', 67, '因子賭博送官'),
 'P3-fa14535c': ('成立', 67, '服補藥太過'),
 'P3-06129ded': ('未核', 67, '后果同行都下'),
 'P3-0b207991': ('部分成立', 64, '次日曰愈'),
 'P3-111eaf2c': ('部分成立', 67, '遊川廣'),
 'P3-17a0a698': ('部分成立', 67, 'the 27th of April'),
 'P3-1e0afe00': ('部分成立', 67, '三客至、内有杨姓'),
 'P3-2dd6eaf9': ('部分成立', 64, '合葬於他處'),
 'P3-2dff83a0': ('成立', 64, '此子未年而死'),
 'P3-37568e9f': ('部分成立', 64, '果然如是'),
 'P3-430cdef8': ('部分成立', 64, '果應於寅年'),
 'P3-4a682ef4': ('部分成立', 64, '早見木日得財'),
 'P3-62b70aa4': ('部分成立', 67, '伐樹起公榭'),
 'P3-8c730836': ('成立', 67, '果於八月其子驚風'),
 'P3-998f74bc': ('部分成立', 63, '1985年卒于纽约'),
 'P3-9e22eeab': ('部分成立', 67, '群蜂满身攒聚'),
 'P3-acb781dd': ('部分成立', 66, '后果然'),
 'P3-ba26b6b9': ('部分成立', 66, '勿以此斷'),
 'P3-bd00bfe2': ('部分成立', 67, '退位'),
 'P3-cb9ddc27': ('部分成立', 66, '5-6月恢复正常'),
 'P3-d2443a9b': ('部分成立', 64, '後報升於巳月'),
 'P3-d2fc8cec': ('部分成立', 67, '网友后回报'),
 'P3-d5240896': ('部分成立', 66, '果一一無錯'),
 'P3-dbfa6d80': ('部分成立', 67, '覆舟而亡'),
 'P3-de3e5fb9': ('部分成立', 67, '存貨堆積四年'),
 'P3-dfa904fd': ('部分成立', 64, '果於子時退災'),
 'P3-dfd5a3c4': ('部分成立', 64, '亥月甲辰日'),
 'P3-e696314e': ('部分成立', 64, '无气象记录佐证'),
 'P3-ef5705d2': ('部分成立', 64, '冲实用神'),
 'P3-f491ecc9': ('成立', 66, '父子相逢'),
 'P3-f736629b': ('成立', 66, '果至巳月而生惡瘡'),
 'P3-fe2dd62b': ('部分成立', 64, '所請準'),
}
# 续接件附加层注记（同例附加层核后属实/已定案，与主旨并行登记、档位不变）
EXTRA = {
 'P3-6dd0d159': '另本轮 X2 旗标兼及 R66 同例新旨（结局时点表述内嵌版本校勘注记）一层：该旨 R66 已定案部分成立、与本旨各旨独立、并行不悖，本轮一并承接、档位不变。',
 'P3-13d0ce5e': '另本轮 X1 旗标兼及 prediction 自注一层（卡面逐爻表 OCR 行序曾错乱、仅据可互证资讯作断、置信已降）——逐字核 R68 prediction 全文（「卡面逐爻表註明OCR行序曾錯亂」）属实且已自注，与本旨并行登记、档位不变。',
 'P3-c3d6b6e1': '另本轮 Y3 旗标兼及卡面动爻记载自相矛盾一层——逐字核 R68 prediction 全文（「卡面动爻记载自相矛盾（原文称寅官动与装卦父母巳火动不合），盘面存疑」）属实且已自注，与本旨（总承式结局）并行登记、档位不变。',
}
assert set(SPEC.keys()) | {'P3-024a8581', 'P3-09c17063', 'P3-0f60e80a', 'P3-58ebbdfe', 'P3-8c72bc76', 'P3-b5b44f93', 'P3-658f01dd'} == set(uniq.keys()), 'SPEC+自裁件与去重 anon 集合不合'
assert not (set(SPEC.keys()) & {'P3-024a8581', 'P3-09c17063', 'P3-0f60e80a', 'P3-58ebbdfe', 'P3-8c72bc76', 'P3-b5b44f93', 'P3-658f01dd'})

CUSTOM_BASIS = {
 'P3-024a8581': '新旗标（R68 新立）：回原卡——所问袖帨中包何物（射覆）；R68 prediction 正文自载「卡面三传后二传天干未载、旬空未载，输入残损，置信低」，basis 亦同旨，原卡 attachments 三传条自注「[天干未载，两本字面相同]」、空亡条作「原书未载旬空」——残损属实一层；但残损已在卡面与 prediction 双处明示、prediction 已降置信交付，射覆主断与结局（是牛黄二块）对应面完整可核。故部分成立（同 YY2-004／OC-009 残损双示口径）。',
 'P3-09c17063': '新旗标（R68 新立）：回原卡——所问占师近病；原卡 attachments.yongshen 作「应上巳火财爻（师病以应为用）」，而 chart_lines_top_to_bottom 载父母申金临应、妻财巳火临世，巳火实在世位非应位——卡面用神文字与盘面世应标记有一处不合属实，R68 prediction basis 已自注此出入（「卡面用神文字与盘面世应标记有一处不合」）并降置信；但取用实质（以巳火财爻为师病之用）未改、主断（近病可愈）与结局（寅日乃愈）对应完整。故部分成立。',
 'P3-0f60e80a': '同例新旨（R64 旧旨为『prediction 为占星师群体押注分布、结局只载选举结果未载押注分布』、定案不成立，本轮新旨与之各旨独立、并行不悖）：回 R68 prediction 全文——正文自载「题面无盘面附件，输入残损，只作方向断并明示与群体表态分歧」，basis 亦明注「输入残损——无盘附件」——残损属实一层；但残损已自注，方向断（特朗普赢得大选）与结局（特朗普以明确优势胜出）对应完整。故部分成立。',
 'P3-58ebbdfe': '新旗标（R68 新立，核后不成立）：回本例 R68 manifest 结局原文逐字核——结局作「此人自二十五歲至五十多歲東奔西走﹐一事無成﹐後因貧困﹐從戒外出。」，「五十多歲」完好可读；且 manifest 全档原始字节无 U+FFFD 替换字符，旗标所指「五�多歲」残损替换字样不存在。故不成立。',
 'P3-8c72bc76': '新旗标（R68 新立，核后不成立）：回原卡——YM-060 所问「占升方（升任何地）」；R68 manifest 本例结局为「后擢西北。」，升方一面直接明载，全文无母病、无惊风字样；旗标所述「结局未载母病终局、转录其子八月惊风」逐点对应 LY-023 结局（「果於八月其子驚風（其後復占子病，見 LY-024）」），且两例 anon 形近（P3-8c72bc76／P3-8c730836，同首缀 P3-8c7）。LY-023 本轮已由 Y3 以其本例 anon 立旗同旨、按同旨续接（R67）定案成立，不因本件改动。本件旗标所述内容不在映射例文本内，疑为席位 anon 错配。故不成立（错配登记另见特别核查②）。',
 'P3-b5b44f93': '新旗标（R68 新立）：回原卡——所问占援例（捐纳）入仕可否；R68 prediction 断「援例可成而遲、過程反覆」，manifest 结局「後竟納之﹐名敗身喪。」——「納之」明载，援例成面与 prediction 成向直接对应、非错面他事，旗标错面之指不全立；但结局未载成之迟速与应期（申日）面、迟面无从核验，且「名敗身喪」后果面为 prediction 未断之附加记载，所指成色一层属实。故部分成立。',
}
CUSTOM_RELATION = {
 'P3-024a8581': '新旗标（R68 新立）',
 'P3-09c17063': '新旗标（R68 新立）',
 'P3-0f60e80a': '同例新旨（R64 旧旨旗标不成立、本轮新旨另立）',
 'P3-58ebbdfe': '新旗标（R68 新立，核后不成立）',
 'P3-8c72bc76': '新旗标（R68 新立，旗标内容错配、核后不成立）',
 'P3-b5b44f93': '新旗标（R68 新立）',
 'P3-658f01dd': '同旨续接（R66）',
}
CUSTOM_CARRY = {
 'P3-024a8581': '同旨新立：自 R69 起承接本 R68 标注：按「卡面三传后二传天干未载、旬空未载，残损已于卡面与 prediction 双示」登记；结局原文照录不改。',
 'P3-09c17063': '同旨新立：自 R69 起承接本 R68 标注：按「卡面用神文字（应上巳火）与盘面世应标记（巳火临世）一处不合、已自注降置信」登记；结局原文照录不改。',
 'P3-0f60e80a': '同例新旨：自 R69 起承接本 R68 标注（与 R64 旧旨定案并行、各旨独立）：按「题面无盘面附件、输入残损已自注，方向断与结局对应完整」登记；结局原文照录不改。',
 'P3-58ebbdfe': '不入附则：本 R68 新立定案（不成立），自 R69 起承接本 R68 标注，不加承接注记；结局原文照录不改。',
 'P3-8c72bc76': '不入附则：本 R68 错配登记定案（不成立），自 R69 起承接本 R68 标注，不加承接注记；LY-023 既有定案（同旨续接 R67 成立）照旧承接、不因本件改动；结局原文照录不改。',
 'P3-b5b44f93': '同旨新立：自 R69 起承接本 R68 标注：按「结局『納之』明载对应援例成面、迟速与应期面未载」登记；结局原文照录不改。',
 'P3-658f01dd': '同旨续接：自 R69 起承接 R66＋本 R68 标注；结局原文照录不改。',
}
CUSTOM_CATEGORY = {
 'P3-024a8581': 'prediction 自载卡面残损（三传后二传天干未载、旬空未载，已自注降置信）',
 'P3-09c17063': '卡面用神文字与盘面世应标记一处不合（已自注降置信）',
 'P3-0f60e80a': '同例新旨：prediction 自载题面无盘面附件、输入残损（已自注）',
 'P3-58ebbdfe': '新旗标：结局残损替换字符之指核后不存在',
 'P3-8c72bc76': '新旗标：旗标内容错配（所述属 LY-023、本例核后不成立）',
 'P3-b5b44f93': '断语与结局疑错面（核后成面对应、迟面未载）',
 'P3-658f01dd': '同旨续接（详见核查事实）',
}
CUSTOM_VERDICT = {
 'P3-024a8581': '部分成立', 'P3-09c17063': '部分成立', 'P3-0f60e80a': '部分成立',
 'P3-58ebbdfe': '不成立', 'P3-8c72bc76': '不成立', 'P3-b5b44f93': '部分成立',
 'P3-658f01dd': '部分成立',
}
CUSTOM_KIND = {
 'P3-024a8581': 'new', 'P3-09c17063': 'new', 'P3-0f60e80a': 'newgist',
 'P3-58ebbdfe': 'new', 'P3-8c72bc76': 'new', 'P3-b5b44f93': 'new',
 'P3-658f01dd': 'cont',
}

flags_out, ann_out = [], []
counts_kind = Counter()
for anon, seat_flags in uniq.items():
    cid = hm[anon]
    assert cid in cases
    seats = [s for s, _ in seat_flags]
    flag_joined = '；'.join(f'{s}：{f}' for s, f in seat_flags)
    sources = [
        f'benchmark/phase3/inputs-dev12/{cid}.json',
        'benchmark/phase3/runs/round68/judging/FLAGS-selfreported-r68.md',
        f'benchmark/phase3/runs/round68/judging/outcome-manifest.json cases[{cid}]',
        f'benchmark/phase3/runs/round68/predictions/{cid}.json',
    ]
    if anon in SPEC:
        verdict, recent, quote = SPEC[anon]
        kind = 'cont'
        counts_kind[kind] += 1
        pf = prior_finding(recent, cid)
        basis = (f'承接既有定案不重裁（历轮最近定案 R{recent} {verdict}）：{pf}'
                 f' 本轮（R68）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。')
        if anon in EXTRA:
            basis += EXTRA[anon]
        relation = f'同旨续接（R{recent}）'
        category = '同旨续接（详见核查事实）'
        if cid == 'YM-070':
            carry = '同旨续接（未核维持）：自 R69 起承接历轮标注：按「结局措辞待核（『都下』语义未明）」登记，与『甲寅旬』出处待核并列；结局原文照录不改、不补字，无盘外独立史源不裁。'
        elif cid == 'LY-537':
            carry = '待核维持：自 R69 起承接 R56／R57／R61／R64＋本 R68 登记：按「结局『果于申予日归』措辞待核、日期干支不明」登记；无盘外独立史源（原书页文本）前不裁；结局原文照录不改。'
        elif verdict == '部分成立':
            carry = f'同旨续接：自 R69 起承接 R{recent}＋本 R68 标注；结局原文照录不改。'
        else:
            carry = f'不入附则：本 R68 同旨续接定案（{verdict}），自 R69 起承接本 R68 标注，不加承接注记；结局原文照录不改。'
        assert quote and quote in cases[cid], f'{cid} 引文断言失败: {quote}'
        for r in range(49, 68):
            p = BASE / f'data/case-annotations-r{r}.json'
            if p.exists():
                d = json.loads(p.read_text(encoding='utf-8'))
                if any(a['case_id'] == cid for a in d.get('annotations', [])):
                    sources.append(f'benchmark/phase3/data/case-annotations-r{r}.json {cid} 条')
    elif anon == 'P3-658f01dd':
        # LR2-016：本轮旗标回指历轮同旨（editor_note 注记层），最近同旨定案 R66 部分成立；
        # R67 同例另一旗标（错配）定案不成立与本旨并行不悖。
        verdict = CUSTOM_VERDICT[anon]
        kind = CUSTOM_KIND[anon]
        counts_kind[kind] += 1
        pf = prior_finding(66, cid)
        basis = (f'承接既有定案不重裁（历轮最近同旨定案 R66 部分成立）：{pf}'
                 f' 本轮（R68）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨；'
                 f'本轮 X2 旗标兼及 editor_note 指令性字样一层（「评分时该细项请按未完全复核处理」存于分列 editor_note、不在 cases 本体），各席与本席均按数据处理未采纳，归属登记另见特别核查③；'
                 f'R67 同例另一旗标（内容错配）定案不成立与本旨并行不悖、照旧登记。')
        relation = CUSTOM_RELATION[anon]
        category = CUSTOM_CATEGORY[anon]
        carry = CUSTOM_CARRY[anon]
        lr = m68['_r56_lr2016_split']
        assert lr['case_id'] == 'LR2-016' and '评分时该细项请按未完全复核处理' in lr['editor_note']
        assert '评分时' not in cases['LR2-016'] and '依拟脱离' in cases['LR2-016']
        for r in range(49, 68):
            p = BASE / f'data/case-annotations-r{r}.json'
            if p.exists():
                d = json.loads(p.read_text(encoding='utf-8'))
                if any(a['case_id'] == cid for a in d.get('annotations', [])):
                    sources.append(f'benchmark/phase3/data/case-annotations-r{r}.json {cid} 条')
    else:
        verdict = CUSTOM_VERDICT[anon]
        kind = CUSTOM_KIND[anon]
        counts_kind[kind] += 1
        basis = CUSTOM_BASIS[anon]
        relation = CUSTOM_RELATION[anon]
        category = CUSTOM_CATEGORY[anon]
        carry = CUSTOM_CARRY[anon]
        if anon == 'P3-024a8581':
            assert '三传后二传天干未载、旬空未载' in pred_text(cid)
            card = json.loads((BASE / f'inputs-dev12/{cid}.json').read_text(encoding='utf-8'))
            assert '天干未载' in card['context']['attachments']['三传'] and '原书未载旬空' in card['context']['attachments']['空亡']
        elif anon == 'P3-09c17063':
            assert '卡面用神文字与盘面世应标记有一处不合' in pred_text(cid)
            card = json.loads((BASE / f'inputs-dev12/{cid}.json').read_text(encoding='utf-8'))
            att = card['context']['attachments']
            assert '应上巳火财爻' in att['yongshen']
            assert '父母申金⚋应' in att['chart_lines_top_to_bottom'] and '妻财巳火⚊世' in att['chart_lines_top_to_bottom']
        elif anon == 'P3-0f60e80a':
            assert '题面无盘面附件，输入残损' in pred_text(cid) and '特朗普以明确优势胜出' in cases[cid]
            sources.append('benchmark/phase3/data/case-annotations-r64.json AS-307 条')
        elif anon == 'P3-58ebbdfe':
            assert '五十多歲' in cases[cid]
            assert b'\xef\xbf\xbd' not in (R68 / 'judging/outcome-manifest.json').read_bytes()
        elif anon == 'P3-8c72bc76':
            assert cases[cid] == '后擢西北。' and '驚風' not in cases[cid] and '驚風' in cases['LY-023']
            assert hm['P3-8c730836'] == 'LY-023'
            sources.append('benchmark/phase3/runs/round68/judging/outcome-manifest.json cases[LY-023]')
        elif anon == 'P3-b5b44f93':
            assert '後竟納之' in cases[cid] and '援例可成而遲' in pred_text(cid)
    views = sorted({s[0] for s in seats})
    flags_out.append({
        'anon_id': anon, 'case_id': cid, 'verdict': verdict, 'disposition': verdict,
        'basis': basis, 'carry_suggestion': carry, 'manifest_carry_suggestion': carry,
        'flag': flag_joined, 'category': category, 'views': views,
        'dual_view': len(seats) > 1, 'relation': relation, 'registered_round': 68,
        'sources_checked': sources,
    })
    ann_out.append({
        'anon_id': anon, 'case_id': cid, 'disposition': verdict, 'finding': basis,
        'flag': flag_joined, 'manifest_carry_suggestion': carry, 'relation': relation,
        'registered_round': 68, 'sources_checked': sources, 'source_seats': seats,
    })

verdicts = Counter(a['disposition'] for a in ann_out)
assert verdicts == Counter({'部分成立': 58, '成立': 12, '不成立': 4, '未核': 2}), verdicts
assert counts_kind == Counter({'cont': 70, 'newgist': 1, 'new': 5}), counts_kind
assert all(a['manifest_carry_suggestion'] for a in ann_out if a['disposition'] == '部分成立')
print('定案分布:', dict(verdicts), '关系分布:', dict(counts_kind))

special = [
 {
  'item': '特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记',
  'conclusion': 'BZ-029／BZ-040 本轮未被任何旗标触及，不在本件范围，维持各自原登记、不另裁、不虚构条目，在本件登记维持原状：BZ-029 维持 R55 卒年待核（未核），其错配线索一层照原登记并列、无盘外独立史源不裁；BZ-040 维持 R55 原登记（许世英享年异说待盘外独立史源）。LY-537 本轮被 X2／Y2 旗标触及，已在本件逐件定案（同旨续接、未核维持：『申予日』措辞待核、无盘外独立史源不裁）；YM-070 本轮被 Y1 旗标触及，已在本件逐件定案（同旨续接、未核维持：『都下』语义未明＋『甲寅旬』出处待核并列、无盘外独立史源不裁），不重复入本附注。',
  'evidence': '据 runs/round68/judging/host-mapping.json 与 FLAGS-selfreported-r68.md 逐件比对：76 件 case_id 集合不含 BZ-029／BZ-040，含 LY-537（P3-57245a7a，X2／Y2）与 YM-070（P3-06129ded，Y1）。',
  'scope_note': '本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。',
 },
 {
  'item': '特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）',
  'conclusion': '引文层错配 1 件：X3 旗标 P3-8c72bc76（host-mapping 指 YM-060）所述母病终局未载／其子八月惊风逐点对应 LY-023 结局、不在 YM-060 结局（「后擢西北。」）内，两例 anon 形近（P3-8c72bc76／P3-8c730836，同首缀 P3-8c7）；已按 R67 错配判例以映射例 YM-060 立条、定案不成立，LY-023 本轮已由 Y3 以其本例 anon 立旗同旨、按同旨续接（R67）定案成立，数据面以本登记补足、无遗漏。主张层不合 1 件：X2 对 LY-507 结局含残损替换字符（「五�多歲」）之指，逐字回读 R68 manifest 结局原文作「五十多歲」完好可读、manifest 全档原始字节无 U+FFFD，所指字样不存在，已按本例文本定案不成立（新立）。其余 74 件旗标引文经逐件回读本例 R68 结局原文核对均在本例结局内（引文逐字断言内置于落盘脚本；LY-432 旗标引文作简体「次日即愈」、结局原文作「次日卽愈」，系席位转写用字之别、所指句在本例内，其同旨定案链 R53／R56／R65／R67 已核、不作错配论）。anon 对位：101 条旗标行经 host-mapping.json 逐件回到 case_id，25 例双席同 anon 逐件对位复核，除上述 8c7 形近一件外无串号。',
  'evidence': '脚本结构化解析八件原始 FLAGS-X1..X4／Y1..Y4.md：101 行、76 anon，与汇编 FLAGS-selfreported-r68.md 逐件比对全等（anon 集合全含）；引文逐字断言内置于落盘脚本（续接件关键引文均断言通过，错配件以「在 LY-023 内／不在 YM-060 内」双向断言通过，LY-507 件以 manifest 原始字节无 EF BF BD 断言通过）。',
  'scope_note': '本核查只登记错配事实，不改分数、不改 manifest、不改旗标原文。',
 },
 {
  'item': '特别核查③：结局文本内嵌指令性字样之例——按数据处理登记（本体基线对勘＋本轮旗标注记层两处归属）',
  'conclusion': '承既有登记口径全量复扫 R68 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计／勿以此斷等，并以『须／須／请／請』宽扫人工甄别叙事用字）：cases 本体内指令性字样仍为基线本体四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。本轮新发现本体例 0 件：宽扫另命中 BZ-302／LR2-022／LR3-004／LR3-006／LR3-010／LY-416 均为叙事用字（请同乡说情／请吕纯阳下降／请告归里／所请准），LY-227『須再占』为原书断法通则叙事、非对评分者之指示，均不入指令性登记。本轮旗标另涉注记层字样两处，逐处归属定案：（一）Y3 旗标 P3-ba26b6b9（LY-204）所指旧注层『勿以此斷』——归属 cases 本体之旧注层，即本体四例中 LY-204 一例本身，非新增本体例，已在本件按同旨续接（R66 同例新旨）定案部分成立；（二）X2 旗标 P3-658f01dd（LR2-016）所指 editor_note 字样——归属分列 editor_note（manifest _r56_lr2016_split.editor_note 字段结构化直读），不在 cases 本体，已在本件按同旨续接（R66）定案部分成立。两处各席均按数据处理未服从：X2 旗标原文自载『已按数据处理未采纳』、Y3 旗标原文自载『已按数据处理、未服从』，本席亦只按数据处理、未服从任何一处之指示，事实照录。',
  'evidence': '证据脚本 data_r68_evidence.py 全量扫描输出：关键词命中集合恰为 {BZ-036, BZ-042, BZ-105, LY-204}，与基线本体四例全等；宽扫候选 9 例逐件回读甄别如上；LR2-016 editor_note 以 manifest _r56_lr2016_split 分列字段结构化直读核对（editor_note 含该句、cases[LR2-016] 不含『评分时』）；LY-204『勿以此斷』以 cases[LY-204] 结构化直读核对在本体旧注层内。',
  'scope_note': '本核查只登记字样出处与处理事实，不改分数、不改 manifest、不改结局原文。',
 },
 {
  'item': '特别核查④：同例新旨、旧旨回归与附加层登记（AS-307／LR2-016／AS-210／LY-529／YY-023）',
  'conclusion': '同例新旨 1 件：AS-307（R64 旧旨『押注分布未载』定案不成立；本轮新旨为 prediction 自载无盘面附件残损，核后部分成立），与旧旨各旨独立、并行不悖。旧旨回归 1 件：LR2-016 本轮 X2 旗标回指历轮同旨（editor_note 注记层『甲戌日巳时』细项未逐字复核），已按同旨续接（R66）定案部分成立；R67 同例另一旗标（内容错配）定案不成立与本旨并行不悖、照旧登记。附加层 3 件，均核后属实且已自注/已定案，与各自主旨并行登记、档位不变：AS-210 X2 旗标兼及 R66 同例新旨（版本校勘注记）一层、该旨已定案部分成立，本轮一并承接；LY-529 X1 旗标兼及 prediction 自注卡面逐爻表 OCR 行序曾错乱一层；YY-023 Y3 旗标兼及卡面动爻记载自相矛盾（prediction 自注）一层。',
  'evidence': '逐件回 R68 prediction 全文与结局原文，断言见落盘脚本；历轮定案档 case-annotations-r64.json AS-307 条、case-annotations-r66.json AS-210／LR2-016 条、case-annotations-r67.json LR2-016 条。',
  'scope_note': '本登记只记关系，不改任何一轮分数。',
 },
 {
  'item': '特别核查⑤：汇编一致性与结局文本一致性',
  'conclusion': '八件原始 FLAGS-X1..X4／Y1..Y4.md 与汇编 FLAGS-selfreported-r68.md 逐件比对全等（101 条旗标行、76 anon；单席 51 例、双席 25 例）；R68 各例结局文本经脚本断言与 R67 manifest 逐件全等（487/487），续接类定案的「结局与历轮所核文本一致」前提全数成立。本轮配对异常仅错配 1 件（见特别核查②），无其他异常。',
  'evidence': '证据脚本 data_r68_evidence.py 与落盘脚本 data_r68_build.py 双脚本断言输出。',
  'scope_note': '本核查只登记一致性事实。',
 },
]

doc = {
 '_provenance': 'R68 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）逐件回源核查 R68 八席自报旗标 101 条旗标行（runs/round68/judging/FLAGS-selfreported-r68.md 汇编；八件原始 FLAGS-X1..X4/Y1..Y4.md 逐件与汇编比对全等）、去重为 76 anon／76 例（同例多席同旨合并 25 例）。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round68/predictions/<case_id>.json 预测原文、runs/round68/judging/outcome-manifest.json cases 载荷（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），并与历轮定案档（data/case-annotations-r49.json 至 -r67.json）核对承接关系：70 件为同旨续接（只承接不重裁，含 LR2-016 旧旨回归续接 R66），1 件为同例新旨（AS-307，另裁部分成立），5 件为 R68 新立（逐件回源另裁：残损双示部分成立 2 件 LR3-116／LY-322、错面核后部分成立 1 件 LY-517、残损字样核后不成立 1 件 LY-507、错配登记 1 件 YM-060）。R68 各例结局文本经脚本断言与 R67 manifest 逐件全等（487/487）。本轮 anon 内容错配 1 件（P3-8c72bc76 所述属 LY-023、映射例为 YM-060，按 R67 判例立条定案不成立），主张层不合 1 件（LY-507 结局残损替换字符之指核后不存在、定案不成立）。指令性字样特别核查：cases 本体仍为基线四例（BZ-036／BZ-042／BZ-105／LY-204），LR2-016 之句只存分列 editor_note，本轮新发现本体例 0 件；本轮旗标注记层两处（LY-204 旧注层、LR2-016 editor_note）归属已逐处定案登记于特别核查③，各席均按数据处理未服从。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。',
 'round': 68,
 'flags': flags_out,
 'annotations': ann_out,
 'special_checks': special,
 'counts': {
  'selfreport_flag_rows_total': 101,
  'selfreport_anons_total': 76,
  'cases_total': 76,
  'continuation_cases': 70,
  'same_case_new_gist_cases': 1,
  'new_flag_cases': 5,
  'verdicts': {'部分成立': 58, '成立': 12, '不成立': 4, '未核': 2},
 },
}
out_json = BASE / 'data/case-annotations-r68.json'
out_json.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
back_doc = json.loads(out_json.read_text(encoding='utf-8'))
assert len(back_doc['annotations']) == 76 and Counter(a['disposition'] for a in back_doc['annotations']) == Counter(back_doc['counts']['verdicts'])
assert len(back_doc['flags']) == 76
print('任务二落盘 + 回读断言通过:', out_json)
print('字节数: 附则', out_add.stat().st_size, '| 定案', out_json.stat().st_size)
