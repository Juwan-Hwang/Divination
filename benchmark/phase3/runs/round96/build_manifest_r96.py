#!/usr/bin/env python3
"""R96 host tooling: build runs/round96/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round95 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82 == 3, _r83 == 0, _r84 == 0, _r85 == 12,
  _r86 == 45, _r87 == 43, _r88 == 0, _r89 == 6, _r90 == 7,
  _r91 == 103, _r92 == 12, _r93 == 5, _r94 == 7).
- _r95_carryover_notes_addendum NEW with 8 items: the R95 registrations
  compiled in data/manifest-carryover-r95-addendum.md s.3 (candidate 1
  per-case LY-245 plus seven round-level candidates 2-8). Per-case text
  (LY-245, partial-upheld, registered_round == 95) taken verbatim from
  the manifest_carry_suggestion field of data/case-annotations-r95.json;
  the seven round-level items take the addendum s.3.2 carry sentences
  verbatim (captured from the "承接建议：" marker to end of line).
- _r96_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round95/judging/outcome-manifest.json"
ANN95 = P3 / "data/case-annotations-r95.json"
ADD95 = P3 / "data/manifest-carryover-r95-addendum.md"
OUT = P3 / "runs/round96/judging/outcome-manifest.json"

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
    "_r92_carryover_notes_addendum": 12,
    "_r93_carryover_notes_addendum": 5,
    "_r94_carryover_notes_addendum": 7,
}

ROUND_KEYS = [
    ("SECTION8-MONITORING-R95", "候选二：第八节执行面监测计数"),
    ("PLATFORM-STAND-R95", "候选三：平台三项全立"),
    ("JUDGE-VOID-RESEAT-R95", "候选四：评审首派作废与重派定稿"),
    ("SUPPLY-RECOUNT-R95", "候选五：供给复算"),
    ("HOLDOUT35-DEFERRED-R95", "候选六：holdout35 未组集顺延"),
    ("W58", "候选七：W58 结论"),
    ("REVISION-B-R95", "候选八：修订裁定 (B)"),
]

CASE_KEYS = ["LY-245"]


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
    assert "_r95_carryover_notes_addendum" not in m

    ann = json.loads(ANN95.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 541, ann["counts"]["cases_total"]
    assert ann["counts"]["new_registrations_r95"] == 6

    notes = {}
    for a in ann["annotations"]:
        if a["case_id"] in CASE_KEYS and a.get("registered_round") == 95:
            notes[a["case_id"]] = a["manifest_carry_suggestion"]
    assert sorted(notes) == sorted(CASE_KEYS), sorted(notes)
    for k, v in notes.items():
        assert v.strip() and "R96" in v, k

    lines = ADD95.read_text(encoding="utf-8").splitlines()
    for key, marker in ROUND_KEYS:
        hits = [ln for ln in lines if marker in ln and "承接建议：" in ln]
        assert len(hits) == 1, (key, len(hits))
        seg = hits[0].split("承接建议：", 1)[1].strip()
        assert seg.startswith("自 R96 起承接本 R95 登记"), (key, seg[:30])
        notes[key] = seg
    assert len(notes) == 8, len(notes)

    m["_r95_carryover_notes_addendum"] = notes
    m["_r96_manifest_note"] = (
        "Built for R96 from runs/round95 manifest: cases payload verbatim "
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
        "_r90_carryover_notes_addendum == 7, "
        "_r91_carryover_notes_addendum == 103, "
        "_r92_carryover_notes_addendum == 12, "
        "_r93_carryover_notes_addendum == 5 and "
        "_r94_carryover_notes_addendum == 7); "
        "_r95_carryover_notes_addendum NEW with 8 items -- the R95 "
        "registrations compiled in data/"
        "manifest-carryover-r95-addendum.md s.3 (candidate 1: LY-245 "
        "partial-upheld registration; candidates 2-8 round-level: "
        "section-8 execution monitoring counts, platform all-stand, "
        "judge first-dispatch void and re-seat, supply recount, "
        "holdout35 deferral, W58 conclusion, revision verdict (B)). "
        "Per-case text taken verbatim from the manifest_carry_suggestion "
        "field of data/case-annotations-r95.json (541 total, 6 new "
        "registrations in R95); the seven round-level texts taken "
        "verbatim from the addendum carry sentences. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r95_carryover_notes_addendum"]) == 8
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes))


if __name__ == "__main__":
    main()
