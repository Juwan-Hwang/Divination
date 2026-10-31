#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R83 组集封存席：按 PREREG-ADDENDUM-r83.md 组建并封存 holdout28（T＝27）。

构成（增补件 §一写死）：八字 DS 13（DS-050–062）／奇门启悟 QM 2（QM-210、
QM-211）／奇门旧池 QM 1（QM-010）／六爻 GSZ 6（GSZ-091、092、093、098、
099、100，建卡口径五要素复核）／六爻 WHY 一轮 5（WHY-012、016、022、
023、024）。
递补链（增补件 §二）：DS 段 DS-063；QM 段无递补（任一例不过先查原文补正、
不可者退出 T 减 1，不得跨段填充）；GSZ 段 GSZ-101、103、104、105、107、
108、109、110；WHY 段 WHY-025、026、027、028、031、032、033、034（其后
一轮余例顺延，再竭入二轮 WHY-080 起）。DS 实成 <10（非六爻 <13）组集不
成立停建。本轮预定 27 例资格断言若全过则递补不触发，逐件登记。
零复用：已用并集盘上实算（口径照 PREREG §4：dev 池＋phase2 holdout2＋
holdout3–27 金标 id＋holdout inputs 卡 id＋顶层 inputs6–10 卡 id），断言
并集＝1139；选例逐 id 零命中。
金标补录（6 例，回原书逐字补录后封，逐件登记于构建报告 gold_supplement）：
- WHY-012/016/022/023/024：台账未单列断语字段（master_prediction 缺位），
  回《六爻分类占验技法》原书页图逐字补录各例〔判斷〕段（印刷 p23／p34／
  pp.44-46／p46（跨 p47）／pp.47-48；扫描本 visual 转录，页图件存
  runs/round83/why-pages-h28/，只留本轮目录未跟踪、不入封存产物）。
- WHY 五例结局经回原书应验段逐例核对与台账一致（WHY-024 应验段在 p48），
  无对调订正件（OUTCOME_SWAP 空）。
- DS-060：台账摘录第二段段内含「……」省略标记一处，回《段氏理象学》原书
  （印刷pp.218-219／PDF242-243）逐字补入省略跨度后封；QWU/QMOLD/GSZ 三段与
  DS 余 12 例台账断语经缺口扫描「……」零命中。
扫描：①逐字片段扫描（结局片段与断语片段全例零命中硬断言）；
②R42 PREREG §5 内容级标记＋字段名黑名单＋禁用键集递归扫描零命中硬断言；
③落盘后逐卡回读复扫。金标 SHA-256 以构建脚本 hashlib 输出记录（封存席
另以独立 sha256sum 复算双读，主持再做第三读）。
快照：自现行活 method/ 复制 runs/round83/kb-snapshot-holdout28＋SHA 清单
（封存时点锚定，含 calibration 第八节现行形态、第九节失效存档、第十节
R82-REV1 与第十一节 R83-REV1 及 SKILL (s) 指针），METHOD-*.md 为登记件、
非快照内容件，自快照排除并登记；与 runs/round83/kb-snapshot（R83 平台
快照）逐件比对登记（预期差异恰为 calibration.md／SKILL.md 两件，即
R83-REV1 集成差异）。
只建卡与封存：不作断、不评分、不开封、不做 git 操作。
适配自 holdout27 构建脚本（runs/round82/build_holdout27_r82.py），逐处定点
改写；脚本内 round82/holdout27 字样仅存于「承先例/范本」实指引用与字段
白名单对齐基准（holdout27 卡实读）。
"""
import json, hashlib, os, re, shutil
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'
R83 = os.path.join(BASE, 'runs/round83')
DIG76 = os.path.join(BASE, 'runs/round76/digestion')
OUT_DIR = os.path.join(BASE, 'holdout28')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R83, 'build-holdout28-report-r83.json')

LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '断曰', '正议', '正議', '验语', '驗語',
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
# 字段白名单以 holdout27 任一卡实读字段集对齐（封存体例照 holdout27 定式）
h27_card = load_json(os.path.join(BASE, 'holdout27/inputs/DS-040.json'))
assert list(h27_card.keys()) == INPUT_FIELDS, list(h27_card.keys())

# ---------- 台账载入 ----------
ds_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-duanshi-r76.json'))
qwu_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-qiwu-r76.json'))
qmo_mining = load_json(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-qimen-r56.json'))
qmo_review = load_json(os.path.join(BASE, 'runs/round58/digestion/QM-REVIEW-r58.json'))
gsz_mining = load_json(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
why_mining = load_json(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json'))

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
for i in range(3, 28):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    s = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip():
                s.add(json.loads(line)['id'])
    gold_per_set[f'holdout{i}'] = len(s)
    gold_ids |= s
used_sources['holdout3_27_gold_ids'] = len(gold_ids)
used_sources['gold_per_set'] = gold_per_set

input_ids = set()
for i in range(2, 28):
    for dname in (f'holdout{i}/inputs', f'holdout{i}-inputs'):
        d = os.path.join(BASE, dname)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'):
                    input_ids.add(fn[:-5])
used_sources['holdout2_27_input_card_ids'] = len(input_ids)
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
assert len(used_union) == 1139, len(used_union)  # 与主持开轮实算（PREREG 开轮登记）一致
h27_ids = set()
for line in open(os.path.join(BASE, 'holdout27/test_gold.jsonl'), encoding='utf-8'):
    if line.strip():
        h27_ids.add(json.loads(line)['id'])
assert len(h27_ids) == 27 and h27_ids <= used_union

selection_register = {}
leak_hold = []   # 排除登记（未入选，承既有裁处）
leak_flags = []  # 入选标旗（照建不动、卡面原样保留，提请主持裁处）
fallback_log = []  # 递补登记（逐件）

# ---------- 预定选例（增补件 §一写死）与递补链（§二） ----------
DS_WANT = [f'DS-{n:03d}' for n in range(50, 63)]
DS_FALLBACK = ['DS-063']
QWU_WANT = ['QM-210', 'QM-211']
QMO_WANT = ['QM-010']
GSZ_WANT = ['GSZ-091', 'GSZ-092', 'GSZ-093', 'GSZ-098', 'GSZ-099', 'GSZ-100']
GSZ_FALLBACK = ['GSZ-101', 'GSZ-103', 'GSZ-104', 'GSZ-105',
                'GSZ-107', 'GSZ-108', 'GSZ-109', 'GSZ-110']
WHY_WANT = ['WHY-012', 'WHY-016', 'WHY-022', 'WHY-023', 'WHY-024']
WHY_FALLBACK = ['WHY-025', 'WHY-026', 'WHY-027', 'WHY-028',
                'WHY-031', 'WHY-032', 'WHY-033', 'WHY-034']
WANT_ALL = DS_WANT + QWU_WANT + QMO_WANT + GSZ_WANT + WHY_WANT
assert len(WANT_ALL) == 27 and len(set(WANT_ALL)) == 27
reuse_hits = [cid for cid in WANT_ALL + DS_FALLBACK + GSZ_FALLBACK + WHY_FALLBACK
              if cid in used_union]
assert not reuse_hits, f'写定名单/递补链与已用并集（1139）相交：{reuse_hits}'

# ---------- DS 13 资格断言 ----------
ds_by = {r['case_id']: r for r in ds_mining['records']}


def ds_qual(cid):
    r = ds_by[cid]
    return (r['eligible_net'] is True and r['anchor_status'] == 'present'
            and r['contamination_pre'] == 'low'
            and all(str(v).startswith('pass') for v in r['filters'].values())
            and r['master_assertion'].strip() and r['outcome'].strip())


DS_SEL = []
for cid in DS_WANT:
    if ds_qual(cid):
        DS_SEL.append(cid)
    else:
        fallback_log.append({'segment': 'DS', 'failed': cid, 'action': '资格断言不过，查递补链'})
for cid in DS_FALLBACK:
    if len(DS_SEL) >= 13:
        break
    if ds_qual(cid):
        DS_SEL.append(cid)
        fallback_log.append({'segment': 'DS', 'used_fallback': cid})
assert len(DS_SEL) == 13, DS_SEL
pillars_sel = [ds_by[c]['input_side']['pillars_verbatim'] for c in DS_SEL]
assert len(set(pillars_sel)) == 13  # 同造（同四柱）组内零重复
selection_register['DS'] = {
    'rule': '增补件 §一写死 DS-050–062 按台账序；逐例 eligible_net∧present∧low∧'
            'filters 四项全 pass∧断语/结局非空断言；入选 13 例四柱互异',
    'selected': DS_SEL, 'fallback_triggered': any(x['segment'] == 'DS' for x in fallback_log),
    'fallback_chain': DS_FALLBACK}

# ---------- 启悟 QM 2 资格断言（无递补） ----------
qwu_by = {c['case_id']: c for c in qwu_mining['cases']}


def qwu_qual(cid):
    c = qwu_by[cid]
    return (c['anchor_status'] == 'present' and c['contamination_pre'] == 'low'
            and c['separable'] is True
            and c['master_assertion'].strip() and c['outcome'].strip())


QWU_SEL = []
for cid in QWU_WANT:
    assert qwu_qual(cid), cid  # QM 段无递补：不过即停建回主持（增补件 §二）
    QWU_SEL.append(cid)
selection_register['QWU'] = {
    'rule': '增补件 §一写死启悟 QM-210、QM-211；逐例 anchor present∧contamination '
            'low∧separable∧断语/结局非空断言；QM 段无递补',
    'selected': QWU_SEL, 'fallback_triggered': False, 'fallback_chain': []}

# ---------- 旧池 QM-010 资格断言（无递补） ----------
qmo_by = {c['provisional_id']: c for c in qmo_mining['cases']}
qmo_rev_by = {c['provisional_id']: c for c in qmo_review['cases']}


def qmo_qual(cid):
    c = qmo_by[cid]
    rv = qmo_rev_by[cid]
    return (rv['eligible_optional'] is True and rv['anchor_reviewed'] == 'present'
            and rv['pollution_reviewed'] == 'low'
            and c['anchor_presence'] == 'present' and c['pollution'] == 'low'
            and c['master_prediction_verbatim'].strip() and c['outcome_record'].strip())


QMO_SEL = []
for cid in QMO_WANT:
    assert qmo_qual(cid), cid  # QM 段无递补：不过即停建回主持（增补件 §二）
    QMO_SEL.append(cid)
selection_register['QMO'] = {
    'rule': '增补件 §一写死旧池 QM-010；台账 anchor present∧pollution low∧复核件 '
            'QM-REVIEW-r58 eligible_optional=true∧anchor_reviewed present∧'
            'pollution_reviewed low∧断语/结局非空断言；QM 段无递补',
    'selected': QMO_SEL, 'fallback_triggered': False, 'fallback_chain': []}

# ---------- GSZ 6 资格断言＋建卡口径五要素复核 ----------
gsz_by = {e['provisional_id']: e for e in gsz_mining['entries']}
gsz_card_list = set(gsz_mining['counts']['net_eligible_A_low_present'])
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


def gsz_qual(cid):
    e = gsz_by[cid]
    base_ok = (e['grade'] == 'A' and e['pollution'] == 'low'
               and e['anchor_presence'] == 'present' and e['eligible_net'] is True
               and cid in gsz_card_list
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
    return ok


GSZ_SEL = []
for cid in GSZ_WANT:
    if gsz_qual(cid):
        GSZ_SEL.append(cid)
    else:
        fallback_log.append({'segment': 'GSZ', 'failed': cid, 'action': '资格断言不过，查递补链'})
for cid in GSZ_FALLBACK:
    if len(GSZ_SEL) >= 6:
        break
    if gsz_qual(cid):
        GSZ_SEL.append(cid)
        fallback_log.append({'segment': 'GSZ', 'used_fallback': cid})
assert len(GSZ_SEL) == 6, GSZ_SEL
selection_register['GSZ'] = {
    'rule': '增补件 §一写死 GSZ 6 例按台账序；逐例 grade A∧low∧present∧eligible_net∧'
            '建卡口径名单成员∧断语/结局非空∧回原书文字层五要素复核全在场断言',
    'selected': GSZ_SEL, 'fallback_triggered': any(x['segment'] == 'GSZ' for x in fallback_log),
    'fallback_chain': GSZ_FALLBACK}

# ---------- WHY 一轮 5 资格断言 ----------
why_by = {e['provisional_id']: e for e in why_mining['entries']}
why_net = why_mining['counts']['net_eligible_A_low_present']


def why_qual(cid):
    e = why_by[cid]
    return (cid in why_net and e['pollution'] == 'low'
            and e['anchor_presence'] == 'present' and not e['anchor_missing']
            and e['outcome_record'].strip())


WHY_SEL = []
for cid in WHY_WANT:
    if why_qual(cid):
        WHY_SEL.append(cid)
    else:
        fallback_log.append({'segment': 'WHY', 'failed': cid, 'action': '资格断言不过，查递补链'})
WHY_SUPPLEMENT_IDS = {'WHY-012', 'WHY-016', 'WHY-022', 'WHY-023', 'WHY-024'}
# 补录定义在本文后段 SUPPLEMENT（键集断言与本集一致）；递补例断语未补录者不得封存
for cid in WHY_FALLBACK:
    if len(WHY_SEL) >= 5:
        break
    if why_qual(cid):
        assert cid in WHY_SUPPLEMENT_IDS, f'WHY 递补例 {cid} 断语未补录，不得封存'
        WHY_SEL.append(cid)
        fallback_log.append({'segment': 'WHY', 'used_fallback': cid})
assert len(WHY_SEL) == 5, WHY_SEL
selection_register['WHY'] = {
    'rule': '增补件 §一写死 WHY 一轮 5 例按台账序；逐例 counts 净入账名单成员∧'
            'low∧present∧anchor_missing 空∧结局非空断言；断语台账未单列字段，'
            '回原书逐字补录（见 gold_supplement）',
    'selected': WHY_SEL, 'fallback_triggered': any(x['segment'] == 'WHY' for x in fallback_log),
    'fallback_chain': WHY_FALLBACK}

ORDER = DS_SEL + QWU_SEL + QMO_SEL + GSZ_SEL + WHY_SEL
assert len(ORDER) == 27 and len(set(ORDER)) == 27
assert not [c for c in ORDER if c in used_union]
assert not [c for c in ORDER if c in h27_ids]
non_liuyao_n = len([c for c in ORDER if not c.startswith(('GSZ-', 'WHY-'))])
assert non_liuyao_n == 16 and len(DS_SEL) == 13, (non_liuyao_n, len(DS_SEL))

# ---------- 断语缺口扫描与补录（回原书逐字补录后封） ----------
gap_register = {}
for cid in ORDER:
    if cid in ds_by:
        mp = ds_by[cid]['master_assertion']
    elif cid in qwu_by:
        mp = qwu_by[cid]['master_assertion']
    elif cid in qmo_by:
        mp = qmo_by[cid]['master_prediction_verbatim']
    elif cid in gsz_by:
        mp = gsz_by[cid]['master_prediction']
    else:
        mp = ''  # WHY 台账未单列断语字段，缺口即整段，逐例补录
    gap_register[cid] = {'mp_gap': '……' in mp, 'mp_missing_field': cid in why_by}
# 缺口登记：DS-060 台账摘录段内含「……」一处（段内省略标记），回原书逐字补入
# 该省略跨度后封（见 SUPPLEMENT['DS-060']）；其余 26 例缺口扫描零命中。
assert [k for k, v in gap_register.items() if v['mp_gap']] == ['DS-060'], \
    [k for k, v in gap_register.items() if v['mp_gap']]

SUPPLEMENT = {
    'DS-060': {
        'master_prediction':
            '该是个公安局的官员，对方说不是。又断那一定当过兵，对方说是当过兵。'
            '我说，那他应该是银行的官员／这个命癸未运走坏了，反了局，2008戊子年'
            '一定遇到大麻烦，子卯相破，杀星被破，整个局反了。癸水财星代表丑土'
            '跑了，犯了经济问题，不是个丢官罢职的事，应该有牢狱之灾！／癸水这个'
            '财透出，被劫了，癸水的数，六数，不是六百万就是六千万。贪污就是'
            '六百万，挪用公款就是六千万。',
        'source_anchor': '《段氏理象学》附录三十二、断例几则·二（印刷pp.218-219，扫描本PDF第242-243页）',
        'note': '台账摘录第二段段内含「……」省略标记一处；本席回原书逐字补入省略跨度'
                '「癸水财星代表丑土跑了，犯了经济问题，不是个丢官罢职的事，」，余段'
                '照台账摘录逐字；transcription=visual（200dpi 渲染页读图）'},
    'WHY-012': {
        'master_prediction':
            '〔判斷〕卦中有動爻，從動爻入手判斷。卦中子孫發動化官鬼，子孫主晴，'
            '官鬼主陰，乃是晴轉陰之象。但是子孫不得日月生扶，不能言旺。而官鬼得'
            '日月幫比，比子孫要旺得多，是否是晴天見多雲？參考第二天的干支，次日'
            '為庚寅日，官鬼受剋子孫得助，應為晴天，有浮雲。',
        'source_anchor': '《六爻分类占验技法》第一章「被測日辰」例二（印刷p23，扫描本PDF第12页左叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段；'
                'transcription=visual（200dpi 渲染页读图，繁体照原书）'},
    'WHY-016': {
        'master_prediction':
            '〔判斷〕兄弟辰土臨螣蛇發動，乃是地震的信息。但是兄弟丑土被日月剋制，'
            '且動而化退，休囚無氣，即使有地震也不會大。地震發生的時間當以退神'
            '定應期，故斷丑月有小的地震。',
        'source_anchor': '《六爻分类占验技法》第二章 例四（印刷p34，扫描本PDF第18页右叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段；'
                'transcription=visual（200dpi 渲染页读图，繁体照原书）'},
    'WHY-022': {
        'master_prediction':
            '〔判斷〕以官鬼為用神，看官鬼的動靜。此卦官鬼戌土發動，必有水災。'
            '官鬼得月建比扶旺相，又在坎宮，很明顯為水災的信息，而且很大。官鬼'
            '戌土動化父母申金，申金為土之長生之地，父母主雨，長生為產生之意，'
            '卦中反映出因下雨會帶來水災。官鬼戌土化出申金空亡，申月出空，申月'
            '必會發生水災。',
        'source_anchor': '《六爻分类占验技法》第三章 水灾例一（印刷pp.44-46，例文与卦图在p45、〔判斷〕在p46，扫描本PDF第23页左叶与第24页右叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段；'
                'transcription=visual（200dpi 渲染页读图，繁体照原书）'},
    'WHY-023': {
        'master_prediction':
            '〔判斷〕以官鬼為用神。卦中官鬼午火兩重發動，今年南方有水災無疑。'
            '官鬼午火得月建巳火比扶為旺相，有水災必大。官鬼午火發動，動而逢值'
            '逢合，水災必在午月發生。',
        'source_anchor': '《六爻分类占验技法》第三章 水灾例二（印刷p46，〔判斷〕跨p46-47，扫描本PDF第24页右叶至左叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段（跨页连续）；'
                'transcription=visual（200dpi 渲染页读图，繁体照原书）'},
    'WHY-024': {
        'master_prediction':
            '〔判斷〕以官鬼為用神。卦中官鬼申金得日月幫扶為旺相。此為洪水凶猛'
            '正是險情萬分的信息。但是官鬼元神妻財戌土發動化退神，這是洪水將會'
            '退去的信息。子孫為剋官鬼之六親，也可以理解為與洪水作戰的人。同時'
            '子孫也為喜悅解憂之神。子孫持世，乃是洪水退卻皆大歡喜的信息。但是'
            '子孫休囚，元神兄弟寅木月破，不能剋制官鬼，洪水現在很難退去。元神'
            '月破，出月不破，只有到了酉月洪水才能退去。九月八日進入酉月，因此'
            '我以酉月的第一個寅日即丙寅日（九月十六日）為洪水退去的應期。',
        'source_anchor': '《六爻分类占验技法》第三章 水灾例三（印刷pp.47-48，〔判斷〕跨p47-48、应验段在p48，扫描本PDF第24页左叶至第25页右叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段（跨页连续，'
                '含应期段）；transcription=visual（200dpi 渲染页读图，繁体照原书）'},
}
assert {k for k in SUPPLEMENT if k.startswith('WHY-')} == WHY_SUPPLEMENT_IDS == set(WHY_SEL), \
    (set(SUPPLEMENT), WHY_SEL)
assert {k for k in SUPPLEMENT if k.startswith('DS-')} == {'DS-060'}
# 结局对调订正：本轮无（WHY 五例结局经回原书应验段逐例核对与台账一致）
OUTCOME_SWAP = {}

# ---------- 泄题标旗（入选、照建不动、卡面原样保留） ----------
# 入选标旗：经逐卡语义通读（见封存日志）本轮无入选标旗件，leak_flags 留空。
leak_hold.append({'id': 'ZCB-003', 'source': '《字触补》',
                  'issue': '主持裁处维持排除（承 PREREG §4）；本轮构成无测字段额、未入选',
                  'status': '维持排除，只登记'})

cards, golds = {}, {}
eligibility, strip_register, field_mapping_notes = {}, {}, {}
deletion_register = []

LICENSE_MODERN = '现代版权文本（扫描本），内部研究用'
PROV_TAIL = '用户经学校图书馆提供；redistributable=false'

# ---------- DS 13 例（八字） ----------
for cid in DS_SEL:
    r = ds_by[cid]
    ok = ds_qual(cid)
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
    gold = {'id': cid,
            'master_prediction': SUPPLEMENT[cid]['master_prediction'] if cid in SUPPLEMENT
                                 else r['master_assertion'],
            'outcome_record': r['outcome'], 'tradition': 'bazi',
            'pollution': 'low', 'grade': 'A', 'grade_note': note,
            'provenance': cards[cid]['provenance'],
            'license_status': cards[cid]['license_status'],
            'redistributable': False}
    if cid in SUPPLEMENT:
        gold['editor_note'] = (f"断语经本轮封存席回原书逐字补录：{SUPPLEMENT[cid]['source_anchor']}；"
                              f"{SUPPLEMENT[cid]['note']}")
    golds[cid] = gold
    strip_register[cid] = ['anchor_status/anchor_note/contamination_pre/'
                           'contamination_note/separable/transcription/dedup/filters/'
                           'eligible_net/verdict_note/composition_type/'
                           'master_assertion/outcome（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject←input_side.subject 逐字；anchors←input_side '
                                'pillars/pillars_verbatim/gender 逐字；setting←source 逐字；'
                                'context/question 为组写（台账无该二字段，组写口径在此登记）')

# ---------- 启悟 QM 2 例（奇门；承 holdout22–25 启悟建卡体例） ----------
for cid in QWU_SEL:
    c = qwu_by[cid]
    ok = qwu_qual(cid)
    eligibility[cid] = {'anchor_status': c['anchor_status'],
                        'contamination': c['contamination_pre'],
                        'separable': c['separable'], 'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-qiwu-r76.json 台账逐字'}
    assert ok, cid
    src, inf = c['source'], c['input_side']
    # 篇首「分類占斷篇」为书目篇名、含标记集字面「占斷」，承 holdout22–25 启悟
    # 建卡先例（QM-203/205/207/209 卡 setting/provenance 均自章次起）于卡面省略，
    # 逐件登记于 deletion_register；台账 section 原文全量保留于构建报告资格登记。
    section_card = src['section'].removeprefix('分類占斷篇')
    assert section_card != src['section'], cid
    context_card = inf['context']
    if cid == 'QM-211':
        # 台账 context 尾部括注为台账编辑注记（含「斷語」「金標不採，見 notes」字样），
        # 非原书本文，卡面删除并逐字登记于 deletion_register；事实内核（覆测为六壬、
        # 其应期不入本局金标）由台账 notes 全量载入金标 grade_note。
        anno = ('（2000 年 10 月 8 日潘氏姐妹再來問何日能還款，劉改用大六壬起課覆測'
                '——其應期斷語不屬本奇門局，金標不採，見 notes。）')
        assert anno in context_card, cid
        context_card = context_card.replace(anno, '')
    cards[cid] = {
        'id': cid, 'tradition': 'qimen',
        'subject': inf['querent'],
        'context': context_card,
        'question': inf['question'],
        'setting': f"{src['book']}（{src['author']}著）·{section_card}；起局时间：{inf['cast_time_verbatim']}",
        'provenance': f"{src['book']}（{src['author']}著，{src['publisher']}）·{section_card}，印刷页{src['printed_pages']}（PDF页{src['pdf_pages']}）；{PROV_TAIL}",
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': {'cast_time_verbatim': inf['cast_time_verbatim'],
                    'board': inf['board']},
    }
    note = (f"锚点 present；污染 low（{c['contamination_reason']}）；"
            f"转录：{c['transcription']}（{c['transcription_confidence']}）；"
            f"去重：{c['dedup']}")
    if c.get('notes'):
        note += f"；台账注记：{c['notes']}"
    golds[cid] = {'id': cid, 'master_prediction': c['master_assertion'],
                  'outcome_record': c['outcome'], 'tradition': 'qimen',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': cards[cid]['provenance'],
                  'license_status': LICENSE_MODERN, 'redistributable': False,
                  'editor_note': '断语逐字核验：台账转录逐字、无摘写/省略标记'
                                 '（断语无「……」类缺口），照台账；本席未另读页图，'
                                 '逐字性以台账视觉转录口径为准，登记备主持复核。'}
    strip_register[cid] = ['anchor_status/contamination_pre/contamination_reason/'
                           'separable/transcription/transcription_confidence/dedup/'
                           'notes/master_assertion/outcome'
                           '（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject←input_side.querent 逐字；context←input_side.context '
                                '逐字；question←input_side.question 逐字；anchors←'
                                'cast_time_verbatim＋board 逐字；setting←source.section（省'
                                '篇首「分類占斷篇」，承先例、登记于 deletion_register）＋'
                                'cast_time_verbatim 组写；provenance←source 各字段组写（section 同 setting 口径）')

# ---------- 旧池 QM-010（奇门；承 holdout21 旧池建卡体例） ----------
for cid in QMO_SEL:
    c = qmo_by[cid]
    rv = qmo_rev_by[cid]
    ok = qmo_qual(cid)
    eligibility[cid] = {'anchor_presence': c['anchor_presence'],
                        'pollution': c['pollution'],
                        'review_eligible_optional': rv['eligible_optional'],
                        'review_anchor': rv['anchor_reviewed'],
                        'review_pollution': rv['pollution_reviewed'],
                        'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-qimen-r56.json 台账逐字＋QM-REVIEW-r58.json 复核逐字'}
    assert ok, cid
    src, inf = c['source'], c['input_fields']
    cards[cid] = {
        'id': cid, 'tradition': 'qimen',
        'subject': inf['querent'],
        'context': inf['context'],
        'question': inf['question'],
        'setting': f"{src['book']}（{src['author']}著）·{src['section']}；起局时间：{inf['cast_time_verbatim']}",
        'provenance': f"{src['book']}（{src['author']}著，{src['publisher']}，{src['edition']}）·{src['section']}，印刷页{src['printed_pages']}；{PROV_TAIL}",
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': {'cast_time_verbatim': inf['cast_time_verbatim'],
                    'board': inf['board']},
    }
    note = (f"锚点复核：{rv['anchor_basis']}；污染复核：{rv['pollution_basis']}；"
            f"台账锚点注记：{c['anchor_note']}；台账污染：{c['pollution_reason']}；"
            f"去重：{c['dedup_check']}")
    if c.get('notes'):
        note += f"；台账注记：{c['notes']}"
    golds[cid] = {'id': cid, 'master_prediction': c['master_prediction_verbatim'],
                  'outcome_record': c['outcome_record'], 'tradition': 'qimen',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': cards[cid]['provenance'],
                  'license_status': LICENSE_MODERN, 'redistributable': False,
                  'editor_note': '断语逐字核验：台账 master_prediction_verbatim 逐字字段、'
                                 '无摘写/省略标记（断语无「……」类缺口），照台账；本席未另读'
                                 '页图，逐字性以台账视觉转录口径为准，登记备主持复核。'}
    strip_register[cid] = ['pollution/pollution_reason/anchor_presence/anchor_note/'
                           'dedup_check/notes/master_prediction_verbatim/outcome_record'
                           '（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject←input_fields.querent 逐字；context←input_fields.context '
                                '逐字；question←input_fields.question 逐字；anchors←'
                                'cast_time_verbatim＋board 逐字；setting←source.section＋'
                                'cast_time_verbatim 组写；provenance←source 各字段组写')

# ---------- GSZ 6 例（六爻，承 holdout27 体例） ----------
for cid in GSZ_SEL:
    e = gsz_by[cid]
    ok = gsz_qual(cid)
    eligibility[cid] = {'grade': e['grade'], 'pollution': e['pollution'],
                        'anchor_presence': e['anchor_presence'],
                        'eligible_net': e['eligible_net'],
                        'card_list_member': cid in gsz_card_list,
                        'five_elements_recheck': liuyao_check[cid]['elements'],
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
                                '（台账无 context 原文，承 holdout27 先例）；'
                                'setting/provenance←台账 source 逐字；anchors←asked_at＋'
                                'input_fields.chart 全列逐字')

# ---------- WHY 一轮 5 例（六爻，承 holdout27 建卡体例；断语回原书补录） ----------
for cid in WHY_SEL:
    e = why_by[cid]
    ok = why_qual(cid)
    eligibility[cid] = {'net_list_member': cid in why_net,
                        'pollution': e['pollution'],
                        'anchor_presence': e['anchor_presence'],
                        'anchor_missing': e['anchor_missing'],
                        'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-wanghuying-r56.json 台账逐字'}
    assert ok, cid
    inf = e['input_fields']
    chart = inf['chart']
    cards[cid] = {
        'id': cid, 'tradition': 'liuyao',
        'subject': e['subject'] if e['subject'] else '求测者（台账 subject 为空、原书未具名）',
        'context': f"占时：{inf['asked_at']}；《六爻分类占验技法》分类占验例",
        'question': inf['question'],
        'setting': f"{e['source']}",
        'provenance': f"{e['source']}；底本为用户经学校图书馆提供之扫描本，redistributable=false",
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': {'asked_at': inf['asked_at'],
                    'ben_gua': chart['ben_gua'],
                    'bian_gua': chart['bian_gua'],
                    'moving_lines': chart['moving_lines'],
                    'chart_lines_top_to_bottom': chart['chart_lines_top_to_bottom']},
    }
    note = ('锚点在场（卦名、变卦、动爻、世应、六亲纳支、月建日辰全列）；'
            '转录：visual（扫描本多模态读图转录）；现代案例书、名案污染已从严定级'
            '、本例判 low；')
    note += (f"断语经本轮封存席回原书逐字补录（{SUPPLEMENT[cid]['source_anchor']}），"
             f"见构建报告 gold_supplement；台账仅录应验情况、未单列断语字段。")
    golds[cid] = {'id': cid,
                  'master_prediction': SUPPLEMENT[cid]['master_prediction'],
                  'outcome_record': e['outcome_record'], 'tradition': 'liuyao',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note,
                  'provenance': cards[cid]['provenance'],
                  'license_status': LICENSE_MODERN, 'redistributable': False}
    strip_register[cid] = ['pollution/anchor_presence/anchor_missing/dedup_check/'
                           'transcription/outcome_type/outcome_record（台账管理与金标侧'
                           '字段，不入输入卡）；台账 input_fields 无 context/setting/'
                           'provenance 独立字段，context 由 asked_at＋书名组写、setting/'
                           'provenance 由台账 source 逐字承接，组写口径登记于构建报告']
    field_mapping_notes[cid] = ('question←input_fields.question；anchors←input_fields.chart '
                                '全列＋asked_at；setting/provenance←台账 source 逐字；'
                                'context←asked_at 与书名组写（台账无 context 原文）')

assert set(cards) == set(ORDER) and set(golds) == set(ORDER)
assert all(eligibility[c]['pass'] for c in ORDER)

# ---------- 建卡卫生：节题/问题中性化核查 ----------
hygiene_scan = {}
for cid in ORDER:
    q = cards[cid]['question']
    hygiene_scan[cid] = {
        'editorial_apparatus_hits': [s for s in ('求测例', '求測例', '求测例题', '求測例題')
                                     if s in q],
        'neutralization_rewrites': [],
        'note': '「求测例/求测例题」类编辑装置残段：question 逐例字面扫描；节题/问题含'
                '结局事实者须中性化并逐件登记——本轮经逐卡语义通读（见封存日志）无'
                '中性化改写件；双人例第二人无关结局字样：经语义级逐卡通读核查'}
    assert not hygiene_scan[cid]['editorial_apparatus_hits'], cid
deletion_register.append({
    'class': '节题/问题中性化改写（结局事实字样）', 'matched_cases': [],
    'deleted_count': 0, 'rewritten_count': 0,
    'note': '入选 27 例节题/问题逐例核查，无含结局事实须中性化者，无改写件'})
deletion_register.append({
    'class': '「求测例/求测例题」类编辑装置残段删除', 'matched_cases': [],
    'deleted_count': 0,
    'note': '入选 27 例 question 逐例字面扫描零匹配，无删除件'})
deletion_register.append({
    'class': '双人例 question 中与所问无关之第二人结局字样删除', 'matched_cases': [],
    'deleted_count': 0,
    'note': '入选例中涉他人面例（QM-211 妹妹转介借款人、GSZ/WHY 诸例代占或群体占）'
            'question 均只及所问之事本身，无第二人无关结局字样，经语义级通读核查，无删除件'})
deletion_register.append({
    'class': '台账编辑注记括注删除（QM-211 context 尾部括注）',
    'matched_cases': ['QM-211'], 'deleted_count': 1,
    'deleted_text': '（2000 年 10 月 8 日潘氏姐妹再來問何日能還款，劉改用大六壬起課覆測'
                    '——其應期斷語不屬本奇門局，金標不採，見 notes。）',
    'note': '该括注为台账编辑注记（含「斷語」「金標不採，見 notes」等管理字样），非原书'
            '本文，卡面删除；事实内核由台账 notes 全量载入金标 grade_note，不影响金标口径'})
deletion_register.append({
    'class': '书目篇名篇首省略（启悟 section 篇首「分類占斷篇」）',
    'matched_cases': ['QM-210', 'QM-211'], 'deleted_count': 2,
    'note': '台账 source.section 篇首「分類占斷篇」为本书篇名（含内容级标记集字面'
            '「占斷」），承 holdout22–25 启悟建卡先例（QM-203/205/207/209 卡均自章次起），'
            '卡面 setting/provenance 省略该篇首、自章次起录；台账原文全量保留于台账与'
            '本报告资格登记，非内容删改'})

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

# ---------- 构成与限度断言（增补件 §一/§二与 PREREG §4 写死值） ----------
SOURCE_OF = {}
for cid in ORDER:
    if cid.startswith('DS-'):
        SOURCE_OF[cid] = '段建业《段氏理象学》'
    elif cid in QWU_SEL:
        SOURCE_OF[cid] = '刘文元《奇门启悟》'
    elif cid in QMO_SEL:
        SOURCE_OF[cid] = '杜新会《奇门遁甲现代实例精解》'
    elif cid.startswith('GSZ-'):
        SOURCE_OF[cid] = '王虎应《六爻卦例说真》'
    else:
        SOURCE_OF[cid] = '王虎应《六爻分类占验技法》'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)
assert len(ORDER) == 27
assert trad_counts == {'bazi': 13, 'qimen': 3, 'liuyao': 11}, trad_counts
assert max(trad_counts.values()) <= 13, trad_counts  # 单体系 ≤50%（计数 ≤13）
assert max(src_counts.values()) <= 13, src_counts    # 单源 ≤50%（计数 ≤13）
assert 27 - trad_counts['liuyao'] >= 13              # 非六爻 ≥13
assert len(src_counts) >= 2                          # 多源构成（五源）
assert all(golds[c]['pollution'] == 'low' for c in ORDER)
assert not [c for c in ORDER if c in used_union]
composition_assertions = {
    'T': 27, 'by_tradition': dict(trad_counts), 'by_source': dict(src_counts),
    'max_single_tradition_share': max(trad_counts.values()) / 27,
    'max_single_source_share': max(src_counts.values()) / 27,
    'non_yijian': 27, 'non_liuyao': 27 - trad_counts['liuyao'],
    'source_count': len(src_counts), 'pollution_low': 27,
    'used_union_intersection': [], 'holdout27_intersection': [], 'all_pass': True}

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
read_cards = {}
for cid in ORDER:
    read_cards[cid] = load_json(os.path.join(IN_DIR, f'{cid}.json'))
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
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
SNAP_DIR = os.path.join(R83, 'kb-snapshot-holdout28')
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
        rel = os.path.relpath(p, SNAP_DIR)
        snap_entries.append((rel, hashlib.sha256(open(p, 'rb').read()).hexdigest()))
SNAP_SHA_PATH = os.path.join(R83, 'kb-snapshot-holdout28-sha256.txt')
with open(SNAP_SHA_PATH, 'w', encoding='utf-8') as f:
    for rel, h in snap_entries:
        f.write(f'{h}  {rel}\n')
snap_list_sha = hashlib.sha256(open(SNAP_SHA_PATH, 'rb').read()).hexdigest()
assert len(snap_entries) == 21, len(snap_entries)
cal_text = open(os.path.join(SNAP_DIR, 'references/calibration.md'), encoding='utf-8').read()
assert 'R83-REV1' in cal_text and 'R82-REV1' in cal_text and 'R80-REV1' in cal_text
cal_sec11_title = [ln for ln in cal_text.splitlines() if ln.startswith('## 十一')]
assert cal_sec11_title, 'calibration 第十一节标题未见'
snap_map = dict(snap_entries)
assert snap_map['references/calibration.md'] == \
    'f84294e6e437d34bedf89c2820ddcab3a76684d3f7a91ff3e2f12a037336e53e', snap_map['references/calibration.md']
assert snap_map['SKILL.md'] == \
    'f311e7aa8f70771da767b13d0f7da03367c414529550263b2095c157b5f63234', snap_map['SKILL.md']
skill_text = open(os.path.join(SNAP_DIR, 'SKILL.md'), encoding='utf-8').read()
assert '(s)' in skill_text and 'R83-REV1' in skill_text
# 与 R83 平台快照（runs/round83/kb-snapshot）逐件比对登记（预期差异恰为集成文件集）
open_snap = os.path.join(R83, 'kb-snapshot')
diff_files = []
open_map = {}
for root, dirs, files in os.walk(open_snap):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        open_map[os.path.relpath(p, open_snap)] = \
            hashlib.sha256(open(p, 'rb').read()).hexdigest()
for rel in sorted(set(open_map) | set(snap_map)):
    if open_map.get(rel) != snap_map.get(rel):
        diff_files.append(rel)
assert diff_files == ['SKILL.md', 'references/calibration.md'], diff_files

report = {
    'round': 83, 'set': 'holdout28', 'built_by': '组集封存席（R83）',
    'ruling': 'runs/round83/PREREG-ADDENDUM-r83.md（组集构成写定）；主预注册 PREREG.md §4',
    'T': 27, 'order': ORDER,
    'selection_register': selection_register,
    'fallback_log': fallback_log,
    'leak_hold_list': leak_hold,
    'leak_flag_list': leak_flags,
    'liuyao_five_element_recheck': liuyao_check,
    'composition_assertions': composition_assertions,
    'eligibility_assertions': eligibility,
    'eligibility_all_pass': True,
    'zero_reuse_recheck': {
        'sources': used_sources,
        'method': '只对 id 集（dev9 基线键集＋inputs-dev9/10/11/12 与 inputs 目录文件名、'
                  'phase2 splits2 holdout2、holdout3–27 各 test_gold.jsonl 仅取 id 字段、'
                  'holdout2–27 inputs 与 *-inputs 目录文件名、顶层 inputs6–10 目录文件名）；'
                  '未打开任何已封存集金标正文做内容比对',
        'used_union_total': len(used_union),
        'holdout27_ids_checked_separately': sorted(h27_ids),
        'selected_hit_count': 0, 'selected_hits': reuse_hits,
        'post_seal_union_would_be': len(used_union) + 27},
    'input_field_whitelist': INPUT_FIELDS,
    'input_field_whitelist_basis': 'holdout27/inputs/DS-040.json 实读字段集（开工对齐断言通过）',
    'strip_register': strip_register,
    'field_mapping_notes': field_mapping_notes,
    'deletion_register': deletion_register,
    'hygiene_question_scan': hygiene_scan,
    'gold_gap_scan': gap_register,
    'gold_supplement': SUPPLEMENT,
    'gold_supplement_count': len(SUPPLEMENT),
    'gold_outcome_swap_correction': OUTCOME_SWAP,
    'scan1_verbatim_fragment': {
        'method': '每例 master_prediction 与 outcome_record 的特征片段（标点分句整句'
                  '（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串扫描；'
                  '结局片段与断语片段全 27 例零命中（硬断言）',
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
    'scan2_independent_rescan': '由独立复扫脚本 scan_holdout28_r83.py 执行，结果另行登记于封存日志',
    'scan3_host_rescan': '主持验封道，非本席执行——留位',
    'gold_sha256_hashlib': sha_lib,
    'gold_bytes': gold_bytes,
    'card_bytes': card_bytes,
    'card_bytes_total': sum(card_bytes.values()),
    'kb_snapshot': {'dir': 'runs/round83/kb-snapshot-holdout28/',
                    'excluded_non_snapshot_files': SNAP_EXCLUDED,
                    'file_count': len(snap_entries),
                    'sha256_list': 'runs/round83/kb-snapshot-holdout28-sha256.txt',
                    'sha256_list_sha256': snap_list_sha,
                    'files': [rel for rel, _ in snap_entries],
                    'calibration_section11_title': cal_sec11_title,
                    'calibration_sha256': snap_map['references/calibration.md'],
                    'skill_sha256': snap_map['SKILL.md'],
                    'contains_calibration_sections_8_10_11_and_skill_pointer_s': True,
                    'diff_vs_round83_platform_snapshot': diff_files},
    'outputs_written': [f'holdout28/inputs/{c}.json' for c in ORDER] +
                       ['holdout28/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 27, 'order': ORDER,
                  'used_union_total': len(used_union),
                  'fallback_log': fallback_log,
                  'snapshot_files': len(snap_entries),
                  'snapshot_excluded': SNAP_EXCLUDED,
                  'diff_vs_platform': diff_files,
                  'gold_sha256_hashlib': sha_lib, 'gold_bytes': gold_bytes,
                  'card_bytes_total': sum(card_bytes.values())},
                 ensure_ascii=False))
