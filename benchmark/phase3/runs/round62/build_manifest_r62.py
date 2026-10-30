#!/usr/bin/env python3
"""R62 host tooling: build runs/round62/judging/outcome-manifest.json.

Carry-note extraction follows the ADDENDUM-r57 s.1 fix: structured read of
the adjudication JSON only (no regex truncation extraction).

Layers:
- cases payload verbatim from runs/round61 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched).
- _r62_carryover_notes_addendum NEW: R61 adjudication partial-upheld 58
  from data/case-annotations-r61.json (manifest_carry_suggestion),
  effective from R62 per STAGE-SUMMARY-46 R62 list item 1. Upheld-14 are
  same-issue continuations already carried in earlier layers; unexamined-2
  are LY-537 / YM-070 (pending / suspension maintained). Counts asserted
  equal to the R61 REPORT s.1 published distribution (14/58/7/2,
  total 81) and every partial item asserted to carry a non-empty
  suggestion. The R62 data seat compiles
  data/manifest-carryover-r62-addendum.md assembling these 58 for
  cross-verification against this layer (PREREG s.4).
No outcome strings changed; no scores touched.
"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round61/judging/outcome-manifest.json"
ANN61 = P3 / "data/case-annotations-r61.json"
OUT = P3 / "runs/round62/judging/outcome-manifest.json"


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
assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert cases["LR2-016"] == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"

notes, ann61 = json_notes(ANN61, {"部分成立"})
assert len(notes) == 58, f"r61 partial = {len(notes)}"
assert ann61["counts"]["verdicts"] == {"成立": 14, "部分成立": 58, "不成立": 7, "未核": 2}, ann61["counts"]
assert ann61["counts"]["cases_total"] == 81

for cid in notes:
    assert cid in cases, f"note case {cid} not in manifest"

src_cases = json.loads(SRC.read_text(encoding="utf-8"))["cases"]
diffs = [c for c in src_cases if cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r62_carryover_notes_addendum"] = notes
m["_r62_manifest_note"] = (
    "Built for R62 from runs/round61 manifest: cases payload verbatim for "
    "all 487 cases (LR2-016 split state preserved); prior layers preserved "
    "(_r56_carryover_notes 29, _r57_carryover_notes_addendum 21, "
    "_r58_carryover_notes_addendum 17, _r59_carryover_notes_addendum 29, "
    "_r60_carryover_notes_addendum_a 14, _r60_carryover_notes_addendum_b 20, "
    "_r61_carryover_notes_addendum 34); "
    "_r62_carryover_notes_addendum from data/case-annotations-r61.json "
    "partial-upheld 58 by structured read (counts asserted equal to R61 "
    "REPORT s.1 distribution 14/58/7/2, total 81). No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK r62 layer:", len(notes))
