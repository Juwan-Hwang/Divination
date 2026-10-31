#!/usr/bin/env python3
"""R74 host tooling: assemble judging/FLAGS-selfreported-r74.md from the
eight judge seats' FLAGS files verbatim (registration only, no scoring),
plus the host tradition-review section from FREEZE-r74 s.2 (checker
initial flags 0 this round, keyword set carried verbatim from R72;
NO host tradition flags for adjudication).
Adjudication is the data seat's job (PREREG s.4)."""
from pathlib import Path

JD = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round74/judging")
SEATS = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3", "Y4"]

parts = ["# FLAGS-selfreported-r74（主持汇编，八席自报旗标原文合并＋主持 tradition 复核节，只登记不改分；定案由本轮数据席执行）\n"]
for s in SEATS:
    text = (JD / f"FLAGS-{s}.md").read_text(encoding="utf-8")
    parts.append(f"\n===== FLAGS-{s} =====\n" + text.rstrip("\n") + "\n")

parts.append("""
===== 主持复核节（tradition 复核，FREEZE-r74 §二）=====
- 本轮主持 tradition 复核**无旗标交定案**：check_tradition_host_r74.py（未标注关键词集逐字承 R73 简繁集＋英文变体集、大小写不敏感）初检 flags **19** 件，经主持逐件回读首行＋卡面字段裁定，全为检查器关键词覆盖缺口型变体措辞（卡面实无 tradition/system 字段、首行如实声明未标注），无虚称无误标、不作废不重测（FREEZE-r74 §二全账）；实效分布 direct 365／none-labelled 122 与 R73 初检全等；声明组数加扫多组文件 0、冲突 0。故本轮定案范围仅为八席自报旗标。
""")

out = JD / "FLAGS-selfreported-r74.md"
out.write_text("".join(parts), encoding="utf-8")
print("written", out, out.stat().st_size, "bytes")
