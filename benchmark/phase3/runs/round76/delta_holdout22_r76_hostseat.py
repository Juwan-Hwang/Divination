#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""holdout22 主持裁处 delta 修正席（R76）：只动主持裁处三项，其余一字不动。
1) ZCB-003 换例 -> ZCB-005（删卡+删金标行；按原测字四例同一规格建卡/建金标）
2) DS-011 输入卡 setting/provenance 中性化（删节题全文，定位只留「第八章第一节六」）
3) QM-301 输入卡 setting/provenance 中性化（删实例题全文，保留定位部分）
收尾：test_gold.jsonl 行序照 id 序（字典序）重整，金标 SHA 双读；
封存日志 append delta 节；构建报告增 delta 节（原节不动，文本插入）；快照不动。
不作断、不评分、不开封验收、不做 git 操作。
"""
import json, hashlib, os, re, subprocess

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R76 = os.path.join(BASE, 'runs/round76')
IN_DIR = os.path.join(BASE, 'holdout22/inputs')
GOLD_PATH = os.path.join(BASE, 'holdout22/test_gold.jsonl')
SEAL_LOG = os.path.join(BASE, 'data/holdout22-seal-log.md')
REPORT_PATH = os.path.join(R76, 'build-holdout22-report-r76.json')
REGISTER_PATH = os.path.join(R76, 'delta-holdout22-register-r76-hostseat.json')
SNAP_SHA_PATH = os.path.join(R76, 'kb-snapshot-holdout22-sha256.txt')
ZC_MINING = os.path.join(R76, 'digestion/SUPPLY-MINING-zichubu-r76.json')

OLD_SHA = '1e299bdaf10724bf2ba66d1f4933fdcbeee11b5970f978df975872bb7164ae6a'

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
INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status', 'anchors']


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


def frag_scan(card, gold):
    card_text = json.dumps(card, ensure_ascii=False)
    mp = [fr for fr in fragments(gold['master_prediction']) if fr in card_text]
    oc = [fr for fr in fragments(gold['outcome_record']) if fr in card_text]
    return mp, oc


def dump_card(path, card):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(card, f, ensure_ascii=False, indent=2)
        f.write('\n')


register = {}

# ---------- 前置核验：旧金标 SHA 与主持第三读一致 ----------
raw_gold_before = open(GOLD_PATH, 'rb').read()
sha_before = hashlib.sha256(raw_gold_before).hexdigest()
assert sha_before == OLD_SHA, sha_before
snap_sha_before = hashlib.sha256(open(SNAP_SHA_PATH, 'rb').read()).hexdigest()
register['precheck'] = {'gold_sha256_before': sha_before,
                       'matches_host_third_read': True,
                       'kb_snapshot_sha256_txt_hash_before': snap_sha_before}

# 原书容器 SHA 与台账 meta 登记一致（取原书路径以台账 meta 为准）
zc_mining = json.load(open(ZC_MINING, encoding='utf-8'))
container = zc_mining['meta']['container_file']
container_sha = hashlib.sha256(open(container, 'rb').read()).hexdigest()
assert container_sha == zc_mining['meta']['container_sha256'], container_sha
register['source_book_check'] = {
    'container_file_per_taizhang_meta': container,
    'container_sha256': container_sha,
    'matches_taizhang_meta': True,
    'note': '主持任务书作 incoming/wanted-books-3；台账 meta 登记之 container_file 为 '
            'incoming/wanted-books-5/Book 同名 PDF，本席以台账 meta 为准取原书，'
            'SHA 与台账登记一致（wanted-books-3/Book 下无此 PDF，仅 Book.7z 等）。'}

# ---------- 1) ZCB-005 建卡与金标（与原测字四例同一规格） ----------
zc_by = {c['case_id']: c for c in zc_mining['cases']}
c5 = zc_by['ZCB-005']
assert c5.get('eligible') is True and c5['anchor_status'] == 'present' \
    and c5['contamination_pre'] == 'low' and c5['separable'] is True \
    and c5['master_assertion'].strip() and c5['outcome'].strip()
src5 = c5['source']
setting5 = (f"《字触补》{src5['juan']}·{src5['leaf']}（《四库未收书辑刊》陆辑第拾捌册，"
            f"PDF页{src5['pdf_pages']}）")
provenance5 = f"{setting5}；用户经学校图书馆提供；redistributable=false"
input5 = c5['input_side']
card5 = {
    'id': 'ZCB-005', 'tradition': 'cezi',
    'subject': '孟瓶庵与榜前同测二友',
    'context': input5,
    'question': '榜前书因字请测（三人同字分测）',
    'setting': setting5,
    'provenance': provenance5,
    'redistributable': False,
    'license_status': '古籍文本（合集扫描本），内部研究用',
    'anchors': {'character': '因',
                'split_process_verbatim': input5},
}
note5 = (f"锚点 present（{c5['anchor_basis']}）；污染 low（{c5['contamination_basis']}）；"
         f"转录：visual（confidence={c5['transcription']['confidence']}"
         + (f"，{c5['transcription']['note']}" if c5['transcription'].get('note') else '')
         + f"）；CZ-QX 计数例：{c5['cz_qx_note']}")
gold5 = {'id': 'ZCB-005', 'master_prediction': c5['master_assertion'],
         'outcome_record': c5['outcome'], 'tradition': 'cezi',
         'pollution': 'low', 'grade': 'A', 'grade_note': note5,
         'provenance': provenance5,
         'license_status': '古籍文本（合集扫描本），内部研究用',
         'redistributable': False}

# 金标断语逐字核验登记（本席读原书 300dpi 渲染页图 PDF557 下半叶9＋PDF558 上半叶9续，逐句对勘）
verification5 = {
    'method': '回原书叶面逐句对勘：容器 PDF 第557页下半（卷二·外部叶9，因字条起）'
              '＋第558页上半（叶9续），300dpi 渲染页图存 '
              'runs/round76/delta-r76-hostseat/zcb005-pg-557.png、zcb005-pg-558.png '
              '及裁切图两件；逐断与原书竖排原文逐字比对（原书无标点，标点为转录/分列标记）。',
    'segments': [
        {'person': '孟瓶庵（第一人）', 'gold_segment': '君必為此科解首矣',
         'in_book': '其人曰「此為國中一人之象君必為此科解首矣」（叶9，PDF557下半）',
         'verbatim': True},
        {'person': '友二（第二人）', 'gold_segment': '君此科恐無分，或後此有恩科亦必中',
         'in_book': '其人曰「君此科恐無分或後此有恩科亦必中」（叶9，PDF557下半；原书无逗号）',
         'verbatim': True},
        {'person': '友三（第三人）', 'gold_segment': '其終於一衿乎',
         'in_book': '其人……曰「君之扇適加因字正中有困之象其終於一衿乎」（叶9续，PDF558上半）',
         'verbatim': True},
        {'person': '结局', 'gold_segment': '後三君皆如其言',
         'in_book': '「後三君皆如其言此人惜不傳姓名殆亦高鳳之流亞矣」（叶9续，PDF558上半）',
         'verbatim': True},
    ],
    'conclusion': '逐字核验通过：三人三断与结局逐句与原书逐字合，照台账入标，不补录。'
                  '台账 master_assertion 中（孟）／（友二）／（友三）标签、逗号与分号为'
                  '三人三断之分列标记（同 DS 例「／」台账摘录分隔符先例），非原书文字，'
                  '在此登记；断语本体逐字。',
    'supplement_needed': False,
    'supplement_chars': None,
    'master_prediction_chars': len(gold5['master_prediction']),
    'master_prediction': gold5['master_prediction'],
    'input_side_note': '输入卡 context／anchors.split_process_verbatim 照台账 input_side 逐字'
                       '（同原四例规格）；台账 input_side 作「以徐[?]茶書一因字」，原书叶面'
                       '该处作「以餘茶書一因字」（餘字清晰），[?] 为台账未判准标记、非断语'
                       '字段，本席照规格不改台账逐字文本，仅此附注登记。',
}
assert all(s['verbatim'] for s in verification5['segments'])
register['zcb005_verification'] = verification5

# ZCB-005 新卡同一套自检
assert list(card5.keys()) == INPUT_FIELDS
bk5 = banned_key_scan(card5)
assert not bk5, bk5
mp_hits5, oc_hits5 = frag_scan(card5, gold5)
marker5 = scan_content(card5) + scan_field_names(card5)
guozhi5 = '故知' in json.dumps(card5, ensure_ascii=False)
class5 = []
for fr in mp_hits5 + oc_hits5:
    in_anchor = fr in c5['input_side']
    class5.append({'fragment': fr, 'in_taizhang_input_side_anchor': in_anchor,
                   'class': '字形拆分过程锚点原文内含语' if in_anchor else '未分类命中'})
    assert in_anchor, fr
scan5 = {'banned_key_hits': bk5, 'master_prediction_hits': mp_hits5,
         'outcome_hits': oc_hits5, 'hit_classification': class5,
         'marker_hits': marker5, 'contains_guozhi_conclusion': guozhi5,
         'field_whitelist_pass': list(card5.keys()) == INPUT_FIELDS}
assert not marker5 and not guozhi5
register['zcb005_card_scan'] = scan5
register['zcb005_card'] = card5
register['zcb005_gold'] = gold5
register['zcb005_field_mapping'] = (
    'context/anchors.split_process_verbatim←台账 input_side 逐字（字形拆分过程为输入侧锚点原文）；'
    'subject/question 为组写（口径在此登记，同原四例）；setting/provenance 只载卷叶与 PDF 页定位、'
    '不载原书条题（条题「因字三測」同法中性化，承原四例口径）；anchors.character←所测字「因」；'
    'provenance 含「用户经学校图书馆提供」、redistributable=false。')
register['zcb005_eligibility'] = {'eligible': c5.get('eligible'),
                                  'anchor_status': c5['anchor_status'],
                                  'contamination': c5['contamination_pre'],
                                  'separable': c5['separable'], 'pass': True,
                                  'basis': 'SUPPLY-MINING-zichubu-r76.json 台账逐字'}

# ---------- 2) DS-011 卡面中性化（精确字串替换，仅 setting/provenance） ----------
DS_TITLE_FULL = '第八章第一节六、商海沉浮，女强人命运多舛'
DS_TITLE_KEEP = '第八章第一节六'
ds_path = os.path.join(IN_DIR, 'DS-011.json')
ds_raw_before = open(ds_path, encoding='utf-8').read()
ds_card = json.loads(ds_raw_before)
# 格式无损自检：未改前重dump与原文一致
assert json.dumps(ds_card, ensure_ascii=False, indent=2) + '\n' == ds_raw_before
ds_before = {'setting': ds_card['setting'], 'provenance': ds_card['provenance']}
ds_counts = {}
for fld in ('setting', 'provenance'):
    ds_counts[fld] = ds_card[fld].count(DS_TITLE_FULL)
    assert ds_counts[fld] == 1, (fld, ds_counts[fld])
    ds_card[fld] = ds_card[fld].replace(DS_TITLE_FULL, DS_TITLE_KEEP)
# 其余字段不得含该节题字串
ds_rest = json.dumps({k: v for k, v in ds_card.items()
                      if k not in ('setting', 'provenance')}, ensure_ascii=False)
assert '商海沉浮，女强人命运多舛' not in json.dumps(ds_card, ensure_ascii=False)
assert '女企业家' in ds_card['subject']  # 输入侧事实，保留
ds_after = {'setting': ds_card['setting'], 'provenance': ds_card['provenance']}
dump_card(ds_path, ds_card)
register['ds011_change'] = {'file': 'holdout22/inputs/DS-011.json',
                            'occurrences_replaced': ds_counts,
                            'before': ds_before, 'after': ds_after,
                            'subject_unchanged': ds_card['subject'],
                            'rule': '删描述性小节题全文「商海沉浮，女强人命运多舛」，'
                                    '定位只留「第八章第一节六」，其余字串一字不动；'
                                    '原题全文只留本日志登记。金标 DS-011 行除行序外一字未动'
                                    '（金标侧 provenance 照原登记载全节名）。'}

# ---------- 3) QM-301 卡面中性化（精确字串删除，逐处登记） ----------
QM_TITLE_FULL = '「少收的贷款能找回」'
qm_path = os.path.join(IN_DIR, 'QM-301.json')
qm_raw_before = open(qm_path, encoding='utf-8').read()
qm_card = json.loads(qm_raw_before)
assert json.dumps(qm_card, ensure_ascii=False, indent=2) + '\n' == qm_raw_before
qm_before = {'setting': qm_card['setting'], 'provenance': qm_card['provenance']}
qm_counts = {}
for fld in list(qm_card.keys()):
    v = qm_card[fld]
    if isinstance(v, str):
        qm_counts[fld] = v.count(QM_TITLE_FULL)
for fld in ('setting', 'provenance'):
    assert qm_counts.get(fld) == 1, (fld, qm_counts)
    qm_card[fld] = qm_card[fld].replace(QM_TITLE_FULL, '')
assert '少收的贷款能找回' not in json.dumps(qm_card, ensure_ascii=False)
qm_after = {'setting': qm_card['setting'], 'provenance': qm_card['provenance']}
dump_card(qm_path, qm_card)
register['qm301_change'] = {'file': 'holdout22/inputs/QM-301.json',
                            'occurrences_removed_by_field_top_level_str': qm_counts,
                            'removed_string': QM_TITLE_FULL,
                            'before': qm_before, 'after': qm_after,
                            'note': 'question「刚才卖货时少收了顾客500元钱，看货款能不能找回来」'
                                    '为输入侧问句原文、非实例题字串，一字未动；卡内其余字段经'
                                    '全卡检索无该题名字串。金标 QM-301 行除行序外一字未动。'}

# 两卡改后复扫（片段＋标记＋禁用键＋白名单）
gold_by_id = {}
for line in open(GOLD_PATH, encoding='utf-8'):
    if line.strip():
        g = json.loads(line)
        gold_by_id[g['id']] = g
rescan = {}
for cid, card in (('DS-011', ds_card), ('QM-301', qm_card)):
    mp, oc = frag_scan(card, gold_by_id[cid])
    rescan[cid] = {'master_prediction_hits': mp, 'outcome_hits': oc,
                   'marker_hits': scan_content(card) + scan_field_names(card),
                   'banned_key_hits': banned_key_scan(card),
                   'field_whitelist_pass': list(card.keys()) == INPUT_FIELDS}
    assert not mp and not oc and not rescan[cid]['marker_hits'] \
        and not rescan[cid]['banned_key_hits']
register['modified_cards_rescan'] = rescan

# ---------- 落盘 ZCB-005 卡；精确删除 ZCB-003 卡 ----------
dump_card(os.path.join(IN_DIR, 'ZCB-005.json'), card5)
os.remove(os.path.join(IN_DIR, 'ZCB-003.json'))
assert not os.path.exists(os.path.join(IN_DIR, 'ZCB-003.json'))
assert os.path.exists(os.path.join(IN_DIR, 'ZCB-005.json'))

# ---------- 金标：删 ZCB-003 行（精确行）、加 ZCB-005 行、照 id 序重整、双读 ----------
lines_before = [l for l in open(GOLD_PATH, encoding='utf-8').read().splitlines() if l.strip()]
assert len(lines_before) == 27
raw_by_id = {}
for l in lines_before:
    raw_by_id[json.loads(l)['id']] = l
assert 'ZCB-003' in raw_by_id
# 未动行字节无损自检
for cid, l in raw_by_id.items():
    assert json.dumps(json.loads(l), ensure_ascii=False) == l, cid
del raw_by_id['ZCB-003']
raw_by_id['ZCB-005'] = json.dumps(gold5, ensure_ascii=False)
new_order = sorted(raw_by_id.keys())
assert len(new_order) == 27
with open(GOLD_PATH, 'w', encoding='utf-8') as f:
    for cid in new_order:
        f.write(raw_by_id[cid] + '\n')
raw_gold_after = open(GOLD_PATH, 'rb').read()
sha_lib = hashlib.sha256(raw_gold_after).hexdigest()
sha_sum = subprocess.run(['sha256sum', GOLD_PATH], capture_output=True,
                         text=True).stdout.split()[0]
assert sha_lib == sha_sum
register['gold_delta'] = {'removed_id': 'ZCB-003', 'added_id': 'ZCB-005',
                          'new_order_id_sorted': new_order,
                          'old_sha256_superseded': OLD_SHA,
                          'new_sha256_hashlib': sha_lib,
                          'new_sha256_sha256sum': sha_sum,
                          'double_read_match': sha_lib == sha_sum}
register['new_selection_ids'] = new_order

# ---------- 全集终检 ----------
disk_ids = sorted(fn[:-5] for fn in os.listdir(IN_DIR) if fn.endswith('.json'))
assert disk_ids == new_order, (disk_ids, new_order)
for cid in new_order:
    card = json.load(open(os.path.join(IN_DIR, f'{cid}.json'), encoding='utf-8'))
    assert list(card.keys()) == INPUT_FIELDS, cid
    assert not banned_key_scan(card), cid
gold_ids_disk = [json.loads(l)['id'] for l in open(GOLD_PATH, encoding='utf-8') if l.strip()]
assert gold_ids_disk == new_order
snap_sha_after = hashlib.sha256(open(SNAP_SHA_PATH, 'rb').read()).hexdigest()
assert snap_sha_after == snap_sha_before
register['final_check'] = {'inputs_count': len(disk_ids), 'gold_lines': len(gold_ids_disk),
                           'ids_match': disk_ids == gold_ids_disk == new_order,
                           'kb_snapshot_untouched': snap_sha_after == snap_sha_before,
                           'kb_snapshot_sha256_txt_hash_after': snap_sha_after}

with open(REGISTER_PATH, 'w', encoding='utf-8') as f:
    json.dump(register, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'new_sha256': sha_lib, 'double_read_match': sha_lib == sha_sum,
                  'new_order': new_order, 'zcb005_scan': scan5}, ensure_ascii=False, indent=2))
