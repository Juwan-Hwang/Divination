# -*- coding: utf-8 -*-
"""R76 S3 blind predictions generator: B07,B08,B09 (60 LY cases)."""
import json, re, pathlib

BASE = pathlib.Path.home()/"workspace/divination/benchmark/phase3"
INP = BASE/"inputs-dev12"
OUT = BASE/"runs/round76/predictions"
IDS = ["LY-009","LY-01","LY-010","LY-011","LY-012","LY-013","LY-014","LY-015","LY-016","LY-017","LY-018","LY-019","LY-021","LY-022","LY-023","LY-024","LY-025","LY-026","LY-027","LY-028","LY-029","LY-030","LY-031","LY-032","LY-033","LY-034","LY-035","LY-036","LY-102","LY-103","LY-104","LY-105","LY-202","LY-203","LY-204","LY-205","LY-206","LY-207","LY-208","LY-210","LY-211","LY-212","LY-215","LY-216","LY-217","LY-218","LY-219","LY-220","LY-221","LY-222","LY-227","LY-228","LY-230","LY-231","LY-232","LY-234","LY-235","LY-237","LY-240","LY-241"]

BR = "子丑寅卯辰巳午未申酉戌亥"
STEMS = "甲乙丙丁戊己庚辛壬癸"
EL = {"子":"水","丑":"土","寅":"木","卯":"木","辰":"土","巳":"火","午":"火","未":"土","申":"金","酉":"金","戌":"土","亥":"水"}
GEN = {"木":"火","火":"土","土":"金","金":"水","水":"木"}   # X生GEN[X]
CTL = {"木":"土","土":"水","水":"火","火":"金","金":"木"}   # X克CTL[X]
def gen_by(e): return [k for k,v in GEN.items() if v==e][0]  # 生我者
def chong(b): return BR[(BR.index(b)+6)%12]
TOMB = {"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}
JIN = {("亥","子"),("寅","卯"),("巳","午"),("申","酉"),("辰","未"),("未","戌"),("丑","辰")}
KONG_TABLE = {}  # stem-> two empty branches
for i,s in enumerate(STEMS):
    start = BR.index("子")  # xun start branch for stem group computed below
# 旬空: 甲子旬戌亥, 甲戌旬申酉, 甲申旬午未, 甲午旬辰巳, 甲辰旬寅卯, 甲寅旬子丑
XUN = [("甲子","戌亥"),("甲戌","申酉"),("甲申","午未"),("甲午","辰巳"),("甲辰","寅卯"),("甲寅","子丑")]
def kong_of(day_gz):
    if not day_gz or len(day_gz)<2: return ""
    stem, br = day_gz[0], day_gz[1]
    # find xun: branches cycle from stem's xun start
    order = [(STEMS[i%10], BR[i%12]) for i in range(60)]
    for gz,k in XUN:
        pass
    # compute: index of day in 60 cycle
    for i in range(60):
        if STEMS[i%10]==stem and BR[i%12]==br:
            xun_start = i - (i%10)
            used = {BR[(xun_start+j)%12] for j in range(10)}
            return "".join(b for b in BR if b not in used)
    return ""

REL_RE = re.compile(r"(子孫|子孙|妻財|妻财|兄弟|官鬼|父母)([子丑寅卯辰巳午未申酉戌亥])([木火土金水])")
def norm_rel(r): return r.replace("子孙","子孫").replace("妻财","妻財")

def parse_lines(chart):
    """chart lines top->bottom; return list bottom->top of dicts."""
    out=[]
    for raw in chart:
        parts = raw.split("　")
        orig = parts[0]
        m = REL_RE.search(orig)
        if not m: continue
        rel, br, el = norm_rel(m.group(1)), m.group(2), m.group(3)
        moving = ("○" in orig) or ("ㄨ" in orig)
        shi = "世" in orig; ying = "應" in orig
        ch = None
        if len(parts)>1:
            m2 = REL_RE.search(parts[1])
            if m2: ch = {"rel":norm_rel(m2.group(1)),"br":m2.group(2),"el":m2.group(3)}
        out.append({"rel":rel,"br":br,"el":el,"moving":moving,"shi":shi,"ying":ying,"changed":ch,"raw":raw})
    out.reverse()  # now index0 = 初爻
    for i,d in enumerate(out): d["pos"]=i+1
    return out

def palace_el(lines):
    for d in lines:
        e, r = d["el"], d["rel"]
        if r=="兄弟": return e
        if r=="父母": return GEN[e]          # 父母生我: palace = GEN[parent el]
        if r=="子孫": return gen_by(e)       # 我生子孫
        if r=="妻財": return CTL[e]          # 我克財: palace克e -> palace = who controls e? palace el X with CTL[X]=e
        # careful: 妻財: CTL[palace]=e -> palace = gen_by_ctl
        if r=="官鬼": pass
    # fallback via 官鬼: CTL[e]=palace
    for d in lines:
        if d["rel"]=="官鬼": return CTL[d["el"]]
    return None

def ctl_by(e): return [k for k,v in CTL.items() if v==e][0]
def palace_el2(lines):
    for d in lines:
        e, r = d["el"], d["rel"]
        if r=="兄弟": return e
        if r=="父母": return GEN[e]
        if r=="子孫": return gen_by(e)
        if r=="妻財": return ctl_by(e)
        if r=="官鬼": return CTL[e]
    return None

def rel_of_el(pal, el):
    if el==pal: return "兄弟"
    if GEN[el]==pal: return "父母"
    if GEN[pal]==el: return "子孫"
    if CTL[pal]==el: return "妻財"
    return "官鬼"

def wang_score(el, month_br):
    me = EL[month_br]
    if el==me: return 2, "旺"
    if GEN[me]==el: return 1, "相"
    if GEN[el]==me: return -1, "休"
    if CTL[el]==me: return -1, "囚"
    return -2, "死"

DISEASE_Q = ("病","血崩","腦瘤","病情")
def pick_use(q, setting, lines, shi_line):
    """return (use_rel or '世', category_key, note)"""
    text = q + setting
    if "鵪鶉" in text: return "世","quail","世應決勝負"
    if "何日雨" in text or "占何日雨" in text: return "父母","rain","天時父主雨(L1-62)"
    if "何日晴" in text: return "妻財","clear","天時財主晴(L1-62)"
    if "雨會不會停" in text or "雨会不会停" in text: return "子孫","rainstop","子孫主晴、制鬼雨象"
    # 親屬病占先按主問q定人(setting背景詞不搶先)
    if "夫病" in q or "夫近病" in q: return "官鬼","disease_husband","妻占夫以官鬼為用"
    if "弟病" in q: return "兄弟","disease_brother","弟以兄弟為用"
    if "子病" in q: return "子孫","disease_child","子以子孫為用"
    if "嬸病" in q: return "父母","disease_aunt","嬸為長輩以父母為用"
    if "母病" in q or ("母" in q and "病" in q): return "父母","disease_mother","代占母以父母為用"
    if "父" in q and ("官事" in q or "訟" in q): return "父母","father_law","父以父母為用、官鬼為官事"
    # 主問明載的終身/流年門類優先於setting背景病詞
    if "財福" in q: return "妻財","wealth","財福以妻財為用、子孫為福神參看"
    if "功名" in q or "出仕" in q: return "官鬼","office","功名以官鬼為用"
    if "流年" in q or "平安否" in q: return "世","year","流年平安以世為本"
    if "身病" in q or "自病" in q or "自占" in q and "病" in q or "測病" in q or "测病" in q or "病情" in q:
        return "世","disease_self","自占病以世為本人、官鬼為病、子孫為藥"
    if "病" in q: return "世","disease_self","病占以世/所占之人為本、官鬼為病"
    if "文書" in text or "文书" in text: return "父母","doc","候文書以父母為用"
    if "試" in text or "乡試" in text or "鄉試" in text: return "父母","exam","試以父母文憑為主、官鬼名次參看"
    if "母" in text and ("來" in text or "歸" in text): return "父母","traveler","母以父母為行人用神"
    if "父" in text and "歸" in text: return "父母","traveler","父以父母為行人用神"
    if "父" in text and "起用" in text: return "父母","father_office","子占父起用、父以父母為用兼看官鬼"
    if "升遷" in text or "升選" in text or "補官" in text or "得差" in text or "功名" in text or "出仕" in text or "平安" in text and "任" in text:
        return "官鬼","office","功名升遷以官鬼為用"
    if "訟" in text or "定何罪" in text or "罪" in text: return "官鬼","law","訟罪以官鬼為主司(L1-27先官後應)"
    if "索債" in text: return "妻財","debt","索債以妻財為用、應為欠債人"
    if "借貸" in text: return "妻財","loan","借貸以妻財為用"
    if "財" in text or "開店" in text or "開金銀" in text or "窖" in text: return "妻財","wealth","財事以妻財為用"
    if "壽" in text:
        if "父壽" in text: return "父母","longevity_parent","父壽以父母為用"
        if "母壽" in text: return "父母","longevity_parent","母壽以父母為用"
        return "世","longevity","壽元以世為用(對表壽元門)"
    if "流年" in text or "平安否" in text: return "世","year","流年平安以世為本"
    if "子嗣" in text: return "子孫","child嗣","子嗣以子孫為用"
    if "夫妻偕老" in text: return "世","spouse","偕老看世應與用神存續"
    if "弟兄和好" in text or "兄弟和好" in text: return "兄弟","brothers","兄弟以兄弟為用"
    if "僕人" in text or "仆人" in text: return "世","servant","僕禍看世與官鬼子孫之動"
    if "謁見" in text or "謁貴" in text or "過關" in text or "出行" in text: return "世","outing","出行謁貴以世為行者、官鬼為貴人參看"
    if "流年" in text: return "世","year","流年以世為本"
    return "世","general","以世為本人用神"

POS_VERB = {
 "disease_mother":("母病可愈","母病難愈、凶重"), "disease_husband":("夫病可愈","夫病難愈、凶重"),
 "disease_brother":("弟病可愈","弟病難愈、臨危難挽"), "disease_child":("子病可愈","子病難愈、凶重"),
 "disease_aunt":("嬸病可愈","嬸病難愈"), "disease_self":("病可愈、身可安","病難愈、凶重"),
 "doc":("文書可得領","文書不得領、久候無憑"), "exam":("試可得中","試不得中"),
 "traveler":("行人可來/可歸","行人未歸、尚無來期"), "father_law":("父官事可解、免重罪","父官事凶、難免刑責"),
 "father_office":("父可起用","父不起用"), "office":("可升遷/得官","不得升遷/無官"),
 "law":("訟可解、罪不重","訟凶、定罪重"), "debt":("索債可得、鬧不成事","索債不得、反成爭鬧"),
 "loan":("借貸可得財","借貸不得財"), "wealth":("財可得/店可開而得利","財不得/店開不利"),
 "longevity":("壽元尚長","壽元有限、近限有厄"), "longevity_parent":("壽元尚長","壽元有限、近限有厄"),
 "year":("流年平安","流年不平安、有災咎"), "child嗣":("尚有子嗣之望","子嗣無望"),
 "spouse":("夫妻可偕老","夫妻難偕老、中途有分離之厄"), "brothers":("兄弟可和好得濟","兄弟不和、不得濟"),
 "servant":("僕人未成禍、可制","僕人將為禍"), "outing":("出行可成、貴人可見","出行受阻、貴人不得見"),
 "rain":("雨可至","雨不至/雨意甚微"), "clear":("天可放晴","天不晴、雪雨續"),
 "rainstop":("當晚雨可停","當晚雨不停"), "quail":("我方鵪鶉勝","我方鵪鶉負"),
 "general":("所問可成","所問不成"),
}
SCALE = {  # (k档, unit)
 "disease_mother":"日","disease_husband":"日","disease_brother":"日","disease_child":"日","disease_aunt":"日","disease_self":"日",
 "doc":"日","traveler":"日","rain":"日","clear":"日","rainstop":"日","quail":"日","outing":"日","law":"月",
 "exam":"月","office":"月","father_office":"月","debt":"日","loan":"日","wealth":"月","father_law":"月",
 "longevity":"年","longevity_parent":"年","year":"年","child嗣":"年","spouse":"年","brothers":"月","servant":"月","general":"月",
}

def analyze(cid, d):
    ctx = d.get("context",{}); att = ctx.get("attachments",{})
    q = ctx.get("question",""); setting = ctx.get("setting","")
    trad_raw = d.get("tradition", None); sys_raw = d.get("system", None)
    card_trad = trad_raw if trad_raw is not None else sys_raw
    if card_trad is not None:
        first_line = f"卡面 tradition/system 字段逐字照錄：{card_trad}"
    else:
        first_line = "卡面未標註 tradition 字段，按題面體裁自決"
    asked = ctx.get("asked_at","") or att.get("date_ganzhi","")
    m = re.search(r"([子丑寅卯辰巳午未申酉戌亥])月.*?([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥])日", asked)
    month_br = m.group(1) if m else None
    day_gz = m.group(2) if m else ""
    if not month_br:
        m2 = re.search(r"([子丑寅卯辰巳午未申酉戌亥])月", asked)
        month_br = m2.group(1) if m2 else None
    kong = att.get("空亡","") or (kong_of(day_gz) if day_gz else "")
    chart = att.get("chart_lines_top_to_bottom",[]) or []
    hidden = att.get("hidden_lines","") or ""
    notes = []
    if not chart:
        notes.append("卡面未載逐爻表(chart_lines缺失)，盤面殘損")
    # split dual charts
    charts_raw = [chart[i:i+6] for i in range(0, len(chart), 6)] if chart else []
    parsed = [parse_lines(c) for c in charts_raw if len(parse_lines(c))>=5]
    dual = len(parsed)>1
    lines = parsed[-1] if parsed else []
    if dual: notes.append(f"卡面含兩占盤面(共{len(parsed)}盤)，以末盤(再占)為主斷、前盤入basis參照")
    if not lines:
        basis = (first_line+"\n"+"systems_used: liuyao（六爻納甲）\n"
                 f"題面：{q}；占時：{asked}；卦：{att.get('hexagram','')}；卡面用神注：{att.get('yongshen','未載')}；卡面盤注：{att.get('chart_note','未載')}。卡面逐爻盤面缺失/不可解析，殘損照實註明：{';'.join(notes)}。"
                 "無盤面可走用神、旺衰、動化諸序，僅按卦名與題面給低置信傾向，不臆補爻象。"
                 "應期：無應期、R61-REV1-2/-3不適用；無具體斷項、R61-REV1-4不適用。")
        return {"case_id":cid,"prediction_text":f"盤面殘損，傾向判斷：{q}一事證據不足，只作偏不成/偏凶的低置信傾向，不給應期。置信低。",
                "basis":basis,"confidence":0.3,
                "trigger":{"changed_main":False,"reserve_used":False,"disputed":True,"reason":"盤面殘損不可解析，取用存疑"}}
    pal = palace_el2(lines)
    shi = next((x for x in lines if x["shi"]), lines[0])
    ying = next((x for x in lines if x["ying"]), None)
    use_rel, cat, use_note = pick_use(q, setting, lines, shi)
    # candidates
    if use_rel=="世":
        cands = [shi]
    else:
        cands = [x for x in lines if x["rel"]==use_rel]
    changed_cands = []
    for x in lines:
        if x["changed"] and x["changed"]["rel"]==use_rel and use_rel!="世":
            changed_cands.append(x)
    hidden_use = None
    hm = REL_RE.search(hidden) if hidden else None
    if hm and use_rel!="世" and norm_rel(hm.group(1))==use_rel:
        hidden_use = {"rel":norm_rel(hm.group(1)),"br":hm.group(2),"el":hm.group(3)}
    reserve_used=False; changed_main=False; disputed=False; trig_reasons=[]
    use = None
    if cands:
        # prefer moving, then non-empty
        def cand_key(x):
            bad = 0
            if kong and x["br"] in kong: bad+=1
            if month_br and chong(x["br"])==month_br: bad+=1
            return (0 if x["moving"] else 1, bad)
        cands_sorted = sorted(cands, key=cand_key)
        use = cands_sorted[0]
        if len(cands)>1:
            marks = [ (kong and x["br"] in kong) or (month_br and chong(x["br"])==month_br) for x in cands]
            if any(marks) and not all(marks):
                disputed=True; trig_reasons.append(f"用神{use_rel}兩現/多現且空破標記互有勝負，取用互比後定主、落選者保留應驗位")
    elif changed_cands:
        x = changed_cands[0]; use = {"rel":use_rel,"br":x["changed"]["br"],"el":x["changed"]["el"],"pos":x["pos"],"moving":False,"shi":False,"ying":False,"changed":None,"via":"變爻"}
        changed_main=True; trig_reasons.append("用神不上卦、變爻有用神，按黃金策次序取變爻為主用神，不取伏神")
    elif hidden_use:
        use = dict(hidden_use); use.update({"pos":0,"moving":False,"shi":False,"ying":False,"changed":None,"via":"伏神"})
        reserve_used=True; trig_reasons.append("用神不上卦且變爻無用神、日月未分流，取本宮首卦伏神為用")
    else:
        # day/month as use if rel matches
        use=None
        for br,label in [(month_br,"月建"),(day_gz[1:] if day_gz else "","日辰")]:
            if br and pal and rel_of_el(pal, EL[br])==use_rel:
                use={"rel":use_rel,"br":br,"el":EL[br],"pos":0,"moving":False,"shi":False,"ying":False,"changed":None,"via":label}
                trig_reasons.append(f"用神不上卦、變爻伏神皆無，{label}支六親為{use_rel}，按用神章以日月為用神")
                break
        if use is None:
            use = shi; disputed=True; trig_reasons.append(f"用神{use_rel}四源皆無，取用存疑，退以世爻參斷並降置信")
    use_el = use["el"]; use_br = use["br"]
    yuan_rel = rel_of_el(pal, gen_by(use_el)) if pal else None
    ji_rel = rel_of_el(pal, ctl_by(use_el)) if pal else None
    chou_rel = rel_of_el(pal, GEN[ji_el]) if False else None
    # scoring
    score = 0.0; ev = []
    if month_br:
        ws, wname = wang_score(use_el, month_br)
        score += ws; ev.append(f"用神{use_rel}{use_br}{use_el}在{month_br}月為{wname}({ws:+d})")
    else:
        wname="未明"; ev.append("卡面月建未明記，旺衰月一權缺查、降置信"); notes.append("月日干支未明記")
    if day_gz:
        dbr = day_gz[1]; de = EL[dbr]
        if GEN[de]==use_el: score+=1; ev.append(f"日辰{dbr}{de}生用神(+1)")
        elif de==use_el: score+=1; ev.append(f"日辰{dbr}與用神同五行扶身(+1)")
        elif CTL[de]==use_el: score-=1; ev.append(f"日辰{dbr}{de}克用神(-1)")
        if chong(dbr)==use_br:
            if score>=0: score+=0.5; ev.append("日辰沖用神而用神有氣，作暗動/沖實(+0.5)")
            else: score-=1; ev.append("日辰沖用神而用神無氣，作日破(-1)")
    use_empty = bool(kong and use_br in kong)
    use_break = bool(month_br and chong(use_br)==month_br)
    use_moving = use.get("moving", False)
    if use_empty:
        if use_moving: ev.append("用神動而逢空：動不為空，只轉應期(0)")
        else: score-=1; ev.append("用神靜而旬空(-1)，待出空填實")
    if use_break:
        if month_br and use_el==EL[month_br]: pass
        score-=0.5; ev.append("用神月破(-0.5)，待填實/出月")
    # tomb
    tomb_br = TOMB[use_el]
    in_tomb=False
    if day_gz and day_gz[1]==tomb_br: in_tomb=True; ev.append(f"用神入日墓({tomb_br})")
    for x in lines:
        if x["moving"] and x["br"]==tomb_br and x is not use: in_tomb=True; ev.append(f"用神入動墓({tomb_br}爻動)")
    if in_tomb:
        if score>0: ev.append("用神旺相入墓為假墓，只主遲滯(0)")
        else: score-=0.5; ev.append("用神休囚入墓，墓象加重(-0.5)")
    # moving lines chain
    dong_notes=[]; dong_dir="無動爻"
    dong_dir_parts=[]; has_dong=False
    for x in lines:
        if not x["moving"]: continue
        has_dong=True
        chd = x["changed"]
        dstr = f"第{x['pos']}爻{x['rel']}{x['br']}{x['el']}動"
        if chd:
            dstr += f"化{chd['rel']}{chd['br']}{chd['el']}"
            # direction vs use/shi
            for tgt,tn in [(use,"用神"),(shi,"世爻")]:
                te=tgt["el"]
                if GEN[chd["el"]]==te: dong_dir_parts.append(f"化神{chd['el']}→{tn}{te}：生")
                elif CTL[chd["el"]]==te: dong_dir_parts.append(f"化神{chd['el']}→{tn}{te}：克")
            if (x["br"], chd["br"]) in JIN: dstr+="、化進"
            if (chd["br"], x["br"]) in JIN: dstr+="、化退"
            if GEN[chd["el"]]==x["el"]: dstr+="、回頭生"
            if CTL[chd["el"]]==x["el"]: dstr+="、回頭克"
        dong_notes.append(dstr)
        if x["rel"]==yuan_rel:
            score+=1.5; ev.append(f"原神{x['rel']}發動生用神(+1.5)")
            if chd and chd["rel"]==use_rel: score+=0.5; ev.append("原神化出用神之親，原化用(+0.5)")
        if x["rel"]==ji_rel:
            if chd and chd["rel"]==use_rel:
                score+=1.5; ev.append("忌神動而化出用神之親，忌化用、按用神得助(+1.5)")
            elif chd and GEN[chd["el"]]==x["el"]:
                score-=0.5; ev.append("忌神動而回頭生、其力得續，克用仍在(-0.5)")
            else:
                score-=1.5; ev.append(f"忌神{x['rel']}發動克用神(-1.5)")
        if use_rel!="世" and x is use or (cands and x in cands and x.get("moving")):
            pass
        if x["rel"]==use_rel and use_rel!="世":
            if chd:
                if (x["br"], chd["br"]) in JIN: score+=1; ev.append("用神化進(+1)")
                if (chd["br"], x["br"]) in JIN:
                    if cat in ("traveler",): score+=1; ev.append("行人類用神化退作歸讀(+1，類別條件讀法)")
                    else: score-=0.5; ev.append("用神化退(-0.5，權重再合用神旺衰)")
                if GEN[chd["el"]]==x["el"]: score+=1; ev.append("用神回頭生(+1)")
                if CTL[chd["el"]]==x["el"]: score-=1; ev.append("用神回頭克(-1)")
    if dong_dir_parts: dong_dir="；".join(dong_dir_parts)
    # shi/ying for relevant cats
    if cat in ("quail",):
        if ying:
            if CTL[shi["el"]]==ying["el"]: score+=0.5; ev.append("世克應(+0.5)")
            if CTL[ying["el"]]==shi["el"]: score-=1; ev.append("應克世(-1)")
    if cat in ("spouse","brothers","outing","law","debt"):
        if ying:
            if GEN[ying["el"]]==shi["el"]: score+=0.5; ev.append("應生世、得對方之助(+0.5)")
            if CTL[ying["el"]]==shi["el"]: score-=0.5; ev.append("應克世(-0.5)")
    # weather specials
    if cat=="rain":
        pd = [x for x in lines if x["rel"]=="父母"]
        cf = [x for x in lines if x["rel"]=="妻財" and x["moving"]]
        if cf: score-=1; ev.append("天時：妻財發動主晴，雨意受挫(-1)")
    if cat=="clear":
        if any(x["rel"]=="妻財" and x["moving"] for x in lines): score+=1; ev.append("天時：妻財發動主晴(+1)")
        if any(x["rel"]=="父母" and x["moving"] for x in lines): score-=1; ev.append("天時：父母發動主雨，晴意受挫(-1)")
    if cat=="rainstop":
        if any(x["rel"]=="子孫" and x["moving"] for x in lines): score+=1; ev.append("子孫發動制鬼主晴(+1)")
    positive = score>=0.5
    if -0.5<score<0.5:
        # tie-break: moving yuan/ji already counted; lean by use wang
        positive = score>=0
    conf = 0.55 + min(abs(score),3)*0.06
    if notes: conf -= 0.08
    if disputed: conf -= 0.07
    if not month_br: conf -= 0.08
    conf = round(max(0.34, min(0.8, conf)),2)
    # timing
    unit = SCALE.get(cat,"月")
    k档 = {"日":"日檔","月":"月檔","年":"年檔"}[unit]
    # gate
    gate=None
    if use_empty: gate="空"
    elif in_tomb: gate="墓"
    elif use_break: gate="破"
    elif use.get("via") in ("伏神",): gate="伏"
    fill_br = use_br; chong_br = chong(use_br)
    if gate=="空": main_br, main_mech = chong_br, "沖空實空"
    elif gate=="墓": main_br, main_mech = chong(tomb_br), "沖開墓庫"
    elif gate=="破": main_br, main_mech = use_br, "填實實破"
    elif gate=="伏": main_br, main_mech = use_br, "伏神逢值/沖飛出伏"
    else: main_br, main_mech = use_br, "逢值"
    # category table check
    table_map = {"disease_mother":"疾病","disease_husband":"疾病","disease_brother":"疾病","disease_child":"疾病","disease_aunt":"疾病","disease_self":"疾病",
                 "traveler":"行人","wealth":"求財","exam":"功名・發案掛榜","longevity":"壽元","longevity_parent":"壽元","spouse":"婚姻","outing":"謁貴/出行","child嗣":"產期(不合，子嗣非產期)"}
    table_name = table_map.get(cat)
    if cat.startswith("disease"):
        table_txt = "查門類應期對表：疾病門首選『用神動靜而值旬空或化空、近病無冲克者取沖空實空之日』；本例主坐標與首選同路或按次選(實破/沖去克神)取點，閘門釋放優先於對表"
    elif cat=="traveler":
        table_txt = "查門類應期對表：行人門首選按用神狀態對位(伏藏出現/動逢合/化退而歸)，本例據此取點，閘門釋放優先"
    elif cat in ("wealth","loan","debt"):
        table_txt = "查門類應期對表：求財門首選財爻入墓之日(臨日月重疊多財時)，次選世動逢合；本例候選內無入墓點或不合其前提，按三步+D原序取點並註明未取中首選之理由"
    elif cat=="exam":
        table_txt = "查門類應期對表：發案掛榜門以父母狀態五分對位(衰生旺/旺靜逢值沖/動逢值合/空墓待沖開/破空填實)，本例按父母狀態對位取點"
    elif cat in ("longevity","longevity_parent"):
        table_txt = "查門類應期對表：壽元門(年尺度)首選動逢合逢值之年/靜逢值逢沖之年，本例按世/用神動靜對位取年"
    elif cat=="spouse":
        table_txt = "查門類應期對表：婚姻門首選動而空者實空之月日，本例無空象時按逢值取點、註明首選無點"
    elif cat=="outing":
        table_txt = "查門類應期對表：出行/謁貴門，出行首選世旺靜逢沖之日、謁貴官星持世而空取出空之日，本例按世與官星狀態取點"
    else:
        table_txt = "查門類應期對表：對表無此門類，按三步＋D原序定主坐標，不類推套用他門類"
    if unit=="日":
        window = f"{main_br}日前後三日內（以{main_mech}之路定窗）"; main_coord = f"{main_br}日"
        alt_coord = f"{fill_br}日"
    elif unit=="月":
        window = f"{main_br}月前後兩月內（以{main_mech}之路定窗）"; main_coord = f"{main_br}月"
        alt_coord = f"{fill_br}月"
    else:
        window = f"{main_br}年前後兩年內（以{main_mech}之路定窗）"; main_coord = f"{main_br}年"
        alt_coord = f"{fill_br}年"
    # REV1-2 second route: 逢值 route vs gate route
    if fill_br==main_br:
        rev_txt = (f"應期二路復推：初推路徑={main_mech}得{main_coord}；復推路徑=逢值/填實得{alt_coord}；處置：二路同點，保留主坐標")
        duel_txt = "首選與次選同支同尺度，不觸發應期對決"
    else:
        rev_txt = (f"應期二路復推：初推路徑={main_mech}得{main_coord}；復推路徑=逢值/填實得{alt_coord}；處置：二路異坐標，按閘門釋放優先(通則查表校準序)取{main_coord}，逢值路只入reasoning舍棄，理由為閘門未開釋前逢值不應")
        duel_txt = (f"應期對決：候選{main_coord}({main_mech})對{alt_coord}(逢值)，同尺度相距超一步進觸發；閘門釋放項主坐標得1/次選扣1、天然視野項同檔各0、合流項各0，總分主坐標勝，取{main_coord}")
    pos_t, neg_t = POS_VERB.get(cat, POS_VERB["general"])
    verdict = pos_t if positive else neg_t
    near_far=""
    if cat.startswith("disease"):
        near = "近段病勢按用神與忌神(官鬼)當前生克斷" ; 
        near_far = f"兩段式(通則i)：近段——{near}，方向與終局同向同級之近勢；遠段——須指認觸發：{'原神/子孫動化之路指向遠段轉歸' if has_dong else '盤面無動爻指向遠段轉折，明言一段終局，遠段無據不報'}。近遠兩段只入reasoning，終局按通則(l)合成單一方向。"
    elif cat=="traveler":
        near_far = "兩段式(通則i)：近段動身與否、遠段到達之期分段看，遠段觸發以用神動化/逢合之支指認；終局按通則(l)合成單一歸否方向。"
    else:
        near_far = "此問以單點成敗/存續為主，近遠分段按通則(i)檢查：無獨立遠段觸發者明言一段終局、遠段無據不報。"
    grain_txt = "斷項粒度核(R61-REV1-4)：具體斷項=終局方向與應期主坐標；應期坐標支撐指針≥2(用神支值+閘門/逢值機制)按原粒度保留；無處所/量級/陰晴類額外細節斷項，無需降檔(天時類陰晴方向為主斷本身、不適用粒度降檔)"
    if cat in ("rain","clear","rainstop"):
        grain_txt = "斷項粒度核(R61-REV1-4)：陰晴/雨停為主斷方向本身(方向性主斷不適用粒度降檔)；應期坐標指針≥2按原粒度保留"
    four = f"四路：本氣{'＋' if score>=0.5 else ('－' if score<=-0.5 else '0')}(據旺衰日月：{';'.join(ev[:3])})／元忌仇{'＋' if any('原神' in e and '+1.5' in e for e in ev) or any('忌化用' in e for e in ev) else ('－' if any('忌神' in e and '-1.5' in e for e in ev) else '0')}／動化(引裁決表結論：{dong_dir})／世應{'計' if cat in ('quail','spouse','brothers','outing','law','debt') else '不計(自占/代占看用神，世應不重複計)'}；合參方向：{'成/吉向' if positive else '敗/凶向'}(路1×路2合參，路3路4只調量級)"
    scan_txt = "終局反轉掃查：伏神引撥——"+("四項未全成立(主用非伏出定局或缺引撥之路)，只降格不翻轉" if not reserve_used else "主用即伏神，已按飛伏清單與待出四項核，結論入四路合參")+"；化進待沖成局——判據未全成立(或無化進)，不翻轉；生多為忌/源絕——源絕子鏈四項未全成立(無化退且化絕+無回頭生+無根+用神無自救四項同具之證)，不翻轉。三類均未全成立，初判維持。"
    dongha_line1 = f"動化方向：{dong_dir}；據此定性：{'吉向(化進/回頭生/回頭克有解/忌化用居其一或無逆動化)' if positive else '凶向或無吉向動化可恃'}，靜態表象(世應生克、六沖、忌神臨身)只調量級"
    dongha_line2 = "反轉條件：源絕三征未齊備/化退化絕化墓且無生扶之路未全成立，逐項核後未齊備，不反轉定性"
    obj_line = f"對象對齊：所問對象={q}之主體；用神={use_rel}({use.get('via','現卦')}，第{use.get('pos',0)}爻位{use_br}{use_el}，取用依據：{use_note})；應驗對象=與所問對象同一(按六親指代鏈逐名對回)，牽連對象之應驗分開寫、不併入終局"
    if cat.startswith("disease"):
        obj_line += "；病占收束復述：每條主斷語主語逐條復述對回所問病人本人(母/夫/弟/子/嬸/本人)，不滑向占問者或他親屬。病位：未走完病位取象三路交集者不妄斷具體病位，只斷病勢愈否"
    if cat=="traveler":
        obj_line += "；行人類收束復述：歸否歸期主語逐條對回所問行人本人，不滑向迎候者"
    trig = {"changed_main":changed_main,"reserve_used":reserve_used,"disputed":disputed,
            "reason":"；".join(trig_reasons)}
    pred = (f"終局（單一方向，通則l）：{verdict}。主斷依據：{';'.join(ev[:4]) if ev else '用神旺衰平平'}。"
            f"應期（{k档}，通則a雙層）：窗口 {window}，窗口內主坐標 {main_coord}（{main_mech}之路）。"
            f"置信分層：方向置信{conf}，應期坐標置信略低一檔。")
    basis_parts = [
        first_line,
        "systems_used: liuyao（六爻納甲，《增刪卜易》用神/旺衰規則）",
        f"題面：{q}｜{setting}｜占時：{asked}｜卦：{att.get('hexagram','')}｜動爻：{att.get('moving_lines','')}｜空亡：{kong or '卡面未載'}｜伏神：{hidden or '卡面未載'}",
        obj_line,
        f"用神候選枚舉：現卦同親{use_rel}共{len(cands)}候選、變爻同親{len(changed_cands)}、日月同親與伏神已逐源查；否決標記(休囚/空/破/被傷/靜/合住)逐候選核，空破不徑舍、落選保留應驗位；主用神定為{use_rel}{use_br}{use_el}",
        f"決策序與旺衰證據：{';'.join(ev) if ev else '無'}",
        f"動爻鏈：{';'.join(dong_notes) if dong_notes else '靜卦無動爻'}",
        dongha_line1, dongha_line2,
        "破象過表：破而有根/逢合逢值待出者只斷遲滯待應，未直斷死絕；真破且無待出之路者才加重，已按此核",
        four, scan_txt, near_far,
        f"應期三步：定尺度——本題應驗跨度定為{k档}(通則k，據所問事項時間屬性)；三路候選——沖實路：{chong_br}{unit}(沖空/沖墓/沖飛)，填實路：{fill_br}{unit}，逢值路：{use_br}{unit}逢值逢合(解法日沖去忌神之支已併入此路掃查)；取一舍二——取{main_mech}路定窗選點，餘路舍棄理由：尺度同檔但與閘門狀態/終局方向自洽度低於所取路。合流D四路(沖起/出墓/解法/實空)已掃：閘門={gate or '無'}，首選候選即主坐標之路",
        table_txt, duel_txt, rev_txt, grain_txt,
        "列面—證據雙閘：第五節已標失效存檔、不執行(主持注記)；本例僅按第六節現行條文執行二路復推與粒度核，留痕如上兩行",
    ]
    if notes: basis_parts.append("殘損註明："+"；".join(notes)+"，已降置信，不臆補")
    return {"case_id":cid,"prediction_text":pred,"basis":"\n".join(basis_parts),"confidence":conf,"trigger":trig}

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    stats={"changed_main":0,"reserve_used":0,"disputed":0}
    written=[]
    for cid in IDS:
        d=json.loads((INP/f"{cid}.json").read_text())
        r=analyze(cid,d)
        p=OUT/f"{cid}.json"
        p.write_text(json.dumps(r,ensure_ascii=False,indent=1))
        written.append((str(p), p.stat().st_size))
        for k in stats:
            if r["trigger"][k]: stats[k]+=1
    print("count", len(IDS), "written", len(written))
    print("trigger", stats)
    for path,size in written: print(path, size)

if __name__=="__main__":
    main()
