#!/usr/bin/env python3
"""R94 host tooling: section-8 execution monitoring counts (FREEZE-r94 s.3).

Caliber verbatim from FREEZE-r92 s.3: grouping by host-meta tradition
(round92 judging/host-meta.json, same source as analyze); markers:
- jieming: basis contains '第八节'
- r80: basis contains 'R80'
- fullname: basis contains '做功主线与功量核算核'
- biaomu: basis contains '功量核'
- mainline: regex 主线认定|主线…(居首|受压|为主)
Groups: liuyao {liuyao, 六爻}, liuren {liuren, 六壬}, rest.
Monitoring only; no verdict.
"""
import json
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
R94 = P3 / "runs/round94"
META = json.loads((P3 / "runs/round92/judging/host-meta.json").read_text(encoding="utf-8"))

MAINLINE = re.compile(r"主线认定|主线[^。\n]{0,12}(居首|受压|为主)")

GROUPS = {"六爻": {"liuyao", "六爻"}, "六壬": {"liuren", "六壬"}}


def group_of(cid):
    t = META[cid].get("tradition")
    for g, vals in GROUPS.items():
        if t in vals:
            return g
    return "其余"


def main():
    stats = {}
    for cid, meta in META.items():
        pred = json.loads((R94 / "predictions" / f"{cid}.json").read_text(encoding="utf-8"))
        basis = pred.get("basis", "")
        g = group_of(cid)
        s = stats.setdefault(g, {"n": 0, "jieming": 0, "r80": 0, "fullname": 0, "biaomu": 0, "mainline": 0})
        s["n"] += 1
        if "第八节" in basis:
            s["jieming"] += 1
        if "R80" in basis:
            s["r80"] += 1
        if "做功主线与功量核算核" in basis:
            s["fullname"] += 1
        if "功量核" in basis:
            s["biaomu"] += 1
        if MAINLINE.search(basis):
            s["mainline"] += 1
    total = {"n": 0, "jieming": 0, "r80": 0, "fullname": 0, "biaomu": 0, "mainline": 0}
    for g in ("六爻", "六壬", "其余"):
        s = stats[g]
        for k in total:
            total[k] += s[k]
        print(g, s)
    print("全集", total)
    assert total["n"] == 487


if __name__ == "__main__":
    main()
