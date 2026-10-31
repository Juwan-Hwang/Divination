#!/usr/bin/env python3
"""R66 data seat evidence dump: structured reads only.
History enumerated explicitly (r49,r50,r51,r53-r65); round66 outputs excluded."""
import json, re, pathlib

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
J66 = BASE / "runs/round66/judging"

hm = json.loads((J66 / "host-mapping.json").read_text(encoding="utf-8"))
om = json.loads((J66 / "outcome-manifest.json").read_text(encoding="utf-8"))
cases = om["cases"]
om65 = json.loads((BASE / "runs/round65/judging/outcome-manifest.json").read_text(encoding="utf-8"))
cases_equal = sum(1 for k in cases if cases[k] == om65["cases"].get(k))
print("cases equal vs R65:", cases_equal, "/", len(cases))

SEATS = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3", "Y4"]

def parse_flags_file(path):
    """Split file into blocks per anon occurrence; keep raw block text."""
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"(P3-[0-9a-f]{8})", text)
    entries = []
    # parts: [pre, anon, rest, anon, rest...]
    for i in range(1, len(parts), 2):
        anon = parts[i]
        block = parts[i + 1] if i + 1 < len(parts) else ""
        block = block[:1500].replace("\n", " ").strip()
        entries.append({"anon": anon, "block": block})
    return entries

per_seat = {}
for s in SEATS:
    per_seat[s] = parse_flags_file(J66 / f"FLAGS-{s}.md")
rows_total = sum(len(v) for v in per_seat.values())
print("flag rows total:", rows_total, {s: len(v) for s, v in per_seat.items()})

selfrep = (J66 / "FLAGS-selfreported-r66.md").read_text(encoding="utf-8")
# verify each seat anon appears in selfreported
verify = {s: all(e["anon"] in selfrep for e in ents) for s, ents in per_seat.items()}
print("selfrep contains all seat anons:", verify)

HIST_ROUNDS = [49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
history = {}
for r in HIST_ROUNDS:
    p = BASE / f"data/case-annotations-r{r}.json"
    if not p.exists():
        print("missing history", r); continue
    d = json.loads(p.read_text(encoding="utf-8"))
    for a in d["annotations"]:
        history.setdefault(a["case_id"], []).append({
            "round": r,
            "disposition": a.get("disposition", ""),
            "relation": a.get("relation", ""),
            "finding": a.get("finding", ""),
            "flag": a.get("flag", ""),
            "manifest_carry_suggestion": a.get("manifest_carry_suggestion", ""),
        })

# unique anons in order of first appearance across seat files X1..Y4
seen = []
for s in SEATS:
    for e in per_seat[s]:
        if e["anon"] not in seen:
            seen.append(e["anon"])
print("unique anons:", len(seen))

def norm(t):
    return re.sub(r"\s+", "", t)

out_entries = []
for anon in seen:
    cid = hm[anon]
    seats_for, blocks = [], {}
    for s in SEATS:
        for e in per_seat[s]:
            if e["anon"] == anon:
                seats_for.append(s)
                blocks[s] = e["block"]
    outcome = cases[cid]
    inp_path = BASE / f"inputs-dev12/{cid}.json"
    inp = json.loads(inp_path.read_text(encoding="utf-8")) if inp_path.exists() else {}
    question = inp.get("context", {}).get("question", "")
    setting = inp.get("context", {}).get("setting", "")
    pred_path = BASE / f"runs/round66/predictions/{cid}.json"
    pred = ""
    if pred_path.exists():
        pred = json.loads(pred_path.read_text(encoding="utf-8")).get("prediction_text", "")
    out_entries.append({
        "anon": anon, "case_id": cid, "seats": seats_for, "blocks": blocks,
        "outcome": outcome, "question": question, "setting": setting,
        "prediction_text": pred, "history": history.get(cid, []),
    })

# directive-word full scan over 487 outcomes (data processing only)
KEYS = ["请按", "须注", "评分时", "比对时", "比对须", "使用时须", "须分开统计", "勿以此斷", "勿以此断", "请注", "盲测", "评分", "须", "请"]
scan = {}
for cid, txt in cases.items():
    hits = [k for k in KEYS if k in txt]
    if hits:
        scan[cid] = {"hits": hits, "outcome": txt}
lr_split = om.get("_r56_lr2016_split", {})

result = {
    "flag_rows_total": rows_total,
    "unique_anons": len(seen),
    "verify_selfrep": verify,
    "cases_equal_vs_r65": cases_equal,
    "entries": out_entries,
    "directive_scan": scan,
    "lr2016_split": lr_split,
    "cases_total": len(cases),
}
(BASE / "runs/round66/data_r66_evidence.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
print("entries:", len(out_entries))
print("directive scan cases:", sorted(scan.keys()))
for cid in sorted(scan):
    print(cid, scan[cid]["hits"])
print("lr split editor_note:", lr_split.get("editor_note", ""))
