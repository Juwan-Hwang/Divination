#!/usr/bin/env python3
"""R89 主持第三道复扫（holdout32 开封前置复验）：对 holdout32/inputs/ 28 张输入卡
全字段递归扫描。标记集逐字承 runs/round42/PREREG.md §5 写死常例：
一级（断语类）+二级（结局侧状态措辞）；另加封存日志口径之
结局泄漏标记集与禁用键字段名扫描。零命中才许开封。
本脚本为 R89 主持独立新写（不 import 建卡/复扫脚本），体例承 R88 同名件适配 holdout32。"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
INPUTS = P3 / "holdout32" / "inputs"

L1 = ["断语线索", "断曰", "断語", "正议", "正議", "验语", "驗語",
      "断语：", "斷語：", "占断", "占斷", "大师断", "大師斷"]
L2 = ["果验", "果然", "果應", "后验", "後驗", "结局", "結局", "应验", "應驗"]
LEAK = ["结局为", "最终", "果如", "后遂", "大师断", "断曰", "outcome", "verdict"]
FORBIDDEN_KEYS = ["outcome", "verdict", "gold_answer", "master_verdict",
                  "断语", "结局", "master", "gold", "answer", "断曰", "正议",
                  "验语", "占断"]

WHITELIST = {"id", "tradition", "subject", "context", "question",
             "setting", "provenance", "redistributable",
             "license_status", "anchors"}


def walk_strings(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        yield path, obj


def walk_keys(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield f"{path}.{k}", k
            yield from walk_keys(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_keys(v, f"{path}[{i}]")


def main():
    files = sorted(INPUTS.glob("*.json"))
    assert len(files) == 28, len(files)
    hits = []
    keyset_bad = []
    for fp in files:
        card = json.loads(fp.read_text(encoding="utf-8"))
        if set(card.keys()) != WHITELIST:
            keyset_bad.append((fp.name, sorted(card.keys())))
        for path, s in walk_strings(card):
            for m in L1 + L2 + LEAK:
                if m in s:
                    hits.append((fp.name, f"marker:{m}", path))
        for path, k in walk_keys(card):
            for fk in FORBIDDEN_KEYS:
                if fk == k:
                    hits.append((fp.name, f"key:{fk}", path))
    print("cards:", len(files))
    print("marker/key hits:", len(hits))
    for h in hits[:40]:
        print(" HIT", h)
    print("whitelist deviations:", keyset_bad)
    assert not hits, hits
    print("THIRD SCAN: zero hits")


if __name__ == "__main__":
    main()
