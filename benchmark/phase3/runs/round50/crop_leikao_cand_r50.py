#!/usr/bin/env python3
"""R50 类考候选放大裁切（LK2-C38..C46）。只读 work-leikao-r50 页图，输出到 crops/。"""
import os
from PIL import Image

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/work-leikao-r50"
OUT = os.path.join(BASE, "crops")
os.makedirs(OUT, exist_ok=True)

# (name, file, box-frac x0,y0,x1,y1)
JOBS = [
    ("c38-gehu泣", "lk-145-145.png", (0.50, 0.05, 1.00, 0.98)),
    ("c39-menzhong", "lk-157-157.png", (0.50, 0.05, 1.00, 0.98)),
    ("c40-daiyinshou", "lk-164-164.png", (0.50, 0.05, 1.00, 0.98)),
    ("c41-wansui-a", "lk-164-164.png", (0.50, 0.55, 1.00, 0.99)),
    ("c41-wansui-b", "lk-165-165.png", (0.00, 0.05, 0.52, 0.60)),
    ("c42-jiangtang", "lk-171-171.png", (0.00, 0.05, 1.00, 0.98)),
    ("c43-chujiu", "lk-174-174.png", (0.00, 0.05, 0.52, 0.98)),
    ("c44-goushegou", "lk-177-177.png", (0.50, 0.05, 1.00, 0.98)),
    ("c45-chengche", "lk-185-185.png", (0.00, 0.05, 0.52, 0.98)),
    ("c46-chezai", "lk-186-186.png", (0.50, 0.05, 1.00, 0.98)),
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

assert len(done) == 10, len(done)
for d in done:
    print("OK", d)
print("total", len(done))
