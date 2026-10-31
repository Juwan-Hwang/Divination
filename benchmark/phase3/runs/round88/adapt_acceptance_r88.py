#!/usr/bin/env python3
"""R88 acceptance tooling adapter: derive the holdout31 acceptance
packet builder and analyzer from the round87 holdout30 originals by
POINT replacements only, each with an asserted hit count.
"""
from pathlib import Path

SRC = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round87/acceptance")
DST = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round88/acceptance")

OLD_IDS = '''CASE_IDS = [
    "DA-038", "DA-041", "DA-042", "DA-044", "DA-046",
    "CYJ-006", "CYJ-007", "CYJ-008", "CYJ-009", "CYJ-010",
    "BY-017", "BY-018", "BY-020", "BY-021",
    "WHY-025", "WHY-026", "WHY-027", "WHY-028", "WHY-031",
    "WHY-032", "WHY-033", "WHY-034", "WHY-035", "WHY-036",
    "GSZ-101", "GSZ-103", "GSZ-104", "GSZ-105",
]'''
NEW_IDS = '''CASE_IDS = [
    "DA-047", "DA-048", "DA-050", "DA-051", "DA-054", "DA-055", "DA-057",
    "BY-022", "BY-023", "BY-024", "BY-025", "BY-027", "BY-028", "BY-030",
    "WHY-037", "WHY-038", "WHY-039", "WHY-040", "WHY-041",
    "WHY-042", "WHY-043", "WHY-044", "WHY-068", "WHY-069",
    "GSZ-107", "GSZ-108", "GSZ-109", "GSZ-110",
]'''


def rep(t, old, new, expected, tag):
    c = t.count(old)
    assert c == expected, f"{tag}: {old!r} hits {c}, expected {expected}"
    return t.replace(old, new)


def adapt(src_name, dst_name, steps):
    t = (SRC / src_name).read_text(encoding="utf-8")
    for old, new, n, tag in steps:
        t = rep(t, old, new, n, f"{dst_name}:{tag}")
    (DST / dst_name).write_text(t, encoding="utf-8")
    print("written", dst_name)


adapt("build_acceptance_packets_h30_r87.py", "build_acceptance_packets_h31_r88.py", [
    ("holdout30 acceptance packet builder (R87)", "holdout31 acceptance packet builder (R88)", 1, "title"),
    ("Gold is OPENED only when the platform fully stands (R87 platform\nall-stand; data/holdout30-seal-log.md opening section). This script is run by the\nhost only after the opening is declared; see\nruns/round87/acceptance/OPENING.md.",
     "Gold is OPENED only when the platform fully stands (R88 platform\nall-stand; data/holdout31-seal-log.md opening section). This script is run by the\nhost only after the opening is declared; see\nruns/round88/acceptance/OPENING.md.", 1, "doc-opening"),
    ("Case id set is the holdout30 acceptance composition written into",
     "Case id set is the holdout31 acceptance composition written into", 1, "doc-caseids"),
    ("Anon ids: H30O-/H30M-<8 hex>,\nrandom.Random(20261102), sorted case order, redraw on collision.",
     "Anon ids: H31O-/H31M-<8 hex>,\nrandom.Random(20261104), sorted case order, redraw on collision.", 1, "doc-anon"),
    ("Outcome/master texts come ONLY from holdout30/test_gold.jsonl itself.",
     "Outcome/master texts come ONLY from holdout31/test_gold.jsonl itself.", 1, "doc-source"),
    ('GOLD = P3 / "holdout30" / "test_gold.jsonl"', 'GOLD = P3 / "holdout31" / "test_gold.jsonl"', 1, "gold-path"),
    ('GOLD_SHA256 = "09e38d9a5f87d1f81b959094035ff266428ca960c96d4fdc1a082643232adcdc"',
     'GOLD_SHA256 = "4b4312147f6657b66fc21fe56207f7ba76857fdd7340ab0a5c5e6728a9210e9d"', 1, "gold-sha"),
    (OLD_IDS, NEW_IDS, 1, "case-ids"),
    ("SEED = 20261102", "SEED = 20261104", 1, "seed"),
    ('new_anon("H30O")', 'new_anon("H31O")', 1, "prefix-ours"),
    ('new_anon("H30M")', 'new_anon("H31M")', 1, "prefix-master"),
    ('f"anon seed: {SEED}; H30O- ours, H30M- master; random.Random(SEED), "',
     'f"anon seed: {SEED}; H31O- ours, H31M- master; random.Random(SEED), "', 1, "seed-file"),
])

adapt("analyze_acceptance_h30_r87.py", "analyze_acceptance_h31_r88.py", [
    ("""holdout30 acceptance analysis (analysis role only). Adapted from the
holdout29 analyzer (analyze_acceptance_h29_r86.py) for R87 opening
(seal log data/holdout30-seal-log.md opening section).

Calibers: the set is all-low (28/28, gold field
`pollution`, seal log data/holdout30-seal-log.md) and has NO known
pollution-caliber conflict case, so MAIN caliber == sealed caliber ==
all 28 cases. The three criteria are judged on this single caliber.""",
     """holdout31 acceptance analysis (analysis role only). Adapted from the
holdout30 analyzer (analyze_acceptance_h30_r87.py) for R88 opening
(seal log data/holdout31-seal-log.md opening section).

Calibers: the set is all-low (28/28, gold field
`pollution`, seal log data/holdout31-seal-log.md) and has NO known
pollution-caliber conflict case, so MAIN caliber == sealed caliber ==
all 28 cases. The three criteria are judged on this single caliber.""", 1, "doc-head"),
    ("CZ-QX: this set has NO cezi cases (composition liuren/ziwei/bazi);\nthe CZ-QX same-tier count stays 16 (settled at R76). Registered only.",
     "CZ-QX: this set has NO cezi cases (composition liuren/liuyao);\nthe CZ-QX same-tier count stays 16 (settled at R76). Registered only.", 1, "doc-czqx"),
    ("""Segment attached reads: liuren (14) and liuyao (14) segment pair
diffs are reported in the segments block as diagnostic attached reads
only and do not modify the three criteria. No qimen cases in this
set, so no direction attached read applies. The CYJ subset (5) sits
inside liuren with its seal-logged fidelity-degraded form; its read
is reported within the liuren_CYJ segment as-is.

Outputs: judging/final-scores-h30.json + stdout.""",
     """Segment attached reads: liuren (14) and liuyao (14) segment pair
diffs are reported in the segments block as diagnostic attached reads
only and do not modify the three criteria. No qimen cases in this
set, so no direction attached read applies. This set has NO CYJ
cases (CYJ regular eligible is 0 under the R87 tightened anchor
ruling); the liuren segment is DA 7 + BY 7 and the liuren_CYJ group
is empty (skipped by the segments builder).

Outputs: judging/final-scores-h31.json + stdout.""", 1, "doc-segments"),
    ('GOLD = ACC.parents[2] / "holdout30" / "test_gold.jsonl"',
     'GOLD = ACC.parents[2] / "holdout31" / "test_gold.jsonl"', 1, "gold-path"),
    ("MID_OVERRIDE = {}  # no conflict case in holdout30 (seal log opening section)",
     "MID_OVERRIDE = {}  # no conflict case in holdout31 (seal log opening section)", 1, "mid-override"),
    ('"gold_file": "benchmark/phase3/holdout30/test_gold.jsonl"',
     '"gold_file": "benchmark/phase3/holdout31/test_gold.jsonl"', 1, "low-info"),
    ('assert len(groups["liuren_DA"]) == 5, len(groups["liuren_DA"])',
     'assert len(groups["liuren_DA"]) == 7, len(groups["liuren_DA"])', 1, "seg-da"),
    ('assert len(groups["liuren_CYJ"]) == 5, len(groups["liuren_CYJ"])',
     'assert len(groups["liuren_CYJ"]) == 0, len(groups["liuren_CYJ"])', 1, "seg-cyj"),
    ('assert len(groups["liuren_BY"]) == 4, len(groups["liuren_BY"])',
     'assert len(groups["liuren_BY"]) == 7, len(groups["liuren_BY"])', 1, "seg-by"),
    ('"caliber": "not applicable: holdout30 contains no qimen cases"',
     '"caliber": "not applicable: holdout31 contains no qimen cases"', 1, "qimen-note"),
    ('"note": "holdout30 contains no cezi cases (composition liuren/liuyao); CZ-QX same-tier count stays 16 (settled at R76)."',
     '"note": "holdout31 contains no cezi cases (composition liuren/liuyao); CZ-QX same-tier count stays 16 (settled at R76)."', 1, "czqx-note"),
    ('open(JD / "final-scores-h30.json", "w", encoding="utf-8")',
     'open(JD / "final-scores-h31.json", "w", encoding="utf-8")', 1, "out-name"),
])

print("acceptance adaptations written")
