import json, re
base='/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12'
b=json.load(open('/home/hatch/workspace/divination/benchmark/phase3/runs/round63/batches.json'))
ids=[]
for k in ['B13','B14','B15']: ids+=b[k]
EL='木火土金水'
GEN={'木':'火','火':'土','土':'金','金':'水','水':'木'}  # X生GEN[X]
KE={'木':'土','土':'水','水':'火','火':'金','金':'木'}   # X克KE[X]
BR_EL={'子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火','午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'}
QINS=['父母','兄弟','子孫','妻財','官鬼']
def palace_el(qin, el):
    # find E
    for E in EL:
        m={'父母': [x for x in EL if GEN[x]==E][0], '兄弟':E, '子孫':GEN[E], '妻財':KE[E], '官鬼':[x for x in EL if KE[x]==E][0]}
        if m[qin]==el: return E
    return '?'
def qin_of(E, el):
    if el==E: return '兄弟'
    if GEN[el]==E: return '父母'
    if GEN[E]==el: return '子孫'
    if KE[E]==el: return '妻財'
    return '官鬼'
XUN={'甲子':'戌亥','乙丑':'戌亥','丙寅':'戌亥','丁卯':'戌亥','戊辰':'戌亥','己巳':'戌亥','庚午':'戌亥','辛未':'戌亥','壬申':'戌亥','癸酉':'戌亥',
'甲戌':'申酉','乙亥':'申酉','丙子':'申酉','丁丑':'申酉','戊寅':'申酉','己卯':'申酉','庚辰':'申酉','辛巳':'申酉','壬午':'申酉','癸未':'申酉',
'甲申':'午未','乙酉':'午未','丙戌':'午未','丁亥':'午未','戊子':'午未','己丑':'午未','庚寅':'午未','辛卯':'午未','壬辰':'午未','癸巳':'午未',
'甲午':'辰巳','乙未':'辰巳','丙申':'辰巳','丁酉':'辰巳','戊戌':'辰巳','己亥':'辰巳','庚子':'辰巳','辛丑':'辰巳','壬寅':'辰巳','癸卯':'辰巳',
'甲辰':'寅卯','乙巳':'寅卯','丙午':'寅卯','丁未':'寅卯','戊申':'寅卯','己酉':'寅卯','庚戌':'寅卯','辛亥':'寅卯','壬子':'寅卯','癸丑':'寅卯',
'甲寅':'子丑','乙卯':'子丑','丙辰':'子丑','丁巳':'子丑','戊午':'子丑','己未':'子丑','庚申':'子丑','辛酉':'子丑','壬戌':'子丑','癸亥':'子丑'}
CHONG={'子':'午','午':'子','丑':'未','未':'丑','寅':'申','申':'寅','卯':'酉','酉':'卯','辰':'戌','戌':'辰','巳':'亥','亥':'巳'}
def wang(el, mel):
    if el==mel: return '旺'
    if GEN[mel]==el: return '相'
    if GEN[el]==mel: return '休'
    if KE[el]==mel: return '囚'
    return '死'
out=[]
for cid in ids:
    d=json.load(open(f'{base}/{cid}.json'))
    ctx=d['context']; att=ctx.get('attachments',{}) or {}
    at=ctx.get('asked_at','') or ''
    dg=att.get('date_ganzhi','')
    src=dg if dg else at
    m=re.search(r'([子丑寅卯辰巳午未申酉戌亥])月', src)
    month=m.group(1) if m else None
    dm=re.search(r'([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日', src)
    daygz=dm.group(0)[:2] if dm else None
    daybr=dm.group(2) if dm else None
    kong=att.get('空亡') or (XUN.get(daygz) if daygz else None)
    lines=att.get('chart_lines_top_to_bottom',[])
    parsed=[]
    E=None
    for i,raw in enumerate(lines[:6]):
        seg=re.split(r'\s{2,}|　　', raw)[0]
        mm=re.match(r'(父母|兄弟|子孫|妻財|官鬼)([子丑寅卯辰巳午未申酉戌亥])(木|火|土|金|水)(.*)', seg)
        if not mm: parsed.append(f'L{6-i}:?{seg}'); continue
        qin,br,el,rest=mm.groups()
        if E is None: E=palace_el(qin,el)
        mov='○' in rest or 'ㄨ' in rest or '×' in rest
        shi='世' in rest; ying='應' in rest
        # changed part
        ch=''
        parts=re.split(r'\s{2,}|　　', raw)
        if len(parts)>1:
            cm=re.match(r'(父母|兄弟|子孫|妻財|官鬼)([子丑寅卯辰巳午未申酉戌亥])(木|火|土|金|水)', parts[1].strip())
            if cm: ch=f"->{cm.group(1)}{cm.group(2)}{cm.group(3)}"
        mel=BR_EL[month] if month else None
        w=wang(el,mel) if mel else '?'
        flags=[]
        if kong and br in kong: flags.append('空')
        if month and CHONG[month]==br: flags.append('月破')
        if daybr and CHONG[daybr]==br: flags.append('日沖')
        if daybr and daybr==br: flags.append('臨日')
        if month and month==br: flags.append('臨月')
        parsed.append(f"L{6-i}:{qin}{br}{el}{'世' if shi else ''}{'應' if ying else ''}{'動' if mov else ''}{ch} 旺衰{w} {'/'.join(flags)}")
    out.append(f"==={cid} q={ctx.get('question')} 月={month} 日={daygz} 空={kong} 宮五行={E}\n" + '\n'.join(parsed) + f"\n moving={att.get('moving_lines')} hex={att.get('hexagram')}")
open('/home/hatch/workspace/divination/benchmark/phase3/runs/round63/analysis_r63_s5.txt','w').write('\n'.join(out))
print('ok')
