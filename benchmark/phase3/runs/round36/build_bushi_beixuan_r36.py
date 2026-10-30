#!/usr/bin/env python3
"""R36 data-corner, task 1: archive the 9 verified alternates (备选-01..09)
from expansion7/bushi-quanshu/BUILD-REPORT.md as formal case records.

Source of text: the校正全本《卜筮全书》 PDF itself (incoming/wanted-books),
pages rendered at 200dpi and transcribed visually by the data corner on
2026-10-30 (same route as expansion7). Transcriptions below are verbatim
from those page images; nothing is reconstructed from the BUILD-REPORT
one-line summaries.

IDs: BQ-026..BQ-034, continuing the expansion7 BQ sequence in BUILD-REPORT
备选 order. Uniqueness vs POOL-IDS / dev9 / holdout3-13 and the whole-tree
id audit are asserted in build_holdout14_r36.py / audit_ids_holdout14_r36.py.

Boundary ruling (备选-02 -> BQ-027): INCLUDED as A. Rationale registered in
BUILD-NOTES.md: the four A-elements (背景/卦象/断语/结局) are all present in
the original sentence; the outcome "果无望" is only three characters but is
a separable verification clause, and the断语 side carries two concrete
chart facts (用爻无气 + 被日辰克害). Precedent in the same batch: BQ-013
was graded A with the four-character outcome "雨果不止". The original
report's stricter option (downgrade to B) is recorded, not adopted.

Output: expansion12/bushi-quanshu-beixuan/cases.jsonl (9 rows).
No git operations. No prediction, no scoring.
"""
import json
from pathlib import Path

R36 = Path(__file__).resolve().parent
P3 = R36.parents[1]
OUT_DIR = P3 / "expansion12" / "bushi-quanshu-beixuan"
EDITION = ("华龄出版社2016年《四库存目纳甲汇刊（六）·校正全本卜筮全书》"
           "（（明）姚际隆撰，郑同校；ISBN 978-7-5169-0728-3）扫描PDF，用户经学校图书馆提供")
MASTER = "黄金策注家（明，《卜筮全书》辑录）"
CASTING = "六爻纳甲（原书只记月日与卦象，未记起卦工具）"
CLAIMED = "书中注家自述亲历/所验之占（千金赋注文第一人称及实占记录，无另引出处）"
CLAIMED_TIANSHI = "书中注家自述亲历/所验之占（天时注文实占记录，无另引出处）"
CLAIMED_SHENZUO = "书中注家所记实占（神作注文，无另引出处）"
CONTAM_R = "无名/地方小例，不见于通行选本"


def prov(page, claimed):
    return {"work": "《卜筮全书》", "edition": EDITION, "page": page,
            "claimed_source": claimed,
            "language": "zh-Hans（原书简体排印，转录从其字形）"}


def pred(excerpt, direction, assertions, timing=None):
    return {"statement_excerpt": excerpt, "direction": direction,
            "key_assertions": assertions, "timing_claim": timing,
            "source_language": "zh-Hans"}


def outc(desc, direction):
    return {"description": desc, "direction": direction, "source_language": "zh-Hans"}


CASES = [
    {
        "id": "BQ-026",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷八·黄金策（一）总断千金赋注",
        "subject": "乡人（与另一人同日同卜官事者之一）",
        "caster_or_relation": "注家记同乡二人同卜",
        "question": "卜官事（官司/官事结果）",
        "category": "词讼",
        "asked_at": "癸巳日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "恒", "changed_name": None,
                     "chart_lines": "原文未列盘；断语自述：「此二卦官鬼俱带刑爻持世」「恒卦则喜日克去之，又应生世」"},
        "completeness_basis": "原文只记卦名恒与断语援引的刑爻持世、日克官鬼、应生世等象，无全盘",
        "provenance": prov("印刷页146（PDF第163页）（卷八·总断千金赋）", CLAIMED),
        "master_predictions": [pred(
            "「盖此二卦官鬼俱带刑爻持世，皆非吉兆。……恒卦则喜日克去之，又应生世，所以无事也。」（与同则遁卦例 BQ-004 对照同断，原文以对照作结）",
            "positive",
            ["官鬼带刑持世、本非吉兆", "日克去官鬼、应生世，故无事"],
        )],
        "outcome": outc("「一人得恒卦，两边和释」——得恒卦之乡人与对方两边和解、官事消释。", "positive"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A：同日同卜对照例之另一半（BQ-004 为遁卦半），背景、卦名、断语要点与结局「两边和释」俱全且可分离。本例原列 expansion7 备选（主批 25 例上限），R36 建档时回原书页图逐字复核无误。",
        "comment": "与 BQ-004 同出原文一则（癸巳日乡人同卜官事），断语互涉，解读时须并看；三键（乡人＋癸巳日＋官事）与 BQ-004 以卦名（恒/遁）与结局（和释/受刑责）相区分，非同例。",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
    {
        "id": "BQ-027",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷八·黄金策（一）总断千金赋注",
        "subject": "占者（未具名）",
        "caster_or_relation": "注家所记之占",
        "question": "占财（求财成否）",
        "category": "求财",
        "asked_at": "五月乙未日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "泰", "changed_name": "大畜",
                     "chart_lines": "原文：「得泰之大畜卦，用爻无气，又被日辰克害」（本节赋题「主象休囚，怕见刑冲克害」）"},
        "completeness_basis": "原文记本卦泰、变卦大畜与用爻状态（无气、被日辰克害），无全盘",
        "provenance": prov("印刷页147（PDF第164页）（卷八·总断千金赋）", CLAIMED),
        "master_predictions": [pred(
            "「用爻无气，又被日辰克害。」（主象休囚而见克害，故断无望）",
            "negative",
            ["用爻无气（主象休囚）", "用爻被日辰克害", "求财无望"],
        )],
        "outcome": outc("「果无望」——求财果然无望。", "negative"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A（边界例，R36 复核裁定入）：结局仅「果无望」三字，原 expansion7 报告自注从严可降 B；本轮逐例复核裁定维持 A——占问背景（五月乙未日占财）、卦象（泰之大畜）、断语（用爻无气、又被日辰克害，两项具体卦象事实）、结局四要素齐备，结局虽极简但系独立应验句、与断语可分离核验；同批先例 BQ-013 结局「雨果不止」四字判 A，口径一致。从严降 B 之议已登记于 BUILD-NOTES，不采。",
        "comment": "边界例裁定与理由见 expansion12/bushi-quanshu-beixuan/BUILD-NOTES.md；验收引用本例时须连同此成色注记。",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
    {
        "id": "BQ-028",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷八·黄金策（一）天时注",
        "subject": "注家本人",
        "caster_or_relation": "注家自占",
        "question": "卜中秋月（中秋月色/月蚀与否）",
        "category": "天时",
        "asked_at": "八月庚申日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "家人", "changed_name": "观",
                     "chart_lines": "原文：「得家人之观卦」（本节赋题「福德带刑，日月必蚀」，注文以子孙带刑、动化鬼爻等象主日月有蚀）"},
        "completeness_basis": "原文记本卦家人、变卦观，动爻细节未逐爻列明，无全盘",
        "provenance": prov("印刷页158（PDF第175页）（卷八·天时）", CLAIMED_TIANSHI),
        "master_predictions": [pred(
            "「如八月庚申日，予卜中秋月得家人之观卦，果应大雨。」（本节通则：福德（子孙）带刑、动化鬼爻，或官鬼动来刑害，或父带螣蛇来克，皆主日月有蚀——中秋月主不明/有蚀）",
            "negative",
            ["中秋月有蚀/不明（福德带刑之断）"],
        )],
        "outcome": outc("「果应大雨」——中秋果降大雨，月不可见。", "negative"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A：日期、卦名与结局俱全；断语以本节通则形式给出（福德带刑主日月有蚀），个案句只载卦与应验，体例与 BQ-013 同（断语要点自本节赋注定断）。应验形态为大雨蔽月而非月食本身，照原文登记，不另训释。",
        "comment": "",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
    {
        "id": "BQ-029",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷八·黄金策（一）天时注",
        "subject": "占者（未具名）",
        "caster_or_relation": "注家所记之占",
        "question": "占晴（天气晴否）",
        "category": "天时",
        "asked_at": "五月丁丑日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "屯", "changed_name": "无妄",
                     "chart_lines": "原文：「得屯之无妄卦，父母虽动然坐在墓爻」（本节赋题「晴利父爻之入墓」：墓主晦滞，父爻动入即是雨意，终不沾濡）"},
        "completeness_basis": "原文记本卦屯、变卦无妄、父母动坐墓爻，无全盘",
        "provenance": prov("印刷页159（PDF第176页）（卷八·天时）", CLAIMED_TIANSHI),
        "master_predictions": [pred(
            "「父母虽动然坐在墓爻。」（父动入墓主晦滞：虽有雨意而不沾濡，主晴而阴滞）",
            "positive",
            ["应晴", "晴而阴滞（晦滞不爽）"],
        )],
        "outcome": outc("「果应晴而阴滞也」——果然放晴，但阴云滞留不散。", "positive"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A：日期、卦名、断象（父母动坐墓）与结局（晴而阴滞，断语两面俱应）俱全。",
        "comment": "",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
    {
        "id": "BQ-030",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷八·黄金策（一）天时注",
        "subject": "占者（未具名）",
        "caster_or_relation": "注家所记之占",
        "question": "占晴（天气晴否）",
        "category": "天时",
        "asked_at": "辛未日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "损", "changed_name": "小畜",
                     "chart_lines": "原文：「得损之小畜卦，财被合住，喜得日辰带兄冲破合爻」（本节赋题「合财兄克破，无风不晴」）"},
        "completeness_basis": "原文记本卦损、变卦小畜、财爻被合住、日辰带兄冲破，无全盘；原文未记月份",
        "provenance": prov("印刷页160（PDF第177页）（卷八·天时）", CLAIMED_TIANSHI),
        "master_predictions": [pred(
            "「财被合住，喜得日辰带兄冲破合爻。」（财合住本不晴明，兄冲破合则必待风起然后晴）",
            "positive",
            ["先不晴明（财被合住）", "待风起而晴"],
        )],
        "outcome": outc("「果应发风而晴也」——果然先发风、继而放晴。", "positive"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A：卦名、断象（财合住、兄冲破）与结局（发风而晴）俱全；原文未记月份，只录日辰。",
        "comment": "",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
    {
        "id": "BQ-031",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷八·黄金策（一）天时注",
        "subject": "占者（未具名）",
        "caster_or_relation": "注家所记之占",
        "question": "占雨（久晴占雨）",
        "category": "天时",
        "asked_at": "五月甲戌日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "屯", "changed_name": None,
                     "chart_lines": "原文：「得屯卦，财不出现，父爻衰空……喜得日辰冲并，卦中土鬼暗动」（静卦）"},
        "completeness_basis": "原文记本卦屯（无变卦）、财不出现、父爻衰空、土鬼暗动，无全盘",
        "provenance": prov("印刷页162（PDF第179页）（卷八·天时）", CLAIMED_TIANSHI),
        "master_predictions": [pred(
            "「财不出现，父爻衰空，同是雨晴难定之象，喜得日辰冲并，卦中土鬼暗动。」（难定之象得日辰冲并、土鬼暗动而决有雨；鬼临土爻克水，故雨不多）",
            "positive",
            ["有雨", "雨量不多（鬼临土爻克水）"],
        )],
        "outcome": outc("「果应有雨，但鬼临土爻克水，所以雨亦不多也」——果然有雨，但雨量不多。", "positive"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A：日期、卦名、断象与结局（有雨而不多，量级亦应）俱全。",
        "comment": "",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
    {
        "id": "BQ-032",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷十·黄金策（三）神作注",
        "subject": "占者（未具名，卜种水田者）",
        "caster_or_relation": "注家所记之占",
        "question": "卜种水田（种田可成否）",
        "category": "农事",
        "asked_at": "乙亥日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "既济", "changed_name": "屯",
                     "chart_lines": "原文：「得既济之屯卦，父母空亡」（本节赋题「或空或动，其田还恐属他人」：父母空亡，田种不成）"},
        "completeness_basis": "原文记本卦既济、变卦屯、父母空亡，无全盘；原文未记月份",
        "provenance": prov("印刷页229（PDF第246页）（卷十·神作）", CLAIMED_SHENZUO),
        "master_predictions": [pred(
            "「父母空亡。」（父母空亡则田种不成——本节注文通则）",
            "negative",
            ["田种不成"],
        )],
        "outcome": outc("「果种不成」——其田果然种不成。", "negative"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A：卦名、断象（父母空亡）与结局俱全；与同页 BQ-023（姤之乾·回赎）、BQ-033、BQ-034 同在本节「百发百中」一段连举，四例三键互异。",
        "comment": "同页连举四例（既济之屯/姤之乾/观之讼/颐之噬嗑）中姤之乾一例已由 expansion7 收为 BQ-023，本批不重复收录。",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
    {
        "id": "BQ-033",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷十·黄金策（三）神作注",
        "subject": "占者（未具名，卜田者）",
        "caster_or_relation": "注家所记之占",
        "question": "卜田（田之归属/可得否）",
        "category": "农事",
        "asked_at": "辛亥日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "观", "changed_name": "讼",
                     "chart_lines": "原文：「得观之讼，世上父母动化出午火生合应爻，又遇官鬼旺动」"},
        "completeness_basis": "原文记本卦观、变卦讼、世上父母动化午火、官鬼旺动，无全盘；原文未记月份",
        "provenance": prov("印刷页229（PDF第246页）（卷十·神作）", CLAIMED_SHENZUO),
        "master_predictions": [pred(
            "「世上父母动化出午火生合应爻，又遇官鬼旺动，遂与邻人拘讼。」（父母动而生合应爻、官鬼旺动：田有更变、涉讼而属他人）",
            "negative",
            ["与邻人拘讼（涉讼）", "其田终卖与他人"],
        )],
        "outcome": outc("「其田果应卖与他人」——其田果然卖给了他人。", "negative"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A：卦名、断象与结局俱全（拘讼过程与卖田结局分载）。",
        "comment": "与同页 BQ-032、BQ-034 及 BQ-023 三键互异（日辰/卦名/事项俱不同）。",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
    {
        "id": "BQ-034",
        "tradition": "六爻",
        "master": MASTER,
        "source_work": "《卜筮全书》卷十·黄金策（三）神作注",
        "subject": "占者（未具名，卜田者）",
        "caster_or_relation": "注家所记之占",
        "question": "卜田（田可得种否）",
        "category": "农事",
        "asked_at": "癸巳日",
        "casting_method": CASTING,
        "hexagram": {"original_name": "颐", "changed_name": "噬嗑",
                     "chart_lines": "原文：「得颐之噬嗑，世临勾陈土财发动」（勾陈主田土、迟滞）"},
        "completeness_basis": "原文记本卦颐、变卦噬嗑、世临勾陈土财发动，无全盘；原文未记月份",
        "provenance": prov("印刷页229（PDF第246页）（卷十·神作）", CLAIMED_SHENZUO),
        "master_predictions": [pred(
            "「世临勾陈土财发动。」（世临勾陈土财发动，田事牵滞、终不得成）",
            "negative",
            ["其田不得成（田主自种）"],
        )],
        "outcome": outc("「其田果因田主自种而不得成也」——其田果然因田主自己耕种而未能得成。", "negative"),
        "contamination": "low",
        "contamination_rationale": CONTAM_R,
        "grade_note": "A：卦名、断象（世临勾陈土财发动）与结局（田主自种、不得成）俱全。",
        "comment": "与同页 BQ-032、BQ-033 及 BQ-023 三键互异。",
        "chart_complete": False,
        "month_day_complete": False,
        "outcome_grade": "A",
        "holdout_eligible": True,
        "license_status": "内部研究使用（用户经学校图书馆提供）",
        "redistributable": False,
    },
]


def main():
    assert len(CASES) == 9
    ids = [c["id"] for c in CASES]
    assert ids == [f"BQ-{n:03d}" for n in range(26, 35)], ids
    for c in CASES:
        for k in ("subject", "question", "master_predictions", "outcome",
                  "outcome_grade", "contamination", "provenance"):
            assert c.get(k), (c["id"], k)
        assert c["outcome_grade"] == "A" and c["contamination"] == "low"
        assert c["master_predictions"][0]["statement_excerpt"].strip()
        assert c["outcome"]["description"].strip()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(c, ensure_ascii=False) + "\n" for c in CASES)
    (OUT_DIR / "cases.jsonl").write_text(text, encoding="utf-8")
    print("wrote", OUT_DIR / "cases.jsonl", "rows:", len(CASES))


if __name__ == "__main__":
    main()
