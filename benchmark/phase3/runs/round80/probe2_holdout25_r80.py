#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R80 holdout25 探查2（只读）：GSZ 五要素复核全池扫描＋DS 入选段四柱/合并组核＋KW/QW/SG 入选段细节。"""
import json, os, re
BASE='/home/hatch/workspace/divination/benchmark/phase3'
DIG76=os.path.join(BASE,'runs/round76/digestion')
def load(p): return json.load(open(p,encoding='utf-8'))
gsz=load(os.path.join(BASE,'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
by={e['provisional_id']:e for e in gsz['entries']}
book=open(os.path.join(BASE,'runs/round76/gsz-book-r76.txt'),encoding='utf-8').read()
LIUQIN=['兄弟','子孙','妻财','官鬼','父母']
GANZHI=list('甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥')
def five(cid):
    e=by[cid]; chart=e['input_fields']['chart']; lines=chart['chart_lines_top_to_bottom']; joined='\n'.join(lines)
    el={}
    el['gua_name']=bool(chart.get('ben_gua'))
    el['moving']=('动' in joined) or bool(chart.get('bian_gua'))
    el['shi_ying']=('世' in joined) and ('应' in joined)
    el['liuqin_nazhi']=all(any(lq in ln and any(g in ln for g in GANZHI) for ln in lines) for lq in [x for x in LIUQIN if any(x in ln for ln in lines)]) and sum(1 for ln in lines if any(lq in ln for lq in LIUQIN))>=6
    asked=e['input_fields']['asked_at']
    el['yuejian_richen']=bool(re.search(r'月',asked) and re.search(r'日',asked))
    el['in_book_ben_gua']=chart['ben_gua'][:2] in book or chart['ben_gua'] in book
    el['in_book_asked']=asked.split('（')[0][:7] in book.replace(' ','')
    return el
net=gsz['counts']['net_eligible_A_low_present']
for cid in net:
    e=by[cid]
    base=(e['grade']=='A' and e['pollution']=='low' and e['anchor_presence']=='present' and e['eligible_net'] is True and e['master_prediction'].strip() and e['outcome_record'].strip())
    el=five(cid); ok=base and all(el.values())
    print(cid,'base',base,'pass',ok,el)
print('--- DS 025-033 ---')
ds=load(os.path.join(DIG76,'SUPPLY-MINING-duanshi-r76.json'))
for r in ds['records']:
    if r['case_id'] in ('DS-025','DS-026','DS-027','DS-028','DS-029','DS-030','DS-031','DS-032','DS-033'):
        print(r['case_id'], r['input_side']['pillars_verbatim'], '| subj:', r['input_side']['subject'][:40], '| dedup:', r['dedup'][:120], '| verdict:', (r.get('verdict_note') or '')[:80], '| gap_mp:', '……' in r['master_assertion'], 'gap_oc:', '……' in r['outcome'])
print('--- KW 026-032 ---')
kw=load(os.path.join(DIG76,'SUPPLY-MINING-kaiwu-r76.json'))
for c in kw['cases']:
    if c['case_id'] in ('QM-026','QM-027','QM-028','QM-029','QM-030','QM-031','QM-032'):
        print(c['case_id'], c['stem_check'], '| src:', c['source'][:60], '| gap_mp:', '……' in c['master_assertion'], 'gap_oc:', '……' in c['outcome'])
        print('   input_side head:', c['input_side'][:150])
print('--- QW 208-211 ---')
qw=load(os.path.join(DIG76,'SUPPLY-MINING-qiwu-r76.json'))
for c in qw['cases']:
    if c['case_id'] in ('QM-208','QM-209','QM-210','QM-211'):
        print(c['case_id'], '| section:', c['source']['section'], '| gap_mp:', '……' in c['master_assertion'], 'gap_oc:', '……' in c['outcome'], '| notes:', (c.get('notes') or '')[:100])
        print('   q:', c['input_side'].get('question','')[:120])
print('--- SG 310-311 ---')
sg=load(os.path.join(DIG76,'SUPPLY-MINING-shijianguo-r76.json'))
for c in sg['cases']:
    if c['case_id'] in ('QM-310','QM-311'):
        print(c['case_id'], '| section:', c['source']['section'], '| tc:', c['transcription_confidence'][:120], '| gap_mp:', '……' in c['master_assertion'], 'gap_oc:', '……' in c['outcome'], '| notes:', (c.get('notes') or '')[:150])
        print('   q:', c['input_side'].get('question','')[:120])
