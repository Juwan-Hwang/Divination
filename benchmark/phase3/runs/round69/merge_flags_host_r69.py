#!/usr/bin/env python3
"""R69 host tooling: assemble judging/FLAGS-selfreported-r69.md from the
eight judge seats' FLAGS files verbatim (registration only, no scoring),
plus the host tradition-review flag section from FREEZE-r69 s.2 (7 cases,
S3 wording falsity, host-ruled: registered, not re-tested). Adjudication
is the data seat's job (PREREG s.4)."""
from pathlib import Path

JD = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round69/judging")
SEATS = ["X1", "X2", "X3", "X4", "Y1", "Y2", "Y3", "Y4"]

parts = ["# FLAGS-selfreported-r69（主持汇编，八席自报旗标原文合并＋主持复核旗标，只登记不改分；定案由本轮数据席执行）\n"]
for s in SEATS:
    text = (JD / f"FLAGS-{s}.md").read_text(encoding="utf-8")
    parts.append(f"\n===== FLAGS-{s} =====\n" + text.rstrip("\n") + "\n")

parts.append("""
===== 主持复核旗标（tradition 复核，FREEZE-r69 §二）=====
- 主持 tradition 复核旗标 7 件（全在 S3 批，卡面确无 tradition/system 字段而 basis 首行作「卡面 tradition＝liuyao，與卡面一致」，BZ-021/ZY-003 型措辞不实；主持裁定登记不重测，值本身与体裁一致、无 value 误标）：LY-017、LY-019、LY-021、LY-022、LY-034、LY-103、LY-105。anon 对位由数据席经 host-mapping 逐件核定后定案。
""")

out = JD / "FLAGS-selfreported-r69.md"
out.write_text("".join(parts), encoding="utf-8")
print("written", out, out.stat().st_size, "bytes")
