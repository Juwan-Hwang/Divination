from pathlib import Path
P3 = Path('/home/hatch/workspace/divination/benchmark/phase3')

def adapt(src, dst, pairs):
    t = (P3/'runs/round93'/src).read_text(encoding='utf-8')
    for a, b, n in pairs:
        c = t.count(a)
        assert c == n, (src, a, c, n)
        t = t.replace(a, b)
    (P3/'runs/round94'/dst).write_text(t, encoding='utf-8')
    print('wrote', dst)

# merge: mechanism verbatim, names only
adapt('merge_judgments_r93.py', 'merge_judgments_r94.py', [
    ('Round 93 host tooling', 'Round 94 host tooling', 1),
    ('merge_judgments_r80.py', 'merge_judgments_r80.py', 1),  # provenance kept
    ('carried through R83-R90', 'carried through R83-R93', 1),
])

# packet builder: seed, meta source, docstring round refs
adapt('build_judge_packets_r93.py', 'build_judge_packets_r94.py', [
    ('Round 93 judging packet builder', 'Round 94 judging packet builder', 1),
    ('SEED = 20261113', 'SEED = 20261114', 1),
    ('anon seed 20261113', 'anon seed 20261114', 1),
    ('round92" / "judging', 'round93" / "judging', 1),
    ('(round92 judging copy)', '(round93 judging copy)', 1),
    ('the new _r92_carryover_notes_addendum layer, 12 cases per R93 opening registration',
     'the new _r93_carryover_notes_addendum layer, 5 registration items per R94 opening registration (round-level items are registration-only and are not folded into per-case packet notes; no dev case key matches them)', 1),
    ('this round\'s judging/outcome-manifest.json (R93 build per PREREG s.0: 487 cases verbatim, LR2-016 editor note split-registered, thirty-seven carryover note layers attached as separate packet fields (incl. ',
     'this round\'s judging/outcome-manifest.json (R94 build per PREREG s.0: 487 cases verbatim, LR2-016 editor note split-registered, thirty-eight carryover note layers attached as separate packet fields (incl. ', 1),
])
