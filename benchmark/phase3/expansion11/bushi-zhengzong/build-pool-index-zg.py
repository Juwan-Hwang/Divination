#!/usr/bin/env python3
"""expansion11 ZG dedup index builder.
Collects (id, question, asked_at, subject) from all pool sources named in task:
masters-dataset all volumes, benchmark/phase3 splits3/4/5/7/8/9 referenced ids are
covered via roster/inputs corpora, holdout3..holdout10 gold, all expansion*/cases
or inputs/answers jsonl, inputs-dev10/.
Output: bszs_pool_index_zg.jsonl in this batch dir (work product, not a case file).
"""
import json, glob, os, sys

BASE = "/home/hatch/workspace/divination"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "work", "pool-index-zg.jsonl")

seen = {}

def add(rec, source):
    cid = rec.get("id")
    if not cid or cid in seen:
        return
    ctx = rec.get("context", {}) if isinstance(rec.get("context"), dict) else {}
    subj = rec.get("subject", {}) if isinstance(rec.get("subject"), dict) else {}
    seen[cid] = {
        "id": cid,
        "question": ctx.get("question"),
        "asked_at": ctx.get("asked_at"),
        "subject": subj.get("name_or_desc"),
        "source": source,
    }

def load_jsonl(path):
    for line in open(path, encoding="utf-8", errors="ignore"):
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except Exception:
            continue
        if isinstance(o, dict):
            add(o, os.path.relpath(path, BASE))

def load_json_dir(path_glob):
    for p in sorted(glob.glob(path_glob)):
        try:
            o = json.load(open(p, encoding="utf-8"))
        except Exception:
            continue
        if isinstance(o, dict):
            add(o, os.path.relpath(p, BASE))

# masters-dataset all volumes
for p in glob.glob(BASE + "/masters-dataset/**/*.jsonl", recursive=True):
    load_jsonl(p)
# expansion*/ cases + inputs/answers
for p in glob.glob(BASE + "/benchmark/phase3/expansion*/**/*.jsonl", recursive=True):
    load_jsonl(p)
for p in glob.glob(BASE + "/benchmark/phase3/expansion/*.jsonl"):
    load_jsonl(p)
# holdout gold
for i in range(3, 11):
    for p in glob.glob(BASE + f"/benchmark/phase3/holdout{i}/**/*.jsonl", recursive=True):
        load_jsonl(p)
# phase3 inputs dirs (inputs, inputs-dev10, inputs9, inputs10, inputs6..9)
for d in ["inputs", "inputs-dev10", "inputs-dev9", "inputs9", "inputs10", "inputs6", "inputs7", "inputs8", "inputs9"]:
    load_json_dir(BASE + f"/benchmark/phase3/{d}/*.json")
# roster files
for p in glob.glob(BASE + "/benchmark/phase3/roster*.jsonl") + glob.glob(BASE + "/benchmark/phase3/data/roster*.jsonl"):
    load_jsonl(p)
# expansion10 cases
for p in glob.glob(BASE + "/benchmark/phase3/expansion10/*/cases.jsonl"):
    load_jsonl(p)

with open(OUT, "w", encoding="utf-8") as f:
    for cid in sorted(seen):
        f.write(json.dumps(seen[cid], ensure_ascii=False) + "\n")
print(f"indexed {len(seen)} unique ids -> {OUT}")
bszs = [v for v in seen.values() if v["id"].startswith("LY-")]
print("LY ids:", len(bszs))
