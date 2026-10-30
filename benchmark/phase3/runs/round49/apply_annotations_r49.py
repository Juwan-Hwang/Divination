#!/usr/bin/env python3
"""R49 host: extend data/case-annotations-r49.json with FLAGS-review-r49
adjudicated annotations (host ruling in runs/round49/ADDENDUM-1.md s.3).
LY-426 excluded (flag anon identity unconfirmed). Appends style_note to
the three R48-adjudicated entries. Idempotent: skips case_ids already
present (except style_note fill).
"""
import json
from pathlib import Path

P = Path("/home/hatch/workspace/divination/benchmark/phase3/data/case-annotations-r49.json")
doc = json.loads(P.read_text(encoding="utf-8"))
ann = doc["annotations"]
have = {a["case_id"] for a in ann}

STYLE = "结局为事件短录体（时点＋事件），R49 复核定案：非断语复述体（FLAGS-review-r49 §五）。"
for a in ann:
    if a["case_id"] in ("LY-437", "LY-206", "LY-011"):
        a.setdefault("style_note", STYLE)

NEW = [
    ("AS-015", "同图兼断例", "Lilly 同图兼断问者本人死期，结局即该兼断之验（FLAGS-review-r49 §3.3）。"),
    ("LY-212", "趨避例（防不測断面）", "所问索債，大师改断危亡之禍并苦留，结局覆舟即所避之祸实况（§3.4）。"),
    ("LY-510", "同条再问例", "结局对应同条再问「挾志遍遊可能如願否」（§3.6）。"),
    ("LY-430", "两占合断例", "结局渴死对应再占「還妨秋令危災／難以到任」断面（§3.7）。"),
    ("LY-533", "占此應彼／防不測断面", "建卡 setting 原注「占此應彼」，断防不测、结局覆舟而亡（§3.9）。"),
    ("LR2-022", "结局段并载同日复占与扶乩复核", "终句「果三日死」为本断应验（§3.10）。"),
    ("LY-222", "改断面例", "子嗣問改斷失散之子見歸，结局父子相逢（§3.11）。"),
    ("LY-023", "占他应我／自标迁移例", "原书明言「不現母病，而現子女有災」，结局子驚風（§3.12）。"),
    ("LY-259", "续断复合体", "结局并载两轮续断原文，末段应续断「終有遷改」（§4.1）。"),
    ("OC-029", "一课多断多问同载", "原例即一式多占，结局逐项应五断（§4.2）。"),
    ("LY-508", "終身財福章兼断寿夭", "结局对应兼断面「難許長年」（§4.4）。"),
    ("BQ-001", "结局含已事印证段", "后断应验以「果如言」总承（§4.5）。"),
    ("LY-504", "防刑獄断面", "结局行文拿問对应第二断「且防刑獄」（§4.9）。"),
    ("LY-436", "占近應遠例（大师自标迁移）", "原书自注「占月令而現壽元，此占近而應遠也」；断验同句属原书体例（§4.11）。"),
    ("LR3-112", "并断贼事例", "结局对应贼事断面，病断死期未验（源已注）（§4.12）。"),
    ("LY-527", "连占合断例", "结局分应初断指认与再占功名（§4.15）。"),
    ("LY-425", "结局对应功名总断（弱）", "问面名目（得缺）与结局名目（中榜）有别（§4.8）。"),
    ("LY-538", "改断面例（弱）", "參劾問改斷離任，结局应離任（§4.18）。"),
    ("LY-513", "間接驗證例", "结局仅记病终，功名断语无对应结局事件，判读粒度弱；outcome 不改（§4.10，(乙) 部分不对位）。"),
    ("LY-458", "结局僅載平安、未載來否結果", "原书明辨所问为來否非平安，判读不得以平安充不來之驗；outcome 不改（§4.16，(乙) 部分不对位）。"),
    ("LY-205", "结局末附原书论辩语", "末句反问系原书驳《黄金策》父母持身旧解之论辩语，非结局事件本体、非建卡带入（§3.14）。"),
    ("LY-220", "对话体断验交叠", "结局判读以末句后时事件（後一年又登申榜）为准（§4.7）。"),
    ("LY-240", "原文残句登记", "结局「果於辰日」为原文应验残句，照錄不補；对应关系明确（§4.3）。"),
    ("LR3-002", "断验同段短承体", "结局以短承回指断语确指事件，逐项可分离（§4.17）。"),
    ("LR2-016", "结局尾句含建卡自注（未复核声明）", "尾句「原文未逐字复核『甲戌日巳时』的日时细节…」系 expansion7 建卡席自注、非原书文本（NOTES-provenance-r49 并案核定案）；该细项按未完全复核处理，注记按数据处理、不作指令。"),
    ("BZ-105", "回溯断验（retrodiction）例", "结局后半「按：此为回溯断验…」系 masters-dataset 建卡编者按语、非原书文本（NOTES-provenance-r49 定案）；使用时与前瞻断语分开统计。"),
]
added = 0
for cid, label, basis in NEW:
    if cid in have:
        continue
    ann.append({"case_id": cid, "type_label": label, "basis": basis,
                "registered_round": 49})
    added += 1

P.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"annotations now {len(ann)} (added {added}); case_ids unique: {len({a['case_id'] for a in ann}) == len(ann)}")
