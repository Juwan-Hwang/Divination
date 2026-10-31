#!/usr/bin/env python3
"""R68 host tooling: build runs/round68/judging/outcome-manifest.json.

Carry-note extraction follows the ADDENDUM-r57 s.1 fix: structured read of
the adjudication JSON only (no regex truncation extraction).

Layers:
- cases payload verbatim from runs/round67 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched).
- _r68_carryover_notes_addendum NEW: R67 adjudication partial-upheld 35
  from data/case-annotations-r67.json (manifest_carry_suggestion),
  effective from R68 per STAGE-SUMMARY-52 R68 list item 1. Upheld-6 are
  same-issue continuations already carried in earlier layers; unexamined-2
  in R67 adjudication (incl. YM-070, held as-is). Counts asserted equal to
  the R67 REPORT s.1 published distribution (6/35/7/2, total 50) and every
  partial item asserted to carry a non-empty suggestion. The R68 data
  seat compiles data/manifest-carryover-r68-addendum.md assembling these
  35 for cross-verification against this layer (PREREG s.4).
No outcome strings changed; no scores touched.
"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round67/judging/outcome-manifest.json"
ANN67 = P3 / "data/case-annotations-r67.json"
OUT = P3 / "runs/round68/judging/outcome-manifest.json"


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
assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert cases["LR2-016"] == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"

notes, ann67 = json_notes(ANN67, {"部分成立"})
assert len(notes) == 35, f"r67 partial = {len(notes)}"
assert ann67["counts"]["verdicts"] == {"部分成立": 35, "成立": 6, "不成立": 7, "未核": 2}, ann67["counts"]
assert ann67["counts"]["cases_total"] == 50

for cid in notes:
    assert cid in cases, f"note case {cid} not in manifest"

src_cases = json.loads(SRC.read_text(encoding="utf-8"))["cases"]
diffs = [c for c in src_cases if cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r68_carryover_notes_addendum"] = notes
m["_r68_manifest_note"] = (
    "Built for R68 from runs/round67 manifest: cases payload verbatim for "
    "all 487 cases (LR2-016 split state preserved); prior layers preserved "
    "(_r56_carryover_notes 29, _r57_carryover_notes_addendum 21, "
    "_r58_carryover_notes_addendum 17, _r59_carryover_notes_addendum 29, "
    "_r60_carryover_notes_addendum_a 14, _r60_carryover_notes_addendum_b 20, "
    "_r61_carryover_notes_addendum 34, _r62_carryover_notes_addendum 58, "
    "_r63_carryover_notes_addendum 65, _r64_carryover_notes_addendum 72, "
    "_r65_carryover_notes_addendum 99, _r66_carryover_notes_addendum 40, "
    "_r67_carryover_notes_addendum 41); "
    "_r68_carryover_notes_addendum from data/case-annotations-r67.json "
    "partial-upheld 35 by structured read (counts asserted equal to R67 "
    "REPORT s.1 distribution 6/35/7/2, total 50). No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK r68 layer:", len(notes))
