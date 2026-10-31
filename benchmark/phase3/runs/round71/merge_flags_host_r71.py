#!/usr/bin/env python3
"""R71 host tooling: assemble judging/FLAGS-selfreported-r71.md from the
eight judge seats' FLAGS files verbatim (registration only, no scoring),
plus the host tradition-review section from FREEZE-r70 s.2 (33 checker
keyword-variant false positives, host-ruled not established; this round
has NO host tradition flags for adjudication). Adjudication is the data
seat's job (PREREG s.4)."""
from pathlib import Path

JD = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round71/judging")
SEATS = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3", "Y4"]

parts = ["# FLAGS-selfreported-r71（主持汇编，八席自报旗标原文合并＋主持 tradition 复核节，只登记不改分；定案由本轮数据席执行）\n"]
for s in SEATS:
    text = (JD / f"FLAGS-{s}.md").read_text(encoding="utf-8")
    parts.append(f"\n===== FLAGS-{s} =====\n" + text.rstrip("\n") + "\n")

parts.append("""
===== 主持复核节（tradition 复核，FREEZE-r71 §二）=====
- 本轮主持 tradition 复核**无旗标交定案**：check_tradition_host_r71.py（未标注关键词集本轮已补繁体变体）初检 flags 7 件经主持逐件核实，全为 WP-001–WP-007 basis 首行英文「Card bears no tradition field; decided by genre: …」未命中检查器中英关键词集的变体误报（卡面确无 tradition/system 字段、首行如实写无字段、无虚称、无值误标），主持裁定不成立、不重测、不交定案，只登记（FREEZE-r71 §二全账）。R70 型繁体变体误报本轮归零；措辞不实型旗标归零；声明组数加扫多组文件 0、冲突 0。
- 注：评审席 X1／Y1 旗标中另有涉 basis 首行 tradition 措辞的观察条目，与上 7 件不同源（属评审席对具体例的定案材料），由数据席经 host-mapping 对位回原卡逐件定案。
""")

out = JD / "FLAGS-selfreported-r71.md"
out.write_text("".join(parts), encoding="utf-8")
print("written", out, out.stat().st_size, "bytes")
