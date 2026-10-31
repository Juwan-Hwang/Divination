import json, math, statistics, collections, pathlib
p = pathlib.Path(__file__).with_name("lr-negatives-dev89.json")
d = json.loads(p.read_text())
negs = d["negatives"]
assert d["n_negative"] == len(negs) == 26 and d["n_liuren_total"] == 30
for n in negs:
    assert abs((n["ours"]-n["master"]) - n["pair_diff"]) < 1e-9, n["case_id"]
print("self-consistent 26/26")
# prior labels: from dev88 sec2 table, plus h16 sec2.1 dev-side for re-entering OC-026/LR3-110/LR3-114
labels = {
 "LR2-013":"D","LR2-014":"W*","LR2-015":"E","LR2-016":"D","LR2-017":"E",
 "LR2-019":"E","LR2-021":"A*","LR2-022":"W*","LR2-023":"W*","LR2-024":"C*",
 "OC-026":"E","OC-027":"W*","OC-029":"E","OC-030":"A",
 "LR3-002":"E","LR3-006":"C*","LR3-008":"D","LR3-101":"W*","LR3-107":"A",
 "LR3-110":"E","LR3-112":"H","LR3-114":"C*","LR3-116":"A",
}
unc = {"LR3-010"}
unlab = {"LR2-018","LR3-104"}
ids = {n["case_id"] for n in negs}
assert set(labels)|unc|unlab == ids, (ids - set(labels) - unc - unlab, (set(labels)|unc|unlab)-ids)
def seg(pred):
    s=[n for n in negs if pred(n)]
    diffs=[n["pair_diff"] for n in s]
    print(f"n={len(s)} sum={sum(diffs):.2f} mean={sum(diffs)/len(diffs):.3f} median={statistics.median(diffs):.3f}")
print("dev8:"); seg(lambda n: n["in_dev8"])
print("LR3:"); seg(lambda n: not n["in_dev8"])
print("merged:"); seg(lambda n: True)
for name, pred in [("dev8", lambda n: n["in_dev8"]), ("LR3", lambda n: not n["in_dev8"]), ("merged", lambda n: True)]:
    s=[n for n in negs if pred(n)]
    lab=[n for n in s if n["case_id"] in labels]
    cnt=collections.Counter(labels[n["case_id"]] for n in lab)
    w=cnt.get("W*",0)
    print(name, "neg_n=",len(s), "labelled_n=",len(lab), dict(sorted(cnt.items())))
    for denom_n, denom in [(len(s),"neg"),(len(lab),"labelled")]:
        if w:
            pr=w/denom_n; se=math.sqrt(pr*(1-pr)/denom_n)*100
            print(f"  W interface {w}/{denom_n} ({denom}) = {pr*100:.1f}% SE {se:.1f}pp")
        else:
            print(f"  W interface 0/{denom_n} ({denom}) = 0.0%")
    print("  W hardcore 0")
# composition diff vs dev88 id set (from dev88 sec1/2)
prev88 = {"LR-001","LR2-013","LR2-014","LR2-015","LR2-016","LR2-017","LR2-018","LR2-019","LR2-021","LR2-022","LR2-023","LR2-024","OC-027","OC-029","OC-030","LR3-002","LR3-006","LR3-008","LR3-010","LR3-101","LR3-104","LR3-107","LR3-112","LR3-116"}
print("entering vs dev88:", sorted(ids-prev88))
print("leaving vs dev88:", sorted(prev88-ids))
print("D main labelled:", [n["case_id"] for n in negs if labels.get(n["case_id"])=="D"])
