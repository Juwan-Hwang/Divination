#!/usr/bin/env python3
"""R52 leikao C48/C51 candidate card builder + stage-2 self-scan (unique name, this round only).
Input whitelist = {id, tradition, subject, context, question, setting, provenance, redistributable, license_status}
Scan marker sets verbatim from task (R42 PREREG s5 lineage).
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "digestion" / "cards-mining-leikao-r52"
OUT.mkdir(parents=True, exist_ok=True)

LICENSE = "古典文本公有領域（明張鳳翼輯《夢占類考》）；掃描底本僅內部研究用"

C48_PROV_IN = "《夢占類考》卷六帷服部「半臂賜錦半臂」條，PDF 199 左；底本 incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf（438 頁）；原書標出處宣室志；transcription=visual（R52 回原頁 300dpi 視覺覆核）"
C48_PROV_GOLD = C48_PROV_IN + "；登記出處 runs/round51/digestion/REGISTER-leikao-cont-r51.md LK2-C48 條"
C51_PROV_IN = "《夢占類考》卷六紗籠類「紗籠中人」條，PDF 204 左起–205 右；底本 incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf（438 頁）；原書標出處原化記；transcription=visual（R52 回原頁 300dpi 視覺覆核）"
C51_PROV_GOLD = C51_PROV_IN + "；登記出處 runs/round51/digestion/REGISTER-leikao-cont-r51.md LK2-C51 條"

c48_input = {
    "id": "LK2-C48",
    "tradition": "mengzhan",
    "subject": "竇參，唐正元中御史中丞；夢者本人",
    "context": "正元中，栩國竇參為御史中丞，嘗一夕夢德宗召對於便殿，以錦半臂賜之。",
    "question": "竇參此夢主何應，其官位將如何？",
    "setting": "唐正元中·便殿；夢占（夢天子賜衣物待解）",
    "provenance": C48_PROV_IN,
    "redistributable": False,
    "license_status": LICENSE,
}
c48_gold = {
    "id": "LK2-C48",
    "tradition": "mengzhan",
    "subject": c48_input["subject"],
    "context": c48_input["context"],
    "question": c48_input["question"],
    "setting": c48_input["setting"],
    "provenance": C48_PROV_GOLD,
    "redistributable": False,
    "license_status": LICENSE,
    "master_predictions": [{
        "date": None, "direction": None, "key_assertions": [],
        "master": "客（無名，竇參之客）",
        "source": "《夢占類考》卷六帷服部引宣室志",
        "statement_excerpt": "半臂者，被股肱之衣也。今公夢天子賜之，豈非上將以股肱之位而委公乎？",
        "tradition": "mengzhan",
    }],
    "outcome": {
        "description": "明日果拜中書侍郎平章事。",
        "verified_by": "原文結局文本（逐字）",
    },
    "passage_full": "正元中，栩國竇參為御史中丞，嘗一夕夢德宗召對於便殿，以錦半臂賜之。默念曰：臂者庇也，大邑所庇吾身也；今夢半臂者，上以其叨居顯位，將給半祿，俾我致政乎。客有解曰：半臂者，被股肱之衣也；今公夢天子賜之，豈非上將以股肱之位而委公乎？明日果拜中書侍郎平章事。宣室志",
    "grade_suggestion": "A",
    "grade_reason": "客解逐字獨立成句，指向股肱之位（宰相職）；結局為獨立句，具時限（明日）與確切官名（中書侍郎平章事），非確認式；夢者自念誤解與客解並錄可分離，輸入/金標可分離。",
    "contamination_suggestion": "mid",
    "contamination_reason": "竇參為唐貞元名相，其拜相屬可先驗知悉的史實一側，污染不低；但本夢軼事出宣室志筆記系統，非正史本傳主幹定本敘事，未至 high。R51 登記原作 mid-high，按本輪四檔（high/mid/low-mid/low）作 mid（偏高一端）。",
    "notes": "結構：夢者先自念一解（誤：給半祿致政），客解為金標斷面，自念只照錄於 passage_full、不入輸入。字讀：年號原書作「正元」（貞元）照錄；R51 待核「栩國」二字 R52 視覺讀定為栩國；「大邑」之大字字形近太，依 R51 登記作大，列待核候主持裁。",
    "record_status": "candidate-r52-mining",
}

c51_input = {
    "id": "LK2-C51",
    "tradition": "mengzhan",
    "subject": "李蕃，唐人，未遇時挈家居揚州；夢者為其友高貟外，夢中所指為李蕃（李三郎）",
    "context": "唐李蕃未遇時，挈家居揚州，與高貟外善。一日，高既來謁，至晚又至李，問其故。高云：朝來看公，歸困甚，就寢，夢有人召出城荊棘中，行見舊莊客，亡已十數年矣。謂某曰：員外不合至此，此宜急返。其謂曰：汝安得在此？曰：為陰吏，蒙差當直李三郎。其曰：何李三郎？曰：住參佐橋，知員外與三郎往還，故此祇候。某曰：三郎安得如此？曰：是紗籠中人。",
    "question": "高員外此夢所指李蕃（李三郎）前程如何，紗籠中人何謂？",
    "setting": "唐·揚州；夢占（友人夢陰吏語涉他人前程，夢象待解）",
    "provenance": C51_PROV_IN,
    "redistributable": False,
    "license_status": LICENSE,
}
c51_gold = {
    "id": "LK2-C51",
    "tradition": "mengzhan",
    "subject": c51_input["subject"],
    "context": c51_input["context"],
    "question": c51_input["question"],
    "setting": c51_input["setting"],
    "provenance": C51_PROV_GOLD,
    "redistributable": False,
    "license_status": LICENSE,
    "master_predictions": [{
        "date": None, "direction": None, "key_assertions": [],
        "master": "新羅僧（無名，李蕃後遇）",
        "source": "《夢占類考》卷六紗籠類引原化記",
        "statement_excerpt": "凡為宰相者，冥司必潛以紗籠護之，恐為異物所擾。",
        "tradition": "mengzhan",
    }],
    "outcome": {
        "description": "後李竟得拜相云。",
        "verified_by": "原文結局文本（逐字）",
    },
    "passage_full": "唐李蕃未遇時，挈家居揚州，與高貟外善。一日，高既來謁，至晚又至李，問其故。高云：朝來看公，歸困甚，就寢，夢有人召出城荊棘中，行見舊莊客，亡已十數年矣。謂某曰：員外不合至此，此宜急返。其謂曰：汝安得在此？曰：為陰吏，蒙差當直李三郎。其曰：何李三郎？曰：住參佐橋，知員外與三郎往還，故此祇候。某曰：三郎安得如此？曰：是紗籠中人。此言合是佳兆，但不知紗籠所謂耳。後遇新羅僧，言：凡為宰相者，冥司必潛以紗籠護之，恐為異物所擾。乃知紗籠宰相事也。後李竟得拜相云。原化記",
    "grade_suggestion": "A",
    "grade_reason": "僧解逐字獨立，以通例形式給出宰相指向；結局「後李竟得拜相云」為獨立事件句、方向與僧解對應，非確認式套語。但成色為 A 之弱端（R51 登記 A-）：結局僅一短句、帶傳聞語氣「云」、無時限與官名細節，斷語亦為通例解說而非對個案直斷；從嚴可降 B，候主持終裁。",
    "contamination_suggestion": "mid",
    "contamination_reason": "李蕃（史稱李藩）為唐名相，拜相屬其已知仕途主線，先驗可知性不低；但本夢軼事出原化記筆記系統，非正史定本主幹敘事，未至 high。R51 登記原作 mid-high，按本輪四檔作 mid（偏高一端）。",
    "notes": "結構（承 R51 登記）：夢者非傳主本人（高員外夢、所指李蕃），斷語為新羅僧通例解說而非對個案直斷，輸入按此結構立問；高氏「佳兆」自評、僧解與結局均不入輸入。字讀：原書作「挈家」（R51 登記背景 paraphrase 作寄家，照原字改）；「貟」為員之異體照錄（高貟外）；傳主名原書作「蕃」照錄，史稱李藩之異寫候主持知悉；夢語「住參佐橋」R52 視覺讀定。",
    "record_status": "candidate-r52-mining",
}

cards = [(c48_input, c48_gold), (c51_input, c51_gold)]
for inp, gold in cards:
    for suffix, obj in (("input", inp), ("gold", gold)):
        p = OUT / f"{inp['id']}-{suffix}.json"
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
        print("wrote", p)

# ---- stage-2 scan on input cards (recursive, all string values + field names) ----
LEVEL1 = ["断语线索","断曰","断語","正议","正議","验语","驗語","断语：","斷語：","占断","占斷","大师断","大師斷"]
LEVEL2 = ["果验","果然","果應","后验","後驗","结局","結局","应验","應驗"]
FIELD_BLACKLIST = ["断语","断曰","正议","验语","占断","线索","断者","grade","contamination","outcome"]
WHITELIST = {"id","tradition","subject","context","question","setting","provenance","redistributable","license_status"}

def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield (path + "/" + k, k, True)
            yield from walk(v, path + "/" + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        yield (path, obj, False)

report = {}
total = 0
for inp, _ in cards:
    p = OUT / f"{inp['id']}-input.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    assert set(data.keys()) == WHITELIST, (inp["id"], set(data.keys()))
    hits = []
    for path, val, is_key in walk(data):
        if is_key:
            for b in FIELD_BLACKLIST:
                if b in val:
                    hits.append({"field": path, "marker": b, "kind": "field-name"})
        else:
            for m in LEVEL1:
                if m in val:
                    hits.append({"field": path, "marker": m, "kind": "level1"})
            for m in LEVEL2:
                if m in val:
                    hits.append({"field": path, "marker": m, "kind": "level2"})
    report[inp["id"]] = {"file": str(p), "hits": hits, "hit_count": len(hits)}
    total += len(hits)
    print(inp["id"], "input scan hits:", len(hits), hits)

scan_path = ROOT / "digestion" / "SCAN-leikao-r52.json"
scan_path.write_text(json.dumps({"stage": "stage2-card-selfcheck", "per_card": report, "total_hits": total}, ensure_ascii=False, indent=1), encoding="utf-8")
print("scan log:", scan_path, "total:", total)
sys.exit(0 if total == 0 else 1)
