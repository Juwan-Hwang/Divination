#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R79 host third scan (seal verification) for holdout23 inputs.
Independent host implementation; marker set verbatim per R42 PREREG s.5
(as carried in runs/round79/scan_holdout23_r79.py). Scans the 27 input
cards only (gold file is read solely to derive outcome/assertion
fragments; its content is never printed). Also verifies the three
adjudicated cards no longer carry the removed leakage strings.
"""
import json
import sys

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
IDS = ['DS-013', 'DS-014', 'DS-015', 'DS-016', 'DS-017', 'DS-018',
       'QM-015', 'QM-016', 'QM-018', 'QM-019', 'QM-020', 'QM-204', 'QM-205',
       'QM-304', 'QM-305', 'QM-306',
       'ZCB-006', 'ZCB-007', 'ZCB-008', 'ZCB-009', 'ZCB-010', 'ZCB-011',
       'GSZ-028', 'GSZ-030', 'GSZ-031', 'GSZ-032', 'GSZ-033']
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
CEZI = {c for c in IDS if c.startswith('ZCB-')}
REMOVED = {}


def walk_strings(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f'{path}[{i}]')
    elif isinstance(obj, str):
        yield path, obj


def walk_keys(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k
            yield from walk_keys(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_keys(v)


def fragments(text, n=8):
    text = ''.join(text.split())
    return {text[i:i + n] for i in range(len(text) - n + 1)}


def main():
    gold = {}
    with open(f'{BASE}/holdout23/test_gold.jsonl', encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if line:
                r = json.loads(line)
                gold[r['id']] = r
    assert set(gold) == set(IDS), 'gold id set mismatch'
    hits = []
    frag_notes = []
    for cid in IDS:
        card = json.load(open(f'{BASE}/holdout23/inputs/{cid}.json', encoding='utf-8'))
        blob = json.dumps(card, ensure_ascii=False)
        for path, s in walk_strings(card):
            for m in LEVEL1 + LEVEL2:
                if m in s:
                    hits.append((cid, path, 'marker', m))
            for m in FIELD_BLACKLIST:
                if m in path:
                    hits.append((cid, path, 'fieldname', m))
        for k in walk_keys(card):
            if k in BANNED:
                hits.append((cid, '', 'banned-key', k))
        g = gold[cid]
        card_flat = ''.join(blob.split())
        for field in ('master_assertion', 'outcome'):
            for fr in fragments(str(g.get(field, ''))):
                if fr in card_flat:
                    frag_notes.append((cid, field, fr))
        if cid in REMOVED and REMOVED[cid] in blob:
            hits.append((cid, '', 'adjudication-not-applied', REMOVED[cid]))
    hard_frag = [f for f in frag_notes if f[0] not in CEZI]
    print('cards scanned:', len(IDS))
    print('marker/field/banned/adjudication hits:', len(hits), hits[:10])
    print('fragment overlaps (non-cezi, must be 0):', len(hard_frag), hard_frag[:5])
    print('fragment overlaps (cezi, register only):', len([f for f in frag_notes if f[0] in CEZI]))
    ok = not hits and not hard_frag
    print('HOST THIRD SCAN:', 'PASS zero hard hits' if ok else 'FAIL')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
