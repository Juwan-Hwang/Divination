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

# C61 candidate: p339 left leaf, 二棺自天而落 (middle band) + 芻狗 tail above
crop(os.path.join(SRC54, "lk-339-339.png"), "339L", (0.0, 0.08, 0.52, 0.72), "c61_erguan_p339_left_r54.png", scale=2)
# C62 candidate: p346 right leaf lower (大墳露棺 start) and left leaf upper (聞淵解 + 結局)
crop(os.path.join(SRC54, "lk-346-346.png"), "346R", (0.50, 0.30, 1.0, 0.97), "c62_dafen_p346_right_r54.png", scale=2)
crop(os.path.join(SRC54, "lk-346-346.png"), "346L", (0.0, 0.08, 0.52, 0.62), "c62_dafen_p346_left_r54.png", scale=2)
# also p339 right leaf for 芻狗 full + 二棺 header context
crop(os.path.join(SRC54, "lk-339-339.png"), "339R", (0.48, 0.08, 1.0, 0.97), "c61_ctx_p339_right_r54.png", scale=2)
