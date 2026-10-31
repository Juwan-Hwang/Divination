#!/usr/bin/env python3
import subprocess, os, sys
B="/home/hatch/workspace/divination/incoming/wanted-books-6/Book"
OUT="/home/hatch/workspace/divination/benchmark/phase3/runs/round84/supply"
books={
 "z4a_tianyi":"紫微斗数初级讲义 (天翼术数研究中心).pdf",
 "z4b_nanbei":"紫微斗数南北派断诀 (朱云山).pdf",
 "z4c_jingcheng":"紫微斗数精成 (大德山人编著).pdf",
 "z4d_xinbian_up":"斗数命理新编 上 (张开卷著).pdf",
 "z4e_xinbian_dn":"斗数命理新编 下 (张开卷著).pdf",
 "z4f_mingyun":"紫微斗数命运分析 (徐曾生著).pdf",
 "z4g_gupiao":"紫微斗数股票战略 (陆在田著).pdf",
 "z4h_shenme":"什么是紫微斗数 (王健).pdf",
 "z4i_shouchao":"亲传紫微斗数手抄笔记 (陈政男).pdf",
 "z4j_tianji":"天纪 紫微斗数听课笔记 (倪海厦讲授).pdf",
 "z4k_yuanli":"紫微斗数原理与宫位说明.pdf",
 "z4m_jicheng":"紫微斗数集成全书.pdf",
 "z4n_bainiang":"紫微白娘子喊你来学紫微斗数 (紫微白娘子).pdf",
}
for key,fn in books.items():
    src=os.path.join(B,fn); dst=os.path.join(OUT,f"txt_{key}_r84.txt")
    r=subprocess.run(["pdftotext","-layout",src,dst],capture_output=True,text=True)
    sz=os.path.getsize(dst) if os.path.exists(dst) else -1
    # count non-whitespace chars
    txt=open(dst,encoding="utf-8",errors="replace").read() if sz>=0 else ""
    nw=sum(1 for c in txt if not c.isspace())
    print(key, "bytes",sz,"nonws",nw, "rc",r.returncode, r.stderr[:100])
# docx
import docx
d=docx.Document(os.path.join(B,"紫微斗数诸星性情资料大全.docx"))
lines=[]
for p in d.paragraphs:
    if p.text.strip(): lines.append(p.text)
for t in d.tables:
    for row in t.rows:
        lines.append(" | ".join(c.text for c in row.cells))
open(os.path.join(OUT,"txt_z4l_xingqing_r84.txt"),"w",encoding="utf-8").write("\n".join(lines))
print("z4l_xingqing paras",len(d.paragraphs),"tables",len(d.tables),"lines",len(lines))
