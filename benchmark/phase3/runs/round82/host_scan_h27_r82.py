#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R82 主持第三道复扫（开封前置）：独立脚本，不 import 构建/封存脚本。
按显式 id 清单逐件精确打开盘上 holdout27 输入卡，重行 R42 PREREG §5
标记集（LEVEL1 断语标记／LEVEL2 结局标记／字段名黑名单／禁用键／字段白名单）
扫描，结果打印并落 runs/round82/host-scan-h27-result-r82.json。"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
IDS = ['DS-040', 'DS-041', 'DS-042', 'DS-043', 'DS-044', 'DS-045', 'DS-046',
       'DS-048', 'DS-049',
       'QM-044', 'QM-045', 'QM-046', 'QM-047', 'QM-048', 'QM-049', 'QM-052',
       'QM-055', 'QM-058',
       'GSZ-079', 'GSZ-081', 'GSZ-084', 'GSZ-086', 'GSZ-088',
       'WHY-008', 'WHY-009', 'WHY-010', 'WHY-011']
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
    p = os.path.join(BASE, 'holdout27', 'inputs', f'{cid}.json')
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
out = os.path.join(BASE, 'runs/round82/host-scan-h27-result-r82.json')
with open(out, 'w', encoding='utf-8') as fh:
    json.dump(result, fh, ensure_ascii=False, indent=1)
print(json.dumps(result, ensure_ascii=False)[:2000])
