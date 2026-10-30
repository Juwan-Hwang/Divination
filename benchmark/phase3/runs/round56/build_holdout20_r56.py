#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R56 建集数据席：按 PREREG-ADDENDUM-1 写死选集组建并封存 holdout20。

裁定：runs/round56/PREREG-ADDENDUM-1.md（选集 T＝25 写死：QW-001–012 八字；
WHY-003/015/021/030/067 六爻；YJ2-012、YJ-001、YJ-004、YJ-006 夷坚；
CZ2-001/002/003 梦占、CZ2-006 相墓；本轮只组集封存、不开封，开封轮为封存后
首个平台全立轮、最早 R57）。
配套口径：runs/round42/PREREG.md §5（内容级断语扫描三道与标记集原文）、
holdout19 先例（benchmark/phase3/data/holdout19-seal-log.md 体例）。

内容级断语扫描标记集：逐字复制 runs/round42/PREREG.md §5 常量（见下方
LEVEL1/LEVEL2/FIELD_BLACKLIST，脚本头注释引节号＝R42 PREREG §5）。
本席执行第一道（候选材料制备期扫描）与第二道（建卡自校验逐卡扫描）；
第三道（主持验封）非本席执行，报告中留位。

材料定位（派单写死）：
- QW/WHY：runs/round56/digestion/SUPPLY-MINING-quwei-r56.json 与
  SUPPLY-MINING-wanghuying-r56.json 的逐例 input_fields＋outcome_record（逐字）。
- YJ/CZ2：存量候选卡（路径承 runs/round53/digestion/STOCK-ANCHOR-r53.md 与
  runs/round54/digestion/SUPPLY-ACCOUNTING-r54.md 引路径）：
  YJ2-012＝runs/round49/digestion/cards-mining-yijian-r49/；
  YJ-001/004/006＝runs/round47/digestion/cards-mining-yijian/；
  CZ2-001/002/003＝runs/round51/digestion/cards-mining-chunzhu-r51/{inputs,gold}/；
  CZ2-006＝runs/round53/digestion/cards-mining-chunzhu-r53/{inputs,gold}/。
  只取输入侧字段与登记的断语（master_predictions statement_excerpt）/结局
  （outcome.description）逐字文本，管理字段剥离。

已知限度（如实登记，不臆补）：QW/WHY 开采台账未单列断语逐字字段——QW 之
outcome_record 为断语释义与命主反馈合录（多例仅录反馈段），WHY 之
outcome_record 仅录应验情况。本席对该 17 例金标 master_prediction 置 null
并逐例于 grade_note 明示，提请主持补录；不以结局文冒充断语。
体系口径：逐卡 tradition 从候选登记逐字（YJ-001/004/006＝mengzhan、
YJ2-012＝fangji），与 ADDENDUM-1 §二体系构成行（六爻 9/梦占 3）不一致，
差异在封存日志标旗，本席不改登记。

只建卡与封存：不作断、不评分、不开封验收、不做 git 操作。
零复用复核只对已用集 id 集（禁打开已封存集金标正文做内容比对）：已用 id
来源＝phase2/splits2.json 之 holdout2（29）＋holdout3–19 各 test_gold.jsonl
仅取 id 字段（515）＋data/master-baseline-dev9.json 键集 dev9（487），
并集 926（holdout19 封存时 901＋holdout19 已用 25）。
"""
import json, hashlib, os, subprocess, sys
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'
R56 = os.path.join(BASE, 'runs/round56')
OUT_DIR = os.path.join(BASE, 'holdout20')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R56, 'build-holdout20-report-r56.json')

# ---------- 内容级断语扫描标记集（逐字复制 R42 PREREG §5） ----------
# 一级标记（断语类）——逐字复制 PREREG §5
LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
# 二级标记（结局侧状态措辞）——逐字复制 PREREG §5
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
# 字段名黑名单片段（PREREG §5：字段名含断语/断曰/正议/验语/占断/线索·断者）
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '斷曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']


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


def load_json(p):
    return json.load(open(p, encoding='utf-8'))


# ---------- 门：例级零复用复核（只对 id 集） ----------
h2_ids = set(load_json(os.path.join(ROOT, 'benchmark/phase2/splits2.json'))['holdout2'])
h3_19_ids = set()
for i in range(3, 20):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    for line in open(p, encoding='utf-8'):
        if line.strip():
            h3_19_ids.add(json.loads(line)['id'])  # 只取 id，不作内容比对
dev9_ids = set(load_json(os.path.join(BASE, 'data/master-baseline-dev9.json')).keys())
used_union = h2_ids | h3_19_ids | dev9_ids
assert len(h2_ids) == 29 and len(h3_19_ids) == 515 and len(dev9_ids) == 487, \
    (len(h2_ids), len(h3_19_ids), len(dev9_ids))
assert len(used_union) == 926, len(used_union)

# ---------- 选集（ADDENDUM-1 §二写死，不得增减） ----------
QW_IDS = [f'QW-{i:03d}' for i in range(1, 13)]
WHY_IDS = ['WHY-003', 'WHY-015', 'WHY-021', 'WHY-030', 'WHY-067']
YJ_IDS = ['YJ2-012', 'YJ-001', 'YJ-004', 'YJ-006']
CZ2_IDS = ['CZ2-001', 'CZ2-002', 'CZ2-003', 'CZ2-006']
ORDER = QW_IDS + WHY_IDS + YJ_IDS + CZ2_IDS
assert len(ORDER) == 25 and len(set(ORDER)) == 25
assert all(cid not in used_union for cid in ORDER), '选例与已用并集相交（零复用门）'

CARD_FILES = {
    'YJ2-012': ('runs/round49/digestion/cards-mining-yijian-r49/YJ2-012-input.json',
                'runs/round49/digestion/cards-mining-yijian-r49/YJ2-012-gold.json'),
    'YJ-001': ('runs/round47/digestion/cards-mining-yijian/YJ-001-input.json',
               'runs/round47/digestion/cards-mining-yijian/YJ-001-gold.json'),
    'YJ-004': ('runs/round47/digestion/cards-mining-yijian/YJ-004-input.json',
               'runs/round47/digestion/cards-mining-yijian/YJ-004-gold.json'),
    'YJ-006': ('runs/round47/digestion/cards-mining-yijian/YJ-006-input.json',
               'runs/round47/digestion/cards-mining-yijian/YJ-006-gold.json'),
    'CZ2-001': ('runs/round51/digestion/cards-mining-chunzhu-r51/inputs/CZ2-001.json',
                'runs/round51/digestion/cards-mining-chunzhu-r51/gold/CZ2-001.json'),
    'CZ2-002': ('runs/round51/digestion/cards-mining-chunzhu-r51/inputs/CZ2-002.json',
                'runs/round51/digestion/cards-mining-chunzhu-r51/gold/CZ2-002.json'),
    'CZ2-003': ('runs/round51/digestion/cards-mining-chunzhu-r51/inputs/CZ2-003.json',
                'runs/round51/digestion/cards-mining-chunzhu-r51/gold/CZ2-003.json'),
    'CZ2-006': ('runs/round53/digestion/cards-mining-chunzhu-r53/inputs/CZ2-006.json',
                'runs/round53/digestion/cards-mining-chunzhu-r53/gold/CZ2-006.json'),
}

INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status', 'anchors']
BANNED_IN_CARD = {'grade_note', 'grade_suggestion', 'grade_reason', 'contamination',
                  'contamination_suggestion', 'contamination_reason',
                  'contamination_rationale', 'outcome', 'outcome_record',
                  'outcome_grade', 'master_predictions', 'master_prediction',
                  'passage_full', 'record_status', 'notes', 'master',
                  'seal_eligible', 'holdout_eligible', 'review', 'pollution',
                  'pollution_note', 'anchor_presence', 'anchor_missing',
                  'anchor_check', 'anchor_note', 'dedup_check', 'filters',
                  'outcome_type', 'outcome_note', 'transcription',
                  'provisional_id', 'source', 'language', 'grade'}


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


PRED_GAP_QW = ('断语登记限度：开采台账 outcome_record 为断语释义与命主反馈合录'
               '（多例仅录反馈段），未单列断语逐字字段，master_prediction 置 null '
               '不臆补，提请主持自原书补录后方可开封判读。')
PRED_GAP_WHY = ('断语登记限度：开采台账仅录应验情况（outcome_record），断语未逐字'
                '转录入账（WHY-030/067 应验文内嵌断语要点括注、照 outcome_record '
                '逐字并存），master_prediction 置 null 不臆补，提请主持自原书'
                '补录后方可开封判读。')

qw_mining = load_json(os.path.join(R56, 'digestion/SUPPLY-MINING-quwei-r56.json'))
why_mining = load_json(os.path.join(R56, 'digestion/SUPPLY-MINING-wanghuying-r56.json'))
qw_by_id = {e['provisional_id']: e for e in qw_mining['entries']}
why_by_id = {e['provisional_id']: e for e in why_mining['entries']}

cards, golds = {}, {}
strip_register, scan_stage1, field_mapping_notes = {}, {}, {}
pred_gap_cases = []

# ---------- QW 12 例（八字） ----------
for cid in QW_IDS:
    e = qw_by_id[cid]
    assert e['pollution'] == 'low' and e['anchor_presence'] == 'present', cid
    inf = e['input_fields']
    scan_stage1[cid] = {'content_hits': scan_content(inf),
                        'fieldname_hits': scan_field_names(inf),
                        'source': 'runs/round56/digestion/SUPPLY-MINING-quwei-r56.json input_fields'}
    subj, ctx, prov = inf['subject'], inf['context'], inf['provenance']
    card_context = ctx['setting']
    if cid == 'QW-010':
        # 附条件改写（承 holdout19 YJ2-007 先例）：台账输入侧 setting 原文嵌成色
        # 限度句「反馈所及仅少年期事件，非一生结局，入账时如实标此限度」含二级
        # 标记「结局」；该限度已由金标 grade_note 之 outcome_note 全文承载，
        # 输入侧删此句，改写前后对照存证于构建报告 qw010_rewrite。
        old = ('函测：命主为 1986 年生少年（求测时约十六岁），父母为其求测；'
               '反馈所及仅少年期事件，非一生结局，入账时如实标此限度')
        assert card_context == old, card_context
        card_context = '函测：命主为 1986 年生少年（求测时约十六岁），父母为其求测'
    card = {
        'id': cid,
        'tradition': 'bazi',
        'subject': f"{subj['name_or_desc']}；{subj['basic_info']}",
        'context': card_context,
        'question': ctx['question'],
        'setting': f"{e['source']}；求测时间：{ctx['asked_at']}",
        'provenance': f"{prov['book']}·{prov['location']}；{prov['edition']}",
        'redistributable': False,
        'license_status': '现代版权文本（TXT 转录本），内部研究用',
        'anchors': {
            'birth_info_verbatim': subj['birth_info_verbatim'],
            'gender': subj['gender'],
            'pillars': ctx['attachments']['pillars'],
            'day_master': ctx['attachments']['day_master'],
        },
    }
    strip_register[cid] = ['pollution/pollution_note/anchor_presence/anchor_note/'
                           'dedup_check/filters/outcome_record（台账管理与金标侧字段，'
                           '不入输入卡）；input_fields 之 id/tradition 与 subject/context/'
                           'provenance 嵌套子字段经字段映射摊平入卡（子字段文本逐字）']
    field_mapping_notes[cid] = ('subject←name_or_desc＋basic_info；context←context.setting；'
                                'question←context.question；setting←source＋context.asked_at；'
                                'provenance←provenance.book＋location＋edition；'
                                'anchors←subject.birth_info_verbatim/gender＋context.attachments')
    note = '作者自选断准集、结局命主自报（无第三方核实）；'
    if e.get('outcome_note'):
        note += e['outcome_note'] + '；'
    note += f"锚点：{e['anchor_note']}；"
    note += ('转录：TXT 转录本（转录出处不明、繁简混排、个别转录误字照录，'
             '见 DIGEST-bazi-quwei-r56 登记）；')
    note += PRED_GAP_QW
    pred_gap_cases.append(cid)
    cards[cid] = card
    golds[cid] = {'id': cid, 'master_prediction': None,
                  'outcome_record': e['outcome_record'], 'tradition': 'bazi',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note}

# ---------- WHY 5 例（六爻） ----------
for cid in WHY_IDS:
    e = why_by_id[cid]
    assert e['pollution'] == 'low' and e['anchor_presence'] == 'present', cid
    assert not e['anchor_missing'], cid
    inf = e['input_fields']
    scan_stage1[cid] = {'content_hits': scan_content(inf),
                        'fieldname_hits': scan_field_names(inf),
                        'source': 'runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json input_fields'}
    chart = inf['chart']
    card = {
        'id': cid,
        'tradition': 'liuyao',
        'subject': e['subject'] if e['subject'] else '求测者（台账 subject 为空、原书未具名）',
        'context': f"占时：{inf['asked_at']}；《六爻分类占验技法》分类占验例",
        'question': inf['question'],
        'setting': f"{e['source']}",
        'provenance': f"{e['source']}；底本为用户经学校图书馆提供之扫描本，redistributable=false",
        'redistributable': False,
        'license_status': '现代版权文本（扫描本），内部研究用',
        'anchors': {
            'asked_at': inf['asked_at'],
            'ben_gua': chart['ben_gua'],
            'bian_gua': chart['bian_gua'],
            'moving_lines': chart['moving_lines'],
            'chart_lines_top_to_bottom': chart['chart_lines_top_to_bottom'],
        },
    }
    strip_register[cid] = ['pollution/anchor_presence/anchor_missing/dedup_check/'
                           'transcription/outcome_type/outcome_record（台账管理与金标侧'
                           '字段，不入输入卡）；台账 input_fields 无 context/setting/'
                           'provenance 独立字段，context 由 asked_at＋书名组写、setting/'
                           'provenance 由台账 source 逐字承接，组写口径登记于构建报告']
    field_mapping_notes[cid] = ('question←input_fields.question；anchors←input_fields.chart '
                                '全列＋asked_at；setting/provenance←台账 source 逐字；'
                                'context←asked_at 与书名组写（台账无 context 原文）')
    note = ('锚点在场（卦名、变卦、动爻、世应、六亲纳支、月建日辰全列）；'
            '转录：visual（扫描本多模态读图转录）；现代案例书、名案污染已从严定级'
            '、本例判 low；')
    note += PRED_GAP_WHY
    pred_gap_cases.append(cid)
    cards[cid] = card
    golds[cid] = {'id': cid, 'master_prediction': None,
                  'outcome_record': e['outcome_record'], 'tradition': 'liuyao',
                  'pollution': 'low', 'grade': 'A', 'grade_note': note}

# ---------- YJ/CZ2 8 例（存量候选卡） ----------
ANCHORS_OF = {
    'YJ2-012': {'anchor_type': '占式（观马物象）／谶语原文',
                'anchor_location': 'context 逐字载马象本体「新得一马，黑体而白鼻」'},
    'YJ-001': {'anchor_type': '梦象符号',
               'anchor_location': 'context 逐字载梦象全叙（梦棘闱晨启、独先入坐堂上）'},
    'YJ-004': {'anchor_type': '梦象符号',
               'anchor_location': 'context 逐字载梦象及榜字'},
    'YJ-006': {'anchor_type': '梦象符号',
               'anchor_location': 'context 逐字载梦象全叙（父子持伞行雨中）'},
    'CZ2-001': {'anchor_type': '梦象符号',
                'anchor_location': 'context 逐字载梦象及梦中题字'},
    'CZ2-002': {'anchor_type': '梦象符号',
                'anchor_location': 'context 逐字载梦象全叙'},
    'CZ2-003': {'anchor_type': '梦象符号',
                'anchor_location': 'context 逐字载梦象及梦中告语原文'},
    'CZ2-006': {'anchor_type': '相墓＝所相先墓（墓地本身）',
                'anchor_location': 'context/subject 逐字载「先墓在弁山之麓」；源文未载墓地形细节，锚点成色弱于 CZ2-004（墓圖），候选卡 notes 已登记、R54 入账裁定已悉'},
}


def flat_str(v):
    """候选卡嵌套 dict 字段摊平为逐字拼接字符串（子字段值逐字、键名作标）。"""
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        return '；'.join(f'{k}：{flat_str(x)}' for k, x in v.items())
    return str(v)


for cid in YJ_IDS + CZ2_IDS:
    in_rel, gold_rel = CARD_FILES[cid]
    cand_in = load_json(os.path.join(BASE, in_rel))
    cand_gold = load_json(os.path.join(BASE, gold_rel))
    scan_stage1[cid] = {'content_hits': scan_content(cand_in),
                        'fieldname_hits': scan_field_names(cand_in),
                        'source': in_rel}
    assert cand_gold['grade_suggestion'] == 'A', cid
    assert cand_gold['contamination_suggestion'] == 'low', cid
    stripped = [k for k in cand_in if k not in
                ('id', 'tradition', 'subject', 'context', 'question', 'setting',
                 'provenance', 'redistributable', 'license_status')]
    strip_register[cid] = ([f'{k}（管理字段，剥离）' for k in stripped] +
                           ['master_predictions/outcome/passage_full/grade_*/'
                            'contamination_*（金标侧，不入输入卡）'])
    ctx_raw = cand_in['context']
    if isinstance(ctx_raw, dict):
        # R47 夷坚卡：context 为 {asked_at, question, setting} 嵌套
        card_context = ctx_raw['question']
        card_question = ctx_raw['question']
        card_setting = f"{ctx_raw['asked_at']}；{ctx_raw['setting']}"
        field_mapping_notes[cid] = ('候选卡 context 为嵌套 dict：context/question 均取其 '
                                    'question 子字段逐字（梦象全叙即在该子字段、为锚点本体），'
                                    'setting←asked_at＋setting 子字段逐字拼接')
    else:
        card_context = ctx_raw
        card_question = cand_in['question']
        card_setting = cand_in['setting']
    if cid == 'CZ2-001':
        # 附条件改写（承 YJ2-007 先例）：候选卡 question 原文「此任結局如何」含
        # 二级标记「結局」（问句用词、非结局内容）；输入侧改写为「此任後事
        # 如何」，改写前后对照存证于构建报告 cz2001_rewrite，原候选卡不动。
        old_q = '禱夢所問：去留當如何，此任結局如何？'
        assert card_question == old_q, card_question
        card_question = '禱夢所問：去留當如何，此任後事如何？'
    if cid == 'CZ2-006':
        # 附条件改写（同 CZ2-001 例）：候选卡 question 原文「主何應驗」含二级
        # 标记「應驗」（问句用词）；输入侧改写为「主何吉凶」，对照存证于报告。
        old_q = '請言此先墓主何應驗？'
        assert card_question == old_q, card_question
        card_question = '請言此先墓主何吉凶？'
    card = {
        'id': cid,
        'tradition': cand_in['tradition'],
        'subject': flat_str(cand_in['subject']),
        'context': card_context,
        'question': card_question,
        'setting': card_setting,
        'provenance': flat_str(cand_in['provenance']),
        'redistributable': cand_in['redistributable'],
        'license_status': cand_in['license_status'],
        'anchors': ANCHORS_OF[cid],
    }
    assert card['redistributable'] is False, cid
    cards[cid] = card
    golds[cid] = {
        'id': cid,
        'master_prediction': cand_gold['master_predictions'][0]['statement_excerpt'],
        'outcome_record': cand_gold['outcome']['description'],
        'tradition': cand_gold['tradition'],
        'pollution': 'low', 'grade': 'A',
        'grade_note': cand_gold['grade_reason'],
    }

assert set(cards) == set(ORDER) and set(golds) == set(ORDER)

# 输入卡字段白名单断言＋禁用键递归零残留
for cid in ORDER:
    assert list(cards[cid].keys()) == INPUT_FIELDS, (cid, list(cards[cid].keys()))
    assert not banned_key_scan(cards[cid]), (cid, banned_key_scan(cards[cid]))
    assert golds[cid]['outcome_record'].strip(), cid
    assert golds[cid]['pollution'] == 'low' and golds[cid]['grade'] == 'A', cid
for cid in YJ_IDS + CZ2_IDS:
    assert golds[cid]['master_prediction'].strip(), cid
assert {c for c in ORDER if golds[c]['master_prediction'] is None} == set(pred_gap_cases)

# ---------- 第一道处置登记 ----------
stage1_disposition = {}
for cid in ORDER:
    hits = scan_stage1[cid]['content_hits'] + scan_stage1[cid]['fieldname_hits']
    paths = sorted({h[0].split('/')[1] if h[0].startswith('/') and len(h[0].split('/')) > 1
                    else h[0] for h in hits})
    if not hits:
        disp = '零命中'
    elif cid in ('QW-010', 'CZ2-001', 'CZ2-006'):
        disp = ('命中落在输入侧正文字段，经附条件改写处置（见报告 qw010_rewrite/'
                'cz2001_rewrite/cz2006_rewrite 前后对照存证），改写后第二道复扫零命中放行')
    else:
        disp = ('命中字段均为将被整项剥离的管理字段（notes），整项剥离不入卡；'
                '剥离后第二道复扫零命中放行')
    stage1_disposition[cid] = {'hit_fields': paths, 'disposition': disp}

# ---------- 第二道：建卡自校验逐卡扫描 ----------
scan_stage2 = {}
for cid in ORDER:
    ch = scan_content(cards[cid])
    fh = scan_field_names(cards[cid])
    scan_stage2[cid] = {'content_hits': ch, 'fieldname_hits': fh}
    assert not ch and not fh, (cid, ch, fh)  # 任一命中即中止，不交付

# ---------- 落盘 ----------
for cid in ORDER:
    with open(os.path.join(IN_DIR, f'{cid}.json'), 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
        f.write('\n')
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in ORDER:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')

read_cards = {fn[:-5]: load_json(os.path.join(IN_DIR, fn))
              for fn in os.listdir(IN_DIR) if fn.endswith('.json')}
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
assert set(read_cards) == set(ORDER) and len(read_cards) == 25
assert {g['id'] for g in read_golds} == set(ORDER) and len(read_golds) == 25
# 落盘后复扫（第二道对盘上文件重行）
for cid in ORDER:
    assert not scan_content(read_cards[cid]) and not scan_field_names(read_cards[cid]), cid
    assert not banned_key_scan(read_cards[cid]), cid

sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
sha_sum = subprocess.run(['sha256sum', gold_path], capture_output=True, text=True).stdout.split()[0]
assert sha_lib == sha_sum

# ---------- 构成统计 ----------
SOURCE_OF = {}
for cid in ORDER:
    if cid.startswith('QW'):
        SOURCE_OF[cid] = '曲炜《详批命例精解》'
    elif cid.startswith('WHY'):
        SOURCE_OF[cid] = '王虎应《六爻分类占验技法》'
    elif cid.startswith(('YJ2', 'YJ-')):
        SOURCE_OF[cid] = '《夷坚志》'
    elif cid.startswith('CZ2'):
        SOURCE_OF[cid] = '《春渚紀聞》'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)

report = {
    'round': 56, 'set': 'holdout20', 'built_by': '建集数据席（R56）',
    'ruling': 'runs/round56/PREREG-ADDENDUM-1.md',
    'T': 25, 'order': ORDER,
    'composition': {
        'by_source': dict(src_counts), 'by_tradition': dict(trad_counts),
        'non_yijian': 21,
        'note': ('逐卡 tradition 从候选登记逐字：bazi 12、liuyao 5、mengzhan 6、'
                 'fangji 1、xiangshu 1；ADDENDUM-1 §二体系构成行作六爻 9/梦占 3，'
                 '与逐卡登记不一致（YJ-001/004/006 登记 mengzhan、YJ2-012 登记 '
                 'fangji），本席从逐卡登记、差异标旗于封存日志')},
    'zero_reuse_recheck': {
        'holdout2_ids': 29, 'holdout3_19_gold_ids': 515, 'dev9_ids': 487,
        'used_union': 926,
        'method': '只对 id 集（phase2/splits2.json、holdout3–19 test_gold.jsonl 仅取 '
                  'id 字段、data/master-baseline-dev9.json 键集）；未打开任何已封存集'
                  '金标正文做内容比对（holdout19 金标正文未开、仅取 id）',
        'selected_hit_count': 0},
    'input_field_whitelist': INPUT_FIELDS,
    'qw010_rewrite': {
        'rule': '输入侧卫生：台账 setting 原文嵌成色限度句、含 R42 §5 二级标记「结局」；'
                '限度由金标 grade_note（outcome_note）全文承载，输入侧删该句（承 '
                'holdout19 YJ2-007 附条件改写先例，改写前后对照存证）',
        'before_context_input_side': ('函测：命主为 1986 年生少年（求测时约十六岁），'
                                      '父母为其求测；反馈所及仅少年期事件，非一生结局，'
                                      '入账时如实标此限度'),
        'after_context_input_side': '函测：命主为 1986 年生少年（求测时约十六岁），父母为其求测',
        'note': '被删限度句原文另在台账 outcome_note 与本卡金标 grade_note 中逐字并存'},
    'cz2001_rewrite': {
        'rule': '输入侧卫生：候选卡 question 原文含 R42 §5 二级标记「結局」（问句用词、'
                '非结局内容泄露）；输入侧改写一词，改写前后对照存证（承 holdout19 '
                'YJ2-007 先例），原候选卡文件不动',
        'before_question_input_side': '禱夢所問：去留當如何，此任結局如何？',
        'after_question_input_side': '禱夢所問：去留當如何，此任後事如何？'},
    'cz2006_rewrite': {
        'rule': '输入侧卫生：候选卡 question 原文含 R42 §5 二级标记「應驗」（问句用词）；'
                '输入侧改写为「主何吉凶」，改写前后对照存证，原候选卡文件不动',
        'before_question_input_side': '請言此先墓主何應驗？',
        'after_question_input_side': '請言此先墓主何吉凶？'},
    'strip_register': strip_register,
    'field_mapping_notes': field_mapping_notes,
    'master_prediction_gap': {
        'cases': pred_gap_cases,
        'count': len(pred_gap_cases),
        'reason': ('QW/WHY 开采台账（SUPPLY-MINING-quwei/wanghuying-r56.json）未单列'
                   '断语逐字字段：QW outcome_record 为断语释义与反馈合录、多例仅录'
                   '反馈段；WHY outcome_record 仅录应验情况。该 17 例金标 '
                   'master_prediction 置 null 并逐例 grade_note 明示，不臆补、'
                   '不以结局文冒充断语；提请主持自原书补录后方可开封判读。'
                   'YJ/CZ2 8 例断语逐字完具（候选金标 statement_excerpt）。')},
    'scan_stage1_candidate_prep': scan_stage1,
    'scan_stage1_disposition': stage1_disposition,
    'scan_stage2_card_selfcheck': scan_stage2,
    'scan_stage2_total_hits': sum(len(v['content_hits']) + len(v['fieldname_hits'])
                                  for v in scan_stage2.values()),
    'scan_stage3_host_verify': '主持验封道，非本席执行——留位：主持以独立脚本对 '
                               'holdout20/inputs/ 全部输入卡复扫，零命中方许封存日志落「验封通过」',
    'markers_source': '标记集逐字复制 runs/round42/PREREG.md §5（LEVEL1/LEVEL2/FIELD_BLACKLIST，见脚本头注释）',
    'gold_sha256': sha_lib, 'gold_sha256_sha256sum': sha_sum,
    'gold_sha256_double_read_match': sha_lib == sha_sum,
    'outputs_written': [f'holdout20/inputs/{c}.json' for c in ORDER] +
                       ['holdout20/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 25,
                  'stage2_total_hits': report['scan_stage2_total_hits'],
                  'pred_gap_count': len(pred_gap_cases),
                  'gold_sha256': sha_lib}, ensure_ascii=False))
