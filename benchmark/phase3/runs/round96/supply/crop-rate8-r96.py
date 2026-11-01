#!/usr/bin/env python3
from PIL import Image
import os
base = "/home/hatch/workspace/divination/benchmark/phase3/runs/round96/supply/pages-caiminghong-r96/hires"
jobs = [
    ("cmh-287.png", (120, 1580, 760, 2230), "cmh-287-crop-rate8.png"),   # CM-36 chart
    ("cmh-288.png", (150, 480, 720, 1080), "cmh-288-crop-rate8.png"),    # CM-37 chart
    ("cmh-306.png", (200, 1120, 760, 1700), "cmh-306-crop-rate8.png"),  # CM-38 chart
    ("cmh-307.png", (280, 460, 860, 1020), "cmh-307-crop-rate8.png"),   # CM-39 chart
    ("cmh-308.png", (200, 540, 720, 1080), "cmh-308-crop-rate8.png"),   # CM-40 chart
]
for src, box, name in jobs:
    im = Image.open(os.path.join(base, src))
    c = im.crop(box)
    c = c.resize((c.width * 2, c.height * 2), Image.LANCZOS)
    out = os.path.join(base, name)
    c.save(out)
    print(name, os.path.getsize(out))
