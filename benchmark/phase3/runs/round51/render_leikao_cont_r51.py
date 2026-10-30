#!/usr/bin/env python3
"""R51 leikao cont: render PDF 190-209, 211-229, 231-233 = 42 pages (skip 210, 230 = R46-sampled per R50 unread list).
Also render PDF 189 for cross-page head check (not counted). Assertions included."""
import subprocess, os
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round51/digestion/work-leikao-r51"
assert os.path.isfile(PDF), "pdf missing"
info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
assert pages == 438, f"expected 438 pages, got {pages}"
os.makedirs(OUT, exist_ok=True)
targets = list(range(190,210)) + list(range(211,230)) + list(range(231,234))
assert len(targets) == 42, len(targets)
extra = [189]
for p in targets + extra:
    assert 1 <= p <= 438
    prefix = os.path.join(OUT, f"lk-{p:03d}")
    r = subprocess.run(["pdftoppm","-png","-r","130","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:500]
files = sorted(os.listdir(OUT))
print("OK pages=438 rendered count:", len(files), files[:3], files[-3:])
assert len(files) >= 43, f"rendered {len(files)}"
