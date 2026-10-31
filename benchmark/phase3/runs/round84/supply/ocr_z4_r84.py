#!/usr/bin/env python3
import subprocess, os, glob
B="/home/hatch/workspace/divination/incoming/wanted-books-6/Book"
W="/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply/ocr_z4_r84"
os.makedirs(W,exist_ok=True)
books={
 "z4d_xinbian_up":"斗数命理新编 上 (张开卷著).pdf",
 "z4e_xinbian_dn":"斗数命理新编 下 (张开卷著).pdf",
 "z4f_mingyun":"紫微斗数命运分析 (徐曾生著).pdf",
 "z4g_gupiao":"紫微斗数股票战略 (陆在田著).pdf",
 "z4i_shouchao":"亲传紫微斗数手抄笔记 (陈政男).pdf",
}
for key,fn in books.items():
    src=os.path.join(B,fn)
    d=os.path.join(W,key); os.makedirs(d,exist_ok=True)
    if not glob.glob(os.path.join(d,"p-001.png")):
        subprocess.run(["pdftoppm","-png","-r","200",src,os.path.join(d,"p")],check=True)
    pages=sorted(glob.glob(os.path.join(d,"p-*.png")))
    out=[]
    for pg in pages:
        base=pg[:-4]
        if not os.path.exists(base+".txt"):
            subprocess.run(["tesseract",pg,base,"-l","chi_tra+chi_sim","--psm","6"],capture_output=True)
        out.append(open(base+".txt",encoding="utf-8",errors="replace").read() if os.path.exists(base+".txt") else "")
    dst=f"/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply/ocr_{key}_r84.txt"
    with open(dst,"w",encoding="utf-8") as f:
        for i,t in enumerate(out,1):
            f.write(f"\n===== PAGE {i} =====\n"+t)
    print(key,"pages",len(pages),"chars",sum(len(x) for x in out),flush=True)
print("DONE")
