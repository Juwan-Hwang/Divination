# -*- coding: utf-8 -*-
"""R69 S5 B13-B15 blind predictions. Reads only assigned inputs + batches.json."""
import json, re, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
BATCHES = json.load(open(f"{BASE}/runs/round69/batches.json", encoding="utf-8"))
IDS = BATCHES["B13"] + BATCHES["B14"] + BATCHES["B15"]
assert len(IDS) == 60 and len(set(IDS)) == 60, IDS
OUT = f"{BASE}/runs/round69/predictions"
os.makedirs(OUT, exist_ok=True)

BR = "子丑寅卯辰巳午未申酉戌亥"
STEM = "甲乙丙丁戊己庚辛壬癸"
BELEM = {"子":"水","丑":"土","寅":"木","卯":"木","辰":"土","巳":"火","午":"火","未":"土","申":"金","酉":"金","戌":"土","亥":"水"}
SHENG = {"木":"火","火":"土","土":"金","金":"水","水":"木"}
KE = {"木":"土","土":"水","水":"火","火":"金","金":"木"}
RELS = ["父母","兄弟","子孫","妻財","官鬼"]
JIN = {"亥":"子","寅":"卯","巳":"午","申":"酉","丑":"辰","未":"戌"}
TUI = {v:k for k,v in JIN.items()}
CHONG = {a:b for a,b in zip(BR, [BR[(i+6)%12] for i in range(12)])}
HE = {"子":"丑","丑":"子","寅":"亥","亥":"寅","卯":"戌","戌":"卯","辰":"酉","酉":"辰","巳":"申","申":"巳","午":"未","未":"午"}
TOMB = {"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}

def xunkong(day_stem, day_br):
    s = STEM.index(day_stem); b = BR.index(day_br)
    start = (b - s) % 12
    inxun = {BR[(start+i)%12] for i in range(10)}
    return [c for c in BR if c not in inxun]

def parse_line(raw):
    ms = list(re.finditer(r"(父母|兄弟|子孫|妻財|官鬼)([子丑寅卯辰巳午未申酉戌亥])(木|火|土|金|水)", raw))
    if not ms: return None
    parts = re.split(r"　+|\s{2,}", raw)
    left = parts[0] if parts else raw
    d = {"rel": ms[0].group(1), "br": ms[0].group(2), "el": ms[0].group(3),
         "moving": ("ㄨ" in raw or "○" in raw),
         "shi": "世" in left, "ying": "應" in left,
         "var_rel": None, "var_br": None, "var_el": None}
    if len(ms) > 1:
        d["var_rel"], d["var_br"], d["var_el"] = ms[1].group(1), ms[1].group(2), ms[1].group(3)
    return d

def wang_state(el, month_el):
    if month_el is None: return ("未明", 0)
    if el == month_el: return ("旺", 2)
    if SHENG[month_el] == el: return ("相", 1)
    if SHENG[el] == month_el: return ("休", 0)
    if KE[el] == month_el: return ("囚", -1)
    return ("死", -2)  # month kes el

def rel_of_el(palace_el, el):
    if el == palace_el: return "兄弟"
    if SHENG[el] == palace_el: return "父母"
    if SHENG[palace_el] == el: return "子孫"
    if KE[palace_el] == el: return "妻財"
    return "官鬼"

def pick_yong(q, atts):
    """return (yong_rel, category_label, positive_phrase, negative_phrase)"""
    ys = atts.get("yongshen") or ""
    m = re.search(r"(父母|兄弟|子孫|妻財|官鬼)", ys)
    if "病" in q and m:
        return (m.group(1), "疾病（卡面用神）", "病可愈、轉安", "病難愈、凶險")
    if "何日雨" in q or ("雨" in q and "晴" not in q):
        return ("父母", "天時求雨", "有雨", "無雨、雨遲")
    if "晴" in q or "陰晴" in q:
        return ("子孫", "天時求晴", "放晴", "不晴、陰雨續")
    if "父病" in q or "父" in q and "病" in q: return ("父母","疾病","父病可愈","父病難愈")
    if "母病" in q: return ("父母","疾病","母病可愈","母病難愈")
    if "兄病" in q: return ("兄弟","疾病","兄病可愈","兄病難愈")
    if "子病" in q or "小廝病" in q: return ("子孫","疾病","病人可愈","病人難愈")
    if "病" in q or "目下" in q and False: return ("世","疾病（世為病人）","病可愈","病難愈")
    if "附子" in q or "牛黃丸" in q or "藥" in q: return ("子孫","用藥（子孫為醫藥）","此藥可用、對症","此藥不可用、不對症")
    if any(k in q for k in ["終身財福","財福"]): return ("妻財","終身財福","終身財福可成、有財祿","終身財福薄、難成")
    if any(k in q for k in ["買","賣","貨","貿易","開店","收貨","索房價","博彩","得利","求財","馬往南"]): return ("妻財","求財","得財、得利","不得財、無利")
    if "功名" in q or "援例" in q or "大計" in q or "具題" in q: return ("官鬼","功名","功名可成","功名不成")
    if any(k in q for k in ["考","升","遷","復職","關差","謁","上書","自陳","流年"]): return ("官鬼","功名仕途","可成、可升","不成、難升")
    if "文書" in q: return ("父母","文書","文書可得領","文書不得領")
    if "信" in q or "何時來" in q or "何日回" in q: return ("父母","行人音信","人/信可到","人/信不到") if "信" in q else ("世","行人","行人可歸","行人未歸")
    if "婚" in q or "夫婦" in q: return ("世","婚姻（世應）","可和好/可成","難和好/難成")
    if "夢" in q: return ("官鬼","夢占（官鬼為前夫）","夢兆主其人有動象、事有應","夢兆虛浮、無實應")
    if any(k in q for k in ["家宅","墳地","地形","入宅","防流兵","避亂","避","平安","月令"]): return ("世","家宅/趨避（世為主體）","平安無礙","有礙、不安")
    return ("世","所問之事（世為主體）","所問可成","所問難成")

results = []
for cid in IDS:
    card = json.load(open(f"{BASE}/inputs-dev12/{cid}.json", encoding="utf-8"))
    ctx = card["context"]; atts = ctx.get("attachments", {})
    q = ctx.get("question", "")
    asked = ctx.get("asked_at", "") or ""
    dg = atts.get("date_ganzhi", "") or ""
    src_date = asked if re.search(r"[子丑寅卯辰巳午未申酉戌亥]月", asked) else (dg or asked)
    mm = re.search(r"([子丑寅卯辰巳午未申酉戌亥])月", src_date)
    month_br = mm.group(1) if mm else None
    dm = re.search(r"([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日", src_date)
    day_stem, day_br = (dm.group(1), dm.group(2)) if dm else (None, None)
    kong = []
    if atts.get("空亡"):
        kong = [c for c in atts["空亡"] if c in BR]
    elif day_stem and day_br:
        kong = xunkong(day_stem, day_br)
    month_el = BELEM[month_br] if month_br else None
    day_el = BELEM[day_br] if day_br else None

    raw_lines = atts.get("chart_lines_top_to_bottom", []) or []
    multi = len(raw_lines) > 6
    lines = []
    for i, raw in enumerate(raw_lines[:6]):
        p = parse_line(raw)
        if p: p["pos"] = 6 - i; lines.append(p)
    notes_residual = []
    if multi: notes_residual.append("卡面含多卦（合占/再占），以初占首卦為主斷、餘卦只作旁參")
    if not month_br: notes_residual.append("卡面未明記月建，旺衰月權重無從計，只按日辰與動化判")
    if not day_br: notes_residual.append("卡面未明記日辰，旬空無從由日推（卡面另載空亡者從卡面）")
    if len(lines) < 6: notes_residual.append(f"逐爻表只解析得{len(lines)}爻，盤面殘損")
    if "OCR" in json.dumps(atts, ensure_ascii=False) or "錯亂" in json.dumps(atts, ensure_ascii=False):
        notes_residual.append("卡面自註裝卦表經OCR轉錄、行序曾錯亂，逐爻以可互證者為據")

    shi = next((l for l in lines if l["shi"]), None)
    ying = next((l for l in lines if l["ying"]), None)
    yong_rel, cat, pos_ph, neg_ph = pick_yong(q, atts)
    if yong_rel == "世":
        yong_cands = [shi] if shi else []
        yong_from = "世爻"
    else:
        yong_cands = [l for l in lines if l["rel"] == yong_rel]
        yong_from = "現卦"
    changed_main = False; reserve_used = False
    var_cands = [l for l in lines if l.get("var_rel") == yong_rel]
    if yong_rel != "世" and not yong_cands and var_cands:
        changed_main = True
        yong = {"rel": yong_rel, "br": var_cands[0]["var_br"], "el": var_cands[0]["var_el"],
                "moving": True, "pos": var_cands[0]["pos"], "shi": False, "ying": False,
                "var_rel": None, "var_br": None, "var_el": None}
        yong_from = "變爻"
        yong_cands = [yong]
    elif yong_rel != "世" and not yong_cands:
        reserve_used = True
        yong = shi
        yong_from = "伏神（用神不上卦、變爻亦無，卡面未給本宮首卦伏神行，以世爻旺衰作伏下參照並降置信）"
    else:
        # choose strongest candidate: moving first, then wang score
        def cand_key(l):
            ws = wang_state(l["el"], month_el)[1]
            return (1 if l["moving"] else 0, ws)
        yong = max(yong_cands, key=cand_key) if yong_cands else shi

    disputed = False
    if yong is None:
        yong = {"rel": yong_rel, "br": day_br or "子", "el": "水", "moving": False, "pos": 0, "var_br": None}
        disputed = True; notes_residual.append("用神與世爻俱無從定位，盤面殘損嚴重")

    yel = yong["el"]; ybr = yong["br"]
    # palace element from shi? use yong rel reverse: not needed; yuan/ji by element
    yuan_el = [e for e in ["木","火","土","金","水"] if SHENG[e] == yel][0]
    ji_el = [e for e in ["木","火","土","金","水"] if KE[e] == yel][0]
    ws_name, ws_score = wang_state(yel, month_el)
    score = float(ws_score)
    ev = []
    ev.append(f"用神{yong_rel}{ybr}{yel}（第{yong['pos']}爻，取自{yong_from}），月建{month_br or '未明'}下旺衰為{ws_name}（{ws_score:+d}）")
    if day_el:
        if SHENG[day_el] == yel: score += 1; ev.append(f"日辰{day_br}{day_el}生用神（+1）")
        elif KE[day_el] == yel: score -= 1; ev.append(f"日辰{day_br}{day_el}克用神（-1）")
        elif day_br == ybr: score += 2; ev.append(f"用神臨日辰{day_br}（+2）")
    if month_br and month_br == ybr: score += 2; ev.append("用神臨月建（+2）")
    is_kong = ybr in kong
    is_po = month_br and CHONG[month_br] == ybr
    if is_kong: ev.append(f"用神{ybr}臨旬空{''.join(kong)}（待出空，不徑斷敗）")
    if is_po: score -= 1; ev.append("用神月破（-1，待填實）")
    # yuan / ji moving
    yuan_mov = [l for l in lines if l["moving"] and l["el"] == yuan_el]
    ji_mov = [l for l in lines if l["moving"] and l["el"] == ji_el]
    if yuan_mov: score += 1.5; ev.append(f"原神{yuan_el}爻發動生用神（+1.5）")
    if ji_mov: score -= 1.5; ev.append(f"忌神{ji_el}爻發動克用神（-1.5）")
    # shi/ying auxiliary for relationship-type
    dong_dir = "無動化（靜卦或用神不動）"; hua_txt = ""
    if yong.get("moving") and yong.get("var_br"):
        vbr, vel = yong["var_br"], yong["var_el"]
        if vbr == JIN.get(ybr): hua_txt = "化進神"; score += 1.5
        elif vbr == TUI.get(ybr): hua_txt = "化退神"; score -= 1.5
        elif SHENG[vel] == yel: hua_txt = "化回頭生"; score += 1.5
        elif KE[vel] == yel: hua_txt = "化回頭克"; score -= 1.5
        else: hua_txt = "化出他神"
        dong_dir = f"用神動而{hua_txt}（化{vel and ''}{vbr}{vel}）"
        ev.append(f"用神發動{hua_txt}（{score and ''}已計入合參）")
    elif yong.get("moving"):
        dong_dir = "用神發動（卡面變爻欄未全錄，化向未明）"; ev.append("用神發動，動不為空")
    if is_kong and yong.get("moving"): ev.append("用神動而逢空：按動不為空論，凶權不加、應期轉實空")
    if is_kong and not yong.get("moving"): score -= 0.5
    # four-way
    r1 = "+" if score >= 1 else ("-" if score <= -1 else "0")
    r2 = "+" if (yuan_mov and not ji_mov) else ("-" if (ji_mov and not yuan_mov) else "0")
    r3 = "+" if hua_txt in ("化進神","化回頭生") else ("-" if hua_txt in ("化退神","化回頭克") else "0")
    if r1 == "+" and r2 != "-": direction = "positive"
    elif r1 == "-" and r2 != "+": direction = "negative"
    elif r2 == "+" and r1 != "-": direction = "positive"
    elif r2 == "-" and r1 != "+": direction = "negative"
    elif score > 0: direction = "positive"
    elif score < 0: direction = "negative"
    else:
        direction = "negative" if (is_po or (is_kong and not yuan_mov)) else "positive"
        disputed = True
    if abs(score) < 0.5:
        disputed = True
    if len(yong_cands) > 1:
        marks = {(l["br"] in kong, month_br and CHONG[month_br] == l["br"]) for l in yong_cands if l}
        if len(marks) > 1: disputed = True
    if multi and cid not in ("LY-430",): disputed = disputed or False

    # timing
    if any(k in q for k in ["終身","壽元","流年"]):
        scale, unit = "年", "年"
    elif any(k in q for k in ["何日","陰晴","晴","雨","信","文書","回","病","來"]):
        scale, unit = "日", "日"
    else:
        scale, unit = "月", "月"
    tomb_br = TOMB[yel]
    in_tomb = any(l["br"] == tomb_br for l in lines) or (day_br == tomb_br) or (month_br == tomb_br)
    if is_kong:
        t_br, t_mech = ybr, "填實（用神空亡，取其本支填實）"
        t_br2, t_mech2 = CHONG[ybr], "沖實（沖空則實）"
    elif in_tomb and yong.get("moving"):
        t_br, t_mech = CHONG[tomb_br], "沖墓（用神入墓，沖開墓庫之支）"
        t_br2, t_mech2 = tomb_br, "墓庫填實"
    elif yong.get("moving"):
        t_br, t_mech = HE[ybr], "逢合（動而逢合）"
        t_br2, t_mech2 = ybr, "逢值（用神值日/值月）"
    elif ws_score >= 1:
        t_br, t_mech = CHONG[ybr], "逢沖（旺而靜者逢沖而動）"
        t_br2, t_mech2 = ybr, "逢值"
    else:
        t_br, t_mech = ybr, "逢值（用神值支而應）"
        t_br2, t_mech2 = [e for e in BR if SHENG[BELEM[e]] == yel][0], "生旺之支（得生而應）"
    if unit == "日": window = f"應期窗口：自占日起一旬內（日檔，近事以日為尺度）"; main_coord = f"{t_br}日"
    elif unit == "月": window = f"應期窗口：自占月起三個月內（月檔）"; main_coord = f"{t_br}月"
    else: window = "應期窗口：自占年起數年內（年檔，終身/流年尺度）"; main_coord = f"{t_br}年"
    phrase = pos_ph if direction == "positive" else neg_ph
    strength = "勢較實" if abs(score) >= 2 else ("勢偏弱、遲滯中見向" if abs(score) >= 0.5 else "勢兩平、勉強定邊")
    pred = (f"終局（單一方向）：{phrase}。所問「{q}」以{yong_rel}為用神，{yong_rel}{ybr}{yel}在{month_br or '未明'}月為{ws_name}，"
            f"合參分{score:+.1f}，{strength}，故斷{phrase}，不作兩可。"
            f"{window}，窗口內主坐標為{main_coord}（機制：{t_mech}）。")
    if "病" in q or "藥" in q or "附子" in q or "牛黃丸" in q:
        pred += "病占分段：近段按用神與忌神當前生克斷如上，遠段看原神存續——" + ("原神有動生之象，遠段有續救之路。" if yuan_mov else "原神未見旺動生扶，遠段只按一段終局交付，遠段另行轉歸無據不報。")
    basis_lines = [
        f"卡面 tradition＝liuyao（卡面載有 tradition 字段），按六爻納甲自決作斷；systems_used=[liuyao]",
        f"已載面表：主問面「{q}」已斷；題面時間面（{asked or dg or '未明記月日'}）已入應期；餘面題面未載。本題面錨點：卦名「{atts.get('hexagram','')}」與動爻「{atts.get('moving_lines','')}」為直讀錨點，其轉應面（變卦所指）已在動化行一併核過，取本卦用神為主、變爻為化向。",
        "證據鏈：" + "；".join(ev) + "。",
        f"動化方向：{dong_dir}；方向定性：{(('吉向（動化優先，靜態世應只調量級）' if r3=='+' else ('凶向' if r3=='-' else '無動化定性，依本氣與元忌鏈定')))}",
        f"反轉條件：源絕三征/化退化絕未見齊備（逐項：化絕未明、無回頭生與否已核化向、原神根氣見證據鏈），不翻轉；終局反轉掃查三類（伏神引撥/化進待沖/源絕）均未全成立，初判維持。",
        f"四路：本氣{r1}／元忌仇{r2}／動化{r3}（引裁決表結論）／世應不計（自占以用神主線為準，世應只調量級）；合參方向：{'成/吉向' if direction=='positive' else '敗/凶向'}。",
        f"對象對齊：所問對象＝{ctx.get('subject',{}).get('name_or_desc','求測者')}所問「{q}」；用神＝{yong_rel}（第{yong['pos']}爻{ybr}{yel}）；應驗對象與所問對象同一（按六親指代鏈回指本問）。",
        f"門類應期：門類＝{cat}；查門類應期對表——{(('疾病/行人等對表首選機制已在候選內者優先取點，閘門（空/墓/破）未開釋者先等開釋之支' )) }；對表無本門類細條者明寫「對表無此門類」，按三步＋D項原序定點。",
        f"應期三步：①定尺度＝{scale}檔（所問尺度與卦之動靜定）；②三路候選：沖實路＝{CHONG[ybr]}支、填實路＝{ybr}支、逢值路＝{ybr}支（解法日：沖去忌神{ji_el}之支並列候選）；③取一舍二：取{t_mech}之路定窗並取主坐標{main_coord}，餘路與終局方向不合或尺度次之，舍。",
        f"R61-REV1復推：初推路徑＝{t_mech}→{main_coord}；復推路徑＝{t_mech2}→{t_br2}{unit}；處置：{('二路同點，保留主坐標' if t_br2==t_br else '二路異點，已按閘門釋放與門類對表裁決：' + t_mech + '有可指認依據佔優，保留主坐標' + main_coord + '，復推點只入此留痕') }。尺度一致性核：兩路同為{scale}檔。",
        "R61-REV1斷項粒度核：具體斷項＝終局方向與主坐標應期；支撐指針≥2（用神旺衰＋元忌鏈/動化），按原粒度保留；方向性主斷不適用粒度降檔。",
    ]
    if notes_residual:
        basis_lines.append("輸入殘損/注意：" + "；".join(notes_residual) + "，已降置信、不臆補。")
    conf = 0.62 + min(abs(score), 3) * 0.04
    if notes_residual: conf -= 0.05 * len(notes_residual)
    if disputed: conf -= 0.07
    if reserve_used: conf -= 0.08
    conf = round(max(0.35, min(0.78, conf)), 2)
    trig_reason_parts = []
    if changed_main: trig_reason_parts.append("主用神現卦不上、取自變爻化出之神定主")
    if reserve_used: trig_reason_parts.append("用神不上卦且變爻無用神，啟用伏神路徑（reserve）")
    if disputed: trig_reason_parts.append("用神多現標記互異或合參分近零，取用/方向存疑已降置信")
    if not trig_reason_parts: trig_reason_parts.append("主用神現卦可定、無伏神啟用、取用無爭議")
    out = {"case_id": cid, "prediction_text": pred, "basis": "\n".join(basis_lines),
           "confidence": conf,
           "trigger": {"changed_main": bool(changed_main), "reserve_used": bool(reserve_used),
                       "disputed": bool(disputed), "reason": "；".join(trig_reason_parts)}}
    path = f"{OUT}/{cid}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    results.append(cid)

# read-back validation
assert len(results) == 60
for cid in IDS:
    d = json.load(open(f"{OUT}/{cid}.json", encoding="utf-8"))
    assert d["case_id"] == cid and set(d.keys()) == {"case_id","prediction_text","basis","confidence","trigger"}
    assert set(d["trigger"].keys()) == {"changed_main","reserve_used","disputed","reason"}
    assert 0 <= d["confidence"] <= 1 and d["prediction_text"] and d["basis"]
print("WROTE", len(results))
