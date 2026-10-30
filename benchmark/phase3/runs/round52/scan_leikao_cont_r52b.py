#!/usr/bin/env python3
"""R52 leikao-cont seat (second seat) stage-2 scan: scans ALL input cards present in
cards-mining-leikao-r52/ with the R42-lineage marker sets (verbatim from build_cards_leikao_r52.py).
This seat built 0 new cards (no A+low candidate in PDF 234-276 range); scan verifies the
directory still contains only the pre-existing LK2-C48/C51 inputs and both are 0-hit.
Unique name, this round only."""
import json, pathlib

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "digestion" / "cards-mining-leikao-r52"
LEVEL1 = ["断语线索","断曰","断語","正议","正議","验语","驗語","断语：","斷語：","占断","占斷","大师断","大師斷"]
LEVEL2 = ["果验","果然","果應","后验","後驗","结局","結局","应验","應驗"]
FIELD_BLACKLIST = ["断语","断曰","正议","验语","占断","线索","断者","grade","contamination","outcome"]
WHITELIST = {"id","tradition","subject","context","question","setting","provenance","redistributable","license_status"}

def walk(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield (path + "/" + k, k, True)
            yield from walk(v, path + "/" + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        yield (path, obj, False)

report = {}
total = 0
ids_present = []
for p in sorted(OUT.glob("*-input.json")):
    data = json.loads(p.read_text(encoding="utf-8"))
    cid = data.get("id")
    ids_present.append(cid)
    assert set(data.keys()) == WHITELIST, (cid, set(data.keys()))
    hits = []
    for path, val, is_key in walk(data):
        if is_key:
            for b in FIELD_BLACKLIST:
                if b in val:
                    hits.append({"field": path, "marker": b, "kind": "field-name"})
        else:
            for m in LEVEL1:
                if m in val:
                    hits.append({"field": path, "marker": m, "kind": "level1"})
            for m in LEVEL2:
                if m in val:
                    hits.append({"field": path, "marker": m, "kind": "level2"})
    report[cid] = {"file": str(p), "hits": hits, "hit_count": len(hits),
                   "built_by_this_seat": False}
    total += len(hits)
    print(cid, "hits:", len(hits))

scan = {
    "stage": "stage2-card-selfcheck",
    "seat": "leikao-cont-r52-second-seat",
    "new_candidates_registered": ["LK2-C52", "LK2-C53", "LK2-C54"],
    "new_cards_built": [],
    "reason_no_cards": "no candidate met A-grade + low contamination + separable threshold (C52 in-pool duplicate XJ47-147/mid-high, C53 A/mid, C54 B/high)",
    "input_card_ids_present_in_dir": ids_present,
    "per_card": report,
    "total_hits": total,
}
out_path = ROOT / "digestion" / "SCAN-leikao-cont-r52.json"
out_path.write_text(json.dumps(scan, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", out_path, "total_hits:", total)
