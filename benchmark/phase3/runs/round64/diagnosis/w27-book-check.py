import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg = json.loads((base/"runs/round64/diagnosis/lr-negatives-dev64.json").read_text())
fs = json.loads((base/"runs/round64/final-scores.json").read_text())
a = fs.get("analysis_r64", {})
fam = a.get("families", {})
# Only the two readings authorised in the task
for k in ("liuren_dev8", "liuren_merged"):
    print(k, json.dumps(fam.get(k), ensure_ascii=False))
print("neg header", neg["round"], neg["n_liuren_total"], neg["n_negative"], len(neg["negatives"]))
# subset means from negatives list only
import statistics
for label, subset in [("all", neg["negatives"]), ("dev8", [x for x in neg["negatives"] if x["in_dev8"]]), ("nondev8", [x for x in neg["negatives"] if not x["in_dev8"]])]:
    print(label, len(subset), round(sum(x["pair_diff"] for x in subset)/len(subset), 4))
out=[]
for x in neg["negatives"]:
    cid=x["case_id"]
    card=json.loads((base/f"inputs-dev12/{cid}.json").read_text())
    book=card.get("provenance",{}).get("book")
    out.append({"case_id":cid,"tradition":x["tradition"],"in_dev8":x["in_dev8"],"pair_diff":x["pair_diff"],"ours":x["ours"],"master":x["master"],"book":book})
    print(cid, x["in_dev8"], x["pair_diff"], book)
guide=[o for o in out if o["book"] and "大六壬占验指南" in o["book"]]
print("guide", len(guide), "nonguide", len(out)-len(guide))
print("guide dev8", sum(1 for o in guide if o["in_dev8"]), "guide nondev8", sum(1 for o in guide if not o["in_dev8"]))
(base/"runs/round64/diagnosis/w27-book-results.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
