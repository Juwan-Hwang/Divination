import json, pathlib
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3"
neg = json.loads((base/"runs/round54/diagnosis/lr-negatives-dev54.json").read_text())
for entry in neg["negatives"]:
    cid = entry["case_id"]
    p = base / f"inputs-dev12/{cid}.json"
    d = json.loads(p.read_text())
    prov = d.get("provenance", {})
    book = prov.get("book") if isinstance(prov, dict) else None
    print(f"{cid}\t{entry['tradition']}\t{entry['in_dev8']}\t{entry['pair_diff']}\t{book}")
# aggregates
import statistics
all_diffs = [x["pair_diff"] for x in neg["negatives"]]
dev8 = [x["pair_diff"] for x in neg["negatives"] if x["in_dev8"]]
non = [x["pair_diff"] for x in neg["negatives"] if not x["in_dev8"]]
print(f"neg merged n={len(all_diffs)} mean={sum(all_diffs)/len(all_diffs):.4f}")
print(f"neg dev8 n={len(dev8)} mean={sum(dev8)/len(dev8):.4f}")
print(f"neg non-dev8 n={len(non)} mean={sum(non)/len(non):.4f}")
# timing subscores from final-scores
fs = json.loads((base/"runs/round54/final-scores.json").read_text())
subs = fs["ours_sub"]
tim_all = [subs[x["case_id"]]["timing"] for x in neg["negatives"]]
tim_dev8 = [subs[x["case_id"]]["timing"] for x in neg["negatives"] if x["in_dev8"]]
tim_non = [subs[x["case_id"]]["timing"] for x in neg["negatives"] if not x["in_dev8"]]
print(f"timing ours mean merged neg {sum(tim_all)/len(tim_all):.4f} dev8 {sum(tim_dev8)/len(tim_dev8):.4f} non {sum(tim_non)/len(tim_non):.4f}")
print(f"timing==0 count merged {sum(1 for t in tim_all if t==0)} dev8 {sum(1 for t in tim_dev8 if t==0)} non {sum(1 for t in tim_non if t==0)}")
print(f"timing==2 count {sum(1 for t in tim_all if t==2)} ; timing<1 count {sum(1 for t in tim_all if t<1)}")
for x in neg["negatives"]:
    cid=x["case_id"]
    print(cid, subs[cid])
