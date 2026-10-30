#!/usr/bin/env python3
"""R57 host tooling: build runs/round57/judging/outcome-manifest.json.

Basis (R57 PREREG s.0/s.5):
- cases payload carried verbatim from runs/round56 manifest (487 cases;
  LR2-016 editor-note split state from R56 preserved as-is).
- R56 addendum application (data/manifest-carryover-r56-addendum.md,
  effective from R57 per its title page): marker texts for the 7 upheld +
  14 partial items of the R55 adjudication are attached under
  _r57_carryover_notes_addendum (case_id -> marker text), outcome strings
  unmodified. The 1 rejected + 2 unverified items are not carried.
No other payload change. Assertions enforce counts and verbatim equality.
"""
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round56/judging/outcome-manifest.json"
ADD = P3 / "data/manifest-carryover-r56-addendum.md"
OUT = P3 / "runs/round57/judging/outcome-manifest.json"

m = json.loads(SRC.read_text(encoding="utf-8"))
cases = dict(m["cases"])
assert len(cases) == 487
assert "_r56_carryover_notes" in m and len(m["_r56_carryover_notes"]) == 29
assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
assert cases["LR2-016"] == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"

# --- parse R56 addendum (sections one and two only) ----------------------
add = ADD.read_text(encoding="utf-8")
sec1 = add.split("## 一、")[1].split("## 二、")[0]
sec2 = add.split("## 二、")[1].split("## 三、")[0]
sec3 = add.split("## 三、")[1].split("## 四、")[0]


def parse_entries(sec):
    out = {}
    for block in re.split(r"\n### ", sec)[1:]:
        head = block.splitlines()[0]
        cid = re.search(r"([A-Z]+\d*-\d+)", head).group(1)
        mm = re.search(r"承接注记建议文本（照原档.*?）：「(.*?)」", block, re.S)
        assert mm, f"no suggestion text for {cid}"
        out[cid] = mm.group(1)
    return out


upheld = parse_entries(sec1)
partial = parse_entries(sec2)
notcarried = re.findall(r"### \d+\. ([A-Z]+\d*-\d+)", sec3)
assert len(upheld) == 7, f"upheld={len(upheld)}"
assert len(partial) == 14, f"partial={len(partial)}"
assert len(notcarried) == 3, f"notcarried={notcarried}"
notes = {}
notes.update(upheld)
notes.update(partial)
assert len(notes) == 21 and not (set(notes) & set(notcarried))
for cid in notes:
    assert cid in cases, f"addendum case {cid} not in manifest"

# --- verify cases payload verbatim vs round56 ----------------------------
src_cases = json.loads(SRC.read_text(encoding="utf-8"))["cases"]
diffs = [c for c in src_cases if cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r57_carryover_notes_addendum"] = notes
m["_r57_manifest_note"] = (
    "Built for R57 from runs/round56 manifest: cases payload verbatim for all "
    "487 cases (LR2-016 split state preserved, see _r56_lr2016_split); R56 "
    "carryover notes (29) preserved under _r56_carryover_notes; R55-adjudication "
    "marker texts from data/manifest-carryover-r56-addendum.md attached under "
    "_r57_carryover_notes_addendum (7 upheld + 14 partial; 1 rejected + 2 "
    "unverified not carried). No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK addendum notes:", len(notes), "| upheld:", len(upheld), "| partial:", len(partial))
print("not carried:", notcarried)
