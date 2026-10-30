#!/usr/bin/env python3
"""R48 xuanjie rotate/dedupe: pdfimages output has md5-duplicate pairs per page; rotate -90 (clockwise) per R46 finding.
Writes view/pNNNN.png for PDF pages 950-1000 and 1040-1051. Assertions on counts."""
import os, glob, hashlib
from PIL import Image

RAW = "/home/hatch/workspace/divination/benchmark/phase3/runs/round48/digestion/work-xuanjie-r48/raw"
VIEW = "/home/hatch/workspace/divination/benchmark/phase3/runs/round48/digestion/work-xuanjie-r48/view"
os.makedirs(VIEW, exist_ok=True)

def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()

groups = {}
for f in sorted(glob.glob(os.path.join(RAW, "*.png"))):
    base = os.path.basename(f)
    # names like x950-950-000.png / x1040-1040-000.png : page = middle token
    parts = base.replace(".png", "").split("-")
    page = int(parts[1])
    groups.setdefault(page, []).append(f)

expect = list(range(950, 1001)) + list(range(1040, 1052))
missing = [p for p in expect if p not in groups]
assert not missing, f"missing pages: {missing}"
for p in expect:
    fs = groups[p]
    hashes = {md5(f) for f in fs}
    assert len(hashes) == 1, f"page {p}: {len(fs)} files, {len(hashes)} distinct hashes"
    im = Image.open(fs[0])
    im = im.rotate(-90, expand=True)
    im.save(os.path.join(VIEW, f"p{p}.png"))
print("rotated pages:", len(expect), "first/last:", expect[0], expect[-1])
print("OK")
