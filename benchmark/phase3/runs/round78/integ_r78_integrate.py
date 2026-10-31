#!/usr/bin/env python3
# R78-REV1 integration + self-verification. Draft text is extracted
# programmatically from the proposal file; nothing is hand-transcribed.
import hashlib, json, os, sys, difflib

BASE = "/home/hatch/workspace/divination"
PROP = BASE + "/benchmark/phase3/runs/round78/diagnosis/REVISION-PROPOSAL-r78.md"
CAL = BASE + "/benchmark/phase3/method/references/calibration.md"
SKILL = BASE + "/benchmark/phase3/method/SKILL.md"
METHOD = BASE + "/benchmark/phase3/method"
SNAP = BASE + "/benchmark/phase3/runs/round78/kb-snapshot"
REPORT = BASE + "/benchmark/phase3/runs/round78/integ_r78_report.json"

def sha(b): return hashlib.sha256(b).hexdigest()

prop_lines = open(PROP, encoding="utf-8").read().split("\n")

def section_range(start_marker, end_marker):
    s = next(i for i, l in enumerate(prop_lines) if l.startswith(start_marker))
    e = next(i for i, l in enumerate(prop_lines) if i > s and l.startswith(end_marker))
    return s, e

def unquote(lines):
    out = []
    for l in lines:
        if l == ">":
            out.append("")
        elif l.startswith("> "):
            out.append(l[2:])
        else:
            raise SystemExit("non-quote line inside draft block: %r" % l)
    return out

# --- extract section 7 draft (proposal 2.1) ---
s21, e21 = section_range("### 2.1", "### 2.2")
block21 = [l for l in prop_lines[s21:e21] if l.startswith(">")]
draft_lines = unquote(block21)
while draft_lines and draft_lines[-1] == "":
    draft_lines.pop()
while draft_lines and draft_lines[0] == "":
    draft_lines.pop(0)
assert draft_lines[0].startswith("## 七、主断方向双路对决前置裁决"), draft_lines[0]
draft_text = "\n".join(draft_lines) + "\n"

# --- extract (o) pointer line (proposal 2.2) ---
s22, e22 = section_range("### 2.2", "## 3.")
block22 = [l for l in prop_lines[s22:e22] if l.startswith(">")]
ptr_lines = unquote(block22)
ptr = [l for l in ptr_lines if l.startswith("- (o)")]
assert len(ptr) == 1, ptr
o_line = ptr[0]
assert o_line == "- (o) 方向对决：作断起手先行主断方向双路对决前置裁决（正本见 references/calibration.md 第七节，R78-REV1，自集成之次轮起算效力）", o_line

# --- read targets, record before state ---
cal_before = open(CAL, "rb").read()
skill_before = open(SKILL, "rb").read()
cal_before_t = cal_before.decode("utf-8")
skill_before_t = skill_before.decode("utf-8")
assert cal_before_t.endswith("\n") and not cal_before_t.endswith("\n\n")

# --- build new calibration: old + one blank line + draft verbatim ---
cal_after_t = cal_before_t + "\n" + draft_text

# --- build new SKILL: insert (o) line right after the (n) line ---
slines = skill_before_t.split("\n")
n_idx = [i for i, l in enumerate(slines) if l.startswith("- (n)")]
assert len(n_idx) == 1, n_idx
assert not any(l.startswith("- (o)") for l in slines)
slines.insert(n_idx[0] + 1, o_line)
skill_after_t = "\n".join(slines)

# --- write ---
open(CAL, "w", encoding="utf-8", newline="").write(cal_after_t)
open(SKILL, "w", encoding="utf-8", newline="").write(skill_after_t)

# --- re-read from disk and verify ---
cal_after = open(CAL, "rb").read()
skill_after = open(SKILL, "rb").read()
cal_after_t2 = cal_after.decode("utf-8")
skill_after_t2 = skill_after.decode("utf-8")

checks = {}
# (2) calibration == before + blank line + draft verbatim
checks["cal_append_exact"] = (cal_after_t2 == cal_before_t + "\n" + draft_text)
# (3) SKILL diff is exactly the (o) line
diff = list(difflib.unified_diff(skill_before_t.split("\n"), skill_after_t2.split("\n"), lineterm=""))
added = [l[1:] for l in diff if l.startswith("+") and not l.startswith("+++")]
removed = [l[1:] for l in diff if l.startswith("-") and not l.startswith("---")]
checks["skill_diff_added"] = added
checks["skill_diff_removed"] = removed
checks["skill_diff_exact"] = (added == [o_line] and removed == [])
# (5) strip-back
stripped_cal = cal_after_t2[: len(cal_before_t)]
checks["stripback_cal_prefix_is_before"] = (stripped_cal == cal_before_t and sha(stripped_cal.encode()) == sha(cal_before))
rest = cal_after_t2[len(cal_before_t):]
checks["stripback_cal_remainder"] = (rest == "\n" + draft_text)
alines = skill_after_t2.split("\n")
o_idx = [i for i, l in enumerate(alines) if l == o_line]
assert len(o_idx) == 1
del alines[o_idx[0]]
stripped_skill = "\n".join(alines)
checks["stripback_skill_sha_equal"] = (sha(stripped_skill.encode()) == sha(skill_before))
checks["stripback_ok"] = checks["stripback_cal_prefix_is_before"] and checks["stripback_cal_remainder"] and checks["stripback_skill_sha_equal"]

# (4) all other method files vs kb-snapshot counterparts
others = []
for root, dirs, files in os.walk(METHOD):
    dirs.sort()
    for f in sorted(files):
        p = os.path.join(root, f)
        rel = os.path.relpath(p, METHOD)
        if p in (CAL, SKILL):
            continue
        snap_p = os.path.join(SNAP, rel)
        entry = {"rel": rel}
        if not os.path.exists(snap_p):
            entry["snapshot_exists"] = False
            entry["equal"] = False
        else:
            entry["snapshot_exists"] = True
            entry["method_sha"] = sha(open(p, "rb").read())
            entry["snapshot_sha"] = sha(open(snap_p, "rb").read())
            entry["equal"] = entry["method_sha"] == entry["snapshot_sha"]
        others.append(entry)
checks["others_count"] = len(others)
checks["others_all_equal"] = all(e.get("equal") for e in others)

report = {
    "calibration": {"before_sha256": sha(cal_before), "before_bytes": len(cal_before),
                    "after_sha256": sha(cal_after), "after_bytes": len(cal_after)},
    "skill": {"before_sha256": sha(skill_before), "before_bytes": len(skill_before),
              "after_sha256": sha(skill_after), "after_bytes": len(skill_after)},
    "draft_lines": len(draft_lines),
    "o_line": o_line,
    "checks": checks,
    "others": others,
}
open(REPORT, "w", encoding="utf-8").write(json.dumps(report, ensure_ascii=False, indent=1))
print(json.dumps({k: report[k] for k in ("calibration", "skill", "draft_lines")}, ensure_ascii=False))
print("cal_append_exact:", checks["cal_append_exact"])
print("skill_diff_exact:", checks["skill_diff_exact"], "| added:", added, "| removed:", removed)
print("stripback_ok:", checks["stripback_ok"])
print("others_count:", checks["others_count"], "| others_all_equal:", checks["others_all_equal"])
for e in others:
    if not e.get("equal"):
        print("MISMATCH/MISSING:", e)
sys.exit(0 if (checks["cal_append_exact"] and checks["skill_diff_exact"] and checks["stripback_ok"] and checks["others_all_equal"]) else 1)
