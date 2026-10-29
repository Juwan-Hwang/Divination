#!/usr/bin/env python3
"""holdout3 acceptance judging-packet builder (packet-building role, review side).

Reads gold (after seal-log unsealing entry was appended), our predictions,
and roster/splits tradition+contamination metadata. Emits anonymized
packetA/packetB (54 entries: ours + master per case), host-mapping.json
(host only) and packet-meta.json. Performs NO scoring.

Master prediction_text construction (no key assertion / timing dropped):
- cases with statement_excerpt + key_assertions: excerpt followed by all
  key_assertions joined (key_assertions == reasoning_points verbatim in this
  pool, so reasoning_points are not repeated). master_predictions[*].outcome
  for the horary cases is byte-identical to the gold outcome description,
  i.e. it is the outcome record, NOT a prediction, and is therefore excluded
  from prediction_text.
- cases with verdict only: the verdict text is the master's statement.
Master direction: structured field copied when present, else null.
Master timing: gold has no structured timing field -> null for all masters.
outcome_record: gold outcome.description verbatim (the narrative text field).
"""
import hashlib
import json
import pathlib

BASE = pathlib.Path(__file__).resolve().parents[3]  # benchmark/phase3
ACC = BASE / "holdout3-acceptance"
OUT = ACC / "judging"


def anon_id(case_id: str, source: str) -> str:
    h = hashlib.sha256(f"holdout3-acc:{case_id}:{source}".encode("utf-8")).hexdigest()
    return "H3-" + h[:8]


def master_text(mp: dict) -> str:
    parts = []
    if mp.get("statement_excerpt"):
        parts.append(mp["statement_excerpt"].strip())
    if mp.get("key_assertions"):
        parts.append("；".join(a.strip() for a in mp["key_assertions"]))
    if mp.get("verdict"):
        parts.append(mp["verdict"].strip())
    return " ".join(p for p in parts if p)


def main() -> None:
    gold = {}
    for line in open(BASE / "holdout3" / "test_gold.jsonl", encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            gold[r["id"]] = r

    roster = {}
    for line in open(BASE / "data" / "roster3.jsonl", encoding="utf-8"):
        if line.strip():
            r = json.loads(line)
            roster[r["id"]] = r

    splits = json.loads(open(BASE / "splits3.json", encoding="utf-8").read())
    assert set(splits["holdout3"]) == set(gold), "splits/gold case mismatch"

    preds = {}
    for f in sorted((ACC / "predictions").glob("*.json")):
        p = json.loads(open(f, encoding="utf-8").read())
        preds[p["case_id"]] = p
    assert set(preds) == set(gold), "prediction/gold case mismatch"

    entries, mapping, meta = [], {}, {}
    for cid in sorted(gold):
        g = gold[cid]
        outcome_record = g["outcome"]["description"]
        tradition = roster[cid]["tradition"]
        contamination = roster[cid]["contamination"]
        assert tradition == g["tradition"]

        p = preds[cid]
        ours = {
            "anon_id": anon_id(cid, "ours"),
            "prediction_text": p["prediction_text"],
            "direction": p.get("direction"),
            "timing": p.get("timing"),
            "outcome_record": outcome_record,
        }

        mp = g["master_predictions"][0]
        master = {
            "anon_id": anon_id(cid, "master"),
            "prediction_text": master_text(mp),
            "direction": mp.get("direction"),
            "timing": mp.get("timing"),
            "outcome_record": outcome_record,
        }

        for src, e in (("ours", ours), ("master", master)):
            assert e["prediction_text"], f"empty prediction_text {cid} {src}"
            entries.append(e)
            mapping[e["anon_id"]] = {"case_id": cid, "source": src}
            meta[e["anon_id"]] = {"tradition": tradition, "contamination": contamination}

    entries.sort(key=lambda e: e["anon_id"])
    assert len(entries) == 54 and len({e["anon_id"] for e in entries}) == 54

    OUT.mkdir(parents=True, exist_ok=True)
    json.dump(entries[:27], open(OUT / "packetA.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(entries[27:], open(OUT / "packetB.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(mapping, open(OUT / "host-mapping.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    json.dump(meta, open(OUT / "packet-meta.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)

    stats = {"total": len(entries),
             "packetA": len(entries[:27]), "packetB": len(entries[27:]),
             "mapping": len(mapping), "meta": len(meta)}
    for src in ("ours", "master"):
        ids = [a for a, m in mapping.items() if m["source"] == src]
        stats[src] = {
            "n": len(ids),
            "direction_null": sum(1 for e in entries if e["anon_id"] in ids and e["direction"] is None),
            "timing_null": sum(1 for e in entries if e["anon_id"] in ids and e["timing"] is None),
        }
    json.dump(stats, open(OUT / "build" / "build-stats.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False))


if __name__ == "__main__":
    main()
