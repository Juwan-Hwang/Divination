#!/usr/bin/env python3
"""R49 leikao cont: render PDF 101-144 (skipping 110,130,140? no - include all, mark skips in register).
Actually targets: 101-109,111-129,131-144 = 42 pages. 110,130 are R46-sampled, excluded.
Assertions included."""
import subprocess, os
PDF = "/home/hatch/workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round49/digestion/work-leikao-r49"
assert os.path.isfile(PDF), "pdf missing"
info = subprocess.run(["pdfinfo", PDF], capture_output=True, text=True).stdout
pages = int([l for l in info.splitlines() if l.startswith("Pages:")][0].split()[1])
assert pages == 438, f"expected 438 pages, got {pages}"
os.makedirs(OUT, exist_ok=True)
targets = list(range(101,110)) + list(range(111,130)) + list(range(131,145))
assert len(targets) == 42, len(targets)
# also render PDF 100 for cross-page head check (not counted)
extra = [100]
for p in targets + extra:
    assert 1 <= p <= 438
    prefix = os.path.join(OUT, f"lk-{p:03d}")
    out_png = prefix + f"-{p}.png"
    # pdftoppm naming: prefix-pagenum.png ; check existence skip if present
    r = subprocess.run(["pdftoppm","-png","-r","130","-f",str(p),"-l",str(p),PDF,prefix], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[:500]
files = sorted(os.listdir(OUT))
print("OK pages=438 rendered count:", len(files), files[:5], files[-5:])
assert len(files) >= 43, f"rendered {len(files)}"
