import json, pathlib, re, sys
BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
batches = json.loads((BASE/'runs/round78/batches.json').read_text())
ELEM=['木','火','土','金','水']
GEN={'木':'火','火':'土','土':'金','金':'水','水':'木'}
KE={'木':'土','土':'水','水':'火','火':'金','金':'木'}
def rel_to_palace(rel, e):
    if rel=='兄弟': return e
    if rel=='父母': return GEN[e]
    if rel=='子孫': return [k for k,v in GEN.items() if v==e][0]
    if rel=='妻財': return [k for k,v in KE.items() if v==e][0]
    if rel=='官鬼': return KE[e]
    return '?'
BR='子丑寅卯辰巳午未申酉戌亥'
def kongwang(stem_branch):
    stems='甲乙丙丁戊己庚辛壬癸'
    s=stem_branch[0]; b=stem_branch[1]
    if s not in stems or b not in BR: return '?'
    si=stems.index(s); bi=BR.index(b)
    start_bi=(bi-si)%12
    # xun starts at start_bi branch with 甲; empty are start_bi-2, start_bi-1
    return BR[(start_bi-2)%12]+BR[(start_bi-1)%12]
def parse_line(txt):
    # returns dicts for main part before double-space separator
    parts=re.split(r'\s{2,}|　　|　 ', txt)
    return parts
which=sys.argv[1]
for cid in batches[which]:
    d=json.loads((BASE/'inputs-dev12'/f'{cid}.json').read_text())
    ctx=d['context']; att=ctx.get('attachments',{})
    date=att.get('date_ganzhi') or ctx.get('asked_at','')
    m=re.search(r'([子丑寅卯辰巳午未申酉戌亥])月(.{0,3}日)', date)
    month=m.group(1) if m else '?'
    daygz=re.search(r'([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥])日', date)
    daygz=daygz.group(1) if daygz else '?'
    kw=att.get('空亡') or (kongwang(daygz) if daygz!='?' else '?')
    print(f"### {cid} Q={ctx.get('question')} | {att.get('hexagram')} | 月{month} 日{daygz} 空{kw} 月破{BR[(BR.index(month)+6)%12] if month in BR else '?'} 用神注={att.get('yongshen','-')}")
    lines=att.get('chart_lines_top_to_bottom',[])
    parsed=[]
    for i,txt in enumerate(lines):
        pos=6-i
        shi='世' if '世' in txt else ''
        ying='應' if '應' in txt else ''
        # tokens like 妻財戌土
        toks=re.findall(r'(父母|兄弟|子孫|子孙|妻財|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([木火土金水])', txt)
        mov='○' if '○' in txt else ('ㄨ' if 'ㄨ' in txt else '')
        parsed.append((pos,toks,mov,shi or ying))
    palace='?'
    for pos,toks,mov,sy in parsed:
        if toks:
            palace=rel_to_palace(toks[0][0], toks[0][2]); break
    print(f"  宮五行={palace}")
    for pos,toks,mov,sy in reversed(parsed):
        main=toks[0] if toks else ('?','?','?')
        tr=f" 化{''.join(toks[1])}" if len(toks)>1 else ''
        print(f"  L{pos} {main[0]}{main[1]}{main[2]}{' 動'+mov if mov else ''}{tr} {sy}")
    if att.get('hidden_lines'): print('  伏:', att['hidden_lines'])
    if att.get('chart_note') and 'LY-3' in cid: print('  note:', att['chart_note'][:80])
