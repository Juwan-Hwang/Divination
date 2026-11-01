#!/usr/bin/env python3
import subprocess, os
src = "/home/hatch/workspace/divination/incoming/wanted-books-6/Book/紫微六玄经脉 钦天四化秘仪在华山 (蔡明宏著).pdf"
outdir = "/home/hatch/workspace/divination/benchmark/phase3/runs/round96/supply/pages-caiminghong-r96/hires"
pages = list(range(519,526)) + list(range(527,534)) + list(range(535,547))
for p in pages:
    out = os.path.join(outdir, f"cmh-{p:03d}")
    target = out + ".png"
    if os.path.exists(target):
        print("reuse", target, os.path.getsize(target)); continue
    subprocess.run(["pdftoppm","-png","-r","250","-f",str(p),"-l",str(p),"-singlefile",src,out],check=True)
    print("made", target, os.path.getsize(target))
