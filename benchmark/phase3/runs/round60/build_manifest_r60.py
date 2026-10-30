#!/usr/bin/env python3
"""R60 host tooling: build runs/round60/judging/outcome-manifest.json.

Carry-note extraction follows the ADDENDUM-r57 s.1 fix: structured read of
the adjudication JSON + whole-line capture cross-verification against the
addendum markdown (first '：「' to LAST '」' on the suggestion line); any
mismatch aborts. No non-greedy truncation extraction.

Layers:
- cases payload verbatim from runs/round59 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched).
- _r60_carryover_notes_addendum_a NEW: R58 adjudication partial-upheld 14
  from data/case-annotations-r58.json (manifest_carry_suggestion),
  cross-verified 14/14 against data/manifest-carryover-r59-addendum.md
  (the R59 addendum assembly of R58 adjudications, effective from R60
  per STAGE-SUMMARY-44 / R59 REPORT s.4).
- _r60_carryover_notes_addendum_b NEW: R59 adjudication partial-upheld 20
  from data/case-annotations-r59.json (manifest_carry_suggestion),
  effective from R60 per R59 REPORT s.4. Upheld-8 are same-issue
  continuations already carried in earlier layers (per the r59 file's
  own _provenance: all 29 are continuations); unexamined-1 is YM-070
  (suspension maintained). No md addendum exists for r59 yet (the R60
  data seat compiles manifest-carryover-r60-addendum.md for R61), so
  cross-verification here is: counts block of the source JSON asserted
  equal to the R59 REPORT s.4 published distribution (8/20/0/1, total
  29) and every partial item asserted to carry a non-empty suggestion.
No outcome strings changed; no scores touched.
"""
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round59/judging/outcome-manifest.json"
ANN58 = P3 / "data/case-annotations-r58.json"
ADD59 = P3 / "data/manifest-carryover-r59-addendum.md"
ANN59 = P3 / "data/case-annotations-r59.json"
OUT = P3 / "runs/round60/judging/outcome-manifest.json"


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
    return out, d


m = json.loads(SRC.read_text(encoding="utf-8"))
cases = dict(m["cases"])
assert len(cases) == 487
assert len(m["_r56_carryover_notes"]) == 29
assert len(m["_r57_carryover_notes_addendum"]) == 21
assert len(m["_r58_carryover_notes_addendum"]) == 17
assert len(m["_r59_carryover_notes_addendum"]) == 29
assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert cases["LR2-016"] == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"

# Layer A: r58 partial 14, cross-verified against the r59 addendum md.
notes_a, ann58 = json_notes(ANN58, {"部分成立"})
assert len(notes_a) == 14, f"r58 partial = {len(notes_a)}"
assert ann58["counts"]["verdicts"] == {"成立": 7, "部分成立": 14, "不成立": 3, "未核": 1}
cap59 = md_capture(ADD59)
missing = [c for c in notes_a if c not in cap59]
assert not missing, f"missing in {ADD59.name}: {missing}"
mismatch = [c for c in notes_a if cap59[c] != notes_a[c]]
assert not mismatch, f"md/json mismatch: {mismatch}"

# Layer B: r59 partial 20; counts asserted against R59 REPORT s.4.
notes_b, ann59 = json_notes(ANN59, {"部分成立"})
assert len(notes_b) == 20, f"r59 partial = {len(notes_b)}"
assert ann59["counts"]["verdicts"] == {"成立": 8, "部分成立": 20, "不成立": 0, "未核": 1}, ann59["counts"]
assert ann59["counts"]["cases_total"] == 29

for cid in list(notes_a) + list(notes_b):
    assert cid in cases, f"note case {cid} not in manifest"

src_cases = json.loads(SRC.read_text(encoding="utf-8"))["cases"]
diffs = [c for c in src_cases if cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r60_carryover_notes_addendum_a"] = notes_a
m["_r60_carryover_notes_addendum_b"] = notes_b
m["_r60_manifest_note"] = (
    "Built for R60 from runs/round59 manifest: cases payload verbatim for "
    "all 487 cases (LR2-016 split state preserved); prior layers preserved "
    "(_r56_carryover_notes 29, _r57_carryover_notes_addendum 21, "
    "_r58_carryover_notes_addendum 17, _r59_carryover_notes_addendum 29); "
    "_r60_carryover_notes_addendum_a from data/case-annotations-r58.json "
    "partial-upheld 14 by structured read, cross-verified 14/14 "
    "verbatim-equal against data/manifest-carryover-r59-addendum.md "
    "whole-line captures; _r60_carryover_notes_addendum_b from "
    "data/case-annotations-r59.json partial-upheld 20 by structured read "
    "(counts asserted equal to R59 REPORT s.4 distribution 8/20/0/1). "
    "No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK r60 layer A:", len(notes_a), "layer B:", len(notes_b))
