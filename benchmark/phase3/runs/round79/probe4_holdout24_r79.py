#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R79 探查 4（只读）：预演选例的逐字片段重叠风险（断语/结局片段 vs 台账 input_side 文本）
与「……」缺口标记扫描。片段函数承 holdout23 构建脚本逐字。"""
import json, os, re

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
DIG76 = os.path.join(BASE, 'runs/round76/digestion')

def load(p):
    return json.load(open(p, encoding='utf-8'))

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

ds = {r['case_id']: r for r in load(os.path.join(DIG76, 'SUPPLY-MINING-duanshi-r76.json'))['records']}
kw = {c['case_id']: c for c in load(os.path.join(DIG76, 'SUPPLY-MINING-kaiwu-r76.json'))['cases']}
qw = {c['case_id']: c for c in load(os.path.join(DIG76, 'SUPPLY-MINING-qiwu-r76.json'))['cases']}
sg = {c['case_id']: c for c in load(os.path.join(DIG76, 'SUPPLY-MINING-shijianguo-r76.json'))['cases']}
zc = {c['case_id']: c for c in load(os.path.join(DIG76, 'SUPPLY-MINING-zichubu-r76.json'))['cases']}
gsz = {e['provisional_id']: e for e in load(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))['entries']}

checks = []
for cid in ('DS-019', 'DS-020', 'DS-021', 'DS-022', 'DS-023', 'DS-024'):
    r = ds[cid]
    checks.append((cid, r['master_assertion'], r['outcome'],
                   json.dumps(r['input_side'], ensure_ascii=False) + r['source']))
for cid in ('QM-021', 'QM-022', 'QM-023', 'QM-024', 'QM-025'):
    c = kw[cid]
    checks.append((cid, c['master_assertion'], c['outcome'], c['input_side'] + c['source']))
for cid in ('QM-206', 'QM-207'):
    c = qw[cid]
    checks.append((cid, c['master_assertion'], c['outcome'],
                   json.dumps(c['input_side'], ensure_ascii=False) +
                   json.dumps(c['source'], ensure_ascii=False)))
for cid in ('QM-307', 'QM-308', 'QM-309'):
    c = sg[cid]
    checks.append((cid, c['master_assertion'], c['outcome'],
                   json.dumps(c['input_side'], ensure_ascii=False) +
                   json.dumps(c['source'], ensure_ascii=False)))
for cid in ('ZCB-012', 'ZCB-013', 'ZCB-014', 'ZCB-015'):
    c = zc[cid]
    checks.append((cid, c['master_assertion'], c['outcome'], c['input_side']))
for cid in ('GSZ-034', 'GSZ-038', 'GSZ-041', 'GSZ-042', 'GSZ-043', 'GSZ-046', 'GSZ-047'):
    e = gsz[cid]
    checks.append((cid, e['master_prediction'], e['outcome_record'],
                   json.dumps(e['input_fields'], ensure_ascii=False) + e['source']))

for cid, mp, oc, input_text in checks:
    gap = ('……' in mp) or ('……' in oc) or ('...' in mp) or ('...' in oc)
    mp_hits = [f for f in fragments(mp) if f in input_text]
    oc_hits = [f for f in fragments(oc) if f in input_text]
    print(cid, 'gap:', gap, 'mp_frag_hits_vs_input:', len(mp_hits), mp_hits[:3],
          'oc_frag_hits_vs_input:', len(oc_hits), oc_hits[:3])
