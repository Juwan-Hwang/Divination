#!/usr/bin/env python3
"""M1 (axis-2 / actual-outcome) scoring writer for R90 holdout32 master packet.
Reads packet-master.json only for anon_id order verification; scores are fixed below.
Writes judgeM1.jsonl and self-verifies: JSONL parse, count, order, sum check.
"""
import json
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round90/acceptance")
PACKET = BASE / "judging" / "packet-master.json"
OUT = BASE / "judging" / "judgeM1.jsonl"

NEUTRAL = "无时点可核（中性记 1）"

# (anon_id, direction, claims, timing, reason)
ROWS = [
    ("H32M-0004f8eb", 2, 2, 1.5,
     "1994年结婚与丈夫移情离异均证实；2008年再婚之断结局未及核验，应期只部分对齐。"),
    ("H32M-0026c324", 2, 1, 1,
     "早死方向证实；病名只部分对位（遗泄近肾、实际成痨而卒），四年之期无基准可核。" + NEUTRAL),
    ("H32M-03573c62", 2, 1.5, 2,
     "财运不佳、无晋升、戌月丈夫罹致命之灾均证实；灾祸形态断为道路车祸，实际为坠窗，形态错位。"),
    ("H32M-03c626de", 1, 1.5, 1,
     "先少后多、年终去半与苦去甘来又乐里生悲大体合；但断语称究竟有成，结局实为受累损半，只部分对位。无具体应期可核。" + NEUTRAL),
    ("H32M-14c6b211", 2, 2, 2, "无"),
    ("H32M-1512b98d", 2, 2, 2, "无"),
    ("H32M-4c15c0f0", 2, 1.5, 2,
     "第六年赴任精确证实；终此任只由第八年丧归间接对位，断语本身含糊。"),
    ("H32M-53cf8275", 2, 1, 1,
     "路费得他人馈赠、先阻后遂证实；必有远行一断只半途而返，未成。无具体应期可核。" + NEUTRAL),
    ("H32M-55fd1702", 2, 2, 2, "无"),
    ("H32M-62bd9044", 1, 1, 1,
     "来聘意诚、后有微嫌、未终局部分对位；所入不逮所出未见结局证实，且结局称无隙末与华而不实只半合。无具体应期可核。" + NEUTRAL),
    ("H32M-6751e6d3", 2, 1.5, 1.5,
     "心病而卒、妻病、本年被医人误治均证实；无子与考试不利未见结局记载，只部分证实。"),
    ("H32M-6cb92a4f", 2, 1.5, 1,
     "省试不中、心病而死证实；更五次不遂与结局纳贿得五甲不尽合。无具体应期可核。" + NEUTRAL),
    ("H32M-6cdd84e3", 1, 1.5, 1,
     "未婚同居、男方私通他人证实；受虐、分居与必分手未见结局证实，方向只部分落定。无具体应期可核。" + NEUTRAL),
    ("H32M-6eab5936", 2, 2, 2, "无"),
    ("H32M-779a19a8", 1.5, 1, 1,
     "四丧与授官职部分证实；无正宅赘婿、终于水边均未见结局记载。具体应期无可核。" + NEUTRAL),
    ("H32M-7d35a9a4", 2, 2, 2, "无"),
    ("H32M-c326af53", 1.5, 1, 1,
     "兵变扰船户、破耗方向对位；但方位断东北，实际为襄樊土匪，坐标错位，口舌小利未证实。无具体应期可核。" + NEUTRAL),
    ("H32M-c99aec45", 1, 2, 1,
     "食道癌这一具体断语精确证实；但病必凶的最终结局记录明言不得而知，方向只部分落定。年内应期无时点可核。" + NEUTRAL),
    ("H32M-d0fa8bbb", 2, 2, 1,
     "旧人回头、现任分手、与谁也未成婚均证实。无具体应期可核。" + NEUTRAL),
    ("H32M-d7dd90d7", 2, 1.5, 2,
     "未月被警察拘留一周证实，应期精确；但祸因断为违法/交通罚款类，实际为旅途斗殴，形态部分错位。"),
    ("H32M-e52ba3af", 2, 1.5, 1,
     "幼失父母、丧妻复娶得子证实；手足他乡等余断未见结局记载。无具体应期可核。" + NEUTRAL),
    ("H32M-e9234f46", 2, 2, 1,
     "结局明言所断皆验且女方回返和好。无具体应期可核。" + NEUTRAL),
    ("H32M-f2fc8187", 2, 2, 1.5,
     "遗精、当年发解、癸丑及第均证实；终三十五岁结局无年龄可核，应期只部分对齐。"),
    ("H32M-f3b7b15b", 2, 2, 1,
     "报社副科长、兄姐死亡、夫妻不和、孩子顽皮均证实。无具体应期可核。" + NEUTRAL),
    ("H32M-fc036e1e", 2, 1.5, 1,
     "以讼笔为业、浪用无成、为人控未结证实；不合伴一断未见结局记载。无具体应期可核。" + NEUTRAL),
    ("H32M-fc446c79", 2, 2, 2, "无"),
    ("H32M-fe9fac43", 2, 2, 2, "无"),
    ("H32M-fec2e492", 2, 1.5, 1,
     "先小产后复孕证实；男孩之象已去与瓦兆等性别断语未见结局核验。无具体应期可核。" + NEUTRAL),
]


def main():
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    packet_ids = [r["anon_id"] for r in packet]
    row_ids = [r[0] for r in ROWS]
    assert row_ids == packet_ids, "anon_id order mismatch vs packet"

    lines = []
    for anon_id, d, c, t, reason in ROWS:
        total = d + c + t
        obj = {
            "anon_id": anon_id,
            "direction": d,
            "claims": c,
            "timing": t,
            "total": total,
            "pass": total >= 4,
            "reason": reason,
        }
        lines.append(json.dumps(obj, ensure_ascii=False))

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Self-verification: re-read, parse each line, check count/order/arithmetic.
    back = OUT.read_text(encoding="utf-8").strip().split("\n")
    assert len(back) == 28, f"line count {len(back)} != 28"
    for i, line in enumerate(back):
        o = json.loads(line)
        assert o["anon_id"] == packet_ids[i], f"order mismatch line {i}"
        assert abs(o["direction"] + o["claims"] + o["timing"] - o["total"]) < 1e-9, \
            f"sum mismatch line {i}"
        assert o["pass"] == (o["total"] >= 4), f"pass mismatch line {i}"
        for k in ("direction", "claims", "timing"):
            assert 0 <= o[k] <= 2, f"range mismatch line {i}"
    nulls = [json.loads(l)["anon_id"] for l in back if json.loads(l)["total"] is None]
    flags = [json.loads(l)["anon_id"] for l in back if "flag" in json.loads(l)]
    print(f"OK rows=28 nulls={nulls} flags={flags} sums_verified=True order_verified=True")


if __name__ == "__main__":
    main()
