#!/usr/bin/env python3
"""R52 leikao cont seat (second seat): crops from EXISTING 130dpi work renders only (no PDF re-render),
enlarged 3x for verbatim check of candidate passages C52/C53/C54."""
from PIL import Image
import pathlib
base = pathlib.Path(__file__).parent / "digestion" / "work-leikao-r52"
out = pathlib.Path(__file__).parent / "digestion" / "work-leikao-r52" / "crops-cont"
out.mkdir(exist_ok=True)
jobs = [
    ("lk-235-235.png", (0.00, 0.12, 0.50, 0.97), "c52_p235_left"),
    ("lk-236-236.png", (0.50, 0.12, 1.00, 0.60), "c52_p236_right_top"),
    ("lk-258-258.png", (0.50, 0.12, 1.00, 0.97), "c53_p258_right"),
    ("lk-271-271.png", (0.00, 0.12, 0.50, 0.97), "c54_p271_left"),
]
for name, (x0, y0, x1, y1), tag in jobs:
    im = Image.open(base / name)
    w, h = im.size
    crop = im.crop((int(w*x0), int(h*y0), int(w*x1), int(h*y1)))
    crop = crop.resize((crop.size[0]*3, crop.size[1]*3), Image.LANCZOS)
    crop.save(out / f"{tag}.png")
    print(tag, crop.size)
print("done")
