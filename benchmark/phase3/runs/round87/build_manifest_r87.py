#!/usr/bin/env python3
"""R87 host tooling: build runs/round87/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round86 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82_carryover_notes_addendum == 3,
  _r83_carryover_notes_addendum == 0,
  _r84_carryover_notes_addendum == 0 and
  _r85_carryover_notes_addendum == 12).
- _r86_carryover_notes_addendum NEW with 45 items: the R86 partial-upheld
  PLATFORM-side set compiled in data/manifest-carryover-r86-addendum.md
  s.3.1, derived here from data/case-annotations-r86.json (disposition
  partial-upheld, registered_round == 86, case_id in dev cases) and
  asserted equal to the published counts list
  new_cases_r86['部分成立_platform'] (45 ids).
- The R86 partial-upheld ACCEPTANCE-side set (holdout29: CYJ-001,
  CYJ-002, CYJ-004, CYJ-005, ZW-015) is NOT in dev cases and, per the
  R83 precedent recorded in the r86 addendum s.4, does not enter the
  dev manifest carry layer; it is asserted as exactly that 5-id set
  and registered in the manifest note only.
- _r87_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round86/judging/outcome-manifest.json"
ANN86 = P3 / "data/case-annotations-r86.json"
OUT = P3 / "runs/round87/judging/outcome-manifest.json"

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
}

EXPECTED_ACCEPTANCE_SIDE = ["CYJ-001", "CYJ-002", "CYJ-004", "CYJ-005", "ZW-015"]


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
    assert "_r86_carryover_notes_addendum" not in m

    ann = json.loads(ANN86.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 238, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 14, "部分成立": 187, "不成立": 35, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_registrations_r86"] == 55
    expected_layer = ann["counts"]["new_cases_r86"]["部分成立_platform"]
    assert len(expected_layer) == 45, len(expected_layer)
    expected_acc = ann["counts"]["new_cases_r86"]["部分成立_acceptance"]
    assert sorted(expected_acc) == EXPECTED_ACCEPTANCE_SIDE, expected_acc

    notes = {}
    acceptance_side = set()
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 86:
            if a["case_id"] in cases:
                notes[a["case_id"]] = a["manifest_carry_suggestion"]
            else:
                acceptance_side.add(a["case_id"])
    assert sorted(notes) == sorted(expected_layer), sorted(notes)
    assert sorted(acceptance_side) == EXPECTED_ACCEPTANCE_SIDE, acceptance_side

    m["_r86_carryover_notes_addendum"] = notes
    m["_r87_manifest_note"] = (
        "Built for R87 from runs/round86 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r82_carryover_notes_addendum == 3, "
        "_r83_carryover_notes_addendum == 0, "
        "_r84_carryover_notes_addendum == 0 and "
        "_r85_carryover_notes_addendum == 12); "
        "_r86_carryover_notes_addendum NEW with 45 items -- the R86 "
        "partial-upheld platform-side set compiled in "
        "data/manifest-carryover-r86-addendum.md s.3.1 (data/"
        "case-annotations-r86.json: 238 total, verdicts 14/187/35/2, "
        "55 new registrations in R86; layer list asserted equal to the "
        "published new_cases_r86 platform list); the R86 partial-upheld "
        "acceptance-side set (holdout29: CYJ-001, CYJ-002, CYJ-004, "
        "CYJ-005, ZW-015) is not in dev cases and per the R83 precedent "
        "does not enter the dev manifest layer -- asserted as exactly "
        "that 5-id set, registered here only. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r86_carryover_notes_addendum"]) == 45
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes), "| acceptance side", len(acceptance_side))


if __name__ == "__main__":
    main()
