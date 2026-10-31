import json, math, statistics, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg = json.loads((base/"runs/round87/diagnosis/lr-negatives-dev87.json").read_text())
labels = {
 "LR2-013": ("D",""), "LR2-014": ("W*","W-face; W<->C"),
 "LR2-015": ("E","same-sign; W note only"), "LR2-016": ("D","W<->magnitude note only"),
 "LR2-017": ("E",""), "LR2-019": ("E",""),
 "LR2-021": ("A*","MW/SEAT; A<->B"), "LR2-023": ("W*","W-face; W<->D/E"),
 "LR2-024": ("C*",""),
 "LR3-002": ("E","A secondary cand GZ/SEAT"), "LR3-006": ("C*",""),
 "LR3-008": ("D",""), "LR3-101": ("W*","W-face; W<->A/C"),
 "LR3-107": ("A","SF/SEAT"), "LR3-116": ("A","QX/SEAT"),
 "OC-026": ("E","same-sign note"), "OC-027": ("W*","W-name; W<->C"),
 "OC-029": ("E","A secondary cand MW/MIX"), "OC-030": ("A","SF/SEAT"),
}
rows=[]
for n in neg["negatives"]:
    cid=n["case_id"]
    assert abs((n["ours"]-n["master"]) - n["pair_diff"])<1e-9, cid
    card=json.loads((base/f"inputs-dev12/{cid}.json").read_text())
    book = card.get("provenance",{}).get("book")
    seg = "dev8" if n["in_dev8"] else "LR3"
    lab,note = labels[cid]
    rows.append({**n,"segment":seg,"label":lab,"note":note,"book":book})
    print(cid, seg, n["pair_diff"], lab, "|", book)
def agg(rs, name):
    from collections import Counter
    c=Counter(r["label"].rstrip("*") for r in rs)
    diffs=[r["pair_diff"] for r in rs]
    w=sum(1 for r in rs if r["label"].startswith("W"))
    hard=sum(1 for r in rs if r["label"]=="W")
    se=lambda k,n: math.sqrt((k/n)*(1-k/n)/n)*100 if n else 0
    print(f"\n{name} n={len(rs)} counts={dict(c)} sum={sum(diffs):.2f} mean={statistics.mean(diffs):.3f} median={statistics.median(diffs):.3f}")
    print(f" W interface {w} = {w/len(rs)*100:.1f}% SE {se(w,len(rs)):.1f}pp ; hardcore {hard}")
    print(f" E {c.get('E',0)} = {c.get('E',0)/len(rs)*100:.1f}% ; A+C {c.get('A',0)+c.get('C',0)} = {(c.get('A',0)+c.get('C',0))/len(rs)*100:.1f}%")
for seg in ["dev8","LR3"]:
    agg([r for r in rows if r["segment"]==seg], seg)
agg(rows,"combined")
from collections import Counter
print("\nbooks:", Counter(r["book"] for r in rows))
print("guide count:", sum(1 for r in rows if r["book"] and "指南" in r["book"]))
