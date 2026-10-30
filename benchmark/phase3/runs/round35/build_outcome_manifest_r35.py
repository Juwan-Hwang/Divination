#!/usr/bin/env python3
"""R35 host tooling: build the explicit outcome source manifest.

Per R35 PREREG s.0/s.4: the manifest is the ONLY outcome source the R35
judging-packet builder may read. Construction:
  base  = runs/round34/judging/outcome-manifest.json (verified R34 manifest,
          itself reconstructed from R33 official packets, overlay-16 applied,
          plus the 9 MP corrections)
  apply = benchmark/phase3/data/outcome-errata-overlay.json in its CURRENT
          on-disk state (16 entries + any R35 s.6.1 additions merged by the
          host after data-verify rulings). Every overlay corrected_outcome is
          substituted over the base and then asserted verbatim in the result.
Assertions: 487 unique cases; overlay size reported; all overlay texts
verbatim in the output manifest.
No rglob / tree search anywhere.
Output: runs/round35/judging/outcome-manifest.json
"""
import json
from pathlib import Path

R35 = Path(__file__).resolve().parent
P3 = R35.parents[1]
R34_MANIFEST = P3 / "runs" / "round34" / "judging" / "outcome-manifest.json"
OVERLAY_PATH = P3 / "data" / "outcome-errata-overlay.json"
OUT = R35 / "judging" / "outcome-manifest.json"


def main():
    base = json.loads(R34_MANIFEST.read_text(encoding="utf-8"))
    cases = dict(base["cases"])
    assert len(cases) == 487, len(cases)

    overlay_raw = json.loads(OVERLAY_PATH.read_text(encoding="utf-8"))
    overlay = {k: (v["corrected_outcome"] if isinstance(v, dict) else v)
               for k, v in overlay_raw.items() if k != "_comment"}
    print(f"overlay entries: {len(overlay)}")

    changed = []
    for cid, corr in overlay.items():
        assert cid in cases, f"overlay case not in pool: {cid}"
        if cases[cid] != corr:
            changed.append(cid)
        cases[cid] = corr
    for cid, corr in overlay.items():
        assert cases[cid] == corr, f"overlay mismatch {cid}"
    print(f"overlay applied; entries differing from R34 manifest: {changed}")

    out = {
        "_provenance": (
            "Built 2026-10-30 for R35 from runs/round34/judging/"
            "outcome-manifest.json with data/outcome-errata-overlay.json "
            f"({len(overlay)} entries) applied verbatim; R35 s.6.1 additions "
            f"substituted for: {changed}. Authoritative for R35 packet "
            "building; no tree search permitted."
        ),
        "cases": cases,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"wrote {OUT} with {len(cases)} cases")


if __name__ == "__main__":
    main()
