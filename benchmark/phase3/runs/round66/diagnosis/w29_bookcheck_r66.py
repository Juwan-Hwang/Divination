import json, os
base = "/home/hatch/workspace/divination/benchmark/phase3"
neg = json.load(open(f"{base}/runs/round66/diagnosis/lr-negatives-dev66.json"))
fs = json.load(open(f"{base}/runs/round66/final-scores.json"))
fam = fs["analysis_r66"]["families"]
out = {"neg_round_field": neg.get("round"), "fs_round_field": fs["analysis_r66"].get("round"),
       "liuren_dev8": fam["liuren_dev8"], "liuren_merged": fam["liuren_merged"],
       "rows": [], "means": {}}
negs = neg["negatives"]
def mean(xs): return round(sum(xs)/len(xs), 3) if xs else None
out["means"] = {
  "merged_neg": mean([r["pair_diff"] for r in negs]),
  "dev8_neg": mean([r["pair_diff"] for r in negs if r["in_dev8"]]),
  "nondev8_neg": mean([r["pair_diff"] for r in negs if not r["in_dev8"]]),
  "n_neg": len(negs),
  "n_dev8_neg": sum(1 for r in negs if r["in_dev8"]),
  "n_nondev8_neg": sum(1 for r in negs if not r["in_dev8"]),
}
for r in negs:
    p = f"{base}/inputs-dev12/{r['case_id']}.json"
    d = json.load(open(p))
    book = (d.get("provenance") or {}).get("book")
    out["rows"].append({**r, "book": book,
        "family": "指南族" if (book and "大六壬占验指南" in book) else ("待核" if not book else "非指南族")})
from collections import Counter
out["counts"] = dict(Counter(x["family"] for x in out["rows"]))
out["counts_dev8"] = dict(Counter(x["family"] for x in out["rows"] if x["in_dev8"]))
out["counts_nondev8"] = dict(Counter(x["family"] for x in out["rows"] if not x["in_dev8"]))
json.dump(out, open(f"{base}/runs/round66/diagnosis/w29_bookresults_r66.json","w"), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ("neg_round_field","fs_round_field","means","counts","counts_dev8","counts_nondev8")}, ensure_ascii=False, indent=1))
for x in out["rows"]:
    print(x["case_id"], "|", x["tradition"], "|", x["in_dev8"], "|", x["pair_diff"], "|", x["book"])
