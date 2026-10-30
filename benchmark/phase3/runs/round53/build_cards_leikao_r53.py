#!/usr/bin/env python3
"""R53 leikao cont: build card LK2-C58 (戴斗避火) + stage-2 input scan.
Format follows R52 build_cards_leikao_r52.py; whitelist extended by anchor_check per PREREG §2(i)."""
import json, sys, pathlib

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "digestion" / "cards-mining-leikao-r53"
OUT.mkdir(parents=True, exist_ok=True)

LICENSE = "古典文本公有領域（明張鳳翼輯《夢占類考》）；掃描底本僅內部研究用"
PROV = ("《夢占類考》卷九燈火部「戴斗避火」條，PDF 306 左；底本 incoming/wanted-books-3/Book/"
        "梦占类考 (（明）张凤翼辑).pdf（438 頁）；原書標出處古今夢徵；transcription=visual"
        "（R53 頁圖 130dpi 視覺轉錄＋3 倍裁切放大覆核）")
CTX = "黃刑部芸，豐城人，夢鄰家火起，延及倉，皇戴斗登山而避，山上冠冕者迎酌之，已而見門外一赤馬，遂乘之而寤。"
Q = "黃芸此夢主何應，其科名將如何？"
SUBJ = "黃芸，豐城人；夢者本人（原文冠以其後官「刑部」稱之）"
SETG = "豐城；夢占（鄰火、戴斗、赤馬待解）"

c58_input = {
    "id": "LK2-C58",
    "tradition": "mengzhan",
    "subject": SUBJ,
    "context": CTX,
    "question": Q,
    "setting": SETG,
    "provenance": PROV,
    "redistributable": False,
    "license_status": LICENSE,
    "anchor_check": {
        "anchor_type": "夢象符號",
        "present_in_source": True,
        "carried_in_card": True,
        "anchors": ["鄰家火起延及倉", "戴斗登山", "山上冠冕者迎酌", "門外一赤馬"],
    },
}
c58_gold = {
    **c58_input,
    "master_predictions": [
        {
            "date": None,
            "direction": None,
            "key_assertions": [],
            "master": "童軒（僉憲；原文作「童僉憲軒」）",
            "source": "《夢占類考》卷九燈火部引古今夢徵",
            "statement_excerpt": "火者，文明之象，應為丙丁；赤，火色，馬應為午；戴斗，魁在頭上也。",
            "tradition": "mengzhan",
        }
    ],
    "outcome": {
        "description": "黃至丙午鄉試，果中江西詩經亞魁。",
        "verified_by": "原文結局文本（逐字）",
    },
    "passage_full": ("黃刑部芸，豐城人，夢鄰家火起，延及倉，皇戴斗登山而避，山上冠冕者迎酌之，"
                     "已而見門外一赤馬，遂乘之而寤。童僉憲軒解之云：火者，文明之象，應為丙丁；"
                     "赤，火色，馬應為午；戴斗，魁在頭上也。黃至丙午鄉試，果中江西詩經亞魁。古今夢徵"),
    "grade_suggestion": "A",
    "grade_reason": ("占者童軒具名（僉憲為其官稱），斷語逐字獨立成句，逐象給出丙丁／午／魁的對應，"
                     "指向丙午年科試居魁列；結局為獨立句，年份（丙午）、場次（江西鄉試）、"
                     "經目與名次（詩經亞魁）俱具體，非確認式收束；輸入／金標可分離。"),
    "contamination_suggestion": "low",
    "contamination_reason": ("黃芸、童軒皆明代地方個案人物，本軼事出《古今夢徵》夢案專書，"
                             "非正史本傳定本敘事，先驗知悉面窄；三鍵去重（masters-dataset、phase3/data、"
                             "round46–52 登記）以黃芸／童軒／戴斗避火檢索無命中，淨新。"),
    "notes": ("錨點：夢象符號（火、赤馬、戴斗、冠冕者）在場且全數載入輸入 context。"
              "「皇戴斗」之「皇」照原書錄，義同遑遽，列待核候主持裁。"
              "童軒另見本輪 PDF 319「黃曆十五冊」條為事後解者、同頁「一級六七級」條為夢者本人"
              "（續文在 PDF 320，本輪掛起）。"),
    "record_status": "candidate-r53-mining",
}

for suffix, obj in (("input", c58_input), ("gold", c58_gold)):
    p = OUT / f"LK2-C58-{suffix}.json"
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    print("wrote", p)

LEVEL1 = ["断语线索", "断曰", "断語", "正议", "正議", "验语", "驗語", "断语：", "斷語：", "占断", "占斷", "大师断", "大師斷"]
LEVEL2 = ["果验", "果然", "果應", "后验", "後驗", "结局", "結局", "应验", "應驗"]
FIELD_BLACKLIST = ["断语", "断曰", "正议", "验语", "占断", "线索", "断者", "grade", "contamination", "outcome"]
WHITELIST = {"id", "tradition", "subject", "context", "question", "setting", "provenance",
             "redistributable", "license_status", "anchor_check"}

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

data = json.loads((OUT / "LK2-C58-input.json").read_text(encoding="utf-8"))
assert set(data.keys()) == WHITELIST, set(data.keys())
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
report = {"LK2-C58": {"file": str(OUT / "LK2-C58-input.json"), "hits": hits, "hit_count": len(hits)}}
scan_path = ROOT / "digestion" / "SCAN-leikao-r53.json"
scan_path.write_text(json.dumps({"stage": "stage2-card-selfcheck", "per_card": report,
                                 "total_hits": len(hits)}, ensure_ascii=False, indent=1), encoding="utf-8")
print("scan:", scan_path, "total:", len(hits), hits)
sys.exit(0 if not hits else 1)
