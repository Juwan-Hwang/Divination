#!/usr/bin/env python3
"""R90 host tooling: build runs/round90/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round89 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82_carryover_notes_addendum == 3,
  _r83_carryover_notes_addendum == 0,
  _r84_carryover_notes_addendum == 0,
  _r85_carryover_notes_addendum == 12,
  _r86_carryover_notes_addendum == 45,
  _r87_carryover_notes_addendum == 43 and
  _r88_carryover_notes_addendum == 0).
- _r89_carryover_notes_addendum NEW with 6 items: the R89 partial-upheld
  PLATFORM-side registrations (LY-525, LY-527, LY-529, LY-530, LY-532,
  LY-538 -- B15+B16 seat card-damage self-reports verified against the
  original cards; see data/manifest-carryover-r89-addendum.md s.3.1),
  taken verbatim from the manifest_carry_suggestion field of
  data/case-annotations-r89.json. R89 had no acceptance-side new
  registrations (holdout32 not unsealed in R89).
- _r90_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round89/judging/outcome-manifest.json"
ANN89 = P3 / "data/case-annotations-r89.json"
OUT = P3 / "runs/round90/judging/outcome-manifest.json"

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
}

EXPECTED_R89_PARTIAL_PLATFORM = ["LY-525", "LY-527", "LY-529", "LY-530", "LY-532", "LY-538"]


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
    assert "_r89_carryover_notes_addendum" not in m

    ann = json.loads(ANN89.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 321, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 14, "部分成立": 244, "不成立": 61, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_registrations_r89"] == 12
    assert sorted(ann["counts"]["r89_partial_upheld_platform"]) == EXPECTED_R89_PARTIAL_PLATFORM

    notes = {}
    acceptance_side = set()
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 89:
            if a["case_id"] in cases:
                notes[a["case_id"]] = a["manifest_carry_suggestion"]
            else:
                acceptance_side.add(a["case_id"])
    assert sorted(notes) == EXPECTED_R89_PARTIAL_PLATFORM, sorted(notes)
    assert acceptance_side == set(), acceptance_side

    m["_r89_carryover_notes_addendum"] = notes
    m["_r90_manifest_note"] = (
        "Built for R90 from runs/round89 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r82_carryover_notes_addendum == 3, "
        "_r83_carryover_notes_addendum == 0, "
        "_r84_carryover_notes_addendum == 0, "
        "_r85_carryover_notes_addendum == 12, "
        "_r86_carryover_notes_addendum == 45, "
        "_r87_carryover_notes_addendum == 43 and "
        "_r88_carryover_notes_addendum == 0); "
        "_r89_carryover_notes_addendum NEW with 6 items -- the R89 "
        "partial-upheld platform-side registrations (LY-525, LY-527, "
        "LY-529, LY-530, LY-532, LY-538; B15+B16 seat card-damage "
        "self-reports verified per-case against the original cards; "
        "compiled in data/manifest-carryover-r89-addendum.md s.3.1; data/"
        "case-annotations-r89.json: 321 total, verdicts 14/244/61/2, "
        "12 new registrations in R89, all platform-side; R89 had no "
        "acceptance-side new registrations because holdout32 was not "
        "unsealed). Note text taken verbatim (full capture) from the "
        "manifest_carry_suggestion fields of case-annotations-r89.json. "
        "No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r89_carryover_notes_addendum"]) == 6
    for cid, txt in back["_r89_carryover_notes_addendum"].items():
        assert txt.strip() and "部分成立" in txt, cid
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes), "| acceptance side", len(acceptance_side))


if __name__ == "__main__":
    main()
