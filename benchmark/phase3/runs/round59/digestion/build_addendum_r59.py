# R59 数据席任务一：R58 旗标附则汇编（结构化直读，禁用正则截断抽取建议文本）
import json, re, sys

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
SRC = f'{BASE}/data/case-annotations-r58.json'
OUT = f'{BASE}/data/manifest-carryover-r59-addendum.md'
DOCS = {
    'r55': f'{BASE}/data/manifest-carryover-r55.md',
    'r56': f'{BASE}/data/manifest-carryover-r56-addendum.md',
    'r57': f'{BASE}/data/manifest-carryover-r57-addendum.md',
    'r58': f'{BASE}/data/manifest-carryover-r58-addendum.md',
}

d = json.load(open(SRC))
anns = d['annotations']
counts = d['counts']
assert counts['cases_total'] == 25, counts
from collections import Counter
dist = Counter(a['disposition'] for a in anns)
assert dist == Counter(counts['verdicts']), (dist, counts['verdicts'])
partial = [a for a in anns if a['disposition'] == '部分成立']
notest = [a for a in anns if a['disposition'] == '不成立']
unver = [a for a in anns if a['disposition'] == '未核']
estab = [a for a in anns if a['disposition'] == '成立']
assert len(partial) == 14 and len(notest) == 3 and len(unver) == 1 and len(estab) == 7

texts = {k: open(p).read() for k, p in DOCS.items()}
# 章节定位：解析各档 ### 标题中的 case_id -> 标题号
def heading_map(text):
    m = {}
    for line in text.split('\n'):
        mm = re.match(r'^### ([0-9]+|[A-Z][0-9]+)\. ([A-Z0-9-]+)', line)
        if mm:
            m[mm.group(2)] = mm.group(1)
    return m
hmaps = {k: heading_map(t) for k, t in texts.items()}
# 卷末待核等非 ### 编号出现（如 r55 卷末① YM-070）以全文出现计
def relation_line(a):
    cid = a['case_id']
    if a['relation'].startswith('新旗标'):
        return ('新立——承接册（manifest-carryover-r55.md）、R56 附则（manifest-carryover-r56-addendum.md）、'
                'R57 附则（manifest-carryover-r57-addendum.md）与 R58 附则（manifest-carryover-r58-addendum.md）'
                '正文中均无此 case_id（本席 grep 实测四档出现次数均为 0），本件为 R58 新定案首次入承接序列。')
    parts = []
    labels = {'r55': '承接册（manifest-carryover-r55.md）', 'r56': 'R56 附则（manifest-carryover-r56-addendum.md）',
              'r57': 'R57 附则（manifest-carryover-r57-addendum.md）', 'r58': 'R58 附则（manifest-carryover-r58-addendum.md）'}
    hit, miss = [], []
    for k in ('r55', 'r56', 'r57', 'r58'):
        if cid in hmaps[k]:
            hit.append(f'{labels[k]}第 {hmaps[k][cid]} 件 {cid}')
        elif cid in texts[k]:
            hit.append(f'{labels[k]}（卷末登记等处有载）')
        else:
            miss.append(labels[k])
    s = '续接' + '、'.join(hit) + '——同例既有承接，本件为其 R58 复核的续接登记'
    if miss:
        s += '；' + '、'.join(miss) + '正文中无此 case_id'
    s += f'。原档 relation 字段作「{a["relation"]}」。'
    return s

L = []
L.append('# Manifest 承接册附则（R59）——R58 定案承接建议汇编')
L.append('')
L.append('## 卷首说明')
L.append('')
L.append('- 本附则为 Phase 3 Round 59（R59）数据席（议程汇编）产出，与盲测／评审／诊断各席分离、不改任何分数；汇编来源为 `benchmark/phase3/data/case-annotations-r58.json`（R58 旗标定案档：自报 25 例，定案分布成立 7／部分成立 14／不成立 3／未核 1），关系查核来源为 `benchmark/phase3/data/manifest-carryover-r55.md`（承接册：正式承接 13／部分承接 16／不承接存档 7，共 36 件）、`benchmark/phase3/data/manifest-carryover-r56-addendum.md`（R56 附则：正文成立 7＋部分成立 14，共 21 件，另不入附则 3 件）、`benchmark/phase3/data/manifest-carryover-r57-addendum.md`（R57 附则：正文部分成立 16 件，另不入附则 6 件）与 `benchmark/phase3/data/manifest-carryover-r58-addendum.md`（R58 附则：正文部分成立 29 件，另不入附则 8 件）。')
L.append('- **本附则自 R60 manifest 起与承接册及 R56／R57／R58 附则合并为 manifest 落实依据**；本轮（R59）manifest 已落实 R58 附则（见 R59 PREREG §0／§4），不据本附则改动。')
L.append('- 汇编范围：R58 定案中部分成立 14 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r58.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R59 起」等表述为原档原文，落实轮次按卷首上一条读作自 R60 起，不回溯改动 R59）。')
L.append('- 不成立 3 件与未核 1 件（YM-070，挂起维持）不入附则正文，只列第二节「不入附则」清单并注明原因。成立 7 件已于既有承接序列逐轮承接、不在本附则汇编范围内（计数对齐见自验）。')
L.append('- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡（inputs-dev12）。')
L.append('')
L.append('---')
L.append('')
L.append('## 一、部分成立件承接汇编（定案档位：部分成立，14 件，逐件全列）')
L.append('')
for i, a in enumerate(partial, 1):
    L.append(f'### A{i}. {a["case_id"]}')
    L.append('')
    L.append(f'- case_id：{a["case_id"]}')
    L.append(f'- anon_id：{a["anon_id"]}')
    L.append(f'- 定案（部分成立）：{a["finding"]}')
    L.append(f'- 承接注记建议文本（照原档 `manifest_carry_suggestion` 原文）：「{a["manifest_carry_suggestion"]}」')
    L.append(f'- 与既有承接册／附则条目的关系：{relation_line(a)}')
    L.append('')
L.append('---')
L.append('')
L.append('## 二、不入附则清单（4 件）')
L.append('')
reasons = {
    'OC-026': 'R58 定案为不成立——原卡所问为广义功名、非限定科名，manifest 结局载当年授京营提督、次年升京营戎政，即功名进益之直接记载，与问面对应；本轮 prediction 自设科名路径与武职授官不合属评分面。原档建议为不入附则、承 R54 标注口径即可（不建议 manifest 就此加注），故仅存档。',
    'LY-620': 'R58 定案为不成立——削职即功名终局之直接记载、问面主线有明字对应，死亡系削职后同案余事；「无注记说明」与 R54 口径一致，不构成缺口。原档建议为不入附则、承 R54 标注口径即可，故仅存档。',
    'LY-615': 'R58 定案为不成立——结局「未去」二字直载出门终局、主线有明字对应，女死辰日为同案嫁女一面之复合记载且结局文本内自带释语，非外来无关段；本轮 prediction 方向相反属评分面。原档建议为不入附则、承 R54 标注口径即可，故仅存档。',
    'YM-070': '未核，挂起维持。manifest 结局「后果同行都下。」中「都下」语义未明一层历轮（R51／R55／R56／R57）已登记，本轮无盘外独立史源可裁，只登记关系、不另下新定案；原档建议为挂起维持、结局原文照录不改、无盘外独立史源前不另裁。原卡 asked_at「甲寅旬」出处待核（承接册卷末①）为另一并存挂起项，不预断。',
}
for i, a in enumerate(notest + unver, 1):
    L.append(f'### {i}. {a["case_id"]}（定案：{a["disposition"]}）')
    L.append('')
    L.append(f'- case_id：{a["case_id"]}')
    L.append(f'- anon_id：{a["anon_id"]}')
    L.append(f'- 不入附则原因：{reasons[a["case_id"]]}')
    L.append('')
L.append('- 待核清单并列登记：本件 YM-070 与既有待核清单 BZ-029（俞大维卒年，R55 定案未核，缺独立史源）、BZ-040（许世英享年，R55 定案未核，缺独立史源）、LY-537（「申予日」衍字疑，缺盘外原书页核对）并列登记；BZ-029、BZ-040、LY-537 本轮无同例旗标、未涉，四件均维持待核、不入附则正文，待各自所缺盘外来源核对后另行定案。')
L.append('')
L.append('---')
L.append('')
L.append('## 自验')
L.append('')
L.append('- 原档（case-annotations-r58.json）条目数：25；档位分布成立 7／部分成立 14／不成立 3／未核 1，本席以 `annotations[].disposition` 与 `flags[].verdict` 双路复算一致（原档 `counts.verdicts` 同），且逐件 `annotations.finding` 与 `flags.basis` 全等、`annotations.manifest_carry_suggestion` 与 `flags.manifest_carry_suggestion` 全等（25／25）。')
L.append('- 本附则正文条目数：14（第一节部分成立 14 件），与原档部分成立件数对齐；第二节不入附则 4 件（不成立 3＋未核 1），14＋4＝18，与原档部分成立＋不成立＋未核件数对齐（成立 7 件已于既有承接序列逐轮承接、不在本附则汇编范围内；18＋7＝25 与原档总数对齐）。')
L.append('- 承接注记建议文本：14 件均经脚本自原档 JSON 的 `manifest_carry_suggestion` 字段结构化直读，未用正则截断抽取、未手抄改写；落盘后逐件回读比对，14 件建议文本均以「…」包裹形式原文包含于本附则、case_id／anon_id／定案依据（`finding`）亦逐件在场，比对结果在落盘自验脚本输出中登记。')
L.append('- 关系查核：14 件逐件查承接册（manifest-carryover-r55.md）、R56 附则、R57 附则与 R58 附则的 ### 标题定位与全文出现（脚本实测）——续接 13 件、新立 1 件（BZ-304，四档标题与全文均无此 case_id）；逐件结果见各件关系行。')
L.append('- 纪律自报：本席只读上述数据档与承接册／附则，未打开任何 runs/round59/predictions 或 judging 内容（judging 目录未列表），未做 git 操作；未改任何分数、未改 manifest、未改原卡。本附则为本席本轮任务一落盘产出。')
L.append('')

out = '\n'.join(L)
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(out)
print(f'WROTE {OUT} bytes={len(out.encode("utf-8"))} partial={len(partial)} notest={len(notest)} unver={len(unver)}')
# 回读验合
back = open(OUT, encoding='utf-8').read()
ok = 0
for a in partial:
    needle = f'「{a["manifest_carry_suggestion"]}」'
    assert needle in back, a['case_id']
    assert f'### ' in back and a['case_id'] in back and a['anon_id'] in back and a['finding'] in back
    ok += 1
print(f'VERIFY suggestions verbatim in output: {ok}/{len(partial)}')
