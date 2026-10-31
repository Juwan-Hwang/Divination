#!/usr/bin/env python3
"""R76 shijianguo full-book OCR pass v2 (parallel, per-page timeout).
OCR is a search/navigation aid only; verbatim quotations are visually verified separately."""
import subprocess, os, sys
from concurrent.futures import ThreadPoolExecutor
D = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(D, "shijianguo-r76.djvu")
OUTDIR = os.path.join(D, "sg-ocr-pages")
os.makedirs(OUTDIR, exist_ok=True)

def ocr_page(p):
    txtbase = os.path.join(OUTDIR, f"sgocr-p{p:03d}")
    txt = txtbase + ".txt"
    if os.path.exists(txt) and os.path.getsize(txt) > 50:
        return (p, "skip")
    ppm = os.path.join(OUTDIR, f"tmp-p{p:03d}.ppm")
    png = os.path.join(OUTDIR, f"tmp-p{p:03d}.png")
    try:
        subprocess.run(["ddjvu", "-format=ppm", f"-page={p}", "-size=1100x1550", SRC, ppm],
                       check=True, timeout=120, capture_output=True)
        subprocess.run(["python3", "-c", f"from PIL import Image; Image.open('{ppm}').convert('L').save('{png}')"],
                       check=True, timeout=60, capture_output=True)
        subprocess.run(["tesseract", png, txtbase, "-l", "chi_sim", "--psm", "6"],
                       check=True, timeout=180, capture_output=True)
        return (p, "ok")
    except Exception as e:
        return (p, f"FAIL {type(e).__name__}")
    finally:
        for f in (ppm, png):
            if os.path.exists(f):
                os.remove(f)

start = int(sys.argv[1]) if len(sys.argv) > 1 else 1
end = int(sys.argv[2]) if len(sys.argv) > 2 else 433
with ThreadPoolExecutor(max_workers=3) as ex:
    for p, status in ex.map(ocr_page, range(start, end + 1)):
        if status != "skip":
            print(p, status, flush=True)
print("range complete", start, end, flush=True)
