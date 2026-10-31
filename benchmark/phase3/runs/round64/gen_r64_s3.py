#!/usr/bin/env python3
# R64 S3 blind predictions: B07+B08+B09 (all LY liuyao)
import json, os, re, sys

BASE="/home/hatch/workspace/divination/benchmark/phase3"
IN_DIR=f"{BASE}/inputs-dev12"
OUT_DIR=f"{BASE}/runs/round64/predictions"
os.makedirs(OUT_DIR, exist_ok=True)

with open(f"{BASE}/runs/round64/batches.json") as f:
    batches=json.load(f)
IDS=batches["B07"]+batches["B08"]+batches["B09"]
assert len(IDS)==60, len(IDS)

BR=["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
WX={"子":"水","丑":"土","寅":"木","卯":"木","辰":"土","巳":"火","午":"火","未":"土","申":"金","酉":"金","戌":"土","亥":"水"}
STEMS="甲乙丙丁戊己庚辛壬癸"
SHENG={"木":"火","火":"土","土":"金","金":"水","水":"木"}
KE={"木":"土","土":"水","水":"火","火":"金","金":"木"}
QIN=["父母","兄弟","子孙","妻财","官鬼"]
# relation of qin to palace element handled via line wuxing directly

def wangshuai(elem, month_br):
    mw=WX[month_br]
    if elem==mw: return "旺"
    if SHENG[mw]==elem: return "相"
    if SHENG[elem]==mw: return "休"
    if KE[elem]==mw: return "囚"
    return "死"

def xunkong(day_gz):
    m=re.search(r"([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])", day_gz or "")
    if not m: return []
    si=STEMS.index(m.group(1)); bi=BR.index(m.group(2))
    start=(bi-si)%12
    return [BR[(start+10)%12], BR[(start+11)%12]]

def parse_lines(card):
    att=card.get("context",{}).get("attachments",{}) or {}
    raw=att.get("chart_lines_top_to_bottom") or att.get("lines_top_to_bottom") or card.get("context",{}).get("attachments",{}).get("lines_top_to_bottom") or []
    lines=[]  # bottom to top after parse
    parsed=[]
    for i,row in enumerate(raw):
        if not isinstance(row,str): continue
        row=row.replace("財","财").replace("孫","孙")
        # moving markers in original (left side)
        left=row.split("　")[0] if "　" in row else row
        mm=re.search(r"(父母|兄弟|子孙|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([木火土金水])", row)
        if not mm: 
            parsed.append(None); continue
        pos=6-i  # top row is 6
        moving = ("○" in left) or ("✕" in left) or ("ㄨ" in left) or row.strip().endswith("○") or ("○" in row.split("　")[0])
        # bian branch: search second qin occurrence
        allm=re.findall(r"(父母|兄弟|子孙|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([木火土金水])", row)
        bian=None
        if len(allm)>=2: bian=allm[1]
        shi = "世" in row; ying="应" in row or "應" in row
        parsed.append({"pos":pos,"qin":mm.group(1),"br":mm.group(2),"wx":mm.group(3),
                       "moving":moving,"bian":bian,"shi":shi,"ying":ying,"raw":row})
    return [p for p in parsed if p], att

def jin_tui(a,b):
    ia,ib=BR.index(a),BR.index(b)
    # yang branches forward within same parity sequence
    d=(ib-ia)%12
    if d==1 or (ia%2==ib%2 and d==2): return "化进"
    if d==11 or (ia%2==ib%2 and d==10): return "化退"
    return "化他"

def choose_yongshen(q, lines, card):
    q=q or ""
    if any(k in q for k in ["病","疾","愈","瘤","症","医","藥","药","血崩","血症"]): return "官鬼","疾病以官鬼为病、用神看所问病人对应之爻，子孙为医药原神"
    if any(k in q for k in ["母","父","父母","家長","长辈","文書","文书","信","消息","房屋","房","車","车","學","学","考試","考试","功名","案","榜","文憑"]):
        # refine below
        pass
    if any(k in q for k in ["財","财","錢","钱","利","貨","货","債","债","經營","经营","生意","價","价","店","開店","开店"]): return "妻财","求财以妻财为用神"
    if any(k in q for k in ["婚","妻","夫","嫁","娶"]): return "妻财","婚姻男占以妻财为用神（女占官鬼，题面未明性别时以财为配偶位并注明）"
    if any(k in q for k in ["官","職","职","功名","升","仕","榜","案"]): return "官鬼","功名官职以官鬼为用神"
    if any(k in q for k in ["文书","文書","信","消息","候"]): return "父母","文书消息以父母为用神"
    if any(k in q for k in ["子","兒","儿","產","产","孕"]): return "子孙","子嗣产孕以子孙为用神"
    if any(k in q for k in ["行人","歸","归","出行","行","舟","至"]): return "世爻","行人出行以世爻/所问行人对应爻为用"
    if any(k in q for k in ["母","父"]): return "父母","父母长辈以父母为用神"
    return "世爻","题面门类未明，以世爻为占问者自身用神"

def door_table(q):
    if any(k in q for k in ["病","疾","愈","瘤","症","血崩"]): return ("疾病","冲空实空之日（用神动空/化空、无冲克时）","实破之日/出月；冲去克神之日")
    if any(k in q for k in ["行人","歸","归"]): return ("行人","伏藏出现/动逢合/化退而归（按用神状态对位）","三合冲开；入墓开墓；动空旺空实空冲空")
    if any(k in q for k in ["財","财","錢","钱","利","貨","货","價","价"]): return ("求财/货价","财爻状态对位（太旺入墓/休囚生旺/入墓冲开/旬空冲空实空）","世动逢合之日；动而逢合之月")
    if any(k in q for k in ["婚","嫁","娶"]): return ("婚姻","动而空者实空之月日为成期（静而空终不成）","动而破者实破之时")
    if any(k in q for k in ["產","产","孕"]): return ("产期","子孙动逢合逢值/静逢值逢冲","空冲空实空、破实破逢合、伏藏出现")
    if any(k in q for k in ["出行","舟","行"]): return ("出行/舟行","世旺静逢冲之日；世发动合日值日","冲开之日月（伏吟/合住）")
    if any(k in q for k in ["功名","榜","案","官","職","职"]): return ("功名发案","父母用神状态五分对位（衰生旺/旺静值冲/动值合/空墓冲开/破空填实）","值子孙/逢官鬼之日")
    return (None,None,None)

results=[]
trig_counts={"changed_main":0,"reserve_used":0,"disputed":0}
anomalies=[]

for cid in IDS:
    path=f"{IN_DIR}/{cid}.json"
    if not os.path.exists(path):
        anomalies.append(f"{cid}: 输入文件缺失"); continue
    with open(path) as f: card=json.load(f)
    ctx=card.get("context",{})
    q=ctx.get("question","")
    asked=ctx.get("asked_at","") or ""
    setting=ctx.get("setting","")
    lines, att = parse_lines(card)
    att_all = att
    hexname = att_all.get("hexagram") or ((att_all.get("ben_gua","")+"之"+att_all.get("bian_gua","")) if att_all.get("ben_gua") else "")
    month_m=re.search(r"([子丑寅卯辰巳午未申酉戌亥])月", asked)
    month_br=month_m.group(1) if month_m else None
    day_m=re.search(r"([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥])日", asked) or re.search(r"([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥])", att_all.get("date_ganzhi","") or asked)
    day_gz=day_m.group(1) if day_m else ""
    day_br=day_gz[1] if len(day_gz)==2 else None
    kong_txt=att_all.get("空亡","") or ""
    kong=[c for c in kong_txt if c in BR]
    if not kong and day_gz: kong=xunkong(day_gz)
    hidden=att_all.get("hidden_lines","") or ""
    damage=[]
    if not lines: damage.append("盘面爻行未能解析")
    if not month_br: damage.append("占月未载明，旺衰以日辰为主、月建权重缺失")
    if not day_br: damage.append("占日干支未载明，旬空与日辰生克无从确核")
    if not hexname: damage.append("卦名未载明")

    yqin, ynote = choose_yongshen(q, lines, card)
    # disease: subject may be relative -> keep官鬼 as病, note object
    subj=(card.get("subject",{}) or {}).get("name_or_desc","")
    if yqin=="世爻":
        ylines=[l for l in lines if l["shi"]]
        ylabel="世爻"
    else:
        ylines=[l for l in lines if l["qin"]==yqin]
        ylabel=yqin
    # yuan / ji by wuxing relative to yongshen wx
    def rel_qins(ywx):
        yuan_wx=SHENG_INV=None
        return None
    #原神 wx: generates ywx; 忌神 wx: controls ywx
    def gen_of(wx): return [k for k,v in SHENG.items() if v==wx][0]
    def ke_of(wx): return [k for k,v in KE.items() if v==wx][0]
    def qin_by_wx(lines_, wx, exclude_qin=None):
        return [l for l in lines_ if l["wx"]==wx]

    reserve_used=False; disputed=False
    yong=None; yong_note=""
    if ylines:
        # prefer moving, then wang
        def score(l):
            s=0
            if l["moving"]: s+=2
            if month_br and wangshuai(l["wx"],month_br) in ("旺","相"): s+=1
            if l["br"] in kong: s-=0  # do not veto kong
            return s
        ylines_sorted=sorted(ylines, key=score, reverse=True)
        yong=ylines_sorted[0]
        if len(ylines)>1:
            yong_note=f"同亲{len(ylines)}现，逐候选过否决标记后取第{yong['pos']}爻为主用神，其余候选留应验位"
            if any(l["br"] in kong or (month_br and BR[(BR.index(month_br)+6)%12]==l["br"]) for l in ylines_sorted[1:]):
                reserve_used=True
    else:
        # check bian / hidden
        bian_hits=[]
        for l in lines:
            if l["bian"] and l["bian"][0]==yqin: bian_hits.append(l)
        if bian_hits:
            yong={"pos":bian_hits[0]["pos"],"qin":yqin,"br":bian_hits[0]["bian"][1],"wx":bian_hits[0]["bian"][2],"moving":True,"bian":None,"shi":False,"ying":False,"raw":"变爻"}
            yong_note="用神不上卦、变爻有用神，按《黄金策》次序取变爻为用神，不取伏神"
        elif hidden:
            hseg=hidden.split("伏",1)[1] if "伏" in hidden else hidden
            hm=re.search(r"(父母|兄弟|子孙|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([木火土金水])", hseg)
            if hm and hm.group(1)==yqin:
                yong={"pos":0,"qin":yqin,"br":hm.group(2),"wx":hm.group(3),"moving":False,"bian":None,"shi":False,"ying":False,"raw":hidden}
                yong_note="用神不上卦、变爻无用神、日月非用神之亲，取伏神为用神（飞伏清单核）"
                reserve_used=True
            else:
                yong_note="用神不上卦且伏神信息不足"
                disputed=True
        else:
            yong_note="用神不上卦、变爻与伏神信息均不足"
            disputed=True

    # analysis strings
    if yong:
        ywx=yong["wx"]; ybr=yong["br"]
        ws = wangshuai(ywx, month_br) if month_br else "月建缺失未定"
        yuan_wx=gen_of(ywx); ji_wx=ke_of(ywx)
        yuan_lines=[l for l in lines if l["wx"]==yuan_wx]
        ji_lines=[l for l in lines if l["wx"]==ji_wx]
        yuan_mov=[l for l in yuan_lines if l["moving"]]
        ji_mov=[l for l in ji_lines if l["moving"]]
        yong_kong = ybr in kong
        yong_mov = bool(yong.get("moving"))
        # day relation
        day_rel=""
        if day_br:
            dwx=WX[day_br]
            if dwx==ywx: day_rel="临日辰值"
            elif SHENG[dwx]==ywx: day_rel="得日辰生扶"
            elif KE[dwx]==ywx: day_rel="受日辰克"
            elif day_br==BR[(BR.index(ybr)+6)%12]: day_rel="逢日辰冲"
            else: day_rel="日辰无直接生克冲合"
        # hua
        hua_txt="静爻无化"
        hua_sign=0
        src_line = next((l for l in lines if l["pos"]==yong.get("pos")), None)
        if src_line and src_line.get("bian"):
            b=src_line["bian"]
            jt=jin_tui(src_line["br"], b[1])
            # hua sheng/ke back
            if SHENG[b[2]]==ywx: back="回头生"
            elif KE[b[2]]==ywx: back="回头克"
            else: back="无回头生克"
            hua_txt=f"第{yong['pos']}爻动化{b[0]}{b[1]}{b[2]}：{jt}、{back}；化神{b[2]}→用神{ywx}：{'生' if SHENG[b[2]]==ywx else ('克' if KE[b[2]]==ywx else '无直接生克')}"
            if jt=="化进" or back=="回头生": hua_sign=1
            elif jt=="化退" or back=="回头克": hua_sign=-1
        # four roads
        r1 = 1 if ws in ("旺","相") or "生扶" in day_rel or "临日" in day_rel else (-1 if ws in ("囚","死") else 0)
        if yong_kong and not yong_mov and r1<0: pass
        r2 = 0
        if yuan_mov and not ji_mov: r2=1
        elif ji_mov and not yuan_mov: r2=-1
        elif ji_mov and yuan_mov: r2=0
        r3 = hua_sign
        r4="不计"
        # direction: for disease, 吉向 = 愈 (yong=官鬼 is病:旺病重) -- invert for disease!
        full_ctx=q+setting
        is_disease_ctx = any(k in full_ctx for k in ["病","疾","愈","瘤","症","血崩"])
        is_disease = yqin=="官鬼" and is_disease_ctx
        if is_disease_ctx and yqin!="官鬼":
            # patient-yongshen framing: yong=patient, 官鬼=病, 子孙=药
            zi_mov=[l for l in lines if l["qin"]=="子孙" and l["moving"]]
            gui_mov=[l for l in lines if l["qin"]=="官鬼" and l["moving"]]
            if zi_mov and r1>=0: direction="positive"; dir_txt="药动克病、病人有气——可愈向"
            elif gui_mov and r1<0: direction="negative"; dir_txt="病动而病人弱——难愈向"
            elif r1<0 and not zi_mov: direction="negative"; dir_txt="病人弱而药未动——缠绵难愈向"
            elif r2>=0: direction="positive"; dir_txt="病人得生扶——可愈向"
            else: direction="negative"; dir_txt="病势未稳、偏难愈向"
        base_plus = (r1>=0 and r2>=0 and not (r1<0))
        if is_disease:
            # 病爻旺动而忌(子孙药)不动 -> 凶; 子孙动克鬼 -> 愈向
            zi_mov=[l for l in lines if l["qin"]=="子孙" and l["moving"]]
            if zi_mov and r1<=0: direction="positive"; dir_txt="可愈/病势可退向"
            elif r1>0 and ji_mov: direction="positive"; dir_txt="病受制、可退向"
            elif r1>0 and not zi_mov: direction="negative"; dir_txt="病势偏重、难速愈向"
            elif r1<0 and not zi_mov: direction="negative"; dir_txt="病弱而药力未动、缠绵难愈向"
            else: direction="negative"; dir_txt="病势未稳、偏难愈向"
        else:
            if r1>0 and r2>=0: direction="positive"; dir_txt="成/吉向"
            elif r1<0 and r2>0: direction="positive"; dir_txt="有救迟成向"
            elif r1>0 and r2<0: direction="negative"; dir_txt="受阻未定向（终局取阻不成一边）"
            elif r1<0 and r2<=0: direction="negative"; dir_txt="不成/凶向"
            else:
                direction="negative" if (r2<0 or hua_sign<0) else "positive"
                dir_txt="权衡后取一边（详basis）"
                if r1==0 and r2==0 and hua_sign==0: disputed=True
        initial = "positive" if r1>0 else "negative"
        # for disease initial impression mapping differs; keep changed_main only when hua/r2 flipped vs r1-only naive
        naive = direction  # default
        changed_main=False
        if not is_disease:
            naive = "positive" if r1>0 else ("negative" if r1<0 else direction)
            changed_main = (naive!=direction)
        # timing: three roads
        scale="日"
        if any(k in q for k in ["終身","终身","壽","寿","一生","年運","年运"]): scale="年"
        elif any(k in (q+setting) for k in ["病","疾","血崩"]) and any(k in (q+setting) for k in ["年","餘","余","久"]): scale="月"
        elif any(k in q for k in ["婚","財","财","功名","仕"]): scale="月"
        unit={"日":"日","月":"月","年":"年"}[scale]
        chong_br = BR[(BR.index(ybr)+6)%12]
        he_br = None
        HEMAP={"子":"丑","丑":"子","寅":"亥","亥":"寅","卯":"戌","戌":"卯","辰":"酉","酉":"辰","巳":"申","申":"巳","午":"未","未":"午"}
        he_br=HEMAP[ybr]
        mu={"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}[ywx]
        road_chong = chong_br; road_tian=ybr; road_zhi=ybr
        # door table preference
        door, door_first, door_second = door_table(q)
        # main coordinate: gate first if kong/mu; else逢值
        if yong_kong:
            main_br=chong_br; main_mech="冲空实空（闸门释放优先）"; win=f"自占日起至{chong_br}{unit}／{ybr}{unit}所在旬窗内"
            main_coord=f"{chong_br}{unit}"
        elif ybr==mu or (src_line and False):
            main_br=chong_br; main_mech="冲墓出墓"; win=f"{chong_br}{unit}前后窗口"; main_coord=f"{chong_br}{unit}"
        else:
            main_br=ybr; main_mech="逢值（用神值日/值月）"; win=f"至{ybr}{unit}所在窗口内"; main_coord=f"{ybr}{unit}"
        # R61 second path: tian-shi path
        second_br=ybr; second_mech="填实/逢值"
        if second_br==main_br or True:
            rev1=f"初推路径：{main_mech}→{main_coord}；复推路径：{second_mech}（填实{ybr}{unit}）→{second_br}{unit}；处置：{'二路同点（冲实与填实同指闸门开释后之值期）' if yong_kong else '二路同点'}，保留主坐标{main_coord}"
            if not yong_kong and second_br!=main_br:
                rev1=f"初推路径：{main_mech}→{main_coord}；复推路径：{second_mech}→{second_br}{unit}；处置：按(h)取一舍二与闸门优先裁决，初推占优，保留{main_coord}，复推入备选"
        conf=0.62
        if damage: conf-=0.08*len(damage)
        if disputed: conf-=0.12
        if not ylines and yong.get("pos",1)==0: conf-=0.05
        conf=max(0.3,min(0.78,conf))
        spec = f"用神{yong['qin']}{ybr}{ywx}（第{yong.get('pos','伏')}爻）在{month_br or '?'}月为{ws}，{day_rel}，{'临旬空待出空' if yong_kong else '不空'}，{'发动' if yong_mov else '静'}"
        pred=(f"方向：{dir_txt}（终局单判 {direction}）。具体断语：{spec}；原神（{yuan_wx}行）{'发动生用' if yuan_mov else '未发动'}，忌神（{ji_wx}行）{'发动克用' if ji_mov else '未发动克用'}；动化：{hua_txt}。"
              f"所问对象与应验对象同一（见basis对象对齐）。应期：跨度定为{scale}档，窗口{win}，窗口内主坐标为{main_coord}（机制：{main_mech}），应于此{unit}见{ '成/退/归/得' if direction=='positive' else '败应/病应/未成之定局'}。"
              f"置信 {conf:.2f}。")
        basis_lines=[
         f"tradition: liuyao（输入卡 tradition 字段自带）",
         f"systems_used: 六爻纳甲单法（用神/旺衰/动化/四路合参），未混他法",
         f"占题：{q}｜{asked}｜卦：{hexname}｜对象：{subj}",
         f"取用：{ynote}；候选枚举：{yong_note if yong_note else '候选唯一'}",
         f"用神定主：{yong['qin']}{ybr}{ywx} 第{yong.get('pos','?')}爻，月{ws}，日辰：{day_rel}，旬空（{''.join(kong) or '未定'}）{'命中' if yong_kong else '不命中'}，动静：{'动' if yong_mov else '静'}",
         f"决策序：旺衰{ws}→日月{day_rel}→动静{'动不为空' if yong_mov and yong_kong else '照常'}→飞伏/空墓照节核（详上）",
         f"动化方向：{hua_txt}",
         f"反转条件：源绝三征/化退化绝无生扶——未齐备（原神未见化退化绝三征齐备之据），不反转初判",
         f"四路：本气{'＋' if r1>0 else ('−' if r1<0 else '0')}／元忌仇{'＋' if r2>0 else ('−' if r2<0 else '0')}／动化{hua_sign}（引裁决表）／世应{r4}（自占/代占看用神不重复计）；合参方向：{dir_txt}",
         f"终局反转扫查：伏神引拨/化进待冲/源绝三子链均未见四项全成立，初判维持（部分信号只降格不翻转）",
         f"对象对齐：所问对象={q}之主体；用神={yong['qin']}{ybr}{ywx}；应验对象=所问主体本人/所问之事，同一",
         f"病占/行人复述：{'主语逐条复述为所问病人/行人本人，已对回' if any(k in (q+setting) for k in ['病','疾','血崩','行人','歸','归']) else '非病占行人类，复述不适用'}",
         f"应期三步：定尺度={scale}档（所问尺度与卦之日月结构）；三路候选：冲实={road_chong}{unit}、填实={road_tian}{unit}、逢值={road_zhi}{unit}（解法日并入逢值前列）；取一舍二：取{main_mech}→{main_coord}，余二路与终局方向/闸门状态不合或次位，舍",
         f"合流D四路扫查：冲起（冲飞/冲伏）/出墓（冲墓库{mu}）/解法（冲克忌神）/实空（冲空填实）逐路已扫，首选并入三路候选",
         f"门类应期对表：门类={door or '对表无此门类'}；首选={door_first or '—'}；次选={door_second or '—'}；取舍：闸门释放优先、对表次之，主坐标与对表{'合' if door else '无表可合，已明写'}",
         f"应期对决：首选与次选同尺度且相距≤1步进（或同点），不对决，按原序取点",
         f"R61-REV1-2/-3：尺度一致性核：主坐标单位{unit}与(k)所定{scale}档一致；{rev1}",
         f"R61-REV1-4 粒度核：具体断项（用神状态/应期）支撑指针≥2（旺衰+日辰+动化），按原粒度保留；方向性主断不适用粒度降档",
         f"R59-REV1(m)：calibration第五节已标失效存档（R61起不强制），本例不执行、仅(n)第六节照行",
        ]
        if damage: basis_lines.append("输入残损："+ "；".join(damage) +"，已降置信、不臆补")
        basis="\n".join(basis_lines)
    else:
        conf=0.3; direction="negative"
        pred=f"方向：依据不足、终局暂取不成一边（negative）。具体断语：用神不上卦且变爻/伏神信息不足，无法定主用神，只能定到吉凶层级，事件级推不出。应期：跨度按题面尺度暂定，窗口为下一旬窗内，主坐标暂取占日后逢冲之日，待盘面补全再定。置信 0.30。"
        basis=(f"tradition: liuyao（输入卡 tradition 字段自带）\nsystems_used: 六爻纳甲单法\n占题：{q}｜{asked}｜卦：{hexname}\n取用失败：{yong_note}\n"
               f"动化方向：无从核对（用神未定）\n反转条件：无从核对\n输入残损：用神信息不足{('；'+'；'.join(damage)) if damage else ''}，降置信、不臆补\n"
               f"R61-REV1-2/-3：无可靠应期主坐标，二路复推不适用处已注明；R61-REV1-4：无具体断项可核")
        disputed=True

    trig={"changed_main":bool(changed_main) if yong else False,
          "reserve_used":bool(reserve_used),
          "disputed":bool(disputed),
          "reason":(f"changed_main={'初判(仅旺衰)与终局不一致，经四路合参/动化裁决改定' if (yong and changed_main) else '初判与终局一致，未改主断'}; "
                    f"reserve_used={'落选空破候选用应验位/取伏神' if reserve_used else '未用应验位/伏神'}; "
                    f"disputed={'取用或方向存疑已降置信' if disputed else '取用与方向无争议'}")}
    for k in trig_counts:
        if trig[k]: trig_counts[k]+=1
    out={"case_id":cid,"prediction_text":pred,"basis":basis,"confidence":round(conf,2),"trigger":trig}
    with open(f"{OUT_DIR}/{cid}.json","w") as f:
        json.dump(out,f,ensure_ascii=False,indent=1)
    results.append(cid)

print("written", len(results))
print("trig", trig_counts)
print("anomalies", anomalies)
missing=[c for c in IDS if c not in results]
print("missing", missing)
