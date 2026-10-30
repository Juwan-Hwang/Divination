#!/usr/bin/env python3
"""R50 leikao cont: render PDF 145-149,151-169,171-189 = 43 pages (skip 150,170 = R46-sampled per R49 unread list).
Also render PDF 144 for cross-page head check (not counted). Assertions included."""
import subprocess, os
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/work-leikao-r50"
assert os.path.isfile(PDF), "pdf missing"
info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
assert pages == 438, f"expected 438 pages, got {pages}"
os.makedirs(OUT, exist_ok=True)
targets = list(range(145,150)) + list(range(151,170)) + list(range(171,190))
assert len(targets) == 43, len(targets)
extra = [144]
for p in targets + extra:
    assert 1 <= p <= 438
    prefix = os.path.join(OUT, f"lk-{p:03d}")
    r = subprocess.run(["pdftoppm","-png","-r","130","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:500]
files = sorted(os.listdir(OUT))
print("OK pages=438 rendered count:", len(files), files[:3], files[-3:])
assert len(files) >= 44, f"rendered {len(files)}"
