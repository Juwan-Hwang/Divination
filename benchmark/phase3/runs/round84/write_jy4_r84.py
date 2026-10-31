#!/usr/bin/env python3
"""R84 judgeY-block4 scorer (seat Y4).

Input file's prediction object is entirely null for every row in this
block (verified per-row below): there is no direction, no assertion and
no timing claim to check against the outcome record. Per the frozen
JUDGE-PROMPT-verbatim scale:
  direction = 0 (no terminal direction to match)
  claims    = 0 (no specific assertion verifiable)
  timing    = 0, noted as "prediction itself states no timing"
  total = 0, pass = False
Writes scores in segments, appending and asserting the cumulative
line count after each segment. Refuses to run if the target exists.
"""
import json
import os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round84/judging"
SRC = os.path.join(BASE, "judgeY-block4.jsonl")
DST = os.path.join(BASE, "judgeY-block4-scores.jsonl")
SEGMENT = 31

REASON = (
    "本块judging文件内prediction四字段均为null，无可核预测断语："
    "方向无从印证、具体断语无可核；预测断语本身无应期。"
    "旗标：prediction全null，未按评审提示回读host-mapping/predictions原件（本席纪律禁止）。"
)

def main():
    assert not os.path.exists(DST), f"target already exists: {DST}"
    rows = [json.loads(line) for line in open(SRC, encoding="utf-8") if line.strip()]
    assert len(rows) == 121, f"expected 121 rows, got {len(rows)}"
    out = []
    for r in rows:
        pred = r["prediction"]
        assert set(pred.keys()) == {"direction", "assertions", "timing", "summary"}, pred.keys()
        assert all(v is None for v in pred.values()), f"non-null prediction in {r['anon_id']}"
        assert r.get("outcome_record"), f"missing outcome in {r['anon_id']}"
        out.append({
            "anon_id": r["anon_id"],
            "direction": 0,
            "claims": 0,
            "timing": 0,
            "total": 0,
            "pass": False,
            "reason": REASON,
        })
    written = 0
    for i in range(0, len(out), SEGMENT):
        chunk = out[i:i + SEGMENT]
        with open(DST, "a", encoding="utf-8") as f:
            for rec in chunk:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        written += len(chunk)
        on_disk = sum(1 for _ in open(DST, encoding="utf-8"))
        assert on_disk == written, f"segment assert failed: disk={on_disk} written={written}"
        print(f"segment ok: cumulative {written}")
    # final read-back verification
    back = [json.loads(line) for line in open(DST, encoding="utf-8")]
    assert len(back) == len(rows) == 121
    assert [b["anon_id"] for b in back] == [r["anon_id"] for r in rows]
    for b in back:
        assert b["direction"] == 0 and b["claims"] == 0 and b["timing"] == 0
        assert b["total"] == b["direction"] + b["claims"] + b["timing"] == 0
        assert b["pass"] is False
        assert set(b.keys()) == {"anon_id", "direction", "claims", "timing", "total", "pass", "reason"}
    print(f"done: {len(back)} scores written and verified")

if __name__ == "__main__":
    main()
