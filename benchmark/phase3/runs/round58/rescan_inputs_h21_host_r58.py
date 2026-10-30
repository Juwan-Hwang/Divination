#!/usr/bin/env python3
"""R58 host seal-verification re-scan (scan 3) for holdout21: independent
fragment-level scan of gold master_prediction + outcome against all input
card texts, plus content-marker scan (markers per R42 PREREG s.5 via
build_holdout20_r56.py) and a targeted check on the QM-004 host rewrite.
"""
import json
import os
import re

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
IN_DIR = os.path.join(BASE, "holdout21", "inputs")
GOLD = os.path.join(BASE, "holdout21", "test_gold.jsonl")

LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']


def card_text(obj):
    parts = []

    def walk(o):
        if isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
        elif isinstance(o, str):
            parts.append(o)

    walk(obj)
    return "\n".join(parts)


def fragments(text):
    frags = set()
    for sent in re.split(r'[。！？；\n]', text):
        s = sent.strip()
        if len(s) >= 8:
            frags.add(s)
        for i in range(max(0, len(s) - 11)):
            frags.add(s[i:i + 12])
    return frags


cards = {}
for f in sorted(os.listdir(IN_DIR)):
    if f.endswith(".json"):
        cards[f[:-5]] = card_text(json.load(open(os.path.join(IN_DIR, f), encoding="utf-8")))
assert len(cards) == 25, len(cards)

gold = [json.loads(l) for l in open(GOLD, encoding="utf-8") if l.strip()]
assert len(gold) == 25, len(gold)
assert {g["id"] for g in gold} == set(cards)

frag_hits = []
for g in gold:
    src = (g.get("master_prediction") or "") + "\n" + (g.get("outcome") or "")
    for frag in fragments(src):
        for cid, txt in cards.items():
            if frag in txt:
                frag_hits.append((g["id"], cid, frag[:24]))
print("fragment hits:", len(frag_hits))
for h in frag_hits[:20]:
    print("  ", h)

marker_hits = []
for cid, txt in cards.items():
    for lvl, markers in (("L1", LEVEL1), ("L2", LEVEL2)):
        for m in markers:
            if m in txt:
                marker_hits.append((cid, lvl, m))
print("marker hits:", marker_hits)

qm4 = cards["QM-004"]
for probe in ["申时来电", "申时复电", "巳时停电"]:
    print(f"QM-004 probe {probe}:", probe in qm4)
print("scan3 done")
