#!/usr/bin/env python3
"""R78 host tooling: build runs/round78/judging/outcome-manifest.json.

Per STAGE-SUMMARY-62 s.3 item 1: R78 has NO new carryover layer (the R77
addendum compilation is the empty set: R77 produced no new adjudications).
This build therefore carries the R77 manifest verbatim (cases payload and
every prior layer untouched, LR2-016 split state preserved) and appends
only a _r78_manifest_note recording the empty-set fact and this round's
provenance. No outcome strings changed; no scores touched.
"""
import hashlib
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SRC = P3 / "runs/round77/judging/outcome-manifest.json"
OUT = P3 / "runs/round78/judging/outcome-manifest.json"
EXPECTED_CASES_SHA = "00f362bd8e4b55ceff31502cb5f7e8239855b1f806a7b1495284af80186a31ad"


def cases_sha(cases):
    return hashlib.sha256(
        json.dumps(cases, ensure_ascii=False, sort_keys=True).encode()
    ).hexdigest()


def main():
    m = json.loads(SRC.read_text(encoding="utf-8"))
    assert len(m["cases"]) == 487, len(m["cases"])
    assert cases_sha(m["cases"]) == EXPECTED_CASES_SHA, "cases payload drift"
    assert "_r78_carryover_notes_addendum" not in m
    m["_r78_manifest_note"] = (
        "R78: no new carryover layer. R77 adjudication produced no new "
        "partial-upheld items (R77 addendum compilation is the empty set, "
        "data/manifest-carryover-r77-addendum.md cross-verified 6/6 carried "
        "items were the R76 set already layered in _r77). All R77 layers "
        "carried verbatim; cases payload identical (sha asserted)."
    )
    OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
    print("written", OUT)
    print("sha256", hashlib.sha256(OUT.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
