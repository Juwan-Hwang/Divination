import json, os, statistics

P3 = "/home/hatch/workspace/divination/benchmark/phase3"
neg_path = P3 + "/runs/round72/diagnosis/lr-negatives-dev72.json"
fs_path = P3 + "/runs/round72/final-scores.json"

with open(neg_path, encoding="utf-8") as f:
    neg = json.load(f)
with open(fs_path, encoding="utf-8") as f:
    fs = json.load(f)

print("neg round:", neg.get("round"), "n_total:", neg.get("n_liuren_total"), "n_negative:", neg.get("n_negative"), "len:", len(neg["negatives"]))
print("fs top keys:", list(fs.keys()))
ana = fs.get("analysis_r72")
print("analysis_r72 type:", type(ana))
print("analysis_r72:", json.dumps(ana, ensure_ascii=False, indent=1)[:8000])

# verify ours_axis2 matches negatives ours
oa = fs.get("ours_axis2", {})
mismatch = []
for n in neg["negatives"]:
    cid = n["case_id"]
    if oa.get(cid) != n["ours"]:
        mismatch.append((cid, oa.get(cid), n["ours"]))
print("ours_axis2 mismatch vs negatives:", mismatch)

# subset means
negs = neg["negatives"]
def mean(xs):
    return sum(xs)/len(xs) if xs else None
all_d = [n["pair_diff"] for n in negs]
dev8 = [n for n in negs if n["in_dev8"]]
non = [n for n in negs if not n["in_dev8"]]
print("neg mean merged:", mean(all_d), "n=", len(all_d))
print("neg mean dev8:", mean([n["pair_diff"] for n in dev8]), "n=", len(dev8))
print("neg mean non-dev8:", mean([n["pair_diff"] for n in non]), "n=", len(non))

# book provenance per case
rows = []
counts = {"guide": 0, "nonguide": 0, "pending": 0}
counts_dev8 = {"guide": 0, "nonguide": 0, "pending": 0}
counts_non = {"guide": 0, "nonguide": 0, "pending": 0}
for n in negs:
    cid = n["case_id"]
    p = P3 + f"/inputs-dev12/{cid}.json"
    book = None
    exists = os.path.exists(p)
    if exists:
        with open(p, encoding="utf-8") as f:
            card = json.load(f)
        prov = card.get("provenance") or {}
        book = prov.get("book")
    if book is None or book == "":
        fam = "待核"; key="pending"
    elif "大六壬占验指南" in book:
        fam = "指南族"; key="guide"
    else:
        fam = "非指南族"; key="nonguide"
    counts[key]+=1
    if n["in_dev8"]:
        counts_dev8[key]+=1
    else:
        counts_non[key]+=1
    rows.append((cid, n["tradition"], n["in_dev8"], n["ours"], n["master"], n["pair_diff"], book, fam, exists))
    print(cid, "| dev8=", n["in_dev8"], "| diff=", n["pair_diff"], "| fam=", fam, "| book=", book, "| exists=", exists)
print("counts total:", counts)
print("counts dev8:", counts_dev8)
print("counts non-dev8:", counts_non)

# file sizes for prior / material files
for p in [
    P3+"/runs/round38/diagnosis/W-CHARTER.md",
    P3+"/runs/round41/diagnosis/DIAG-LR-fresh-h16.md",
    P3+"/runs/round71/diagnosis/DIAG-LR-weight-dev71.md",
    neg_path,
    fs_path,
]:
    print("size:", p, os.path.getsize(p))
