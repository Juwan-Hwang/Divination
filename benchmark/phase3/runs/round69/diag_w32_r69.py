import json, pathlib, statistics
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
fs = json.loads((base/"runs/round69/final-scores.json").read_text(encoding="utf-8"))
print("TOPKEYS", list(fs.keys()))
ana = fs.get("analysis_r69")
print("ANALYSIS_R69", json.dumps(ana, ensure_ascii=False, indent=2))
neg = json.loads((base/"runs/round69/diagnosis/lr-negatives-dev69.json").read_text(encoding="utf-8"))
print("NEG_META", neg.get("round"), neg.get("n_liuren_total"), neg.get("n_negative"), len(neg["negatives"]))
# means
def mean(vals): return sum(vals)/len(vals) if vals else None
all_d=[x["pair_diff"] for x in neg["negatives"]]
dev8=[x["pair_diff"] for x in neg["negatives"] if x["in_dev8"]]
non=[x["pair_diff"] for x in neg["negatives"] if not x["in_dev8"]]
print("MEANS merged_neg", mean(all_d), len(all_d))
print("MEANS dev8_neg", mean(dev8), len(dev8))
print("MEANS nondev8_neg", mean(non), len(non))
# provenance
for x in neg["negatives"]:
    cid=x["case_id"]
    p=base/f"inputs-dev12/{cid}.json"
    try:
        d=json.loads(p.read_text(encoding="utf-8"))
        book=(d.get("provenance") or {}).get("book")
    except Exception as e:
        book=f"ERR:{e}"
    fam="指南族" if (book and "大六壬占验指南" in book) else ("待核" if not book else "非指南族")
    print(f"ROW {cid}\t{x['in_dev8']}\t{x['pair_diff']}\t{fam}\t{book}")
# file sizes prior
import os
for rel in ["runs/round38/diagnosis/W-CHARTER.md","runs/round41/diagnosis/DIAG-LR-fresh-h16.md","runs/round68/diagnosis/DIAG-LR-weight-dev68.md","runs/round69/diagnosis/lr-negatives-dev69.json","runs/round69/final-scores.json"]:
    print("SIZE", rel, (base/rel).stat().st_size)
