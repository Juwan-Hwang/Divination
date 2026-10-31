#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R79 holdout24 组集修订席独立复扫（主持裁处执行后，修订席自写、独立实现）。
不 import 构建脚本/原复扫脚本/改写脚本；标记集参照 runs/round79/scan_holdout24_r79.py
（承 R42 PREREG §5 一级/二级标记、字段名黑名单、禁用键集、字段白名单）。
按显式 id 清单逐件精确打开 holdout24/inputs 全部 27 卡与本集 test_gold.jsonl，执行：
① 内容级一级/二级标记全字段递归扫描；② 字段名黑名单；③ 禁用键集；
④ 字段白名单与键序；⑤ 逐字片段扫描（结局片段全例、断语片段非测字例）；
⑥ 附加短片段核（金标断语 ≥8 字连续子串在卡面出现者逐条登记，仅信息登记）；
⑦ 裁处专项核：QM-308/309 例题字样自 setting/provenance 消失且章节题保留、
   QM-206 question 与写定保留值逐字全等。
结果落 runs/round79/rescan-holdout24-result-r79-revseat.json；硬断言不过即非零退出。
"""
import json
import os
import re
import sys

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
IDS = ['DS-019', 'DS-020', 'DS-021', 'DS-022', 'DS-023', 'DS-024',
       'QM-021', 'QM-022', 'QM-023', 'QM-024', 'QM-025',
       'QM-206', 'QM-207', 'QM-307', 'QM-308', 'QM-309',
       'ZCB-012', 'ZCB-013', 'ZCB-014', 'ZCB-015',
       'GSZ-034', 'GSZ-038', 'GSZ-041', 'GSZ-042', 'GSZ-043', 'GSZ-046', 'GSZ-047']
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
FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
          'provenance', 'redistributable', 'license_status', 'anchors']
CEZI = {c for c in IDS if c.startswith('ZCB-')}
Q206_KEEP = '求測者未明言來意，只說「最近我遇到了麻煩事，如果不說，你能測出來嗎？」'


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


def main():
    golds = {}
    with open(os.path.join(BASE, 'holdout24/test_gold.jsonl'), encoding='utf-8') as f:
        for line in f:
            if line.strip():
                g = json.loads(line)
                golds[g['id']] = g
    assert set(golds) == set(IDS), (set(golds) ^ set(IDS))

    per_case = {}
    failures = []
    for cid in IDS:
        with open(os.path.join(BASE, 'holdout24/inputs', f'{cid}.json'), encoding='utf-8') as f:
            card = json.load(f)
        entry = {}
        if list(card.keys()) != FIELDS:
            failures.append(f'{cid}: 字段白名单/键序不合 {list(card.keys())}')
        marker_hits = []
        for path, s in walk_strings(card):
            for lvl, markers in (('L1', LEVEL1), ('L2', LEVEL2)):
                for m in markers:
                    if m in s:
                        marker_hits.append([path, lvl, m])
        entry['marker_hits'] = marker_hits
        if marker_hits:
            failures.append(f'{cid}: 标记命中 {marker_hits}')
        fn_hits = [[p, k] for p, k in walk_keys(card) if any(x in k for x in FIELD_BLACKLIST)]
        entry['fieldname_hits'] = fn_hits
        if fn_hits:
            failures.append(f'{cid}: 字段名命中 {fn_hits}')
        bk_hits = [p for p, k in walk_keys(card) if k in BANNED]
        entry['banned_key_hits'] = bk_hits
        if bk_hits:
            failures.append(f'{cid}: 禁用键命中 {bk_hits}')
        card_text = json.dumps(card, ensure_ascii=False)
        g = golds[cid]
        oc = [x for x in fragments(g['outcome_record']) if x in card_text]
        mp = [x for x in fragments(g['master_prediction']) if x in card_text]
        entry['outcome_fragment_hits'] = oc
        entry['master_fragment_hits'] = mp
        if oc:
            failures.append(f'{cid}: 结局片段命中 {oc[:3]}')
        if cid not in CEZI and mp:
            failures.append(f'{cid}: 非测字断语片段命中 {mp[:3]}')
        short = set()
        mpn = re.sub(r'\s+', '', g['master_prediction'])
        for n in (10, 9, 8):
            for i in range(0, len(mpn) - n + 1):
                sub = mpn[i:i + n]
                if sub in card_text and not any(sub in s or s in sub for s in short):
                    short.add(sub)
        entry['short_substring_info'] = sorted(short)
        per_case[cid] = entry

    # ⑦ 裁处专项核
    adjudication = {}
    c308 = json.load(open(os.path.join(BASE, 'holdout24/inputs/QM-308.json'), encoding='utf-8'))
    ok308 = ('出走的妻子能平安回家' not in c308['setting']
             and '出走的妻子能平安回家' not in c308['provenance']
             and '行人走失预测' in c308['setting'] and '行人走失预测' in c308['provenance'])
    adjudication['QM-308_removed_and_chapter_kept'] = ok308
    if not ok308:
        failures.append('QM-308: 裁处专项核不过')
    c309 = json.load(open(os.path.join(BASE, 'holdout24/inputs/QM-309.json'), encoding='utf-8'))
    ok309 = ('弟弟有病手术后全愈' not in c309['setting']
             and '弟弟有病手术后全愈' not in c309['provenance']
             and '人体疾病预测' in c309['setting'] and '人体疾病预测' in c309['provenance'])
    adjudication['QM-309_removed_and_chapter_kept'] = ok309
    if not ok309:
        failures.append('QM-309: 裁处专项核不过')
    c206 = json.load(open(os.path.join(BASE, 'holdout24/inputs/QM-206.json'), encoding='utf-8'))
    ok206 = (c206['question'] == Q206_KEEP)
    adjudication['QM-206_question_equals_keep'] = ok206
    if not ok206:
        failures.append('QM-206: 裁处专项核不过')

    result = {
        'scan': 'holdout24 修订席独立复扫（R79 主持裁处执行后）',
        'ids': IDS, 'per_case': per_case, 'failures': failures,
        'adjudication_checks': adjudication,
        'total_marker_hits': sum(len(v['marker_hits']) for v in per_case.values()),
        'total_fieldname_hits': sum(len(v['fieldname_hits']) for v in per_case.values()),
        'total_banned_key_hits': sum(len(v['banned_key_hits']) for v in per_case.values()),
        'total_outcome_fragment_hits': sum(len(v['outcome_fragment_hits']) for v in per_case.values()),
        'total_master_fragment_hits_non_cezi': sum(
            len(v['master_fragment_hits']) for k, v in per_case.items() if k not in CEZI),
        'total_master_fragment_hits_cezi': sum(
            len(v['master_fragment_hits']) for k, v in per_case.items() if k in CEZI),
        'short_substring_info': {k: v['short_substring_info'] for k, v in per_case.items()
                                 if v['short_substring_info']},
        'pass': not failures,
    }
    out_path = os.path.join(BASE, 'runs/round79/rescan-holdout24-result-r79-revseat.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(json.dumps({'pass': result['pass'], 'failures': failures,
                      'marker': result['total_marker_hits'],
                      'fieldname': result['total_fieldname_hits'],
                      'banned': result['total_banned_key_hits'],
                      'outcome_frag': result['total_outcome_fragment_hits'],
                      'master_frag_non_cezi': result['total_master_fragment_hits_non_cezi'],
                      'master_frag_cezi': result['total_master_fragment_hits_cezi'],
                      'adjudication_checks': adjudication,
                      'short_info': result['short_substring_info']},
                     ensure_ascii=False))
    return 0 if result['pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
