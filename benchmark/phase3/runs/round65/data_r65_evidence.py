#!/usr/bin/env python3
"""R65 data seat evidence dump: structured reads only, no regex truncation of notes.
History glob explicitly excludes round65 outputs (self-nesting guard)."""
import json, re, pathlib, collections

BASE = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
J65 = BASE / "runs/round65/judging"

hm = json.loads((J65 / "host-mapping.json").read_text(encoding="utf-8"))
om = json.loads((J65 / "outcome-manifest.json").read_text(encoding="utf-8"))
cases = om["cases"]

SEATS = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3", "Y4"]

def parse_flags_file(path):
    """Parse one FLAGS file into entries {anon, gist, excerpt} by line structure."""
    lines = path.read_text(encoding="utf-8").splitlines()
    entries = []
    cur = None
    for ln in lines:
        m = re.search(r"P3-[0-9a-f]{8}", ln)
        if m and ("anon_id" in ln or ln.strip().startswith("#") or ln.strip().startswith("- anon")):
            if cur:
                entries.append(cur)
            cur = {"anon": m.group(0), "gist": "", "excerpt": ""}
            continue
        if cur is None:
            continue
        if "旗标要旨" in ln:
            cur["gist"] = ln.split("：", 1)[-1].split(":", 1)[-1].strip() if "：" in ln or ":" in ln else ln.strip()
            # more robust: take text after first colon
            idx = max(ln.find("："), ln.find(":"))
            cur["gist"] = ln[idx+1:].strip()
        elif "结局原文逐字摘录" in ln or "結局原文逐字摘錄" in ln:
            idx = max(ln.find("："), ln.find(":"))
            cur["excerpt"] = ln[idx+1:].strip().strip("「」『』\"")
    if cur:
        entries.append(cur)
    return entries

per_seat = {}
for s in SEATS:
    per_seat[s] = parse_flags_file(J65 / f"FLAGS-{s}.md")

selfrep = (J65 / "FLAGS-selfreported-r65.md").read_text(encoding="utf-8")
# verify: each seat file's anon set appears in selfreported; gist substring check (normalized whitespace)
verify = {}
for s, ents in per_seat.items():
    ok = []
    for e in ents:
        in_self = e["anon"] in selfrep
        # gist core: strip punctuation, check first 12 chars present
        core = e["gist"][:12]
        gist_in = core in selfrep.replace(" ", "")
        ok.append({"anon": e["anon"], "in_selfrep": in_self, "gist_head_in_selfrep": gist_in})
    verify[s] = ok

# history: explicit rounds list, exclude r65
HIST_ROUNDS = [49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]
history = {}  # case_id -> list of {round, disposition, relation, finding_head, flag}
for r in HIST_ROUNDS:
    p = BASE / f"data/case-annotations-r{r}.json"
    if not p.exists():
        continue
    d = json.loads(p.read_text(encoding="utf-8"))
    for a in d["annotations"]:
        history.setdefault(a["case_id"], []).append({
            "round": r,
            "disposition": a.get("disposition") or ("类型标注：" + a.get("type_label", "")),
            "relation": a.get("relation", ""),
            "finding": a.get("finding") or a.get("basis", ""),
            "flag": a.get("flag", ""),
            "manifest_carry_suggestion": a.get("manifest_carry_suggestion", ""),
        })

# unique anons in order of first appearance in selfreported
seen = []
for m in re.finditer(r"P3-[0-9a-f]{8}", selfrep):
    a = m.group(0)
    if a not in seen:
        seen.append(a)

out_entries = []
for anon in seen:
    cid = hm[anon]
    seats_for = []
    gists = []
    excerpts = []
    for s, ents in per_seat.items():
        for e in ents:
            if e["anon"] == anon:
                seats_for.append(s)
                gists.append(f"{s}：{e['gist']}")
                excerpts.append(e["excerpt"])
    outcome = cases[cid]
    # excerpt verbatim check: normalize by removing whitespace
    def norm(t):
        return re.sub(r"\s+", "", t)
    excerpt_checks = []
    for ex in excerpts:
        excerpt_checks.append({"excerpt": ex, "verbatim_in_outcome": norm(ex) in norm(outcome) if ex else None})
    inp_path = BASE / f"inputs-dev12/{cid}.json"
    inp = json.loads(inp_path.read_text(encoding="utf-8")) if inp_path.exists() else {}
    question = inp.get("context", {}).get("question", "")
    setting = inp.get("context", {}).get("setting", "")
    pred_path = BASE / f"runs/round65/predictions/{cid}.json"
    pred = ""
    if pred_path.exists():
        pred = json.loads(pred_path.read_text(encoding="utf-8")).get("prediction_text", "")
    out_entries.append({
        "anon": anon, "case_id": cid, "seats": seats_for, "gists": gists,
        "excerpts": excerpts, "excerpt_checks": excerpt_checks,
        "outcome": outcome, "question": question, "setting": setting,
        "prediction_text": pred,
        "history": history.get(cid, []),
    })

# directive-word scan over all 487 outcomes (data processing only)
KEYS = ["请按", "须注", "评分时", "比对时", "比对须", "使用时须", "请注", "须分开统计", "评分", "盲测"]
scan = {}
for cid, txt in cases.items():
    hits = [k for k in KEYS if k in txt]
    if hits:
        scan[cid] = {"hits": hits, "outcome": txt}
# also scan editor_note layer
lr_split = om.get("_r56_lr2016_split", {})

result = {
    "flag_rows_total": sum(len(v) for v in per_seat.values()),
    "unique_anons": len(seen),
    "verify_selfrep": verify,
    "entries": out_entries,
    "directive_scan": scan,
    "lr2016_split": lr_split,
    "cases_total": len(cases),
}
(BASE / "runs/round65/data_r65_evidence.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
print("rows", result["flag_rows_total"], "unique", len(seen))
print("directive scan cases:", list(scan.keys()))
for cid, v in scan.items():
    print(cid, v["hits"], v["outcome"][:200])
print("lr split:", json.dumps(lr_split, ensure_ascii=False)[:600])
bad = [(e["anon"], e["case_id"]) for e in out_entries for c in e["excerpt_checks"] if c["verbatim_in_outcome"] is False]
print("excerpt NOT verbatim:", bad)
