import re, json, pathlib
SRC="/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/work-yijian-r50/yijian-text-lines.txt"
raw=open(SRC,encoding="utf-8",errors="replace").read().splitlines()
def content(i):
    l=raw[i-1]
    m=re.match(r"^\d+\t(.*)$", l)
    return m.group(1) if m else l.strip()
# print structure stats for body face 132-2481
rows=[]
for i in range(132,2482):
    c=content(i)
    rows.append((i,c))
# headers
for i,c in rows:
    if re.match(r"^夷坚[甲乙丙丁]志卷第.*事$", c.strip()):
        print("HDR",i,c.strip())
