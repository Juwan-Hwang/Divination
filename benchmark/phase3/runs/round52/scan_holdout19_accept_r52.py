#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R52 主持验收侧复扫：holdout19 输入卡内容级断语扫描（开封前置第 (2) 项）。

依据：runs/round52/PREREG.md §3 开封前置 (2)；标记集逐字承
runs/round42/PREREG.md §5 常量（一级 13 项＋二级 9 项＋字段名黑名单），
与 runs/round42/scan_content_markers_r42.py 脚本常量逐字一致（本脚本内嵌
常量并与该脚本常量断言全等，防漂移）。扫描对象：holdout19/inputs/ 25 卡
全字段递归字符串＋全部字段名。零命中才许开封分发。
"""
import json
from pathlib import Path

# 一级标记（断语类）——逐字复制 R42 PREREG §5
LEVEL1 = ['断语线索', '断曰', '断語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
# 二级标记（结局侧状态措辞）——逐字复制 R42 PREREG §5
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
# 字段名黑名单片段（R42 PREREG §5：字段名含断语/断曰/正议/验语/占断/线索·断者）
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '斷曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']


def strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from strings(v)


def field_names(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield k
            yield from field_names(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from field_names(v)


def main():
    # 与 R42 脚本常量全等断言（防标记集漂移）
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "scan42", Path(__file__).resolve().parent.parent / "round42" / "scan_content_markers_r42.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert LEVEL1 == mod.LEVEL1 and LEVEL2 == mod.LEVEL2 and FIELD_BLACKLIST == mod.FIELD_BLACKLIST, \
        "marker set drift vs R42 script constants"
    assert len(LEVEL1) == 13 and len(LEVEL2) == 9

    inputs = sorted((Path(__file__).resolve().parent.parent.parent / "holdout19" / "inputs").glob("*.json"))
    assert len(inputs) == 25, len(inputs)
    total_hits = 0
    for p in inputs:
        card = json.loads(p.read_text(encoding="utf-8"))
        for s in strings(card):
            for lvl, markers in (("L1", LEVEL1), ("L2", LEVEL2)):
                for m in markers:
                    if m in s:
                        total_hits += 1
                        print(f"HIT {p.name} {lvl} marker={m!r}")
        for name in field_names(card):
            for frag in FIELD_BLACKLIST:
                if frag in name:
                    total_hits += 1
                    print(f"FIELD-HIT {p.name} field={name!r} frag={frag!r}")
    print(f"accept-scan r52: {len(inputs)} cards, total hits = {total_hits}")
    assert total_hits == 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
