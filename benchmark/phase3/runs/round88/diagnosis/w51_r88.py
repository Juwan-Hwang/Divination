# W51 R88 recomputation script (unique file for this round)
# Inputs (allowed only):
#  - round88 lr-negatives-dev88.json (scores)
#  - prior labels transcribed verbatim from round87 DIAG-LR-weight-dev87.md
#    section 2 table and section 1 composition-difference list (style-reference file)
#  - LR3-010 UNC per task instruction (maintain original, no re-coding)
import json, math, statistics

SRC = "/home/hatch/workspace/divination/benchmark/phase3/runs/round88/diagnosis/lr-negatives-dev88.json"
data = json.load(open(SRC, encoding="utf-8"))
negs = data["negatives"]
assert data["n_negative"] == len(negs) == 24, (data["n_negative"], len(negs))
print("n_liuren_total(declared)=", data["n_liuren_total"], " n_negative=", len(negs))

# self-consistency: pair_diff == ours - master
bad = []
for c in negs:
    if abs((c["ours"] - c["master"]) - c["pair_diff"]) > 1e-9:
        bad.append(c["case_id"])
print("pair_diff self-consistency: %d/%d ok, bad=%s" % (len(negs) - len(bad), len(negs), bad))
assert not bad

# prior labels from dev87 file (section 2 table; section 1 leaving list)
labels = {
    "LR2-013": "D", "LR2-014": "W*", "LR2-015": "E", "LR2-016": "D",
    "LR2-017": "E", "LR2-019": "E", "LR2-021": "A*", "LR2-023": "W*",
    "LR2-024": "C*", "LR3-002": "E", "LR3-006": "C*", "LR3-008": "D",
    "LR3-101": "W*", "LR3-107": "A", "LR3-116": "A",
    "OC-027": "W*", "OC-029": "E", "OC-030": "A",
    "LR2-022": "W*",   # dev87 sec.1 leaving list: LR2-022 (W*)
    "LR3-112": "H",    # dev87 sec.1 leaving list: LR3-112 (H)
}
unc = {"LR3-010"}  # per task instruction, UNC maintained

def seg(c):
    return "dev8" if c["in_dev8"] else "LR3"

for name, subset in [("dev8", [c for c in negs if c["in_dev8"]]),
                     ("LR3", [c for c in negs if not c["in_dev8"]]),
                     ("merged", negs)]:
    diffs = [c["pair_diff"] for c in subset]
    print("%s: n=%d sum=%.2f mean=%.3f median=%.3f" %
          (name, len(subset), sum(diffs), sum(diffs)/len(diffs), statistics.median(diffs)))

for name, subset in [("dev8", [c for c in negs if c["in_dev8"]]),
                     ("LR3", [c for c in negs if not c["in_dev8"]]),
                     ("merged", negs)]:
    lab = [c for c in subset if c["case_id"] in labels]
    w_int = [c for c in lab if labels[c["case_id"]].startswith("W")]
    d_main = [c for c in lab if labels[c["case_id"]] == "D"]
    unl = [c["case_id"] for c in subset if c["case_id"] not in labels and c["case_id"] not in unc]
    uncl = [c["case_id"] for c in subset if c["case_id"] in unc]
    print("%s: neg_n=%d labelled=%d UNC=%s unlabelled_in_allowed_inputs=%s" %
          (name, len(subset), len(lab), uncl, unl))
    print("   W-interface=%d  hard-core=0  D-main=%d" % (len(w_int), len(d_main)))
    for denom_label, denom in [("neg_n", len(subset)), ("labelled_n", len(lab))]:
        if denom:
            p = len(w_int) / denom
            se = math.sqrt(p * (1 - p) / denom) * 100
            print("   W share by %s=%d: %.1f%% (SE %.1f pp)" % (denom_label, denom, p * 100, se))

# label distribution over labelled cases
from collections import Counter
cnt = Counter(labels[c["case_id"]] for c in negs if c["case_id"] in labels)
print("label distribution (labelled only):", dict(sorted(cnt.items())))
dev8_ids = [c["case_id"] for c in negs if c["in_dev8"]]
lr3_ids = [c["case_id"] for c in negs if not c["in_dev8"]]
print("dev8 ids:", dev8_ids)
print("LR3 ids:", lr3_ids)
# overlap with dev87 list (19 ids in its sec.2 table)
dev87_ids = ["LR2-013","LR2-014","LR2-015","LR2-016","LR2-017","LR2-019","LR2-021",
             "LR2-023","LR2-024","LR3-002","LR3-006","LR3-008","LR3-101","LR3-107",
             "LR3-116","OC-026","OC-027","OC-029","OC-030"]
cur = {c["case_id"] for c in negs}
print("entered vs dev87 table:", sorted(cur - set(dev87_ids)))
print("left vs dev87 table:", sorted(set(dev87_ids) - cur))
