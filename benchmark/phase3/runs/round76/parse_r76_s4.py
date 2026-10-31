# -*- coding: utf-8 -*-
"""R76 S4 stage2: parse charts, compute wangshuai/relations. Analysis aid only."""
import json, os, re
BASE = "/home/hatch/workspace/divination/benchmark/phase3"
IDS = ["LY-242","LY-243","LY-244","LY-245","LY-246","LY-249","LY-250","LY-251","LY-252","LY-253",
"LY-254","LY-255","LY-259","LY-301","LY-304","LY-305","LY-306","LY-307","LY-309","LY-311",
"LY-312","LY-314","LY-315","LY-318","LY-319","LY-320","LY-322","LY-323","LY-324","LY-325",
"LY-328","LY-329","LY-330","LY-331","LY-332","LY-333","LY-335","LY-336","LY-338","LY-339",
"LY-340","LY-342","LY-344","LY-402","LY-403","LY-404","LY-405","LY-406","LY-407","LY-408",
"LY-411","LY-413","LY-415","LY-416","LY-417","LY-418","LY-421","LY-423","LY-424","LY-425"]
BR = "子丑寅卯辰巳午未申酉戌亥"
EL = {"子":"水","丑":"土","寅":"木","卯":"木","辰":"土","巳":"火","午":"火","未":"土","申":"金","酉":"金","戌":"土","亥":"水"}
GAN = "甲乙丙丁戊己庚辛壬癸"
SHENG = {"木":"火","火":"土","土":"金","金":"水","水":"木"}
KE = {"木":"土","土":"水","水":"火","火":"金","金":"木"}
def rel(a, b):  # a element vs b element: a生b etc
    if a == b: return "同"
    if SHENG[a] == b: return "生"
    if KE[a] == b: return "克"
    if SHENG[b] == a: return "被生"
    if KE[b] == a: return "被克"
CHONG = {BR[i]: BR[(i+6) % 12] for i in range(12)}
HE = {"子":"丑","丑":"子","寅":"亥","亥":"寅","卯":"戌","戌":"卯","辰":"酉","酉":"辰","巳":"申","申":"巳","午":"未","未":"午"}
JIN = {"寅":"卯","巳":"午","申":"酉","亥":"子","丑":"辰","辰":"未","未":"戌","戌":"丑"}
TUI = {v: k for k, v in JIN.items()}
MU = {"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}
XUN_KONG = {}
for s in range(0, 60, 10):
    start = s  # jiazi index of xun start (甲子=0)
    present = set()
    for i in range(10):
        idx = (start + i) % 60
        present.add(BR[idx % 12])
    XUN_KONG[s] = [b for b in BR if b not in present]
def jiazi(g, z):
    return (GAN.index(g) * 10 + 0)  # placeholder unused
def kong_of(day_gz):
    g, z = day_gz[0], day_gz[1]
    # find jiazi index
    for i in range(60):
        if GAN[i % 10] == g and BR[i % 12] == z:
            start = (i // 10) * 10
            pres = {BR[(start + j) % 12] for j in range(10)}
            return "".join(b for b in BR if b not in pres)
    return "?"
QIN = ["父母","兄弟","子孫","妻財","官鬼"]
def parse_line(s):
    toks = []
    for m in re.finditer(r"(父母|兄弟|子孫|子孙|妻財|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([金木水火土])", s):
        toks.append((m.group(1), m.group(2), m.group(3)))
    moving = ("ㄨ" in s) or ("○" in s) or ("○" in s)
    return toks, moving
out = []
for cid in IDS:
    with open(os.path.join(BASE, "inputs-dev12", cid + ".json"), encoding="utf-8") as f:
        d = json.load(f)
    ctx = d.get("context", {}); att = ctx.get("attachments", {}) or {}
    out.append("="*16 + " " + cid + " | Q:" + str(ctx.get("question")))
    dg = att.get("date_ganzhi")
    asked = str(ctx.get("asked_at") or "")
    if not dg:
        m = re.search(r"([子丑寅卯辰巳午未申酉戌亥])月([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日", asked)
        if m: dg = m.group(1) + "月" + m.group(2) + m.group(3) + "日"
    month_br = day_gz = None
    if dg:
        mm = re.search(r"([子丑寅卯辰巳午未申酉戌亥])月([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日", dg)
        if mm:
            month_br = mm.group(1); day_gz = mm.group(2) + mm.group(3)
    if not month_br:
        out.append("DATE: 未明記 (asked_at=" + asked + ")")
    kong = att.get("空亡") or (kong_of(day_gz) if day_gz else "?")
    if day_gz:
        out.append(f"DATE: {month_br}月 {day_gz}日 空亡={kong}")
    mel = EL[month_br] if month_br else None
    del_ = EL[day_gz[1]] if day_gz else None
    lines = att.get("chart_lines_top_to_bottom") or []
    parsed = []
    for s in lines:
        toks, moving = parse_line(s)
        shi = "世" in s.split("　")[0] if s else False
        # shi/ying may appear anywhere in本卦 side; approximate: search before变卦 token region
        parsed.append((s, toks, moving))
    n = len(parsed)
    for i, (s, toks, moving) in enumerate(parsed):
        pos = n - i  # 6 top .. 1 bottom
        if not toks:
            out.append(f" L{pos}: UNPARSED {s}"); continue
        q, b, e = toks[0]
        tag = ""
        # shi ying: look in raw string segment up to second token start
        seg = s
        if "世" in seg: tag += " [含世字]"
        if "應" in seg or "应" in seg: tag += " [含應字]"
        ws = ""
        if mel:
            r = rel(e, mel)
            ws = {"同":"旺","被生":"相","生":"休","克":"囚","被克":"死"}[r]
        dr = ""
        if day_gz:
            db = day_gz[1]
            parts = []
            if b == db: parts.append("臨日")
            if CHONG[b] == db: parts.append("日沖")
            if HE.get(b) == db: parts.append("日合")
            rr = rel(e, del_)
            parts.append("日" + {"同":"同","生":"生之","克":"克之","被生":"生它泄","被克":"被它克"}[rr] if False else "")
            # clearer: day element acts on line
            if SHENG[del_] == e: parts.append("日生爻")
            elif KE[del_] == e: parts.append("日克爻")
            elif SHENG[e] == del_: parts.append("爻生日泄")
            elif KE[e] == del_: parts.append("爻克日")
            else: parts.append("日同")
            if b in str(kong): parts.append("旬空")
            if CHONG[b] == month_br: parts.append("月破")
            dr = " ".join(p for p in parts if p)
        tr = ""
        if moving and len(toks) > 1:
            q2, b2, e2 = toks[1]
            jr = "化進" if JIN.get(b) == b2 else ("化退" if TUI.get(b) == b2 else "")
            rb = rel(e2, e)  # 化神 vs 本爻
            rbname = {"生":"回頭生","克":"回頭克","同":"比和","被生":"化泄(本生化)","被克":"化克本?"}[rb]
            # careful: rel(e2,e): 生 means 化神生本爻
            tr = f" -> 化{q2}{b2}{e2} [{jr}{rbname}]"
            if b2 in str(kong): tr += " 化神空"
            if month_br and CHONG[b2] == month_br: tr += " 化神月破"
        out.append(f" L{pos}: {q}{b}{e} {'動' if moving else '靜'} 月:{ws} {dr}{tr}{tag} || {s}")
    hl = att.get("hidden_lines")
    if hl: out.append(" hidden: " + str(hl))
    if att.get("yongshen"): out.append(" yongshen(卡載): " + str(att["yongshen"]))
    out.append(" hex: " + str(att.get("hexagram")) + " | moving: " + str(att.get("moving_lines")))
with open(os.path.join(BASE, "runs/round76/analysis_r76_s4.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("done")
