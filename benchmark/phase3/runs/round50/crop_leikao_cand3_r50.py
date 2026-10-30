#!/usr/bin/env python3
"""R50 类考候选补裁二（对侧半页）。"""
import os
from PIL import Image

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/work-leikao-r50"
OUT = os.path.join(BASE, "crops")

JOBS = [
    ("c39b-menzhong", "lk-157-157.png", (0.00, 0.05, 0.52, 0.98)),
    ("c44b-goushegou", "lk-177-177.png", (0.00, 0.05, 0.52, 0.98)),
    ("c45b-chengche", "lk-185-185.png", (0.50, 0.05, 1.00, 0.98)),
    ("c46b-chezai", "lk-186-186.png", (0.00, 0.05, 0.52, 0.98)),
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
