#!/usr/bin/env python3
"""R93 host tooling: build runs/round93/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round92 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82 == 3, _r83 == 0, _r84 == 0, _r85 == 12,
  _r86 == 45, _r87 == 43, _r88 == 0, _r89 == 6, _r90 == 7,
  _r91 == 103).
- _r92_carryover_notes_addendum NEW with 12 items: the R92
  partial-upheld PLATFORM-side registrations (see data/
  manifest-carryover-r92-addendum.md s.3), taken verbatim from the
  manifest_carry_suggestion field of data/case-annotations-r92.json
  (529 total: 517 carried + 12 new platform registrations in R92;
  R92 had no acceptance opening, so there is no acceptance side).
- _r93_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round92/judging/outcome-manifest.json"
ANN92 = P3 / "data/case-annotations-r92.json"
OUT = P3 / "runs/round93/judging/outcome-manifest.json"

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
    "_r88_carryover_notes_addendum": 0,
    "_r89_carryover_notes_addendum": 6,
    "_r90_carryover_notes_addendum": 7,
    "_r91_carryover_notes_addendum": 103,
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
    assert "_r92_carryover_notes_addendum" not in m

    ann = json.loads(ANN92.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 529, ann["counts"]["cases_total"]
    assert ann["counts"]["new_registrations_r92"] == 12
    expected_platform = sorted(ann["counts"]["r92_partial_upheld_platform"])
    assert len(expected_platform) == 12, len(expected_platform)

    notes = {}
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 92:
            assert a["case_id"] in cases, a["case_id"]
            assert a["case_id"] not in notes, a["case_id"]
            notes[a["case_id"]] = a["manifest_carry_suggestion"]
    assert sorted(notes) == expected_platform, (
        sorted(set(expected_platform) ^ set(notes)))

    m["_r92_carryover_notes_addendum"] = notes
    m["_r93_manifest_note"] = (
        "Built for R93 from runs/round92 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r82_carryover_notes_addendum == 3, "
        "_r83_carryover_notes_addendum == 0, "
        "_r84_carryover_notes_addendum == 0, "
        "_r85_carryover_notes_addendum == 12, "
        "_r86_carryover_notes_addendum == 45, "
        "_r87_carryover_notes_addendum == 43, "
        "_r88_carryover_notes_addendum == 0, "
        "_r89_carryover_notes_addendum == 6, "
        "_r90_carryover_notes_addendum == 7 and "
        "_r91_carryover_notes_addendum == 103); "
        "_r92_carryover_notes_addendum NEW with 12 items -- the R92 "
        "partial-upheld platform-side registrations (compiled in data/"
        "manifest-carryover-r92-addendum.md s.3; data/"
        "case-annotations-r92.json: 529 total, 12 new platform "
        "registrations in R92; R92 had no acceptance opening so there "
        "is no acceptance side). Note text taken verbatim (full "
        "capture) from the manifest_carry_suggestion fields of "
        "case-annotations-r92.json. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r92_carryover_notes_addendum"]) == 12
    for cid, txt in back["_r92_carryover_notes_addendum"].items():
        assert txt.strip() and "部分成立" in txt, cid
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes))


if __name__ == "__main__":
    main()
