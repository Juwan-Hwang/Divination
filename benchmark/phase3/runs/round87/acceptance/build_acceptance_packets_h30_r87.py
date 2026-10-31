#!/usr/bin/env python3
"""holdout30 acceptance packet builder (R87) (host tooling, build-only; no scoring).

Gold is OPENED only when the platform fully stands (R87 platform
all-stand; data/holdout30-seal-log.md opening section). This script is run by the
host only after the opening is declared; see
runs/round87/acceptance/OPENING.md.
- packet-ours.json: our blind predictions (predictions/<case_id>.json ->
  prediction_text) vs gold outcome text.
- packet-master.json: masters' recorded predictions, taken verbatim from
  the gold master_prediction string field, vs the same gold outcome text.
Case id set is the holdout30 acceptance composition written into
CASE_IDS below (28 ids, per seal log; asserted equal to the gold id
set). Anon ids: H30O-/H30M-<8 hex>,
random.Random(20261102), sorted case order, redraw on collision. Mappings
in judging/host-mapping.json (host-only).
Outcome/master texts come ONLY from holdout30/test_gold.jsonl itself.
Gold integrity gate: the SHA-256 of holdout30/test_gold.jsonl is asserted
equal to the sealed value before any packet is built; a mismatch aborts.
Built-in assertions: both packets 28 items; anon id sets unique and
disjoint; host-mapping covers 56 entries; every outcome_record verbatim
equal to the gold outcome text; packet-ours prediction_text verbatim equal
to the predictions file prediction_text; packet-master prediction_text
verbatim equal to the composed gold master text.
"""
import hashlib
import json
import random
from pathlib import Path

ACC = Path(__file__).resolve().parent
P3 = ACC.parents[2]
GOLD = P3 / "holdout30" / "test_gold.jsonl"
GOLD_SHA256 = "09e38d9a5f87d1f81b959094035ff266428ca960c96d4fdc1a082643232adcdc"
CASE_IDS = [
    "DA-038", "DA-041", "DA-042", "DA-044", "DA-046",
    "CYJ-006", "CYJ-007", "CYJ-008", "CYJ-009", "CYJ-010",
    "BY-017", "BY-018", "BY-020", "BY-021",
    "WHY-025", "WHY-026", "WHY-027", "WHY-028", "WHY-031",
    "WHY-032", "WHY-033", "WHY-034", "WHY-035", "WHY-036",
    "GSZ-101", "GSZ-103", "GSZ-104", "GSZ-105",
]
SEED = 20261102


def outcome_text(rec):
    o = rec.get("outcome_record")
    if isinstance(o, str) and o.strip():
        return o
    raise ValueError(f"no outcome text for {rec.get('id')}")


def master_text(rec):
    m = rec.get("master_prediction")
    if isinstance(m, str) and m.strip():
        return m
    raise ValueError(f"no master text for {rec.get('id')}")


def main():
    digest = hashlib.sha256(GOLD.read_bytes()).hexdigest()
    assert digest == GOLD_SHA256, digest
    print(f"gold SHA-256 assertion passed: {digest}")

    gold = {}
    for line in open(GOLD, encoding="utf-8"):
        line = line.strip()
        if line:
            r = json.loads(line)
            gold[r["id"]] = r
    batch_ids = list(CASE_IDS)
    assert len(batch_ids) == 28 and len(set(batch_ids)) == 28, len(batch_ids)
    assert set(batch_ids) == set(gold), (
        sorted(set(batch_ids) - set(gold)), sorted(set(gold) - set(batch_ids)))
    ids = sorted(batch_ids)
    assert len(ids) == 28, len(ids)

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
        a1 = new_anon("H30O")
        ours_items.append({"anon_id": a1, "prediction_text": preds[cid],
                           "outcome_record": oc})
        mapping["ours"][a1] = cid
        a2 = new_anon("H30M")
        master_items.append({"anon_id": a2, "prediction_text": master_text(gold[cid]),
                             "outcome_record": oc})
        mapping["master"][a2] = cid
    ours_items.sort(key=lambda x: x["anon_id"])
    master_items.sort(key=lambda x: x["anon_id"])

    assert len(ours_items) == 28, len(ours_items)
    assert len(master_items) == 28, len(master_items)
    anon_ours = [e["anon_id"] for e in ours_items]
    anon_master = [e["anon_id"] for e in master_items]
    assert len(set(anon_ours)) == 28, len(set(anon_ours))
    assert len(set(anon_master)) == 28, len(set(anon_master))
    assert not (set(anon_ours) & set(anon_master))
    assert len(mapping["ours"]) + len(mapping["master"]) == 56
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
    print("assertions passed: packets 28+28; anon sets unique (28+28) and disjoint; "
          "host-mapping covers 56")
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
        f"anon seed: {SEED}; H30O- ours, H30M- master; random.Random(SEED), "
        "sorted case order, redraw on collision.\n", encoding="utf-8")
    print(f"gold: {len(ids)}; packet-ours: {len(ours_items)}; packet-master: {len(master_items)}")
    print("outcome non-empty:", sum(1 for e in ours_items if e["outcome_record"].strip()))
    print("master text non-empty:", sum(1 for e in master_items if e["prediction_text"].strip()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
