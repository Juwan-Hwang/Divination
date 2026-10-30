#!/usr/bin/env python3
"""R39 DIAG-LR-R39-CHARTER-RESPONSE 复算脚本（诊断席，只计数不改 method）。
显式文件清单，无 glob：final-scores.json + test_gold.jsonl + 编码表（本文件内）。
编码口径：W-CHARTER §1.2 优先序 H->C->B->A->W->D/E，每例一主标；
同号排除、不可测排除；双报＝接口含入（W 主标）／硬核下限（basis 含显式权重自述
或「列面齐备＋终局归属面与结局主导面相反」两项同立且无含混）。
"""
import json, math

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
FS = f"{BASE}/runs/holdout15-acceptance/judging/final-scores.json"
GOLD = f"{BASE}/holdout15/test_gold.jsonl"

# 手工编码表（逐例依据见 DIAG-LR-R39-CHARTER-RESPONSE.md §1.3-§1.4 附表说明栏）
# label: 主标; hardcore: 仅 W 例有意义; star: 边界含混（接口带）
CODING = {
    # BYZ 《六壬辨疑》8 负例
    "BYZ-001": dict(label="W", hardcore=True,  star=False),  # basis 明言「鬼面降次级事件线」显式权重自述，元首/末传落点压鬼面定主线，翻转即反号
    "BYZ-006": dict(label="E", hardcore=False, star=False),  # 科场/守望终局同号（利/安），同号排除 W；名分不显 vs 必中＝量级档位（子型三残余 E），权重现象只记附注
    "BYZ-007": dict(label="E", hardcore=False, star=False),  # 县治可成方向与主线未翻转，差在升迁荐举/李公化解/妾孕等具体断语漏读错位＝E
    "BYZ-008": dict(label="W", hardcore=False, star=True),   # 进茹递进面已列且被赋首权定「就署成」，连茹鬼方/相害面翻转即反号；但静守文书空面未入列，W<->A 接口含混，非硬核
    "BYZ-011": dict(label="A", hardcore=False, star=False),  # 结局主导面（兵灾/劫煞/贼符游都/丑墓克宅）从未进入候选集，A 先于 W 命中
    "BYZ-012": dict(label="A", hardcore=False, star=True),   # 主导面（命上巳泄鬼生干化凶＋虎马待酉冲动身）未入候选集 -> A；乱首课名赋权为 A/W 接口附注
    "BYZ-013": dict(label="E", hardcore=False, star=False),  # 会试不成终局同向同主线，差在生男不育/行程实况等事件线具体度＝E
    "BYZ-014": dict(label="A", hardcore=False, star=True),   # 主导面（禄逢死气/魁度天门/子午冲害组）未入候选集 -> A；已列鬼/子孙赋权问题为 A/W 接口附注
    # YXS 《大六壬预测学》6 负例
    "YXS-010": dict(label="E", hardcore=False, star=True),   # 预售困难主线不误，量级由利薄升格为凶灾＝子型三量级残余 E；三交课名赋权为 W<->E 接口附注，不入 W 主标
    "YXS-011": dict(label="E", hardcore=False, star=False),  # 方向同号且近合，-0.25 残余量级/具体度微差＝E
    "YXS-012": dict(label="A", hardcore=False, star=True),   # 主导课名面（绝嗣/闭口无禄/禄坐绝）未入候选集（仅列涉害）-> A；涉害独大为 A/W-名接口附注
    "YXS-013": dict(label="D", hardcore=False, star=False),  # 方向主线全对，差在应期尺度（十天内 vs 月档巳日）＝D 应期残余；竞争者断语漏读记 E 附注
    "YXS-014": dict(label="E", hardcore=False, star=False),  # 终局无碍同号，病位具体断语错位（脾胃 vs 子宫肌瘤复发象）＝E
    "YXS-016": dict(label="A", hardcore=False, star=False),  # 主导面（太岁受冲、四月宣布条件）从未进入候选集 -> A；非应期残余，因终局方向已翻转
}

def se(p, n):
    return math.sqrt(p * (1 - p) / n) if n else 0.0

def report(ids, name):
    n = len(ids)
    from collections import Counter
    c = Counter(CODING[i]["label"] for i in ids)
    w_incl = c.get("W", 0)
    w_hard = sum(1 for i in ids if CODING[i]["label"] == "W" and CODING[i]["hardcore"])
    de = c.get("D", 0) + c.get("E", 0)
    merged = w_incl + de
    print(f"--- {name} (n={n}) ---")
    for lab in ["W", "A", "B", "C", "D", "E", "H"]:
        k = c.get(lab, 0)
        print(f"  {lab}: {k}/{n} = {100*k/n:.1f}% (SE {100*se(k/n, n):.1f}pp)")
    print(f"  W 接口含入: {w_incl}/{n} = {100*w_incl/n:.1f}% (SE {100*se(w_incl/n, n):.1f}pp)")
    print(f"  W 硬核下限: {w_hard}/{n} = {100*w_hard/n:.1f}% (SE {100*se(w_hard/n, n):.1f}pp)")
    print(f"  子型三残余 D+E: {de}/{n} = {100*de/n:.1f}% (SE {100*se(de/n, n):.1f}pp)")
    print(f"  合并层 W+(D+E): {merged}/{n} = {100*merged/n:.1f}% (SE {100*se(merged/n, n):.1f}pp)")
    print(f"  含混例: {[i for i in ids if CODING[i]['star']]}")
    return dict(n=n, counter=dict(c), w_incl=w_incl, w_hard=w_hard, de=de, merged=merged)

def main():
    fs = json.load(open(FS))
    per = fs["per_case"]
    liuren = [k for k in per if k.startswith("BYZ") or k.startswith("YXS")]
    assert len(liuren) == 20, len(liuren)
    neg = sorted([k for k in liuren if per[k]["diff"] < 0])
    assert set(neg) == set(CODING), (set(neg) ^ set(CODING))
    byz = [k for k in neg if k.startswith("BYZ")]
    yxs = [k for k in neg if k.startswith("YXS")]
    print(f"六壬 20 例 W/T/L 复核: W={sum(1 for k in liuren if per[k]['diff']>0)} "
          f"T={sum(1 for k in liuren if per[k]['diff']==0)} L={len(neg)}")
    print(f"负例: BYZ {len(byz)} {byz}")
    print(f"负例: YXS {len(yxs)} {yxs}")
    seg = fs["segments"]
    for s in ["liuren-BYZ", "liuren-YXS", "liuren-all20"]:
        print(f"  {s}: diff={seg[s]['pair_diff']} SE={seg[s]['SE']}")
    # 金标构成核验（显式 id 逐行匹配，不扫他批）
    want = set(neg)
    gold = {}
    for line in open(GOLD):
        d = json.loads(line)
        if d["id"] in want:
            gold[d["id"]] = d
    assert set(gold) == want
    for cid in neg:
        g = gold[cid]
        print(f"  GOLD {cid}: src={g['source_work'][:20]} topic={g['question_or_topic'][:40]} "
              f"chart_complete={g['chart_complete']} grade={g['outcome_grade']} contam={g['contamination']}")
    report(byz, "BYZ 辨疑负例")
    report(yxs, "YXS 预测学负例")
    report(neg, "新鲜六壬负例合计（仅附读，不替代分源表）")

if __name__ == "__main__":
    main()
