#!/usr/bin/env python3
"""R50 W monitoring round13 extraction. Assertions on counts."""
import json, pathlib
ROOT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round50")
BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg = json.loads((ROOT/"diagnosis/lr-negatives-dev50.json").read_text())
assert neg["round"]==50 and neg["n_liuren_total"]==30 and neg["n_negative"]==24, neg.keys()
neg_ids = [x["case_id"] for x in neg["negatives"]]
assert len(neg_ids)==24 and len(set(neg_ids))==24
# total 30 ids: from host-meta tradition liuren/六壬
host = json.loads((ROOT/"judging/host-meta.json").read_text())
total_ids = [k for k,v in host.items() if v.get("tradition") in ("liuren","六壬")]
assert len(total_ids)==30, (len(total_ids), total_ids)
assert set(neg_ids) <= set(total_ids)
nonneg = [i for i in total_ids if i not in neg_ids]
assert len(nonneg)==6, nonneg
fs = json.loads((ROOT/"final-scores.json").read_text())
# analysis keys search
def find(obj, path=""):
    if isinstance(obj, dict):
        for k,v in obj.items():
            if "liuren" in str(k).lower() or "analysis" in str(k).lower():
                print("KEY", path+"/"+str(k), str(v)[:500])
            find(v, path+"/"+str(k))
print("TOTAL30", sorted(total_ids))
print("NONNEG6", sorted(nonneg))
print("NEG dev8", sum(1 for x in neg["negatives"] if x["in_dev8"]), "LR3", sum(1 for x in neg["negatives"] if not x["in_dev8"]))
s=sum(x["pair_diff"] for x in neg["negatives"]); print("neg mean combined", s/24, s)
for flag in (True, False):
    sub=[x for x in neg["negatives"] if x["in_dev8"]==flag]
    print("neg mean in_dev8=",flag, sum(x["pair_diff"] for x in sub)/len(sub), len(sub))
find(fs)
outm = json.loads((ROOT/"judging/outcome-manifest.json").read_text())
cases = outm["cases"]
assert set(total_ids) <= set(cases.keys())
out_path = ROOT/"diagnosis/w13-extract-r50.txt"
lines=[]
for cid in sorted(total_ids):
    pred = json.loads((ROOT/f"predictions/{cid}.json").read_text())
    inp = json.loads((BASE/f"inputs-dev12/{cid}.json").read_text())
    book = inp.get("provenance",{}).get("book","")
    oc = cases[cid]
    oc_text = oc if isinstance(oc,str) else json.dumps(oc, ensure_ascii=False)
    lines.append(f"\n===== {cid} in_dev8={host[cid].get('in_dev8')} neg={cid in neg_ids} pair={[x['pair_diff'] for x in neg['negatives'] if x['case_id']==cid]} ours_sub={fs.get('ours_sub',{}).get(cid)} book={book} =====")
    lines.append("PRED_KEYS: "+",".join(pred.keys()))
    lines.append("PREDICTION_TEXT: "+str(pred.get("prediction_text","")))
    lines.append("BASIS: "+str(pred.get("basis","")))
    # other pred fields that might carry text
    for k,v in pred.items():
        if k not in ("prediction_text","basis","case_id"):
            lines.append(f"PRED_{k}: {v}")
    lines.append("OUTCOME: "+oc_text[:4000])
out_path.write_text("\n".join(lines), encoding="utf-8")
print("wrote", out_path, len(lines))
