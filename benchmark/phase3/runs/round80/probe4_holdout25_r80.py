#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R80 holdout25 探查4（只读）：入选段 KW/QW/SG 全文与 DS-030 结局、GSZ 入选段 source/问句。"""
import json, os
BASE='/home/hatch/workspace/divination/benchmark/phase3'
DIG76=os.path.join(BASE,'runs/round76/digestion')
def load(p): return json.load(open(p,encoding='utf-8'))
kw={c['case_id']:c for c in load(os.path.join(DIG76,'SUPPLY-MINING-kaiwu-r76.json'))['cases']}
for cid in ('QM-027','QM-028','QM-029','QM-030','QM-031','QM-032'):
    c=kw[cid]
    print('='*20, cid, '| caster:', c['caster'], '| topic:', c.get('topic'))
    print('INPUT_SIDE:', c['input_side'])
    print('NOTE:', c.get('note'))
qw={c['case_id']:c for c in load(os.path.join(DIG76,'SUPPLY-MINING-qiwu-r76.json'))['cases']}
for cid in ('QM-208','QM-209'):
    c=qw[cid]
    print('='*20, cid, 'QW input_side keys:', list(c['input_side'].keys()))
    print(json.dumps(c['input_side'],ensure_ascii=False)[:1500])
    print('OUTCOME:', c['outcome'])
sg={c['case_id']:c for c in load(os.path.join(DIG76,'SUPPLY-MINING-shijianguo-r76.json'))['cases']}
for cid in ('QM-310','QM-311'):
    c=sg[cid]
    print('='*20, cid, 'SG input_side:', json.dumps(c['input_side'],ensure_ascii=False)[:1200])
ds={r['case_id']:r for r in load(os.path.join(DIG76,'SUPPLY-MINING-duanshi-r76.json'))['records']}
print('='*20,'DS-030 outcome:', ds['DS-030']['outcome'])
print('DS-030 mp:', ds['DS-030']['master_assertion'])
print('DS-030 subject:', ds['DS-030']['input_side']['subject'], '| source:', ds['DS-030']['source'])
for cid in ('DS-025','DS-026','DS-027','DS-028','DS-029'):
    print(cid,'subj:',ds[cid]['input_side']['subject'],'| src:',ds[cid]['source'][-40:])
gsz={e['provisional_id']:e for e in load(os.path.join(BASE,'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))['entries']}
for cid in ('GSZ-049','GSZ-050','GSZ-052','GSZ-053','GSZ-054','GSZ-055','GSZ-058','GSZ-059','GSZ-060','GSZ-061','GSZ-068'):
    e=gsz[cid]
    print(cid,'| src:',e['source'],'| subj:',e['subject'],'| asked:',e['input_fields']['asked_at'],'| q:',e['input_fields']['question'][:60],'| ben:',e['input_fields']['chart'].get('ben_gua'),'| bian:',e['input_fields']['chart'].get('bian_gua'))
