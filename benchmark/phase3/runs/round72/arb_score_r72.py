import json

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round72/judging/arbitration-scores.jsonl"
ALLOWED = {0, 0.5, 1, 1.5, 2}

rows = [
    {
        "anon_id": "P3-884e246d",
        "direction": 0,
        "claims": 0,
        "timing": 1,
        "reason": "預測斷擇此日入宅有礙父母、於父母不利宜改日；結局直載平安一十七載，與不利方向相反，具體斷語未獲印證。預測有日檔應期而結局無可核時點，timing按口徑記1。",
    },
    {
        "anon_id": "P3-88572e05",
        "direction": 2,
        "claims": 2,
        "timing": 2,
        "reason": "預測Waller勝、Hopton敗；結局載議會軍一方於Cheriton獲勝並俘獲多人多械，方向與逐條斷語均印證。應期日檔29日當日與1644年3月29日會戰日吻合。",
    },
]

assert len(rows) == 2
for r in rows:
    for k in ("direction", "claims", "timing"):
        assert r[k] in ALLOWED, (r["anon_id"], k, r[k])
    r["total"] = r["direction"] + r["claims"] + r["timing"]
    r["pass"] = r["total"] >= 4
    out = {"anon_id": r["anon_id"], "direction": r["direction"], "claims": r["claims"],
           "timing": r["timing"], "total": r["total"], "pass": r["pass"], "reason": r["reason"]}
    assert out["total"] == out["direction"] + out["claims"] + out["timing"]
    assert out["pass"] == (out["total"] >= 4)
    r.clear()
    r.update(out)

with open(OUT, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")

# 回讀斷言
with open(OUT, encoding="utf-8") as f:
    lines = [json.loads(x) for x in f if x.strip()]
assert len(lines) == 2
assert [x["anon_id"] for x in lines] == ["P3-884e246d", "P3-88572e05"]
for x in lines:
    assert x["total"] == x["direction"] + x["claims"] + x["timing"]
    assert x["pass"] == (x["total"] >= 4)
print("OK", len(lines), [(x["anon_id"], x["total"]) for x in lines])
