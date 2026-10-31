#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R80 组集封存席独立复扫（断语扫描第二道，本席交卷前独立执行）。
独立实现（不 import 构建脚本）：按显式 id 清单逐件精确打开 holdout25/inputs/<id>.json
与 holdout25/test_gold.jsonl（仅本集自产件），执行：
① R42 PREREG §5 内容级一级/二级标记全字段递归扫描；
② 字段名黑名单扫描；③ 禁用键集递归扫描；④ 字段白名单与键序核；
⑤ 逐字片段扫描（结局片段与断语片段全例须零命中，本集无测字段、无分类例外）；
⑥ 附加短片段核：金标断语任意 ≥8 字连续子串在卡面出现的逐条登记（信息登记，不作断言）。
结果落 runs/round80/scan-holdout25-result-r80.json；任一硬断言不过即非零退出。
适配自 runs/round79/scan_holdout24_r79.py，逐处定点改写集号/id 清单/结果路径；
本集无 ZCB 入选，测字分类例外整段移除（非连环替换，逐处核对）。
"""
import json, os, re, sys

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
IDS = ['DS-025', 'DS-026', 'DS-027', 'DS-028', 'DS-029', 'DS-030',
       'QM-027', 'QM-028', 'QM-029', 'QM-030', 'QM-031', 'QM-032',
       'QM-208', 'QM-209', 'QM-310', 'QM-311',
       'GSZ-049', 'GSZ-050', 'GSZ-052', 'GSZ-053', 'GSZ-054', 'GSZ-055',
       'GSZ-058', 'GSZ-059', 'GSZ-060', 'GSZ-061', 'GSZ-068']
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


golds = {}
for line in open(os.path.join(BASE, 'holdout25/test_gold.jsonl'), encoding='utf-8'):
    if line.strip():
        g = json.loads(line)
        golds[g['id']] = g
assert set(golds) == set(IDS), (set(golds) ^ set(IDS))

per_case = {}
failures = []
for cid in IDS:
    card = json.load(open(os.path.join(BASE, 'holdout25/inputs', f'{cid}.json'),
                          encoding='utf-8'))
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
    fn_hits = [[p, k] for p, k in walk_keys(card)
               if any(f in k for f in FIELD_BLACKLIST)]
    entry['fieldname_hits'] = fn_hits
    if fn_hits:
        failures.append(f'{cid}: 字段名命中 {fn_hits}')
    bk_hits = [p for p, k in walk_keys(card) if k in BANNED]
    entry['banned_key_hits'] = bk_hits
    if bk_hits:
        failures.append(f'{cid}: 禁用键命中 {bk_hits}')
    card_text = json.dumps(card, ensure_ascii=False)
    g = golds[cid]
    oc = [f for f in fragments(g['outcome_record']) if f in card_text]
    mp = [f for f in fragments(g['master_prediction']) if f in card_text]
    entry['outcome_fragment_hits'] = oc
    entry['master_fragment_hits'] = mp
    if oc:
        failures.append(f'{cid}: 结局片段命中 {oc[:3]}')
    if mp:
        failures.append(f'{cid}: 断语片段命中 {mp[:3]}')
    # 附加短片段核（信息登记）：断语 ≥8 字连续子串在卡面出现
    short = set()
    mpn = re.sub(r'\s+', '', g['master_prediction'])
    for n in (10, 9, 8):
        for i in range(0, len(mpn) - n + 1):
            sub = mpn[i:i + n]
            if sub in card_text and not any(sub in s or s in sub for s in short):
                short.add(sub)
    entry['short_substring_info'] = sorted(short)
    per_case[cid] = entry

result = {'scan': 'holdout25 独立复扫（第二道）', 'ids': IDS,
          'per_case': per_case, 'failures': failures,
          'total_marker_hits': sum(len(v['marker_hits']) for v in per_case.values()),
          'total_fieldname_hits': sum(len(v['fieldname_hits']) for v in per_case.values()),
          'total_banned_key_hits': sum(len(v['banned_key_hits']) for v in per_case.values()),
          'total_outcome_fragment_hits': sum(len(v['outcome_fragment_hits']) for v in per_case.values()),
          'total_master_fragment_hits': sum(len(v['master_fragment_hits']) for v in per_case.values()),
          'pass': not failures}
out_path = os.path.join(BASE, 'runs/round80/scan-holdout25-result-r80.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'pass': result['pass'], 'failures': failures,
                  'marker': result['total_marker_hits'],
                  'fieldname': result['total_fieldname_hits'],
                  'banned': result['total_banned_key_hits'],
                  'outcome_frag': result['total_outcome_fragment_hits'],
                  'master_frag': result['total_master_fragment_hits'],
                  'short_info': {k: v['short_substring_info'] for k, v in per_case.items()
                                 if v['short_substring_info']}},
                 ensure_ascii=False))
sys.exit(0 if result['pass'] else 1)
