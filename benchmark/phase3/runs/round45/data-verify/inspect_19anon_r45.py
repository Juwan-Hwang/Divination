#!/usr/bin/env python3
"""R45 data seat: exact-id source lookup for the 19 R44 anon flags.
Only reads: round44 outcome-manifest, inputs-dev12/<id>.json, and
answers.jsonl / cases.jsonl / cases-reviewed.jsonl under phase3/expansion*
and masters-dataset/. Prints matched lines' key fields only."""
import json, os, sys

BASE = os.path.expanduser("~/workspace/divination")
P3 = os.path.join(BASE, "benchmark/phase3")
CASES = {
    # double-report
    "LY-011": "double", "LY-023": "double", "LY-206": "double",
    "LY-222": "double", "LY-430": "double", "LY-437": "double",
    "LY-533": "double", "LR2-022": "double", "LR2-023": "double",
    "LR3-112": "double", "OC-029": "double",
    # single named
    "LY-220": "single-named", "LY-426": "single-named",
    "LY-432": "single-named", "LY-526": "single-named",
    # single anon -> mapped
    "BQ-001": "single-anon:P3-c4600500", "LY-517": "single-anon:P3-e7f0d59d",
    "LR3-107": "single-anon:P3-19688ca8", "YM-070": "single-anon:P3-8fcaabc5",
}
ALLOWED = {"answers.jsonl", "cases.jsonl", "cases-reviewed.jsonl"}

manifest = json.load(open(os.path.join(
    P3, "runs/round44/judging/outcome-manifest.json")))["cases"]

roots = []
for d in sorted(os.listdir(P3)):
    if d.startswith("expansion") and os.path.isdir(os.path.join(P3, d)):
        roots.append(os.path.join(P3, d))
roots.append(os.path.join(BASE, "masters-dataset"))

files = []
for root in roots:
    for dirpath, _dirs, names in os.walk(root):
        for n in names:
            if n in ALLOWED:
                files.append(os.path.join(dirpath, n))
files.sort()

def grab(obj, keys, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in keys and isinstance(v, str) and v.strip():
                out.append(f"{k}={v}")
            else:
                grab(v, keys, out)
    elif isinstance(obj, list):
        for v in obj:
            grab(v, keys, out)

KEYS = {"statement_excerpt", "description", "comment", "question",
        "outcome_text", "master_prediction", "prediction", "断语", "结局"}

for cid, src in CASES.items():
    print(f"\n===== {cid} [{src}] =====")
    inp = json.load(open(os.path.join(P3, "inputs-dev12", cid + ".json")))
    ctx = inp.get("context", {})
    print("QUESTION:", ctx.get("question"))
    print("SETTING:", (ctx.get("setting") or "")[:300])
    print("PROV:", json.dumps(inp.get("provenance", {}), ensure_ascii=False)[:300])
    print("OUTCOME(manifest):", manifest.get(cid))
    hits = 0
    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if f'"{cid}"' not in line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                if obj.get("id") != cid and obj.get("case_id") != cid:
                    continue
                hits += 1
                rel = os.path.relpath(f, BASE)
                fields = []
                grab(obj, KEYS, fields)
                print(f"-- SRC {rel}")
                for x in fields[:8]:
                    print("   ", x[:600])
    if not hits:
        print("-- SRC: NO MATCH in allowed files")
print("\nDONE", len(files), "files scanned")
