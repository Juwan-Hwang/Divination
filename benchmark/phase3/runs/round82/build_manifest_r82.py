#!/usr/bin/env python3
"""R82 host tooling: build runs/round82/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round81 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r80_carryover_notes_addendum == 1).
- _r81_carryover_notes_addendum NEW: R81 adjudication partial-upheld
  platform items = 14: the 13 platform cases with registered_round == 81
  and disposition partial-upheld in data/case-annotations-r81.json
  (manifest_carry_suggestion verbatim, structured read) + AS-307
  same-case re-adjudication whose R82 layer text is the verbatim text
  written in data/manifest-carryover-r81-addendum.md s.3.1.
  The 11 acceptance-side partial items of R81 (DS-020, QM-307, GSZ-047,
  ZCB-014, QM-031, GSZ-052, GSZ-060, GSZ-049, GSZ-053, GSZ-058, GSZ-061)
  are NOT dev-manifest cases; per the addendum they are carried by the
  gold/acceptance note layer, not this manifest, and are asserted to be
  exactly the non-case remainder.
- _r82_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round81/judging/outcome-manifest.json"
ANN81 = P3 / "data/case-annotations-r81.json"
ADD81 = P3 / "data/manifest-carryover-r81-addendum.md"
OUT = P3 / "runs/round82/judging/outcome-manifest.json"

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
}

EXPECTED_NEW_PARTIAL_R81 = [
    "LY-528", "BZ-042", "LY-416", "LY-105", "LY-332", "LY-624",
    "LY-423", "BZ-105", "LR3-116", "YM-069", "LY-602", "OC-009",
    "LR2-024", "DS-020", "QM-307", "GSZ-047", "ZCB-014", "QM-031",
    "GSZ-052", "GSZ-060", "GSZ-049", "GSZ-053", "GSZ-058", "GSZ-061",
]
EXPECTED_ACCEPTANCE_SIDE = {
    "DS-020", "QM-307", "GSZ-047", "ZCB-014", "QM-031", "GSZ-052",
    "GSZ-060", "GSZ-049", "GSZ-053", "GSZ-058", "GSZ-061",
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
    assert "_r81_carryover_notes_addendum" not in m

    ann = json.loads(ANN81.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 121, ann["counts"]
    assert ann["counts"]["verdicts"] == {
        "成立": 12, "部分成立": 101, "不成立": 6, "未核": 2,
    }, ann["counts"]["verdicts"]
    assert ann["counts"]["new_partial_cases_r81"] == EXPECTED_NEW_PARTIAL_R81
    assert ann["counts"]["new_registrations_r81"] == 24

    notes = {}
    acceptance_side = set()
    for a in ann["annotations"]:
        if a["disposition"] == "部分成立" and a.get("registered_round") == 81:
            assert a["manifest_carry_suggestion"], a["case_id"]
            if a["case_id"] in cases:
                notes[a["case_id"]] = a["manifest_carry_suggestion"]
            else:
                acceptance_side.add(a["case_id"])
    assert acceptance_side == EXPECTED_ACCEPTANCE_SIDE, acceptance_side
    assert len(notes) == 13, sorted(notes)

    # AS-307 same-case re-adjudication: R82 layer text verbatim from the
    # R81 addendum s.3.1 (structured capture of the quoted suggestion).
    add = ADD81.read_text(encoding="utf-8")
    mt = re.search(
        r"承接注记建议文本（供 R82 manifest 落实，原文）：「(.+?)」",
        add,
        re.S,
    )
    assert mt, "AS-307 s.3.1 text not found in addendum"
    as307_text = mt.group(1)
    assert "自 R82 起承接本 R81 标注" in as307_text
    assert "AS-307" in cases
    notes["AS-307"] = as307_text
    assert len(notes) == 14, sorted(notes)

    m["_r81_carryover_notes_addendum"] = notes
    m["_r82_manifest_note"] = (
        "Built for R82 from runs/round81 manifest: cases payload verbatim "
        "for all 487 cases (LR2-016 split state preserved); all prior "
        "layers preserved verbatim (sizes asserted, including "
        "_r80_carryover_notes_addendum == 1); "
        "_r81_carryover_notes_addendum NEW with 14 platform items = R81 "
        "adjudication partial-upheld platform cases (13 with "
        "registered_round == 81 in data/case-annotations-r81.json, "
        "structured read, counts asserted equal to R81 published "
        "distribution 12/101/6/2, total 121) + AS-307 same-case "
        "re-adjudication text verbatim from "
        "data/manifest-carryover-r81-addendum.md s.3.1; the 11 "
        "acceptance-side partial items are not dev-manifest cases and "
        "are carried by the gold/acceptance note layer per the addendum. "
        "No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes), sorted(notes))


if __name__ == "__main__":
    main()
