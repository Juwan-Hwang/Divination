#!/usr/bin/env python3
"""R73 host tooling: assemble judging/FLAGS-selfreported-r73.md from the
eight judge seats' FLAGS files verbatim (registration only, no scoring),
plus the host tradition-review section from FREEZE-r73 s.2 (checker
initial flags 0 this round, keyword set carried verbatim from R72;
NO host tradition flags for adjudication).
Adjudication is the data seat's job (PREREG s.4)."""
from pathlib import Path

JD = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round73/judging")
SEATS = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3", "Y4"]

parts = ["# FLAGS-selfreported-r73（主持汇编，八席自报旗标原文合并＋主持 tradition 复核节，只登记不改分；定案由本轮数据席执行）\n"]
for s in SEATS:
    text = (JD / f"FLAGS-{s}.md").read_text(encoding="utf-8")
    parts.append(f"\n===== FLAGS-{s} =====\n" + text.rstrip("\n") + "\n")

parts.append("""
===== 主持复核节（tradition 复核，FREEZE-r73 §二）=====
- 本轮主持 tradition 复核**无旗标交定案**：check_tradition_host_r73.py（未标注关键词集逐字承 R72 简繁集＋英文变体集、大小写不敏感）初检 flags **0** 件——direct 365／none-labelled 122 与 R72 初检分布全等（只登记），措辞不实型旗标连续第三轮归零；声明组数加扫多组文件 0、冲突 0（FREEZE-r73 §二全账）。故本轮定案范围仅为八席自报旗标。
""")

out = JD / "FLAGS-selfreported-r73.md"
out.write_text("".join(parts), encoding="utf-8")
print("written", out, out.stat().st_size, "bytes")
