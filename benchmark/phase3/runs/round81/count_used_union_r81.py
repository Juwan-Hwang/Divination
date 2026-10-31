#!/usr/bin/env python3
"""R81 host tooling: recompute the used-id union on disk (opening check).

Method follows data/holdout25-seal-log.md s.1 zero-reuse accounting:
- dev pool: data/master-baseline-dev9.json keys + card ids in
  inputs-dev9/10/11/12 and inputs dirs;
- phase2 splits2 holdout2 ids;
- holdout3..25 test_gold.jsonl id fields;
- holdout inputs card ids (holdoutN/inputs and holdoutN-inputs dirs);
- top-level inputs6..inputs10 card ids.
Expected at R81 opening: 1085 (R80 opening 1058 + holdout25's 27 new ids).
"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
BM = P3.parent


def card_ids(d):
    out = set()
    if d.is_dir():
        for f in d.glob("*.json"):
            out.add(f.stem)
    return out


def gold_ids(p):
    out = set()
    if p.is_file():
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                out.add(json.loads(line)["id"])
    return out


def main():
    parts = {}

    dev = set(json.loads((P3 / "data/master-baseline-dev9.json").read_text(encoding="utf-8")).keys())
    for name in ["inputs-dev9", "inputs-dev10", "inputs-dev11", "inputs-dev12", "inputs"]:
        dev |= card_ids(P3 / name)
    parts["dev"] = dev

    sp2 = json.loads((BM / "phase2/splits2.json").read_text(encoding="utf-8"))
    h2 = set()
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "holdout2" and isinstance(v, list):
                    h2.update(x if isinstance(x, str) else x.get("id") for x in v)
                else:
                    walk(v)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(sp2)
    parts["holdout2_splits2"] = h2

    golds = set()
    for n in range(3, 26):
        golds |= gold_ids(P3 / f"holdout{n}" / "test_gold.jsonl")
    parts["gold_h3_25"] = golds

    hinputs = set()
    for n in range(2, 26):
        hinputs |= card_ids(P3 / f"holdout{n}" / "inputs")
        hinputs |= card_ids(P3 / f"holdout{n}-inputs")
    parts["holdout_inputs"] = hinputs

    top = set()
    for name in ["inputs6", "inputs7", "inputs8", "inputs9", "inputs10"]:
        top |= card_ids(P3 / name)
    parts["top_inputs6_10"] = top

    union = set()
    for k, v in parts.items():
        print(k, len(v))
        union |= v
    print("UNION", len(union))
    h25 = gold_ids(P3 / "holdout25" / "test_gold.jsonl")
    print("holdout25 gold ids", len(h25), "all in union:", h25 <= union)


if __name__ == "__main__":
    main()
