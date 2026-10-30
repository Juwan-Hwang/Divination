#!/usr/bin/env python3
"""R53 leikao cont: render PDF 277-289, 291-309, 311-319 = 41 pages (skip 290, 310 = R46-sampled pattern).
Starts at 277 to resolve hanging '紫府瓊臺記' (starts PDF 276, continuation 277)."""
import subprocess, os
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round53/digestion/work-leikao-r53"
assert os.path.isfile(PDF), "pdf missing"
info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
assert pages == 438, f"expected 438 pages, got {pages}"
os.makedirs(OUT, exist_ok=True)
targets = list(range(277,290)) + list(range(291,310)) + list(range(311,320))
assert len(targets) == 41, len(targets)
for p in targets:
    assert 1 <= p <= 438
    prefix = os.path.join(OUT, f"lk-{p:03d}")
    r = subprocess.run(["pdftoppm","-png","-r","130","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:500]
files = sorted(os.listdir(OUT))
print("OK pages=438 rendered count:", len(files), files[:3], files[-3:])
assert len(files) == 41, f"rendered {len(files)}"
