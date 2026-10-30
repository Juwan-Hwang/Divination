#!/usr/bin/env python3
# R53 春渚余卷开采建卡脚本（唯一名，仅本轮使用）
# 合格候选 1 张：CZ2-006 丑年世科第（卷一，相墓，xiangshu）
import json, pathlib

BASE = pathlib.Path.home() / "workspace/divination/benchmark/phase3/runs/round53/digestion/cards-mining-chunzhu-r53"

prov = ("《春渚紀聞》卷一·丑年世科第；維基文庫在線文本（zh.wikisource.org《春渚紀聞》卷01頁，"
        "主會話活瀏覽器存檔；本地存檔 incoming/online-mining/chunzhu-juan01-wikisource.txt，"
        "標題 L33、正文 L35；原文證據 incoming/online-mining/chunzhu-卷01-raw.wiki）；存檔日期 2026-10-31")
lic = "古典文本公有領域（學津討原本系）；維基文庫站點條款未逐條核，內部研究用"
anchor = {"anchor_type": "相術（相墓）＝所相先墓（墓地本身）",
          "present_in_source": True, "carried_in_card": True}

inp = {
    "anchor_check": anchor,
    "context": "先友提學張公大亨，字嘉甫，霅川人。先墓在弁山之麓，有相墓者為之相其墓。家人初未之信。",
    "id": "CZ2-006",
    "license_status": lic,
    "provenance": prov,
    "question": "請言此先墓主何應驗？",
    "redistributable": False,
    "setting": "北宋·霅川弁山；相墓術（相術/風水，以先墓相）",
    "subject": "張大亨（字嘉甫，霅川人，官提學）一家；所相者為其先墓（弁山之麓）；占者為相墓者（原文未具名）",
    "tradition": "xiangshu",
}

passage = ("先友提學張公大亨，字嘉甫，霅川人。先墓在弁山之麓，相墓者云：「公家遇丑年，"
           "有赴舉者必登高第。」初未之信。熙寧癸丑，嘉甫之父通直公著登第；元豐乙丑，"
           "嘉甫登乙科；大觀己丑，嘉甫之兄大成中甲科；重和辛丑，嘉甫之弟大受復中乙科。"
           "此亦人事地理相符之異也。")

gold = dict(inp)
gold.update({
    "contamination_reason": ("張大亨一家為霅川地方人物，四次登第皆其家門本事、非著名事件，"
                             "文本外無名案流傳之跡。本輪派單禁聯網，席位未做在線冷門性檢索，"
                             "此判級據文本內證與一般史識作出；§2(ii)(γ) 冷門性落盤證據待主持復核。"),
    "contamination_suggestion": "low",
    "grade_reason": ("斷語逐字獨立成文（「公家遇丑年，有赴舉者必登高第」）；結局為四代丑年登第的"
                     "逐項具體記載（干支年＋何人＋科別：癸丑父著登第、乙丑嘉甫乙科、己丑兄大成甲科、"
                     "辛丑弟大受乙科），逐項對應斷語，非確認式；輸入/金標可分離。占者佚名一節，"
                     "依 R53 PREREG §2(ii) 裁定理由（四濾 (i) 所驗為斷語逐字與結局可分離，占者姓名非檢驗對象）判過。"),
    "grade_suggestion": "A",
    "master_predictions": [{
        "date": None, "direction": None, "key_assertions": [],
        "master": "相墓者（佚名，《春渚紀聞》卷一）",
        "source": "《春渚紀聞》卷一·丑年世科第",
        "statement_excerpt": "公家遇丑年，有赴舉者必登高第。",
        "tradition": "xiangshu",
    }],
    "notes": ("復核點兩項留主持：① 錨點——主導錨點為所相先墓本身（弁山之麓），見於源文且已載入輸入卡；"
              "然源文未載該墓地形細節（方位山勢等），錨點成色弱於 CZ2-004（墓圖），是否判部分在場留主持裁。"
              "② 佚名＋冷門性證據——占者佚名，依 §2(ii) 佚名具斷語者附條件口徑建為候選；(γ) 冷門性在線檢索記錄"
              "因本輪禁聯網未附，入賬前須主持補核。本卡與卷二張鬼靈相墓術（CZ2-004/005）為異人異墓異案，三鍵不撞。"),
    "outcome": {
        "description": "熙寧癸丑，嘉甫之父通直公著登第；元豐乙丑，嘉甫登乙科；大觀己丑，嘉甫之兄大成中甲科；重和辛丑，嘉甫之弟大受復中乙科。",
        "verified_by": "原文結局文本（逐字）",
    },
    "passage_full": passage,
    "provenance": prov + "；transcription=online-verbatim；全文 SHA-256 33ad77e321f0b8da44286c2c8598a01add6fb18ae0e869a794a10fe21e68a8ba",
    "record_status": "candidate-r53-mining",
})

for sub, obj in (("inputs", inp), ("gold", gold)):
    p = BASE / sub / "CZ2-006.json"
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("wrote", p)
