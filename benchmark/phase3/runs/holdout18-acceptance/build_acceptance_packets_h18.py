#!/usr/bin/env python3
"""holdout18 acceptance packet builder (host tooling, build-only; no scoring).

Mirror of the holdout17 builder. Gold was OPENED under R42 (see OPENING.md
in this directory).
- packet-ours.json: our blind predictions (predictions/<case_id>.json ->
  prediction_text) vs gold outcome text.
- packet-master.json: masters' recorded predictions, composed verbatim from
  gold master_predictions (statement_excerpt + key_assertions + timing_claim)
  vs the same gold outcome text.
Case id set comes from batches.json (30 ids; asserted equal to the gold id
set). Anon ids: H18O-/H18M-<8 hex>, random.Random(20261043), sorted case
order, redraw on collision. Mappings in judging/host-mapping.json (host-only).
Outcome/master texts come ONLY from holdout17/test_gold.jsonl itself.
Built-in assertions: both packets 40 items; anon id sets unique and
disjoint; host-mapping covers 80 entries; every outcome_record verbatim
equal to the gold outcome text; packet-ours prediction_text verbatim equal
to the predictions file prediction_text; packet-master prediction_text
verbatim equal to the composed gold master text.
"""
import json
import random
from pathlib import Path

ACC = Path(__file__).resolve().parent
P3 = ACC.parents[1]
GOLD = P3 / "holdout18" / "test_gold.jsonl"
SEED = 20261043


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
    batches = json.loads((ACC / "batches.json").read_text(encoding="utf-8"))
    batch_ids = [cid for group in batches.values() for cid in group]
    assert len(batch_ids) == 30 and len(set(batch_ids)) == 30, len(batch_ids)
    assert set(batch_ids) == set(gold), (
        sorted(set(batch_ids) - set(gold)), sorted(set(gold) - set(batch_ids)))
    ids = sorted(batch_ids)
    assert len(ids) == 30, len(ids)

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
        a1 = new_anon("H18O")
        ours_items.append({"anon_id": a1, "prediction_text": preds[cid],
                           "outcome_record": oc})
        mapping["ours"][a1] = cid
        a2 = new_anon("H18M")
        master_items.append({"anon_id": a2, "prediction_text": master_text(gold[cid]),
                             "outcome_record": oc})
        mapping["master"][a2] = cid
    ours_items.sort(key=lambda x: x["anon_id"])
    master_items.sort(key=lambda x: x["anon_id"])

    assert len(ours_items) == 30, len(ours_items)
    assert len(master_items) == 30, len(master_items)
    anon_ours = [e["anon_id"] for e in ours_items]
    anon_master = [e["anon_id"] for e in master_items]
    assert len(set(anon_ours)) == 30, len(set(anon_ours))
    assert len(set(anon_master)) == 30, len(set(anon_master))
    assert not (set(anon_ours) & set(anon_master))
    assert len(mapping["ours"]) + len(mapping["master"]) == 60
    assert set(mapping["ours"]) == set(anon_ours)
    assert set(mapping["master"]) == set(anon_master)
    assert set(mapping["ours"].values()) == set(ids)
    assert set(mapping["master"].values()) == set(ids)
    for e in ours_items:
        cid = mapping["ours"][e["anon_id"]]
        assert e["outcome_record"] == outcome_text(gold[cid]), cid
        assert e["prediction_text"] == preds[cid], cid
    for e in master_items:
        cid = mapping["master"][e["anon_id"]]
        assert e["outcome_record"] == outcome_text(gold[cid]), cid
        assert e["prediction_text"] == master_text(gold[cid]), cid
    print("assertions passed: packets 30+30; anon sets unique (30+30) and disjoint; "
          "host-mapping covers 60")
    print("assertions passed: every outcome_record verbatim vs gold outcome; "
          "ours prediction_text verbatim vs predictions files; "
          "master prediction_text verbatim vs gold master text")

    JD = ACC / "judging"
    JD.mkdir(parents=True, exist_ok=True)
    for name, obj in (("packet-ours.json", ours_items),
                      ("packet-master.json", master_items),
                      ("host-mapping.json", mapping)):
        with open(JD / name, "w", encoding="utf-8") as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
    (JD / "anon-seed.txt").write_text(
        f"anon seed: {SEED}; H18O- ours, H18M- master; random.Random(SEED), "
        "sorted case order, redraw on collision.\n", encoding="utf-8")
    print(f"gold: {len(ids)}; packet-ours: {len(ours_items)}; packet-master: {len(master_items)}")
    print("outcome non-empty:", sum(1 for e in ours_items if e["outcome_record"].strip()))
    print("master text non-empty:", sum(1 for e in master_items if e["prediction_text"].strip()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
