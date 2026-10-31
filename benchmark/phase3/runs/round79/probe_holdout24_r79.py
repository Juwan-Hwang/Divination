#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R79 组集封存席探查（只读）：打印六台账候选序、字段结构、存量计数。不写任何产物。"""
import json, os

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
DIG76 = os.path.join(BASE, 'runs/round76/digestion')

def load(p):
    return json.load(open(p, encoding='utf-8'))

ds = load(os.path.join(DIG76, 'SUPPLY-MINING-duanshi-r76.json'))
kw = load(os.path.join(DIG76, 'SUPPLY-MINING-kaiwu-r76.json'))
qw = load(os.path.join(DIG76, 'SUPPLY-MINING-qiwu-r76.json'))
sg = load(os.path.join(DIG76, 'SUPPLY-MINING-shijianguo-r76.json'))
zc = load(os.path.join(DIG76, 'SUPPLY-MINING-zichubu-r76.json'))
gsz = load(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))

print('== top-level keys ==')
for name, m in (('DS', ds), ('KW', kw), ('QW', qw), ('SG', sg), ('ZCB', zc), ('GSZ', gsz)):
    print(name, list(m.keys()))
    for k, v in m.items():
        if not isinstance(v, list):
            print('   ', k, '=', json.dumps(v, ensure_ascii=False)[:400])

print('== DS records: id, elig, anchor, contam, filters-pass, assertion/outcome nonempty, dedup ==')
for r in ds['records']:
    fp = all(str(v).startswith('pass') for v in r['filters'].values())
    print(r['case_id'], r['eligible_net'], r['anchor_status'], r['contamination_pre'], fp,
          bool(r['master_assertion'].strip()), bool(r['outcome'].strip()),
          '| dedup:', json.dumps(r.get('dedup'), ensure_ascii=False)[:120],
          '| comp:', r.get('composition_type'))

print('== KW cases: id, anchor, contam, separable, stem ok, assertion/outcome ==')
for c in kw['cases']:
    print(c['case_id'], c['anchor_status'], c['contamination_pre'], c['separable'],
          c['stem_check']['tianpan_ok'], c['stem_check']['dipan_ok'],
          bool(c['master_assertion'].strip()), bool(c['outcome'].strip()))

print('== QW cases ==')
for c in qw['cases']:
    print(c['case_id'], c['anchor_status'], c['contamination_pre'], c['separable'],
          bool(c['master_assertion'].strip()), bool(c['outcome'].strip()),
          '| notes:', json.dumps(c.get('notes'), ensure_ascii=False)[:100])

print('== SG cases ==')
for c in sg['cases']:
    print(c['case_id'], c['anchor_status'], c['contamination_pre'], c['separable'],
          bool(c['master_assertion'].strip()), bool(c['outcome'].strip()),
          '| notes:', json.dumps(c.get('notes'), ensure_ascii=False)[:160])

print('== ZCB cases: id, eligible, anchor, contam, separable, assertion/outcome ==')
for c in zc['cases']:
    print(c['case_id'], c.get('eligible'), c['anchor_status'], c['contamination_pre'],
          c['separable'], bool(c['master_assertion'].strip()), bool(c['outcome'].strip()),
          '| assertion:', c['master_assertion'][:60])

print('== GSZ counts keys ==')
print(json.dumps(gsz['counts'], ensure_ascii=False)[:800])
print('== GSZ net pool order ==')
print(gsz['counts']['net_eligible_A_low_present'])
print('== GSZ entries count ==', len(gsz['entries']))
