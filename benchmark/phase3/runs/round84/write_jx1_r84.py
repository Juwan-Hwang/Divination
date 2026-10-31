#!/usr/bin/env python3
"""R84 judgeX-block1 scorer (seat X1).

Basis: JUDGE-PROMPT-verbatim frozen text. In this block every input row has
prediction.direction/assertions/timing/summary all null, so there is no
direction, no assertion and no timing claim to verify against the outcome:
direction=0, claims=0, timing=0 (frozen rule: prediction itself has no
timing claim -> timing 0, noted in reason). total=0, pass=False.
Writes by segmented append with per-segment assertions; no overwrite/delete.
"""
import json
import os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round84"
SRC = os.path.join(BASE, "judging", "judgeX-block1.jsonl")
OUT = os.path.join(BASE, "judging", "judgeX-block1-scores.jsonl")
REASON = (
    "prediction 四字段（direction/assertions/timing/summary）均为 null，"
    "无终局方向、无具体断语、无应期可与结局核对；"
    "预测断语本身无应期，timing 记 0。"
)

def main():
    assert not os.path.exists(OUT), "output already exists; refusing to overwrite/append blindly"
    rows = [json.loads(line) for line in open(SRC, encoding="utf-8") if line.strip()]
    assert len(rows) == 122, f"input rows {len(rows)} != 122"
    ids = []
    for r in rows:
        assert set(r["prediction"].values()) == {None}, f"non-null prediction found: {r['anon_id']}"
        assert r.get("outcome_record"), f"empty outcome: {r['anon_id']}"
        ids.append(r["anon_id"])
    assert len(set(ids)) == 122, "duplicate anon_id in block"

    scores = [
        {
            "anon_id": aid,
            "direction": 0,
            "claims": 0,
            "timing": 0,
            "total": 0,
            "pass": False,
            "reason": REASON,
        }
        for aid in ids
    ]

    chunk = 31
    written = 0
    with open(OUT, "a", encoding="utf-8") as f:
        for i in range(0, len(scores), chunk):
            seg = scores[i : i + chunk]
            for s in seg:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
            f.flush()
            written += len(seg)
            on_disk = sum(1 for _ in open(OUT, encoding="utf-8"))
            assert on_disk == written, f"segment assertion failed: disk {on_disk} != written {written}"
            print(f"segment appended: cumulative {written}")

    # final self-check
    back = [json.loads(line) for line in open(OUT, encoding="utf-8") if line.strip()]
    assert len(back) == 122, f"final count {len(back)} != 122"
    assert [b["anon_id"] for b in back] == ids, "anon_id order/set mismatch vs input"
    for b in back:
        assert b["total"] == b["direction"] + b["claims"] + b["timing"]
        assert b["pass"] == (b["total"] >= 4)
    print(f"OK: wrote {len(back)} scores to {OUT}")

if __name__ == "__main__":
    main()
