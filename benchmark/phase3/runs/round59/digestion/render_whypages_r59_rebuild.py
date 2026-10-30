#!/usr/bin/env python3
"""R59 rebuild (data seat): render WHY source pages for recheck of 41 WHY candidates.
Same page-mapping as predecessor render_recheck_r59.py (sheet N -> printed 2N-2 right, 2N-1 left),
re-derived independently; output to /tmp/whyrb/ as half-page JPGs at 200dpi.
"""
import subprocess, os, glob
from PIL import Image

SRC = "/home/hatch/workspace/divination/incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf"
OUT = "/tmp/whyrb"
os.makedirs(OUT, exist_ok=True)
printed = [9,10,11,29,30,31,32,35,36,37,38,39,40,55,56,57,91,92,93,127,
           145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,
           167,168,171,172,173,175,176,196,197,200,201,202,203]
sheets = sorted(set(p//2 + 1 for p in printed))
for s in sheets:
    png = f"{OUT}/s{s}.png"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm","-png","-r","200","-f",str(s),"-l",str(s),SRC,f"{OUT}/s{s}"], check=True)
        got = glob.glob(f"{OUT}/s{s}-*.png"); assert len(got)==1, got
        os.rename(got[0], png)
    im = Image.open(png); w,h = im.size
    right = im.crop((w//2,0,w,h)); left = im.crop((0,0,w//2,h))
    for page, img in ((2*s-2, right),(2*s-1, left)):
        if page in printed:
            img.save(f"{OUT}/p{page}.jpg", quality=82)
print("done", len(os.listdir(OUT)))
