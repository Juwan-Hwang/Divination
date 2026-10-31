# R84 judgeY-block3 scoring writer (seat Y3)
# Evidence basis: ONLY judging/judgeY-block3.jsonl (per seat discipline;
# host-mapping / predictions originals NOT opened).
# Finding: every row's prediction fields (direction/assertions/timing/summary)
# are all null in the judging file, so no verifiable prediction text exists
# within the permitted evidence. Scoring per JUDGE-PROMPT-verbatim:
# direction=0 (no direction to match), claims=0 (no assertion verifiable),
# timing=0 with note (prediction itself states no timing).
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round84"
SRC = os.path.join(BASE, "judging", "judgeY-block3.jsonl")
DST = os.path.join(BASE, "judging", "judgeY-block3-scores.jsonl")

REASON = ("本块judging文件内prediction四字段均为null，无可核预测断语："
          "方向无从印证、具体断语无可核；预测断语本身无应期。"
          "旗标：prediction全null，未按评审提示回读host-mapping/predictions原件（本席纪律禁止）。")

assert not os.path.exists(DST), "output already exists; refusing to overwrite"

rows = [json.loads(line) for line in open(SRC, encoding="utf-8") if line.strip()]
assert len(rows) == 122, f"expected 122 input rows, got {len(rows)}"

scores = []
for r in rows:
    p = r.get("prediction") or {}
    assert all(p.get(k) is None for k in ("direction", "assertions", "timing", "summary")), r["anon_id"]
    assert r.get("outcome_record"), r["anon_id"]
    scores.append({
        "anon_id": r["anon_id"],
        "direction": 0,
        "claims": 0,
        "timing": 0,
        "total": 0,
        "pass": False,
        "reason": REASON,
    })

# segmented append: 8 segments, assert cumulative line count after each
SEG = 8
per = (len(scores) + SEG - 1) // SEG
written = 0
with open(DST, "a", encoding="utf-8") as f:
    for s in range(SEG):
        chunk = scores[s * per:(s + 1) * per]
        for sc in chunk:
            f.write(json.dumps(sc, ensure_ascii=False) + "\n")
        f.flush()
        written += len(chunk)
        on_disk = sum(1 for _ in open(DST, encoding="utf-8"))
        assert on_disk == written, f"segment {s}: disk {on_disk} != written {written}"

# final self-verification
out = [json.loads(line) for line in open(DST, encoding="utf-8") if line.strip()]
assert len(out) == len(rows) == 122
assert [o["anon_id"] for o in out] == [r["anon_id"] for r in rows], "anon_id order mismatch"
for o in out:
    assert o["total"] == o["direction"] + o["claims"] + o["timing"]
    assert o["pass"] == (o["total"] >= 4)
print("OK wrote", len(out), "scores to", DST)
