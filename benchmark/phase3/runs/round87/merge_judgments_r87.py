#!/usr/bin/env python3
"""Round 87 host tooling: merge judge seat files into views X/Y, verify
coverage against the host mapping, compute the arbitration dispute set
(|X.total - Y.total| >= 3) and build the arbitration packet.
Platform family only (487, scores-judgeX1..4 / scores-judgeY1..4).
No scoring is done here.
R84 naming note: this round's packet files carry the judgeX-block*.jsonl
names and the seats' score outputs are judgeX-block*-scores.jsonl (R82
dispatch wording, carried through R83/R84/R85), so main() reads those names; mechanism otherwise
verbatim from merge_judge_views_r79.py via merge_judgments_r80.py, carried verbatim.
BUILD-ONLY: written ahead of judging; run by the host only after
the judge seats return their scored judgeX/judgeY block files.
(Verbatim mechanism of merge_judge_views_r79.py.)
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


def merge_family(view_files, mapping_name, packet_names, tag):
    views = []
    for files in view_files:
        view = {}
        for name in files:
            part = load_jsonl(name)
            overlap = set(view) & set(part)
            assert not overlap, f"{tag} overlap {overlap}"
            view.update(part)
        views.append(view)
    vx, vy = views
    hmap = json.loads((JD / mapping_name).read_text(encoding="utf-8"))
    assert set(vx) == set(hmap) == set(vy), (tag, len(vx), len(vy), len(hmap))
    for name, view in ((f"judgeX-merged{tag}.json", vx), (f"judgeY-merged{tag}.json", vy)):
        with open(JD / name, "w", encoding="utf-8") as fh:
            json.dump(view, fh, ensure_ascii=False, indent=1)
    items = {}
    for name in packet_names:
        for e in json.loads((JD / name).read_text(encoding="utf-8")):
            items[e["anon_id"]] = e
    disputed = sorted(a for a in hmap if abs(vx[a]["total"] - vy[a]["total"]) >= 3)
    disputes = [{"anon_id": a,
                 "case_id": hmap[a]["case_id"] if isinstance(hmap[a], dict) else hmap[a]}
                for a in disputed]
    with open(JD / f"disputes{tag}.json", "w", encoding="utf-8") as fh:
        json.dump(disputes, fh, ensure_ascii=False, indent=1)
    arb = [items[a] for a in disputed]
    with open(JD / f"arbitration-packet{tag}.json", "w", encoding="utf-8") as fh:
        json.dump(arb, fh, ensure_ascii=False, indent=1)
    print(f"{tag or 'platform'}: view X {len(vx)}, view Y {len(vy)}, "
          f"anon set == mapping True; disputes {len(disputes)} -> "
          f"{[d['case_id'] for d in disputes]}")
    return disputes


def main():
    merge_family(
        ([f"judgeX-block{i}-scores.jsonl" for i in range(1, 5)],
         [f"judgeY-block{i}-scores.jsonl" for i in range(1, 5)]),
        "host-mapping.json", ("packetA.json", "packetB.json"), "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
