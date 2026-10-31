#!/usr/bin/env python3
"""R90 holdout32 judge O2 (axis-2, actual-outcome) writer + self-check.
Reads only packet-ours.json (for order verification). Writes judgeO2.jsonl.
"""
import json
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round90/acceptance")
PACKET = BASE / "judging" / "packet-ours.json"
OUT = BASE / "judging" / "judgeO2.jsonl"

# anon_id, direction, claims, timing, reason, flag(or None)
ROWS = [
    ("H32O-1bf143d2", 0, 0, 0,
     "方向反向：断入仕中平，实际患遗泄成痨早卒、前程未展；断语与午年应期均被结局证伪。", None),
    ("H32O-2f0229c1", 0, 0, 0,
     "方向反向：断下半年得财，实际财运不佳无晋升且戌月丧夫；午月财信未现，应期不合。", None),
    ("H32O-33b93bd5", 2, 2, 1,
     "婚姻、得女与断语相合且记录称余断皆合；但结婚在1988年，卯年主坐标偏一程，应期部分对齐。",
     "疑似虚称：结局以『其他断语也皆符合』概括，未逐项给出对应事实。"),
    ("H32O-391c6db0", 1, 1, 1,
     "先难与得子部分相合，但财不聚、田土纠缠、晚年小成均未见实据；结局无可核年份，无时点可核（中性记 1）。", None),
    ("H32O-43703c8a", 2, 1, 1,
     "癌症凶断同向同级，部位断胸部心肺与食道癌错位；结局未记危期时点，无时点可核（中性记 1）。", None),
    ("H32O-4c5706c7", 2, 1, 1,
     "馆未终局与有始无终同向，意诚微嫌部分合；实际秋末远行，未月主坐标偏，应期部分对齐。", None),
    ("H32O-5f9d5b17", 1, 1, 0,
     "终能到任但迟至第六年，与一月内未日成行完全不合；到后调动之断亦未见，丧归收束。", None),
    ("H32O-5fe6c940", 2, 1, 1,
     "关系终散同向，但三角构成相反（前女友回归而非女方随另一男子）；结局无月份，无时点可核（中性记 1）。", None),
    ("H32O-645e500d", 0, 0, 1,
     "断子女成器、自立得力，实际懒惰独身、无子女，方向与断语大体被证伪；申年无对应时点，无时点可核（中性记 1）。", None),
    ("H32O-66616b38", 2, 2, 1,
     "破耗与低谷同向，记录称诸断全对；但辰月无对应记载，无时点可核（中性记 1）。",
     "疑似虚称：结局称『以上判断全部正确』，但所述辞职在1989年、财运低谷在1997年，与本年断语的时间对应未逐项给出。"),
    ("H32O-6cdb1eb6", 1, 1, 1,
     "中第授司户为有限进益而非升任迁转，铨试不中且授后病死；庚戌授官在数年窗口内而申年主坐标不合，应期部分对齐。", None),
    ("H32O-6cdcd67b", 2, 2, 1,
     "和好回归与断语全合；但子日应期结局未记日期，无时点可核（中性记 1）。",
     "疑似虚称：结局称『所断皆验』，仅记和好一事，子日应期无日期可核。"),
    ("H32O-7358a085", 2, 2, 1,
     "六月小产证实孕不成实的核心断语；血光口舌未见，丑日无日级记载可核，无时点可核（中性记 1）。", None),
    ("H32O-8c7a7c7d", 1, 1, 1,
     "土匪勒耗仅泛合行商受阻破耗，货脱人阻未落到本人；卯日无可核日期，无时点可核（中性记 1）。", None),
    ("H32O-8deac93b", 2, 2, 1,
     "馆事先少后多、年终去半受累，与先苦后甘后段生变轨迹相合；寅月聘定无月份可核，无时点可核（中性记 1）。", None),
    ("H32O-90cd7fb3", 0.5, 0.5, 1,
     "仅部门领导一节泛合，入狱与饭店不挣钱与中上平稳、经营得利相悖；午年无对应时点，无时点可核（中性记 1）。", None),
    ("H32O-a7278c48", 0.5, 0.5, 1,
     "夫妻不和略合婚姻不佳，但孩子不听话与晚年子靠相悖、财散无据；申年无对应时点，无时点可核（中性记 1）。", None),
    ("H32O-ab167668", 0, 0, 0,
     "方向反向：断文教升任，实际患心病九年而卒、文教进身未见；数年窗口内升任未现，应期不合。", None),
    ("H32O-ab8606bf", 1, 1, 1,
     "被控未结、无所成泛合进取受制，但土匪挈家远飏并非退守得安；亥月无对应记载，无时点可核（中性记 1）。", None),
    ("H32O-b0ece1b4", 0, 0, 1,
     "方向反向：断缘成可续，实际未婚同居且男方移情私通；亥日无日期可核，无时点可核（中性记 1）。", None),
    ("H32O-b3238cc5", 0, 0, 1,
     "方向反向：断试不成落空，实际当年发解、后及第授官；结果在本年试期窗口内揭晓而申日主坐标无据，应期部分对齐。", None),
    ("H32O-c5665410", 1, 1, 2,
     "官非拘留一节在未月应验且量级相合，但形态是旅途打架而非行车罚责，财面进账未见记载。", None),
    ("H32O-c9ffcd01", 1.5, 1, 1,
     "授江阴军知录合佐贰进益一节，靠人成事未见据；甲子授官在数年窗口内而寅年主坐标不合，应期部分对齐。", None),
    ("H32O-daafa169", 2, 2, 1,
     "省试不中、文学不遂与断语全合；巳日放榜无日期可核，无时点可核（中性记 1）。", None),
    ("H32O-e556d890", 2, 1, 0,
     "骨癌致死证实重病凶断与肿瘤一节，但病位下腹下焦未获证实；实际死于丙辰日，与巳日应期不合。", None),
    ("H32O-e7bba204", 1, 1, 1,
     "1994年结婚合缘成一节，但其后离异、丈夫再婚与能续相悖；婚约未日无日期可核，无时点可核（中性记 1）。", None),
    ("H32O-f50f2a57", 0, 0, 1,
     "方向反向：断弃官就商，实际为处级干部记者、未从商；戌年财顶无对应时点，无时点可核（中性记 1）。", None),
    ("H32O-fcb3084c", 2, 2, 1,
     "所约者馈赠相助、先阻后遂与断语相合，但半途而返未在断中；丑日无日期可核，无时点可核（中性记 1）。",
     "疑似虚称：结局称『其说亦准』为概括语，且半途而返未见于断语，丑日应期无日期可核。"),
]

def main():
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    packet_ids = [r["anon_id"] for r in packet]
    assert [r[0] for r in ROWS] == packet_ids, "row order != packet order"

    lines = []
    for anon_id, d, c, t, reason, flag in ROWS:
        total = d + c + t
        if float(total).is_integer():
            total = int(total)
        rec = {
            "anon_id": anon_id,
            "direction": d,
            "claims": c,
            "timing": t,
            "total": total,
            "pass": total >= 4,
            "reason": reason,
        }
        if flag is not None:
            rec["flag"] = flag
        lines.append(json.dumps(rec, ensure_ascii=False))

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # self-check: re-read, parse each line, verify order and sums
    raw = OUT.read_text(encoding="utf-8").strip().split("\n")
    assert len(raw) == 28, f"line count {len(raw)}"
    npass = 0
    for i, line in enumerate(raw):
        rec = json.loads(line)
        assert rec["anon_id"] == packet_ids[i], f"order mismatch line {i+1}"
        s = rec["direction"] + rec["claims"] + rec["timing"]
        assert abs(s - rec["total"]) < 1e-9, f"sum mismatch {rec['anon_id']}"
        assert rec["pass"] == (rec["total"] >= 4), f"pass mismatch {rec['anon_id']}"
        for k in ("direction", "claims", "timing"):
            assert 0 <= rec[k] <= 2, f"range {rec['anon_id']} {k}"
        npass += 1 if rec["pass"] else 0
    flags = [json.loads(l)["anon_id"] for l in raw if "flag" in json.loads(l)]
    print(f"OK lines=28 pass={npass} fail={28-npass} flags={flags}")

if __name__ == "__main__":
    main()
