#!/usr/bin/env python3
"""R95 host tooling: build runs/round95/judging/outcome-manifest.json.

Layers:
- cases payload verbatim from runs/round94 manifest (487 cases; LR2-016
  split state and all prior note layers preserved untouched, sizes
  asserted including _r82 == 3, _r83 == 0, _r84 == 0, _r85 == 12,
  _r86 == 45, _r87 == 43, _r88 == 0, _r89 == 6, _r90 == 7,
  _r91 == 103, _r92 == 12, _r93 == 5).
- _r94_carryover_notes_addendum NEW with 7 items: the R94 registrations
  compiled in data/manifest-carryover-r94-addendum.md s.3 (candidates
  1-7). Per-case texts (AS-210 / BY-049 / WHY-115, all partial-upheld,
  registered_round == 94) taken verbatim from the
  manifest_carry_suggestion fields of data/case-annotations-r94.json;
  the four round-level items take the addendum s.3.4 carry sentences
  verbatim (captured from the "承接建议：" marker to end of line).
- _r95_manifest_note records the build.
No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round94/judging/outcome-manifest.json"
ANN94 = P3 / "data/case-annotations-r94.json"
ADD94 = P3 / "data/manifest-carryover-r94-addendum.md"
OUT = P3 / "runs/round95/judging/outcome-manifest.json"

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
}

ROUND_KEYS = [
    ("SECTION8-MONITORING-R94", "候选四：第八节执行面监测计数"),
    ("HOLDOUT34-OPENED", "候选五：holdout34 开封事实"),
    ("W57", "候选六：W57 结论"),
    ("SUPPLY-RECOUNT-R94", "候选七：供给复算"),
]

CASE_KEYS = ["AS-210", "BY-049", "WHY-115"]


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
    assert "_r94_carryover_notes_addendum" not in m

    ann = json.loads(ANN94.read_text(encoding="utf-8"))
    assert ann["counts"]["cases_total"] == 535, ann["counts"]["cases_total"]
    assert ann["counts"]["new_registrations_r94"] == 3

    notes = {}
    for a in ann["annotations"]:
        if a["case_id"] in CASE_KEYS and a.get("registered_round") == 94:
            notes[a["case_id"]] = a["manifest_carry_suggestion"]
    assert sorted(notes) == sorted(CASE_KEYS), sorted(notes)
    for k, v in notes.items():
        assert v.strip() and "R95" in v, k

    lines = ADD94.read_text(encoding="utf-8").splitlines()
    for key, marker in ROUND_KEYS:
        hits = [ln for ln in lines if marker in ln and "承接建议：" in ln]
        assert len(hits) == 1, (key, len(hits))
        seg = hits[0].split("承接建议：", 1)[1].strip()
        assert seg.startswith("自 R95 起承接本 R94 登记"), (key, seg[:30])
        notes[key] = seg
    assert len(notes) == 7, len(notes)

    m["_r94_carryover_notes_addendum"] = notes
    m["_r95_manifest_note"] = (
        "Built for R95 from runs/round94 manifest: cases payload verbatim "
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
        "_r92_carryover_notes_addendum == 12 and "
        "_r93_carryover_notes_addendum == 5); "
        "_r94_carryover_notes_addendum NEW with 7 items -- the R94 "
        "registrations compiled in data/"
        "manifest-carryover-r94-addendum.md s.3 (candidates 1-7: "
        "AS-210 / BY-049 / WHY-115 partial-upheld registrations, "
        "section-8 execution monitoring counts, holdout34 opening "
        "fact, W57 conclusion, supply recount). Per-case texts taken "
        "verbatim from the manifest_carry_suggestion fields of data/"
        "case-annotations-r94.json (535 total, 3 new registrations "
        "in R94); the four round-level texts taken verbatim from the "
        "addendum carry sentences. No scores changed."
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")

    back = json.loads(OUT.read_text(encoding="utf-8"))
    assert len(back["_r94_carryover_notes_addendum"]) == 7
    raw = OUT.read_bytes()
    print("written", OUT)
    print("sha256", hashlib.sha256(raw).hexdigest())
    print("layer items", len(notes))


if __name__ == "__main__":
    main()
