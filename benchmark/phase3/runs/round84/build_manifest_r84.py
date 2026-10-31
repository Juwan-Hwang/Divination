#!/usr/bin/env python3
"""R84 host tooling: build runs/round84/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round83 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82_carryover_notes_addendum == 3).
- _r83_carryover_notes_addendum NEW but EMPTY: R83 adjudication
  partial-upheld items = 11 (data/case-annotations-r83.json,
  registered_round == 83, disposition partial-upheld), ALL of them
  acceptance-side (holdout27 cases DS-040, DS-048, QM-052, QM-058,
  GSZ-079, GSZ-081, GSZ-084, GSZ-088, WHY-008, WHY-009, WHY-010), none
  present in the dev manifest cases. Per data/manifest-carryover-r83-
  addendum.md s.3.1 the platform side is an explicitly empty set; the
  11 acceptance-side items are carried by the gold/acceptance note
  layer, not this manifest, and are asserted to be exactly the
  non-case remainder.
- _r84_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round83/judging/outcome-manifest.json"
ANN83 = P3 / "data/case-annotations-r83.json"
OUT = P3 / "runs/round84/judging/outcome-manifest.json"

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
    "_r82_carryover_notes_addendum": 3,
}

EXPECTED_NEW_PARTIAL_R83 = [
    "DS-040", "DS-048", "QM-052", "QM-058", "GSZ-079", "GSZ-088",
    "GSZ-081", "GSZ-084", "WHY-008", "WHY-009", "WHY-010",
]
EXPECTED_ACCEPTANCE_SIDE = set(EXPECTED_NEW_PARTIAL_R83)


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
    assert "_r83_carryover_notes_addendum" not in m

    ann = json.loads(ANN83.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 147, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 12, "部分成立": 125, "不成立": 8, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_partial_cases_r83"] == EXPECTED_NEW_PARTIAL_R83
    assert ann["counts"]["new_registrations_r83"] == 13

    notes = {}
    acceptance_side = set()
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 83:
            assert a["manifest_carry_suggestion"], a["case_id"]
            if a["case_id"] in cases:
                notes[a["case_id"]] = a["manifest_carry_suggestion"]
            else:
                acceptance_side.add(a["case_id"])
    assert acceptance_side == EXPECTED_ACCEPTANCE_SIDE, acceptance_side
    assert notes == {}, sorted(notes)

    m["_r83_carryover_notes_addendum"] = notes
    m["_r84_manifest_note"] = (
        "Built for R84 from runs/round83 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r82_carryover_notes_addendum == 3); "
        "_r83_carryover_notes_addendum NEW but EMPTY -- R83 adjudication "
        "partial-upheld items (11, registered_round == 83 in "
        "data/case-annotations-r83.json, counts asserted equal to R83 "
        "published distribution 12/125/8/2, total 147) are all "
        "acceptance-side holdout27 cases, not dev-manifest cases; the "
        "platform side is an explicitly empty set per "
        "data/manifest-carryover-r83-addendum.md s.3.1, and the 11 "
        "acceptance-side items are carried by the gold/acceptance note "
        "layer per that addendum. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert back["_r83_carryover_notes_addendum"] == {}
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes), "| acceptance side", len(acceptance_side))


if __name__ == "__main__":
    main()
