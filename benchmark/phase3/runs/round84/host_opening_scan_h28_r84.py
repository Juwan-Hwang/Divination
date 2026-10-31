#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R84 主持开封前复验第三道复扫：独立脚本，不 import 构建/封存脚本。
按显式 id 清单逐件精确打开盘上 holdout28 输入卡，重行 R42 PREREG §5
标记集（LEVEL1 断语标记／LEVEL2 结局标记／字段名黑名单／禁用键／字段白名单）
扫描，结果打印并落 runs/round84/host-opening-scan-h28-result-r84.json。"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
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


hits = []
cards = 0
for cid in IDS:
    p = os.path.join(BASE, 'holdout28', 'inputs', f'{cid}.json')
    with open(p, encoding='utf-8') as fh:
        card = json.load(fh)
    cards += 1
    if list(card.keys()) != FIELDS:
        hits.append((cid, 'field_whitelist', list(card.keys())))
    for path, key in walk_keys(card):
        if key in BANNED:
            hits.append((cid, 'banned_key', path))
        for fb in FIELD_BLACKLIST:
            if fb in key:
                hits.append((cid, 'field_blacklist', path))
    for path, s in walk_str(card):
        for m in LEVEL1:
            if m in s:
                hits.append((cid, 'level1_marker', f'{path}:{m}'))
        for m in LEVEL2:
            if m in s:
                hits.append((cid, 'level2_marker', f'{path}:{m}'))

result = {'cards_scanned': cards, 'hits': hits, 'hit_count': len(hits)}
out = os.path.join(BASE, 'runs/round84/host-opening-scan-h28-result-r84.json')
with open(out, 'w', encoding='utf-8') as fh:
    json.dump(result, fh, ensure_ascii=False, indent=1)
print(json.dumps(result, ensure_ascii=False)[:2000])
