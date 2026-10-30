#!/usr/bin/env python3
"""R54 leikao crops: crop regions from r54 rendered pages (and r53 lk-289 for hanging check) at native res, upscale 2x."""
from PIL import Image
import os
SRC54 = "/home/hatch/workspace/divination/benchmark/phase3/runs/round54/digestion/work-leikao-r54"
SRC53 = "/home/hatch/workspace/divination/benchmark/phase3/runs/round53/digestion/work-leikao-r53"
OUT = os.path.join(SRC54, "crops-r54")
os.makedirs(OUT, exist_ok=True)

def crop(src, name, box_frac, out_name, scale=2):
    im = Image.open(src)
    w, h = im.size
    box = (int(w*box_frac[0]), int(h*box_frac[1]), int(w*box_frac[2]), int(h*box_frac[3]))
    c = im.crop(box)
    if scale != 1:
        c = c.resize((c.width*scale, c.height*scale), Image.LANCZOS)
    p = os.path.join(OUT, out_name)
    c.save(p)
    print(p, c.size)

# 289 right half = first leaf of spread (right side of image), where 失墨蒙責 sits per R53
crop(os.path.join(SRC53, "lk-289-289.png"), "289", (0.50, 0.10, 1.0, 0.95), "shimo_p289_righthalf_r54.png", scale=1)
