#!/usr/bin/env python3
"""R67 数据席落盘脚本：
任务一 -> benchmark/phase3/data/manifest-carryover-r67-addendum.md（R66 部分成立 41 件承接汇编 + 与 R67 manifest 对勘）
任务二 -> benchmark/phase3/data/case-annotations-r67.json（R67 旗标定案，67 行/50 例）
引文逐字断言内置：任一断言不过即不落盘。注记抽取一律结构化直读 JSON 字段。"""
import json
from collections import Counter
from pathlib import Path

BASE = Path('/home/hatch/workspace/divination/benchmark/phase3')
R67 = BASE / 'runs/round67'
SEATS = ['X1', 'X2', 'X3', 'X4', 'Y1', 'Y2', 'Y3', 'Y4']

m67 = json.loads((R67 / 'judging/outcome-manifest.json').read_text(encoding='utf-8'))
cases = m67['cases']
hm = json.loads((R67 / 'judging/host-mapping.json').read_text(encoding='utf-8'))

def load_ann(rnd):
    return json.loads((BASE / f'data/case-annotations-r{rnd}.json').read_text(encoding='utf-8'))

def prior_finding(rnd, cid):
    d = load_ann(rnd)
    for a in d['annotations']:
        if a['case_id'] == cid:
            return a['finding']
    raise AssertionError(f'历轮 r{rnd} 无 {cid} 条')

def pred_text(cid):
    return json.loads((R67 / f'predictions/{cid}.json').read_text(encoding='utf-8'))['prediction_text']

# ---------------- 任务一：承接附则 ----------------
ann66 = load_ann(66)
assert ann66['counts']['verdicts'] == {'部分成立': 41, '成立': 10, '不成立': 2, '未核': 1}
assert Counter(a['disposition'] for a in ann66['annotations']) == Counter(ann66['counts']['verdicts'])
assert len(ann66['annotations']) == 54
partial = [a for a in ann66['annotations'] if a['disposition'] == '部分成立']
assert len(partial) == 41
add = m67['_r67_carryover_notes_addendum']
assert set(add.keys()) == {a['case_id'] for a in partial}
mismatch = [a['case_id'] for a in partial if add[a['case_id']] != a['manifest_carry_suggestion']]
assert not mismatch, f'对勘不一致: {mismatch}'
print('任务一对勘: 41/41 全等，键集全等，counts 断言通过')

lines = []
lines.append('# Manifest 承接册附则（R67）——R66 定案承接建议汇编')
lines.append('')
lines.append('## 卷首说明')
lines.append('')
lines.append('- 本附则为 Phase 3 Round 67（R67）数据席（任务一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r66.json`（R66 定案正本：annotations 54 件，定案分布成立 10／部分成立 41／不成立 2／未核 1）。')
lines.append('- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 10／部分成立 41／不成立 2／未核 1、总 54，与 R66 公布分布逐项一致；部分成立 41 件每件 `manifest_carry_suggestion` 非空断言亦通过。')
lines.append('- 对勘结果：41/41 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round67/judging/outcome-manifest.json` 的 `_r67_carryover_notes_addendum` 层（本席只读该层与 `cases` 键名集），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 0 件）。')
lines.append('- **本附则自 R68 manifest 起落实**；本轮（R67）manifest 不据本附则改动。')
lines.append('- **本件只汇编与对勘，不改任何分数与结局原文。**')
lines.append('- 汇编范围：R66 定案中部分成立 41 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r66.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R67 起」等表述为原档原文，落实轮次按卷首上一条读作自 R68 起，不回溯改动 R67）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。')
lines.append('- 成立 10／不成立 2／未核 1 共 13 件不入正文逐件节，只在文末列 case_id 清单。')
lines.append('- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 一、部分成立件承接汇编（定案档位：部分成立，41 件，逐件全列）')
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
lines.append('- 对勘对象：本汇编第一节 41 件承接注记建议文本（源：`case-annotations-r66.json` 各件 `manifest_carry_suggestion`）与 `benchmark/phase3/runs/round67/judging/outcome-manifest.json` 的 `_r67_carryover_notes_addendum` 对应条目，逐件逐字（全文字符串相等）对勘。')
detail = '、'.join(f"{a['case_id']}＝一致" for a in partial)
lines.append(f'- 对勘结果：41 件逐字一致，差异 0 件（对勘明细：{detail}）。')
lines.append('- 键集合差异：无（manifest 层 41 键与部分成立 41 件 case_id 集合全等）。')
lines.append('- 不一致登记：无。两侧均未作任何静默改动；本附则建议文本照源档原文录入，manifest 侧文本照其盘上原文对勘。勘误结论：无须勘误；本附则结论自 R68 manifest 起落实。')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 自验')
lines.append('')
lines.append('- 原档（case-annotations-r66.json）条目数：54；档位分布成立 10／部分成立 41／不成立 2／未核 1，本席以 `annotations[].disposition` 与原档 `counts.verdicts` 双路复算一致。')
lines.append('- 本附则正文条目数：41（第一节部分成立 41 件），与原档部分成立件数对齐；文末不入附则清单 13 件（成立 10＋不成立 2＋未核 1），41＋13＝54 与原档总数对齐。')
lines.append('- 承接注记建议文本：41 件均自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读录入，未手抄改写；且经上节对勘与 R67 manifest `_r67_carryover_notes_addendum` 逐件逐字一致（41／41）。')
lines.append('- 回读断言：本附则写出后由生成脚本回读，断言第一节条目数＝41、每件承接注记建议文本与原档字段逐字一致（结果见产出时回读记录：通过）。')
lines.append('- 纪律自报：本席只汇编与对勘，未改任何分数、未改 manifest、未改 annotations、未改原卡；outcome-manifest 只读 `_r67_carryover_notes_addendum` 层与 `cases` 键名集（另为续接前提核对 cases 与 R66 逐件全等 487/487，只读）。')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 文末清单：不入附则 13 件（成立 10＋不成立 2＋未核 1，仅列 case_id）')
lines.append('')
for verdict in ['成立', '不成立', '未核']:
    ids = [a['case_id'] for a in ann66['annotations'] if a['disposition'] == verdict]
    lines.append(f"### {verdict} {len(ids)} 件")
    lines.append('')
    for cid in ids:
        lines.append(f'- {cid}')
    lines.append('')
addendum_text = '\n'.join(lines)
out_add = BASE / 'data/manifest-carryover-r67-addendum.md'
out_add.write_text(addendum_text, encoding='utf-8')
# 回读断言
back = out_add.read_text(encoding='utf-8')
assert back.count('### A') == 41
for a in partial:
    assert f"「{a['manifest_carry_suggestion']}」" in back
print('任务一落盘 + 回读断言通过:', out_add)

# ---------------- 任务二：R67 旗标定案 ----------------
# 自报旗标结构化解析（分件逐件打开，禁 ls judging 目录）
import re
def parse_flags_text(text):
    rows = []
    for line in text.splitlines():
        mm = re.match(r'- (P3-[0-9a-f]+)：(.*)$', line)
        if mm:
            rows.append((mm.group(1), mm.group(2)))
    return rows

per_seat = {}
for s in SEATS:
    per_seat[s] = parse_flags_text((R67 / f'judging/FLAGS-{s}.md').read_text(encoding='utf-8'))
flag_rows = [(s, anon, flag) for s in SEATS for anon, flag in per_seat[s]]
assert len(flag_rows) == 67
uniq = {}
for s, anon, flag in flag_rows:
    uniq.setdefault(anon, []).append((s, flag))
assert len(uniq) == 50

# 定案规格：anon -> (verdict, kind, recent_round, basis_round, outcome_quote)
# kind: cont=同旨续接 / newgist=同例新旨 / new=新立
SPEC = {
 'P3-0776fcf5': ('部分成立', 'cont', 66, 66, '三客至、内有杨姓'),
 'P3-20d9674f': ('未核', 'cont', 66, 66, '后果同行都下'),
 'P3-245bdea6': ('不成立', 'cont', 65, 65, '次日卽愈'),
 'P3-2be68f14': ('部分成立', 'cont', 66, 66, '败血三日后复完胎'),
 'P3-31d0b944': ('部分成立', 'cont', 66, 66, 'she died the eighth of October'),
 'P3-34247232': ('成立', 'cont', 66, 66, '盡覆沒'),
 'P3-4458bafd': ('部分成立', 'cont', 64, 64, '照壁之後有一株大樹'),
 'P3-4b7d65d8': ('部分成立', 'cont', 66, 66, '病断（甲戌年不保）原文未载后续结局'),
 'P3-62fa062f': ('部分成立', 'cont', 66, 66, '果死於卯日'),
 'P3-6f4f0d21': ('部分成立', 'cont', 64, 64, '沒有中榜'),
 'P3-4c52a706': ('不成立', 'cont', 66, 66, '而不知已堕于井'),
 'P3-49f01e46': ('未核', 'cont', 64, 64, '果于申予日归'),
 'P3-80732627': ('不成立', 'cont', 66, 66, 'Marked as externally verified, not Lilly-stated.'),
 'P3-8af38d87': ('部分成立', 'cont', 66, 66, '至戊申日沈屙復起'),
 'P3-8c828dc2': ('部分成立', 'cont', 66, 66, '直至戊寅年戊午月壬戌日故'),
 'P3-8f102f3f': ('部分成立', 'cont', 64, 64, '後於申年升任'),
 'P3-9c892d1d': ('部分成立', 'cont', 66, 66, '果於次年三月妹至'),
 'P3-b7521cd5': ('部分成立', 'cont', 64, 64, '后果然'),
 'P3-b68247f2': ('部分成立', 'cont', 65, 65, 'Gopalakrishnan于选后公开承认错误'),
 'P3-c0ab2bd0': ('成立', 'cont', 66, 66, '因子賭博送官'),
 'P3-c202b3c4': ('部分成立', 'cont', 66, 66, '后于午月覆舟而亡'),
 'P3-c4b506a3': ('不成立', 'new', None, None, None),
 'P3-d104f96e': ('部分成立', 'cont', 66, 66, '遊川廣'),
 'P3-d21e91ec': ('部分成立', 'cont', 65, 65, '報出行文拿問'),
 'P3-d25df6d8': ('部分成立', 'cont', 65, 65, '儿妇妊性别如断'),
 'P3-dffdab34': ('部分成立', 'cont', 66, 66, '星辰無光'),
 'P3-e0eca011': ('成立', 'cont', 66, 66, '被論革職'),
 'P3-e5bfad36': ('部分成立', 'cont', 66, 66, '未执政'),
 'P3-eaeac460': ('成立', 'cont', 66, 66, '在午年子月而死'),
 'P3-ebada812': ('成立', 'cont', 66, 66, '果於八月其子驚風'),
 'P3-ead1eca5': ('部分成立', 'cont', 66, 66, '我死，有三尺人来迎'),
 'P3-cde6abf4': ('部分成立', 'cont', 64, 64, '伐樹起公榭'),
 'P3-18eda406': ('成立', 'cont', 66, 66, '服補藥太過'),
 'P3-06f6eaf6': ('部分成立', 'cont', 66, 66, '果有金弟屬猴'),
 'P3-0a0b070c': ('部分成立', 'cont', 64, 64, '驚險異常'),
 'P3-0d88c3ca': ('部分成立', 'cont', 66, 66, '城破与官府一同被害，'),
 'P3-080218a9': ('不成立', 'newgist', 64, None, 'an errour in part I confess it was'),
 'P3-17259218': ('不成立', 'new', None, None, '折花墮地傷股'),
 'P3-1c6bc07a': ('部分成立', 'new', None, None, '存貨堆積四年'),
 'P3-3a71c430': ('不成立', 'newgist', 65, None, '女死辰日'),
 'P3-bbdd9d17': ('部分成立', 'cont', 64, 64, 'within lesse three weekes'),
 'P3-bf42126d': ('部分成立', 'cont', 66, 66, '一一皆是'),
 'P3-c20dd14f': ('部分成立', 'cont', 66, 66, '群蜂满身攒聚'),
 'P3-c1f3d044': ('部分成立', 'cont', 65, 65, '直至戊寅年甲子月癸卯日故'),
 'P3-cad838a6': ('部分成立', 'cont', 64, 64, '网友后回报'),
 'P3-d1dcaddb': ('部分成立', 'cont', 64, 64, '老友夫妇告知'),
 'P3-d2ee60b6': ('部分成立', 'cont', 64, 64, '果於申日文書實收俱到'),
 'P3-d39de2df': ('部分成立', 'cont', 66, 66, '放火燒村而去'),
 'P3-f37596fb': ('部分成立', 'cont', 66, 66, '退位'),
 'P3-fc68afbb': ('部分成立', 'cont', 63, 63, 'OCR prints 1644'),
}
assert set(SPEC.keys()) == set(uniq.keys()), 'SPEC 与去重 anon 集合不合'

CUSTOM_BASIS = {
 'P3-c4b506a3': '新旗标（R67 新立，核后不成立）：回原卡——LR2-016 所问犯人能否出狱；R67 manifest 本例结局为『众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。』，全文无坟地、无改葬、无『即如所言』字样；旗标所述『改向改葬后即如所言、原问坟地吉凶未独立分载』逐点对应 LY-629 结局（『彼果依斷，葬後即如所言．』），且两例 anon 形近（P3-c4b506a3／P3-c4bd4747，同首缀 P3-c4b）。LY-629 本轮未被以其本例 anon 立旗，其既有定案（R64 部分成立：总承式且系改向之后应验、原问坟地吉凶未独立分载）照旧承接、不因本件改动。本件旗标所述内容不在映射例文本内，疑为席位 anon 错配。故不成立（错配登记另见特别核查②）。',
 'P3-080218a9': '同例新旨（R64 旧旨为『结局为混合记载且自承原判部分有误、含解释与更正层』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：回本例 R67 prediction 原始字节逐字核——全文无 U+FFFD 替换字符，旗标所指『埃塞克斯所制』一句在 prediction_text 中作『反为埃塞克斯所制、终致失势』完好可读，所指乱码不存在。故本轮新旨不成立。',
 'P3-17259218': '新旗标（R67 新立，核后不成立）：回本例 R67 prediction 原始字节逐字核——全文无 U+FFFD 替换字符，旗标所指『次日将有一名少女』一句在 prediction_text 中完好可读（『次日將有一名少女來折梅花』），所指乱码不存在；本例结局『次晚果有鄰女折花墮地傷股』与 prediction 对应面完整。故不成立。',
 'P3-1c6bc07a': '新旗标（R67 新立）：回本例 R67 prediction 全文逐字核——爻位处『子孙申金?卦中』『父母子水初?财源』两处确含半角问号『?』字样，所指字样存在一层属实；但 prediction 主体断语（不利、利薄、戌月出脱、置信 0.55）完整可读，且『?』字样在本轮另 7 例 prediction（LY-322／LY-333／LY-510／LY-515／LY-528／LY-533／LY-535）中同式用作连接替代字样、非本例独有残损。故部分成立。',
 'P3-3a71c430': '同例新旨（R65 旧旨为『结局后段为应验解释层』、定案部分成立，本轮新旨与之各旨独立、并行不悖）：回本例 R67 prediction 原始字节逐字核——全文无 U+FFFD 替换字符，旗标所指『窗口』一句（『窗口為旬內，主坐標午日』）在 prediction_text 中完好可读、无乱码字样。故本轮新旨不成立。',
}
CUSTOM_RELATION = {
 'P3-c4b506a3': '新旗标（R67 新立，旗标内容错配、核后不成立）',
 'P3-080218a9': '同例新旨（R64 旧旨旗标部分成立、本轮新旨核后不成立）',
 'P3-17259218': '新旗标（R67 新立，核后不成立）',
 'P3-1c6bc07a': '新旗标（R67 新立）',
 'P3-3a71c430': '同例新旨（R65 旧旨旗标部分成立、本轮新旨核后不成立）',
}
CUSTOM_CARRY = {
 'P3-c4b506a3': '不入附则：本 R67 错配登记定案（不成立），自 R68 起承接本 R67 标注，不加承接注记；LY-629 既有定案（R64 部分成立）照旧承接、不因本件改动；结局原文照录不改。',
 'P3-080218a9': '不入附则：本 R67 同例新旨定案（不成立），自 R68 起承接本 R67 标注，不加承接注记；R64 旧旨部分成立定案照旧登记；结局原文照录不改。',
 'P3-17259218': '不入附则：本 R67 新立定案（不成立），自 R68 起承接本 R67 标注，不加承接注记；结局原文照录不改。',
 'P3-1c6bc07a': '同旨新立：自 R68 起承接本 R67 标注：按「prediction 爻位处含『?』占位字样两处、主体断语完整可读」登记；结局原文照录不改。',
 'P3-3a71c430': '不入附则：本 R67 同例新旨定案（不成立），自 R68 起承接本 R67 标注，不加承接注记；R65 旧旨部分成立定案照旧登记；结局原文照录不改。',
}
CUSTOM_CATEGORY = {
 'P3-c4b506a3': '新旗标：旗标内容错配（所述属 LY-629、本例核后不成立）',
 'P3-080218a9': '同例新旨：prediction 乱码字样核后不存在',
 'P3-17259218': '新旗标：prediction 乱码字样核后不存在',
 'P3-1c6bc07a': 'prediction 爻位处含 ? 占位字样（主体可读）',
 'P3-3a71c430': '同例新旨：prediction 乱码字样核后不存在',
}

flags_out, ann_out = [], []
counts_kind = Counter()
for anon, seat_flags in uniq.items():
    cid = hm[anon]
    assert cid in cases
    verdict, kind, recent, basis_round, quote = SPEC[anon]
    counts_kind[kind] += 1
    seats = [s for s, _ in seat_flags]
    flag_joined = '；'.join(f'{s}：{f}' for s, f in seat_flags)
    sources = [
        f'benchmark/phase3/inputs-dev12/{cid}.json',
        'benchmark/phase3/runs/round67/judging/FLAGS-selfreported-r67.md',
        f'benchmark/phase3/runs/round67/judging/outcome-manifest.json cases[{cid}]',
        f'benchmark/phase3/runs/round67/predictions/{cid}.json',
    ]
    if kind == 'cont':
        pf = prior_finding(basis_round, cid)
        basis = (f'承接既有定案不重裁（历轮最近定案 R{recent} {verdict}）：{pf}'
                 f' 本轮（R67）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。')
        relation = f'同旨续接（R{recent}）'
        category = '同旨续接（详见核查事实）'
        if cid == 'YM-070':
            carry = '同旨续接（未核维持）：自 R68 起承接历轮标注：按「结局措辞待核（『都下』语义未明）」登记，与『甲寅旬』出处待核并列；结局原文照录不改、不补字，无盘外独立史源不裁。'
        elif cid == 'LY-537':
            carry = '待核维持：自 R68 起承接 R56／R57／R61／R64＋本 R67 登记：按「结局『果于申予日归』措辞待核、日期干支不明」登记；无盘外独立史源（原书页文本）前不裁；结局原文照录不改。'
        elif verdict == '部分成立':
            carry = f'同旨续接：自 R68 起承接 R{recent}＋本 R67 标注；结局原文照录不改。'
        else:
            carry = f'不入附则：本 R67 同旨续接定案（{verdict}），自 R68 起承接本 R67 标注，不加承接注记；结局原文照录不改。'
        # 引文逐字断言（判例①②）
        assert quote and quote in cases[cid], f'{cid} 引文断言失败: {quote}'
        for r in range(49, 67):
            p = BASE / f'data/case-annotations-r{r}.json'
            if p.exists():
                d = json.loads(p.read_text(encoding='utf-8'))
                if any(a['case_id'] == cid for a in d.get('annotations', [])):
                    sources.append(f'benchmark/phase3/data/case-annotations-r{r}.json {cid} 条')
    else:
        basis = CUSTOM_BASIS[anon]
        relation = CUSTOM_RELATION[anon]
        category = CUSTOM_CATEGORY[anon]
        carry = CUSTOM_CARRY[anon]
        if anon == 'P3-c4b506a3':
            assert '即如所言' in cases['LY-629'] and '即如所言' not in cases['LR2-016']
            sources.append('benchmark/phase3/data/case-annotations-r64.json LY-629 条')
        elif anon in ('P3-080218a9', 'P3-17259218', 'P3-3a71c430'):
            raw = (R67 / f'predictions/{cid}.json').read_bytes()
            assert b'\xef\xbf\xbd' not in raw
            if quote:
                assert quote in cases[cid], f'{cid} 引文断言失败'
            if anon == 'P3-3a71c430':
                assert '窗口為旬內' in pred_text(cid)
        elif anon == 'P3-1c6bc07a':
            assert '子孙申金?卦中' in pred_text(cid) and '父母子水初?财源' in pred_text(cid)
            assert quote in cases[cid]
    views = sorted({s[0] for s in seats})
    flags_out.append({
        'anon_id': anon, 'case_id': cid, 'verdict': verdict, 'disposition': verdict,
        'basis': basis, 'carry_suggestion': carry, 'manifest_carry_suggestion': carry,
        'flag': flag_joined, 'category': category, 'views': views,
        'dual_view': len(seats) > 1, 'relation': relation, 'registered_round': 67,
        'sources_checked': sources,
    })
    ann_out.append({
        'anon_id': anon, 'case_id': cid, 'disposition': verdict, 'finding': basis,
        'flag': flag_joined, 'manifest_carry_suggestion': carry, 'relation': relation,
        'registered_round': 67, 'sources_checked': sources, 'source_seats': seats,
    })

verdicts = Counter(a['disposition'] for a in ann_out)
assert verdicts == Counter({'部分成立': 35, '成立': 6, '不成立': 7, '未核': 2}), verdicts
assert counts_kind == Counter({'cont': 45, 'newgist': 2, 'new': 3}), counts_kind
print('定案分布:', dict(verdicts), '关系分布:', dict(counts_kind))

special = [
 {
  'item': '特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记',
  'conclusion': 'BZ-029／BZ-040 本轮未被任何旗标触及，不在本件范围，维持各自原登记、不另裁、不虚构条目：BZ-029 维持 R55 卒年待核（未核），其错配线索一层照原登记并列、无盘外独立史源不裁；BZ-040 维持 R55 原登记（许世英享年异说待盘外独立史源）。LY-537 本轮被 X2 旗标触及，已在本件逐件定案（同旨续接、未核维持：『申予日』措辞待核、无盘外独立史源不裁）；YM-070 本轮被 X1 旗标触及，已在本件逐件定案（同旨续接、未核维持：『都下』语义未明＋『甲寅旬』出处待核并列、无盘外独立史源不裁），不重复入本附注。',
  'evidence': '据 runs/round67/judging/host-mapping.json 与 FLAGS-selfreported-r67.md 逐件比对：50 件 case_id 集合不含 BZ-029／BZ-040，含 LY-537（P3-49f01e46，X2）与 YM-070（P3-20d9674f，X1）。',
  'scope_note': '本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。',
 },
 {
  'item': '特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）',
  'conclusion': '引文层错配 1 件：X4 旗标 P3-c4b506a3（host-mapping 指 LR2-016）所述改葬／『即如所言』逐点对应 LY-629 结局、不在 LR2-016 结局内，两例 anon 形近（P3-c4b506a3／P3-c4bd4747，同首缀 P3-c4b）；已按 R64 错配判例以映射例 LR2-016 立条、定案不成立，LY-629 本轮未被以其本例 anon 立旗、其 R64 部分成立既有定案照旧承接，数据面以本登记补足、无遗漏。其余 49 件旗标引文经逐件回读本例 R67 结局原文核对均在本例结局内（引文逐字断言内置于落盘脚本）。主张层不合 3 件：Y1 对 AS-208／MH-001／LY-615 三例 prediction_text 乱码（U+FFFD）之指，逐件回读原始字节均无该字符、所指句完好可读，已各按本例文本定案不成立（AS-208／LY-615 为同例新旨、MH-001 为新立）。Y1 对 LY-520『?』占位字样之指逐字属实（两处），已定案部分成立（新立）。anon 对位：67 条旗标行经 host-mapping.json 逐件回到 case_id，17 例双席同 anon 逐件对位复核，除上述 c4b 形近一件外无串号。',
  'evidence': '脚本结构化解析八件原始 FLAGS-X1..X4／Y1..Y4.md：67 行、50 anon，与汇编 FLAGS-selfreported-r67.md 逐件比对全等（anon 集合全含）；引文逐字断言内置于落盘脚本（50 件关键引文均断言通过，错配件以「在 LY-629 内／不在 LR2-016 内」双向断言通过；三件乱码件以原始字节无 EF BF BD 断言通过）。',
  'scope_note': '本核查只登记错配事实，不改分数、不改 manifest、不改旗标原文。',
 },
 {
  'item': '特别核查③：结局文本内嵌指令性字样之例——按数据处理登记',
  'conclusion': '承既有登记口径全量复扫 R67 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计／勿以此斷等，并以『须／須／请／請』宽扫人工甄别叙事用字）：cases 本体内指令性字样仍为本体四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。本轮无新发现（0 件）：宽扫另命中 BZ-302／LR2-022／LR3-004／LR3-006／LR3-010／LY-416 均为叙事用字（请情愿／请告归里／所请准），LY-227『須再占』为原书断法通则叙事、非对评分者之指示，均不入指令性登记。各席与本席均只按数据处理、未服从任何一处之指示。',
  'evidence': '证据脚本 data_r67_evidence.py 全量扫描输出：关键词命中集合恰为 {BZ-036, BZ-042, BZ-105, LY-204}；宽扫候选 9 例逐件回读甄别如上；LR2-016 editor_note 以 manifest _r56_lr2016_split 分列字段结构化直读核对。',
  'scope_note': '本核查只登记字样出处与处理事实，不改分数、不改 manifest、不改结局原文。',
 },
 {
  'item': '特别核查④：同例新旨（AS-208／LY-615）与旧旨回指（AS-210）登记',
  'conclusion': '同例新旨 2 件，均与各自旧旨各旨独立、并行不悖，本轮新旨定案均为不成立：AS-208（R64 旧旨『混合记载含解释与更正层』部分成立；本轮新旨为 prediction 乱码之指、核后不存在）；LY-615（R65 旧旨『结局后段应验解释层』部分成立；本轮新旨为 prediction 乱码之指、核后不存在）。AS-210 本轮 Y3 旗标回指历轮旧旨（得缺以总承语带过、未明名），已按同旨续接（R64）定案部分成立；R66 同例新旨（版本校勘注记）定案并行不悖、照旧登记。',
  'evidence': '逐件回 R67 prediction 原始字节与结局原文，断言见落盘脚本；历轮定案档 case-annotations-r64.json AS-208／AS-210 条、case-annotations-r65.json LY-615 条。',
  'scope_note': '本登记只记关系，不改任何一轮分数。',
 },
 {
  'item': '特别核查⑤：汇编一致性与结局文本一致性',
  'conclusion': '八件原始 FLAGS-X1..X4／Y1..Y4.md 与汇编 FLAGS-selfreported-r67.md 逐件比对全等（67 条旗标行、50 anon）；R67 各例结局文本经脚本断言与 R66 manifest 逐件全等（487/487），续接类定案的「结局与历轮所核文本一致」前提全数成立。本轮无主张层不合件之外的配对异常（错配 1 件见特别核查②）。',
  'evidence': '证据脚本 data_r67_evidence.py 与落盘脚本 data_r67_build.py 双脚本断言输出。',
  'scope_note': '本核查只登记一致性事实。',
 },
]

doc = {
 '_provenance': 'R67 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断/修订，不改任何分数）逐件回源核查 R67 八席自报旗标 67 条旗标行（runs/round67/judging/FLAGS-selfreported-r67.md 汇编；八件原始 FLAGS-X1..X4/Y1..Y4.md 逐件与汇编比对全等）、去重为 50 anon／50 例（同例多席同旨合并 17 例）。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round67/predictions/<case_id>.json 预测原文、runs/round67/judging/outcome-manifest.json cases 载荷（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），并与历轮定案档（data/case-annotations-r49.json 至 -r66.json）核对承接关系：45 件为同旨续接（只承接不重裁），2 件为同例新旨（另裁、均核后不成立），3 件为 R67 新立（逐件回源另裁：错配登记 1、乱码核后不成立 1、? 占位字样部分成立 1）。R67 各例结局文本经脚本断言与 R66 manifest 逐件全等（487/487）。本轮 anon 内容错配 1 件（P3-c4b506a3 所述属 LY-629、映射例为 LR2-016，按 R64 判例立条定案不成立），主张层不合 3 件（三例 prediction 乱码之指核后不存在、均定案不成立）。本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。',
 'round': 67,
 'flags': flags_out,
 'annotations': ann_out,
 'special_checks': special,
 'counts': {
  'selfreport_flag_rows_total': 67,
  'selfreport_anons_total': 50,
  'cases_total': 50,
  'continuation_cases': 45,
  'same_case_new_gist_cases': 2,
  'new_flag_cases': 3,
  'verdicts': {'部分成立': 35, '成立': 6, '不成立': 7, '未核': 2},
 },
}
out_json = BASE / 'data/case-annotations-r67.json'
out_json.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding='utf-8')
back = json.loads(out_json.read_text(encoding='utf-8'))
assert len(back['annotations']) == 50 and Counter(a['disposition'] for a in back['annotations']) == Counter(back['counts']['verdicts'])
print('任务二落盘 + 回读断言通过:', out_json)
print('字节数: 附则', out_add.stat().st_size, '| 定案', out_json.stat().st_size)
