#!/usr/bin/env python3
"""R37 host tooling: build the explicit outcome source manifest with
PREREG s.6 predicate-hygiene stripping (judging side only).

Base = runs/round36/judging/outcome-manifest.json (487 cases, overlay-16
already applied verbatim -- asserted before any change).
Apply data-verify/strip-spec_r37.json (72 A-class cases, substrings
verified unique by the data seat). Host ruling for the single ESCALATE
case LR2-024: apply the spec's candidate sub-clause strip (rationale in
data-verify/HYGIENE-STRIP-LOG.md).
Overlay precedence (PREREG s.6): if an overlay case is also in the
72-case strip list, its final outcome is the overlay corrected text
verbatim (strip not applied); the overlap is logged.
Outputs: judging/outcome-manifest.json (cases + stripped_tail),
data-verify/hygiene-strip-log_r37.json (machine log).
No rglob / tree search anywhere.
"""
import json
from pathlib import Path

R37 = Path(__file__).resolve().parent
P3 = R37.parents[1]
R36_MANIFEST = P3 / "runs" / "round36" / "judging" / "outcome-manifest.json"
OVERLAY_PATH = P3 / "data" / "outcome-errata-overlay.json"
SPEC_PATH = R37 / "data-verify" / "strip-spec_r37.json"
OUT = R37 / "judging" / "outcome-manifest.json"
LOG = R37 / "data-verify" / "hygiene-strip-log_r37.json"


def main():
    base = json.loads(R36_MANIFEST.read_text(encoding="utf-8"))
    cases = dict(base["cases"])
    assert len(cases) == 487, len(cases)

    overlay_raw = json.loads(OVERLAY_PATH.read_text(encoding="utf-8"))
    overlay = {k: (v["corrected_outcome"] if isinstance(v, dict) else v)
               for k, v in overlay_raw.items() if k != "_comment"}
    assert len(overlay) == 16, len(overlay)
    for cid, corr in overlay.items():
        assert cases[cid] == corr, f"base manifest overlay mismatch {cid}"
    print("base: overlay 16/16 verbatim in R36 manifest")

    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    assert len(spec) == 72, len(spec)

    overlap = sorted(set(spec) & set(overlay))
    print(f"overlay cases inside strip list: {overlap}")

    stripped_tail, log = {}, []
    for cid in sorted(spec):
        entry = spec[cid]
        original = cases[cid]
        if cid in overlay:
            # overlay precedence: keep overlay text, strip not applied
            stripped_tail[cid] = ""
            log.append({"case_id": cid, "type": entry["type"],
                        "action": "overlay-precedence-no-strip",
                        "removed_chars": 0})
            continue
        text = original
        removed_parts = []
        for sub in entry["remove"]:
            assert text.count(sub) == 1, f"{cid}: substring count {text.count(sub)} != 1"
            text = text.replace(sub, "", 1)
            removed_parts.append(sub)
        text = text.strip()
        assert text, f"{cid}: empty after strip"
        cases[cid] = text
        stripped_tail[cid] = "".join(removed_parts)
        log.append({"case_id": cid, "type": entry["type"],
                    "action": "host-ruling-candidate-strip" if cid == "LR2-024" else "stripped",
                    "removed_chars": sum(len(s) for s in removed_parts),
                    "n_substrings": len(removed_parts)})

    for cid, corr in overlay.items():
        assert cases[cid] == corr, f"final overlay mismatch {cid}"
    print("final: overlay 16/16 verbatim")

    out = {
        "_provenance": (
            "Built 2026-10-30 for R37 from runs/round36/judging/"
            "outcome-manifest.json with PREREG s.6 predicate-hygiene "
            "stripping applied per data-verify/strip-spec_r37.json "
            "(72 A-class cases; LR2-024 by host ruling candidate strip; "
            "overlay-16 precedence preserved verbatim). Authoritative "
            "for R37 packet building; no tree search permitted."
        ),
        "cases": cases,
        "stripped_tail": stripped_tail,
    }
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    LOG.write_text(json.dumps({"overlap_overlay": overlap, "entries": log},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    n_stripped = sum(1 for e in log if e["action"] == "stripped")
    n_host = sum(1 for e in log if e["action"] == "host-ruling-candidate-strip")
    n_ov = sum(1 for e in log if e["action"] == "overlay-precedence-no-strip")
    print(f"wrote manifest: 487 cases; stripped {n_stripped}, "
          f"host-ruling {n_host}, overlay-precedence {n_ov}")


if __name__ == "__main__":
    main()
