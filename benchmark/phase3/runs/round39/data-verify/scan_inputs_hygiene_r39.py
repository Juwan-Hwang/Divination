#!/usr/bin/env python3
"""R39 data seat: inputs-dev11 hygiene scan (count only, no card edits).
Extracts all non-question fields from each card and flags candidate
prediction/outcome-directional text for manual adjudication.
Core question fields excluded from flagging: context.question,
subject.name_or_desc/basic_info/birth/gender, chart attachments that are
pure chart data (hexagram names, pillars, casting, lines, etc.).
Fields scanned: provenance.* (all), notes.*, master/system/era/title-like,
context.setting, context.asked_at, context.attachments.note/chart_note/source/
secondhand/completeness_basis/chart_excerpt, subject.birth.note.
Output: candidates_hygiene_r39.jsonl in same dir.
"""
import json, glob, os, re

BASE = "/home/hatch/workspace/divination/benchmark/phase3/inputs-dev11"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "candidates_hygiene_r39.jsonl")

# patterns indicating a prediction statement or outcome direction in EN/ZH
PATTERNS = [
    (r"predict(ed|s|ion)?\b.{0,80}(win|won|victory|elected|president|seat)", "en-prediction-outcome"),
    (r"(will|would)\s+(win|be crowned|become|die|recover|marry|succeed)", "en-future-outcome"),
    (r"trump-will-be|would-win|will-win|predicted.*win|who-predicted", "url-slug-prediction"),
    (r"(forecast|prophe|omen).{0,60}(win|die|death|recover|success|fail)", "en-forecast"),
    (r"果(然|驗|验|中|死|生|至|歸|归|得|應|应)", "zh-outcome-guo"),
    (r"(斷曰|断曰|占曰|曰).{0,40}(必|當|当|果|死|生男|生女|中|勝|胜|敗|败)", "zh-judgment"),
    (r"(後|后).{0,20}(果|驗|验|卒|死|中|歸|归|生)", "zh-later-outcome"),
    (r"(應驗|应验|驗證|验证|結局|结局|結果|结果).{0,30}", "zh-verification"),
    (r"(必死|必中|當選|当选|勝選|胜选|落選|落选|登第|及第|陞遷|升迁|病癒|病愈|不治|身亡|去世|逝世)", "zh-directional"),
    (r"(died|death of|recovered|was elected|won the|lost the|gave birth|married .* (in|by)|succeeded)", "en-outcome-event"),
    (r"(judg(e)?ment|judged).{0,80}(would|will|shall|die|recover|live|marry)", "en-judgment"),
    (r"(in fact|eventually|afterwards|later).{0,60}(died|recovered|won|married|returned)", "en-later-outcome"),
]

def get_nested(d, path):
    cur = d
    for p in path.split("."):
        if isinstance(cur, dict) and p in cur:
            cur = cur[p]
        else:
            return None
    return cur

SCAN_PATHS = []
def collect_paths(d, prefix=""):
    paths = []
    if isinstance(d, dict):
        for k, v in d.items():
            p = f"{prefix}.{k}" if prefix else k
            if isinstance(v, (dict, list)):
                paths += collect_paths(v, p)
            else:
                paths.append((p, str(v)))
    elif isinstance(d, list):
        for i, v in enumerate(d):
            if isinstance(v, (dict, list)):
                paths += collect_paths(v, prefix)
            else:
                paths.append((prefix, str(v)))
    return paths

EXCLUDE_PREFIXES = (
    "context.question", "subject.name_or_desc", "subject.basic_info",
    "subject.gender", "subject.birth.date", "subject.birth.time",
    "subject.birth.place", "subject.birth.pillars",
    "context.attachments.hexagram", "context.attachments.pillars",
    "context.attachments.casting", "context.attachments.chart_lines",
    "context.attachments.lines_top_to_bottom", "context.attachments.moving_lines",
    "context.attachments.hidden_lines", "context.attachments.date_ganzhi",
    "context.attachments.casting_method", "context.casting_method",
    "context.attachments.ben_gua", "context.attachments.bian_gua",
    "context.attachments.configuration", "context.hexagram",
    "language", "id", "uid", "tradition", "system", "license_status",
    "redistributable", "source_id", "era",
)
# chart-data attachments that are pure data even if not listed above
CHART_OK_KEYS = {"ascendant","asc_ruler","key_positions","yongshen","空亡","月将","三传","四课","课式","chart_complete","completeness_basis","hidden_spirit","day_master","chart_note"}

rows = []
for f in sorted(glob.glob(os.path.join(BASE, "*.json"))):
    d = json.load(open(f))
    cid = d.get("id") or d.get("uid") or os.path.basename(f)
    for path, val in collect_paths(d):
        if any(path == e or path.startswith(e + ".") for e in EXCLUDE_PREFIXES):
            continue
        last = path.split(".")[-1]
        if last in CHART_OK_KEYS and path.startswith("context.attachments"):
            continue
        if not val.strip():
            continue
        hits = []
        for pat, name in PATTERNS:
            if re.search(pat, val, flags=re.I):
                hits.append(name)
        if hits:
            rows.append({"id": cid, "file": os.path.basename(f), "field": path, "patterns": hits, "value": val[:600]})

with open(OUT, "w") as fh:
    for r in rows:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"candidate rows: {len(rows)}")
from collections import Counter
print(Counter(r["id"] for r in rows))
print(Counter(r["field"] for r in rows))
