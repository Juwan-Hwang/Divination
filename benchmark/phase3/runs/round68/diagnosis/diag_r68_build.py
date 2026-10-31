import json, pathlib, statistics
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg_path = base/"runs/round68/diagnosis/lr-negatives-dev68.json"
fs_path = base/"runs/round68/final-scores.json"
out_path = base/"runs/round68/diagnosis/diag_r68_results.json"

neg = json.loads(neg_path.read_text(encoding="utf-8"))
fs = json.loads(fs_path.read_text(encoding="utf-8"))
# only analysis_r68
ana = fs.get("analysis_r68")
result = {"analysis_r68": ana}
# extract liuren families if present
# also compute negative means
negs = neg["negatives"]
def mean(xs): return sum(xs)/len(xs) if xs else None
result["neg_counts"] = {"total": len(negs), "dev8": sum(1 for n in negs if n["in_dev8"]), "non_dev8": sum(1 for n in negs if not n["in_dev8"])}
result["means"] = {
 "merged_neg": mean([n["pair_diff"] for n in negs]),
 "dev8_neg": mean([n["pair_diff"] for n in negs if n["in_dev8"]]),
 "non_dev8_neg": mean([n["pair_diff"] for n in negs if not n["in_dev8"]]),
}
books=[]
for n in negs:
    cid=n["case_id"]
    p=base/f"inputs-dev12/{cid}.json"
    d=json.loads(p.read_text(encoding="utf-8"))
    book=d.get("provenance",{}).get("book")
    fam="指南族" if (book and "大六壬占验指南" in book) else ("待核" if not book else "非指南族")
    books.append({"case_id":cid,"tradition":n["tradition"],"in_dev8":n["in_dev8"],"pair_diff":n["pair_diff"],"book":book,"family":fam})
result["books"]=books
from collections import Counter
result["family_counts"]=dict(Counter(b["family"] for b in books))
result["family_counts_dev8"]=dict(Counter(b["family"] for b in books if b["in_dev8"]))
result["family_counts_non"]=dict(Counter(b["family"] for b in books if not b["in_dev8"]))
out_path.write_text(json.dumps(result,ensure_ascii=False,indent=1),encoding="utf-8")
print(json.dumps({"analysis_r68":ana,"neg_counts":result["neg_counts"],"means":result["means"],"family_counts":result["family_counts"],"family_dev8":result["family_counts_dev8"],"family_non":result["family_counts_non"]},ensure_ascii=False,indent=1))
for b in books: print(b["case_id"], b["family"], b["book"])
