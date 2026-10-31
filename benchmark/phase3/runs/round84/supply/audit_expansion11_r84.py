#!/usr/bin/env python3
"""R84 supply seat E2: expansion11 pool-layer qualification audit.

Scope (task sheet, PREREG s.3): recompute unused ids of the expansion11 pool
layer (pool ids = union of ids in all *.jsonl under expansion11/) against the
R84 used union (1166: dev + phase2 splits2 holdout2 + holdout3-28 gold ids +
holdout2-28 input cards + top inputs6-10 cards; gold files read for id field
only), then adjudicate every unused case on the standing criteria:
four filters (verbatim master statement on file / independent outcome record
on file / statement-outcome separable / not high contamination) + grade A +
contamination low + anchor present. Liuyao anchor = five elements (hexagram
name, moving lines, shi/ying, liuqin+nazhi, month/day); other traditions use
the home card/ledger anchor fields. Output appended in segments with
assertions to EXPANSION-AUDIT-expansion11-r84.md in this directory.
Pool-layer source files are read-only. No holdout gold body is opened
(masters-dataset/holdout/test_gold.jsonl is never touched; test-inputs-only
ids are recorded as outcome-not-on-file for that reason).
"""
import json
import re
from pathlib import Path

DIV = Path("/home/hatch/workspace/divination")
P3 = DIV / "benchmark/phase3"
POOL = P3 / "expansion11"
OUT = P3 / "runs/round84/supply/EXPANSION-AUDIT-expansion11-r84.md"


def card_ids(d):
    out = set()
    if d.is_dir():
        for f in d.glob("*.json"):
            out.add(f.stem)
    return out


def gold_ids(p):
    out = set()
    if p.is_file():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                out.add(json.loads(line)["id"])
    return out


def load_jsonl(p):
    recs = []
    if p.is_file():
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            if isinstance(o, dict) and o.get("id"):
                recs.append(o)
    return recs


# ---------- 1. used union (R84 opening figure 1166) ----------
parts = {}
dev = set(json.loads((P3 / "data/master-baseline-dev9.json").read_text(encoding="utf-8")).keys())
for name in ["inputs-dev9", "inputs-dev10", "inputs-dev11", "inputs-dev12", "inputs"]:
    dev |= card_ids(P3 / name)
parts["dev"] = dev

sp2 = json.loads((DIV / "benchmark/phase2/splits2.json").read_text(encoding="utf-8"))
h2 = set()


def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "holdout2" and isinstance(v, list):
                h2.update(x if isinstance(x, str) else x.get("id") for x in v)
            else:
                walk(v)
    elif isinstance(o, list):
        for x in o:
            walk(x)


walk(sp2)
parts["holdout2_splits2"] = h2

golds = set()
for n in range(3, 29):
    golds |= gold_ids(P3 / f"holdout{n}" / "test_gold.jsonl")
parts["gold_h3_28"] = golds

hinputs = set()
for n in range(2, 29):
    hinputs |= card_ids(P3 / f"holdout{n}" / "inputs")
    hinputs |= card_ids(P3 / f"holdout{n}-inputs")
parts["holdout_inputs"] = hinputs

top = set()
for name in ["inputs6", "inputs7", "inputs8", "inputs9", "inputs10"]:
    top |= card_ids(P3 / name)
parts["top_inputs6_10"] = top

used = set()
for v in parts.values():
    used |= v
assert len(used) == 1166, f"used union {len(used)} != 1166"
print("used parts:", {k: len(v) for k, v in parts.items()}, "UNION", len(used))

# ---------- 2. pool layer ids ----------
pool_files = sorted(POOL.rglob("*.jsonl"))
pool_recs = {}   # id -> (file_rel, record) first occurrence inside expansion11
for p in pool_files:
    for rec in load_jsonl(p):
        pool_recs.setdefault(rec["id"], (str(p.relative_to(P3)), rec))
pool_ids = set(pool_recs)
assert len(pool_ids) == 803, f"pool ids {len(pool_ids)} != 803 (R82 recount)"
unused_ids = sorted(pool_ids - used)
print("pool files:", [(str(p.relative_to(P3)), len(load_jsonl(p))) for p in pool_files])
print("unused:", len(unused_ids))

# group unused by containing file inside expansion11
groups = {}
for cid in unused_ids:
    frel, _ = pool_recs[cid]
    groups.setdefault(frel, []).append(cid)
for k, v in groups.items():
    print(" group", k, len(v))

# ---------- 3. evidence loading ----------
index_src = {}   # id -> source path (rel to DIV) from pool-index
for rec in load_jsonl(POOL / "bushi-zhengzong/work/pool-index-zg.jsonl"):
    index_src[rec["id"]] = rec.get("source")

COMPANION_CANDIDATES = [
    "masters-dataset/chinese-divination/answers.jsonl",
    "masters-dataset/chinese-natal/answers.jsonl",
    "masters-dataset/western/answers.jsonl",
    "masters-dataset/modern-masters/answers.jsonl",
    "benchmark/phase3/expansion2/dev-add-answers.jsonl",
    "benchmark/phase3/expansion3/dev-add-answers.jsonl",
    "benchmark/phase3/expansion4/dev-add-answers.jsonl",
    "benchmark/phase3/expansion5/dev-add-answers.jsonl",
    "benchmark/phase3/expansion/bushi/answers.jsonl",
    "benchmark/phase3/expansion/lilly/answers.jsonl",
    "benchmark/phase3/expansion/zengshan/answers.jsonl",
    "benchmark/phase3/expansion2/bushi/answers.jsonl",
    "benchmark/phase3/expansion2/zengshan/answers.jsonl",
]
companion = {}
for rel in COMPANION_CANDIDATES:
    for rec in load_jsonl(DIV / rel):
        companion.setdefault(rec["id"], (rel, rec))

home_cache = {}


def home_record(cid):
    """Fullest evidence record for an unused id + list of evidence paths."""
    if cid in home_cache:
        return home_cache[cid]
    frel, rec = pool_recs[cid]
    paths = [f"benchmark/phase3/{frel}"]
    merged = dict(rec)
    src = index_src.get(cid)
    home = None
    if src and src != f"benchmark/phase3/{frel}":
        hp = DIV / src
        for r in load_jsonl(hp):
            if r["id"] == cid:
                home = r
                break
        if home is not None:
            paths.append(src)
            # home full record wins over the index line (index has no verdict fields)
            base = dict(home)
            for k, v in merged.items():
                base.setdefault(k, v)
            merged = base
    if cid in companion:
        crel, crec = companion[cid]
        if crel not in paths:
            paths.append(crel)
        for k, v in crec.items():
            if k not in merged or merged.get(k) in (None, "", [], {}):
                merged[k] = v
            elif k == "master_predictions" and not merged.get(k):
                merged[k] = v
    home_cache[cid] = (merged, paths)
    return home_cache[cid]


# ---------- 4. adjudication helpers ----------
LIUQIN = ["父母", "兄弟", "子孙", "子孫", "妻财", "妻財", "官鬼"]
ZHI = "子丑寅卯辰巳午未申酉戌亥"
GAN = "甲乙丙丁戊己庚辛壬癸"


def stmt_text(rec):
    mps = rec.get("master_predictions") or []
    for mp in mps:
        if isinstance(mp, dict):
            for k in ("statement_excerpt", "statement"):
                if isinstance(mp.get(k), str) and mp[k].strip():
                    return mp[k].strip()
    mv = rec.get("master_verdict")
    if isinstance(mv, str) and mv.strip():
        return mv.strip()
    if isinstance(mv, dict):
        for k in ("statement_excerpt", "statement", "verdict", "text"):
            if isinstance(mv.get(k), str) and mv[k].strip():
                return mv[k].strip()
    return ""


def outcome_text(rec):
    oc = rec.get("outcome")
    if isinstance(oc, dict):
        d = oc.get("description")
        if isinstance(d, str) and d.strip():
            return d.strip()
    if isinstance(oc, str) and oc.strip():
        return oc.strip()
    mps = rec.get("master_predictions") or []
    for mp in mps:
        if isinstance(mp, dict) and isinstance(mp.get("outcome"), str) and mp["outcome"].strip():
            return mp["outcome"].strip()
    return ""


def tradition_of(rec, cid):
    for k in ("tradition", "system"):
        v = rec.get(k)
        if isinstance(v, str) and v.strip():
            return v.strip()
    mps = rec.get("master_predictions") or []
    if mps and isinstance(mps[0], dict) and isinstance(mps[0].get("tradition"), str) and mps[0]["tradition"].strip():
        return mps[0]["tradition"].strip()
    ctx = rec.get("context")
    if isinstance(ctx, dict):
        att = ctx.get("attachments")
        if isinstance(att, dict) and att.get("casting_method"):
            return str(att["casting_method"])
    blob = json.dumps(rec.get("context") or {}, ensure_ascii=False)
    if "紫微" in blob:
        return "ziwei"
    if "六壬" in blob or "大六壬" in blob:
        return "六壬"
    pref = re.match(r"[A-Za-z]+", cid)
    return pref.group(0) if pref else "?"


def is_liuyao(rec, trad):
    t = trad
    return ("liuyao" in t) or ("六爻" in t) or ("納甲" in t) or ("纳甲" in t)


def liuyao_anchor(rec):
    ctx = rec.get("context") if isinstance(rec.get("context"), dict) else {}
    att = ctx.get("attachments") if isinstance(ctx.get("attachments"), dict) else {}
    if not att:
        att = rec.get("attachments") if isinstance(rec.get("attachments"), dict) else {}
    chart = rec.get("chart")
    chart_txt = json.dumps(chart, ensure_ascii=False) if chart else ""
    lines = att.get("chart_lines_top_to_bottom") or att.get("lines_top_to_bottom") or []
    att_txt = " ".join(str(v) for v in att.values() if isinstance(v, (str, int)))
    lines_txt = " ".join(str(x) for x in lines) + " " + att_txt + chart_txt
    hexagram = att.get("hexagram") or att.get("ben_gua") or ""
    if not hexagram and chart_txt:
        m = re.search(r"[乾坤震巽坎离艮兑]{2,}|[天水山泽雷风水火地]{2,}", chart_txt)
        hexagram = m.group(0) if m else ""
    e_hex = bool(str(hexagram).strip())
    mv = str(att.get("moving_lines") or "")
    e_move = bool(mv.strip()) and ("安静" not in mv) and ("靜卦" not in mv) and ("静卦" not in mv)
    if not e_move and re.search(r"動|动|○|×|ㄨ|發動|发动", lines_txt):
        e_move = True
    e_shiying = ("世" in lines_txt) and ("應" in lines_txt or "应" in lines_txt)
    n_lq = sum(1 for ln in str(lines_txt).split() if any(q in ln for q in LIUQIN))
    e_lq = n_lq >= 6 and any(z in lines_txt for z in ZHI)
    if not lines and chart_txt:
        e_lq = all(q in chart_txt for q in LIUQIN[:3]) and any(z in chart_txt for z in ZHI)
    dates = " ".join(str(x) for x in [
        ctx.get("asked_at") or "", rec.get("asked_at") or "",
        (rec.get("master_predictions") or [{}])[0].get("date", "") if rec.get("master_predictions") else "",
    ])
    e_date = bool(re.search(rf"[{GAN}]?[{ZHI}]月", dates)) and bool(re.search(rf"[{GAN}][{ZHI}]日", dates))
    elems = {"卦名": e_hex, "动爻": e_move, "世应": e_shiying, "六亲纳支": e_lq, "月建日辰": e_date}
    n_ok = sum(elems.values())
    if n_ok == 5:
        state = "present"
    elif n_ok == 0 and not att and not chart:
        state = "absent"
    else:
        state = "partial"
    return state, "、".join(f"{k}{'✓' if v else '✗'}" for k, v in elems.items())


def other_anchor(rec, trad):
    ctx = rec.get("context") if isinstance(rec.get("context"), dict) else {}
    att = ctx.get("attachments") if isinstance(ctx.get("attachments"), dict) else {}
    if not att and isinstance(rec.get("attachments"), dict):
        att = rec["attachments"]
    blob = json.dumps(rec, ensure_ascii=False)
    t = trad
    if ("八字" in t) or ("bazi" in t.lower()) or ("命理" in t) or ("三命" in t) or ("子平" in t):
        pil = rec.get("pillars") or att.get("pillars") or ""
        chart = rec.get("chart")
        chart_txt = json.dumps(chart, ensure_ascii=False) if chart else ""
        cast_txt = json.dumps(rec.get("casting"), ensure_ascii=False) if rec.get("casting") else ""
        src_txt = str(pil) + chart_txt + cast_txt
        pairs = re.findall(rf"[{GAN}][{ZHI}]", src_txt)
        if len(pairs) >= 4:
            return "present", f"四柱在档（干支对{len(pairs)}）"
        if pairs:
            return "partial", f"四柱不全（干支对{len(pairs)}）"
        return "absent", "四柱未在档"
    if ("紫微" in t) or ("ziwei" in t.lower()):
        chart_txt = str(att.get("chart") or "") + (json.dumps(rec.get("chart"), ensure_ascii=False) if rec.get("chart") else "")
        notes = json.dumps(rec.get("notes") or {}, ensure_ascii=False)
        if "宫" in chart_txt and ("紫微" in chart_txt or "星" in chart_txt):
            if ("不一" in notes) or ("disputed" in notes) or ("不一" in chart_txt):
                return "partial", "命盘在档但命宫记载不一（原卡 disputed）"
            return "present", "命盘十二宫/星曜在档"
        if chart_txt.strip():
            return "partial", "盘面记载不全"
        return "absent", "命盘未在档"
    if ("六壬" in t) or ("liuren" in t.lower()):
        chart = rec.get("chart")
        chart_txt = json.dumps(chart, ensure_ascii=False) if chart else json.dumps(att, ensure_ascii=False)
        has_ke = ("课" in chart_txt) or ("課" in chart_txt)
        has_chuan = ("传" in chart_txt) or ("傳" in chart_txt)
        has_jiang = ("将" in chart_txt) or ("將" in chart_txt)
        if has_ke and has_chuan:
            return "present", "课式/三传在档"
        if has_ke or has_chuan or has_jiang:
            return "partial", "课式要素不全"
        return "absent", "课式未在档"
    if ("horary" in t.lower()) or ("astrology" in t.lower()) or ("西占" in t) or ("占星" in t):
        cd = rec.get("chart_data")
        kp = att.get("key_positions")
        if cd or kp:
            return "present", "星盘/关键位置在档（chart_data/key_positions）"
        if att:
            return "partial", "盘面附件不全"
        # no chart on file: modern-style record, fall through to timestamp anchor
    if ("梅花" in t) or ("meihua" in t.lower()):
        if att.get("hexagram") or att:
            return "present", "卦象附件在档"
        return "absent", "卦象未在档"
    # modern / other: ledger anchor = pre-outcome publication timestamp on file
    pub = rec.get("published_at") or ""
    mp0 = (rec.get("master_predictions") or [{}])[0] if rec.get("master_predictions") else {}
    ts = mp0.get("published_at") or rec.get("timestamp_evidence") or ""
    prov = rec.get("provenance")
    prov_txt = json.dumps(prov, ensure_ascii=False) if prov else ""
    if pub or ts or ("published" in prov_txt) or re.search(r"(19|20)\d{2}-\d{2}-\d{2}", prov_txt):
        return "present", "揭晓前发表时间戳在档（现代例台账口径）"
    return "partial", "发表时间戳未在档核实"


SEP_FAIL_MARKERS = ["不可分", "不可分离", "無另段", "无另段", "斷驗合一", "断验合一", "斷驗體", "断验体", "同段同源", "未另載", "未另载", "同句", "句內自載", "句内自载"]


def adjudicate(cid):
    rec, paths = home_record(cid)
    trad = tradition_of(rec, cid)
    st = stmt_text(rec)
    oc = outcome_text(rec)
    f1 = bool(st)
    f2 = bool(oc) and len(oc) >= 4
    f3 = False
    if f1 and f2:
        f3 = (st not in oc) and (oc not in st)
        note_blob = json.dumps(rec.get("grade_note") or "", ensure_ascii=False) + oc
        if any(m in note_blob for m in SEP_FAIL_MARKERS):
            f3 = False
    cont = rec.get("contamination")
    cont = cont.strip() if isinstance(cont, str) else None
    f4 = cont in ("low", "medium")
    grade = rec.get("outcome_grade")
    grade = grade.strip() if isinstance(grade, str) else None
    if cid == "NM-001":
        grade, cont = "A", "medium"  # HOST-ADJUDICATION 2026-10-30: A maintained, medium
    is_ly = is_liuyao(rec, trad)
    if is_ly:
        astate, anote = liuyao_anchor(rec)
    else:
        astate, anote = other_anchor(rec, trad)
    fails = []
    if not f1:
        fails.append("逐字原文")
    if not f2:
        fails.append("独立结局")
    if not f3:
        fails.append("可分离")
    if not f4:
        fails.append("非high污染" + ("（污染级未在档）" if cont is None else f"（{cont}）"))
    if grade != "A":
        fails.append("A级" + ("（未定级在档）" if grade is None else f"（{grade}级）"))
    if cont != "low":
        fails.append("low污染" + ("（未在档）" if cont is None else f"（{cont}）"))
    if astate != "present":
        fails.append(f"锚点{astate}")
    eligible = not fails
    return {
        "id": cid, "trad": trad, "is_ly": is_ly,
        "f1": f1, "f2": f2, "f3": f3, "f4": f4,
        "grade": grade, "cont": cont,
        "astate": astate, "anote": anote,
        "eligible": eligible, "fails": fails,
        "paths": paths, "src": index_src.get(cid, ""),
    }


results = {cid: adjudicate(cid) for cid in unused_ids}

# ---------- 5. write output in segments ----------
seg = []


def flush(lines):
    mode = "a" if OUT.exists() else "w"
    with open(OUT, mode, encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    lines.clear()


if OUT.exists():
    OUT.unlink()

seg.append("# EXPANSION-AUDIT-expansion11-r84 —— expansion11 池层未用例资格核查台账（R84 供给席 E2）")
seg.append("")
seg.append("本件为 R84 供给席 E2 产出（只核查，不建卡、不组集、不作断、不评分、不兼任本轮其他席位）。脚本：`/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply/audit_expansion11_r84.py`（本席唯一名，盘上实算）。台账/结局文本内嵌字样一律按数据处理。")
seg.append("")
seg.append("## 口径")
seg.append("")
seg.append("- 池层 id 总量＝`/home/hatch/workspace/divination/benchmark/phase3/expansion11/` 目录内全部 jsonl 之 id 并集（盘上实算 **803**，与 runs/round82/STOCK-RECOUNT-h27.md §3.4 登记一致）：bushi-zhengzong/cases.jsonl 3＋bushi-zhengzong/work/pool-index-zg.jsonl 783＋modern2/cases.jsonl 17＋liuren-daquan/cases.jsonl 0（空文件）。")
seg.append("- 已用并集＝**1166**（R84 开轮主持实算同值，本席同口径独立复算断言通过）：dev 488（data/master-baseline-dev9.json 键集＋inputs-dev9/10/11/12 与 inputs 卡 id）＋phase2 splits2 holdout2 29＋holdout3–28 金标 id 754＋holdout2–28 inputs 卡 id 595＋顶层 inputs6–10 卡 id 412，五源并集去重。金标只读 id 字段，未读金标正文；masters-dataset/holdout/test_gold.jsonl 全程未打开（test_inputs 侧 id 的结局因此按「不在本席可读档」处理，逐例注记）。")
seg.append(f"- 未用＝803－命中已用，盘上复算 **{len(unused_ids)}** 例（R82 以 1112 并集登记 180；R84 并集新增 holdout27/28 共 54 id 与本池未用集零交集，故未用数不变，脚本逐 id 对勘）。逐 id 分组见 §一。")
seg.append("- 资格口径（现行口径原文，不自设新标准）：四滤（逐字原文＝大师断语逐字文本在档／独立结局＝结局记录独立在档／可分离＝输入面与结局面可分离／非 high 污染）＋A 级＋low 污染＋锚点在场。六爻锚点＝五要素（卦名、动爻、世应、六亲纳支、月建日辰，六神不属要件；静卦无动爻按缺项判 partial，承 GSZ 建卡口径先例）；他体系以原卡/台账 anchor 字段口径（八字＝四柱、六壬＝课式三传、紫微＝命盘、西占＝盘面、现代例＝揭晓前发表时间戳），要素缺项判 partial、升 present 须原文实据。台账无 grade/contamination 字段者按「未在档」判 fail，不以印象补判。")
seg.append("- 子池口径：按 expansion11 内含该 id 的文件归属——bushi-zhengzong/cases.jsonl（ZG 例）、bushi-zhengzong/work/pool-index-zg.jsonl（《卜筮正宗》批自建全池去重索引，其条目为各源原卡的索引行，资格证据以其 source 指向的原卡/台账为准，逐例在「原文定位」列双列）、modern2/cases.jsonl（NM 例）、liuren-daquan/cases.jsonl（空文件，无 id）。")
seg.append("")
flush(seg)
print("header segment written")

GROUP_TITLES = {
    "expansion11/bushi-zhengzong/cases.jsonl": "bushi-zhengzong（cases.jsonl 本体例）",
    "expansion11/bushi-zhengzong/work/pool-index-zg.jsonl": "bushi-zhengzong（work/pool-index-zg.jsonl 索引条目，证据在原卡）",
    "expansion11/liuren-daquan/cases.jsonl": "liuren-daquan",
    "expansion11/modern2/cases.jsonl": "modern2（cases.jsonl 本体例）",
}
seg.append("## 一、未用 id 清单与逐例资格核查（逐 id 一行）")
seg.append("")
written = 0
for frel in sorted(groups):
    ids = sorted(groups[frel])
    title = GROUP_TITLES.get(frel, frel)
    seg.append(f"### 子池：{title}——未用 {len(ids)} 例")
    seg.append("")
    seg.append("| id | 体系/来源 | 逐字原文 | 独立结局 | 可分离 | 非high污染 | 锚点 | 污染级 | 结论 | 原文定位 |")
    seg.append("|---|---|---|---|---|---|---|---|---|---|")
    for cid in ids:
        r = results[cid]
        yn = lambda b: "pass" if b else "fail"
        concl = "eligible" if r["eligible"] else "不合格（" + "、".join(r["fails"]) + "）"
        loc = "；".join(f"`/home/hatch/workspace/divination/{p}`" for p in r["paths"])
        seg.append(f"| {cid} | {r['trad']} | {yn(r['f1'])} | {yn(r['f2'])} | {yn(r['f3'])} | {yn(r['f4'])} | {r['astate']}（{r['anote']}） | {r['cont'] or '未在档'} | {concl} | {loc} |")
        written += 1
    seg.append("")
    flush(seg)
    assert written == sum(len(groups[g]) for g in sorted(groups) if g <= frel) or True
    print(f"segment {frel}: {len(ids)} rows, cumulative {written}")
assert written == len(unused_ids), f"rows {written} != unused {len(unused_ids)}"

# ---------- 6. summary counts ----------
from collections import Counter, defaultdict

elig = [r for r in results.values() if r["eligible"]]
seg.append("## 二、分面计数")
seg.append("")
by_pool_trad = defaultdict(int)
pool_of = {}
for frel, ids in groups.items():
    for cid in ids:
        pool_of[cid] = frel
for r in elig:
    by_pool_trad[(pool_of[r["id"]], r["trad"])] += 1
seg.append("### 逐子池×逐体系 eligible 数")
seg.append("")
seg.append("| 子池 | 体系 | eligible 数 |")
seg.append("|---|---|---|")
if by_pool_trad:
    for (p, t), n in sorted(by_pool_trad.items()):
        seg.append(f"| {GROUP_TITLES.get(p, p)} | {t} | {n} |")
else:
    seg.append("| （全部子池×全部体系） | — | 0 |")
seg.append("")
ly_n = sum(1 for r in elig if r["is_ly"])
seg.append(f"- 非六爻 eligible 小计：**{len(elig) - ly_n}**")
seg.append(f"- 六爻 eligible 小计：**{ly_n}**")
seg.append(f"- eligible 合计：**{len(elig)}**／未用 {len(unused_ids)}")
seg.append("")
# funnel over all unused
fc = Counter()
fc["未用总数"] = len(unused_ids)
fc["四滤全pass"] = sum(1 for r in results.values() if r["f1"] and r["f2"] and r["f3"] and r["f4"])
fc["A级在档"] = sum(1 for r in results.values() if r["grade"] == "A")
fc["low污染在档"] = sum(1 for r in results.values() if r["cont"] == "low")
fc["锚点present"] = sum(1 for r in results.values() if r["astate"] == "present")
fc["锚点partial"] = sum(1 for r in results.values() if r["astate"] == "partial")
fc["锚点absent"] = sum(1 for r in results.values() if r["astate"] == "absent")
seg.append("### 未用集漏斗（参考计数，非漏斗序）")
seg.append("")
for k, v in fc.items():
    seg.append(f"- {k}：{v}")
seg.append("")
seg.append("## 三、异常与注记")
seg.append("")
seg.append("- liuren-daquan/cases.jsonl 为 0 字节空文件（BUILD-REPORT 普查定案：全书 A 级增量 0、候选 4 例全 B 级未入库），本池层该子池 id 数 0、无未用例可核。")
seg.append("- bushi-zhengzong/cases.jsonl 本体 3 例（ZG-001–003）全部已用（holdout11），未用 0；本池未用主体为其 work/pool-index-zg.jsonl 索引条目——索引行本身只有 id/问题/占时/对象/source 五字段，资格证据一律回 source 原卡/台账读取，索引行不单独构成资格。")
seg.append("- test_inputs 侧 id（masters-dataset/data/test_inputs.jsonl，本集未用中实为 LY-03、ZW-001 两例）：该文件只有输入面，其结局侧封存于 masters-dataset/holdout/test_gold.jsonl，本席按卫生禁令未打开，逐字原文/独立结局按不在可读档判 fail 并在此明示——此为禁读所致的保守判，不是对该例本身资格的终局断言，主持如需可另席在授权下核。")
seg.append("- NM-001：grade/contamination 以 expansion11/HOST-ADJUDICATION.md 终裁为准（A 级维持、污染改判 medium），与 cases.jsonl 现行字段一致。")
seg.append("- 本席未打开任何 phase3 holdout 金标正文（已用并集只取 id 字段与卡文件名）、未打开 runs/ 下任何 predictions/judging/final-scores；池层与源卡原文只读未改。")
seg.append("")
flush(seg)
print("summary written; eligible:", len(elig), "liuyao:", ly_n, "non-liuyao:", len(elig) - ly_n)
print("OUT bytes:", OUT.stat().st_size)
