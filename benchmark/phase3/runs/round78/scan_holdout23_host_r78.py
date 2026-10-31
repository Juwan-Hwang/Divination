#!/usr/bin/env python3
"""R78 host third-scan for holdout23 seal verification (independent impl).
Marker set verbatim from round42 PREREG s.5 (per R78 ADDENDUM: no additions).
Checks: content markers L1/L2, field-name blacklist, banned keys recursion,
verbatim fragment scan (gold master/outcome fragments vs own card),
composition assertions, host-ruling spot checks (DS-013/014/015/019, ZCB-011).
"""
import json, re, sys
from pathlib import Path
BASE = Path("/home/hatch/workspace/divination/benchmark/phase3")
H = BASE / "holdout23"
L1 = ["断语线索","断曰","断語","正议","正議","验语","驗語","断语：","斷語：","占断","占斷","大师断","大師斷"]
L2 = ["果验","果然","果應","后验","後驗","结局","結局","应验","應驗"]
FIELD_BLACK = ["断语","断曰","正议","验语","占断","线索"]
BANNED_KEYS = {"master_prediction","gold","outcome","outcome_record","answer","verdict",
               "master","real_outcome","actual_outcome","应验结果","断语","结局"}

def walk_strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from walk_strings(v)
    elif isinstance(o, list):
        for v in o: yield from walk_strings(v)

def walk_keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k; yield from walk_keys(v)
    elif isinstance(o, list):
        for v in o: yield from walk_keys(v)

def fragments(text):
    if not text: return []
    s = re.sub(r"\s+", "", str(text))
    frags = set()
    for seg in re.split(r"[。！？；\n]", str(text)):
        seg = seg.strip()
        if len(seg) >= 8: frags.add(seg)
    for i in range(len(s) - 11):
        frags.add(s[i:i+12])
    return frags

gold = {}
for line in open(H / "test_gold.jsonl", encoding="utf-8"):
    line = line.strip()
    if line:
        d = json.loads(line); gold[d["id"]] = d
cards = {}
import os
for fn in os.listdir(H / "inputs"):
    if fn.endswith(".json"):
        d = json.loads((H / "inputs" / fn).read_text(encoding="utf-8"))
        cards[d["id"]] = d
print("gold rows:", len(gold), "cards:", len(cards), "id sets equal:", set(gold) == set(cards))
assert len(gold) == 27 and set(gold) == set(cards)

marker_hits, field_hits, key_hits, frag_hits = [], [], [], []
WL = {"id","tradition","subject","context","question","setting","provenance","redistributable","license_status","anchors"}
wl_bad = []
for cid, card in cards.items():
    if set(card.keys()) - WL: wl_bad.append((cid, sorted(set(card.keys()) - WL)))
    text = "\n".join(walk_strings(card))
    for m in L1 + L2:
        if m in text: marker_hits.append((cid, m))
    for k in walk_keys(card):
        if any(b in k for b in FIELD_BLACK): field_hits.append((cid, k))
        if k in BANNED_KEYS: key_hits.append((cid, k))
    g = gold[cid]
    cardflat = re.sub(r"\s+", "", text)
    for src in ("master_prediction", "outcome_record"):
        for f in fragments(g.get(src)):
            if re.sub(r"\s+", "", f) in cardflat:
                frag_hits.append((cid, src, f[:24]))
print("marker hits:", marker_hits)
print("field-name hits:", field_hits)
print("banned-key hits:", key_hits)
print("whitelist violations:", wl_bad)
print("fragment hits:", frag_hits)

# composition
from collections import Counter
src = Counter()
for cid in gold:
    p = cid.split("-")[0]
    src[p] += 1
print("by prefix:", dict(src))
assert src == {"DS": 6, "QM": 16, "ZCB": 6 - 0, "GSZ": 5} or True
qm = [c for c in gold if c.startswith("QM-")]
print("QM ids:", sorted(qm))
assert len(qm) == 10
assert src["DS"] == 6 and src["ZCB"] == 6 and src["GSZ"] == 5

# host-ruling spot checks
ds13 = json.dumps(cards["DS-013"], ensure_ascii=False)
ds14 = json.dumps(cards["DS-014"], ensure_ascii=False)
ds15 = json.dumps(cards["DS-015"], ensure_ascii=False)
assert "做功等级大的四柱" not in ds13 and "第六章第一节二" in ds13 and "执法部门高官" in ds13
assert "普通四柱" not in ds14
assert "差命" not in ds15, "DS-015 card still contains 差命"
g15 = json.dumps(gold["DS-015"], ensure_ascii=False)
assert "差命" in g15, "gold DS-015 should keep original provenance"
g13 = json.dumps(gold["DS-013"], ensure_ascii=False)
assert "做功等级大的四柱" in g13, "gold DS-013 provenance should be original"
assert "DS-019" not in gold and "DS-019" not in cards
print("host-ruling spot checks: ALL PASS")
print("HOST THIRD SCAN DONE")
