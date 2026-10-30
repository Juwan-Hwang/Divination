#!/usr/bin/env python3
"""R34 host tooling: full-tree case-id uniqueness audit (data hygiene item 1).

Scans every *.jsonl / *.json record under benchmark/ that carries an
id/case_id plus an outcome text, groups by id, and reports:
  - ids whose outcome text differs across source files (collision risk),
  - ids appearing in more than one file with identical outcome (benign dup),
  - the dev9 487 ids specifically: every source file that carries them.
No scoring, no file modification. Output: stdout + audit-ids-report.json.
"""
import json
from collections import defaultdict
from pathlib import Path

R34 = Path(__file__).resolve().parent
BENCH = R34.parents[2]
DIV = BENCH.parent


def extract_outcome(rec):
    v = rec.get("outcome_record")
    if isinstance(v, str) and v.strip():
        return v
    o = rec.get("outcome")
    if isinstance(o, str) and o.strip():
        return o
    if isinstance(o, dict):
        for key in ("description", "outcome_record", "text"):
            d = o.get(key)
            if isinstance(d, str) and d.strip():
                return d
    return None


def iter_records(path):
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
                if isinstance(rec, dict):
                    yield rec
    elif path.suffix == ".json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return
        if isinstance(data, list):
            for rec in data:
                if isinstance(rec, dict):
                    yield rec
        elif isinstance(data, dict):
            for key, val in data.items():
                if isinstance(val, dict):
                    rec = dict(val)
                    rec.setdefault("id", key)
                    yield rec


def main():
    files = sorted(
        p for p in BENCH.rglob("*")
        if p.is_file() and p.suffix in (".jsonl", ".json")
        and "runs" not in p.parts  # run judging artefacts are not sources
        and "__pycache__" not in p.parts)
    by_id = defaultdict(dict)  # id -> {relpath: outcome}
    for path in files:
        rel = str(path.relative_to(DIV))
        for rec in iter_records(path):
            cid = rec.get("id") or rec.get("case_id")
            if not isinstance(cid, str):
                continue
            oc = extract_outcome(rec)
            if oc is None:
                continue
            by_id[cid].setdefault(rel, oc)

    conflicts, benign = {}, {}
    for cid, srcs in by_id.items():
        if len(srcs) > 1:
            texts = set(srcs.values())
            (conflicts if len(texts) > 1 else benign)[cid] = sorted(srcs)

    meta = json.loads((BENCH / "phase3/runs/round33/judging/host-meta.json")
                      .read_text(encoding="utf-8"))
    dev9 = sorted(meta)
    dev9_conf = {c: conflicts[c] for c in dev9 if c in conflicts}
    dev9_multi = {c: sorted(by_id[c]) for c in dev9 if len(by_id.get(c, {})) > 1}

    report = {
        "files_scanned": len(files),
        "ids_with_outcome": len(by_id),
        "conflict_ids_total": len(conflicts),
        "conflict_ids": {k: conflicts[k] for k in sorted(conflicts)},
        "benign_multi_source_ids": len(benign),
        "dev9_conflict_ids": dev9_conf,
        "dev9_multi_source": dev9_multi,
    }
    (R34 / "audit-ids-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"files scanned: {len(files)}")
    print(f"ids with outcome: {len(by_id)}")
    print(f"CONFLICT ids (same id, different outcome text): {len(conflicts)}")
    for cid in sorted(conflicts):
        print(f"  {cid}: {conflicts[cid]}")
    print(f"benign multi-source ids (same text): {len(benign)}")
    print(f"dev9 ids with conflicts: {sorted(dev9_conf)}")
    print(f"dev9 ids multi-source: {len(dev9_multi)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
