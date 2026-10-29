# -*- coding: utf-8 -*-
"""
易林补遗总断章（书页1-21）补普查批建档脚本（expansion10/yilin-buyi-zongduan 唯一脚本名）。
读 ../yilin-najia-gen-yb 生成盘面，组装 cases.jsonl 与 inputs/YB-014…YB-022.json（原 YB-023 革之困例经去重判定与 YY-020 同例剔除，见 BUILD-REPORT），
执行对全池（各 expansion cases.jsonl＋roster3＋roster4-9 additions＋masters-dataset data）三键去重与泄漏自检。
转录来源：校正全本主本 PDF 页19-39（书页1-21）200dpi 单页图视觉通读。
"""
import json, os, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))  # expansion10/
gen = __import__("yilin-najia-gen-yb")

BOOK = "易林补遗"
EDITION = "华龄出版社《四库存目纳甲汇刊（三）》校正全本（（明）张世宝撰，郑同校；用户经学校图书馆提供之扫描本）"
LICENSE = "用户经学校图书馆提供，内部研究使用（redistributable=false）"
SETTING = "明代民间卖卜占验实录（张世宝自记占例，散文体附断语与应验）"
GN = "断验分离成立：断语（含应期断言）在前、原书另载应验在后，结局为冷门局部事实"
CONT = "明代民间占例，求测者皆未具名，结局为冷门局部事实，无著名人物与事件，无从常识先验得知"

def build(cid, subject, gender, question, asked_at, hex_full, moving, changed_full,
          page, excerpt, direction, assertions, timing, outcome_desc, grade_note,
          completeness, comment, tags, mdc=True):
    d = gen.describe(hex_full, moving=moving, changed_full=changed_full)
    base = d["base"]
    hex_label = f"{base['palace']}宫：{hex_full}（{base['palace_label']}）"
    if d["changed_name"]:
        hex_label += f" 之 {d['changed_name']}"
    chapter_page = f"卷一总断章第一，书页{page}"
    return {
        "id": cid, "tradition": "liuyao",
        "subject": {"name_or_desc": subject, "gender": gender},
        "context": {"question": question, "asked_at": asked_at, "setting": SETTING,
                    "attachments": {"casting_method": "liuyao", "hexagram": hex_label,
                                    "moving_lines": d["moving_lines_text"],
                                    "chart_lines_top_to_bottom": d["chart_lines_top_to_bottom"]}},
        "provenance": {"book": BOOK, "edition": EDITION, "license_note": LICENSE, "page": chapter_page},
        "language": "zh-Hant",
        "master_predictions": [{"master": "张世宝", "tradition": "liuyao", "date": asked_at,
                                "statement_excerpt": excerpt, "source": f"《易林补遗》{chapter_page}",
                                "direction": direction, "key_assertions": assertions, "timing_claim": timing}],
        "outcome": {"description": outcome_desc, "verified_by": "原书自载应验（张世宝自记）"},
        "license_status": "internal-research-only", "redistributable": False,
        "outcome_grade": "A", "grade_note": grade_note,
        "contamination": "low", "contamination_reason": CONT,
        "month_day_complete": mdc, "chart_complete": True,
        "completeness_basis": completeness, "holdout_eligible": True,
        "notes": {"tags": tags, "comment": comment, "cross_ref": ""},
    }

CASES = []
CASES.append(build(
    "YB-014", "病子（父为之占，未具名）", "男", "父占子病，问子病吉凶",
    "未月甲寅旬壬戌日", "乾为天", None, None, "2",
    "此卦子值旬空，本为凶兆，岂知伏出坤卦癸亥水，子孙在壬申金之下，水赖金生，正所谓「飞来生伏得长生」，反为有救。后至甲子日，本宫子象当权，病得瘥也",
    "positive", ["子孙值旬空本为凶兆，然伏神癸亥水得飞神壬申金生扶（飞来生伏），反为有救", "甲子日本宫子象当权，病愈"],
    "甲子日病愈", "甲子日，子病瘥（愈）。",
    GN + "；原文以「且如」引例而附明确后验（甲子日病瘥），非纯规则譬喻，与前批 YB-001 同口径",
    "原文记卦名（乾卦安静）与占日；逐爻装卦按通行纳甲法则复原。甲寅旬空子丑，初爻子孙甲子水正值旬空，与原文「子值旬空」合；原文「子孙在壬申金之下」指伏神癸亥水赖五爻壬申金生扶之飞伏生扶关系，照原文登记",
    "总断章飞伏节首例：飞来生伏得长生", ["疾病", "父占子病", "飞伏", "旬空"]))
CASES.append(build(
    "YB-015", "求财者（自占，未具名）", "未载", "问求财，问财利有无",
    "秋月甲申日", "火泽睽", None, "雷泽归妹", "2",
    "此卦六爻无财，须看艮宫丙子水。所嫌伏在未土之下，水被土伤，本不为美。岂知未土空亡，透出子水，况逢长生申日，反主亨通。后至戊子日，果得厚利也",
    "positive", ["卦内无财，伏神丙子水伏未土下本受土伤；未土空亡，伏财透出，又逢申日长生，反主亨通", "戊子日得厚利"],
    "戊子日得厚利", "戊子日，得厚利。",
    GN + "；原文以「又如」引例而附「果得」后验，与前批同口径",
    "原文记本变卦名（睽之归妹）与占日；动爻由本变卦爻位异同唯一确定，逐爻装卦按通行纳甲法则复原。生成器伏神定位：妻财丙子水伏五爻兄弟己未土之下，与原文「伏在未土之下」全合；甲申日属甲申旬、空午未，飞神未土正值旬空，与原文「未土空亡，透出子水」全合；申日为水长生之日，与原文「况逢长生申日」合",
    "总断章飞伏节求财例；与 YB-002 同为睽卦而问事、占日、结局皆异", ["求财", "伏神", "飞伏"]))
CASES.append(build(
    "YB-016", "远行之夫（妻为之占，未具名）", "男", "妻占夫到，问行人何日归",
    "十月甲辰日", "风火家人", None, "风雷益", "7",
    "此卦忌神不动，而仇神又空，元神正临身世，独嫌卦内无官，伏出辛酉金，在三爻亥水之下；又怪伏生飞，名为泄气，目下未来，待后申酉用爻值日，便得相逢——果应己酉日到也",
    "positive", ["卦内无官，官鬼伏神辛酉金伏三爻亥水之下、伏生飞为泄气，目下未归", "待申酉用爻值日相逢，己酉日到"],
    "己酉日夫到", "己酉日，夫到。",
    GN + "；断语以「待后…便得相逢」预断、原书另载应验句于后",
    "原文记本变卦名（家人之益）与占日；动爻由本变卦爻位异同唯一确定。家人为巽宫二世，卦内无官鬼，官鬼辛酉金为本宫首卦巽为风上爻，原文「伏出辛酉金，在三爻亥水之下」之伏位口径照原文登记（通行复原伏神定位以生成器 hidden() 为准，见脚本验盘输出）",
    "总断章用神值日节行人例", ["行人", "妻占夫到", "伏神"]))
CASES.append(build(
    "YB-017", "病弟（兄为之占，未具名）", "男", "兄占弟病，问弟病吉凶",
    "二月甲申旬壬辰日", "天水讼", None, None, "7",
    "卦内元神虽旺，独嫌用值旬空，细推空而带相，决不伤身，过旬方好。待后庚子日冲实，用爻不受水克，其病此日全然瘥也",
    "positive", ["用神值旬空而带相，决不伤身，过旬方好", "庚子日冲实、用爻不受水克，病全然瘥"],
    "庚子日病全然瘥", "庚子日，弟病全然瘥。",
    "断验分离弱于同批他例：应验以「待后某日…其病此日全愈」式一句叙述（与前批 YB-002 应验句同式），断语之应期断言与应验同句相承，已照实标注，待主持复核",
    "原文记卦名（讼卦安静）与占日；逐爻装卦按通行纳甲法则复原。甲申旬空午未，卦中官鬼午火（世爻及三爻）正值旬空；原文「用值旬空」之用神取法照原文登记，不另推",
    "总断章真空/填实节例", ["疾病", "兄占弟病", "旬空填实"]))
CASES.append(build(
    "YB-018", "病妻（夫为之占，未具名）", "女", "夫占妻病，问妻病吉凶",
    "子月甲午旬辛丑日", "雷地豫", None, "雷山小过", "8",
    "此卦用爻持世，忌神虽动化绝在申，本当有救，谁知《海底眼》中所犯「兄化官兮休下状，占病难医须见哭」；后至癸亥日，兄弟绝处逢生，果然命尽，可应此言也",
    "negative", ["用爻持世、忌神动化绝本当有救，然犯「兄化官」之诀，主难医", "癸亥日兄弟绝处逢生，命尽"],
    "癸亥日命尽", "癸亥日，妻命尽（死）。",
    GN,
    "原文记本变卦名（豫之小过）与占日；动爻由本变卦爻位异同唯一确定，逐爻装卦按通行纳甲法则复原；原文「忌神虽动化绝在申」与复原动爻化出申位之爻可互证",
    "总断章变法节例，引《海底眼》诀", ["疾病", "夫占妻病", "兄化官"]))
CASES.append(build(
    "YB-019", "病妻（夫为之占，未具名；与 YB-018 同日另一人）", "女", "占妻病，问妻病吉凶",
    "子月甲午旬辛丑日", "雷地豫", None, "雷风恒", "8",
    "此卦有两爻发动，巳火子孙变成亥水父母，卯木兄弟又变酉金官鬼，内有二爻动者，故不准「兄化官兮休下状，占病难医须见哭」，反取「兄弟化为冲克，不能克制财爻」，后至丙午日财遇生扶，妻病全好",
    "positive", ["两爻发动，不作「兄化官」断；兄弟化冲克不能克制财爻", "丙午日财遇生扶，妻病全好"],
    "丙午日妻病全好", "丙午日，妻病全好。",
    GN + "；原文「当日又一人占妻病」与 YB-018 同日同问而异人异卦异结局，三键以对象（另一人）相别，见 BUILD-REPORT 去重节",
    "原文记本变卦名（豫之恒）并明言两爻发动（巳火子孙变亥水父母、卯木兄弟变酉金官鬼）；动爻由本变卦爻位异同唯一确定且与原文自叙化爻干支全合，逐爻装卦按通行纳甲法则复原",
    "与 YB-018 同页对举：乱动不可将京房书断", ["疾病", "夫占妻病", "乱动"]))
CASES.append(build(
    "YB-020", "见官者（来问，未具名）", "未载", "问见官（参官），问吉凶",
    "丑月辛丑日", "坤为地", None, "山地剥", "9",
    "此卦子孙持世发动，更得日月生扶，本为佳兆，岂知「子化官兮防祸患，占病忧疑尽不如」，以后参官，果受其累",
    "negative", ["子孙持世发动得日月生扶本为佳兆，然子化官主祸患，吉处藏凶", "参官后受其累"],
    "无明确日期（断参官后受累）", "参官后，受其累。",
    GN + "；应验为事实性结局（参官后受牵累），具体形态原文未细载，照原文登记",
    "原文记本变卦名（坤之剥）与占日；动爻由本变卦爻位异同唯一确定（上爻动），逐爻装卦按通行纳甲法则复原",
    "总断章吉中藏凶节例", ["见官", "子化官", "吉处藏凶"]))
CASES.append(build(
    "YB-021", "求财者（自占，未具名）", "未载", "问月内何日得财",
    "戌月丁亥日", "山水蒙", None, None, "10",
    "又如此月此日，问月内何日得财？亦占蒙卦，待后丁酉日果得财也",
    "positive", ["亦占蒙卦，断丁酉日得财"],
    "丁酉日得财", "丁酉日，得财。",
    GN + "；占日「此月此日」承同页前例（戌月丁亥日巳时问当日求财，蒙卦安静）指代明确，照承前口径登记",
    "原文记卦名（蒙卦）与应验日；前例明言蒙卦安静，本例「亦占蒙卦」未言动爻，盘面按安静复原，逐爻装卦按通行纳甲法则推算",
    "与同页当日求财例（C 级）同日同卦而问法异（月内何日 vs 当日）", ["求财", "应期", "日辰为主"]))
CASES.append(build(
    "YB-022", "出外多年之夫（妻为之占，未具名）", "男", "妻占夫出外多年，问何年返舍",
    "酉年卯月乙酉日", "火山旅", None, None, "10",
    "又如妻占夫出外多年，要知何年返舍？此月此日亦得旅卦，便言亥年方到，不可将亥月推之，果然己亥年正月到家，应此理也",
    "positive", ["断亥年方到（不可作亥月推）", "己亥年正月到家"],
    "亥年（己亥年正月）到家", "己亥年正月，夫到家。",
    GN + "；占日「此月此日」承同页前例（酉年卯月乙酉日问远路行人）指代明确",
    "原文记卦名（旅卦）与占日（承前）；原文未言动爻，盘面按安静复原，逐爻装卦按通行纳甲法则推算",
    "总断章远期应期节例：年占以年断", ["行人", "妻占夫归", "远年应期"]))

# ---------- 三键去重：对全池执行 ----------
pool_files = []
for pat in ["benchmark/phase3/expansion*/**/cases.jsonl", "benchmark/phase3/expansion*/cases.jsonl",
            "benchmark/phase3/data/roster3.jsonl", "benchmark/phase3/roster*-additions.jsonl",
            "masters-dataset/data/**/*.jsonl", "masters-dataset/**/*.jsonl"]:
    pool_files += glob.glob(os.path.expanduser(f"~/workspace/divination/{pat}"), recursive=True)
pool_files = sorted(set(pool_files))
pool = []
for f in pool_files:
    try:
        for line in open(f, encoding="utf-8"):
            line = line.strip()
            if line.startswith("{"):
                pool.append((f, json.loads(line)))
    except Exception:
        pass
print(f"POOL files={len(pool_files)} records={len(pool)}")

def keys_of(c):
    ctx = c.get("context", {}) if isinstance(c.get("context"), dict) else {}
    att = ctx.get("attachments", {}) if isinstance(ctx.get("attachments"), dict) else {}
    return (c.get("id", "?"), str(c.get("subject", "")), str(ctx.get("question", "") or c.get("question", "")),
            str(ctx.get("asked_at", "") or c.get("asked_at", "")), str(att.get("hexagram", "") or c.get("hexagram", "")))

HEXKEY = {"YB-014": "乾为天", "YB-015": "归妹", "YB-016": "家人", "YB-017": "天水讼",
          "YB-018": "豫", "YB-019": "豫", "YB-020": "坤为地", "YB-021": "山水蒙",
          "YB-022": "火山旅"}
QKEY = {"YB-014": "子病", "YB-015": "求财", "YB-016": "夫到", "YB-017": "弟病",
        "YB-018": "妻病", "YB-019": "妻病", "YB-020": "见官", "YB-021": "得财",
        "YB-022": "返"}
hits = {}
for c in CASES:
    cid = c["id"]
    for f, r in pool:
        if r.get("id") == cid:
            continue
        blob = json.dumps(r, ensure_ascii=False)
        if HEXKEY[cid] in blob and QKEY[cid] in blob:
            hits.setdefault(cid, []).append((r.get("id", "?"), os.path.basename(f)))
print("DEDUP near-hits (hexagram+question keyword co-occurrence, for manual three-key review):")
for cid, hs in hits.items():
    print(" ", cid, hs)
if not hits:
    print("  none")

# ---------- 写盘 ----------
os.makedirs(os.path.join(HERE, "inputs"), exist_ok=True)
with open(os.path.join(HERE, "cases.jsonl"), "w", encoding="utf-8") as fh:
    for c in CASES:
        fh.write(json.dumps(c, ensure_ascii=False) + "\n")
FORBIDDEN = ["outcome", "master_predictions", "key_assertions", "direction", "timing_claim"]
OUTCOME_WORDS = ["病得瘥", "果得厚利", "果应己酉日到", "全然瘥", "果然命尽", "妻病全好",
                 "果受其累", "果得财", "到家", "病即愈", "命尽", "厚利"]
leak = 0
for c in CASES:
    inp = {k: v for k, v in c.items() if k not in ("master_predictions", "outcome")}
    p = os.path.join(HERE, "inputs", f"{c['id']}.json")
    with open(p, "w", encoding="utf-8") as fh:
        json.dump(inp, fh, ensure_ascii=False, indent=2)
    txt = open(p, encoding="utf-8").read()
    for w in FORBIDDEN:
        if f'"{w}"' in txt:
            print("LEAK field", c["id"], w); leak += 1
    for w in OUTCOME_WORDS:
        if w in txt:
            print("LEAK word", c["id"], w); leak += 1
print(f"WROTE cases={len(CASES)} inputs={len(os.listdir(os.path.join(HERE,'inputs')))} leak_hits={leak}")
for c in CASES:
    d = gen.describe(c["context"]["attachments"]["hexagram"].split("：")[1].split("（")[0],
                     changed_full=None) if False else None
    print(c["id"], c["context"]["attachments"]["hexagram"], "|", c["context"]["attachments"]["moving_lines"], "| hidden:", gen.hidden(c["context"]["attachments"]["hexagram"].split("：")[1].split("（")[0]))
