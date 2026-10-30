import re, json, sys
SRC="/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/work-yijian-r50/yijian-text-lines.txt"
raw=open(SRC,encoding="utf-8",errors="replace").read().splitlines()
def content(i):
    l=raw[i-1]
    m=re.match(r"^\d+\t(.*)$", l)
    return m.group(1) if m else l.strip()
want=[int(x) for x in sys.argv[1:]]
entries=json.load(open("/home/hatch/workspace/divination/benchmark/phase3/runs/round52/entries-r52.json",encoding="utf-8"))
by={e["fl_title"]:e for e in entries}
# headers for vol
hdrs=[(i,content(i).strip()) for i in range(132,2482) if re.match(r"^夷坚[甲乙丙丁]志卷第.*事$", content(i).strip())]
def vol_of(fl):
    v=""
    for h,t in hdrs:
        if h<fl: v=t
        else: break
    return v
for fl in want:
    e=by[fl]
    print(f"\n===== L{fl} [{vol_of(fl)}] 《{e['title']}》 body L{fl+1} len {e['blen']} =====")
    print(e["body"])
