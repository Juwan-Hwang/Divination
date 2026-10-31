import json, re
BASE='/home/hatch/workspace/divination/benchmark/phase3'
b=json.load(open(f'{BASE}/runs/round64/batches.json'))
ids=b['B13']+b['B14']+b['B15']
EL={'子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火','午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'}
SHENG={'木':'火','火':'土','土':'金','金':'水','水':'木'}
KE={'木':'土','土':'水','水':'火','火':'金','金':'木'}
# palace element from a line: qin relation
def palace(el,q):
    if q=='兄弟': return el
    if q=='父母': return SHENG[el]  # parent生我 -> 我 is child of el
    if q=='子孫': return [k for k,v in SHENG.items() if v==el][0]
    if q=='妻財': return [k for k,v in KE.items() if v==el][0]  # 我克财
    if q=='官鬼': return KE[el]  # 鬼克我
    return '?'
STEMS='甲乙丙丁戊己庚辛壬癸'; BR='子丑寅卯辰巳午未申酉戌亥'
def kongwang(gz):
    if not gz or len(gz)<2: return '?'
    s=STEMS.index(gz[0]); b=BR.index(gz[1]); start=(b-s)%12
    return BR[(start+10)%12]+BR[(start+11)%12]
# fix 甲寅旬
def wang(el, mel):
    if el==mel: return '旺'
    if SHENG[mel]==el: return '相'
    if SHENG[el]==mel: return '休'
    if KE[el]==mel: return '囚'
    if KE[mel]==el: return '死'
    return '?'
for cid in ids:
    d=json.load(open(f'{BASE}/inputs-dev12/{cid}.json'))
    a=d['context']['attachments']; ctx=d['context']
    date=a.get('date_ganzhi') or ctx['asked_at']
    m=re.search(r'([子丑寅卯辰巳午未申酉戌亥])月', date)
    dm=re.search(r'([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日', date)
    M=m.group(1) if m else '?'; D=dm.group(2) if dm else '?'; gz=(dm.group(1)+dm.group(2)) if dm else '?'
    kong=a.get('空亡') or kongwang(gz)
    mel=EL.get(M,'?')
    print(f"== {cid} | {ctx['question']} | {ctx.get('setting','')} | {date} 月{M}({mel}) 日{D} 空{ kong } | {a.get('hexagram')} | MV:{a.get('moving_lines')}")
    if a.get('yongshen'): print('   yongshen-field:', a['yongshen'])
    if a.get('hidden_lines'): print('   hidden:', a['hidden_lines'])
    lines=a['chart_lines_top_to_bottom']
    # split multi-hexagram cards: 12 lines = two hexagrams
    groups=[lines[i:i+6] for i in range(0,len(lines),6)]
    for gi,g in enumerate(groups):
        if len(groups)>1: print(f'   --卦{gi+1}--')
        pal=None
        parsed=[]
        for idx,row in enumerate(g):
            pos=6-idx
            parts=row.split('　')
            main=parts[0].strip(); var=parts[1].strip() if len(parts)>1 else ''
            mm=re.match(r'(父母|兄弟|子孫|妻財|官鬼)([子丑寅卯辰巳午未申酉戌亥])(.)', main)
            if not mm: parsed.append((pos,main,var)); continue
            q,br,sym=mm.groups(); el=EL[br]
            if pal is None: pal=palace(el,q)
            mark=''
            if '世' in main: mark+='世'
            if '應' in main: mark+='應'
            mov='動' if ('○' in main or 'ㄨ' in main) else ''
            vm=re.match(r'(父母|兄弟|子孫|妻財|官鬼)([子丑寅卯辰巳午未申酉戌亥])', var) if var else None
            vs=f" ->{vm.group(1)}{vm.group(2)}{EL[vm.group(2)]}" if vm else ''
            extra=[]
            if br in str(kong): extra.append('空')
            if M in {'子':'午','午':'子','丑':'未','未':'丑','寅':'申','申':'寅','卯':'酉','酉':'卯','辰':'戌','戌':'辰','巳':'亥','亥':'巳'} and br== {'子':'午','午':'子','丑':'未','未':'丑','寅':'申','申':'寅','卯':'酉','酉':'卯','辰':'戌','戌':'辰','巳':'亥','亥':'巳'}[M]: extra.append('月破')
            if D in {'子':'午','午':'子','丑':'未','未':'丑','寅':'申','申':'寅','卯':'酉','酉':'卯','辰':'戌','戌':'辰','巳':'亥','亥':'巳'} and br== {'子':'午','午':'子','丑':'未','未':'丑','寅':'申','申':'寅','卯':'酉','酉':'卯','辰':'戌','戌':'辰','巳':'亥','亥':'巳'}[D]: extra.append('日沖')
            parsed.append((pos,f"{pos}爻 {q}{br}{el} {wang(el,mel) if mel!='?' else ''} {mark}{mov}{vs} {' '.join(extra)}"))
        print(f'   宮五行={pal}')
        for p,t in parsed: print('   ',t)
