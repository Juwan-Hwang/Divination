# -*- coding: utf-8 -*-
"""R78 S5 liuyao engine: builds prediction dicts from parsed cards (method: kb-snapshot SKILL + chinese-liuyao-meihua)."""
import re
from gen_r78_s5_parse import parse_card, BR, EL, GEN, KE

OPP = {BR[i]: BR[(i+6) % 12] for i in range(12)}
HE = {frozenset(p): p for p in [("子","丑"),("寅","亥"),("卯","戌"),("辰","酉"),("巳","申"),("午","未")]}
def he_partner(b):
    for p in [("子","丑"),("寅","亥"),("卯","戌"),("辰","酉"),("巳","申"),("午","未")]:
        if b in p: return p[0] if p[1] == b else p[1]
    return None
TOMB = {"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}
TRI_BITS = {(1,1,1):"乾",(1,1,0):"兌",(1,0,1):"離",(1,0,0):"震",(0,1,1):"巽",(0,1,0):"坎",(0,0,1):"艮",(0,0,0):"坤"}
TRI_EL = {"乾":"金","兌":"金","離":"火","震":"木","巽":"木","坎":"水","艮":"土","坤":"土"}
NAJIA_FIRST = {"乾":["子","寅","辰","午","申","戌"],"坤":["未","巳","卯","丑","亥","酉"],
 "震":["子","寅","辰","午","申","戌"],"巽":["丑","亥","酉","未","巳","卯"],
 "坎":["寅","辰","午","申","戌","子"],"離":["卯","丑","亥","酉","未","巳"],
 "艮":["辰","午","申","戌","子","寅"],"兌":["巳","卯","丑","亥","酉","未"]}

def qin_of(pal_el, el):
    if el == pal_el: return "兄弟"
    if GEN[pal_el] == el: return "子孫"
    if GEN[el] == pal_el: return "父母"
    if KE[pal_el] == el: return "妻財"
    return "官鬼"  # KE[el]==pal_el

def palace_and_shi(lines):
    bits = {L["pos"]: (1 if L["main"].get("yang") else 0) for L in lines}
    lower = (bits[1], bits[2], bits[3]); upper = (bits[4], bits[5], bits[6])
    lt, ut = TRI_BITS.get(lower), TRI_BITS.get(upper)
    if not lt or not ut: return None, None, lt, ut
    for pname, pbits in [(k, tuple(1 if TRI_BITS[b] == k else 0 for b in [])) for k in []]:
        pass
    # generate palace series
    def bits_of(name):
        return {v: k for k, v in TRI_BITS.items()}[name]
    for pname in TRI_BITS.values():
        pb = bits_of(pname)
        def flip(t, i): 
            t = list(t); t[i] = 1 - t[i]; return tuple(t)
        l1 = flip(pb, 0); l12 = flip(l1, 1); l123 = flip(l12, 2)
        u1 = flip(pb, 0); u12 = flip(u1, 1)
        series = [((pb, pb), 6), ((l1, pb), 1), ((l12, pb), 2), ((l123, pb), 3),
                  ((l123, u1), 4), ((l123, u12), 5), ((l123, u1), 4), ((pb, u12), 3)]
        # fix yu-hun: upper = flip back line4 only from wushi upper -> u2 = flip(u12,0)=u1? standard: youhun upper differs from ben by line4 only of upper relative to wushi: use (l123, u1) is sishi; youhun = (l123, flip(u12,0))
        series[6] = ((l123, flip(u12, 0)), 4)
        for (lo, up), shi in series:
            if lo == lower and up == upper:
                return pname, shi, lt, ut
    return None, None, lt, ut

def month_grade(el, month_br):
    if not month_br: return 0, "月建未載、不計"
    me = EL[month_br]
    if el == me: return 2, "旺"
    if GEN[me] == el: return 1, "相"
    if GEN[el] == me: return 0, "休"
    if KE[el] == me: return -1, "囚"
    return -2, "死"

def day_score(br, el, day_br, grade):
    if not day_br: return 0, []
    notes = []; s = 0; de = EL[day_br]
    if br == day_br: s += 2; notes.append("臨日辰")
    if GEN[de] == el: s += 1; notes.append("日生")
    if de == el: s += 1; notes.append("日同氣")
    if he_partner(br) == day_br: s += 1; notes.append("日合")
    if OPP[br] == day_br:
        if grade >= 1: s += 1; notes.append("日沖有氣判暗動")
        else: s -= 2; notes.append("日沖無氣判日破")
    if KE[de] == el: s -= 1; notes.append("日克")
    return s, notes

def line_states(L, c, grade_map):
    mn = L["main"]; b, e = mn["br"], mn["el"]
    st = []
    if b in c["kong"]: st.append("旬空")
    if c["month_br"] and OPP[b] == c["month_br"]: st.append("月破")
    tomb = TOMB[e]
    tomb_src = []
    if c["day_gz"] and c["day_gz"][1] == tomb: tomb_src.append("日")
    if c["month_br"] == tomb: tomb_src.append("月")
    for o in c["lines"]:
        if o["main"].get("moving") and o["main"]["br"] == tomb: tomb_src.append("動爻")
    if tomb_src: st.append("入墓(" + "/".join(tomb_src) + "墓)")
    return st

def hua_kind(mn, ch):
    """return (kind, desc) kind in 進/退/回頭生/回頭克/泄/耗/同支"""
    if ch is None or not ch.get("br"): return "無變爻", ""
    b, cb = mn["br"], ch["br"]; e, ce = mn["el"], ch["el"]
    if b == cb: return "同支", f"化{ch['qin']}{cb}{ce}、支同不論進退"
    d = (BR.index(cb) - BR.index(b)) % 12
    if GEN[ce] == e: return "回頭生", f"化{ch['qin']}{cb}{ce}回頭生本爻"
    if KE[ce] == e: return "回頭克", f"化{ch['qin']}{cb}{ce}回頭克本爻"
    if e == ce and (d == 1 or d == 3): return "進", f"化{ch['qin']}{cb}{ce}為進神"
    if e == ce and (d == 11 or d == 9): return "退", f"化{ch['qin']}{cb}{ce}為退神"
    if GEN[e] == ce: return "泄", f"化{ch['qin']}{cb}{ce}、本爻生化神主泄"
    if KE[e] == ce: return "耗", f"化{ch['qin']}{cb}{ce}、本爻克化神主耗"
    return "他變", f"化{ch['qin']}{cb}{ce}"

CAT_TABLE = {  # 對表門類 (from method table)
 "疾病": "疾病門：首選沖空實空之日（用神動空/化空、近病）、次選實破/沖去克神之日",
 "行人": "行人門：首選按用神狀態對位（伏藏出現日/動逢合日/化退歸期）、次選沖開墓合之月日",
 "求財": "求財門：首選財臨日月待入墓之日、次選世動逢合之日",
 "功名發案": "功名發案門：首選按父母狀態五分對位（衰取生旺日、旺靜逢值沖、動逢值合、空墓待沖開、破空填實）",
 "出行": "出行門：首選世旺靜逢沖之日、次選沖開之日月",
 "婚姻": "婚姻門：首選動而空者實空之月日、次選動而破者實破之時",
 "終身財福": "終身財福門：首選逢生之年/沖空實空之年、次選墓沖開之年",
 "壽元": "壽元門：首選動逢合逢值之年/靜逢值逢沖之年",
}

def categorize(c):
    q, s = c["question"], c["setting"]
    t = q + "｜" + s
    if any(k in t for k in ["陰晴", "何日晴", "何日雨", "久雪", "連日雪", "連日雨", "月令"]):
        return "天時", None
    if "援例" in s and "流年" in q: return "功名", "官鬼"
    if any(k in t for k in ["附子", "牛黃丸"]): return "疾病用藥", None
    if "病" in t: return "疾病", None
    if "終身財福" in t: return "終身財福", "妻財"
    if "終身功名" in t: return "終身功名", "官鬼"
    if "終身" in t: return "終身", "世爻"
    if any(k in t for k in ["道考", "歲考"]): return "考試", "父母"
    if any(k in t for k in ["候文書"]): return "文書", "父母"
    if any(k in t for k in ["具題"]): return "文書", "父母"
    if any(k in t for k in ["功名", "關差", "掣籤", "援例", "復職", "升遷", "升否", "上書", "自陳", "大計"]):
        return "功名", "官鬼"
    if any(k in t for k in ["夫婦", "婚姻", "和好"]): return "婚姻", "官鬼"
    if any(k in t for k in ["母在外", "何時來", "何日回", "何日歸", "僕何日"]): return "行人", None
    if any(k in t for k in ["家宅", "墳地", "地形勢", "入宅"]): return "家宅", "父母"
    if "夢" in t: return "夢占", "世爻"
    if any(k in t for k in ["避亂", "防流兵", "避誤", "保全"]): return "趨避", "世爻"
    if any(k in t for k in ["貿易", "買", "賣", "收貨", "囤", "店", "房價", "得利", "貨"]):
        return "求財", "妻財"
    return "一般", "官鬼"

def person_qin(c):
    t = c["question"] + c["setting"]
    if "父" in t: return "父母"
    if "母" in t: return "父母"
    if "兄" in t: return "兄弟"
    if re.search(r"子病|占子|兒", t): return "子孫"
    if any(k in t for k in ["小廝", "僕"]): return "妻財"
    return "世爻"

