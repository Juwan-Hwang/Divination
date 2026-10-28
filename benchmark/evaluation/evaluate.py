#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MastersDivination Benchmark 评测脚本（离线，无第三方依赖）

输入：
  --gold   金标 JSONL（masters-dataset 的 dev.jsonl 或开封后的 test_gold.jsonl）
  --pred   预测 JSONL，每行：
           {"id": "...", "direction": "positive|negative|mixed|neutral",
            "assertions": "自由文本断语（供评审）",
            "assertion_score": 0-2（可选，评审按 PROTOCOL 量表判定后回填）,
            "outcome_score":   0-2（可选，同上）,
            "method": "可选，作答所用体系——仅用于跨体系收敛统计，不计分"}
输出（stdout + 可选 --out 报告文件）：
  方向一致率（自动比对 direction）、关键断语对齐率、应验对齐率（评审分聚合）、
  按体系与按大师分项、总分（PROTOCOL 口径：每例三项合计 >=4 为通过）。
判定规则成文于 ../PROTOCOL.md；本脚本不代替评审判定断语/应验两项。
"""
import argparse, json, sys
from collections import defaultdict

def load_jsonl(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gold", required=True)
    ap.add_argument("--pred", required=True)
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    gold = {c["id"]: c for c in load_jsonl(args.gold)}
    preds = {p["id"]: p for p in load_jsonl(args.pred)}
    missing = [i for i in gold if i not in preds]

    per_case = []
    by_trad, by_master = defaultdict(list), defaultdict(list)
    n_dir_ok = 0; sum_assert = 0.0; sum_outcome = 0.0; judged = 0; passed = 0; convergent = 0
    for cid, case in gold.items():
        mp = case["master_predictions"][0]
        trad, master = mp["tradition"], mp["master"]
        p = preds.get(cid)
        if p is None:
            per_case.append((cid, trad, master, None, None, None, False, False))
            by_trad[trad].append(0); by_master[master].append(0)
            continue
        dir_ok = (p.get("direction") == mp["direction"])
        n_dir_ok += 1 if dir_ok else 0
        a_s = p.get("assertion_score"); o_s = p.get("outcome_score")
        conv = bool(p.get("method")) and p["method"] != trad and dir_ok
        convergent += 1 if conv else 0
        if a_s is not None and o_s is not None:
            judged += 1; sum_assert += a_s; sum_outcome += o_s
            total = (2 if dir_ok else 0) + a_s + o_s
            ok = total >= 4
            passed += 1 if ok else 0
        else:
            total, ok = None, False
        per_case.append((cid, trad, master, dir_ok, a_s, o_s, ok, conv))
        score01 = (1 if dir_ok else 0) + ((a_s or 0) + (o_s or 0)) / 4 if a_s is not None else (1 if dir_ok else 0)
        by_trad[trad].append(score01); by_master[master].append(score01)

    n = len(gold)
    lines = []
    lines.append("MastersDivination Benchmark — Evaluation Report")
    lines.append(f"gold={args.gold}  pred={args.pred}")
    lines.append(f"cases={n}  answered={n-len(missing)}  missing={missing if missing else '[]'}")
    lines.append(f"方向一致率 direction accuracy: {n_dir_ok}/{n} = {n_dir_ok/max(n,1):.3f}")
    if judged:
        lines.append(f"关键断语对齐 assertion alignment (judged {judged}): {sum_assert/(2*judged):.3f}")
        lines.append(f"应验对齐 outcome alignment (judged {judged}): {sum_outcome/(2*judged):.3f}")
        lines.append(f"通过率 pass (total>=4, judged only): {passed}/{judged} = {passed/judged:.3f}")
    else:
        lines.append("关键断语/应验两项尚无评审分（assertion_score/outcome_score 未回填），只报方向一致率。")
    lines.append(f"跨体系收敛 cross-system convergence: {convergent} 例")
    lines.append("-- per case --")
    for cid, trad, master, d, a, o, ok, conv in per_case:
        lines.append(f"{cid} [{trad} / {master}] direction={'OK' if d else ('MISS' if d is not None else 'NO-PRED')} assertion={a} outcome={o} pass={ok} convergent={conv}")
    lines.append("-- by tradition (mean case score, direction=1pt + judged halves) --")
    for k, v in sorted(by_trad.items()):
        lines.append(f"{k}: {sum(v)/len(v):.3f} (n={len(v)})")
    lines.append("-- by master --")
    for k, v in sorted(by_master.items()):
        lines.append(f"{k}: {sum(v)/len(v):.3f} (n={len(v)})")
    report = "\n".join(lines)
    print(report)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report + "\n")

if __name__ == "__main__":
    main()
