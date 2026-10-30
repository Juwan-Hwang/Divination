import re, json
SRC="/home/hatch/workspace/divination/benchmark/phase3/runs/round50/digestion/work-yijian-r50/yijian-text-lines.txt"
raw=open(SRC,encoding="utf-8",errors="replace").read().splitlines()
def content(i):
    l=raw[i-1]
    m=re.match(r"^\d+\t(.*)$", l)
    return m.group(1) if m else l.strip()
# track current volume header
vol=""
entries=[]
i=132
while i<=2481:
    c=content(i).strip()
    m=re.match(r"^夷坚([甲乙丙丁])志卷第(.+?)(\d+)事$", c)
    if m:
        vol=c
        i+=1
        continue
    # title candidate: short line, next line long
    if 0 < len(c) <= 20 and i+1<=2481:
        nxt=content(i+1).strip()
        # next should not be header and should be long body OR body could span? In this file body is single long line typically
        if len(nxt)>=40 and not re.match(r"^夷坚[甲乙丙丁]志卷第", nxt):
            # collect body: consecutive long lines until next title/header? Actually format alternates title/body single lines; but some bodies split in 2 lines (R51 note). Merge following lines that are long and not title-like until next short+long pattern is ambiguous.
            # Take just next line as body primary, plus if line i+2 is also long (>40) and i+3 is not... treat as continuation if i+2 length>40 and (i+3 missing or header) - simpler: body = nxt only; record next lines separately.
            entries.append({"fl_title":i,"fl_body":i+1,"vol":vol,"title":c,"body":nxt,"blen":len(nxt)})
            i+=2
            continue
    i+=1
print("entries parsed:",len(entries))
# save
json.dump(entries, open("/home/hatch/workspace/divination/benchmark/phase3/runs/round52/entries-r52.json","w",encoding="utf-8"), ensure_ascii=False)
for e in entries[:5]:
    print(e["fl_title"], e["vol"], e["title"], e["blen"])
