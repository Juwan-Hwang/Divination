import json, re
BASE='/home/hatch/workspace/divination/benchmark/phase3'
b=json.load(open(f'{BASE}/runs/round63/batches.json'))
ids=b['B16']+b['B17']+b['B18']
BR='子丑寅卯辰巳午未申酉戌亥'
EL={'子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火','午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'}
GEN={'木':'火','火':'土','土':'金','金':'水','水':'木'}  # X生GEN[X]
KE={'木':'土','土':'水','水':'火','火':'金','金':'木'}   # X克KE[X]
def wang(el,mel):
    if el==mel: return '旺'
    if GEN[mel]==el: return '相'
    if GEN[el]==mel: return '休'
    if KE[el]==mel: return '囚'
    return '死'
def rel(a,b): # a对b
    if a==b: return '同'
    if GEN[a]==b: return '生b'
    if GEN[b]==a: return '被b生'
    if KE[a]==b: return '克b'
    if KE[b]==a: return '被b克'
    return '?'
pat=re.compile(r'(父母|兄弟|子孫|子孙|官鬼|妻財|妻财)(['+BR+r'])([木火土金水])')
def parse_line(s):
    ms=pat.findall(s)
    out=[]
    for q,br,el in ms:
        q=q.replace('子孙','子孫').replace('妻财','妻財')
        out.append((q,br,el))
    shi='世' in s; ying='應' in s or '应' in s
    return out,shi,ying
for cid in ids:
    if not cid.startswith('LY'): continue
    d=json.load(open(f'{BASE}/inputs-dev12/{cid}.json'))
    ctx=d['context']; att=ctx.get('attachments') or {}
    hx=ctx.get('hexagram')
    if isinstance(hx,dict):
        lines=hx.get('chart_lines'); dg=hx.get('date_ganzhi'); kw=hx.get('kongwang'); mov=hx.get('moving_lines'); hid=hx.get('hidden_lines'); palace=hx.get('palace')
        name=hx.get('original_name')+'>'+str(hx.get('changed_name'))
    else:
        lines=att.get('chart_lines_top_to_bottom'); dg=att.get('date_ganzhi'); kw=att.get('空亡'); mov=att.get('moving_lines'); hid=att.get('hidden_lines'); palace=''; name=str(hx)
    mm=re.search(r'(['+BR+r'])月(.)(['+BR+r'])日', dg or '')
    mb,db = (mm.group(1), mm.group(3)) if mm else ('?','?')
    mel,del_ = EL.get(mb,'?'), EL.get(db,'?')
    kwset=set(kw) if kw else set()
    print(f"\n== {cid} {ctx.get('question')} | {name} 宮{palace} 月{mb}({mel}) 日{db}({del_}) 空{kw} 動:{mov} 伏:{hid}")
    if not lines: print('  NO LINES'); continue
    for i,s in enumerate(lines):
        pos=6-i
        segs,shi,ying=parse_line(s)
        if not segs: print(f'  {pos}爻 PARSE_FAIL {s}'); continue
        q,br,el=segs[0]
        chg = segs[1] if len(segs)>1 else None
        tags=[]
        if shi: tags.append('世')
        if ying: tags.append('應')
        if br in kwset: tags.append('空')
        # 月破: 月支冲
        if BR.index(br)==(BR.index(mb)+6)%12: tags.append('月破')
        if BR.index(br)==(BR.index(db)+6)%12: tags.append('日沖')
        w=wang(el,mel)
        drel=rel(del_,el)
        info=f'  {pos}爻 {q}{br}{el} 旺衰{w} 日{drel}'
        if chg: info+=f' -> {chg[0]}{chg[1]}{chg[2]}(化神對本: {rel(chg[2],el)}, 支序{BR.index(chg[1])-BR.index(br)})'
        print(info+' '+' '.join(tags))
