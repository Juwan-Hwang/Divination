#!/usr/bin/env python3
"""R54 leikao cont: render PDF 320-329,331-349,351-369,371-389,391-409,411-429,431-438 (113 pp)
plus confrontation page 290 (R46-sampled, not in denominator). Skip pattern every 20th (330,350,...430) = R46-sampled pattern carried from R52/R53."""
import subprocess, os
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round54/digestion/work-leikao-r54"
assert os.path.isfile(PDF), "pdf missing"
info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
assert pages == 438, f"expected 438 pages, got {pages}"
os.makedirs(OUT, exist_ok=True)
targets = (list(range(320,330)) + list(range(331,350)) + list(range(351,370)) +
           list(range(371,390)) + list(range(391,410)) + list(range(411,430)) +
           list(range(431,439)))
assert len(targets) == 113, len(targets)
extra = [290]
for p in targets + extra:
    assert 1 <= p <= 438
    prefix = os.path.join(OUT, f"lk-{p:03d}")
    r = subprocess.run(["pdftoppm","-png","-r","130","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:500]
files = sorted(os.listdir(OUT))
print("OK pages=438 rendered count:", len(files))
assert len(files) == 114, f"rendered {len(files)}"
