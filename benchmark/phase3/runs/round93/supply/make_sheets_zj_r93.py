#!/usr/bin/env python3
"""R93 Zhengjie: rotate 200dpi renders CCW 90 (measured body orientation),
build rotated working copies + contact sheets for case-face location.
Raw renders stay in pages-zhengjie-r93/ untouched."""
import os
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "pages-zhengjie-r93")
ROT = os.path.join(BASE, "pages-zhengjie-r93-rot")
SHEETS = os.path.join(BASE, "sheets-zhengjie-r93")
os.makedirs(ROT, exist_ok=True)
os.makedirs(SHEETS, exist_ok=True)

pages = sorted(f for f in os.listdir(SRC) if f.startswith("zj-") and f.endswith(".png"))
print("pages:", len(pages))
thumbs = []
for f in pages:
    out = os.path.join(ROT, f)
    im = Image.open(os.path.join(SRC, f))
    if not os.path.exists(out):
        im.rotate(90, expand=True).save(out)
    t = im.rotate(90, expand=True)
    t.thumbnail((360, 500))
    thumbs.append((f, t))

# contact sheets: 12 per sheet (3 cols x 4 rows), labelled by filename in file order
per = 12
for s in range(0, len(thumbs), per):
    chunk = thumbs[s:s + per]
    cols, rows = 3, 4
    cw = max(t.width for _, t in chunk) + 8
    ch = max(t.height for _, t in chunk) + 8
    sheet = Image.new("L", (cols * cw, rows * ch), 255)
    for i, (_, t) in enumerate(chunk):
        x = (i % cols) * cw + 4
        y = (i // cols) * ch + 4
        sheet.paste(t, (x, y))
    sheet.save(os.path.join(SHEETS, f"sheet-{s // per + 1:02d}.png"))
print("sheets:", (len(thumbs) + per - 1) // per)
