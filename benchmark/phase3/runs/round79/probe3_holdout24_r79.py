#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R79 探查 3（只读）：GSZ 候选五要素复核预演（函数承 holdout23 构建脚本逐字）＋已用并集预演规模。
只取各金标 id 字段建集，不打开已封存集金标正文。"""
import json, os, re

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'

def load_json(p):
    return json.load(open(p, encoding='utf-8'))

# 已用并集（口径：增补件 §二.1 —— dev 基线键集＋inputs-dev9/10/11/12 与 inputs 目录卡 id
# ＋holdout2–23 各 test_gold.jsonl 仅取 id＋各集 inputs 目录卡 id；另承历轮口径含
# phase2 splits2 holdout2 与顶层 inputs6–10 目录卡 id，一并实算登记）
dev_ids = set(load_json(os.path.join(BASE, 'data/master-baseline-dev9.json')).keys())
n0 = len(dev_ids)
for dv in ('inputs-dev9', 'inputs-dev10', 'inputs-dev11', 'inputs-dev12', 'inputs'):
    d = os.path.join(BASE, dv)
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                dev_ids.add(fn[:-5])
print('dev baseline keys:', n0, 'dev pool with dirs:', len(dev_ids))

h2_ids = set(load_json(os.path.join(ROOT, 'benchmark/phase2/splits2.json'))['holdout2'])
print('phase2 splits2 holdout2:', len(h2_ids))

gold_ids = set()
per = {}
for i in range(3, 24):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    s = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip():
                s.add(json.loads(line)['id'])
    per[f'holdout{i}'] = len(s)
    gold_ids |= s
print('gold per set:', per)
print('holdout3_23 gold union:', len(gold_ids))

input_ids = set()
for i in range(2, 24):
    for dname in (f'holdout{i}/inputs', f'holdout{i}-inputs'):
        d = os.path.join(BASE, dname)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'):
                    input_ids.add(fn[:-5])
print('holdout2_23 input card ids:', len(input_ids))
extra = set()
for i in range(6, 11):
    d = os.path.join(BASE, f'inputs{i}')
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                extra.add(fn[:-5])
print('toplevel inputs6_10:', len(extra))
used = dev_ids | h2_ids | gold_ids | input_ids | extra
print('USED UNION TOTAL:', len(used))
for probe in ('DS-019', 'DS-020', 'QM-021', 'QM-206', 'QM-307', 'QM-308', 'ZCB-012',
              'ZCB-003', 'GSZ-034', 'GSZ-020'):
    print(probe, 'in used:', probe in used)

# ---- GSZ 五要素（承 build_holdout23_r78.five_elements 逐字） ----
gsz_mining = load_json(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
gsz_by = {e['provisional_id']: e for e in gsz_mining['entries']}
book_txt = open(os.path.join(BASE, 'runs/round76/gsz-book-r76.txt'), encoding='utf-8').read()
LIUQIN = ['兄弟', '子孙', '妻财', '官鬼', '父母']
GANZHI = list('甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥')

def five_elements(cid):
    e = gsz_by[cid]
    chart = e['input_fields']['chart']
    lines = chart['chart_lines_top_to_bottom']
    joined = '\n'.join(lines)
    el = {}
    el['gua_name'] = bool(chart.get('ben_gua'))
    el['moving'] = ('动' in joined) or bool(chart.get('bian_gua'))
    el['shi_ying'] = ('世' in joined) and ('应' in joined)
    el['liuqin_nazhi'] = all(
        any(lq in ln and any(g in ln for g in GANZHI) for ln in lines)
        for lq in [x for x in LIUQIN if any(x in ln for ln in lines)]) and \
        sum(1 for ln in lines if any(lq in ln for lq in LIUQIN)) >= 6
    asked = e['input_fields']['asked_at']
    el['yuejian_richen'] = bool(re.search(r'月', asked) and re.search(r'日', asked))
    el['in_book_ben_gua'] = chart['ben_gua'][:2] in book_txt or chart['ben_gua'] in book_txt
    el['in_book_asked'] = asked.split('（')[0][:7] in book_txt.replace(' ', '')
    return el

net = gsz_mining['counts']['net_eligible_A_low_present']
pool = [c for c in net if c not in used]
print('GSZ net:', len(net), 'used in net:', [c for c in net if c in used], 'pool:', len(pool))
picked = []
for cid in pool:
    e = gsz_by[cid]
    base_ok = (e['grade'] == 'A' and e['pollution'] == 'low'
               and e['anchor_presence'] == 'present' and e['eligible_net'] is True
               and e['master_prediction'].strip() and e['outcome_record'].strip())
    el = five_elements(cid)
    ok = base_ok and all(el.values())
    print(cid, 'base:', base_ok, 'elements:', el, 'PASS:', ok)
    if ok:
        picked.append(cid)
    if len(picked) == 9:
        break
print('GSZ picked (first 9 passing):', picked)
