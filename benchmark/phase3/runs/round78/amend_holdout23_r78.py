#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R78 holdout23 封存裁处执行席脚本（主持裁处五项，逐项执行、不改裁处）。

1. DS-013 节题中性化：setting/provenance 删「、做功等级大的四柱」全文（承 holdout22 §九.4 DS-011 体例），其余字串一字不动；金标 DS-013 行不动。
2. DS-014 节题中性化：同法删「、普通四柱」；金标行不动。
3. DS-015 中性化补入、DS-019 退出：按台账 SUPPLY-MINING-duanshi-r76.json 逐字、承 build_holdout23_r78.py DS 建卡规格建卡建标；
   节题「差命」在卡面各字段全文删除只留章节定位（逐处登记）；金标侧 provenance 照台账原登记不中性化；
   精确删除 DS-019 输入卡文件与金标行；金标行序照 id 序重整；DS-015 过已用并集逐 id 滤复核。
4. ZCB-006/007/011 照建不动、标旗维持，裁处理由原样记入封存日志。
5. 封存日志追加「主持裁处」节（改前/改后逐字对照、构成全表更新、复核结论）。
改后复验：变更卡逐卡重行片段/标记/禁用键/白名单扫描；全集 27 卡复扫（第二道口径，独立实现）；
金标 SHA-256 双读（hashlib＋sha256sum 子进程）。不做 git 操作；不打开 judging/、predictions/、已开封集金标正文
（holdout22/test_gold.jsonl 仅取 id 列，承构建脚本已用并集口径）。
"""
import hashlib, json, os, re, subprocess, sys

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R78 = os.path.join(BASE, 'runs/round78')
DIG76 = os.path.join(BASE, 'runs/round76/digestion')
ROOT = '/home/hatch/workspace/divination'
IN_DIR = os.path.join(BASE, 'holdout23/inputs')
GOLD = os.path.join(BASE, 'holdout23/test_gold.jsonl')
SEAL_LOG = os.path.join(BASE, 'data/holdout23-seal-log.md')
OLD_SHA = '301d37d56c6b5fe88ad5d0f6bc022b3efba5bdbb443fee8e6cce7c7741cbe55e'

# 标记集承 runs/round42/PREREG.md §5（与封存席复扫脚本常量逐字一致）
LEVEL1 = ['断语线索', '断曰', '断語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']
BANNED = {'grade_note', 'grade_suggestion', 'grade_reason', 'contamination',
          'contamination_suggestion', 'contamination_reason',
          'contamination_rationale', 'outcome', 'outcome_record', 'outcome_grade',
          'master_predictions', 'master_prediction', 'master_assertion',
          'passage_full', 'record_status', 'notes', 'master', 'gold', 'gold_side',
          'answer', 'seal_eligible', 'holdout_eligible', 'review', 'pollution',
          'pollution_note', 'anchor_presence', 'anchor_missing', 'anchor_check',
          'anchor_note', 'dedup_check', 'filters', 'outcome_type', 'outcome_note',
          'transcription', 'provisional_id', 'source', 'language', 'grade'}
INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status', 'anchors']
NEW_IDS = ['DS-013', 'DS-014', 'DS-015', 'DS-016', 'DS-017', 'DS-018',
           'GSZ-028', 'GSZ-030', 'GSZ-031', 'GSZ-032', 'GSZ-033',
           'QM-015', 'QM-016', 'QM-018', 'QM-019', 'QM-020',
           'QM-204', 'QM-205', 'QM-304', 'QM-305', 'QM-306',
           'ZCB-006', 'ZCB-007', 'ZCB-008', 'ZCB-009', 'ZCB-010', 'ZCB-011']
CEZI = {c for c in NEW_IDS if c.startswith('ZCB-')}


def load_json(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def walk_strings(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f'{path}[{i}]')
    elif isinstance(obj, str):
        yield path, obj


def walk_keys(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield f'{path}/{k}', k
            yield from walk_keys(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_keys(v, f'{path}[{i}]')


def fragments(text):
    out = set()
    for clause in re.split(r'[。！？；\n]', text):
        c = clause.strip('「」『』“”‘’"\' ')
        if len(c) >= 8:
            out.add(c)
    t = re.sub(r'\s+', '', text)
    for i in range(0, max(0, len(t) - 11)):
        out.add(t[i:i + 12])
    return out


def scan_card(cid, card, gold):
    """单卡四项扫描：片段（断语/结局逐字子串）、内容级标记、禁用键递归、字段白名单/键序。"""
    res = {}
    res['whitelist_keyorder_ok'] = list(card.keys()) == INPUT_FIELDS
    marker_hits = []
    for path, s in walk_strings(card):
        for lvl, markers in (('L1', LEVEL1), ('L2', LEVEL2)):
            for m in markers:
                if m in s:
                    marker_hits.append([path, lvl, m])
    res['marker_hits'] = marker_hits
    res['fieldname_hits'] = [[p, k] for p, k in walk_keys(card)
                             if any(f in k for f in FIELD_BLACKLIST)]
    res['banned_key_hits'] = [p for p, k in walk_keys(card) if k in BANNED]
    card_text = json.dumps(card, ensure_ascii=False)
    res['master_fragment_hits'] = sorted(
        f for f in fragments(gold['master_prediction']) if f in card_text)
    res['outcome_fragment_hits'] = sorted(
        f for f in fragments(gold['outcome_record']) if f in card_text)
    short = set()
    mpn = re.sub(r'\s+', '', gold['master_prediction'])
    for n in (10, 9, 8):
        for i in range(0, len(mpn) - n + 1):
            sub = mpn[i:i + n]
            if sub in card_text and not any(sub in s or s in sub for s in short):
                short.add(sub)
    res['short_substring_info'] = sorted(short)
    res['pass'] = (res['whitelist_keyorder_ok'] and not marker_hits
                   and not res['fieldname_hits'] and not res['banned_key_hits']
                   and not res['outcome_fragment_hits']
                   and (cid in CEZI or not res['master_fragment_hits']))
    return res


# ================= 前置核验 =================
pre_sha = hashlib.sha256(open(GOLD, 'rb').read()).hexdigest()
assert pre_sha == OLD_SHA, f'动手前金标 SHA 不合：{pre_sha}'
seal_log_size_before = os.path.getsize(SEAL_LOG)
gold_raw_lines = [l for l in open(GOLD, encoding='utf-8').read().splitlines() if l.strip()]
assert len(gold_raw_lines) == 27
gold_before = {}
for l in gold_raw_lines:
    g = json.loads(l)
    gold_before[g['id']] = (l, g)
assert 'DS-019' in gold_before and 'DS-015' not in gold_before

# ================= 已用并集复算（承 build_holdout23_r78.py 口径，逐 id） =================
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
gold_ids, gold_per_set = set(), {}
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
assert len(used_union) == 1004, len(used_union)
ds015_zero_reuse = 'DS-015' not in used_union
assert ds015_zero_reuse

# ================= 台账 DS-015 / DS-019 =================
ds_mining = load_json(os.path.join(DIG76, 'SUPPLY-MINING-duanshi-r76.json'))
ds_by = {r['case_id']: r for r in ds_mining['records']}
r15, r19 = ds_by['DS-015'], ds_by['DS-019']
ok15 = (r15['eligible_net'] is True and r15['anchor_status'] == 'present'
        and r15['contamination_pre'] == 'low'
        and all(str(v).startswith('pass') for v in r15['filters'].values())
        and r15['master_assertion'].strip() and r15['outcome'].strip())
assert ok15, 'DS-015 资格复断言不过'
assert '差命' in r15['source']

# ================= 裁处 1/2：DS-013 / DS-014 中性化（内存预演） =================
NEUT = {'DS-013': '、做功等级大的四柱', 'DS-014': '、普通四柱'}
TITLE_ONLY = {'DS-013': '做功等级大的四柱', 'DS-014': '普通四柱'}
neut_register = {}
new_card_text = {}
for cid, delstr in NEUT.items():
    p = os.path.join(IN_DIR, f'{cid}.json')
    raw = open(p, encoding='utf-8').read()
    cnt = raw.count(delstr)
    assert cnt == 2, (cid, cnt)  # setting 与 provenance 各 1 处
    card0 = json.loads(raw)
    card1 = json.loads(raw.replace(delstr, ''))
    assert TITLE_ONLY[cid] not in json.dumps(card1, ensure_ascii=False)
    neut_register[cid] = {
        'deleted_string': delstr, 'occurrences_in_file': cnt,
        'setting_before': card0['setting'], 'setting_after': card1['setting'],
        'provenance_before': card0['provenance'],
        'provenance_after': card1['provenance'],
        'subject_unchanged': card0['subject'] == card1['subject'],
        'other_fields_byte_identical_except_two': True}
    new_card_text[cid] = raw.replace(delstr, '')
assert neut_register['DS-013']['subject_unchanged']


# ================= 裁处 3：DS-015 建卡建标（内存预演，承构建脚本 DS 规格） =================
src15 = r15['source']
neut15 = src15.replace('、差命', '')
assert '差命' not in neut15 and src15.count('、差命') == 1
inf15 = r15['input_side']
card15 = {
    'id': 'DS-015', 'tradition': 'bazi',
    'subject': inf15['subject'],
    'context': f"《段氏理象学》命例（{r15['composition_type']}）；四柱载于 anchors",
    'question': '就此四柱命造求测（原书命例体例，无独立问句原文载录）',
    'setting': neut15,
    'provenance': f"{neut15}；底本为用户经学校图书馆提供，redistributable=false",
    'redistributable': False,
    'license_status': '现代版权文本（扫描图 PDF），内部研究用',
    'anchors': {'pillars': inf15['pillars'],
                'pillars_verbatim': inf15['pillars_verbatim'],
                'gender': inf15['gender']},
}
note15 = (f"入账口径：eligible_net=true、锚点 present、contamination low、四滤全 pass；"
          f"锚点：{r15['anchor_note']}；污染：{r15['contamination_note']}；"
          f"转录：visual（confidence={r15['transcription']['confidence']}，"
          f"{r15['transcription']['note']}）；断语为原书断语逐字摘录，"
          f"多段以／分隔（台账摘录分隔符）")
if r15.get('verdict_note'):
    note15 += f"；台账 verdict_note：{r15['verdict_note']}"
gold15 = {'id': 'DS-015', 'master_prediction': r15['master_assertion'],
          'outcome_record': r15['outcome'], 'tradition': 'bazi',
          'pollution': 'low', 'grade': 'A', 'grade_note': note15,
          'provenance': f"{src15}；底本为用户经学校图书馆提供，redistributable=false",
          'license_status': card15['license_status'],
          'redistributable': False}
# 「差命」在 DS-015 卡面各字段的出现处登记（中性化前口径：字段值承台账原串者）
ds015_title_locations = []
pre15 = {'setting': src15, 'provenance': f"{src15}；底本为用户经学校图书馆提供，redistributable=false"}
for k, v in pre15.items():
    if '差命' in v:
        ds015_title_locations.append(k)
for path, s in walk_strings(card15):
    assert '差命' not in s, path  # 中性化后卡面零残留
assert ds015_title_locations == ['setting', 'provenance']
# 金标侧 provenance 照台账原登记、不中性化（含「差命」原样）
assert '差命' in gold15['provenance']

# 新金标（内存）：删 DS-019 行、增 DS-015 行、行序照 id 序重整；未动行原始行文逐字保留
new_lines = {}
for gid, (raw_l, _g) in gold_before.items():
    if gid != 'DS-019':
        new_lines[gid] = raw_l
new_lines['DS-015'] = json.dumps(gold15, ensure_ascii=False)
assert sorted(new_lines) == NEW_IDS
gold_after = {gid: json.loads(l) for gid, l in new_lines.items()}

# ================= 变更卡内存预扫 =================
pre_scan = {}
for cid in ('DS-013', 'DS-014'):
    pre_scan[cid] = scan_card(cid, json.loads(new_card_text[cid]), gold_before[cid][1])
pre_scan['DS-015'] = scan_card('DS-015', card15, gold15)
for cid, r in pre_scan.items():
    assert r['pass'], (cid, r)
    assert not r['master_fragment_hits'] and not r['outcome_fragment_hits'], cid

# ================= 落盘变更 =================
for cid in ('DS-013', 'DS-014'):
    with open(os.path.join(IN_DIR, f'{cid}.json'), 'w', encoding='utf-8') as f:
        f.write(new_card_text[cid])
with open(os.path.join(IN_DIR, 'DS-015.json'), 'w', encoding='utf-8') as f:
    json.dump(card15, f, ensure_ascii=False, indent=2)
    f.write('\n')
ds019_card_path = os.path.join(IN_DIR, 'DS-019.json')  # 精确路径删除（禁通配）
assert os.path.isfile(ds019_card_path)
os.remove(ds019_card_path)
assert not os.path.exists(ds019_card_path)
with open(GOLD, 'w', encoding='utf-8') as f:
    for gid in NEW_IDS:
        f.write(new_lines[gid] + '\n')

# 未动金标行逐行字节无损自检（26 行原始行文与改前一致）
lines_now = [l for l in open(GOLD, encoding='utf-8').read().splitlines() if l.strip()]
assert len(lines_now) == 27
for l in lines_now:
    g = json.loads(l)
    if g['id'] not in ('DS-015',):
        assert l == gold_before[g['id']][0], g['id']
assert [json.loads(l)['id'] for l in lines_now] == NEW_IDS

# ================= 改后复验：盘上全集 27 卡复扫（第二道口径） =================
disk_golds = {}
for l in lines_now:
    g = json.loads(l)
    disk_golds[g['id']] = g
full_scan, full_failures = {}, []
for cid in NEW_IDS:
    card = load_json(os.path.join(IN_DIR, f'{cid}.json'))
    r = scan_card(cid, card, disk_golds[cid])
    full_scan[cid] = r
    if not r['pass']:
        full_failures.append(cid)
tot = {
    'marker_hits': sum(len(v['marker_hits']) for v in full_scan.values()),
    'fieldname_hits': sum(len(v['fieldname_hits']) for v in full_scan.values()),
    'banned_key_hits': sum(len(v['banned_key_hits']) for v in full_scan.values()),
    'outcome_fragment_hits': sum(len(v['outcome_fragment_hits']) for v in full_scan.values()),
    'master_fragment_hits_noncezi': sum(
        len(v['master_fragment_hits']) for k, v in full_scan.items() if k not in CEZI),
    'master_fragment_hits_cezi': {k: v['master_fragment_hits']
                                  for k, v in full_scan.items()
                                  if k in CEZI and v['master_fragment_hits']},
    'whitelist_failures': [k for k, v in full_scan.items()
                           if not v['whitelist_keyorder_ok']],
}
assert not full_failures, full_failures
assert tot['marker_hits'] == 0 and tot['fieldname_hits'] == 0
assert tot['banned_key_hits'] == 0 and tot['outcome_fragment_hits'] == 0
assert tot['master_fragment_hits_noncezi'] == 0 and not tot['whitelist_failures']
# 测字既知命中仅 ZCB-011 一件（封存日志 §四已分类登记，本轮照建不动）
assert tot['master_fragment_hits_cezi'] == {
    'ZCB-011': ['子勿死，邊吉乃周字也']}, tot['master_fragment_hits_cezi']
changed_scan = {cid: full_scan[cid] for cid in ('DS-013', 'DS-014', 'DS-015')}
for cid, r in changed_scan.items():
    assert not r['marker_hits'] and not r['fieldname_hits'] and not r['banned_key_hits']
    assert not r['master_fragment_hits'] and not r['outcome_fragment_hits']
    assert r['whitelist_keyorder_ok']


# ================= 金标 SHA-256 双读 =================
sha_lib = hashlib.sha256(open(GOLD, 'rb').read()).hexdigest()
sha_sum = subprocess.run(['sha256sum', GOLD], capture_output=True,
                         text=True).stdout.split()[0]
assert sha_lib == sha_sum
gold_bytes = os.path.getsize(GOLD)

# ================= 构成复断言 =================
from collections import Counter
SRC_OF = {}
for cid in NEW_IDS:
    if cid.startswith('DS-'):
        SRC_OF[cid] = '段建业《段氏理象学》'
    elif cid in ('QM-015', 'QM-016', 'QM-018', 'QM-019', 'QM-020'):
        SRC_OF[cid] = '张志春《开悟之门》'
    elif cid in ('QM-204', 'QM-205'):
        SRC_OF[cid] = '刘文元《奇门启悟》'
    elif cid in ('QM-304', 'QM-305', 'QM-306'):
        SRC_OF[cid] = '石建国《奇门遁甲最新实例解析》'
    elif cid.startswith('ZCB-'):
        SRC_OF[cid] = '《字触补》（《四库未收书辑刊》陆辑第拾捌册）'
    else:
        SRC_OF[cid] = '王虎应《六爻卦例说真》'
trad_of = {cid: disk_golds[cid]['tradition'] for cid in NEW_IDS}
trad_counts = Counter(trad_of.values())
src_counts = Counter(SRC_OF.values())
assert len(NEW_IDS) == 27 and max(trad_counts.values()) * 2 <= 27
assert max(src_counts.values()) * 2 <= 27 and len(src_counts) == 6
assert 27 - trad_counts['liuyao'] >= 13
assert all(disk_golds[c]['pollution'] == 'low' for c in NEW_IDS)

# ================= 封存日志追加「主持裁处」节 =================
n13, n14 = neut_register['DS-013'], neut_register['DS-014']
cezi_master_hits_str = '；'.join(
    f"{k}：{'、'.join(v)}" for k, v in tot['master_fragment_hits_cezi'].items())
sec = f"""
## 八、主持裁处（R78 主持裁处执行席，2026-10-31）

本节为封存后主持裁处之执行登记，以 append 追加，原 §一–§七一字未动。执行脚本 `runs/round78/amend_holdout23_r78.py`、登记件 `runs/round78/amend-holdout23-register-r78.json`。前置核验：动手前金标 SHA-256 实测 `{OLD_SHA}`，与封存日志 §首定版读数及主持给定值一致；快照 `kb-snapshot-holdout23` 未动。本席只执行裁处：不作断、不评分、未开封验收、未做 git 操作。

### 八.1 五项裁处执行

1. **DS-013 节题中性化——已执行**（逐字对照见 §八.2）。`holdout23/inputs/DS-013.json` 的 setting 与 provenance 各 1 处（全卡共 2 处），删原书第六章小节题全文「做功等级大的四柱」（连同其前「、」），定位只留「第六章第一节二」与「例六」，其余字串一字不动（承 holdout22 §九.4 DS-011 体例）；subject「匿名乾造（执法部门高官）」照裁处不动。金标 DS-013 行一字未动（未动行逐行字节无损自检通过）。
2. **DS-014 节题中性化——已执行**（逐字对照见 §八.2）。同法删节题全文「普通四柱」（连同其前「、」），setting 与 provenance 各 1 处，定位只留「第六章第一节二」与「例五」；金标 DS-014 行一字未动。
3. **DS-015 中性化补入、DS-019 退出——已执行**。按台账 `runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json` 之 DS-015 记录逐字、承 `build_holdout23_r78.py` DS 建卡规格建卡（字段白名单与键序同现 DS 各卡；subject←input_side.subject 逐字；anchors←input_side pillars/pillars_verbatim/gender 逐字；context/question 组写口径同现 DS 各卡）与金标行（master_prediction/outcome_record 自台账 master_assertion/outcome 逐字取录）。节题「差命」在卡面出现处共 2 处——setting 1 处、provenance 1 处（均承台账 source），逐处全文删除（连同其前「、」）、只留章节定位「第六章第一节二」与「例五」（逐字对照见 §八.2）；卡面其余字段经逐字段检索无该题字串，中性化后全卡「差命」子串零残留。**金标侧 provenance 照台账原登记、不中性化**（含「差命」原样，承 holdout22 §九.1「金标侧 provenance 照原登记」口径）。同步精确删除 DS-019 输入卡文件（精确路径 `holdout23/inputs/DS-019.json`，非通配删除）与金标 DS-019 行；金标行序照 id 序重整（27 行，未动 26 行原始行文逐字无损、仅行序与一删一增）。DS-015 资格复断言全过（eligible_net＝true、anchor_status＝present、contamination_pre＝low、filters 四项全 pass、断语/结局逐字非空）。
4. **ZCB-006／ZCB-007／ZCB-011 照建不动、标旗维持——已登记**。三卡与对应金标行一字未动（在未动行字节无损自检范围内）。裁处理由（主持原文，原样记入）：「拆分过程原文系附则明列之输入侧锚点载荷，与 holdout22 ZCB 四例同口径；ZCB-011 语出梦中神告、属叙事内谶语即待释之占象本身；ZCB-003 之排除系其已有专门裁处在案，与此三件情形有别。」
5. **本节即裁处第 5 项之执行**：1–4 项全文要点、逐处改前/改后逐字对照（§八.2）、构成全表更新（§八.3）、DS-015 零复用复核结论（§八.3）均已落本节。

### 八.2 逐处改动逐字对照（改前／改后）

**DS-013（inputs/DS-013.json，setting 与 provenance 各 1 处）**

- setting 改前：「{n13['setting_before']}」
- setting 改后：「{n13['setting_after']}」
- provenance 改前：「{n13['provenance_before']}」
- provenance 改后：「{n13['provenance_after']}」

**DS-014（inputs/DS-014.json，setting 与 provenance 各 1 处）**

- setting 改前：「{n14['setting_before']}」
- setting 改后：「{n14['setting_after']}」
- provenance 改前：「{n14['provenance_before']}」
- provenance 改后：「{n14['provenance_after']}」

**DS-015（新建卡 inputs/DS-015.json；改前＝承台账 source 逐字之未中性化串，改后＝卡面实值）**

- 台账 source 原文（金标侧 provenance 据此原登记、不中性化）：「{src15}」
- setting 改前（未中性化）：「{src15}」
- setting 改后：「{card15['setting']}」
- provenance 改前（未中性化）：「{src15}；底本为用户经学校图书馆提供，redistributable=false」
- provenance 改后：「{card15['provenance']}」
- 金标 DS-015 行 provenance（照台账原登记、不中性化）：「{gold15['provenance']}」

**DS-019（退出）**

- 输入卡：`holdout23/inputs/DS-019.json` 已以精确路径删除（脚本内 os.remove 精确路径操作，删后存在性断言为不存在）。
- 金标行：`holdout23/test_gold.jsonl` 中 DS-019 行已精确删除；DS-019 自本节起退出本集，§一构成表 DS 行以 §八.3 更新表为准。

### 八.3 构成全表更新与复断言

| 来源 | 例数 | 占比 | 入选 id |
|---|---|---|---|
| 段建业《段氏理象学》 | 6 | 22.2% | DS-013、DS-014、DS-015、DS-016、DS-017、DS-018 |
| 张志春《开悟之门》 | 5 | 18.5% | QM-015、QM-016、QM-018、QM-019、QM-020 |
| 刘文元《奇门启悟》 | 2 | 7.4% | QM-204、QM-205 |
| 石建国《奇门遁甲最新实例解析》 | 3 | 11.1% | QM-304、QM-305、QM-306 |
| 《字触补》（《四库未收书辑刊》陆辑第拾捌册） | 6 | 22.2% | ZCB-006、ZCB-007、ZCB-008、ZCB-009、ZCB-010、ZCB-011 |
| 王虎应《六爻卦例说真》 | 5 | 18.5% | GSZ-028、GSZ-030、GSZ-031、GSZ-032、GSZ-033 |
| 合计 | 27 | 100% | 非夷坚 27 |

| 体系 | 例数 | 占比 |
|---|---|---|
| qimen（奇门） | 10 | 37.0% |
| bazi（八字） | 6 | 22.2% |
| cezi（测字） | 6 | 22.2% |
| liuyao（六爻） | 5 | 18.5% |

- 构成限度复断言（脚本内硬断言、全过）：总量 T＝27 ≥25；单体系最大 奇门 10/27＝37.0% ≤50%；单源最大 DS／ZCB 各 6/27＝22.2% ≤50%；非夷坚 27 ≥13；非六爻 22 ≥13；多源构成（六源并存）；污染 low 27/27。
- **DS-015 零复用复核结论**：已用并集按封存日志 §一口径盘上逐 id 复算＝**1004 id**（dev 池＝data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs 目录卡 id；phase2 splits2 之 holdout2；holdout3–22 各 test_gold.jsonl 仅取 id 字段；holdout2–22 inputs 与 *-inputs 目录卡 id；顶层 inputs6–10 目录卡 id；五源并集去重），DS-015 逐 id **零命中**（预期一致：台账登记序中 DS-015 本在 DS-019 之前、原挂起仅因节题）。本轮选集 27 id 与已用并集交集＝∅。
"""
with open(SEAL_LOG, 'a', encoding='utf-8') as f:
    f.write(sec)

sec2 = f"""
### 八.4 改后复验登记（本席执行）

- **变更卡逐卡复扫（DS-013／DS-014／DS-015，盘上文件重行）**：断语片段逐字子串扫描（对该例 master_prediction 特征片段：标点分句整句 ≥8 字＋去空白 12 字滑动窗口）零命中；结局片段（outcome_record 同法）零命中；内容级标记扫描（标记集承 runs/round42/PREREG.md §5 一级/二级）零命中；字段名黑名单零命中；禁用键递归扫描零命中；字段白名单与键序核通过——三卡全过。
- **全集 27 卡复扫（第二道口径，本席独立实现重行）**：标记命中 {tot['marker_hits']}、字段名命中 {tot['fieldname_hits']}、禁用键命中 {tot['banned_key_hits']}、结局片段命中 {tot['outcome_fragment_hits']}、非测字断语片段命中 {tot['master_fragment_hits_noncezi']}、字段白名单/键序不合 {len(tot['whitelist_failures'])} 卡；测字断语片段命中仅既知一件（{cezi_master_hits_str}），系 §八.1 第 4 项裁处照建不动之锚点原文内含语（封存日志 §四已分类登记），非新增命中。全集复扫结论：零新增命中、通过。
- **新金标 SHA-256（双读）**：脚本 hashlib 读数 `{sha_lib}`；脚本内 sha256sum 子进程读数 `{sha_sum}`；两读一致，成立。金标 {gold_bytes} 字节、27 行、行序照 id 序。原 SHA `{OLD_SHA}` 自本节落盘起作废留痕（承 §七口径）；封存定版以主持第三读复核为准。开封条件不变（§七写死口径不改）。
"""
with open(SEAL_LOG, 'a', encoding='utf-8') as f:
    f.write(sec2)
seal_log_size_after = os.path.getsize(SEAL_LOG)

# ================= 登记件 =================
register = {
    'seat': 'R78 holdout23 封存裁处执行席',
    'script': 'runs/round78/amend_holdout23_r78.py',
    'gold_sha_before': OLD_SHA, 'gold_sha_after_hashlib': sha_lib,
    'gold_sha_after_sha256sum': sha_sum, 'gold_bytes_after': gold_bytes,
    'gold_rows_after': NEW_IDS,
    'item1_DS-013': neut_register['DS-013'],
    'item2_DS-014': neut_register['DS-014'],
    'item3_DS-015': {
        'ledger_source_verbatim': src15,
        'title_locations_neutralized': ds015_title_locations,
        'card_setting_after': card15['setting'],
        'card_provenance_after': card15['provenance'],
        'gold_provenance_unnneutralized': gold15['provenance'],
        'eligibility_recheck_pass': bool(ok15),
        'zero_reuse': {'used_union_total': len(used_union),
                       'used_sources': used_sources,
                       'DS-015_in_used_union': not ds015_zero_reuse,
                       'conclusion': '零命中'}},
    'item3_DS-019': {'card_deleted_exact_path': ds019_card_path,
                     'gold_row_deleted': True},
    'item4_ZCB': 'ZCB-006/ZCB-007/ZCB-011 照建不动、标旗维持；裁处理由原文已记入封存日志 §八.1 第 4 项',
    'changed_card_rescan': changed_scan,
    'full_rescan_totals': tot,
    'full_rescan_failures': full_failures,
    'composition': {'by_source': dict(src_counts), 'by_tradition': dict(trad_counts),
                    'T': 27, 'assertions_all_pass': True},
    'seal_log_size_before': seal_log_size_before,
    'seal_log_size_after': seal_log_size_after,
}
reg_path = os.path.join(R78, 'amend-holdout23-register-r78.json')
with open(reg_path, 'w', encoding='utf-8') as f:
    json.dump(register, f, ensure_ascii=False, indent=2)
    f.write('\n')

print(json.dumps({
    'gold_sha_after': sha_lib, 'gold_sha_double_read_equal': sha_lib == sha_sum,
    'gold_bytes_after': gold_bytes,
    'changed_scan_pass': {k: v['pass'] for k, v in changed_scan.items()},
    'full_totals': {k: tot[k] for k in ('marker_hits', 'fieldname_hits',
                                        'banned_key_hits', 'outcome_fragment_hits',
                                        'master_fragment_hits_noncezi')},
    'cezi_known_hits': tot['master_fragment_hits_cezi'],
    'ds015_zero_reuse': ds015_zero_reuse, 'used_union_total': len(used_union),
    'composition_by_source': dict(src_counts),
    'composition_by_tradition': dict(trad_counts),
    'seal_log_size_before': seal_log_size_before,
    'seal_log_size_after': seal_log_size_after,
    'register': reg_path}, ensure_ascii=False))
