#!/usr/bin/env python3
"""R86 host tooling: build runs/round86/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round85 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82_carryover_notes_addendum == 3,
  _r83_carryover_notes_addendum == 0 and
  _r84_carryover_notes_addendum == 0).
- _r85_carryover_notes_addendum NEW with 12 items: the R85 partial-upheld
  platform-side set compiled in data/manifest-carryover-r85-addendum.md
  s.3.2 (AS-004, OC-026, LR3-107, YY2-003, YM-068, LY-443, YM-059,
  LY-203, LY-028, LY-231, LY-539, LY-517), derived here from
  data/case-annotations-r85.json (disposition partial-upheld,
  registered_round == 85) and asserted equal to the published layer list
  ann['counts']['r85_layer_partial_upheld']. R85 had no acceptance-side
  adjudications (no unsealing in R85), so the acceptance side set is
  asserted empty.
- _r86_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round85/judging/outcome-manifest.json"
ANN85 = P3 / "data/case-annotations-r85.json"
OUT = P3 / "runs/round86/judging/outcome-manifest.json"

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
}

EXPECTED_R85_LAYER = [
    "AS-004", "OC-026", "LR3-107", "YY2-003", "YM-068", "LY-443",
    "YM-059", "LY-203", "LY-028", "LY-231", "LY-539", "LY-517",
]


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
    assert "_r85_carryover_notes_addendum" not in m

    ann = json.loads(ANN85.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 183, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 14, "部分成立": 137, "不成立": 30, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_registrations_r85"] == 19
    assert ann["counts"]["r85_layer_partial_upheld"] == EXPECTED_R85_LAYER

    notes = {}
    acceptance_side = set()
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 85:
            if a["case_id"] in cases:
                notes[a["case_id"]] = a["manifest_carry_suggestion"]
            else:
                acceptance_side.add(a["case_id"])
    assert sorted(notes) == sorted(EXPECTED_R85_LAYER), sorted(notes)
    assert acceptance_side == set(), acceptance_side

    m["_r85_carryover_notes_addendum"] = notes
    m["_r86_manifest_note"] = (
        "Built for R86 from runs/round85 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r82_carryover_notes_addendum == 3, "
        "_r83_carryover_notes_addendum == 0 and "
        "_r84_carryover_notes_addendum == 0); "
        "_r85_carryover_notes_addendum NEW with 12 items -- the R85 "
        "partial-upheld platform-side set compiled in "
        "data/manifest-carryover-r85-addendum.md s.3.2 (data/"
        "case-annotations-r85.json: 183 total, verdicts 14/137/30/2, "
        "19 new registrations in R85; layer list asserted equal to the "
        "published r85_layer_partial_upheld list); R85 had no acceptance "
        "side (no unsealing), asserted empty. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r85_carryover_notes_addendum"]) == 12
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes), "| acceptance side", len(acceptance_side))


if __name__ == "__main__":
    main()
