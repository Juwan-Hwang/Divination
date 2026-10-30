#!/usr/bin/env python3
"""R52 leikao C48/C51 page render - unique script for this task only."""
import subprocess, pathlib
pdf = pathlib.Path.home() / "workspace/divination/incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf"
outdir = pathlib.Path(__file__).parent / "leikao_r52_pages"
outdir.mkdir(exist_ok=True)
for p in (199, 204, 205):
    prefix = outdir / f"p{p}"
    subprocess.run(["pdftoppm", "-png", "-r", "300", "-f", str(p), "-l", str(p), str(pdf), str(prefix)], check=True)
    print(f"rendered {p}")
print(list(outdir.iterdir()))
