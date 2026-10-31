#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R80 holdout25 探查3（只读）：GSZ counts 全文＋049-068 条目字段核。"""
import json, os
BASE='/home/hatch/workspace/divination/benchmark/phase3'
def load(p): return json.load(open(p,encoding='utf-8'))
gsz=load(os.path.join(BASE,'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
print(json.dumps(gsz['counts'],ensure_ascii=False,indent=1)[:3000])
print('rules:', json.dumps(gsz.get('rules'),ensure_ascii=False)[:800])
by={e['provisional_id']:e for e in gsz['entries']}
for cid in ('GSZ-049','GSZ-050','GSZ-052','GSZ-058','GSZ-059','GSZ-068'):
    e=by[cid]
    print(cid, {k:(v if not isinstance(v,(dict,list)) else '...') for k,v in e.items()})
    print('  subject:', e.get('subject'), '| source:', e.get('source'))
    print('  question:', e['input_fields']['question'][:100])
print('entries order around 049:', [e['provisional_id'] for e in gsz['entries'][40:60]])
