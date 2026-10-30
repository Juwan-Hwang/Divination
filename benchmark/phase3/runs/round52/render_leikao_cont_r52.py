#!/usr/bin/env python3
"""R52 leikao cont: render PDF 234-249, 251-269, 271-276 = 41 pages (skip 250, 270 = R46-sampled).
Extra (not counted): 209, 210, 233 for hanging-item verification (PDF210 continuation, PDF233 head)."""
import subprocess, os
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round52/digestion/work-leikao-r52"
assert os.path.isfile(PDF), "pdf missing"
info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
assert pages == 438, f"expected 438 pages, got {pages}"
os.makedirs(OUT, exist_ok=True)
targets = list(range(234,250)) + list(range(251,270)) + list(range(271,277))
assert len(targets) == 41, len(targets)
extra = [209, 210, 233]
for p in targets + extra:
    assert 1 <= p <= 438
    prefix = os.path.join(OUT, f"lk-{p:03d}")
    r = subprocess.run(["pdftoppm","-png","-r","130","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:500]
files = sorted(os.listdir(OUT))
print("OK pages=438 rendered count:", len(files), files[:3], files[-3:])
assert len(files) >= 44, f"rendered {len(files)}"
