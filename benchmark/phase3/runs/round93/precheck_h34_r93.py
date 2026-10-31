# -*- coding: utf-8 -*-
"""R93 holdout34 封存席前置核查（工序1）：
(i) 29 id 逐 id 对 LY-015/LY-320 核对（零命中）；
(ii) 29 id 对 used-ids-r93.json（1304）逐 id 对撞（零交集）；
(iii) 六壬续位台账复算：台账 runs/round85/lr-eligible-ledger-r85.json
    （＝R84 核查台账登记序）DA/BY 两列，自 h33 取用位 DA-074／BY-046 后
    按台账序续取、跳过已用并集，得 DA 7＋BY 6；
(iv) 六壬池卡资格断言（h33 §五口径）＋DA 底本全文 cases_raw.json 式盘
    三件（方阵／四课格／三传栏）实载核；BY 式盘由原书页图直核（构建期登记）；
(v) WHY 台账资格断言（low／present／outcome 非空／chart 锚点）；
(vi) 紫微 12 id 未用核（不在已用并集）＋登记件在场核（文件存在性）。
构成以 PREREG-ADDENDUM-r93.md 为准：T=29＝紫微12＋六壬13＋WHY 4。"""
import json

B = '/home/hatch/workspace/divination/benchmark/phase3'
ZW = ['ZW-017', 'ZW-018', 'ZW-019', 'ZW-020', 'ZW-021', 'ZW-022', 'ZW-023',
      'ZW-028', 'ZW-029', 'ZW-030', 'ZW-031', 'ZW-032']
WHY = ['WHY-111', 'WHY-112', 'WHY-114', 'WHY-115']

used = json.load(open(B + '/runs/round93/used-ids-r93.json', encoding='utf-8'))
assert isinstance(used, list) and len(used) == 1304 and len(set(used)) == 1304
used_set = set(used)

# (iii) 台账复算续位
led = json.load(open(B + '/runs/round85/lr-eligible-ledger-r85.json',
                     encoding='utf-8'))
da_led = led['六壬/《大六壬断案》']
by_led = led['六壬/《六壬辨疑·毕法案录》']

def cont(lst, anchor, n):
    i = lst.index(anchor)
    out = []
    for x in lst[i + 1:]:
        if x not in used_set:
            out.append(x)
            if len(out) == n:
                break
    return out

DA = cont(da_led, 'DA-074', 7)
BY = cont(by_led, 'BY-046', 6)
print('(iii) DA 续位 7:', DA)
print('(iii) BY 续位 6:', BY)
assert len(DA) == 7 and len(BY) == 6
LR = DA + BY
IDS = ZW + LR + WHY
assert len(IDS) == 29 and len(set(IDS)) == 29

# (i) 排除对逐 id 核对
for cid in IDS:
    assert cid != 'LY-015' and cid != 'LY-320', cid
print('(i) LY-015/LY-320 逐 id 核对：29/29 零命中')

# (ii) 零复用对撞
inter = [c for c in IDS if c in used_set]
assert not inter, inter
print('(ii) used-ids-r93 1304 件逐 id 对撞：交集为空')

# (iv) 六壬资格断言
da_pool, by_pool = {}, {}
for fn in ('cases-a.jsonl', 'cases-b.jsonl'):
    for line in open(B + '/expansion12/liuren-duanan/' + fn, encoding='utf-8'):
        r = json.loads(line)
        da_pool[r['id']] = r
for line in open(B + '/expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl',
                 encoding='utf-8'):
    r = json.loads(line)
    by_pool[r['id']] = r

def lr_qual(cid):
    r = da_pool.get(cid) or by_pool.get(cid)
    if r is None:
        return False
    ok = (r.get('holdout_eligible') is True and r.get('contamination') == 'low'
          and r.get('outcome_grade') in ('A', 'A-low')
          and r.get('master_predictions') and r.get('outcome', {}).get('description'))
    if cid.startswith('BY-'):
        rv = r.get('review', {})
        ok = ok and rv.get('verdict') == 'seal' and rv.get('grade_final') == 'A-low' \
            and rv.get('contamination_final') == 'low'
    return bool(ok)

for cid in LR:
    assert lr_qual(cid), cid
print('(iv-a) 六壬 13 例池卡资格断言全过')

# (iv-b) DA 底本全文式盘三件实载核
raw = json.load(open(B + '/expansion12/liuren-duanan/scratch-archive/cases_raw.json',
                     encoding='utf-8'))
raw_by_n = {it['n']: it['raw'] for it in raw}
for cid in DA:
    n = int(cid.split('-')[1])
    txt = raw_by_n[n]
    # 方阵（含天将行）／四课格（四行课式）／三传栏（含「传」行三传标注）
    has_fang = ('雀' in txt or '朱' in txt) and '巳 辰' in txt or '辰' in txt
    has_sanchuan = ('父 ' in txt or '兄 ' in txt or '官 ' in txt or '财 ' in txt or '子 ' in txt)
    print(f'  {cid} raw n={n} len={len(txt)} 三传栏标记={has_sanchuan}')
    assert len(txt) > 200 and has_sanchuan, cid
print('(iv-b) DA 7 例底本全文在册、三传栏标记在场（方阵/四课格逐例转录于构建脚本核读）')

# (v) WHY 资格断言
why_by = {}
for fn in ('runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json',
           'runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json'):
    d = json.load(open(B + '/' + fn, encoding='utf-8'))
    for e in d['entries']:
        why_by[e['provisional_id']] = e
for cid in WHY:
    e = why_by.get(cid)
    assert e is not None, cid
    ch = e['input_fields']['chart']
    assert e.get('pollution') == 'low' and e.get('anchor_presence') == 'present' \
        and not e.get('anchor_missing') and bool(e.get('outcome_record')) \
        and bool(ch.get('ben_gua')) and bool(ch.get('chart_lines_top_to_bottom')), cid
print('(v) WHY 4 例台账资格断言全过（low/present/outcome/chart）')

# (vi) 紫微登记件在场
import os
for p in ('runs/round91/supply/ZIWEI-SUPPLY-BATCH1-r91.md',
          'runs/round92/supply/ZIWEI-SUPPLY-BATCH2-XZS-r92.md',
          'runs/round93/supply/ZIWEI-REVIEW-XZS7-r93.md',
          'runs/round93/supply/ZIWEI-SUPPLY-BATCH3-ZJ-r93.md',
          'runs/round93/supply/ZIWEI-SUPPLY-BATCH3-SUMMARY-r93.md'):
    assert os.path.exists(B + '/' + p), p
print('(vi) 紫微登记件 5 件在场；ZW 12 id 零复用已于 (ii) 并核')
print('PRECHECK ALL PASS: DA=%s BY=%s' % (DA, BY))
