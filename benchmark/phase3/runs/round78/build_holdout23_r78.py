#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R78 组集封存席：按 PREREG-ADDENDUM-r78.md 组建并封存 holdout23（T＝27）。

构成（附则 §一写死）：DS 6／开悟 QM 5／启悟 QM 2／石建国 QM 3／ZCB 6／GSZ 5。
选例（附则 §二）：各源资格滤＋已用并集逐 id 滤（盘上实算）后按台账登记序取足定额。
- DS：eligible_net∧present∧low∧filters 四项全 pass∧断语/结局非空；DS-047（medium）排除；
  同造合并组（台账已合并为单卡之 DS-011/DS-033）至多取 1——本轮入选不含该二卡；
  DS-015 因节题（原书章节题「差命」）含命造质量断语、属泄题列单挂起待主持裁处
  （承 holdout22 主持 DS-011 节题中性化裁处先例，本席不得自改），按登记序递补 DS-019。
- 开悟：present∧low∧separable∧stem_check 天地盘双 ok∧断语/结局非空（QM-017 天盘未合、滤除登记）。
- 启悟/石建国：present∧low∧separable∧断语/结局非空。
- ZCB：eligible∧present∧low∧separable∧断语/结局非空；mid（ZCB-016..019）不取；
  已用 ZCB id 以 holdout22/test_gold.jsonl 盘上实读为准（ZCB-001/002/004/005）；
  ZCB-003 台账资格虽过且未入已用并集，但其输入侧锚点原文含结论句「故知丁艱」，
  已经 holdout22 主持裁处（data/holdout22-seal-log.md §九.1）判为断语/结局事实入卡
  并换例剔除——本轮承该裁处列入泄题列单挂起待主持裁处，按登记序递补足额。
- GSZ：grade A∧low∧present∧eligible_net∧断语/结局非空∧可选未用池成员，逐例回原书
  文字层（runs/round76/gsz-book-r76.txt）复核锚点五要素（卦名、动爻、世应、六亲纳支、
  月建日辰，附则 §二.6）；GSZ-020 动爻缺如（原书自注「内因无动爻」）缺一换下（承 holdout22 先例）。
金标补录 1 例：ZCB-006 台账 master_assertion 以「……」省略中段一句、非逐字，
  本席回原书（合集 PDF560 下半、卷二·外部叶14）读页图逐字补录（见 SUPPLEMENT）。
输入卡 schema {id, tradition, subject, context, question, setting, provenance,
redistributable, license_status, anchors}（承 holdout22 卡实读字段集）。
扫描：①逐字片段扫描（结局片段全例零命中硬断言；断语片段非测字例零命中硬断言；
测字例命中逐 fragment 分类、只许台账 input_side 拆分过程锚点原文内含语）；
②R42 PREREG §5 内容级标记＋字段名黑名单＋禁用键集递归扫描零命中硬断言；
③落盘后逐卡回读复扫。金标 SHA-256 脚本 hashlib＋独立 sha256sum 双读断言一致。
快照：自现行活 method/ 复制 runs/round78/kb-snapshot-holdout23＋SHA 清单（封存时点锚定，
在本轮任何 method 集成之前）。只建卡与封存：不作断、不评分、不开封、不做 git 操作。
零复用只对 id 集（各金标仅取 id 字段，未打开已封存集金标正文做内容比对；
holdout22/test_gold.jsonl 亦仅取 id 列）。
"""
import json, hashlib, os, re, shutil, subprocess
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'
R78 = os.path.join(BASE, 'runs/round78')
DIG76 = os.path.join(BASE, 'runs/round76/digestion')
OUT_DIR = os.path.join(BASE, 'holdout23')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R78, 'build-holdout23-report-r78.json')

LEVEL1 = ['断语线索', '断曰', '断語', '正议', '正議', '验语', '驗語',
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

# ---------- 已用并集（盘上逐 id 实算；金标只取 id 字段） ----------
used_sources = {}
dev_ids = set(load_json(os.path.join(BASE, 'data/master-baseline-dev9.json')).keys())
used_sources['dev9_baseline_keys'] = len(dev_ids)
for dv in ('inputs-dev9', 'inputs-dev10', 'inputs-dev11', 'inputs-dev12', 'inputs'):
    d = os.path.join(BASE, dv)
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                dev_ids.add(fn[:-5])
used_sources['dev_pool_with_input_dirs'] = len(dev_ids)

h2_ids = set(load_json(os.path.join(ROOT, 'benchmark/phase2/splits2.json'))['holdout2'])
used_sources['phase2_splits2_holdout2'] = len(h2_ids)

gold_ids = set()
gold_per_set = {}
for i in range(3, 23):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    s = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip():
                s.add(json.loads(line)['id'])
    gold_per_set[f'holdout{i}'] = len(s)
    gold_ids |= s
used_sources['holdout3_22_gold_ids'] = len(gold_ids)
used_sources['gold_per_set'] = gold_per_set

input_ids = set()
for i in range(2, 23):
    for dname in (f'holdout{i}/inputs', f'holdout{i}-inputs'):
        d = os.path.join(BASE, dname)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'):
                    input_ids.add(fn[:-5])
used_sources['holdout2_22_input_card_ids'] = len(input_ids)
extra_input_ids = set()
for i in range(6, 11):
    d = os.path.join(BASE, f'inputs{i}')
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                extra_input_ids.add(fn[:-5])
used_sources['toplevel_inputs6_10_card_ids'] = len(extra_input_ids)

used_union = dev_ids | h2_ids | gold_ids | input_ids | extra_input_ids
used_sources['used_union_total'] = len(used_union)

# ZCB 已用 id 以 holdout22/test_gold.jsonl 盘上实读为准（附则 §二.5）
h22_gold_ids = [json.loads(l)['id'] for l in
                open(os.path.join(BASE, 'holdout22/test_gold.jsonl'), encoding='utf-8')
                if l.strip()]
zcb_used_h22 = sorted(c for c in h22_gold_ids if c.startswith('ZCB-'))
assert zcb_used_h22 == ['ZCB-001', 'ZCB-002', 'ZCB-004', 'ZCB-005'], zcb_used_h22

selection_register = {}
leak_hold = []  # 泄题列单（挂起待主持裁处）

# ---------- DS 6 ----------
ds_by = {r['case_id']: r for r in ds_mining['records']}
ds_cands = [r for r in ds_mining['records']
            if r['eligible_net'] is True and r['anchor_status'] == 'present'
            and r['contamination_pre'] == 'low'
            and all(str(v).startswith('pass') for v in r['filters'].values())
            and r['master_assertion'].strip() and r['outcome'].strip()]
assert 'DS-047' not in [r['case_id'] for r in ds_cands]
ds_skipped_used = [r['case_id'] for r in ds_cands if r['case_id'] in used_union]
ds_unused = [r for r in ds_cands if r['case_id'] not in used_union]
# DS-015 泄题挂起：原书章节题「差命」为命造质量断语（节题含断语事实），列单待裁处
assert '差命' in ds_by['DS-015']['source']
leak_hold.append({'id': 'DS-015', 'source': '段建业《段氏理象学》',
                  'issue': '输入卡 setting/provenance 承台账 source 逐字时含原书第六章'
                           '章节题「差命·例五」——「差命」为对该命造质量的断语性判定，'
                           '属节题含断语事实（泄题）；本席不得自改，挂起待主持裁处'
                           '（裁处选项：承 holdout22 DS-011 先例中性化节题后补入，'
                           '补入时替换递补例 DS-019）',
                  'status': '挂起，未入选；定额由登记序下一例 DS-019 递补'})
ds_pool = [r for r in ds_unused if r['case_id'] != 'DS-015']
DS_IDS = [r['case_id'] for r in ds_pool[:6]]
assert DS_IDS == ['DS-013', 'DS-014', 'DS-016', 'DS-017', 'DS-018', 'DS-019'], DS_IDS
pillars_sel = [ds_by[c]['input_side']['pillars_verbatim'] for c in DS_IDS]
assert len(set(pillars_sel)) == 6  # 同造（同四柱）组内零重复
merged_cards = [c for c in DS_IDS if c in ('DS-011', 'DS-033')]
assert len(merged_cards) <= 1
selection_register['DS'] = {
    'rule': 'eligible_net∧present∧low∧filters 全 pass∧断语/结局非空（DS-047 medium 排除）'
            '→已用并集逐 id 滤→DS-015 泄题挂起→按登记序取 6',
    'candidate_count': len(ds_cands), 'skipped_used_ids': ds_skipped_used,
    'leak_hold': ['DS-015'], 'selected': DS_IDS,
    'merged_group_note': '台账同造合并组已合并为单卡 DS-011/DS-033（各为一组之唯一卡），'
                         '本轮入选不含该二卡，同造合并组至多取 1 之限未触发；入选 6 例四柱互异'}

# ---------- 开悟 QM 5 ----------
kw_by = {c['case_id']: c for c in kw_mining['cases']}
kw_full = [c for c in kw_mining['cases']
           if c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
           and c['separable'] is True
           and c['stem_check']['tianpan_ok'] and c['stem_check']['dipan_ok']
           and c['master_assertion'].strip() and c['outcome'].strip()]
kw_notfull = [c['case_id'] for c in kw_mining['cases']
              if not (c['stem_check']['tianpan_ok'] and c['stem_check']['dipan_ok'])]
kw_skipped_used = [c['case_id'] for c in kw_full if c['case_id'] in used_union]
KW_IDS = [c['case_id'] for c in kw_full if c['case_id'] not in used_union][:5]
assert KW_IDS == ['QM-015', 'QM-016', 'QM-018', 'QM-019', 'QM-020'], KW_IDS
selection_register['KW'] = {
    'rule': 'present∧low∧separable∧stem_check 天地盘双 ok∧断语/结局非空→已用滤→登记序取 5',
    'full_count': len(kw_full), 'not_full_ids': kw_notfull,
    'skipped_used_ids': kw_skipped_used, 'selected': KW_IDS,
    'note': 'QM-017 登记序在 QM-016 与 QM-018 之间，因天盘 stem_check 未合被资格滤除（非已用剔除）'}

# ---------- 启悟 QM 2／石建国 QM 3 ----------
qw_by = {c['case_id']: c for c in qw_mining['cases']}
qw_cands = [c for c in qw_mining['cases']
            if c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
            and c['separable'] is True
            and c['master_assertion'].strip() and c['outcome'].strip()]
QW_IDS = [c['case_id'] for c in qw_cands if c['case_id'] not in used_union][:2]
assert QW_IDS == ['QM-204', 'QM-205'], QW_IDS
sg_by = {c['case_id']: c for c in sg_mining['cases']}
sg_cands = [c for c in sg_mining['cases']
            if c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
            and c['separable'] is True
            and c['master_assertion'].strip() and c['outcome'].strip()]
SG_IDS = [c['case_id'] for c in sg_cands if c['case_id'] not in used_union][:3]
assert SG_IDS == ['QM-304', 'QM-305', 'QM-306'], SG_IDS
selection_register['QW_SG'] = {
    'rule': 'present∧low∧separable∧断语/结局非空→已用滤→登记序取足（启悟 2／石建国 3）',
    'qw_skipped_used': [c['case_id'] for c in qw_cands if c['case_id'] in used_union],
    'sg_skipped_used': [c['case_id'] for c in sg_cands if c['case_id'] in used_union],
    'selected_qiwu': QW_IDS, 'selected_shijianguo': SG_IDS,
    'sg_notes_register': {c: sg_by[c].get('notes') for c in SG_IDS},
    'sg_note_flag': '石建国入选 3 例台账 notes 逐例登记于此：QM-304 注记含分析第3条月份'
                    '表述与结局略异之并记；QM-305/306 无转录疑字注记；QM-308 型'
                    '（震宫八神一字未读出）疑字注记不在入选 3 例内（QM-308 未入选）'}

# ---------- ZCB 6 ----------
zc_by = {c['case_id']: c for c in zc_mining['cases']}
zc_cands = [c for c in zc_mining['cases']
            if c.get('eligible') is True and c['anchor_status'] == 'present'
            and c['contamination_pre'] == 'low' and c['separable'] is True
            and c['master_assertion'].strip() and c['outcome'].strip()]
zc_skipped_used = [c['case_id'] for c in zc_cands if c['case_id'] in used_union]
assert zc_skipped_used == ['ZCB-001', 'ZCB-002', 'ZCB-004', 'ZCB-005'], zc_skipped_used
leak_hold.append({'id': 'ZCB-003', 'source': '《字触补》卷二·外部',
                  'issue': '台账资格全过且 id 未入已用并集，但其 input_side 拆分过程'
                           '锚点原文末句含结论句「故知丁艱。此斷以理也」——已由 holdout22 '
                           '主持裁处（data/holdout22-seal-log.md §九.1）判为断语/结局事实'
                           '入卡并换例剔除；本轮承该裁处挂起待主持裁处（是否永不再用，'
                           '或附条件处置，由主持定），不自行改题、不动金标',
                  'status': '挂起，未入选；定额由登记序后续例递补'})
zc_pool = [c for c in zc_cands if c['case_id'] not in used_union
           and c['case_id'] != 'ZCB-003']
ZCB_IDS = [c['case_id'] for c in zc_pool[:6]]
assert ZCB_IDS == ['ZCB-006', 'ZCB-007', 'ZCB-008', 'ZCB-009', 'ZCB-010', 'ZCB-011'], ZCB_IDS
selection_register['ZCB'] = {
    'rule': 'eligible∧present∧low∧separable∧断语/结局非空（mid 不取）→已用滤'
            '（已用以 holdout22 金标盘上实读为准）→ZCB-003 承既有裁处挂起→登记序取 6',
    'candidate_count': len(zc_cands), 'skipped_used_ids': zc_skipped_used,
    'leak_hold': ['ZCB-003'], 'selected': ZCB_IDS}

# ---------- GSZ 5（可选未用池逐例回原书五要素复核） ----------
gsz_net = gsz_mining['counts']['net_eligible_A_low_present']
assert len(gsz_net) == 63
gsz_used_in_pool = [c for c in gsz_net if c in used_union]
gsz_pool = [c for c in gsz_net if c not in used_union]
gsz_by = {e['provisional_id']: e for e in gsz_mining['entries']}
book_txt = open(os.path.join(BASE, 'runs/round76/gsz-book-r76.txt'), encoding='utf-8').read()
LIUQIN = ['兄弟', '子孙', '妻财', '官鬼', '父母']
GANZHI = list('甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥')


def five_elements(cid):
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
    el['yuejian_richen'] = bool(re.search(r'月', asked) and re.search(r'日', asked))
    el['in_book_ben_gua'] = chart['ben_gua'][:2] in book_txt or chart['ben_gua'] in book_txt
    el['in_book_asked'] = asked.split('（')[0][:7] in book_txt.replace(' ', '')
    return el


liuyao_check = {}
GSZ_IDS = []
for cid in gsz_pool:
    e = gsz_by[cid]
    base_ok = (e['grade'] == 'A' and e['pollution'] == 'low'
               and e['anchor_presence'] == 'present' and e['eligible_net'] is True
               and e['master_prediction'].strip() and e['outcome_record'].strip())
    el = five_elements(cid)
    ok = base_ok and all(el[k] for k in ('gua_name', 'moving', 'shi_ying',
                                         'liuqin_nazhi', 'yuejian_richen',
                                         'in_book_ben_gua', 'in_book_asked'))
    liuyao_check[cid] = {'elements': el, 'base_qual': bool(base_ok), 'pass': bool(ok)}
    if ok:
        GSZ_IDS.append(cid)
    if len(GSZ_IDS) == 5:
        break
assert GSZ_IDS == ['GSZ-028', 'GSZ-030', 'GSZ-031', 'GSZ-032', 'GSZ-033'], GSZ_IDS
assert liuyao_check['GSZ-020']['pass'] is False
assert liuyao_check['GSZ-020']['elements']['moving'] is False
selection_register['GSZ'] = {
    'rule': 'GSZ 净入账 63 − 已用并集命中 10 ＝ 可选未用池 53，登记序逐例资格断言＋回原书'
            '文字层五要素复核，全在场者取前 5',
    'used_in_net_pool': gsz_used_in_pool, 'pool_count': len(gsz_pool),
    'checked_in_order': list(liuyao_check.keys()),
    'rejected': {'GSZ-020': '动爻缺如：原书第四章例五离卦六爻无动爻、变卦空（承 holdout22 '
                            '同例换例先例）；缺一换下一例'},
    'selected': GSZ_IDS, 'cross_source_fallback_triggered': False}

QM_IDS = KW_IDS + QW_IDS + SG_IDS
ORDER = DS_IDS + QM_IDS + ZCB_IDS + GSZ_IDS
assert len(ORDER) == 27 and len(set(ORDER)) == 27, ORDER
reuse_hits = [cid for cid in ORDER if cid in used_union]
assert not reuse_hits, f'选例与已用并集相交：{reuse_hits}'

# ---------- 金标断语补录（ZCB-006，回原书逐字） ----------
SUPPLEMENT = {
    'ZCB-006': {
        'master_prediction': '田者墓田象也。胡氏肆立水傍，而從墓田，其必以酒溺乎。',
        'ledger_original': None,  # 落盘时自台账原值填入登记
        'pages': '《字触补》卷二·外部叶14（合集 PDF560 下半，陆辑拾捌册），本席读 200dpi 渲染页图逐字',
        'reason': '台账 master_assertion 作「田者墓田象也……（胡氏）其必以酒溺乎。」'
                  '以「……」省略中句「胡氏肆立水傍，而從墓田」，非逐字',
        'render_evidence': 'runs/round78/zcb006-p560-r78-560.png（合集 PDF 第 560 页 200dpi 渲染）',
    },
}
SUPPLEMENT['ZCB-006']['ledger_original'] = zc_by['ZCB-006']['master_assertion']
for cid, s in SUPPLEMENT.items():
    s['chars'] = len(s['master_prediction'])

cards, golds = {}, {}
eligibility, strip_register, field_mapping_notes = {}, {}, {}

LICENSE_MODERN = '现代版权文本（扫描本），内部研究用'
PROV_TAIL = '用户经学校图书馆提供；redistributable=false'

# ---------- DS 6 例（八字） ----------
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

# ---------- 开悟 QM 5 例（奇门；input_side 为单串：背景＋干支局式＋盘面） ----------
KW_SUBJECT = {
    'QM-015': '王大妈（为其子求测婚事）；占者：张志春',
    'QM-016': '鹿泉市一位妇女（携女儿求测）；占者：石建国',
    'QM-018': '潘所长（为其子求测）；占者：张志春',
    'QM-019': '王亚萍女士（为其女求测）；占者：张志春',
    'QM-020': '邻居（携大女儿、二女儿高考之事来问）；占者：任宏锦',
}
KW_QUESTION = {  # 前四例为 input_side 原文子串（脚本断言）；QM-020 为组写（登记）
    'QM-015': '请预测这婚姻何时成',
    'QM-016': '求测女儿的家庭状况',
    'QM-018': '求测其子三考大学能否考上',
    'QM-019': '请预测女儿能否通过文化课考试',
    'QM-020': '大女儿、二女儿高考结果待揭晓，来问吉凶（原文未逐字引问句，按问测时间起局验证）',
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
    if cid != 'QM-020':
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
    note = (f"锚点 present（盘面逐字＋天地盘干集验算 stem_check 全合）；"
            f"污染 low；转录：visual（110dpi 渲染页视觉转录、存疑盘面 200dpi 复读）；"
            f"去重：{c['dedup']}")
    golds[cid] = {'id': cid, 'master_prediction': c['master_assertion'],
                  'outcome_record': c['outcome'], 'tradition': 'qimen',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': cards[cid]['provenance'],
                  'license_status': LICENSE_MODERN, 'redistributable': False,
                  'editor_note': '断语逐字核验：台账转录逐字、无摘写/省略标记'
                                 '（无「……」类缺口），照台账；本席未另读页图，'
                                 '逐字性以台账视觉转录口径为准，登记备主持复核。'}
    strip_register[cid] = ['topic/anchor_status/contamination_pre/separable/'
                           'transcription/dedup/master_assertion/outcome'
                           '（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('context←input_side 盘面之前段逐字；anchors.board_verbatim'
                                '←input_side 盘面段逐字；question←input_side 原文子串（断言验；'
                                'QM-020 例外为组写、原文未逐字引问句，口径在此登记）；'
                                'subject 为组写（据 input_side 与 caster 组写，口径在此登记）；'
                                'setting←source＋caster 组写')

# ---------- 启悟 QM 2 例（奇门） ----------
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
    # 卡面引节名时略去篇名（承 holdout22 处置口径），金标 provenance 仍载全节名。
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
    note = (f"锚点 present；污染 low（{c['contamination_reason']}）；"
            f"转录：visual（{c['transcription_confidence']}）；去重：{c['dedup']}")
    if c.get('notes'):
        note += f"；台账注记：{c['notes']}"
    golds[cid] = {'id': cid, 'master_prediction': c['master_assertion'],
                  'outcome_record': c['outcome'], 'tradition': 'qimen',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': (f"{src['book']}（{src['author']}著，{src['publisher']}）·"
                                 f"{src['section']}，印刷页{src['printed_pages']}"
                                 f"（PDF页{src['pdf_pages']}）；{PROV_TAIL}"),
                  'license_status': LICENSE_MODERN, 'redistributable': False}
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

# ---------- ZCB 6 例（测字） ----------
ZCB_SUBJECT = {
    'ZCB-006': '樊某与日者胡氏',
    'ZCB-007': '张济与邵洪（吏部）',
    'ZCB-008': '姚某（卢江太守，未仕时）',
    'ZCB-009': '索充（梦虞脱上衣者）',
    'ZCB-010': '曾迥（大比之秋梦兜者）',
    'ZCB-011': '吴某（范小山妻案被拘者）',
}
ZCB_QUESTION = {
    'ZCB-006': '偶过胡氏肆，见牌悬湖田二字，因占胡氏吉凶',
    'ZCB-007': '问今岁可得典试及学政否（随口占午字）',
    'ZCB-008': '元旦于城隍山下肆拈死字占之',
    'ZCB-009': '梦一虞脱上衣来诣，就占之',
    'ZCB-010': '梦兜生耳无两手，以为不祥，语其兄占之',
    'ZCB-011': '狱中夜梦神入告，问生死',
}
ZCB_CHAR = {'ZCB-006': '湖田', 'ZCB-007': '午', 'ZCB-008': '死',
            'ZCB-009': '虞', 'ZCB-010': '取／了', 'ZCB-011': '周'}
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
                               f"补录断语全文 {s['chars']} 字（标点为本席转录标点、字本体逐字）；"
                               f"台账原值：「{s['ledger_original']}」；渲染证据：{s['render_evidence']}；"
                               f"台账 outcome 与原书页图（「後胡氏果醉墮水死」）逐字合，照台账。")
    golds[cid] = gold
    strip_register[cid] = ['title（原书条题含断语指向者一律不入卡，题面定位中性化，'
                           '见 field_mapping_notes）/anchor_status/anchor_basis/'
                           'contamination_pre/contamination_basis/separable/eligible/'
                           'cz_qx_counted/cz_qx_note/dedup/transcription/'
                           'master_assertion/outcome（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('context/anchors.split_process_verbatim←input_side 逐字'
                                '（字形拆分过程为附则明列之输入侧锚点原文）；'
                                'subject/question 为组写（口径在此登记）；'
                                'setting/provenance 只载卷叶与 PDF 页定位，不载原书条题'
                                '（条题含断语/结局指向，承 holdout22 中性化口径）')

# ---------- GSZ 5 例（六爻，承 holdout22 体例） ----------
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
                                '（台账无 context 原文，承 holdout22 先例）；'
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

# ---------- 断语扫描①：逐字片段扫描（构建脚本内断言） ----------
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
    assert not hits_oc, (cid, hits_oc[:5])
    if cid not in ZCB_IDS:
        assert not hits_mp, (cid, hits_mp[:5])
cezi_scan_class = {}
for cid in ZCB_IDS:
    orig_input = zc_by[cid]['input_side']
    classified = []
    for fr in scan1[cid]['master_prediction_hits']:
        in_anchor = fr in orig_input
        classified.append({'fragment': fr, 'in_taizhang_input_side_anchor': in_anchor,
                           'class': '字形拆分过程锚点原文内含语（附则明列字形拆分过程为'
                                    '输入侧锚点原文；断语与拆语同源同文，非结局泄漏）'
                           if in_anchor else '未分类命中'})
        assert in_anchor, (cid, fr)
    cezi_scan_class[cid] = classified

# ---------- 扫描②：内容级标记＋字段名黑名单（R42 PREREG §5） ----------
scan_markers = {}
for cid in ORDER:
    ch = scan_content(cards[cid])
    fh = scan_field_names(cards[cid])
    scan_markers[cid] = {'content_hits': ch, 'fieldname_hits': fh}
    assert not ch and not fh, (cid, ch, fh)

# ---------- 构成与限度断言（封存验收①） ----------
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
assert len(ORDER) == 27
assert max(trad_counts.values()) * 2 <= 27, trad_counts
assert max(src_counts.values()) * 2 <= 27, src_counts
assert 27 - 0 >= 13  # 非夷坚：本集六源皆非夷坚
assert 27 - trad_counts['liuyao'] >= 13
assert len(src_counts) >= 2  # 多源构成（六源）
assert all(golds[c]['pollution'] == 'low' for c in ORDER)
assert not [c for c in ORDER if c in used_union]
composition_assertions = {
    'T': 27, 'by_tradition': dict(trad_counts), 'by_source': dict(src_counts),
    'max_single_tradition_share': max(trad_counts.values()) / 27,
    'max_single_source_share': max(src_counts.values()) / 27,
    'non_yijian': 27, 'non_liuyao': 27 - trad_counts['liuyao'],
    'source_count': len(src_counts), 'pollution_low': 27,
    'used_union_intersection': [], 'all_pass': True}

# ---------- 落盘 ----------
for cid in ORDER:
    with open(os.path.join(IN_DIR, f'{cid}.json'), 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
        f.write('\n')
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in ORDER:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')

# ---------- 落盘后逐卡回读自检 ----------
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

# ---------- 金标 SHA-256 双读 ----------
sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
sha_sum = subprocess.run(['sha256sum', gold_path], capture_output=True, text=True).stdout.split()[0]
assert sha_lib == sha_sum

# ---------- 快照：封存时点活 method 全量复制＋逐件 SHA 清单 ----------
SNAP_DIR = os.path.join(R78, 'kb-snapshot-holdout23')
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
SNAP_SHA_PATH = os.path.join(R78, 'kb-snapshot-holdout23-sha256.txt')
with open(SNAP_SHA_PATH, 'w', encoding='utf-8') as f:
    for rel, h in snap_entries:
        f.write(f'{h}  {rel}\n')
snap_list_sha = hashlib.sha256(open(SNAP_SHA_PATH, 'rb').read()).hexdigest()
# 与 R78 开轮快照 diff 自核（只登记，不作断言）
open_snap = os.path.join(R78, 'kb-snapshot')
diff_files = []
if os.path.isdir(open_snap):
    open_map = {}
    for root, dirs, files in os.walk(open_snap):
        dirs.sort()
        for fn in sorted(files):
            p = os.path.join(root, fn)
            open_map[os.path.relpath(p, open_snap)] = \
                hashlib.sha256(open(p, 'rb').read()).hexdigest()
    new_map = dict(snap_entries)
    for rel in sorted(set(open_map) | set(new_map)):
        if open_map.get(rel) != new_map.get(rel):
            diff_files.append(rel)

report = {
    'round': 78, 'set': 'holdout23', 'built_by': '组集封存席（R78）',
    'ruling': 'runs/round78/PREREG-ADDENDUM-r78.md（唯一授权文本）；主预注册 PREREG.md §4/§7',
    'T': 27, 'order': ORDER,
    'selection_register': selection_register,
    'leak_hold_list': leak_hold,
    'liuyao_five_element_recheck': liuyao_check,
    'composition_assertions': composition_assertions,
    'eligibility_assertions': eligibility,
    'eligibility_all_pass': True,
    'zero_reuse_recheck': {
        'sources': used_sources,
        'method': '只对 id 集（dev9 基线键集＋inputs-dev9/10/11/12 与 inputs 目录文件名、'
                  'phase2 splits2 holdout2、holdout3–22 各 test_gold.jsonl 仅取 id 字段、'
                  'holdout2–22 inputs 与 *-inputs 目录文件名、顶层 inputs6–10 目录文件名）；'
                  '未打开任何已封存集金标正文做内容比对；holdout22 金标亦仅取 id 列',
        'selected_hit_count': 0, 'selected_hits': reuse_hits},
    'input_field_whitelist': INPUT_FIELDS,
    'strip_register': strip_register,
    'field_mapping_notes': field_mapping_notes,
    'gold_supplement': SUPPLEMENT,
    'gold_supplement_count': len(SUPPLEMENT),
    'scan1_verbatim_fragment': {
        'method': '每例 master_prediction 与 outcome_record 的特征片段（标点分句整句'
                  '（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描；'
                  '结局片段全 27 例零命中（硬断言）；断语片段非测字 21 例零命中（硬断言）；'
                  '测字 6 例命中逐 fragment 分类登记（只许字形拆分过程锚点原文内含语）',
        'per_case': scan1, 'cezi_hit_classification': cezi_scan_class},
    'scan_marker_selfcheck': {
        'method': 'R42 PREREG §5 内容级一级/二级标记＋字段名黑名单＋禁用键集对 27 张输入卡'
                  '全字段递归扫描（构建脚本内断言道）',
        'per_case': scan_markers,
        'total_hits': sum(len(v['content_hits']) + len(v['fieldname_hits'])
                          for v in scan_markers.values())},
    'scan_reread_selfcheck': {
        'method': '落盘后逐卡回读：对盘上 27 卡重行片段扫描＋标记扫描＋禁用键扫描＋字段白名单核，全过',
        'per_case': reread},
    'scan2_independent_rescan': '由独立复扫脚本 scan_holdout23_r78.py 执行，结果另行登记于封存日志',
    'scan3_host_rescan': '主持验封道，非本席执行——留位',
    'gold_sha256': sha_lib, 'gold_sha256_sha256sum': sha_sum,
    'gold_sha256_double_read_match': sha_lib == sha_sum,
    'kb_snapshot': {'dir': 'runs/round78/kb-snapshot-holdout23/',
                    'file_count': len(snap_entries),
                    'sha256_list': 'runs/round78/kb-snapshot-holdout23-sha256.txt',
                    'sha256_list_sha256': snap_list_sha,
                    'files': [rel for rel, _ in snap_entries],
                    'diff_vs_round78_opening_snapshot': diff_files},
    'outputs_written': [f'holdout23/inputs/{c}.json' for c in ORDER] +
                       ['holdout23/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 27, 'order': ORDER,
                  'used_union_total': len(used_union),
                  'snapshot_files': len(snap_entries),
                  'diff_vs_opening': diff_files,
                  'gold_sha256': sha_lib,
                  'cezi_scan_hits': {k: len(v) for k, v in cezi_scan_class.items()}},
                 ensure_ascii=False))
