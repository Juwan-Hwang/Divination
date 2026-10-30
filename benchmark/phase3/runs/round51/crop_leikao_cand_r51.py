#!/usr/bin/env python3
"""R51 leikao crops: render PDF 193 & 199 at 300dpi, crop candidate regions for verbatim check."""
import subprocess, os
from PIL import Image
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round51/digestion/work-leikao-r51/crops"
os.makedirs(OUT, exist_ok=True)
for p in (193, 199):
    prefix = f"/tmp/lk300-{p}"
    r = subprocess.run(["pdftoppm","-png","-r","300","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:300]
    f = [x for x in os.listdir("/tmp") if x.startswith(f"lk300-{p}")][0]
    im = Image.open(os.path.join("/tmp", f))
    w, h = im.size
    print(p, im.size)
    # right leaf = right half of scan, left leaf = left half
    im.crop((int(w*0.52), 0, w, h)).save(os.path.join(OUT, f"c{p}-right.png"))
    im.crop((0, 0, int(w*0.48), h)).save(os.path.join(OUT, f"c{p}-left.png"))
print("done", sorted(os.listdir(OUT)))
