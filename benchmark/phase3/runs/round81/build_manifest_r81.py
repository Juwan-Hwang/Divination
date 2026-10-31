#!/usr/bin/env python3
"""R81 host tooling: build runs/round81/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round80 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r79_carryover_notes_addendum == 23).
- _r80_carryover_notes_addendum NEW: R80 adjudication partial-upheld 1 =
  AS-307 (registered_round == 80 in data/case-annotations-r80.json,
  manifest_carry_suggestion verbatim, structured read; LR3-004/LR3-104
  not-upheld items are registration-only and do NOT enter the layer).
  Effective from R81 per STAGE-SUMMARY-65 R81 list item 1 and
  data/manifest-carryover-r80-addendum.md s.3.
- _r81_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round80/judging/outcome-manifest.json"
ANN80 = P3 / "data/case-annotations-r80.json"
OUT = P3 / "runs/round81/judging/outcome-manifest.json"

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
    assert "_r80_carryover_notes_addendum" not in m

    ann = json.loads(ANN80.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 97, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 12, "部分成立": 77, "不成立": 6, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_partial_cases_r80"] == ["AS-307"]
    assert ann["counts"]["new_registrations_r80"] == 3
    assert ann["counts"]["new_not_upheld_cases_r80"] == ["LR3-004", "LR3-104"]

    notes = {}
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 80:
            assert a["manifest_carry_suggestion"], a["case_id"]
            notes[a["case_id"]] = a["manifest_carry_suggestion"]
    assert sorted(notes) == ["AS-307"], sorted(notes)
    assert len(notes) == 1

    for cid in notes:
        assert cid in cases, f"note case {cid} not in manifest"

    m["_r80_carryover_notes_addendum"] = notes
    m["_r81_manifest_note"] = (
        "Built for R81 from runs/round80 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r79_carryover_notes_addendum == 23); "
        "_r80_carryover_notes_addendum NEW with 1 item = R80 adjudication "
        "partial-upheld AS-307 (registered_round == 80 in "
        "data/case-annotations-r80.json, structured read, counts asserted "
        "equal to R80 published distribution 12/77/6/2, total 97); "
        "LR3-004/LR3-104 not-upheld items registration-only, not in layer. "
        "No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes))


if __name__ == "__main__":
    main()
