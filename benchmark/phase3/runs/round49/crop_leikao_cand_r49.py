#!/usr/bin/env python3
"""R49: crop candidate regions from existing 130dpi renders for verbatim check. Assertions included."""
import os
from PIL import Image
SRC = "/home/hatch/workspace/divination/benchmark/phase3/runs/round49/digestion/work-leikao-r49"
OUT = os.path.join(SRC, "crops")
os.makedirs(OUT, exist_ok=True)
# (page, name, box as fractions x0,y0,x1,y1) - right half is x 0.5-1.0 in reading order first; images show right half on right side
jobs = [
 (102,"c102-lvdu-left", (0.0,0.12,0.52,0.97)),
 (104,"c104-niuliangwei-left", (0.0,0.12,0.52,0.97)),
 (105,"c105-baitu-right", (0.48,0.12,1.0,0.97)),
 (105,"c105-baitu-left", (0.0,0.12,0.52,0.97)),
 (106,"c106-niushou-right", (0.48,0.12,1.0,0.97)),
 (109,"c109-dayang-left", (0.0,0.12,0.52,0.97)),
 (111,"c111-zhupian-right", (0.48,0.12,1.0,0.97)),
 (112,"c112-muzhu-left", (0.0,0.55,0.52,0.97)),
 (113,"c113-maowo-left", (0.0,0.12,0.52,0.75)),
 (127,"c127-shefu-left", (0.0,0.12,0.52,0.97)),
 (132,"c132-cancan-right", (0.48,0.12,1.0,0.75)),
 (133,"c133-momai-left", (0.0,0.12,0.52,0.97)),
 (134,"c134-luobo-left", (0.0,0.12,0.52,0.97)),
 (136,"c136-songchu-left", (0.0,0.30,0.52,0.97)),
 (137,"c137-songhu-right", (0.48,0.12,1.0,0.60)),
 (140,"c140-fenli-right", (0.48,0.12,1.0,0.97)),
 (142,"c142-zhu-left", (0.0,0.12,0.52,0.97)),
]
done=[]
for p,name,(x0,y0,x1,y1) in jobs:
    f = os.path.join(SRC, f"lk-{p:03d}-{p}.png")
    assert os.path.isfile(f), f
    im = Image.open(f); w,h = im.size
    crop = im.crop((int(w*x0),int(h*y0),int(w*x1),int(h*y1)))
    crop = crop.resize((crop.width*2, crop.height*2), Image.LANCZOS)
    o = os.path.join(OUT, name+".png"); crop.save(o); done.append(name)
print("OK crops:", len(done), done)
assert len(done)==len(jobs)
