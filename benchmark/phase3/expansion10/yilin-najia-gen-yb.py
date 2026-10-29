# -*- coding: utf-8 -*-
"""
易林补遗批专用纳甲装卦生成器（expansion10 唯一脚本名，勿他批复用改名）。
口径照易冒批：原文散文体无装卦表，据本卦/变卦名与占日按通行纳甲法则复原；
动爻由本变卦爻位异同唯一确定（原文另明言动爻者从原文）；化爻干支取变卦本位、
六亲以本卦宫五行为准。伏神定位照通行法：本卦所缺六亲，取本宫首卦同位之爻伏于本卦同位飞神之下
（已以《易林补遗》原文四处自叙互证：晋子水伏初爻土下、睽子水伏未土下、大畜申金伏三爻辰土下、归妹亥水伏四爻下）。
校验：以《易隐》YY-001（萃之困）原书卦表逐爻比对。
"""
import json, sys

# 八卦：名 -> (爻位自下而上阴阳, 五行, 内卦天干, 外卦天干, 内卦地支(自下而上), 外卦地支)
TRI = {
    "乾": ((1,1,1), "金", "甲", "壬", ("子","寅","辰"), ("午","申","戌")),
    "坤": ((0,0,0), "土", "乙", "癸", ("未","巳","卯"), ("丑","亥","酉")),
    "震": ((1,0,0), "木", "庚", "庚", ("子","寅","辰"), ("午","申","戌")),
    "巽": ((0,1,1), "木", "辛", "辛", ("丑","亥","酉"), ("未","巳","卯")),
    "坎": ((0,1,0), "水", "戊", "戊", ("寅","辰","午"), ("申","戌","子")),
    "离": ((1,0,1), "火", "己", "己", ("卯","丑","亥"), ("酉","未","巳")),
    "艮": ((0,0,1), "土", "丙", "丙", ("辰","午","申"), ("戌","子","寅")),
    "兑": ((1,1,0), "金", "丁", "丁", ("巳","卯","丑"), ("亥","酉","未")),
}
BR_EL = {"子":"水","亥":"水","丑":"土","辰":"土","未":"土","戌":"土",
         "寅":"木","卯":"木","巳":"火","午":"火","申":"金","酉":"金"}
NAMES = {  # (上卦, 下卦) -> 卦名
    ("乾","乾"):"乾为天",("乾","坤"):"天地否",("乾","坎"):"天水讼",("乾","艮"):"天山遁",
    ("乾","震"):"天雷无妄",("乾","巽"):"天风姤",("乾","离"):"天火同人",("乾","兑"):"天泽履",
    ("坤","坤"):"坤为地",("坤","乾"):"地天泰",("坤","坎"):"地水师",("坤","艮"):"地山谦",
    ("坤","震"):"地雷复",("坤","巽"):"地风升",("坤","离"):"地火明夷",("坤","兑"):"地泽临",
    ("坎","坎"):"坎为水",("坎","乾"):"水天需",("坎","坤"):"水地比",("坎","艮"):"水山蹇",
    ("坎","震"):"水雷屯",("坎","巽"):"水风井",("坎","离"):"水火既济",("坎","兑"):"水泽节",
    ("艮","艮"):"艮为山",("艮","乾"):"山天大畜",("艮","坤"):"山地剥",("艮","坎"):"山水蒙",
    ("艮","震"):"山雷颐",("艮","巽"):"山风蛊",("艮","离"):"山火贲",("艮","兑"):"山泽损",
    ("震","震"):"震为雷",("震","乾"):"雷天大壮",("震","坤"):"雷地豫",("震","坎"):"雷水解",
    ("震","艮"):"雷山小过",("震","巽"):"雷风恒",("震","离"):"雷火丰",("震","兑"):"雷泽归妹",
    ("巽","巽"):"巽为风",("巽","乾"):"风天小畜",("巽","坤"):"风地观",("巽","坎"):"风水涣",
    ("巽","艮"):"风山渐",("巽","震"):"风雷益",("巽","离"):"风火家人",("巽","兑"):"风泽中孚",
    ("离","离"):"离为火",("离","乾"):"火天大有",("离","坤"):"火地晋",("离","坎"):"火水未济",
    ("离","艮"):"火山旅",("离","震"):"火雷噬嗑",("离","巽"):"火风鼎",("离","兑"):"火泽睽",
    ("兑","兑"):"兑为泽",("兑","乾"):"泽天夬",("兑","坤"):"泽地萃",("兑","坎"):"泽水困",
    ("兑","艮"):"泽山咸",("兑","震"):"泽雷随",("兑","巽"):"泽风大过",("兑","离"):"泽火革",
}
SHORT = {v: (v[-2:] if not v.startswith(("乾为","坤为","坎为","艮为","震为","巽为","离为","兑为")) else v[-1]) for v in NAMES.values()}
for k in list(SHORT):
    pass
# 短名映射（单字卦名如晋、睽、师……）由全名尾字/尾二字生成有歧义，改用显式表：
SHORT2FULL = {}
for full in NAMES.values():
    if full[1] == "为":
        SHORT2FULL[full[2]] = full
    else:
        SHORT2FULL[full[2:]] = full

def rel(palace_el, el):
    if el == palace_el: return "兄弟"
    gen = {"金":"水","水":"木","木":"火","火":"土","土":"金"}   # 生
    ctl = {"金":"木","木":"土","土":"水","水":"火","火":"金"}   # 克
    if gen[palace_el] == el: return "子孙"
    if gen[el] == palace_el: return "父母"
    if ctl[palace_el] == el: return "妻财"
    if ctl[el] == palace_el: return "官鬼"
    raise ValueError

def palace_of(bits):
    """bits: 6 自下而上。返回 (宫名, 世位, 序名)"""
    for pal, t in TRI.items():
        tb = t[0] + t[0]
        flips = [{}, {0}, {0,1}, {0,1,2}, {0,1,2,3}, {0,1,2,3,4}, {0,1,2,4}, {4}]
        labels = ["本宫","一世","二世","三世","四世","五世","游魂","归魂"]
        shi = [6,1,2,3,4,5,4,3]
        for fs, lab, s in zip(flips, labels, shi):
            b = tuple(1-x if i in fs else x for i, x in enumerate(tb))
            if b == bits:
                return pal, s, lab
    raise ValueError("no palace")

def chart(full_name):
    up = down = None
    for (u, d), n in NAMES.items():
        if n == full_name:
            up, down = u, d
            break
    bits = TRI[down][0] + TRI[up][0]
    pal, shi, lab = palace_of(bits)
    pal_el = TRI[pal][1]
    lines = []  # 自下而上: (六亲, 干支, 五行)
    for pos in range(1, 7):
        tri = TRI[down] if pos <= 3 else TRI[up]
        stem = tri[2] if pos <= 3 else tri[3]
        br = (tri[4] if pos <= 3 else tri[5])[pos-1 if pos <= 3 else pos-4]
        el = BR_EL[br]
        lines.append((rel(pal_el, el), stem + br, el))
    ying = shi + 3 if shi <= 3 else shi - 3
    return {"name": full_name, "palace": pal, "palace_label": lab, "shi": shi,
            "ying": ying, "lines": lines, "bits": bits, "palace_el": pal_el}

def hidden(full_name):
    """缺失六亲的伏神：[(位, 伏神六亲干支, 飞神六亲干支)]"""
    c = chart(full_name)
    head = chart(TRI[c["palace"]][0] and NAMES[(c["palace"], c["palace"])])
    present = {l[0] for l in c["lines"]}
    out = []
    for pos in range(1, 7):
        r, gz, el = head["lines"][pos-1]
        if r not in present:
            out.append((pos, f"{r}{gz}{el}", f"{c['lines'][pos-1][0]}{c['lines'][pos-1][1]}{c['lines'][pos-1][2]}"))
    return out

def describe(base_full, moving=None, changed_full=None):
    """moving: 动爻位列表(自下而上1-6)。changed_full 与 moving 二选一（由异同推动爻）。"""
    c = chart(base_full)
    if changed_full and not moving:
        cb = chart(changed_full)["bits"]
        moving = [i+1 for i in range(6) if cb[i] != c["bits"][i]]
    moving = moving or []
    cc = None
    if moving:
        bits2 = tuple(1-x if (i+1) in moving else x for i, x in enumerate(c["bits"]))
        nm = [n for (u, d), n in NAMES.items() if TRI[d][0] + TRI[u][0] == bits2][0]
        cc = chart(nm)
    lines_out = []
    for pos in range(6, 0, -1):
        r, gz, el = c["lines"][pos-1]
        s = f"{r}{gz}{el}"
        if pos == c["shi"]: s += " 世"
        if pos == c["ying"]: s += " 应"
        if pos in moving: s += "（动）"
        lines_out.append(s)
    mv_desc = []
    for pos in moving:
        r, gz, el = c["lines"][pos-1]
        tag = "（世爻）" if pos == c["shi"] else ("（应爻）" if pos == c["ying"] else "")
        if cc:
            r2, gz2, el2 = cc["lines"][pos-1]
            r2b = rel(c["palace_el"], el2)
            mv_desc.append(f"{['','初','二','三','四','五','上'][pos]}爻{r}{gz}{el}动{tag}，化{r2b}{gz2}{el2}")
        else:
            mv_desc.append(f"{['','初','二','三','四','五','上'][pos]}爻{r}{gz}{el}动{tag}")
    return {"base": c, "changed_name": cc["name"] if cc else None,
            "chart_lines_top_to_bottom": lines_out,
            "moving_lines_text": "；".join(mv_desc) if mv_desc else "六爻安静",
            "hidden": hidden(base_full)}

if __name__ == "__main__":
    # 校验一：《易隐》YY-001 萃之困 原书卦表
    d = describe("泽地萃", changed_full="泽水困")
    expect = ["父母丁未土", "兄弟丁酉金 应", "子孙丁亥水", "妻财乙卯木", "官鬼乙巳火 世（动）", "父母乙未土"]
    got = d["chart_lines_top_to_bottom"]
    print("萃之困 chart:", got)
    print("MATCH YY-001:", got == expect, "| 化爻:", d["moving_lines_text"])
    # 校验二：易林补遗原文自叙四处伏神定位
    for nm, want in [("火地晋", (1, "子孙甲子水")), ("火泽睽", (5, "妻财丙子水")),
                     ("山天大畜", (3, "子孙丙申金")), ("雷泽归妹", (4, "子孙丁亥水"))]:
        h = hidden(nm)
        ok = any(p == want[0] and g == want[1] for p, g, f in h)
        print(nm, "伏神:", h, "MATCH:", ok)
    # 校验三：原文自叙世位/爻支抽查
    d = describe("天风姤")
    print("姤:", d["chart_lines_top_to_bottom"], "世", d["base"]["shi"])
    d = describe("泽山咸", moving=[2, 5])
    print("咸2,5动:", d["chart_lines_top_to_bottom"], "| 变:", d["changed_name"], "|", d["moving_lines_text"])
    d = describe("雷天大壮", changed_full="火天大有")
    print("大壮之大有:", d["chart_lines_top_to_bottom"], "|", d["moving_lines_text"])
    d = describe("地水师", moving=[2, 6])
    print("师2,6动:", d["chart_lines_top_to_bottom"], "| 变:", d["changed_name"], "|", d["moving_lines_text"])
    d = describe("泽地萃", moving=[6])
    print("萃上六动:", d["chart_lines_top_to_bottom"], "| 变:", d["changed_name"], "|", d["moving_lines_text"])
    d = describe("风水涣", changed_full="天风姤")
    print("涣之姤:", d["chart_lines_top_to_bottom"], "|", d["moving_lines_text"])
    d = describe("风地观", changed_full="风雷益")
    print("观之益:", d["chart_lines_top_to_bottom"], "|", d["moving_lines_text"])
