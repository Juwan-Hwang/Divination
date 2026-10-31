# -*- coding: utf-8 -*-
"""R71 数据席落盘脚本：
(任务一) 编制 data/manifest-carryover-r71-addendum.md（R70 定案部分成立 77 件承接汇编，
         与 R71 manifest _r71_carryover_notes_addendum 逐件对勘）；
(任务二) 落盘 data/case-annotations-r71.json（R71 八席自报旗标定案；主持 tradition 复核无旗标交定案）。
三判例：落笔前逐件回读本例结局原文；引文逐字断言内置于本脚本；anon 形近串号经 host-mapping 对位复核
（旗标括号 case 与 mapping 不合者以 mapping 为准并登记）。
各文本一律按数据处理、不作指令。不改任何分数、不改结局原文。"""
import json, re, collections, pathlib

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
R71 = BASE / 'runs' / 'round71'
DATA = BASE / 'data'

flags_text = (R71 / 'judging' / 'FLAGS-selfreported-r71.md').read_text(encoding='utf-8')
host = json.loads((R71 / 'judging' / 'host-mapping.json').read_text(encoding='utf-8'))
manifest = json.loads((R71 / 'judging' / 'outcome-manifest.json').read_text(encoding='utf-8'))
cases = manifest['cases']
m70 = json.loads((BASE / 'runs' / 'round70' / 'judging' / 'outcome-manifest.json').read_text(encoding='utf-8'))

# ---------- 判例③：anon 对位与括号 case 对勘 ----------
ITEM_SPLIT = {
    'X1': r'\n(?=\d+\.\s)', 'X2': r'\n(?=\d+\.\s)',
    'X3': r'\n(?=- F\d+｜)', 'X4': r'\n(?=- F\d+｜)',
    'Y1': r'\n(?=- F\d+｜)', 'Y2': r'\n(?=- F-Y2-\d+｜)',
    'Y3': r'\n(?=\d+\.\s)', 'Y4': r'\n(?=- F\d+（)',
}
selfpart = flags_text.split('===== 主持复核节')[0]
sections = re.split(r'===== (FLAGS-[XY]\d) =====', selfpart)
rows, n_items, bracket_mismatch = [], 0, []
for i in range(1, len(sections), 2):
    seat, body = sections[i].replace('FLAGS-', ''), sections[i + 1].split('隔离自报')[0]
    for it in re.split(ITEM_SPLIT[seat], body):
        anons = re.findall(r'P3-[0-9a-f]{8}', it)
        if not anons:
            continue
        n_items += 1
        txt = re.sub(r'\s+', ' ', it).strip()
        for a in dict.fromkeys(anons):
            assert a in host, f'anon 不在 host-mapping: {a}'
            for pat in (a + r'[（(]([A-Z]{2,3}\d?-\d+)', a + r' / ([A-Z]{2,3}\d?-\d+)'):
                mm = re.search(pat, txt)
                if mm and mm.group(1) != host[a]:
                    bracket_mismatch.append((seat, a, mm.group(1), host[a]))
            rows.append((seat, a, txt))
assert bracket_mismatch == [('X2', 'P3-468cd1e2', 'LY-023', 'LR2-018')], bracket_mismatch
anon2rows = collections.defaultdict(list)
for s, a, t in rows:
    anon2rows[a].append((s, t))
assert len(anon2rows) == 105 and len(rows) == 159 and n_items == 147, (len(anon2rows), len(rows), n_items)
case2anon = {host[a]: a for a in anon2rows}
assert len(case2anon) == 105

# ---------- 判例①②：结局原文回读与逐字引文断言 ----------
assert len(cases) == 487
assert all(cases[c] == m70['cases'][c] for c in cases), 'R71 结局与 R70 不全等'
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
assert cases['LY-432'] == '五月高遷。 次日卽愈。'
assert cases['YY-022'] == '后果然。'
assert cases['LR2-018'] == '后曹大司礼奉命热审，开豁谪戍。'
assert cases['LY-023'] == '果於八月其子驚風（其後復占子病，見 LY-024）'
assert cases['LY-516'].startswith('果得眞定。') and '以初爻爲內地' in cases['LY-516']
assert 'He dyed the fourteenth of August following' in cases['AS-204']
assert '后知来占者为赵忻城昆弟' in cases['OC-026'] and '授京营提督' in cases['OC-026']
assert '赵忻城' not in cases['OC-012'] and '京营提督' not in cases['OC-012'] and '杨秀琼' in cases['OC-012']
assert cases['LY-445'] == '果於寅日云卯日大雨辰日大晴。'
assert '1934年称帝，为日本傀儡' in cases['OC-010'] and '\ufffd' not in cases['OC-010']
assert '连署后于2023-11-24宣布退选' in cases['MP-010'] and '\ufffd' not in cases['MP-010']
assert not any('\ufffd' in t for t in cases.values()), 'cases 本体含替换字符'

def pred(cid):
    return json.loads((R71 / 'predictions' / f'{cid}.json').read_text(encoding='utf-8'))

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

TRAD4 = ['LY-017', 'LY-019', 'LY-021', 'LY-034']
for cid in TRAD4:
    c, p = card(cid), pred(cid)
    assert 'tradition' not in all_keys(c) and 'system' not in all_keys(c), cid
    assert p['basis'].startswith('卡面未标注 tradition'), cid
    assert '與卡面一致' not in p['basis'] and '與卡面一致' not in p['prediction_text'], cid
for cid in ('LY-520', 'LY-613'):
    p = pred(cid)
    assert '?' not in p['prediction_text'] and '？' not in p['prediction_text'], cid
    assert '?' not in p['basis'] and '？' not in p['basis'], cid
p628 = pred('LY-628')
assert '?' not in p628['prediction_text'] and p628['basis'].count('?') == 1 and '辰土生?' in p628['basis']
p036 = pred('LY-036')
assert '难定而偏不成' in p036['prediction_text'] and '不报方向' not in p036['prediction_text']
c332 = card('LY-332')
assert c332['context']['attachments']['yongshen'] == '官鬼午火为用神'
assert any('官鬼巳火' in line for line in c332['context']['attachments']['chart_lines_top_to_bottom'])
assert '从化官午火与巳火两现合参并记存疑' in pred('LY-332')['prediction_text']
for cid, clean in (('YM-037', '原神兄弟亥水'), ('YM-048', '父母丑土')):
    raw = (R71 / 'predictions' / f'{cid}.json').read_text(encoding='utf-8')
    assert '\ufffd' not in raw and clean in pred(cid)['prediction_text'], cid

# ---------- 历轮定案索引 ----------
prior = {}
for r in range(49, 71):
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

# ---------- 旗标文本（组条目逐件要旨覆写，键为 (seat, anon)） ----------
OVERRIDE = {
 ('X1', 'P3-28d1139c'): '总承式结局（「后果然」）、断面未分载（X1 于 LY-528 条下同类并提）',
 ('X1', 'P3-334c4b7e'): '总承＋时点式结局、事件未分载（X1 于 LY-528 条下同类并提）',
 ('X1', 'P3-155bb28c'): '结局大半为断语解释层（X1 于 YY2-001 条下同类并提）',
 ('X1', 'P3-17943f0f'): '结局含断语解释层混入（X1 于 YY2-001 条下同类并提）',
 ('X1', 'P3-24ee723f'): '结局含断语解释层混入（X1 于 YY2-001 条下同类并提）',
 ('X1', 'P3-39142f41'): '结局括注含编者评价层（X1 于 YY2-001 条下同类并提）',
 ('X1', 'P3-1901070d'): '卡面无 tradition/system 字段、basis 首行『與卡面一致』措辞不实（tradition 值与体裁一致、无 value 误标）',
 ('X1', 'P3-31551bad'): '卡面无 tradition/system 字段、basis 首行『與卡面一致』措辞不实（tradition 值与体裁一致、无 value 误标）',
 ('X1', 'P3-38734ec4'): '卡面无 tradition/system 字段、basis 首行『與卡面一致』措辞不实（tradition 值与体裁一致、无 value 误标）',
 ('X4', 'P3-c61639b4'): '结局以逗号收尾、疑似截断「後應申月所請準﹐酉歲迎靈而歸﹐」，主结局明载（X4 合并登记）',
 ('X4', 'P3-d424eeae'): '结局以逗号收尾、疑似截断「果卒於甲戌日﹐」，主结局明载（X4 合并登记）',
 ('X4', 'P3-f3849008'): '结局以逗号收尾、疑似截断「至七月城破与官府一同被害，」，主结局明载（X4 合并登记）',
 ('X4', 'P3-fffe1950'): '结局以逗号收尾、疑似截断「後報升於巳月﹐」，主结局明载（X4 合并登记）',
 ('X4', 'P3-d79a72f9'): '结局自注卒年不详于所据来源、终局时点无从核验（已自注）',
 ('X4', 'P3-e7d485aa'): '结局原文自注「其晚年败落细节本数据集所据来源未备……待另核」',
 ('X4', 'P3-c49a9dad'): '结局仅一句干支日记录（如「果於寅日云卯日大雨辰日大晴」），prediction 的机理类子断语无从逐条核验（X4 合并登记）',
}

def clean_flag(seat, anon, txt):
    if (seat, anon) in OVERRIDE:
        return f'{seat}：{OVERRIDE[(seat, anon)]}'
    t = re.sub(r'^\d+\.\s*', '', txt)
    t = re.sub(r'^- F[-\w]*\d*\s*｜\s*', '', t)
    t = re.sub(r'^- F\d+（' + anon + r'\s*/\s*[^）]*）：\s*', '', t)
    t = re.sub(r'^anon_id\s+', '', t)
    t = re.sub(r'^' + anon + r'\s*[（(][^）)]*[）)]\s*[：::]?\s*', '', t)
    t = re.sub(r'^' + anon + r'\s*[｜—：:]\s*', '', t)
    return f'{seat}：{t.strip()}'

# ---------- 新立件定案（逐件回原卡核毕） ----------
NEW = {
 'LR2-018': ('不成立',
   '新旗标（R71 新立）：anon 形近串号对位复核——X2 旗标 P3-468cd1e2 括号作（LY-023），经 host-mapping 逐件对位，该 anon 指 LR2-018，以 mapping 为准登记。回原卡核对：LR2-018 所问吴振缨被逮、刑部已定重辟吉凶，R71 manifest 结局「后曹大司礼奉命热审，开豁谪戍。」；旗标所述母病终局未载、子惊风对应迁移断面等情在本例卡面、结局与 prediction 中均无对应，所述引文「果於八月其子驚風（其後復占子病，見 LY-024）」实为 LY-023 结局原文（LY-023 本轮另由 Y2 旗标 P3-45feb719 正确对位自报、已按同旨续接定案）。旗标内容与本例不合，故不成立。',
   '新立定案：自 R72 起承接本 R71 标注（旗标不成立、括号 case 与 mapping 不合以 mapping 为准登记）；结局原文照录不改。'),
 'AS-204': ('不成立',
   '新旗标（R71 新立）：anon 对位复核——X4 旗标 P3-fae17093 经 host-mapping 指 AS-204（旗标未附括号 case）。回原卡核对：AS-204 为 Lilly 病占例（问患病医生之病位／病性／可治否），R71 manifest 结局为症状叙述并以「He dyed the fourteenth of August following」收束；旗标所述「个案结局仅『果得真定』、后半混入断法通则」在本例卡面、结局与 prediction 中均无对应——该引文实为 LY-516 结局原文（「果得眞定。又有以初爻爲內地…」），LY-516 本轮未被自报旗标触及。旗标内容与本例不合，故不成立。',
   '新立定案：自 R72 起承接本 R71 标注（旗标不成立、内容错配登记）；结局原文照录不改。'),
 'OC-012': ('不成立',
   '新旗标（R71 新立）：回原卡核对——OC-012 所问游泳冠军命主成名、婚姻与一生行运，R71 manifest 结局载其 1937 年结婚、后移居香港北美、1982 年卒于温哥华，主语单一；Y1 旗标所引「后知来占者为赵忻城昆弟；果于是年六月奉诏进京，授京营提督」经全量检索实为 OC-026 结局原文、不在本例，本例亦无昆弟二人分断与结局主语未分载情事。旗标内容与本例不合，故不成立。',
   '新立定案：自 R72 起承接本 R71 标注（旗标不成立、引文错配登记）；结局原文照录不改。'),
 'OC-010': ('不成立',
   '新旗标（R71 新立）：回源逐字核——Y2 旗标称 outcome_record 含替换字符乱码一处（「1934年称��，为日本傀儡」）；逐字回读 R71 manifest cases[OC-010] 原文作「1934年称帝，为日本傀儡」，全例无 U+FFFD 替换字符（断言通过），且本轮 487 例 cases 本体无一例含替换字符。旗标所指字样不在盘上文本，故不成立（字样或系评审侧转码产物，按盘上原文登记）。',
   '新立定案：自 R72 起承接本 R71 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。'),
 'MP-010': ('不成立',
   '新旗标（R71 新立）：回源逐字核——Y2 旗标称 outcome_record 含替换字符乱码一处（「郭台铭独立参选连署后��2023-11-24宣布退选」）；逐字回读 R71 manifest cases[MP-010] 原文作「郭台铭独立参选连署后于2023-11-24宣布退选」，全例无 U+FFFD 替换字符（断言通过）。旗标所指字样不在盘上文本，故不成立（按盘上原文登记）。',
   '新立定案：自 R72 起承接本 R71 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。'),
 'YM-037': ('不成立',
   '新旗标（R71 新立）：回源逐字核——Y2 旗标称 prediction_text 含替换字符乱码一处（「原神���弟亥水两见于变爻」）；逐字回读 R71 runs/round71/predictions/YM-037.json 原始文件，prediction_text 与 basis 均无 U+FFFD 替换字符（断言通过），对应文句在盘上作「原神兄弟亥水两见于变爻」、文义完整。旗标所指字样不在盘上文本，故不成立（按盘上原文登记）。',
   '新立定案：自 R72 起承接本 R71 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。'),
 'YM-048': ('不成立',
   '新旗标（R71 新立）：回源逐字核——Y2 旗标称 prediction_text 含替换字符乱码一处（「二爻财动化父母��土而丑临空」）；逐字回读 R71 runs/round71/predictions/YM-048.json 原始文件无 U+FFFD 替换字符（断言通过），对应文句在盘上作「二爻财动化父母丑土而丑临空」、文义完整。旗标所指字样不在盘上文本，故不成立（按盘上原文登记）。',
   '新立定案：自 R72 起承接本 R71 标注（旗标不成立、盘上文本无该字样登记）；结局原文照录不改。'),
 'LY-332': ('部分成立',
   '新旗标（R71 新立）：回原卡——所问「占会试」；原卡 attachments.yongshen 明载「官鬼午火为用神」，而逐爻表（chart_lines_top_to_bottom）官鬼作巳火两现，用神指针与逐爻表不合属实；R71 prediction 文末已自注此不合（「卡面用神作官鬼午火，与逐爻表官鬼巳火不合，从化官午火与巳火两现合参并记存疑」），basis 亦两说并记——不合属实但已自注双记，结局「果中探花．」明载。故部分成立（同 AS-008 双处自注口径）。',
   '同旨新立：自 R72 起承接本 R71 标注：按「卡面用神官鬼午火与逐爻表官鬼巳火不合、prediction 已自注并记存疑」登记；结局原文照录不改。'),
 'LY-445': ('部分成立',
   '新旗标（R71 新立）：回原卡——所问「占何日雨（三占合斷）」；R71 manifest 结局仅「果於寅日云卯日大雨辰日大晴。」一句干支日记录，X4 合并登记所举之例即本例原文，单句纪录属实；prediction 合断主坐标为亥日有雨，结局未载亥日、机理类子断语无从逐条核验一层属实；但结局并非全无记载，寅日云、卯日大雨、辰日大晴逐日有载、卯日雨面可核。故部分成立。',
   '同旨新立：自 R72 起承接本 R71 标注：按「结局仅一句干支日记录、亥日未载、机理类子断语无从逐条核验」登记；结局原文照录不改。'),
 'YM-053': ('部分成立',
   '新旗标（R71 新立）：回原卡——所问「占女身（女病吉凶）」；R71 manifest 结局「其女不死；中男相继而病，及甲申旬中男反亡。」——女不死一面有载，但结局并载中男相继病亡之旁及他人断面、女愈时点未载，所指属实；主问女病终局（不死）本身有对应记载。故部分成立。',
   '同旨新立：自 R72 起承接本 R71 标注：按「结局旁及中男病亡混载、女愈时点未载」登记；结局原文照录不改。'),
}

# ---------- 续接件本轮核明附注 ----------
APPEND = {
 'LY-017': '另本轮核明：逐字核 R71 prediction basis 首行作「卡面未标注 tradition 字段，按题面体裁自决」，本轮 prediction 并无『與卡面一致』之语——本轮旗标所指系旧措辞经 carry 注记转述，与本轮 prediction 口径不合一层属实（同 R70 五件口径），与本旨并行登记、档位不变；卡面无 tradition/system 字段一层经结构化直读复核属实。',
 'LY-019': '另本轮核明：逐字核 R71 prediction basis 首行作「卡面未标注 tradition 字段，按题面体裁自决」，本轮 prediction 并无『與卡面一致』之语——本轮旗标所指系旧措辞经 carry 注记转述，与本轮 prediction 口径不合一层属实，与本旨并行登记、档位不变；卡面无 tradition/system 字段一层经结构化直读复核属实。',
 'LY-021': '另本轮核明：逐字核 R71 prediction basis 首行作「卡面未标注 tradition 字段，按题面体裁自决」，本轮 prediction 并无『與卡面一致』之语——本轮旗标所指系旧措辞经 carry 注记转述，与本轮 prediction 口径不合一层属实，与本旨并行登记、档位不变；卡面无 tradition/system 字段一层经结构化直读复核属实。',
 'LY-034': '另本轮核明：逐字核 R71 prediction basis 首行作「卡面未标注 tradition 字段，按题面体裁自决」，本轮 prediction 并无『與卡面一致』之语——本轮旗标所指系旧措辞经 carry 注记转述，与本轮 prediction 口径不合一层属实，与本旨并行登记、档位不变；卡面无 tradition/system 字段一层经结构化直读复核属实。',
 'LY-520': '另注记层核明：逐字核 R71 prediction 全文（prediction_text 与 basis）并无「?／？」字样，旗标所据为 carry 旧注——旧注与本轮 prediction 口径不合一层并行登记、档位不变。',
 'LY-613': '另注记层核明：逐字核 R71 prediction 全文（prediction_text 与 basis）并无「?／？」字样（R70 轮 basis 曾载全角「？」两处、本轮已无），Y2 旗标亦自注回读 prediction_text 未见该占位字——字样层本轮不在场，旗标所据为 carry 旧注，注记层不合一层并行登记、档位不变。',
 'LY-628': '另本轮核明：逐字核 R71 prediction——prediction_text 无「?」字样，basis 载半角「?」一处（「辰土生?世持」），字样本轮仍在场（所在层位为 basis 行文、非爻位），计数与旗标所报一处合，主体断语完整可读，档位不变。',
 'LY-222': '另本轮核明：R71 prediction 明言失散之子归否「记有面无据不报」、主断子嗣可再有，结局「果於次年六月父子相逢」对应其自承不报之面，与既有改断面定案口径一致，档位不变。',
 'LY-430': '另本轮核明：逐字核 R71 prediction_text 确仅载掣签到任断面、无病死断语（与 X3 旗标所读一致），再占危灾断面系大师原断层面、本轮 prediction 未载，与本旨并行登记、档位不变。',
 'LR2-016': '另本轮核明：X4 旗标所涉「评分时该细项请按未完全复核处理」一语只存于 manifest 分列 _r56_lr2016_split 的 editor_note、不在 cases 本体，各席与本席均按数据处理未服从，归属登记另见特别核查③，档位不变。',
 'BZ-036': '另归属登记：本例结局含基线指令性字样『盲测比对须注』，即特别核查③本体基线例本身、非新增本体例，各席均按数据处理。',
 'BZ-105': '另归属登记：本例结局含基线指令性字样『使用时须分开统计』，即特别核查③本体基线例本身、非新增本体例，各席均按数据处理。',
 'LY-204': '另归属登记：Y3 旗标所涉旧注层『勿以此斷』即特别核查③本体基线例本身，各席与本席均按数据处理未服从。',
 'BZ-042': '另归属登记：本例结局含基线注记『（盲测比对时以格局大富一项为主）』，即特别核查③本体基线例本身；本轮旗标主旨为晚年败落细节来源未备一层，与字样层并行登记。',
}

# ---------- 定案组装 ----------
PENDING = {'YM-070'}
annotations, flags = [], []
for cid in sorted(case2anon):
    anon = case2anon[cid]
    srows = anon2rows[anon]
    seats = sorted({s for s, _ in srows})
    flag_txt = '；'.join(clean_flag(s, anon, t) for s, t in srows)
    srcs = [f'benchmark/phase3/inputs-dev12/{cid}.json',
            'benchmark/phase3/runs/round71/judging/FLAGS-selfreported-r71.md',
            f'benchmark/phase3/runs/round71/judging/outcome-manifest.json cases[{cid}]',
            f'benchmark/phase3/runs/round71/predictions/{cid}.json']
    pr = prior.get(cid, [])
    if cid in PENDING:
        disp = '未核'
        finding = ('待核维持（本轮旗标触及、只登记不裁）：X2／Y2 旗标登记结局措辞「后果同行都下」语义未明'
                   '——逐字回读 R71 结局原文确作『后果同行都下。』，触及属实；本例维持 R68 未核原登记'
                   '（『都下』语义未明＋『甲寅旬』出处待核并列、无盘外独立史源不裁），本轮只登记触及、不入裁断。')
        relation = '待核维持（旗标触及、只登记不裁）'
        sugg = '待核维持：自 R72 起维持原登记（『都下』语义未明＋『甲寅旬』出处待核、无盘外独立史源不裁）；结局原文照录不改。'
        category = '待核维持（旗标触及、只登记不裁）'
    elif cid == 'LY-036':
        disp = '部分成立'
        finding = ('同例新旨（R70 旧旨『卡面逐爻表不录、prediction 自承六爻全缺不报方向、残损已双示』定案部分成立、'
                   '本轮新旨与之各旨独立）：回原卡与本轮 prediction——逐字核 R71 prediction_text 首行作'
                   '「终局单一方向：难定而偏不成（negative）——升选本月内难落实」，实含方向断；Y2 旗标所指 carry_note '
                   '登记「prediction 自承六爻全缺不报方向」，与本轮 prediction_text 口径不合属实（同 LY-207 R69 '
                   '注记过时口径）；卡面逐爻表不录之残损与结局（本月升任山东、未及一载复任江西）明载均如旧旨所核。故部分成立。')
        relation = '同例新旨（R70 旧旨并行、本轮新旨另立）'
        sugg = ('同例新旨：自 R72 起承接本 R71 标注（与 R70 旧旨定案并行、各旨独立）：按「carry_note 所称 prediction '
                '不报方向与 R71 prediction_text 实含『难定而偏不成』方向断口径不合」登记；结局原文照录不改。')
        category = '同例新旨（详见核查事实）'
        srcs.append('benchmark/phase3/data/case-annotations-r70.json LY-036 条')
    elif cid in NEW:
        disp, finding, sugg = NEW[cid]
        relation = '新旗标（R71 新立）'
        category = '新旗标（R71 新立）'
        srcs.append('benchmark/phase3/data/case-annotations-r49.json 至 -r70.json（去重检索无本 case_id 条目）')
        if cid == 'LR2-018':
            srcs.append('benchmark/phase3/runs/round71/judging/host-mapping.json P3-468cd1e2 对位（括号 LY-023 与 mapping 不合、以 mapping 为准）')
            srcs.append('benchmark/phase3/runs/round71/judging/outcome-manifest.json cases[LY-023]（旗标引文出处核对）')
        if cid == 'AS-204':
            srcs.append('benchmark/phase3/runs/round71/judging/outcome-manifest.json cases[LY-516]（旗标引文出处核对）')
        if cid == 'OC-012':
            srcs.append('benchmark/phase3/runs/round71/judging/outcome-manifest.json cases[OC-026]（旗标引文出处核对）')
    else:
        if cid == 'LY-215':
            lr, la = pr[[r for r, _ in pr].index(56)]
            disp = la['disposition']
            finding = ('承接既有定案不重裁（历轮同旨最近定案 R56 不成立；R64 索债新旨定案不成立与本旨并行不悖）：' + la['finding'])
            finding += (' 本轮（R71）manifest 该例结局与历轮所核文本一致；本轮旗标所指流年财运面未载一节，'
                        '结局即 R56 定案所据流年险厄趋避断面实况，非数据缺口。')
            relation = '同旨续接（R56）'
            sugg = '同旨续接：自 R72 起承接 R56＋本 R71 标注；结局原文照录不改。'
            category = '同旨续接（详见核查事实）'
        else:
            lr, la = pr[-1]
            disp = la['disposition']
            finding = f'承接既有定案不重裁（历轮最近定案 R{lr} {disp}）：' + la['finding']
            finding += ' 本轮（R71）manifest 该例结局与历轮所核文本一致、自报与既有定案同旨。'
            relation = f'同旨续接（R{lr}）'
            sugg = f'同旨续接：自 R72 起承接 R{lr}＋本 R71 标注；结局原文照录不改。'
            category = '同旨续接（详见核查事实）'
        if cid in APPEND:
            finding += APPEND[cid]
    for r, _ in pr:
        srcs.append(f'benchmark/phase3/data/case-annotations-r{r}.json {cid} 条')
    ann = {'anon_id': anon, 'case_id': cid, 'disposition': disp, 'finding': finding, 'flag': flag_txt,
           'manifest_carry_suggestion': sugg, 'relation': relation, 'registered_round': 71,
           'sources_checked': srcs, 'source_seats': seats}
    annotations.append(ann)
    flags.append({'anon_id': anon, 'case_id': cid, 'verdict': disp, 'disposition': disp, 'basis': finding,
                  'carry_suggestion': sugg, 'manifest_carry_suggestion': sugg, 'flag': flag_txt,
                  'category': category, 'views': sorted({s[0] for s in seats}), 'dual_view': len({s[0] for s in seats}) > 1,
                  'relation': relation, 'registered_round': 71, 'sources_checked': srcs})

verdicts = dict(collections.Counter(a['disposition'] for a in annotations))
assert verdicts == {'成立': 12, '部分成立': 83, '不成立': 9, '未核': 1}, verdicts
assert all(a['manifest_carry_suggestion'] for a in annotations if a['disposition'] == '部分成立')
counts = {'selfreport_flag_rows_total': 159, 'selfreport_numbered_items_total': 147,
          'selfreport_anons_total': 105, 'selfreport_cases_total': 105,
          'host_tradition_flags_total': 0, 'host_tradition_only_cases': 0,
          'cases_total': 105, 'continuation_cases': 93, 'same_case_new_gist_cases': 1,
          'new_flag_cases': 10, 'pending_touch_cases': 1, 'verdicts': verdicts}

special_checks = [
 {'item': '特别核查①：待核维持件（BZ-029／BZ-040／LY-537／YM-070）状态登记',
  'conclusion': 'BZ-029／BZ-040／LY-537 本轮未被任何旗标触及，不入 annotations、维持各自原登记（BZ-029 维持 R55 卒年待核（未核）；BZ-040 维持 R55 原登记（许世英享年异说待盘外独立史源）；LY-537 维持 R68 未核原登记（『申予日』措辞待核））。YM-070 本轮被旗标触及（X2 旗标「结局措辞待核（『都下』语义未明）」条与 Y2 旗标同旨条），依任务口径只登记触及、维持原登记、不入裁断：以未核入本轮 annotations，finding 只录触及事实与逐字回读结果，无盘外独立史源不裁。',
  'evidence': '据 runs/round71/judging/host-mapping.json 与 FLAGS-selfreported-r71.md 逐件比对：105 件 case_id 集合含 YM-070、不含 BZ-029／BZ-040／LY-537（落盘脚本断言通过）；YM-070 结局原文逐字断言（「后果同行都下。」）通过。',
  'scope_note': '本核查只登记状态，不改分数、不改 manifest；待核口径照旧，无盘外独立史源不裁。'},
 {'item': '特别核查②：旗标内容错配核查（引文层与主张层；anon 形近串号对位复核）',
  'conclusion': '引文层错配 3 件，均已逐件定案：（一）括号对位错配 1 件——X2 旗标 P3-468cd1e2 括号作（LY-023），host-mapping 指 LR2-018，以 mapping 为准登记为 LR2-018 定案；旗标所述母病／子惊风断面实为 LY-023 结局原文，与 LR2-018 卡面、结局、prediction 均无对应，定案不成立（LY-023 本轮另由 Y2 旗标 P3-45feb719 正确对位自报，按同旨续接 R70 成立定案）。（二）无括号内容错配 2 件——X4 旗标 P3-fae17093（mapping 指 AS-204）所述「果得真定＋断法通则」实为 LY-516 结局原文，与 AS-204 本例无对应，定案不成立；Y1 旗标 P3-3a2eca6c（mapping 指 OC-012）所引赵忻城昆弟结局实为 OC-026 结局原文，与 OC-012 本例无对应，定案不成立。乱码主张 4 件盘上无据、定案不成立：OC-010／MP-010 结局与 YM-037／YM-048 prediction 经逐字回读均无 U+FFFD 替换字符（本轮 487 例 cases 本体亦无一例含替换字符），对应文句在盘上文义完整。主张层口径不合 7 件，均已并行登记、档位照各自主旨：（一）tradition 措辞四件（LY-017／LY-019／LY-021／LY-034）——R71 prediction basis 首行已作「卡面未标注 tradition 字段，按题面体裁自决」，本轮 prediction 并无『與卡面一致』之语，旗标所指系旧措辞经 carry 转述，本轮核明层已逐件入定案附注（卡面无 tradition/system 字段一层经结构化直读复核属实）；主持复核节另裁定 7 件英文变体误报不成立、不入定案范围，本席未将其入案。（二）「?」字样三件——LY-520／LY-613 逐字核 R71 prediction 全文无「?／？」字样（旗标所据为 carry 旧注；LY-613 之 Y2 旗标亦自注回读未见）；LY-628 字样本轮在 basis 以半角「?」一处在场、prediction_text 无，所在层位与旗标所报（爻位）不尽合。另同例新旨 1 件（LY-036：carry_note 所称 prediction 不报方向与 R71 prediction_text 实含方向断不合）见特别核查④。其余各件旗标引文经逐件回读本例 R71 结局原文／prediction 原文核对均在本例内（引文逐字断言内置于落盘脚本）。',
  'evidence': '落盘脚本断言：括号对位不合恰为 [(X2, P3-468cd1e2, LY-023, LR2-018)] 一件；LR2-018／LY-023／LY-516／AS-204／OC-026 结局逐字断言、OC-010／MP-010 结局洁净文句断言、YM-037／YM-048 prediction 原始文件无替换字符断言、TRAD4 卡面无 tradition/system 键与 basis 首行断言、LY-520／LY-613 全文无问号断言、LY-628 basis 半角问号计数断言均通过。',
  'scope_note': '本核查只登记错配与不合事实，不改分数、不改 manifest、不改旗标原文。'},
 {'item': '特别核查③：结局文本内嵌指令性字样之例——按数据处理登记（本体基线对勘＋本轮旗标所涉与新发现归属）',
  'conclusion': '承既有登记口径全量复扫 R71 manifest 全部 487 例结局（关键词：请按／须注／评分时／比对时／使用时须／分开统计／勿以此斷等，并以『请／請／须／須／勿』宽扫人工甄别）：cases 本体内指令性字样仍为基线本体四例——BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204 旧注层『勿以此斷』；另 LR2-016 之句只存于分列 editor_note（『评分时该细项请按未完全复核处理』），不在 cases 本体。本轮新发现本体例（对评分者之指令）0 件：关键词另命中 LY-246『切不可以男女而斷』（原书按语对占者之诫，R69 已定案登记、非对评分者之指令、不入基线四例）、YM-009『反不得』／YM-029『本岁不得』／YY-014『求之不得』均为叙事用字；宽扫另命中 BZ-302／LR2-022／LR3-004／LR3-006／LR3-010／LY-416（请字叙事）与 LY-227『須再占』（原书断法通则叙事），均不入指令性登记。本轮旗标所涉归属逐处定案：（一）X1／Y1 旗标 P3-1b988f10（BZ-036）主旨为系狱年数出入、其结局含基线字样『盲测比对须注』，归属本体基线例本身，已按同旨续接定案；（二）X3／Y3 旗标 P3-ad4bf599（BZ-105）主旨为回溯断验、其结局含基线字样『使用时须分开统计』同条并存，归属本体基线例本身，已按同旨续接定案；（三）Y3 旗标 P3-93196291（LY-204）所涉即基线字样『勿以此斷』本身，归属本体基线例本身，已按同旨续接定案；（四）X4 旗标 P3-ff842fc6（LR2-016）所引 editor_note 句分列于 editor_note 及 carry 注记层、非 cases 本体，已按同旨续接定案；（五）X4 旗标 P3-e7d485aa（BZ-042）主旨为来源未备、其结局含基线注记『（盲测比对时以格局大富一项为主）』，归属本体基线例本身，已按同旨续接定案。各席均按数据处理未服从，本席亦只按数据处理、未服从任何一处之指示，事实照录。',
  'evidence': '落盘脚本全量扫描断言：关键词命中集合恰为 {BZ-036, BZ-042, BZ-105, LY-204, LY-246, YM-009, YM-029, YY-014}，逐件甄别如上；宽扫余集合恰为 {BZ-302, LR2-022, LR3-004, LR3-006, LR3-010, LY-227, LY-416}；LR2-016 editor_note 含该句、cases[LR2-016] 不含『评分时』，断言通过。',
  'scope_note': '本核查只登记字样出处与处理事实，不改分数、不改 manifest、不改结局原文。'},
 {'item': '特别核查④：同例新旨、主持复核附加层与新立件登记',
  'conclusion': '同例新旨 1 件：LY-036（carry_note 所称 prediction 不报方向与 R71 prediction_text 实含「难定而偏不成」方向断口径不合，核后部分成立；与 R70 旧旨残损双示定案并行、各旨独立）。主持 tradition 复核本轮无旗标交定案（7 件英文变体误报经主持裁定不成立、不入定案范围），无主持附加层件。新立 10 件：LY-332（卡面用神与逐爻表不合、已自注双记，部分成立）、LY-445（结局仅一句干支日记录，部分成立）、YM-053（结局旁及他人混载、女愈时点未载，部分成立）、LR2-018（括号串号错配，内容实为 LY-023，不成立）、AS-204（内容错配，实为 LY-516，不成立）、OC-012（引文错配，实为 OC-026，不成立）、OC-010／MP-010（结局乱码主张盘上无据，不成立）、YM-037／YM-048（prediction 乱码主张盘上无据，不成立）。并行登记一件：LY-215 本轮旗标同旨于 R56 旧旨（结局断面错位疑，定案不成立），R64 索债新旨定案不成立与之并行不悖、本轮一并承接、档位不变。待核触及 1 件（YM-070）见特别核查①。',
  'evidence': '据 FLAGS-selfreported-r71.md 主持复核节、data/case-annotations-r56.json LY-215 条、-r64.json LY-215 条、-r70.json LY-036 条与本轮逐件回源核查。',
  'scope_note': '本核查只登记构成事实，不改分数、不改 manifest。'},
 {'item': '特别核查⑤：汇编一致性与结局文本一致性',
  'conclusion': '汇编 FLAGS-selfreported-r71.md 八席自报共 147 条含 anon 条目、159 条席位-anon 旗标行、105 anon、105 例（单席 51 例、双席 54 例），主持 tradition 复核交定案 0 件，合计定案 105 例；R71 各例结局文本经脚本断言与 R70 manifest 逐件全等（487/487），续接类定案的『结局与历轮所核文本一致』前提全数成立。本轮括号对位异常 1 件、内容错配 2 件（见特别核查②）。承接附则对勘：R70 定案部分成立 77 件与 R71 manifest _r71_carryover_notes_addendum 逐件全等（77/77），见 data/manifest-carryover-r71-addendum.md。',
  'evidence': '证据脚本 data_r71_evidence.py 与落盘脚本 data_r71_build.py 双脚本断言输出。',
  'scope_note': '本核查只登记一致性事实。'},
]

out = {
 '_provenance': ('R71 数据席（旗标定案专席，独立席位，不兼任本轮盲测/评审/诊断，不改任何分数）逐件回源核查 R71 八席自报旗标 '
   '147 条含 anon 条目／159 条席位-anon 旗标行、去重为 105 anon／105 例，主持 tradition 复核本轮无旗标交定案（7 件英文变体误报经主持裁定不成立、'
   '不入定案范围；评审席 X1／Y1／X3／Y3 旗标所涉 LY-017／LY-019／LY-021／LY-034 四件 basis 措辞观察经 host-mapping 对位回原卡逐件定案，'
   '归入同旨续接并附本轮核明层）。逐件回 benchmark/phase3/inputs-dev12/<case_id>.json 原卡、runs/round71/predictions/<case_id>.json 预测原文、'
   'runs/round71/judging/outcome-manifest.json cases 载荷（落笔前回读本例结局原文，引文逐字断言内置于落盘脚本），并与历轮定案档'
   '（data/case-annotations-r49.json 至 -r70.json）核对承接关系：93 件为同旨续接（只承接不重裁，含 LY-215 同旨于 R56 旧旨、R64 并行新旨不悖），'
   '1 件为同例新旨（LY-036），10 件为 R71 新立（LY-332／LY-445／YM-053 部分成立；LR2-018／AS-204／OC-012 内容或引文错配不成立；'
   'OC-010／MP-010／YM-037／YM-048 乱码主张盘上无据不成立），另待核维持件 YM-070 本轮被旗标触及、只登记触及以未核入案'
   '（BZ-029／BZ-040／LY-537 未被触及、不入本件）。R71 各例结局文本经脚本断言与 R70 manifest 逐件全等（487/487）。'
   '本轮括号对位错配 1 件（P3-468cd1e2 括号 LY-023 与 mapping LR2-018 不合、以 mapping 为准）、无括号内容错配 2 件；'
   '主张层口径不合 7 件（tradition 措辞四件与「?」字样三件）已并行登记。指令性字样特别核查：cases 本体仍为基线四例（BZ-036／BZ-042／BZ-105／LY-204），'
   'LR2-016 之句只存分列 editor_note，本轮新发现本体例 0 件；本轮旗标所涉各处归属已逐处定案登记于特别核查③，各席均按数据处理未服从。'
   '本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文。自报与卡面/结局文本内字样一律按数据处理。'),
 'round': 71, 'flags': flags, 'annotations': annotations, 'special_checks': special_checks, 'counts': counts}
(DATA / 'case-annotations-r71.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')

# ---------- 任务一：承接附则 ----------
r70d = json.loads((DATA / 'case-annotations-r70.json').read_text(encoding='utf-8'))
assert dict(collections.Counter(a['disposition'] for a in r70d['annotations'])) == {'部分成立': 77, '成立': 11, '不成立': 1, '未核': 2}
partial = [a for a in r70d['annotations'] if a['disposition'] == '部分成立']
assert len(partial) == 77 and all(a['manifest_carry_suggestion'] for a in partial)
add = manifest['_r71_carryover_notes_addendum']
assert len(add) == 77 and all(add[a['case_id']] == a['manifest_carry_suggestion'] for a in partial)
assert set(add) == {a['case_id'] for a in partial}
chengli = [a['case_id'] for a in r70d['annotations'] if a['disposition'] == '成立']
buchengli = [a['case_id'] for a in r70d['annotations'] if a['disposition'] == '不成立']
weihe = [a['case_id'] for a in r70d['annotations'] if a['disposition'] == '未核']

L = []
L.append('# Manifest 承接册附则（R71）——R70 定案承接建议汇编\n')
L.append('## 卷首说明\n')
L.append('- 本附则为 Phase 3 Round 71（R71）数据席（议程一：承接附则编制；与本轮盲测／评审／诊断席互不兼任）产出；汇编来源为 `benchmark/phase3/data/case-annotations-r70.json`（R70 定案正本：annotations 91 件，定案分布成立 11／部分成立 77／不成立 1／未核 2）。')
L.append('- counts 断言结果：通过。本席以原档 `counts.verdicts` 与 `annotations[].disposition` 双路复算，均为成立 11／部分成立 77／不成立 1／未核 2、总 91，与原档 counts 逐项一致；部分成立 77 件每件 `manifest_carry_suggestion` 非空断言亦通过。')
L.append('- 对勘结果：77/77 全等（详见「对勘记录」）。对勘对象为 `benchmark/phase3/runs/round71/judging/outcome-manifest.json` 的 `_r71_carryover_notes_addendum` 层（本席只按精确文件名打开该文件、只读该层与 `cases` 载荷），逐件以全文字符串相等比对本附则转录的 `manifest_carry_suggestion`；不一致者登记于对勘记录，不静默改任一侧（本轮不一致 0 件、多键 0 件）。')
L.append('- **本附则自 R72 manifest 起落实**；本轮（R71）manifest 不据本附则改动。')
L.append('- **本件只汇编与对勘，不改任何分数与结局原文。**')
L.append('- 汇编范围：R70 定案中部分成立 77 件，逐件全列于第一节（顺序照原档 `annotations` 排列）；每件的承接注记建议文本照 `case-annotations-r70.json` 该件 `manifest_carry_suggestion` 字段原文录入，不改写（其中「自 R71 起」等表述为原档原文，落实轮次按卷首上一条读作自 R72 起，不回溯改动 R71）。每件定案要旨照原档 `finding` 字段、原旗标要旨照原档 `flag` 字段、与既有承接册／附则条目的关系照原档 `relation` 字段录入。')
L.append('- 成立 11 件、不成立 1 件、未核 2 件不入正文逐件节，只在文末列 case_id 清单。')
L.append('- 承接只标注、不改任何既往或本轮分数、不改结局原文、不改原卡。\n')
L.append('---\n')
L.append('## 一、部分成立件承接汇编（定案档位：部分成立，77 件，逐件全列）\n')
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
L.append('- 对勘源：`benchmark/phase3/runs/round71/judging/outcome-manifest.json` 的 `_r71_carryover_notes_addendum` 层，共 77 件。')
L.append('- 逐件对勘：77 件 case_id 集合与本附则汇编集合全等；每件注记文本与 `case-annotations-r70.json` 对应件 `manifest_carry_suggestion` 全文字符串相等，77/77 全等。')
L.append('- 不一致登记：0 件；附则侧与 manifest 侧均未作任何改动（不静默改任一侧）。')
L.append('- 勘误：无。\n')
L.append('---\n')
L.append('## 三、不入正文清单（照 R70 定案档位）\n')
L.append(f'- 成立 11 件：{"／".join(chengli)}')
L.append(f'- 不成立 1 件：{"／".join(buchengli)}')
L.append(f'- 未核 2 件：{"／".join(weihe)}')
(DATA / 'manifest-carryover-r71-addendum.md').write_text('\n'.join(L) + '\n', encoding='utf-8')

chk = json.loads((DATA / 'case-annotations-r71.json').read_text(encoding='utf-8'))
assert dict(collections.Counter(a['disposition'] for a in chk['annotations'])) == verdicts
assert chk['counts']['cases_total'] == len(chk['annotations']) == 105
print('OK verdicts', verdicts, 'counts', counts)
print('addendum bytes', (DATA / 'manifest-carryover-r71-addendum.md').stat().st_size)
print('annotations bytes', (DATA / 'case-annotations-r71.json').stat().st_size)
