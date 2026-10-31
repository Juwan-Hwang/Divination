#!/usr/bin/env python3
"""R73 W36 diagnosis seat: verify dual report, ours_axis2 consistency, per-case book source.
Only reads specified fields of final-scores.json: analysis_r73.round,
analysis_r73.families.liuren_dev8 / liuren_merged, top-level ours_axis2 (negative ids only).
Only reads provenance.book from inputs-dev12/<case_id>.json for negative ids.
Outputs summary to stdout only; writes no other file.
"""
import json, pathlib, statistics

base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
neg_path = base / "runs/round73/diagnosis/lr-negatives-dev73.json"
fs_path = base / "runs/round73/final-scores.json"
inputs = base / "inputs-dev12"

neg_doc = json.loads(neg_path.read_text(encoding="utf-8"))
negs = neg_doc["negatives"]
print("neg_round", neg_doc.get("round"), "n_liuren_total", neg_doc.get("n_liuren_total"), "n_negative", neg_doc.get("n_negative"), "len_negs", len(negs))

fs = json.loads(fs_path.read_text(encoding="utf-8"))
# Access only analysis_r73 specified subfields
a = fs.get("analysis_r73") or {}
print("analysis_round", a.get("round"))
fams = a.get("families") or {}
for key in ("liuren_dev8", "liuren_merged"):
    print(key, json.dumps(fams.get(key), ensure_ascii=False, sort_keys=True))

ours_axis2 = fs.get("ours_axis2") or {}
# ours_axis2 may be dict by case_id or list; normalize without reading other sections
def get_ours(cid):
    if isinstance(ours_axis2, dict):
        v = ours_axis2.get(cid)
        if isinstance(v, dict):
            # try common keys
            for k in ("ours", "score", "total", "value"):
                if k in v:
                    return v[k]
            return v
        return v
    if isinstance(ours_axis2, list):
        for item in ours_axis2:
            if isinstance(item, dict) and item.get("case_id") == cid:
                for k in ("ours", "score", "total", "value"):
                    if k in item:
                        return item[k]
                return item
    return None

mismatch = []
for n in negs:
    cid = n["case_id"]
    ov = get_ours(cid)
    # ov may be dict still; compare numeric if possible
    try:
        ok = float(ov) == float(n["ours"])
    except Exception:
        ok = False
        print("ours_unparsed", cid, repr(ov), "neg_ours", n["ours"])
    if not ok:
        mismatch.append((cid, ov, n["ours"]))
print("ours_axis2_type", type(ours_axis2).__name__, "ours_axis2_len", len(ours_axis2) if hasattr(ours_axis2, "__len__") else None)
print("ours_mismatch_count", len(mismatch), mismatch)

# subset means from negative list pair_diff
def mean(vals):
    return sum(vals)/len(vals) if vals else None
all_pd = [n["pair_diff"] for n in negs]
dev_pd = [n["pair_diff"] for n in negs if n["in_dev8"]]
non_pd = [n["pair_diff"] for n in negs if not n["in_dev8"]]
print("neg_mean_all", round(mean(all_pd), 6), len(all_pd))
print("neg_mean_dev8", round(mean(dev_pd), 6), len(dev_pd))
print("neg_mean_nondev8", round(mean(non_pd), 6), len(non_pd))
print("neg_dev8_count", len(dev_pd), "neg_nondev8_count", len(non_pd))

# per-case book
counts = {"guide": 0, "non_guide": 0, "pending": 0}
counts_dev = {"guide": 0, "non_guide": 0, "pending": 0}
counts_non = {"guide": 0, "non_guide": 0, "pending": 0}
for n in negs:
    cid = n["case_id"]
    p = inputs / f"{cid}.json"
    doc = json.loads(p.read_text(encoding="utf-8"))
    prov = doc.get("provenance") or {}
    book = prov.get("book")
    if book is None or (isinstance(book, str) and book.strip() == ""):
        fam = "pending"
    elif "大六壬占验指南" in str(book):
        fam = "guide"
    else:
        fam = "non_guide"
    counts[fam] += 1
    (counts_dev if n["in_dev8"] else counts_non)[fam] += 1
    print("CASE", cid, n["tradition"], n["in_dev8"], n["ours"], n["master"], n["pair_diff"], fam, json.dumps(book, ensure_ascii=False))
print("counts_all", counts)
print("counts_dev8neg", counts_dev)
print("counts_nondev8neg", counts_non)
