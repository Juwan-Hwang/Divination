#!/usr/bin/env python3
"""R48: crop center-fold (banxin) strips for xuanjie PDF 950-1000 views, montage 13 per sheet.
Banxin text sits on the left edge strip of each rotated view. Assertions on page count."""
import os
from PIL import Image

VIEW = "/home/hatch/workspace/divination/benchmark/phase3/runs/round48/digestion/work-xuanjie-r48/view"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round48/digestion/work-xuanjie-r48/banxin"
os.makedirs(OUT, exist_ok=True)

pages = list(range(950, 1001))
strips = []
for p in pages:
    im = Image.open(os.path.join(VIEW, f"p{p}.png"))
    w, h = im.size
    strip = im.crop((0, 0, int(w * 0.14), h))          # left fold strip
    strip = strip.rotate(-90, expand=True)              # make banxin text horizontal
    strip = strip.resize((strip.width * 2, strip.height * 2), Image.LANCZOS)
    strips.append((p, strip))
assert len(strips) == 51, len(strips)

per = 13
for gi in range(0, len(strips), per):
    chunk = strips[gi:gi + per]
    W = max(s.width for _, s in chunk)
    H = sum(s.height for _, s in chunk)
    sheet = Image.new("L", (W, H), 255)
    y = 0
    for _, s in chunk:
        sheet.paste(s, (0, y)); y += s.height
    name = f"banxin-{chunk[0][0]}-{chunk[-1][0]}.png"
    sheet.save(os.path.join(OUT, name))
    print(name, sheet.size)
print("OK")
