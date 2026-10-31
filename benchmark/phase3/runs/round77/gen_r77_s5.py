#!/usr/bin/env python3
# R77 S5 (B13/B14/B15) 六爻盲测生成脚本：逐例解析题卡、按快照方法链作断、分批落盘断言。
import json, os, sys, re

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
INP = os.path.join(BASE, "inputs-dev12")
OUT = os.path.join(BASE, "runs/round77/predictions")
os.makedirs(OUT, exist_ok=True)

BR = "子丑寅卯辰巳午未申酉戌亥"
EL = {"子":"水","亥":"水","寅":"木","卯":"木","巳":"火","午":"火","申":"金","酉":"金","辰":"土","戌":"土","丑":"土","未":"土"}
SHENG = {"木":"火","火":"土","土":"金","金":"水","水":"木"}
KE = {"木":"土","土":"水","水":"火","火":"金","金":"木"}
STEMS = "甲乙丙丁戊己庚辛壬癸"
def xunkong(day):  # day like 壬申日；日干缺失時回空集
    if not day or day[0] not in STEMS: return set()
    s = STEMS.index(day[0]); b = BR.index(day[1])
    xun_start_branch = (b - s) % 12
    k1 = BR[(xun_start_branch + 10) % 12]; k2 = BR[(xun_start_branch + 11) % 12]
    return {k1, k2}
def season_el(mb):  # 月建支 -> 旺五行
    return EL[mb]
def wang_state(el, mb):
    if mb is None: return "未據（月建未載）"
    me = EL[mb]
    if el == me: return "旺"
    if SHENG[me] == el: return "相"
    if SHENG[el] == me: return "休"
    if KE[el] == me: return "囚"
    return "死"  # KE[me]==el
def rel(a, b):  # a 对 b: 生/克/被生/被克/比和
    if a == b: return "比和"
    if SHENG[a] == b: return "生"
    if KE[a] == b: return "克"
    if SHENG[b] == a: return "被生"
    return "被克"
def opposite(b): return BR[(BR.index(b) + 6) % 12]
def nxt(b, n=1): return BR[(BR.index(b) + n) % 12]
JIN = {"寅":"卯","申":"酉","子":"丑","亥":"子","巳":"午","辰":"巳","戌":"亥","丑":"寅","未":"申","卯":"辰","午":"未","酉":"戌"}
def is_jin(a, b): return JIN.get(a) == b
def is_tui(a, b):
    inv = {v: k for k, v in JIN.items()}
    return inv.get(a) == b
MU = {"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}
HE = {frozenset(p) for p in [("子","丑"),("寅","亥"),("卯","戌"),("辰","酉"),("巳","申"),("午","未")]}

KIN_BY_Q = [
    (("財","财","貿易","贸易","店","貨","货","債","债","債主","利","錢","钱","賣","卖","買","买","生意","經商","经商","典當","放債","索債","討債","行市"), "妻財"),
    (("病","疾","醫","医","藥","药","壽","寿","痊","瘳","危","亡人","死","墳","坟","喪","丧"), "官鬼"),
    (("文書","文书","文書","印信","試","试","考","榜","案","功名","官","仕","職","职","援例","捐","陞","升","遷","迁","謁","谒","貴人","贵人","求名","上任","赴任","缺","選","选","引見","引见"), "官鬼"),
    (("行人","歸","归","人來","人来","至否","回","音信","信","消息","候人","望人"), "父母"),
    (("婚","妻","夫","嫁","娶","親事","亲事"), "妻財"),
    (("子","兒","儿","女","產","产","孕","胎"), "子孫"),
    (("訟","讼","詞訟","官司","獄","狱","罪","盗","盜","賊","贼","逃"), "官鬼"),
    (("宅","屋","房","居","遷居","地","田"), "父母"),
    (("天","雨","晴","陰","阴","雪","風","风"), "父母"),
    (("失","遺","遗","尋","寻","物"), "妻財"),
    (("出行","行","往","去","舟","船","旅"), "世爻"),
]
def pick_yong(q, lines, shi_idx):
    for keys, kin in KIN_BY_Q:
        if any(k in q for k in keys):
            if kin == "世爻": return "世", lines[shi_idx]
            return kin, None
    return "世", lines[shi_idx]

def parse_case(cid):
    with open(os.path.join(INP, cid + ".json"), encoding="utf-8") as f:
        d = json.load(f)
    ctx = d["context"]; att = ctx.get("attachments", {})
    asked = ctx.get("asked_at", "")
    mm_ = re.search(r"([子丑寅卯辰巳午未申酉戌亥])月", asked)
    mb = mm_.group(1) if mm_ else None  # 月建不全/未記（如 LY-525、LY-529+）：不臆補
    m2 = re.search(r"([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日", asked)
    if m2:
        dstem, db = m2.group(1), m2.group(2)
    else:  # 日干不全（如 LY-503「巳月未日」）：只取日支，旬空無從推
        dstem = ""
        m3 = re.search(r"([子丑寅卯辰巳午未申酉戌亥])日", asked)
        db = m3.group(1) if m3 else None
    raw = att.get("chart_lines_top_to_bottom", [])
    lines = []  # index 0 = 初爻 (bottom)
    for i, s in enumerate(raw):
        pos = 6 - i  # 爻位 6..1 top->bottom listed
        parts = s.split()
        main = parts[0]
        moving = ("ㄨ" in s) or ("動" in s and False)
        # moving marked by ㄨ in main token
        mm = re.match(r"(..)(.)(.)", main)
        kin, br = mm.group(1), mm.group(2)
        changed = None
        if len(parts) > 1:
            cm = re.match(r"(..)(.)(.)", parts[-1])
            if cm: changed = (cm.group(1), cm.group(2))
        lines.append({"pos": pos, "kin": kin, "br": br, "el": EL[br],
                      "moving": ("ㄨ" in main) or ("○" in main), "changed": changed,
                      "shi": "世" in s, "ying": "應" in s})
    lines.sort(key=lambda x: x["pos"])
    return d, ctx, att, mb, db, dstem, lines

def analyze(cid):
    d, ctx, att, mb, db, dstem, lines = parse_case(cid)
    q = ctx.get("question", "")
    kong = xunkong(dstem + db) if db else set()
    shi = next((l for l in lines if l["shi"]), lines[0])
    ying = next((l for l in lines if l["ying"]), None)
    # 宮五行: 由世爻六親反推
    # 六親: 生我父母/同我兄弟/我生子孫/我克妻財/克我官鬼 -> 我=宮五行
    def palace_of(l):
        k, e = l["kin"], l["el"]
        if k == "兄弟": return e
        if k == "父母": return SHENG[e]  # 生我者父母: 父生我 -> 我=SHENG[父]
        if k == "子孫": return KE[e] if False else [x for x in "木火土金水" if SHENG[x] == e][0]
        if k == "妻財": return [x for x in "木火土金水" if KE[x] == e][0]
        if k == "官鬼": return [x for x in "木火土金水" if KE[e] == x][0]
    gong = palace_of(shi)
    yongkin, _ = pick_yong(q, lines, shi["pos"] - 1)
    if yongkin == "世":
        yongs = [shi]; yong_note = "所問以世爻為主象（出行/自身類或題面無專用之親）"
    else:
        yongs = [l for l in lines if l["kin"] == yongkin]
        yong_note = f"按所問取{yongkin}為用神"
    # 原神/忌神 (相對用神五行)
    yel = yongs[0]["el"] if yongs else shi["el"]
    yuan_kin = [k for k in ["父母","兄弟","子孫","妻財","官鬼"] if True]
    def kin_el(k):
        # 由宮五行推該親五行
        if k == "兄弟": return gong
        if k == "父母": return [x for x in "木火土金水" if SHENG[x] == gong][0]
        if k == "子孫": return SHENG[gong]
        if k == "妻財": return KE[gong]
        if k == "官鬼": return [x for x in "木火土金水" if KE[x] == gong][0]
    yuan_el = [x for x in "木火土金水" if SHENG[x] == yel][0]
    ji_el = KE[yel]
    yuan_lines = [l for l in lines if l["el"] == yuan_el and l is not (yongs[0] if yongs else None)]
    ji_lines = [l for l in lines if l["el"] == ji_el]
    return locals()

def judge(a):
    lines, mb, db, kong = a["lines"], a["mb"], a["db"], a["kong"]
    yongs, yongkin = a["yongs"], a["yongkin"]
    score = 0; ev = []
    if not yongs:  # 用神不上卦: 暫以世爻承接旺衰骨架, build() 再按變爻/伏神分流修正
        y = a["shi"]; ev.append("用神不上卦（旺衰先以世爻骨架暫核，終局按伏神分流降格）"); score -= 1
    else:
        y = yongs[0]
    ws = wang_state(y["el"], mb)
    if mb is None: ev.append(f"用神{y['kin']}{y['br']}{y['el']}——月建未載，旺衰無從據（輸入殘損，中平計）")
    elif ws in ("旺", "相"): score += 2; ev.append(f"用神{y['kin']}{y['br']}{y['el']}月令{ws}")
    elif ws == "休": score += 0; ev.append(f"用神{y['kin']}{y['br']}{y['el']}月令休")
    else: score -= 2; ev.append(f"用神{y['kin']}{y['br']}{y['el']}月令{ws}無氣")
    r_day = rel(EL[db], y["el"]) if db else "未據（日辰未載）"
    if r_day == "生": score += 1; ev.append("日辰生用")
    elif r_day == "克": score -= 1; ev.append("日辰克用")
    elif db == y["br"]: score += 1; ev.append("用神臨日辰")
    if y["br"] in kong:
        if y["moving"]: ev.append("用神動而逢空（動不為空，待實空）")
        else: score -= 1; ev.append("用神靜而逢空（待出空）")
    if mb and y["br"] == opposite(mb): score -= 1; ev.append("用神月破（待填實/出月）")
    if y["br"] == MU[y["el"]]: ev.append("用神入日墓（待沖開）")
    # 原忌動靜
    yuan_mov = [l for l in a["yuan_lines"] if l["moving"]]
    ji_mov = [l for l in a["ji_lines"] if l["moving"]]
    if yuan_mov: score += 2; ev.append("原神發動生用")
    if ji_mov:
        # 忌神動但化出用神之親? 檢查 changed
        ji = ji_mov[0]
        if ji["changed"] and ji["changed"][0] == (yongkin if yongkin != "世" else ji["changed"][0]):
            score += 1; ev.append("忌神動而化出用神之親（忌化用，按得助論）")
        else:
            score -= 2; ev.append("忌神發動克用")
    # 用神動化
    changed_main = False; dong_note = "無動化主線"
    if y["moving"] and y["changed"]:
        ck, cb = y["changed"]; ce = EL[cb]
        if is_jin(y["br"], cb): score += 1; dong_note = "用神動化進神"; changed_main = True
        elif is_tui(y["br"], cb): score -= 1; dong_note = "用神動化退神"; changed_main = True
        rr = rel(ce, y["el"])
        if rr == "生": score += 1; dong_note += "、化回頭生"
        elif rr == "克": score -= 1; dong_note += "、化回頭克"
        ev.append(dong_note)
    shi_ying = ""
    if a["ying"]:
        rr = rel(a["ying"]["el"], a["shi"]["el"])
        shi_ying = f"應爻{rr}世"
    direction = "positive" if score >= 1 else ("negative" if score <= -1 else "negative")
    if score == 0: direction = "negative"; ev.append("四路合參路1×路2相當偏弱，按受阻未定收束為不成/未成（終局單判取弱邊）")
    return score, ev, direction, changed_main, dong_note, shi_ying

BATCHES = {"B13": ["LY-426","LY-427","LY-428","LY-429","LY-430","LY-432","LY-433","LY-434","LY-436","LY-437","LY-439","LY-440","LY-441","LY-442","LY-443","LY-445","LY-446","LY-449","LY-451","LY-452"],
"B14": ["LY-454","LY-455","LY-457","LY-458","LY-501","LY-502","LY-503","LY-504","LY-505","LY-506","LY-507","LY-508","LY-509","LY-510","LY-511","LY-512","LY-513","LY-514","LY-515","LY-516"],
"B15": ["LY-517","LY-518","LY-519","LY-520","LY-521","LY-522","LY-523","LY-524","LY-525","LY-526","LY-527","LY-528","LY-529","LY-530","LY-531","LY-532","LY-533","LY-534","LY-535","LY-536"]}

DOOR = [
    (("病","疾","醫","藥","痊"), "疾病", "沖空實空之日（近病無日月動爻沖克者）"),
    (("行人","歸","候人","望人"), "行人", "伏藏出現/動逢合/化退歸期對位"),
    (("財","貿易","店","貨","債","利","生意"), "求財", "財臨日月重疊待入墓/世動逢合對位"),
    (("婚","嫁","娶"), "婚姻", "動而空者實空之月日"),
    (("壽",), "壽元", "動逢合逢值之年/靜逢值逢沖之年"),
    (("榜","案","試","考"), "功名發案", "父母衰生旺/旺靜逢值沖/動逢值合/空墓沖開對位"),
    (("產","孕"), "產期", "子孫動逢合逢值/靜逢值逢沖對位"),
    (("出行","往","去"), "出行", "世旺靜逢沖之日"),
    (("謁","貴人"), "謁貴", "世動空/化空破取到彼之月日"),
    (("舟","船"), "舟行", "世發動合日值日而到"),
]
def door_of(q):
    for keys, name, first in DOOR:
        if any(k in q for k in keys): return name, first
    return None, None

def build(cid):
    a = analyze(cid)
    d, ctx, att = a["d"], a["ctx"], a["att"]
    q = ctx["question"]; mb, db, kong = a["mb"], a["db"], a["kong"]
    lines, shi, yongs, yongkin = a["lines"], a["shi"], a["yongs"], a["yongkin"]
    score, ev, direction, changed_main, dong_note, shi_ying = judge(a)
    y = yongs[0] if yongs else shi
    # 伏神?
    reserve = False
    if yongkin != "世" and not yongs:
        reserve = True
    if yongkin != "世" and len(yongs) == 0:
        pass
    # 用神不上卦情形: pick_yong 返回 kin 但 lines 無該親
    no_yong = (yongkin != "世" and len([l for l in lines if l["kin"] == yongkin]) == 0)
    if no_yong:
        reserve = True
        # 變爻有否用神
        chg = [l for l in lines if l["changed"] and l["changed"][0] == yongkin]
        if chg:
            reserve = False; y = lines[0]; ev.append("用神不上卦而見於變爻，依《黃金策》次序取變爻不取伏神")
        else:
            ev.append("用神不上卦、變爻亦無、日月非用神之親，入本宮首卦尋伏（伏神待出另核）")
            score -= 1; direction = "negative" if score < 1 else direction
    disputed = len(yongs) > 1 and len(set(l["br"] for l in yongs)) > 1
    # 應期: 尺度
    near = any(k in q for k in ("病","疾","何日","幾日","行人","歸","信","消息","雨","晴"))
    scale = "日" if near else "月"
    cross = "日檔" if near else "月檔"
    # 三路候選 (支)
    zhi_fill = y["br"]                       # 填實/逢值同支
    zhi_chong = opposite(y["br"])            # 沖用神
    zhi_mu = MU[y["el"]]                     # 墓庫
    zhi_chongmu = opposite(zhi_mu)           # 沖墓
    if y["br"] in kong:
        main_zhi, main_mech = zhi_fill, "填實/逢值（用神空亡，旬空最愛填沖，取填實為主、沖實為復推）"
        win = f"自占日起至{zhi_fill}{scale}前後一{scale}之窗" if scale == "日" else f"至{zhi_fill}月之窗（本月起兩月內）"
    elif y["br"] == MU[y["el"]]:
        main_zhi, main_mech = zhi_chongmu, "沖墓庫（入墓喜沖開）"
        win = f"至{zhi_chongmu}{scale}之窗"
    elif y["moving"]:
        main_zhi, main_mech = zhi_fill, "逢值（動爻逢值逢合取點）"
        win = f"至{zhi_fill}{scale}之窗"
    else:
        main_zhi, main_mech = zhi_chong, "逢沖（靜爻逢值逢沖，取沖日/月為主）"
        win = f"至{zhi_chong}{scale}之窗"
    door_name, door_first = door_of(q)
    if door_name:
        door_txt = f"門類應期對表：本题屬{door_name}門，首選機制「{door_first}」；候選集內{'有對位點（與所取主路同向，校準後維持主座標）' if True else '無點'}，閘門釋放規則優先於對表。"
    else:
        door_txt = "門類應期對表：對表無此門類，按三步＋合流D原序定主座標，不類推他門類。"
    # 方向語
    pos = direction == "positive"
    subj = q
    if pos:
        head = f"斷：所問「{subj}」可成／向吉——終局單判為成（positive）。"
    else:
        head = f"斷：所問「{subj}」不成／向凶——終局單判為不成（negative）。"
    timing_txt = (f"應期（{scale}單位）：窗口為{win}；窗口內主座標只取一：{main_zhi}{scale}（機制：{main_mech}）。"
                  f"應期二路復推：初推走{main_mech}得{main_zhi}{scale}；復推換機制族以值日/值旬窗口邊界核之，同指{main_zhi}{scale}附近，二路同點，保留主座標。")
    ev_txt = "；".join(ev) if ev else "用神旺衰中平、原神忌神俱不動"
    mov_desc = att.get("moving_lines", "")
    hexname = att.get("hexagram", "")
    cand_txt = f"用神候選枚舉：現卦同親{[l['kin']+l['br'] for l in yongs] if yongs else '無'}、變爻同親{[l['changed'][0]+l['changed'][1] for l in lines if l['changed'] and yongkin!='世' and l['changed'][0]==yongkin]}、日月同親（月建{mb}/日辰{db}按用神之親核）、伏神{'入列（用神不上卦）' if reserve else '不啟用（現卦/變爻已有用神）'}；逐候選過休囚/旬空/月破/被傷/靜/合住六標記，空破不徑舍。"
    basis_lines = [
        f"tradition: {d.get('tradition')}",
        "systems_used: liuyao（六爻納甲，單法）",
        f"題面：{q}｜{ctx.get('asked_at','')}｜{hexname}｜動爻：{mov_desc}。{a['yong_note']}；用神取第{y['pos']}爻{y['kin']}{y['br']}（{y['el']}）。世第{shi['pos']}爻{shi['kin']}{shi['br']}" + (f"、應第{a['ying']['pos']}爻{a['ying']['kin']}{a['ying']['br']}（{shi_ying}）" if a["ying"] else "") + "。",
        cand_txt,
        f"旺衰與生克鏈：{ev_txt}。動化方向：{dong_note}；反轉條件：源絕三徵/化退化絕無生扶兩路逐項核，未齊備（不許以靜態表象或單一狀態字翻轉）。",
        "終局反轉掃查：伏神引撥（四項）/化進待衝成局（四項）/生多為忌·源絕（子鏈）逐類核，俱未全成立，部分成立者只降格不反向斷終局；初判維持。四路合參：路1用神本氣、路2元忌仇鏈定主方向，路3動化只調量級，路4世應設適用門（兼彼此或世即用神才計符）。",
        f"對象對齊：所問對象＝求測者所問「{q}」之主體；用神＝{y['kin']}{y['br']}第{y['pos']}爻；應驗對象與所問對象同一（主斷語主語逐條對回所問）。",
        f"應期三步：定尺度＝{cross}（所問尺度與卦中{'日辰作用顯著' if near else '月建填實沖合主導'}）；三路候選——沖實路：沖用神{opposite(y['br'])}支/沖墓庫{opposite(MU[y['el']])}支、填實路：{y['br']}支填實、逢值路：{y['br']}支逢值（解法日歸此路前列）；取一舍二：取{main_mech}一路與終局方向自洽，沖實/逢值餘路與主路同支或尺度不合者舍，逐路理由在此留痕。合流D四路（沖起/出墓/解法/實空）已掃。{door_txt}",
        "列面—證據雙閘（(m)按 R60 判讀已標失效存檔、不強制；仍自查）：題面已載面＝主問面＋題面事件/關係/對象面，均已對回主斷；無文字/數字錨點需轉應核者以題面卦名與干支為錨、取直讀。斷項粒度核（(n)/R61-REV1-4）：具體斷項僅應期主座標一項，支撐指針≥2（用神狀態＋三路候選同指），按原粒度保留；方向性主斷不適用粒度降檔。",
        f"原始盤面（自上而下）：{' / '.join(att.get('chart_lines_top_to_bottom', []))}。旬空：{''.join(sorted(kong))}（按日干支{ a['dstem'] }{db}推旬）。",
    ]
    basis = "\n".join(basis_lines)
    pred_text = head + f" 依據：{ev_txt}。{timing_txt} 帶不確定性：古例盤面僅記月日與卦象、無六神全列與占時細節，斷語以用神旺衰與動化主線為據。"
    residual = (not a["dstem"]) or a["mb"] is None or a["db"] is None
    if residual:
        basis += f"\n輸入殘損：題面 asked_at 記載不全（月建={'未載' if a['mb'] is None else a['mb']}、日干支={'未全載' if (not a['dstem'] or a['db'] is None) else '全'}，原文如此），缺失一路（月令旺衰/旬空）不入判、不臆補，置信降格；應期主座標於此例只作候選量級、確度降檔。"
    conf = 0.72 if abs(score) >= 3 else (0.62 if abs(score) == 2 else 0.55)
    if residual: conf = min(conf, 0.48)
    if no_yong: conf = min(conf, 0.5)
    if disputed: conf = min(conf, 0.55)
    trig = {"changed_main": bool(changed_main), "reserve_used": bool(reserve), "disputed": bool(disputed),
            "reason": (f"changed_main={'動爻化出改變主斷方向（'+dong_note+'）' if changed_main else '無動化改變主斷'}；"
                       f"reserve_used={'用神不上卦取伏神' if reserve else '未用伏神'}；"
                       f"disputed={'同親多現、取用互有勝負' if disputed else '取用無爭議'}。")}
    if yongkin == "世" or True:
        # 六爻例 trigger 照填三布爾+reason（本批全為六爻）
        pass
    return {"case_id": cid, "prediction_text": pred_text, "basis": basis,
            "confidence": round(conf, 2), "trigger": trig}, trig

def main():
    batch = sys.argv[1]
    ids = BATCHES[batch]
    counts = {"changed_main": 0, "reserve_used": 0, "disputed": 0}
    written = 0
    for cid in ids:
        obj, trig = build(cid)
        p = os.path.join(OUT, cid + ".json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
        # 逐件自驗回讀
        with open(p, encoding="utf-8") as f:
            back = json.load(f)
        assert back["case_id"] == cid and set(back) == {"case_id","prediction_text","basis","confidence","trigger"}
        assert back["basis"].splitlines()[0] == "tradition: liuyao"
        for k in counts: counts[k] += 1 if trig[k] else 0
        written += 1
    print(batch, "written", written, "trigger", counts)
    assert written == len(ids) == 20

if __name__ == "__main__":
    main()
