#!/usr/bin/env python3
"""R51 host acceptance-side re-scan for holdout19 input cards (PREREG s.3 pre-unseal check).
Marker set copied verbatim from runs/round42/scan_content_markers_r42.py
(R42 PREREG s.5 constants); host-side independent re-scan, scan-3 slot in
build-holdout19-report-r50.json / data/holdout19-seal-log.md."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "round42"))
import importlib.util

spec = importlib.util.spec_from_file_location(
    "scan42", Path(__file__).resolve().parent.parent / "round42" / "scan_content_markers_r42.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
LEVEL1, LEVEL2 = mod.LEVEL1, mod.LEVEL2


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)


def main():
    inputs = sorted((Path(__file__).resolve().parent.parent.parent / "holdout19" / "inputs").glob("*.json"))
    assert len(inputs) == 25, len(inputs)
    total_hits = 0
    for p in inputs:
        card = json.loads(p.read_text(encoding="utf-8"))
        for s in strings(card):
            for lvl, markers in (("L1", LEVEL1), ("L2", LEVEL2)):
                for m in markers:
                    if m in s:
                        total_hits += 1
                        print(f"HIT {p.name} {lvl} marker={m!r}")
    print(f"accept-scan: {len(inputs)} cards, total hits = {total_hits}")
    assert total_hits == 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
