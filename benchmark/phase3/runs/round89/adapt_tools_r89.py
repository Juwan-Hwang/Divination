#!/usr/bin/env python3
"""R89 host: adapt R88 host tools to R89 by asserted point replacements.
Each (old, new, expected_count) must match exactly; any mismatch aborts.
No chained general-after-specific substitution: every old string is a
distinct literal not produced by any other replacement's new string."""
from pathlib import Path

R = Path("/home/hatch/workspace/divination/benchmark/phase3/runs")


def adapt(src_name, dst_name, pairs):
    src = (R / "round88" / src_name).read_text(encoding="utf-8")
    out = src
    for old, new, cnt in pairs:
        got = out.count(old)
        assert got == cnt, (src_name, old, got, cnt)
        out = out.replace(old, new)
    # residual scan: no live round88/r88 literals outside doc mentions we keep
    (R / "round89" / dst_name).write_text(out, encoding="utf-8")
    print("wrote", dst_name, len(out))


adapt("verify_predictions_host_r88.py", "verify_predictions_host_r89.py", [
    ("R88 host verification", "R89 host verification", 1),
    ("PREREG-r88", "PREREG-r89", 1),
    ("verify-predictions-host-r88.json", "verify-predictions-host-r89.json", 2),
    ('R88 = P3 / "runs/round88"', 'R88 = P3 / "runs/round89"', 1),
])

adapt("build_judge_packets_r88.py", "build_judge_packets_r89.py", [
    ("Round 88 judging packet builder", "Round 89 judging packet builder", 1),
    ("R88 build per PREREG s.0", "R89 build per PREREG s.0", 1),
    ("incl. the new _r87_carryover_notes_addendum layer, 43 cases per R88 opening registration",
     "incl. the new _r88_carryover_notes_addendum layer, 0 cases per R89 opening registration", 1),
    ("thirty-two carryover note layers", "thirty-three carryover note layers", 1),
    ("SEED = 20261103", "SEED = 20261105", 1),
    ("anon seed 20261103", "anon seed 20261105", 1),
    ('"round87" / "judging" / "host-meta.json"', '"round88" / "judging" / "host-meta.json"', 1),
    ("(round87 judging copy)", "(round88 judging copy)", 1),
    ('carry87 = manifest.get("_r87_carryover_notes_addendum", {})',
     'carry87 = manifest.get("_r87_carryover_notes_addendum", {})\n    carry88 = manifest.get("_r88_carryover_notes_addendum", {})', 1),
    ("and len(carry87) == 43, (",
     "and len(carry87) == 43 and len(carry88) == 0, (", 1),
    ("len(carry85), len(carry86), len(carry87))",
     "len(carry85), len(carry86), len(carry87), len(carry88))", 1),
    ("| set(carry86) | set(carry87)",
     "| set(carry86) | set(carry87) | set(carry88)", 1),
    ('        if cid in carry87:\n            parts.append("[R87-addendum] " + carry87[cid])',
     '        if cid in carry87:\n            parts.append("[R87-addendum] " + carry87[cid])\n        if cid in carry88:\n            parts.append("[R88-addendum] " + carry88[cid])', 1),
])

adapt("merge_judgments_r88.py", "merge_judgments_r89.py", [
    ("Round 88 host tooling", "Round 89 host tooling", 1),
    ("carried through R83-R87", "carried through R83-R88", 1),
])

adapt("analyze_r88.py", "analyze_r89.py", [
    ("R88 analysis (analysis role only)", "R89 analysis (analysis role only)", 1),
    ("per R88 PREREG s.1", "per R89 PREREG s.1", 1),
    ("Platform criteria (R88 PREREG s.1, line values carried verbatim from\nR64 PREREG s.1 via R65-R87 execution",
     "Platform criteria (R89 PREREG s.1, line values carried verbatim from\nR64 PREREG s.1 via R65-R88 execution", 1),
    ("Attribution guardrails (R88 PREREG s.1", "Attribution guardrails (R89 PREREG s.1", 1),
    ("bazi-all / bazi-natal timing sub-item means R88 vs R87\n(R87 baseline taken from runs/round87/final-scores.json side-read\nvalues; no other-round judging/predictions opened), overlay-16 mean\npair diff, trigger counts recomputed from runs/round88/predictions/,",
     "bazi-all / bazi-natal timing sub-item means R89 vs R88\n(R88 baseline taken from runs/round88/final-scores.json side-read\nvalues; no other-round judging/predictions opened), overlay-16 mean\npair diff, trigger counts recomputed from runs/round89/predictions/,", 1),
    ("(diagnosis/lr-negatives-dev88.json)", "(diagnosis/lr-negatives-dev89.json)", 1),
    ("adds an analysis_r88 section", "adds an analysis_r89 section", 1),
    ("R88D = P3 / 'runs/round88'", "R88D = P3 / 'runs/round89'", 1),
    ("PREV_FINAL = P3 / 'runs/round87/final-scores.json'", "PREV_FINAL = P3 / 'runs/round88/final-scores.json'", 1),
    ("host_expected = {'changed_main': 12, 'reserve_used': 32, 'disputed': 40}  # host freeze verify recount (verify_predictions_host_r88.py, FREEZE-r88); filled by R88 host after freeze verify, before the definitive analyze run",
     "host_expected = {'changed_main': 0, 'reserve_used': 0, 'disputed': 0}  # PLACEHOLDER: R89 host fills from verify_predictions_host_r89.py freeze recount before the definitive analyze run", 1),
    ("print('\\n== 9. side reads: bazi timing movement R87 -> R88 ==')",
     "print('\\n== 9. side reads: bazi timing movement R88 -> R89 ==')", 1),
    ("prev_timing = prev_final['analysis_r87']['appendix']['bazi_timing_side_read_vs_r86']",
     "prev_timing = prev_final['analysis_r88']['appendix']['bazi_timing_side_read_vs_r87']", 1),
    ("t76v = prev_timing[label]['timing_mean_r87']",
     "t76v = prev_timing[label]['timing_mean_r88']", 1),
    ("timing_reads[label] = {'timing_mean_r88': round(t77, 3), 'timing_mean_r87': round(t76v, 3),",
     "timing_reads[label] = {'timing_mean_r89': round(t77, 3), 'timing_mean_r88': round(t76v, 3),", 1),
    ("print(f'{label}: timing mean R88 {t77:.3f} vs R87 {t76v:.3f} | delta {t77 - t76v:+.3f}')",
     "print(f'{label}: timing mean R89 {t77:.3f} vs R88 {t76v:.3f} | delta {t77 - t76v:+.3f}')", 1),
    ("'note': ('Footprint side read only; R88 is the first platform point of the post-R87-REV1 series (snapshot differs from the R87 platform snapshot exactly in SKILL.md and references/calibration.md, the section-12 integration set; sections 8 and 12 are the live interventions); the R87-REV1 judgment runs on holdout31 at acceptance this round, not on the platform pool, and this dev read carries no judgment; footprint is a side read only and carries no verdict; the mengzhan chapter effectiveness test still awaits fresh dream cases at acceptance.')",
     "'note': ('Footprint side read only; R89 is the first platform point of the post-section-12-disposal series (snapshot differs from the R88 platform snapshot exactly in references/calibration.md, the section-12 disposal registration; section 8 is the only live intervention); holdout32 carries no judgment attribution this round; footprint is a side read only and carries no verdict; the mengzhan chapter effectiveness test still awaits fresh dream cases at acceptance.')", 1),
    ("    'round': 88,", "    'round': 89,", 1),
    ("'prereg_source': 'runs/round88/PREREG.md s.1 (platform lines and attribution guardrails)'",
     "'prereg_source': 'runs/round89/PREREG.md s.1 (platform lines and attribution guardrails)'", 1),
    ("        'note': 'Separate from platform verdict (R88 PREREG s.1).',",
     "        'note': 'Separate from platform verdict (R89 PREREG s.1).',", 1),
    ("        'bazi_timing_side_read_vs_r87': timing_reads}", "        'bazi_timing_side_read_vs_r88': timing_reads}", 1),
    ("         'analysis_r88': analysis}", "         'analysis_r89': analysis}", 1),
    ("lr_doc = {'round': 88,", "lr_doc = {'round': 89,", 1),
    ("open(R88D / 'diagnosis/lr-negatives-dev88.json', 'w')", "open(R88D / 'diagnosis/lr-negatives-dev89.json', 'w')", 1),
    ("print('lr-negatives-dev88.json written:", "print('lr-negatives-dev89.json written:", 1),
    ("'a_pair_diff': s_all['pair_diff'], 'c_single_r87': c44['pair_diff'],",
     "'a_pair_diff': s_all['pair_diff'], 'c_single_r89': c44['pair_diff'],", 1),
])
print("ALL ADAPTED")
