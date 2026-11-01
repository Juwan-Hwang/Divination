#!/usr/bin/env python3
"""R96 census setup: contact sheets (12 pages/sheet) for caiminghong renders.
Reads raw/cm-*.png, writes sheets/sheet-NN.png with page-number labels."""
import os
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "pages-caiminghong-r96", "raw")
SHEETS = os.path.join(BASE, "pages-caiminghong-r96", "sheets")
os.makedirs(SHEETS, exist_ok=True)

files = sorted(f for f in os.listdir(RAW) if f.startswith("cm-") and f.endswith(".png"))
assert len(files) == 608, len(files)

THUMB_W = 340
COLS, ROWS = 3, 4
LABEL_H = 22
per = COLS * ROWS  # 12

made = []
for s in range(0, len(files), per):
    chunk = files[s:s + per]
    thumbs = []
    for f in chunk:
        im = Image.open(os.path.join(RAW, f)).convert("RGB")
        r = THUMB_W / im.width
        thumbs.append(im.resize((THUMB_W, int(im.height * r))))
    cell_h = max(t.height for t in thumbs) + LABEL_H
    sheet = Image.new("RGB", (COLS * THUMB_W + (COLS + 1) * 8, ROWS * cell_h + (ROWS + 1) * 8), "white")
    d = ImageDraw.Draw(sheet)
    for i, (f, t) in enumerate(zip(chunk, thumbs)):
        cx = 8 + (i % COLS) * (THUMB_W + 8)
        cy = 8 + (i // COLS) * (cell_h + 8)
        d.text((cx + 4, cy + 3), f, fill="black")
        sheet.paste(t, (cx, cy + LABEL_H))
    name = f"sheet-{s // per + 1:02d}.png"
    sheet.save(os.path.join(SHEETS, name))
    made.append(name)

print("sheets:", len(made), made[0], made[-1])
print("sheet_bytes_total:", sum(os.path.getsize(os.path.join(SHEETS, m)) for m in made))
