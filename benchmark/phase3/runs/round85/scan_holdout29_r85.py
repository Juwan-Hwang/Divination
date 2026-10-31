#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R85 组集封存席独立复扫（第二道）：不 import 构建脚本，按写定 id 清单
逐件精确打开盘上 holdout29 输入卡与金标，重行 R42 PREREG §5 内容级标记
（一级/二级，逐字承该节）＋字段名黑名单＋禁用键集＋字段白名单＋逐字片段
（结局/断语）五项扫描。结果落 runs/round85/scan-holdout29-result-r85.json。
"""
import json, os, re

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
IDS = ['DA-025', 'CYJ-001', 'BY-012', 'DA-033', 'CYJ-002', 'BY-014',
       'DA-034', 'CYJ-004', 'BY-015', 'DA-035', 'CYJ-005', 'BY-016',
       'DA-037', 'ZW-004', 'ZW-005', 'ZW-006', 'ZW-007', 'ZW-008',
       'ZW-009', 'ZW-010', 'ZW-011', 'ZW-012', 'ZW-013', 'ZW-014',
       'ZW-015', 'ZW-016', 'DS-063']
LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '正议', '正議', '验语', '驗語',
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
WHITELIST = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
             'provenance', 'redistributable', 'license_status', 'anchors']


def walk(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f'{path}[{i}]')
    elif isinstance(obj, str):
        yield path, obj


def keys_walk(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield f'{path}/{k}', k
            yield from keys_walk(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from keys_walk(v, f'{path}[{i}]')


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


golds = {}
for line in open(os.path.join(BASE, 'holdout29/test_gold.jsonl'), encoding='utf-8'):
    if line.strip():
        g = json.loads(line)
        golds[g['id']] = g
assert sorted(golds) == sorted(IDS), (sorted(golds), IDS)

per_case, failures = {}, []
tot = {'marker': 0, 'fieldname': 0, 'banned': 0, 'outcome_frag': 0, 'master_frag': 0}
for cid in IDS:
    card = json.load(open(os.path.join(BASE, 'holdout29/inputs', f'{cid}.json'), encoding='utf-8'))
    marker_hits, field_hits, banned_hits = [], [], []
    for path, s in walk(card):
        for lvl, markers in (('L1', LEVEL1), ('L2', LEVEL2)):
            for m in markers:
                i = s.find(m)
                if i >= 0:
                    marker_hits.append([path, lvl, m, s[max(0, i - 12):i + len(m) + 12]])
    for path, k in keys_walk(card):
        if any(f in k for f in FIELD_BLACKLIST):
            field_hits.append([path, k])
        if k in BANNED:
            banned_hits.append(path)
    wl_ok = list(card.keys()) == WHITELIST
    card_text = json.dumps(card, ensure_ascii=False)
    g = golds[cid]
    oc_hits = [f for f in fragments(g['outcome_record']) if f in card_text]
    mp_hits = [f for f in fragments(g['master_prediction']) if f in card_text]
    per_case[cid] = {'marker_hits': marker_hits, 'fieldname_hits': field_hits,
                     'banned_key_hits': banned_hits, 'whitelist_ok': wl_ok,
                     'outcome_fragment_hits': oc_hits, 'master_fragment_hits': mp_hits}
    tot['marker'] += len(marker_hits); tot['fieldname'] += len(field_hits)
    tot['banned'] += len(banned_hits); tot['outcome_frag'] += len(oc_hits)
    tot['master_frag'] += len(mp_hits)
    if marker_hits or field_hits or banned_hits or oc_hits or mp_hits or not wl_ok:
        failures.append(cid)

result = {'set': 'holdout29', 'scanner': 'scan_holdout29_r85.py（独立复扫，第二道）',
          'marker_set_source': 'R42 PREREG §5（一级/二级，逐字承之）',
          'ids': IDS, 'totals': tot, 'per_case': per_case,
          'pass': not failures, 'failures': failures}
out = os.path.join(BASE, 'runs/round85/scan-holdout29-result-r85.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'pass': result['pass'], 'failures': failures, 'totals': tot,
                  'result_bytes': os.path.getsize(out)}, ensure_ascii=False))
