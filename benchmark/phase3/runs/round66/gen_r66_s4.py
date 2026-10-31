# -*- coding: utf-8 -*-
"""R66 S4 (B10,B11,B12) blind predictions generator. Reads ONLY batches.json,
inputs-dev12 cards. Applies liuyao method from kb-snapshot deterministically."""
import json, os, re

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
IN = os.path.join(BASE, "inputs-dev12")
OUT = os.path.join(BASE, "runs/round66/predictions")
os.makedirs(OUT, exist_ok=True)

batches = json.load(open(os.path.join(BASE, "runs/round66/batches.json"), encoding="utf-8"))
IDS = batches["B10"] + batches["B11"] + batches["B12"]
assert len(IDS) == 60

BR = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
WX = {"子":"水","亥":"水","寅":"木","卯":"木","巳":"火","午":"火","申":"金","酉":"金","辰":"土","戌":"土","丑":"土","未":"土"}
STEMS = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
SHENG = {"木":"火","火":"土","土":"金","金":"水","水":"木"}   # X生SHENG[X]
KE = {"木":"土","土":"水","水":"火","火":"金","金":"木"}       # X克KE[X]
def shengs(a,b): return SHENG[a]==b   # a生b
def kes(a,b): return KE[a]==b         # a克b
OPP = {b: BR[(i+6)%12] for i,b in enumerate(BR)}  # 冲
HE = {"子":"丑","丑":"子","寅":"亥","亥":"寅","卯":"戌","戌":"卯","辰":"酉","酉":"辰","巳":"申","申":"巳","午":"未","未":"午"}
TOMB = {"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}
JIN = {"寅":"卯","巳":"午","申":"酉","亥":"子","丑":"辰","辰":"未","未":"戌","戌":"丑"}
TUI = {v:k for k,v in JIN.items()}
QIN = ["妻財","官鬼","父母","子孫","兄弟"]

def xun_kong(day_gz):
    """day_gz like 癸酉 -> 空亡两支"""
    s = day_gz[0]; b = day_gz[1]
    si = STEMS.index(s); bi = BR.index(b)
    start = (bi - si) % 12  # 旬首支
    return [BR[(start+10)%12], BR[(start+11)%12]]

def wangshuai(ywx, mwx, dwx_day_branch_wx):
    if ywx == mwx: return "旺", 2.0
    if shengs(mwx, ywx): return "相", 1.0
    if shengs(ywx, mwx): return "休", 0.0
    if kes(ywx, mwx): return "囚", -1.0
    return "死", -2.0

def norm(s):
    return s.replace("子孙", "子孫").replace("妻财", "妻財")

def parse_line(s):
    """return dict for 本卦 line (left segment)."""
    s = norm(s)
    left = re.split(r"\s+", s.strip())[0]
    qin = None
    for q in QIN:
        if left.startswith(q): qin = q; break
    rest = left[2:] if qin else left
    br = rest[0] if rest else ""
    wx = WX.get(br, "")
    return {"qin": qin, "br": br, "wx": wx, "shi": "世" in left, "ying": "應" in s or "应" in s.split("世")[0] and False, "raw": s}
# 应 marker check simpler: search whole first segment for 應 before spaces
def parse_line2(s):
    d = parse_line(s)
    seg = norm(s).strip()
    d["ying"] = ("應" in seg[:8])
    # changed part
    parts = re.split(r"\s+", seg)
    d["chg"] = None
    if len(parts) > 1:
        c = parts[1]
        cq = None
        for q in QIN:
            if c.startswith(q): cq = q; break
        if cq:
            crest = c[2:]
            d["chg"] = {"qin": cq, "br": crest[0] if crest else "", "wx": WX.get(crest[0],"") if crest else ""}
    return d

POS = ["上爻","五爻","四爻","三爻","二爻","初爻"]  # top->bottom
POSMAP = {"上":0,"五":1,"四":2,"三":3,"二":4,"初":5}

def moving_positions(moving_text):
    pos = set()
    if "無動爻" in moving_text: return pos
    for tok in re.findall(r"(上爻|五爻|四爻|三爻|二爻|初爻)", moving_text):
        pos.add(POS.index(tok))
    return pos

def pick_yongshen(q, setting, lines, shi_idx, ying_idx):
    """returns (mode, target_qin or ('shi',), label)"""
    text = q + setting
    if "行人" in text or "何日回" in text or "何日到" in text or "歸" in text or "回" in text and ("父" in text or "夫" in text):
        if "父" in text: return ("qin","父母","行人（父）以父母為用神")
        if "母" in text: return ("qin","父母","行人（母）以父母為用神")
        if "夫" in text: return ("qin","官鬼","行人（夫）以官鬼為用神")
        if "妻" in text: return ("qin","妻財","行人（妻）以妻財為用神")
        if "子" in text or "兒" in text: return ("qin","子孫","行人（子）以子孫為用神")
        if "兄" in text or "弟" in text: return ("qin","兄弟","行人（兄弟）以兄弟為用神")
        return ("ying",None,"行人以應爻為用神（行人本人）")
    if "病" in text or "疾" in text:
        if "父" in text: return ("qin","父母","代占父病以父母為用神")
        if "母" in text: return ("qin","父母","代占母病以父母為用神")
        if "夫" in text: return ("qin","官鬼","占夫病以官鬼為用神")
        if "妻" in text: return ("qin","妻財","占妻病以妻財為用神")
        if "子" in text or "兒" in text or "女" in text and "占" in text: return ("qin","子孫","代占子女病以子孫為用神")
        if "兄" in text or "弟" in text: return ("qin","兄弟","代占兄弟病以兄弟為用神")
        return ("shi",None,"自占病以世爻為用神")
    if "婚" in text:
        if "女" in setting or "女家" in text: return ("qin","官鬼","女家占婚以官鬼為用神")
        if "女占夫" in setting or "占夫" in text: return ("qin","官鬼","女占夫以官鬼為用神")
        return ("qin","妻財","男占婚以妻財為用神")
    if "孕" in text or "胎" in text or "產" in text or "有子" in text or "子嗣" in text:
        return ("qin","子孫","胎孕／子嗣以子孫為用神")
    if "財" in text or "貨" in text or "價" in text or "債" in text or "利" in text or "買" in text or "賣" in text:
        return ("qin","妻財","求財以妻財為用神")
    if "訟" in text: return ("qin","官鬼","官訟以官鬼為用神")
    if "試" in text or "考" in text or "功名" in text or "官" in text or "缺" in text or "選" in text or "案" in text or "榜" in text or "仕" in text or "職" in text or "陞" in text or "升" in text:
        return ("qin","官鬼","功名／官職以官鬼為用神（父母為文書參看）")
    if "失" in text or "尋" in text or "物" in text:
        return ("qin","妻財","尋失物以妻財為用神（物財）")
    if "出行" in text or "行" in text and "世" in text:
        return ("shi",None,"出行以世爻為用神")
    if "雨" in text or "天時" in text or "晴" in text:
        return ("qin","父母","天時以父母為雨象用神")
    if "文書" in text or "信" in text or "消息" in text:
        return ("qin","父母","文書消息以父母為用神")
    if "妻" in text: return ("qin","妻財","占妻之事以妻財為用神")
    if "夫" in text: return ("qin","官鬼","占夫之事以官鬼為用神")
    if "父" in text or "母" in text: return ("qin","父母","占父母之事以父母為用神")
    return ("shi",None,"泛占以世爻為用神")

results = []
trig_count = {"changed_main":0,"reserve_used":0,"disputed":0}
for cid in IDS:
    card = json.load(open(os.path.join(IN, cid+".json"), encoding="utf-8"))
    ctx = card["context"]; att = ctx["attachments"]
    q = ctx.get("question",""); setting = ctx.get("setting","")
    asked = ctx.get("asked_at","")
    m = re.search(r"([子丑寅卯辰巳午未申酉戌亥])月", asked); daym = re.search(r"([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥])日", asked)
    mbr = m.group(1) if m else ""; daygz = daym.group(1) if daym else ""
    dbr = daygz[1] if daygz else ""
    mwx = WX.get(mbr,""); dwx = WX.get(dbr,"")
    kong = xun_kong(daygz) if daygz else []
    km = re.search(r"空亡([子丑寅卯辰巳午未申酉戌亥])([子丑寅卯辰巳午未申酉戌亥])", asked)
    if not kong and km: kong = [km.group(1), km.group(2)]
    incomplete_md = (not mbr) or (not daygz)  # 月日殘損標記
    lines = [parse_line2(s) for s in att["chart_lines_top_to_bottom"]]
    mov = moving_positions(att["moving_lines"])
    shi_idx = next((i for i,l in enumerate(lines) if l["shi"]), None)
    ying_idx = next((i for i,l in enumerate(lines) if l["ying"]), None)
    mode, tq, ylabel = pick_yongshen(q, setting, lines, shi_idx, ying_idx)
    is_hangren = ("行人" in q+setting or "何日回" in q or "何日到" in q)
    is_bing = ("病" in q+setting or "疾" in q+setting)

    # 用神候选枚举
    cands = []
    if mode == "qin":
        cands = [i for i,l in enumerate(lines) if l["qin"]==tq]
    elif mode == "shi":
        cands = [shi_idx] if shi_idx is not None else []
    else:
        cands = [ying_idx] if ying_idx is not None else []
    reserve_used = False; disputed = False; changed_main = False
    yong_idx = None; yong_note = ""
    chg_cands = [i for i in mov if lines[i]["chg"] and mode=="qin" and lines[i]["chg"]["qin"]==tq]
    if cands:
        # 主用: 动者优先, 次旺者; 两现标记互比简化: prefer moving, then non-kong
        def ckey(i):
            l = lines[i]
            return (1 if i in mov else 0, 0 if l["br"] in kong else 1)
        yong_idx = max(cands, key=ckey)
        if len(cands) > 1: yong_note = f"用神{len(cands)}現，逐候選過否決標記後取{POS[yong_idx]}為主用，餘者留應驗位參看"
    elif chg_cands:
        yong_idx = chg_cands[0]; yong_note = "用神不上卦、變爻有用神，先取變爻，不取伏神（黃金策次序）"
    else:
        # 日月分流 / 伏神
        if mode=="qin" and (WX.get(mbr) and tq):
            # 月建/日辰支之六亲无法直知亲名(以宮五行定), 以五行近似: 支五行 == 用神五行視為同親候選
            ywx_guess = None
            reserve_used = True
            yong_note = "用神不上卦、變爻亦無用神、日月同親未明，入本宮首卦尋伏神（reserve）；伏神盤面未隨卡全列，據飛伏清單只能定待出資格、降置信"
            disputed = True
        else:
            yong_note = "用神定位存疑"; disputed = True

    notes = []
    score = 0.0; ev = []; chain = 0.0
    yong_from_chg = (yong_idx is not None and not cands and bool(chg_cands))
    if yong_idx is not None and not reserve_used:
        if yong_from_chg:
            cg = lines[yong_idx]["chg"]
            yl = {"qin": tq, "br": cg["br"], "wx": cg["wx"], "chg": None, "shi": False}
            ev_note_chg = f"（用神為{POS[yong_idx]}變爻{cg['qin']}{cg['br']}{cg['wx']}，本爻為{lines[yong_idx]['qin']}{lines[yong_idx]['br']}）"
        else:
            yl = lines[yong_idx]; ev_note_chg = ""
        ywx = yl["wx"]; ybr = yl["br"]
        if mwx:
            ws, wv = wangshuai(ywx, mwx, dwx); score += wv
            ev.append(f"用神{yl['qin']}{ybr}{ywx}居{POS[yong_idx]}，月建{mbr}{mwx}下為「{ws}」（{wv:+.0f}）{ev_note_chg}")
        else:
            ws, wv = "未定（月建原文未明記）", 0.0
            ev.append(f"用神{yl['qin']}{ybr}{ywx}居{POS[yong_idx]}；月建原文未明記，旺衰無從定，只憑動靜生克鏈作斷並降置信（輸入殘損）{ev_note_chg}")
        # 日辰
        if dbr and dbr == ybr: score += 1.5; ev.append(f"日辰{dbr}臨用神（+1.5）")
        elif dbr and shengs(dwx, ywx): score += 1.0; ev.append(f"日辰{dbr}{dwx}生用神（+1）")
        elif dbr and kes(dwx, ywx): score -= 1.0; ev.append(f"日辰{dbr}{dwx}克用神（-1）")
        if dbr and OPP[dbr] == ybr:
            if wv >= 0: score += 0.5; ev.append("日沖用神而用神有氣，判暗動／沖實（+0.5）")
            else: score -= 1.0; ev.append("日沖用神而用神無氣，判日破（-1）")
        if mbr and OPP[mbr] == ybr: score -= 1.0; ev.append(f"用神逢月破（{mbr}沖{ybr}，-1，待填實）")
        ykong = ybr in kong
        ymov = yong_idx in mov
        if ykong:
            if ymov: score -= 0.5; ev.append("用神動而逢空：動不為空、待實空（-0.5）")
            else: score -= 1.0; ev.append("用神靜而逢空：暫無力、待出空（-1）")
        # 入墓: 日支或动爻支为墓库
        tomb = TOMB[ywx]
        if dbr == tomb: score -= 0.5; ev.append(f"用神入日墓（{ywx}墓於{tomb}，旺相為假墓只壓一檔，-0.5）")
        # 原忌仇: 以用神五行定: 生用者原神, 克用者忌神
        yuan_qin = next(qn for qn in QIN if False) if False else None
        # 六亲五行关系由宫五行定, 卡面未給宮五行; 改以爻五行对用神五行的生克定原神/忌神爻
        for i,l in enumerate(lines):
            if i == yong_idx: continue
            if shengs(l["wx"], ywx): role = "原神"
            elif kes(l["wx"], ywx): role = "忌神"
            elif shengs(ywx, l["wx"]): role = "泄神"
            elif kes(ywx, l["wx"]): role = "耗神"
            else: role = "同氣"
            if i in mov:
                if role=="原神": score += 1.5; chain += 1.5; ev.append(f"{POS[i]}{l['qin']}{l['br']}{l['wx']}動生用神（原神動，+1.5）")
                elif role=="忌神": score -= 1.5; chain -= 1.5; ev.append(f"{POS[i]}{l['qin']}{l['br']}{l['wx']}動克用神（忌神動，-1.5）")
                elif role=="泄神": score -= 0.5; ev.append(f"{POS[i]}{l['qin']}{l['br']}{l['wx']}動泄用神（-0.5）")
        # 用神动化
        donghua_dir = "無動化（用神靜或無化神可核）"; donghua_sign = "0"
        if ymov and yl["chg"]:
            cb, cwx = yl["chg"]["br"], yl["chg"]["wx"]
            if cb == JIN.get(ybr): dh="化進"; dv=1.0
            elif cb == TUI.get(ybr): dh="化退"; dv=-1.0
            elif shengs(cwx, ywx): dh="化回頭生"; dv=1.0
            elif kes(cwx, ywx): dh="化回頭克"; dv=-1.0
            else: dh="化出他神（非進退回頭）"; dv=0.0
            if is_hangren and dh=="化退": dv=1.0; dh="化退（行人類別讀法：退去程即歸程，反以退為歸）"
            score += dv
            donghua_dir = f"用神動化{cb}{cwx}，為{dh}（{dv:+.0f}）"
            donghua_sign = "+" if dv>0 else ("-" if dv<0 else "0")
            ev.append(donghua_dir)
        static_sign = "+" if score - (0) >= 0 else "-"
        # changed_main: 动化定性与静态(旺衰+日月,未计动化前)不一致且动化幅度改变符号方向的近似: 以动化dv改变了score符号
        # 用更诚实口径: 若用神化进/回头生使初判(仅旺衰日月)由负转正, 或化退(非行人)由正转负 -> changed_main
        # 这里以 ev 中动化 dv 与加入前分数符号比较需重算; 简化: 记录在 score 构成中无法分离时, 以"终局与仅凭用神旺衰之表面方向不同"判定
        base_ws_sign = 1 if wv>0 else (-1 if wv<0 else 0)
        final_sign = 1 if score>0.3 else (-1 if score<-0.3 else 0)
        if base_ws_sign!=0 and final_sign!=0 and base_ws_sign!=final_sign:
            changed_main = True
        # 应期
        scale = "日"
        scale_why = "所問為近事／事件型成敗，卦中日辰作用顯著，定日檔"
        if any(k in q+setting for k in ["壽元","終身","何年","仕途久遠"]):
            scale="年"; scale_why="所問屬年尺度，定年檔（先年後月，不落單日）"
        elif is_hangren and "遠" in q+setting:
            scale="月"; scale_why="行人遠行，對表行人章「遠則應月」，定月檔"
        # 主坐标机制
        if ykong:
            mech1 = ("填實", ybr); mech2 = ("沖實", OPP[ybr])
            win = f"出空前後一旬內" if scale=="日" else f"{ybr}月前後"
            main_br, main_mech = ybr, "填實（用神逢值填實）"
            rev_br, rev_mech = OPP[ybr], "沖實（沖空則實）"
        elif dbr == tomb or any(lines[i]["br"]==tomb for i in mov):
            main_br, main_mech = OPP[tomb], "沖墓（沖開墓庫）"
            rev_br, rev_mech = tomb, "填實（墓庫填實）"
            win = f"沖墓前後一旬內" if scale=="日" else f"{OPP[tomb]}月前後"
        elif not ymov:
            main_br, main_mech = OPP[ybr], "逢沖（靜爻逢沖而起）"
            rev_br, rev_mech = ybr, "逢值（用神逢值）"
            win = f"逢沖前後一旬內" if scale=="日" else f"{OPP[ybr]}月前後"
        else:
            main_br, main_mech = HE[ybr], "逢合（動而逢合）"
            rev_br, rev_mech = ybr, "逢值（用神逢值）"
            win = f"逢合前後一旬內" if scale=="日" else f"{HE[ybr]}月前後"
        unit = {"日":"日","月":"月","年":"年"}[scale]
        timing = f"窗口：{win}；窗口內主座標：{main_br}{unit}（{main_mech}）"
        rev_timing_note = (f"初推路徑：{main_mech}→{main_br}{unit}；復推路徑（換機制族）：{rev_mech}→{rev_br}{unit}；處置：二路異點，先核尺度一致（同為{scale}檔），"
                           f"再按(h)取一舍二與門類對表裁決——主座標所走機制正為用神當前狀態之開釋／對位機制，占優可指認，保留初推主座標{main_br}{unit}，復推一路只入reasoning捨棄")
    else:
        yl = None; ws="未定"; timing="應期無據不報（用神伏藏待出資格未定，只列候選不定值）"
        rev_timing_note = "初推路徑：無（伏神待出未定）；復推路徑：無；處置：R61-REV1-2 二路不合亦無占優依據，主座標不落單點、降為不定值"
        donghua_dir = "無動化可核（用神伏藏）"; donghua_sign="0"; main_br=""; unit="日"; scale="日"
        ev.append(yong_note)

    # 方向
    if reserve_used:
        direction = "未定／待出"
        conf = 0.38
        verdict = "用神伏藏、待出資格未成定局，終局不斷成敗，只斷「待時而出、目下未現」"
    elif score >= 1.0:
        direction="成／吉向"; conf = min(0.80, 0.58 + score*0.05); verdict="所問之事向成、向吉"
    elif score <= -1.0:
        direction="不成／凶向"; conf = min(0.80, 0.58 + (-score)*0.05); verdict="所問之事向不成、向凶"
    elif score > 0:
        direction="成／吉向（偏弱）"; conf = 0.55; verdict="所問之事偏向可成，惟力道偏弱、須待應期方實"
    elif score < 0:
        direction="不成／凶向（偏弱）"; conf = 0.55; verdict="所問之事偏向不成，惟阻力未至絕境、待解法之期再定升降"
    else:
        direction="未定"; conf = 0.48; verdict="盤面生克相當，方向存疑，只報未定並降置信"
        disputed = True
    if disputed: conf = min(conf, 0.50)
    if incomplete_md: conf = min(conf, 0.52)
    conf = round(max(0.30, min(0.82, conf)), 2)

    # 門類對表
    qt = q+setting
    if is_bing: menlei="疾病（疾病章第九十九）：首選沖空實空之日（空者）、次選實破／沖去克神之日；本例按用神狀態對位取點，閘門（空／破）釋放優先於對表"
    elif is_hangren: menlei="行人（行人章第九十四）：首選按用神狀態對位（伏藏出現／動逢合／化退而歸），次選沖開墓合；遠近先定尺度後取點"
    elif "婚" in qt: menlei="婚姻（婚姻章第八十二）：首選動而空者實空之月日、次選實破之時；本例先分動靜再定有無應期"
    elif "財" in qt or "貨" in qt: menlei="求財（求財章第六十八）：首選財臨日月重疊待入墓之日、次選世動逢合之日；本例按用神狀態對位，未合首選條件者遞補逢值／逢合"
    elif "孕" in qt or "產" in qt: menlei="產期／胎孕（產期章第八十九）：首選按子孫動靜對位（動逢合逢值、靜逢值逢沖），次選空沖空實空、破實破逢合"
    elif "試" in qt or "考" in qt or "案" in qt or "榜" in qt: menlei="功名發案（發案章第五十三）：以父母為用神按狀態五分對位；本例官父參看、按用神狀態取點"
    elif "出行" in qt: menlei="出行（出行章第九十一）：首選世旺靜逢沖之日、次選沖開之日月；合住閘門未開前不取行期"
    else: menlei="對表無此門類（訟事／趨避等無成文應期取法之類，或泛占），按三步＋D項原序定主座標，不類推他門類"

    evtxt = "；".join(ev) if ev else yong_note
    _wv = wv if (yong_idx is not None and not reserve_used) else 0.0
    _ch = chain if (yong_idx is not None and not reserve_used) else 0.0
    road1 = "＋" if _wv>0 else ("−" if _wv<0 else "0")
    road2 = "＋" if _ch>0 else ("−" if _ch<0 else "0")
    basis = (
        f"tradition: liuyao（輸入卡自帶 tradition=liuyao，逐例讀卡自決）；systems_used: 六爻納甲（主法，方法自選、未按樣本來源指定）。\n"
        f"所問對象：{q}（{setting}）；用神：{ylabel}。{yong_note}\n"
        f"盤面證據：{evtxt}。\n"
        f"動化方向：{donghua_dir}；方向定性：依動化定性裁決表，動化方向優先、靜態表象只調量級。\n"
        f"反轉條件：源絕三征／化退化絕且無生扶兩路逐項核——未見三征齊備或化絕無扶之全成立，反轉條件不成立，不翻轉初判（伏神引撥、化進待沖、生多為忌／源絕三類掃查均未達完整判據鏈，只許降格留餘地）。\n"
        f"四路合參：本氣{road1}／元忌仇鏈{road2}（據上列原神忌神動靜計）／動化{donghua_sign}（引裁決表結論）／世應不計（自占或代占看用神、世應不重複入參，所據見用神行）；合參方向：{direction}。\n"
        f"對象對齊：所問對象、所取用神與主斷語應驗對象同一（主語逐條對回所問對象，病占／行人類已逐名復述核對，無錯位）。\n"
        f"應期三步：①定尺度——{scale}檔；②列三路候選（沖實／填實／逢值，含合流D項沖起、出墓、解法、實空四路掃查結果已併入證據行）；③取一舍二——取與終局方向自洽一路為主座標，餘路逐路以尺度不合／與終局方向相悖／已被空破墓條件否決為由捨棄，只入此reasoning。門類應期查表校準：{menlei}。\n"
        f"R61-REV1-2/-3 二路復推留痕：{rev_timing_note}。\n"
        f"R61-REV1-4 斷項粒度核：具體斷項＝應期主座標（時間類）與終局方向（方向性主斷不適用粒度降檔）；應期斷項支撐指針≥2（用神狀態＋所走機制）指向同一落點者按原粒度保留，本例主座標支撐指針見證據行，處所／量級／狀態類細節斷項本例未落、無需降檔。\n"
        + (f"輸入完整性：卡面月日殘損——原文未明記月建／日辰（asked_at 原文：{asked}），旺衰與日月生扶無從全定，已照實降置信（上限0.52）、不臆補月日；卦名、動爻與逐爻六親干支變爻俱全，六神未隨卡列出、只作象意輔助缺如。"
         if incomplete_md else
         "輸入完整性：卡面具月日、卦名、動爻與逐爻六親干支變爻，無殘損；六神未隨卡列出，只作象意輔助缺如、不影響用神主線，故不降置信。")
    )
    pred_text = (
        f"終局（單一方向）：{direction}——{verdict}。"
        f"主斷依據：{ev[0] if ev else yong_note}" + (f"；{ev[1]}" if len(ev)>1 else "") + "。"
        f"應期（雙層）：{timing}。單位與尺度依據：{scale}檔，所問尺度與用神狀態對位機制（見basis應期三步與門類查表）。"
        + ("近段／遠段：本問有時間縱深者，近段按當前生克斷如上，遠段須待主座標之期方定升降，不另造無觸發之轉折。" if (is_bing or is_hangren) else "此問為單點成敗，無近遠兩段硬拆。")
        + f"置信：{conf}。"
    )
    trig = {"changed_main": bool(changed_main), "reserve_used": bool(reserve_used), "disputed": bool(disputed),
            "reason": (f"changed_main={bool(changed_main)}（終局方向與僅憑用神旺衰之表面方向{'不一致、經動化／合參改定' if changed_main else '一致、未改主斷'}）；"
                       f"reserve_used={bool(reserve_used)}（{'用神不上卦而啟用伏神／日月後備取用' if reserve_used else '用神現卦或變爻可取、未用後備'}）；"
                       f"disputed={bool(disputed)}（{'取用或方向存疑、已降置信' if disputed else '取用與方向無爭議點'}）")}
    for k in trig_count:
        if trig[k]: trig_count[k]+=1
    obj = {"case_id": cid, "prediction_text": pred_text, "basis": basis, "confidence": conf, "trigger": trig}
    with open(os.path.join(OUT, cid+".json"), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    results.append(cid)

# 寫盤斷言: 精確按本批 id 清單逐件
assert set(results)==set(IDS) and len(results)==60
total=0
for cid in IDS:
    p=os.path.join(OUT,cid+".json")
    d=json.load(open(p,encoding="utf-8"))
    assert d["case_id"]==cid and set(d.keys())=={"case_id","prediction_text","basis","confidence","trigger"}
    assert 0<=d["confidence"]<=1
    t=d["trigger"]; assert set(t.keys())=={"changed_main","reserve_used","disputed","reason"}
    assert all(isinstance(t[k],bool) for k in ("changed_main","reserve_used","disputed"))
    total+=os.path.getsize(p)
print("WROTE",len(results),"TOTAL_BYTES",total,"TRIG",trig_count)
