#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R58 建集数据席：按 PREREG-ADDENDUM（runs/round58/PREREG-ADDENDUM.md）写死选集
组建并封存 holdout21（T＝25）。

选集（附则 §一写死）：
- GSZ-003/005/009/015/016/017 ← runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json
- WHY-072/073/074/075/078/079 ← runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json
- QW-013/014/015/016/017 ← runs/round56/digestion/SUPPLY-MINING-quwei-r56.json
  （断语逐字以 data/holdout21-gold-supplement.md 补录件为准，附则 §二）
- QM-001–008 ← runs/round56/digestion/SUPPLY-MINING-qimen-r56.json
  ＋ runs/round58/digestion/QM-REVIEW-r58.json（eligible 判定以复核件为准）

口径承 holdout20 定式（runs/round56/build_holdout20_r56.py 先例）：
输入卡 schema {id, tradition, subject, context, question, setting, provenance,
redistributable, license_status, anchors}；金标 schema 同 holdout20
{id, master_prediction, outcome_record, tradition, pollution, grade, grade_note}
并按本轮派单加 provenance/license_status/redistributable（QW 例另加 editor_note）。
断语扫描：① 脚本逐字子串扫描（每例 master_prediction 与 outcome 的特征片段
对全部 input_side 文本零命中）；② 语义级抽查 ≥8 例（名单与结论入构建报告、
封存日志）；③ 主持复扫（本席不执行，报告留位）。
另行 h20 式内容级标记扫描（R42 PREREG §5 LEVEL1/LEVEL2/字段名黑名单＋禁用键
递归扫描）作输入卡卫生自校验，逐卡零命中方落盘。

只建卡与封存：不作断、不评分、不开封验收、不做 git 操作。
零复用只对 id 集（禁打开已封存集金标正文做内容比对；各 gold 仅取 id 字段）。
"""
import json, hashlib, os, re, shutil, subprocess
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'
R58 = os.path.join(BASE, 'runs/round58')
OUT_DIR = os.path.join(BASE, 'holdout21')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R58, 'build-holdout21-report-r58.json')

# ---------- 内容级标记集（逐字复制 R42 PREREG §5，同 holdout20 脚本） ----------
LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '斷曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']
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


# ---------- 选集（附则 §一写死，不得增减） ----------
GSZ_IDS = ['GSZ-003', 'GSZ-005', 'GSZ-009', 'GSZ-015', 'GSZ-016', 'GSZ-017']
WHY_IDS = ['WHY-072', 'WHY-073', 'WHY-074', 'WHY-075', 'WHY-078', 'WHY-079']
QW_IDS = ['QW-013', 'QW-014', 'QW-015', 'QW-016', 'QW-017']
QM_IDS = [f'QM-{i:03d}' for i in range(1, 9)]
ORDER = GSZ_IDS + WHY_IDS + QW_IDS + QM_IDS
assert len(ORDER) == 25 and len(set(ORDER)) == 25

INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status', 'anchors']

# ---------- 门：例级零复用复核（只对 id 集） ----------
used_sources = {}
h2_ids = set(load_json(os.path.join(ROOT, 'benchmark/phase2/splits2.json'))['holdout2'])
used_sources['phase2_splits2_holdout2'] = len(h2_ids)
gold_ids = set()
for i in list(range(3, 21)):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip():
                gold_ids.add(json.loads(line)['id'])  # 只取 id，不作内容比对
used_sources['holdout3_20_gold_ids'] = len(gold_ids)
input_ids = set()
for i in range(2, 21):
    d = os.path.join(BASE, f'holdout{i}/inputs')
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                input_ids.add(fn[:-5])
    d2 = os.path.join(BASE, f'holdout{i}-inputs')
    if os.path.isdir(d2):
        for fn in os.listdir(d2):
            if fn.endswith('.json'):
                input_ids.add(fn[:-5])
used_sources['holdout2_20_input_card_ids'] = len(input_ids)
dev_ids = set(load_json(os.path.join(BASE, 'data/master-baseline-dev9.json')).keys())
for dv in ('inputs-dev9', 'inputs-dev10', 'inputs-dev11', 'inputs-dev12', 'inputs'):
    d = os.path.join(BASE, dv)
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                dev_ids.add(fn[:-5])
used_sources['dev_pool_ids_dev9keys_plus_dev_input_dirs'] = len(dev_ids)
used_union = h2_ids | gold_ids | input_ids | dev_ids
reuse_hits = [cid for cid in ORDER if cid in used_union]
assert not reuse_hits, f'选例与已用并集相交（零复用门）：{reuse_hits}'

# ---------- 台账载入 ----------
gsz_mining = load_json(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
why_mining = load_json(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json'))
qw_mining = load_json(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-quwei-r56.json'))
qm_mining = load_json(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-qimen-r56.json'))
qm_review = load_json(os.path.join(R58, 'digestion/QM-REVIEW-r58.json'))
gsz_by = {e['provisional_id']: e for e in gsz_mining['entries']}
why_by = {e['provisional_id']: e for e in why_mining['entries']}
qw_by = {e['provisional_id']: e for e in qw_mining['entries']}
qm_by = {c['provisional_id']: c for c in qm_mining['cases']}
qm_rev_by = {c['provisional_id']: c for c in qm_review['cases']}

# ---------- QW 补录件解析（断语逐字以补录件为准） ----------
supp_text = open(os.path.join(BASE, 'data/holdout21-gold-supplement.md'), encoding='utf-8').read()
supp = {}
for m in re.finditer(r'^## (QW-\d{3})\s*$', supp_text, flags=re.M):
    cid = m.group(1)
    sec = supp_text[m.start():]
    nxt = re.search(r'^## ', sec[3:], flags=re.M)
    if nxt:
        sec = sec[:nxt.start() + 3]
    mp_m = re.search(r'\*\*master_prediction（逐字）\*\*：\s*\n```\n(.*?)\n```', sec, flags=re.S)
    oc_m = re.search(r'\*\*结局逐字（源 TXT 反馈段摘录）\*\*：\s*\n```\n(.*?)\n```', sec, flags=re.S)
    len_m = re.search(r'\*\*断语字数\*\*：(\d+)', sec)
    loc_m = re.search(r'\*\*出处定位\*\*：(.*)', sec)
    assert mp_m and oc_m and len_m, cid
    supp[cid] = {'master_prediction': mp_m.group(1), 'outcome_block': oc_m.group(1),
                 'stated_len': int(len_m.group(1)),
                 'location': loc_m.group(1).strip() if loc_m else ''}
    # 补录件字数自检（含换行口径：块正文＋末尾换行）
    blk = supp[cid]['master_prediction']
    assert len(blk) == supp[cid]['stated_len'] or len(blk) + 1 == supp[cid]['stated_len'], \
        (cid, len(blk), supp[cid]['stated_len'])
assert set(supp) == set(QW_IDS), set(supp)

QW_LINENO_NOTE = ('台账行号为折行计数口径，与源 TXT 物理行号不一致；定位以补录件'
                  '物理行号＋唯一锚句为准（补录件「行号标旗」登记，源文件 SHA-256 '
                  '与台账登记一致、确为同一文件）。')
QW16_EDITOR_NOTE = ('QW-016 性格第 8 条：原文误标「释：」起头，补录席按断语回收、'
                    '复原编号「8、」（编号序列 7→9 之间缺 8），断语正文不改'
                    '（补录件 QW-016 注记登记）。')

cards, golds = {}, {}
eligibility, strip_register, field_mapping_notes = {}, {}, {}

# ---------- GSZ/WHY 12 例（六爻） ----------
def build_liuyao(cid, e, book_short, base_note):
    inf = e['input_fields']
    chart = inf['chart']
    anchors = {'asked_at': inf['asked_at']}
    anchors.update(chart)  # 卦象逐字：本卦/变卦/动爻（有则）/六爻全列/伏神（有则）
    card = {
        'id': cid,
        'tradition': 'liuyao',
        'subject': e['subject'] if e['subject'] else '求测者（台账 subject 为空、原书未具名）',
        'context': f"占时：{inf['asked_at']}；{book_short}",
        'question': inf['question'],
        'setting': f"{e['source']}",
        'provenance': f"{e['source']}；底本为用户经学校图书馆提供，redistributable=false",
        'redistributable': False,
        'license_status': base_note,
        'anchors': anchors,
    }
    note = ''
    if e.get('grade_note'):
        note += e['grade_note'] + '；'
    note += f"污染判级：{e['pollution_note']}；"
    note += f"转录：{e['transcription']}（transcription_confidence={e['transcription_confidence']}）"
    gold = {'id': cid, 'master_prediction': e['master_prediction'],
            'outcome_record': e['outcome_record'], 'tradition': 'liuyao',
            'pollution': 'low', 'grade': 'A', 'grade_note': note,
            'provenance': card['provenance'],
            'license_status': card['license_status'], 'redistributable': False}
    return card, gold


for cid in GSZ_IDS:
    e = gsz_by[cid]
    ok = (e['grade'] == 'A' and e['pollution'] == 'low'
          and e['anchor_presence'] == 'present' and e['eligible_net'] is True
          and e['master_prediction'].strip() and e['outcome_record'].strip())
    eligibility[cid] = {'grade': e['grade'], 'pollution': e['pollution'],
                        'anchor_presence': e['anchor_presence'],
                        'eligible_net': e['eligible_net'],
                        'master_prediction_nonempty': bool(e['master_prediction'].strip()),
                        'pass': bool(ok), 'basis': 'SUPPLY-MINING-guaishuo-r57.json 台账逐字'}
    assert ok, f'资格断言不过：{cid}'
    cards[cid], golds[cid] = build_liuyao(
        cid, e, '《六爻卦例说真》卦例', '现代版权文本（文字版PDF），内部研究用')
    strip_register[cid] = ['pollution/pollution_note/anchor_presence/anchor_missing/'
                           'dedup_check/filters/outcome_type/outcome_record/'
                           'master_prediction（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('question←input_fields.question；context←asked_at＋书名组写'
                                '（台账无 context 原文，承 holdout20 WHY 组写先例）；'
                                'setting/provenance←台账 source 逐字；anchors←asked_at＋'
                                'input_fields.chart 全列逐字')

for cid in WHY_IDS:
    e = why_by[cid]
    ok = (e['grade'] == 'A' and e['pollution'] == 'low'
          and e['anchor_presence'] == 'present' and e['eligible_net'] is True
          and e['master_prediction'].strip() and e['outcome_record'].strip())
    eligibility[cid] = {'grade': e['grade'], 'pollution': e['pollution'],
                        'anchor_presence': e['anchor_presence'],
                        'eligible_net': e['eligible_net'],
                        'master_prediction_nonempty': bool(e['master_prediction'].strip()),
                        'pass': bool(ok), 'basis': 'SUPPLY-MINING-wanghuying-r57-r2.json 台账逐字'}
    assert ok, f'资格断言不过：{cid}'
    cards[cid], golds[cid] = build_liuyao(
        cid, e, '《六爻分类占验技法》分类占验例', '现代版权文本（扫描本），内部研究用')
    strip_register[cid] = ['pollution/pollution_note/anchor_presence/anchor_missing/'
                           'dedup_check/filters/outcome_type/outcome_record/'
                           'master_prediction（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('question←input_fields.question；context←asked_at＋书名组写'
                                '（台账无 context 原文，承 holdout20 WHY 组写先例）；'
                                'setting/provenance←台账 source 逐字；anchors←asked_at＋'
                                'input_fields.chart 全列逐字（含 moving_lines/fu_shen）')

# ---------- QW 5 例（八字） ----------
for cid in QW_IDS:
    e = qw_by[cid]
    s = supp[cid]
    # 结局交叉核对：台账 outcome_record 各段（去「反馈：/实际：」前缀）须见于补录件结局块
    # （补录件块含「（XXXX条）」席位标注，核对时剔除该标注）
    oc_block_clean = re.sub(r'（[^）]*条）', '', s['outcome_block'])
    for seg in e['outcome_record'].split('／'):
        seg_clean = re.sub(r'^(反馈|实际)：', '', seg.strip())
        assert seg_clean in oc_block_clean, (cid, seg_clean[:30])
    ok = (e['pollution'] == 'low' and e['anchor_presence'] == 'present'
          and s['master_prediction'].strip() and e['outcome_record'].strip()
          and all(str(e['filters'][k]).startswith('pass') for k in
                  ('verbatim_transcribable', 'independent_outcome', 'separable',
                   'pollution_non_high')))
    eligibility[cid] = {'grade': 'A（附则 §一全例 A 级；台账 filters 四项 pass、'
                                  'holdout20 同源 QW-001–012 已以 A 级建卡）',
                        'pollution': e['pollution'],
                        'anchor_presence': e['anchor_presence'],
                        'eligible_net': '台账无 eligible_net 字段；以 filters 四 pass＋'
                                        '附则选集写定为准',
                        'master_prediction_nonempty': bool(s['master_prediction'].strip()),
                        'master_prediction_source': 'data/holdout21-gold-supplement.md 补录件逐字'
                                                    f"（字数自检 {len(s['master_prediction'])}"
                                                    f"／登记 {s['stated_len']}，含换行口径相符）",
                        'outcome_crosscheck': '台账 outcome_record 各段逐段见于补录件结局块，一致',
                        'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-quwei-r56.json 台账＋holdout21-gold-supplement.md'}
    assert ok, f'资格断言不过：{cid}'
    inf = e['input_fields']
    subj, ctx, prov = inf['subject'], inf['context'], inf['provenance']
    card = {
        'id': cid,
        'tradition': 'bazi',
        'subject': f"{subj['name_or_desc']}；{subj['basic_info']}",
        'context': ctx['setting'],
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
    note = '作者自选断准集、结局命主自报（无第三方核实）；'
    if e.get('outcome_note'):
        note += e['outcome_note'] + '；'
    note += f"锚点：{e['anchor_note']}；"
    note += ('转录：TXT 转录本（转录出处不明、繁简混排、个别转录误字照录，'
             '见 DIGEST-bazi-quwei-r56 登记）；')
    note += ('断语经 R58 补录席自源 TXT 补录（transcription=verbatim、confidence=0.95），'
             '见 data/holdout21-gold-supplement.md')
    editor_note = QW_LINENO_NOTE + (QW16_EDITOR_NOTE if cid == 'QW-016' else '')
    gold = {'id': cid, 'master_prediction': s['master_prediction'],
            'outcome_record': e['outcome_record'], 'tradition': 'bazi',
            'pollution': 'low', 'grade': 'A', 'grade_note': note,
            'provenance': (f"断语出处：{s['location']}（补录件物理行号）；"
                           f"台账 provenance：{prov['book']}·{prov['location']}；"
                           f"{prov['edition']}"),
            'license_status': card['license_status'], 'redistributable': False,
            'editor_note': editor_note}
    cards[cid] = card
    golds[cid] = gold
    strip_register[cid] = ['pollution/pollution_note/anchor_presence/anchor_note/'
                           'dedup_check/filters/outcome_record（台账管理与金标侧字段，'
                           '不入输入卡）；input_fields 之 id/tradition 与 subject/context/'
                           'provenance 嵌套子字段经字段映射摊平入卡（子字段文本逐字）']
    field_mapping_notes[cid] = ('subject←name_or_desc＋basic_info；context←context.setting；'
                                'question←context.question；setting←source＋context.asked_at；'
                                'provenance←provenance.book＋location＋edition；'
                                'anchors←subject.birth_info_verbatim/gender＋context.attachments'
                                '（birth 四元组＋sex，承 holdout20 QW 口径）')

# ---------- QM 8 例（奇门） ----------
QM007_REWRITE = None
for cid in QM_IDS:
    c = qm_by[cid]
    r = qm_rev_by[cid]
    src = c['source']
    ok = (r['eligible_optional'] is True and r['pollution_reviewed'] == 'low'
          and r['anchor_reviewed'] == 'present'
          and c['pollution'] == 'low' and c['anchor_presence'] == 'present'
          and c['master_prediction_verbatim'].strip()
          and c['outcome_record'].strip())
    eligibility[cid] = {'grade': 'A（QM 复核件 eligible_optional=true；台账建池口径'
                                  'A 级入账，附则 §一全例 A 级）',
                        'pollution': r['pollution_reviewed'],
                        'anchor_presence': r['anchor_reviewed'],
                        'eligible_optional_review': r['eligible_optional'],
                        'master_prediction_nonempty': bool(c['master_prediction_verbatim'].strip()),
                        'pass': bool(ok),
                        'basis': 'SUPPLY-MINING-qimen-r56.json 台账＋QM-REVIEW-r58.json 复核件'}
    assert ok, f'资格断言不过：{cid}'
    inf = c['input_fields']
    card_context = inf['context']
    if cid == 'QM-007':
        # 附条件改写（承 holdout20 附条件改写先例）：台账 context 原文嵌伤情细节
        # （尾椎骨摔伤、大小便失禁——张断后由小郑证实者）与「不入输入侧背景以免
        # 泄断」注记句；台账 notes 亦明载该细节不入输入。本席按台账注记删此细节
        # 与注记句，改写前后对照存证于构建报告 qm007_rewrite；细节只入命主背景
        # 之 question 原文既载部分（电线杆摔伤入院、已手术，为求测者自述）不动。
        old = ('1996年5月9日下午4点20分，小郑来测侄子摔伤（尾椎骨摔伤、大小便失禁、'
               '已手术）之预后与出院时间；伤情细节为张断后由小郑证实者（「从电线杆上'
               '掉下来、把尾椎骨摔伤了」），不入输入侧背景以免泄断。')
        assert card_context == old, card_context
        card_context = '1996年5月9日下午4点20分，小郑来测侄子摔伤之预后与出院时间。'
        QM007_REWRITE = {'before_context_input_side': old,
                         'after_context_input_side': card_context,
                         'rule': '台账 context 自带「不入输入侧背景以免泄断」注记、台账 notes '
                                 '同旨；删张断后证实之伤情细节与注记句，对照存证，原台账不动'}
    anchors = {'cast_time_verbatim': inf['cast_time_verbatim']}
    if 'boards' in inf:
        anchors['boards'] = inf['boards']
    else:
        anchors['board'] = inf['board']
    if 'board_basis' in inf:
        anchors['board_basis'] = inf['board_basis']
    setting = (f"{src['book']}（{src['author']}著）·{src['section']}；"
               f"起局时间：{inf['cast_time_verbatim']}")
    if 'board_basis' in inf:
        setting += '；起局基准：event_time（按事件举行时间起局，台账 board_basis 逐字登记）'
    provenance = (f"{src['book']}（{src['author']}著，{src['publisher']}，{src['edition']}）"
                  f"·{src['section']}，印刷页{src['printed_pages']}；"
                  f"用户经学校图书馆提供；redistributable=false")
    card = {
        'id': cid,
        'tradition': 'qimen',
        'subject': inf['querent'],
        'context': card_context,
        'question': inf['question'],
        'setting': setting,
        'provenance': provenance,
        'redistributable': False,
        'license_status': '现代版权文本（扫描本），内部研究用',
        'anchors': anchors,
    }
    note = (f"锚点：{c['anchor_note']}；复核：{r['anchor_basis']}；"
            f"转录：visual（多模态视觉读图，transcription_confidence="
            f"{src['transcription_confidence']}）；占者：{inf['caster']}。")
    if c.get('notes'):
        note += f"台账注记：{c['notes']}"
    gold = {'id': cid, 'master_prediction': c['master_prediction_verbatim'],
            'outcome_record': c['outcome_record'], 'tradition': 'qimen',
            'pollution': 'low', 'grade': 'A', 'grade_note': note,
            'provenance': provenance,
            'license_status': card['license_status'], 'redistributable': False}
    cards[cid] = card
    golds[cid] = gold
    strip_register[cid] = ['pollution/pollution_reason/anchor_presence/anchor_note/'
                           'dedup_check/notes/master_prediction_verbatim/outcome_record'
                           '（台账管理与金标侧字段，不入输入卡）；input_fields 之 '
                           'querent/caster/question/context/cast_time/board 经字段映射入卡']
    field_mapping_notes[cid] = ('subject←input_fields.querent；question/context←input_fields '
                                '逐字；setting←source.book/author/section＋cast_time_verbatim '
                                '组写；anchors←cast_time_verbatim＋board/boards 全载逐字'
                                '（局式逐字：header_verbatim＋九宫 palaces＋center_palace_5）')

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

# ---------- 断语扫描①：逐字子串特征片段扫描 ----------
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


scan1 = {}
for cid in ORDER:
    card_text = json.dumps(cards[cid], ensure_ascii=False)
    hits = []
    for field in ('master_prediction', 'outcome_record'):
        for fr in fragments(golds[cid][field]):
            if fr in card_text:
                hits.append([field, fr])
    scan1[cid] = {'fragment_count': len(fragments(golds[cid]['master_prediction'])) +
                  len(fragments(golds[cid]['outcome_record'])),
                  'hits': hits}
    assert not hits, (cid, hits[:5])
scan1_total_hits = sum(len(v['hits']) for v in scan1.values())

# ---------- 输入卡卫生自校验（h20 第二道口径：内容级标记＋字段名黑名单） ----------
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

read_cards = {fn[:-5]: load_json(os.path.join(IN_DIR, fn))
              for fn in os.listdir(IN_DIR) if fn.endswith('.json')}
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
assert set(read_cards) == set(ORDER) and len(read_cards) == 25
assert {g['id'] for g in read_golds} == set(ORDER) and len(read_golds) == 25
# 落盘后复扫：扫描①与标记扫描对盘上文件重行
for cid in ORDER:
    card_text = json.dumps(read_cards[cid], ensure_ascii=False)
    g = next(x for x in read_golds if x['id'] == cid)
    for field in ('master_prediction', 'outcome_record'):
        for fr in fragments(g[field]):
            assert fr not in card_text, (cid, field, fr)
    assert not scan_content(read_cards[cid]) and not scan_field_names(read_cards[cid]), cid
    assert not banned_key_scan(read_cards[cid]), cid

sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
sha_sum = subprocess.run(['sha256sum', gold_path], capture_output=True, text=True).stdout.split()[0]
assert sha_lib == sha_sum

# ---------- 验收快照：封存时点活 method 全目录复制＋逐文件 SHA-256 清单 ----------
SNAP_DIR = os.path.join(R58, 'kb-snapshot-holdout21')
if os.path.exists(SNAP_DIR):
    shutil.rmtree(SNAP_DIR)
shutil.copytree(os.path.join(BASE, 'method'), SNAP_DIR)
snap_entries = []
for root, dirs, files in os.walk(SNAP_DIR):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, SNAP_DIR)
        if rel == 'sha256.txt':
            continue
        snap_entries.append((rel, hashlib.sha256(open(p, 'rb').read()).hexdigest()))
with open(os.path.join(SNAP_DIR, 'sha256.txt'), 'w', encoding='utf-8') as f:
    for rel, h in snap_entries:
        f.write(f'{h}  {rel}\n')
snap_count = len(snap_entries)

# ---------- 构成统计 ----------
SOURCE_OF = {}
for cid in ORDER:
    if cid.startswith('GSZ'):
        SOURCE_OF[cid] = '王虎应《六爻卦例说真》'
    elif cid.startswith('WHY'):
        SOURCE_OF[cid] = '王虎应《六爻分类占验技法》（二轮）'
    elif cid.startswith('QW'):
        SOURCE_OF[cid] = '曲炜《详批命例精解》'
    elif cid in ('QM-001', 'QM-002', 'QM-003', 'QM-004', 'QM-005'):
        SOURCE_OF[cid] = '杜新会《奇门遁甲现代实例精解》'
    else:
        SOURCE_OF[cid] = '张志春《神奇之门——奇门遁甲大解谜》'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)

report = {
    'round': 58, 'set': 'holdout21', 'built_by': '建集数据席（R58）',
    'ruling': 'runs/round58/PREREG-ADDENDUM.md',
    'T': 25, 'order': ORDER,
    'composition': {'by_source': dict(src_counts), 'by_tradition': dict(trad_counts),
                    'non_liuyao': 13, 'non_yijian': 25,
                    'max_single_source': max(src_counts.values())},
    'eligibility_assertions': eligibility,
    'eligibility_all_pass': True,
    'zero_reuse_recheck': {
        'sources': used_sources, 'used_union': len(used_union),
        'method': '只对 id 集（phase2/splits2.json holdout2、holdout3–20 test_gold.jsonl '
                  '仅取 id 字段、holdout2–20 inputs 与 *-inputs 目录文件名、'
                  'data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs '
                  '目录文件名）；未打开任何已封存集金标正文做内容比对',
        'selected_hit_count': 0, 'selected_hits': reuse_hits},
    'input_field_whitelist': INPUT_FIELDS,
    'qm007_rewrite': QM007_REWRITE,
    'strip_register': strip_register,
    'field_mapping_notes': field_mapping_notes,
    'scan1_verbatim_fragment': {
        'method': '每例 master_prediction 与 outcome_record 的特征片段（标点分句整句'
                  '（≥8 字）＋去空白 12 字滑动窗口全集）对该例输入卡全文本逐字子串'
                  '扫描，零命中方落盘；落盘后对盘上文件重行仍零命中',
        'per_case': scan1, 'total_hits': scan1_total_hits},
    'scan_marker_selfcheck': {
        'method': 'h20 第二道口径：R42 PREREG §5 内容级一级/二级标记＋字段名黑名单'
                  '＋禁用键集对 25 张输入卡全字段递归扫描',
        'per_case': scan_markers,
        'total_hits': sum(len(v['content_hits']) + len(v['fieldname_hits'])
                          for v in scan_markers.values())},
    'scan2_semantic_spotcheck': '见封存日志登记名单（建集席逐例读卡人工核）',
    'scan3_host_rescan': '主持验封道，非本席执行——留位：主持以独立脚本对 '
                         'holdout21/inputs/ 全部输入卡复扫，零命中方许封存日志落「验封通过」',
    'gold_sha256': sha_lib, 'gold_sha256_sha256sum': sha_sum,
    'gold_sha256_double_read_match': sha_lib == sha_sum,
    'kb_snapshot': {'dir': 'runs/round58/kb-snapshot-holdout21/',
                    'file_count': snap_count,
                    'sha256_list': 'runs/round58/kb-snapshot-holdout21/sha256.txt',
                    'files': [rel for rel, _ in snap_entries]},
    'outputs_written': [f'holdout21/inputs/{c}.json' for c in ORDER] +
                       ['holdout21/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 25, 'scan1_total_hits': scan1_total_hits,
                  'marker_total_hits': report['scan_marker_selfcheck']['total_hits'],
                  'used_union': len(used_union), 'snapshot_files': snap_count,
                  'gold_sha256': sha_lib}, ensure_ascii=False))
