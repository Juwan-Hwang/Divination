# -*- coding: utf-8 -*-
"""R65 S3 分析引擎: 只读 inputs-dev12 本批60例, 输出结构化事实表供定断。"""
import json, re

BASE='/home/hatch/workspace/divination/benchmark/phase3'
IDS=[]
b=json.load(open(f'{BASE}/runs/round65/batches.json'))
for k in ['B07','B08','B09']: IDS+=b[k]

BR=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
EL={'子':'水','亥':'水','寅':'木','卯':'木','巳':'火','午':'火','申':'金','酉':'金','辰':'土','戌':'土','丑':'土','未':'土'}
SHENG={'木':'火','火':'土','土':'金','金':'水','水':'木'}
KE={'木':'土','土':'水','水':'火','火':'金','金':'木'}
HE={frozenset(p) for p in [('子','丑'),('寅','亥'),('卯','戌'),('辰','酉'),('巳','申'),('午','未')]}
CHONG={frozenset(p) for p in [('子','午'),('丑','未'),('寅','申'),('卯','酉'),('辰','戌'),('巳','亥')]}
MU={'木':'未','火':'戌','金':'丑','水':'辰','土':'辰'}
JUE={'木':'申','火':'亥','金':'寅','水':'巳','土':'巳'}
STEMS='甲乙丙丁戊己庚辛壬癸'
XUN=[('甲子',{'戌','亥'}),('甲戌',{'申','酉'}),('甲申',{'午','未'}),('甲午',{'辰','巳'}),('甲辰',{'寅','卯'}),('甲寅',{'子','丑'})]
def xunkong(day):  # day like 壬辰
    if not day or len(day)<2: return None
    s,br=day[0],day[1]
    # find xun: stem index and branch index
    si=STEMS.index(s); bi=BR.index(br)
    # xun start: stem 甲 at position where (bi - k) ...
    for name,kong in XUN:
        hs,hb=name[0],name[1]
        # day belongs if (si - STEMS.index(hs))%10 == (bi - BR.index(hb))%12 and diff<10
        d1=(si-STEMS.index(hs))%10; d2=(bi-BR.index(hb))%12
        if d1==d2: return kong
    return None
def wangshuai(el, month_el):
    if el==month_el: return '旺'
    if SHENG[month_el]==el: return '相'
    if SHENG[el]==month_el: return '休'
    if KE[el]==month_el: return '囚'
    return '死'  # month ke el
def jin_tui(a,b):
    order=BR
    if a==b: return '同支'
    jin_pairs={('寅','卯'),('巳','午'),('申','酉'),('亥','子'),('丑','辰'),('辰','未'),('未','戌'),('戌','丑')}
    if (a,b) in jin_pairs: return '化进'
    if (b,a) in jin_pairs: return '化退'
    return ''
QIN_RE=re.compile(r'(父母|妻財|妻财|官鬼|子孫|子孙|兄弟)([子丑寅卯辰巳午未申酉戌亥])([水木火土金])')
def parse_line(s):
    m=QIN_RE.search(s)
    if not m: return None
    qin,br,el=m.group(1).replace('妻财','妻財').replace('子孙','子孫'),m.group(2),m.group(3)
    moving = ('○' in s) or ('ㄨ' in s)
    yinyang = '⚊' if '⚊' in s else ('⚋' if '⚋' in s else '?')
    return dict(qin=qin,br=br,el=el,moving=moving,yy=yinyang,shi=('世' in s),ying=('應' in s or '应' in s),raw=s)
def parse_pair(s):
    # "本爻 ... 變爻 ..." two segments each containing qin+br+el; find all matches
    ms=list(QIN_RE.finditer(s))
    out=[]
    for m in ms[:2]:
        out.append(dict(qin=m.group(1).replace('妻财','妻財').replace('子孙','子孫'),br=m.group(2),el=m.group(3)))
    moving=('○' in s) or ('ㄨ' in s)
    return out, moving, ('世' in s.split('　')[0] if '　' in s else '世' in s), ('應' in s or '应' in s)
for cid in IDS:
    d=json.load(open(f'{BASE}/inputs-dev12/{cid}.json'))
    ctx=d.get('context',{}); att=ctx.get('attachments',{})
    raw_lines=att.get('chart_lines_top_to_bottom') or att.get('lines_top_to_bottom') or []
    # dual-chart cases: 12 lines -> second chart is the "moving" one for LY-204/218/227
    dual = len(raw_lines)>6
    lines_src = raw_lines[6:] if dual else raw_lines
    if dual: print(f'--- {cid} DUAL: first chart static lines:', raw_lines[:6])
    date = att.get('date_ganzhi') or ctx.get('asked_at') or ''
    mm=re.search(r'([子丑寅卯辰巳午未申酉戌亥])月', date)
    month=mm.group(1) if mm else None
    dm=re.search(r'([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日', date)
    day=dm.group(0)[:2] if dm else None
    kong=att.get('空亡')
    kongset=set(kong) if kong else xunkong(day)
    print(f'=== {cid} Q:{ctx.get("question")} 月:{month}({EL.get(month,"?")}) 日:{day} 空:{sorted(kongset) if kongset else "?"} HEX:{att.get("hexagram") or att.get("ben_gua")}->{att.get("bian_gua","")}')
    parsed=[]
    for i,s in enumerate(lines_src):
        pos=6-i  # top first
        pr, moving, shi, ying = parse_pair(s)
        if not pr: print(f'  爻{pos}: PARSE FAIL {s}'); continue
        ben=pr[0]; bian=pr[1] if len(pr)>1 else None
        info=dict(pos=pos,**ben,moving=moving,shi=shi,ying=ying,bian=bian)
        parsed.append(info)
        ws=wangshuai(ben['el'], EL[month]) if month else '?'
        tags=[]
        if kongset and ben['br'] in kongset: tags.append('旬空')
        if month and frozenset((ben['br'],month)) in CHONG: tags.append('月破')
        if day and len(day)>1 and frozenset((ben['br'],day[1])) in CHONG: tags.append('日冲')
        if day and len(day)>1 and frozenset((ben['br'],day[1])) in HE: tags.append('日合')
        if month and frozenset((ben['br'],month)) in HE: tags.append('月合')
        if ben['br']==MU[ben['el']]: pass
        btxt=''
        if bian and moving:
            jt=jin_tui(ben['br'],bian['br'])
            rel = '回头生' if SHENG[bian['el']]==ben['el'] else ('回头克' if KE[bian['el']]==ben['el'] else ('泄' if SHENG[ben['el']]==bian['el'] else ('被泄方' if False else '')))
            # careful: bian生ben=回头生; bian克ben=回头克; ben生bian=泄气; ben克bian=克出
            if SHENG[ben['el']]==bian['el']: rel='本生化(泄)'
            if KE[ben['el']]==bian['el']: rel='本克化'
            bk=[]
            if kongset and bian['br'] in kongset: bk.append('化空')
            if month and frozenset((bian['br'],month)) in CHONG: bk.append('化月破')
            if bian['br']==MU[ben['el']]: bk.append('化墓')
            if bian['br']==JUE[ben['el']]: bk.append('化绝')
            btxt=f" -> {bian['qin']}{bian['br']}{bian['el']}[{jt}{rel}{'/'.join(bk)}]"
        print(f"  爻{pos}: {ben['qin']}{ben['br']}{ben['el']} 月{ws} {'動' if moving else '靜'}{'世' if shi else ''}{'應' if ying else ''} {' '.join(tags)}{btxt}")
    if att.get('hidden_lines'): print('  伏:', att['hidden_lines'])
    if att.get('yongshen'): print('  卡載用神:', att['yongshen'])
    if att.get('chart_note'): print('  NOTE:', att['chart_note'][:80])
