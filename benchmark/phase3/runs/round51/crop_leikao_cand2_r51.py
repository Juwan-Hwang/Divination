#!/usr/bin/env python3
"""R51 leikao crops #2: PDF 203/204/205 candidate regions."""
import subprocess, os
from PIL import Image
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round51/digestion/work-leikao-r51/crops"
os.makedirs(OUT, exist_ok=True)
for p, side in ((203, "left"), (204, "right"), (205, "right")):
    prefix = f"/tmp/lk300b-{p}"
    r = subprocess.run(["pdftoppm","-png","-r","300","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:300]
    f = [x for x in os.listdir("/tmp") if x.startswith(f"lk300b-{p}")][0]
    im = Image.open(os.path.join("/tmp", f))
    w, h = im.size
    if side == "right":
        im.crop((int(w*0.52), 0, w, h)).save(os.path.join(OUT, f"c{p}-right.png"))
    else:
        im.crop((0, 0, int(w*0.48), h)).save(os.path.join(OUT, f"c{p}-left.png"))
    print(p, side, "ok")
print("done")
