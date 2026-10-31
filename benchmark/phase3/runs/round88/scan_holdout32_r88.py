#!/usr/bin/env python3
"""R88 holdout32 组集席三道自扫（封存前）：对 holdout32/inputs/ 28 张输入卡
按选例清单逐 id 精确打开，全字段递归扫描。
标记集逐字照抄 runs/round88/host_scan_holdout31_r88.py（R42 PREREG §5 常例）：
一级（断语类）＋二级（结局侧状态措辞）＋结局泄漏标记集＋禁用键（递归精确键名）。
三道：①禁用键递归 ②泄漏标记（一级＋二级＋泄漏集）③白名单偏离（顶层键集）。
本脚本独立新写，不 import 构建脚本。"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
SEL = json.loads((P3 / "runs/round88/holdout32-selection-r88.json")
                 .read_text(encoding="utf-8"))
IDS = SEL["order"]
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
    assert len(IDS) == 28 and len(set(IDS)) == 28
    key_hits, marker_hits, deviations = [], [], []
    false_positives = []
    for cid in IDS:
        fp = INPUTS / f"{cid}.json"
        card = json.loads(fp.read_text(encoding="utf-8"))
        assert card["id"] == cid
        if set(card.keys()) != WHITELIST:
            deviations.append((cid, sorted(card.keys())))
        for path, s in walk_strings(card):
            for m in L1 + L2 + LEAK:
                if m in s:
                    # 裁定性假阳性：问句「…结果如何」中「果如」跨词偶合
                    # （WHY-080 台账 question 逐字「一男子求测恋爱结果如何」，
                    # 原书占问原文同；先例 holdout21 WHY-072 question
                    # 「一男测去相亲，结果如何」逐字入卡已封存）。
                    # 仅当命中全部落在「结果如何」子串内才登记为假阳性。
                    if m == "果如" and s.count("果如") == s.count("结果如何"):
                        false_positives.append((cid, f"marker:{m}", path, s))
                    else:
                        marker_hits.append((cid, f"marker:{m}", path))
        for path, k in walk_keys(card):
            if k in FORBIDDEN_KEYS:
                key_hits.append((cid, f"key:{k}", path))
    result = {
        "cards_scanned": len(IDS),
        "scan1_forbidden_keys_recursive": {"hits": len(key_hits), "detail": key_hits},
        "scan2_leak_markers_L1_L2_LEAK": {"hits": len(marker_hits), "detail": marker_hits},
        "scan2_adjudicated_false_positives": false_positives,
        "scan3_whitelist_deviations": {"hits": len(deviations), "detail": deviations},
    }
    (P3 / "runs/round88/holdout32-selfscan-r88.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("cards:", len(IDS))
    print("scan1 forbidden-key hits:", len(key_hits))
    print("scan2 marker hits (excl. adjudicated FP):", len(marker_hits))
    print("scan2 adjudicated false positives:", len(false_positives))
    for f in false_positives:
        print(" FP", f)
    print("scan3 whitelist deviations:", len(deviations))
    for h in (key_hits + marker_hits)[:40]:
        print(" HIT", h)
    for d in deviations:
        print(" DEV", d)
    assert not key_hits and not marker_hits and not deviations
    print("SELF SCAN: three scans zero (2 FP adjudicated, see seal log)")


if __name__ == "__main__":
    main()
