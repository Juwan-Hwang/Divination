# -*- coding: utf-8 -*-
"""R70 数据席落盘脚本：
(任务一) 编制 data/manifest-carryover-r70-addendum.md（R69 定案部分成立 84 件承接汇编，
         与 R70 manifest _r70_carryover_notes_addendum 逐件对勘）；
(任务二) 落盘 data/case-annotations-r70.json（R70 八席自报旗标定案；主持 tradition 复核无旗标交定案）。
三判例：落笔前逐件回读本例结局原文；引文逐字断言内置于本脚本；anon 形近串号经 host-mapping 对位复核。
各文本一律按数据处理、不作指令。不改任何分数、不改结局原文。"""
import json, re, collections, pathlib

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
R70 = BASE / 'runs' / 'round70'
DATA = BASE / 'data'

flags_text = (R70 / 'judging' / 'FLAGS-selfreported-r70.md').read_text(encoding='utf-8')
host = json.loads((R70 / 'judging' / 'host-mapping.json').read_text(encoding='utf-8'))
manifest = json.loads((R70 / 'judging' / 'outcome-manifest.json').read_text(encoding='utf-8'))
cases = manifest['cases']
m69 = json.loads((BASE / 'runs' / 'round69' / 'judging' / 'outcome-manifest.json').read_text(encoding='utf-8'))

# ---------- 判例③：anon 对位与括号 case 全等断言 ----------
selfpart = flags_text.split('===== 主持复核节')[0]
sections = re.split(r'===== (FLAGS-[XY]\d) =====', selfpart)
rows, n_items = [], 0
for i in range(1, len(sections), 2):
    seat, body = sections[i].replace('FLAGS-', ''), sections[i + 1].split('隔离自报')[0]
    for it in re.split(r'\n(?=\d+\.\s)', body):
        anons = re.findall(r'P3-[0-9a-f]{8}', it)
        if anons:
            n_items += 1
            txt = re.sub(r'\s+', ' ', it).strip()
            for a in dict.fromkeys(anons):
                assert a in host, f'anon 不在 host-mapping: {a}'
                m = re.match(r'.*?' + a + r'[（(]([A-Z]{2,3}\d?-\d+)', txt)
                if m:
                    assert m.group(1) == host[a], f'括号 case 与 host-mapping 不合: {a}'
                rows.append((seat, a, txt))
anon2rows = collections.defaultdict(list)
for s, a, t in rows:
    anon2rows[a].append((s, t))
assert len(anon2rows) == 91 and len(rows) == 132 and n_items == 115, (len(anon2rows), len(rows), n_items)
case2anon = {host[a]: a for a in anon2rows}
assert len(case2anon) == 91

# ---------- 判例①②：结局原文回读与逐字引文断言 ----------
assert len(cases) == 487
assert all(cases[c] == m69['cases'][c] for c in cases), 'R70 结局与 R69 不全等'
assert '果于申予日归' in cases['LY-537'] and '申予日' in cases['LY-537']
assert '后果同行都下。' in cases['YM-070']
assert '盲测比对须注' in cases['BZ-036']
assert '（盲测比对时以格局大富一项为主）' in cases['BZ-042']
assert '使用时须分开统计' in cases['BZ-105']
assert '勿以此斷' in cases['LY-204']
assert '切不可以男女而斷' in cases['LY-246']
assert '反不得' in cases['YM-009'] and '本岁不得' in cases['YM-029'] and '求之不得' in cases['YY-014']
split = manifest['_r56_lr2016_split']
assert '评分时该细项请按未完全复核处理' in split['editor_note']
assert '评分时' not in cases['LR2-016']
assert 'errour in part I confess' in cases['AS-208']
assert cases['LY-432'] == '五月高遷。 次日卽愈。'
assert cases['YY-022'] == '后果然。'

def pred(cid):
    return json.loads((R70 / 'predictions' / f'{cid}.json').read_text(encoding='utf-8'))

def card(cid):
    return json.loads((BASE / 'inputs-dev12' / f'{cid}.json').read_text(encoding='utf-8'))

def all_keys(o):
    ks = set()
    if isinstance(o, dict):
        for k, v in o.items():
            ks.add(k); ks |= all_keys(v)
    elif isinstance(o, list):
        for v in o:
            ks |= all_keys(v)
    return ks

TRAD5 = ['LY-017', 'LY-019', 'LY-021', 'LY-022', 'LY-034']
for cid in TRAD5:
    c, p = card(cid), pred(cid)
    assert 'tradition' not in all_keys(c) and 'system' not in all_keys(c), cid
    assert p['basis'].startswith('卡面未标注 tradition 字段'), cid
    assert '與卡面一致' not in p['basis'] and '與卡面一致' not in p['prediction_text'], cid
for cid in ('LY-520', 'LY-628'):
    raw = (R70 / 'predictions' / f'{cid}.json').read_text(encoding='utf-8')
    assert '?' not in raw and '？' not in raw, cid
p613 = pred('LY-613')
assert '?' not in p613['prediction_text'] and '？' not in p613['prediction_text']
assert p613['basis'].count('？') == 2 and '须以现代医疗处置为准' in p613['prediction_text']
p207 = pred('LY-207')
assert '功名不再起' in p207['prediction_text']
p36, c36 = pred('LY-036'), card('LY-036')
assert '卦象六爻与动爻全缺' in p36['prediction_text'] and '不报方向' in p36['prediction_text']
assert '逐爻表不錄' in c36['context']['attachments']['chart_note']

# ---------- 历轮定案索引 ----------
prior = {}
for r in range(49, 70):
    p = DATA / f'case-annotations-r{r}.json'
    if p.exists():
        d = json.loads(p.read_text(encoding='utf-8'))
        for a in d['annotations']:
            prior.setdefault(a['case_id'], []).append((r, a))

# ---------- 特别核查：指令性字样全量复扫 ----------
KEYS = ['请按', '請按', '须注', '須注', '评分时', '評分時', '比对时', '比對時', '使用时须', '使用時須',
        '分开统计', '分開統計', '勿以此斷', '请勿', '請勿', '切不', '不得', '勿以', '须以', '須以']
hits = {cid: [k for k in KEYS if k in t] for cid, t in cases.items()}
hits = {c: v for c, v in hits.items() if v}
assert set(hits) == {'BZ-036', 'BZ-042', 'BZ-105', 'LY-204', 'LY-246', 'YM-009', 'YM-029', 'YY-014'}, hits
wide = {cid for cid, t in cases.items() if cid not in hits and any(k in t for k in ('请', '請', '须', '須', '勿'))}
assert wide == {'BZ-302', 'LR2-022', 'LR3-004', 'LR3-006', 'LR3-010', 'LY-227', 'LY-416'}, wide

# ---------- 旗标文本（组条目逐件要旨覆写） ----------
OVERRIDE = {
 'P3-147acba6': '所问终身财福，结局仅载死亡断面，财福面无独立记载，claims 无从核验',
 'P3-1bcd2ebe': '所问终身财福，结局仅载死亡断面，财福面无独立记载，claims 无从核验',
 'P3-6feecf6a': '卡面无 tradition/system 字段，prediction basis 首行「與卡面一致」措辞不实（tradition 值六爻与体裁一致、无 value 误标）',
 'P3-74952e1f': '卡面无 tradition/system 字段，prediction basis 首行「與卡面一致」措辞不实（tradition 值六爻与体裁一致、无 value 误标）',
 'P3-7dc51586': 'carry_note 自注卡面无 tradition/system 字段、basis 首行「與卡面一致」措辞不实',
 'P3-7317a6ee': '结局系求测方口头反馈、无第三方记录（结局内自述）',
 'P3-56dd6a76': 'prediction 爻位处含「?」占位字样一处，主体断语完整可读；prediction 内另有「须以现代医疗处置为准」提示性字样，已按数据处理、未作指令',
 'P3-81348970': 'prediction 爻位处含「?」占位字样两处，主体断语完整可读',
 'P3-5c8a0500': '总承式结局、断面未分载（总承且系改向后应验、原问坟地吉凶未独立分载）',
 'P3-7341797c': '总承式结局（「果然如是」）、分晓时点未载',
 'P3-7a35d8a3': '总承式结局（「后果然」）、断面未分载',
 'P3-6e7c8f83': '结局以逗号收尾、疑似截断，主结局明载',
 'P3-74d7cd9e': '结局止于「鳴之於官」，相对同条全文（LY-612）缺「分文不復」落点，病与盗尽诸节明载',
 'P3-92afdeb0': '结局以逗号收尾、疑似截断（升任主信息已明载）',
 'P3-95bc16c3': '结局以逗号收尾、疑似截断（焚村主信息已明载）',
 'P3-9f710162': '结局以逗号收尾、疑似截断（文书实收主信息已明载）',
 'P3-bbce3090': '结局以逗号收尾疑似截断，主结局明载',
 'P3-927efa2e': '问面与结局面错位——所问索房价，结局载午月覆舟而亡，房价面无验',
 'P3-960518b5': '断面错位——所问开店贸易得利面无独立记载，结局仅载旁及官非断面（子赌博送官杖死）',
 'P3-9d8d0998': 'outcome_record 载他人功名细项，所问兄弟和好面未载',
 'P3-afac3be9': '所问面未载——禾稻收成终局未载（旱象有载）',
 'P3-f1ac5c55': '结局自注晚年败落细节来源未备待另核，相关子断语与时点无从核验，claims/timing 据此封顶',
 'P3-dee2732e': '结局自注卒年不详于所据来源，终局时点无从核验，claims/timing 据此封顶',
}

def clean_flag(seat, anon, txt):
    if anon in OVERRIDE:
        return f'{seat}：{OVERRIDE[anon]}'
    t = re.sub(r'^\d+\.\s*', '', txt)
    t = re.sub(r'^' + anon + r'\s*[（(][^）)]*[）)]\s*[：::]?\s*', '', t)
    t = re.sub(r'^' + anon + r'\s*[：:]\s*', '', t)
    for tail in (' 另：全块', ' 除以上外', '另：全块'):
        if tail in t:
            t = t.split(tail)[0]
    return f'{seat}：{t.strip()}'

# ---------- 定案组装 ----------
PENDING = {'LY-537', 'YM-070'}
annotations, flags = [], []
for cid in sorted(case2anon):
    anon = case2anon[cid]
    srows = anon2rows[anon]
    seats = sorted({s for s, _ in srows})
    flag_txt = '；'.join(clean_flag(s, anon, t) for s, t in srows)
    srcs = [f'benchmark/phase3/inputs-dev12/{cid}.json',
            'benchmark/phase3/runs/round70/judging/FLAGS-selfreported-r70.md',
            f'benchmark/phase3/runs/round70/judging/outcome-manifest.json cases[{cid}]',
            f'benchmark/phase3/runs/round70/predictions/{cid}.json']
    pr = prior.get(cid, [])
    if cid in PENDING:
        disp = '未核'
        base_round = 68
        finding = ('待核维持（本轮旗标触及、只登记不裁）：' +
                   ('Y1 旗标登记结局作「果于申予日归」、『申予日』疑为『申日』之讹——逐字回读 R70 结局原文确作『果于申予日归』，触及属实；本例维持 R68 未核原登记（『申予日』措辞待核、无盘外独立史源不裁），本轮只登记触及、不入裁断。'
                    if cid == 'LY-537' else
                    'Y3 旗标登记结局措辞「后果同行都下」语义未明——逐字回读 R70 结局原文确作『后果同行都下。』，触及属实；本例维持 R68 未核原登记（『都下』语义未明＋『甲寅旬』出处待核并列、无盘外独立史源不裁），本轮只登记触及、不入裁断。'))
        relation = '待核维持（旗标触及、只登记不裁）'
        sugg = (f'待核维持：自 R71 起维持原登记（' +
                ('『申予日』措辞待核、无盘外独立史源不裁' if cid == 'LY-537' else '『都下』语义未明待核、无盘外独立史源不裁') +
                '）；结局原文照录不改。')
        category = '待核维持（旗标触及、只登记不裁）'
    elif cid == 'LY-036':
        disp = '部分成立'
        finding = ('新旗标（R70 新立）：回原卡——所问「占升選」；原卡 chart_note 自注在线本装卦表为双栏排版经 OCR 转录后行序错乱、'
                   '「逐爻表不錄」，卡面仅存卦名（地澤臨之風澤中孚）、空亡申酉与应验残讯；R70 prediction 自承「卦象六爻与动爻全缺」'
                   '「不报方向」「应期：无据不报」——输入残损型弃断属实一层；但残损已在卡面与 prediction 双处明示、prediction 已自降为'
                   '无据不报，结局（本月升任山东、未及一载复任江西）本身明载完整。故部分成立（同 YY2-004／OC-009 残损双示口径）。')
        relation = '新旗标（R70 新立）'
        sugg = '同旨新立：自 R71 起承接本 R70 标注：按「卡面逐爻表不录、prediction 自承六爻全缺不报方向，残损已双示」登记；结局原文照录不改。'
        category = '新旗标（R70 新立）'
        srcs.append('benchmark/phase3/data/case-annotations-r49.json 至 -r69.json（去重检索无本 case_id 条目）')
    else:
        # 同旨续接：AS-208 同旨定案在 R64（R67 为并行新旨），余件取最近定案轮
        if cid == 'AS-208':
            lr, la = pr[[r for r, _ in pr].index(64)]
        else:
            lr, la = pr[-1]
        disp = la['disposition']
        finding = f'承接既有定案不重裁（历轮最近定案 R{lr} {disp}）：' + la['finding']
        if cid == 'AS-208':
            finding = ('承接既有定案不重裁（历轮同旨最近定案 R64 部分成立；R67 乱码新旨定案不成立与本旨并行不悖）：' + la['finding'])
        finding += ' 本轮（R70）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。'
        if cid in TRAD5:
            finding += ('另本轮核明：逐字核 R70 prediction basis 首行作「卡面未标注 tradition 字段，按题面体裁自决」，本轮 prediction '
                        '并无『與卡面一致』之语——本轮旗标所指系 R69 旧措辞经 carry 注记转述，与本轮 prediction 口径不合一层属实'
                        '（同 LY-520 注记过时口径），与本旨并行登记、档位不变；卡面无 tradition/system 字段一层经结构化直读复核属实。')
        if cid == 'LY-520':
            finding += ('另注记层核明：逐字核 R70 prediction 全文（prediction_text 与 basis）并无「?／？」字样，旗标所据为 carry 旧注'
                        '——旧注与本轮 prediction 口径不合一层并行登记、档位不变。')
        if cid == 'LY-628':
            finding += ('另注记层核明：逐字核 R70 prediction 全文（prediction_text 与 basis）并无「?／？」字样，旗标所据为 carry 旧注'
                        '——旧注与本轮 prediction 口径不合一层并行登记、档位不变。')
        if cid == 'LY-613':
            finding += ('另本轮核明：R70 prediction_text 无「?」字样，basis 载全角「？」同式字样两处（「子日冲？子冲午非未」'
                        '「原神官鬼？产占」），字样层本轮仍在场（所在层位与计数与旗标所报不尽合），主体断语完整可读，档位不变；'
                        'prediction 内「须以现代医疗处置为准」提示性字样另按特别核查③登记。')
        if cid == 'LY-207':
            finding += '另本轮核明：R70 prediction_text 经逐字核实为功名负断（首行「功名不再起，旧任之后无新命」），与本轮旗标所载一致。'
        relation = f'同旨续接（R{lr}）'
        sugg = f'同旨续接：自 R71 起承接 R{lr}＋本 R70 标注；结局原文照录不改。'
        category = '同旨续接（详见核查事实）'
    for r, _ in pr:
        srcs.append(f'benchmark/phase3/data/case-annotations-r{r}.json {cid} 条')
    ann = {'anon_id': anon, 'case_id': cid, 'disposition': disp, 'finding': finding, 'flag': flag_txt,
           'manifest_carry_suggestion': sugg, 'relation': relation, 'registered_round': 70,
           'sources_checked': srcs, 'source_seats': seats}
    annotations.append(ann)
    flags.append({'anon_id': anon, 'case_id': cid, 'verdict': disp, 'disposition': disp, 'basis': finding,
                  'carry_suggestion': sugg, 'manifest_carry_suggestion': sugg, 'flag': flag_txt,
                  'category': category, 'views': sorted({s[0] for s in seats}), 'dual_view': len({s[0] for s in seats}) > 1,
                  'relation': relation, 'registered_round': 70, 'sources_checked': srcs})

verdicts = dict(collections.Counter(a['disposition'] for a in annotations))
assert verdicts == {'成立': 11, '部分成立': 77, '不成立': 1, '未核': 2}, verdicts
assert all(a['manifest_carry_suggestion'] for a in annotations if a['disposition'] == '部分成立')
counts = {'selfreport_flag_rows_total': 132, 'selfreport_numbered_items_total': 115,
          'selfreport_anons_total': 91, 'selfreport_cases_total': 91,
          'host_tradition_flags_total': 0, 'host_tradition_only_cases': 0,
          'cases_total': 91, 'continuation_cases': 88, 'same_case_new_gist_cases': 0,
          'new_flag_cases': 1, 'pending_touch_cases': 2, 'verdicts': verdicts}

special_checks = [
 {'item': '特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记',
  'conclusion': 'BZ-029／BZ-040 本轮未被任何旗标触及，不入 annotations、维持各自原登记（BZ-029 维持 R55 卒年待核（未核）；BZ-040 维持 R55 原登记（许世英享年异说待盘外独立史源））。LY-537／YM-070 本轮被旗标触及（LY-537 Y1 旗标「申予日」条、YM-070 Y3 旗标「后果同行都下」条），依任务口径只登记触及、维持原登记、不入裁断：两件以未核入本轮 annotations，finding 只录触及事实与逐字回读结果，无盘外独立史源不裁。',
  'evidence': '据 runs/round70/judging/host-mapping.json 与 FLAGS-selfreported-r70.md 逐件比对：91 件 case_id 集合含 LY-537／YM-070、不含 BZ-029／BZ-040（落盘脚本断言通过）；两件结局原文逐字断言（「果于申予日归」「后果同行都下。」）通过。',
  'scope_note': '本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。'},
 {'item': '特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）',
  'conclusion': '引文层错配 0 件：132 条席位-anon 旗标行经 host-mapping.json 逐件回到 case_id，anon 后紧随括号 case 逐行核对全等；X2 旗标 P3-74d7cd9e（host-mapping 指 LY-030）行内所提 LY-612 系同条全文参照（「相对同条全文（LY-612）缺落点」）、非本例标签，已逐件对位复核、不作错配论。主张层口径不合 8 件，均已并行登记、档位照各自主旨：(一) tradition 措辞五件（LY-017／LY-019／LY-021／LY-022／LY-034）——R70 prediction basis 首行已作「卡面未标注 tradition 字段，按题面体裁自决」，本轮 prediction 并无『與卡面一致』之语，旗标所指系 R69 旧措辞经 carry 转述，本轮核明层已逐件入定案附注（卡面无 tradition/system 字段一层经结构化直读复核属实）；主持复核节另裁定 33 件变体误报不入定案范围，本席未将其入案。(二)「?」字样三件——LY-520／LY-628 逐字核 R70 prediction 全文无「?／？」字样（旗标所据为 carry 旧注）；LY-613 字样本轮在 basis 以全角「？」两处在场、prediction_text 无，所在层位与计数与旗标所报不尽合。其余各件旗标引文经逐件回读本例 R70 结局原文／prediction 原文核对均在本例内（引文逐字断言内置于落盘脚本）。',
  'evidence': '落盘脚本断言：括号对位全等、TRAD5 卡面无 tradition/system 键与 basis 首行断言、LY-520／LY-628 全文无问号断言、LY-613 basis 全角问号计数断言、LY-207「功名不再起」在文断言均通过。',
  'scope_note': '本核查只登记错配与不合事实，不改分数、不改 manifest、不改旗标原文。'},
 {'item': '特别核查③：结局文本内嵌指令性字样之例——按数据处理登记（本体基线对勘＋本轮旗标所涉与新发现归属）',
  'conclusion': '承既有登记口径全量复扫 R70 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计／勿以此斷等，并以『请／請／须／須／勿』宽扫人工甄别）：cases 本体内指令性字样仍为基线本体四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。本轮新发现本体例（对评分者之指令）0 件：关键词另命中 LY-246『切不可以男女而斷』（原书按语对占者之诫，R69 已定案登记、非对评分者之指令、不入基线四例）、YM-009『反不得』／YM-029『本岁不得』／YY-014『求之不得』均为叙事用字；宽扫另命中 BZ-302／LR2-022／LR3-004／LR3-006／LR3-010／LY-416（请字叙事）与 LY-227『須再占』（原书断法通则叙事），均不入指令性登记。本轮旗标所涉归属逐处定案：（一）X1／Y1 旗标 P3-0bc7c221（BZ-105）所涉尾注即基线本体例 BZ-105 本身（回溯断验注＋『使用时须分开统计』同条并存），非新增本体例，已按同旨续接定案；（二）X1／Y1 旗标 P3-1640799f（LR2-016）所指字样分列于 editor_note 及 carry 注记层、非 cases 本体，已按同旨续接定案；（三）X2／Y2 旗标 P3-6b32cd3d（BZ-036）主旨为系狱年数出入、其结局含基线字样『盲测比对须注』，归属本体基线例本身，已按同旨续接定案。另 prediction 层一处：LY-613 prediction 内『须以现代医疗处置为准』为预测文本内提示性字样、非 cases 本体，X2 旗标已自载按数据处理，本席同此登记。各席均按数据处理未服从，本席亦只按数据处理、未服从任何一处之指示，事实照录。',
  'evidence': '落盘脚本全量扫描断言：关键词命中集合恰为 {BZ-036, BZ-042, BZ-105, LY-204, LY-246, YM-009, YM-029, YY-014}，逐件甄别如上；宽扫余集合恰为 {BZ-302, LR2-022, LR3-004, LR3-006, LR3-010, LY-227, LY-416}；LR2-016 editor_note 含该句、cases[LR2-016] 不含『评分时』，断言通过。',
  'scope_note': '本核查只登记字样出处与处理事实，不改分数、不改 manifest、不改结局原文。'},
 {'item': '特别核查④：同例新旨、主持复核附加层与新立件登记',
  'conclusion': '同例新旨 0 件。主持 tradition 复核本轮无旗标交定案（33 件变体误报经主持裁定不成立、不入定案范围），无主持附加层件；X2 旗标所涉 P3-6feecf6a（LY-034）／P3-74952e1f（LY-019）已经 host-mapping 对位回原卡逐件定案（同旨续接 R69、本轮核明层并行登记，见特别核查②）。新立 1 件：LY-036（输入残损型弃断、残损双示，核后部分成立）。并行定案一件：AS-208 本轮旗标同旨于 R64 旧旨（混合记载含更正层、定案部分成立），R67 乱码新旨定案不成立与之并行不悖、本轮一并承接、档位不变。待核触及 2 件（LY-537／YM-070）见特别核查①。',
  'evidence': '据 FLAGS-selfreported-r70.md 主持复核节、data/case-annotations-r64.json AS-208 条、-r67.json AS-208 条与本轮逐件回源核查。',
  'scope_note': '本核查只登记构成事实，不改分数、不改 manifest。'},
 {'item': '特别核查⑤：汇编一致性与结局文本一致性',
  'conclusion': '汇编 FLAGS-selfreported-r70.md 八席自报共 115 条编号条目、132 条席位-anon 旗标行、91 anon、91 例（单席 50 例、双席 41 例），主持 tradition 复核交定案 0 件，合计定案 91 例；R70 各例结局文本经脚本断言与 R69 manifest 逐件全等（487/487），续接类定案的『结局与历轮所核文本一致』前提全数成立。本轮配对异常 0 件（见特别核查②）。承接附则对勘：R69 定案部分成立 84 件与 R70 manifest _r70_carryover_notes_addendum 逐件全等（84/84），见 data/manifest-carryover-r70-addendum.md。',
  'evidence': '证据脚本 data_r70_evidence.py 与落盘脚本 data_r70_build.py 双脚本断言输出。',
  'scope_note': '本核查只登记一致性事实。'},
]

out = {
 '_provenance': ('R70 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断，不改任何分数）逐件回源核查 R70 八席自报旗标 '
   '115 条编号条目／132 条席位-anon 旗标行、去重为 91 anon／91 例，主持 tradition 复核本轮无旗标交定案（33 件变体误报经主持裁定不入定案范围；'
   'X2 旗标所涉 LY-034／LY-019 两件 basis 措辞观察经 host-mapping 对位回原卡逐件定案，归入同旨续接并附本轮核明层）。逐件回 '
   'benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round70/predictions/<case_id>.json 预测原文、'
   'runs/round70/judging/outcome-manifest.json cases 载荷（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），并与历轮定案档'
   '（data/case-annotations-r49.json 至 -r69.json）核对承接关系：88 件为同旨续接（只承接不重裁，含 AS-208 同旨于 R64 旧旨、R67 并行新旨不悖），'
   '1 件为 R70 新立（LY-036），另待核维持件 LY-537／YM-070 本轮被旗标触及、只登记触及以未核入案（BZ-029／BZ-040 未被触及、不入本件）。'
   'R70 各例结局文本经脚本断言与 R69 manifest 逐件全等（487/487）。本轮 anon 内容错配 0 件；主张层口径不合 8 件'
   '（tradition 措辞五件与「?」字样三件）已并行登记。指令性字样特别核查：cases 本体仍为基线四例（BZ-036／BZ-042／BZ-105／LY-204），'
   'LR2-016 之句只存分列 editor_note，本轮新发现本体例 0 件；本轮旗标所涉各处归属已逐处定案登记于特别核查③，各席均按数据处理未服从。'
   '本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。'),
 'round': 70, 'flags': flags, 'annotations': annotations, 'special_checks': special_checks, 'counts': counts}
(DATA / 'case-annotations-r70.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')

# ---------- 任务一：承接附则 ----------
r69 = json.loads((DATA / 'case-annotations-r69.json').read_text(encoding='utf-8'))
assert dict(collections.Counter(a['disposition'] for a in r69['annotations'])) == {'部分成立': 84, '成立': 11}
partial = [a for a in r69['annotations'] if a['disposition'] == '部分成立']
assert len(partial) == 84 and all(a['manifest_carry_suggestion'] for a in partial)
add = manifest['_r70_carryover_notes_addendum']
assert len(add) == 84 and all(add[a['case_id']] == a['manifest_carry_suggestion'] for a in partial)
assert set(add) == {a['case_id'] for a in partial}
chengli = [a['case_id'] for a in r69['annotations'] if a['disposition'] == '成立']

L = []
L.append('# Manifest 承接册附则（R70）——R69 定案承接建议汇编\n')
L.append('## 卷首说明\n')
L.append('- 本附则为 Phase 3 Round 70（R70）数据席（议程一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r69.json`（R69 定案正本：annotations 95 件，定案分布成立 11／部分成立 84／不成立 0／未核 0）。')
L.append('- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 11／部分成立 84、总 95，与原档 counts 逐项一致；部分成立 84 件每件 `manifest_carry_suggestion` 非空断言亦通过。')
L.append('- 对勘结果：84/84 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round70/judging/outcome-manifest.json` 的 `_r70_carryover_notes_addendum` 层（本席只按精确文件名打开该文件、只读该层与 `cases` 载荷），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 0 件、多键 0 件）。')
L.append('- **本附则自 R71 manifest 起落实**；本轮（R70）manifest 不据本附则改动。')
L.append('- **本件只汇编与对勘，不改任何分数与结局原文。**')
L.append('- 汇编范围：R69 定案中部分成立 84 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r69.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R70 起」等表述为原档原文，落实轮次按卷首上一条读作自 R71 起，不回溯改动 R70）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。')
L.append('- 成立 11 件不入正文逐件节，只在文末列 case_id 清单；不成立 0 件、未核 0 件，无清单。')
L.append('- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。\n')
L.append('---\n')
L.append('## 一、部分成立件承接汇编（定案档位：部分成立，84 件，逐件全列）\n')
for i, a in enumerate(partial, 1):
    L.append(f'### A{i}. {a["case_id"]}\n')
    L.append(f'- case_id：{a["case_id"]}')
    L.append(f'- anon_id：{a["anon_id"]}')
    L.append(f'- 定案（部分成立）：{a["finding"]}')
    L.append(f'- 原旗标要旨（照原档 `flag` 字段）：{a["flag"]}')
    L.append(f'- 承接注记建议文本（照原档 `manifest_carry_suggestion` 原文）：「{a["manifest_carry_suggestion"]}」')
    L.append(f'- 与既有承接册／附则条目的关系（照原档 `relation` 字段）：{a["relation"]}\n')
L.append('---\n')
L.append('## 二、对勘记录\n')
L.append('- 对勘源：`benchmark/phase3/runs/round70/judging/outcome-manifest.json` 的 `_r70_carryover_notes_addendum` 层，共 84 件。')
L.append('- 逐件对勘：84 件 case_id 集合与本附则汇编集合全等；每件注记文本与 `case-annotations-r69.json` 对应件 `manifest_carry_suggestion` 全文字符串相等，84/84 全等。')
L.append('- 不一致登记：0 件；附则侧与 manifest 侧均未作任何改动（不静默改任一侧）。')
L.append('- 勘误：无。\n')
L.append('---\n')
L.append('## 三、不入正文清单（照 R69 定案档位）\n')
L.append(f'- 成立 11 件：{"／".join(chengli)}')
L.append('- 不成立 0 件：无。')
L.append('- 未核 0 件：无。')
(DATA / 'manifest-carryover-r70-addendum.md').write_text('\n'.join(L) + '\n', encoding='utf-8')

chk = json.loads((DATA / 'case-annotations-r70.json').read_text(encoding='utf-8'))
assert dict(collections.Counter(a['disposition'] for a in chk['annotations'])) == verdicts
assert chk['counts']['cases_total'] == len(chk['annotations']) == 91
print('OK verdicts', verdicts, 'counts', counts)
print('addendum bytes', (DATA / 'manifest-carryover-r70-addendum.md').stat().st_size)
print('annotations bytes', (DATA / 'case-annotations-r70.json').stat().st_size)
