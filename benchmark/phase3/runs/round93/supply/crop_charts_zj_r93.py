#!/usr/bin/env python3
"""Crop chart regions from rotated 200dpi pages and upscale 2x for cell-level reading.
Usage: python3 crop_charts_zj_r93.py <page> <x0> <y0> <x1> <y1> <tag>  (fractions of W/H)"""
import os, sys
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
ROT = os.path.join(BASE, "pages-zhengjie-r93-rot")
OUT = os.path.join(BASE, "crops-zhengjie-r93")
os.makedirs(OUT, exist_ok=True)

page, x0, y0, x1, y1, tag = sys.argv[1], *map(float, sys.argv[2:6]), sys.argv[6]
im = Image.open(os.path.join(ROT, f"zj-{int(page):03d}.png"))
W, H = im.size
box = (int(W * x0), int(H * y0), int(W * x1), int(H * y1))
c = im.crop(box)
c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
out = os.path.join(OUT, f"crop-{int(page):03d}-{tag}.png")
c.save(out)
print(out, c.size)
