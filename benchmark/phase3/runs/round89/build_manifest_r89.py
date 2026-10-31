#!/usr/bin/env python3
"""R89 host tooling: build runs/round89/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round88 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82_carryover_notes_addendum == 3,
  _r83_carryover_notes_addendum == 0,
  _r84_carryover_notes_addendum == 0,
  _r85_carryover_notes_addendum == 12,
  _r86_carryover_notes_addendum == 45 and
  _r87_carryover_notes_addendum == 43).
- _r88_carryover_notes_addendum NEW with 0 items: R88 produced NO new
  partial-upheld PLATFORM-side registrations (all 9 new R88
  registrations are acceptance-side, from DIAG-H31 s.5 flags; see
  data/manifest-carryover-r88-addendum.md s.3). Per the R83 precedent
  the R88 partial-upheld ACCEPTANCE-side set (holdout31: WHY-043,
  DA-051, GSZ-107) is not in dev cases and does not enter the dev
  manifest carry layer; it is asserted as exactly that 3-id set and
  registered in the manifest note only.
- _r89_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round88/judging/outcome-manifest.json"
ANN88 = P3 / "data/case-annotations-r88.json"
OUT = P3 / "runs/round89/judging/outcome-manifest.json"

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
    "_r83_carryover_notes_addendum": 0,
    "_r84_carryover_notes_addendum": 0,
    "_r85_carryover_notes_addendum": 12,
    "_r86_carryover_notes_addendum": 45,
    "_r87_carryover_notes_addendum": 43,
}

EXPECTED_ACCEPTANCE_SIDE = ["DA-051", "GSZ-107", "WHY-043"]


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
    assert "_r88_carryover_notes_addendum" not in m

    ann = json.loads(ANN88.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 309, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 14, "部分成立": 238, "不成立": 55, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_registrations_r88"] == 9
    expected_acc = ann["counts"]["new_cases_r88"]["部分成立_acceptance"]
    assert sorted(expected_acc) == EXPECTED_ACCEPTANCE_SIDE, expected_acc
    assert "部分成立_platform" not in ann["counts"]["new_cases_r88"] or \
        ann["counts"]["new_cases_r88"].get("部分成立_platform") in (None, []), \
        ann["counts"]["new_cases_r88"]

    notes = {}
    acceptance_side = set()
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 88:
            if a["case_id"] in cases:
                notes[a["case_id"]] = a["manifest_carry_suggestion"]
            else:
                acceptance_side.add(a["case_id"])
    assert notes == {}, notes
    assert sorted(acceptance_side) == EXPECTED_ACCEPTANCE_SIDE, acceptance_side

    m["_r88_carryover_notes_addendum"] = notes
    m["_r89_manifest_note"] = (
        "Built for R89 from runs/round88 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r82_carryover_notes_addendum == 3, "
        "_r83_carryover_notes_addendum == 0, "
        "_r84_carryover_notes_addendum == 0, "
        "_r85_carryover_notes_addendum == 12, "
        "_r86_carryover_notes_addendum == 45 and "
        "_r87_carryover_notes_addendum == 43); "
        "_r88_carryover_notes_addendum NEW with 0 items -- R88 produced "
        "no new partial-upheld platform-side registrations (all 9 new "
        "R88 registrations are acceptance-side, compiled in data/"
        "manifest-carryover-r88-addendum.md s.3; data/"
        "case-annotations-r88.json: 309 total, verdicts 14/238/55/2, "
        "9 new registrations in R88); the R88 partial-upheld "
        "acceptance-side set (holdout31: WHY-043, DA-051, GSZ-107) is "
        "not in dev cases and per the R83 precedent does not enter the "
        "dev manifest layer -- asserted as exactly that 3-id set, "
        "registered here only. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r88_carryover_notes_addendum"]) == 0
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes), "| acceptance side", len(acceptance_side))


if __name__ == "__main__":
    main()
