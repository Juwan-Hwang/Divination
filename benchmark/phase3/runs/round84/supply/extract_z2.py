import subprocess, os
base="/home/hatch/workspace/divination/incoming/wanted-books-6/Book"
outdir="/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply"
files={
 "A_chuji":"中州派紫微斗数初级讲义 (王亭之).pdf",
 "B_shenzao_xia":"中州派紫微斗数深造讲义 下 (王亭之).pdf",
 "C_lubin":"陆斌兆紫微斗数讲义评注 (陆斌兆原著；王亭之评注).pdf",
 "D_gufa":"紫微斗数古法群内部讲义 (古法群).pdf",
}
for key,f in files.items():
    p=os.path.join(base,f)
    out=os.path.join(outdir,f"z2_{key}.txt")
    # pdftotext with page breaks preserved (default inserts \f)
    subprocess.run(["pdftotext","-layout",p,out],check=True)
    data=open(out,encoding="utf-8",errors="replace").read()
    pages=data.split("\f")
    print(key, "chars",len(data),"pagesplit",len(pages))
