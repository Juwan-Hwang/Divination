#!/usr/bin/env python3
"""R81 host third-scan for holdout25 unsealing pre-verification (PREREG s.2).

Marker set verbatim from R42 PREREG s.5 as instantiated in
runs/round80/scan_holdout25_r80.py (LEVEL1/LEVEL2). Scans all 27 input cards
in phase3/holdout25/inputs/ by explicit id list from the seal log s.1.
Zero hits required to unseal.
"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
IDS = ["DS-025", "DS-026", "DS-027", "DS-028", "DS-029", "DS-030",
       "QM-027", "QM-028", "QM-029", "QM-030", "QM-031", "QM-032",
       "QM-208", "QM-209", "QM-310", "QM-311",
       "GSZ-049", "GSZ-050", "GSZ-052", "GSZ-053", "GSZ-054", "GSZ-055",
       "GSZ-058", "GSZ-059", "GSZ-060", "GSZ-061", "GSZ-068"]
LEVEL1 = ['断语线索', '断曰', '断語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']


def walk(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            yield from walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v)
    elif isinstance(obj, str):
        yield obj


def main():
    hits = []
    n = 0
    for cid in IDS:
        p = P3 / "holdout25" / "inputs" / f"{cid}.json"
        assert p.exists(), cid
        n += 1
        card = json.loads(p.read_text(encoding="utf-8"))
        text = "\n".join(walk(card))
        for lvl, markers in (("L1", LEVEL1), ("L2", LEVEL2)):
            for m in markers:
                if m in text:
                    hits.append([cid, lvl, m])
    out = {"cards_scanned": n, "marker_hits": hits, "total_hits": len(hits)}
    (P3 / "runs/round81/host-scan-h25-unseal-r81.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
