#!/usr/bin/env python3
"""R94 host tooling: build runs/round94/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round93 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82 == 3, _r83 == 0, _r84 == 0, _r85 == 12,
  _r86 == 45, _r87 == 43, _r88 == 0, _r89 == 6, _r90 == 7,
  _r91 == 103, _r92 == 12).
- _r93_carryover_notes_addendum NEW with 5 items: the R93 factual
  registrations compiled in data/manifest-carryover-r93-addendum.md s.3
  (candidates 1-5). WHY-112 text taken verbatim from the
  manifest_carry_suggestion field of data/case-annotations-r93.json;
  the four round-level items take the addendum s.3.2-3.5 carry
  sentences verbatim (full lines captured from the addendum file,
  prefix "承接建议：" stripped). R93 had no partial-upheld per-case
  platform registrations (0 new partial-upheld), so the layer holds
  these 5 registration items only.
- _r94_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round93/judging/outcome-manifest.json"
ANN93 = P3 / "data/case-annotations-r93.json"
ADD93 = P3 / "data/manifest-carryover-r93-addendum.md"
OUT = P3 / "runs/round94/judging/outcome-manifest.json"

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
}

ROUND_KEYS = [
    ("HOLDOUT34-SEAL", "holdout34 封存成立"),
    ("ZIWEI-SUPPLY-BATCH3", "紫微第三批"),
    ("SECTION8-MONITORING-R93", "第八节执行面监测"),
    ("W56", "W56 不可判定"),
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
    assert "_r93_carryover_notes_addendum" not in m

    ann = json.loads(ANN93.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 532, ann["counts"]["cases_total"]
    assert ann["counts"]["new_registrations_r93"] == 3

    notes = {}
    for a in ann["annotations"]:
        if a["case_id"] == "WHY-112" and a.get("registered_round") == 93:
            notes["WHY-112"] = a["manifest_carry_suggestion"]
    assert "WHY-112" in notes and notes["WHY-112"].strip()

    lines = ADD93.read_text(encoding="utf-8").splitlines()
    carry = [ln.strip() for ln in lines
             if ln.strip().startswith("- 承接建议：自 R94 起承接本 R93 登记")]
    assert len(carry) == 4, len(carry)
    for key, marker in ROUND_KEYS:
        hits = [ln for ln in carry if marker in ln]
        assert len(hits) == 1, (key, len(hits))
        notes[key] = hits[0][len("- 承接建议："):]
    assert len(notes) == 5, len(notes)
    for k, v in notes.items():
        assert v.strip() and "R94" in v, k

    m["_r93_carryover_notes_addendum"] = notes
    m["_r94_manifest_note"] = (
        "Built for R94 from runs/round93 manifest: cases payload verbatim "
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
        "_r91_carryover_notes_addendum == 103 and "
        "_r92_carryover_notes_addendum == 12); "
        "_r93_carryover_notes_addendum NEW with 5 items -- the R93 "
        "factual registrations compiled in data/"
        "manifest-carryover-r93-addendum.md s.3 (candidates 1-5: "
        "WHY-112 errata, holdout34 seal fact, ziwei supply batch 3, "
        "section-8 execution monitoring counts, W56 conclusion). "
        "WHY-112 text taken verbatim from the manifest_carry_suggestion "
        "field of data/case-annotations-r93.json (532 total, 3 new "
        "registrations in R93, none partial-upheld per-case); the four "
        "round-level texts taken verbatim from the addendum carry "
        "sentences. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r93_carryover_notes_addendum"]) == 5
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes))


if __name__ == "__main__":
    main()
