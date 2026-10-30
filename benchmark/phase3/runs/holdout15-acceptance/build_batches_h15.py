#!/usr/bin/env python3
"""holdout15 acceptance batch builder (host tooling). Mixed batches by
source stride: interleave the three source lists round-robin in SEALED
source order (ZC, BYZ, YXS), then deal cyclically into three batches
A1/A2/A3 (14/13/13). Source composition is not disclosed to the blind
seats; seats read only holdout15-inputs/ cards.
"""
import json
from collections import deque
from pathlib import Path

ACC = Path(__file__).resolve().parent
P3 = ACC.parents[1]

groups = {}
for cid in [json.loads(l)["id"] for l in open(P3 / "holdout15" / "test_gold.jsonl") if l.strip()]:
    groups.setdefault(cid.split("-")[0], []).append(cid)
order = ["ZC", "BYZ", "YXS"]
queues = {k: deque(sorted(groups[k])) for k in order}
mixed = []
while any(queues.values()):
    for k in order:
        if queues[k]:
            mixed.append(queues[k].popleft())
assert len(mixed) == 40
# NOTE: plain cyclic dealing over a 3-source round-robin degenerates to
# per-source batches (period 3 == batch count); shuffle with a fixed seed
# first so batches are genuinely mixed (host-side only; composition is
# not disclosed to seats either way).
import random
random.Random(20261039).shuffle(mixed)
batches = {"A1": [], "A2": [], "A3": []}
for i, cid in enumerate(mixed):
    batches[f"A{i % 3 + 1}"].append(cid)
with open(ACC / "batches.json", "w", encoding="utf-8") as fh:
    json.dump(batches, fh, ensure_ascii=False, indent=1)
print({k: len(v) for k, v in batches.items()})
