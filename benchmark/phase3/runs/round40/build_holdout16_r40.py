#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R40 数据角：组建并封存 holdout16（测字20＋辨疑10＋预测学3＋断案7＝40）。
口径：runs/round40/PREREG.md §5。只建卡与封存：不作断、不评分。
输入全部为显式路径；六壬 enrich 来自本轮回源核读落盘的 liuren-enrich-r40.jsonl；
断案课式自 cases_raw.json 逐例解析补录（库存行概要不直接建卡）。
"""
import json, re, hashlib, os, sys

BASE = os.path.expanduser('~/workspace/divination/benchmark/phase3')
OUT_DIR = os.path.join(BASE, 'holdout16')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)

ZC_SEL = ['ZC-070','ZC-071','ZC-075','ZC-077','ZC-079','ZC-081','ZC-082','ZC-083','ZC-084','ZC-085',
          'ZC-090','ZC-091','ZC-092','ZC-093','ZC-097','ZC-108','ZC-118','ZC-123','ZC-125','ZC-133']
BYZ_SEL = ['BYZ-016','BYZ-026','BYZ-029','BYZ-030','BYZ-043','BYZ-049','BYZ-070','BYZ-091','BYZ-101','BYZ-106']
YXS_SEL = ['YXS-017','YXS-018','YXS-019']
DA_SEL = ['DA-030','DA-045','DA-106','DA-123','DA-136','DA-165','DA-205']

BANNED = {'grade_note','contamination','contamination_reason','contamination_rationale','outcome',
          'outcome_grade','master','master_predictions','seal_eligible','seal_fail_reasons',
          'holdout_eligible','review','method_hint','disposition','notes','extractor_verdict_tail'}

def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

def norm(s):
    if s is None: return ''
    s = str(s)
    s = re.sub(r'[\s，。；：、（）()《》「」『』·\-—…·/．\.]', '', s)
    return s.lower()

def subj_text(subj):
    if isinstance(subj, dict): return subj.get('name_or_desc', '')
    return str(subj)

# ---------- sources ----------
zc = {}
for p in ['runs/round38/data-verify/zichu-cases-r38.jsonl',
          'runs/round39/data-verify/zichu-j3-cases-r39.jsonl']:
    for r in load_jsonl(os.path.join(BASE, p)): zc[r['id']] = r
byz = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round38/data-verify/bianyi-stock-r38.jsonl'))}
yxs = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round38/data-verify/yuce-stock-r38.jsonl'))}
enr = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round40/build-holdout16/liuren-enrich-r40.jsonl'))}
da = {}
for p in ['expansion12/liuren-duanan/cases-a.jsonl', 'expansion12/liuren-duanan/cases-b.jsonl']:
    for r in load_jsonl(os.path.join(BASE, p)): da[r['id']] = r
raw_cases = {c['n']: c for c in json.load(open(os.path.join(BASE, 'expansion12/liuren-duanan/scratch-archive/cases_raw.json'), encoding='utf-8'))}

cards, golds = {}, {}
strip_register = {}

# ---------- 测字 ----------
for cid in ZC_SEL:
    led = zc[cid]; ctx = led['context']; atts = ctx.get('attachments', {})
    strip_register[cid] = ['master_predictions（金标侧）','outcome（金标侧）','grade_note','contamination/contamination_reason',
                           'outcome_grade','holdout_eligible','notes','context.attachments.method_hint（空值）']
    cards[cid] = {
        'id': cid, 'tradition': '测字',
        'subject': led['subject'],
        'context': {'question': ctx.get('question'), 'asked_at': ctx.get('asked_at'),
                    'setting': ctx.get('setting'),
                    'attachments': {'character_written': atts.get('character_written')}},
        'provenance': {'book': led['provenance'].get('book'), 'edition': led['provenance'].get('edition'),
                       'page': led['provenance'].get('page')},
        'language': led.get('language')}
    mp = led.get('master_predictions') or [{}]
    golds[cid] = {
        'id': cid, 'tradition': '测字',
        'master': mp[0].get('master'),
        'source_work': '《字触》',
        'subject': led['subject'],
        'question_or_topic': ctx.get('question'),
        'asked_at': ctx.get('asked_at'),
        'context_at_prediction': ctx.get('setting'),
        'master_predictions': led['master_predictions'],
        'outcome': led['outcome'],
        'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': led.get('contamination_reason'),
        'grade_note': led.get('grade_note'),
        'provenance': {'work': '《字触》', 'edition': led['provenance'].get('edition'),
                       'page': led['provenance'].get('page')},
        'transcription': led['provenance'].get('transcription'),
        'license_status': led.get('license_status'),
        'redistributable': led.get('redistributable')}

# ---------- 六壬（辨疑＋预测学） ----------
LIU_META = {
    'BYZ': {'master': '张官德（清）', 'book': '六壬辨疑',
            'rationale': '清代地方个案，仅见于本书小众刻本，结局为局部事实，模型先验大概率不含；R40 回原书逐项核对。'},
    'YXS': {'master': '秦瑞生', 'book': '大六壬预测学',
            'rationale': '台湾命理书个案，人物为当地素人/学员，结局为个案事实，繁体竖排小众版本，污染低；R40 回原书页图逐项核对。'}}
PAGE_OVERRIDE = {'BYZ-106': '书页125（PDF139）'}
for cid in BYZ_SEL + YXS_SEL:
    led = byz[cid] if cid in byz else yxs[cid]
    e = enr[cid]; meta = LIU_META[cid[:3]]
    strip_register[cid] = ['master_predictions（金标侧，本轮回原书补录）','outcome（金标侧）','grade_note',
                           'contamination','outcome_grade','seal_eligible','seal_fail_reasons',
                           'chart（台账课名概要，不入卡；卡载回源全式）'] + (['disposition'] if cid in yxs else [])
    page = PAGE_OVERRIDE.get(cid, led['provenance'].get('page'))
    cards[cid] = {
        'id': cid, 'tradition': '六壬',
        'subject': {'name_or_desc': led['subject']},
        'context': {'question': e['question_or_topic'], 'asked_at': led['asked_at'],
                    'setting': '原书占验课式（全式见附件）',
                    'attachments': {'课式原文': e['chart_full'], 'chart_complete': True}},
        'provenance': {'book': meta['book'], 'edition': led['provenance'].get('edition'), 'page': page},
        'language': 'zh-Hans'}
    gn = led.get('grade_note') or ''
    grade_note = (f"A-low：{gn}；断验俱全可分离、断先于验。R40 回原书对勘相符。"
                  if gn else "A-low：断验俱全可分离、断先于验（原书断语＋案验/验证）；R40 回原书对勘相符、课式自原页全式转录。")
    golds[cid] = {
        'id': cid, 'tradition': '六壬', 'master': meta['master'],
        'source_work': led['source_work'], 'subject': led['subject'],
        'question_or_topic': e['question_or_topic'], 'asked_at': led['asked_at'],
        'context_at_prediction': '', 'chart_full': e['chart_full'], 'chart_complete': True,
        'master_predictions': e['master_predictions'], 'outcome': led['outcome'],
        'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': meta['rationale'], 'grade_note': grade_note,
        'provenance': {'work': led['source_work'], 'edition': led['provenance'].get('edition'), 'page': page},
        'transcription': 'visual', 'license_status': 'in-copyright', 'redistributable': False}

# ---------- 断案（cases_raw 逐例补录） ----------
JIANG = set('贵蛇朱合勾青空常玄虎后阴')
da_parse = {}
for cid in DA_SEL:
    n = int(cid.split('-')[1]); led = da[cid]; raw = raw_cases[n]['raw']
    lines = raw.split('\n')
    tidx = next(i for i, l in enumerate(lines) if re.match(r'\s*\d+\.', l))
    title = lines[tidx].strip()
    chart_lines = []
    for l in lines[tidx+1:]:
        if '邵先生曰' in l: break
        s = l.strip()
        if not s: continue
        if any(c in l for c in '。：，；、') or '谛' in l or '按' in l: continue
        if len(s) <= 60:
            chart_lines.append(' '.join(l.split()))
    assert len(chart_lines) >= 6, (cid, chart_lines)
    kepan = '；'.join(chart_lines)
    # 三传：每行末三 token 恰为「六亲 干支 天将」者（底本右栏三传列），应得恰 3 行
    sanchuan = []
    for cl in chart_lines:
        toks = cl.split()
        if len(toks) >= 3:
            a, b, c = toks[-3], toks[-2], toks[-1].rstrip('◎⊙')
            if a in '父母官兄财子' and re.fullmatch(r'[甲乙丙丁戊己庚辛壬癸]?[子丑寅卯辰巳午未申酉戌亥]', b) and c in JIANG:
                sanchuan.append(f"{a}{b}（{c}）")
    assert len(sanchuan) == 3, (cid, sanchuan)
    head = '\n'.join(lines[:tidx+4])
    m_yj = re.search(r'日([子丑寅卯辰巳午未申酉戌亥])将', head)
    m_xk = re.search(r'(甲[子戌申午辰寅]旬)，([子丑寅卯辰巳午未申酉戌亥]{2})空', head)
    assert m_yj and m_xk, (cid, head)
    yuejiang, xunkong = m_yj.group(1) + '将', f"{m_xk.group(1)}，{m_xk.group(2)}空"
    m_nm = re.search(r'([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥])生', title)
    atts = {'课盘原文': kepan, '三传': '；'.join(sanchuan), '月将': yuejiang, '旬空': xunkong}
    if m_nm: atts['年命'] = '本命' + m_nm.group(1)
    # 回源对勘：台账断语摘录（去标点后）须有连续 6 字窗口见于底本全文
    excerpt = (led['master_predictions'][0].get('statement_excerpt') or '')
    exn = re.sub(r'[^一-鿿A-Za-z0-9]', '', re.sub(r'^邵先生曰：', '', excerpt))
    bodyn = re.sub(r'[^一-鿿A-Za-z0-9]', '', raw)
    frag = next((exn[i:i+6] for i in range(len(exn)-5) if exn[i:i+6] in bodyn), '')
    assert frag, (cid, excerpt)
    da_parse[cid] = {'title': title, '三传': atts['三传'], '月将': yuejiang, '旬空': xunkong,
                     '年命': atts.get('年命'), '对勘断语片段': frag}
    strip_register[cid] = ['master_predictions（金标侧）','outcome（金标侧）','holdout_eligible',
                           '库存行无课式字段：课盘/三传/月将/旬空自 cases_raw 底本逐例补录']
    cards[cid] = {
        'id': cid,
        'subject': {'name_or_desc': led['subject']},
        'context': {'question': led['question_or_topic'], 'asked_at': led['asked_at'],
                    'setting': '原书课案（干支/月将/旬空见课盘原文）', 'attachments': atts},
        'provenance': {'book': '大六壬断案', 'edition': '缘生谛校注版（数字文本）',
                       'page': led['provenance'].get('page')},
        'language': 'zh-Hant'}
    golds[cid] = {
        'id': cid, 'tradition': '六壬', 'master': led['master'], 'source_work': led['source_work'],
        'subject': led['subject'], 'question_or_topic': led['question_or_topic'],
        'asked_at': led['asked_at'], 'context_at_prediction': led.get('context_at_prediction', ''),
        'chart_full': kepan, 'chart_complete': True,
        'master_predictions': led['master_predictions'], 'outcome': led['outcome'],
        'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': led.get('contamination_rationale'),
        'grade_note': led.get('grade_note'), 'provenance': led['provenance'],
        'transcription': led.get('transcription'), 'license_status': 'in-copyright',
        'redistributable': False}

# ---------- assertions ----------
order = ZC_SEL + BYZ_SEL + YXS_SEL + DA_SEL
assert len(order) == 40 and len(set(order)) == 40
assert set(cards) == set(order) and set(golds) == set(order)
for cid in order:
    g = golds[cid]
    assert g['outcome_grade'] == 'A-low' and g['contamination'] == 'low', cid
def scan_keys(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in BANNED: hits.append(path + '/' + k)
            hits += scan_keys(v, path + '/' + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj): hits += scan_keys(v, f'{path}[{i}]')
    return hits
for cid in order:
    hits = scan_keys(cards[cid])
    assert not hits, (cid, hits)

# ---------- 三键去重（对象＋时间＋事项） ----------
def card_triple(c):
    ctx = c.get('context', {})
    ch = (ctx.get('attachments', {}) or {}).get('character_written', '')
    return (norm(subj_text(c.get('subject'))), norm(ctx.get('asked_at')), norm(ctx.get('question')), norm(ch))
def gold_triple(g):
    return (norm(subj_text(g.get('subject'))), norm(g.get('asked_at')), norm(g.get('question_or_topic')), '')

ref_triples, ref_ids = {}, {}
def add_ref(src, cid, trip):
    ref_triples.setdefault(trip, []).append((src, cid)); ref_ids.setdefault(cid, []).append(src)
for fn in sorted(os.listdir(os.path.join(BASE, 'inputs-dev12'))):
    if fn.endswith('.json'):
        c = json.load(open(os.path.join(BASE, 'inputs-dev12', fn), encoding='utf-8'))
        if 'id' not in c: continue
        add_ref('dev12', c['id'], card_triple(c))
for fn in sorted(os.listdir(os.path.join(BASE, 'holdout15-inputs'))):
    if fn.endswith('.json'):
        c = json.load(open(os.path.join(BASE, 'holdout15-inputs', fn), encoding='utf-8'))
        add_ref('holdout15', c['id'], card_triple(c))
for hn in range(3, 15):
    for g in load_jsonl(os.path.join(BASE, f'holdout{hn}', 'test_gold.jsonl')):
        add_ref(f'holdout{hn}', g['id'], gold_triple(g))

sel_triples = {cid: card_triple(cards[cid]) for cid in order}
assert len(set(sel_triples.values())) == 40, 'selected within-set triple collision'
dedup_hits = []
for cid in order:
    t = sel_triples[cid]
    if t in ref_triples: dedup_hits.append((cid, ref_triples[t]))
    if cid in ref_ids: dedup_hits.append((cid, [('id-collision', ref_ids[cid])]))
assert not dedup_hits, dedup_hits
# 弱核对登记：同对象＋同事项（不论时间）亦应为零
ref_sq = {}
for t, owners in ref_triples.items(): ref_sq.setdefault((t[0], t[2]), []).append(owners)
weak = [(cid, ref_sq[(t[0], t[2])]) for cid, t in sel_triples.items() if (t[0], t[2]) in ref_sq and t[0] and t[2]]
assert not weak, weak

# ---------- write ----------
for cid in order:
    with open(os.path.join(IN_DIR, cid + '.json'), 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in order:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')
sha = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()

report = {'counts': {'测字': len(ZC_SEL), '辨疑': len(BYZ_SEL), '预测学': len(YXS_SEL), '断案': len(DA_SEL), 'total': 40},
          'gold_sha256': sha, 'dedup': {'ref_triples': len(ref_triples), 'hits': 0, 'weak_hits': 0},
          'da_parse': da_parse, 'strip_register': strip_register}
with open(os.path.join(BASE, 'runs/round40/build-holdout16/build-report-r40.json'), 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print('OK cards=40 gold=40 sha256=', sha)
print('dedup ref_triples=', len(ref_triples), 'hits=0 weak=0')
