#!/usr/bin/env python3
"""R70 host tooling: assemble judging/FLAGS-selfreported-r70.md from the
eight judge seats' FLAGS files verbatim (registration only, no scoring),
plus the host tradition-review section from FREEZE-r70 s.2 (33 checker
keyword-variant false positives, host-ruled not established; this round
has NO host tradition flags for adjudication). Adjudication is the data
seat's job (PREREG s.4)."""
from pathlib import Path

JD = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round70/judging")
SEATS = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3", "Y4"]

parts = ["# FLAGS-selfreported-r70（主持汇编，八席自报旗标原文合并＋主持 tradition 复核节，只登记不改分；定案由本轮数据席执行）\n"]
for s in SEATS:
    text = (JD / f"FLAGS-{s}.md").read_text(encoding="utf-8")
    parts.append(f"\n===== FLAGS-{s} =====\n" + text.rstrip("\n") + "\n")

parts.append("""
===== 主持复核节（tradition 复核，FREEZE-r70 §二）=====
- 本轮主持 tradition 复核**无旗标交定案**：check_tradition_host_r70.py 初检 flags 33 件经主持逐件核实，全为 S2 批 basis 首行繁体「未標註」字面未命中检查器简体关键词集的变体误报（卡面确无 tradition/system 字段、首行如实写未标注、无虚称、无值误标），主持裁定不成立、不重测、不交定案，只登记（FREEZE-r70 §二全账）。R70 强化措辞注记本轮生效、措辞不实型旗标归零；声明组数加扫多组文件 0、冲突 0。
- 注：评审席 X2 旗标中另有两件 anon（P3-6feecf6a／P3-74952e1f）涉 basis 首行「與卡面一致」措辞观察，与上 33 件不同源，由数据席经 host-mapping 对位回原卡逐件定案。
""")

out = JD / "FLAGS-selfreported-r70.md"
out.write_text("".join(parts), encoding="utf-8")
print("written", out, out.stat().st_size, "bytes")
