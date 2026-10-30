#!/usr/bin/env python3
"""R49 leikao S-1: render PDF 213-216 (target 214 = Qian Youzhu entry head) at 130dpi. Assertions included."""
import subprocess, os
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round49/digestion/work-leikao-s1-r49"
assert os.path.isfile(PDF), "pdf missing"
info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
assert pages == 438, f"expected 438 pages, got {pages}"
os.makedirs(OUT, exist_ok=True)
targets = [213, 214, 215, 216]
for p in targets:
    assert 1 <= p <= 438
    prefix = os.path.join(OUT, f"s1p{p:03d}")
    r = subprocess.run(["pdftoppm", "-png", "-r", "130", "-f", str(p), "-l", str(p), PDF, prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:500]
files = sorted(os.listdir(OUT))
assert len(files) >= len(targets), f"rendered {len(files)} < targets {len(targets)}"
print("OK pages=438 rendered:", files)
