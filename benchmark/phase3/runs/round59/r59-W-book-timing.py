import json, pathlib, statistics
base = pathlib.Path("/home/hatch/workspace/divination")
neg = json.load(open(base/"benchmark/phase3/runs/round59/diagnosis/lr-negatives-dev59.json"))
fs = json.load(open(base/"benchmark/phase3/runs/round59/final-scores.json"))
ours_sub = fs["ours_sub"]
rows=[]
for n in neg["negatives"]:
    cid=n["case_id"]
    card=json.load(open(base/f"benchmark/phase3/inputs-dev12/{cid}.json"))
    book=card.get("provenance",{}).get("book")
    fam="指南族" if (book and "大六壬占验指南" in book) else "非指南族"
    timing=ours_sub.get(cid,{}).get("timing")
    total=ours_sub.get(cid,{}).get("total")
    rows.append({**n,"book":book,"family":fam,"timing":timing,"ours_sub_total":total})
for r in rows:
    print(r)
def mean(xs): return sum(xs)/len(xs) if xs else None
print("neg mean merged", mean([r["pair_diff"] for r in rows]), len(rows))
print("neg mean dev8", mean([r["pair_diff"] for r in rows if r["in_dev8"]]), sum(1 for r in rows if r["in_dev8"]))
print("neg mean nondev8", mean([r["pair_diff"] for r in rows if not r["in_dev8"]]), sum(1 for r in rows if not r["in_dev8"]))
print("family counts", {f: sum(1 for r in rows if r["family"]==f) for f in set(r["family"] for r in rows)})
print("family dev8", {f: sum(1 for r in rows if r["family"]==f and r["in_dev8"]) for f in set(r["family"] for r in rows)})
print("family nondev8", {f: sum(1 for r in rows if r["family"]==f and not r["in_dev8"]) for f in set(r["family"] for r in rows)})
# timing
for label, subset in [("merged", rows), ("dev8", [r for r in rows if r["in_dev8"]]), ("nondev8", [r for r in rows if not r["in_dev8"]])]:
    print(label, "timing mean", mean([r["timing"] for r in subset]), "n", len(subset))
    print(label, "timing=0", [r["case_id"] for r in subset if r["timing"]==0])
    print(label, "0<t<1", [(r["case_id"], r["timing"]) for r in subset if 0<r["timing"]<1])
    print(label, "t=1", [r["case_id"] for r in subset if r["timing"]==1.0])
    print(label, "t>1", [(r["case_id"], r["timing"]) for r in subset if r["timing"]>1])
print(json.dumps(rows, ensure_ascii=False, indent=1))
