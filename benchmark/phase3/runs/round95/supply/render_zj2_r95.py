#!/usr/bin/env python3
"""R95 ZJ2: render Zhengjie source pages for ch12/13 existence census.
Raw renders + CCW-rotated copies + contact sheets, all inside
pages-zhengjie-ch1213-r95/. Source PDF is read-only, never copied."""
import os, subprocess, sys
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = "/home/hatch/workspace/divination/incoming/wanted-books-6/Book/紫微斗数命理学正解 (许铨仁著).pdf"
WORK = os.path.join(BASE, "pages-zhengjie-ch1213-r95")
RAW = os.path.join(WORK, "raw")
ROT = os.path.join(WORK, "rot")
SHEETS = os.path.join(WORK, "sheets")
for d in (RAW, ROT, SHEETS):
    os.makedirs(d, exist_ok=True)

if not os.listdir(RAW):
    subprocess.run(["pdftoppm", "-png", "-r", "150", SRC, os.path.join(RAW, "zj")], check=True)
pages = sorted(f for f in os.listdir(RAW) if f.startswith("zj") and f.endswith(".png"))
print("rendered pages:", len(pages))
assert len(pages) == 352, len(pages)

thumbs = []
for f in pages:
    im = Image.open(os.path.join(RAW, f))
    r = im.rotate(90, expand=True)  # CCW 90, measured body orientation (BATCH3-ZJ)
    out = os.path.join(ROT, f)
    if not os.path.exists(out):
        r.save(out)
    t = r.copy()
    t.thumbnail((360, 500))
    thumbs.append((f, t))

per = 12
nsheets = 0
for s in range(0, len(thumbs), per):
    chunk = thumbs[s:s + per]
    cols, rows = 3, 4
    cw = max(t.width for _, t in chunk) + 8
    ch = max(t.height for _, t in chunk) + 8
    sheet = Image.new("L", (cols * cw, rows * ch), 255)
    for i, (_, t) in enumerate(chunk):
        sheet.paste(t, ((i % cols) * cw + 4, (i // cols) * ch + 4))
    sheet.save(os.path.join(SHEETS, f"sheet-{s // per + 1:02d}.png"))
    nsheets += 1
print("sheets:", nsheets)
assert nsheets == 30, nsheets
print("OK")
