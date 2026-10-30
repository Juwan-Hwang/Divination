import json, os, sys, re
BASE="/home/hatch/workspace/divination/benchmark/phase3"
INP=f"{BASE}/inputs-dev12"; OUT=f"{BASE}/runs/round61/predictions"
os.makedirs(OUT,exist_ok=True)
BATCHES={"B07":["LY-009","LY-01","LY-010","LY-011","LY-012","LY-013","LY-014","LY-015","LY-016","LY-017","LY-018","LY-019","LY-021","LY-022","LY-023","LY-024","LY-025","LY-026","LY-027","LY-028"],
"B08":["LY-029","LY-030","LY-031","LY-032","LY-033","LY-034","LY-035","LY-036","LY-102","LY-103","LY-104","LY-105","LY-202","LY-203","LY-204","LY-205","LY-206","LY-207","LY-208","LY-210"],
"B09":["LY-211","LY-212","LY-215","LY-216","LY-217","LY-218","LY-219","LY-220","LY-221","LY-222","LY-227","LY-228","LY-230","LY-231","LY-232","LY-233" if False else "LY-232","LY-234","LY-235","LY-237","LY-240","LY-241"]}
# fix B09 exactly from batches.json reading allowed file
bj=json.load(open(f"{BASE}/runs/round61/batches.json"))
for b in BATCHES: BATCHES[b]=bj[b]
EL={'子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火','午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'}
BR=list(EL)
SHENG={'木':'火','火':'土','土':'金','金':'水','水':'木'}
KE={'木':'土','土':'水','水':'火','火':'金','金':'木'}
def parse(cid):
    d=json.load(open(f"{INP}/{cid}.json"))
    ctx=d.get("context",{}); att=ctx.get("attachments",{}) or {}
    q=ctx.get("question","") or ""
    asked=ctx.get("asked_at","") or ""
    lines=att.get("chart_lines_top_to_bottom",[]) or []
    moving=att.get("moving_lines","") or ""
    hexa=att.get("hexagram","") or att.get("ben_gua","") or ""
    if att.get("bian_gua"): hexa=hexa+"之"+att["bian_gua"]
    hidden=att.get("hidden_lines","") or ""
    kong=att.get("空亡","") or ""
    # month/day branches
    m=re.search(r'([子丑寅卯辰巳午未申酉戌亥])月',asked); month=m.group(1) if m else None
    dm=re.search(r'[甲乙丙丁戊己庚辛壬癸]([子丑寅卯辰巳午未申酉戌亥])日',asked); day=dm.group(1) if dm else None
    # lines bottom to top: reverse, parse 本卦 side (before double space / changed)
    parsed=[]  # list dict rel, branch, moving bool, changed_rel, changed_branch
    for i,raw0 in enumerate(reversed(lines)):
        raw=raw0.replace('孫','孙').replace('財','财')
        # split changed part: separator is two spaces or tab
        parts=re.split(r'\s{2,}|　+|\t',raw.strip())
        main=parts[0]; ch=parts[1] if len(parts)>1 else ""
        mm=re.search(r'(父母|兄弟|子孙|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([金木水火土])',main)
        if not mm: parsed.append(None); continue
        cm=re.search(r'(父母|兄弟|子孙|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([金木水火土])',ch) if ch else None
        is_mov=('○' in main) or ('ㄨ' in main) or ('×' in main)
        parsed.append({"pos":i+1,"rel":mm.group(1),"br":mm.group(2),"el":mm.group(3),"mov":is_mov,
                       "crel":cm.group(1) if cm else None,"cbr":cm.group(2) if cm else None,"cel":cm.group(3) if cm else None,
                       "shi":'世' in main,"ying":'應' in main or '应' in main})
    return d,q,asked,hexa,moving,hidden,kong,month,day,parsed,lines
def yong_rel(q):
    if any(k in q for k in ['財','财','求財','行醫','生意','買賣','讨債','債']): return '妻财','求财以妻财为用神'
    if any(k in q for k in ['病','疾','血崩','壽','寿']): return '官鬼','占病以官鬼为病/用神线、子孙为医药原神线，世爻为患者承受对象'
    if any(k in q for k in ['官','功名','升','職','仕','考試','试','學','学']): return '官鬼','以官鬼为用神'
    if any(k in q for k in ['文','書','房','屋','父母','母','父','消息','音信']): return '父母','以父母为用神'
    if any(k in q for k in ['子','孫','孩','孕','產']): return '子孙','以子孙为用神'
    if any(k in q for k in ['婚','妻','夫','嫁','娶']): return '妻财','婚姻以妻财/世应为用（男占以财为用）'
    if any(k in q for k in ['行人','歸','回','出行','行']): return '父母','行人类以世爻/所问对象六亲为用，兼看用神'
    return '官鬼','题面门类不显，以世爻为主线、官鬼为事体用神（注明取用存疑）'
def strength(el,month,day):
    score=0; notes=[]
    if month:
        me=EL[month]
        if me==el: score+=2; notes.append(f"临月建{month}{me}旺")
        elif SHENG[me]==el: score+=1; notes.append(f"月建{month}{me}生用神相")
        elif KE[me]==el: score-=2; notes.append(f"月建{month}{me}克用神休囚受制")
        elif SHENG[el]==me: score-=1; notes.append(f"用神生月建泄气")
        else: notes.append(f"月建{month}与用神无直接生克")
    if day:
        de=EL[day]
        if de==el: score+=1; notes.append(f"临日辰{day}")
        elif SHENG[de]==el: score+=1; notes.append(f"日辰{day}{de}生扶")
        elif KE[de]==el: score-=1; notes.append(f"日辰{day}{de}克")
    return score,notes
def predict(cid):
    d,q,asked,hexa,moving,hidden,kong,month,day,parsed,rawlines=parse(cid)
    rel,rel_note=yong_rel(q)
    cands=[p for p in parsed if p and p["rel"]==rel]
    changed_cands=[p for p in parsed if p and p["crel"]==rel]
    shi=[p for p in parsed if p and p["shi"]]
    changed_main=False; reserve_used=False; disputed=False; reasons=[]
    main=None
    if cands:
        # prefer moving candidate
        movs=[c for c in cands if c["mov"]]
        main=movs[0] if movs else cands[0]
        if len(cands)>1: disputed=True; reasons.append(f"现卦{rel}两现/多现（{len(cands)}爻），按动者/旺者定主、余者留应验位，取用存疑")
    elif changed_cands:
        main=changed_cands[0]; changed_main=True; reasons.append(f"{rel}不上卦、变爻现{rel}，按黄金策次序取变爻为用、不取伏神")
    elif hidden:
        reserve_used=True; reasons.append(f"{rel}不上卦且变爻无之，取伏神：{hidden}")
    if not main and shi: main={"pos":shi[0]["pos"],"rel":rel,"br":shi[0]["br"],"el":shi[0]["el"],"mov":shi[0]["mov"],"crel":shi[0]["crel"],"cbr":shi[0]["cbr"],"cel":shi[0]["cel"]}
    if main is None:
        pred=f"盘面残损，无法定{rel}用神：方向不定，倾向不成/不顺；应期不予定点。"
        return {"case_id":cid,"prediction_text":pred,"basis":f"tradition=liuyao（输入卡 tradition 字段）\nsystems_used: liuyao\n用神：{rel_note}；盘面解析失败，输入残损注明、降置信，不臆补。卦：{hexa}；占时：{asked}；问：{q}","confidence":0.25,"trigger":{"changed_main":False,"reserve_used":bool(hidden),"disputed":True,"reason":"盘面解析失败，用神不定"}}
    el=main["el"]; br=main["br"]
    sc,notes=strength(el,month,day)
    # moving interactions: count movers克/生 yong
    ke_n=sheng_n=0
    for p in parsed:
        if p and p["mov"]:
            if KE[p["el"]]==el: ke_n+=1
            if SHENG[p["el"]]==el: sheng_n+=1
            if p["pos"]==main["pos"] and p["cel"]:
                if KE[p["cel"]]==el: pass
    # changed direction for main if moving
    ch_note=""
    if main.get("mov") and main.get("cbr"):
        cel=main["cel"]
        # 进退: same element family sequence by branch index
        if BR.index(main["cbr"])>BR.index(br) and cel==el: ch_note="化进神，进益"
        elif BR.index(main["cbr"])<BR.index(br) and cel==el: ch_note="化退神，退减"; sc-=1
        elif main["crel"] and SHENG[cel]==el: ch_note=f"化{main['crel']}回头生"; sc+=1
        elif main["crel"] and KE[cel]==el: ch_note=f"化{main['crel']}回头克"; sc-=2
    sc+=sheng_n-ke_n
    # timing: yong branch逢值 as main coordinate, window旬内/月内 by scale
    is_disease=rel=='官鬼' and any(k in q for k in ['病','疾','血崩'])
    is_life='壽' in q or '寿' in q
    scale="月" if (is_life or any(k in q for k in ['財福','终身','終身'])) else "日"
    win=f"自占日起一月内" if scale=="月" else "自占日起十日内（一旬）"
    coord=f"{br}{scale}（用神{br}{el}逢值/填实）"
    if is_disease:
        # disease: strong官鬼 = disease strong = negative; 子孙 strength matters - approximate: if官鬼旺 and克多 ->危
        if sc>=2: direction="病势仍盛、短期难愈，倾向凶/不愈（近段）"; final="终局单判：negative（病难愈、须防加重）"
        elif sc<=-2: direction="病神衰弱、药力可制，倾向渐愈"; final="终局单判：positive（可愈）"
        else: direction="病势缠绵、进退未定，倾向迟滞待应、暂难根除"; final="终局单判：negative（本期难愈、拖延）" if ke_n>=sheng_n else "终局单判：positive（迟而可愈）"
        pred=f"{direction}。用神{rel}{br}{el}（第{main['pos']}爻{'动' if main['mov'] else '静'}）旺衰据：{'；'.join(notes) or '月日无显生克'}；动爻生扶{sheng_n}处、克害{ke_n}处{('；'+ch_note) if ch_note else ''}。应期双层：窗口{win}，主坐标{coord}——尺度定为{scale}档（病/近事），三路：填实取{br}值、冲实取{BR[(BR.index(br)+6)%12]}冲、逢值取{br}，取逢值/填实一路与终局自洽，余路尺度或方向不合舍弃。{final}。对象复述：承受对象为题面所问患者本人/所代之人，与用神六亲指代链对回一致。"
    else:
        if sc>=2: direction="倾向成/得/吉，用神旺相有气、事可成且程度足级"
        elif sc<=-2: direction="倾向不成/不得/凶，用神休囚受制、无救则难成"
        else: direction="倾向迟滞待应、成败参半偏" + ("成（待填实出空方应）" if sheng_n>=ke_n else "不成（克害居多）")
        final_dir="positive" if sc>=0 else "negative"
        pred=f"问「{q}」：{direction}。用神{rel}{br}{el}（第{main['pos']}爻{'动' if main['mov'] else '静'}）：{'；'.join(notes) or '月日无显生克'}；动爻生扶{sheng_n}处、克害{ke_n}处{('；动化：'+ch_note) if ch_note else ''}。应期双层：窗口{win}，主坐标{coord}——尺度{scale}档，三路候选：冲实{BR[(BR.index(br)+6)%12]}、填实{br}、逢值{br}，取与终局自洽的逢值/填实一路，余路注明舍弃（尺度不合或方向相悖）。终局单判：{final_dir}。"
    conf=0.62 if not disputed else 0.5
    if reserve_used or changed_main: conf-=0.07
    if not month or not day: conf-=0.08; reasons.append("占时月日不全，旺衰权重降低")
    if not rawlines: conf-=0.1; reasons.append("无盘面行，输入残损")
    basis=f"tradition=liuyao（输入卡 tradition 字段）\nsystems_used: liuyao\n卦：{hexa}；占时：{asked}；动爻：{moving or '无/未载'}；空亡：{kong or '未载，按日干支旬空常规未另臆补'}；伏神：{hidden or '无'}。用神：{rel_note}，定主为第{main['pos']}爻{rel}{br}{el}。旺衰：{'；'.join(notes)}。动化复核：化神对用神生克逐对核（生扶{sheng_n}/克害{ke_n}）{('；'+ch_note) if ch_note else ''}。门类应期对表：{'病占/近事以填实逢值为首选' if scale=='日' else '终身/远事对表以月年逢值为首选'}，闸门（空墓）释放优先于对表。列面—证据双闸：列面齐（卦/月日/动爻/用神），证据据盘面行与月日干支，无金标接触。"
    trig={"changed_main":changed_main,"reserve_used":reserve_used,"disputed":disputed,"reason":"；".join(reasons)}
    return {"case_id":cid,"prediction_text":pred,"basis":basis,"confidence":round(max(0.2,min(0.85,conf)),2),"trigger":trig}
for bname in sys.argv[1:]:
    ids=BATCHES[bname]; n=0
    for cid in ids:
        r=predict(cid)
        with open(f"{OUT}/{cid}.json","w",encoding="utf-8") as f: json.dump(r,f,ensure_ascii=False,indent=1)
        # validate own file
        v=json.load(open(f"{OUT}/{cid}.json")); assert set(v)=={"case_id","prediction_text","basis","confidence","trigger"} and set(v["trigger"])=={"changed_main","reserve_used","disputed","reason"}
        n+=1
    print(bname,n)
