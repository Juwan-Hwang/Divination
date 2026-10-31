#!/usr/bin/env python3
"""Judge X block4 R84 scorer. Predictions in packet are all-null; score per frozen JUDGE-PROMPT."""
import json
from pathlib import Path

BASE = Path.home() / "workspace/divination/benchmark/phase3/runs/round84"
SRC = BASE / "judging/judgeX-block4.jsonl"
DST = BASE / "judging/judgeX-block4-scores.jsonl"

REASON = "预测四字段(direction/assertions/timing/summary)全为null，无终局方向、无具体断语可核；timing记0：预测断语本身无应期。"

def main():
    rows = [json.loads(ln) for ln in SRC.read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert len(rows) == 121, f"input count {len(rows)} != 121"
    assert len({r['anon_id'] for r in rows}) == 121
    scores = []
    for r in rows:
        pred = r.get("prediction") or {}
        assert all(pred.get(k) is None for k in ("direction", "assertions", "timing", "summary")), r["anon_id"]
        assert r.get("outcome_record"), r["anon_id"]
        reason = REASON
        if r["anon_id"] == "P3-e533c7df":
            reason += " 另：editor_note称甲戌日巳时细节未逐字复核——本条本无断语，该细项不影响零分。"
        scores.append({
            "anon_id": r["anon_id"],
            "direction": 0,
            "claims": 0,
            "timing": 0,
            "total": 0,
            "pass": False,
            "reason": reason,
        })
    # segmented append with per-segment assertions; no overwrite if file exists non-empty
    assert not DST.exists() or DST.stat().st_size == 0, "destination exists non-empty; refusing overwrite"
    chunks = [scores[i:i+31] for i in range(0, len(scores), 31)]
    written = 0
    with DST.open("a", encoding="utf-8") as f:
        for ci, chunk in enumerate(chunks):
            for s in chunk:
                f.write(json.dumps(s, ensure_ascii=False) + "\n")
            f.flush()
            written += len(chunk)
            cur = [ln for ln in DST.read_text(encoding="utf-8").splitlines() if ln.strip()]
            assert len(cur) == written, f"segment {ci}: on-disk {len(cur)} != written {written}"
    # final self-verify
    out = [json.loads(ln) for ln in DST.read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert len(out) == 121, len(out)
    assert [o["anon_id"] for o in out] == [r["anon_id"] for r in rows], "order/id mismatch"
    for o in out:
        assert o["total"] == o["direction"] + o["claims"] + o["timing"]
        assert o["pass"] == (o["total"] >= 4)
    print(f"OK written={len(out)} bytes={DST.stat().st_size}")

if __name__ == "__main__":
    main()
