# -*- coding: utf-8 -*-
"""holdout31 独立复扫（R87 组集封存席）：不 import 构建脚本，按 28 id 清单逐件
精确打开盘上输入卡与金标，重行标记/字段名/禁用键/白名单/片段五项扫描。"""
import json, os, re, hashlib

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
IDS = ['DA-047', 'BY-022', 'DA-048', 'BY-023', 'DA-050', 'BY-024', 'DA-051',
       'BY-025', 'DA-054', 'BY-027', 'DA-055', 'BY-028', 'DA-057', 'BY-030',
       'WHY-037', 'WHY-038', 'WHY-039', 'WHY-040', 'WHY-041', 'WHY-042',
       'WHY-043', 'WHY-044', 'WHY-068', 'WHY-069',
       'GSZ-107', 'GSZ-108', 'GSZ-109', 'GSZ-110']
INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question',
                'setting', 'provenance', 'redistributable', 'license_status', 'anchors']
GOLD_FIELDS = ['id', 'master_prediction', 'outcome_record', 'tradition',
               'pollution', 'grade', 'grade_note', 'provenance',
               'license_status', 'redistributable']
LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗语', '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '正议', '正議', '验语', '驗语', '占断', '占斷', '线索', '線索']
BANNED = {'grade_note', 'contamination', 'contamination_rationale', 'outcome', 'outcome_record',
          'master_prediction', 'master_assertion', 'gold', 'answer', 'holdout_eligible',
          'review', 'pollution', 'pollution_note', 'anchor_status', 'anchor_presence',
          'anchor_missing', 'dedup_check', 'filters', 'transcription', 'transcription_confidence',
          'source', 'grade', 'fail_reason', 'eligible_net', 'outcome_type', 'master',
          'master_predictions', 'input_fields', 'provisional_id'}


def fragments(text):
    out = set()
    for seg in re.split(r'[。；：！？\n]', text):
        seg = seg.strip(' ，、')
        if len(seg) >= 8:
            out.add(seg)
    flat = re.sub(r'\s+', '', text)
    for i in range(len(flat) - 11):
        out.add(flat[i:i + 12])
    return out


def walk_strings(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from walk_strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk_strings(v)
    elif isinstance(o, str):
        yield o


def walk_keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from walk_keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk_keys(v)


golds = {}
for line in open(os.path.join(BASE, 'holdout31/test_gold.jsonl'), encoding='utf-8'):
    if line.strip():
        g = json.loads(line)
        golds[g['id']] = g
assert set(golds) == set(IDS) and len(golds) == 28

per_case, totals = {}, {'content': 0, 'fieldname': 0, 'banned': 0, 'mp_frag': 0, 'oc_frag': 0}
for cid in IDS:
    card = json.load(open(os.path.join(BASE, 'holdout31/inputs', f'{cid}.json'), encoding='utf-8'))
    g = golds[cid]
    assert list(card.keys()) == INPUT_FIELDS, cid
    assert list(g.keys()) == GOLD_FIELDS, cid
    assert g['pollution'] == 'low' and card['redistributable'] is False and g['redistributable'] is False
    text = json.dumps(card, ensure_ascii=False)
    ch = [mk for s in walk_strings(card) for mk in LEVEL1 + LEVEL2 if mk in s]
    fh = [b for k in walk_keys(card) for b in FIELD_BLACKLIST if b in str(k)]
    bk = [k for k in walk_keys(card) if k in BANNED]
    mp = [fr for fr in fragments(g['master_prediction']) if fr in text]
    oc = [fr for fr in fragments(g['outcome_record']) if fr in text]
    per_case[cid] = {'content_hits': ch, 'fieldname_hits': fh, 'banned_key_hits': bk,
                     'master_prediction_fragment_hits': mp, 'outcome_fragment_hits': oc,
                     'pass': not (ch or fh or bk or mp or oc)}
    totals['content'] += len(ch); totals['fieldname'] += len(fh); totals['banned'] += len(bk)
    totals['mp_frag'] += len(mp); totals['oc_frag'] += len(oc)
    assert per_case[cid]['pass'], (cid, ch[:2], fh[:2], bk[:2], mp[:2], oc[:2])

gold_path = os.path.join(BASE, 'holdout31/test_gold.jsonl')
sha = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
result = {'set': 'holdout31', 'rescan_by': '独立复扫脚本 scan_holdout31_r87.py（R87 组集封存席）',
          'T': 28, 'per_case': per_case, 'totals': totals, 'all_pass': True,
          'gold_sha256': sha, 'gold_bytes': os.path.getsize(gold_path)}
out = os.path.join(BASE, 'runs/round87/scan-holdout31-rescan-r87.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'all_pass': True, 'totals': totals, 'gold_sha256': sha}, ensure_ascii=False))
