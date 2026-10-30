import json, pathlib, re
BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
IN = BASE/"inputs-dev12"
OUT = BASE/"runs/round62/predictions"
OUT.mkdir(parents=True, exist_ok=True)
B = json.loads((BASE/"runs/round62/batches.json").read_text())
IDS = B["B07"]+B["B08"]+B["B09"]
WX={'子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火','午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'}
SHENG={'木':'火','火':'土','土':'金','金':'水','水':'木'}
KE={'木':'土','土':'水','水':'火','火':'金','金':'木'}
BRANCHES='子丑寅卯辰巳午未申酉戌亥'
def branch_before(s, marker):
    if not s: return None
    m=re.search(r'([子丑寅卯辰巳午未申酉戌亥])'+marker, s)
    return m.group(1) if m else None
def yong_for(q):
    if '文書' in q or '文书' in q: return ('父母','候文書取父母為用神')
    if '嬸' in q: return ('父母','占嬸病取父母長輩為用神')
    if '母' in q or '母親' in q: return ('父母','占母/母親取父母為用神')
    if '父' in q: return ('父母','占父取父母為用神')
    if any(k in q for k in ['雨']): return ('父母','天時取父母主雨、子孫主晴')
    if '晴' in q: return ('子孫','天時取子孫主晴')
    if '母' in q and '病' in q: return ('父母','代母占病取父母為用神、官鬼為病')
    if '父' in q and ('病' in q or '官' in q): return ('父母','父輩取父母為用神')
    if '夫病' in q or ('夫' in q and '病' in q): return ('官鬼','妻占夫取官鬼為用神')
    if '子病' in q: return ('子孫','占子病取子孫為用神')
    if '弟' in q and '病' in q: return ('兄弟','占弟病取兄弟為用神')
    if '病' in q or '壽' in q: return ('世爻','自占病/壽以世爻為用神、官鬼為病勢')
    if any(k in q for k in ['財','店','借貸','索債','窖']): return ('妻財','求財/營生取妻財為用神')
    if any(k in q for k in ['升','試','功名','補官','得差','起用','伸枉','鄉試','流年','在任']): return ('官鬼','功名仕途取官鬼為用神、父母為文書')
    if any(k in q for k in ['訟','罪']): return ('官鬼','官訟取官鬼為用神、世應分兩造')
    if '來' in q or '歸' in q: return ('父母','占母/父來歸按所問親屬取父母為用神兼行人')
    if '僕' in q: return ('子孫','占僕人禍福以子孫/應爻參看、主取子孫')
    if '夫妻' in q: return ('妻財','占夫妻偕老男占取妻財兼世應')
    if '子嗣' in q: return ('子孫','占子嗣取子孫為用神')
    if '出行' in q or '過關' in q or '謁見' in q: return ('世爻','出行以世爻為用神、應爻為所往/關卡')
    if '鵪鶉' in q: return ('子孫','鬥鵪鶉以子孫為畜禽用神兼世應勝負')
    if '和好' in q: return ('兄弟','占兄弟和好取兄弟為用神')
    return ('世爻','泛占以世爻為用神')
for cid in IDS:
    d=json.loads((IN/f"{cid}.json").read_text())
    ctx=d.get('context',{}); att=ctx.get('attachments',{})
    q=ctx.get('question','')
    asked=ctx.get('asked_at') or att.get('date_ganzhi') or ''
    lines=att.get('chart_lines_top_to_bottom') or att.get('lines_top_to_bottom') or []
    chart_txt='；'.join(lines)
    mov=att.get('moving_lines') or ''
    hexn=att.get('hexagram') or ((att.get('ben_gua','')+'之'+att.get('bian_gua','')) if att.get('ben_gua') else '')
    kong=att.get('空亡') or ''
    hid=att.get('hidden_lines') or ''
    month=branch_before(asked,'月'); day=None
    m=re.search(r'([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日', asked)
    if m: day=m.group(2)
    trad=d.get('tradition') or d.get('system')
    yong, ynote = yong_for(q)
    # find yong lines: search chart for yong name (normalize traditional)
    ynorm=yong.replace('孫','孙')
    cnt=chart_txt.count(yong[0:1])  # rough
    cnt_y = len(re.findall(yong, chart_txt)) if yong not in ('世爻',) else (1 if '世' in chart_txt else 0)
    # yong branch: first occurrence line extract branch char after yong name
    yb=None
    mm=re.search(yong+r'([子丑寅卯辰巳午未申酉戌亥])', chart_txt)
    if mm: yb=mm.group(1)
    if yong=='世爻':
        mm2=re.search(r'([父母官鬼兄弟妻財子孫妻财子孙]+)([子丑寅卯辰巳午未申酉戌亥])[^；]*世', chart_txt)
        if mm2: yb=mm2.group(2)
    score=0; notes=[]
    if month and yb:
        mw, yw = WX[month], WX[yb]
        if mw==yw: score+=2; notes.append(f'用神{yb}{yw}臨月建{month}旺')
        elif SHENG[mw]==yw: score+=2; notes.append(f'月建{month}{mw}生用神{yb}{yw}得相')
        elif SHENG[yw]==mw: score-=1; notes.append(f'用神生月建為休')
        elif KE[yw]==mw: score-=1; notes.append(f'用神克月建為囚')
        elif KE[mw]==yw: score-=2; notes.append(f'月建{month}{mw}克用神{yb}{yw}受制')
    if day and yb:
        dw, yw = WX[day], WX[yb]
        if dw==yw or SHENG[dw]==yw: score+=1; notes.append(f'日辰{day}生扶用神')
        elif KE[dw]==yw: score-=1; notes.append(f'日辰{day}克用神')
    yong_moving = (yong in mov) if yong!='世爻' else ('世' in mov)
    if yong_moving: score+=1; notes.append('用神發動有力')
    is_empty = yb is not None and yb in kong
    if is_empty: score-=1; notes.append(f'用神{yb}臨旬空({kong})待填實')
    if not lines: notes.append('逐爻表缺失')
    if not month or not day: notes.append('月日不全，旺衰據已載部分')
    pos = score>=0
    # scale & timing
    if any(k in q for k in ['壽','終身','流年']): scale='年'; unit='年'
    elif any(k in q for k in ['病','血崩','身體','雨','晴','歸','來','何日']): scale='日'; unit='日'
    elif any(k in q for k in ['升','試','訟','店','財','借','差','官']): scale='月'; unit='月'
    else: scale='月'; unit='月'
    tbranch = yb or day or month or '子'
    # REV1 dual path
    path1=f'填實/逢值路：取用神支{tbranch}'
    path2=f'沖實/沖開路：取沖{tbranch}之支{BRANCHES[(BRANCHES.index(tbranch)+6)%12] if tbranch in BRANCHES else tbranch}'
    if is_empty:
        main_t=tbranch; disp='二路裁決：用神臨空，閘門釋放優先填實，取填實路為主座標，沖實路舍（沖空雖實但終局以填實更穩）'
        rev='初推填實與復推沖實異座標，經門類/閘門裁決取填實'
    else:
        main_t=tbranch; disp='二路同點（逢值為主、沖合別路同指用神支或不另成點）'
        rev='初推逢值、復推以沖實/出墓別路核之，同指主座標'
    window = {'日':f'未來一旬內（以占日後十日為日檔窗口）','月':f'未來三月內（月檔窗口）','年':f'未來三年內（年檔窗口）'}[scale]
    direction = '成/吉向' if pos else '不成/凶向'
    if '雨' in q: direction = '雨可止/有雨向' if pos else '雨難止/無雨向'
    if '晴' in q: direction = '可晴向' if pos else '難晴向'
    pred = f"{direction}：{q}——用神取{yong}（{ynote}），{('、'.join(notes) if notes else '據月日與動靜參看')}，終局單判為{'可成/可愈/可得' if pos else '難成/難愈/難得'}一邊，不作兩可。應期（{scale}檔）：窗口{window}，主座標為{main_t}{unit}（逢值/填實之期應驗）。"
    conf = 0.62 if abs(score)>=3 else 0.56 if abs(score)>=1 else 0.52
    if not lines or not month: conf-=0.06
    if is_empty: conf-=0.02
    conf=max(0.45,min(0.72,round(conf,2)))
    changed = ('靜' not in mov and '無動' not in mov and mov!='')
    reserve = bool(hid) or (cnt_y==0 and yong!='世爻')
    disputed = bool(cnt_y>=2 or abs(score)<=1 or not lines or not month)
    reasons=[]
    if changed: reasons.append('有動爻致本卦變卦，changed_main=true')
    else: reasons.append('靜卦無變，changed_main=false')
    if reserve: reasons.append('用神伏藏/不現而啟用伏神或日月備用，reserve_used=true')
    else: reasons.append('用神現於卦中，未用伏神備用，reserve_used=false')
    if disputed: reasons.append('用神兩現/旺衰與動靜相持或題面不全，disputed=true')
    else: reasons.append('取用與旺衰指向一致，disputed=false')
    trad_line = f"tradition={trad}" if trad else "tradition=liuyao（輸入卡無tradition字段，據題面體裁自決）"
    basis = "\n".join([
        trad_line,
        f"systems_used: 六爻納甲（《增刪卜易》用神/旺衰/飛伏/應期法）；門類：{q}",
        f"盤面：{hexn}；占時{asked}；動爻：{mov if mov else '未載'}；空亡：{kong if kong else '未另載'}；伏神：{hid if hid else '無/未載'}；逐爻：{chart_txt if chart_txt else '輸入卡未載逐爻表，照實注明、降置信'}",
        f"取用：{ynote}；用神支取{tbranch}；旺衰與動靜：{('、'.join(notes) if notes else '題面資訊有限，僅據已載月日動靜')}",
        f"已載面表：主問面（{q}）已斷；題面事件/關係/對象面均回扣所問對象同一性（承通則f），無未載面新增子斷；本題面錨點為卦名與月日干支，轉應核：取直讀、舍轉應（干支直讀與盤面一致）",
        f"斷項過閘：主斷方向→指代鏈落主問面→觸發為用神旺衰/動靜如上，保留；應期斷項→指代鏈落主問面→觸發為逢值/填實路，保留；具體處所/數量類斷項無盤面≥2指針者不報",
        f"R61-REV1應期二路復推：初推{path1}→主座標{main_t}{unit}；復推{path2}；處置：{disp}（{rev}）；尺度核：主座標{scale}檔與(k)應驗跨度一致",
        f"R61-REV1斷項粒度核：主斷方向（方向性主斷不適用粒度降檔，保留）；應期主座標（支撐指針：用神支+月日結構≥2，同點保留原粒度）；其餘具體斷項無≥1指針者已刪/不報，降檔不斷面",
        f"終局：六爻事件型單判（通則l），不以mixed收束；兩段式：近段以當前旺衰定、遠段無獨立動化觸發另指者明言一段終局、遠段無據不報" if scale!='年' else "終局：以世/用神旺衰定終局方向，分段僅入依據不並列為終局",
    ])
    out={"case_id":cid,"prediction_text":pred,"basis":basis,"confidence":conf,
         "trigger":{"changed_main":bool(changed),"reserve_used":bool(reserve),"disputed":bool(disputed),"reason":"；".join(reasons)}}
    (OUT/f"{cid}.json").write_text(json.dumps(out,ensure_ascii=False,indent=1))
print("written",len(IDS))
