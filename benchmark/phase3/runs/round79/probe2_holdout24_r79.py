#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R79 探查 2（只读）：倾印 holdout24 候选例台账全文，供建卡组写。输出到 round79 内文本件。"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
DIG76 = os.path.join(BASE, 'runs/round76/digestion')
OUT = os.path.join(BASE, 'runs/round79/probe2-holdout24-out-r79.txt')

def load(p):
    return json.load(open(p, encoding='utf-8'))

ds = load(os.path.join(DIG76, 'SUPPLY-MINING-duanshi-r76.json'))
kw = load(os.path.join(DIG76, 'SUPPLY-MINING-kaiwu-r76.json'))
qw = load(os.path.join(DIG76, 'SUPPLY-MINING-qiwu-r76.json'))
sg = load(os.path.join(DIG76, 'SUPPLY-MINING-shijianguo-r76.json'))
zc = load(os.path.join(DIG76, 'SUPPLY-MINING-zichubu-r76.json'))
gsz = load(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))

lines = []
def dump(tag, obj):
    lines.append(f'===== {tag} =====')
    lines.append(json.dumps(obj, ensure_ascii=False, indent=1))

for r in ds['records']:
    if r['case_id'] in ('DS-019', 'DS-020', 'DS-021', 'DS-022', 'DS-023', 'DS-024', 'DS-025'):
        dump(r['case_id'], r)
for c in kw['cases']:
    if c['case_id'] in ('QM-021', 'QM-022', 'QM-023', 'QM-024', 'QM-025'):
        dump(c['case_id'], c)
for c in qw['cases']:
    if c['case_id'] in ('QM-206', 'QM-207'):
        dump(c['case_id'], c)
for c in sg['cases']:
    if c['case_id'] in ('QM-307', 'QM-308', 'QM-309'):
        dump(c['case_id'], c)
for c in zc['cases']:
    if c['case_id'] in ('ZCB-012', 'ZCB-013', 'ZCB-014', 'ZCB-015'):
        dump(c['case_id'], c)
gsz_by = {e['provisional_id']: e for e in gsz['entries']}
for cid in ('GSZ-034', 'GSZ-038', 'GSZ-041', 'GSZ-042', 'GSZ-043', 'GSZ-046',
            'GSZ-047', 'GSZ-049', 'GSZ-050', 'GSZ-052'):
    dump(cid, gsz_by[cid])

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('written', OUT, os.path.getsize(OUT))
