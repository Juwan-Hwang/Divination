#!/usr/bin/env python3
"""R51 yuewei mining: write YW4-001 pair (inputs/gold separated).
Input-side banned-word assertions: no prediction/outcome marker phrases anywhere on input side."""
import json, os
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round51/digestion/cards-mining-yuewei-r51"
os.makedirs(OUT, exist_ok=True)

common = {
    "id": "YW4-001",
    "tradition": "ming",
    "subject": "阮吾山（杨盻刑部同官）",
    "context": "杨主事盻，纪昀甲辰典试所取士也，相法及推算八字五星皆有验。官刑部时，与阮吾山共事。盻以其法推算吾山仕途，已有所断，然当时刑部侍郎并不缺员，盻亦自惑其故。次日堂参后，盻私语同官，另有一语断其出缺之由。",
    "question": "杨盻推阮吾山仕途的断语为何？侍郎不缺员，其所断出缺之由又为何？（输入侧只入背景与疑问，断语与结局不入）",
    "setting": "清·京师刑部；杨盻以相法及推算八字五星为同官阮吾山推仕途，先公开语人、次日堂参后私语同官",
    "provenance": "《阅微草堂笔记》·卷八·如是我闻二(5)；在线全文实取 arteducation 分页站卷八(5) https://www.arteducation.com.tw/guwen/bookv_17106.html；transcription=online-verbatim；访问日期 2026-10-31",
    "record_status": "candidate-r51-mining",
    "redistributable": False,
    "license_status": "古典文本公有领域；在线转录站条款未明，内部研究用",
}

inp = dict(common)
inp["notes"] = "同条另有一子案，只登记于 MINING-yuewei-cont-r51.md、不并入本卡。本卡判级与污染复核点见 gold 侧。"

gold = dict(common)
gold["notes"] = "同条另有杨盻推其子死期一子案：原文死期只作「某月」、结局仅「果如所说」，毙 (i)/(ii)，只登记于 MINING-yuewei-cont-r51.md、不并入本卡断面。本卡断面以出缺一断为核，判级与污染两点请主持复核（详 grade_reason / contamination_reason）。"
gold.update({
    "master_predictions": [
        {
            "master": "杨盻（杨主事，纪昀甲辰所取士）",
            "date": None,
            "tradition": "ming",
            "direction": None,
            "key_assertions": [],
            "source": "《阅微草堂笔记》·卷八·如是我闻二",
            "statement_excerpt": "以我法论，吾山半月内当为刑部侍郎，然今刑部侍郎不缺员，是何故耶？（次日堂参后私语同官）杜公缺也。"
        }
    ],
    "outcome": {
        "description": "既而杜凝台果有伊犁之役。",
        "verified_by": "原文结局文本（逐字；独立事件，非确认式）"
    },
    "passage_full": "杨主事盻，余甲辰典试所取士也，相法及推算八字五星皆有验。官刑部时，与阮吾山共事，忽语人曰：以我法论，吾山半月内当为刑部侍郎，然今刑部侍郎不缺员，是何故耶？次日堂参后，私语同官曰：杜公缺也。既而杜凝台果有伊犁之役。一日，仓皇乞假，归来辞余，曰：家惟一子侍老父，今推子某月当死，恐老父过哀，故急归耳。是时尚未至死期，后询其乡人，果如所说，尤可异也。",
    "grade_suggestion": "A",
    "grade_reason": "断语逐字可录且具体（半月内陞侍郎＋出缺者为杜公）；结局「杜凝台果有伊犁之役」为独立具体事件文本、非确认式，与「杜公缺也」一断逐项对应。单注：阮吾山本人陞任原文未再叙，核验落在出缺一断，主持若以陞任未叙为据可降 B，本席照实登记不粉饰。",
    "contamination_suggestion": "low-mid",
    "contamination_reason": "对象阮吾山与出缺者杜凝台均为侍郎级官员，按口径自 mid 起评从严；但 2026-10-31 以标志句「吾山半月内当为刑部侍郎」「杜凝台果有伊犁之役」精确检索均零个案命中（返回皆无关人物与本书通论页），以「杜凝台」「杨盻」检索亦未见二人独立条目/专页，个案冷僻，据冷门性证据降一档至 low-mid；入账与否候主持终裁（照 R50 台账口径：low-mid 只登记不入账）。"
})

banned = ["杜公缺", "杜凝台", "伊犁", "半月内当为", "半月內當為", "果有伊犁", "某月当死", "某月當死", "果如所说", "果如所說"]
inp_text = json.dumps(inp, ensure_ascii=False)
for b in banned:
    assert b not in inp_text, f"input side leak: {b}"
for name, obj in [("YW4-001-input.json", inp), ("YW4-001-gold.json", gold)]:
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
print("OK: 1 pair written:", sorted(os.listdir(OUT)))
