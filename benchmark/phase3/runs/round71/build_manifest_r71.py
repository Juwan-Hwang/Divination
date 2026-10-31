#!/usr/bin/env python3
"""R71 host tooling: build runs/round71/judging/outcome-manifest.json.

Carry-note extraction follows the ADDENDUM-r57 s.1 fix: structured read of
the adjudication JSON only (no regex truncation extraction).

Layers:
- cases payload verbatim from runs/round70 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched).
- _r71_carryover_notes_addendum NEW: R70 adjudication partial-upheld 77
  from data/case-annotations-r70.json (manifest_carry_suggestion),
  effective from R71 per STAGE-SUMMARY-55 R71 list item 1 and item 5.
  R70 verdict distribution asserted equal to the R70 REPORT s.1
  published distribution (11/77/1/2, total 91) and every partial item
  asserted to carry a non-empty suggestion. The R71 data seat compiles
  data/manifest-carryover-r71-addendum.md assembling these 77 for
  cross-verification against this layer (PREREG s.4).
No outcome strings changed; no scores touched.
"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round70/judging/outcome-manifest.json"
ANN70 = P3 / "data/case-annotations-r70.json"
OUT = P3 / "runs/round71/judging/outcome-manifest.json"


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
assert len(m["_r60_carryover_notes_addendum_a"]) == 14
assert len(m["_r60_carryover_notes_addendum_b"]) == 20
assert len(m["_r61_carryover_notes_addendum"]) == 34
assert len(m["_r62_carryover_notes_addendum"]) == 58
assert len(m["_r63_carryover_notes_addendum"]) == 65
assert len(m["_r64_carryover_notes_addendum"]) == 72
assert len(m["_r65_carryover_notes_addendum"]) == 99
assert len(m["_r66_carryover_notes_addendum"]) == 40
assert len(m["_r67_carryover_notes_addendum"]) == 41
assert len(m["_r68_carryover_notes_addendum"]) == 35
assert len(m["_r69_carryover_notes_addendum"]) == 58
assert len(m["_r70_carryover_notes_addendum"]) == 84
assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert cases["LR2-016"] == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"

notes, ann70 = json_notes(ANN70, {"部分成立"})
assert len(notes) == 77, f"r70 partial = {len(notes)}"
assert ann70["counts"]["verdicts"] == {"成立": 11, "部分成立": 77, "不成立": 1, "未核": 2}, ann70["counts"]
assert ann70["counts"]["cases_total"] == 91

for cid in notes:
    assert cid in cases, f"note case {cid} not in manifest"

src_cases = json.loads(SRC.read_text(encoding="utf-8"))["cases"]
diffs = [c for c in src_cases if cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r71_carryover_notes_addendum"] = notes
m["_r71_manifest_note"] = (
    "Built for R71 from runs/round70 manifest: cases payload verbatim for "
    "all 487 cases (LR2-016 split state preserved); prior layers preserved "
    "(_r56_carryover_notes 29, _r57_carryover_notes_addendum 21, "
    "_r58_carryover_notes_addendum 17, _r59_carryover_notes_addendum 29, "
    "_r60_carryover_notes_addendum_a 14, _r60_carryover_notes_addendum_b 20, "
    "_r61_carryover_notes_addendum 34, _r62_carryover_notes_addendum 58, "
    "_r63_carryover_notes_addendum 65, _r64_carryover_notes_addendum 72, "
    "_r65_carryover_notes_addendum 99, _r66_carryover_notes_addendum 40, "
    "_r67_carryover_notes_addendum 41, _r68_carryover_notes_addendum 35, "
    "_r69_carryover_notes_addendum 58, _r70_carryover_notes_addendum 84); "
    "_r71_carryover_notes_addendum from data/case-annotations-r70.json "
    "partial-upheld 77 by structured read (counts asserted equal to R70 "
    "REPORT s.1 distribution 11/77/1/2, total 91). No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK r71 layer:", len(notes))
