#!/usr/bin/env python3
"""R59 WHY partial recheck: render scanned source sheets and split into printed pages.
Source: incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf (scanned, no text layer)
Mapping verified on sheet 6: PDF sheet N contains printed pages (2N-2 right, 2N-1 left).
"""
import subprocess, os
from PIL import Image

SRC = "/home/hatch/workspace/divination/incoming/wanted-books-4/Book/六爻分类占验技法 (王虎应著).pdf"
OUT = "/tmp/whyrecheck/pages"
os.makedirs(OUT, exist_ok=True)

# printed pages needed for the 41 mechanically-derived candidates
printed = [9,10,11,29,30,31,32,35,36,37,38,39,40,55,56,57,91,92,93,127,
           145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,
           167,168,171,172,173,175,176,196,197,200,201,202,203]
sheets = sorted(set(p//2 + 1 for p in printed))
print("sheets:", sheets)
for s in sheets:
    png = f"/tmp/whyrecheck/s{s}.png"
    if not os.path.exists(png):
        subprocess.run(["pdftoppm","-png","-r","150","-f",str(s),"-l",str(s),SRC,f"/tmp/whyrecheck/s{s}"], check=True)
        # pdftoppm names output s{s}-NNN.png
        import glob
        got = glob.glob(f"/tmp/whyrecheck/s{s}-*.png")
        assert len(got)==1, got
        os.rename(got[0], png)
    im = Image.open(png)
    w,h = im.size
    # right half = printed page 2s-2, left half = printed page 2s-1 (verified sheet6: right=p10, left=p11)
    right = im.crop((w//2,0,w,h)); left = im.crop((0,0,w//2,h))
    for page, img in ((2*s-2, right),(2*s-1, left)):
        if page in printed:
            img.save(f"{OUT}/p{page}.png")
print("done", sorted(os.listdir(OUT)))
