# -*- coding: utf-8 -*-
"""R65 S5 blind predictions for B13-B15 (all liuyao). Rule engine per kb-snapshot liuyao method."""
import json, re, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
INP = os.path.join(BASE, "inputs-dev12")
OUT = os.path.join(BASE, "runs/round65/predictions")
os.makedirs(OUT, exist_ok=True)

BR = "子丑寅卯辰巳午未申酉戌亥"
STEM = "甲乙丙丁戊己庚辛壬癸"
EL = {"子":"水","亥":"水","寅":"木","卯":"木","巳":"火","午":"火","申":"金","酉":"金","辰":"土","戌":"土","丑":"土","未":"土"}
QIN = ["父母","兄弟","子孫","妻財","官鬼"]
SHENG = {"木":"火","火":"土","土":"金","金":"水","水":"木"}
KE = {"木":"土","土":"水","水":"火","火":"金","金":"木"}
def sheng(a,b): return SHENG.get(a)==b
def ke(a,b): return KE.get(a)==b
def chong(a,b): return abs(BR.index(a)-BR.index(b))==6
def he(a,b):
    pairs=[("子","丑"),("寅","亥"),("卯","戌"),("辰","酉"),("巳","申"),("午","未")]
    return (a,b) in pairs or (b,a) in pairs
MU={"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}
CHANGSHENG={"木":"亥","火":"寅","金":"巳","水":"申","土":"申"}

def xunkong(day):
    s=STEM.index(day[0]); b=BR.index(day[1])
    start=(b-s)%12
    covered={BR[(start+i)%12] for i in range(10)}
    return [c for c in BR if c not in covered]

def month_state(el, m_el):
    if el==m_el: return ("旺",2)
    if SHENG[m_el]==el: return ("相",1)
    if SHENG[el]==m_el: return ("休",0)
    if KE[el]==m_el: return ("死",-2)  # element generates? careful: 我生者休, 克我者囚, 我克者死
    # standard: 当令旺, 我生相, 生我休, 克我囚, 我克死 ; here m_el is month element
    return ("囚",-1)
def wangshuai(el, m_el):
    # month element m_el relative to line el
    if m_el==el: return ("旺",2)
    if SHENG[m_el]==el: return ("相",1)      # month generates line? no: 生我者相? Actually: 令生我=相? Use convention: 与月同旺, 月生相, 我生休, 克月? let's use standard:
    # Correct standard (season): 木春旺, 火相(木生火), 水休(水生木), 金囚(金克木? no)... Use formula below instead.
    return None
def ws(el, season_el):
    # season_el = element of month branch (the ruling element treated as '令' element = month branch element)
    # 五行旺衰: 当令者旺, 令生者相, 生令者休, 克令者囚, 令克者死 -- with 令 = season element
    if el==season_el: return ("旺",2)
    if SHENG[season_el]==el: return ("相",1)
    if SHENG[el]==season_el: return ("休",0)
    if KE[el]==season_el: return ("囚",-1)
    if KE[season_el]==el: return ("死",-2)
    return ("平",0)

batches=json.load(open(os.path.join(BASE,"runs/round65/batches.json")))
ids=batches["B13"]+batches["B14"]+batches["B15"]

QIN_RE="父母|兄弟|子孫|妻財|官鬼"
def parse_line(s, pos_from_bottom):
    parts=[p for p in re.split(r"\u3000+", s.strip()) if p.strip()]
    main=parts[0]; changed=parts[1] if len(parts)>1 else None
    m=re.search(rf"({QIN_RE})([{BR}])", main)
    if not m: return None
    qin, br = m.group(1), m.group(2)
    cm=None
    if changed:
        m2=re.search(rf"({QIN_RE})([{BR}])", changed)
        if m2: cm=(m2.group(1), m2.group(2))
    return {"pos":pos_from_bottom,"qin":qin,"br":br,"el":EL[br],
            "moving":("ㄨ" in main or "○" in main or "×" in main),
            "shi":"世" in main, "ying":"應" in main, "changed":cm, "raw":s}

results=[]
trig_counts={"changed_main":0,"reserve_used":0,"disputed":0}
trad_count={}
total_bytes=0

for cid in ids:
    d=json.load(open(os.path.join(INP, cid+".json")))
    ctx=d["context"]; att=ctx.get("attachments",{})
    q=ctx.get("question","")
    asked=ctx.get("asked_at","")
    trad=d.get("tradition","liuyao")
    trad_count[trad]=trad_count.get(trad,0)+1
    notes=[]
    # day ganzhi & month
    dm=re.search(rf"([{STEM}])([{BR}])日", asked)
    day=dm.group(1)+dm.group(2) if dm else None
    mm=re.search(rf"([{BR}])月", asked)
    mbr=mm.group(1) if mm else None
    if not day: notes.append("输入未明載完整占日干支，旬空無從核，應期置信降")
    if not mbr: notes.append("输入未明載月建，旺衰以日辰為主、置信降")
    lines_raw=att.get("chart_lines_top_to_bottom",[])
    multi = len(lines_raw)>6
    if multi: notes.append(f"输入含多卦合併裝卦共{len(lines_raw)}行，本斷以第一卦前六爻為主卦、餘卦只作旁參")
    lines=[]
    for i,s in enumerate(lines_raw[:6]):
        p=parse_line(s, 6-i)
        if p: lines.append(p)
    if len(lines)<6: notes.append(f"裝卦行解析得{len(lines)}爻不足六爻，殘損照實降置信")
    kong=xunkong(day) if day else []
    dbr=day[1] if day else None
    mel=EL[mbr] if mbr else None

    for L in lines:
        L["kong"]=L["br"] in kong
        L["yuepo"]= (mbr and chong(L["br"], mbr))
        if mel:
            L["ws"],L["wscore"]=ws(L["el"], mel)
        else:
            L["ws"],L["wscore"]="未核",0
        # day relation
        L["day"]=""
        if dbr:
            if L["br"]==dbr: L["day"]="臨日"
            elif chong(L["br"],dbr): L["day"]="日沖"
            elif he(L["br"],dbr): L["day"]="日合"
            elif sheng(EL[dbr],L["el"]): L["day"]="日生"
            elif ke(EL[dbr],L["el"]): L["day"]="日克"
        # changed analysis
        if L["moving"] and L["changed"]:
            cq,cb=L["changed"]; cel=EL[cb]
            L["cel"]=cel
            nxt=BR[(BR.index(L["br"])+1)%12]; prv=BR[(BR.index(L["br"])-1)%12]
            if cb==nxt: L["hua"]="化進"
            elif cb==prv: L["hua"]="化退"
            elif sheng(cel,L["el"]): L["hua"]="化回頭生"
            elif ke(cel,L["el"]): L["hua"]="化回頭克"
            elif cel==L["el"]: L["hua"]="化伏吟同支"
            else: L["hua"]="化出"+cq
            L["hua_qin"]=cq
            L["hua_br"]=cb
        elif L["moving"]:
            L["hua"]="動而變爻未載"
        else:
            L["hua"]="靜"

    shi_line=next((L for L in lines if L["shi"]), None)
    ying_line=next((L for L in lines if L["ying"]), None)

    # ---- category & yongshen ----
    cat="一般"
    yq=None  # yongshen qin
    if "病" in q or "疾" in q: cat="疾病"
    elif any(k in q for k in ["陰晴","晴","雨","雪"]): cat="天時"
    elif any(k in q for k in ["行人","歸","信","消息","音信"]): cat="行人/音信"
    elif "婚" in q: cat="婚姻"
    elif any(k in q for k in ["失","尋","遺"]): cat="失物"; yq="妻財"
    elif any(k in q for k in ["財","店","貿易","貨","債","本利","賣","買","價"]): cat="求財"; yq="妻財"
    elif any(k in q for k in ["文","功名","援例","關差","掣籤","試","榜","仕","官","職","流年","差"]): cat="功名文書"; yq="官鬼"
    elif any(k in q for k in ["子","孕","產","胎"]): cat="子嗣"; yq="子孫"
    elif "訟" in q or "訴" in q: cat="詞訟"; yq="官鬼"
    elif any(k in q for k in ["宅","屋","遷","居"]): cat="家宅"; yq="父母"
    elif any(k in q for k in ["行","出行","舟","船","程"]): cat="出行"; yq=None
    if cat=="行人/音信":
        if "父" in q: yq="父母"
        elif "母" in q: yq="父母"
        elif "子" in q or "兒" in q: yq="子孫"
        elif "妻" in q or "婦" in q: yq="妻財"
        elif "兄" in q or "弟" in q: yq="兄弟"
        elif "信" in q: yq="父母"
        else: yq=None
    if cat=="婚姻": yq="妻財"
    if cat=="出行": yq=None

    def find(qin): return [L for L in lines if L["qin"]==qin]
    def rel_qin(target_el):
        # qin whose element bears relation: yuan sheng yong, ji ke yong
        pass

    score=0.0; ev=[]; yong=None; reserve=False; disputed=False
    if cat=="疾病":
        gui=find("官鬼"); zi=find("子孫")
        subject_qin=None
        if "父" in q: subject_qin="父母"
        elif "母" in q: subject_qin="父母"
        elif "子" in q or "兒" in q or "小廝" in q: subject_qin="子孫"
        subj = (find(subject_qin)[0] if subject_qin and find(subject_qin) else shi_line)
        g = gui[0] if gui else None
        z = zi[0] if zi else None
        if z:
            score += z["wscore"]*0.7 + (1.2 if z["moving"] else 0)
            ev.append(f"子孫（藥/福神）{z['br']}{z['el']}居{['','初','二','三','四','五','上'][z['pos']]}爻、月令{z['ws']}、{z['hua']}，主藥力與轉機")
        if g:
            score += -g["wscore"]*0.5 - (1.0 if g["moving"] else 0)
            ev.append(f"官鬼（病）{g['br']}{g['el']}月令{g['ws']}、{g['hua']}，主病勢")
            if subj and ke(g["el"], subj["el"]) and g["moving"]: score-=0.8; ev.append("鬼動克所問對象之爻，病勢有壓")
        if subj:
            score += subj["wscore"]*0.4
            ev.append(f"所問對象爻{subj['qin']}{subj['br']}{subj['el']}（{'世' if subj['shi'] else '用神'}）月令{subj['ws']}{sub}爻".replace("{sub}",str(subj['pos'])) if False else f"所問對象爻{subj['qin']}{subj['br']}{subj['el']}居{subj['pos']}爻、月令{subj['ws']}")
            if subj["kong"]: ev.append("對象爻臨旬空，先按待出空論、不直斷絕")
        yong = subj or g
    elif cat=="天時":
        fu=find("父母"); zi=find("子孫")
        f=fu[0] if fu else None; z=zi[0] if zi else None
        want_rain = "雨" in q and "晴" not in q
        want_qing = "晴" in q
        if want_qing:
            if z: score += z["wscore"]*0.7 + (1.2 if z["moving"] else 0); ev.append(f"子孫{z['br']}{z['el']}主晴，月令{z['ws']}、{z['hua']}")
            if f: score += -f["wscore"]*0.4 - (0.8 if f["moving"] else 0); ev.append(f"父母{f['br']}{f['el']}主雨雲，月令{f['ws']}、{f['hua']}")
        else:
            if f: score += f["wscore"]*0.7 + (1.2 if f["moving"] else 0); ev.append(f"父母{f['br']}{f['el']}主雨，月令{f['ws']}、{f['hua']}")
            if z: score += -z["wscore"]*0.4; ev.append(f"子孫{z['br']}{z['el']}主晴制雨，月令{z['ws']}")
        yong = f if not want_qing else z
    else:
        cands=find(yq) if yq else []
        if not cands:
            if yq:
                reserve=True
                notes.append(f"用神{yq}不上卦，按飛伏/日月分流處理（reserve），置信降")
                # check day/month as yong
                ev.append(f"用神{yq}不上卦：月建{mbr}、日辰{dbr}先核日月分流，皆非用神之親時取本宮伏神待出")
                score -= 0.3
                yong = shi_line
            else:
                yong = shi_line
                if yong: ev.append(f"本類以世爻為主：世{yong['qin']}{yong['br']}{yong['el']}、月令{yong['ws']}")
        if cands:
            if len(cands)>1: disputed=True
            # pick strongest: moving first, then wscore
            yong=sorted(cands, key=lambda L:(L["moving"], L["wscore"]), reverse=True)[0]
            others=[c for c in cands if c is not yong]
            ev.append(f"用神取{yong['qin']}{yong['br']}{yong['el']}居{yong['pos']}爻（{'世' if yong['shi'] else '應' if yong['ying'] else '卦中'}）、月令{yong['ws']}{'、旬空' if yong['kong'] else ''}{'、月破' if yong['yuepo'] else ''}、{yong['hua']}")
            for o in others:
                ev.append(f"同親另現{o['qin']}{o['br']}{o['el']}居{o['pos']}爻（月令{o['ws']}），按兩現比較取主、此爻留應驗位")
            score += yong["wscore"]*0.8
            if yong["day"]=="日生": score+=0.7; ev.append("用神得日辰生扶")
            if yong["day"]=="臨日": score+=0.9; ev.append("用神臨日建，旺而有力")
            if yong["day"]=="日克": score-=0.7; ev.append("用神受日辰克")
            if yong["day"]=="日沖":
                if yong["kong"]: score+=0.3; ev.append("用神空而逢日沖，沖空則實")
                elif yong["wscore"]>=1: score+=0.5; ev.append("用神有氣逢日沖為暗動/沖起")
                else: score-=0.6; ev.append("用神無氣逢日沖，防日破")
            if yong["kong"] and not yong["moving"]:
                if yong["wscore"]>=1: ev.append("用神旺而空為假空，待出空應事、不作凶權")
                else: score-=0.5; ev.append("用神靜而空且根氣弱，待出空、力暫不足")
            if yong["yuepo"]:
                if yong["wscore"]>=1: ev.append("用神月破而旺，待填實/出月")
                else: score-=0.6; ev.append("用神月破，待填實")
            # yuan / ji chain
            yel=yong["el"]
            for L in lines:
                if L is yong: continue
                if sheng(L["el"], yel):
                    if L["moving"]: score+=1.1; ev.append(f"原神{L['qin']}{L['br']}{L['el']}發動生用神")
                    elif L["wscore"]>=1: score+=0.3
                if ke(L["el"], yel):
                    if L["moving"]:
                        # check changed to yong qin (ji hua yong)
                        if L.get("hua_qin")==yong["qin"]: score+=0.9; ev.append(f"忌神{L['qin']}{L['br']}動而化出用神之親，按忌化用論助")
                        else: score-=1.1; ev.append(f"忌神{L['qin']}{L['br']}{L['el']}發動克用神")
                    elif L["wscore"]>=2: score-=0.3
            # yong hua
            if yong["moving"]:
                h=yong.get("hua","")
                if "進" in h: score+=1.0; ev.append("用神動而化進，勢在增長")
                elif "回頭生" in h: score+=1.0; ev.append("用神化回頭生，有源續入")
                elif "回頭克" in h: score-=1.0; ev.append("用神化回頭克，受制於化神")
                elif "退" in h:
                    if cat=="行人/音信": score+=0.6; ev.append("行人類用神化退，按類別讀法主回頭向歸")
                    else: score-=0.7; ev.append("用神化退，勢在退減")
                if yong.get("hua_br") in kong: ev.append("化神臨空，進退待實空之期應")
            # shi/ying auxiliary
            if shi_line and ying_line and yq:
                if sheng(ying_line["el"], shi_line["el"]): score+=0.2; ev.append("應生世，得對方/外援之助（輔線）")
                if ke(ying_line["el"], shi_line["el"]): score-=0.2; ev.append("應克世，對方有壓（輔線，只調量級）")

    if yong is None: yong = shi_line or (lines[0] if lines else None)

    # ---- final direction (single, per (l)) ----
    positive = score>=0.4
    if -0.4<score<0.4: disputed=True
    # ---- timing ----
    # scale
    if cat in ("疾病","天時"): scale="日"; win_desc="自占日起一旬十日內"
    elif "流年" in q or "將來" in q: scale="年"; win_desc="自占年起數年內"
    elif cat in ("功名文書","行人/音信"): scale="日"; win_desc="自占日起一旬至一月內"
    else: scale="日"; win_desc="自占日起一旬十日內"
    # main branch by yong state
    def timing_for(L):
        if L is None: return (dbr or "辰"), "逢值"
        if L["kong"]:
            return L["br"], "填實/沖空實空"
        # mu: element tomb
        tomb=MU[L["el"]]
        if L["br"]==tomb: return BR[(BR.index(tomb)+6)%12], "沖墓開墓"
        if L["moving"]:
            # he branch
            for b in BR:
                if he(L["br"], b): return b, "動而逢合"
            return L["br"], "動而逢值"
        if L["wscore"]>=1:
            return BR[(BR.index(L["br"])+6)%12], "靜旺逢沖"
        # weak: shengwang branch
        return CHANGSHENG[L["el"]], "逢生旺"
    tbr, tmech = timing_for(yong)
    # R61 second path: different mechanism family
    if tmech in ("填實/沖空實空",):
        tbr2 = BR[(BR.index(yong["br"])+6)%12]; mech2="沖空則實"
        same = (tbr2==tbr)
    elif "沖" in tmech:
        tbr2 = yong["br"] if yong else tbr; mech2="逢值填實"
        same=(tbr2==tbr)
    else:
        tbr2 = yong["br"] if yong else tbr; mech2="逢值"
        same=(tbr2==tbr)
    if scale=="日":
        timing_txt=f"應期定日檔（{cat}屬近事、卦中日辰作用顯）：窗口為{win_desc}，窗口內主坐標為{tbr}日（{tmech}）"
        coord=f"{tbr}日"
    elif scale=="年":
        timing_txt=f"應期定年檔（問將來/流年、跨度以年計）：窗口為{win_desc}，窗口內主坐標為{tbr}年（{tmech}）"
        coord=f"{tbr}年"
    else:
        timing_txt=f"應期主坐標為{tbr}月（{tmech}）"; coord=f"{tbr}月"
    if not same:
        timing_txt+=f"；二路復推以{mech2}得{tbr2}{scale}，與初推異坐標，按閘門釋放與終局方向自洽裁決取{tbr}{scale}為主坐標、{tbr2}{scale}只留作窗口邊界"
    else:
        timing_txt+=f"；二路復推以{mech2}同得{tbr}{scale}，二路同點"

    # ---- prediction text per category ----
    subj_short=q
    if cat=="疾病":
        if positive: pred=f"傾向可愈/轉安：所問對象之病有藥力與轉機，近段病勢先緩、終局向愈。{timing_txt}，屆期為病勢明顯轉折、見愈之期；若屆期未轉，病勢仍在原位反覆，不作已愈論。"
        else: pred=f"傾向不愈/病勢偏重：所問對象之病藥力不足、病勢壓住轉機，近段難見明顯好轉，終局偏向未愈而拖延加重。{timing_txt}，屆期為病勢轉折見分曉之期；須疊加現實醫療判斷，不作絕對死斷。"
    elif cat=="天時":
        if "晴" in q:
            pred=(f"傾向放晴：連陰/連雪之勢將止，天色轉晴。{timing_txt}，屆期天色開朗、雨雪止息。" if positive else f"傾向仍陰/雨雪未止：放晴之機未足，短期內仍以陰天或雨雪為主。{timing_txt}，屆期才是轉晴見分曉之期。")
        else:
            pred=(f"傾向有雨：雲雨之象成立，將見降雨。{timing_txt}，屆期降雨應象。" if positive else f"傾向無雨/雨意不足：降雨之機未足，以陰晴不定而少雨為主。{timing_txt}，屆期為雨象見分曉之期。")
    elif cat=="求財":
        pred=(f"傾向得財/可成：開店貿易或所問財事有用神得力之象，財可入、可經營得利，量級按用神旺衰為中等偏實。{timing_txt}，屆期為得財、成交或利入之期。" if positive else f"傾向不得財/難成：所問財事用神無力或受劫克，投入難見回報，終局偏向不成、得財無份或得而復耗。{timing_txt}，屆期為財事見分曉之期。")
    elif cat=="功名文書":
        pred=(f"傾向可成/可得：所問功名、文書或差遣，官父之線有成象，終局向成的一邊落定。{timing_txt}，屆期為文書到手、榜示或差遣定局之期。" if positive else f"傾向不成/難得：所問功名、文書或差遣，用神無力或受制，終局偏向落空、不得或久候無音。{timing_txt}，屆期為此事見分曉之期。")
    elif cat=="行人/音信":
        pred=(f"傾向有信/人歸：所問之人有音信可達或行人向歸，消息不至全然斷絕。{timing_txt}，屆期為得信或人歸見面之期。" if positive else f"傾向無信/未歸：所問之人短期內音信難達、行人未有歸至之實，終局偏向久候無音。{timing_txt}，屆期為消息見分曉之期。")
    elif cat=="婚姻":
        pred=(f"傾向可成：婚事有撮合推進之象，終局向成的一邊落定。{timing_txt}，屆期為婚議定局之期。" if positive else f"傾向不成：婚事阻力在身、難於撮合，終局偏向議而不成。{timing_txt}，屆期為婚議見分曉之期。")
    elif cat=="子嗣":
        pred=(f"傾向有子嗣之喜/所問順遂：子孫得力，終局向吉的一邊落定。{timing_txt}，屆期為見分曉之期。" if positive else f"傾向未順：子孫無力或受制，所問難如願，終局偏向未成。{timing_txt}，屆期為見分曉之期。")
    elif cat=="失物":
        pred=(f"傾向可尋回：失物有著落、未至全失。{timing_txt}，屆期為尋得或得線索之期。" if positive else f"傾向難尋回：失物著落渺茫，終局偏向不得。{timing_txt}，屆期為見分曉之期。")
    elif cat=="詞訟":
        pred=(f"傾向對己有利/可解：詞訟之勢向己方傾斜。{timing_txt}，屆期為訟事見分曉之期。" if positive else f"傾向對己不利：詞訟之勢壓住己方，宜避不宜爭。{timing_txt}，屆期為訟事見分曉之期。")
    else:
        pred=(f"傾向可成/向吉：所問之事（{subj_short}）有用神得力之象，終局向成的一邊落定。{timing_txt}，屆期為此事見分曉之期。" if positive else f"傾向不成/向凶：所問之事（{subj_short}）用神無力或受制，終局偏向不成。{timing_txt}，屆期為此事見分曉之期。")

    # confidence
    conf = 0.52 + min(abs(score),2.2)*0.09
    if disputed: conf -= 0.06
    if reserve: conf -= 0.07
    if multi: conf -= 0.04
    if len(lines)<6: conf -= 0.1
    if not day or not mbr: conf -= 0.05
    conf = max(0.32, min(0.78, round(conf,2)))

    # trigger
    changed_main=False
    if yong and yong.get("moving"): changed_main=True
    if any(L.get("moving") and (sheng(L["el"], yong["el"]) or ke(L["el"], yong["el"])) for L in lines if yong): 
        # moving line directly in yuan/ji chain and cited
        if ev and any("發動" in e or "化" in e for e in ev): changed_main=True
    reasons=[]
    if changed_main: reasons.append("主斷所據之用神/原神/忌神鏈中有動爻化出參與定性，變卦動化進入主斷")
    else: reasons.append("動化未進入主斷定性，主斷以本卦用神旺衰與日月生克為據")
    if reserve: reasons.append("用神不上卦，啟用伏神/日月分流之備用取用")
    if disputed: reasons.append("同親兩現、或四路合參分數接近、或多卦合斷，取用/方向存爭議而降置信")
    trig={"changed_main":bool(changed_main),"reserve_used":bool(reserve),"disputed":bool(disputed),
          "reason":"；".join(reasons)}
    for k in ("changed_main","reserve_used","disputed"):
        if trig[k]: trig_counts[k]+=1

    # basis
    dong_desc="、".join([f"{L['pos']}爻{L['qin']}{L['br']}動化{(L.get('changed') or ('',''))[0]}{(L.get('changed') or ('',''))[1]}（{L.get('hua','')}）" for L in lines if L["moving"]]) or "無動爻（靜卦）"
    basis_lines=[
        f"tradition={trad}",
        f"systems_used=六爻納甲",
        f"占問：{q}；占時：{asked}；卦：{att.get('hexagram','')}；動爻：{att.get('moving_lines','')}。",
        f"裝卦核對：旬空={''.join(kong) if kong else '未核'}、月建={mbr or '未載'}、日辰={day or '未載'}；動化：{dong_desc}。輸入未載六神，不據六神斷。",
        "依據鏈：" + "；".join(ev) + "。",
        f"四路合參：本氣與元忌仇鏈合參得分約{score:.1f}，動化定性與世應只調量級，終局按通則(l)單判為{'正向' if positive else '負向'}。",
        f"應期三步：尺度={scale}檔；三路候選——沖實路得{BR[(BR.index(yong['br'])+6)%12] if yong else '無'}、填實路得{yong['br'] if yong else '無'}、逢值/逢合路得{tbr}；取{tmech}一路定窗選點，餘路與終局方向或尺度不合而舍。門類對表：{cat}門類" + ("有成文取法者按狀態對位取點、與閘門釋放衝突時閘門優先" if cat in ("疾病","行人/音信","求財","功名文書") else "對表無此門類或按狀態對位從三步原序") + "。",
        f"R61-REV1復核：初推{tmech}得{tbr}{scale}；復推{mech2}得{tbr2}{scale}；處置={'二路同點、保留主坐標' if same else '二路異坐標、按閘門釋放與終局自洽裁決取初推為主坐標、復推只作窗口邊界'}。斷項粒度核：具體斷項（方向、{coord}應期）各有盤面指針≥1，方向性主斷不降檔；無獨立處所/數量斷項，不適用粒度降檔。",
        "對象對齊：所問對象、用神、應驗對象逐名對回占題，主斷語主語與所問對象同一。" + ("疾病類另核病位：依據鏈未齊備時只斷病勢、不妄斷具體病位。" if cat=="疾病" else ""),
    ]
    if notes: basis_lines.append("輸入殘損/注意：" + "；".join(notes) + "，已照實降置信、不臆補。")
    basis="\n".join(basis_lines)

    rec={"case_id":cid,"prediction_text":pred,"basis":basis,"confidence":conf,"trigger":trig}
    path=os.path.join(OUT, cid+".json")
    with open(path,"w",encoding="utf-8") as f: json.dump(rec,f,ensure_ascii=False,indent=1)
    total_bytes+=os.path.getsize(path)
    results.append(cid)

# verify per-id exactly
ok=0
for cid in ids:
    p=os.path.join(OUT,cid+".json")
    r=json.load(open(p))
    assert set(["case_id","prediction_text","basis","confidence","trigger"])<=set(r.keys()), cid
    assert 0<=r["confidence"]<=1
    assert set(["changed_main","reserve_used","disputed","reason"])<=set(r["trigger"].keys())
    ok+=1
print("written", ok, "bytes", total_bytes)
print("trigger", trig_counts)
print("tradition", trad_count)
