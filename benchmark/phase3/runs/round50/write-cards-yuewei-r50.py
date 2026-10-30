# -*- coding: utf-8 -*-
"""R50 阅微续检写卡脚本：YW3-001（赵孙英扶乩预告对句）、YW3-002（戴户曹梦冥司簿「犀」字）。
口径：round50/PREREG.md §2②。输入侧只含对象基本信息与当时背景；
断语与结局一律不入输入侧（下方零命中断言）。文本 2026-10-30 自 arteducation 分页站复取逐字核对。"""
import json, pathlib

OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/cards-mining-yuewei-r50")
OUT.mkdir(parents=True, exist_ok=True)

DATE = "2026-10-30"

# ---------- YW3-001 ----------
URL1 = "https://www.arteducation.com.tw/guwen/bookv_17094.html"
PROV1 = ("《阅微草堂笔记》·卷六·滦阳消夏录六(2)；在线全文实取 arteducation 分页站卷六(2) "
         f"L2 {URL1}；transcription=online-verbatim；访问日期 {DATE}")

inp1 = {
    "id": "YW3-001",
    "tradition": "fuji",
    "subject": "冀宁道赵公孙英，及其幕友乔、车二姓",
    "context": ("阳曲王近光言，冀宁道赵公孙英有两幕友，一姓乔，一姓车，合雇一骡轿回籍，"
                "赵公戏以其姓作对曰：乔，车二幕友，各乘半轿而行。恰皆轿之半字也。"
                "时署中召仙，即举以请对。越半载，又召仙乩。"),
    "question": "赵公戏对「乔、车二幕友，各乘半轿而行」举请乩仙属对，能否得对？（输入侧只入所请，乩判不入）",
    "setting": "清·冀宁道署中扶乩召仙；先后两次召乩，间隔半载",
    "provenance": PROV1,
    "record_status": "candidate-r50-mining",
    "redistributable": False,
    "license_status": "古典文本公有领域；在线转录站条款未明，内部研究用",
    "notes": ("归型单注：占者为署中扶乩之仙（佚名），照 R48 SS-004、R49 YW2-001 先例登记滤(i)判定；"
              "严口径下「具名占者」一条存风险，请主持复核。乩判含预告时地（四日后辰巳间南门外），"
              "结局为届期遣役侦视的独立事件文本，非确认式。"),
}

gold1 = dict(inp1)
gold1.update({
    "master_predictions": [
        {
            "master": "扶乩之仙（佚名，赵公署中召仙）",
            "date": None,
            "tradition": "fuji",
            "direction": None,
            "key_assertions": [],
            "source": "《阅微草堂笔记》·卷六·滦阳消夏录六",
            "statement_excerpt": ("（初判）此是实人实事，非可强凑而成。"
                                  "（越半载再判）前对吾已得之矣。卢、马两书生，共引一驴而走。"
                                  "又判曰：四日后，辰巳之间，往南门外候之。"),
        }
    ],
    "outcome": {
        "description": "至期遣役侦视，果有卢，马两生，以一驴负新科墨卷，赴会城出售。",
        "verified_by": "原文结局文本（逐字）",
    },
    "passage_full": ("阳曲王近光言，冀宁道赵公孙英有两幕友，一姓乔，一姓车，合雇一骡轿回籍，"
                     "赵公戏以其姓作对曰：乔，车二幕友，各乘半轿而行。恰皆轿之半字也。"
                     "时署中召仙，即举以请对，乩判曰：此是实人实事，非可强凑而成。"
                     "越半载，又召仙乩，忽判曰：前对吾已得之矣。卢、马两书生，共引一驴而走。"
                     "又判曰：四日后，辰巳之间，往南门外候之。至期遣役侦视，果有卢，马两生，"
                     "以一驴负新科墨卷，赴会城出售，赵公笑曰：巧则诚巧。然两生之受侮深矣，"
                     "此所谓箭在弦上，不得不发。虽仙人亦忍俊不禁也。"),
    "grade_suggestion": "B",
    "grade_reason": ("乩判与预告可逐字录，结局为届期侦视的独立事件文本、非确认式；"
                     "但案体属戏对巧合、断语主体为对句而非问事吉凶断，且初判有「非可强凑」的过程性表述，"
                     "建议 B，只登记候选、预期不入账。"),
    "contamination_suggestion": "low",
    "contamination_reason": ("2026-10-30 以乩判标志句「盧、馬兩書生，共引一驢而走」精确检索，零个案命中"
                             "（返回全为本书通论与目录页）；对象为地方官与无名书生，无名人无名案，冷门性证据如上。"),
})

# ---------- YW3-002 ----------
URL2 = "https://www.arteducation.com.tw/guwen/bookv_17096.html"
PROV2 = ("《阅微草堂笔记》·卷六·滦阳消夏录六(4)；在线全文实取 arteducation 分页站卷六(4) "
         f"L21 {URL2}；transcription=online-verbatim；访问日期 {DATE}")

inp2 = {
    "id": "YW3-002",
    "tradition": "mengzhan",
    "subject": "戴临（户曹，以工书供俸内廷）",
    "context": ("戴户曹临，以工书供俸（供奉）内廷，尝梦至冥司，遇一吏故友也，留与谈，"
                "偶揭其簿，正见己名下朱笔草书，似一犀字，吏遂夺而掩之。意似薄怒，问之亦不答，"
                "忽惶遽而醒，莫测其故。偶告裘文达公求解。"),
    "question": "梦中冥司簿上己名下朱笔草书似「犀」字，主何吉凶？（告裘文达公求解）",
    "setting": "清·京师；梦后以梦告裘文达公（裘曰修），文达沉思而解",
    "provenance": PROV2,
    "record_status": "candidate-r50-mining",
    "redistributable": False,
    "license_status": "古典文本公有领域；在线转录站条款未明，内部研究用",
    "notes": ("梦占例：梦象（冥司簿朱笔似犀字）入输入侧，解者断语与结局入金标侧。"
              "解者裘文达公为名人，个案本身冷僻，污染按名人预设起评后以冷门性证据降至 low-mid，请主持复核。"),
}

gold2 = dict(inp2)
gold2.update({
    "master_predictions": [
        {
            "master": "裘文达公（裘曰修）",
            "date": None,
            "tradition": "mengzhan",
            "direction": None,
            "key_assertions": [],
            "source": "《阅微草堂笔记》·卷六·滦阳消夏录六",
            "statement_excerpt": "此殆阴曹简便之籍，如部院之略节，户中二字，连写颇似犀字。君其终于户部郎中乎？",
        }
    ],
    "outcome": {
        "description": "后竟如文达之言。",
        "verified_by": "原文结局文本（逐字；确认式）",
    },
    "passage_full": ("戴户曹临，以工书供俸内廷，尝梦至冥司，遇一吏故友也，留与谈，偶揭其簿，"
                     "正见己名下朱笔草书，似一犀字，吏遂夺而掩之。意似薄怒，问之亦不答，"
                     "忽惶遽而醒，莫测其故。偶告裘文达公，文达沉思曰：此殆阴曹简便之籍，"
                     "如部院之略节，户中二字，连写颇似犀字。君其终于户部郎中乎？后竟如文达之言。"),
    "grade_suggestion": "B",
    "grade_reason": ("断语可逐字录（拆字式解梦：户中二字连写似犀、断终于户部郎中）；"
                     "结局仅「后竟如文达之言」一语，为确认式薄结局，按四滤(ii)判 B，只登记候选、预期不入账。"),
    "contamination_suggestion": "low-mid",
    "contamination_reason": ("解者裘文达公（裘曰修）为清代名人，按口径名人预设 high 起评；"
                             "但本案对象戴临冷僻，2026-10-30 以断语标志句「戶中二字，連寫頗似犀字」精确检索，"
                             "零个案命中（返回全为本书通论与目录页），据冷门性证据降至 low-mid，检索式如上落盘。"),
})

# 输入侧零命中断言：断语标志语与结局标志语一律不得出现在输入侧
inp1_text = json.dumps(inp1, ensure_ascii=False)
for forbidden in ["盧、馬兩書生", "卢、马两书生", "盧馬", "共引一驢而走", "四日後", "南門外候之", "負新科墨卷", "不得不發", "此是實人實事"]:
    assert forbidden not in inp1_text, f"YW3-001 输入侧命中禁词: {forbidden}"
inp2_text = json.dumps(inp2, ensure_ascii=False)
for forbidden in ["陰曹簡便之籍", "戶中二字", "終於戶部郎中", "後竟如文達之言", "略節"]:
    assert forbidden not in inp2_text, f"YW3-002 输入侧命中禁词: {forbidden}"

for inp, gold in [(inp1, gold1), (inp2, gold2)]:
    cid = inp["id"]
    (OUT / f"{cid}-input.json").write_text(json.dumps(inp, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT / f"{cid}-gold.json").write_text(json.dumps(gold, ensure_ascii=False, indent=2), encoding="utf-8")

files = sorted(OUT.glob("YW3-*.json"))
assert len(files) == 4, files
for f in files:
    json.loads(f.read_text(encoding="utf-8"))
print("OK: 2 pairs written:", [f.name for f in files])
