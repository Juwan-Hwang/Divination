#!/usr/bin/env python3
"""R48 leikao census: render candidate volume-head / sample pages. Assertions included."""
import subprocess, os, sys
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round48/digestion/work-leikao-census-r48"
assert os.path.isfile(PDF), "pdf missing"
info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
assert pages == 438, f"expected 438 pages, got {pages}"
os.makedirs(OUT, exist_ok=True)
# candidate pages: scan band for volume starts + samples across all volumes
targets = [61,65,70,75,80,85,105,115,120,125,135,140,155,160,180,185,195,200,215,220,225,235,240,255,260,275,280,295,300,315,320,335,340,355,360,375,380,395,400,415,420,425]
for p in targets:
    assert 1 <= p <= 438
    prefix = os.path.join(OUT, f"c{p:03d}")
    r = subprocess.run(["pdftoppm","-png","-r","110","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:500]
files = sorted(os.listdir(OUT))
assert len(files) >= len(targets), f"rendered {len(files)} < targets {len(targets)}"
print("OK pages=438 rendered:", files)
