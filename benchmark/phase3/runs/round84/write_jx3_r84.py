#!/usr/bin/env python3
"""R84 judgeX-block3 scoring writer (X3 seat).

Input block verified by seat before writing: all 122 rows carry
prediction == {direction: null, assertions: null, timing: null, summary: null}
and no prediction_text / question fields. Per frozen JUDGE-PROMPT scale,
an empty prediction has no direction to match (direction=0), no specific
assertions to verify (claims=0), and itself states no timing
(timing=0 per the prompt's 'prediction itself has no timing -> 0' rule).
This script asserts that precondition per row and fails loudly otherwise;
it never invents prediction content.
"""
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "judging", "judgeX-block3.jsonl")
DST = os.path.join(BASE, "judging", "judgeX-block3-scores.jsonl")
CHUNK = 31
REASON = (
    "预测为空(direction/assertions/timing/summary均为null),"
    "无终局方向、无具体断语、无应期可核;"
    "direction=0,claims=0;"
    "timing按冻结口径「预测断语本身无应期」记0并注明"
)


def main():
    assert os.path.exists(SRC), "input missing"
    assert not os.path.exists(DST), "output already exists; refusing to overwrite"

    rows = []
    with open(SRC, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    assert len(rows) == 122, f"expected 122 input rows, got {len(rows)}"

    scored = []
    for r in rows:
        pred = r.get("prediction")
        assert pred == {
            "direction": None,
            "assertions": None,
            "timing": None,
            "summary": None,
        }, f"non-null prediction encountered, manual scoring required: {r.get('anon_id')}"
        scored.append(
            {
                "anon_id": r["anon_id"],
                "direction": 0,
                "claims": 0,
                "timing": 0,
                "total": 0,
                "pass": False,
                "reason": REASON,
            }
        )

    written = 0
    for start in range(0, len(scored), CHUNK):
        part = scored[start : start + CHUNK]
        with open(DST, "a", encoding="utf-8") as out:
            for s in part:
                out.write(json.dumps(s, ensure_ascii=False) + "\n")
        written += len(part)
        # segment assertion: file line count must equal cumulative written
        with open(DST, encoding="utf-8") as chk:
            on_disk = sum(1 for ln in chk if ln.strip())
        assert on_disk == written, f"segment mismatch: disk={on_disk} written={written}"
        print(f"segment ok: {written}/{len(scored)}")

    assert written == len(rows) == 122
    print(f"DONE rows_in={len(rows)} rows_out={written}")


if __name__ == "__main__":
    main()
