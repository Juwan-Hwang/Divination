#!/usr/bin/env python3
"""R80 host tooling: build runs/round80/judging/outcome-manifest.json.

Carry-note extraction follows the ADDENDUM-r57 s.1 fix: structured read of
the adjudication JSON only (no regex truncation extraction). The single
same-case-new-gist item (BZ-037) is taken verbatim from
data/manifest-carryover-r79-addendum.md s.3.2 and asserted by full-string
containment in that file (no extraction parsing).

Layers:
- cases payload verbatim from runs/round79 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched).
- _r79_carryover_notes_addendum NEW: R79 adjudication partial-upheld 23 =
  22 NEW registrations (registered_round == 79 in
  data/case-annotations-r79.json, manifest_carry_suggestion verbatim)
  + BZ-037 same-case-new-gist note (text verbatim from the R79 addendum
  compilation, parallel to its R76 tradition-gist note already carried in
  _r76_carryover_notes_addendum). Effective from R80 per STAGE-SUMMARY-64
  R80 list item 1 and R79 PREREG s.4.
- _r80_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round79/judging/outcome-manifest.json"
ANN79 = P3 / "data/case-annotations-r79.json"
ADD79 = P3 / "data/manifest-carryover-r79-addendum.md"
OUT = P3 / "runs/round80/judging/outcome-manifest.json"

EXPECTED_CASES_SHA = "00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad"
EXPECTED_NEW22 = [
    "AS-209", "AS-215", "AS-304", "BQ-021", "BZ-104", "LR2-016",
    "LR3-002", "LY-011", "LY-255", "LY-322", "LY-329", "LY-408",
    "LY-411", "LY-413", "LY-428", "LY-434", "LY-440", "LY-514",
    "LY-523", "LY-525", "LY-538", "LY-623",
]
BZ037_NEW_GIST = (
    "同例新旨：自 R80 起承接本 R79 标注（与 R76 主持裁定 tradition 旨并行）"
    "：按「结局自注『未执政』与史实不合、已自标为已知偏差点」登记；"
    "结局原文照录不改。"
)

LAYER_SIZES = {
    "_r56_carryover_notes": 29,
    "_r57_carryover_notes_addendum": 21,
    "_r58_carryover_notes_addendum": 17,
    "_r59_carryover_notes_addendum": 29,
    "_r60_carryover_notes_addendum_a": 14,
    "_r60_carryover_notes_addendum_b": 20,
    "_r61_carryover_notes_addendum": 34,
    "_r62_carryover_notes_addendum": 58,
    "_r63_carryover_notes_addendum": 65,
    "_r64_carryover_notes_addendum": 72,
    "_r65_carryover_notes_addendum": 99,
    "_r66_carryover_notes_addendum": 40,
    "_r67_carryover_notes_addendum": 41,
    "_r68_carryover_notes_addendum": 35,
    "_r69_carryover_notes_addendum": 58,
    "_r70_carryover_notes_addendum": 84,
    "_r71_carryover_notes_addendum": 77,
    "_r72_carryover_notes_addendum": 83,
    "_r73_carryover_notes_addendum": 77,
    "_r74_carryover_notes_addendum": 140,
    "_r75_carryover_notes_addendum": 67,
    "_r76_carryover_notes_addendum": 48,
    "_r77_carryover_notes_addendum": 6,
}


def cases_sha(cases):
    return hashlib.sha256(
        json.dumps(cases, ensure_ascii=False, sort_keys=True).encode()
    ).hexdigest()


def main():
    m = json.loads(SRC.read_text(encoding="utf-8"))
    cases = m["cases"]
    assert len(cases) == 487, len(cases)
    assert cases_sha(cases) == EXPECTED_CASES_SHA, "cases payload drift"
    for k, n in LAYER_SIZES.items():
        assert len(m[k]) == n, (k, len(m[k]))
    assert m["_r56_lr2016_split"]["case_id"] == "LR2-016"
    assert "_r79_carryover_notes_addendum" not in m

    ann = json.loads(ANN79.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 94, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 12, "部分成立": 76, "不成立": 4, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_partial_cases_r79"] == EXPECTED_NEW22
    assert ann["counts"]["new_registrations_r79"] == 24
    assert ann["counts"]["same_case_new_gist_cases"] == ["BZ-037"]

    notes = {}
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 79:
            assert a["manifest_carry_suggestion"], a["case_id"]
            notes[a["case_id"]] = a["manifest_carry_suggestion"]
    assert sorted(notes) == sorted(EXPECTED_NEW22), sorted(notes)

    add_text = ADD79.read_text(encoding="utf-8")
    assert BZ037_NEW_GIST in add_text, "BZ-037 new-gist text not in addendum"
    assert "BZ-037" not in notes
    notes["BZ-037"] = BZ037_NEW_GIST
    assert len(notes) == 23

    for cid in notes:
        assert cid in cases, f"note case {cid} not in manifest"

    m["_r79_carryover_notes_addendum"] = notes
    m["_r80_manifest_note"] = (
        "Built for R80 from runs/round79 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted); "
        "_r79_carryover_notes_addendum NEW with 23 items = R79 "
        "adjudication NEW partial-upheld 22 (registered_round == 79 in "
        "data/case-annotations-r79.json, structured read, counts asserted "
        "equal to R79 published distribution 12/76/4/2, total 94) + BZ-037 "
        "same-case-new-gist note verbatim from "
        "data/manifest-carryover-r79-addendum.md s.3.2 (full-string "
        "containment asserted). No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes))


if __name__ == "__main__":
    main()
