#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R80 holdout25 探查（只读）：已用并集复算＋各源资格池登记序清单。"""
import json, os
BASE='/home/hatch/workspace/divination/benchmark/phase3'
ROOT='/home/hatch/workspace/divination'
DIG76=os.path.join(BASE,'runs/round76/digestion')
def load(p): return json.load(open(p,encoding='utf-8'))
# used union exactly as r79 build script, extended to holdout24
dev_ids=set(load(os.path.join(BASE,'data/master-baseline-dev9.json')).keys())
src={'dev9_keys':len(dev_ids)}
for dv in ('inputs-dev9','inputs-dev10','inputs-dev11','inputs-dev12','inputs'):
    d=os.path.join(BASE,dv)
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'): dev_ids.add(fn[:-5])
src['dev_pool']=len(dev_ids)
h2=set(load(os.path.join(ROOT,'benchmark/phase2/splits2.json'))['holdout2'])
gold=set(); per={}
for i in range(3,25):
    p=os.path.join(BASE,f'holdout{i}/test_gold.jsonl'); s=set()
    if os.path.exists(p):
        for line in open(p,encoding='utf-8'):
            if line.strip(): s.add(json.loads(line)['id'])
    per[f'holdout{i}']=len(s); gold|=s
src['gold_per_set']=per; src['gold_total']=len(gold)
inp=set()
for i in range(2,25):
    for dn in (f'holdout{i}/inputs',f'holdout{i}-inputs'):
        d=os.path.join(BASE,dn)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'): inp.add(fn[:-5])
src['holdout_input_ids']=len(inp)
extra=set()
for i in range(6,11):
    d=os.path.join(BASE,f'inputs{i}')
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'): extra.add(fn[:-5])
src['toplevel_inputs6_10']=len(extra)
used=dev_ids|h2|gold|inp|extra
src['used_union_total']=len(used)
print(json.dumps(src,ensure_ascii=False,indent=1))
# DS
ds=load(os.path.join(DIG76,'SUPPLY-MINING-duanshi-r76.json'))
print('DS keys sample', list(ds['records'][0].keys()))
print('DS total', len(ds['records']))
# merged group info: look for fields mentioning merge/合并
for r in ds['records'][:3]:
    print('DS sample', json.dumps(r,ensure_ascii=False)[:800])
cands=[]
for r in ds['records']:
    ok = r['eligible_net'] is True and r['anchor_status']=='present' and r['contamination_pre']=='low' and all(str(v).startswith('pass') for v in r['filters'].values()) and r['master_assertion'].strip() and r['outcome'].strip()
    if ok: cands.append(r['case_id'])
print('DS cands all', cands)
print('DS cands unused', [c for c in cands if c not in used])
# KW
kw=load(os.path.join(DIG76,'SUPPLY-MINING-kaiwu-r76.json'))
print('KW total', len(kw['cases']), 'keys', list(kw['cases'][0].keys()))
full=[c['case_id'] for c in kw['cases'] if c['anchor_status']=='present' and c['contamination_pre']=='low' and c['separable'] is True and c['stem_check']['tianpan_ok'] and c['stem_check']['dipan_ok'] and c['master_assertion'].strip() and c['outcome'].strip()]
print('KW full', full)
print('KW full unused', [c for c in full if c not in used])
# QW
qw=load(os.path.join(DIG76,'SUPPLY-MINING-qiwu-r76.json'))
print('QW total', len(qw['cases']), 'keys', list(qw['cases'][0].keys()))
qwc=[c['case_id'] for c in qw['cases'] if c['anchor_status']=='present' and c['contamination_pre']=='low' and c['separable'] is True and c['master_assertion'].strip() and c['outcome'].strip()]
print('QW cands', qwc); print('QW unused', [c for c in qwc if c not in used])
# SG
sg=load(os.path.join(DIG76,'SUPPLY-MINING-shijianguo-r76.json'))
print('SG total', len(sg['cases']), 'keys', list(sg['cases'][0].keys()))
sgc=[c['case_id'] for c in sg['cases'] if c['anchor_status']=='present' and c['contamination_pre']=='low' and c['separable'] is True and c['master_assertion'].strip() and c['outcome'].strip()]
print('SG cands', sgc); print('SG unused', [c for c in sgc if c not in used])
# GSZ
gsz=load(os.path.join(BASE,'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
print('GSZ keys', list(gsz.keys()))
net=gsz['counts']['net_eligible_A_low_present']
print('GSZ net len', len(net), net)
print('GSZ net unused', [c for c in net if c not in used])
