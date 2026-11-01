from pathlib import Path
P3 = Path('/home/hatch/workspace/divination/benchmark/phase3')
t = (P3/'runs/round93/analyze_r93.py').read_text(encoding='utf-8')

def rep(a, b, n):
    global t
    c = t.count(a)
    assert c == n, (a, c, n)
    t = t.replace(a, b)

def rep_all(a, b):
    global t
    c = t.count(a)
    t = t.replace(a, b)
    print(f'{a!r} -> {b!r}: {c} hits')
    return c

rep("host_expected = {'changed_main': 15, 'reserve_used': 41, 'disputed': 59}  # host freeze verify recount (verify_predictions_host_r93.py, FREEZE-r93)",
    "host_expected = None  # host fills after R94 freeze verify (verify_predictions_host_r94.py, FREEZE-r94)", 1)
rep("prev_final['analysis_r92']['appendix']['bazi_timing_side_read_vs_r91']",
    "prev_final['analysis_r93']['appendix']['bazi_timing_side_read_vs_r92']", 1)
rep("'timing_mean_r93': round(t77, 3), 'timing_mean_r92': round(t76v, 3)",
    "'timing_mean_r94': round(t77, 3), 'timing_mean_r93': round(t76v, 3)", 1)
rep("prev_timing[label]['timing_mean_r92']", "prev_timing[label]['timing_mean_r93']", 1)
rep("timing mean R93 {t77:.3f} vs R92 {t76v:.3f}", "timing mean R94 {t77:.3f} vs R93 {t76v:.3f}", 1)
rep("bazi timing movement R92 -> R93", "bazi timing movement R93 -> R94", 1)
rep("'bazi_timing_side_read_vs_r92': timing_reads", "'bazi_timing_side_read_vs_r93': timing_reads", 1)
rep("R93 is the fifth platform point of the post-disposal new series (snapshot byte-identical to the R92 platform snapshot, verified at R93 opening;",
    "R94 is the sixth platform point of the post-disposal new series (snapshot byte-identical to the R93 platform snapshot, verified at R94 opening;", 1)
rep("via R65-R92 execution", "via R65-R93 execution", 1)
rep("R92 baseline taken from runs/round92/final-scores.json side-read\nvalues; no other-round judging/predictions opened), overlay-16 mean",
    "R93 baseline taken from runs/round93/final-scores.json side-read\nvalues; no other-round judging/predictions opened), overlay-16 mean", 1)
rep("PREV_FINAL = P3 / 'runs/round92/final-scores.json'", "PREV_FINAL = P3 / 'runs/round93/final-scores.json'", 1)
rep("'round': 93", "'round': 94", 2)
rep("'analysis_r93': analysis", "'analysis_r94': analysis", 1)
rep_all('R91D', 'R94D')
rep_all('round93', 'round94')
rep_all('R93', 'R94')
rep_all('dev93', 'dev94')
rep_all('c_single_r93', 'c_single_r94')
(P3/'runs/round94/analyze_r94.py').write_text(t, encoding='utf-8')
print('written analyze_r94.py')
