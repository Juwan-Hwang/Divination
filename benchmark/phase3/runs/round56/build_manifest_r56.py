#!/usr/bin/env python3
"""R56 host tooling: build runs/round56/judging/outcome-manifest.json.

Basis (R56 PREREG s.0/s.4):
- cases payload carried verbatim from runs/round55 manifest for 486 cases.
- LR2-016: embedded editor note split out (R55 REPORT s.6 ruling,
  STAGE-SUMMARY-40 s.3): outcome keeps only the outcome text; the note
  sentence is preserved verbatim under _r56_lr2016_split.editor_note.
- Carryover register application (data/manifest-carryover-r55.md,
  effective from R56): marker texts for the 13 upheld + 16 partial items
  are attached under _r56_carryover_notes (case_id -> marker text),
  outcome strings unmodified. The 7 rejected items are not carried.
No other payload change. Assertions enforce counts and verbatim equality.
"""
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round55/judging/outcome-manifest.json"
REG = P3 / "data/manifest-carryover-r55.md"
OUT = P3 / "runs/round56/judging/outcome-manifest.json"

m = json.loads(SRC.read_text(encoding="utf-8"))
cases = dict(m["cases"])
assert len(cases) == 487

# --- parse carryover register -------------------------------------------
reg = REG.read_text(encoding="utf-8")
sec1 = reg.split("## 一、")[1].split("## 二、")[0]
sec2 = reg.split("## 二、")[1].split("## 三、")[0]
sec3 = reg.split("## 三、")[1].split("## 卷末登记")[0]


def parse_entries(sec):
    out = {}
    for block in re.split(r"\n### ", sec)[1:]:
        head = block.splitlines()[0]
        cid = re.search(r"([A-Z]+\d*-\d+)", head).group(1)
        mm = re.search(r"承接标记文本：「(.*?)」", block, re.S)
        if mm:
            out[cid] = mm.group(1)
    return out


formal = parse_entries(sec1)
partial = parse_entries(sec2)
rejected_heads = re.findall(r"### \d+\. ([A-Z]+\d*-\d+)", sec3)
assert len(formal) == 13, f"formal={len(formal)}"
assert len(partial) == 16, f"partial={len(partial)}"
assert len(rejected_heads) == 7, f"rejected={len(rejected_heads)}"
notes = {}
notes.update(formal)
notes.update(partial)
assert len(notes) == 29 and not (set(notes) & set(rejected_heads))
for cid in notes:
    assert cid in cases, f"carryover case {cid} not in manifest"

# --- LR2-016 split -------------------------------------------------------
orig = cases["LR2-016"]
note_sentence = "原文未逐字复核「甲戌日巳时」的日时细节，评分时该细项请按未完全复核处理。"
assert note_sentence in orig, "LR2-016 note sentence not found verbatim"
outcome_only = orig.replace(note_sentence, "").strip()
assert outcome_only == "众不然其说，三月冯大司寇上疏，旨意驳下，四月上疏，依拟脱离。"
cases["LR2-016"] = outcome_only

# --- verify verbatim for all other cases --------------------------------
src_cases = m["cases"]
diffs = [c for c in src_cases if c != "LR2-016" and cases[c] != src_cases[c]]
assert not diffs, f"unexpected payload diffs: {diffs}"

m["cases"] = cases
m["_r56_carryover_notes"] = notes
m["_r56_lr2016_split"] = {
    "case_id": "LR2-016",
    "editor_note": note_sentence,
    "ruling": "R55 REPORT s.6 / STAGE-SUMMARY-40 s.3: embedded editor note split-registered apart from outcome text; outcome text itself unmodified apart from removal of the note sentence, which is preserved verbatim here.",
}
m["_r56_manifest_note"] = (
    "Built for R56 from runs/round55 manifest: cases payload verbatim for 486 cases; "
    "LR2-016 editor note split-registered (see _r56_lr2016_split); carryover marker "
    "texts from data/manifest-carryover-r55.md attached under _r56_carryover_notes "
    "(13 upheld + 16 partial; 7 rejected items not carried). No scores changed."
)
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
print("OK notes:", len(notes), "| formal:", len(formal), "| partial:", len(partial))
print("LR2-016 outcome now:", cases["LR2-016"])
