#!/usr/bin/env python3
"""R83 host tooling: build runs/round83/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round82 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r81_carryover_notes_addendum == 14).
- _r82_carryover_notes_addendum NEW: R82 adjudication partial-upheld
  items = 13 (data/case-annotations-r82.json, registered_round == 82,
  disposition partial-upheld). Of these, the 3 platform cases present in
  the dev manifest cases (LY-406, LY-446, LY-524) enter this layer with
  manifest_carry_suggestion captured VERBATIM IN FULL by structured read
  of the annotations JSON field (AS-307 ruling of R82: no prefix/regex
  capture; full text, tail verified after write by readback assertion).
  The 10 acceptance-side items (QM-034, QM-038, QM-036, QM-039, QM-042,
  GSZ-069, GSZ-074, GSZ-077, WHY-005, DS-034) are NOT dev-manifest cases;
  per the R82 addendum they are carried by the gold/acceptance note
  layer, not this manifest, and are asserted to be exactly the non-case
  remainder.
- _r83_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round82/judging/outcome-manifest.json"
ANN82 = P3 / "data/case-annotations-r82.json"
OUT = P3 / "runs/round83/judging/outcome-manifest.json"

EXPECTED_CASES_SHA = "00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad"

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
    "_r79_carryover_notes_addendum": 23,
    "_r80_carryover_notes_addendum": 1,
    "_r81_carryover_notes_addendum": 14,
}

EXPECTED_NEW_PARTIAL_R82 = [
    "LY-406", "LY-446", "LY-524",
    "QM-034", "QM-038", "QM-036", "QM-039", "QM-042",
    "GSZ-069", "GSZ-074", "GSZ-077", "WHY-005", "DS-034",
]
EXPECTED_ACCEPTANCE_SIDE = {
    "QM-034", "QM-038", "QM-036", "QM-039", "QM-042",
    "GSZ-069", "GSZ-074", "GSZ-077", "WHY-005", "DS-034",
}
EXPECTED_PLATFORM = {"LY-406", "LY-446", "LY-524"}


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
    assert "_r82_carryover_notes_addendum" not in m

    ann = json.loads(ANN82.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 134, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 12, "部分成立": 114, "不成立": 6, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_partial_cases_r82"] == EXPECTED_NEW_PARTIAL_R82
    assert ann["counts"]["new_registrations_r82"] == 13

    notes = {}
    acceptance_side = set()
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 82:
            assert a["manifest_carry_suggestion"], a["case_id"]
            if a["case_id"] in cases:
                notes[a["case_id"]] = a["manifest_carry_suggestion"]
            else:
                acceptance_side.add(a["case_id"])
    assert acceptance_side == EXPECTED_ACCEPTANCE_SIDE, acceptance_side
    assert set(notes) == EXPECTED_PLATFORM, sorted(notes)
    # Full-text tail integrity (AS-307 ruling): every captured suggestion
    # must end with the complete closing tail, not a prefix.
    for cid, txt in notes.items():
        assert txt.endswith("照录不改。"), (cid, txt[-20:])

    m["_r82_carryover_notes_addendum"] = notes
    m["_r83_manifest_note"] = (
        "Built for R83 from runs/round82 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r81_carryover_notes_addendum == 14); "
        "_r82_carryover_notes_addendum NEW with 3 platform items = R82 "
        "adjudication partial-upheld platform cases (registered_round "
        "== 82 in data/case-annotations-r82.json, structured read, "
        "counts asserted equal to R82 published distribution "
        "12/114/6/2, total 134; suggestion texts captured verbatim in "
        "full per the R82 AS-307 ruling, tails asserted); the 10 "
        "acceptance-side partial items are not dev-manifest cases and "
        "are carried by the gold/acceptance note layer per the R82 "
        "addendum. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    # Readback verification: layer texts on disk equal the source fields
    # verbatim in full, and the manifest tail is intact.
    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert back["_r82_carryover_notes_addendum"] == notes
    for cid, txt in back["_r82_carryover_notes_addendum"].items():
        assert txt.endswith("结局原文照录不改。"), (cid, txt[-20:])
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes), sorted(notes))


if __name__ == "__main__":
    main()
