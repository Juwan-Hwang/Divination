#!/usr/bin/env python3
"""R79 host tooling: build runs/round79/judging/outcome-manifest.json.

R79 has NO new carryover layer: the R78 addendum compilation is the
empty set (R78 produced no new adjudications; R78 annotations carried
the 70-item set with an empty new-adjudication set, per R78 REPORT s.5
and data/manifest-carryover-r78-addendum.md). This build therefore
carries the R78 manifest verbatim (cases payload and every prior layer
untouched, LR2-016 split state preserved) and appends only a
_r79_manifest_note recording the empty-set fact and this round's
provenance. No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round78/judging/outcome-manifest.json"
OUT = P3 / "runs/round79/judging/outcome-manifest.json"
EXPECTED_CASES_SHA = "00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad"


def cases_sha(cases):
    return hashlib.sha256(
        json.dumps(cases, ensure_ascii=False, sort_keys=True).encode()
    ).hexdigest()


def main():
    m = json.loads(SRC.read_text(encoding="utf-8"))
    assert len(m["cases"]) == 487, len(m["cases"])
    assert cases_sha(m["cases"]) == EXPECTED_CASES_SHA, "cases payload drift"
    assert "_r79_carryover_notes_addendum" not in m
    m["_r79_manifest_note"] = (
        "R79: no new carryover layer. R78 adjudication produced no new "
        "partial-upheld items (R78 addendum compilation is the empty set, "
        "data/manifest-carryover-r78-addendum.md; R78 annotations carried "
        "70 items with an empty new-adjudication set). All R78 layers "
        "carried verbatim; cases payload identical (sha asserted)."
    )
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
    print("sha256", hashlib.sha256(OUT.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
