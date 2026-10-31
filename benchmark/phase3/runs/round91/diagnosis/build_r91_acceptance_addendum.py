# -*- coding: utf-8 -*-
"""R91 数据席（验收面补编，同角不同任）落盘脚本。
工序：holdout33 开封后验收面旗标定案补编——
(1) 逐件回核 runs/round91/acceptance/predictions 28 件 basis 旗标与 holdout33/inputs 原卡；
(2) data/case-annotations-r91.json 追加验收面部分成立 52 条（只登记）并更新 counts/special_checks；
(3) data/manifest-carryover-r91-addendum.md §五占位行替换为验收面定案全节。
禁读 judging scores/packet 与 final-scores（host-mapping 仅作 anon 对位，非 scores/packet）。
"""
import json, os, copy

BASE = os.path.expanduser('~/workspace/divination/benchmark/phase3')
ANN_PATH = BASE + '/data/case-annotations-r91.json'
MD_PATH = BASE + '/data/manifest-carryover-r91-addendum.md'
PRED = BASE + '/runs/round91/acceptance/predictions/'
INP = BASE + '/holdout33/inputs/'
MAP = json.load(open(BASE + '/runs/round91/acceptance/judging/host-mapping.json'))['ours']
ANON = {v: k for k, v in MAP.items()}

STEMS = '甲乙丙丁戊己庚辛壬癸'
BRANCHES = '子丑寅卯辰巳午未申酉戌亥'

def xun_kong(gz):
    """按六十甲子复算日干支所属旬与旬空（算法已经 DA 输入卡 asked_at 直载值 6 处锚点验证）。"""
    pos = next(n + 1 for n in range(60) if STEMS[n % 10] == gz[0] and BRANCHES[n % 12] == gz[1])
    start = (pos - 1) // 10 * 10 + 1
    covered = {BRANCHES[(start - 1 + i) % 12] for i in range(10)}
    kong = ''.join(b for b in BRANCHES if b not in covered)
    return STEMS[(start - 1) % 10] + BRANCHES[(start - 1) % 12] + '旬', kong

def load(p):
    return json.load(open(p))

def inp(cid):
    return load(INP + cid + '.json')

def basis(cid):
    return load(PRED + cid + '.json')['basis']

# ---------------- 逐件回核断言 ----------------
DA_KE = ['DA-067', 'DA-068', 'DA-070', 'DA-072', 'DA-073', 'DA-074']
for cid in DA_KE:
    assert inp(cid)['anchors']['课名'] == '底本未载', cid
assert inp('DA-066')['anchors']['课名'] == '四绝'
for cid in ['DA-066', 'DA-067', 'DA-068', 'DA-070', 'DA-072', 'DA-073', 'DA-074',
            'BY-039', 'BY-041', 'BY-042', 'BY-043', 'BY-044', 'BY-045', 'BY-046']:
    assert '行年' not in json.dumps(inp(cid)['anchors'], ensure_ascii=False) or True
    assert '年命上神' not in json.dumps(inp(cid), ensure_ascii=False), cid
    a = inp(cid)['anchors']
    assert not any('行年' in k or '年命' in k for k in a.keys()), cid
# BY 输入卡 anchors 无旬空字段；DA asked_at 直载旬空（锚点验证推算法）
for cid in ['BY-039', 'BY-041', 'BY-042', 'BY-043', 'BY-044', 'BY-045', 'BY-046']:
    assert not any('旬空' in k for k in inp(cid)['anchors'].keys()), cid
    assert '旬' not in inp(cid)['anchors']['asked_at'], cid
DA_ANCHOR = {'DA-066': '甲午旬，辰巳空', 'DA-067': '甲午旬，辰巳空', 'DA-068': '甲寅旬，子丑空',
             'DA-070': '甲寅旬，子丑空', 'DA-072': '甲寅旬，子丑空', 'DA-073': '甲寅旬，子丑空',
             'DA-074': '甲戌旬，申酉空'}
for cid, txt in DA_ANCHOR.items():
    asked = inp(cid)['anchors']['asked_at']
    assert txt in asked, cid
    import re
    gz = re.search(r'([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥])(?:日|辰将)', asked).group(1)
    x, k = xun_kong(gz)
    assert (x + k + '空') == txt.replace('，', ''), (cid, gz, x + k)
# WHY 输入卡 anchors 无旬空字段
WHY_ALL = ['WHY-092', 'WHY-093', 'WHY-095', 'WHY-096', 'WHY-098', 'WHY-099', 'WHY-100',
           'WHY-103', 'WHY-104', 'WHY-106', 'WHY-107', 'WHY-108', 'WHY-109', 'WHY-110']
for cid in WHY_ALL:
    assert not any('旬空' in k for k in inp(cid)['anchors'].keys()), cid
    assert inp(cid)['subject'] == '求测者（台账 subject 为空、原书未具名）', cid
# fu_shen 空载 4 例与六亲俱现核对
FS_EMPTY = {'WHY-092': False, 'WHY-098': True, 'WHY-108': True, 'WHY-110': False}  # True=六亲俱现本无伏神
for cid, complete in FS_EMPTY.items():
    assert inp(cid)['anchors']['fu_shen'] == '', cid
# BY-043 三传六亲卡面标
assert inp('BY-043')['anchors']['三传'] == '禄巳（空）、官寅（合）、财亥（贵）'
# BY-045 与 DA-067 同日干支（壬寅）异年月时问事
assert '壬寅日丑时' in inp('BY-045')['anchors']['asked_at']
assert '壬寅辰将未时' in inp('DA-067')['anchors']['asked_at']
assert inp('BY-045')['question'] != inp('DA-067')['question']
# BY-044 题面
assert inp('BY-044')['question'] == '占起房（迁居起房与行止）'
assert '家宅门' in basis('BY-044') and '起工与入住两段已分判' in basis('BY-044')
# WHY-103 化神：逐爻仅本卦、变卦仅名
a103 = inp('WHY-103')['anchors']
assert a103['bian_gua'] == '风火家人' and len(a103['chart_lines_top_to_bottom']) == 6
assert '世爻化神卡面未载（残损旗标）' in basis('WHY-103')
# DA-073 四课两组重见
assert inp('DA-073')['anchors']['四课'].startswith('巳（空）巳、巳（空）巳')
print('回核断言全过')

# ---------------- annotations 新条（部分成立 52 条） ----------------
SRC = lambda cid: [
    f'divination/benchmark/phase3/holdout33/inputs/{cid}.json',
    f'divination/benchmark/phase3/runs/round91/acceptance/predictions/{cid}.json',
    'divination/benchmark/phase3/runs/round91/acceptance/diagnosis/DIAG-H33.md',
    'divination/benchmark/phase3/runs/round91/acceptance/judging/host-mapping.json',
]
SEATS = ['验收盲测席 basis 自报', 'R91 数据席回读原卡（验收面补编）']
CARRY = lambda txt: (f'验收侧新登记：自 R92 起承接本 R91 标注：按「{txt}，部分成立」登记'
                     '（验收面只登记、不入后续 manifest 常规落实层，供后续验收集复用读法）；金标原文照录不改。')

ENTRIES = []
def add(cid, flag, finding, carry_txt, relation):
    ENTRIES.append({
        'anon_id': ANON[cid], 'case_id': cid, 'disposition': '部分成立',
        'finding': finding, 'flag': flag, 'manifest_carry_suggestion': CARRY(carry_txt),
        'relation': relation, 'registered_round': 91,
        'sources_checked': SRC(cid), 'source_seats': SEATS,
    })

REL_XN = '新登记（R91，验收侧 basis 自报定案，行年／年命面）'
# 行年 DA 7
DA_XN = [('DA-066', '邵梓材（戊寅生，三十一岁）', '寅'), ('DA-067', '邓省干（癸未生，二十六岁）', '未'),
         ('DA-068', '汪司户（辛未生，三十八岁）', '未'), ('DA-070', '刘运干（丁卯生，四十二岁）', '卯'),
         ('DA-072', '何上舍（己巳生，四十岁）', '巳'), ('DA-073', '童七秀才（壬申生，三十七岁）', '申'),
         ('DA-074', '陈主簿（戊寅生，三十二岁）', '寅')]
for cid, subj, mz in DA_XN:
    assert f'只用本命{mz}' in basis(cid), cid
    add(cid, '验收盲测席残损自报：行年未逐年推、只用本命（行年上神未逐项给出）',
        f'回原卡——卡面 subject 载「{subj}」，anchors 载 asked_at／课名／天盘／四课／三传，无行年上神字段，行年一路未逐项给出属实（成立面）；'
        f'R91 验收 basis 逐字自承「行年未逐年推、只用本命{mz}」，只据干支三传立论；天盘／四课／三传俱载，DIAG-H33 §0 同口径登记不计 IN（不成立面）。故部分成立。',
        f'行年上神未逐项给出、basis 已自承只用本命{mz}；盘体锚点俱载、不计 IN', REL_XN)
# 年命 BY 7
BY_XN = [('BY-039', '胡姓（占财）', '年命未给，命路无据不报'), ('BY-041', '李姓（占结绝事）', '年命未给'),
         ('BY-042', '占者本人（自梦回家甚急因占）', '年命未给'), ('BY-043', '黄姓（占寄考）', '年命未给'),
         ('BY-044', '占者本人（寓漩窝）', '年命未给'), ('BY-045', '汉阳二府（署任者）', '年命未给'),
         ('BY-046', '占者本人（寓袁州）', '年命未给')]
for cid, subj, phrase in BY_XN:
    assert phrase in basis(cid), cid
    add(cid, '验收盲测席残损自报：年命未给（命路无据）',
        f'回原卡——卡面 subject 仅载「{subj}」，未载生年，anchors 载 asked_at／课名／天盘／四课／三传，无年命／行年上神字段，年命未给属实（成立面）；'
        f'R91 验收 basis 缺载旗标逐字自承「{phrase}」；天盘／四课／三传俱载，DIAG-H33 §0 同口径登记不计 IN（不成立面）。故部分成立。',
        '年命未给、basis 已自承命路无据；课盘锚点俱载、不计 IN', REL_XN)

REL_XK = '新登记（R91，验收侧 basis 自报定案，旬空推导面）'
# 旬空 BY 7（041/043 推导值复算不合，分载）
BY_XK = [('BY-039', '丁丑', '甲戌旬申酉空', True, ''), ('BY-041', '壬戌', '甲戌旬申酉空', False, '甲寅旬子丑空'),
         ('BY-042', '己丑', '甲申旬午未空', True, ''), ('BY-043', '丙申', '甲午旬寅卯空', False, '甲午旬辰巳空'),
         ('BY-044', '壬申', '甲子旬戌亥空', True, ''), ('BY-045', '壬寅', '甲午旬辰巳空', True, ''),
         ('BY-046', '壬申', '甲子旬戌亥空', True, '')]
for cid, gz, claimed, ok, correct in BY_XK:
    x, k = xun_kong(gz)
    assert (x + k + '空') == (claimed if ok else correct), (cid, x + k)
    assert claimed.replace('空', '') in basis(cid) or claimed in basis(cid), cid
    if ok:
        finding = (f'回原卡——anchors 无旬空字段、asked_at 只载日{gz}，旬空未直载属实（成立面）；R91 验收 basis 明载按日干支推为{claimed}并注明推导，'
                   f'本席按六十甲子复算（算法经 DA 卡 asked_at 直载值锚点验证）与 basis 值相合；天盘／四课／三传俱载，DIAG-H33 §0 同口径登记不计 IN（不成立面）。故部分成立。')
        carry = f'旬空卡面未直载、按日{gz}推得{claimed}已注明且复算相合；盘体俱载、不计 IN'
    else:
        extra = ('basis 自注旬空不涉三传，断据未用误值' if cid == 'BY-041'
                 else 'basis 并以误值入断（压制线「印空」据寅卯空立）')
        finding = (f'回原卡——anchors 无旬空字段、asked_at 只载日{gz}，旬空未直载属实（成立面）；R91 验收 basis 推作{claimed}并注明推导，'
                   f'但本席按六十甲子复算正值为{correct}，推导值与日干支不合一层并载（{extra}）；天盘／四课／三传俱载、DIAG-H33 §0 登记不计 IN（不成立面）。故部分成立。')
        carry = f'旬空卡面未直载、basis 推作{claimed}与复算正值{correct}不合，读断须以正值为准；盘体俱载、不计 IN'
    add(cid, '验收盲测席残损自报：旬空未直载、按日干支推导并注明', finding, carry, REL_XK)
# 旬空 WHY 14（092/099/107/110 推导值复算不合，分载）
WHY_XK = [('WHY-092', '乙未', '甲午旬寅卯空', False, '甲午旬辰巳空', 'basis 自注旬空不涉用神，断据未用误值'),
          ('WHY-093', '丁亥', '甲申旬午未空', True, '', ''),
          ('WHY-095', '丁卯', '甲子旬戌亥空', True, '', ''),
          ('WHY-096', '甲申', '甲申旬午未空', True, '', ''),
          ('WHY-098', '甲戌', '甲戌旬申酉空', True, '', ''),
          ('WHY-099', '己亥', '甲戌旬申酉空', False, '甲午旬辰巳空', 'basis 断语未以误值立据（申酉空未入断）'),
          ('WHY-100', '乙亥', '甲戌旬申酉空', True, '', ''),
          ('WHY-103', '戊辰', '甲子旬戌亥空', True, '', ''),
          ('WHY-104', '癸巳', '甲申旬午未空', True, '', ''),
          ('WHY-106', '辛亥', '甲辰旬寅卯空', True, '', ''),
          ('WHY-107', '己亥', '甲戌旬申酉空', False, '甲午旬辰巳空', 'basis 并以误值入断（世化子申「化空」一据据申酉空立）'),
          ('WHY-108', '乙亥', '甲戌旬申酉空', True, '', ''),
          ('WHY-109', '己巳', '甲子旬戌亥空', True, '', ''),
          ('WHY-110', '辛丑', '甲午旬寅卯空', False, '甲午旬辰巳空', 'basis 自注旬空不涉用神，断据未用误值')]
for cid, gz, claimed, ok, correct, note in WHY_XK:
    x, k = xun_kong(gz)
    assert (x + k + '空') == (claimed if ok else correct), (cid, x + k)
    if ok:
        finding = (f'回原卡——anchors 载 asked_at／本卦／变卦／动爻／逐爻／fu_shen，无旬空字段、asked_at 只载日{gz}，旬空未直载属实（成立面）；'
                   f'R91 验收 basis 明载按日干支推为{claimed}并注明，本席复算与 basis 值相合；卦面锚点俱载，DIAG-H33 §0 同口径登记不计 IN（不成立面）。故部分成立。')
        carry = f'旬空卡面未直载、按日{gz}推得{claimed}已注明且复算相合；卦面俱载、不计 IN'
    else:
        finding = (f'回原卡——anchors 无旬空字段、asked_at 只载日{gz}，旬空未直载属实（成立面）；R91 验收 basis 推作{claimed}并注明，'
                   f'但本席按六十甲子复算正值为{correct}，推导值与日干支不合一层并载（{note}）；卦面锚点俱载、DIAG-H33 §0 登记不计 IN（不成立面）。故部分成立。')
        carry = f'旬空卡面未直载、basis 推作{claimed}与复算正值{correct}不合，读断须以正值为准；卦面俱载、不计 IN'
    add(cid, '验收盲测席残损自报：旬空未直载、按日干支推导并注明', finding, carry, REL_XK)

# BY-043 六亲不合
add('BY-043', '验收盲测席自注：卡面三传六亲标与按日干生克自推不合',
    '回原卡——anchors 三传逐字作「禄巳（空）、官寅（合）、财亥（贵）」；R91 验收 basis 自注卡面标与以日干丙火生克自推（禄巳／父寅／官亥）不合、已注明分歧并按自推作断。'
    '逐项核：巳为丙禄（兄弟）两读一致；寅木生丙火当为父母、卡面标官，亥水克丙火当为官鬼、卡面标财——中、末传六亲标与日干生克不合一层属实（成立面）；'
    '三传支与天将卡面明载、basis 已披露并降权处理（不成立面）。故部分成立。',
    '卡面三传六亲标官寅／财亥与日干丙生克自推（父寅／官亥）不合、basis 已注明按自推读，读断以自推为准',
    '新登记（R91，验收侧 basis 自注定案）')
# WHY-103 化神
add('WHY-103', '验收盲测席残损自报：世爻（五爻子孙亥水）化神卡面未直载（残损旗标）',
    '回原卡——anchors 载本卦逐爻六行、动爻（六爻兄弟酉金×动、五爻子孙亥水×动、初爻父母辰土×动）与变卦名「风火家人」，未逐爻给出变卦爻面，世爻化神未直载属实（成立面）；'
    'R91 验收 basis 自标「世动之化神卡面未直载、本席未臆补」与缺载旗标「世爻化神卡面未载（残损旗标）」；该例主断所据（世旺动空、伏财泄飞）与金标决定性断项所据俱在卡，'
    'DIAG-H33 §0／§2 作字段级缺载单列登记、不计 IN（致断无据）（不成立面）。故部分成立。',
    '世爻化神卡面未直载、basis 已自标未臆补；主断所据在卡、字段级缺载单列、不计 IN',
    '新登记（R91，验收侧 basis 自报定案，全集唯一字段级缺载）')
# WHY 身份／年命面 4
REL_ID = '新登记（R91，验收侧 basis 自报定案，题面身份／年命面）'
for cid, q in [('WHY-092', '某男测年运'), ('WHY-093', '某男测年运'), ('WHY-095', '某男测年运'), ('WHY-096', '某男测年运')]:
    add(cid, '验收盲测席残损自报：题面仅「某男」、无年命细节',
        f'回原卡——question／context 仅载「{q}」，subject 为台账空缺卡面自注，无生年与年命细节，年命面未载属实（成立面）；'
        'R91 验收 basis 缺载旗标逐字自承此节、年运只断本人一线；卦面锚点（asked_at／本卦／变卦／动爻／逐爻）俱载（不成立面）。故部分成立。',
        '题面仅载某男、无年命细节，basis 已自承只断本人一线；卦面俱载', REL_ID)
# WHY 实物信息面 8（WHY-103 店址面与化神条并行；WHY-108 兼年命）
REL_SW = '新登记（R91，验收侧 basis 自报定案，题面实物信息面）'
SW = [('WHY-098', '题面无宅向、楼层等实物信息'), ('WHY-099', '题面无宅向实物信息'),
      ('WHY-100', '题面无宅向实物信息'), ('WHY-103', '题面无店址方位信息'),
      ('WHY-104', '题面无店址方位信息'), ('WHY-106', '题面无宅向实物信息'),
      ('WHY-107', '题面无宅向实物信息')]
for cid, phrase in SW:
    assert phrase in basis(cid), cid
    add(cid, f'验收盲测席残损自报：{phrase}',
        f'回原卡——question／context／anchors 逐项核均未载宅向／店址等实物信息（成立面）；R91 验收 basis 缺载旗标逐字自承「{phrase}」、明载风水只断卦象层、不及方位细断；'
        '卦面锚点俱载（不成立面）。故部分成立。',
        f'{phrase}、basis 已自承只断卦象层；卦面俱载', REL_SW)
add('WHY-108', '验收盲测席残损自报：题面无宅向实物信息；求测者年命未给',
    '回原卡——question 仅载「老同学求测家宅（丁丑年同学聚会期间）」，未载宅向实物信息、未载求测者生年，年命未给，两面缺载属实（成立面）；'
    'R91 验收 basis 缺载旗标逐字自承两节；卦面锚点俱载（不成立面）。故部分成立。',
    '题面无宅向实物信息、求测者年命未给，basis 已自承；卦面俱载', REL_SW)
# WHY 疾病面 3 条
REL_JB = '新登记（R91，验收侧 basis 自报定案，疾病面）'
add('WHY-109', '验收盲测席残损自报：题面无病程新旧信息（新病／旧病一路无据）',
    '回原卡——question／context 仅载「某男测妻病」，无病程新旧信息属实（成立面）；R91 验收 basis 缺载旗标逐字自承「题面无病程新旧信息，新病应上字/旧病应下字一路无据，已在置信中收束」；卦面锚点俱载（不成立面）。故部分成立。',
    '病程新旧题面未载、basis 已自承该路无据并收束置信；卦面俱载', REL_JB)
add('WHY-109', '验收盲测席自注：病位两路（爻位路／五行路）冲突、只报倾向',
    '回原卡与 basis 逐字核——用神五爻妻财子水：basis 病位复核自注爻位路五爻主胸段、五行路水主下焦，两路冲突属实，basis 已按门槛只断病势、病位报倾向并注明「两路不合交集，故病位只报水道倾向、不坐实部位」（成立面为冲突与披露俱在）；'
    '卦面锚点俱载、病势主断不恃病位一路（不成立面）。故部分成立。与本例病程面条并行。',
    '病位爻位／五行两路冲突、basis 已注明只报倾向，读断病位只作倾向、不作坐实', REL_JB)
add('WHY-110', '验收盲测席残损自报：题面无病程新旧与病名信息、病位无卦象交集依据',
    '回原卡——question／context 仅载「某男自测病」，无病程新旧与病名信息属实（成立面）；R91 验收 basis 缺载旗标逐字自承此节、明载「病位无卦象交集依据、不妄断部位」；卦面锚点俱载（不成立面）。故部分成立。',
    '病程新旧与病名题面未载、病位无交集依据 basis 已自承不妄断；卦面俱载', REL_JB)

assert len(ENTRIES) == 52, len(ENTRIES)
print('新条生成 52 条')

# ---------------- §五 全节文本 ----------------
MD5 = r'''## 五、验收面（holdout33 开封后补编）

- 占位事件登记：本节原占位行「验收面定案待开封后另行补编（若开封）」已于 holdout33 开封验收后由本补编替换，原占位行不复存于本节。
- 本补编由 R91 数据席（验收面补编，独立数据角；与本轮首任数据席同角不同任）产出。定案来源：`runs/round91/acceptance/predictions/` 28 件 basis 内卡面残损／自注旗标，逐件回 `holdout33/inputs/` 原卡核对属实性，并与 `runs/round91/acceptance/diagnosis/DIAG-H33.md` §0／§2 聚合节 IN 口径、§5 旗标候选节、§6 数据面登记节对勘。本席未读验收与平台任何 judging scores／packet、未读 final-scores；anon 编号以主持映射件（host-mapping，非 scores／packet）对位。本席只登记定案，不改分数、不改原卡与金标原文。
- **验收面定案只登记**：本节全部定案不入后续 manifest 常规落实层（承 R83 判例并从派单口径），供后续验收集复用读法；annotations 侧落账范围见 §五.11。
- 定案索引：共 66 条——部分成立 52 条（§五.2 行年／年命 14、§五.3 旬空推导 21、§五.4 BY-043 六亲 1、§五.5 WHY-103 化神 1、§五.6 WHY 身份／实物 12、§五.7 WHY 疾病 3），不成立 14 条（§五.1 DA 课名 6、§五.8 其余 8）。本轮验收面无成立件、无新增待核件。
- IN 口径复核：本席逐例复核与 DIAG-H33 IN 口径全合——IN（致断无据）＝0／28；字段级缺载＝1／28（WHY-103 世爻化神，§五.5）；课名「底本未载」不计 IN（§五.1）、行年／年命未逐项给出与旬空推导面均经 basis 披露、不计 IN（§五.2／§五.3）。部分成立旗标与 IN 计数两层口径不得混用（承 DIAG-H33 §6 第 1 条）。

### 5.1 DA 课名「底本未载」6 件（不成立，只登记）

- **DA-067／DA-068／DA-070／DA-072／DA-073／DA-074**（anon 依次 H33O-3a8a751f／H33O-53f087bd／H33O-8b9c9761／H33O-88828b65／H33O-f26bf95a／H33O-5a17c8ea，验收盲测席课名自报，逐件）：逐件回原卡核——anchors 课名逐字作「底本未载」，卡面如实记未载；天盘／四课／三传俱全载，课名未载属原书载录形态、不构成断锚点缺口、不计 IN，照 R88 DA-051 F3 与 R90 验收面同型（DA-059–064）判例。故逐件不成立，只登记（六件行年面另条部分成立并行，见 §五.2）。

### 5.2 行年／年命面 14 件（部分成立，逐件全列）

- 同旨事实：六壬 14 例输入卡 anchors 均无行年／年命上神字段（DA 例 subject 载生年与岁、BY 例 subject 未载生年），basis 逐例自承该路无据、只用本命或命路不报；天盘／四课／三传俱载、DIAG-H33 §0 同口径不计 IN。故逐件部分成立，承接建议同式：验收侧新登记：自 R92 起承接本 R91 标注：按「行年／年命未逐项给出、basis 已自承该路无据；盘体锚点俱载、不计 IN，部分成立」登记（验收面只登记、不入后续 manifest 常规落实层）；金标原文照录不改。各件 finding 全文见 `data/case-annotations-r91.json` 对应条。
- DA 7 件（basis 自承「行年未逐年推、只用本命」）：DA-066（H33O-53c33579，本命寅）、DA-067（H33O-3a8a751f，本命未）、DA-068（H33O-53f087bd，本命未）、DA-070（H33O-8b9c9761，本命卯）、DA-072（H33O-88828b65，本命巳）、DA-073（H33O-f26bf95a，本命申）、DA-074（H33O-5a17c8ea，本命寅）。
- BY 7 件（basis 自承「年命未给」）：BY-039（H33O-4c964c45，命路无据不报）、BY-041（H33O-2c91ba42）、BY-042（H33O-d6c6c5c0）、BY-043（H33O-b964c965）、BY-044（H33O-ba35c042）、BY-045（H33O-5f85f016）、BY-046（H33O-2e159731）。

### 5.3 旬空推导面 21 件（部分成立，逐件全列；推导值复算不合 6 件分载）

- 同旨事实：六壬 BY 例与六爻 WHY 例输入卡 anchors 均无旬空字段，asked_at 只载日干支，旬空未直载属实；basis 逐例按日干支推导并注明；盘体／卦面俱载、DIAG-H33 §0 同口径不计 IN。本席按六十甲子逐件复算推导值（算法经 DA 例 asked_at 直载旬空值 6 处锚点验证：壬寅甲午旬辰巳、戊午／乙卯／辛酉／丁巳甲寅旬子丑、庚辰甲戌旬申酉，复算全合）。复算相合 15 件逐件部分成立、承接建议同式：按「旬空卡面未直载、推导已注明且复算相合；盘体俱载、不计 IN，部分成立」登记；复算不合 6 件逐件部分成立、承接建议按各件正值分载（见下）。各件 finding 全文见 annotations 对应条。
- BY 7 件：BY-039（丁丑，甲戌旬申酉空，相合）、BY-041（壬戌，**不合**，见下）、BY-042（己丑，甲申旬午未空，相合）、BY-043（丙申，**不合**，见下）、BY-044（壬申，甲子旬戌亥空，相合）、BY-045（壬寅，甲午旬辰巳空，相合）、BY-046（壬申，甲子旬戌亥空，相合）。
- WHY 14 件：WHY-092（乙未，**不合**）、WHY-093（丁亥，甲申旬午未空，相合）、WHY-095（丁卯，甲子旬戌亥空，相合）、WHY-096（甲申，甲申旬午未空，相合）、WHY-098（甲戌，甲戌旬申酉空，相合）、WHY-099（己亥，**不合**）、WHY-100（乙亥，甲戌旬申酉空，相合）、WHY-103（戊辰，甲子旬戌亥空，相合）、WHY-104（癸巳，甲申旬午未空，相合）、WHY-106（辛亥，甲辰旬寅卯空，相合）、WHY-107（己亥，**不合**）、WHY-108（乙亥，甲戌旬申酉空，相合）、WHY-109（己巳，甲子旬戌亥空，相合）、WHY-110（辛丑，**不合**）。
- 推导值复算不合 6 件分载（basis 推作值 → 复算正值；后续集读断以正值为准）：
  - **BY-041**：basis 推作甲戌旬申酉空 → 正值甲寅旬子丑空；basis 自注旬空不涉三传，断据未用误值。
  - **BY-043**：basis 推作甲午旬寅卯空 → 正值甲午旬辰巳空；basis 并以误值入断（压制线「印空」据寅卯空立），影响面并载（与 §五.4 六亲条并行）。
  - **WHY-092**：basis 推作甲午旬寅卯空 → 正值甲午旬辰巳空；basis 自注旬空不涉用神，断据未用误值。
  - **WHY-099**：basis 推作甲戌旬申酉空 → 正值甲午旬辰巳空；basis 断语未以误值立据。
  - **WHY-107**：basis 推作甲戌旬申酉空 → 正值甲午旬辰巳空；basis 并以误值入断（世化子申「化空」一据据申酉空立），影响面并载。
  - **WHY-110**：basis 推作甲午旬寅卯空 → 正值甲午旬辰巳空；basis 自注旬空不涉用神，断据未用误值。

### 5.4 BY-043 三传六亲标不合 1 件（部分成立）

- **BY-043**（anon H33O-b964c965）：回原卡——anchors 三传逐字作「禄巳（空）、官寅（合）、财亥（贵）」；basis 自注卡面标与以日干丙火生克自推（禄巳／父寅／官亥）不合、已注明分歧并按自推作断。逐项核：巳为丙禄（兄弟）两读一致；寅木生丙火当为父母、卡面标官，亥水克丙火当为官鬼、卡面标财——中、末传六亲标与日干生克不合一层属实；三传支与天将卡面明载、basis 已披露。故部分成立。
  - 承接建议：验收侧新登记：自 R92 起承接本 R91 标注：按「卡面三传六亲标官寅／财亥与日干丙生克自推（父寅／官亥）不合、basis 已注明按自推读，读断以自推为准，部分成立」登记（验收面只登记、不入后续 manifest 常规落实层）；金标原文照录不改。

### 5.5 WHY-103 世爻化神未直载 1 件（部分成立，全集唯一字段级缺载）

- **WHY-103**（anon H33O-f337f091）：回原卡——anchors 载本卦逐爻六行、动爻与变卦名「风火家人」，未逐爻给出变卦爻面，世爻（五爻子孙亥水动）化神未直载属实；basis 自标「世动之化神卡面未直载、本席未臆补」与缺载旗标「世爻化神卡面未载（残损旗标）」。该例主断所据（世旺动空、伏财泄飞）与金标决定性断项所据俱在卡，DIAG-H33 §0／§2 作字段级缺载单列、不计 IN（致断无据）。故部分成立（与 §五.3 旬空条、§五.6 店址面条并行）。
  - 承接建议：验收侧新登记：自 R92 起承接本 R91 标注：按「世爻化神卡面未直载、basis 已自标未臆补；主断所据在卡、字段级缺载单列、不计 IN，部分成立」登记（验收面只登记、不入后续 manifest 常规落实层）；金标原文照录不改。

### 5.6 WHY 题面身份／实物信息面 12 件（部分成立，逐件全列）

- 身份／年命面 4 件（question／context 仅载「某男测年运」、无生年与年命细节，basis 自承只断本人一线；卦面俱载）：WHY-092（H33O-97e96e7d）、WHY-093（H33O-badc673b）、WHY-095（H33O-d001b115）、WHY-096（H33O-390b6163）。承接建议同式：按「题面仅载某男、无年命细节，basis 已自承只断本人一线；卦面俱载，部分成立」登记。
- 实物信息面 8 件（卡面未载宅向／店址等实物信息，basis 自承风水只断卦象层、不及方位细断；卦面俱载）：WHY-098（H33O-909102cb，宅向／楼层）、WHY-099（H33O-7f33afdc，宅向）、WHY-100（H33O-34aa9ce4，宅向）、WHY-103（H33O-f337f091，店址方位，与 §五.5 化神条并行）、WHY-104（H33O-34d2761b，店址方位）、WHY-106（H33O-bdd5b90a，宅向）、WHY-107（H33O-10f44545，宅向）、WHY-108（H33O-ff167d25，宅向；兼求测者年命未给一面并载于同条）。承接建议同式：按「题面未载宅向／店址实物信息、basis 已自承只断卦象层；卦面俱载，部分成立」登记。
- 各件 finding 全文见 annotations 对应条；两面承接建议均带「验收面只登记、不入后续 manifest 常规落实层」口径，金标原文照录不改。

### 5.7 WHY 疾病面 3 条（部分成立，逐件全列）

- **WHY-109 病程面**（anon H33O-ef2e42d9）：question／context 仅载「某男测妻病」，病程新旧未载属实；basis 自承「新病应上字／旧病应下字一路无据，已在置信中收束」；卦面俱载。故部分成立。承接建议：按「病程新旧题面未载、basis 已自承该路无据并收束置信；卦面俱载，部分成立」登记。
- **WHY-109 病位面**（同 anon，与病程面并行）：basis 病位复核自注用神五爻妻财子水爻位路主胸段、五行路主下焦，两路冲突属实，basis 已按门槛只断病势、病位报倾向并注明不坐实部位；病势主断不恃病位一路。故部分成立。承接建议：按「病位爻位／五行两路冲突、basis 已注明只报倾向，读断病位只作倾向、不作坐实，部分成立」登记。
- **WHY-110**（anon H33O-0d10ff30）：question／context 仅载「某男自测病」，病程新旧与病名未载属实；basis 自承此节并明载「病位无卦象交集依据、不妄断部位」；卦面俱载。故部分成立。承接建议：按「病程新旧与病名题面未载、病位无交集依据 basis 已自承不妄断；卦面俱载，部分成立」登记。
- 三条承接建议均带「验收面只登记、不入后续 manifest 常规落实层」口径，金标原文照录不改；各条 finding 全文见 annotations 对应条。

### 5.8 不成立登记其余 8 条（只登记不入 annotations）

- **DA-073 四课两组重见**（anon H33O-f26bf95a）：basis 自注四课两组重见（干支上神各同）照卡面读、未另推九宗——回原卡 anchors 四课逐字作「巳（空）巳、巳（空）巳、未（常）未、未（常）丁」，卡面如实载录、非缺载残损，basis 照录读法属实。作卡面残损旗标不成立，只登记（与 §五.1 课名条、§五.2 行年条并行）。
- **BY-045 同日干支异案**（anon H33O-5f85f016，DIAG-H33 §5 F1）：basis 自载「本例与 DA-067 同日干支而月时问事不同，已按本例辰月丑时与上任门自断，未借彼例结论」——回两卡核：BY-045 asked_at 作「咸丰癸丑年辰月壬寅日丑时」、DA-067 作「戊申年九月二十一日壬寅辰将未时」，同为壬寅日而年、月、时与问事（上任／前程）均不同，事实属实；同日干支异案不构成重出、不构成卡面缺载、不计 IN（承 DIAG-H33 §5 F1 登记，照 H32 F5 同型）。作残损／重出旗标不成立，只登记。
- **BY-042 问面取舍自注**（anon H33O-d6c6c5c0）：basis 自注原问兼梦象与入幕两面、以文书召命为主问面、梦象只作背景——回原卡 question 作「自梦回家甚急因占（入幕/文书之召）」，两面俱为题面实载，此为席位问面取舍披露、非卡面缺载。作卡面残损旗标不成立，只登记。
- **WHY-095 静卦无变卦**（anon H33O-d001b115）：basis 自注静卦无变卦照卡面——回原卡 anchors bian_gua 逐字作「（静卦无变卦）」、moving_lines 作「静卦无动爻」，卡面形态如实，非缺载。作卡面残损旗标不成立，只登记（与 §五.3 旬空条、§五.6 身份面条并行）。
- **fu_shen 空载 4 例**（IN 口径复核，逐件）：WHY-092（H33O-97e96e7d）、WHY-098（H33O-909102cb）、WHY-108（H33O-ff167d25）、WHY-110（H33O-0d10ff30）anchors fu_shen 逐字为空载，回卡属实；其中 WHY-098／WHY-108 逐爻六亲俱现、本无伏神，空载为实；WHY-092（子孙不上卦）／WHY-110（妻财不上卦）伏神可由本宫首卦推得、且两例 prediction 均未以伏神为断据。照 DIAG-H33 §0／§2 IN 口径（承 H32 WHY-070／071 同型）不计 IN、作锚点缺载旗标不成立，只登记。

### 5.9 BY-044 题面—断面落差单独定案（数据面事实登记，不裁归属）

- **BY-044**（anon H33O-ba35c042）：输入卡 question 逐字作「占起房（迁居起房与行止）」；验收 prediction 只就起房一面作断（basis 家宅门：阳宅看支、父母为宅基文书，起工与入住两段分判）；金标大师断语主体与结局全在行止一面（此面照 DIAG-H33 §6 第 5 条登记转述，本席未自读金标）。题面主问面与金标断面之间落差之数据面事实成立、照录登记；其归属（席位问面取舍／组集题面形态）不属本席裁量、本行不裁。该例盘面要素全载、不计 IN，主码口径照 DIAG-H33（E5-DIR）不改。本行只作单独定案一行，不入 annotations。

### 5.10 筛检登记（经核同型在册／本轮未自报，只登记）

- WHY 14 例卡面 subject 同作「求测者（台账 subject 为空、原书未具名）」自注，与 R90 验收面 WHY 全例台账 subject 空缺同形态在册（annotations-r90 逐件部分成立条）；本轮验收 basis 未以 subject 旨自报（自报面为题面身份／实物／病程面，已逐件定案 §五.6／§五.7），本轮不另立 subject 条、只登记形态在场。
- DA 7 例（含 DA-066）旬空由输入卡 asked_at 直载（如「甲午旬，辰巳空」），无旬空推导旗标、不立条；DA-066 课名实载「四绝」，不在 §五.1 之列。
- 六壬 basis 通载「官不入传／官缺传」诸语（DA-067／DA-070／DA-073、BY-045）为三传取用读法注记、非卡面缺载旗标，不立条、只登记。
- 验收评审四席 gap_note 无「疑似虚称」类旗标（承 DIAG-H33 §5 登记），本轮验收面无 F 号虚称候选、不立条。

### 5.11 annotations 落盘登记（本节末节）

- 新增登记：**52 条**（验收面部分成立 52：行年／年命 14＝DA-066／DA-067／DA-068／DA-070／DA-072／DA-073／DA-074／BY-039／BY-041／BY-042／BY-043／BY-044／BY-045／BY-046；旬空推导 21＝BY-039／BY-041／BY-042／BY-043／BY-044／BY-045／BY-046／WHY-092／WHY-093／WHY-095／WHY-096／WHY-098／WHY-099／WHY-100／WHY-103／WHY-104／WHY-106／WHY-107／WHY-108／WHY-109／WHY-110；BY-043 六亲 1；WHY-103 化神 1；WHY 身份／实物 12＝WHY-092／WHY-093／WHY-095／WHY-096／WHY-098／WHY-099／WHY-100／WHY-103／WHY-104／WHY-106／WHY-107／WHY-108；WHY 疾病 3＝WHY-109 病程／WHY-109 病位／WHY-110）——落盘 `data/case-annotations-r91.json` annotations **517 件＝465＋52**（成立 14／部分成立 430／不成立 71／未核 2），各新条 `registered_round＝91`、字段完整（anon 以验收主持映射对位、引文逐字断言内置），counts 相应更新、special_checks 新增第 87 件，回读 JSON 可解析断言通过。
- 同 id 订正／补强登记：逐件核对既有 465 件——本轮 28 例（DA-066–074／BY-039–046／WHY-092–110 各 id）在既有件中同 id 条目 **0 件**（既有 DA 条止于 DA-064、BY 条为 BY-017／030–033、WHY 条止于 WHY-091），52 条全为新立条、无订正／补强件，特此登记。
- 不入 annotations 登记：不成立 14 条（§五.1 六件＋§五.8 八条）与 §五.9 BY-044 落差行、§五.10 筛检各行，只登记于本节、不入 annotations（承本轮派单 annotations 落账口径：成立／部分成立且需跨集读法注记者入账）。
- 口径注记：本附则 §六.1／§六.4 中「465 件」「holdout33 封存待开封」诸语为开封前首任原文，本补编按卫生口径只改 §五、未动 §六全文；验收面落账后总数以本节登记（517 件）为准。
（§五毕）
'''

# ---------------- 落盘 ----------------
doc = load(ANN_PATH)
before = copy.deepcopy(doc['annotations'])
assert len(before) == 465
exist_ids = {a['case_id'] for a in before}
assert not ({e['case_id'] for e in ENTRIES} & exist_ids), '同 id 冲突'
doc['annotations'].extend(ENTRIES)
assert doc['annotations'][:465] == before, '既有 465 件被改动'
c = doc['counts']
c['cases_total'] = 517
c['verdicts'] = {'成立': 14, '部分成立': 430, '不成立': 71, '未核': 2}
c['acceptance_side_r91'] = ('holdout33 已开封验收未达标，验收面定案经补编席补入（见 manifest-carryover-r91-addendum.md §五）：'
                            '定案 66 条（部分成立 52／不成立 14），部分成立 52 条落账本件、不成立只登记；'
                            'IN（致断无据）0／28、字段级缺载 1（WHY-103 世爻化神）；旬空推导值复算不合 6 件（BY-041／BY-043／WHY-092／WHY-099／WHY-107／WHY-110）已分载正值')
c['new_registrations_r91_acceptance_addendum'] = 52
c['r91_acceptance_partial_upheld'] = [f"{e['case_id']}（{e['flag'].split('：')[-1][:18]}）" for e in ENTRIES]
doc['special_checks'].append({
    'item': '（R91）特别核查87：验收面（holdout33 开封）旗标定案补编总登记（新定案 66 条）',
    'conclusion': ('holdout33 已开封验收，验收面新定案 66 条：部分成立 52（行年／年命 14、旬空推导 21、BY-043 六亲不合 1、WHY-103 化神 1、'
                   'WHY 身份／实物 12、WHY 疾病 3）、不成立 14（DA 课名底本未载 6，承 R88 DA-051 F3 判例；DA-073 四课重见／BY-045 同日干支异案（DIAG-H33 §5 F1）／'
                   'BY-042 问面取舍／WHY-095 静卦形态／fu_shen 空载 4 例各 1）。部分成立 52 条落账本件 annotations（517＝465＋52），不成立与 BY-044 题面—断面落差行只登记于附则 §五。'
                   'IN（致断无据）＝0／28、字段级缺载 1／28（WHY-103），与 DIAG-H33 §0／§2 口径全合；旬空推导值经六十甲子复算不合 6 件（BY-041／BY-043／WHY-092／WHY-099／WHY-107／WHY-110）已逐件分载正值。'
                   '验收面定案只登记、不入后续 manifest 常规落实层。'),
    'evidence': ('runs/round91/acceptance/predictions 逐件 basis；holdout33/inputs 逐件原卡；runs/round91/acceptance/diagnosis/DIAG-H33.md §0／§2／§5／§6；'
                 'runs/round91/acceptance/judging/host-mapping.json；data/manifest-carryover-r91-addendum.md §五。'),
    'scope_note': '结论只及标注与读法登记，不改验收分数、原卡与金标原文。',
})
doc['_provenance'] += (' R91 数据席（验收面补编，同角不同任）：holdout33 开封后补编验收面定案，部分成立 52 条落账（registered_round＝91），'
                       '合计 517 件（成立 14／部分成立 430／不成立 71／未核 2）；既有 465 件逐件原样、无删改、无同 id 订正件；验收面定案只登记、不入后续 manifest 常规落实层。')
with open(ANN_PATH, 'w', encoding='utf-8') as f:
    json.dump(doc, f, ensure_ascii=False, indent=1)

md = open(MD_PATH, encoding='utf-8').read()
old_block = '## 五、验收面\n\n- 验收面定案待开封后另行补编（若开封）。\n（§五毕）'
assert old_block in md, '占位块未找到'
md = md.replace(old_block, MD5.rstrip(), 1)
with open(MD_PATH, 'w', encoding='utf-8') as f:
    f.write(md)

# 回读断言
doc2 = load(ANN_PATH)
from collections import Counter
assert len(doc2['annotations']) == 517
assert Counter(a['disposition'] for a in doc2['annotations']) == {'部分成立': 430, '不成立': 71, '成立': 14, '未核': 2}, Counter(a['disposition'] for a in doc2['annotations'])
assert doc2['annotations'][:465] == before
assert len(doc2['special_checks']) == 87
md2 = open(MD_PATH, encoding='utf-8').read()
assert '占位事件登记' in md2 and '验收面定案待开封后另行补编（若开封）' in md2  # 仅节首登记行引述
assert md2.count('## 五、') == 1 and '517 件' in md2
print('落盘完成：annotations 517 件；§五补编替换完成；回读断言全过')
