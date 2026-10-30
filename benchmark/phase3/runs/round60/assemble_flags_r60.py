#!/usr/bin/env python3
"""R60 host tooling: assemble judging/FLAGS-selfreported-r60.md from the
eight judge seats' FLAGS-{X,Y}{1..4}.md files. Mechanical merge only:
group by anon_id, seats listed, seat wording preserved verbatim after
the seat tag; case_id resolved via judging/host-mapping.json. No
adjudication here (data seat adjudicates into data/case-annotations-r60.json).
"""
import json
import re
from pathlib import Path

JD = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round60/judging")
hmap = json.loads((JD / "host-mapping.json").read_text(encoding="utf-8"))

entries = {}
for view in ("X", "Y"):
    for i in range(1, 5):
        seat = f"{view}{i}"
        text = (JD / f"FLAGS-{seat}.md").read_text(encoding="utf-8")
        for m in re.finditer(r"^-\s*(P3-[0-9a-f]{8})[：:]\s*(.+)$", text, re.M):
            anon, note = m.group(1), m.group(2).strip()
            assert anon in hmap, f"{anon} not in mapping ({seat})"
            entries.setdefault(anon, []).append((seat, note))

lines = [
    "# FLAGS-selfreported-r60（R60 平台评审自报旗标汇编，主持汇编）",
    "",
    f"共 {len(entries)} anon（去重后），逐条：anon_id｜case_id（主持据 host-mapping 对照）｜自报席位与疑点原文。定案由 R60 数据席逐件回原卡核对后落 data/case-annotations-r60.json；本汇编只登记、不裁断。",
    "",
]
for anon in sorted(entries):
    cid = hmap[anon]
    parts = "；".join(f"{seat}：{note}" for seat, note in entries[anon])
    lines.append(f"- {anon}｜{cid}｜{parts}")
(JD / "FLAGS-selfreported-r60.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("anons:", len(entries), "| raw seat entries:", sum(len(v) for v in entries.values()))
