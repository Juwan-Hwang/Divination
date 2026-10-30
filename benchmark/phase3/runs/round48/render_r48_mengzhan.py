#!/usr/bin/env python3
"""R48 render script: leikao pp.61-100 via pdftoppm; xuanjie pp.950-1000 + 1040-1051 via pdfimages+rotate.
Assertions included per R48 PREREG §10 write-disk discipline."""
import subprocess, os, glob
from PIL import Image

ROOT = "/home/hatch/workspace/divination"
LK = os.path.join(ROOT, "incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf")
XJ = os.path.join(ROOT, "incoming/wanted-books-3/Book/梦林玄解 (（宋）邵雍，（明）陈士元).pdf")
LKDIR = os.path.join(ROOT, "benchmark/phase3/runs/round48/digestion/work-leikao-r48")
XJDIR = os.path.join(ROOT, "benchmark/phase3/runs/round48/digestion/work-xuanjie-r48/raw")
os.makedirs(LKDIR, exist_ok=True)
os.makedirs(XJDIR, exist_ok=True)

# --- Leikao 61-100 ---
subprocess.run(["pdftoppm", "-png", "-r", "130", "-f", "61", "-l", "100", LK,
                os.path.join(LKDIR, "lk")], check=True)
lk = sorted(glob.glob(os.path.join(LKDIR, "lk-*.png")))
assert len(lk) == 40, f"leikao pages {len(lk)} != 40"
# rename lk-061.png -> lk-61.png style consistent w/ R47 (lk-021..lk-060 no zero pad beyond 3)
print("leikao rendered:", len(lk), lk[0], lk[-1])

# --- Xuanjie: extract embedded images for ranges ---
def extract(first, last):
    pre = os.path.join(XJDIR, f"x{first}")
    subprocess.run(["pdfimages", "-png", "-f", str(first), "-l", str(last), "-p", XJ, pre], check=True)
    files = sorted(glob.glob(pre + "*.png")) + sorted(glob.glob(pre + "*.jpg")) + sorted(glob.glob(pre + "*.ppm")) + sorted(glob.glob(pre + "*.pbm"))
    return files

for rng in [(950, 1000), (1040, 1051)]:
    fs = extract(*rng)
    print("xuanjie extract", rng, "files:", len(fs), fs[:3])
    assert len(fs) > 0
print("OK")
