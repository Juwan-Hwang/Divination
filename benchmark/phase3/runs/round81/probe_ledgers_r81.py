#!/usr/bin/env python3
import json, os
from pathlib import Path
BASE=Path("/home/hatch/workspace/divination/benchmark/phase3")
paths=[
 "runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json",
 "runs/round76/digestion/SUPPLY-MINING-kaiwu-r76.json",
 "runs/round76/digestion/SUPPLY-MINING-qiwu-r76.json",
 "runs/round76/digestion/SUPPLY-MINING-shijianguo-r76.json",
 "runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json",
 "runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json",
 "runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json",
 "runs/round56/digestion/SUPPLY-MINING-quwei-r56.json",
 "runs/round56/digestion/SUPPLY-MINING-qimen-r56.json",
 "runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json",
 "runs/round59/digestion/SUPPLY-MINING-quwei-r59.json",
 "runs/round56/digestion/SUPPLY-GOLD-SUPPLEMENT-r56.json",
 "runs/round57/digestion/SUPPLY-RECHECK-qwpartial-r57.json",
 "runs/round59/digestion/SUPPLY-RECHECK-why-partial-r59.json",
 "runs/round58/digestion/QM-REVIEW-r58.json",
]
for rel in paths:
    p=BASE/rel
    print("="*80)
    print(rel, "exists", p.exists(), "bytes", p.stat().st_size if p.exists() else None)
    if not p.exists(): continue
    try:
        d=json.load(open(p,encoding='utf-8'))
    except Exception as e:
        print(" load err", e); continue
    if isinstance(d, dict):
        print(" top keys:", list(d.keys()))
        for k,v in d.items():
            if isinstance(v, list):
                print(f"  {k}: list len={len(v)}")
                if v and isinstance(v[0], dict):
                    print(f"    item0 keys: {list(v[0].keys())}")
                    # print small sample values for eligibility fields
                    import copy
                    s={kk: (str(vv)[:200]) for kk,vv in v[0].items() if kk not in ('input_side','input_fields','master_assertion','outcome','master_prediction','outcome_record','passage_full')}
                    print(f"    item0 (trunc): {s}")
            elif isinstance(v, dict):
                print(f"  {k}: dict keys={list(v.keys())[:30]}")
                print(f"    value trunc: {str(v)[:800]}")
            else:
                print(f"  {k}: {str(v)[:500]}")
    elif isinstance(d, list):
        print(f" list len={len(d)} item0 keys={list(d[0].keys()) if d and isinstance(d[0],dict) else d[:2]}")
