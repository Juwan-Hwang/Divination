#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R41 数据/组集席：组建并封存 holdout17（测字20＋断案7＋辨疑7＋粹言6＝40）。
口径：runs/round41/PREREG.md §4.2 主持执行口径（Z=32≥20 → T=40；六壬 DA7/BYZ7/YXS6）。
只建卡与封存：不作断、不评分。输入全部为显式路径，禁 rglob/通配遍历。
测字选例：题材分散（单例题材全入选、卷四幾部功名≤6），未选12例登记留库存。
粹言6例课盘列由本席回源页图视觉逐字转录（见 CY_VISUAL），复原值逐项标来源、不冒充转录值。
断案课式以候选行（已自 cases_raw 逐例补录）为准，本脚本再对 cases_raw 复核三传与断语窗口。
"""
import json, re, hashlib, os, sys

BASE = os.path.expanduser('~/workspace/divination/benchmark/phase3')
OUT_DIR = os.path.join(BASE, 'holdout17')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
SEAL_LOG = os.path.join(BASE, 'data/holdout17-seal-log.md')

# ---------------- 选例（写死） ----------------
ZC_NEW_SEL = ['ZC-134', 'ZC-135', 'ZC-136', 'ZC-137', 'ZC-138', 'ZC-140', 'ZC-141', 'ZC-142',
              'ZC-147', 'ZC-148', 'ZC-151', 'ZC-152', 'ZC-153', 'ZC-155', 'ZC-159', 'ZC-161', 'ZC-162']
ZC_INV_SEL = ['ZC-072', 'ZC-073', 'ZC-130']
ZC_SEL = ZC_NEW_SEL + ZC_INV_SEL  # 20
ZC_UNSOLD = ['ZC-139', 'ZC-143', 'ZC-144', 'ZC-145', 'ZC-146', 'ZC-149', 'ZC-150', 'ZC-154',
             'ZC-156', 'ZC-157', 'ZC-158', 'ZC-160']  # 12 留库存
DA_SEL = ['DA-032', 'DA-040', 'DA-052', 'DA-058', 'DA-109', 'DA-125', 'DA-128']
BYZ_SEL = ['BYZ-017', 'BYZ-023', 'BYZ-028', 'BYZ-032', 'BYZ-037', 'BYZ-046', 'BYZ-052']
CY_SEL = ['CY-009', 'CY-013', 'CY-017', 'CY-023', 'CY-027', 'CY-030']

BANNED = {'grade_note', 'contamination', 'contamination_reason', 'contamination_rationale', 'outcome',
          'outcome_grade', 'master', 'master_predictions', 'seal_eligible', 'seal_fail_reasons',
          'holdout_eligible', 'review', 'method_hint', 'disposition', 'notes', 'extractor_verdict_tail'}

def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

# ---------------- 材料源（显式路径） ----------------
zc_cand = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round41/data-verify/zc-candidates-r41.jsonl'))}
dabyz_cand = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round41/data-verify/da-byz-candidates-r41.jsonl'))}
cy_cand = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round41/data-verify/yxs-candidates-r41.jsonl'))}
zc_led = {}
for p in ['runs/round38/data-verify/zichu-cases-r38.jsonl',
          'runs/round39/data-verify/zichu-j3-cases-r39.jsonl']:
    for r in load_jsonl(os.path.join(BASE, p)):
        zc_led[r['id']] = r
da_led = {}
for p in ['expansion12/liuren-duanan/cases-a.jsonl', 'expansion12/liuren-duanan/cases-b.jsonl']:
    for r in load_jsonl(os.path.join(BASE, p)):
        da_led[r['id']] = r
raw_cases = {c['n']: c for c in json.load(open(os.path.join(BASE, 'expansion12/liuren-duanan/scratch-archive/cases_raw.json'), encoding='utf-8'))}

cards, golds = {}, {}
strip_register = {}
grade_register = {}

ZC_ASKED = '原文未记（条内年号干支见断语／结局字段者照录）'
ZC_OUTCOME_VERIFIED = '原书自载（辑录者周亮工汇编，转述来源见各条；断语与结局分载情况见 grade_note）'
ZC_CONT_RATIONALE = '冷门轶事：事主多未具名或仅称谓／姓氏，结局为局部个案事实，模型先验大概率不含（《字触》口径承 holdout16 金标体例；本例 low 判定逐例据见候选行 compliance.rationale）'

ZC_MASTER = {'ZC-134': '筮者（佚名）', 'ZC-135': '张宣（梦者自解）', 'ZC-136': '占者（佚名）',
             'ZC-137': '节推（问者自解）', 'ZC-138': '赵直', 'ZC-140': '李盛（自解）',
             'ZC-141': '索紞', 'ZC-142': '索紞', 'ZC-147': '李仙药', 'ZC-148': '占者（佚名）',
             'ZC-151': '占者（佚名）', 'ZC-152': '占者（佚名）', 'ZC-153': '占者（佚名）',
             'ZC-155': '圆者（佚名）', 'ZC-159': '占者（佚名）', 'ZC-161': '占者（佚名）',
             'ZC-162': '马守愚'}
ZC_ASSERT = {'ZC-134': ['忧狱讼', '杀妻者为冯昌'],
             'ZC-135': ['得临安县令', '任数月而去'],
             'ZC-136': ['前程止于考功'],
             'ZC-137': ['杀人者为周彪'],
             'ZC-138': ['寿不过四十八（叶字四十下八）'],
             'ZC-140': ['必有荣闰（暴富贵）'],
             'ZC-141': ['饱肉食'],
             'ZC-142': ['后三年必有大禍'],
             'ZC-147': ['牛将失'],
             'ZC-148': ['四举成名'],
             'ZC-151': ['弓舆一人得（中选）、同行不得'],
             'ZC-152': ['当为解元'],
             'ZC-153': ['解元为郑姓、名含莫言之义'],
             'ZC-155': ['女当出横山（适横山地方）'],
             'ZC-159': ['父母丧亡之变'],
             'ZC-161': ['有荣耀之光（登第）'],
             'ZC-162': ['问者为蔡姓', '少失父兄', '冶游耗尽家产']}
# ZC-162 结局原文含候选席编辑括注、ZC-159 结局含条文分载括注：描述取括注前正文，括注意旨并入 grade_note
ZC_OUTCOME_TRIM = {'ZC-162', 'ZC-159'}

# ---------------- 测字：新核 17 ----------------
for cid in ZC_NEW_SEL:
    c = zc_cand[cid]
    im, gm = c['input_material'], c['gold_material']
    strip_register[cid] = ['gold_material.master_prediction（金标侧）', 'gold_material.outcome（金标侧）',
                           'compliance.outcome_grade/contamination/rationale（金标侧）', 'dedup_key',
                           'transcription_confidence（席位元数据）']
    cards[cid] = {
        'id': cid, 'tradition': '测字',
        'subject': {'name_or_desc': im['subject']},
        'context': {'question': im['question'], 'asked_at': ZC_ASKED, 'setting': '《字触》辑录成例',
                    'attachments': {'character_written': im['character_or_omen']}},
        'provenance': {'book': c['provenance'].get('book'), 'edition': c['provenance'].get('edition'),
                       'page': c['provenance'].get('page')},
        'language': 'zh-Hant'}
    outcome_desc = gm['outcome']
    if cid in ZC_OUTCOME_TRIM:
        outcome_desc = outcome_desc.split('（')[0]
    src = c['provenance'].get('book', '') + ' ' + str(c['provenance'].get('page', '')).split('（')[0]
    golds[cid] = {
        'id': cid, 'tradition': '测字', 'master': ZC_MASTER[cid], 'source_work': '《字触》',
        'subject': {'name_or_desc': im['subject']},
        'question_or_topic': im['question'], 'asked_at': ZC_ASKED,
        'context_at_prediction': '《字触》辑录成例',
        'master_predictions': [{'master': ZC_MASTER[cid], 'tradition': 'cezi', 'date': '原文未记',
                                'statement_excerpt': gm['master_prediction'], 'source': src,
                                'key_assertions': ZC_ASSERT[cid]}],
        'outcome': {'description': outcome_desc, 'verified_by': ZC_OUTCOME_VERIFIED},
        'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': ZC_CONT_RATIONALE,
        'grade_note': c['compliance']['rationale'],
        'provenance': {'work': '《字触》', 'edition': c['provenance'].get('edition'),
                       'page': c['provenance'].get('page')},
        'transcription': c.get('transcription'), 'license_status': 'public-domain', 'redistributable': False}
    grade_register[cid] = '测字：断语/结局视觉转录（transcription=visual，置信 ' + str(c.get('transcription_confidence')) + '，据候选行）'

# ---------------- 测字：库存 3（承 holdout16 体例自台账建卡） ----------------
for cid in ZC_INV_SEL:
    led = zc_led[cid]
    ctx = led['context']; atts = ctx.get('attachments', {})
    strip_register[cid] = ['master_predictions（金标侧）', 'outcome（金标侧）', 'grade_note', 'contamination/contamination_reason',
                           'outcome_grade', 'holdout_eligible', 'notes', 'context.attachments.method_hint（空值）']
    cards[cid] = {
        'id': cid, 'tradition': '测字', 'subject': led['subject'],
        'context': {'question': ctx.get('question'), 'asked_at': ctx.get('asked_at'), 'setting': ctx.get('setting'),
                    'attachments': {'character_written': atts.get('character_written')}},
        'provenance': {'book': led['provenance'].get('book'), 'edition': led['provenance'].get('edition'),
                       'page': led['provenance'].get('page')},
        'language': led.get('language')}
    mp = led.get('master_predictions') or [{}]
    golds[cid] = {
        'id': cid, 'tradition': '测字', 'master': mp[0].get('master'), 'source_work': '《字触》',
        'subject': led['subject'], 'question_or_topic': ctx.get('question'), 'asked_at': ctx.get('asked_at'),
        'context_at_prediction': ctx.get('setting'), 'master_predictions': led['master_predictions'],
        'outcome': led['outcome'], 'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': led.get('contamination_reason'), 'grade_note': led.get('grade_note'),
        'provenance': {'work': '《字触》', 'edition': led['provenance'].get('edition'),
                       'page': led['provenance'].get('page')},
        'transcription': led['provenance'].get('transcription'),
        'license_status': led.get('license_status'), 'redistributable': led.get('redistributable')}
    grade_register[cid] = '测字：库存台账例（R38/R39 视觉转录），断验俱全'

# ---------------- 断案 7（候选行课式已经 cases_raw 补录；本脚本复核） ----------------
JIANG = set('贵蛇朱合勾青空常玄虎后阴')
da_verify = {}
for cid in DA_SEL:
    c = dabyz_cand[cid]
    n = int(cid.split('-')[1])
    raw = raw_cases[n]['raw']
    # 复核一：候选三传串须与底本三传列解析一致（h16 体例解析器）
    lines = raw.split('\n')
    tidx = next(i for i, l in enumerate(lines) if re.match(r'\s*\d+\.', l))
    chart_lines = []
    for l in lines[tidx + 1:]:
        if '邵先生曰' in l:
            break
        s = l.strip()
        if not s:
            continue
        if any(ch in l for ch in '。：，；、') or '谛' in l or '按' in l:
            continue
        if len(s) <= 60:
            chart_lines.append(' '.join(l.split()))
    assert len(chart_lines) >= 6, (cid, chart_lines)
    sanchuan = []
    for cl in chart_lines:
        toks = cl.split()
        if len(toks) >= 3:
            a, b, cc = toks[-3], toks[-2], toks[-1].rstrip('◎⊙')
            if a in '父母官兄财子' and re.fullmatch(r'[甲乙丙丁戊己庚辛壬癸]?[子丑寅卯辰巳午未申酉戌亥]', b) and cc in JIANG:
                sanchuan.append(f"{a}{b}（{cc}）")
    assert len(sanchuan) == 3, (cid, sanchuan)
    assert '；'.join(sanchuan) == c['chart']['三传'], (cid, sanchuan, c['chart']['三传'])
    # 复核二：台账断语 6 字窗口见于底本
    excerpt = (c['master_predictions'][0].get('statement_excerpt') or '')
    exn = re.sub(r'[^一-鿿A-Za-z0-9]', '', re.sub(r'^邵先生曰：', '', excerpt))
    bodyn = re.sub(r'[^一-鿿A-Za-z0-9]', '', raw)
    frag = next((exn[i:i + 6] for i in range(len(exn) - 5) if exn[i:i + 6] in bodyn), '')
    assert frag, (cid, excerpt)
    da_verify[cid] = {'三传复核': '合', '断语窗口': frag}
    ch = c['chart']
    atts = {'课盘原文': ch['课盘原文'],
            '四课': '；'.join(f"{k} {v}" for k, v in ch['四课'].items()),
            '三传': ch['三传'], '月将': ch['月将'], '旬空': ch['旬空']}
    if ch.get('年命'):
        atts['年命'] = ch['年命']
    strip_register[cid] = ['master_predictions（金标侧）', 'outcome（金标侧）', 'grade_note_stock（金标侧）',
                           'outcome_grade_stock/compliance/dedup/grade/grade_evidence（席位元数据）', 'notes（席位元数据）',
                           'chart.四课说明/四课干支校验（席位元数据）']
    cards[cid] = {
        'id': cid, 'tradition': '六壬',
        'subject': {'name_or_desc': c['subject']},
        'context': {'question': c['question_or_topic'], 'asked_at': c['asked_at'],
                    'setting': '原书课案（干支/月将/旬空见课盘原文）', 'attachments': atts},
        'provenance': {'book': '大六壬断案', 'edition': '缘生谛校注版（数字文本）',
                       'page': c['provenance'].get('page')},
        'language': 'zh-Hant'}
    led = da_led[cid]
    golds[cid] = {
        'id': cid, 'tradition': '六壬', 'master': c['master'], 'source_work': c['source_work'],
        'subject': c['subject'], 'question_or_topic': c['question_or_topic'], 'asked_at': c['asked_at'],
        'context_at_prediction': c.get('context_at_prediction', ''),
        'chart_full': ch['课盘原文'], 'chart_complete': True,
        'master_predictions': c['master_predictions'], 'outcome': c['outcome'],
        'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': led.get('contamination_rationale'),
        'grade_note': c.get('grade_note_stock'),
        'provenance': c['provenance'], 'transcription': c.get('transcription'),
        'license_status': 'in-copyright', 'redistributable': False}
    grade_register[cid] = '甲（底本全课式可直读；本脚本对 cases_raw 复核三传一致、断语窗口命中「' + frag + '」）'

# ---------------- 辨疑 7 ----------------
BYZ_RATIONALE = '清代地方个案，仅见于本书小众刻本，结局为局部事实，模型先验大概率不含；R41 回原书逐项核对。'
for cid in BYZ_SEL:
    c = dabyz_cand[cid]
    ch = c['chart']
    strip_register[cid] = ['master_predictions（金标侧）', 'outcome/outcome_original（金标侧）', 'grade_note_stock（金标侧）',
                           'outcome_grade_stock/compliance/dedup/grade/grade_evidence（席位元数据）', 'notes（席位元数据）',
                           'chart.月将/旬空（原书未单列、推得注记，不入卡）']
    cards[cid] = {
        'id': cid, 'tradition': '六壬',
        'subject': {'name_or_desc': c['subject']},
        'context': {'question': c['question_or_topic'], 'asked_at': c['asked_at'],
                    'setting': '原书占验课式（全式见附件）',
                    'attachments': {'课式原文': ch['课式原文'], 'chart_complete': True}},
        'provenance': {'book': '六壬辨疑', 'edition': c['provenance'].get('edition'),
                       'page': c['provenance'].get('page')},
        'language': 'zh-Hans'}
    out_desc = c['outcome']['description']
    orig = (c.get('outcome_original') or '')
    if orig.startswith('案验：'):
        out_desc = orig[len('案验：'):]
    gn = c.get('grade_note_stock') or ''
    grade_note = (f"A-low：{gn}；断验俱全可分离、断先于验。R41 回原书对勘相符。"
                  if gn else "A-low：断验俱全可分离、断先于验（原书断语＋案验/验证）；R41 回原书对勘相符、课式自原页全式转录。")
    notes = c.get('notes') or []
    if notes:
        grade_note += ' 注记：' + '；'.join(notes)
    golds[cid] = {
        'id': cid, 'tradition': '六壬', 'master': c['master'], 'source_work': c['source_work'],
        'subject': c['subject'], 'question_or_topic': c['question_or_topic'], 'asked_at': c['asked_at'],
        'context_at_prediction': '', 'chart_full': ch['课式原文'], 'chart_complete': True,
        'master_predictions': c['master_predictions'], 'outcome': {'description': out_desc},
        'outcome_grade': 'A-low', 'contamination': 'low', 'contamination_rationale': BYZ_RATIONALE,
        'grade_note': grade_note,
        'provenance': {'work': c['provenance'].get('work'), 'edition': c['provenance'].get('edition'),
                       'page': c['provenance'].get('page')},
        'transcription': 'visual', 'license_status': 'in-copyright', 'redistributable': False}
    grade_register[cid] = '甲（原页全式可直读，据候选行回源对勘登记）'

# ---------------- 粹言 6（课盘列视觉逐字转录，本席 R41 回源） ----------------
# 课盘列转录：自原书页图（expansion12/liuren-cuiyan/render/cy-p-*.png）逐字读列，列序自右至左、自上而下。
# 四课分位与候选行常法复原互证；天地盘加临/旬空为复原/推定值，逐项标来源，不冒充转录值。
CY_VISUAL = {
    'CY-009': {'page_img': 'render/cy-p-155.png（卷六验五叶，PDF p.155）',
               'columns': '子·乙·辰·己·午·未 ／ 酉·巳·丑 ／ 申·子·卯 ／ 丑·巳·寅 ／ 酉·丑·丑·子·亥·戌（底行：酉·申·未）',
               'sike_verified': '一课 子/乙、二课 申/子、三课 丑/巳、四课 酉/丑 四对俱见于刊印列，与复原互证全合',
               'grade': '甲', 'residual': '无未决项：课盘列全录、四课互证全合；原书体例无独立三传栏/天将列，三传字见盘列、断语线索照候选行登记'},
    'CY-013': {'page_img': 'render/cy-p-156.png（卷六验七叶，PDF p.156）',
               'columns': '未·庚·未·申·酉·戌 ／ 午·未·午 ／ 亥·子·巳 ／ 戌·亥·辰·卯·寅·丑（底行：子·亥）',
               'sike_verified': '一课 未/庚、二课 午/未、三课 亥/子、四课 戌/亥 四对俱见于刊印列，与复原互证全合',
               'grade': '甲', 'residual': '无未决项：课盘列全录、四课互证全合；原书体例无独立三传栏/天将列，同 CY-009 注'},
    'CY-017': {'page_img': 'render/cy-p-157.png（卷六验十叶，PDF p.157 下叶）',
               'columns': '辰·甲·戌·亥·子·丑 ／ 午·辰·酉 ／ 辰·寅·子·申 ／ 辰·午·申 ／ 巳·辰（底行：卯·寅）',
               'sike_verified': '一课 辰/甲、二课 午/辰、三课 寅/子、四课 辰/寅 四对俱见于刊印列，与复原互证全合',
               'grade': '甲', 'residual': '无未决项：课盘列全录、四课互证全合；原书体例无独立三传栏/天将列，同 CY-009 注'},
    'CY-023': {'page_img': 'render/cy-p-159.png（卷六验十三叶，PDF p.159 上叶第二例）',
               'columns': '寅·丁·卯·辰·巳·午 ／ 酉·寅·寅 ／ 子·巳·丑 ／ 未·子·子·亥·戌（底行：申·酉）',
               'sike_verified': '一课 寅/丁、二课 酉/寅、三课 子/巳、四课 未/子 四对俱见于刊印列，与复原互证全合',
               'grade': '甲', 'residual': '无未决项：课盘列全录、四课互证全合；原书体例无独立三传栏/天将列，同 CY-009 注'},
    'CY-027': {'page_img': 'render/cy-p-160.png（卷六验十五叶，PDF p.160 上叶第二例）',
               'columns': '丑·戊·辰·巳·午·未 ／ 酉·丑·卯 ／ 寅·戌·午 ／ 寅·午·丑·子·亥·戌（底行：酉）',
               'sike_verified': '一课 丑/戊、二课 酉/丑、四课 寅/午 三对见于刊印列；三课 午/戌 两字见于列（寅·戌·午列），分位以复原互证定',
               'grade': '甲', 'residual': '课盘列全录、四课字全合；三课午/戌在刊印列中上下读序与盘式分位以复原互证后定，已逐项标明'},
    'CY-030': {'page_img': 'render/cy-p-161.png（卷六验十七叶，PDF p.161）',
               'columns': '辰·甲（形近壬，存疑）·戌·亥·子·丑 ／ 午·辰·酉 ／ 辰·午·申 ／ 甲（形近壬，存疑）·午·未·午·巳·辰（底行：卯·寅）',
               'sike_verified': '三课 午/辰、四课 申/午 两对见于刊印列；一课 丑/壬、二课 卯/丑 两对分位未能在刊印列中确指',
               'grade': '乙', 'residual': '残损/未决三项：①验语尾字残（候选行已登记，结局仅「果」字起、到任日文残）；②一课（丑/壬）、二课（卯/丑）分位未能确指，干字形近「甲」待核；③课盘列余字已逐字转录、四课后两对可确指'},
}
for cid in CY_SEL:
    c = cy_cand[cid]
    inp, gs = c['input_side'], c['gold_side']
    ch = inp['chart']; vis = CY_VISUAL[cid]
    chart_text = (f"例头原文：{ch['例头原文']}。课盘列视觉逐字转录（{vis['page_img']}，列序自右至左、自上而下）：{vis['columns']}。"
                  f"四课（刊印列转录＋复原互证）：{vis['sike_verified']}；复原四课照候选行：一课 {ch['四课']['一课']}、二课 {ch['四课']['二课']}、三课 {ch['四课']['三课']}、四课 {ch['四课']['四课']}。"
                  f"天地盘加临（复原值，非转录）：{ch['天地盘']['天盘加临']}（{ch['天地盘']['value']}，来源：按例头干支/月将/占时常法复原）。"
                  f"月将：{ch['月将']['value']}（来源：底本例头明载）。旬空：{ch['旬空']['value']}（来源：推定，底本例头未载、按日干支所属旬推定）。"
                  f"三传：原书无独立三传栏，未逐字转录；断语线索：{ch['三传']['断语线索']}。成色：{vis['grade']}（{vis['residual']}）")
    strip_register[cid] = ['gold_side.master_predictions（金标侧）', 'gold_side.outcome（金标侧）',
                           'gold_side.grade_note/contamination_rationale（金标侧）',
                           'compliance/freshness_check/holdout_eligible_inventory（席位元数据）',
                           'input_side.课式成色/残损登记（席位元数据，成色结论已改按 R41 回源转录实况登记）']
    cards[cid] = {
        'id': cid, 'tradition': '六壬',
        'subject': {'name_or_desc': inp['subject']},
        'context': {'question': inp['question_or_topic'], 'asked_at': inp['asked_at'],
                    'setting': '原书占验课式（课盘列见附件）',
                    'attachments': {'课式原文': chart_text, 'chart_complete': vis['grade'] == '甲'}},
        'provenance': {'book': '六壬粹言', 'edition': inp['provenance'].get('edition'),
                       'page': inp['provenance'].get('page')},
        'language': 'zh-Hant'}
    golds[cid] = {
        'id': cid, 'tradition': '六壬', 'master': c['master'], 'source_work': c['source_work'],
        'subject': inp['subject'], 'question_or_topic': inp['question_or_topic'], 'asked_at': inp['asked_at'],
        'context_at_prediction': '', 'chart_full': chart_text, 'chart_complete': vis['grade'] == '甲',
        'master_predictions': gs['master_predictions'], 'outcome': gs['outcome'],
        'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': gs['contamination_rationale'],
        'grade_note': gs['grade_note'] + f"；R41 回源页图逐字转录课盘列，成色{vis['grade']}：{vis['residual']}",
        'provenance': {'work': inp['provenance'].get('work'), 'edition': inp['provenance'].get('edition'),
                       'page': inp['provenance'].get('page')},
        'transcription': 'visual', 'license_status': 'in-copyright', 'redistributable': False}
    grade_register[cid] = vis['grade'] + f"（R41 回源页图转录：{vis['residual']}）"

# ---------------- 自校验 ----------------
order = ZC_SEL + DA_SEL + BYZ_SEL + CY_SEL
assert len(order) == 40 and len(set(order)) == 40, order
assert set(cards) == set(order) and set(golds) == set(order)
for cid in order:
    g = golds[cid]
    assert g['outcome_grade'] == 'A-low' and g['contamination'] == 'low', cid
    for k in ['id', 'tradition', 'subject', 'context', 'provenance', 'language']:
        assert k in cards[cid] and cards[cid][k] not in (None, ''), (cid, k)
    for k in ['id', 'tradition', 'master', 'source_work', 'subject', 'question_or_topic', 'asked_at',
              'context_at_prediction', 'master_predictions', 'outcome', 'outcome_grade', 'contamination',
              'contamination_rationale', 'grade_note', 'provenance', 'transcription', 'license_status', 'redistributable']:
        assert k in g, (cid, k)

def scan_keys(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in BANNED:
                hits.append(path + '/' + k)
            hits += scan_keys(v, path + '/' + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_keys(v, f'{path}[{i}]')
    return hits

for cid in order:
    hits = scan_keys(cards[cid])
    assert not hits, (cid, hits)

# ---------------- 落盘 ----------------
for cid in order:
    with open(os.path.join(IN_DIR, cid + '.json'), 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in order:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')
# 回读校验：JSON 全合法、卡/金标 id 集一致
read_cards = {}
for cid in order:
    read_cards[cid] = json.load(open(os.path.join(IN_DIR, cid + '.json'), encoding='utf-8'))
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
assert {g['id'] for g in read_golds} == set(read_cards) == set(order) and len(read_golds) == 40
sha = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()

report = {'counts': {'测字': 20, '断案': 7, '辨疑': 7, '粹言': 6, 'total': 40},
          'ids': order, 'gold_sha256': sha, 'da_verify': da_verify,
          'grade_register': grade_register, 'strip_register': strip_register,
          'zc_unselected_inventory': ZC_UNSOLD}
with open(os.path.join(BASE, 'runs/round41/build-holdout17-report.json'), 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
print('OK cards=40 gold=40 sha256=', sha)
print('da_verify=', json.dumps(da_verify, ensure_ascii=False))
