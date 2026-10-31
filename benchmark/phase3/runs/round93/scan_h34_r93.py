#!/usr/bin/env python3
"""R93 holdout34 封存席三道扫描（封存后复核）：对 holdout34/inputs/ 29 张输入卡
按构成清单逐 id 精确打开，全文递归扫描。
标记集出处＝holdout32-seal-log.md §八（源出 R42 PREREG §5），与 holdout33 轮同表：
一级 13 词＋二级 9 词＋泄漏标记集 8 词＋禁用键 13 键（递归精确键名）。
三道：①结局泄漏（禁用键递归＋一级/二级/泄漏集全文）
      ②大师姓名（邵彦和／邵先生／张官德／王虎应／徐曾生／许铨仁）
      ③字段白名单偏离。
本脚本独立新写，不 import 构建/封存脚本。命中逐件回读裁记入封存日志 §九。
"""
import json
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
IDS = ['DA-075', 'DA-076', 'DA-077', 'DA-078', 'DA-079', 'DA-080', 'DA-081',
       'BY-047', 'BY-048', 'BY-049', 'BY-050', 'BY-051', 'BY-053',
       'WHY-111', 'WHY-112', 'WHY-114', 'WHY-115',
       'ZW-017', 'ZW-018', 'ZW-019', 'ZW-020', 'ZW-021', 'ZW-022', 'ZW-023',
       'ZW-028', 'ZW-029', 'ZW-030', 'ZW-031', 'ZW-032']
INPUTS = P3 / "holdout34" / "inputs"

L1 = ["断语线索", "断曰", "断語", "正议", "正議", "验语", "驗語",
      "断语：", "斷語：", "占断", "占斷", "大师断", "大師斷"]
L2 = ["果验", "果然", "果應", "后验", "後驗", "结局", "結局", "应验", "應驗"]
LEAK = ["结局为", "最终", "果如", "后遂", "大师断", "断曰", "outcome", "verdict"]
FORBIDDEN_KEYS = ["outcome", "verdict", "gold_answer", "master_verdict",
                  "断语", "结局", "master", "gold", "answer", "断曰", "正议",
                  "验语", "占断"]
MASTERS = ["邵彦和", "邵先生", "张官德", "王虎应", "徐曾生", "许铨仁"]
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
    assert len(IDS) == 29 and len(set(IDS)) == 29
    key_hits, marker_hits, master_hits, deviations = [], [], [], []
    for cid in IDS:
        fp = INPUTS / f"{cid}.json"
        card = json.loads(fp.read_text(encoding="utf-8"))
        assert card["id"] == cid
        if set(card.keys()) != WHITELIST:
            deviations.append((cid, sorted(card.keys())))
        for path, s in walk_strings(card):
            for m in L1 + L2 + LEAK:
                if m in s:
                    marker_hits.append((cid, m, path, s))
            for nm in MASTERS:
                if nm in s:
                    master_hits.append((cid, nm, path, s))
        for path, k in walk_keys(card):
            if k in FORBIDDEN_KEYS:
                key_hits.append((cid, k, path))
    result = {
        "cards_scanned": len(IDS),
        "scan1_forbidden_keys_recursive": {"hits": len(key_hits), "detail": key_hits},
        "scan1_leak_markers_L1_L2_LEAK": {"hits": len(marker_hits), "detail": marker_hits},
        "scan2_master_names": {"hits": len(master_hits), "detail": master_hits},
        "scan3_whitelist_deviations": {"hits": len(deviations), "detail": deviations},
    }
    (P3 / "runs/round93/holdout34-scan-r93.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("cards:", len(IDS))
    print("scan1 forbidden-key hits:", len(key_hits))
    print("scan1 leak-marker hits:", len(marker_hits))
    for h in marker_hits:
        print("  MARKER", h)
    print("scan2 master-name hits:", len(master_hits))
    for h in master_hits:
        print("  NAME", h[0], h[1], h[2])
    print("scan3 whitelist deviations:", len(deviations))


if __name__ == "__main__":
    main()
