# -*- coding: utf-8 -*-
"""R78 S5 parser: reads ONLY assigned inputs-dev12 cards, prints compact summaries to stdout.
Writes nothing except (when run with 'write' arg) prediction files under runs/round78/predictions/."""
import json, os, re, sys

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
IDS = {
 "B13": ["LY-426","LY-427","LY-428","LY-429","LY-430","LY-432","LY-433","LY-434","LY-436","LY-437","LY-439","LY-440","LY-441","LY-442","LY-443","LY-445","LY-446","LY-449","LY-451","LY-452"],
 "B14": ["LY-454","LY-455","LY-457","LY-458","LY-501","LY-502","LY-503","LY-504","LY-505","LY-506","LY-507","LY-508","LY-509","LY-510","LY-511","LY-512","LY-513","LY-514","LY-515","LY-516"],
 "B15": ["LY-517","LY-518","LY-519","LY-520","LY-521","LY-522","LY-523","LY-524","LY-525","LY-526","LY-527","LY-528","LY-529","LY-530","LY-531","LY-532","LY-533","LY-534","LY-535","LY-536"],
}
BR = "子丑寅卯辰巳午未申酉戌亥"
STEM = "甲乙丙丁戊己庚辛壬癸"
EL = {"子":"水","亥":"水","寅":"木","卯":"木","巳":"火","午":"火","申":"金","酉":"金","辰":"土","戌":"土","丑":"土","未":"土"}
GEN = {"木":"火","火":"土","土":"金","金":"水","水":"木"}   # X生GEN[X]
KE  = {"木":"土","土":"水","水":"火","火":"金","金":"木"}   # X克KE[X]
QIN = ["父母","兄弟","子孫","妻財","官鬼"]

def xun_kong(day_gz):
    s, b = day_gz[0], day_gz[1]
    si, bi = STEM.index(s), BR.index(b)
    start = (bi - si) % 12  # 旬首支
    return [BR[(start+10)%12], BR[(start+11)%12]]

def parse_card(cid):
    with open(f"{BASE}/inputs-dev12/{cid}.json", encoding="utf-8") as f:
        card = json.load(f)
    ctx = card.get("context", {})
    att = ctx.get("attachments", {}) or {}
    asked = ctx.get("asked_at","") or ""
    mm = re.search(r"(.)月", asked)
    month_br = mm.group(1) if mm and mm.group(1) in BR else None
    dm = re.search(r"([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日", asked)
    day_gz = (dm.group(1)+dm.group(2)) if dm else None
    lines_raw = att.get("chart_lines_top_to_bottom", []) or []
    multi = len(lines_raw) > 6
    if multi:
        lines_raw = lines_raw[:6]  # primary = first-listed hexagram; rest noted as corroborating casts
    lines = []  # bottom->top after reverse; each dict pos1..6
    for i, raw in enumerate(lines_raw):
        pos = 6 - i
        # split 本卦 / 變卦 parts by runs of spaces (incl fullwidth)
        parts = re.split(r"[ 　]+", raw.strip())
        def parse_part(p):
            qin = next((q for q in QIN if p.startswith(q)), None)
            rest = p[len(qin):] if qin else p
            br = rest[0] if rest else None
            el = rest[1] if len(rest)>1 else None
            moving = ("○" in p) or ("ㄨ" in p) or ("×" in p)
            return {"qin":qin,"br":br,"el":el,"moving":moving,"yang":("⚊" in p),
                    "shi":"世" in p,"ying":"應" in p,"raw":p}
        main = parse_part(parts[0]) if parts else {}
        chg = parse_part(parts[1]) if len(parts)>1 else None
        d = {"pos":pos, "main":main, "chg":chg}
        lines.append(d)
    lines.sort(key=lambda d: d["pos"])
    return {"id":cid, "tradition":card.get("tradition"), "card":card,
            "question":ctx.get("question",""), "setting":ctx.get("setting",""),
            "asked":asked, "month_br":month_br, "day_gz":day_gz,
            "kong": (xun_kong(day_gz) if day_gz else
                     (lambda km: [km.group(1), km.group(2)] if km else [])(
                         re.search(r"空亡(.)(.)", att.get("hexagram","") or ""))),
            "hexagram": att.get("hexagram",""), "moving_text": att.get("moving_lines",""),
            "multi": multi, "lines":lines}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv)>1 else "ALL"
    for b, ids in IDS.items():
        if which not in ("ALL", b): continue
        for cid in ids:
            c = parse_card(cid)
            print(f"== {cid} trad={c['tradition']} Q={c['question']} | {c['setting']} | {c['asked']} 空={''.join(c['kong'])} 卦={c['hexagram']} 動={c['moving_text']}")
            for L in c["lines"]:
                mn, ch = L["main"], L["chg"]
                tag = ("世" if mn.get("shi") else "")+("應" if mn.get("ying") else "")+("動" if mn.get("moving") else "")
                chs = f" -> {ch['qin']}{ch['br']}{ch['el']}" if ch else ""
                print(f"   {L['pos']}爻 {mn['qin']}{mn['br']}{mn['el']} {tag}{chs}")
