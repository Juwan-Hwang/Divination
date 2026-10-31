import json

rows = [
    {
        "anon_id": "P3-57e5aeb2",
        "direction": 0,
        "claims": 0,
        "timing": 0,
        "total": 0,
        "pass": False,
        "reason": "预测明日无雨主晴、父母不上卦雨象不现，结局次日大雨，方向全反；无雨、主晴、雨神不现等具体断语无一被印证；应期主坐标为明日全日无雨，同日大雨恰击破该时点断语，timing 0（预测有应期、结局有时点，特殊口径不适用）。",
    },
    {
        "anon_id": "P3-58793f59",
        "direction": 1.5,
        "claims": 0.5,
        "timing": 0,
        "total": 2.0,
        "pass": False,
        "reason": "终局确发乡科，与功名有望方向部分吻合，但预测单一终局为今科得中，结局改丙戌才发，故 direction 不满；具体断语仅最终发乡科一项得印证，今科得中、酉月而应被结局否定，官旺、文书发动、化空待填实等未被结局记载，claims 低；应期壬午年酉月与结局丙戌年不合，timing 0。",
    },
]

for r in rows:
    assert r["total"] == r["direction"] + r["claims"] + r["timing"], r
    assert r["pass"] == (r["total"] >= 4), r

out = "/home/hatch/workspace/divination/benchmark/phase3/runs/round87/judging/arbitration-scores.jsonl"
with open(out, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

print("written", len(rows), "rows to", out)
