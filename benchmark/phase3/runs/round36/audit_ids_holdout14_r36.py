#!/usr/bin/env python3
"""R36 data-corner tooling: pre-seal id-uniqueness audit for holdout14 picks.

Scope (per tasking, mirroring R35 audit-ids): ID CONFLICTS ONLY. Scans
every *.jsonl / *.json record under benchmark/ that carries an `id`,
plus inputs-dev11 card filenames, data/splits*.json id lists and
expansion12/POOL-IDS.txt, and reports for each of the 40 selected ids
every file/list that carries it. It never reads or compares outcome
text; identity of a same-id record is judged by the human reader from
the printed file list, not by this script.

This round's own outputs (holdout14/, holdout14-inputs/, runs/round36/)
are excluded from the scan. Expected benign carriers: each id's own
source cases file (PU also its natal-batch2/cases.jsonl twin original;
BY also its liuren-bianyi-yuce/cases.jsonl pre-review original). Any
appearance in dev inputs, another holdout gold, POOL-IDS or splits
lists is a conflict to disposition before sealing.

Output: stdout + audit-ids-holdout14-report.json next to this script.
No file modification elsewhere. No scoring.
"""
import json
from collections import defaultdict
from pathlib import Path

R36 = Path(__file__).resolve().parent
BENCH = R36.parents[2]
P3 = BENCH / "phase3"

SELECTED = [
    "DA-015", "DA-016", "DA-017", "DA-019", "DA-020", "DA-021", "DA-022", "DA-023",
    "BY-007", "BY-008", "BY-009", "BY-010", "BY-011",
    "CY-005", "CY-006", "CY-008",
    "BQ-026", "BQ-027", "BQ-028", "BQ-029", "BQ-030", "BQ-031", "BQ-032", "BQ-033", "BQ-034",
    "PU-003", "PU-008",
    "CZ-018", "CZ-019", "CZ-020", "CZ-022", "CZ-023", "CZ-024", "CZ-026", "CZ-027",
    "CZ-028", "CZ-030", "CZ-031", "CZ-032", "CZ-033",
]
assert len(SELECTED) == 40 and len(set(SELECTED)) == 40
SEL = set(SELECTED)

SOURCE_FILE = {}
for cid in SELECTED:
    if cid.startswith("DA-"):
        SOURCE_FILE[cid] = "expansion12/liuren-duanan/"
    elif cid.startswith("BY-"):
        SOURCE_FILE[cid] = "expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl"
    elif cid.startswith("CY-"):
        SOURCE_FILE[cid] = "expansion12/liuren-cuiyan/cases-munong.jsonl"
    elif cid.startswith("BQ-"):
        SOURCE_FILE[cid] = "expansion12/bushi-quanshu-beixuan/cases.jsonl"
    elif cid.startswith("PU-"):
        SOURCE_FILE[cid] = "expansion12/natal-batch2/cases-reviewed.jsonl"
    elif cid.startswith("CZ-"):
        SOURCE_FILE[cid] = "expansion12/online-routes/cases.jsonl"


def iter_ids(path):
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return
    if path.suffix == ".jsonl":
        for line in text.splitlines():
            if '"id"' not in line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict) and isinstance(obj.get("id"), str):
                yield obj["id"]
    else:
        try:
            obj = json.loads(text)
        except json.JSONDecodeError:
            return
        stack = [obj]
        while stack:
            cur = stack.pop()
            if isinstance(cur, dict):
                if isinstance(cur.get("id"), str):
                    yield cur["id"]
                stack.extend(cur.values())
            elif isinstance(cur, list):
                stack.extend(cur)


def main():
    hits = defaultdict(list)
    own_prefixes = ("holdout14/", "holdout14-inputs/", "runs/round36/")
    scanned = 0
    for path in sorted(BENCH.rglob("*")):
        if not path.is_file() or path.suffix not in (".json", ".jsonl"):
            continue
        rel = path.relative_to(P3).as_posix() if path.is_relative_to(P3) else path.relative_to(BENCH).as_posix()
        if rel.startswith(own_prefixes) or "/runs/" in rel:
            continue
        scanned += 1
        for cid in iter_ids(path):
            if cid in SEL:
                hits[cid].append(rel)
    # filename / list based carriers
    dev_names = {p.stem for p in (P3 / "inputs-dev11").glob("*.json")}
    pool = set((P3 / "expansion12/POOL-IDS.txt").read_text(encoding="utf-8").split())
    splits_ids = set()
    for sp in sorted((P3 / "data").glob("splits*.json")):
        try:
            obj = json.loads(sp.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        def walk(o):
            if isinstance(o, dict):
                for v in o.values():
                    yield from walk(v)
            elif isinstance(o, list):
                for v in o:
                    yield from walk(v)
            elif isinstance(o, str):
                yield o
        splits_ids |= {s for s in walk(obj) if s in SEL}
    report = {"scanned_files": scanned, "selected": SELECTED, "hits": {},
              "dev11_filename_hits": sorted(SEL & dev_names),
              "pool_ids_hits": sorted(SEL & pool),
              "splits_hits": sorted(splits_ids)}
    conflicts = []
    for cid in SELECTED:
        files = sorted(set(hits.get(cid, [])))
        others = [f for f in files if not f.startswith(SOURCE_FILE[cid].rsplit("/", 1)[0] + "/")
                  and f != SOURCE_FILE[cid]]
        report["hits"][cid] = {"files": files, "other_files": others}
        if others:
            conflicts.append(cid)
    report["ids_with_other_files"] = conflicts
    (R36 / "audit-ids-holdout14-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"scanned_files": scanned,
                      "dev11_filename_hits": report["dev11_filename_hits"],
                      "pool_ids_hits": report["pool_ids_hits"],
                      "splits_hits": report["splits_hits"],
                      "ids_with_other_files": conflicts,
                      "other_files_detail": {c: report["hits"][c]["other_files"] for c in conflicts}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
