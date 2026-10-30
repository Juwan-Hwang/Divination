#!/usr/bin/env python3
# R48 数据席（测字普查·乙）：将 §3 总清单表拼入 CENSUS-zichuquan-r48.md（§4 之前），含断言
from pathlib import Path

ROOT = Path("/home/hatch/workspace/divination")
CENSUS = ROOT / "benchmark/phase3/runs/round48/digestion/CENSUS-zichuquan-r48.md"
TABLE = ROOT / "benchmark/phase3/runs/round48/digestion/work-cezi-r48/section3-table-r48.md"

text = CENSUS.read_text(encoding="utf-8")
assert "## §3" not in text, "§3 已存在，勿重复拼入"
assert "## §4" in text
table = TABLE.read_text(encoding="utf-8")
assert table.count("| ZC-") == 165, table.count("| ZC-")
header = """## §3 成例总清单（编号判级 165 条，按卷内序）

编号沿 ZC 既有编号（抽例轮次序：R38 卷二全卷＋卷三/卷四抽页→001–098、R39 卷三补全→099–133、R41 未读页→134–162、R42 补核→163–165），本表按卷内书页序重排以便回叶对勘。题旨＝所测字·事主/所问（台账字段压缩转录）。新版页：标「实测」者为 R46 抽验或本席卷界实查页位，其余为逐卷锚点推定（±2–3 页，见 §6.4）；旧书页为台账实测值（ZC-072 采 R38 档 39，见 §6.3）。状态全为原判转录：已用＝合规且已入 h15–h18 封存集；不合格＝B 或 A-high 原判（A-high 在状态列作「A·high」）。
"""
new = text.replace("## §4", header + table + "\n## §4", 1)
CENSUS.write_text(new, encoding="utf-8")
chk = CENSUS.read_text(encoding="utf-8")
assert chk.count("| ZC-") == 165 and "## §3" in chk and "## §6" in chk
print(f"[assert ok] §3 已拼入，CENSUS 现 {len(chk.splitlines())} 行，ZC 表行 165")
