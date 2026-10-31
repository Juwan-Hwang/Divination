import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg = json.loads((base/"runs/round92/diagnosis/lr-negatives-dev92.json").read_text())
om = json.loads((base/"runs/round92/judging/outcome-manifest.json").read_text())["cases"]
out = {}
for n in neg["negatives"]:
    cid = n["case_id"]
    pred = json.loads((base/f"runs/round92/predictions/{cid}.json").read_text())
    card = json.loads((base/f"inputs-dev12/{cid}.json").read_text())
    assert pred["prediction_text"] and pred["basis"]
    assert abs((n["ours"]-n["master"]) - n["pair_diff"]) < 1e-9, cid
    out[cid] = {
        "pair_diff": n["pair_diff"], "ours": n["ours"], "master": n["master"],
        "in_dev8": n["in_dev8"],
        "subject": card.get("subject"), "context": card.get("context"),
        "book": (card.get("provenance") or {}).get("book"),
        "prediction_text": pred["prediction_text"], "basis": pred["basis"],
        "outcome": om[cid],
    }
p = base/"runs/round92/diagnosis/w55_r92_extract.json"
p.write_text(json.dumps(out, ensure_ascii=False, indent=1))
print("wrote", p, len(out), "cases;", p.stat().st_size, "bytes")
s = sum(n["pair_diff"] for n in neg["negatives"])
print("neg sum", s, "mean", s/len(neg["negatives"]))
for seg in (True, False):
    sub = [n["pair_diff"] for n in neg["negatives"] if n["in_dev8"] is seg]
    print("in_dev8=", seg, "n=", len(sub), "sum=", sum(sub), "mean=", sum(sub)/len(sub))
