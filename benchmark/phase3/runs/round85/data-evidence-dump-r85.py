#!/usr/bin/env python3
# R85 data seat: structured evidence dump for flag adjudication. Read-only.
import json, os
BASE='/home/hatch/workspace/divination/benchmark/phase3'
FLAGS="LY-533 BQ-025 LR3-112 LY-513 LY-240 YY-023 LY-206 AS-004 LY-216 LY-329 LY-504 LY-506 LY-205 BQ-021 AS-015 BZ-104 LY-524 LY-529 LY-015 LY-320 LY-036 LY-525 LR3-002 LY-628 LR3-101 LY-212 LY-105 LY-104 LY-510 LY-413 LY-259 LY-516 LY-623 LY-430 LY-251 LY-614 LY-436 LR2-023 BQ-001 AS-307 LY-437 BZ-036 BZ-037 OC-026 LY-220 AS-210 YM-070 LR3-107 LY-627 YY2-003 LY-011 LY-222 BQ-017 LY-540 LY-441 LY-629 LY-458 LY-508 LY-531 LY-207 LY-418 LY-434 LY-523 LY-411 LY-528 AS-301 LY-445 BZ-105 LY-227 YM-030 LR2-022 BZ-304 YM-068 YY2-004 LY-538 LY-023 OC-009 LY-443 OC-023 LY-234 YM-059 LY-203 LY-028 LY-537 LY-602 BZ-040 YM-067 LY-231 LY-526 AS-209 YM-043 LY-103 LY-539 YY-017 LY-255 LY-433 LY-429 LY-425 LY-517 MH-001 MH-003 AS-009 LY-406 LY-446 BZ-029 LY-204 BZ-042 LR2-016 LY-342".split()
man=json.load(open(f'{BASE}/runs/round85/judging/outcome-manifest.json'))
cases=man['cases']
hm=json.load(open(f'{BASE}/runs/round85/judging/host-mapping.json'))
inv={v:k for k,v in hm.items()}
mx=json.load(open(f'{BASE}/runs/round85/judging/judgeX-merged.json'))
my=json.load(open(f'{BASE}/runs/round85/judging/judgeY-merged.json'))
r84=json.load(open(f'{BASE}/data/case-annotations-r84.json'))
reg={a['case_id']:a for a in r84['annotations']}
# packets carry_note: search packetA/B (and 1-4 fallback)
packets={}
for pn in ['packetA.json','packetB.json']:
    for it in json.load(open(f'{BASE}/runs/round85/judging/{pn}')):
        packets[it['anon_id']]=it
# manifest layers: collect notes per case
layers={}
for k,v in man.items():
    if isinstance(v,dict):
        for cid,txt in v.items():
            if isinstance(txt,str):
                layers.setdefault(cid,[]).append((k,txt))
out=[]
for cid in FLAGS:
    out.append(f'######## {cid}')
    a=reg.get(cid)
    if a: out.append(f"IN-REG: disp={a['disposition']} round={a['registered_round']} flag={a['flag'][:160]}")
    else: out.append('IN-REG: NO')
    cp=f'{BASE}/inputs-dev12/{cid}.json'
    if os.path.exists(cp):
        c=json.load(open(cp))
        ctx=c.get('context',{})
        out.append(f"Q: {ctx.get('question')} | setting: {ctx.get('setting')} | trad: {c.get('tradition')} system: {c.get('system')}")
    else: out.append('CARD: MISSING in inputs-dev12')
    out.append(f"OUTCOME: {cases.get(cid)}")
    anon=inv.get(cid)
    out.append(f"ANON: {anon}")
    pk=packets.get(anon)
    if pk and pk.get('carry_note'): out.append(f"CARRY: {pk['carry_note']}")
    for lk,txt in layers.get(cid,[]):
        out.append(f"LAYER {lk}: {txt[:400]}")
    if anon in mx: out.append(f"Xreason: {mx[anon].get('reason')}")
    if anon in my: out.append(f"Yreason: {my[anon].get('reason')}")
    pp=f'{BASE}/runs/round85/predictions/{cid}.json'
    if os.path.exists(pp):
        pr=json.load(open(pp))
        b=pr.get('basis') or pr.get('prediction') or ''
        out.append(f"PREDbasis: {str(b)[:500]}")
    out.append('')
open(f'{BASE}/runs/round85/data-evidence-r85.txt','w').write('\n'.join(out))
print('written', len(FLAGS))
