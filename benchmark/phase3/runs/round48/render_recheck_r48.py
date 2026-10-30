#!/usr/bin/env python3
"""R48 data-verify: render original pages at 300dpi and make column crops.
Assertions included per派单纪律. Only reads the two incoming PDFs, writes
under runs/round48/data-verify/work-r48/."""
import subprocess, os
from PIL import Image

BASE = "/home/hatch/workspace/divination"
OUT = f"{BASE}/benchmark/phase3/runs/round48/data-verify/work-r48"
os.makedirs(OUT, exist_ok=True)

XJ = f"{BASE}/incoming/wanted-books-3/Book/梦林玄解 (（宋）邵雍，（明）陈士元).pdf"
LK = f"{BASE}/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
assert os.path.exists(XJ), "xuanjie pdf missing"
assert os.path.exists(LK), "leikao pdf missing"

def render(pdf, page, tag):
    prefix = f"{OUT}/{tag}"
    subprocess.run(["pdftoppm", "-png", "-r", "300", "-f", str(page), "-l", str(page), pdf, prefix], check=True)
    files = [f for f in os.listdir(OUT) if f.startswith(tag + "-")]
    assert len(files) == 1, (tag, files)
    p = f"{OUT}/{files[0]}"
    im = Image.open(p)
    print(tag, "page", page, "size", im.size)
    return p, im

def crop(im, box, name, scale=2):
    w, h = im.size
    x0, y0, x1, y1 = (int(box[0]*w), int(box[1]*h), int(box[2]*w), int(box[3]*h))
    c = im.crop((x0, y0, x1, y1))
    c = c.resize((c.size[0]*scale, c.size[1]*scale), Image.LANCZOS)
    c.save(f"{OUT}/{name}")
    print("crop", name, c.size)

# --- Leikao p13: LK-009 on right leaf, Zhang Bin column ---
p, im = render(LK, 13, "lk-p13")
# full right leaf
crop(im, (0.50, 0.08, 0.99, 0.97), "lk009-rightleaf.png", 1)
# columns: first col (LK-008, contains 木上破天/未字) + Zhang Bin col (3rd from right on right leaf)
crop(im, (0.78, 0.08, 0.99, 0.97), "lk009-cols-a.png", 1)
crop(im, (0.60, 0.08, 0.86, 0.97), "lk009-cols-b.png", 1)

# --- Xuanjie pages ---
pages = {1062: "xj-p1062", 1125: "xj-p1125", 1155: "xj-p1155", 1156: "xj-p1156",
         1163: "xj-p1163", 1175: "xj-p1175", 1189: "xj-p1189"}
ims = {}
for pg, tag in pages.items():
    _, ims[pg] = render(XJ, pg, tag)

# 047: left leaf, first columns (Chen Qi text at far left of p1062)
crop(ims[1062], (0.00, 0.05, 0.22, 0.98), "xj047-chenqi.png", 1)
# 267: right leaf columns 3-5 (title + Zheng Fan text)
crop(ims[1125], (0.62, 0.05, 0.99, 0.98), "xj267-zhengfan.png", 1)
# 368: left leaf far-left columns (Song X dreamer name at start)
crop(ims[1155], (0.00, 0.05, 0.30, 0.98), "xj368-song.png", 1)
# 371: left leaf middle columns (Wei Wen / Zhang name)
crop(ims[1156], (0.15, 0.05, 0.52, 0.98), "xj371-weiwen.png", 1)
# 393: left leaf columns (Yuan Yuan text incl. damaged column)
crop(ims[1163], (0.00, 0.05, 0.50, 0.98), "xj393-yuanyuan.png", 1)
# 439: left leaf far-left column (Song Qiong)
crop(ims[1175], (0.00, 0.05, 0.18, 0.98), "xj439-songqiong.png", 1)
# 495: right leaf columns (Zhu Dan)
crop(ims[1189], (0.58, 0.05, 0.99, 0.98), "xj495-zhu.png", 1)
print("DONE", len(os.listdir(OUT)), "files in", OUT)
