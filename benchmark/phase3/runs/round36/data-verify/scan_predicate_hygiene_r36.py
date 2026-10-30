#!/usr/bin/env python3
"""R36 data-verify task1: predicate-hygiene scan of R35 outcome-manifest.

Scans ALL 487 outcome texts in runs/round35/judging/outcome-manifest.json
with high-recall marker patterns for OC-023-type contamination
(extractor verdict / meta sentences mixed into outcome text).
Output: scan_predicate_hygiene_r36_hits.json in this directory.
This script only READS the manifest; it modifies nothing.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE.parent.parent / "round35" / "judging" / "outcome-manifest.json"

PATTERNS = {
    # verdict-on-match: sentence judging whether master prediction matched outcome
    "P1_match_verdict": r"相合|相符|吻合|逐项合|逐項合|落空|皆反|全反|不合|证伪|證偽|应验|應驗|果然|驗|相符",
    # reference to the prediction text itself
    "P2_prediction_ref": r"断语|斷語|断言|斷言|预测|預測|大师断|大師斷|原断|原斷|所断|所斷",
    # meta about source text / separability / coverage
    "P3_meta_text": r"可分离|可分離|独立成句|獨立成句|独立载|獨立載|原文中|原文未|未载|未載|未被结局|无从单独|無從單獨|文本|记载|記載|注称|注稱",
    # verdict self-reference openers
    "P4_verdict_opener": r"断曰|斷曰|断为|斷為|占断|占斷|占曰|予曰|断：|斷：",
    # english verdict/meta framing
    "P5_english": r"[Cc]onfirmed|I judged|judged that|prediction|matched|verified|the text",
    # evaluator parenthetical / partial-match phrasing
    "P6_partial_eval": r"仅部分|僅部分|部分相合|不计|不計|仅作|僅作",
    # sweep 2: original-text / verification-passage references
    "P7_source_ref": r"如言|如斷|如断|依斷|依断|之驗|之验|proved|was true|very true|原文|原书|原書|書內|书内|自述|自載|自载|注家|徵驗|应验段|應驗段|独立|獨立",
    # sweep 3: correspondence phrasing
    "P8_correspond": r"对应|對應|印证|印證|命中|恰合|正合|相契|不差|无误|無誤|fulfilled",
    # residual manual-read phrases (extractor-composed families read in full)
    "P9_residual": r"exactly as judged|Recorded within|并非「|相应|應了|应了「|按部分合|超出「|多合|对勘成立|對勘成立",
}

def main():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    cases = data["cases"]
    hits = {}
    for cid, outcome in cases.items():
        matched = {}
        for name, pat in PATTERNS.items():
            ms = [m.group(0) for m in re.finditer(pat, outcome)]
            if ms:
                matched[name] = ms
        if matched:
            hits[cid] = {"patterns": matched, "outcome": outcome}
    out = {
        "manifest": str(MANIFEST),
        "total_cases": len(cases),
        "hit_cases": len(hits),
        "patterns": PATTERNS,
        "hits": hits,
    }
    out_path = HERE / "scan_predicate_hygiene_r36_hits.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"total={len(cases)} hits={len(hits)}")
    for cid in hits:
        print(cid, ",".join(hits[cid]["patterns"].keys()))

if __name__ == "__main__":
    main()
