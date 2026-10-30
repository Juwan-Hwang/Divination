#!/usr/bin/env python3
"""R46 data seat: exact-id source lookup for the 11 R45 anon flags.
Only reads: round45 judging host-mapping.json / host-meta.json /
outcome-manifest.json (11 cases only), round45 judging judgeX/judgeY
block files (reason field, by anon only), inputs-dev12/<id>.json, and
answers.jsonl / cases.jsonl / cases-reviewed.jsonl under phase3/expansion*
and masters-dataset/. Prints matched lines' key fields only.
Does NOT read any predictions, old-round basis, or final-scores."""
import json, os, glob

BASE = os.path.expanduser("~/workspace/divination")
P3 = os.path.join(BASE, "benchmark/phase3")
CASES = ["LY-259", "LY-510", "YM-030", "LY-513", "LR3-002", "AS-015",
         "BQ-017", "LY-623", "LY-504", "LY-205", "LY-458"]
ALLOWED = {"answers.jsonl", "cases.jsonl", "cases-reviewed.jsonl"}

JUD = os.path.join(P3, "runs/round45/judging")
mapping = json.load(open(os.path.join(JUD, "host-mapping.json")))
inv = {v: k for k, v in mapping.items()}
meta = json.load(open(os.path.join(JUD, "host-meta.json")))
manifest = json.load(open(os.path.join(JUD, "outcome-manifest.json")))["cases"]

# judge reasons by anon (round45 block files only)
judge_reasons = {}
for f in sorted(glob.glob(os.path.join(JUD, "judge*-block*.jsonl"))):
    seat = os.path.basename(f).split("-")[0]  # judgeX / judgeY
    with open(f, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                obj = json.loads(line)
            except Exception:
                continue
            anon = obj.get("anon_id")
            if anon in {inv.get(c) for c in CASES}:
                judge_reasons.setdefault(anon, []).append(
                    (seat, os.path.basename(f), obj.get("reason")))

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
            elif k == "key_assertions" and isinstance(v, list):
                out.append("key_assertions=" + "；".join(str(x) for x in v))
            else:
                grab(v, keys, out)
    elif isinstance(obj, list):
        for v in obj:
            grab(v, keys, out)

KEYS = {"statement_excerpt", "description", "comment", "question",
        "outcome_text", "master_prediction", "prediction", "key_assertions"}

for cid in CASES:
    anon = inv.get(cid)
    print(f"\n===== {cid} [anon={anon}] =====")
    print("META:", json.dumps(meta.get(cid), ensure_ascii=False))
    for seat, bf, reason in judge_reasons.get(anon, []):
        print(f"JUDGE-REASON({seat}/{bf}):", reason)
    if anon not in judge_reasons:
        print("JUDGE-REASON: NO MATCH in judge block files")
    inp = json.load(open(os.path.join(P3, "inputs-dev12", cid + ".json")))
    ctx = inp.get("context", {})
    print("QUESTION:", ctx.get("question"))
    print("SETTING:", (ctx.get("setting") or "")[:500])
    print("PROV:", json.dumps(inp.get("provenance", {}), ensure_ascii=False)[:500])
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
                for x in fields[:10]:
                    print("   ", x[:900])
    if not hits:
        print("-- SRC: NO MATCH in allowed files")
print("\nDONE", len(files), "files scanned")
