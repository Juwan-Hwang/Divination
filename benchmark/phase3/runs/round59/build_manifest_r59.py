#!/usr/bin/env python3
"""R59 host tooling: build runs/round59/judging/outcome-manifest.json.

Carry-note extraction follows the ADDENDUM-r57 s.1 fix: structured read of
the adjudication JSON + whole-line capture cross-verification against the
addendum markdown (first '：「' to LAST '」' on the suggestion line); any
mismatch aborts. No non-greedy truncation extraction.

Layers:
- cases payload verbatim from runs/round58 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched).
- _r59_carryover_notes_addendum NEW: R57 adjudication partial-upheld 29
  from data/case-annotations-r57.json (manifest_carry_suggestion),
  cross-verified 29/29 against data/manifest-carryover-r58-addendum.md
  (the R58 addendum assembly, effective from R59 per STAGE-SUMMARY-43).
  Note: LY-011 also appears in the _r58 layer with the same R57 text
  (early clarification carry); layers are separate fields, no merge.
No outcome strings changed; no scores touched.
"""
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round58/judging/outcome-manifest.json"
ANN57 = P3 / "data/case-annotations-r57.json"
ADD58 = P3 / "data/manifest-carryover-r58-addendum.md"
OUT = P3 / "runs/round59/judging/outcome-manifest.json"


def md_capture(md_path):
    out = {}
    text = md_path.read_text(encoding="utf-8")
    for block in re.split(r"\n### ", text)[1:]:
        head = block.splitlines()[0]
        mm = re.search(r"([A-Z]+\d*-\d+)", head)
        if not mm:
            continue
        cid = mm.group(1)
        for line in block.splitlines():
            if line.startswith("- 承接注记建议文本") and "：「" in line:
                i = line.index("：「") + 2
                j = line.rindex("」")
                assert j > i, f"unclosed note for {cid} in {md_path.name}"
                out[cid] = line[i:j]
                break
    return out


def json_notes(ann_path, dispositions):
    d = json.loads(ann_path.read_text(encoding="utf-8"))
    out = {}
    for a in d["annotations"]:
        if a["disposition"] in dispositions:
            assert a["manifest_carry_suggestion"], a["case_id"]
            out[a["case_id"]] = a["manifest_carry_suggestion"]
    return out


m = json.loads(SRC.read_text(encoding="utf-8"))
cases = dict(m["cases"])
assert len(cases) == 487
assert len(m["_r56_carryover_notes"]) == 29
assert len(m["_r57_carryover_notes_addendum"]) == 21
assert len(m["_r58_carryover_notes_addendum"]) == 17
assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert cases["LR2-016"] == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"

notes59 = json_notes(ANN57, {"部分成立"})
assert len(notes59) == 29, f"r57 partial = {len(notes59)}"
cap58 = md_capture(ADD58)
missing = [c for c in notes59 if c not in cap58]
assert not missing, f"missing in {ADD58.name}: {missing}"
mismatch = [c for c in notes59 if cap58[c] != notes59[c]]
assert not mismatch, f"md/json mismatch: {mismatch}"
for cid in notes59:
    assert cid in cases, f"note case {cid} not in manifest"

src_cases = json.loads(SRC.read_text(encoding="utf-8"))["cases"]
diffs = [c for c in src_cases if cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r59_carryover_notes_addendum"] = notes59
m["_r59_manifest_note"] = (
    "Built for R59 from runs/round58 manifest: cases payload verbatim for "
    "all 487 cases (LR2-016 split state preserved); prior layers preserved "
    "(_r56_carryover_notes 29, _r57_carryover_notes_addendum 21, "
    "_r58_carryover_notes_addendum 17); _r59_carryover_notes_addendum from "
    "data/case-annotations-r57.json partial-upheld 29 by structured read, "
    "cross-verified 29/29 verbatim-equal against "
    "data/manifest-carryover-r58-addendum.md whole-line captures. "
    "No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK r59 layer:", len(notes59))
