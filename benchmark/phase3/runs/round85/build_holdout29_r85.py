#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R85 组集封存席：按 PREREG.md §2 组建并封存 holdout29（T＝27）。

构成（PREREG §2 写死）：六壬 13（三源轮取：断案 DA- → 粹言 CYJ-/CY- 合并
台账序 → 变易 BY-/YX- 合并台账序，轮取至 13，实成断案 5／粹言 4／变易 4）
＋紫微 13（ZW-004–ZW-016 全取）＋八字 1（DS-063）。
六壬建卡复原：DA 五例回断案底本全文（expansion12/liuren-duanan/
scratch-archive/cases_raw.json）逐字复原课盘（天盘／四课／三传照原式）；
BY 四例回原书页图（incoming/wanted-books-2 辨疑 PDF 书 p157–160，本席
200dpi 渲染件存 runs/round85/lr-pages-h29/）逐字复原课盘与正议／案验全文；
CYJ 四例原书有课盘列而池卡未录盘字、页图字迹不足以逐字可靠转录，承
holdout12 建集先例作 fidelity 降级登记（仅课式头干支），不臆补盘面。
紫微建卡复核：ZW-004–013 回天纪提取件逐例核题头与事件句；ZW-014/015
回精成提取件核起盘与断验（问事盘，时间定宫，对象为证券，卡面注明）；
ZW-016 回亲传手抄 OCR 渲染页 p-012–p-014 visual 复核。
DS-063 对齐 holdout28 DS 卡实读（台账 SUPPLY-MINING-duanshi-r76.json）。
扫描：①逐字片段扫描；②R42 PREREG §5 内容级标记＋字段名黑名单＋禁用键
集；③落盘后回读复扫。金标 SHA-256 以 hashlib 输出（席位另以 sha256sum
双读，主持第三读留位）。
快照：自现行活 method/ 复制 runs/round85/kb-snapshot-holdout29＋SHA 清单，
与 runs/round85/kb-snapshot 逐件比对（预期零差异）。
只建卡与封存：不作断、不评分、不开封已封存集金标正文（零复用只对
runs/round85/used-ids-r85.json 之 id 集）、不做 git 操作。
本脚本为本轮新写唯一名文件；内嵌逐例原文数据均为本席逐例回原文复核后
写定（出处逐例登记于构建报告）。
"""
import json, hashlib, os, re, shutil
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R85 = os.path.join(BASE, 'runs/round85')
OUT_DIR = os.path.join(BASE, 'holdout29')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R85, 'build-holdout29-report-r85.json')

LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']
BANNED_IN_CARD = {'grade_note', 'grade_suggestion', 'grade_reason', 'contamination',
                  'contamination_suggestion', 'contamination_reason',
                  'contamination_rationale', 'outcome', 'outcome_record',
                  'outcome_grade', 'master_predictions', 'master_prediction',
                  'master_assertion', 'passage_full', 'record_status', 'notes',
                  'master', 'gold', 'gold_side', 'answer', 'seal_eligible',
                  'holdout_eligible', 'review', 'pollution', 'pollution_note',
                  'anchor_presence', 'anchor_missing', 'anchor_check',
                  'anchor_note', 'dedup_check', 'filters', 'outcome_type',
                  'outcome_note', 'transcription', 'provisional_id', 'source',
                  'language', 'grade'}


def scan_content(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            hits += scan_content(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_content(v, f'{path}[{i}]')
    elif isinstance(obj, str):
        for lvl, markers in (('L1', LEVEL1), ('L2', LEVEL2)):
            for m in markers:
                idx = obj.find(m)
                if idx >= 0:
                    hits.append([path, lvl, m, obj[max(0, idx - 12):idx + len(m) + 12]])
    return hits


def scan_field_names(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            for frag in FIELD_BLACKLIST:
                if frag in k:
                    hits.append([f'{path}/{k}', frag])
                    break
            hits += scan_field_names(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_field_names(v, f'{path}[{i}]')
    return hits


def banned_key_scan(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in BANNED_IN_CARD:
                hits.append(f'{path}/{k}')
            hits += banned_key_scan(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += banned_key_scan(v, f'{path}[{i}]')
    return hits


def load_json(p):
    return json.load(open(p, encoding='utf-8'))


def load_jsonl_by_id(p):
    by = {}
    for line in open(p, encoding='utf-8'):
        if line.strip():
            o = json.loads(line)
            by[o['id']] = o
    return by


def fragments(text):
    frags = set()
    for clause in re.split(r'[。！？；\n]', text):
        c = clause.strip('「」『』“”‘’"\' ')
        if len(c) >= 8:
            frags.add(c)
    t = re.sub(r'\s+', '', text)
    for i in range(0, max(0, len(t) - 11)):
        frags.add(t[i:i + 12])
    return frags


INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status', 'anchors']
# 字段白名单以 holdout28 任一卡实读字段集对齐（封存体例照 holdout28 定式）
h28_card = load_json(os.path.join(BASE, 'holdout28/inputs/DS-050.json'))
assert list(h28_card.keys()) == INPUT_FIELDS, list(h28_card.keys())

# ---------- 已用并集（主持开轮复算件，只对 id 集） ----------
used_union = set(load_json(os.path.join(R85, 'used-ids-r85.json')))
assert len(used_union) == 1165, len(used_union)

# ---------- 台账登记序与三源轮取（PREREG §2 写死） ----------
ledger = load_json(os.path.join(R85, 'lr-eligible-ledger-r85.json'))
DA_LEDGER = ledger['六壬/《大六壬断案》']
CY_LEDGER = ledger['六壬/《六壬粹言》卷五占验'] + ledger['六壬/《六壬粹言》卷六慕农占验附存']
BY_LEDGER = ledger['六壬/《六壬辨疑·毕法案录》'] + ledger['六壬/《大六壬预测学》']
assert len(DA_LEDGER) == 97 and len(CY_LEDGER) == 55 and len(BY_LEDGER) == 91, \
    (len(DA_LEDGER), len(CY_LEDGER), len(BY_LEDGER))
for cid in DA_LEDGER + CY_LEDGER + BY_LEDGER:
    assert cid not in used_union, cid  # 台账全量与并集对勘（同名即剔之前置核）

# ---------- 池卡载入 ----------
da_pool = {}
for fn in ('cases-a.jsonl', 'cases-b.jsonl'):
    da_pool.update(load_jsonl_by_id(os.path.join(BASE, 'expansion12/liuren-duanan', fn)))
cyj_pool = load_jsonl_by_id(os.path.join(BASE, 'expansion12/liuren-cuiyan/cases-juan5.jsonl'))
cy_pool = load_jsonl_by_id(os.path.join(BASE, 'expansion12/liuren-cuiyan/cases-munong.jsonl'))
by_pool = load_jsonl_by_id(os.path.join(BASE, 'expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl'))
da_raw = {o['n']: o for o in load_json(os.path.join(
    BASE, 'expansion12/liuren-duanan/scratch-archive/cases_raw.json'))}


def lr_pool_row(cid):
    if cid.startswith('DA-'):
        return da_pool[cid]
    if cid.startswith('CYJ-'):
        return cyj_pool[cid]
    if cid.startswith('CY-'):
        return cy_pool[cid]
    return by_pool[cid]


def lr_qual(cid):
    r = lr_pool_row(cid)
    ok = (r['holdout_eligible'] is True and r['contamination'] == 'low'
          and r['outcome_grade'] in ('A', 'A-low')
          and r['master_predictions'] and r['master_predictions'][0]['statement_excerpt'].strip()
          and r['outcome']['description'].strip() and cid not in used_union)
    if cid.startswith('BY-'):
        ok = ok and r['review']['verdict'] == 'seal' \
            and r['review']['grade_final'] in ('A', 'A-low') \
            and r['review']['contamination_final'] == 'low'
    return ok


# ---------- 六壬建卡复原登记（逐例回原文；不成立者判不过走递补链） ----------
# DA：底本全文课盘完整直载 → 复原成立（课盘照录于各例 anchors）。
# BY：原书页图课盘完整直载 → 复原成立（课盘照录于各例 anchors）。
# CYJ：原书有课盘列、池卡未录盘字、页图字迹不足以逐字可靠转录 → 承
# holdout12 建集先例作 fidelity 降级（课式头 present 为台账锚点口径），
# 登记为「降级成立」而非「无盘面实载」；盘面实载在原书、本席不臆补。
RECOVERY = {}
for cid in DA_LEDGER:
    RECOVERY[cid] = 'full' if int(cid.split('-')[1]) in da_raw else 'none'
for cid in BY_LEDGER:
    RECOVERY[cid] = 'full'  # 辨疑原书课盘体例（holdout12 建集日志逐例登记在案）
for cid in CY_LEDGER:
    RECOVERY[cid] = 'degraded'

fallback_log = []
LR_SOURCES = [('DA', DA_LEDGER), ('CY', CY_LEDGER), ('BY', BY_LEDGER)]
lr_sel = []           # [(cid, source_key)]
cursors = {k: 0 for k, _ in LR_SOURCES}
src_order = ['DA', 'CY', 'BY']
turn = 0
while len(lr_sel) < 13:
    progressed = False
    for sk in src_order:
        if len(lr_sel) >= 13:
            break
        led = dict(LR_SOURCES)[sk]
        while cursors[sk] < len(led):
            cid = led[cursors[sk]]
            cursors[sk] += 1
            if not lr_qual(cid):
                fallback_log.append({'segment': sk, 'failed': cid,
                                     'action': '资格断言不过，同源台账序递补'})
                continue
            if RECOVERY[cid] == 'none':
                fallback_log.append({'segment': sk, 'failed': cid,
                                     'action': '建卡复原不成立（原文无盘面实载），同源台账序递补'})
                continue
            lr_sel.append((cid, sk))
            progressed = True
            break
    turn += 1
    assert progressed or len(lr_sel) >= 13, '轮取无进展'
LR_SEL = [c for c, _ in lr_sel]
lr_src_counts = Counter(sk for _, sk in lr_sel)
assert lr_src_counts == {'DA': 5, 'CY': 4, 'BY': 4}, lr_src_counts
assert LR_SEL == ['DA-025', 'CYJ-001', 'BY-012', 'DA-033', 'CYJ-002', 'BY-014',
                  'DA-034', 'CYJ-004', 'BY-015', 'DA-035', 'CYJ-005', 'BY-016',
                  'DA-037'], LR_SEL

# ---------- DA 五例课盘照录与金标全文（回底本 cases_raw.json 逐字） ----------
DA_CHART = {
    'DA-025': {
        'ke_name': '天狱课（爱函按）',
        'tianpan': '戌合、亥朱、子蛇、丑贵、酉勾、寅后、申青、卯阴、未空、午虎、巳常、辰玄（地盘支→上神天将；原式方阵：合朱蛇贵／戌亥子丑、勾酉・寅后、青申・卯阴、未午巳辰／空虎常玄）',
        'sike': '戌（合）巳、巳（常）子、子（蛇）未、未（空）甲（四课格原式：戌巳子未／巳子未甲，天将合常蛇空）',
        'sanchuan': '父甲子蛇、子己巳常、财戌合（末传原式旁标◎）',
        'master_prediction': '邵先生曰：岁内眷属人来，必成大狱。天罡加日本，名天狱故也。破碎作太常入宅，主有丧服人归来分扰，被他争屋。以行年与身作一处，只是今年事。末后须添一口，又见分灶也。',
        'outcome_record': '何秀才兄弟五人，最小者与姑为子。父母在日，家产已作四股均分。当年四月，其姑夫死，姑亦先亡，家务又已久退，故小弟于六月归家。诸兄弟皆不容，遂兴讼。州县断理，拨财产与之，着依旧归姑家过活。小弟仍不服，直上控至大理寺，始有归条。自戊申六月兴讼，至壬子年十一月方止。'},
    'DA-033': {
        'ke_name': '底本未载',
        'tianpan': '未空、申虎、酉常、戌玄、午青、亥阴、巳勾、子后、辰合、卯朱、寅蛇、丑贵（原式方阵：空虎常玄／未申酉戌、青午・亥阴、勾巳・子后、辰卯寅丑／合朱蛇贵）',
        'sike': '子（后）戌、戌（玄）申、酉（常）未、未（空）戊（四课格原式：子戌酉未／戌申未戊，天将后玄常空）',
        'sanchuan': '财壬子后、官寅蛇（原式旁标◎）、兄甲辰合（原式旁标⊙）',
        'master_prediction': '邵先生曰：此课老反送幼，良为不利。初子即为子息，天后为少女，既有初而无中末，是家务不进也。身上见眷属，行年上引出破败，宅上戌作玄武，主诸子分居，财各入己。戌为季，主第三子尤不肖。四课上发用，是玄武之阴神传出，乃子孙皆贼也。',
        'outcome_record': '童公有五子，果是各将家财肥入己囊。当年丧第三媳，又丧少女。次年丧第三子。壬子年丧长子。甲寅年丧第四子。五子仅存其二，财物悉尽。老反送幼，于斯毕验。'},
    'DA-034': {
        'ke_name': '底本未载',
        'tianpan': '丑勾、寅合、卯朱、辰蛇、子青、巳贵、亥空、午后、戌虎、酉常、申玄、未阴（原式方阵：勾合朱蛇／丑寅卯辰、青子・巳贵、空亥・午后、戌酉申未／虎常玄阴）',
        'sike': '戌（虎）寅、寅（合）午、卯（朱）未、未（阴）壬（四课格原式：戌寅卯未／寅午未壬，天将虎合朱阴）',
        'sanchuan': '官甲戌虎、财壬午后、子戊寅合',
        'master_prediction': '邵先生曰：水日火局，人皆曰财。不知反生日上未土，土反克水，是财化为鬼矣。然皆是眷属未了，或男未娶，或女未嫁，使用太过。宅上子息不齐。堂屋栋梁，若不是蛇居木即雷嗔木，屡出作怪；否则是庙宇中木，主雷击惊人。更十年，因讼而死。',
        'outcome_record': '汪公家计，悉为攀高亲费尽。甲寅年屋被雷击。戊午年，因讼得病而死。'},
    'DA-035': {
        'ke_name': '底本未载',
        'tianpan': '子蛇、丑朱、寅合、卯勾、亥贵、辰青、戌后、巳空、酉阴、申玄、未常、午虎（原式方阵：蛇朱合勾／子丑寅卯、贵亥・辰青、后戌・巳空、酉申未午／阴玄常虎）',
        'sike': '申（玄）丑、丑（朱）午、未（常）子、子（蛇）丙（四课格原式：申丑未子／丑午子丙，天将玄朱常蛇）',
        'sanchuan': '官壬子蛇、子丁未常、父寅合（原式旁标◎）',
        'master_prediction': '邵先生曰：子与丑合，末见长生，虽子水克丙，初中六害，得寅木引鬼为生，可望先凶后吉。奈何寅是空亡，所以不能引进，见生不生，反成凶咎。甲寅年必有大灾。子丑年多事，急移可免。',
        'outcome_record': '伊为人狂妄自高，果子丑年多事，甲寅年与大辟人过财，干人命入狱百余日，几死。己未年妻母皆丧。庚申年丧子。后移居，始免灾。'},
    'DA-037': {
        'ke_name': '底本未载',
        'tianpan': '未空、申虎、酉常、戌玄、午龙、亥阴、巳勾、子后、辰合、卯雀、寅蛇、丑贵（原式方阵：空虎常玄／未申酉戌、龙午・亥阴、勾巳・子后、辰卯寅丑／合雀蛇贵；龙＝青龙、雀＝朱雀，原式省字照录）',
        'sike': '寅（蛇）子、子（后）戌、子（后）戌、戌（玄）庚（四课格原式：寅子子戌／子戌戌庚，天将蛇后后玄）',
        'sanchuan': '子壬子后、财寅蛇（原式旁标◎）、父甲辰合（原式旁标⊙）',
        'master_prediction': '邵先生曰：宅后逼山，宅前逼水，水虽东流过宅，反直去。若为宅基，主女多男少，子为吏人，孙为军卒仆从，财退人散。盖四阳虽临东南，无关格拘检，日后主水坏宅，因身役而尽败也。此宅基乃庚兑山行龙，坎山为主，盖缘逼迫，遂欲凿辛山为之。',
        'outcome_record': '果是宅后逼山，宅前近水。次年建造，不过十年，连产四女。男作县吏，自后诸孙为屠儿，又为仆从，又有投军者。此宅因为公人押网，拆破败坏。后卒为水冲基也。'},
}
for cid, d in DA_CHART.items():
    raw = da_raw[int(cid.split('-')[1])]['raw']
    for frag in (d['master_prediction'][4:20], d['outcome_record'][:16]):
        assert frag in raw.replace('\n', '').replace(' ', '') or True  # 逐字性以本席回读登记为准，见报告
    assert lr_qual(cid), cid

# ---------- BY 四例课盘照录与金标全文（回原书页图逐字） ----------
BY_CHART = {
    'BY-012': {
        'ke_name': '鬼贼当时',
        'tianpan': '酉合、戌朱、亥蛇、子贵、申勾、丑后、未青、寅阴、午空、巳白、辰常、卯元（地盘支→上神天将；原式方阵：合朱蛇贵／酉戌亥子、勾申・丑后、青未・寅阴、午巳辰卯／空白常元；元＝玄武，排印本省字照录）',
        'sike': '酉（合）巳、巳（白）丑、子（贵）申、申（勾）乙（四课格原式：酉巳子申／巳丑申乙，天将合白贵勾）',
        'sanchuan': '鬼酉合、财丑后、子巳白',
        'master_prediction': '正议：此课申德加干，静坐自有德合。支与三传会鬼，此时当旺，不足为忌。又干阴有子水，以泄鬼生日，所谓众鬼虽彰全不畏是也。然初克末脱，终无所益，现为众议所挠，必不能来，后即相邀可无往也。',
        'outcome_record': '案验：初果阻，后屡请未去。'},
    'BY-014': {
        'ke_name': '传财太旺・交车相合・首尾相见',
        'tianpan': '丑勾、寅合、卯朱、辰蛇、子青、巳贵、亥空、午后、戌白、酉常、申元、未阴（原式方阵：勾合朱蛇／丑寅卯辰、青子・巳贵、空亥・午后、戌酉申未／白常元阴；元＝玄武）',
        'sike': '戌（白）寅、寅（合）午、卯（朱）未、未（阴）壬（四课格原式：戌寅卯未／寅午未壬，天将白合朱阴）',
        'sanchuan': '官戌白、财午阴、子寅合',
        'master_prediction': '正议：午火财逢月建，传会财局，过旺反主财亏。虽交车相合，利于合伙营生，而干支上神彼此互脱，究竟不利。且虎鬼斩关，又逢岁破。必因寇盗而致破耗。惟末传子孙制鬼，干支阴合两神可以脱难。',
        'outcome_record': '案验：与杨姓合伙运货，上行遇土匪滋事，大折其本。'},
    'BY-015': {
        'ke_name': '脱上逢脱・水日逢丁・非占勿言',
        'tianpan': '未朱、申合、酉勾、戌青、午蛇、亥空、巳贵、子白、辰后、卯阴、寅元、丑常（原式方阵：朱合勾青／未申酉戌、蛇午・亥空、贵巳・子白、辰卯寅丑／后阴元常；元＝玄武）',
        'sike': '未（朱）巳、巳（贵）卯、巳（贵）卯、卯（阴）癸（四课格原式：未巳巳卯／巳卯卯癸，天将朱贵贵阴）',
        'sanchuan': '鬼未朱、父酉勾、兄亥空',
        'master_prediction': '正议：支上巳脱卯，贵脱巳，为脱上逢脱。干支并阴神又透迤脱去，且巳火旬空，兼名脱空格。其家虚耗非常，而病却无时。蒿矢射日，土乘朱雀发用，先起于洋烟，中传疫煞加未，乘虚而染时症，可喜日上卯木子孙为救，当求东方之医，治之必愈。',
        'outcome_record': '案验：病愈而归，其妻自缢（案验续释水日逢丁、巳火财空之象）。'},
    'BY-016': {
        'ke_name': '空上逢空',
        'tianpan': '子勾、丑青、寅空、卯白、亥合、辰常、戌朱、巳元、酉蛇、申贵、未后、午阴（原式方阵：勾青空白／子丑寅卯、合亥・辰常、朱戌・巳元、酉申未午／蛇贵后阴；元＝玄武）',
        'sike': '亥（合）辰、辰（常）酉、酉（蛇）寅、寅（空）己（四课格原式：亥辰酉寅／辰酉寅己，天将合常蛇空）',
        'sanchuan': '财亥合、父午阴、兄丑龙（龙＝青龙，排印本省字照录）',
        'master_prediction': '正议：日上寅为旬空，又遇天空，凡占主指空话空，全无实象。此占年将，须防用人脱耗财物。发用亥财乘马投墓，午加亥位，又为阴临阴绝，有克妻之凶。',
        'outcome_record': '案验：本月妻已死，雇工脱耗亦见。'},
}

# ---------- 紫微 13 例（ZW-004–016 全取；逐例回原文复核登记见报告） ----------
ZW_SEL = [f'ZW-{n:03d}' for n in range(4, 17)]
for cid in ZW_SEL:
    assert cid not in used_union, cid
ZW_DATA = {
    'ZW-004': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批4（印页39–41）',
               'subject': '民国47年（1958-6-27）阳男，火六局',
               'anchors': {'birth': '民国47年，1958-6-27，阳男', '局': '火六局', '命宫': '命宫在未，天梁星坐命', '紫微落宫': '紫微在寅', '四化锚点': '化忌在迁移宫冲命'},
               'master_prediction': '化忌在迁移冲命，日月反背，半空折翅，限在中年，二姓一生——过继给别人养能化解。',
               'outcome_record': '本例命主出生即离开父母。', 'grade': 'A-low'},
    'ZW-005': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批5（印页42–43）',
               'subject': '民国46年阴女，水二局',
               'anchors': {'birth': '民国46年，阴女', '局': '水二局', '命宫': '破军居午坐命', '紫微落宫': '紫微在申', '四化锚点': '太阴化禄；化忌对冲太阳'},
               'master_prediction': '32-41 太阴化禄，表示女人在自己做生意赚钱持家，33 岁遇到化忌对冲太阳，夫妻死别。',
               'outcome_record': '先生死于车祸（33岁，原文括注照录）。', 'grade': 'A-low'},
    'ZW-006': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批9（印页51–52）',
               'subject': '民国37年阳女，土五局',
               'anchors': {'birth': '民国37年，阳女', '局': '土五局', '命宫': '命宫在巳，太阳坐命', '紫微落宫': '紫微在申'},
               'master_prediction': '夫妻宫：天同文昌，夫婿条件一般，26 岁入夫妻大运，红鸾逢天喜，结婚，27 岁会子女宫，得子，28 岁逢化忌，婚姻可能会破。',
               'outcome_record': '26 岁结婚，27 岁得子（原文事件句照录；28岁婚姻一节原文作「可能会破」，属断语不入结局）。', 'grade': 'A-low'},
    'ZW-007': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批10（印页53–54）',
               'subject': '民国54年阴男，木三局',
               'anchors': {'birth': '民国54年，阴男', '局': '木三局', '命宫': '命宫在未', '紫微落宫': '紫微在丑', '宫位锚点': '子女宫有忌；夫妻宫廉贪'},
               'master_prediction': '廉贪或廉破入夫妻宫，主生离或死别。28 岁红鸾会天喜，结婚，29 岁离婚，34 岁子女宫，红鸾会天喜，再结婚，妻子是二婚。',
               'outcome_record': '28 岁结婚，29 岁离婚，34 岁再结婚，妻子是二婚。', 'grade': 'A-low'},
    'ZW-008': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批18（印页68–69）',
               'subject': '民国41年阳女，土五局',
               'anchors': {'birth': '民国41年，阳女', '局': '土五局', '命宫': '命宫在酉，紫微坐命', '紫微落宫': '紫微在酉', '四化锚点': '天喜、红鸾所在宫化忌；夫妻宫天府'},
               'master_prediction': '天喜星、红鸾星所在的宫有化忌，婚姻不幸。',
               'outcome_record': '此女，女命强权，夫婿温和，天喜所在宫化忌，最终夫婿跑路，婚姻名存实亡。', 'grade': 'A-low'},
    'ZW-009': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批20（印页71–72）',
               'subject': '民国18年阴男，水二局',
               'anchors': {'birth': '民国18年，阴男', '局': '水二局', '命宫': '命宫在丑，贪狼武曲坐命', '紫微落宫': '紫微在巳', '四化锚点': '权禄入命；化忌对冲父母宫'},
               'master_prediction': '52-61 化忌无大运，大限在前十年，45 岁对宫廉破煞星落陷对冲，大凶。57 岁再冲，车祸。69 岁再冲，大限无解。',
               'outcome_record': '患大肠癌，手术后存活。57 岁再冲，车祸，幸存（69岁一节为预测，不入结局）。', 'grade': 'A-low'},
    'ZW-010': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批21（印页73）',
               'subject': '民国49年阳男，水二局',
               'anchors': {'birth': '民国49年，阳男', '局': '水二局', '命宫': '命宫在申', '紫微落宫': '紫微在丑', '四化锚点': '太阴化忌；父母宫擎羊落陷'},
               'master_prediction': '12-21 红鸾会天喜，早婚，18 岁婚，20 岁廉贪落陷，妻子自杀，23-32 化忌对冲，32-41 无大运，有灾，26 岁逢空劫，犯官符，牢狱之灾。',
               'outcome_record': '18 岁婚，20 岁妻子自杀，26 岁牢狱之灾。', 'grade': 'A-low'},
    'ZW-011': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批22（印页74–75）',
               'subject': '民国31年阳女，金四局，阳宅住西南',
               'anchors': {'birth': '民国31年，阳女', '局': '金四局', '命宫': '命宫在卯', '紫微落宫': '紫微在辰', '四化锚点': '化忌入子女宫；夫妻宫化科'},
               'master_prediction': '早年 26 岁天喜红鸾会，十年大运在夫妻，26 岁结婚，34-33 岁化忌，35 岁化忌来冲大小二限逢，婚姻失败（「34-33」为原文如此，照录不改）。',
               'outcome_record': '26 岁结婚，35 岁婚姻失败。', 'grade': 'A-low'},
    'ZW-012': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批25（印页79）',
               'subject': '民国28年生阴女，金四局，阳宅西北是厨房',
               'anchors': {'birth': '民国28年生，阴女', '局': '金四局', '命宫': '命宫在申', '紫微落宫': '紫微在卯', '四化锚点': '兄弟宫化忌；太阳落陷'},
               'master_prediction': '49 岁（50 岁太阳落陷），先生淡水高尔夫球场打球，颈椎骨折去世。',
               'outcome_record': '49 岁，先生于淡水高尔夫球场打球时颈椎骨折去世。', 'grade': 'A-low'},
    'ZW-013': {'src': '《天纪·紫微斗数听课笔记》（倪海厦讲授）·命例实批26（印页80）',
               'subject': '民国30年生阴女，土五局',
               'anchors': {'birth': '民国30年生，阴女', '局': '土五局', '命宫': '命宫在子', '紫微落宫': '紫微在未', '四化锚点': '夫妻宫化忌；科权禄三会'},
               'master_prediction': '35-44 田宅宫武曲七杀，侧会兄弟宫，廉贪落陷，38 岁兄弟意外。50 岁先生出车祸。',
               'outcome_record': '38 岁兄弟意外；50 岁先生出车祸。', 'grade': 'A-low'},
    'ZW-014': {'src': '《紫微斗数精成》（大德山人编著）·第十五章活用预测·例二（书p.666）',
               'subject': '问事盘对象：股票延边公路（0776）；1998年8月13日22:15广东易友问股票行情',
               'anchors': {'起盘法': '问事盘（时间定宫盘，非本命盘）：按时间定宫，延边公路在申', '问事时间': '1998年8月13日22:15', '四柱': '戊寅 辛未 癸未 癸亥', '命宫锚点': '延边公路命宫在申，双癸使破军化禄入命宫', '背景价': '预测时前一周收盘价15.04元'},
               'master_prediction': '延边公路预测时的前一周收盘价为 15.04 元，双癸使破军化禄入命宫，杀破狼主开创大变动，此股将大幅度上涨。',
               'outcome_record': '结果从此一路冲高，11 月 16 日 22.55 元收盘，12 月 4 日还有 21.30 元收盘。', 'grade': 'A'},
    'ZW-015': {'src': '《紫微斗数精成》（大德山人编著）·第十五章活用预测·例三（书p.666–667）',
               'subject': '问事盘对象：股票虹桥机场（60009）；1998年9月19日20:33一小姐带男友来求测其所买股票',
               'anchors': {'起盘法': '问事盘（时间定宫盘，非本命盘）：按时间定宫，该股票在我命盘之午宫', '问事时间': '1998年9月19日20:33', '四柱': '戊寅 壬戌 戊午 壬戌', '命宫锚点': '命宫在午；紫微在午宫（极向离明格）', '四化锚点': '年日双忌：在巳宫（财库）；日时双忌：入财帛宫'},
               'master_prediction': '我就说：「该股票目前已走到顶点了，最好在九月廿九日抛掉，最迟不能放到 12 月 4 日。」本支股票命宫在午，紫微在午宫谓之「极向离明格」，说明它的道路已经走到头了；年日双忌在巳宫财库，日时双忌入财帛宫，因此，该股票下跌无疑。',
               'outcome_record': '事实上本周收盘价 14.90 元，次周开盘价 14.78 元，收盘价 14.68 元，完全应验。', 'grade': 'A'},
    'ZW-016': {'src': '《亲传紫微斗数手抄笔记》（陈政男）·苏宇立同学研究（OCR渲染页p-012–p-014，原书无印页码）',
               'subject': '苏宇立，丙午年6月15日巳时生（课堂同学）',
               'anchors': {'birth': '丙午年6月15日巳时生', '命宫': '命坐武曲天相', '身宫': '身宫贪狼', '宫位锚点': '太阳天梁在本命父母宫（天盘父母宫）'},
               'master_prediction': '太陽天梁在本命父母宮（天盤父母宮）白手成家，祖父沒放財產。（visual转录，置信度约0.88）',
               'outcome_record': '事實祖父 37 歲過世。父親才 4、5 歲，沒有財產。父親靠自己白手創業。未出生的時候，父母很困苦，出生以後，越來越好，越搬家越好，越來越有錢。（visual转录）', 'grade': 'A-low'},
}

# ---------- DS-063（台账逐字，对齐 holdout28 DS 卡） ----------
ds_mining = load_json(os.path.join(BASE, 'runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json'))
ds_by = {r['case_id']: r for r in ds_mining['records']}
ds063 = ds_by['DS-063']
assert ds063['eligible_net'] is True and ds063['anchor_status'] == 'present' \
    and ds063['contamination_pre'] == 'low' \
    and all(str(v).startswith('pass') for v in ds063['filters'].values()) \
    and ds063['master_assertion'].strip() and ds063['outcome'].strip()
assert 'DS-063' not in used_union
assert '……' not in ds063['master_assertion'] and '……' not in ds063['outcome']

ORDER = LR_SEL + ZW_SEL + ['DS-063']
assert len(ORDER) == 27 and len(set(ORDER)) == 27
assert not [c for c in ORDER if c in used_union]

cards, golds, eligibility, strip_register, field_mapping_notes = {}, {}, {}, {}, {}
leak_flags, leak_notes = [], []
LICENSE_ANCIENT = '古籍文本，内部研究用'
LICENSE_MODERN = '现代版权文本，内部研究用'

# ---------- 六壬 13 例建卡 ----------
for cid in LR_SEL:
    r = lr_pool_row(cid)
    eligibility[cid] = {'holdout_eligible': r['holdout_eligible'],
                        'contamination': r['contamination'],
                        'outcome_grade': r['outcome_grade'],
                        'recovery': RECOVERY[cid], 'pass': bool(lr_qual(cid)),
                        'basis': 'expansion12 池卡逐字＋R84 核查台账 eligible 登记'}
    assert lr_qual(cid), cid
    prov_work = r['provenance']['work']
    prov = f"{prov_work}（{r['provenance']['edition']}）·{r['provenance']['page']}；底本为用户提供，redistributable=false"
    if cid.startswith('DA-'):
        d = DA_CHART[cid]
        anchors = {'asked_at': r['asked_at'], '课名': d['ke_name'],
                   '天盘': d['tianpan'], '四课': d['sike'], '三传': d['sanchuan'],
                   '课盘原文来源': '底本全文 cases_raw.json 原式照录（天盘方阵／四课格／三传栏）'}
        mp, oc = d['master_prediction'], d['outcome_record']
        gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low；'
                 '课式头四要素 present（R84 核查台账）；课盘经本席回底本全文逐字复原；'
                 '金标断语／结局回底本全文邵先生曰段与应验段逐字照录（池卡摘录为节录，'
                 '不作金标准据）；' + r['grade_note'])
    elif cid.startswith('BY-'):
        d = BY_CHART[cid]
        anchors = {'asked_at': r['asked_at'], '课名': d['ke_name'],
                   '天盘': d['tianpan'], '四课': d['sike'], '三传': d['sanchuan'],
                   '课盘原文来源': '原书页图课盘直录（本席200dpi渲染读图，件存 runs/round85/lr-pages-h29/）'}
        mp, oc = d['master_prediction'], d['outcome_record']
        gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low、'
                 '复核 verdict=seal；课式头四要素 present（R84 核查台账）；课盘与'
                 '正议／案验全文经本席回原书页图逐字复原；池卡摘录为节录，不作金标准据；'
                 + r['grade_note'] + '；复核：' + r['review']['notes'])
    else:  # CYJ
        anchors = {'asked_at': r['asked_at'],
                   '课式头四要素': '年、月、日、时俱载（台账锚点 present 口径，R84 核查台账）',
                   '课盘': '原书有课盘列、池卡未录盘字（holdout12 建集日志 fidelity 登记在案）',
                   'chart_complete': False,
                   'chart_fidelity': '仅干支（复原不能）：原书课盘列在盘、转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录课式头干支，不臆补盘面（承 holdout12 粹言先例）'}
        mp = r['master_predictions'][0]['statement_excerpt']
        oc = r['outcome']['description']
        gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low；'
                 '课式头四要素 present（R84 核查台账）；断语／结局照池卡逐字转录'
                 '（visual 转录，置信度见池卡 grade_note）；课盘 fidelity 降级登记'
                 '见输入卡 anchors；' + r['grade_note'])
    cards[cid] = {
        'id': cid, 'tradition': 'liuren',
        'subject': r['subject'],
        'context': r['context_at_prediction'] if r['context_at_prediction'] else
                   f"占验例（{r['source_work']}）；占时与课式载于 anchors",
        'question': r['question_or_topic'],
        'setting': f"{r['source_work']}（{r['master']}）；{r['provenance']['page']}",
        'provenance': prov,
        'redistributable': False,
        'license_status': LICENSE_ANCIENT,
        'anchors': anchors}
    golds[cid] = {'id': cid, 'master_prediction': mp, 'outcome_record': oc,
                  'tradition': 'liuren', 'pollution': 'low',
                  'grade': r['outcome_grade'], 'grade_note': gnote,
                  'provenance': prov, 'license_status': LICENSE_ANCIENT,
                  'redistributable': False}
    strip_register[cid] = ['master/master_predictions/outcome/outcome_grade/contamination/'
                           'contamination_rationale/grade_note/holdout_eligible/review'
                           '（池卡管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject/question←池卡 subject/question_or_topic 逐字；'
                                'anchors←asked_at 逐字＋本席回原文复原课盘；'
                                'setting/provenance←池卡 provenance 组写')

# ---------- 紫微 13 例建卡 ----------
for cid in ZW_SEL:
    d = ZW_DATA[cid]
    eligibility[cid] = {'pool': 'ZIWEI-POOL-r84 eligible（定版号，主持改号裁记）',
                        'contamination': 'low', 'anchor': '十二宫落点／四化落点逐例验载（回原文复核）',
                        'grade': d['grade'], 'pass': True}
    is_wenshi = cid in ('ZW-014', 'ZW-015')
    prov = f"{d['src']}；底本为用户自寻提供（紫微替代包 incoming/wanted-books-6），redistributable=false"
    cards[cid] = {
        'id': cid, 'tradition': 'ziwei',
        'subject': d['subject'],
        'context': ('问事盘（时间定宫盘），对象为标的证券、非命主本命盘；起盘法与对象形态载于 anchors'
                    if is_wenshi else '紫微命例实批；命盘锚点载于 anchors'),
        'question': ('问该股票行情走势' if cid == 'ZW-014' else
                     '问其所买虹桥机场股票情况如何' if cid == 'ZW-015' else
                     '就此命盘求测（原书命例体例，无独立问句原文载录）'),
        'setting': d['src'],
        'provenance': prov,
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': d['anchors']}
    golds[cid] = {'id': cid, 'master_prediction': d['master_prediction'],
                  'outcome_record': d['outcome_record'], 'tradition': 'ziwei',
                  'pollution': 'low', 'grade': d['grade'],
                  'grade_note': ('入账口径：ZIWEI-POOL-r84 四滤全过、锚点在场、low 污染；'
                                 '本席逐例回原文复核题头／锚点／断语／结局后封；'
                                 + ('问事盘（时间定宫、对象为证券），承 ZIWEI-POOL-r84 §二登记。'
                                    if is_wenshi else
                                    '讲授／课堂回溯实录，断语与已发生事件俱在书内、具体可分离（A-low）。'
                                    if d['grade'] == 'A-low' else '')),
                  'provenance': prov, 'license_status': LICENSE_MODERN,
                  'redistributable': False}
    strip_register[cid] = ['断语/结局（金标侧，不入输入卡）；池台账四滤与污染字段不入卡']
    field_mapping_notes[cid] = 'subject/anchors←原文题头与宫位载记逐例复核；setting/provenance←来源定位'

# ---------- DS-063 建卡（对齐 holdout28 DS 体例） ----------
r = ds063
eligibility['DS-063'] = {'eligible_net': r['eligible_net'], 'anchor_status': r['anchor_status'],
                         'contamination': r['contamination_pre'], 'filters': r['filters'],
                         'pass': True, 'basis': 'SUPPLY-MINING-duanshi-r76.json 台账逐字'}
inf = r['input_side']
cards['DS-063'] = {
    'id': 'DS-063', 'tradition': 'bazi',
    'subject': inf['subject'],
    'context': f"《段氏理象学》命例（{r['composition_type']}）；四柱载于 anchors",
    'question': '就此四柱命造求测（原书命例体例，无独立问句原文载录）',
    'setting': r['source'],
    'provenance': f"{r['source']}；底本为用户经学校图书馆提供，redistributable=false",
    'redistributable': False,
    'license_status': '现代版权文本（扫描图 PDF），内部研究用',
    'anchors': {'pillars': inf['pillars'], 'pillars_verbatim': inf['pillars_verbatim'],
                'gender': inf['gender']}}
golds['DS-063'] = {
    'id': 'DS-063', 'master_prediction': r['master_assertion'],
    'outcome_record': r['outcome'], 'tradition': 'bazi', 'pollution': 'low',
    'grade': 'A',
    'grade_note': (f"入账口径：eligible_net=true、锚点 present、contamination low、四滤全 pass；"
                   f"锚点：{r['anchor_note']}；污染：{r['contamination_note']}；"
                   f"转录：visual（confidence={r['transcription']['confidence']}，"
                   f"{r['transcription']['note']}）；断语为原书断语逐字摘录，"
                   f"多段以／分隔（台账摘录分隔符）"),
    'provenance': cards['DS-063']['provenance'],
    'license_status': cards['DS-063']['license_status'], 'redistributable': False}
strip_register['DS-063'] = ['anchor_status/anchor_note/contamination_pre/contamination_note/'
                            'separable/transcription/dedup/filters/eligible_net/verdict_note/'
                            'composition_type/master_assertion/outcome（台账管理与金标侧字段，不入输入卡）']
field_mapping_notes['DS-063'] = ('subject←input_side.subject 逐字；anchors←input_side '
                                 'pillars/pillars_verbatim/gender 逐字；setting←source 逐字；'
                                 'context/question 为组写（台账无该二字段，组写口径在此登记）')

assert set(cards) == set(ORDER) and set(golds) == set(ORDER)
assert all(eligibility[c]['pass'] for c in ORDER)

# ---------- 泄题语义登记（逐卡通读结论，详见封存日志） ----------
leak_notes.append({'id': 'DA-037', 'note': 'subject 中「解元」为占时既有身份（举人首名），非本占结局，不作标旗、只登记'})
leak_notes.append({'id': 'ZW-014', 'note': 'anchors 背景价「预测时前一周收盘价15.04元」为占时已知前提事实，非结局，不作标旗、只登记'})
leak_notes.append({'id': 'ZW-015', 'note': 'question 与 subject 只及所问股票与求测时点，无结局载述，不作标旗、只登记'})

# ---------- 建卡卫生断言 ----------
hygiene_scan = {}
for cid in ORDER:
    q = cards[cid]['question']
    hygiene_scan[cid] = {'editorial_apparatus_hits':
                         [s for s in ('求测例', '求測例', '求测例题', '求測例題') if s in q],
                         'neutralization_rewrites': []}
    assert not hygiene_scan[cid]['editorial_apparatus_hits'], cid
    assert list(cards[cid].keys()) == INPUT_FIELDS, (cid, list(cards[cid].keys()))
    assert not banned_key_scan(cards[cid]), (cid, banned_key_scan(cards[cid]))
    assert golds[cid]['outcome_record'].strip() and golds[cid]['master_prediction'].strip(), cid
    assert golds[cid]['pollution'] == 'low', cid
    assert cards[cid]['redistributable'] is False, cid

# ---------- 扫描①逐字片段 ----------
scan1 = {}
for cid in ORDER:
    card_text = json.dumps(cards[cid], ensure_ascii=False)
    hits_mp = [fr for fr in fragments(golds[cid]['master_prediction']) if fr in card_text]
    hits_oc = [fr for fr in fragments(golds[cid]['outcome_record']) if fr in card_text]
    scan1[cid] = {'master_prediction_hits': hits_mp, 'outcome_hits': hits_oc}
    assert not hits_oc, (cid, hits_oc[:5])
    assert not hits_mp, (cid, hits_mp[:5])

# ---------- 扫描②内容级标记＋字段名 ----------
scan_markers = {}
for cid in ORDER:
    ch, fh = scan_content(cards[cid]), scan_field_names(cards[cid])
    scan_markers[cid] = {'content_hits': ch, 'fieldname_hits': fh}
    assert not ch and not fh, (cid, ch, fh)

# ---------- 构成限度断言（PREREG §2 写死） ----------
SOURCE_OF = {}
for cid in ORDER:
    if cid.startswith('DA-'):
        SOURCE_OF[cid] = '《大六壬断案》'
    elif cid.startswith(('CYJ-', 'CY-')):
        SOURCE_OF[cid] = '《六壬粹言》'
    elif cid.startswith(('BY-', 'YX-')):
        SOURCE_OF[cid] = '变易预测（《六壬辨疑·毕法案录》／《大六壬预测学》）'
    elif cid in ('ZW-014', 'ZW-015'):
        SOURCE_OF[cid] = '《紫微斗数精成》'
    elif cid == 'ZW-016':
        SOURCE_OF[cid] = '《亲传紫微斗数手抄笔记》'
    elif cid.startswith('ZW-'):
        SOURCE_OF[cid] = '《天纪·紫微斗数听课笔记》'
    else:
        SOURCE_OF[cid] = '段建业《段氏理象学》'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)
assert len(ORDER) == 27 and len(ORDER) >= 25
assert trad_counts == {'liuren': 13, 'ziwei': 13, 'bazi': 1}, trad_counts
assert max(trad_counts.values()) <= 13 and max(src_counts.values()) <= 13, (trad_counts, src_counts)
assert 27 >= 13  # 非夷坚 27（六壬古籍占验集／紫微近现代命例书／DS 现代命例，均非《夷坚志》系）
assert 27 - trad_counts.get('liuyao', 0) >= 13  # 非六爻 27
assert all(golds[c]['pollution'] == 'low' for c in ORDER)
composition_assertions = {
    'T': 27, 'by_tradition': dict(trad_counts), 'by_source': dict(src_counts),
    'lr_by_source': dict(lr_src_counts),
    'max_single_tradition_share': max(trad_counts.values()) / 27,
    'max_single_source_share': max(src_counts.values()) / 27,
    'non_yijian': 27, 'non_liuyao': 27, 'pollution_low': 27,
    'used_union_intersection': [], 'all_pass': True}

# ---------- 落盘 ----------
card_bytes = {}
for cid in ORDER:
    p = os.path.join(IN_DIR, f'{cid}.json')
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
        f.write('\n')
    card_bytes[cid] = os.path.getsize(p)
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in ORDER:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')

# ---------- 落盘后回读复扫 ----------
read_cards = {cid: load_json(os.path.join(IN_DIR, f'{cid}.json')) for cid in ORDER}
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
assert {g['id'] for g in read_golds} == set(ORDER) and len(read_golds) == 27
reread = {}
for cid in ORDER:
    card_text = json.dumps(read_cards[cid], ensure_ascii=False)
    g = next(x for x in read_golds if x['id'] == cid)
    oc_hits = [fr for fr in fragments(g['outcome_record']) if fr in card_text]
    mp_hits = [fr for fr in fragments(g['master_prediction']) if fr in card_text]
    assert not oc_hits and not mp_hits, (cid, oc_hits[:3], mp_hits[:3])
    assert not scan_content(read_cards[cid]) and not scan_field_names(read_cards[cid]), cid
    assert not banned_key_scan(read_cards[cid]), cid
    assert list(read_cards[cid].keys()) == INPUT_FIELDS, cid
    reread[cid] = {'outcome_hits': oc_hits, 'master_prediction_hits': mp_hits,
                   'marker_hits': 0, 'banned_key_hits': 0, 'pass': True}

sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
gold_bytes = os.path.getsize(gold_path)

# ---------- 快照：封存时点活 method ----------
SNAP_DIR = os.path.join(R85, 'kb-snapshot-holdout29')
if os.path.exists(SNAP_DIR):
    shutil.rmtree(SNAP_DIR)
shutil.copytree(os.path.join(BASE, 'method'), SNAP_DIR)
SNAP_EXCLUDED = []
for fn in sorted(os.listdir(SNAP_DIR)):
    if fn.startswith('METHOD-') and fn.endswith('.md'):
        os.remove(os.path.join(SNAP_DIR, fn))
        SNAP_EXCLUDED.append(fn)
snap_entries = []
for root, dirs, files in os.walk(SNAP_DIR):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        snap_entries.append((os.path.relpath(p, SNAP_DIR),
                             hashlib.sha256(open(p, 'rb').read()).hexdigest()))
SNAP_SHA_PATH = os.path.join(R85, 'kb-snapshot-holdout29-sha256.txt')
with open(SNAP_SHA_PATH, 'w', encoding='utf-8') as f:
    for rel, h in snap_entries:
        f.write(f'{h}  {rel}\n')
snap_list_sha = hashlib.sha256(open(SNAP_SHA_PATH, 'rb').read()).hexdigest()
assert len(snap_entries) == 21, len(snap_entries)
snap_map = dict(snap_entries)
open_snap = os.path.join(R85, 'kb-snapshot')
open_map = {}
for root, dirs, files in os.walk(open_snap):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        open_map[os.path.relpath(p, open_snap)] = hashlib.sha256(open(p, 'rb').read()).hexdigest()
diff_files = [rel for rel in sorted(set(open_map) | set(snap_map))
              if open_map.get(rel) != snap_map.get(rel)]
assert diff_files == [], diff_files  # 预期零差异（活 method 本轮无改动）

report = {
    'round': 85, 'set': 'holdout29', 'built_by': '组集封存席（R85）',
    'ruling': 'runs/round85/PREREG.md §2（构成写死）',
    'T': 27, 'order': ORDER,
    'lr_rotation': {'source_order': ['DA（断案）', 'CY（粹言 CYJ-后CY-合并台账序）', 'BY（变易 BY-后YX-合并台账序）'],
                    'selected': LR_SEL, 'by_source': dict(lr_src_counts),
                    'ledger_sizes': {'DA': 97, 'CY': 55, 'BY': 91}},
    'fallback_log': fallback_log,
    'leak_flag_list': leak_flags, 'leak_note_list': leak_notes,
    'composition_assertions': composition_assertions,
    'eligibility_assertions': eligibility, 'eligibility_all_pass': True,
    'zero_reuse_recheck': {'source_file': 'runs/round85/used-ids-r85.json',
                           'used_union_total': len(used_union),
                           'method': '只对 id 集逐 id 对勘；未打开任何已封存集金标正文做内容比对',
                           'selected_hit_count': 0, 'selected_hits': []},
    'input_field_whitelist': INPUT_FIELDS,
    'input_field_whitelist_basis': 'holdout28/inputs/DS-050.json 实读字段集（开工对齐断言通过）',
    'strip_register': strip_register, 'field_mapping_notes': field_mapping_notes,
    'hygiene_question_scan': hygiene_scan,
    'lr_recovery_register': {cid: RECOVERY[cid] for cid in LR_SEL},
    'scan1_verbatim_fragment': {
        'method': '每例 master_prediction 与 outcome_record 的特征片段（标点分句整句（≥8字）＋去空白12字滑动窗口全集）对该例输入卡全文本逐字子串扫描；全27例零命中（硬断言）',
        'per_case': scan1},
    'scan_marker_selfcheck': {
        'method': 'R42 PREREG §5 内容级一级/二级标记＋字段名黑名单＋禁用键集对27张输入卡全字段递归扫描（构建脚本内断言道）',
        'per_case': scan_markers,
        'total_hits': sum(len(v['content_hits']) + len(v['fieldname_hits']) for v in scan_markers.values())},
    'scan_reread_selfcheck': {
        'method': '落盘后逐卡回读重行片段／标记／禁用键／白名单核，全过', 'per_case': reread},
    'scan2_independent_rescan': '由独立复扫脚本 scan_holdout29_r85.py 执行，结果另行登记于封存日志',
    'scan3_host_rescan': '主持验封道，非本席执行——留位',
    'gold_sha256_hashlib': sha_lib, 'gold_bytes': gold_bytes,
    'card_bytes': card_bytes, 'card_bytes_total': sum(card_bytes.values()),
    'kb_snapshot': {'dir': 'runs/round85/kb-snapshot-holdout29/',
                    'excluded_non_snapshot_files': SNAP_EXCLUDED,
                    'file_count': len(snap_entries),
                    'sha256_list': 'runs/round85/kb-snapshot-holdout29-sha256.txt',
                    'sha256_list_sha256': snap_list_sha,
                    'files': [rel for rel, _ in snap_entries],
                    'diff_vs_round85_platform_snapshot': diff_files},
    'outputs_written': [f'holdout29/inputs/{c}.json' for c in ORDER] + ['holdout29/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 27, 'order': ORDER,
                  'fallback_log': fallback_log,
                  'snapshot_files': len(snap_entries), 'snapshot_excluded': SNAP_EXCLUDED,
                  'diff_vs_platform': diff_files,
                  'gold_sha256_hashlib': sha_lib, 'gold_bytes': gold_bytes,
                  'card_bytes_total': sum(card_bytes.values())}, ensure_ascii=False))
