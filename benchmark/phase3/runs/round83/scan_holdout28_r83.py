#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R83 封存席独立复扫（第二道）：不 import 构建脚本，按显式 id 清单逐件精确打开
盘上 holdout28 输入卡与金标，重行 R42 PREREG §5 标记/字段名/禁用键/白名单/片段
五项扫描，结果落 runs/round83/scan-holdout28-result-r83.json。"""
import json, os, re

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R83 = os.path.join(BASE, 'runs/round83')
IDS = ['DS-050', 'DS-051', 'DS-052', 'DS-053', 'DS-054', 'DS-055', 'DS-056',
       'DS-057', 'DS-058', 'DS-059', 'DS-060', 'DS-061', 'DS-062',
       'QM-210', 'QM-211', 'QM-010',
       'GSZ-091', 'GSZ-092', 'GSZ-093', 'GSZ-098', 'GSZ-099', 'GSZ-100',
       'WHY-012', 'WHY-016', 'WHY-022', 'WHY-023', 'WHY-024']
LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '断曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']
BANNED = {'grade_note', 'grade_suggestion', 'grade_reason', 'contamination',
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
FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
          'provenance', 'redistributable', 'license_status', 'anchors']


def walk_str(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_str(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_str(v, f'{path}[{i}]')
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
    frags = set()
    for clause in re.split(r'[。！？；\n]', text):
        c = clause.strip('「」『』“”‘’"\' ')
        if len(c) >= 8:
            frags.add(c)
    t = re.sub(r'\s+', '', text)
    for i in range(0, max(0, len(t) - 11)):
        frags.add(t[i:i + 12])
    return frags


def short_fragments(text):
    t = re.sub(r'\s+', '', text)
    return {t[i:i + 8] for i in range(0, max(0, len(t) - 7))}


golds = {}
for line in open(os.path.join(BASE, 'holdout28/test_gold.jsonl'), encoding='utf-8'):
    if line.strip():
        g = json.loads(line)
        golds[g['id']] = g
assert set(golds) == set(IDS) and len(golds) == 27

per_case, failures = {}, []
tot = {'marker': 0, 'fieldname': 0, 'banned': 0, 'oc_frag': 0, 'mp_frag': 0,
       'short_frag_info': 0}
for cid in IDS:
    card = json.load(open(os.path.join(BASE, f'holdout28/inputs/{cid}.json'),
                          encoding='utf-8'))
    g = golds[cid]
    marker_hits = []
    for path, s in walk_str(card):
        for lvl, markers in (('L1', LEVEL1), ('L2', LEVEL2)):
            for m in markers:
                if m in s:
                    marker_hits.append([path, lvl, m])
    fn_hits = [[p, k] for p, k in walk_keys(card)
               if any(f in k for f in FIELD_BLACKLIST)]
    banned_hits = [p for p, k in walk_keys(card) if k in BANNED]
    wl_ok = list(card.keys()) == FIELDS
    card_text = json.dumps(card, ensure_ascii=False)
    oc_hits = [f for f in fragments(g['outcome_record']) if f in card_text]
    mp_hits = [f for f in fragments(g['master_prediction']) if f in card_text]
    short_hits = [f for f in short_fragments(g['master_prediction'])
                  if f in re.sub(r'\s+', '', card_text)]
    per_case[cid] = {'marker_hits': marker_hits, 'fieldname_hits': fn_hits,
                     'banned_key_hits': banned_hits, 'whitelist_ok': wl_ok,
                     'outcome_fragment_hits': oc_hits,
                     'master_prediction_fragment_hits': mp_hits,
                     'short_fragment_info_hits': short_hits}
    tot['marker'] += len(marker_hits)
    tot['fieldname'] += len(fn_hits)
    tot['banned'] += len(banned_hits)
    tot['oc_frag'] += len(oc_hits)
    tot['mp_frag'] += len(mp_hits)
    tot['short_frag_info'] += len(short_hits)
    if marker_hits or fn_hits or banned_hits or not wl_ok or oc_hits or mp_hits:
        failures.append(cid)

result = {'set': 'holdout28', 'scan': 'independent rescan (seat, second pass)',
          'pass': not failures, 'failures': failures, 'totals': tot,
          'per_case': per_case,
          'note': 'short_fragment_info_hits 为附加短片段核（断语 ≥8 字连续子串），仅信息登记'}
with open(os.path.join(R83, 'scan-holdout28-result-r83.json'), 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'pass': result['pass'], 'failures': failures, 'totals': tot},
                 ensure_ascii=False))
