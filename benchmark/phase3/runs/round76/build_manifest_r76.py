#!/usr/bin/env python3
"""R76 host tooling: build runs/round76/judging/outcome-manifest.json.

Carry-note extraction follows the ADDENDUM-r57 s.1 fix: structured read of
the adjudication JSON only (no regex truncation extraction).

Layers:
- cases payload verbatim from runs/round75 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched).
- _r76_carryover_notes_addendum NEW: R75 adjudication partial-upheld 48
  from data/case-annotations-r75.json (manifest_carry_suggestion),
  effective from R76 per STAGE-SUMMARY-60 R76 list items 2 and 5.
  R75 verdict distribution asserted equal to the R75 REPORT s.4
  published distribution (12/48/2/2, total 64) and every partial item
  asserted to carry a non-empty suggestion. The R76 data seat compiles
  data/manifest-carryover-r76-addendum.md assembling these 48 for
  cross-verification against this layer (PREREG s.4).
Two-layer wording (R75 data-seat note, ADDENDUM-r75 s.4): this manifest
layer stores the suggestion text verbatim; the "[R76-addendum]" prefix is
added only by build_judge_packets_r76.py at the packet carry_note layer.
No outcome strings changed; no scores touched.
"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round75/judging/outcome-manifest.json"
ANN75 = P3 / "data/case-annotations-r75.json"
OUT = P3 / "runs/round76/judging/outcome-manifest.json"


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
assert len(m["_r71_carryover_notes_addendum"]) == 77
assert len(m["_r72_carryover_notes_addendum"]) == 83
assert len(m["_r73_carryover_notes_addendum"]) == 77
assert len(m["_r74_carryover_notes_addendum"]) == 140
assert len(m["_r75_carryover_notes_addendum"]) == 67
assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert cases["LR2-016"] == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"

notes, ann75 = json_notes(ANN75, {"部分成立"})
assert len(notes) == 48, f"r75 partial = {len(notes)}"
assert ann75["counts"]["verdicts"] == {"成立": 12, "部分成立": 48, "不成立": 2, "未核": 2}, ann75["counts"]
assert ann75["counts"]["cases_total"] == 64

for cid in notes:
    assert cid in cases, f"note case {cid} not in manifest"

src_cases = json.loads(SRC.read_text(encoding="utf-8"))["cases"]
diffs = [c for c in src_cases if cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r76_carryover_notes_addendum"] = notes
m["_r76_manifest_note"] = (
    "Built for R76 from runs/round75 manifest: cases payload verbatim for "
    "all 487 cases (LR2-016 split state preserved); prior layers preserved "
    "(_r56_carryover_notes 29, _r57_carryover_notes_addendum 21, "
    "_r58_carryover_notes_addendum 17, _r59_carryover_notes_addendum 29, "
    "_r60_carryover_notes_addendum_a 14, _r60_carryover_notes_addendum_b 20, "
    "_r61_carryover_notes_addendum 34, _r62_carryover_notes_addendum 58, "
    "_r63_carryover_notes_addendum 65, _r64_carryover_notes_addendum 72, "
    "_r65_carryover_notes_addendum 99, _r66_carryover_notes_addendum 40, "
    "_r67_carryover_notes_addendum 41, _r68_carryover_notes_addendum 35, "
    "_r69_carryover_notes_addendum 58, _r70_carryover_notes_addendum 84, "
    "_r71_carryover_notes_addendum 77, _r72_carryover_notes_addendum 83, "
    "_r73_carryover_notes_addendum 77, _r74_carryover_notes_addendum 140, "
    "_r75_carryover_notes_addendum 67); "
    "_r76_carryover_notes_addendum from data/case-annotations-r75.json "
    "partial-upheld 48 by structured read (counts asserted equal to R75 "
    "REPORT s.4 distribution 12/48/2/2, total 64). No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK r76 layer:", len(notes))
