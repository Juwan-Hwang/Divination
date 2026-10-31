#!/usr/bin/env python3
"""R80 data seat: verify R79 carryover落实 + build case-annotations-r80.json.

Data compilation only: no adjudication, no scoring, no case/manifest edits.
Flag texts are copied verbatim from FREEZE-r80 (containment asserted before
any annotation is written)."""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
ANN79 = P3 / "data/case-annotations-r79.json"
ADD79 = P3 / "data/manifest-carryover-r79-addendum.md"
M80 = P3 / "runs/round80/judging/outcome-manifest.json"
FREEZE = P3 / "runs/round80/FREEZE-r80.md"
OUT = P3 / "data/case-annotations-r80.json"

freeze = FREEZE.read_text(encoding="utf-8")
# --- flag discipline: verbatim-quote containment asserted before writing ---
Q_AS307_A = "卡面顶层明载 tradition＝astrology，basis 首行却作「卡面未标注 tradition 字段——此卡无 tradition 行」，属对卡面字段之误读误述"
Q_AS307_B = "本例实际所用方法为西洋占星（systems_used 行明载），与卡面 tradition 值实质一致、断语方向不受影响"
Q_AS307_C = "照 R76 BZ 六件判例之 operative 口径（方法实质一致、断语不受影响）裁定部分成立，不作废不重测"
Q_LR_A = "两例卡面确无 tradition/system 字段，basis 首行已以散文逐字写明「本例卡面没有 tradition／system 两字段……自决作断」，属未标注声明之完整表述；检查器未标注关键词集未含「没有」变体，属覆盖缺口（承 R78/R79 同型判例）。不作废不重测"
for q in (Q_AS307_A, Q_AS307_B, Q_AS307_C, Q_LR_A):
    assert q in freeze, q[:40]

m80 = json.loads(M80.read_text(encoding="utf-8"))
ann79 = json.loads(ANN79.read_text(encoding="utf-8"))
add79 = ADD79.read_text(encoding="utf-8")
assert ann79["counts"]["cases_total"] == 94
assert len(ann79["annotations"]) == 94

# --- check 1: _r79_carryover_notes_addendum 23 items落实对勘 ---
layer = m80["_r79_carryover_notes_addendum"]
assert len(layer) == 23, len(layer)
results = {}
for a in ann79["annotations"]:
    if a["disposition"] == "部分成立" and a.get("registered_round") == 79:
        cid = a["case_id"]
        ok = layer.get(cid) == a["manifest_carry_suggestion"]
        # suggestion text must also be the text compiled in the r79 addendum
        assert a["manifest_carry_suggestion"] in add79, cid
        results[cid] = ok
assert len(results) == 22
BZ037 = ("同例新旨：自 R80 起承接本 R79 标注（与 R76 主持裁定 tradition 旨并行）"
         "：按「结局自注『未执政』与史实不合、已自标为已知偏差点」登记；"
         "结局原文照录不改。")
assert BZ037 in add79
results["BZ-037"] = layer.get("BZ-037") == BZ037
assert len(results) == 23 and all(results.values()), results
print("carryover check: 23/23 落实")

# --- check 2: baseline six (BZ-036/BZ-042/BZ-105/LY-204 + LR2-016 x2 layers) ---
cases = m80["cases"]
assert "盲测比对须注" in cases["BZ-036"]
assert "（盲测比对时以格局大富一项为主）" in cases["BZ-042"]
assert "使用时须分开统计" in cases["BZ-105"]
assert "勿以此斷" in cases["LY-204"]
EN = "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
assert m80["_r56_lr2016_split"]["editor_note"] == EN
assert json.dumps(m80, ensure_ascii=False).count(EN) == 1
for pkt in ("packet1.json", "packetA.json"):
    t = (P3 / f"runs/round80/judging/{pkt}").read_text(encoding="utf-8")
    assert EN in t, pkt
print("baseline six: 6/6 在盘形态未变")

# --- check 3: R80 platform flag facts on disk ---
hm = json.loads((P3 / "runs/round80/judging/host-mapping.json").read_text(encoding="utf-8"))
inv = {v: k for k, v in hm.items()}
assert inv["AS-307"] == "P3-c6628422" and inv["LR3-004"] == "P3-c40edcb6" and inv["LR3-104"] == "P3-1f7319bb"
card307 = json.loads((P3 / "inputs/AS-307.json").read_text(encoding="utf-8"))
assert card307["tradition"] == "astrology"
p307 = json.loads((P3 / "runs/round80/predictions/AS-307.json").read_text(encoding="utf-8"))
assert p307["basis"].split("\n")[0] == "卡面未标注 tradition 字段——此卡无 tradition 行，按群体访谈式选举占星的题面自决。"
assert "systems_used: 西洋占星（多位占星师公开表态汇总）单法。" in p307["basis"]
for cid, first in (
    ("LR3-004", "本例卡面没有 tradition／system 两字段，题面问的是功名前程，按六壬仕宦门自决作断。"),
    ("LR3-104", "本例卡面没有 tradition／system 字段，问上疏吉凶属章奏门，课式从革绝嗣为六壬格，自决用大六壬章奏门。"),
):
    card = json.loads((P3 / f"inputs-dev12/{cid}.json").read_text(encoding="utf-8"))
    assert "tradition" not in card and "system" not in card, cid
    pred = json.loads((P3 / f"runs/round80/predictions/{cid}.json").read_text(encoding="utf-8"))
    assert pred["basis"].split("\n")[0] == first, cid
assert cases["AS-307"] == "特朗普以明确优势胜出"
assert (P3 / "runs/round80/predictions/LY-537.json").exists()
print("platform flag facts: verified on disk")

NEW = [
    {
        "anon_id": "P3-c6628422",
        "case_id": "AS-307",
        "disposition": "部分成立",
        "finding": (
            "平台旗标定案（FREEZE-r80 §一.1，本席只承接登记、不重裁）：裁定逐字引录——「"
            + Q_AS307_A + "」；「" + Q_AS307_B + "」；「" + Q_AS307_C
            + "，入本轮旗标定案流水待数据席 manifest 注记落实」。本席盘上复核：原卡 inputs/AS-307.json 顶层 tradition＝astrology 在盘；"
            "R80 prediction basis 首行逐字作「卡面未标注 tradition 字段——此卡无 tradition 行，按群体访谈式选举占星的题面自决。」、"
            "basis 内 systems_used 行作「西洋占星（多位占星师公开表态汇总）单法。」——与裁定所载合。"
        ),
        "flag": "主持检查器（FREEZE-r80 §一）：tradition 首行核查旗标——卡面 tradition＝astrology 与 basis 首行「卡面未标注 tradition 字段——此卡无 tradition 行」误读误述",
        "manifest_carry_suggestion": "平台旗标定案：自 R81 起承接本 R80 标注：按「卡面 tradition＝astrology、basis 首行误读作未标注，实际所用方法为西洋占星与卡面实质一致、断语方向不受影响，部分成立，不作废不重测」登记；结局原文照录不改。",
        "relation": "新立（R80 平台旗标定案）",
        "registered_round": 80,
        "sources_checked": [
            "divination/benchmark/phase3/inputs/AS-307.json",
            "divination/benchmark/phase3/runs/round80/FREEZE-r80.md §一.1",
            "divination/benchmark/phase3/runs/round80/judging/host-mapping.json（anon 解析：P3-c6628422＝AS-307）",
            "divination/benchmark/phase3/runs/round80/predictions/AS-307.json",
            "divination/benchmark/phase3/runs/round80/judging/outcome-manifest.json cases[AS-307]",
        ],
        "source_seats": ["主持检查器（FREEZE-r80）"],
    },
    {
        "anon_id": "P3-c40edcb6",
        "case_id": "LR3-004",
        "disposition": "不成立",
        "finding": (
            "平台旗标定案（FREEZE-r80 §一.2，本席只承接登记、不重裁）：裁定逐字引录——「"
            + Q_LR_A + "」，定案不成立（检查器误报）。本席盘上复核：原卡 inputs-dev12/LR3-004.json 无 tradition／system 字段；"
            "R80 prediction basis 首行逐字作「本例卡面没有 tradition／system 两字段，题面问的是功名前程，按六壬仕宦门自决作断。」——未标注声明完整在盘，与裁定所载合。"
        ),
        "flag": "主持检查器（FREEZE-r80 §一）：tradition 首行核查旗标——basis 首行未标注声明（「没有」变体）未被检查器关键词集命中",
        "manifest_carry_suggestion": "只登记不入层：自 R81 起承接本 R80 标注（不成立＝检查器误报，不入 _r80_carryover_notes_addendum 承接层）；结局原文照录不改。",
        "relation": "新立（R80 平台旗标定案）",
        "registered_round": 80,
        "sources_checked": [
            "divination/benchmark/phase3/inputs-dev12/LR3-004.json",
            "divination/benchmark/phase3/runs/round80/FREEZE-r80.md §一.2",
            "divination/benchmark/phase3/runs/round80/judging/host-mapping.json（anon 解析：P3-c40edcb6＝LR3-004）",
            "divination/benchmark/phase3/runs/round80/predictions/LR3-004.json",
            "divination/benchmark/phase3/runs/round80/judging/outcome-manifest.json cases[LR3-004]",
        ],
        "source_seats": ["主持检查器（FREEZE-r80）"],
    },
    {
        "anon_id": "P3-1f7319bb",
        "case_id": "LR3-104",
        "disposition": "不成立",
        "finding": (
            "平台旗标定案（FREEZE-r80 §一.2，本席只承接登记、不重裁）：裁定逐字引录——「"
            + Q_LR_A + "」，定案不成立（检查器误报）。本席盘上复核：原卡 inputs-dev12/LR3-104.json 无 tradition／system 字段；"
            "R80 prediction basis 首行逐字作「本例卡面没有 tradition／system 字段，问上疏吉凶属章奏门，课式从革绝嗣为六壬格，自决用大六壬章奏门。」——未标注声明完整在盘，与裁定所载合。"
        ),
        "flag": "主持检查器（FREEZE-r80 §一）：tradition 首行核查旗标——basis 首行未标注声明（「没有」变体）未被检查器关键词集命中",
        "manifest_carry_suggestion": "只登记不入层：自 R81 起承接本 R80 标注（不成立＝检查器误报，不入 _r80_carryover_notes_addendum 承接层）；结局原文照录不改。",
        "relation": "新立（R80 平台旗标定案）",
        "registered_round": 80,
        "sources_checked": [
            "divination/benchmark/phase3/inputs-dev12/LR3-104.json",
            "divination/benchmark/phase3/runs/round80/FREEZE-r80.md §一.2",
            "divination/benchmark/phase3/runs/round80/judging/host-mapping.json（anon 解析：P3-1f7319bb＝LR3-104）",
            "divination/benchmark/phase3/runs/round80/predictions/LR3-104.json",
            "divination/benchmark/phase3/runs/round80/judging/outcome-manifest.json cases[LR3-104]",
        ],
        "source_seats": ["主持检查器（FREEZE-r80）"],
    },
]

SPECIAL = [
    {
        "item": "特别核查㉔（R80）：R79 附则承接建议 23 件于 R80 manifest 落实对勘",
        "conclusion": "R80 manifest 新层 _r79_carryover_notes_addendum 共 23 件，与 R79 附则（data/manifest-carryover-r79-addendum.md §三）所载建议文本逐件全等：新登记 22 件逐件与 case-annotations-r79.json 对应条 manifest_carry_suggestion 逐字全等（且该文本逐字在 R79 附则内），BZ-037 同例新旨 1 件与 R79 附则 §3.2 建议原文逐字全等。23 件全部落实，未落实 0 件。",
        "evidence": "落盘脚本逐件断言：layer 键集＝22 件（registered_round＝79 且部分成立）∪{BZ-037}、逐件文本全等；层件数 23。",
        "scope_note": "对勘只读 R80 manifest 与 R79 附则／标注，不改 manifest 任一侧；逐件表见附则 §二。",
    },
    {
        "item": "特别核查㉕（R80）：平台旗标定案 3 件登记与验收（holdout24）留位",
        "conclusion": "本轮平台侧旗标定案仅 FREEZE-r80 §一 tradition 首行核查 3 件：AS-307 部分成立（入承接建议、供 R81 以 _r80_carryover_notes_addendum 落实）、LR3-004／LR3-104 不成立＝检查器误报（只登记不入层）。验收（holdout24）旗标定案尚未产生，本件只含平台侧；验收侧由后续附记补入时另行登记，此处明记留位、不预填。",
        "evidence": "FREEZE-r80 §一逐字引录断言内置于落盘脚本（四段裁定原文断言包含后才落笔）；anon 经 runs/round80/judging/host-mapping.json 对位：P3-c6628422＝AS-307、P3-c40edcb6＝LR3-004、P3-1f7319bb＝LR3-104。",
        "scope_note": "本席只承接登记主持已作之裁定，不作断、不评审、不重裁。",
    },
    {
        "item": "特别核查㉖（R80）：指令性字样特别核查基线六处复核（承 R79 附则 §四基线）",
        "conclusion": "基线六处经 R80 manifest 与 R80 评审包盘上复核在册、形态未变：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）逐字在场；LR2-016 manifest editor_note 一处在 _r56_lr2016_split 分列层、全文恰出现 1 次；LR2-016 评审包 editor_note 层一处在 R80 judging/packet1.json 与 packetA.json 中逐字在场、同句全等。无新增同型件登记。",
        "evidence": "脚本逐字断言：BZ-036『盲测比对须注』、BZ-042『（盲测比对时以格局大富一项为主）』、BZ-105『使用时须分开统计』、LY-204『勿以此斷』均在 cases 本体；editor_note 全句与分列层全等且 manifest 全文计数 1、评审包两件各在场。",
        "scope_note": "各席与本席均按数据处理、不作指令；只登记、不改文本。",
    },
    {
        "item": "特别核查㉗（R80）：待核四件维持登记与 LY-537 本轮触及关联",
        "conclusion": "BZ-029（俞大维卒年待核＋旗标错配线索）／BZ-040（许世英享年待核）／LY-537（「申予日」衍字疑）／YM-070（「甲寅旬」挂起）四件维持原登记，本轮不核查、不关闭。LY-537 本轮被平台盲测正常作答（runs/round80/predictions/LY-537.json 在盘，R80 anon P3-b92fb78b），只登记关联、不改其未核待核状态；余三件本轮无新触及登记。",
        "evidence": "R80 manifest cases[LY-537] 仍作『果于申予日归』（与 R79 件逐字全等，cases 载荷 SHA 同前）；LY-537／YM-070 未核条目随 94 件全量承接在册。",
        "scope_note": "待核件无盘外独立史源不裁；CZ-QX 维持 16 只登记、无增减。",
    },
]

out = {
    "_provenance": (
        "R80 数据席（附则承接对勘＋annotations 全量承接与本轮平台旗标定案，独立席位，不兼任本轮盲测/评审/诊断/组集/修订/集成，不改任何分数）："
        "以 data/case-annotations-r79.json 为底承接全量 94 件（成立 12／部分成立 76／不成立 4／未核 2），前 94 件逐件原样、无删改（落盘脚本以数组全等断言验过）；"
        "承接对勘：R79 附则 §三汇编 23 件已于 R80 manifest 以 _r79_carryover_notes_addendum 层逐件逐字落实（22 件与 r79 标注建议全等、BZ-037 与附则 §3.2 原文全等），23/23 落实、未落实 0 件；"
        "本轮新定案仅平台侧 3 件（FREEZE-r80 §一 tradition 首行核查裁定，引文逐字断言内置于落盘脚本）：AS-307 部分成立（新登记、承接建议供 R81 以 _r80_carryover_notes_addendum 落实）、LR3-004／LR3-104 不成立＝检查器误报（只登记不入层）；"
        "承接后总件数 97（成立 12／部分成立 77／不成立 6／未核 2）。验收（holdout24）旗标定案尚未产生，本件只含平台侧，验收侧留位、由后续附记补入时另行登记。"
        "指令性字样基线六处经 R80 manifest 与评审包复核在册、形态未变（见特别核查㉖）。待核四件 BZ-029／BZ-040／LY-537／YM-070 维持原登记、不核查不关闭；LY-537 本轮被平台盲测正常作答只登记关联、不改待核状态。CZ-QX 维持 16 只登记。"
        "本标注只入本数据侧元数据文件，不动原卡、manifest 与任何分数、结局原文；结局/注记文本内指令性字样一律按数据处理。"
    ),
    "round": 80,
    "annotations": ann79["annotations"] + NEW,
    "special_checks": ann79["special_checks"] + SPECIAL,
    "counts": {
        "base_file": "data/case-annotations-r79.json",
        "base_cases_total": 94,
        "base_verdicts": {"成立": 12, "部分成立": 76, "不成立": 4, "未核": 2},
        "carryover_check_r79_addendum": {"layer": "_r79_carryover_notes_addendum", "items": 23, "implemented": 23, "not_implemented": 0},
        "platform_checker_flags_r80": 3,
        "platform_flag_verdicts_r80": {"部分成立": 1, "不成立": 2},
        "new_registrations_r80": 3,
        "new_partial_cases_r80": ["AS-307"],
        "new_not_upheld_cases_r80": ["LR3-004", "LR3-104"],
        "acceptance_holdout24_flags": "尚未产生（留位，验收侧由后续附记补入时另行登记）",
        "cases_total": 97,
        "verdicts": {"成立": 12, "部分成立": 77, "不成立": 6, "未核": 2},
    },
}

# --- post-write assertions ---
assert out["annotations"][:94] == ann79["annotations"]
ids79 = {(a["case_id"], a["anon_id"]) for a in ann79["annotations"]}
ids80 = {(a["case_id"], a["anon_id"]) for a in out["annotations"]}
assert len(out["annotations"]) == 97 and ids79 < ids80 and len(ids80) == 97
REQ = {"anon_id", "case_id", "disposition", "finding", "flag", "manifest_carry_suggestion", "relation", "registered_round", "sources_checked", "source_seats"}
for a in NEW:
    assert REQ <= set(a) and a["registered_round"] == 80, a["case_id"]
from collections import Counter
assert Counter(a["disposition"] for a in out["annotations"]) == {"成立": 12, "部分成立": 77, "不成立": 6, "未核": 2}

OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
back = json.loads(OUT.read_text(encoding="utf-8"))
assert len(back["annotations"]) == 97
raw = OUT.read_bytes()
print("written", OUT, "bytes", len(raw), "sha256", hashlib.sha256(raw).hexdigest())
print("total 97; verdicts 12/77/6/2; subset OK; fields OK")
