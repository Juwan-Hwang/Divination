#!/usr/bin/env python3
from PIL import Image
import pathlib
base = pathlib.Path(__file__).parent / "leikao_r52_pages"
out = pathlib.Path(__file__).parent / "leikao_r52_crops"
out.mkdir(exist_ok=True)
# p199 left half is C48: crop left 0-48% width, full height, then enlarge
for name, box_rel, scale_name in [
    ("p199-199.png", (0.00, 0.10, 0.50, 0.97), "c48_left"),
    ("p204-204.png", (0.00, 0.10, 0.22, 0.97), "c51_start_leftedge"),
    ("p205-205.png", (0.50, 0.10, 1.00, 0.97), "c51_cont_right"),
]:
    im = Image.open(base / name)
    w, h = im.size
    box = (int(w*box_rel[0]), int(h*box_rel[1]), int(w*box_rel[2]), int(h*box_rel[3]))
    crop = im.crop(box)
    crop.save(out / f"{scale_name}.png")
    print(scale_name, crop.size)
print("done")
