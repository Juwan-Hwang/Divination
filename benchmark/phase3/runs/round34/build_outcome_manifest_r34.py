#!/usr/bin/env python3
"""R34 host tooling: build the explicit outcome source manifest (hygiene 1).

The manifest is the ONLY outcome source the R34 judging-packet builder may
read. It is reconstructed from the official R33 judging artefacts:
  runs/round33/judging/packetA.json + packetB.json  (overlay-16 applied texts)
  runs/round33/judging/packetMP.json               (9 corrected MP outcomes)
  runs/round33/judging/host-mapping.json           (anon -> case_id)
Assertions: 487 unique cases; overlay-16 texts match the overlay file
verbatim; the 9 corrected MP outcomes match packetMP verbatim; every
manifest outcome for MP-001..019 is NOT the natal-batch2 text (spot-checked
against expansion12/natal-batch2/cases.jsonl inequality).
Output: runs/round34/judging/outcome-manifest.json
"""
import json
from pathlib import Path

R34 = Path(__file__).resolve().parent
P3 = R34.parents[1]
R33J = P3 / "runs" / "round33" / "judging"


def load_items(name):
    return json.loads((R33J / name).read_text(encoding="utf-8"))


def main():
    hmap = json.loads((R33J / "host-mapping.json").read_text(encoding="utf-8"))
    outcomes = {}
    for name in ("packetA.json", "packetB.json"):
        for e in load_items(name):
            outcomes[hmap[e["anon_id"]]] = e["outcome_record"]
    assert len(outcomes) == 487, len(outcomes)
    mp_items = load_items("packetMP.json")
    assert len(mp_items) == 9
    for e in mp_items:
        outcomes[hmap[e["anon_id"]]] = e["outcome_record"]

    overlay_raw = json.loads(
        (P3 / "data" / "outcome-errata-overlay.json").read_text(encoding="utf-8"))
    overlay = {k: (v["corrected_outcome"] if isinstance(v, dict) else v)
               for k, v in overlay_raw.items() if k != "_comment"}
    assert len(overlay) == 16
    for cid, corr in overlay.items():
        assert outcomes[cid] == corr, f"overlay mismatch {cid}"
    print("overlay 16/16 verbatim in manifest")

    nb2 = {}
    for line in open(P3 / "expansion12/natal-batch2/cases.jsonl", encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            oc = r.get("outcome_record") or r.get("outcome")
            if isinstance(oc, str):
                nb2[r["id"]] = oc
    bad = [c for c in outcomes if c.startswith("MP-") and c in nb2
           and outcomes[c] == nb2[c]]
    assert not bad, f"manifest still carries natal-batch2 texts: {bad}"
    print("MP spot-check: no manifest outcome equals the natal-batch2 text")

    manifest = {
        "_provenance": (
            "Reconstructed 2026-10-30 from runs/round33 official judging "
            "packets (packetA/packetB, overlay-16 applied) with the 9 MP "
            "corrections from packetMP.json substituted; case keys via "
            "round33 host-mapping. Authoritative for R34 packet building; "
            "no tree search permitted."),
        "cases": {cid: outcomes[cid] for cid in sorted(outcomes)},
    }
    out = R34 / "judging" / "outcome-manifest.json"
    out.write_text(json.dumps(manifest, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    print(f"manifest written: {len(outcomes)} cases -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
