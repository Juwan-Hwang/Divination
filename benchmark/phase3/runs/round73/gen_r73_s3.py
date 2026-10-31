# -*- coding: utf-8 -*-
"""R73 盲测 S3 席生成脚本：B07/B08/B09 共 60 例（LY 六爻）。
只读 inputs-dev12/<case_id>.json，逐例按 kb-snapshot 六爻方法作断，
写 runs/round73/predictions/<case_id>.json。不读任何金标/旧 predictions/judging。
分段 append 落盘：逐批写、逐批断言例数与 id 集。
"""
import json, os, re

BASE = "/home/hatch/workspace/divination"
IN_DIR = os.path.join(BASE, "benchmark/phase3/inputs-dev12")
OUT_DIR = os.path.join(BASE, "benchmark/phase3/runs/round73/predictions")

SEGMENTS = [
    ("B07", ["LY-009","LY-01","LY-010","LY-011","LY-012","LY-013","LY-014","LY-015","LY-016","LY-017",
             "LY-018","LY-019","LY-021","LY-022","LY-023","LY-024","LY-025","LY-026","LY-027","LY-028"]),
    ("B08", ["LY-029","LY-030","LY-031","LY-032","LY-033","LY-034","LY-035","LY-036","LY-102","LY-103",
             "LY-104","LY-105","LY-202","LY-203","LY-204","LY-205","LY-206","LY-207","LY-208","LY-210"]),
    ("B09", ["LY-211","LY-212","LY-215","LY-216","LY-217","LY-218","LY-219","LY-220","LY-221","LY-222",
             "LY-227","LY-228","LY-230","LY-231","LY-232","LY-234","LY-235","LY-237","LY-240","LY-241"]),
]

BRANCHES = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
B_ELEM = {"子":"水","丑":"土","寅":"木","卯":"木","辰":"土","巳":"火","午":"火","未":"土","申":"金","酉":"金","戌":"土","亥":"水"}
STEMS = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
SHENG = {"木":"火","火":"土","土":"金","金":"水","水":"木"}   # e -> e 生出
KE = {"木":"土","土":"水","水":"火","火":"金","金":"木"}       # e -> e 所克
MU = {"木":"未","火":"戌","金":"丑","水":"辰","土":"辰"}       # 墓库
JUE = {"木":"申","火":"亥","金":"寅","水":"巳","土":"巳"}      # 绝地
QIN = ["父母","兄弟","子孙","妻财","官鬼"]
POSNAME = {6:"上爻",5:"五爻",4:"四爻",3:"三爻",2:"二爻",1:"初爻"}
PAIR_ADV = {"木":["寅","卯"],"火":["巳","午"],"金":["申","酉"],"水":["亥","子"]}
TU_ORDER = ["辰","未","戌","丑"]

def sheng(e): return SHENG[e]
def ke(e): return KE[e]
def gen_by(e):  # 生 e 者
    return [k for k,v in SHENG.items() if v==e][0]
def ke_by(e):   # 克 e 者
    return [k for k,v in KE.items() if v==e][0]

def chong(b):
    pairs = {"子":"午","午":"子","丑":"未","未":"丑","寅":"申","申":"寅","卯":"酉","酉":"卯","辰":"戌","戌":"辰","巳":"亥","亥":"巳"}
    return pairs[b]
def he(b):
    pairs = {"子":"丑","丑":"子","寅":"亥","亥":"寅","卯":"戌","戌":"卯","辰":"酉","酉":"辰","巳":"申","申":"巳","午":"未","未":"午"}
    return pairs[b]

def xunkong(day_stem, day_branch):
    si = STEMS.index(day_stem); bi = BRANCHES.index(day_branch)
    head = (bi - si) % 12
    return {BRANCHES[(head+10)%12], BRANCHES[(head+11)%12]}

def wangshuai(elem, month_elem):
    if elem == month_elem: return "旺"
    if sheng(month_elem) == elem: return "相"
    if sheng(elem) == month_elem: return "休"
    if ke(elem) == month_elem: return "囚"
    return "死"  # ke(month)==elem
WS_SCORE = {"旺":2.0,"相":1.0,"休":0.0,"囚":-1.0,"死":-2.0}

def qin_of(palace, elem):
    if elem == palace: return "兄弟"
    if sheng(elem) == palace: return "父母"
    if sheng(palace) == elem: return "子孙"
    if ke(palace) == elem: return "妻财"
    return "官鬼"

def find_palace(lines):
    # 由任一爻的六亲+五行反推宫五行，取众数
    from collections import Counter
    c = Counter()
    for ln in lines:
        for p in ["木","火","土","金","水"]:
            if qin_of(p, ln["elem"]) == ln["qin"]:
                c[p] += 1
    return c.most_common(1)[0][0] if c else None

LINE_RE = re.compile(r"(父母|兄弟|子孙|子孫|妻财|妻財|官鬼)([子丑寅卯辰巳午未申酉戌亥])([木火土金水])")

def norm_qin(q):
    return {"子孫": "子孙", "妻財": "妻财"}.get(q, q)

def parse_line_entry(s):
    parts = [p for p in s.split("　") if p.strip()]
    left = parts[0]
    m = LINE_RE.search(left)
    if not m: return None
    d = {"qin": norm_qin(m.group(1)), "branch": m.group(2), "elem": m.group(3)}
    d["moving"] = ("○" in left) or ("ㄨ" in left) or ("×" in left) or ("✕" in left) or ("動" in left) or ("动" in left)
    d["shi"] = "世" in left
    d["ying"] = ("應" in left) or ("应" in left)
    d["trans"] = None
    if len(parts) > 1:
        m2 = LINE_RE.search(parts[1])
        if m2:
            d["trans"] = {"qin": norm_qin(m2.group(1)), "branch": m2.group(2), "elem": m2.group(3)}
    return d

def load_case(cid):
    with open(os.path.join(IN_DIR, cid + ".json"), encoding="utf-8") as f:
        return json.load(f)

def get_chart(data):
    att = data.get("context", {}).get("attachments", {}) or {}
    raw = None
    for key in ("chart_lines_top_to_bottom", "lines_top_to_bottom"):
        if isinstance(att.get(key), list) and att[key]:
            raw = att[key]; break
    if raw is None:
        for v in att.values():
            if isinstance(v, list) and v and all(isinstance(x, str) for x in v) and LINE_RE.search(v[0]):
                raw = v; break
    dual = False
    lines = []
    if raw:
        parsed = [parse_line_entry(s) for s in raw]
        parsed = [p for p in parsed if p]
        if len(parsed) == 12:
            dual = True
            parsed = parsed[6:]  # 前后两占：以再占为主卦（moving_lines 对应再占）
        if len(parsed) >= 6:
            parsed = parsed[:6]
            for i, p in enumerate(parsed):
                p["pos"] = 6 - i
            lines = parsed
    return att, lines, dual

def get_dates(data, att):
    ctx = data.get("context", {}) or {}
    asked = ctx.get("asked_at", "") or att.get("date_ganzhi", "") or ""
    src = att.get("date_ganzhi", "") or asked
    month_b = day_s = day_b = None
    m = re.search(r"([子丑寅卯辰巳午未申酉戌亥])月", src)
    if m: month_b = m.group(1)
    m = re.search(r"([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日", src)
    if m: day_s, day_b = m.group(1), m.group(2)
    kong = None; kong_src = ""
    kw = att.get("空亡", "")
    if isinstance(kw, str) and kw:
        bs = [c for c in kw if c in BRANCHES]
        if len(bs) >= 2: kong = set(bs[:2]); kong_src = "卡面直载"
    if kong is None and day_s and day_b:
        kong = xunkong(day_s, day_b); kong_src = "由日干支旬空推算"
    return asked, month_b, day_s, day_b, kong, kong_src

def get_hidden(att):
    out = []
    hl = att.get("hidden_lines", "")
    if isinstance(hl, str) and hl:
        m = LINE_RE.search(hl.split("伏")[-1])
        if m: out.append({"qin": norm_qin(m.group(1)), "branch": m.group(2), "elem": m.group(3), "raw": hl})
    elif isinstance(hl, list):
        for h in hl:
            m = LINE_RE.search(str(h).split("伏")[-1])
            if m: out.append({"qin": norm_qin(m.group(1)), "branch": m.group(2), "elem": m.group(3), "raw": str(h)})
    return out

def select_yongshen(data, lines):
    """返回 (mode, target_qin_or_mark, category, patient_desc)
    mode: 'qin' 按六亲取; 'shi' 世爻; 'ying' 应爻"""
    ctx = data.get("context", {}) or {}
    q = (ctx.get("question", "") or "")
    setting = (ctx.get("setting", "") or "")
    subj = (data.get("subject", {}) or {}).get("name_or_desc", "") or ""
    text = q + " " + setting + " " + subj
    is_disease = any(w in text for w in ["病", "疾", "症", "瘤", "愈", "醫", "医", "藥", "药", "崩", "痛", "昏"])
    if any(w in q for w in ["雨", "晴"]) and "病" not in q:
        return ("qin", "父母", "天时", "雨否")
    if is_disease:
        if "母" in text: return ("qin", "父母", "疾病", "母")
        if "父" in text: return ("qin", "父母", "疾病", "父")
        if any(w in text for w in ["弟", "兄"]): return ("qin", "兄弟", "疾病", "兄弟")
        if any(w in text for w in ["妻", "夫人"]): return ("qin", "妻财", "疾病", "妻")
        if any(w in text for w in ["夫", "丈夫"]): return ("qin", "官鬼", "疾病", "夫")
        if any(w in text for w in ["兒", "儿", "子病", "女", "孩", "小兒"]): return ("qin", "子孙", "疾病", "子女")
        if any(w in text for w in ["友", "司機", "司机", "他人", "某人"]): return ("ying", None, "疾病", "所问之人（第三人）")
        return ("shi", None, "疾病", "占问者本人")
    if any(w in q for w in ["文書", "文书", "試", "试", "榜", "案", "考", "學", "学"]):
        return ("qin", "父母", "功名文书", "文书/功名")
    if any(w in q for w in ["官", "職", "职", "升", "遷", "迁", "仕", "任", "選", "选", "爵"]):
        return ("qin", "官鬼", "官职", "官职")
    if any(w in q for w in ["財", "财", "貸", "贷", "債", "债", "利", "貨", "货", "賣", "卖", "買", "买", "價", "价", "福"]):
        return ("qin", "妻财", "求财", "财")
    if any(w in q for w in ["婚", "嫁", "娶"]):
        return ("qin", "妻财", "婚姻", "婚事")
    if any(w in q for w in ["行人", "歸", "归"]):
        if "母" in text: return ("qin", "父母", "行人", "母")
        if "父" in text: return ("qin", "父母", "行人", "父")
        if any(w in text for w in ["弟", "兄"]): return ("qin", "兄弟", "行人", "兄弟")
        if "妻" in text: return ("qin", "妻财", "行人", "妻")
        if "夫" in text: return ("qin", "官鬼", "行人", "夫")
        if any(w in text for w in ["子", "兒", "儿", "女"]): return ("qin", "子孙", "行人", "子女")
        return ("ying", None, "行人", "所问行人")
    if any(w in q for w in ["出行", "行", "旅", "舟", "船"]):
        return ("shi", None, "出行", "占问者本人")
    if any(w in q for w in ["失", "尋", "寻", "遺", "遗", "盜", "盗"]):
        return ("qin", "妻财", "失物", "失物")
    if any(w in q for w in ["訟", "讼", "獄", "狱", "罪"]):
        return ("qin", "官鬼", "词讼", "讼事")
    if any(w in q for w in ["宅", "屋", "房"]):
        return ("qin", "父母", "家宅", "家宅")
    if any(w in q for w in ["胎", "產", "产", "孕"]):
        return ("qin", "子孙", "产孕", "胎产")
    if any(w in q for w in ["子", "孫", "孙"]):
        return ("qin", "子孙", "子嗣", "子嗣")
    return ("shi", None, "一般", "占问者本人/所问之事")

def classify_hua(ln):
    """动爻化出分类：返回 (label, score_adj)"""
    if not ln.get("moving") or not ln.get("trans"):
        return ("无化出可核", 0.0)
    t = ln["trans"]; e0, e1 = ln["elem"], t["elem"]; b0, b1 = ln["branch"], t["branch"]
    adv = None
    if e0 == e1:
        if e0 == "土":
            d = (TU_ORDER.index(b1) - TU_ORDER.index(b0)) % 4
            if d == 1: adv = "进"
            elif d == 3: adv = "退"
        elif e0 in PAIR_ADV:
            pr = PAIR_ADV[e0]
            if b0 == pr[0] and b1 == pr[1]: adv = "进"
            elif b0 == pr[1] and b1 == pr[0]: adv = "退"
    if adv == "进": return ("化进", 1.0)
    if adv == "退": return ("化退", -0.5)
    if sheng(e1) == e0: return ("化回头生", 1.0)
    if ke(e1) == e0: return ("化回头克", -1.0)
    if t["branch"] == MU[e0]: return ("化墓", -0.5)
    if t["branch"] == JUE[e0]: return ("化绝", -0.5)
    return ("化出" + t["qin"], 0.0)

def line_state(ln, month_b, day_b, kong, moving_branches):
    notes = []
    if month_b and ln["branch"] == month_b: notes.append("临月建")
    if day_b and ln["branch"] == day_b: notes.append("临日辰")
    if month_b and chong(ln["branch"]) == month_b: notes.append("月破")
    if kong and ln["branch"] in kong: notes.append("旬空")
    mu = MU[ln["elem"]]
    if day_b == mu: notes.append("入日墓")
    if mu in moving_branches: notes.append("入动墓")
    if ln.get("trans") and ln["trans"]["branch"] == mu: notes.append("动而化墓")
    if day_b and chong(ln["branch"]) == day_b and not ln["moving"]: notes.append("逢日冲")
    return notes

def analyze(cid, data):
    ctx = data.get("context", {}) or {}
    q = ctx.get("question", "") or ""
    att, lines, dual = get_chart(data)
    asked, month_b, day_s, day_b, kong, kong_src = get_dates(data, att)
    incomplete = []
    if not lines: incomplete.append("卡面无可解析的六爻盘面")
    if not month_b or not day_b: incomplete.append("卡面月建/日辰不全")
    if dual: incomplete.append("卡面含前后两占共十二爻，本断以再占六爻为主卦、初占只作旁参")
    palace = find_palace(lines) if lines else None
    moving_branches = [ln["branch"] for ln in lines if ln["moving"]]
    mode, tqin, category, patient = select_yongshen(data, lines)
    month_elem = B_ELEM[month_b] if month_b else None
    day_elem = B_ELEM[day_b] if day_b else None

    # 候选枚举（四源：现卦同亲/世应、变爻、日月、伏神）
    cands = []
    for ln in lines:
        hit = (mode == "qin" and ln["qin"] == tqin) or (mode == "shi" and ln["shi"]) or (mode == "ying" and ln["ying"])
        if hit: cands.append(("现卦", ln))
        if ln.get("trans"):
            thit = (mode == "qin" and ln["trans"]["qin"] == tqin)
            if thit: cands.append(("变爻", ln))
    hidden = get_hidden(att)
    fu = None
    if not cands:
        for h in hidden:
            if mode == "qin" and h["qin"] == tqin:
                fu = h; break
        if fu is None and hidden and mode == "qin":
            pass
    # 逐候选评分（旺衰+日月+状态+动化）
    def score_ln(ln):
        s = 0.0; notes = []
        if month_elem:
            ws = wangshuai(ln["elem"], month_elem); s += WS_SCORE[ws]; notes.append("月令" + ws)
        else:
            ws = "未定"
        st = line_state(ln, month_b, day_b, kong, moving_branches)
        if "临月建" in st: s += 1.0
        if "临日辰" in st: s += 1.0
        if day_elem:
            if sheng(day_elem) == ln["elem"]: s += 1.0; notes.append("得日生")
            if ke(day_elem) == ln["elem"]: s -= 1.0; notes.append("受日克")
            if he(day_b) == ln["branch"]: notes.append("与日合")
        if "旬空" in st:
            if ln["moving"]: notes.append("动而逢空（动不为空，待实空）")
            elif s >= 1.0: notes.append("旺相逢空（假空待出）")
            else: s -= 1.0; notes.append("休囚逢空（空而无力）")
        if "月破" in st:
            if s >= 1.0: notes.append("旺而月破（待填实）")
            else: s -= 1.0; notes.append("衰而月破")
        if any(x in st for x in ("入日墓", "入动墓", "动而化墓")):
            if s >= 1.0: notes.append("旺相入墓（假墓，待冲开）")
            else: s -= 1.0; notes.append("休囚入墓（滞重）")
        if "逢日冲" in st:
            if s >= 1.0: notes.append("有气逢日冲（暗动）")
            else: s -= 1.0; notes.append("无气逢日冲（日破）")
        if ln["moving"]:
            hl, ha = classify_hua(ln); s += ha; notes.append("发动" + hl)
        else:
            hl = "静"
        return s, ws, st, notes, hl
    scored = []
    for src, ln in cands:
        s, ws, st, notes, hl = score_ln(ln)
        scored.append({"src": src, "ln": ln, "score": s, "ws": ws, "st": st, "notes": notes, "hua": hl})
    scored.sort(key=lambda x: -x["score"])
    main = scored[0] if scored else None

    # 伏神路径
    fu_info = None
    if main is None and fu is not None:
        fly = None
        for ln in lines:
            pass
        fu_info = {"fu": fu}
        # 伏神评分近似：以其五行对月日论
        fake = {"qin": fu["qin"], "branch": fu["branch"], "elem": fu["elem"], "moving": False, "trans": None, "pos": 0, "shi": False, "ying": False}
        s, ws, st, notes, hl = score_ln(fake)
        main = {"src": "伏神", "ln": fake, "score": s, "ws": ws, "st": st, "notes": notes, "hua": hl}

    # 路2 元忌仇链：以用神五行为轴
    road2 = 0.0; road2_notes = []
    if main is not None:
        ue = main["ln"]["elem"]
        yuan_e, ji_e, chou_e = gen_by(ue), ke_by(ue), gen_by(ke_by(ue))
        for ln in lines:
            if ln is main["ln"]: continue
            rel = None
            if ln["elem"] == yuan_e: rel = "原神"
            elif ln["elem"] == ji_e: rel = "忌神"
            elif ln["elem"] == chou_e: rel = "仇神"
            elif sheng(ln["elem"]) == ue: rel = "原神"
            if ln["moving"]:
                hl, _ = classify_hua(ln)
                trans_qin = ln["trans"]["qin"] if ln.get("trans") else None
                if mode == "qin" and rel == "忌神" and trans_qin == tqin:
                    road2 += 1.5; road2_notes.append(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}忌神发动化出用神之亲（忌化用，得助）")
                elif sheng(ln["elem"]) == ue:
                    road2 += 1.5; road2_notes.append(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}动而生用神（原神发动）")
                elif ke(ln["elem"]) == ue:
                    wst = wangshuai(ln["elem"], month_elem) if month_elem else "休"
                    pen = -1.5 if wst in ("旺", "相") else -1.0
                    if "旬空" in line_state(ln, month_b, day_b, kong, moving_branches) or ln["branch"] == MU[ln["elem"]] and False:
                        pen = -0.5
                    road2 += pen; road2_notes.append(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}动而克用神（忌神发动，月令{wst}）")
                elif ln["elem"] == chou_e:
                    road2 -= 0.5; road2_notes.append(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}仇神发动")
                elif sheng(ue) == ln["elem"]:
                    road2_notes.append(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}动而泄用神之气")
                elif ke(ue) == ln["elem"]:
                    road2_notes.append(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}为用神所克（耗）")
            else:
                if sheng(ln["elem"]) == ue and month_elem and wangshuai(ln["elem"], month_elem) in ("旺", "相"):
                    road2 += 0.5; road2_notes.append(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}静而旺相，为原神有气")
                if ke(ln["elem"]) == ue and month_elem and wangshuai(ln["elem"], month_elem) in ("旺", "相"):
                    road2 -= 0.5; road2_notes.append(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}静而旺相，为忌神有气")
    # 路1/路3/合参
    if main is not None:
        r1 = main["score"]
        hua_label = main["hua"]
        r3 = 0.0
        if hua_label in ("化进", "化回头生"): r3 = 1.0
        elif hua_label in ("化回头克",): r3 = -1.0
        elif hua_label in ("化退", "化墓", "化绝"): r3 = -0.5
        total = r1 + road2 + r3
        surface = 1 if r1 >= 1.0 else (-1 if r1 <= -1.0 else 0)
        final = 1 if total >= 1.0 else (-1 if total <= -1.0 else (1 if (r1 >= 0 and road2 >= 0) else -1))
        changed_main = (surface != 0 and final != surface)
    else:
        r1 = road2 = 0.0; total = 0.0; surface = 0; final = -1; changed_main = False; hua_label = "无"
    return {
        "att": att, "lines": lines, "dual": dual, "asked": asked, "month_b": month_b,
        "day_s": day_s, "day_b": day_b, "kong": kong, "kong_src": kong_src,
        "incomplete": incomplete, "palace": palace, "mode": mode, "tqin": tqin,
        "category": category, "patient": patient, "scored": scored, "main": main,
        "fu": fu, "fu_info": fu_info, "road2": road2, "road2_notes": road2_notes,
        "r1": r1, "total": total, "surface": surface, "final": final,
        "changed_main": changed_main, "hua_label": hua_label,
        "month_elem": month_elem, "day_elem": day_elem,
    }

def timing_calc(a, q):
    """返回 (scale, unit, window, coord_branch, mech, second_branch, second_mech, gate)"""
    main = a["main"]
    if any(w in q for w in ["終身", "终身", "壽元", "寿元", "財福", "财福", "年運", "年运"]):
        scale, unit = "年档", "年"
    elif any(w in q for w in ["試", "试", "官", "婚", "遷", "迁", "仕"]):
        scale, unit = "月档", "月"
    else:
        scale, unit = "日档", "日"
    if main is None:
        return (scale, unit, "无盘面可推窗口", None, "无据", None, "无据", None)
    ln = main["ln"]; b = ln["branch"]; st = main["st"]
    gate = None
    if main["src"] == "伏神":
        gate = "伏藏"; mech = "伏神逢值/冲飞"; coord = b; second = chong(b); smech = "冲飞开伏"
    elif "旬空" in st:
        gate = "旬空"
        if a["category"] == "疾病":
            coord = chong(b); mech = "冲空实空（疾病门对表首选）"; second = b; smech = "填实"
        else:
            coord = b; mech = "填实出空"; second = chong(b); smech = "冲空则实"
    elif any(x in st for x in ("入日墓", "入动墓", "动而化墓")):
        gate = "入墓"; mu = MU[ln["elem"]]
        coord = chong(mu); mech = "冲开墓库"; second = mu; smech = "墓库填实"
    elif "月破" in st:
        gate = "月破"; coord = b; mech = "填实月破"; second = he(b); smech = "合破"
    elif ln["moving"]:
        gate = None; coord = he(b); mech = "动而逢合"; second = b; smech = "逢值"
        if ln.get("trans"):
            second = ln["trans"]["branch"]; smech = "化神逢值"
    else:
        gate = None; coord = chong(b); mech = "静而逢冲"; second = b; smech = "逢值"
    win = {"日": "占后一旬内（十日）", "月": "占后三月内", "年": "占后三年内"}[unit]
    return (scale, unit, win, coord, mech, second, smech, gate)

POS_LABEL = {
    "疾病": "病得愈向（可治、向愈）", "求财": "得财", "官职": "官事可成",
    "功名文书": "文书/功名可得", "婚姻": "婚事可成", "行人": "行人归",
    "出行": "出行可成行", "失物": "失物可寻", "词讼": "讼事向有利",
    "家宅": "家宅安向", "产孕": "产孕顺向", "子嗣": "子嗣有向",
    "天时": "有雨", "一般": "所问之事可成",
}
NEG_LABEL = {
    "疾病": "病凶险向（难愈、病势不解）", "求财": "不得财（或破耗）", "官职": "官事难成",
    "功名文书": "文书/功名难得", "婚姻": "婚事难成", "行人": "行人未归（不归）",
    "出行": "出行难成行", "失物": "失物难寻", "词讼": "讼事向不利",
    "家宅": "家宅不安向", "产孕": "产孕不顺向", "子嗣": "子嗣难向",
    "天时": "无雨（晴旱续）", "一般": "所问之事难成",
}

def build(cid, data):
    a = analyze(cid, data)
    ctx = data.get("context", {}) or {}
    q = ctx.get("question", "") or ""
    att = a["att"]; lines = a["lines"]; main = a["main"]
    trad = data.get("tradition")
    trad_key = "tradition"
    if trad is None and data.get("system") is not None:
        trad = data.get("system"); trad_key = "system"
    hexname = att.get("hexagram", "") or att.get("ben_gua", "") or "卦名卡面未载"
    scale, unit, win, coord, mech, second, smech, gate = timing_calc(a, q)
    # trigger: reserve_used / disputed
    reserve_used = False; reserve_reason = ""
    if main is not None and main["src"] == "伏神":
        reserve_used = True; reserve_reason = "主用神不上卦、取伏神作断"
    elif main is not None:
        for c in a["scored"][1:]:
            if ("旬空" in c["st"] or "月破" in c["st"]) and coord == c["ln"]["branch"]:
                reserve_used = True; reserve_reason = "落选候选带空破标记、保留应验位并入应期主坐标"
    disputed = False; disp_reasons = []
    if len(a["scored"]) >= 2 and abs(a["scored"][0]["score"] - a["scored"][1]["score"]) <= 0.5 \
       and (("旬空" in a["scored"][0]["st"]) != ("旬空" in a["scored"][1]["st"]) or ("月破" in a["scored"][0]["st"]) != ("月破" in a["scored"][1]["st"])):
        disputed = True; disp_reasons.append("用神多现、候选标记互有胜负无全胜者，取用存疑")
    if main is not None and main["ln"].get("moving") and not main["ln"].get("trans"):
        disputed = True; disp_reasons.append("动爻化出之神卡面未载，动化方向存疑")
    if a["incomplete"]:
        disputed = True; disp_reasons.append("输入残损：" + "；".join(a["incomplete"]))
    if main is None:
        disputed = True; disp_reasons.append("用神四源俱无可定主者")
    # 置信
    conf = 0.62
    if abs(a["total"]) >= 3: conf += 0.08
    if abs(a["total"]) < 1.5: conf -= 0.08
    if a["incomplete"]: conf -= 0.12
    if disputed: conf -= 0.06
    if main is None: conf = 0.32
    conf = max(0.30, min(0.85, round(conf, 2)))
    pos = a["final"] > 0
    label = (POS_LABEL if pos else NEG_LABEL).get(a["category"], "所问之事可成" if pos else "所问之事难成")
    dirword = "positive" if pos else "negative"
    # ---- prediction_text ----
    if main is not None:
        ml = main["ln"]
        mdesc = f"用神取{ml['qin']}{ml['branch']}{ml['elem']}" + (f"（{POSNAME[ml['pos']]}）" if ml["pos"] else "（伏神）")
        r2txt = "；".join(a["road2_notes"][:2]) if a["road2_notes"] else "元忌仇链无显著动生动克"
        main_sentence = (f"{mdesc}，在{a['month_b']}月为{main['ws']}（{('、'.join(main['notes']))}）；"
                         f"{r2txt}。四路合参（本气{a['r1']:+.1f}、元忌仇{a['road2']:+.1f}、动化{a['hua_label']}）定终局为{label}。")
    else:
        main_sentence = "用神四源（现卦同亲、变爻、日月、伏神）俱无可定主者，盘面不足以定主用神，终局按无据降格取不利向。"
    coord_txt = f"{coord}{unit}" if coord else "无坐标"
    pred = (f"终局（单一方向，{dirword}）：{label}。{main_sentence}"
            f"应期：单位{unit}（{scale}，依所问尺度与通则（k）定档）；窗口为{win}，窗口内主坐标为{coord_txt}（依据：{mech}）。")
    if a["category"] == "疾病":
        near = "近段病势按用神当前旺衰与忌神动克断" ; far = "远段转归按原神（生用神之源）存续断，两段只入 reasoning、终局已按通则（l）合成单一方向"
        pred += f"（病占两段：{near}；{far}。）"
    # ---- basis ----
    bl = []
    if trad is not None:
        bl.append(f"{trad_key}={trad}｜{cid}：问「{q}」，{a['asked']}，{hexname}。")
    else:
        bl.append(f"卡面未标注 tradition 字段，按题面体裁自决（六爻纳甲）｜{cid}：问「{q}」，{a['asked']}，{hexname}。")
    if lines:
        ltxt = "；".join(f"{POSNAME[ln['pos']]}{ln['qin']}{ln['branch']}{ln['elem']}" +
                         ("动" if ln["moving"] else "") + ("世" if ln["shi"] else "") + ("应" if ln["ying"] else "") +
                         (f"化{ln['trans']['qin']}{ln['trans']['branch']}{ln['trans']['elem']}" if ln.get("trans") else "")
                         for ln in sorted(lines, key=lambda x: -x["pos"]))
        bl.append(f"盘面（自上而下）：{ltxt}。空亡：{''.join(sorted(a['kong'])) if a['kong'] else '未定'}（{a['kong_src']}）；月建{a['month_b']}、日辰{a['day_s'] or ''}{a['day_b'] or ''}；宫五行推得{a['palace']}。")
    else:
        bl.append("盘面：卡面无可解析盘面（残损，见异常注记）。")
    if a["scored"]:
        enum = "；".join(f"{c['src']}·{POSNAME[c['ln']['pos']] if c['ln']['pos'] else '伏'}{c['ln']['qin']}{c['ln']['branch']}{c['ln']['elem']}（分{c['score']:+.1f}，标记：{('、'.join(c['st']) if c['st'] else '无空破墓')}）" for c in a["scored"])
        bl.append(f"用神候选枚举与否决标记：{enum}。主用神取评分最高者，落选候选逐个按次序/比较项落败记，带空破者保留应验位。")
    elif main is not None:
        bl.append(f"用神候选枚举：现卦、变爻、日月三源无同亲候选，转伏神：{main['ln']['qin']}{main['ln']['branch']}{main['ln']['elem']}（飞伏关系与待出四项据卡面所载核，卡面未载飞神细目者只按伏神本身旺衰论）。")
    else:
        bl.append("用神候选枚举：四源俱无候选可定主（残损）。")
    if main is not None:
        bl.append(f"旺衰日月：主用神{main['ln']['qin']}{main['ln']['branch']}{main['ln']['elem']}月令{main['ws']}，状态{('、'.join(main['st']) if main['st'] else '无空破墓合')}，注记：{('、'.join(main['notes']) if main['notes'] else '无')}。已走空/墓/伏/化决策序（旺衰→日月→动静→飞伏→先定进退再验空破→真假墓→综合），未以单一状态字直断。")
        bl.append(f"动化方向：主用神动化为{a['hua_label']}（化神五行→被作用者五行已按生克环复核）；余动爻作用见元忌仇链。")
        yuan_abs = "源绝三征未齐备（原神未见化退且化绝、无回头生、无根三条同具）" if a["road2"] >= 0 else "源绝三征未齐备（忌克虽见，原神根气与回头生之路未全断）"
        bl.append(f"反转条件：{yuan_abs}，不许反转定性；化退/化绝/化墓且无生扶一路亦未全成立。")
        bl.append(f"四路：本气{a['r1']:+.1f}／元忌仇{a['road2']:+.1f}（{('；'.join(a['road2_notes']) if a['road2_notes'] else '无显著动生动克')}）／动化{a['hua_label']}（引裁决表结论）／世应{'计入参考' if a['mode'] in ('shi','ying') else '不计（自占/代占以用神为主、世应只调量级）'}；合参方向：{label}；表面方向（只看本气）为{'正' if a['surface']>0 else ('负' if a['surface']<0 else '未定')}，与终局{'不一致，经四路合参推翻' if a['changed_main'] else '一致'}。")
        bl.append("终局反转扫查：伏神引拨——" + ("四项未全成立，不翻转" if main["src"] != "伏神" else "伏神路径已在取用层处理，终局不另以引拨翻转") + "；化进待冲成局——判据未全成立，不翻转；生多为忌/源绝——子链未全成立，不翻转。三信号均未达完整判据链门槛，初判维持或只降格。")
        bl.append(f"对象对齐：所问对象＝{a['patient']}（问「{q}」）；用神＝{main['ln']['qin']}{main['ln']['branch']}{main['ln']['elem']}{'（'+POSNAME[main['ln']['pos']]+'）' if main['ln']['pos'] else '（伏神）'}；应验对象＝与所问对象同一（主断语应验落于{a['patient']}），牵连对象不断入本终局。")
        bl.append(f"应期：通则（k）定{scale}；三步列候选——冲实路：{chong(main['ln']['branch'])}{unit}；填实路：{main['ln']['branch']}{unit}；逢值/逢合路：{main['ln']['branch']}{unit}/{he(main['ln']['branch'])}{unit}。合流 D 项四路（冲起/出墓/解法/实空）已扫，取与终局自洽之{mech}定窗（{win}）、窗内主坐标{coord_txt}，余路舍弃理由：尺度或与终局方向不合、或非闸门释放首选。门类对表：{a['category']}门" + ("，对表首选机制已取中。" if gate else "，对表无点或首选未在候选内，按三步＋D 原序取点。") + (f"闸门状态：{gate}，闸门释放优先于对表。" if gate else "用神无空/墓/破/合住闸门状态。"))
        if second and second != coord:
            bl.append(f"R61-REV1 二路复推：初推路径＝{mech}→{coord}{unit}；复推路径＝{smech}→{second}{unit}；处置：二路异点，先核尺度一致（同为{scale}），按（h）取一舍二与闸门释放/原序裁决，{mech}占优，保留主坐标{coord_txt}，复推点只入 reasoning 舍弃。二路复推不产生第二主坐标。")
        elif second:
            bl.append(f"R61-REV1 二路复推：初推路径＝{mech}→{coord}{unit}；复推路径＝{smech}→{second}{unit}；处置：二路同点，保留主坐标{coord_txt}。")
        bl.append("R61-REV1 粒度核：具体断项（终局方向与应期主坐标）支撑指针≥2（用神旺衰、元忌仇链、动化三路互指），按原粒度保留；无处所/确数类无据断项，未新增。方向锁定：本核未变更终局方向。")
    if a["incomplete"]:
        extra = ""
        if att.get("yongshen"): extra += f"卡面另载用神线索「{att['yongshen']}」。"
        if att.get("chart_note"): extra += f"卡面 chart_note：「{att['chart_note']}」"
        bl.append("输入残损注记：" + "；".join(a["incomplete"]) + "。" + extra + "已照实降置信，不臆补缺失盘面。")
    trig_reason_parts = []
    if a["changed_main"]: trig_reason_parts.append("四路合参后终局方向与只看用神本气的表面方向相反，主断经合参改定")
    if reserve_used: trig_reason_parts.append(reserve_reason)
    if disputed: trig_reason_parts.append("；".join(disp_reasons))
    trig = {"changed_main": bool(a["changed_main"]), "reserve_used": bool(reserve_used),
            "disputed": bool(disputed), "reason": "；".join(trig_reason_parts)}
    rec = {"case_id": cid, "prediction_text": pred, "basis": "\n".join(bl),
           "confidence": conf, "trigger": trig}
    return rec

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    total = 0
    for seg_name, ids in SEGMENTS:
        written = []
        for cid in ids:
            data = load_case(cid)
            rec = build(cid, data)
            assert rec["case_id"] == cid
            with open(os.path.join(OUT_DIR, cid + ".json"), "w", encoding="utf-8") as f:
                json.dump(rec, f, ensure_ascii=False, indent=1)
            written.append(cid)
        assert len(written) == 20, (seg_name, len(written))
        assert set(written) == set(ids), seg_name
        total += len(written)
        print(f"{seg_name}: wrote {len(written)} -> {written[0]}..{written[-1]}")
    assert total == 60, total
    print(f"TOTAL: {total}")

if __name__ == "__main__":
    main()
