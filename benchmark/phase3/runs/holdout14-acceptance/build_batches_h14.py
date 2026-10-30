#!/usr/bin/env python3
"""holdout14 acceptance batch builder (host tooling). Mixed batches by
source stride: interleave the six source lists round-robin in SEALED
source order (DA, BY, CY, BQ, PU, CZ), then deal cyclically into three
batches A1/A2/A3 (14/13/13). Source composition is not disclosed to the
blind seats; seats read only holdout14-inputs/ cards.
"""
import json
from collections import deque
from pathlib import Path

ACC = Path(__file__).resolve().parent
P3 = ACC.parents[1]

groups = {}
for cid in [json.loads(l)["id"] for l in open(P3 / "holdout14" / "test_gold.jsonl") if l.strip()]:
    groups.setdefault(cid.split("-")[0], []).append(cid)
order = ["DA", "BY", "CY", "BQ", "PU", "CZ"]
queues = {k: deque(sorted(groups[k])) for k in order}
mixed = []
while any(queues.values()):
    for k in order:
        if queues[k]:
            mixed.append(queues[k].popleft())
assert len(mixed) == 40
batches = {"A1": [], "A2": [], "A3": []}
for i, cid in enumerate(mixed):
    batches[f"A{i % 3 + 1}"].append(cid)
with open(ACC / "batches.json", "w", encoding="utf-8") as fh:
    json.dump(batches, fh, ensure_ascii=False, indent=1)
print({k: len(v) for k, v in batches.items()})
print(batches)
