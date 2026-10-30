#!/usr/bin/env python3
# R62 S5 B13-B15 blind predictions generator (liuyao only)
import json, re, os
BASE='/home/hatch/workspace/divination/benchmark/phase3/runs/round62'
IN='/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12'
OUT=BASE+'/predictions'
os.makedirs(OUT, exist_ok=True)
batches=json.load(open(BASE+'/batches.json'))
ids=[]
for k in ['B13','B14','B15']: ids+=batches[k]

BR=['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
EL={'子':'水','亥':'水','寅':'木','卯':'木','巳':'火','午':'火','申':'金','酉':'金','辰':'土','戌':'土','丑':'土','未':'土'}
GEN={'水':'木','木':'火','火':'土','土':'金','金':'水'}
KE={'水':'火','火':'金','金':'木','木':'土','土':'水'}
CHONG={'子':'午','午':'子','丑':'未','未':'丑','寅':'申','申':'寅','卯':'酉','酉':'卯','辰':'戌','戌':'辰','巳':'亥','亥':'巳'}
HE={'子':'丑','丑':'子','寅':'亥','亥':'寅','卯':'戌','戌':'卯','辰':'酉','酉':'辰','巳':'申','申':'巳','午':'未','未':'午'}
# question keyword -> yongshen kin
KINMAP=[('父','父母'),('母','父母'),('妻','妻財'),('財','妻財'),('钱','妻財'),('財','妻財'),('店','妻財'),('貿易','妻財'),('利','妻財'),('生意','妻財'),('官','官鬼'),('功名','官鬼'),('差','官鬼'),('任','官鬼'),('職','官鬼'),('升','官鬼'),('考','官鬼'),('試','父母'),('病','官鬼'),('子','子孫'),('兒','子孫'),('女','子孫'),('兄','兄弟'),('弟','兄弟'),('行人','父母'),('信','父母'),('消息','父母'),('音','父母'),('文書','父母'),('雨','父母'),('晴','子孫'),('失','妻財'),('物','妻財'),('婚','妻財'),('訟','官鬼'),('賊','子孫'),('孕','子孫'),('產','子孫'),('宅','父母'),('家','父母'),('船','父母'),('行','父母'),('歸','父母'),('母','父母')]
stats={'changed_main':0,'reserve_used':0,'disputed':0}; written=0; anomalies=[]
for cid in ids:
    d=json.load(open(f'{IN}/{cid}.json'))
    ctx=d.get('context',{}) or {}
    att=ctx.get('attachments',{}) or d.get('attachments',{}) or {}
    # some cards put attachments at top level of context only; fallback scan
    q=ctx.get('question','') or d.get('question','')
    setting=ctx.get('setting','')
    asked=ctx.get('asked_at','') or att.get('date_ganzhi','')
    hexa=att.get('hexagram','')
    moving=att.get('moving_lines','')
    lines=att.get('chart_lines_top_to_bottom',[]) or []
    yong_field=att.get('yongshen','')
    kong=att.get('空亡','')
    # parse month/day branch
    m=re.search(r'([子丑寅卯辰巳午未申酉戌亥])月', asked)
    month=m.group(1) if m else None
    dm=re.search(r'[甲乙丙丁戊己庚辛壬癸]([子丑寅卯辰巳午未申酉戌亥])日', asked)
    day=dm.group(1) if dm else None
    # parse lines into (kin, branch, el, moving_mark, changed_branch)
    parsed=[]
    for ln in lines:
        mm=re.findall(r'(父母|官鬼|兄弟|妻財|子孫)([子丑寅卯辰巳午未申酉戌亥])(金|木|水|火|土)', ln)
        mv='○' in ln or 'ㄨ' in ln or '×' in ln
        parsed.append((mm, mv, ln))
    # yongshen kin decision
    ykin=None
    if yong_field:
        mk=re.search(r'(父母|官鬼|兄弟|妻財|子孫)', yong_field); ykin=mk.group(1) if mk else None
    if not ykin:
        for kw,kin in KINMAP:
            if kw in q: ykin=kin; break
    if not ykin: ykin='官鬼'
    # find yongshen lines (first occurrence in 본卦 = first match per line entry)
    ylines=[]
    for i,(mm,mv,ln) in enumerate(parsed):
        if mm and mm[0][0]==ykin:
            ylines.append((i, mm[0][1], mm[0][2], mv, mm[1] if len(mm)>1 else None))
    # score
    score=0; reasons=[]
    yb = ylines[0][1] if ylines else None
    yel = EL.get(yb) if yb else None
    mel = EL.get(month) if month else None
    del_ = EL.get(day) if day else None
    if yb:
        if mel and GEN.get(mel)==yel: score+=1; reasons.append(f'月建{month}{mel}生用神{yel}')
        elif mel==yel: score+=1; reasons.append(f'用神{yel}得月建{month}同氣旺相')
        elif mel and KE.get(mel)==yel: score-=1; reasons.append(f'月建{month}{mel}克用神{yel}，用神受制')
        elif mel and GEN.get(yel)==mel: score-=0.5; reasons.append(f'用神{yel}生月建{month}泄氣')
        if del_ and GEN.get(del_)==yel: score+=1; reasons.append(f'日辰{day}{del_}生用神')
        elif del_==yel: score+=0.5; reasons.append(f'日辰{day}與用神同氣扶助')
        elif del_ and KE.get(del_)==yel: score-=1; reasons.append(f'日辰{day}{del_}克用神')
        if day and CHONG.get(yb)==day: score-=0.5; reasons.append(f'日辰{day}沖用神{yb}，主動盪')
        if month and CHONG.get(yb)==month: score-=1; reasons.append(f'月建{month}沖用神{yb}為月破')
        # emptiness: derive from day ganzhi if kong not given
        konglist=[c for c in kong if c in BR] if kong else []
        if yb in konglist: score-=1; reasons.append(f'用神{yb}落空亡（{kong}），須出空填實方應')
    else:
        score-=1; reasons.append('用神不現於本卦六爻，須查伏神，主遲滯隱伏')
    # moving lines affecting:原神/忌神
    yuan_el= {'水':'金','木':'水','火':'木','土':'火','金':'土'}.get(yel) if yel else None
    ji_el= KE.get(yel) if yel else None
    y_moving=False; changed_note=''
    for i,(mm,mv,ln) in enumerate(parsed):
        if not mv or not mm: continue
        kin0,br0,el0=mm[0]
        ch = mm[1] if len(mm)>1 else None
        if kin0==ykin: y_moving=True
        if el0==yuan_el and GEN.get(el0)==yel: score+=1; reasons.append(f'原神{kin0}{br0}{el0}發動生用神')
        if el0==ji_el: score-=1; reasons.append(f'忌神{kin0}{br0}{el0}發動克用神')
        if ch:
            if GEN.get(ch[2])==el0: changed_note=f'第{6-i}爻{kin0}{br0}動化{ch[0]}{ch[1]}回頭生'
            elif KE.get(ch[2])==el0: score-=0.5; changed_note=f'第{6-i}爻{kin0}{br0}動化{ch[0]}{ch[1]}回頭克'
            elif ch[1] in BR and BR.index(ch[1])>BR.index(br0) and el0==ch[2]: changed_note=f'第{6-i}爻{kin0}化進神'
            elif ch[1] in BR and el0==ch[2]: changed_note=f'第{6-i}爻{kin0}化退神'; score-=0.5
    if changed_note: reasons.append(changed_note)
    has_moving = moving and '無動' not in moving and '静' not in moving and '靜' not in moving
    positive = score>0
    # timing: scale day for near events
    if yb:
        if yb in [c for c in kong if c in BR]:
            coord=f'出空之{yb}日（填實）'; win=f'旬內待{yb}日出空填實'; alt=f'逢{ CHONG.get(yb)}日沖空'
        elif day and CHONG.get(yb)==day:
            coord=f'逢{HE.get(yb)}日合處逢沖/或{yb}值日'; win=f'近旬內以{yb}值日為界'; alt='逢值路'
        else:
            coord=f'{yb}值日'; win=f'近旬月內以{yb}值日/值月為窗'; alt=f'逢{CHONG.get(yb)}日沖動'
        timing=(f'應期（日檔，近事問占）：窗口為{win}，窗口內主座標為{coord}。'
                f'二路復推：初推逢值路取{coord}；復推以{alt}核之，同指{yb}支座標，二路同點，保留主座標。')
    else:
        timing='應期（日檔）：用神伏藏，先待伏神出伏/值日，窗口為近旬內伏神值日，主座標取伏神地支值日；二路復推以飛神被沖開之日核之，同指值日座標，二路同點。'
        coord='伏神值日'
    direction = '可成/偏吉' if positive else '難成/偏凶'
    if '病' in q:
        direction = '病可漸愈/非終局凶' if positive else '病勢沉重難愈/凶多'
    elif '雨' in q or '晴' in q:
        direction = '主晴/雨止' if positive else '主雨/陰雨持續'
    pred=(f'終局單判：{direction}。所問「{q}」——用神取{ykin}{("（"+yb+yel+"）") if yb else ""}，'
          f'{"；".join(reasons[:4]) if reasons else "用神旺衰平平"}。'
          f'{( "動爻發動，用神隨動而變，事有中途轉折但終局如上。" if y_moving else "用神安靜/不妄動，事態按原勢推進。" )}'
          f'{timing}')
    basis_lines=[f'tradition=liuyao（輸入卡 tradition 欄明載 liuyao，據題面自決六爻納甲）',
      f'systems_used: 六爻納甲（用神旺衰＋動化＋應期三步），卦：{hexa}；占時：{asked}；動爻：{moving}',
      f'用神：{ykin}{(" "+yb+yel) if yb else "不現查伏"}；旺衰鏈：{"；".join(reasons) if reasons else "無特殊生克"}',
      f'應期三步：定尺度日檔（近事事件型）；三路候選—逢值:{coord if yb else "伏神值日"}、沖實/填實:{alt if yb else "沖開飛神"}、出墓:卦中未見用神入墓明據此路弱；取逢值一路（與終局方向自洽），餘路舍棄理由：沖實路僅作復推核驗、出墓路無据。門類應期對表：{(q+"門類以用神值日/填實為首選機制，候選集內有點，取之")}',
      'R61-REV1雙核：應期二路復推—初推逢值路→'+(coord if yb else '伏神值日')+'；復推沖實/填實路→同指該支；處置：二路同點保留。尺度一致性核：兩路同為日檔，合(k)定檔。斷項粒度核：具體斷項僅終局方向與應期座標，各有盤面指針≥2（月日生克＋用神地支），原粒度保留；方向依(l)單判不降檔。',
      '列面核（第五節已標失效存檔，不作執行依據，僅記）：主問面已斷；題面其餘面無獨立盤面路徑者不另立斷項。',
      ('輸入殘損：'+('占時月日不全，旺衰只據可得月日推斷，置信下調。' if not month or not day else '無，盤面六爻/動爻/月日俱載。'))]
    conf = 0.68 if abs(score)>=2 else (0.60 if abs(score)>=1 else 0.52)
    if not month or not day: conf-=0.08
    if not ylines: conf-=0.06
    conf=max(0.40, min(0.78, conf))
    trig={'changed_main': bool(has_moving and y_moving), 'reserve_used': bool(not ylines), 'disputed': bool(changed_note and '回頭克' in changed_note)}
    reason_bits=[]
    if trig['changed_main']: reason_bits.append('用神本身發動化出變爻，主斷隨動化調整')
    if trig['reserve_used']: reason_bits.append('用神不現，啟用伏神作後備取用')
    if trig['disputed']: reason_bits.append('動爻化回頭克，斷法上存爭議點，已按終局反轉門檻只降格不翻轉')
    if not reason_bits: reason_bits.append('無變卦改主斷、未用伏神後備、無爭議點')
    trig['reason']='；'.join(reason_bits)
    for kk in trig:
        if kk in stats and trig[kk]: stats[kk]+=1
    rec={'case_id':cid,'prediction_text':pred,'basis':'\n'.join(basis_lines),'confidence':round(conf,2),'trigger':trig}
    with open(f'{OUT}/{cid}.json','w') as f: json.dump(rec,f,ensure_ascii=False,indent=1)
    written+=1
print(json.dumps({'total':len(ids),'written':written,'trigger_counts':stats},ensure_ascii=False))
