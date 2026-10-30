#!/usr/bin/env python3
"""R50 类考候选补裁（另一半页）。"""
import os
from PIL import Image

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/work-leikao-r50"
OUT = os.path.join(BASE, "crops")

JOBS = [
    ("c38b-gehu", "lk-145-145.png", (0.00, 0.05, 0.52, 0.98)),
    ("c40b-daiyinshou", "lk-164-164.png", (0.00, 0.05, 0.52, 0.98)),
    ("c43b-chujiu", "lk-174-174.png", (0.50, 0.05, 1.00, 0.98)),
    ("c41c-wansui-165L", "lk-165-165.png", (0.50, 0.05, 1.00, 0.70)),
]
done = []
for name, fn, (x0, y0, x1, y1) in JOBS:
    p = os.path.join(BASE, fn)
    assert os.path.exists(p), p
    im = Image.open(p)
    w, h = im.size
    crop = im.crop((int(w * x0), int(h * y0), int(w * x1), int(h * y1)))
    crop = crop.resize((crop.width * 2, crop.height * 2), Image.LANCZOS)
    out = os.path.join(OUT, f"{name}.png")
    crop.save(out)
    done.append(out)
assert len(done) == 4
for d in done:
    print("OK", d)
