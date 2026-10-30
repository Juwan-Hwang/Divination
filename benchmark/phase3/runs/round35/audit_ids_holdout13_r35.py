#!/usr/bin/env python3
"""R35 data-corner tooling: pre-seal id-uniqueness audit for holdout13 picks.

Scope (per tasking): ID CONFLICTS ONLY. Scans every *.jsonl / *.json record
under benchmark/ that carries an `id`, plus inputs-dev11 card filenames,
data/splits*.json id lists and expansion12/POOL-IDS.txt, and reports for each
of the 40 selected ids every file/list that carries it. It never reads or
compares outcome text to resolve anything (no first-hit outcome lookup);
identity of a same-id record, where needed, is judged by the human reader
from the printed file list, not by this script.

Expected benign carriers of a selected id: its own source cases file (and,
for QL, natal-batch2/cases.jsonl pre-rename QM twin is under a different id,
so it does NOT appear). Any appearance in dev inputs, another holdout gold,
POOL-IDS or splits lists is a conflict to disposition before sealing.

Output: stdout + audit-ids-holdout13-report.json next to this script.
No file modification elsewhere. No scoring.
"""
import json
from collections import defaultdict
from pathlib import Path

R35 = Path(__file__).resolve().parent
BENCH = R35.parents[2]
P3 = BENCH / "phase3"

SELECTED = [
    "DA-002", "DA-004", "DA-005", "DA-008", "DA-010", "DA-011", "DA-012",
    "DA-013",
    "BY-002", "BY-003", "BY-004", "BY-005", "BY-006",
    "CY-002", "CY-003", "CY-004",
    "QL-013", "QL-014", "QL-023", "QL-025", "QL-026", "QL-027", "QL-030",
    "QL-031", "QL-032", "QL-035",
    "NL-006", "NL-049",
    "CZ-002", "CZ-003", "CZ-004", "CZ-006", "CZ-007", "CZ-008", "CZ-010",
    "CZ-011", "CZ-012", "CZ-014", "CZ-015", "CZ-016",
]
assert len(SELECTED) == 40 and len(set(SELECTED)) == 40

# The one legitimate source file per selected id (relative to workspace root
# of the divination tree). Anything outside this + this round's own outputs
# is listed as OTHER and must be dispositioned in BUILD-LOG.
SOURCE_FILE = {}
for cid in SELECTED:
    if cid.startswith("DA-"):
        SOURCE_FILE[cid] = "expansion12/liuren-duanan/"
    elif cid.startswith("BY-"):
        SOURCE_FILE[cid] = "expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl"
    elif cid.startswith("CY-"):
        SOURCE_FILE[cid] = "expansion12/liuren-cuiyan/cases-munong.jsonl"
    elif cid.startswith("QL-"):
        SOURCE_FILE[cid] = "expansion12/natal-batch2/cases-reviewed.jsonl"
    elif cid.startswith("NL-"):
        SOURCE_FILE[cid] = "expansion12/natal-leftovers/cases.jsonl"
    elif cid.startswith("CZ-"):
        SOURCE_FILE[cid] = "expansion12/online-routes/cases.jsonl"


def iter_ids(path):
    if path.suffix == ".jsonl":
        with open(path, encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if isinstance(rec, dict) and isinstance(rec.get("id"), str):
                    yield rec["id"]
    elif path.suffix == ".json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return
        if isinstance(data, list):
            for rec in data:
                if isinstance(rec, dict) and isinstance(rec.get("id"), str):
                    yield rec["id"]
        elif isinstance(data, dict):
            for key, val in data.items():
                if isinstance(val, dict) and isinstance(val.get("id"), str):
                    yield val["id"]


def main():
    carriers = defaultdict(set)  # id -> set of relpaths carrying it
    files = sorted(
        p for p in BENCH.rglob("*")
        if p.is_file() and p.suffix in (".jsonl", ".json")
        and "runs" not in p.parts
        and "__pycache__" not in p.parts
        and "holdout13" not in p.parts)
    for path in files:
        rel = str(path.relative_to(BENCH.parent))
        for cid in iter_ids(path):
            if cid in SELECTED:
                carriers[cid].add(rel)

    dev_ids = {p.stem for p in (P3 / "inputs-dev11").glob("*.json")}
    pool_ids = set((P3 / "expansion12/POOL-IDS.txt").read_text(
        encoding="utf-8").split())
    splits_ids = set()
    for sname in ("splits10.json", "splits11.json"):
        d = json.loads((P3 / "data" / sname).read_text(encoding="utf-8"))
        for key, val in d.items():
            if isinstance(val, list):
                splits_ids.update(x for x in val if isinstance(x, str))

    report = {"selected": SELECTED, "per_id": {}, "conflicts": {}}
    for cid in SELECTED:
        hits = sorted(carriers.get(cid, set()))
        in_dev = cid in dev_ids
        in_pool = cid in pool_ids
        in_splits = cid in splits_ids
        others = [h for h in hits if SOURCE_FILE[cid] not in h]
        entry = {
            "carriers": hits,
            "in_inputs_dev11": in_dev,
            "in_pool_ids": in_pool,
            "in_splits_lists": in_splits,
            "carriers_outside_source": others,
        }
        report["per_id"][cid] = entry
        if in_dev or in_pool or in_splits or others:
            report["conflicts"][cid] = entry
    (R35 / "audit-ids-holdout13-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"files scanned: {len(files)}")
    print(f"selected ids: {len(SELECTED)}")
    print(f"ids with any flag: {len(report['conflicts'])}")
    for cid in SELECTED:
        e = report["per_id"][cid]
        print(f"{cid}: carriers={e['carriers']} dev={e['in_inputs_dev11']} "
              f"pool={e['in_pool_ids']} splits={e['in_splits_lists']} "
              f"outside_source={e['carriers_outside_source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
