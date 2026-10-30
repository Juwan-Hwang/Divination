#!/usr/bin/env python3
"""Round 33 host tooling: merge the four judge seats' part files into the two
independent views (X = Judge-A + Judge-A2, Y = Judge-B + Judge-B2), verify
each view covers exactly the host-mapping anon set (487), then compute the
arbitration dispute set (|X.total - Y.total| >= 3) and build the arbitration
packet. Mirrors the round32 host merge step. No scoring is done here.
"""
import json
from pathlib import Path

JD = Path(__file__).resolve().parent / "judging"


def load_jsonl(name):
    rows = {}
    for line in open(JD / name, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            assert r["anon_id"] not in rows, f"dup {r['anon_id']} in {name}"
            rows[r["anon_id"]] = r
    return rows


def main():
    view_x = {}
    for name in ("judgeA-part1.jsonl", "judgeA-part2.jsonl",
                 "judgeA2-part1.jsonl", "judgeA2-part2.jsonl"):
        part = load_jsonl(name)
        overlap = set(view_x) & set(part)
        assert not overlap, f"view X overlap {overlap}"
        view_x.update(part)
    view_y = {}
    for name in ("judgeB-part1.jsonl", "judgeB-part2.jsonl",
                 "judgeB2-part1.jsonl", "judgeB2-part2.jsonl"):
        part = load_jsonl(name)
        overlap = set(view_y) & set(part)
        assert not overlap, f"view Y overlap {overlap}"
        view_y.update(part)

    hmap = json.loads((JD / "host-mapping.json").read_text(encoding="utf-8"))
    assert set(view_x) == set(hmap) == set(view_y), (
        len(view_x), len(view_y), len(hmap))

    for name, view in (("judgeX-merged.json", view_x), ("judgeY-merged.json", view_y)):
        with open(JD / name, "w", encoding="utf-8") as fh:
            json.dump(view, fh, ensure_ascii=False, indent=1)

    disputes = sorted(
        ({"case_id": hmap[a]} for a in hmap
         if abs(view_x[a]["total"] - view_y[a]["total"]) >= 3),
        key=lambda d: d["case_id"])
    with open(JD / "disputes.json", "w", encoding="utf-8") as fh:
        json.dump(disputes, fh, ensure_ascii=False, indent=1)

    items = {}
    for name in ("packetA.json", "packetB.json"):
        for e in json.loads((JD / name).read_text(encoding="utf-8")):
            items[e["anon_id"]] = e
    disputed_anons = {a for a in hmap
                      if abs(view_x[a]["total"] - view_y[a]["total"]) >= 3}
    arb_packet = [items[a] for a in sorted(disputed_anons)]
    with open(JD / "arbitration-packet.json", "w", encoding="utf-8") as fh:
        json.dump(arb_packet, fh, ensure_ascii=False, indent=1)

    print(f"view X: {len(view_x)}, view Y: {len(view_y)}, anon set == host-mapping: True")
    print(f"disputes (|dTotal|>=3): {len(disputes)} -> {[d['case_id'] for d in disputes]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
