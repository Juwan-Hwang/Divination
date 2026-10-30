#!/usr/bin/env python3
"""R53 second crop: qianchai middle columns (315 left, last columns) at 4x."""
from PIL import Image
import pathlib
base = pathlib.Path(__file__).parent / "digestion" / "work-leikao-r53"
out = base / "crops-cont"
im = Image.open(base / "lk-315-315.png")
w, h = im.size
crop = im.crop((0, int(h*0.50), int(w*0.24), int(h*0.99)))
crop = crop.resize((crop.size[0]*4, crop.size[1]*4), Image.LANCZOS)
crop.save(out / "qianchai_p315_detail.png")
print("saved", crop.size)
im2 = Image.open(base / "lk-315-315.png")
crop2 = im2.crop((int(w*0.20), int(h*0.50), int(w*0.52), int(h*0.99)))
crop2 = crop2.resize((crop2.size[0]*4, crop2.size[1]*4), Image.LANCZOS)
crop2.save(out / "qianchai_p315_mid.png")
print("saved2", crop2.size)
