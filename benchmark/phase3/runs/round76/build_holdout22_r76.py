#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R76 组集封存席：按 PREREG-ADDENDUM-r76.md §三写定组建并封存 holdout22（T＝27）。

选集（§三选取规则 1-6 照序执行）：
- DS-001..009 ← runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json
  （eligible∧present∧low 按 DIGEST 登记序前 9；DS-047 medium 不在前 9；
   同造合并组 DS-011/DS-033 不在前 9，至多取 1 之限未触发）
- 开悟 QM-011..014 ← SUPPLY-MINING-kaiwu-r76.json（stem_check 天地盘全合者登记序前 4）
- 启悟 QM-201..203 ← SUPPLY-MINING-qiwu-r76.json（登记序前 3）
- 石建国 QM-301..303 ← SUPPLY-MINING-shijianguo-r76.json（登记序前 3；QM-308 未入选）
- ZCB-001..004 ← SUPPLY-MINING-zichubu-r76.json（eligible∧present∧low 登记序前 4）
- 六爻 GSZ-022/023/024/026 ← runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json
  可选未用池（承 R59 定案 GSZ 净入账 63 − holdout21 用 6 ＝ 57）登记序逐例回原书
  （文字版 PDF 文字层）复核锚点五要素：GSZ-020 无动爻（原书自注「内因无动爻」）
  缺一换下；GSZ-022/023/024/026 五要素全在场入选。
跨书同案再核（规则 5）：QM 入选 10 例与 R56 QM 池 QM-001..010 以
占事＋占时＋占者三键逐例对勘（脚本内登记键表，人工复核结论入报告/日志）。

金标断语逐字核验：台账 master_assertion 非逐字者回原书逐字补录（4 例）：
- QM-012/QM-013：台账为分析文摘写（QM-013 括注且误植 A 例分析），补录自
  《开悟之门》印刷 210-212 页分析（1）-（4）全文（本席读 110dpi 渲染页图逐字）。
- QM-203：台账第一局断语以「……」省略中段一句，补录自《奇门启悟》印刷 202 页全文。
- ZCB-004：台账为问答摘写摘要，补录自《字触补》卷二叶 8-9 原文断语诸段
  （合集 PDF 页图 hi-557 逐字，诸段以；分隔，分隔符为本席登记）。
其余 23 例断语经核为台账逐字（开悟 QM-011 与原书印刷 207 页「断：」段逐段合、
QM-014 与印刷 215 页引文逐字合，本席读页图核；GSZ 为文字层 verbatim；
DS/QW/SG/ZCB-001..003 为台账视觉转录逐字断语、无摘写标记）。

输入卡 schema {id, tradition, subject, context, question, setting, provenance,
redistributable, license_status, anchors}（承 holdout21 体例）；金标 schema 承
holdout21。断语扫描：①逐字片段扫描（非测字例零命中断言；测字例命中只许落在
台账 input_side 字形拆分过程锚点原文内含语、逐 fragment 分类登记，结局片段
全例零命中断言）；②h20 内容级标记扫描（R42 PREREG §5）逐卡零命中断言
（ZCB-004 附条件改写删定期断语段后复扫）；③建后逐卡回读自检（落盘复扫）。
只建卡与封存：不作断、不评分、不开封、不做 git 操作。
零复用只对 id 集（禁打开已封存集金标正文做内容比对；各 gold 仅取 id 字段）。
"""
import json, hashlib, os, re, shutil, subprocess
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'
R76 = os.path.join(BASE, 'runs/round76')
DIG76 = os.path.join(R76, 'digestion')
OUT_DIR = os.path.join(BASE, 'holdout22')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R76, 'build-holdout22-report-r76.json')

LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '斷曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']
BANNED_IN_CARD = {'grade_note', 'grade_suggestion', 'grade_reason', 'contamination',
                  'contamination_suggestion', 'contamination_reason',
                  'contamination_rationale', 'outcome', 'outcome_record',
                  'outcome_grade', 'master_predictions', 'master_prediction',
                  'master_assertion', 'passage_full', 'record_status', 'notes',
                  'master', 'seal_eligible', 'holdout_eligible', 'review',
                  'pollution', 'pollution_note', 'anchor_presence', 'anchor_missing',
                  'anchor_check', 'anchor_note', 'dedup_check', 'filters',
                  'outcome_type', 'outcome_note', 'transcription',
                  'provisional_id', 'source', 'language', 'grade'}


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

# ---------- 台账载入 ----------
ds_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-duanshi-r76.json'))
kw_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-kaiwu-r76.json'))
qw_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-qiwu-r76.json'))
sg_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-shijianguo-r76.json'))
zc_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-zichubu-r76.json'))
gsz_mining = load_json(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
qm56_mining = load_json(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-qimen-r56.json'))

# ---------- 门：例级零复用并集先行（只对 id 集；承 R59 定案 1052 口径） ----------
used_sources = {}
h2_ids = set(load_json(os.path.join(ROOT, 'benchmark/phase2/splits2.json'))['holdout2'])
used_sources['phase2_splits2_holdout2'] = len(h2_ids)
gold_ids_3_20 = set()
for i in range(3, 21):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip():
                gold_ids_3_20.add(json.loads(line)['id'])
used_sources['holdout3_20_gold_ids'] = len(gold_ids_3_20)
gold21_ids = set()
for line in open(os.path.join(BASE, 'holdout21/test_gold.jsonl'), encoding='utf-8'):
    if line.strip():
        gold21_ids.add(json.loads(line)['id'])
used_sources['holdout21_gold_ids'] = len(gold21_ids)
assert len(gold21_ids) == 25
input_ids = set()
for i in range(2, 22):
    for dname in (f'holdout{i}/inputs', f'holdout{i}-inputs'):
        d = os.path.join(BASE, dname)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'):
                    input_ids.add(fn[:-5])
used_sources['holdout2_21_input_card_ids'] = len(input_ids)
dev_ids = set(load_json(os.path.join(BASE, 'data/master-baseline-dev9.json')).keys())
dev9_count = len(dev_ids)
for dv in ('inputs-dev9', 'inputs-dev10', 'inputs-dev11', 'inputs-dev12', 'inputs'):
    d = os.path.join(BASE, dv)
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                dev_ids.add(fn[:-5])
used_sources['dev_pool_ids_dev9keys_plus_dev_input_dirs'] = len(dev_ids)
used_union = h2_ids | gold_ids_3_20 | gold21_ids | input_ids | dev_ids
r59_accounting = {'dev9_keys': dev9_count,
                  'holdout2_20_additive': 540,
                  'holdout21': 25,
                  'total_stated': 1052,
                  'note': '承 ADDENDUM-r59 §四定案加法口径（dev 487＋holdout2–20 540'
                          '＋holdout21 25＝1052，跨源未去重）；本席盘上 id 集实算并集'
                          '见 used_union_actual，去重口径不同、数值不强求相等，'
                          '零复用以逐 id 对实算并集零命中为准'}


selection_register = {}

# ---------- 规则 1：DS 9 ----------
ds_cands = [r for r in ds_mining['records']
            if r['eligible_net'] is True and r['anchor_status'] == 'present'
            and r['contamination_pre'] == 'low']
assert 'DS-047' not in [r['case_id'] for r in ds_cands]  # medium 已滤
# 零复用剔除（盘上实证，主持 §一「构造性零复用」对 DS 号段证伪）：
# holdout10 金标已有 DS-001/DS-002/DS-003（任铁樵《滴天髓阐微》例，与本批段氏例
# 同名异例）。§三构成限度「与已用 1052 id 零复用」为硬限，故该 3 id 逐 id 剔除、
# 按登记序递补 DS-010/DS-011/DS-012，DS 仍取 9 例。剔除/递补事实在此登记，
# 并入封存日志与回传（偏离规则 1 字面「前 9」，以零复用限度为准）。
ds_skipped_used = [r['case_id'] for r in ds_cands if r['case_id'] in used_union]
ds_unused = [r for r in ds_cands if r['case_id'] not in used_union]
DS_IDS = [r['case_id'] for r in ds_unused[:9]]
assert ds_skipped_used == ['DS-001', 'DS-002', 'DS-003'], ds_skipped_used
assert DS_IDS == ['DS-004', 'DS-005', 'DS-006', 'DS-007', 'DS-008', 'DS-009',
                  'DS-010', 'DS-011', 'DS-012'], DS_IDS
merged_group = [c for c in DS_IDS if c in ('DS-011', 'DS-033')]
assert len(merged_group) <= 1 and merged_group == ['DS-011']
selection_register['DS'] = {
    'rule': 'eligible∧present∧low∧未用（id 零复用）按 DIGEST 登记序前 9，排除 DS-047',
    'candidate_count': len(ds_cands), 'selected': DS_IDS,
    'skipped_used_ids': ds_skipped_used,
    'skipped_reason': 'DS-001/DS-002/DS-003 已见于 holdout10/test_gold.jsonl'
                      '（任铁樵《滴天髓阐微》例，同名异例）；PREREG-ADDENDUM-r76 §一'
                      '「新 id 命名空间与已用并集 1052 按 id 零复用为构造性成立」'
                      '对 DS 号段经盘上实测证伪，本席以 §三构成限度（零复用）为准'
                      '剔除并按登记序递补 DS-010/DS-011/DS-012',
    'merged_group_DS011_DS033_in_selected': merged_group,
    'merged_group_note': '同造合并组 DS-011/DS-033 只取 DS-011（递补入选），DS-033 未取，至多 1 之限守合'}

# ---------- 规则 2：开悟 QM 4（仅 stem_check 天地盘全合） ----------
kw_full = [c for c in kw_mining['cases']
           if c['stem_check']['tianpan_ok'] and c['stem_check']['dipan_ok']]
kw_notfull = [c['case_id'] for c in kw_mining['cases']
              if not (c['stem_check']['tianpan_ok'] and c['stem_check']['dipan_ok'])]
KW_IDS = [c['case_id'] for c in kw_full[:4]]
assert KW_IDS == ['QM-011', 'QM-012', 'QM-013', 'QM-014'], KW_IDS
selection_register['KW'] = {
    'rule': '仅 stem_check 天地盘全合者按登记序前 4；未全合一律不取',
    'full_count_recheck': len(kw_full), 'not_full_ids': kw_notfull,
    'note': '盘上 JSON 复算全合 38 例（PREREG-ADDENDUM-r76 §一作 42，差 4；'
            '不合 14 例逐 id 如上。前 4 例不受此差影响，选集不变，如实登记待主持知悉）',
    'selected': KW_IDS}

# ---------- 规则 3：启悟 QM 3／石建国 QM 3 ----------
QW_IDS = [c['case_id'] for c in qw_mining['cases'][:3]]
SG_IDS = [c['case_id'] for c in sg_mining['cases'][:3]]
assert QW_IDS == ['QM-201', 'QM-202', 'QM-203'], QW_IDS
assert SG_IDS == ['QM-301', 'QM-302', 'QM-303'], SG_IDS
selection_register['QW_SG'] = {
    'rule': '按登记序各取前 3', 'selected_qiwu': QW_IDS, 'selected_shijianguo': SG_IDS,
    'qm308_note': 'QM-308（震宫八神一字未读出）不在石建国前 3，未入选，单列注记条件未触发'}

# ---------- 规则 4：ZCB 4 ----------
zc_cands = [c for c in zc_mining['cases']
            if c.get('eligible') is True and c['anchor_status'] == 'present'
            and c['contamination_pre'] == 'low']
ZCB_IDS = [c['case_id'] for c in zc_cands[:4]]
assert ZCB_IDS == ['ZCB-001', 'ZCB-002', 'ZCB-003', 'ZCB-004'], ZCB_IDS
selection_register['ZCB'] = {
    'rule': 'eligible∧present∧low 按登记序前 4；mid（ZCB-016..019）不取',
    'candidate_count': len(zc_cands), 'selected': ZCB_IDS}

# ---------- 规则 6：六爻 4（可选未用池逐例回原书复核五要素） ----------
gsz_net = gsz_mining['counts']['net_eligible_A_low_present']
assert len(gsz_net) == 63
gsz_used_h21 = ['GSZ-003', 'GSZ-005', 'GSZ-009', 'GSZ-015', 'GSZ-016', 'GSZ-017']
gsz_pool = [c for c in gsz_net if c not in gsz_used_h21]
assert len(gsz_pool) == 57, len(gsz_pool)
gsz_by = {e['provisional_id']: e for e in gsz_mining['entries']}
# 原书文字层（pdftotext 提取件，与台账 transcription=verbatim 同源原书）
book_txt = open(os.path.join(R76, 'gsz-book-r76.txt'), encoding='utf-8').read()

LIUQIN = ['兄弟', '子孙', '妻财', '官鬼', '父母']
GANZHI = list('甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥')


def five_elements(cid):
    """逐例五要素在场判定：台账 chart 结构化核 + 原书文字层对勘。"""
    e = gsz_by[cid]
    chart = e['input_fields']['chart']
    lines = chart['chart_lines_top_to_bottom']
    joined = '\n'.join(lines)
    el = {}
    el['gua_name'] = bool(chart.get('ben_gua'))
    el['moving'] = ('动' in joined) or bool(chart.get('bian_gua'))
    el['shi_ying'] = ('世' in joined) and ('应' in joined)
    el['liuqin_nazhi'] = all(
        any(lq in ln and any(g in ln for g in GANZHI) for ln in lines)
        for lq in [x for x in LIUQIN if any(x in ln for ln in lines)]) and \
        sum(1 for ln in lines if any(lq in ln for lq in LIUQIN)) >= 6
    asked = e['input_fields']['asked_at']
    el['yuejian_ri chen'.replace(' ', '')] = bool(
        re.search(r'月', asked) and re.search(r'日', asked))
    # 原书对勘：本卦名与 asked_at 年月日干支须见于原书文字层
    el['in_book_ben_gua'] = chart['ben_gua'][:2] in book_txt or chart['ben_gua'] in book_txt
    el['in_book_asked'] = asked.split('（')[0][:7] in book_txt.replace(' ', '')
    return el


liuyao_check = {}
GSZ_IDS = []
for cid in gsz_pool:
    el = five_elements(cid)
    ok = all(el[k] for k in ('gua_name', 'moving', 'shi_ying', 'liuqin_nazhi',
                             'yuejian_richen', 'in_book_ben_gua', 'in_book_asked'))
    liuyao_check[cid] = {'elements': el, 'pass': bool(ok)}
    if ok:
        GSZ_IDS.append(cid)
    if len(GSZ_IDS) == 4:
        break
assert GSZ_IDS == ['GSZ-022', 'GSZ-023', 'GSZ-024', 'GSZ-026'], GSZ_IDS
assert liuyao_check['GSZ-020']['pass'] is False
assert liuyao_check['GSZ-020']['elements']['moving'] is False
selection_register['GSZ'] = {
    'rule': '可选未用池（GSZ 净入账 63 − holdout21 用 6 ＝ 57）登记序逐例回原书'
            '（《六爻卦例说真》文字版 PDF，pdftotext 文字层提取件 '
            'runs/round76/gsz-book-r76.txt）复核锚点五要素，全在场者取前 4',
    'checked_in_order': list(liuyao_check.keys()),
    'rejected': {'GSZ-020': '动爻缺如：原书第四章例五离卦六爻无动爻、变卦空，'
                            '原书自注「为什么没断死，就因为内因无动爻来克世」；'
                            '缺一换下一例（规则 6）'},
    'selected': GSZ_IDS, 'fallback_triggered': False}

QM_IDS = KW_IDS + QW_IDS + SG_IDS
ORDER = DS_IDS + QM_IDS + ZCB_IDS + GSZ_IDS
assert len(ORDER) == 27 and len(set(ORDER)) == 27, ORDER
reuse_hits = [cid for cid in ORDER if cid in used_union]
assert not reuse_hits, f'选例与已用并集相交（零复用门）：{reuse_hits}'

# ---------- 规则 5：跨书同案再核（QM 10 例 vs R56 QM-001..010 三键对勘） ----------
# 三键＝占事＋占时＋占者；R56 池键表自台账逐字，本轮 10 例键表自各台账逐字，
# 逐对人工复核结论登记于此（占者集合先行比对：R56 占者为杜新会/张志春/王建国；
# 本轮占者为吕常文/刘文元/石建国，占者一键即全数不合，无同案可能；
# 仍逐例登记占时与占事以备复核）。
r56_keys = {}
for c in qm56_mining['cases']:
    inf = c['input_fields']
    r56_keys[c['provisional_id']] = {'caster': inf['caster'],
                                     'time': inf['cast_time_verbatim'],
                                     'event': inf['question']}
new_keys = {}
kw_by = {c['case_id']: c for c in kw_mining['cases']}
qw_by = {c['case_id']: c for c in qw_mining['cases']}
sg_by = {c['case_id']: c for c in sg_mining['cases']}
for cid in KW_IDS:
    c = kw_by[cid]
    new_keys[cid] = {'caster': c['caster'], 'time': c['input_side'].split('。')[0],
                     'event': c['topic']}
for cid in QW_IDS:
    c = qw_by[cid]
    new_keys[cid] = {'caster': c['input_side']['caster'],
                     'time': c['input_side']['cast_time_verbatim'],
                     'event': c['input_side']['question']}
for cid in SG_IDS:
    c = sg_by[cid]
    new_keys[cid] = {'caster': c['input_side']['caster'],
                     'time': c['input_side']['cast_time'],
                     'event': c['input_side']['question']}
r56_casters = {v['caster'] for v in r56_keys.values()}
new_casters = {v['caster'] for v in new_keys.values()}
triple_check = {
    'r56_pool_keys': r56_keys, 'new_keys': new_keys,
    'r56_casters': sorted(r56_casters), 'new_casters': sorted(new_casters),
    'caster_overlap': sorted(r56_casters & new_casters),
    'result': '三键逐对对勘零同案命中：占者集合不交（R56＝杜新会/张志春/王建国；'
              '本轮＝吕常文/刘文元/石建国），占时与占事亦逐例互异；无剔除、无递补。'
              '另：开悟台账 dedup_note 载本书疾病例二 B 与 QM-006 同案已出局不入池，'
              '该例不在本轮入选 4 例内（入选为例一/例三 A/例三 B/例四）',
    'hits': [], 'removed': [], 'replacements': []}
assert not triple_check['hits']

# ---------- 金标断语补录（非逐字 4 例，回原书逐字） ----------
RESTORED_QM203 = ('你剛才說從懷孕到現在六個多月，那麽到下個月也就是七個多月，'
                  '按理說是沒到生孩子的時候，但我的奇門盤中反映出來的資訊就是'
                  '下個月你要生小孩的，而且還要剖腹產。')
SUPPLEMENT = {
    'QM-012': {
        'master_prediction': (
            '（1）天芮星为病神，落离宫。癸+辛，为网盖天牢，测病死症难逃，大凶。'
            '乙+辛龙逃走，凶。（2）日干甲午辛为病鸡，落巽宫，为死墓之地，又逢'
            '死门，大凶。辛+丙，测病不愈。（3）天心星和乙奇为医生和药物，分别'
            '落兑宫、离宫，均不克病神落宫，病无治。（4）综上所述分析，病无治，'
            '必死。因日干辛处死墓绝之地，又死于月令午火，根据死墓绝应期，金怕'
            '火克，必死于火日火时，今正逢甲午日，故判死于当日巳时或午时。'),
        'pages': '《开悟之门》印刷210-211页（PDF238-239）分析（1）-（4）全文',
        'reason': '台账 master_assertion 为分析文摘写：删「乙+辛龙逃走，凶」'
                  '「辛+丙，测病不愈」等句、改「综上所述分析」为「综上分析」等，非逐字'},
    'QM-013': {
        'master_prediction': (
            '（1）天芮星为病神，落坤宫。生门+死门，病难救。（2）天心星和乙奇为'
            '医生和药物，分别落乾宫和坤宫，均不克天芮星落宫，病无治。（3）日干'
            '己为病鸡，落巽宫为旺地，又得月令午火之生，旺极。物极必反，故必死。'
            '（4）综上所述，病无治，必死。因开门落巽宫为门迫，又反吟，故死速。'
            '日干己土旺极，必死于长生之地，火土同源，应死于寅日寅时，又时比日'
            '速，故判死于次日（庚子日）寅时，即1998年6月22日寅时，此为长生旺'
            '相应期。'),
        'pages': '《开悟之门》印刷211-212页（PDF239-240）分析（1）-（4）全文',
        'reason': '台账 master_assertion 为摘写，且括注误植 A 例（母鸡）分析（2）'
                  '内容充 B 例（公鸡）分析（4），非逐字'},
    'QM-203': {
        'master_prediction': (
            '第一局：「你懷的肯定是女孩子。你不能順產，必須剖腹產。這些都是小'
            '問題，現在關鍵的問題是你腹中這孩子下個月就要出生了，而且必須做'
            '剖腹產手術才能把孩子生下來。' + RESTORED_QM203 +
            '希望你從現在開始起，不要到處走動，最好在家休息，以保證胎兒在最'
            '後這段時間裏能平穩地渡過，直到出生。」第二局：「你在運動過程中'
            '被撞而摔倒，動了胎氣，已經見紅（血），胎兒不能等到預產期了，現'
            '在需要馬上做剖腹產手術，孩子可以保住，但前提是必須馬上做剖腹產'
            '手術，不然孩子肯定是保不住的。依我之見，馬上到醫院做剖腹產手術，'
            '孩子會平安地生下來，只是時間尚不到預產期，只能生下一個早產嬰兒'
            '了。」'),
        'pages': '《奇门启悟》印刷202页（PDF102-103 跨页）第一局断语全文；'
                 '第二局台账已逐字、与印刷203-204页合',
        'reason': '台账第一局断语以「……」省略中段一句（' + str(len(RESTORED_QM203)) +
                  '字），非全文逐字'},
    'ZCB-004': {
        'master_prediction': (
            '公遣戍矣，是千里萬里也；下為口字，上為外字偏傍，是口外矣；日在于'
            '西為夕，其西域乎；必賜環也；口為四字之外圍而中缺兩筆，其不足四'
            '年乎，今年為戊子，至四年為辛卯，夕字卯字偏傍亦相合也'),
        'pages': '《字触补》卷二·外部叶8-9（合集 PDF553 下半-557 上半，页图 hi-557）'
                 '墨字董字名字条后段',
        'reason': '台账 master_assertion 为问答摘写摘要（嵌问句、删拆语主干），非逐字；'
                  '补录为原文断语诸段逐字、以；分隔（分隔符为本席登记）'},
}
for cid, s in SUPPLEMENT.items():
    s['chars'] = len(s['master_prediction'])

cards, golds = {}, {}
eligibility, strip_register, field_mapping_notes = {}, {}, {}
rewrites = {}

LICENSE_MODERN = '现代版权文本（扫描本），内部研究用'
PROV_TAIL = '用户经学校图书馆提供；redistributable=false'

# ---------- DS 9 例（八字） ----------
ds_by = {r['case_id']: r for r in ds_mining['records']}
for cid in DS_IDS:
    r = ds_by[cid]
    ok = (r['eligible_net'] is True and r['anchor_status'] == 'present'
          and r['contamination_pre'] == 'low'
          and all(str(v).startswith('pass') for v in r['filters'].values())
          and r['master_assertion'].strip() and r['outcome'].strip())
    eligibility[cid] = {'eligible_net': r['eligible_net'],
                        'anchor_status': r['anchor_status'],
                        'contamination': r['contamination_pre'],
                        'filters': r['filters'], 'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-duanshi-r76.json 台账逐字'}
    assert ok, cid
    inf = r['input_side']
    cards[cid] = {
        'id': cid, 'tradition': 'bazi',
        'subject': inf['subject'],
        'context': f"《段氏理象学》命例（{r['composition_type']}）；四柱载于 anchors",
        'question': '就此四柱命造求测（原书命例体例，无独立问句原文载录）',
        'setting': r['source'],
        'provenance': f"{r['source']}；底本为用户经学校图书馆提供，redistributable=false",
        'redistributable': False,
        'license_status': '现代版权文本（扫描图 PDF），内部研究用',
        'anchors': {'pillars': inf['pillars'],
                    'pillars_verbatim': inf['pillars_verbatim'],
                    'gender': inf['gender']},
    }
    note = (f"入账口径：eligible_net=true、锚点 present、contamination low、四滤全 pass；"
            f"锚点：{r['anchor_note']}；污染：{r['contamination_note']}；"
            f"转录：visual（confidence={r['transcription']['confidence']}，"
            f"{r['transcription']['note']}）；断语为原书断语逐字摘录，"
            f"多段以／分隔（台账摘录分隔符）")
    if r.get('verdict_note'):
        note += f"；台账 verdict_note：{r['verdict_note']}"
    golds[cid] = {'id': cid, 'master_prediction': r['master_assertion'],
                  'outcome_record': r['outcome'], 'tradition': 'bazi',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': cards[cid]['provenance'],
                  'license_status': cards[cid]['license_status'],
                  'redistributable': False}
    strip_register[cid] = ['anchor_status/anchor_note/contamination_pre/'
                           'contamination_note/separable/transcription/dedup/filters/'
                           'eligible_net/verdict_note/composition_type/'
                           'master_assertion/outcome（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject←input_side.subject 逐字；anchors←input_side '
                                'pillars/pillars_verbatim/gender 逐字；setting←source 逐字；'
                                'context/question 为组写（台账无该二字段，组写口径在此登记）')

# ---------- 开悟 QM 4 例（奇门；input_side 为单串：背景＋干支局式＋盘面） ----------
KW_SUBJECT = {
    'QM-011': '工厂工人刘照桂（患鼻癌住院）；占者：吕常文（江西省泰和县学员）',
    'QM-012': '自家所养一只母鸡（白痢病）；占者：吕常文',
    'QM-013': '所养一只公鸡（白痢病态）；占者：吕常文',
    'QM-014': '学员王连明（住院）；占者：刘文元',
}
KW_QUESTION = {  # 均为 input_side 原文子串，脚本断言
    'QM-011': '求测其病吉凶',
    'QM-012': '用奇门测这只鸡的病能否治好',
    'QM-013': '测其病能否治好',
    'QM-014': '求测明天的手术能否顺利、还能否继续活下去',
}
for cid in KW_IDS:
    c = kw_by[cid]
    ok = (c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
          and c['separable'] is True and c['stem_check']['tianpan_ok']
          and c['stem_check']['dipan_ok']
          and c['master_assertion'].strip() and c['outcome'].strip())
    eligibility[cid] = {'anchor_status': c['anchor_status'],
                        'contamination': c['contamination_pre'],
                        'separable': c['separable'], 'stem_check': c['stem_check'],
                        'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-kaiwu-r76.json 台账逐字'}
    assert ok, cid
    text = c['input_side']
    assert KW_QUESTION[cid] in text, cid
    head, sep, board = text.partition('盘面（')
    assert sep, cid
    cards[cid] = {
        'id': cid, 'tradition': 'qimen',
        'subject': KW_SUBJECT[cid],
        'context': head.rstrip('。') + '。',
        'question': KW_QUESTION[cid],
        'setting': f"{c['source']}；占者：{c['caster']}",
        'provenance': f"{c['source']}（张志春著）；{PROV_TAIL}",
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': {'board_verbatim': '盘面（' + board,
                    'stems_tianpan': c['stems_tianpan'],
                    'stems_dipan': c['stems_dipan'],
                    'stem_check': c['stem_check']},
    }
    mp = SUPPLEMENT[cid]['master_prediction'] if cid in SUPPLEMENT else c['master_assertion']
    note = (f"锚点 present（盘面逐字＋天地盘干集验算 stem_check 全合）；"
            f"污染 low；转录：visual（110dpi 渲染页视觉转录、存疑盘面 200dpi 复读）；"
            f"去重：{c['dedup']}")
    gold = {'id': cid, 'master_prediction': mp,
            'outcome_record': c['outcome'], 'tradition': 'qimen',
            'pollution': 'low', 'grade': 'A', 'grade_note': note,
            'provenance': cards[cid]['provenance'],
            'license_status': LICENSE_MODERN, 'redistributable': False}
    if cid in SUPPLEMENT:
        s = SUPPLEMENT[cid]
        gold['editor_note'] = (f"断语补录：台账 master_assertion 非逐字（{s['reason']}），"
                               f"金标断语由本席回原书逐字补录，出处：{s['pages']}；"
                               f"补录断语全文 {s['chars']} 字。台账 outcome 与原书对勘一致，照台账。")
    else:
        gold['editor_note'] = ('断语逐字核验：本席读原书页图核——'
                               + ('QM-011 与印刷207页「断：」（1）-（4）逐段合；'
                                  if cid == 'QM-011' else
                                  'QM-014 与印刷215页断语引文逐字合；')
                               + '台账转录逐字、无摘写标记，照台账。')
    golds[cid] = gold
    strip_register[cid] = ['topic/anchor_status/contamination_pre/separable/'
                           'transcription/dedup/master_assertion/outcome'
                           '（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('context←input_side 盘面之前段逐字；anchors.board_verbatim'
                                '←input_side 盘面段逐字；question←input_side 原文子串（断言验）；'
                                'subject 为组写（据 input_side 与 caster 组写，口径在此登记）；'
                                'setting←source＋caster 组写')

# ---------- 启悟 QM 3 例（奇门） ----------
for cid in QW_IDS:
    c = qw_by[cid]
    src, inf = c['source'], c['input_side']
    ok = (c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
          and c['separable'] is True
          and c['master_assertion'].strip() and c['outcome'].strip())
    eligibility[cid] = {'anchor_status': c['anchor_status'],
                        'contamination': c['contamination_pre'],
                        'separable': c['separable'], 'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-qiwu-r76.json 台账逐字'}
    assert ok, cid
    anchors = {'cast_time_verbatim': inf['cast_time_verbatim']}
    if 'boards' in inf:
        anchors['boards'] = inf['boards']
    else:
        anchors['board'] = inf['board']
    # 篇名「分類占斷篇」含内容级一级标记字样（占斷），属书目信息而非断语内容；
    # 卡面引节名时略去篇名（承 h20 第一道命中处置口径），金标 provenance 仍载全节名。
    section_card = src['section'].replace('分類占斷篇', '')
    setting = (f"{src['book']}（{src['author']}著）·{section_card}；"
               f"起局时间：{inf['cast_time_verbatim']}")
    provenance = (f"{src['book']}（{src['author']}著，{src['publisher']}）·{section_card}，"
                  f"印刷页{src['printed_pages']}（PDF页{src['pdf_pages']}）；{PROV_TAIL}")
    cards[cid] = {
        'id': cid, 'tradition': 'qimen',
        'subject': inf['querent'],
        'context': inf['context'],
        'question': inf['question'],
        'setting': setting,
        'provenance': provenance,
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': anchors,
    }
    mp = SUPPLEMENT[cid]['master_prediction'] if cid in SUPPLEMENT else c['master_assertion']
    note = (f"锚点 present；污染 low（{c['contamination_reason']}）；"
            f"转录：visual（{c['transcription_confidence']}）；去重：{c['dedup']}")
    if c.get('notes'):
        note += f"；台账注记：{c['notes']}"
    gold = {'id': cid, 'master_prediction': mp,
            'outcome_record': c['outcome'], 'tradition': 'qimen',
            'pollution': 'low', 'grade': 'A', 'grade_note': note,
            'provenance': (f"{src['book']}（{src['author']}著，{src['publisher']}）·"
                           f"{src['section']}，印刷页{src['printed_pages']}"
                           f"（PDF页{src['pdf_pages']}）；{PROV_TAIL}"),
            'license_status': LICENSE_MODERN, 'redistributable': False}
    if cid in SUPPLEMENT:
        s = SUPPLEMENT[cid]
        gold['editor_note'] = (f"断语补录：台账 master_assertion 非逐字（{s['reason']}），"
                               f"金标断语由本席回原书逐字补录，出处：{s['pages']}；"
                               f"补录断语全文 {s['chars']} 字（其中第一局补回省略句 "
                               f"{len(RESTORED_QM203)} 字）。台账 outcome 与原书对勘一致，照台账。")
    golds[cid] = gold
    strip_register[cid] = ['anchor_status/contamination_pre/contamination_reason/'
                           'separable/transcription/transcription_confidence/dedup/notes/'
                           'master_assertion/outcome（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject←input_side.querent；question/context←input_side 逐字；'
                                'setting←source＋cast_time_verbatim 组写（节名略去篇名'
                                '「分類占斷篇」：含内容级标记字样、属书目信息，处置登记于此；'
                                '金标 provenance 载全节名）；anchors←'
                                'cast_time_verbatim＋board/boards 全载逐字')

# ---------- 石建国 QM 3 例（奇门） ----------
for cid in SG_IDS:
    c = sg_by[cid]
    src, inf = c['source'], c['input_side']
    ok = (c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
          and c['separable'] is True
          and c['master_assertion'].strip() and c['outcome'].strip())
    eligibility[cid] = {'anchor_status': c['anchor_status'],
                        'contamination': c['contamination_pre'],
                        'separable': c['separable'], 'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-shijianguo-r76.json 台账逐字'}
    assert ok, cid
    setting = (f"{src['book']}（{src['author']}著）·{src['section']}；"
               f"起局时间：{inf['cast_time']}（{inf['ganzhi']}）")
    provenance = (f"{src['book']}（{src['author']}著，{src['publisher']}，"
                  f"ISBN {src['isbn']}）·{src['section']}，印刷页{src['printed_pages']}"
                  f"（DjVu页{src['djvu_pages']}）；{PROV_TAIL}")
    cards[cid] = {
        'id': cid, 'tradition': 'qimen',
        'subject': inf['querent'],
        'context': inf['context'],
        'question': inf['question'],
        'setting': setting,
        'provenance': provenance,
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': {'cast_time': inf['cast_time'], 'ganzhi': inf['ganzhi'],
                    'chart_header': inf['chart_header'], 'chart': inf['chart']},
    }
    note = (f"锚点 present；污染 low；转录：visual（{c['transcription_confidence']}）；"
            f"去重：{c['dedup']}")
    if c.get('notes'):
        note += f"；台账注记：{c['notes']}"
    golds[cid] = {'id': cid, 'master_prediction': c['master_assertion'],
                  'outcome_record': c['outcome'], 'tradition': 'qimen',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': provenance,
                  'license_status': LICENSE_MODERN, 'redistributable': False}
    strip_register[cid] = ['anchor_status/contamination_pre/separable/transcription/'
                           'transcription_confidence/dedup/notes/master_assertion/outcome'
                           '（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject←input_side.querent；question/context←input_side 逐字；'
                                'setting←source＋cast_time/ganzhi 组写；anchors←cast_time/'
                                'ganzhi/chart_header/chart 全载逐字')

# ---------- ZCB 4 例（测字） ----------
zc_by = {c['case_id']: c for c in zc_mining['cases']}
ZCB_SUBJECT = {
    'ZCB-001': '释昙迁（俗姓王氏）与失物之妪',
    'ZCB-002': '杨向春与巡按欧阳',
    'ZCB-003': '富阳能占者与书王字问者',
    'ZCB-004': '徐燕辽与董姓军官',
}
ZCB_QUESTION = {
    'ZCB-001': '妪失物就卦，问所失何物、能否寻得',
    'ZCB-002': '书一梅字占之，不言所占何事',
    'ZCB-003': '书王字问督学之事',
    'ZCB-004': '书董字使拆，又书名字使拆；问将来得归否、在何年',
}
ZCB_CHAR = {'ZCB-001': '兑', 'ZCB-002': '梅', 'ZCB-003': '王', 'ZCB-004': '董／名字'}
for cid in ZCB_IDS:
    c = zc_by[cid]
    ok = (c.get('eligible') is True and c['anchor_status'] == 'present'
          and c['contamination_pre'] == 'low' and c['separable'] is True
          and c['master_assertion'].strip() and c['outcome'].strip())
    eligibility[cid] = {'eligible': c.get('eligible'),
                        'anchor_status': c['anchor_status'],
                        'contamination': c['contamination_pre'],
                        'separable': c['separable'], 'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-zichubu-r76.json 台账逐字'}
    assert ok, cid
    src = c['source']
    input_text = c['input_side']
    if cid == 'ZCB-004':
        # 附条件改写（承 holdout20/21 先例）：台账 input_side 末段「定期则…」整段为
        # 应期断语（至四年为辛卯），非字形拆分本身，输入侧删此段；对照存证于
        # rewrites，台账不动。删后复扫（标记＋片段）于落盘前断言。
        seg = ('；定期則「口為四字[?]……其不足四年乎，今年為戊子，至四年為辛卯，'
               '夕字卯字偏傍亦相合也」')
        assert seg in input_text, input_text
        new_text = input_text.replace(seg, '')
        rewrites[cid] = {'before_input_side': input_text,
                         'after_input_side': new_text,
                         'removed_segment': seg,
                         'rule': '定期段为应期断语（断语内容）、非字形拆分锚点本身，'
                                 '输入侧剥离；对照存证，台账不动'}
        input_text = new_text
    setting = (f"《字触补》{src['juan']}·{src['leaf']}（《四库未收书辑刊》陆辑第拾捌册，"
               f"PDF页{src['pdf_pages']}）")
    provenance = f"{setting}；{PROV_TAIL}"
    cards[cid] = {
        'id': cid, 'tradition': 'cezi',
        'subject': ZCB_SUBJECT[cid],
        'context': input_text,
        'question': ZCB_QUESTION[cid],
        'setting': setting,
        'provenance': provenance,
        'redistributable': False,
        'license_status': '古籍文本（合集扫描本），内部研究用',
        'anchors': {'character': ZCB_CHAR[cid],
                    'split_process_verbatim': input_text},
    }
    mp = SUPPLEMENT[cid]['master_prediction'] if cid in SUPPLEMENT else c['master_assertion']
    note = (f"锚点 present（{c['anchor_basis']}）；污染 low（{c['contamination_basis']}）；"
            f"转录：visual（confidence={c['transcription']['confidence']}"
            + (f"，{c['transcription']['note']}" if c['transcription'].get('note') else '')
            + f"）；CZ-QX 计数例：{c['cz_qx_note']}")
    gold = {'id': cid, 'master_prediction': mp,
            'outcome_record': c['outcome'], 'tradition': 'cezi',
            'pollution': 'low', 'grade': 'A', 'grade_note': note,
            'provenance': provenance,
            'license_status': '古籍文本（合集扫描本），内部研究用',
            'redistributable': False}
    if cid in SUPPLEMENT:
        s = SUPPLEMENT[cid]
        gold['editor_note'] = (f"断语补录：台账 master_assertion 非逐字（{s['reason']}），"
                               f"金标断语由本席回原书逐字补录，出处：{s['pages']}；"
                               f"补录断语全文 {s['chars']} 字。台账 outcome 与原书对勘"
                               f"（至是果验、辛卯应期）一致，照台账。")
    golds[cid] = gold
    strip_register[cid] = ['title（原书条题含断语指向者一律不入卡，题面定位中性化，'
                           '见 field_mapping_notes）/anchor_status/anchor_basis/'
                           'contamination_pre/contamination_basis/separable/eligible/'
                           'cz_qx_counted/cz_qx_note/dedup/transcription/'
                           'master_assertion/outcome（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('context/anchors.split_process_verbatim←input_side 逐字'
                                '（字形拆分过程为 §三明列之输入侧锚点原文；ZCB-004 经'
                                '附条件改写删定期断语段）；subject/question 为组写'
                                '（口径在此登记；ZCB-002 question 为 input_side 原文）；'
                                'setting/provenance 只载卷叶与 PDF 页定位，不载原书条题'
                                '（条题如「督学丁艰」「失金钗」含断语/结局指向，承 '
                                'holdout21 QM-004 裁处中性化剔除）')

# ---------- GSZ 4 例（六爻，承 holdout21 build_liuyao 体例） ----------
for cid in GSZ_IDS:
    e = gsz_by[cid]
    ok = (e['grade'] == 'A' and e['pollution'] == 'low'
          and e['anchor_presence'] == 'present' and e['eligible_net'] is True
          and e['master_prediction'].strip() and e['outcome_record'].strip()
          and liuyao_check[cid]['pass'])
    eligibility[cid] = {'grade': e['grade'], 'pollution': e['pollution'],
                        'anchor_presence': e['anchor_presence'],
                        'eligible_net': e['eligible_net'],
                        'five_elements_recheck': liuyao_check[cid]['elements'],
                        'unused_in_pool': cid in gsz_pool,
                        'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-guaishuo-r57.json 台账逐字＋原书文字层五要素复核'}
    assert ok, cid
    inf = e['input_fields']
    anchors = {'asked_at': inf['asked_at']}
    anchors.update(inf['chart'])
    cards[cid] = {
        'id': cid, 'tradition': 'liuyao',
        'subject': e['subject'] if e['subject'] else '求测者（台账 subject 为空、原书未具名）',
        'context': f"占时：{inf['asked_at']}；《六爻卦例说真》卦例",
        'question': inf['question'],
        'setting': f"{e['source']}",
        'provenance': f"{e['source']}；底本为用户经学校图书馆提供，redistributable=false",
        'redistributable': False,
        'license_status': '现代版权文本（文字版PDF），内部研究用',
        'anchors': anchors,
    }
    note = ''
    if e.get('grade_note'):
        note += e['grade_note'] + '；'
    note += f"污染判级：{e['pollution_note']}；"
    note += f"转录：{e['transcription']}（transcription_confidence={e['transcription_confidence']}）；"
    note += '锚点五要素经本席回原书文字层复核全在场（卦名/动爻/世应/六亲纳支/月建日辰）'
    golds[cid] = {'id': cid, 'master_prediction': e['master_prediction'],
                  'outcome_record': e['outcome_record'], 'tradition': 'liuyao',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': cards[cid]['provenance'],
                  'license_status': cards[cid]['license_status'],
                  'redistributable': False}
    strip_register[cid] = ['pollution/pollution_note/anchor_presence/anchor_missing/'
                           'dedup_check/filters/outcome_type/outcome_record/'
                           'master_prediction（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('question←input_fields.question；context←asked_at＋书名组写'
                                '（台账无 context 原文，承 holdout20/21 先例）；'
                                'setting/provenance←台账 source 逐字；anchors←asked_at＋'
                                'input_fields.chart 全列逐字')

assert set(cards) == set(ORDER) and set(golds) == set(ORDER)
assert all(eligibility[c]['pass'] for c in ORDER)

# 输入卡字段白名单断言＋禁用键递归零残留
for cid in ORDER:
    assert list(cards[cid].keys()) == INPUT_FIELDS, (cid, list(cards[cid].keys()))
    assert not banned_key_scan(cards[cid]), (cid, banned_key_scan(cards[cid]))
    assert golds[cid]['outcome_record'].strip(), cid
    assert golds[cid]['master_prediction'].strip(), cid
    assert golds[cid]['pollution'] == 'low' and golds[cid]['grade'] == 'A', cid
    assert cards[cid]['redistributable'] is False, cid
    assert '用户经学校图书馆提供' in cards[cid]['provenance'], cid

# ---------- 断语扫描①：逐字片段扫描 ----------
scan1 = {}
for cid in ORDER:
    card_text = json.dumps(cards[cid], ensure_ascii=False)
    hits_mp, hits_oc = [], []
    for fr in fragments(golds[cid]['master_prediction']):
        if fr in card_text:
            hits_mp.append(fr)
    for fr in fragments(golds[cid]['outcome_record']):
        if fr in card_text:
            hits_oc.append(fr)
    scan1[cid] = {'master_prediction_hits': hits_mp, 'outcome_hits': hits_oc}
    assert not hits_oc, (cid, hits_oc[:5])  # 结局片段全例零命中（硬断言）
    if cid not in ZCB_IDS:
        assert not hits_mp, (cid, hits_mp[:5])  # 非测字例断语片段零命中（硬断言）
# 测字例断语片段命中分类：只许命中字形拆分语（台账 input_side 拆分过程引文内含语），
# 且命中 fragment 必须逐字见于台账原 input_side（即卡面锚点原文），逐 fragment 登记。
cezi_scan_class = {}
for cid in ZCB_IDS:
    orig_input = zc_by[cid]['input_side']
    classified = []
    for fr in scan1[cid]['master_prediction_hits']:
        in_anchor = fr in orig_input
        classified.append({'fragment': fr, 'in_taizhang_input_side_anchor': in_anchor,
                           'class': '字形拆分过程锚点原文内含语（§三明列字形拆分过程为'
                                    '输入侧锚点原文；断语与拆语同源同文，非结局泄漏）'
                           if in_anchor else '未分类命中'})
        assert in_anchor, (cid, fr)
    cezi_scan_class[cid] = classified

# ---------- 扫描②：内容级标记＋字段名黑名单（h20 第二道口径） ----------
scan_markers = {}
for cid in ORDER:
    ch = scan_content(cards[cid])
    fh = scan_field_names(cards[cid])
    scan_markers[cid] = {'content_hits': ch, 'fieldname_hits': fh}
    assert not ch and not fh, (cid, ch, fh)

# ---------- 落盘 ----------
for cid in ORDER:
    with open(os.path.join(IN_DIR, f'{cid}.json'), 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
        f.write('\n')
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in ORDER:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')

# ---------- 建后逐卡回读自检（第三道之建集席部分）：盘上文件复扫 ----------
read_cards = {fn[:-5]: load_json(os.path.join(IN_DIR, fn))
              for fn in os.listdir(IN_DIR) if fn.endswith('.json')}
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
assert set(read_cards) == set(ORDER) and len(read_cards) == 27
assert {g['id'] for g in read_golds} == set(ORDER) and len(read_golds) == 27
reread = {}
for cid in ORDER:
    card_text = json.dumps(read_cards[cid], ensure_ascii=False)
    g = next(x for x in read_golds if x['id'] == cid)
    oc_hits = [fr for fr in fragments(g['outcome_record']) if fr in card_text]
    mp_hits = [fr for fr in fragments(g['master_prediction']) if fr in card_text]
    assert not oc_hits, (cid, oc_hits[:3])
    if cid not in ZCB_IDS:
        assert not mp_hits, (cid, mp_hits[:3])
    assert not scan_content(read_cards[cid]) and not scan_field_names(read_cards[cid]), cid
    assert not banned_key_scan(read_cards[cid]), cid
    assert list(read_cards[cid].keys()) == INPUT_FIELDS, cid
    reread[cid] = {'outcome_hits': oc_hits, 'master_prediction_hits': mp_hits,
                   'marker_hits': 0, 'banned_key_hits': 0, 'pass': True}

sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
sha_sum = subprocess.run(['sha256sum', gold_path], capture_output=True, text=True).stdout.split()[0]
assert sha_lib == sha_sum

# ---------- 快照：封存时点活 method 全量复制＋逐件 SHA 清单 ----------
SNAP_DIR = os.path.join(R76, 'kb-snapshot-holdout22')
if os.path.exists(SNAP_DIR):
    shutil.rmtree(SNAP_DIR)
shutil.copytree(os.path.join(BASE, 'method'), SNAP_DIR)
snap_entries = []
for root, dirs, files in os.walk(SNAP_DIR):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, SNAP_DIR)
        snap_entries.append((rel, hashlib.sha256(open(p, 'rb').read()).hexdigest()))
SNAP_SHA_PATH = os.path.join(R76, 'kb-snapshot-holdout22-sha256.txt')
with open(SNAP_SHA_PATH, 'w', encoding='utf-8') as f:
    for rel, h in snap_entries:
        f.write(f'{h}  {rel}\n')
# 与 R76 开轮快照 diff 自核（应恰为 cezi/qimen/bazi 三件）
open_snap = os.path.join(R76, 'kb-snapshot')
diff_files = []
open_rels = set()
for root, dirs, files in os.walk(open_snap):
    dirs.sort()
    for fn in sorted(files):
        rel = os.path.relpath(os.path.join(root, fn), open_snap)
        open_rels.add(rel)
new_map = dict(snap_entries)
for rel in sorted(open_rels | set(new_map)):
    op = os.path.join(open_snap, rel)
    oh = hashlib.sha256(open(op, 'rb').read()).hexdigest() if os.path.exists(op) else None
    if oh != new_map.get(rel):
        diff_files.append(rel)
assert diff_files == ['references/chinese-bazi-ziwei.md',
                      'references/chinese-cezi.md',
                      'references/chinese-qimen.md'], diff_files

# ---------- 构成统计 ----------
SOURCE_OF = {}
for cid in ORDER:
    if cid.startswith('DS-'):
        SOURCE_OF[cid] = '段建业《段氏理象学》'
    elif cid in KW_IDS:
        SOURCE_OF[cid] = '张志春《开悟之门》'
    elif cid in QW_IDS:
        SOURCE_OF[cid] = '刘文元《奇门启悟》'
    elif cid in SG_IDS:
        SOURCE_OF[cid] = '石建国《奇门遁甲最新实例解析》'
    elif cid.startswith('ZCB-'):
        SOURCE_OF[cid] = '《字触补》（《四库未收书辑刊》陆辑第拾捌册）'
    else:
        SOURCE_OF[cid] = '王虎应《六爻卦例说真》'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)

report = {
    'round': 76, 'set': 'holdout22', 'built_by': '组集封存席（R76）',
    'ruling': 'runs/round76/PREREG-ADDENDUM-r76.md §三',
    'T': 27, 'order': ORDER,
    'selection_register': selection_register,
    'liuyao_five_element_recheck': liuyao_check,
    'triple_key_crosscheck_qm': triple_check,
    'composition': {'by_source': dict(src_counts), 'by_tradition': dict(trad_counts),
                    'non_liuyao': 27 - trad_counts['liuyao'],
                    'non_yijian': 27,
                    'max_single_tradition': max(trad_counts.values()),
                    'max_single_source': max(src_counts.values())},
    'eligibility_assertions': eligibility,
    'eligibility_all_pass': True,
    'zero_reuse_recheck': {
        'sources': used_sources, 'used_union_actual': len(used_union),
        'r59_accounting_1052': r59_accounting,
        'method': '只对 id 集（phase2/splits2.json holdout2、holdout3–21 test_gold.jsonl '
                  '仅取 id 字段、holdout2–21 inputs 与 *-inputs 目录文件名、'
                  'data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs '
                  '目录文件名）；未打开任何已封存集金标正文做内容比对；六爻 4 例另逐 id '
                  '核可选未用池（GSZ 57）成员状态',
        'selected_hit_count': 0, 'selected_hits': reuse_hits},
    'input_field_whitelist': INPUT_FIELDS,
    'rewrites': rewrites,
    'strip_register': strip_register,
    'field_mapping_notes': field_mapping_notes,
    'gold_supplement': SUPPLEMENT,
    'gold_supplement_count': len(SUPPLEMENT),
    'scan1_verbatim_fragment': {
        'method': '每例 master_prediction 与 outcome_record 的特征片段（标点分句整句'
                  '（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描；'
                  '结局片段全 27 例零命中（硬断言）；断语片段非测字 23 例零命中（硬断言）；'
                  '测字 4 例命中逐 fragment 分类登记（只许字形拆分过程锚点原文内含语）',
        'per_case': scan1, 'cezi_hit_classification': cezi_scan_class},
    'scan_marker_selfcheck': {
        'method': 'h20 第二道口径：R42 PREREG §5 内容级一级/二级标记＋字段名黑名单'
                  '＋禁用键集对 27 张输入卡全字段递归扫描',
        'per_case': scan_markers,
        'total_hits': sum(len(v['content_hits']) + len(v['fieldname_hits'])
                          for v in scan_markers.values())},
    'scan_reread_selfcheck': {
        'method': '建后逐卡回读自检：落盘后对盘上 27 卡重行片段扫描＋标记扫描＋'
                  '禁用键扫描＋字段白名单核，全过',
        'per_case': reread},
    'scan2_semantic_spotcheck': '见封存日志登记名单（组集席逐例读卡人工核）',
    'scan3_host_rescan': '主持验封道，非本席执行——留位',
    'gold_sha256': sha_lib, 'gold_sha256_sha256sum': sha_sum,
    'gold_sha256_double_read_match': sha_lib == sha_sum,
    'kb_snapshot': {'dir': 'runs/round76/kb-snapshot-holdout22/',
                    'file_count': len(snap_entries),
                    'sha256_list': 'runs/round76/kb-snapshot-holdout22-sha256.txt',
                    'files': [rel for rel, _ in snap_entries],
                    'diff_vs_round76_opening_snapshot': diff_files},
    'outputs_written': [f'holdout22/inputs/{c}.json' for c in ORDER] +
                       ['holdout22/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 27, 'order': ORDER,
                  'used_union_actual': len(used_union),
                  'snapshot_files': len(snap_entries),
                  'diff_vs_opening': diff_files,
                  'gold_sha256': sha_lib,
                  'cezi_scan_hits': {k: len(v) for k, v in cezi_scan_class.items()}},
                 ensure_ascii=False))
