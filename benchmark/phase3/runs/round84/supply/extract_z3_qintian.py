import subprocess, os
base="/home/hatch/workspace/divination/incoming/wanted-books-6/Book"
outdir="/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply"
files={
 "A_zhengjie":"紫微斗数命理学正解 (许铨仁著).pdf",
 "B_qintian":"钦天四化紫微斗数命理学 (许铨仁讲述).pdf",
 "C_liuxuan":"紫微六玄经脉 钦天四化秘仪在华山 (蔡明宏著).pdf",
 "D_chuangzuo":"紫微斗数的创作原理 十八飞星与十天干四化 (谢昕润述).pdf",
 "E_lingdonglai":"紫微斗数命理学 (令东来编著).pdf",
}
for key,f in files.items():
    p=os.path.join(base,f)
    out=os.path.join(outdir,f"z3_{key}.txt")
    subprocess.run(["pdftotext","-layout",p,out],check=True)
    data=open(out,encoding="utf-8",errors="replace").read()
    pages=data.split("\f")
    nonspace=sum(1 for c in data if not c.isspace())
    print(key,"chars",len(data),"nonspace",nonspace,"pagesplit",len(pages))
