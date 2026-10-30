#!/usr/bin/env python3
"""R58 host tooling: build runs/round58/judging/outcome-manifest.json.

Fix per ADDENDUM-r57 s.1 (R58 build rule): carry-note extraction must NOT
use the non-greedy regex that truncated 9 notes in R57. This build reads
notes STRUCTURALLY from the adjudication JSON files
(data/case-annotations-r55.json / -r56.json, field manifest_carry_suggestion)
and cross-verifies every note against a whole-line greedy capture from the
corresponding addendum markdown (text between the first '：「' and the
LAST '」' on the suggestion line). Any mismatch aborts the build.

Layers:
- cases payload verbatim from runs/round57 manifest (487 cases;
  LR2-016 split state preserved; _r56_carryover_notes 29 preserved).
- _r57_carryover_notes_addendum REBUILT from case-annotations-r55.json
  (7 upheld + 14 partial = 21) -- repairs the 9 R57 truncations.
- _r58_carryover_notes_addendum from case-annotations-r56.json
  (16 partial) PLUS LY-011 with its R57 adjudication suggestion
  (ADDENDUM-r57 s.2: clarification effective from R58 manifest).
No outcome strings changed; no scores touched.
"""
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round57/judging/outcome-manifest.json"
ANN55 = P3 / "data/case-annotations-r55.json"
ANN56 = P3 / "data/case-annotations-r56.json"
ANN57 = P3 / "data/case-annotations-r57.json"
ADD56 = P3 / "data/manifest-carryover-r56-addendum.md"  # carries r55 adjudication
ADD57 = P3 / "data/manifest-carryover-r57-addendum.md"  # carries r56 adjudication
OUT = P3 / "runs/round58/judging/outcome-manifest.json"


def md_capture(md_path):
    """Whole-line capture: case_id -> suggestion text (first '：「' to
    last '」' on the suggestion line). No non-greedy truncation."""
    out = {}
    text = md_path.read_text(encoding="utf-8")
    for block in re.split(r"\n### ", text)[1:]:
        head = block.splitlines()[0]
        m = re.search(r"([A-Z]+\d*-\d+)", head)
        if not m:
            continue
        cid = m.group(1)
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
assert "_r56_carryover_notes" in m and len(m["_r56_carryover_notes"]) == 29
assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert cases["LR2-016"] == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"

# --- layer r57 (repairs R57 truncations) ---------------------------------
notes57 = json_notes(ANN55, {"成立", "部分成立"})
assert len(notes57) == 21, f"r55 carried = {len(notes57)}"
cap56 = md_capture(ADD56)
for cid, txt in notes57.items():
    assert cid in cap56, f"{cid} missing in {ADD56.name}"
    assert cap56[cid] == txt, f"md/json mismatch for {cid}"
# the 9 notes truncated in R57 must now differ from R57's stored layer
old57 = m.get("_r57_carryover_notes_addendum", {})
trunc9 = ["LY-240", "OC-014", "LY-528", "YY-022", "YM-070",
          "AS-210", "LR2-023", "LR3-112", "LR2-016"]
repaired = [c for c in trunc9 if notes57.get(c) and notes57[c] != old57.get(c)]
print("truncated-9 now repaired (full text restored):", repaired)

# --- layer r58 (R56 adjudication partial 16 + LY-011 R57 clarification) --
notes58 = json_notes(ANN56, {"部分成立"})
assert len(notes58) == 16, f"r56 partial = {len(notes58)}"
cap57 = md_capture(ADD57)
for cid, txt in notes58.items():
    assert cid in cap57, f"{cid} missing in {ADD57.name}"
    assert cap57[cid] == txt, f"md/json mismatch for {cid}"
ann57 = json.loads(ANN57.read_text(encoding="utf-8"))
ly011 = [a for a in ann57["annotations"] if a["case_id"] == "LY-011"]
assert len(ly011) == 1 and ly011[0]["disposition"] == "部分成立"
assert "双断为原书大师原断" in ly011[0]["manifest_carry_suggestion"]
notes58["LY-011"] = ly011[0]["manifest_carry_suggestion"]
assert len(notes58) == 17

for cid in list(notes57) + list(notes58):
    assert cid in cases, f"note case {cid} not in manifest"

# --- verbatim payload check ----------------------------------------------
src_cases = json.loads(SRC.read_text(encoding="utf-8"))["cases"]
diffs = [c for c in src_cases if cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r57_carryover_notes_addendum"] = notes57
m["_r58_carryover_notes_addendum"] = notes58
m["_r58_manifest_note"] = (
    "Built for R58 from runs/round57 manifest: cases payload verbatim for "
    "all 487 cases (LR2-016 split state preserved); _r56_carryover_notes "
    "(29) preserved; _r57_carryover_notes_addendum REBUILT by structured "
    "read of data/case-annotations-r55.json (7 upheld + 14 partial = 21), "
    "repairing the 9 notes truncated by the R57 build regex (ADDENDUM-r57 "
    "s.1 fix: structured read + whole-line capture cross-verified against "
    "manifest-carryover-r56-addendum.md, all 21 verbatim-equal); "
    "_r58_carryover_notes_addendum from data/case-annotations-r56.json "
    "(16 partial, cross-verified against manifest-carryover-r57-addendum.md) "
    "plus LY-011 carrying its R57 adjudication clarification text "
    "(ADDENDUM-r57 s.2). No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK r57 layer:", len(notes57), "| r58 layer:", len(notes58))
