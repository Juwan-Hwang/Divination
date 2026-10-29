#!/usr/bin/env python3
"""R30 liuyao diagnosis (diagnosis role, liuyao track).

Population: dev9 cases whose host-meta tradition is 'liuyao' or '六爻'
(n=325 = dev8 liuyao-sense 246 + dev8 BQ cases labelled 六爻 16 + YM 56 + DT 7).
Dual read: round28 (live method after rollback) and round29 (adjudication
add-on snapshot). Deep-loss set (declared): R29 pair diff <= -3.0.
Basis primary morphology classes below were assigned by the diagnosis role
after reading every deep-loss basis text (round29 predictions); this script
only encodes those assignments and computes all statistics.
Outputs: R30-deep-loss-cases.jsonl + stats JSON printed to stdout.
No method/input/score files are modified.
"""
import json, math, re
from pathlib import Path
from collections import Counter, defaultdict

P3 = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent

meta = json.load(open(P3 / 'runs/round29/judging/host-meta.json'))
master = json.load(open(P3 / 'data/master-baseline-dev9.json'))
fs = {r: json.load(open(P3 / f'runs/{r}/final-scores.json')) for r in ('round26', 'round28', 'round29')}
dev8_ids = set(json.load(open(P3 / 'data/master-baseline-dev8.json')))

def tot(fsd, c):
    v = fsd['ours_axis2'][c]
    return v['total'] if isinstance(v, dict) else v

pop = sorted(c for c in fs['round29']['ours_axis2'] if meta[c]['tradition'] in ('liuyao', '六爻'))

def seg(ids, fsd):
    ids = [c for c in ids if c in fsd['ours_axis2'] and c in master]
    pair = [tot(fsd, c) - master[c]['total'] for c in ids]
    n = len(pair); mean = sum(pair) / n
    se = math.sqrt(sum((x - mean) ** 2 for x in pair) / (n - 1)) / math.sqrt(n) if n > 1 else 0.0
    return {'n': n, 'pair_diff': round(mean, 3), 'SE': round(se, 3),
            'ours_mean': round(sum(tot(fsd, c) for c in ids) / n, 3),
            'master_mean': round(sum(master[c]['total'] for c in ids) / n, 3),
            'W/T/L': f"{sum(1 for x in pair if x > 0)}/{sum(1 for x in pair if x == 0)}/{sum(1 for x in pair if x < 0)}"}

def source_group(c):
    inp = json.load(open(P3 / 'inputs-r28' / f'{c}.json'))
    prov = inp.get('provenance') or {}
    book = prov.get('book') or prov.get('work') or ''
    for key, name in [('增刪卜易', '增删卜易'), ('增删卜易', '增删卜易'), ('卜筮正宗', '卜筮正宗'),
                      ('卜筮全书', '卜筮全书'), ('卜筮全書', '卜筮全书'), ('易冒', '易冒'),
                      ('易隐', '易隐'), ('易隱', '易隐'), ('断易天机', '断易天机'), ('斷易天機', '断易天机')]:
        if key in book:
            return name
    if c.startswith('YM-'): return '易冒'
    if c.startswith('DT-'): return '断易天机'
    if c.startswith('YY'): return '易隐'
    if c.startswith('BQ-'): return '卜筮全书'
    if c.startswith('LY-'): return '增删卜易/卜筮正宗等(LY系,书名未标注)'
    return '其他'

CAT_RULES = [
    ('疾病', ['病', '疾', '痘', '產', '产', '胎', '瘧', '疟']),
    ('寿元生死', ['壽', '寿', '生死']),
    ('天时农事', ['雨', '晴', '陰晴', '阴晴', '風', '风', '禾', '旱', '天時', '天时']),
    ('婚姻感情', ['婚', '夫妻', '偕老', '和好', '娶', '嫁']),
    ('官职功名', ['官', '升遷', '升迁', '功名', '貴', '贵', '考', '候選', '候选', '自陳', '自陈', '謁', '谒', '廷师', '延师', '援例', '月令', '發跡', '发迹', '掣籤', '掣签', '任']),
    ('求财债务', ['財', '财', '借貸', '借贷', '索債', '索债', '還銀', '还银', '貿易', '贸易', '開店', '开店', '搖會', '摇会', '會金', '银']),
    ('出行行人音信', ['出門', '出门', '行', '回', '信', '同行', '避亂', '避乱']),
    ('诉讼', ['訟', '讼']),
    ('家宅', ['宅', '井']),
]
def category(q):
    if not q: return '未明'
    for name, kws in CAT_RULES:
        if any(k in q for k in kws):
            return name
    return '其他'

def question(c):
    inp = json.load(open(P3 / 'inputs-r28' / f'{c}.json'))
    return (inp.get('context') or {}).get('question') or ''

# ---- headline stats
stats = {}
for r in ('round28', 'round29'):
    stats[r] = {'pop325': seg(pop, fs[r]),
                'dev8_262': seg([c for c in pop if c in dev8_ids], fs[r]),
                'dev8_246trad': seg([c for c in pop if c in dev8_ids and meta[c]['tradition'] == 'liuyao'], fs[r]),
                'YM56': seg([c for c in pop if c.startswith('YM-')], fs[r]),
                'DT7': seg([c for c in pop if c.startswith('DT-')], fs[r])}
stats['round26_dev8overlap'] = seg([c for c in pop if c in fs['round26']['ours_axis2']], fs['round26'])

# ---- component contributions (master sub-scores exist only for a subset)
comp = {}
for r in ('round28', 'round29'):
    sub_ids = [c for c in pop if 'direction' in master[c]]
    gaps = {}
    for k in ('direction', 'claims', 'timing'):
        gaps[k] = sum(master[c][k] - fs[r]['ours_sub'][c][k] for c in sub_ids)
    tot_gap = sum(gaps.values())
    comp[r] = {'n_sub': len(sub_ids),
               'gap': {k: round(v, 2) for k, v in gaps.items()},
               'share_pct': {k: round(v / tot_gap * 100, 1) for k, v in gaps.items()},
               'total_gap_sub': round(tot_gap, 2),
               'mean_pair_sub': round(-tot_gap / len(sub_ids), 3)}
    # direction-zero mass over full pop (ours_sub only)
    dz = [c for c in pop if fs[r]['ours_sub'][c]['direction'] == 0]
    neg_mass = -sum(min(0.0, tot(fs[r], c) - master[c]['total']) for c in pop)
    dz_mass = -sum(tot(fs[r], c) - master[c]['total'] for c in dz)
    comp[r]['dir0'] = {'n': len(dz), 'gap': round(dz_mass, 2), 'share_of_neg_mass_pct': round(dz_mass / neg_mass * 100, 1)}

# ---- deep-loss set: R29 pair diff <= -3.0 (declared in report)
deep = [c for c in pop if tot(fs['round29'], c) - master[c]['total'] <= -3.0]
deep.sort(key=lambda c: tot(fs['round29'], c) - master[c]['total'])
neg_mass29 = -sum(min(0.0, tot(fs['round29'], c) - master[c]['total']) for c in pop)
deep_gap = -sum(tot(fs['round29'], c) - master[c]['total'] for c in deep)
deep_stats = {'n': len(deep), 'gap': round(deep_gap, 2), 'neg_mass_r29': round(neg_mass29, 2),
              'share_pct': round(deep_gap / neg_mass29 * 100, 1),
              'also_deep_r28': sum(1 for c in deep if tot(fs['round28'], c) - master[c]['total'] <= -3.0),
              'deep_r28_n': sum(1 for c in pop if tot(fs['round28'], c) - master[c]['total'] <= -3.0)}

# ---- basis morphology: manual primary assignments (read case-by-case by diagnosis role)
CLASS = {
 'V': '伏神待出门槛否决', 'H': '动化定性单点定终局', 'T': '合参相抵/票决合成',
 'S': '静态本气与空破待实资格主导', 'I': '输入残损自认主导', 'E': '电报式压缩(无推理链)',
 'A': '应期/等级坐标主导(方向基本对)'}
ASSIGN = {
 'BQ-014': 'I', 'LY-006': 'T', 'LY-013': 'H', 'LY-015': 'H', 'LY-017': 'S', 'LY-417': 'T',
 'LY-434': 'T', 'YM-009': 'T', 'YM-025': 'V', 'YM-049': 'T', 'LY-231': 'H', 'LY-421': 'T',
 'LY-433': 'T', 'YY-016': 'V', 'LY-211': 'H', 'LY-235': 'T', 'LY-253': 'H', 'LY-426': 'T',
 'LY-437': 'H', 'LY-441': 'T', 'LY-609': 'H', 'LY-003': 'V', 'LY-033': 'H', 'LY-523': 'H',
 'LY-024': 'E', 'LY-405': 'H', 'LY-506': 'H', 'LY-022': 'E', 'LY-613': 'V', 'LY-627': 'T',
 'YM-029': 'V', 'LY-206': 'V', 'LY-221': 'T', 'LY-244': 'H', 'LY-342': 'S', 'YM-008': 'S',
 'YM-032': 'V', 'LY-215': 'H', 'LY-219': 'S', 'LY-322': 'S', 'LY-436': 'H', 'DT-004': 'H',
 'LY-023': 'E', 'LY-305': 'H', 'LY-425': 'H', 'LY-430': 'I', 'LY-531': 'S', 'DT-007': 'T',
 'LY-427': 'S', 'LY-502': 'T', 'LY-515': 'T', 'YM-023': 'A', 'LY-202': 'S', 'LY-402': 'H',
 'LY-449': 'T', 'LY-526': 'S', 'LY-611': 'H', 'YM-054': 'H', 'LY-212': 'H', 'LY-220': 'H',
 'LY-241': 'H', 'LY-603': 'T', 'YM-055': 'A', 'BQ-018': 'I', 'BQ-021': 'I', 'DT-006': 'V',
 'LY-026': 'E', 'LY-028': 'H', 'LY-335': 'I', 'LY-527': 'T', 'LY-539': 'T', 'LY-615': 'H',
 'LY-624': 'T', 'YM-035': 'A', 'YM-070': 'S', 'YY-006': 'T', 'YY-014': 'T', 'YY-018': 'T',
}
missing = [c for c in deep if c not in ASSIGN]
extra = [c for c in ASSIGN if c not in deep]
assert not missing and not extra, f'assignment mismatch missing={missing} extra={extra}'

class_stats = {}
for code, name in CLASS.items():
    ids = [c for c in deep if ASSIGN[c] == code]
    g = -sum(tot(fs['round29'], c) - master[c]['total'] for c in ids)
    class_stats[code] = {'name': name, 'n': len(ids), 'gap': round(g, 2),
                         'share_of_deep_pct': round(g / deep_gap * 100, 1), 'ids': ids}

# ---- per-case rows
rows = []
for c in deep:
    pred29 = json.load(open(P3 / 'runs/round29/predictions' / f'{c}.json'))
    ms = master[c]
    row = {'id': c,
           'ours_r29': tot(fs['round29'], c), 'master': ms['total'],
           'pair_diff_r29': round(tot(fs['round29'], c) - ms['total'], 2),
           'pair_diff_r28': round(tot(fs['round28'], c) - ms['total'], 2),
           'ours_sub_r29': fs['round29']['ours_sub'][c],
           'master_sub': {k: ms[k] for k in ('direction', 'claims', 'timing') if k in ms} or None,
           'sub_diff_r29': ({k: round(fs['round29']['ours_sub'][c][k] - ms[k], 2)
                             for k in ('direction', 'claims', 'timing')} if 'direction' in ms else None),
           'source_group': source_group(c), 'category': category(question(c)),
           'question': question(c), 'basis_class': ASSIGN[c], 'basis_class_name': CLASS[ASSIGN[c]],
           'basis_len': len(pred29.get('basis') or ''), 'basis_r29': pred29.get('basis')}
    rows.append(row)
with open(OUT / 'R30-deep-loss-cases.jsonl', 'w') as f:
    for row in rows:
        f.write(json.dumps(row, ensure_ascii=False) + '\n')

# ---- W vs deep feature comparison (R29)
FEATS = {'四路合参': '四路', '裁决记录/表': '裁决', '对表无此门类/无点': '对表无', '伏神': '伏',
         '只调量级': '只调量级', '应期对决': '对决', '输入残损/存疑': '残损', 'disputed标记词': 'disputed'}
def feats(c):
    pred = json.load(open(P3 / 'runs/round29/predictions' / f'{c}.json'))
    b = pred.get('basis') or ''
    return b, {k: (v in b) for k, v in FEATS.items()}
wins = [c for c in pop if tot(fs['round29'], c) - master[c]['total'] > 0]
wins8 = [c for c in wins if c in dev8_ids and meta[c]['tradition'] == 'liuyao']
cmp_ = {'pop_base': {'n': len(pop), 'category': Counter(category(question(c)) for c in pop),
                     'source': Counter(source_group(c) for c in pop),
                     'deep_dir0_n': sum(1 for c in deep if fs['round29']['ours_sub'][c]['direction'] == 0)}}
for label, ids in [('deep78', deep), ('W69_all', wins), ('W53_dev8trad', wins8),
                   ('nondeep_neg', [c for c in pop if -3 < tot(fs['round29'], c) - master[c]['total'] < 0])]:
    lens, fcount = [], Counter()
    for c in ids:
        b, fm = feats(c)
        lens.append(len(b)); fcount.update(k for k, v in fm.items() if v)
    lens.sort()
    cmp_[label] = {'n': len(ids), 'basis_len_median': lens[len(lens) // 2] if lens else None,
                   'feat_pct': {k: round(fcount[k] / len(ids) * 100, 1) for k in FEATS} if ids else {},
                   'category': Counter(category(question(c)) for c in ids),
                   'source': Counter(source_group(c) for c in ids)}

print(json.dumps({'stats': stats, 'comp': comp, 'deep': deep_stats,
                  'class_stats': class_stats, 'compare': cmp_}, ensure_ascii=False, indent=1))
