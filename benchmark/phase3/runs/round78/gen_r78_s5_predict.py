# -*- coding: utf-8 -*-
"""R78 S5 predict(): per-case liuyao reading per kb-snapshot method."""
import re
from gen_r78_s5_parse import parse_card, BR, EL, GEN, KE
from gen_r78_s5_engine import (OPP, he_partner, TOMB, TRI_EL, NAJIA_FIRST, qin_of,
    palace_and_shi, month_grade, day_score, line_states, hua_kind, categorize,
    person_qin, CAT_TABLE)

def predict(cid):
    c = parse_card(cid)
    lines = c["lines"]
    month_br, day_gz = c["month_br"], c["day_gz"]
    day_br = day_gz[1] if day_gz else None
    pal, shi_calc, lt, ut = palace_and_shi(lines)
    pal_el = TRI_EL.get(pal) if pal else None
    shi_line = next((L for L in lines if L["main"].get("shi")), None)
    ying_line = next((L for L in lines if L["main"].get("ying")), None)
    cat, useqin = categorize(c)
    notes_missing = []
    if not month_br: notes_missing.append("卡面未載月建")
    if not day_gz: notes_missing.append("卡面未載日干支（空亡據卦名括注或不計）")
    if c.get("multi"): notes_missing.append("卡面含多占並列、本斷以卡面首列之卦為主卦、餘卦只作旁參不另立斷")

    if cat == "天時":
        if any(k in c["question"] for k in ["何日雨", "占雨"]): useqin, tian_target = "父母", "雨"
        elif "月令" in c["question"]: useqin, tian_target = "父母", "月令雨晴"
        else: useqin, tian_target = "妻財", "晴"
    elif cat == "疾病":
        useqin = person_qin(c); tian_target = None
    elif cat == "疾病用藥":
        useqin = ("子孫" if "附子" in (c["question"] + c["setting"]) else "父母"); tian_target = None
    elif cat == "行人":
        useqin = person_qin(c); tian_target = None
    else:
        tian_target = None
    if useqin is None: useqin = "官鬼"

    info = {}
    for L in lines:
        mn = L["main"]; g, gname = month_grade(mn["el"], month_br)
        ds, dnotes = day_score(mn["br"], mn["el"], day_br, g)
        st = line_states(L, c, None)
        info[L["pos"]] = {"g": g, "gname": gname, "ds": ds, "dnotes": dnotes, "st": st,
                          "score": g + ds + (2 if mn.get("moving") else 0)}

    cands = []
    if useqin != "世爻":
        for L in lines:
            mn = L["main"]
            if mn["qin"] == useqin:
                cands.append({"src": "現卦", "pos": L["pos"], "br": mn["br"], "el": mn["el"],
                              "moving": bool(mn.get("moving")), "score": info[L["pos"]]["score"],
                              "st": info[L["pos"]]["st"],
                              "desc": f"現卦第{L['pos']}爻{mn['qin']}{mn['br']}{mn['el']}" + ("動" if mn.get("moving") else "靜")})
        for L in lines:
            mn, ch = L["main"], L["chg"]
            if mn.get("moving") and ch and ch.get("qin") == useqin:
                cg, _ = month_grade(ch["el"], month_br)
                cands.append({"src": "變爻", "pos": L["pos"], "br": ch["br"], "el": ch["el"],
                              "moving": True, "score": cg + 1, "st": [],
                              "desc": f"第{L['pos']}爻動化{ch['qin']}{ch['br']}{ch['el']}"})
        if pal_el:
            for lbl, brv in [("月建", month_br), ("日辰", day_br)]:
                if brv and qin_of(pal_el, EL[brv]) == useqin:
                    cands.append({"src": lbl, "pos": None, "br": brv, "el": EL[brv], "moving": False,
                                  "score": 3, "st": [], "desc": f"{lbl}{brv}{EL[brv]}臨{useqin}之親"})
        present = any(x["src"] == "現卦" for x in cands)
        chg_has = any(x["src"] == "變爻" for x in cands)
        if not present and not chg_has and pal:
            for i, fb in enumerate(NAJIA_FIRST[pal]):
                if qin_of(pal_el, EL[fb]) == useqin:
                    fly = lines[i]["main"]
                    cands.append({"src": "伏神", "pos": i + 1, "br": fb, "el": EL[fb], "moving": False,
                                  "score": month_grade(EL[fb], month_br)[0], "st": [],
                                  "desc": f"伏神{useqin}{fb}{EL[fb]}伏於第{i+1}爻{fly['qin']}{fly['br']}{fly['el']}之下（{pal}宮首卦同位）"})
    else:
        if shi_line:
            mn = shi_line["main"]
            cands.append({"src": "現卦", "pos": shi_line["pos"], "br": mn["br"], "el": mn["el"],
                          "moving": bool(mn.get("moving")), "score": info[shi_line["pos"]]["score"],
                          "st": info[shi_line["pos"]]["st"],
                          "desc": f"世爻第{shi_line['pos']}爻{mn['qin']}{mn['br']}{mn['el']}" + ("動" if mn.get("moving") else "靜")})
    tier = {"現卦": 0, "變爻": 1, "月建": 2, "日辰": 2, "伏神": 3, "無候補": 4}
    cands.sort(key=lambda x: (tier.get(x["src"], 9), -x["score"]))
    main_c = cands[0] if cands else None
    disputed_take = bool(len(cands) > 1 and main_c and cands[1]["score"] == main_c["score"]
                         and cands[1]["src"] == main_c["src"])
    reserve_used = bool(main_c and main_c["src"] in ("變爻", "月建", "日辰", "伏神"))
    if main_c is None:
        main_c = {"src": "無候補", "pos": None, "br": day_br or month_br or "子",
                  "el": EL[day_br or month_br or "子"], "moving": False, "score": 0, "st": [],
                  "desc": "四源俱無用神候補、姑以日月之支記其位"}
        disputed_take = True

    ue = main_c["el"]
    yuan_el = next(e for e in ["木", "火", "土", "金", "水"] if GEN[e] == ue)
    ji_el = next(e for e in ["木", "火", "土", "金", "水"] if KE[e] == ue)
    def best_of_el(elx):
        bs = [L for L in lines if L["main"]["el"] == elx]
        return max(bs, key=lambda L: info[L["pos"]]["score"]) if bs else None
    yuan = best_of_el(yuan_el); ji = best_of_el(ji_el)
    sun = gui = None
    if cat in ("疾病", "疾病用藥"):
        sl = [L for L in lines if L["main"]["qin"] == "子孫"]
        gl = [L for L in lines if L["main"]["qin"] == "官鬼"]
        sun = max(sl, key=lambda L: info[L["pos"]]["score"]) if sl else None
        gui = max(gl, key=lambda L: info[L["pos"]]["score"]) if gl else None
        yuan_eff, ji_eff = sun, gui
    else:
        yuan_eff, ji_eff = yuan, ji

    if main_c["src"] == "現卦" and main_c["pos"]:
        r1v = info[main_c["pos"]]["g"] + info[main_c["pos"]]["ds"]
    else:
        r1v = main_c["score"] - (2 if main_c["moving"] else 0)
    r1 = "+" if r1v >= 1 else ("-" if r1v <= -1 else "0")
    def eff_sign():
        ys = info[yuan_eff["pos"]]["score"] if yuan_eff else -9
        js = info[ji_eff["pos"]]["score"] if ji_eff else -9
        ym = bool(yuan_eff and yuan_eff["main"].get("moving"))
        jm = bool(ji_eff and ji_eff["main"].get("moving"))
        if yuan_eff and ys >= 2 and ym and not (ji_eff and js >= 3 and jm): return "+"
        if ji_eff and js >= 2 and jm and not (yuan_eff and ys >= 3): return "-"
        if ji_eff and js >= 3 and jm and (not yuan_eff or ys < 1): return "-"
        if yuan_eff and ys >= 3 and not ji_eff: return "+"
        return "0"
    r2 = eff_sign()

    rel_pos = set()
    if main_c["pos"]: rel_pos.add(main_c["pos"])
    if shi_line: rel_pos.add(shi_line["pos"])
    if yuan_eff: rel_pos.add(yuan_eff["pos"])
    hua_notes = []; r3 = "0"
    for L in lines:
        if not L["main"].get("moving"): continue
        kind, desc = hua_kind(L["main"], L["chg"])
        tag = "（用神/世/原神位）" if L["pos"] in rel_pos else ""
        hua_notes.append(f"第{L['pos']}爻{L['main']['qin']}{L['main']['br']}{L['main']['el']}動：{kind}——{desc}{tag}")
        if L["pos"] in rel_pos:
            if kind in ("進", "回頭生"): r3 = "+"
            elif kind in ("退", "回頭克") and r3 != "+": r3 = "-"
    jinhua = ""
    if ji_eff and ji_eff["main"].get("moving") and ji_eff["chg"] and ji_eff["chg"].get("el") == ue:
        r3 = "+"; jinhua = "忌神動化出用神之五行、按忌化用論（裁決表第2步吉向）"
    r4, r4note = "不計", "非兼彼此之事、世應不入合參（路4適用門不開）"
    if cat == "婚姻" and shi_line and ying_line:
        se, ye = shi_line["main"]["el"], ying_line["main"]["el"]
        if GEN[ye] == se or he_partner(shi_line["main"]["br"]) == ying_line["main"]["br"]:
            r4 = "+"; r4note = "應生世/世應相合、兼彼此之事計符"
        elif KE[ye] == se or OPP[shi_line["main"]["br"]] == ying_line["main"]["br"]:
            r4 = "-"; r4note = "應克世/世應相沖、兼彼此之事計符"
        else:
            r4 = "0"; r4note = "世應無生克沖合、計符為0"

    blocked = False
    if r1 == "+" and r2 != "-": direction, comb = "+", "用神有氣、忌克無力或受制"
    elif r1 == "+" and r2 == "-": direction, comb, blocked = "0", "用神有氣而忌神旺動克用、原神無救——受阻未定", True
    elif r1 in ("-", "0") and r2 == "+": direction, comb = "+", "用神衰弱而得原神/福神生扶——絕處逢生、遲成向"
    elif r1 == "-" and r2 in ("-", "0"): direction, comb = "-", "用神衰弱無力、又無生扶或逢忌克"
    else: direction, comb = "0", "用神與元忌兩路俱中平"
    initial_dir = {"+" : "positive", "-": "negative", "0": "undecided"}[r1]
    if direction == "0":
        if r3 == "+": direction = "+"; comb += "；受阻/未定之局以動化吉向收束為遲成"
        elif r3 == "-": direction = "-"; comb += "；動化凶向收束"
        elif r4 in ("+", "-"): direction = r4; comb += "；以世應次級參考定偏向"
        else:
            pen = 1 if (main_c["st"] and not main_c["moving"] and r1v <= 0) else 0
            direction = "+" if (r1v - pen) > 0 else "-"
            comb += "；終以用神本氣微差定偏向（靜而空破者再扣一檔）、方向存疑降置信"
        blocked = True

    scan = []; flipped = False
    if main_c["src"] == "伏神":
        fb, pos = main_c["br"], main_c["pos"]
        fly = lines[pos - 1]["main"]
        i1 = month_grade(main_c["el"], month_br)[0] >= 1 or fb in (day_br, month_br) or any(
            L["main"].get("moving") and GEN[L["main"]["el"]] == main_c["el"] for L in lines)
        i2 = (fly["br"] in c["kong"]) or (month_br and OPP[fly["br"]] == month_br) or \
             month_grade(fly["el"], month_br)[0] <= -1 or (day_br and OPP[fly["br"]] == day_br)
        i3 = any(L["main"].get("moving") and (GEN[L["main"]["el"]] == main_c["el"] or OPP[L["main"]["br"]] == fly["br"]) for L in lines) \
             or (day_br and OPP[day_br] == fb)
        i4 = not (month_grade(fly["el"], month_br)[0] >= 1 and KE[fly["el"]] == main_c["el"])
        got = [bool(x) for x in (i1, i2, i3, i4)]
        if all(got):
            scan.append("伏神引撥：判據四項全成立（伏有氣/飛神開/引撥路通/無破絕反證）")
            if direction == "-":
                direction = "+"; flipped = True
                scan.append("與初判衝突、復核後按伏出改定終局")
        elif any(got):
            scan.append(f"伏神引撥：部分成立（{sum(got)}/4項、缺項未全）、只降格留餘地不翻轉")
        else:
            scan.append("伏神引撥：無此信號")
    else:
        scan.append("伏神引撥：用神非伏藏、無此信號")
    if r3 == "+" and any("動：進" in h for h in hua_notes):
        scan.append("化進待沖成局：化進已見、餘判據未逐項全備、記部分成立不另翻轉（與合參同向佐證）")
    else:
        scan.append("化進待沖成局：無此信號")
    scan.append("生多為忌/源絕：源絕子鏈四項未全備（原神化退且化絕+無回頭生+無根+用神無自救未同具）、無此信號、初判維持")

    final_positive = (direction == "+")
    changed_main = (initial_dir != "undecided" and ((initial_dir == "positive") != final_positive))

    if cat in ("終身財福", "終身功名", "終身"):
        scale, unit = "年", "年"
    elif cat == "疾病" and "久病" in (c["question"] + c["setting"]):
        scale, unit = "月", "月"
    elif cat == "功名" and any(k in (c["question"] + c["setting"]) for k in ["升遷", "復職"]):
        scale, unit = "月", "月"
    elif cat == "天時" and "月令" in c["question"]:
        scale, unit = "月", "月"
    elif cat == "家宅":
        scale, unit = "月", "月"
    else:
        scale, unit = "日", "日"
    ub = main_c["br"]; ust = main_c["st"]
    if "入墓" in " ".join(ust):
        coord_br, mech = OPP[TOMB[ue]], f"用神入{TOMB[ue]}墓、取沖墓之支開墓"
    elif "旬空" in ust:
        if cat == "疾病": coord_br, mech = OPP[ub], "疾病門對表首選沖空實空之日"
        elif main_c["moving"]: coord_br, mech = ub, "動而逢空、取填實逢值之支（動不為空、應於實空）"
        else: coord_br, mech = OPP[ub], "用神旬空、取沖空則實之支"
    elif "月破" in ust:
        coord_br, mech = ub, "月破取填實之支"
    elif main_c["pos"] and lines[main_c["pos"] - 1]["main"].get("moving"):
        hp = he_partner(ub)
        coord_br, mech = (hp, "動而逢合、取逢合之支") if hp else (ub, "動者取逢值之支")
    elif main_c["pos"] and info[main_c["pos"]]["g"] >= 1:
        coord_br, mech = OPP[ub], "靜而旺相、取逢沖之支"
    else:
        coord_br, mech = ub, "靜者取逢值之支"
    if cat == "天時":
        coord_br, mech = ub, f"{tian_target}象用神逢值之支"
    window = {"日": "占後一旬內（日檔、旬窗）", "月": "占後數月內（月檔）", "年": "終身運程內（年檔）"}[scale]
    timing = f"窗口{window}；主座標：{coord_br}{unit}（{mech}）"

    table_key = {"疾病": "疾病", "行人": "行人", "求財": "求財", "考試": "功名發案",
                 "終身財福": "終身財福", "婚姻": "婚姻"}.get(cat)
    table_note = CAT_TABLE[table_key] if table_key else "對表無此門類、按三步＋合流D原序取點"

    conf = 0.62
    if r1 == "+" and r2 == "+" and not blocked: conf = 0.72
    if blocked or disputed_take: conf = 0.5
    if r1 == "0" and r2 == "0": conf = min(conf, 0.48)
    if notes_missing: conf -= 0.07 * len([n for n in notes_missing if "未載" in n])
    if flipped: conf = min(conf, 0.6)
    conf = round(max(0.3, min(0.8, conf)), 2)

    line_sum = "；".join(
        f"第{L['pos']}爻{L['main']['qin']}{L['main']['br']}{L['main']['el']}"
        + ("（世）" if L["main"].get("shi") else "") + ("（應）" if L["main"].get("ying") else "")
        + ("動" if L["main"].get("moving") else "")
        + (f"→{L['chg']['qin']}{L['chg']['br']}{L['chg']['el']}" if L["main"].get("moving") and L["chg"] else "")
        for L in lines)
    dir_word = "成／吉向（positive）" if final_positive else "不成／凶向（negative）"
    spec = {
        "求財": "財利落點在用神妻財本身之旺衰與原神子孫之源",
        "功名": "功名落點在官鬼（職位/差使）本身、父母文書為佐",
        "考試": "等第落點在父母（文書/試卷）本身、子孫福神為佐",
        "疾病": "愈否落點在所問病人之用神本身、官鬼為病、子孫為醫藥",
        "疾病用藥": "可否落點在所問之藥/病人用神本身、官鬼為病勢",
        "天時": f"所問天象（{tian_target}）落點在{tian_target}象用神與對方象之消長",
        "行人": "歸否落點在所問行人之用神本身",
        "婚姻": "和好/成否落點在世應與用神官鬼（夫位）本身",
        "家宅": "吉凶落點在父母（宅/長輩）本身、世為宅中之人",
        "終身財福": "終身財福落點在妻財與世爻本身",
        "終身功名": "終身功名落點在官鬼與世爻本身",
        "終身": "終身所為落點在世爻本身之旺衰去向",
        "文書": "文書落點在父母（文書）本身",
        "夢占": "夢兆吉凶落點在占者世爻本身",
        "趨避": "趨避吉凶落點在世爻（避難者本人）本身、子孫為平安之象",
        "一般": "成敗落點在用神本身",
    }.get(cat, "成敗落點在用神本身")
    pred_text = (
        f"【原始結果】{c['hexagram']}｜{c['asked']}、旬空{''.join(c['kong']) or '未載'}｜自下而上：{line_sum}。"
        f"【所用之法】六爻納甲（《增刪卜易》用神/旺衰），{cat}門以{useqin}為用神。"
        f"【逐項解讀】主用神：{main_c['desc']}（出自{main_c['src']}源），月令{month_grade(main_c['el'], month_br)[1]}、盤面狀態{('、'.join(main_c['st'])) if main_c['st'] else '無空破墓'}；"
        f"原神（{yuan_eff['main']['el'] if yuan_eff else yuan_el}行）{'第%d爻%s%s%s' % (yuan_eff['pos'], yuan_eff['main']['qin'], yuan_eff['main']['br'], yuan_eff['main']['el']) if yuan_eff else '不上卦'}、忌神（{ji_eff['main']['el'] if ji_eff else ji_el}行）{'第%d爻%s%s%s' % (ji_eff['pos'], ji_eff['main']['qin'], ji_eff['main']['br'], ji_eff['main']['el']) if ji_eff else '不上卦'}"
        + (f"；病象官鬼{'第%d爻' % gui['pos'] if gui else '不上卦'}、醫藥子孫{'第%d爻' % sun['pos'] if sun else '不上卦'}" if cat in ("疾病", "疾病用藥") else "")
        + (f"；{jinhua}" if jinhua else "")
        + f"；動化：{'；'.join(hua_notes) if hua_notes else '靜卦無動化'}。"
        f"【傾向判斷】方向：{dir_word}——{comb}；{spec}，斷語只及此對象、不回收他人。應期（{scale}檔）：{timing}。置信 {conf}。"
        f"【歸檔行】{cid}｜{c['question']}｜六爻納甲｜{main_c['desc']}｜{dir_word}｜應期{coord_br}{unit}"
    )
    trig_parts = []
    trig_parts.append(f"changed_main={'true' if changed_main else 'false'}：初判按用神本氣路1為{r1}（{initial_dir}）、終局為{'positive' if final_positive else 'negative'}" + ("、經合參/掃查改定" if changed_main else "、未改定"))
    trig_parts.append(f"reserve_used={'true' if reserve_used else 'false'}：主用神出自{main_c['src']}源" + ("（備用取用路徑：變爻/日月/伏神）" if reserve_used else "（現卦正取、未用備用路徑）"))
    is_disputed = bool(disputed_take or blocked)
    trig_parts.append(f"disputed={'true' if is_disputed else 'false'}：" + ("取用同分並列或合參受阻未定、方向存疑已降置信" if is_disputed else "取用與合參俱無並列存疑"))
    basis_lines = [
        f"tradition: {c['tradition']}",
        "systems_used: [liuyao]（六爻納甲、單一主法）",
        f"卡面：{cid}｜問：{c['question']}｜{c['setting']}｜{c['asked']}｜卦：{c['hexagram']}" + (f"｜缺損：{'；'.join(notes_missing)}、已降置信不臆補" if notes_missing else ""),
        f"裝卦核對：{pal}宮（下{lt}上{ut}）、生成表世位{shi_calc}與卡面世位{shi_line['pos'] if shi_line else '未標'}對照" + ("一致" if shi_calc == (shi_line['pos'] if shi_line else None) else "未完全對上、以卡面世應標記為準"),
        "用神候補枚舉：" + ("；".join(f"{x['desc']}[{x['src']}、分{x['score']}、狀態{('、'.join(x['st'])) if x['st'] else '無'}]" for x in cands) if cands else "四源俱無候補") +
        f"；定主：{main_c['desc']}（{main_c['src']}源）" + ("；同分並列、記取用存疑" if disputed_take else "；落選候補逐個留痕如上、帶空破者其逢值/出空之期仍入應期候補池"),
        f"旺衰日月：用神{ue}行於{month_br or '未載'}月為{month_grade(ue, month_br)[1]}；日辰{day_gz or '未載'}；空亡{''.join(c['kong']) or '未載'}",
        f"動化方向：{'；'.join(hua_notes) if hua_notes else '靜卦無動化、方向定性無動化可引'}",
        "反轉條件：源絕三征/化退化絕無生扶兩路均未齊備（逐項核：原神化退化絕未同具、伏神引撥未全項）",
        "；".join(scan),
        f"四路：本氣{r1}／元忌仇{r2}／動化{r3}（引裁決表結論）／世應{r4}（{r4note}）；合參方向：{'positive' if final_positive else 'negative'}；表面方向與終局" + ("不一致、經合參/掃查路推翻" if changed_main else "一致"),
        f"對象對齊：所問對象＝{c['question']}之主體；用神＝{main_c['desc']}；應驗對象＝與所問對象同一（{spec}）、牽連對象不另立斷",
        f"應期三步：定尺度{scale}檔（所問性質與卦中時間結構）；三路候選——沖實（沖空/沖墓/沖飛之支）、填實（用神{ub}逢值）、逢值（逢合/逢值、解法日歸此路）；取一舍二：取{mech}一路定{coord_br}{unit}、餘二路與終局方向或尺度不合舍之；合流D四路已掃（沖起/出墓/解法/實空）；{table_note}；已按對表校準取點（對表首選在候補內者優先、閘門釋放優先於對表）",
        f"trigger: {'; '.join(trig_parts)}",
    ]
    return {"case_id": cid, "prediction_text": pred_text, "basis": "\n".join(basis_lines),
            "confidence": conf,
            "trigger": {"changed_main": changed_main, "reserve_used": reserve_used,
                        "disputed": is_disputed, "reason": "; ".join(trig_parts)}}
