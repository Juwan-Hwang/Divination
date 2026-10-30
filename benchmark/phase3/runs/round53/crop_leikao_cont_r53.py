#!/usr/bin/env python3
"""R53 leikao cont: crops from EXISTING 130dpi work renders only (no PDF re-render), enlarged 3x
for verbatim check of candidate passages."""
from PIL import Image
import pathlib
base = pathlib.Path(__file__).parent / "digestion" / "work-leikao-r53"
r52 = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round52/digestion/work-leikao-r52")
out = base / "crops-cont"
out.mkdir(exist_ok=True)
jobs = [
    (base, "lk-281-281.png", (0.50, 0.10, 1.00, 0.98), "c55_p281_right"),
    (base, "lk-283-283.png", (0.00, 0.10, 0.52, 0.98), "c56_p283_left"),
    (base, "lk-304-304.png", (0.00, 0.10, 0.52, 0.98), "c57_p304_left"),
    (base, "lk-306-306.png", (0.00, 0.10, 0.52, 0.98), "c58_p306_left"),
    (base, "lk-311-311.png", (0.00, 0.55, 0.52, 0.98), "c59_p311_leftbot"),
    (base, "lk-312-312.png", (0.50, 0.10, 1.00, 0.65), "c59_p312_righttop"),
    (base, "lk-315-315.png", (0.00, 0.55, 0.52, 0.98), "qianchai_p315_leftbot"),
    (base, "lk-316-316.png", (0.50, 0.10, 1.00, 0.55), "qianchai_p316_righttop"),
    (r52, "lk-276-276.png", (0.00, 0.10, 0.52, 0.98), "zifu_p276_left"),
    (base, "lk-277-277.png", (0.50, 0.10, 1.00, 0.55), "zifu_p277_righttop"),
    (base, "lk-313-313.png", (0.50, 0.45, 1.00, 0.98), "deyimao_p313_rightbot"),
    (base, "lk-319-319.png", (0.00, 0.10, 0.52, 0.98), "huangli_p319_left"),
    (base, "lk-289-289.png", (0.50, 0.10, 1.00, 0.98), "shimo_p289_right"),
]
for b, name, (x0, y0, x1, y1), tag in jobs:
    im = Image.open(b / name)
    w, h = im.size
    crop = im.crop((int(w*x0), int(h*y0), int(w*x1), int(h*y1)))
    crop = crop.resize((crop.size[0]*3, crop.size[1]*3), Image.LANCZOS)
    crop.save(out / f"{tag}.png")
    print(tag, crop.size)
print("done")
