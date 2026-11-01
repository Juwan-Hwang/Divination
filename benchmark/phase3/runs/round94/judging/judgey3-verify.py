import json
base = "/home/hatch/workspace/divination/benchmark/phase3/runs/round94/judging/"
block = [json.loads(l) for l in open(base + "judgeY-block3.jsonl") if l.strip()]
scores = [json.loads(l) for l in open(base + "judgeY3-scores.jsonl") if l.strip()]
print("block", len(block), "scores", len(scores))
bids = [r["anon_id"] for r in block]
sids = [r["anon_id"] for r in scores]
print("set equal:", set(bids) == set(sids), "order equal:", bids == sids, "dup:", len(sids) != len(set(sids)))
bad = []
for s in scores:
    if s["total"] != s["direction"] + s["claims"] + s["timing"]:
        bad.append((s["anon_id"], "total"))
    if s["pass"] != (s["total"] >= 4):
        bad.append((s["anon_id"], "pass"))
    for k in ("direction", "claims", "timing"):
        if s[k] not in (0, 1, 2):
            bad.append((s["anon_id"], k))
    if set(s.keys()) != {"anon_id", "direction", "claims", "timing", "total", "pass", "gap_note"}:
        bad.append((s["anon_id"], "keys"))
print("bad:", bad)
tot = sum(s["total"] for s in scores)
print("sum", tot, "mean", round(tot / len(scores), 3))
print("pass count", sum(1 for s in scores if s["pass"]))
from collections import Counter
print("total dist", sorted(Counter(s["total"] for s in scores).items()))
