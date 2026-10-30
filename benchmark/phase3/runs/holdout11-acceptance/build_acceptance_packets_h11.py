#!/usr/bin/env python3
"""holdout11 acceptance packet builder (host tooling, build-only; no scoring).

Builds two anonymized packets from the OPENED gold (opening recorded in
OPENING.md after SHA verification against data/holdout11-seal-log.md):
- packet-ours.json: our blind predictions (predictions/<case_id>.json ->
  prediction_text) vs gold outcome text.
- packet-master.json: masters' recorded predictions, composed verbatim from
  gold master_predictions (statement_excerpt + key_assertions + timing_claim)
  vs the same gold outcome text.
Anon ids: H11O-/H11M-<8 hex>, random.Random(20261033), sorted case order,
redraw on collision. Mappings written to judging/host-mapping.json.
Outcome text: gold outcome.description (fallback: outcome str).
"""
import json
import random
from pathlib import Path

ACC = Path(__file__).resolve().parent
P3 = ACC.parents[1]
GOLD = P3 / "holdout11" / "test_gold.jsonl"
SEED = 20261033


def outcome_text(rec):
    o = rec.get("outcome")
    if isinstance(o, dict):
        d = o.get("description")
        if isinstance(d, str) and d.strip():
            return d
    if isinstance(o, str) and o.strip():
        return o
    raise ValueError(f"no outcome text for {rec.get('id')}")


def master_text(rec):
    parts = []
    for m in rec["master_predictions"]:
        seg = []
        if m.get("statement_excerpt"):
            seg.append(m["statement_excerpt"])
        ka = m.get("key_assertions") or []
        if ka:
            seg.append("断语：" + "；".join(ka))
        if m.get("timing_claim"):
            seg.append("应期：" + m["timing_claim"])
        parts.append("\n".join(seg))
    return "\n".join(parts)


def main():
    gold = {}
    for line in open(GOLD, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            gold[r["id"]] = r
    ids = sorted(gold)
    assert len(ids) == 25

    preds = {}
    for cid in ids:
        p = json.loads((ACC / "predictions" / f"{cid}.json").read_text(encoding="utf-8"))
        preds[cid] = p["prediction_text"]

    rng = random.Random(SEED)
    used = set()

    def new_anon(prefix):
        while True:
            a = prefix + "-%08x" % rng.getrandbits(32)
            if a not in used:
                used.add(a)
                return a

    ours_items, master_items = [], []
    mapping = {"ours": {}, "master": {}}
    for cid in ids:
        oc = outcome_text(gold[cid])
        a1 = new_anon("H11O")
        ours_items.append({"anon_id": a1, "prediction_text": preds[cid],
                           "outcome_record": oc})
        mapping["ours"][a1] = cid
        a2 = new_anon("H11M")
        master_items.append({"anon_id": a2, "prediction_text": master_text(gold[cid]),
                             "outcome_record": oc})
        mapping["master"][a2] = cid
    ours_items.sort(key=lambda x: x["anon_id"])
    master_items.sort(key=lambda x: x["anon_id"])

    JD = ACC / "judging"
    JD.mkdir(parents=True, exist_ok=True)
    for name, obj in (("packet-ours.json", ours_items),
                      ("packet-master.json", master_items),
                      ("host-mapping.json", mapping)):
        with open(JD / name, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
    (JD / "anon-seed.txt").write_text(
        f"anon seed: {SEED}; H11O- ours, H11M- master; random.Random(SEED), "
        "sorted case order, redraw on collision.\n", encoding="utf-8")
    print(f"gold: {len(ids)}; packet-ours: {len(ours_items)}; packet-master: {len(master_items)}")
    print("outcome non-empty:", sum(1 for e in ours_items if e["outcome_record"].strip()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
