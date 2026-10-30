#!/usr/bin/env python3
"""R48 banxin montage v2: 5 strips per sheet, no upscale. Unique name per round48 discipline."""
import os
from PIL import Image

VIEW = "/home/hatch/workspace/divination/benchmark/phase3/runs/round48/digestion/work-xuanjie-r48/view"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round48/digestion/work-xuanjie-r48/banxin2"
os.makedirs(OUT, exist_ok=True)

pages = list(range(950, 1001))
strips = []
for p in pages:
    im = Image.open(os.path.join(VIEW, f"p{p}.png"))
    w, h = im.size
    strip = im.crop((0, 0, int(w * 0.14), h)).rotate(-90, expand=True)
    strips.append((p, strip))
assert len(strips) == 51

per = 5
for gi in range(0, len(strips), per):
    chunk = strips[gi:gi + per]
    W = max(s.width for _, s in chunk)
    H = sum(s.height for _, s in chunk)
    sheet = Image.new("L", (W, H), 255)
    y = 0
    for _, s in chunk:
        sheet.paste(s, (0, y)); y += s.height
    name = f"b2-{chunk[0][0]}-{chunk[-1][0]}.png"
    sheet.save(os.path.join(OUT, name))
    print(name, sheet.size)
print("OK")
