import json, pathlib
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3"
fs = json.loads((base/"runs/round54/final-scores.json").read_text())
print("TOP KEYS", list(fs.keys()))
ana = fs.get("analysis_r54", {})
print("ANALYSIS KEYS", list(ana.keys()))
for k, v in ana.items():
    if k in ("headline", "families"):
        continue
    print(k, ":", json.dumps(v, ensure_ascii=False)[:2000])
print("--- families liuren ---")
for k, v in ana.get("families", {}).items():
    if "liuren" in k:
        print(k, v)
print("--- headline ---")
print(ana.get("headline"))
neg = json.loads((base/"runs/round54/diagnosis/lr-negatives-dev54.json").read_text())
print("neg n", neg["n_negative"], "total", neg["n_liuren_total"])
ids = [x["case_id"] for x in neg["negatives"]]
print(ids)
# timing subscores for negatives from ours_sub
for cid in ids:
    sub = fs.get("ours_sub", {}).get(cid)
    print(cid, "pair", [x["pair_diff"] for x in neg["negatives"] if x["case_id"]==cid], "sub", sub)
