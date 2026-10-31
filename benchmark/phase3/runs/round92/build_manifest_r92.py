#!/usr/bin/env python3
"""R92 host tooling: build runs/round92/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round91 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82 == 3, _r83 == 0, _r84 == 0, _r85 == 12,
  _r86 == 45, _r87 == 43, _r88 == 0, _r89 == 6, _r90 == 7).
- _r91_carryover_notes_addendum NEW with 103 items: the R91
  partial-upheld PLATFORM-side registrations (see data/
  manifest-carryover-r91-addendum.md s.3), taken verbatim from the
  manifest_carry_suggestion field of data/case-annotations-r91.json
  (517 total: 465 compiled at platform close + 52 acceptance-side
  addendum registrations). R91 acceptance-side partial-upheld
  registrations (52 entries over the 28 holdout33 ids) are NOT dev
  cases and per the R83 precedent do not enter the dev manifest layer.
- _r92_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round91/judging/outcome-manifest.json"
ANN91 = P3 / "data/case-annotations-r91.json"
OUT = P3 / "runs/round92/judging/outcome-manifest.json"

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
}

EXPECTED_R91_ACCEPTANCE_IDS = {
    "BY-039", "BY-041", "BY-042", "BY-043", "BY-044", "BY-045", "BY-046",
    "DA-066", "DA-067", "DA-068", "DA-070", "DA-072", "DA-073", "DA-074",
    "WHY-092", "WHY-093", "WHY-095", "WHY-096", "WHY-098", "WHY-099",
    "WHY-100", "WHY-103", "WHY-104", "WHY-106", "WHY-107", "WHY-108",
    "WHY-109", "WHY-110",
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
    assert "_r91_carryover_notes_addendum" not in m

    ann = json.loads(ANN91.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 517, ann["counts"]["cases_total"]
    assert ann["counts"]["verdicts"] == {
        "成立": 14, "部分成立": 430, "不成立": 71, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_registrations_r91"] == 103
    assert ann["counts"]["new_registrations_r91_acceptance_addendum"] == 52
    expected_platform = sorted(ann["counts"]["r91_partial_upheld_platform"])
    assert len(expected_platform) == 103, len(expected_platform)

    notes = {}
    acceptance_side = set()
    n_acc_entries = 0
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 91:
            if a["case_id"] in cases:
                assert a["case_id"] not in notes, a["case_id"]
                notes[a["case_id"]] = a["manifest_carry_suggestion"]
            else:
                acceptance_side.add(a["case_id"])
                n_acc_entries += 1
    assert sorted(notes) == expected_platform, (
        sorted(set(expected_platform) ^ set(notes)))
    assert acceptance_side == EXPECTED_R91_ACCEPTANCE_IDS, acceptance_side
    assert n_acc_entries == 52, n_acc_entries

    m["_r91_carryover_notes_addendum"] = notes
    m["_r92_manifest_note"] = (
        "Built for R92 from runs/round91 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r82_carryover_notes_addendum == 3, "
        "_r83_carryover_notes_addendum == 0, "
        "_r84_carryover_notes_addendum == 0, "
        "_r85_carryover_notes_addendum == 12, "
        "_r86_carryover_notes_addendum == 45, "
        "_r87_carryover_notes_addendum == 43, "
        "_r88_carryover_notes_addendum == 0, "
        "_r89_carryover_notes_addendum == 6 and "
        "_r90_carryover_notes_addendum == 7); "
        "_r91_carryover_notes_addendum NEW with 103 items -- the R91 "
        "partial-upheld platform-side registrations (compiled in data/"
        "manifest-carryover-r91-addendum.md s.3; data/"
        "case-annotations-r91.json: 517 total, verdicts 14/430/71/2, "
        "103 new platform registrations in R91 plus 52 acceptance-side "
        "addendum registrations). The R91 acceptance-side partial-upheld "
        "registrations (52 entries over the 28 holdout33 ids) do not "
        "enter the dev layer per the R83 precedent. Note text taken "
        "verbatim (full capture) from the manifest_carry_suggestion "
        "fields of case-annotations-r91.json. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r91_carryover_notes_addendum"]) == 103
    for cid, txt in back["_r91_carryover_notes_addendum"].items():
        assert txt.strip() and "部分成立" in txt, cid
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes), "| acceptance side ids", len(acceptance_side),
          "| acceptance entries", n_acc_entries)


if __name__ == "__main__":
    main()
