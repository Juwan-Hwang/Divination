#!/usr/bin/env python3
"""R76 shijianguo DjVu page renderer: ddjvu ppm -> PNG via Pillow. Usage: render-shijianguo-r76.py START END [W H]"""
import sys, subprocess, os
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(D, "shijianguo-r76.djvu")
start, end = int(sys.argv[1]), int(sys.argv[2])
w = sys.argv[3] if len(sys.argv) > 3 else "1100"
h = sys.argv[4] if len(sys.argv) > 4 else "1550"
for p in range(start, end + 1):
    ppm = os.path.join(D, f"sg-p{p:03d}.ppm")
    png = os.path.join(D, f"sg-p{p:03d}.png")
    if os.path.exists(png):
        continue
    subprocess.run(["ddjvu", f"-format=ppm", f"-page={p}", f"-size={w}x{h}", SRC, ppm], check=True)
    Image.open(ppm).save(png)
    os.remove(ppm)
    print("done", p)
