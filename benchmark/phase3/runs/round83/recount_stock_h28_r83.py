#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R83 供给复算（组集席开工盘上复算）：holdout28 组集前 eligible 未用存量全口径复算。
口径承 runs/round82/STOCK-RECOUNT-h27.md 与 runs/round83/PREREG.md §4：
已用并集盘上逐 id 实算（dev 池＋phase2 holdout2＋holdout3–27 金标 id＋holdout
inputs 卡 id＋顶层 inputs6–10 卡 id），断言＝1139；各主台账资格漏斗逐 id 复算；
GSZ 建卡口径以同一 five_elements 函数回原书文字层复核。结果落
runs/round83/recount_stock_h28_r83_out.json。只复算、不建卡。"""
import json, os, re

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
ROOT = '/home/hatch/workspace/divination'
R83 = os.path.join(BASE, 'runs/round83')


def load(p):
    return json.load(open(p, encoding='utf-8'))


# ---------- 已用并集 ----------
used_sources = {}
dev_ids = set(load(os.path.join(BASE, 'data/master-baseline-dev9.json')).keys())
used_sources['dev9_baseline_keys'] = len(dev_ids)
for dv in ('inputs-dev9', 'inputs-dev10', 'inputs-dev11', 'inputs-dev12', 'inputs'):
    d = os.path.join(BASE, dv)
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                dev_ids.add(fn[:-5])
used_sources['dev_pool_with_input_dirs'] = len(dev_ids)
h2_ids = set(load(os.path.join(ROOT, 'benchmark/phase2/splits2.json'))['holdout2'])
used_sources['phase2_splits2_holdout2'] = len(h2_ids)
gold_ids, gold_per_set = set(), {}
for i in range(3, 28):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    s = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            if line.strip():
                s.add(json.loads(line)['id'])
    gold_per_set[f'holdout{i}'] = len(s)
    gold_ids |= s
used_sources['holdout3_27_gold_ids'] = len(gold_ids)
used_sources['gold_per_set'] = gold_per_set
input_ids = set()
for i in range(2, 28):
    for dname in (f'holdout{i}/inputs', f'holdout{i}-inputs'):
        d = os.path.join(BASE, dname)
        if os.path.isdir(d):
            for fn in os.listdir(d):
                if fn.endswith('.json'):
                    input_ids.add(fn[:-5])
used_sources['holdout2_27_input_card_ids'] = len(input_ids)
extra_input_ids = set()
for i in range(6, 11):
    d = os.path.join(BASE, f'inputs{i}')
    if os.path.isdir(d):
        for fn in os.listdir(d):
            if fn.endswith('.json'):
                extra_input_ids.add(fn[:-5])
used_sources['toplevel_inputs6_10_card_ids'] = len(extra_input_ids)
used_union = dev_ids | h2_ids | gold_ids | input_ids | extra_input_ids
used_sources['used_union_total'] = len(used_union)
assert len(used_union) == 1139, len(used_union)

out = {'used_sources': used_sources, 'used_union_total': len(used_union), 'ledgers': {}}


def funnel(name, total, steps, qualified):
    """steps: list of (label, eliminated_ids) applied in order to qualified-track.
    qualified: set of ids passing all filters. Returns entry dict."""
    used = sorted(qualified & used_union)
    unused = sorted(qualified - used_union)
    out['ledgers'][name] = {
        'total': total,
        'steps': [{'label': lb, 'eliminated': el} for lb, el in steps],
        'qualified': sorted(qualified), 'qualified_n': len(qualified),
        'used': used, 'unused': unused, 'unused_n': len(unused)}
    return unused


# ---------- DS ----------
ds = load(os.path.join(BASE, 'runs/round76/digestion/SUPPLY-MINING-duanshi-r76.json'))
ds_by = {r['case_id']: r for r in ds['records']}
elig = set(ds_by)
s1 = sorted(c for c in elig if ds_by[c]['eligible_net'] is not True); elig -= set(s1)
s2 = sorted(c for c in elig if ds_by[c]['anchor_status'] != 'present'); elig -= set(s2)
s3 = sorted(c for c in elig if ds_by[c]['contamination_pre'] != 'low'); elig -= set(s3)
s4 = sorted(c for c in elig if not all(str(v).startswith('pass') for v in ds_by[c]['filters'].values())); elig -= set(s4)
s5 = sorted(c for c in elig if not (ds_by[c]['master_assertion'].strip() and ds_by[c]['outcome'].strip())); elig -= set(s5)
funnel('DS', len(ds_by), [('eligible_net=true', s1), ('anchor present', s2),
                          ('contamination low', s3), ('四滤全pass', s4), ('断语/结局非空', s5)], elig)

# ---------- QM 开悟 ----------
kw = load(os.path.join(BASE, 'runs/round76/digestion/SUPPLY-MINING-kaiwu-r76.json'))
kw_by = {c['case_id']: c for c in kw['cases']}
elig = set(kw_by)
s1 = sorted(c for c in elig if kw_by[c]['anchor_status'] != 'present'); elig -= set(s1)
s2 = sorted(c for c in elig if kw_by[c]['contamination_pre'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if kw_by[c]['separable'] is not True); elig -= set(s3)
s4 = sorted(c for c in elig if not (kw_by[c]['stem_check']['tianpan_ok'] and kw_by[c]['stem_check']['dipan_ok'])); elig -= set(s4)
s5 = sorted(c for c in elig if not (kw_by[c]['master_assertion'].strip() and kw_by[c]['outcome'].strip())); elig -= set(s5)
funnel('QM_KAIWU', len(kw_by), [('anchor present', s1), ('contamination low', s2),
                                ('separable=true', s3), ('stem_check天地盘双ok', s4), ('断语/结局非空', s5)], elig)

# ---------- QM 启悟 ----------
qw = load(os.path.join(BASE, 'runs/round76/digestion/SUPPLY-MINING-qiwu-r76.json'))
qw_by = {c['case_id']: c for c in qw['cases']}
elig = set(qw_by)
s1 = sorted(c for c in elig if qw_by[c]['anchor_status'] != 'present'); elig -= set(s1)
s2 = sorted(c for c in elig if qw_by[c]['contamination_pre'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if qw_by[c]['separable'] is not True); elig -= set(s3)
s4 = sorted(c for c in elig if not (qw_by[c]['master_assertion'].strip() and qw_by[c]['outcome'].strip())); elig -= set(s4)
funnel('QM_QIWU', len(qw_by), [('anchor present', s1), ('contamination low', s2),
                               ('separable=true', s3), ('断语/结局非空', s4)], elig)

# ---------- QM 石建国 ----------
sj = load(os.path.join(BASE, 'runs/round76/digestion/SUPPLY-MINING-shijianguo-r76.json'))
sj_by = {c['case_id']: c for c in sj['cases']}
elig = set(sj_by)
s1 = sorted(c for c in elig if sj_by[c]['anchor_status'] != 'present'); elig -= set(s1)
s2 = sorted(c for c in elig if sj_by[c]['contamination_pre'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if sj_by[c]['separable'] is not True); elig -= set(s3)
s4 = sorted(c for c in elig if not (sj_by[c]['master_assertion'].strip() and sj_by[c]['outcome'].strip())); elig -= set(s4)
funnel('QM_SHIJIANGUO', len(sj_by), [('anchor present', s1), ('contamination low', s2),
                                     ('separable=true', s3), ('断语/结局非空', s4)], elig)

# ---------- ZCB ----------
zc = load(os.path.join(BASE, 'runs/round76/digestion/SUPPLY-MINING-zichubu-r76.json'))
zc_cases = zc.get('cases') or zc.get('records') or zc.get('entries')
zc_by = {c['case_id']: c for c in zc_cases}
elig = set(zc_by)
s1 = sorted(c for c in elig if zc_by[c].get('eligible') is not True); elig -= set(s1)
s2 = sorted(c for c in elig if zc_by[c].get('anchor_status') != 'present'); elig -= set(s2)
s3 = sorted(c for c in elig if zc_by[c].get('contamination_pre') != 'low'); elig -= set(s3)
s4 = sorted(c for c in elig if zc_by[c].get('separable') is not True); elig -= set(s4)
s5 = sorted(c for c in elig if not ((zc_by[c].get('master_assertion') or '').strip() and (zc_by[c].get('outcome') or '').strip())); elig -= set(s5)
funnel('ZCB', len(zc_by), [('eligible=true', s1), ('anchor present', s2),
                           ('contamination low', s3), ('separable=true', s4), ('断语/结局非空', s5)], elig)

# ---------- GSZ（台账净资格＋建卡口径五要素） ----------
gsz = load(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
gsz_by = {e['provisional_id']: e for e in gsz['entries']}
elig = set(gsz_by)
s1 = sorted(c for c in elig if gsz_by[c]['grade'] != 'A'); elig -= set(s1)
s2 = sorted(c for c in elig if gsz_by[c]['pollution'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if gsz_by[c]['anchor_presence'] != 'present'); elig -= set(s3)
s4 = sorted(c for c in elig if gsz_by[c]['eligible_net'] is not True); elig -= set(s4)
s5 = sorted(c for c in elig if not all(gsz_by[c]['filters'].values())); elig -= set(s5)
s6 = sorted(c for c in elig if not (gsz_by[c]['master_prediction'].strip() and gsz_by[c]['outcome_record'].strip())); elig -= set(s6)
net_list = set(gsz['counts']['net_eligible_A_low_present'])
assert elig == net_list, (sorted(elig ^ net_list))
funnel('GSZ_NET', len(gsz_by), [('grade A', s1), ('pollution low', s2), ('anchor present', s3),
                                ('eligible_net=true', s4), ('四滤全true', s5), ('断语/结局非空', s6)], elig)

book_txt = open(os.path.join(BASE, 'runs/round76/gsz-book-r76.txt'), encoding='utf-8').read()
LIUQIN = ['兄弟', '子孙', '妻财', '官鬼', '父母']
GANZHI = list('甲乙丙丁戊己庚辛壬癸子丑寅卯辰巳午未申酉戌亥')


def five_elements(cid):
    e = gsz_by[cid]
    chart = e['input_fields']['chart']
    lines = chart['chart_lines_top_to_bottom']
    joined = '\n'.join(lines)
    el = {}
    el['gua_name'] = bool(chart.get('ben_gua'))
    el['moving'] = ('动' in joined) or bool(chart.get('bian_gua'))
    el['shi_ying'] = ('世' in joined) and ('应' in joined)
    el['liuqin_nazhi'] = all(
        any(lq in ln and any(g in ln for g in GANZHI) for ln in lines)
        for lq in [x for x in LIUQIN if any(x in ln for ln in lines)]) and \
        sum(1 for ln in lines if any(lq in ln for lq in LIUQIN)) >= 6
    asked = e['input_fields']['asked_at']
    el['yuejian_richen'] = bool(re.search(r'月', asked) and re.search(r'日', asked))
    el['in_book_ben_gua'] = chart['ben_gua'][:2] in book_txt or chart['ben_gua'] in book_txt
    el['in_book_asked'] = asked.split('（')[0][:7] in book_txt.replace(' ', '')
    return el


fe = {}
for cid in sorted(elig):
    el = five_elements(cid)
    fe[cid] = {'elements': el, 'pass': bool(all(el.values()))}
card_elig = {c for c in elig if fe[c]['pass']}
out['gsz_five_elements'] = fe
funnel('GSZ_CARD', len(gsz_by), [('台账净资格全过后五要素复核不过',
                                  sorted(elig - card_elig))], card_elig)

# ---------- WHY 一轮 ----------
why = load(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json'))
why_by = {e['provisional_id']: e for e in why['entries']}
why_net = set(why['counts']['net_eligible_A_low_present'])
elig = set(why_by)
s1 = sorted(c for c in elig if why_by[c]['anchor_presence'] != 'present'); elig -= set(s1)
s2 = sorted(c for c in elig if why_by[c]['pollution'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if c not in why_net); elig -= set(s3)
assert elig == why_net, sorted(elig ^ why_net)
funnel('WHY_R1', len(why_by), [('anchor present', s1), ('pollution low', s2),
                               ('counts净入账名单成员', s3)], elig)

# ---------- WHY 二轮 ----------
why2 = load(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json'))
why2_by = {e['provisional_id']: e for e in why2['entries']}
elig = set(why2_by)
s1 = sorted(c for c in elig if why2_by[c]['grade'] != 'A'); elig -= set(s1)
s2 = sorted(c for c in elig if why2_by[c]['pollution'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if why2_by[c]['anchor_presence'] != 'present'); elig -= set(s3)
s4 = sorted(c for c in elig if why2_by[c]['eligible_net'] is not True); elig -= set(s4)
s5 = sorted(c for c in elig if not all(why2_by[c]['filters'].values())); elig -= set(s5)
s6 = sorted(c for c in elig if not (why2_by[c]['master_prediction'].strip() and why2_by[c]['outcome_record'].strip())); elig -= set(s6)
_n2 = why2['counts']['net_eligible_A_low_present']
assert elig == (set(_n2) if isinstance(_n2, list) else elig) and len(elig) == (len(_n2) if isinstance(_n2, list) else _n2) == 36, len(elig)
cnt2 = why2.get('counts') or {}
out['why2_counts_keys'] = {k: (len(v) if isinstance(v, list) else v) for k, v in cnt2.items()}
funnel('WHY_R2', len(why2_by), [('grade A', s1), ('pollution low', s2), ('anchor present', s3),
                                ('eligible_net=true', s4), ('四滤全true', s5), ('断语/结局非空(字段口径见注)', s6)], elig)

# ---------- QW ----------
qwq = load(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-quwei-r56.json'))
qwq_by = {c['provisional_id']: c for c in qwq['entries']}
elig = set(qwq_by)
s1 = sorted(c for c in elig if qwq_by[c]['anchor_presence'] != 'present'); elig -= set(s1)
s2 = sorted(c for c in elig if qwq_by[c]['pollution'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if not all(str(v).startswith('pass') for v in qwq_by[c]['filters'].values())); elig -= set(s3)
s4 = sorted(c for c in elig if not qwq_by[c]['outcome_record'].strip()); elig -= set(s4)
funnel('QW', len(qwq_by), [('anchor present', s1), ('pollution low', s2),
                           ('四滤全pass', s3), ('结局非空', s4)], elig)
qw59 = load(os.path.join(BASE, 'runs/round59/digestion/SUPPLY-MINING-quwei-r59.json'))
qw59_by = {c['provisional_id']: c for c in qw59['entries']}
elig = set(qw59_by)
s1 = sorted(c for c in elig if qw59_by[c]['anchor_presence'] != 'present'); elig -= set(s1)
s2 = sorted(c for c in elig if qw59_by[c]['pollution'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if not all(str(v).startswith('pass') for v in qw59_by[c]['filters'].values())); elig -= set(s3)
s4 = sorted(c for c in elig if qw59_by[c]['eligible_net'] is not True); elig -= set(s4)
s5 = sorted(c for c in elig if not (qw59_by[c]['master_prediction'].strip() and qw59_by[c]['outcome_record'].strip())); elig -= set(s5)
funnel('QW_R59', len(qw59_by), [('anchor present', s1), ('pollution low', s2),
                                ('四滤全pass', s3), ('eligible_net=true', s4), ('断语/结局非空', s5)], elig)

# ---------- QM 旧池 ----------
qmo = load(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-qimen-r56.json'))
qmo_by = {c['provisional_id']: c for c in qmo['cases']}
rev = load(os.path.join(BASE, 'runs/round58/digestion/QM-REVIEW-r58.json'))
rev_by = {c['provisional_id']: c for c in rev['cases']}
elig = set(qmo_by)
s1 = sorted(c for c in elig if qmo_by[c]['anchor_presence'] != 'present'); elig -= set(s1)
s2 = sorted(c for c in elig if qmo_by[c]['pollution'] != 'low'); elig -= set(s2)
s3 = sorted(c for c in elig if rev_by.get(c, {}).get('eligible_optional') is not True); elig -= set(s3)
s4 = sorted(c for c in elig if not (qmo_by[c]['master_prediction_verbatim'].strip() and qmo_by[c]['outcome_record'].strip())); elig -= set(s4)
funnel('QM_OLD', len(qmo_by), [('anchor present(台账)', s1), ('pollution low(台账)', s2),
                               ('R58复核 eligible_optional=true', s3), ('断语/结局非空', s4)], elig)

# ---------- 汇总 ----------
L = out['ledgers']
summary = {
    'non_liuyao_unused': L['DS']['unused_n'] + L['QM_KAIWU']['unused_n'] + L['QM_QIWU']['unused_n']
        + L['QM_SHIJIANGUO']['unused_n'] + L['QM_OLD']['unused_n'] + L['QW']['unused_n']
        + L['ZCB']['unused_n'] - (1 if 'ZCB-003' in L['ZCB']['unused'] else 0),
    'zcb003_in_unused_raw': 'ZCB-003' in L['ZCB']['unused'],
    'liuyao_unused_card': L['GSZ_CARD']['unused_n'] + L['WHY_R1']['unused_n'] + L['WHY_R2']['unused_n'],
    'liuyao_unused_net': L['GSZ_NET']['unused_n'] + L['WHY_R1']['unused_n'] + L['WHY_R2']['unused_n'],
    'total_card': None,
}
summary['total_card'] = summary['non_liuyao_unused'] + summary['liuyao_unused_card']
out['summary'] = summary
with open(os.path.join(R83, 'recount_stock_h28_r83_out.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'used_union': len(used_union),
                  'unused': {k: v['unused'] for k, v in L.items()},
                  'summary': summary}, ensure_ascii=False))
