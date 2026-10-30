# -*- coding: utf-8 -*-
"""R49 阅微续检写卡脚本：YW2-001（束城李某妇案扶乩判诗）。
口径：round49/PREREG.md §1①。输入侧只含对象基本信息与当时背景；
断语与结局一律不入输入侧（下方零命中断言）。"""
import json, pathlib

OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round49/digestion/cards-mining-yuewei")
OUT.mkdir(parents=True, exist_ok=True)

URL = "https://www.arteducation.com.tw/guwen/bookv_17081.html"
PROV = ("《阅微草堂笔记》·卷三·滦阳消夏录三(1)；在线全文实取 arteducation 分页站卷三(1) "
        f"L21-22 {URL}；transcription=online-verbatim；访问日期 2026-10-30")

inp = {
    "id": "YW2-001",
    "tradition": "fuji",
    "subject": "束城李某（贩枣者）与邻县一少妇，及少妇之夫",
    "context": ("束城李某以贩枣往来于邻县，私诱居停主人少妇归家；比至家，其妻已先偕人逃走。"
                "既而此妇不乐居田家，复随一少年遁去。后其夫踪迹至束城，欲讼李；"
                "李以妇已他去、无佐证，坚不承认。纠纷间，闻里有扶乩者，众议质问于乩仙。"),
    "question": "此讼纠纷真相如何？（众质于乩仙）",
    "setting": "清·束城；里有扶乩者，众以讼争质于仙，仙判以诗（隐语待解型，输入侧只入所问）",
    "provenance": PROV,
    "record_status": "candidate-r49-mining",
    "redistributable": False,
    "license_status": "古典文本公有领域；在线转录站条款未明，内部研究用",
    "notes": ("归型单注：乩判诗为隐语待解型断语，照 R47 PREREG §1⑦ 写死边界，输入侧只入所问与背景，"
              "乩诗与事后揭示不入输入侧，请主持裁定归型。占者为里中扶乩之仙（佚名），"
              "照 R48 SS-004 扶乩者佚名建卡先例登记滤(i)判定。"),
}

gold = dict(inp)
gold.update({
    "master_predictions": [
        {
            "master": "扶乩之仙（佚名，里有扶乩者）",
            "date": None,
            "tradition": "fuji",
            "direction": None,
            "key_assertions": [],
            "source": "《阅微草堂笔记》·卷三·滦阳消夏录三",
            "statement_excerpt": "鴛鴦夢好兩歡娛，記否羅敷自有夫，今日相逢需一笑，分明依樣畫葫蘆。",
        }
    ],
    "outcome": {
        "description": "其夫默然徑返。兩邑接壤有知其事者，曰此婦初亦其夫誘來者也。",
        "verified_by": "原文结局文本（逐字）",
    },
    "passage_full": ("束城李某，以販棗往來於鄰縣，私誘居停主人少婦歸。比至家，其妻先已偕人逃，"
                     "自詫曰：幸攜此婦來，不然鰥矣。人計其妻遷賄之期，正當此婦乘垣後日。適相報，尚不悟耶？"
                     "既而此婦不樂居田家，復隨一少年遁，始茫然自失。後其夫蹤跡至束城，欲訟李，"
                     "李以婦已他去，無佐證，堅不承。糾紛間，聞里有扶乩者，眾曰：盍質於仙。"
                     "仙判一詩曰：鴛鴦夢好兩歡娛，記否羅敷自有夫，今日相逢需一笑，分明依樣畫葫蘆。"
                     "其夫默然徑返。兩邑接壤有知其事者，曰此婦初亦其夫誘來者也。"),
    "grade_suggestion": "B",
    "grade_reason": ("乩判诗可逐字录、结局为断语后独立文本（其夫默然径返＋知情者揭示此妇初亦其夫诱来，"
                     "与判诗「罗敷自有夫／依样画葫芦」之义逐项对应、可剥离）；但结局事件本身仅「默然径返」一句、"
                     "无具体后果细节，按 R48 SS-003 确认式薄结局先例建议 B，只登记候选、预期不入账。"),
    "contamination_suggestion": "low",
    "contamination_reason": ("2026-10-30 以判诗标志句「鴛鴦夢好兩歡娛」精确检索，零个案命中（返回全为本书通论与无关诗词页）；"
                             "对象仅称束城李某、占者佚名，无名人无名案，冷门性证据如上落盘。"),
})

# 输入侧零命中断言：断语标志语与结局标志语一律不得出现在输入侧
inp_text = json.dumps(inp, ensure_ascii=False)
for forbidden in ["鴛鴦夢好", "羅敷自有夫", "依樣畫葫蘆", "默然徑返", "初亦其夫誘來"]:
    assert forbidden not in inp_text, f"输入侧命中禁词: {forbidden}"

(OUT / "YW2-001-input.json").write_text(json.dumps(inp, ensure_ascii=False, indent=2), encoding="utf-8")
(OUT / "YW2-001-gold.json").write_text(json.dumps(gold, ensure_ascii=False, indent=2), encoding="utf-8")

# 计数与可解析断言
files = sorted(OUT.glob("YW2-*.json"))
assert len(files) == 2, files
for f in files:
    json.loads(f.read_text(encoding="utf-8"))
print("OK: 1 pair written:", [f.name for f in files])
