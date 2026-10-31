#!/usr/bin/env python3
"""R88 host independent seal verification for holdout32 (third read).
Independent of the sealing seat's scripts: re-reads the gold SHA-256,
re-scans the 28 input cards (banned keys / leak markers / field
whitelist, marker set per R42 PREREG s.5 carried verbatim), re-checks
composition against used-ids-r88.json, and re-verifies the snapshot
against the live method by SHA-256.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
H32 = P3 / "holdout32"
SEAT_SHA = "f5a8ae014cef3363273e4c9ae4b3591c16f79a8a3c8944d39a0d83c97ca158b8"

BANNED_KEYS = {
    "outcome", "outcome_text", "outcome_record", "actual_outcome",
    "result", "verdict", "gold", "gold_outcome", "master_prediction",
    "master_verdict", "master_total", "answer", "answers",
    "scoring", "scores", "score", "judge", "judges",
}
LEAK_MARKERS = ["大师断", "大师曰", "原断曰", "断语曰", "果如", "果应", "后验", "后果",
                "结局", "结果载", "实测结局", "最终结局", "应验于", "果验"]

gold_bytes = (H32 / "test_gold.jsonl").read_bytes()
sha = hashlib.sha256(gold_bytes).hexdigest()
gold = [json.loads(l) for l in gold_bytes.decode("utf-8").splitlines() if l.strip()]
gold_ids = sorted(r["id"] for r in gold)
print("gold SHA host third read:", sha, "| match seat dual-read:", sha == SEAT_SHA,
      "| bytes:", len(gold_bytes), "| lines:", len(gold))

sel = json.loads((P3 / "runs/round88/holdout32-selection-r88.json").read_text(encoding="utf-8"))
print("selection file keys:", sorted(sel)[:8])

used = set(json.loads((P3 / "runs/round88/used-ids-r88.json").read_text(encoding="utf-8")))
print("used union:", len(used), "| overlap with gold ids:", sorted(used & set(gold_ids)))
print("LY-015/LY-320 in set:", [x for x in ("LY-015", "LY-320") if x in gold_ids])

WL_TOP = {"id", "tradition", "question", "context", "anchors",
          "anchor_texts", "provenance", "grade_note"}
hits, wl_dev = {}, []
import os
n_cards = 0
for cid in gold_ids:
    card = json.loads((H32 / "inputs" / f"{cid}.json").read_text(encoding="utf-8"))
    n_cards += 1
    assert card.get("id") == cid, cid
    extra = set(card) - WL_TOP
    if extra:
        wl_dev.append((cid, sorted(extra)))

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k.lower() in BANNED_KEYS:
                    hits.setdefault(cid, []).append("key:" + k)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, str):
            for m in LEAK_MARKERS:
                if m in o:
                    hits.setdefault(cid, []).append("marker:" + m)
    walk(card)
print("cards read:", n_cards)
print("scan hits:", hits)
print("whitelist deviations:", wl_dev)
print("pollution counts:", {p: sum(1 for r in gold if r.get("pollution") == p)
                            for p in {r.get("pollution") for r in gold}})

SNAP = P3 / "runs/round88/kb-snapshot-holdout32"
LIVE = P3 / "method"
diff = []
count = 0
for f in sorted(SNAP.rglob("*")):
    if f.is_file():
        rel = f.relative_to(SNAP)
        lf = LIVE / rel
        count += 1
        if not lf.exists() or hashlib.sha256(f.read_bytes()).hexdigest() != hashlib.sha256(lf.read_bytes()).hexdigest():
            diff.append(str(rel))
print("snapshot files:", count, "| diff vs live method:", diff)
