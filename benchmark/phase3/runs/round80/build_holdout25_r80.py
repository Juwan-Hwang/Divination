#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R80 组集封存席：按 PREREG-ADDENDUM-r80.md 组建并封存 holdout25（T＝27）。

构成（增补件 §一写定）：DS 6／开悟 QM 5／启悟 QM 2／石建国 QM 3／GSZ 11；ZCB 定额 0。
选例（增补件 §二）：各源资格滤＋已用并集逐 id 滤（盘上实算，holdout2–24，实算 1058 id）
后按台账登记序取足定额；逐 id 资格断言全过才入选。
- DS：eligible_net∧present∧low∧filters 四项全 pass∧断语/结局非空；DS-047（medium）排除；
  同造合并组（台账已合并为单卡之 DS-011/DS-033）至多取 1——本轮入选不含该二卡；
  登记序取 DS-025–DS-030（四柱互异）。
- 开悟：present∧low∧separable∧stem_check 天地盘双 ok（全合）∧断语/结局非空；
  QM-026 天盘 ok、地盘未 ok（未全合）登记序首位滤除，取 QM-027–QM-031。
- 启悟：present∧low∧separable∧断语/结局非空，取 QM-208、QM-209。
- 石建国：同上四项；台账全 11 例中未用合格者仅 QM-310、QM-311 两例，定额 3 不足 1 例，
  触发增补件 §二跨源递补规则②：差额先由 QM 他子源余例（开悟须全合）按登记序递补——
  他子源以增补件 §一表列序（开悟→启悟）为序，开悟全合余例首例 QM-032 递补 1 例；
  GSZ 二次递补未触发。递补后复断言：单体系最大六爻 11≤13、单源最大 GSZ 11≤13、
  非六爻 16≥13、非夷坚 27。
- GSZ：grade A∧low∧present∧eligible_net∧断语/结局非空∧可选未用池成员，逐例回原书
  文字层（runs/round76/gsz-book-r76.txt）复核锚点五要素（卦名、动爻、世应、六亲纳支、
  月建日辰，增补件 §二.5）；登记序首例 GSZ-020 动爻缺如缺一换下（承 holdout22–24 先例），
  取 GSZ-049、GSZ-050、GSZ-052、GSZ-053、GSZ-054、GSZ-055、GSZ-058、GSZ-059、GSZ-060、
  GSZ-061、GSZ-068 共 11 例。
- ZCB：定额 0、不取例；合格存量复算 eligible∧present∧low∧separable 共 15 例，已用 14 例
  （holdout22/23/24），ZCB-003 维持排除 1 例，可选余 0（承增补件 §一与 PREREG §4 登记）。
金标补录：本轮 27 例断语逐字核验无「……」类缺口，补录 0 例、照台账逐字入标；
结局内「……」2 例（DS-030、QM-208）均为原书叙事/引语内省略字样、属台账逐字原文，
非台账摘录缺口，登记备核。
泄题列单（本席不得自改、卡面原样保留待主持裁处）：
  入选标旗 1 件——QM-208（question 承台账逐字，其背景括注含「經劉斷出南行後自述貨種」，
  引述大师已断内容字样）；排除登记 1 件——ZCB-003（维持排除、未入选）。
建卡卫生删除登记：启悟 2 例卡面 setting/provenance 引节名时略去篇名「分類占斷篇」
（书目信息性字样、含内容级一级标记字，承 holdout22–24 处置口径，金标 provenance 载全）；
「求测例/求测例题」类编辑装置残段与双人例第二人无关结局字样两类删除扫描——入选 27 例
question 逐例核查零匹配、删除 0 件（逐例登记于构建报告 deletion_register）。
输入卡 schema {id, tradition, subject, context, question, setting, provenance,
redistributable, license_status, anchors}（以 holdout24 卡实读字段集对齐）。
扫描：①逐字片段扫描（结局片段与断语片段全例零命中硬断言，本集无测字段）；
②R42 PREREG §5 内容级标记＋字段名黑名单＋禁用键集递归扫描零命中硬断言；
③落盘后逐卡回读复扫。金标 SHA-256 以构建脚本 hashlib 输出记录（封存席另以独立
sha256sum 复算双读，主持再做第三读，本席报告 hashlib 值并在封存日志登记双读）。
快照：自现行活 method/ 复制 runs/round80/kb-snapshot-holdout25＋SHA 清单（封存时点锚定，
含 calibration 第八节 R80-REV1），METHOD-INTEGRATION-r78.md 与 METHOD-INTEGRATION-r80.md
为集成登记件、非快照内容件，自快照排除并登记；与 runs/round80/kb-snapshot 逐件比对登记
（预期差异恰为集成文件集 SKILL.md 与 references/calibration.md）。
只建卡与封存：不作断、不评分、不开封、不做 git 操作。
零复用只对 id 集（各金标仅取 id 字段，未打开已封存集金标正文做内容比对）。
适配自 holdout24 构建脚本（runs/round79/build_holdout24_r79.py），已逐处定点改写
轮次/集号/定额/选例登记；脚本内 round79/holdout24 字样仅存于「承先例/裁处」实指引用
与字段白名单对齐基准（holdout24 卡实读）。
"""
import json, hashlib, os, re, shutil
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'
R80 = os.path.join(BASE, 'runs/round80')
DIG76 = os.path.join(BASE, 'runs/round76/digestion')
OUT_DIR = os.path.join(BASE, 'holdout25')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R80, 'build-holdout25-report-r80.json')

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
# 字段白名单以 holdout24 任一卡实读字段集对齐（增补件 §三）
h24_card = load_json(os.path.join(BASE, 'holdout24/inputs/DS-019.json'))
assert list(h24_card.keys()) == INPUT_FIELDS, list(h24_card.keys())

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
for i in range(3, 25):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    s = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip():
                s.add(json.loads(line)['id'])
    gold_per_set[f'holdout{i}'] = len(s)
    gold_ids |= s
used_sources['holdout3_24_gold_ids'] = len(gold_ids)
used_sources['gold_per_set'] = gold_per_set

input_ids = set()
for i in range(2, 25):
    for dname in (f'holdout{i}/inputs', f'holdout{i}-inputs'):
        d = os.path.join(BASE, dname)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'):
                    input_ids.add(fn[:-5])
used_sources['holdout2_24_input_card_ids'] = len(input_ids)
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
assert len(used_union) == 1058, len(used_union)  # 与主持开轮实算（PREREG 开轮登记）一致

selection_register = {}
leak_hold = []   # 排除登记（未入选，承既有裁处）
leak_flags = []  # 入选标旗（照建不动、卡面原样保留，提请主持裁处）

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
DS_IDS = [r['case_id'] for r in ds_unused[:6]]
assert DS_IDS == ['DS-025', 'DS-026', 'DS-027', 'DS-028', 'DS-029', 'DS-030'], DS_IDS
pillars_sel = [ds_by[c]['input_side']['pillars_verbatim'] for c in DS_IDS]
assert len(set(pillars_sel)) == 6  # 同造（同四柱）组内零重复
merged_cards = [c for c in DS_IDS if c in ('DS-011', 'DS-033')]
assert len(merged_cards) <= 1
selection_register['DS'] = {
    'rule': 'eligible_net∧present∧low∧filters 全 pass∧断语/结局非空（DS-047 medium 排除）'
            '→已用并集逐 id 滤→按登记序取 6',
    'candidate_count': len(ds_cands), 'skipped_used_ids': ds_skipped_used,
    'selected': DS_IDS,
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
kw_full_unused = [c for c in kw_full if c['case_id'] not in used_union]
KW_IDS = [c['case_id'] for c in kw_full_unused[:5]]
assert KW_IDS == ['QM-027', 'QM-028', 'QM-029', 'QM-030', 'QM-031'], KW_IDS
assert 'QM-026' in kw_notfull  # 登记序首位、未全合（地盘未 ok）滤除
selection_register['KW'] = {
    'rule': 'present∧low∧separable∧stem_check 天地盘双 ok（全合）∧断语/结局非空→已用滤→登记序取 5',
    'full_count': len(kw_full), 'not_full_ids': kw_notfull,
    'skipped_used_ids': kw_skipped_used, 'selected': KW_IDS,
    'note': '未全合者本轮不入选、不做建卡精核升格（增补件 §二.3）；QM-026 登记序在 '
            'QM-027 之前、天盘 ok 而地盘未 ok，资格滤除登记'}

# ---------- 启悟 QM 2／石建国 QM 3（石建国不足→跨源递补规则②） ----------
qw_by = {c['case_id']: c for c in qw_mining['cases']}
qw_cands = [c for c in qw_mining['cases']
            if c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
            and c['separable'] is True
            and c['master_assertion'].strip() and c['outcome'].strip()]
QW_IDS = [c['case_id'] for c in qw_cands if c['case_id'] not in used_union][:2]
assert QW_IDS == ['QM-208', 'QM-209'], QW_IDS
sg_by = {c['case_id']: c for c in sg_mining['cases']}
sg_cands = [c for c in sg_mining['cases']
            if c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
            and c['separable'] is True
            and c['master_assertion'].strip() and c['outcome'].strip()]
sg_unused = [c['case_id'] for c in sg_cands if c['case_id'] not in used_union]
SG_IDS = sg_unused[:3]
SG_QUOTA = 3
SG_SHORTFALL = SG_QUOTA - len(SG_IDS)
assert SG_IDS == ['QM-310', 'QM-311'], SG_IDS
assert SG_SHORTFALL == 1, SG_SHORTFALL
# 递补规则②：差额先由 QM 他子源余例（开悟须全合）按登记序递补。他子源序以增补件
# §一表列序为准（开悟→启悟）：开悟全合余例首例为 QM-032；启悟余例 QM-210/QM-211 未及动用。
FALLBACK_IDS = [c['case_id'] for c in kw_full_unused[5:5 + SG_SHORTFALL]]
assert FALLBACK_IDS == ['QM-032'], FALLBACK_IDS
selection_register['QW_SG'] = {
    'rule': 'present∧low∧separable∧断语/结局非空→已用滤→登记序取足（启悟 2／石建国 3）',
    'qw_skipped_used': [c['case_id'] for c in qw_cands if c['case_id'] in used_union],
    'sg_skipped_used': [c['case_id'] for c in sg_cands if c['case_id'] in used_union],
    'selected_qiwu': QW_IDS, 'selected_shijianguo': SG_IDS,
    'sg_all_cases_count': len(sg_mining['cases']),
    'sg_unused_qualified': sg_unused,
    'sg_shortfall': SG_SHORTFALL,
    'fallback': '石建国定额 3、未用合格余例仅 QM-310/QM-311 两例，差额 1 例触发增补件 '
                '§二跨源递补规则②：由 QM 他子源余例递补——他子源以增补件 §一表列序'
                '（开悟→启悟）为序，开悟全合余例登记序首例 QM-032 递补（全合断言：'
                'stem_check 天地盘双 ok）；启悟余例 QM-210/QM-211 未动用；GSZ 二次递补未触发',
    'fallback_selected': FALLBACK_IDS,
    'sg_notes_register': {c: sg_by[c].get('notes') for c in SG_IDS},
    'sg_transcription_confidence': {c: sg_by[c].get('transcription_confidence') for c in SG_IDS},
    'sg_note_flag': '增补件 §二.4 转录疑字注记单列：QM-310/QM-311 台账 notes 均为空、'
                    'transcription_confidence 均为 high，无转录疑字注记，本轮无单列件'}

# ---------- ZCB 定额 0（合格存量复算登记，不取例） ----------
zc_by = {c['case_id']: c for c in zc_mining['cases']}
zc_cands = [c for c in zc_mining['cases']
            if c.get('eligible') is True and c['anchor_status'] == 'present'
            and c['contamination_pre'] == 'low' and c['separable'] is True
            and c['master_assertion'].strip() and c['outcome'].strip()]
zc_skipped_used = [c['case_id'] for c in zc_cands if c['case_id'] in used_union]
zc_pool = [c for c in zc_cands if c['case_id'] not in used_union
           and c['case_id'] != 'ZCB-003']
assert 'ZCB-003' not in used_union  # 从未实际入封任何 holdout 集（盘上金标/卡实读）
assert len(zc_pool) == 0, [c['case_id'] for c in zc_pool]
leak_hold.append({'id': 'ZCB-003', 'source': '《字触补》卷二·外部',
                  'issue': '台账资格全过且 id 未入已用并集，但其 input_side 拆分过程锚点原文'
                           '末句含结论句「故知丁艱。此斷以理也」，已经 holdout22 主持裁处'
                           '（data/holdout22-seal-log.md §九.1）判为断语/结局事实入卡并换例'
                           '剔除；本轮承 PREREG §4 与增补件 §二.6 裁处维持排除、不入选，'
                           '登记序跳过并登记',
                  'status': '维持排除，未入选；本轮 ZCB 定额 0，本无取例'})
selection_register['ZCB'] = {
    'rule': '定额 0，不取例（增补件 §一）；合格存量复算登记如下',
    'stock_recount': {
        'eligible_present_low_total': len(zc_cands),
        'used_ids': zc_skipped_used,
        'excluded_standing_ruling': ['ZCB-003'],
        'selectable_remaining': [c['case_id'] for c in zc_pool],
        'note': '合格总存量 15 − 已用 14（holdout22 取 4、holdout23 取 6、holdout24 取 4）'
                '− ZCB-003 维持排除 1 ＝ 可选 0，与增补件 §一登记（测字同层合格存量已竭）一致'},
    'selected': [], 'quota': 0}

# ---------- GSZ 定额 11（可选未用池逐例回原书五要素复核） ----------
GSZ_QUOTA = 11
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
    liuyao_check[cid] = {'elements': el, 'base_qual': bool(base_ok), 'pass': bool(ok),
                         'ben_gua': e['input_fields']['chart'].get('ben_gua'),
                         'bian_gua': e['input_fields']['chart'].get('bian_gua'),
                         'asked_at': e['input_fields']['asked_at'],
                         'source': e['source']}
    if ok:
        GSZ_IDS.append(cid)
    if len(GSZ_IDS) == GSZ_QUOTA:
        break
assert GSZ_IDS == ['GSZ-049', 'GSZ-050', 'GSZ-052', 'GSZ-053', 'GSZ-054', 'GSZ-055',
                   'GSZ-058', 'GSZ-059', 'GSZ-060', 'GSZ-061', 'GSZ-068'], GSZ_IDS
assert liuyao_check['GSZ-020']['pass'] is False
assert liuyao_check['GSZ-020']['elements']['moving'] is False
selection_register['GSZ'] = {
    'rule': 'GSZ 净入账 63 − 已用并集命中 22 ＝ 可选未用池 41，登记序逐例资格断言＋回原书'
            '文字层五要素复核，全在场者取前 11',
    'used_in_net_pool': gsz_used_in_pool, 'pool_count': len(gsz_pool),
    'checked_in_order': list(liuyao_check.keys()),
    'rejected': {'GSZ-020': '动爻缺如：原书第四章例五离卦六爻无动爻、变卦空（承 holdout22/23/24 '
                            '同例换例先例）；缺一换下一例'},
    'selected': GSZ_IDS, 'quota': GSZ_QUOTA,
    'cross_source_fallback_in': 0,
    'note': 'GSZ 定额 11 足额（未承接他源递补增额）；石建国差额由开悟 QM-032 递补（规则②），'
            '未及 GSZ'}

QM_IDS = KW_IDS + FALLBACK_IDS + QW_IDS + SG_IDS
ORDER = DS_IDS + QM_IDS + GSZ_IDS
assert len(ORDER) == 27 and len(set(ORDER)) == 27, ORDER
reuse_hits = [cid for cid in ORDER if cid in used_union]
assert not reuse_hits, f'选例与已用并集相交：{reuse_hits}'

# ---------- 断语缺口扫描（补录前置核） ----------
gap_register = {}
for cid in ORDER:
    if cid in ds_by:
        mp, oc = ds_by[cid]['master_assertion'], ds_by[cid]['outcome']
    elif cid in kw_by:
        mp, oc = kw_by[cid]['master_assertion'], kw_by[cid]['outcome']
    elif cid in qw_by:
        mp, oc = qw_by[cid]['master_assertion'], qw_by[cid]['outcome']
    elif cid in sg_by:
        mp, oc = sg_by[cid]['master_assertion'], sg_by[cid]['outcome']
    else:
        mp, oc = gsz_by[cid]['master_prediction'], gsz_by[cid]['outcome_record']
    gap_register[cid] = {'mp_gap': '……' in mp, 'oc_gap': '……' in oc}
assert not any(v['mp_gap'] for v in gap_register.values()), \
    [k for k, v in gap_register.items() if v['mp_gap']]
# 结局内「……」2 例均为原书叙事/引语内省略字样（台账逐字原文），非台账摘录缺口，登记备核
assert [k for k, v in gap_register.items() if v['oc_gap']] == ['DS-030', 'QM-208'], \
    [k for k, v in gap_register.items() if v['oc_gap']]
SUPPLEMENT = {}

# ---------- 泄题标旗（入选、照建不动、卡面原样保留） ----------
leak_flags.append({'id': 'QM-208', 'source': '刘文元《奇门启悟》',
                   'field': 'question（承台账 input_side.question 逐字）',
                   'hit': 'question 背景括注含「經劉斷出南行後自述貨種」——引述大师已断内容'
                          '字样（所断「南行」为该例断语方向内容之一部）；括注其余为求测者'
                          '自述之已事背景（货种、差价、组织车皮）',
                   'status': '照台账逐字入卡、原样保留，标旗提请主持裁处'})

cards, golds = {}, {}
eligibility, strip_register, field_mapping_notes = {}, {}, {}
deletion_register = []

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

# ---------- 开悟 QM 6 例（定额 5＋石建国递补 1；奇门；input_side 为单串） ----------
KW_SUBJECT = {
    'QM-027': '河北科迪药业公司陈老板（求测国家科技基金资助）；占者：张志春',
    'QM-028': '河北科迪药业公司陈老板（求测药厂工地开工，三局）；占者：张志春',
    'QM-029': '鹿泉市某药店老板（求测财运）；占者：石建国',
    'QM-030': '李月珍（求测开发建设「太和日化城」项目）；占者：张志春',
    'QM-031': '张志春之一朋友（求测购买太和日化城商位）；占者：张志春',
    'QM-032': '鹿泉市张某（求测蛋糕做不成的原因）；占者：石建国',
}
KW_QUESTION = {  # QM-029 为组写（原文未逐字引问句，登记）；余为 input_side 原文子串（脚本断言）
    'QM-027': '能否得到国家科技基金资助',
    'QM-028': '明天药厂工地能不能开工',
    'QM-029': '求测财运（原文未逐字引问句，按问事时间起局）',
    'QM-030': '拟开发建设「太和日化城」项目能否成功',
    'QM-031': '准备购买太和日化城的商位，不知将来前景如何，能否获利',
    'QM-032': '求测蛋糕做不成的原因',
}
for cid in KW_IDS + FALLBACK_IDS:
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
    if cid != 'QM-029':
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
    if c.get('note'):
        note += f"；台账注记：{c['note']}"
    if cid in FALLBACK_IDS:
        note += ('；本例为石建国定额不足之跨源递补例（增补件 §二规则②，开悟全合余例'
                 '登记序首例），逐件登记于构建报告与封存日志')
    golds[cid] = {'id': cid, 'master_prediction': c['master_assertion'],
                  'outcome_record': c['outcome'], 'tradition': 'qimen',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': cards[cid]['provenance'],
                  'license_status': LICENSE_MODERN, 'redistributable': False,
                  'editor_note': '断语逐字核验：台账转录逐字、无摘写/省略标记'
                                 '（断语无「……」类缺口），照台账；本席未另读页图，'
                                 '逐字性以台账视觉转录口径为准，登记备主持复核。'}
    strip_register[cid] = ['topic/anchor_status/contamination_pre/separable/'
                           'transcription/dedup/master_assertion/outcome'
                           '（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('context←input_side 盘面之前段逐字；anchors.board_verbatim'
                                '←input_side 盘面段逐字（QM-028 三局盘面全载，partition 于'
                                '第一局盘面标记）；question←input_side 原文子串（断言验；'
                                'QM-029 例外为组写、原文未逐字引问句，口径在此登记）；'
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
    # 卡面引节名时略去篇名（承 holdout22–24 处置口径），金标 provenance 仍载全节名。
    section_card = src['section'].replace('分類占斷篇', '')
    deletion_register.append({
        'id': cid, 'class': '书目信息性字样略去（篇名含一级标记字，承 holdout22–24 口径）',
        'fields': ['setting', 'provenance'],
        'deleted_verbatim': '分類占斷篇',
        'before_section': src['section'], 'after_section': section_card,
        'gold_provenance_unchanged': True})
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
                                '「分類占斷篇」：含内容级标记字样、属书目信息，处置登记于'
                                ' deletion_register；金标 provenance 载全节名）；anchors←'
                                'cast_time_verbatim＋board/boards 全载逐字')

# ---------- 石建国 QM 2 例（奇门；定额 3 实取 2，差额开悟递补见 selection_register） ----------
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

# ---------- GSZ 11 例（六爻，承 holdout22–24 体例） ----------
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
                                '（台账无 context 原文，承 holdout22–24 先例）；'
                                'setting/provenance←台账 source 逐字；anchors←asked_at＋'
                                'input_fields.chart 全列逐字')

assert set(cards) == set(ORDER) and set(golds) == set(ORDER)
assert all(eligibility[c]['pass'] for c in ORDER)

# ---------- 建卡卫生删除两类扫描（question 字段逐例核查，登记） ----------
hygiene_scan = {}
for cid in ORDER:
    q = cards[cid]['question']
    hygiene_scan[cid] = {
        'editorial_apparatus_hits': [s for s in ('求测例', '求測例', '求测例题', '求測例題')
                                     if s in q],
        'note': '「求测例/求测例题」类编辑装置残段：question 尾部逐字核查；'
                '双人例第二人无关结局字样：经语义级逐卡通读核查（结论登记于封存日志 §四），'
                '本字段只登记字面扫描'}
    assert not hygiene_scan[cid]['editorial_apparatus_hits'], cid
deletion_register.append({
    'class': '「求测例/求测例题」类编辑装置残段删除', 'matched_cases': [],
    'deleted_count': 0,
    'note': '入选 27 例 question 逐例字面扫描零匹配，无删除件'})
deletion_register.append({
    'class': '双人例 question 中与所问无关之第二人结局字样删除', 'matched_cases': [],
    'deleted_count': 0,
    'note': '入选例中双人/合伙面例（QM-310 合伙投资、QM-027/028 同一求测人续例）question '
            '均只及所问之事本身，无第二人无关结局字样，经语义级通读核查，无删除件'})

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
    assert not hits_mp, (cid, hits_mp[:5])

# ---------- 扫描②：内容级标记＋字段名黑名单（R42 PREREG §5） ----------
scan_markers = {}
for cid in ORDER:
    ch = scan_content(cards[cid])
    fh = scan_field_names(cards[cid])
    scan_markers[cid] = {'content_hits': ch, 'fieldname_hits': fh}
    assert not ch and not fh, (cid, ch, fh)

# ---------- 构成与限度断言 ----------
SOURCE_OF = {}
for cid in ORDER:
    if cid.startswith('DS-'):
        SOURCE_OF[cid] = '段建业《段氏理象学》'
    elif cid in KW_IDS + FALLBACK_IDS:
        SOURCE_OF[cid] = '张志春《开悟之门》'
    elif cid in QW_IDS:
        SOURCE_OF[cid] = '刘文元《奇门启悟》'
    elif cid in SG_IDS:
        SOURCE_OF[cid] = '石建国《奇门遁甲最新实例解析》'
    else:
        SOURCE_OF[cid] = '王虎应《六爻卦例说真》'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)
assert len(ORDER) == 27
assert trad_counts == {'bazi': 6, 'qimen': 10, 'liuyao': 11}, trad_counts
assert max(trad_counts.values()) <= 13, trad_counts
assert max(src_counts.values()) <= 13, src_counts
assert 27 - trad_counts['liuyao'] >= 13
assert len(src_counts) >= 2  # 多源构成（五源）
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
    assert not mp_hits, (cid, mp_hits[:3])
    assert not scan_content(read_cards[cid]) and not scan_field_names(read_cards[cid]), cid
    assert not banned_key_scan(read_cards[cid]), cid
    assert list(read_cards[cid].keys()) == INPUT_FIELDS, cid
    reread[cid] = {'outcome_hits': oc_hits, 'master_prediction_hits': mp_hits,
                   'marker_hits': 0, 'banned_key_hits': 0, 'pass': True}

# ---------- 金标 SHA-256（构建脚本 hashlib 输出） ----------
sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
gold_bytes = os.path.getsize(gold_path)

# ---------- 快照：封存时点活 method 全量复制＋逐件 SHA 清单 ----------
SNAP_DIR = os.path.join(R80, 'kb-snapshot-holdout25')
if os.path.exists(SNAP_DIR):
    shutil.rmtree(SNAP_DIR)
shutil.copytree(os.path.join(BASE, 'method'), SNAP_DIR)
# method/ 根下 METHOD-INTEGRATION-*.md 为集成登记件、非快照内容件（快照 21 文件口径
# 承历轮），自快照排除并逐件登记（与 runs/round80/kb-snapshot 口径一致）
SNAP_EXCLUDED = []
for _name in ('METHOD-INTEGRATION-r78.md', 'METHOD-INTEGRATION-r80.md'):
    _extra = os.path.join(SNAP_DIR, _name)
    if os.path.exists(_extra):
        os.remove(_extra)
        SNAP_EXCLUDED.append(_name)
assert SNAP_EXCLUDED == ['METHOD-INTEGRATION-r78.md', 'METHOD-INTEGRATION-r80.md'], SNAP_EXCLUDED
snap_entries = []
for root, dirs, files in os.walk(SNAP_DIR):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, SNAP_DIR)
        snap_entries.append((rel, hashlib.sha256(open(p, 'rb').read()).hexdigest()))
SNAP_SHA_PATH = os.path.join(R80, 'kb-snapshot-holdout25-sha256.txt')
with open(SNAP_SHA_PATH, 'w', encoding='utf-8') as f:
    for rel, h in snap_entries:
        f.write(f'{h}  {rel}\n')
snap_list_sha = hashlib.sha256(open(SNAP_SHA_PATH, 'rb').read()).hexdigest()
assert len(snap_entries) == 21, len(snap_entries)
# 快照含第八节核验：calibration 第八节标题在盘
cal_text = open(os.path.join(SNAP_DIR, 'references/calibration.md'), encoding='utf-8').read()
assert '## 八、做功主线与功量核算核（R80 干预 R80-REV1' in cal_text
# 与 R80 开轮快照（runs/round80/kb-snapshot）逐件比对登记（预期差异恰为集成文件集）
open_snap = os.path.join(R80, 'kb-snapshot')
diff_files = []
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
assert diff_files == ['SKILL.md', 'references/calibration.md'], diff_files

report = {
    'round': 80, 'set': 'holdout25', 'built_by': '组集封存席（R80）',
    'ruling': 'runs/round80/PREREG-ADDENDUM-r80.md（唯一授权文本）；主预注册 PREREG.md §4/§7',
    'T': 27, 'order': ORDER,
    'selection_register': selection_register,
    'leak_hold_list': leak_hold,
    'leak_flag_list': leak_flags,
    'liuyao_five_element_recheck': liuyao_check,
    'composition_assertions': composition_assertions,
    'eligibility_assertions': eligibility,
    'eligibility_all_pass': True,
    'zero_reuse_recheck': {
        'sources': used_sources,
        'method': '只对 id 集（dev9 基线键集＋inputs-dev9/10/11/12 与 inputs 目录文件名、'
                  'phase2 splits2 holdout2、holdout3–24 各 test_gold.jsonl 仅取 id 字段、'
                  'holdout2–24 inputs 与 *-inputs 目录文件名、顶层 inputs6–10 目录文件名）；'
                  '未打开任何已封存集金标正文做内容比对',
        'selected_hit_count': 0, 'selected_hits': reuse_hits},
    'input_field_whitelist': INPUT_FIELDS,
    'input_field_whitelist_basis': 'holdout24/inputs/DS-019.json 实读字段集（开工对齐断言通过）',
    'strip_register': strip_register,
    'field_mapping_notes': field_mapping_notes,
    'deletion_register': deletion_register,
    'hygiene_question_scan': hygiene_scan,
    'gold_gap_scan': gap_register,
    'gold_supplement': SUPPLEMENT,
    'gold_supplement_count': 0,
    'gold_supplement_note': '27 例断语逐字核验无「……」类缺口、照台账逐字入标，补录 0 例；'
                            'DS-030、QM-208 结局内「……」为原书叙事/引语内省略字样'
                            '（台账逐字原文），非台账摘录缺口，登记备核',
    'scan1_verbatim_fragment': {
        'method': '每例 master_prediction 与 outcome_record 的特征片段（标点分句整句'
                  '（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描；'
                  '结局片段与断语片段全 27 例零命中（硬断言，本集无测字段、无分类例外）',
        'per_case': scan1},
    'scan_marker_selfcheck': {
        'method': 'R42 PREREG §5 内容级一级/二级标记＋字段名黑名单＋禁用键集对 27 张输入卡'
                  '全字段递归扫描（构建脚本内断言道）',
        'per_case': scan_markers,
        'total_hits': sum(len(v['content_hits']) + len(v['fieldname_hits'])
                          for v in scan_markers.values())},
    'scan_reread_selfcheck': {
        'method': '落盘后逐卡回读：对盘上 27 卡重行片段扫描＋标记扫描＋禁用键扫描＋字段白名单核，全过',
        'per_case': reread},
    'scan2_independent_rescan': '由独立复扫脚本 scan_holdout25_r80.py 执行，结果另行登记于封存日志',
    'scan3_host_rescan': '主持验封道，非本席执行——留位',
    'gold_sha256_hashlib': sha_lib,
    'gold_bytes': gold_bytes,
    'card_bytes': card_bytes,
    'card_bytes_total': sum(card_bytes.values()),
    'kb_snapshot': {'dir': 'runs/round80/kb-snapshot-holdout25/',
                    'excluded_non_snapshot_files': SNAP_EXCLUDED,
                    'file_count': len(snap_entries),
                    'sha256_list': 'runs/round80/kb-snapshot-holdout25-sha256.txt',
                    'sha256_list_sha256': snap_list_sha,
                    'files': [rel for rel, _ in snap_entries],
                    'contains_calibration_section8': True,
                    'diff_vs_round80_opening_snapshot': diff_files},
    'outputs_written': [f'holdout25/inputs/{c}.json' for c in ORDER] +
                       ['holdout25/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 27, 'order': ORDER,
                  'used_union_total': len(used_union),
                  'snapshot_files': len(snap_entries),
                  'diff_vs_opening': diff_files,
                  'gold_sha256_hashlib': sha_lib, 'gold_bytes': gold_bytes,
                  'card_bytes_total': sum(card_bytes.values())},
                 ensure_ascii=False))
