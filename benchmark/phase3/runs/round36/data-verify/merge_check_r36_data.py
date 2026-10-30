#!/usr/bin/env python3
"""R36 data-verify: check staging IDs against live method/references.
Only reads; writes one output txt beside this script.
Defined-ID extraction: IDs appearing in a heading line or at start of a
bold/list entry, deduplicated, sorted. Fallback: all unique IDs.
"""
import re, pathlib, json

BASE = pathlib.Path.home() / "workspace/divination/benchmark/phase3"
REFS = BASE / "method/references"
OUT = pathlib.Path(__file__).with_name("merge-check-r36-output.txt")

live = {}
for p in sorted(REFS.glob("*.md")):
    live[p.name] = p.read_text(errors="ignore").splitlines()

def find_id(idstr):
    hits = []
    for fname, lines in live.items():
        for i, ln in enumerate(lines, 1):
            if idstr in ln:
                hits.append(f"{fname}:{i}")
                break
    return hits

def extract(path, patterns):
    text = (BASE / path).read_text(errors="ignore")
    lines = text.splitlines()
    defined = []
    seen = set()
    pat = re.compile("|".join(patterns))
    for ln in lines:
        is_def = ln.startswith("#") or ln.startswith("**") or ln.startswith("- **") or re.match(r"^-?\s*\*\*[A-Z]", ln) or re.match(r"^(M|P)\d+\s", ln)
        for m in pat.findall(ln):
            tok = m if isinstance(m, str) else m[0]
            if tok not in seen:
                seen.add(tok); defined.append(tok)
    return defined, text

JOBS = [
    ("1-duanan", "expansion12/liuren-duanan/METHOD-EXTRACTION.md", [r"DA-M\d+"]),
    ("2-bianyi-yuce", "expansion12/liuren-bianyi-yuce/METHOD-EXTRACTION.md", [r"G-BY-[A-Z]\d+", r"G-YX-[A-Z]\d+", r"G-YC-[A-Z]\d+"]),
    ("3-cuiyan", "expansion12/liuren-cuiyan/METHOD-EXTRACTION.md", [r"CX-M\d+"]),
    ("4-natal-batch2-QM", "expansion12/natal-batch2/METHOD-EXTRACTION.md", [r"QM-M\d+"]),
    ("4-natal-batch2-MP", "expansion12/natal-batch2/METHOD-EXTRACTION.md", [r"MP-P\d+"]),
    ("5-xmt", "expansion12/mingli-tanyuan-zhenben/METHOD-EXTRACTION.md", [r"XMT-\d+"]),
    ("6-ziwei-zz", "expansion12/ziwei-zhongzhou/METHOD-EXTRACTION.md", [r"ZZ-M\d+"]),
    ("7-yuangui", "expansion12/yuangui/METHOD-EXTRACTION.md", [r"YG-M\d+"]),
    ("8-cezi-draft-CZ", "expansion12/cezi-zichu/CHAPTER-DRAFT.md", [r"CZ-M\d+"]),
    ("8-cezi-draft-ZC", "expansion12/cezi-zichu/CHAPTER-DRAFT.md", [r"ZC-M\d+"]),
    ("9-qiongtong", "expansion12/qiongtong-baojian/METHOD-CANDIDATES.md", [r"QT-[A-Z]+\d+"]),
    ("10-online-cezi-cases", "expansion12/online-routes/METHOD-NOTES-cezi.md", [r"CZ-\d+"]),
    ("11-l1", "method-extraction/l1/DRAFT.md", [r"L1-\d+"]),
    ("11-l2", "method-extraction/l2/DRAFT.md", [r"L2-\d+"]),
    ("11-b1", "method-extraction/b1/DRAFT.md", [r"B1-\d+"]),
]

report = []
summary = {}
for name, rel, pats in JOBS:
    ids, _ = extract(rel, pats)
    found, missing = {}, []
    for i in ids:
        h = find_id(i)
        if h: found[i] = h
        else: missing.append(i)
    summary[name] = {"total_defined_unique": len(ids), "found": len(found), "missing": missing}
    report.append(f"\n===== {name}  src={rel}  defined_unique={len(ids)} found_in_live={len(found)} missing={len(missing)} =====")
    report.append("MISSING: " + (", ".join(missing) if missing else "(none)"))
    for i in ids:
        report.append(f"  {i}: {' ; '.join(found[i]) if i in found else 'NOT FOUND'}")

# Keyword / layer probes
report.append("\n===== KEYWORD PROBES IN LIVE REFS =====")
for kw in ["穷通", "QT-", "中州", "ZZ-M", "元龟", "YG-M", "粹言", "CX-M", "千里命稿", "QM-M", "袁氏命谱", "MP-P", "新命理探原", "XMT-", "字触", "ZC-M", "测字秘牒", "CZ-M", "断案", "辨疑", "预测学", "G-BY", "G-YX"]:
    hits = []
    for fname, lines in live.items():
        for i, ln in enumerate(lines, 1):
            if kw in ln:
                hits.append(f"{fname}:{i}:{ln.strip()[:140]}")
    report.append(f"\n-- {kw}: {len(hits)} lines")
    for h in hits[:12]:
        report.append("   " + h)

# z1 heading overlap
report.append("\n===== Z1 vs live chinese-ziwei headings =====")
z1 = (BASE / "method-extraction/z1/DRAFT-chinese-ziwei.md").read_text(errors="ignore").splitlines()
live_ziwei = live.get("chinese-ziwei.md", [])
live_set = set(l.strip() for l in live_ziwei)
z_heads = [l.strip() for l in z1 if l.startswith("#")]
same = [h for h in z_heads if h in live_set]
report.append(f"z1 headings={len(z_heads)} identical_in_live_ziwei={len(same)}")
for h in z_heads:
    report.append(f"  {'IN ' if h in live_set else 'OUT'} {h[:150]}")
report.append(f"live chinese-ziwei.md lines={len(live_ziwei)} ; z1 lines={len(z1)}")
# first lines comparison
report.append("live ziwei first 5: " + " | ".join(live_ziwei[:5]))
report.append("z1 first 5: " + " | ".join(z1[:5]))

OUT.write_text("\n".join(report) + "\n\nSUMMARY_JSON\n" + json.dumps(summary, ensure_ascii=False, indent=1))
print(json.dumps(summary, ensure_ascii=False, indent=1))
print("wrote", OUT)
