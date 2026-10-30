#!/usr/bin/env python3
# R42 主持验封扫描（第三道，独立实现）— 标记集逐字承 runs/round42/PREREG.md §5。
# 用法: scan_verify_host_r42.py <inputs_dir> [extra_file ...]
# 递归扫描每个 JSON 文件的全部字符串值（含键名），命中任一标记即逐行报告；
# 退出码 0 = 零命中，1 = 有命中，2 = 用法/IO 错误。
import json
import sys
from pathlib import Path

MARKERS_L1 = ["断语线索", "断曰", "断語", "正议", "正議", "验语", "驗語",
              "断语：", "斷語：", "占断", "占斷", "大师断", "大師斷"]
MARKERS_L2 = ["果验", "果然", "果應", "后验", "後驗", "结局", "結局", "应验", "應驗"]
MARKERS = MARKERS_L1 + MARKERS_L2


def iter_strings(node, path="$"):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from iter_strings(k, path + ".<key>")
            yield from iter_strings(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from iter_strings(v, f"{path}[{i}]")
    elif isinstance(node, str):
        yield path, node


def scan_file(fp: Path):
    hits = []
    try:
        data = json.loads(fp.read_text(encoding="utf-8"))
    except Exception as e:  # 非 JSON 按纯文本扫
        text = fp.read_text(encoding="utf-8", errors="replace")
        for m in MARKERS:
            if m in text:
                hits.append(("$text", m))
        if hits:
            return hits
        print(f"WARN 非JSON且零命中: {fp} ({e})")
        return hits
    for path, s in iter_strings(data):
        for m in MARKERS:
            if m in s:
                hits.append((path, m))
    return hits


def main():
    if len(sys.argv) < 2:
        print("usage: scan_verify_host_r42.py <inputs_dir> [extra_file ...]")
        return 2
    files = []
    d = Path(sys.argv[1])
    if d.is_dir():
        files = sorted(d.glob("*.json"))
    elif d.is_file():
        files = [d]
    files += [Path(p) for p in sys.argv[2:]]
    total_hits = 0
    for fp in files:
        hits = scan_file(fp)
        for path, m in hits:
            print(f"HIT {fp.name} {path} marker={m}")
        total_hits += len(hits)
    print(f"scanned={len(files)} files, hits={total_hits}")
    return 1 if total_hits else 0


if __name__ == "__main__":
    sys.exit(main())
