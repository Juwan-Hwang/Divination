#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R82 组集封存席：按 PREREG-ADDENDUM-r82.md 组建并封存 holdout27（T＝27）。

构成（增补件 §一写死）：八字 DS 9（DS-040、041、042、043、044、045、046、
048、049；DS-047 污染 medium 不在名单）／奇门开悟 QM 9（QM-044、045、046、
047、048、049、052、055、058，开悟 eligible 未用全 9 例）／六爻 GSZ 5
（GSZ-079、081、084、086、088，建卡口径五要素复核）／六爻 WHY 一轮 4
（WHY-008、009、010、011）。
递补链（增补件 §一）：DS 段 DS-050 起顺延；开悟段已取全 9 例、无同源递补
（若开悟例不过，跨位由启悟 QM-210、QM-211、旧池 QM-010 依次递补，体系仍记
qimen）；GSZ 段 GSZ-091 起顺延；WHY 段 WHY-012 起顺延。本轮预定 27 例资格
断言若全过则递补不触发，逐件登记。
零复用：已用并集盘上实算（口径照 PREREG §4 与 count_used_union_r82.py：
dev 池＋phase2 holdout2＋holdout3–26 金标 id＋holdout inputs 卡 id＋顶层
inputs6–10 卡 id），断言并集＝1112；选例逐 id 零命中；另对 holdout26 之
27 id 单列零命中断言（该 27 id 已含于 1112 并集内，封存后并集将为 1139）。
金标补录（4 例，回原书逐字补录后封，逐件登记于构建报告 gold_supplement）：
- WHY-008–011：台账未单列断语字段（master_prediction 缺位），回《六爻分类
  占验技法》原书页图逐字补录各例〔判斷〕段（印刷 pp.18-19／p20／p21／
  pp.21-22；扫描本 visual 转录，体例承 SUPPLY-GOLD-SUPPLEMENT-r56）。
- DS/KW/GSZ 三段台账断语经缺口扫描「……」零命中，无摘录缺口补录件；WHY 四例
  结局经回原书应验段逐例核对与台账一致，无对调订正件（OUTCOME_SWAP 空）。
扫描：①逐字片段扫描（结局片段与断语片段全例零命中硬断言）；
②R42 PREREG §5 内容级标记＋字段名黑名单＋禁用键集递归扫描零命中硬断言；
③落盘后逐卡回读复扫。金标 SHA-256 以构建脚本 hashlib 输出记录（封存席
另以独立 sha256sum 复算双读，主持再做第三读）。
快照：自现行活 method/ 复制 runs/round82/kb-snapshot-holdout27＋SHA 清单
（封存时点锚定，含 calibration 第八节现行形态、第九节 R81-REV1 与第十节
R82-REV1），METHOD-INTEGRATION-*.md 为集成登记件、非快照内容件，自快照
排除并登记；与 runs/round82/kb-snapshot（R82 平台快照）逐件比对登记
（预期差异恰为 calibration.md／SKILL.md 两件，即 R82-REV1 集成差异）。
只建卡与封存：不作断、不评分、不开封、不做 git 操作。
适配自 holdout26 构建脚本（runs/round81/build_holdout26_r81.py）与 holdout20
WHY 建卡段（runs/round56/build_holdout20_r56.py），逐处定点改写；脚本内
round81/holdout26 字样仅存于「承先例/范本」实指引用与字段白名单对齐基准
（holdout26 卡实读）。
"""
import json, hashlib, os, re, shutil
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'
R82 = os.path.join(BASE, 'runs/round82')
DIG76 = os.path.join(BASE, 'runs/round76/digestion')
OUT_DIR = os.path.join(BASE, 'holdout27')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R82, 'build-holdout27-report-r82.json')

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
# 字段白名单以 holdout26 任一卡实读字段集对齐（封存体例照 holdout26 定式）
h26_card = load_json(os.path.join(BASE, 'holdout26/inputs/DS-031.json'))
assert list(h26_card.keys()) == INPUT_FIELDS, list(h26_card.keys())

# ---------- 台账载入 ----------
ds_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-duanshi-r76.json'))
kw_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-kaiwu-r76.json'))
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
for i in range(3, 27):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    s = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip():
                s.add(json.loads(line)['id'])
    gold_per_set[f'holdout{i}'] = len(s)
    gold_ids |= s
used_sources['holdout3_26_gold_ids'] = len(gold_ids)
used_sources['gold_per_set'] = gold_per_set

input_ids = set()
for i in range(2, 27):
    for dname in (f'holdout{i}/inputs', f'holdout{i}-inputs'):
        d = os.path.join(BASE, dname)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'):
                    input_ids.add(fn[:-5])
used_sources['holdout2_26_input_card_ids'] = len(input_ids)
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
assert len(used_union) == 1112, len(used_union)  # 与主持开轮实算（PREREG 开轮登记）一致
h26_ids = set()
for line in open(os.path.join(BASE, 'holdout26/test_gold.jsonl'), encoding='utf-8'):
    if line.strip():
        h26_ids.add(json.loads(line)['id'])
assert len(h26_ids) == 27 and h26_ids <= used_union

selection_register = {}
leak_hold = []   # 排除登记（未入选，承既有裁处）
leak_flags = []  # 入选标旗（照建不动、卡面原样保留，提请主持裁处）

# ---------- 预定选例（增补件 §一写死） ----------
DS_WANT = ['DS-040', 'DS-041', 'DS-042', 'DS-043', 'DS-044',
           'DS-045', 'DS-046', 'DS-048', 'DS-049']
KW_WANT = ['QM-044', 'QM-045', 'QM-046', 'QM-047', 'QM-048',
           'QM-049', 'QM-052', 'QM-055', 'QM-058']
GSZ_WANT = ['GSZ-079', 'GSZ-081', 'GSZ-084', 'GSZ-086', 'GSZ-088']
WHY_WANT = ['WHY-008', 'WHY-009', 'WHY-010', 'WHY-011']
ORDER = DS_WANT + KW_WANT + GSZ_WANT + WHY_WANT
assert len(ORDER) == 27 and len(set(ORDER)) == 27
reuse_hits = [cid for cid in ORDER if cid in used_union]
assert not reuse_hits, f'选例与已用并集（1112）相交：{reuse_hits}'
assert not [cid for cid in ORDER if cid in h26_ids], '选例与 holdout26 之 27 id 相交'

# ---------- DS 9 资格断言 ----------
ds_by = {r['case_id']: r for r in ds_mining['records']}
for cid in DS_WANT:
    r = ds_by[cid]
    assert r['eligible_net'] is True and r['anchor_status'] == 'present', cid
    assert r['contamination_pre'] == 'low', cid
    assert all(str(v).startswith('pass') for v in r['filters'].values()), cid
    assert r['master_assertion'].strip() and r['outcome'].strip(), cid
pillars_sel = [ds_by[c]['input_side']['pillars_verbatim'] for c in DS_WANT]
assert len(set(pillars_sel)) == 9  # 同造（同四柱）组内零重复
# 同造合并组（DS-011/DS-033）唯一卡 DS-033 已于 holdout26 取用，本段 9 例不涉该组（四柱互异断言在上行）
selection_register['DS'] = {
    'rule': '增补件 §一写死 DS-040–046、048、049 按名单序（DS-047 污染 medium、'
            '不在名单）；逐例 eligible_net∧present∧low∧filters 四项全 pass∧'
            '断语/结局非空断言；入选 9 例四柱互异',
    'selected': DS_WANT, 'fallback_triggered': False,
    'fallback_chain_head': 'DS-050（未动用）'}

# ---------- 开悟 QM 9 资格断言 ----------
kw_by = {c['case_id']: c for c in kw_mining['cases']}
for cid in KW_WANT:
    c = kw_by[cid]
    assert c['anchor_status'] == 'present' and c['contamination_pre'] == 'low', cid
    assert c['separable'] is True, cid
    assert c['stem_check']['tianpan_ok'] and c['stem_check']['dipan_ok'], cid
    assert c['master_assertion'].strip() and c['outcome'].strip(), cid
selection_register['KW'] = {
    'rule': '增补件 §一写死开悟 9 例按名单序（开悟 eligible 未用恰 9 例、已取全）；'
            '逐例 present∧low∧separable∧stem_check 天地盘双 ok（全合）∧断语/结局'
            '非空断言；同源无递补，跨位递补链为启悟 QM-210、QM-211、旧池 QM-010',
    'selected': KW_WANT, 'fallback_triggered': False,
    'fallback_chain_head': 'QM-210（跨位递补链首位，未动用）'}

# ---------- GSZ 5 资格断言＋建卡口径五要素复核 ----------
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
for cid in GSZ_WANT:
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
    assert ok, (cid, liuyao_check[cid])
selection_register['GSZ'] = {
    'rule': '增补件 §一写死 GSZ 5 例按名单序；逐例 grade A∧low∧present∧eligible_net∧'
            '断语/结局非空∧回原书文字层五要素复核全在场断言',
    'selected': GSZ_WANT, 'fallback_triggered': False,
    'fallback_chain_head': 'GSZ-091（未动用）'}

# ---------- WHY 一轮 4 资格断言 ----------
why_by = {e['provisional_id']: e for e in why_mining['entries']}
why_net = why_mining['counts']['net_eligible_A_low_present']
for cid in WHY_WANT:
    e = why_by[cid]
    assert cid in why_net, cid
    assert e['pollution'] == 'low' and e['anchor_presence'] == 'present', cid
    assert not e['anchor_missing'], cid
    assert e['outcome_record'].strip(), cid
selection_register['WHY'] = {
    'rule': '增补件 §一写死 WHY 一轮 4 例按名单序；逐例 counts 净入账名单成员∧'
            'low∧present∧anchor_missing 空∧结局非空断言；断语台账未单列字段，'
            '回原书逐字补录（见 gold_supplement）',
    'selected': WHY_WANT, 'fallback_triggered': False,
    'fallback_chain_head': 'WHY-012（未动用）'}

# ---------- 断语缺口扫描与补录（回原书逐字补录后封） ----------
gap_register = {}
for cid in ORDER:
    if cid in ds_by:
        mp = ds_by[cid]['master_assertion']
    elif cid in kw_by:
        mp = kw_by[cid]['master_assertion']
    elif cid in gsz_by:
        mp = gsz_by[cid]['master_prediction']
    else:
        mp = ''  # WHY 台账未单列断语字段，缺口即整段，逐例补录
    gap_register[cid] = {'mp_gap': '……' in mp, 'mp_missing_field': cid in why_by}
assert [k for k, v in gap_register.items() if v['mp_gap']] == [], \
    [k for k, v in gap_register.items() if v['mp_gap']]

SUPPLEMENT = {
    'WHY-008': {
        'master_prediction':
            '〔判斷〕世爻辰土為水庫，在水池或湖邊清理環境垃圾。世爻得日辰比扶旺相，'
            '卦中兄弟卯木、寅木兩動剋世，又在巽宮，乃是逆風，外出勞動定受風吹之苦。',
        'source_anchor': '《六爻分类占验技法》第一章「順風和逆風」例二（印刷pp.18-19，〔判斷〕在p19，扫描本PDF第10页左叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段；'
                'transcription=visual（300dpi 渲染页读图，繁体照原书）'},
    'WHY-009': {
        'master_prediction':
            '〔判斷〕卦中有動爻出現，從動爻入手判斷。父母丑土得月建生扶為旺相，發動'
            '主雨、官鬼午火得月扶日生發動化父母未土，乃是雷雨交加之象。父母為土，'
            '土為陰雲，更增加了陰雨的信息。官鬼通常為濃雲、霧氣、雷電的信息，但並'
            '不是說官鬼發動就有雷電產生。此卦金爻既不逢空，又不發動，也不是官鬼，'
            '所以以金爻來判斷雷電有些勉強。此卦中官鬼為火發動，從五行的角度看火為'
            '閃電，閃電出現必有雷鳴，因此次日天氣當為雷雨天氣。',
        'source_anchor': '《六爻分类占验技法》第一章「五行」例一（印刷p20，扫描本PDF第11页右叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段；'
                'transcription=visual（300dpi 渲染页读图，繁体照原书）'},
    'WHY-010': {
        'master_prediction':
            '〔判斷〕卦中有動爻，從動爻入手判斷。初爻妻財丑土發動，妻財主晴，乍一看'
            '當斷為晴天，但是動而化出父母子水，又有官鬼申金暗動，當斷為晴轉陰，有'
            '小雨才對。首先看妻財丑土，從五行角度看，土為陰天、雲霧，動而化出父母，'
            '其意更強。父母為雨，若臨水，水又主雨，下雨的信息就會強烈一些。但父母'
            '爻乃是由初爻變來，且與動爻相合，理當斷有霧才對，而卦中還有官鬼申金暗'
            '動，也應納入參考因素。官鬼為金，逢空暗動，為打雷的信息，因此綜合整個'
            '卦中信息，本日天氣當為晴轉陰有像霧一樣的濛濛小雨，且有雷聲。',
        'source_anchor': '《六爻分类占验技法》第一章「五行」例二（印刷p21，扫描本PDF第11页左叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段；'
                'transcription=visual（300dpi 渲染页读图，繁体照原书）'},
    'WHY-011': {
        'master_prediction':
            '〔判斷〕卦中有動爻，從動爻入手判斷。卦中父母子水發動，父母主雨，但父母'
            '被日月剋制為休囚，按照常規應斷為陰天，但第二天為亥日，與父母的五行相同，'
            '有助旺父母爻的作用，因此斷為下雨，但因父母不旺為小雨。父母動而化出兄弟，'
            '乃是有風有雨。',
        'source_anchor': '《六爻分类占验技法》第一章「被測日辰」例一（印刷pp.21-22，〔判斷〕在p22，扫描本PDF第12页右叶）',
        'note': '台账未单列断语字段；本席回原书页图逐字补录〔判斷〕全段；'
                'transcription=visual（300dpi 渲染页读图，繁体照原书）'},
}
# 结局对调订正：本轮无（WHY-008–011 结局经回原书应验段逐例核对与台账一致）
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

# ---------- DS 9 例（八字） ----------
for cid in DS_WANT:
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
    mp = SUPPLEMENT[cid]['master_prediction'] if cid in SUPPLEMENT else r['master_assertion']
    note = (f"入账口径：eligible_net=true、锚点 present、contamination low、四滤全 pass；"
            f"锚点：{r['anchor_note']}；污染：{r['contamination_note']}；"
            f"转录：visual（confidence={r['transcription']['confidence']}，"
            f"{r['transcription']['note']}）；断语为原书断语逐字摘录，"
            f"多段以／分隔（台账摘录分隔符）")
    if r.get('verdict_note'):
        note += f"；台账 verdict_note：{r['verdict_note']}"
    gold = {'id': cid, 'master_prediction': mp,
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

# ---------- 开悟 QM 9 例（奇门；input_side 为单串） ----------
KW_SUBJECT = {
    'QM-044': '鹿泉市个体汽修厂厂长田凤良（骑摩托车回家途中遗失公文包求测）；占者：石建国',
    'QM-045': '石建国（自家摩托车被盗自测）；占者：石建国（自测）',
    'QM-046': '一位中年妇女（耳环不见求测）；占者：王夕强（山东省文登市学员）',
    'QM-047': '佟安琪之妻（摩托车早上发现不见，电话告之）；占者：佟安琪',
    'QM-048': '河北科迪药业有限公司陈董事长（土地官司求测）；占者：张志春',
    'QM-049': '鹿泉市孟女士（为丈夫出事求测）；占者：石建国',
    'QM-052': '某市七中校长袁某（七中升省级重点中学求测）；占者：张志春',
    'QM-055': '张志春（自测赴台出席国际易学研讨大会能否成行）；占者：张志春',
    'QM-058': '一位中年男子（晒小麦时驾驶证弄丢求测）；占者：王夕强',
}
KW_QUESTION = {  # 除 QM-045 外均为 input_side 原文子串（脚本断言）；QM-045 为组写（原文未逐字引问句，登记）
    'QM-044': '请你给我测一测，下午7点左右，我骑摩托车回家，把公文包挂在车把上，到家后发现包不在了',
    'QM-045': '求测摩托车被盗能否找到（原文未逐字引问句，按丢失时间起局）',
    'QM-046': '请预测一下能否找到',
    'QM-047': '想算一算能不能找到',
    'QM-048': '求测这场官司能不能打、能不能打赢',
    'QM-049': '丈夫出了事，问能否平安渡过难关',
    'QM-052': '预测七中升省重点一事能否办成',
    'QM-055': '测一下这次赴台能否成行',
    'QM-058': '求测一下能否找到',
}
for cid in KW_WANT:
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
    if cid != 'QM-045':
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
                                '←input_side 盘面段逐字（QM-052 两局盘面（第二、三局）全载，'
                                'partition 于第一局盘面标记）；question←input_side 原文'
                                '子串（断言验；QM-045 例外为组写、原文未逐字引问句，口径'
                                '在此登记）；subject 为组写（据 input_side 与 caster 组写，'
                                '口径在此登记）；setting←source＋caster 组写')

# ---------- GSZ 5 例（六爻，承 holdout26 体例） ----------
for cid in GSZ_WANT:
    e = gsz_by[cid]
    ok = (e['grade'] == 'A' and e['pollution'] == 'low'
          and e['anchor_presence'] == 'present' and e['eligible_net'] is True
          and e['master_prediction'].strip() and e['outcome_record'].strip()
          and liuyao_check[cid]['pass'])
    eligibility[cid] = {'grade': e['grade'], 'pollution': e['pollution'],
                        'anchor_presence': e['anchor_presence'],
                        'eligible_net': e['eligible_net'],
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
                                '（台账无 context 原文，承 holdout26 先例）；'
                                'setting/provenance←台账 source 逐字；anchors←asked_at＋'
                                'input_fields.chart 全列逐字')

# ---------- WHY 一轮 4 例（六爻，承 holdout20 建卡体例；断语回原书补录） ----------
for cid in WHY_WANT:
    e = why_by[cid]
    ok = (cid in why_net and e['pollution'] == 'low'
          and e['anchor_presence'] == 'present' and not e['anchor_missing']
          and e['outcome_record'].strip())
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
    outcome = e['outcome_record']
    if cid in OUTCOME_SWAP:
        outcome = why_by[OUTCOME_SWAP[cid]['ledger_holder']]['outcome_record']
    note = ('锚点在场（卦名、变卦、动爻、世应、六亲纳支、月建日辰全列）；'
            '转录：visual（扫描本多模态读图转录）；现代案例书、名案污染已从严定级'
            '、本例判 low；')
    note += (f"断语经本轮封存席回原书逐字补录（{SUPPLEMENT[cid]['source_anchor']}），"
             f"见构建报告 gold_supplement；台账仅录应验情况、未单列断语字段。")
    if cid in OUTCOME_SWAP:
        note += (f"结局订正：台账 outcome_record 与 {OUTCOME_SWAP[cid]['ledger_holder']} "
                 f"互换（回原书核对，{OUTCOME_SWAP[cid]['book_anchor']}），本席按原书"
                 f"对调还原，提请主持验封复核。")
    golds[cid] = {'id': cid,
                  'master_prediction': SUPPLEMENT[cid]['master_prediction'],
                  'outcome_record': outcome, 'tradition': 'liuyao',
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
# 入选 27 例 question/setting 逐例核查：GSZ/WHY question 承台账逐字、均只及所问之事，
# 无结局事实；KW question 为原文子串或组写（登记在案）；DS question/setting 为组写与
# 台账 source 逐字，无结局事实。无中性化改写件，删除 0 件、改写 0 件，逐项登记于此。
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
    'note': '入选例中涉他人面例（QM-049 妻为夫求测、GSZ-081 某女代占其子、GSZ-084 某女'
            '代占其母、WHY-008 日本学生自测）question 均只及所问之事本身，无第二人'
            '无关结局字样，经语义级通读核查，无删除件'})

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

# ---------- 构成与限度断言（增补件 §二写死值） ----------
SOURCE_OF = {}
for cid in ORDER:
    if cid.startswith('DS-'):
        SOURCE_OF[cid] = '段建业《段氏理象学》'
    elif cid in KW_WANT:
        SOURCE_OF[cid] = '张志春《开悟之门》'
    elif cid.startswith('GSZ-'):
        SOURCE_OF[cid] = '王虎应《六爻卦例说真》'
    else:
        SOURCE_OF[cid] = '王虎应《六爻分类占验技法》'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)
assert len(ORDER) == 27
assert trad_counts == {'bazi': 9, 'qimen': 9, 'liuyao': 9}, trad_counts
assert max(trad_counts.values()) <= 13, trad_counts  # 单体系 ≤50%（计数 ≤13）
assert max(src_counts.values()) <= 13, src_counts    # 单源 ≤50%（计数 ≤13）
assert 27 - trad_counts['liuyao'] >= 13              # 非六爻 ≥13
assert len(src_counts) >= 2                          # 多源构成（四源）
assert all(golds[c]['pollution'] == 'low' for c in ORDER)
assert not [c for c in ORDER if c in used_union]
composition_assertions = {
    'T': 27, 'by_tradition': dict(trad_counts), 'by_source': dict(src_counts),
    'max_single_tradition_share': max(trad_counts.values()) / 27,
    'max_single_source_share': max(src_counts.values()) / 27,
    'non_yijian': 27, 'non_liuyao': 27 - trad_counts['liuyao'],
    'source_count': len(src_counts), 'pollution_low': 27,
    'used_union_intersection': [], 'holdout26_intersection': [], 'all_pass': True}

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
SNAP_DIR = os.path.join(R82, 'kb-snapshot-holdout27')
if os.path.exists(SNAP_DIR):
    shutil.rmtree(SNAP_DIR)
shutil.copytree(os.path.join(BASE, 'method'), SNAP_DIR)
SNAP_EXCLUDED = []
for fn in sorted(os.listdir(SNAP_DIR)):
    if fn.startswith('METHOD-INTEGRATION-') and fn.endswith('.md'):
        os.remove(os.path.join(SNAP_DIR, fn))
        SNAP_EXCLUDED.append(fn)
snap_entries = []
for root, dirs, files in os.walk(SNAP_DIR):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, SNAP_DIR)
        snap_entries.append((rel, hashlib.sha256(open(p, 'rb').read()).hexdigest()))
SNAP_SHA_PATH = os.path.join(R82, 'kb-snapshot-holdout27-sha256.txt')
with open(SNAP_SHA_PATH, 'w', encoding='utf-8') as f:
    for rel, h in snap_entries:
        f.write(f'{h}  {rel}\n')
snap_list_sha = hashlib.sha256(open(SNAP_SHA_PATH, 'rb').read()).hexdigest()
assert len(snap_entries) == 21, len(snap_entries)
cal_text = open(os.path.join(SNAP_DIR, 'references/calibration.md'), encoding='utf-8').read()
assert 'R82-REV1' in cal_text and 'R81-REV1' in cal_text and 'R80-REV1' in cal_text
cal_sec10_title = [ln for ln in cal_text.splitlines() if ln.startswith('## 十')]
assert cal_sec10_title, 'calibration 第十节标题未见'
# 与 R82 平台快照（runs/round82/kb-snapshot）逐件比对登记（预期差异恰为集成文件集）
open_snap = os.path.join(R82, 'kb-snapshot')
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
    'round': 82, 'set': 'holdout27', 'built_by': '组集封存席（R82）',
    'ruling': 'runs/round82/PREREG-ADDENDUM-r82.md（组集构成写定）；主预注册 PREREG.md §4',
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
                  'phase2 splits2 holdout2、holdout3–26 各 test_gold.jsonl 仅取 id 字段、'
                  'holdout2–26 inputs 与 *-inputs 目录文件名、顶层 inputs6–10 目录文件名）；'
                  '未打开任何已封存集金标正文做内容比对',
        'used_union_total': len(used_union),
        'holdout26_ids_checked_separately': sorted(h26_ids),
        'selected_hit_count': 0, 'selected_hits': reuse_hits,
        'post_seal_union_would_be': len(used_union) + 27},
    'input_field_whitelist': INPUT_FIELDS,
    'input_field_whitelist_basis': 'holdout26/inputs/DS-031.json 实读字段集（开工对齐断言通过）',
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
    'scan2_independent_rescan': '由独立复扫脚本 scan_holdout27_r82.py 执行，结果另行登记于封存日志',
    'scan3_host_rescan': '主持验封道，非本席执行——留位',
    'gold_sha256_hashlib': sha_lib,
    'gold_bytes': gold_bytes,
    'card_bytes': card_bytes,
    'card_bytes_total': sum(card_bytes.values()),
    'kb_snapshot': {'dir': 'runs/round82/kb-snapshot-holdout27/',
                    'excluded_non_snapshot_files': SNAP_EXCLUDED,
                    'file_count': len(snap_entries),
                    'sha256_list': 'runs/round82/kb-snapshot-holdout27-sha256.txt',
                    'sha256_list_sha256': snap_list_sha,
                    'files': [rel for rel, _ in snap_entries],
                    'calibration_section10_title': cal_sec10_title,
                    'contains_calibration_section8_section9_and_section10': True,
                    'diff_vs_round82_platform_snapshot': diff_files},
    'outputs_written': [f'holdout27/inputs/{c}.json' for c in ORDER] +
                       ['holdout27/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 27, 'order': ORDER,
                  'used_union_total': len(used_union),
                  'snapshot_files': len(snap_entries),
                  'snapshot_excluded': SNAP_EXCLUDED,
                  'diff_vs_platform': diff_files,
                  'gold_sha256_hashlib': sha_lib, 'gold_bytes': gold_bytes,
                  'card_bytes_total': sum(card_bytes.values())},
                 ensure_ascii=False))
