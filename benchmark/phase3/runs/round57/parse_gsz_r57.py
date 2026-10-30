# R57 开采席解析脚本：把《六爻卦例说真》文字层按章/例切分，输出中间件供逐例核查（不作断、不评分）
import re, json
src = "/tmp/gsz57/full.txt"
t = open(src, encoding="utf-8").read()
# 章标题（正文，非目录）：行首 第X章 + 标题
chap_pat = re.compile(r'^\s*第([一二三四五六七八九十]+)章\s+(\S.*?)\s*$', re.M)
cn = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'十一':11,'十二':12,'十三':13,'十四':14,'十五':15,'十六':16,'十七':17,'十八':18}
chaps = []
for m in chap_pat.finditer(t):
    # 目录行含点线，跳过
    if '....' in m.group(0):
        continue
    chaps.append((m.start(), cn.get(m.group(1), m.group(1)), m.group(2).strip()))
ex_pat = re.compile(r'例([一二三四五六七八九十]+)')
exs = [m for m in ex_pat.finditer(t)]
print("chapters found:", len(chaps))
for c in chaps: print(c)
print("例 occurrences:", len(exs))
# 每例归属章 = 位置之前最后一个章标题；例序在章内递增重置
segs = []
cur_ch = None
for i, m in enumerate(exs):
    for c in chaps:
        if c[0] < m.start():
            cur_ch = c
    start = m.start()
    end = exs[i+1].start() if i+1 < len(exs) else len(t)
    # 若下一章标题在中间，截到章标题
    for c in chaps:
        if start < c[0] < end:
            end = c[0]
            break
    segs.append({"idx": i+1, "chapter": cur_ch[1] if cur_ch else None, "chapter_title": cur_ch[2] if cur_ch else "", "ex_label": m.group(0), "text": t[start:end]})
json.dump(segs, open("/tmp/gsz57/segs.json","w"), ensure_ascii=False, indent=1)
from collections import Counter
print(Counter(s["chapter"] for s in segs))
print("total segs:", len(segs))
for s in segs[:3]:
    print("=====", s["idx"], s["chapter"], s["ex_label"], len(s["text"]))
