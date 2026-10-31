#!/usr/bin/env python3
"""R88 host tooling adapter: derive round88 host scripts from round87
originals by POINT replacements only. Every replacement carries an
expected hit count and asserts it (hit-range verification per the
anti-chained-replacement rule); any mismatch aborts before writing.
Post-run residual scan is done by the host separately.
"""
from pathlib import Path

R87 = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round87")
R88 = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round88")


def rep(t, old, new, expected, tag):
    c = t.count(old)
    assert c == expected, f"{tag}: {old!r} hits {c}, expected {expected}"
    return t.replace(old, new)


def adapt(src_name, dst_name, steps):
    t = (R87 / src_name).read_text(encoding="utf-8")
    for old, new, n, tag in steps:
        t = rep(t, old, new, n, f"{dst_name}:{tag}")
    (R88 / dst_name).write_text(t, encoding="utf-8")
    print("written", dst_name)


# ---------------- verify_predictions_host_r88.py ----------------
adapt("verify_predictions_host_r87.py", "verify_predictions_host_r88.py", [
    ("round87", "round88", 2, "paths"),
    ("R87", "R88", 5, "round-var-and-title"),
    ("r87", "r88", 3, "filenames"),
    ("PREREG-r88 s.7", "PREREG-r88 s.6", 1, "checker-set-section"),
])

# ---------------- build_judge_packets_r88.py ----------------
adapt("build_judge_packets_r87.py", "build_judge_packets_r88.py", [
    ("Round 87 judging packet builder (host tooling, build-only; no scoring).",
     "Round 88 judging packet builder (host tooling, build-only; no scoring).", 1, "title"),
    ("(R87 build per PREREG s.0: 487 cases verbatim, LR2-016 editor note split-registered, thirty-one carryover note layers attached as separate packet fields (incl. the new _r86_carryover_notes_addendum layer, 45 cases per R87 opening registration))",
     "(R88 build per PREREG s.0: 487 cases verbatim, LR2-016 editor note split-registered, thirty-two carryover note layers attached as separate packet fields (incl. the new _r87_carryover_notes_addendum layer, 43 cases per R88 opening registration))", 1, "docstring-layers"),
    ("anon seed 20261101", "anon seed 20261103", 1, "docstring-seed"),
    ("SEED = 20261101", "SEED = 20261103", 1, "seed"),
    ('ROUND_DIR.parent / "round86" / "judging" / "host-meta.json"',
     'ROUND_DIR.parent / "round87" / "judging" / "host-meta.json"', 1, "meta-src"),
    ("(round86 judging copy)", "(round87 judging copy)", 1, "meta-doc"),
    ('    carry86 = manifest.get("_r86_carryover_notes_addendum", {})\n',
     '    carry86 = manifest.get("_r86_carryover_notes_addendum", {})\n'
     '    carry87 = manifest.get("_r87_carryover_notes_addendum", {})\n', 1, "carry87-load"),
    ("and len(carry85) == 12 and len(carry86) == 45, (",
     "and len(carry85) == 12 and len(carry86) == 45 and len(carry87) == 43, (", 1, "carry87-assert"),
    ("len(carry56), len(carry57), len(carry58), len(carry59), len(carry60a), len(carry60b), len(carry61), len(carry62), len(carry63), len(carry64), len(carry65), len(carry66), len(carry67), len(carry68), len(carry69), len(carry70), len(carry71), len(carry72), len(carry73), len(carry74), len(carry75), len(carry76), len(carry77), len(carry79), len(carry80), len(carry81), len(carry82), len(carry83), len(carry84), len(carry85), len(carry86))",
     "len(carry56), len(carry57), len(carry58), len(carry59), len(carry60a), len(carry60b), len(carry61), len(carry62), len(carry63), len(carry64), len(carry65), len(carry66), len(carry67), len(carry68), len(carry69), len(carry70), len(carry71), len(carry72), len(carry73), len(carry74), len(carry75), len(carry76), len(carry77), len(carry79), len(carry80), len(carry81), len(carry82), len(carry83), len(carry84), len(carry85), len(carry86), len(carry87))", 1, "carry87-assert-tuple"),
    ("all_carry = set(carry56) | set(carry57) | set(carry58) | set(carry59) | set(carry60a) | set(carry60b) | set(carry61) | set(carry62) | set(carry63) | set(carry64) | set(carry65) | set(carry66) | set(carry67) | set(carry68) | set(carry69) | set(carry70) | set(carry71) | set(carry72) | set(carry73) | set(carry74) | set(carry75) | set(carry76) | set(carry77) | set(carry79) | set(carry80) | set(carry81) | set(carry82) | set(carry83) | set(carry84) | set(carry85) | set(carry86)",
     "all_carry = set(carry56) | set(carry57) | set(carry58) | set(carry59) | set(carry60a) | set(carry60b) | set(carry61) | set(carry62) | set(carry63) | set(carry64) | set(carry65) | set(carry66) | set(carry67) | set(carry68) | set(carry69) | set(carry70) | set(carry71) | set(carry72) | set(carry73) | set(carry74) | set(carry75) | set(carry76) | set(carry77) | set(carry79) | set(carry80) | set(carry81) | set(carry82) | set(carry83) | set(carry84) | set(carry85) | set(carry86) | set(carry87)", 1, "carry87-union"),
    ('        if cid in carry86:\n            parts.append("[R86-addendum] " + carry86[cid])\n',
     '        if cid in carry86:\n            parts.append("[R86-addendum] " + carry86[cid])\n'
     '        if cid in carry87:\n            parts.append("[R87-addendum] " + carry87[cid])\n', 1, "carry87-parts"),
])

# ---------------- merge_judgments_r88.py ----------------
adapt("merge_judgments_r87.py", "merge_judgments_r88.py", [
    ("Round 87 host tooling", "Round 88 host tooling", 1, "title"),
    ("carried through R83/R84/R85", "carried through R83-R87", 1, "naming-note"),
])

# ---------------- analyze_r88.py ----------------
adapt("analyze_r87.py", "analyze_r88.py", [
    # anchored section-9 fixes first
    ("bazi-all / bazi-natal timing sub-item means R87 vs R86",
     "bazi-all / bazi-natal timing sub-item means R88 vs R87", 1, "s9-doc"),
    ("print('\\n== 9. side reads: bazi timing movement R86 -> R87 ==')",
     "print('\\n== 9. side reads: bazi timing movement R87 -> R88 ==')", 1, "s9-print"),
    ("prev_timing[label]['timing_mean_r86']",
     "prev_timing[label]['timing_mean_r87']", 1, "s9-prev-key"),
    ("timing_reads[label] = {'timing_mean_r87': round(t77, 3), 'timing_mean_r86': round(t76v, 3),",
     "timing_reads[label] = {'timing_mean_r88': round(t77, 3), 'timing_mean_r87': round(t76v, 3),", 1, "s9-reads"),
    ("print(f'{label}: timing mean R87 {t77:.3f} vs R86 {t76v:.3f} | delta {t77 - t76v:+.3f}')",
     "print(f'{label}: timing mean R88 {t77:.3f} vs R87 {t76v:.3f} | delta {t77 - t76v:+.3f}')", 1, "s9-fstring"),
    ("'bazi_timing_side_read_vs_r86': timing_reads",
     "'bazi_timing_side_read_vs_r87': timing_reads", 1, "s9-outkey"),
    ("host_expected = {'changed_main': 26, 'reserve_used': 46, 'disputed': 55}  # host freeze verify recount (verify_predictions_host_r87.py, FREEZE-r87); filled by R87 host after freeze verify, before the definitive analyze run",
     "host_expected = None  # host fills after R88 freeze verify (verify_predictions_host_r88.py, FREEZE-r88), before the definitive analyze run", 1, "host-expected"),
    ("'note': ('Footprint side read only; R87 is the third platform point of the post-R84 new series (snapshot byte-identical to the R86 snapshot: s.11 archived form and the completed ziwei chapter); no intervention judgment is pending on the platform side and this dev read carries no judgment; footprint is a side read only and carries no verdict; the mengzhan chapter effectiveness test still awaits fresh dream cases at acceptance.')",
     "'note': ('Footprint side read only; R88 is the first platform point of the post-R87-REV1 series (snapshot differs from the R87 platform snapshot exactly in SKILL.md and references/calibration.md, the section-12 integration set; sections 8 and 12 are the live interventions); the R87-REV1 judgment runs on holdout31 at acceptance this round, not on the platform pool, and this dev read carries no judgment; footprint is a side read only and carries no verdict; the mengzhan chapter effectiveness test still awaits fresh dream cases at acceptance.')", 1, "s9b-note"),
    ("via R65-R85 execution", "via R65-R87 execution", 1, "docstring-via"),
    # globals after anchors
    ("'round': 87", "'round': 88", 2, "round-fields"),
    ("dev87", "dev88", 3, "lr-neg-name"),
    ("round87", "round88", 4, "round88-paths"),
    ("round86", "round87", 2, "prev-paths"),
    ("R87D", "R88D", 7, "round-dir-var"),
    ("R87 analysis (analysis role only)", "R88 analysis (analysis role only)", 1, "title"),
    ("(R87 PREREG s.1", "(R88 PREREG s.1", 3, "prereg-refs"),
    ("per R87 PREREG s.1. No method files touched", "per R88 PREREG s.1. No method files touched", 1, "docstring-per"),
    ("print('R87 single:", "print('R88 single:", 1, "single-print"),
    ("R86", "R87", 1, "prev-refs"),
    ("analysis_r87", "analysis_r88", 2, "out-analysis-key"),
    ("prev_final['analysis_r86']['appendix']['bazi_timing_side_read_vs_r85']",
     "prev_final['analysis_r87']['appendix']['bazi_timing_side_read_vs_r86']", 1, "prev-access"),
])

print("all adaptations written")
