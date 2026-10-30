#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R42 数据席 D4（续行）：裁定后定案构成下组建并封存 holdout18（测字15＋六壬15＝30）。

定案：runs/round42/data-verify/HOST-RULING-H18-COMPOSITION.md（Z_fresh＝15 → C＝15、L＝15、T＝30；
测字15全入封；六壬 DA5／BYZ5／粹言5，选例序写死）。口径：PREREG §4.3/§5、§1.2 转录规格 v1。
前席：build_holdout18_r42.py（D3，构成门登记版）与 scan_content_markers_r42.py（§5 标记集）已交付，
本脚本为唯一名续行脚本，不改前席脚本本体。只建卡与封存：不作断、不评分、不做 git 操作。
BYZ-018/019 建卡级材料由本席回原书页图（PDF58/59，200dpi 渲染）逐例制备（BYZ_PREP）；
CY 五例课盘列由本席回 render 页图逐字转录（CY_VISUAL）；CY-010 材料自 cases-munong.jsonl 台账行
＋页图转录制备（候选文件无行）。复原值逐项标来源、不冒充转录值。
输入卫生：六壬卡执行 §1.2 转录规格 v1 七项字段；残损自评只入封存日志与金标 grade_note，不入卡；
粹言四例（CY-034/040/047/061）候选行「三传.断语线索」子字段整项不入卡（第一道已拦截，见前席报告）。
第二道扫描：以 scan_content_markers_r42.py 对 30 卡全字段递归自校验，任一命中即中止不交付。
"""
import json, re, hashlib, os, sys, subprocess

BASE = os.path.expanduser('~/workspace/divination/benchmark/phase3')
R42 = os.path.join(BASE, 'runs/round42')
OUT_DIR = os.path.join(BASE, 'holdout18')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
SEAL_LOG = os.path.join(BASE, 'data/holdout18-seal-log.md')
sys.path.insert(0, R42)
from scan_content_markers_r42 import scan_content, scan_field_names  # PREREG §5

def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]

# ---------------- 门：例级零复用自行复核（已用并集 871） ----------------
HOLDOUT_GOLDS = [os.path.join(BASE, f'holdout{i}/test_gold.jsonl') for i in
                 (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)]
used_gold = set()
for p in HOLDOUT_GOLDS:
    for r in load_jsonl(p):
        used_gold.add(r['id'])
batches = json.load(open(os.path.join(R42, 'batches.json'), encoding='utf-8'))
used_dev = set()
for v in batches.values():
    used_dev.update(v)
used_union = used_gold | used_dev
assert len(used_gold) == 460 and len(used_dev) == 487 and len(used_union) == 871, \
    (len(used_gold), len(used_dev), len(used_union))

# ---------------- 选例（裁定写死） ----------------
ZC_SEL = ['ZC-139', 'ZC-143', 'ZC-144', 'ZC-145', 'ZC-146', 'ZC-149', 'ZC-150', 'ZC-154',
          'ZC-156', 'ZC-157', 'ZC-158', 'ZC-160', 'ZC-163', 'ZC-164', 'ZC-165']
DA_SEL = ['DA-134', 'DA-145', 'DA-152', 'DA-159', 'DA-167']
BYZ_SEL = ['BYZ-078', 'BYZ-107', 'BYZ-114', 'BYZ-018', 'BYZ-019']
CY_SEL = ['CY-034', 'CY-040', 'CY-047', 'CY-061', 'CY-010']
ORDER = ZC_SEL + DA_SEL + BYZ_SEL + CY_SEL
assert len(ORDER) == 30 and len(set(ORDER)) == 30
assert all(i not in used_union for i in ORDER), '选例与已用并集相交'

BANNED = {'grade_note', 'contamination', 'contamination_reason', 'contamination_rationale', 'outcome',
          'outcome_grade', 'master', 'master_predictions', 'seal_eligible', 'seal_fail_reasons',
          'holdout_eligible', 'review', 'method_hint', 'disposition', 'notes', 'extractor_verdict_tail'}

# ---------------- 材料源（显式路径） ----------------
zc_rows = {}
for p in ['runs/round41/data-verify/zc-candidates-r41.jsonl',
          'runs/round42/data-verify/zc-candidates-r42.jsonl']:
    for r in load_jsonl(os.path.join(BASE, p)):
        zc_rows[r['id']] = r
dabyz = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round41/data-verify/da-byz-candidates-r41.jsonl'))}
yxs = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round41/data-verify/yxs-candidates-r41.jsonl'))}
byz_stock = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'runs/round38/data-verify/bianyi-stock-r38.jsonl'))}
munong = {r['id']: r for r in load_jsonl(os.path.join(BASE, 'expansion12/liuren-cuiyan/cases-munong.jsonl'))}
da_led = {}
for p in ['expansion12/liuren-duanan/cases-a.jsonl', 'expansion12/liuren-duanan/cases-b.jsonl']:
    for r in load_jsonl(os.path.join(BASE, p)):
        da_led[r['id']] = r
raw_cases = {c['n']: c for c in json.load(open(os.path.join(BASE, 'expansion12/liuren-duanan/scratch-archive/cases_raw.json'), encoding='utf-8'))}

cards, golds = {}, {}
strip_register, grade_register, residual_register = {}, {}, {}

ZHI = '子丑寅卯辰巳午未申酉戌亥'
JI_GONG = {'甲': '寅', '乙': '辰', '丙': '巳', '丁': '未', '戊': '巳',
           '己': '未', '庚': '申', '辛': '戌', '壬': '亥', '癸': '丑'}

def zhi_add(z, n):
    return ZHI[(ZHI.index(z) + n) % 12]

def sike_from_candidate(ch_sike):
    """候选行四课 dict（一课→'上/下（注）'）→ 规格 v1 独立字段 dict（值取注前正文）。"""
    out = {}
    for k in ['一课', '二课', '三课', '四课']:
        out[k] = ch_sike[k].split('（')[0]
    return out

def sike_down_up(sike):
    """四课 dict → [(上,下)×4]。"""
    pairs = []
    for k in ['一课', '二课', '三课', '四课']:
        up, down = sike[k].split('/')
        pairs.append((up, down))
    return pairs

# ================= 测字 15 =================
ZC_ASKED = '原文未记'
ZC_OUTCOME_VERIFIED = '原书自载（辑录者周亮工汇编，转述来源见各条；断语与结局分载情况见 grade_note）'
ZC_CONT_RATIONALE = '冷门轶事：事主多未具名或仅称谓／姓氏，结局为局部个案事实，模型先验大概率不含（《字触》口径承 holdout16 金标体例；本例 low 判定逐例据见候选行 compliance.rationale）'
ZC_MASTER = {'ZC-139': '占者（佚名）', 'ZC-143': '索紞', 'ZC-144': '楊雄（自占）',
             'ZC-145': '郭瑀（自解）', 'ZC-146': '楊元慎', 'ZC-149': '解者（佚名）',
             'ZC-150': '夢中術士', 'ZC-154': '仙人（夢中點撥）', 'ZC-156': '其子（病中自解）',
             'ZC-157': '夢人（夢語）', 'ZC-158': '術士（佚名）', 'ZC-160': '占者（佚名）',
             'ZC-163': '道士（佚名）', 'ZC-164': '夢答（祈夢）', 'ZC-165': '金迥秀'}
ZC_ASSERT = {'ZC-139': ['松字十八公', '後十八年為公'],
             'ZC-143': ['此亡友也'],
             'ZC-144': ['吾其戮乎（車傍于斤、肉傍筋）'],
             'ZC-145': ['吾其死乎（龍飛在尸）'],
             'ZC-146': ['三公之兆（面斷）', '亡後得三公（槐字木傍鬼，私解）'],
             'ZC-149': ['門中側耳是聞字（指向聞喜）'],
             'ZC-150': ['一陽（冬至）', '三水（河清）'],
             'ZC-154': ['加田于牛之上（生字）、科名將發'],
             'ZC-156': ['魁字二十鬼、吾其休矣'],
             'ZC-157': ['更己酉、成進士'],
             'ZC-158': ['人傍木、休字（主罷）'],
             'ZC-160': ['皮傍石、破字（主家破）'],
             'ZC-163': ['困無多日（篾箍木為困、日落西山無多日）'],
             'ZC-164': ['上不成、下不成（編碼正解戊戌）'],
             'ZC-165': ['羹寒無火為美、天無二為人', '當有美人桑中之喜']}
ZC_OUTCOME_TRIM = {'ZC-139'}  # 结局原文含候选席编辑括注，描述取括注前正文、注旨并入 grade_note

for cid in ZC_SEL:
    c = zc_rows[cid]
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
    grade_note = c['compliance']['rationale']
    if cid == 'ZC-164':
        grade_note += ('；判级倚 ZC-153 先例：梦中答语为对所问（成否）的事前直接答语、误读与正解之差即断面本体'
                       '（承 HOST-RULING-ZC164 维持 A-low 与 HOST-RULING-H18-COMPOSITION 第四节：随新鲜 15 例全池入封）')
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
        'grade_note': grade_note,
        'provenance': {'work': '《字触》', 'edition': c['provenance'].get('edition'),
                       'page': c['provenance'].get('page')},
        'transcription': c.get('transcription'), 'license_status': 'public-domain', 'redistributable': False}
    grade_register[cid] = ('测字：断语/结局视觉转录（transcription=visual，置信 '
                           + str(c.get('transcription_confidence')) + '，据候选行）'
                           + ('；ZC-164 判级倚 ZC-153 先例（承主持两裁定，见金标 grade_note）' if cid == 'ZC-164' else ''))
    residual_register[cid] = '不适用（残损代码为六壬规格 v1 第 7 项）'

# ================= 断案 5（候选行课式已经 cases_raw 补录；本脚本复核＋规格 v1 结构化） =================
JIANG = set('贵蛇朱合勾青空常玄虎后阴')

def da_tianpan(chart_text, sike):
    """自断案课盘原文方阵位置解析天盘加临表（地盘支→天盘支＋天将），并以四课链与轮转一致性校验。"""
    segs = [s.strip() for s in chart_text.split('；') if s.strip()]
    assert len(segs) >= 6, segs
    toks = [s.split() for s in segs]
    top_j, top_z = toks[0][:4], toks[1][:4]
    left, right = [], []
    for si in (2, 3):
        lt, rt = toks[si][0], toks[si][1]
        assert len(lt) == 2 and len(rt) == 2, (si, lt, rt)
        left.append((lt[1], lt[0]))    # 天将+天盘
        right.append((rt[0], rt[1]))   # 天盘+天将
    bot_z, bot_j = toks[4][:4], toks[5][:4]
    pos = {}
    for z, zz, jj in zip(['巳', '午', '未', '申'], top_z, top_j):
        pos[z] = (zz, jj)
    for z, (zz, jj) in zip(['辰', '卯'], left):
        pos[z] = (zz, jj)
    for z, (zz, jj) in zip(['酉', '戌'], right):
        pos[z] = (zz, jj)
    for z, zz, jj in zip(['寅', '丑', '子', '亥'], bot_z, bot_j):
        pos[z] = (zz, jj)
    assert len(pos) == 12, pos
    offs = {(ZHI.index(v[0]) - ZHI.index(k)) % 12 for k, v in pos.items()}
    assert len(offs) == 1, ('天盘轮转不一致', offs)
    pairs = sike_down_up(sike)
    (u1, d1), (u2, d2), (u3, d3), (u4, d4) = pairs
    gan, zhi_ = d1, d3
    assert pos[JI_GONG[gan]][0] == u1 and pos[u1][0] == u2, ('干上链不合', cid_hint[0])
    assert pos[zhi_][0] == u3 and pos[u3][0] == u4, ('支上链不合', cid_hint[0])
    return {z: f"{pos[z][0]}（{pos[z][1]}）" for z in ZHI}, pos

da_verify = {}
cid_hint = ['']
for cid in DA_SEL:
    cid_hint[0] = cid
    c = dabyz[cid]
    n = int(cid.split('-')[1])
    raw = raw_cases[n]['raw']
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
        tk = cl.split()
        if len(tk) >= 3:
            a, b, cc = tk[-3], tk[-2], tk[-1].rstrip('◎⊙')
            if a in '父母官兄财子' and re.fullmatch(r'[甲乙丙丁戊己庚辛壬癸]?[子丑寅卯辰巳午未申酉戌亥]', b) and cc in JIANG:
                sanchuan.append(f"{a}{b}（{cc}）")
    assert len(sanchuan) == 3, (cid, sanchuan)
    assert '；'.join(sanchuan) == c['chart']['三传'], (cid, sanchuan, c['chart']['三传'])
    excerpt = (c['master_predictions'][0].get('statement_excerpt') or '')
    exn = re.sub(r'[^一-鿿A-Za-z0-9]', '', re.sub(r'^邵先生曰：', '', excerpt))
    bodyn = re.sub(r'[^一-鿿A-Za-z0-9]', '', raw)
    frag = next((exn[i:i + 6] for i in range(len(exn) - 5) if exn[i:i + 6] in bodyn), '')
    assert frag, (cid, excerpt)
    da_verify[cid] = {'三传复核': '合', '断语窗口': frag}

    ch = c['chart']
    sike = sike_from_candidate(ch['四课'])
    tp_table, tp_pos = da_tianpan(ch['课盘原文'], sike)
    nm_raw = ch.get('年命') or ''
    if '行人' in nm_raw:
        nm_gz, nm_note = nm_raw, '行人年命见底本标题句；占者本命底本未给'
        nm_zhi = re.search(r'命([子丑寅卯辰巳午未申酉戌亥])', nm_raw)
        nm_branch = nm_raw[nm_raw.index('命') - 1] if '命' in nm_raw else ''
        # 行人庚午命：取「午」
        m = re.search(r'([子丑寅卯辰巳午未申酉戌亥])命', nm_raw)
        nm_branch = m.group(1) if m else ''
    else:
        nm_gz, nm_note = nm_raw, '底本课首明载本命'
        m = re.search(r'本命[甲乙丙丁戊己庚辛壬癸]([子丑寅卯辰巳午未申酉戌亥])', nm_raw)
        nm_branch = m.group(1) if m else ''
    assert nm_branch, (cid, nm_raw)
    nm_up_z, nm_up_j = tp_pos[nm_branch]
    nm_group = {'年命干支': nm_gz + '（' + nm_note + '）',
                '行年干支': '底本未单列',
                '年命上神': f"{nm_up_z}（{nm_up_j}）（推定（据天盘）：年命支{nm_branch}宫天盘{nm_up_z}乘{nm_up_j}，据本卡天盘加临表）"}
    atts = {'课盘原文': ch['课盘原文'],
            '四课': sike,
            '天盘加临表': tp_table,
            '课名': '底本未载',
            '月将': ch['月将'] + '（底本课首明载）',
            '旬空': ch['旬空'] + '（底本课首明载）',
            '年命字段组': nm_group,
            '三传': ch['三传'],
            '三传定位状态': '明载（底本三传列逐字）',
            '字段来源登记': '课盘原文/四课/三传：底本转录（候选行已自 cases_raw 逐例补录，本席复核三传一致）；天盘加临表：自课盘原文方阵位置解析（经四课链与轮转一致性校验）；年命上神：推定（据天盘），链见年命字段组'}
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
    notes = c.get('notes') or []
    gn = c.get('grade_note_stock') or ''
    if notes:
        gn += ' 注记：' + '；'.join(notes)
    gn += f"；残损自评（规格 v1 第 7 项，只入本字段与封存日志）：{('R-KM、R-NM（占者本命未给）' if cid == 'DA-159' else 'R-KM')}。"
    golds[cid] = {
        'id': cid, 'tradition': '六壬', 'master': c['master'], 'source_work': c['source_work'],
        'subject': c['subject'], 'question_or_topic': c['question_or_topic'], 'asked_at': c['asked_at'],
        'context_at_prediction': c.get('context_at_prediction', ''),
        'chart_full': ch['课盘原文'], 'chart_complete': True,
        'master_predictions': c['master_predictions'], 'outcome': c['outcome'],
        'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': led.get('contamination_rationale'),
        'grade_note': gn,
        'provenance': c['provenance'], 'transcription': c.get('transcription'),
        'license_status': 'in-copyright', 'redistributable': False}
    grade_register[cid] = ('甲（底本全课式可直读；本脚本对 cases_raw 复核三传一致、断语窗口命中「' + frag + '」；'
                           '天盘加临表方阵解析经四课链校验合）')
    residual_register[cid] = ('R-KM（课名底本未载）；R-NM（占者本命未给、行人年命明载）' if cid == 'DA-159'
                              else 'R-KM（课名底本未载）')

# ================= 辨疑 5 =================
BYZ_RATIONALE = '清代地方个案，仅见于本书小众刻本，结局为局部事实，模型先验大概率不含；逐例回原书对勘。'
# BYZ-018/019 建卡级材料：本席回原书页图（书页46/47＝PDF58/59，pdftoppm 200dpi 渲染）逐例制备。
# 课式全式线性转录与候选三例同体例（天将行／三传栏／四课格）；正议/案验只入金标侧（见 BYZ_PREP_GOLD）。
BYZ_PREP = {
    'BYZ-018': {
        'chart_text': '课名：遥克弹射元胎课。干支：庚戌日申时（道光己酉年寅月）。课式全式线性转录（天将行／三传栏／四课格）：青勾合朱／申酉戌亥；财寅后、元贵后朱、空未、子蛇；官巳常、辰丑寅亥、白午、丑贵；禄申青、丑戌亥庚；盘下：巳辰卯寅／常元阴后。',
        'sike': {'一课': '亥/庚', '二课': '寅/亥', '三课': '丑/戌', '四课': '辰/丑'},
        'sanchuan': '财寅（后）；官巳（常）；禄申（青）', 'offset': 3,
        'jiang_by_zhi': {'申': '青', '酉': '勾', '戌': '合', '亥': '朱', '未': '空', '子': '蛇',
                         '午': '白', '丑': '贵', '巳': '常', '辰': '元', '卯': '阴', '寅': '后'},
        'keming': '遥克弹射元胎课', 'xunkong': '甲辰旬，寅卯空（据日干支推得，原书未单列）'},
    'BYZ-019': {
        'chart_text': '课名：遥克弹射元胎课。干支：壬申日戌时（道光庚戌年丑月）。课式全式线性转录（天将行／三传栏／四课格）：合勾青空／申酉戌亥；财巳贵、元空贵元、朱未、子白；父申合、寅亥巳寅、蛇午、丑常；兄亥空、亥申寅壬；盘下：巳辰卯寅／贵后阴元。',
        'sike': {'一课': '寅/壬', '二课': '巳/寅', '三课': '亥/申', '四课': '寅/亥'},
        'sanchuan': '财巳（贵）；父申（合）；兄亥（空）', 'offset': 3,
        'jiang_by_zhi': {'申': '合', '酉': '勾', '戌': '青', '亥': '空', '未': '朱', '子': '白',
                         '午': '蛇', '丑': '常', '巳': '贵', '辰': '后', '卯': '阴', '寅': '元'},
        'keming': '遥克弹射元胎课', 'xunkong': '甲子旬，戌亥空（据日干支推得，原书未单列）'},
}
BYZ_PREP_GOLD = {
    'BYZ-018': {
        'master_predictions': [{'statement_excerpt': '正议：问：支上贵人乘墓履狱，占官似不吉。曰：喜本命戊辰上见夜贵，乘丁冲墓，亥水太阳加日，末传青龙乘驿内战，乃出谷迁乔之象。但脱上逢脱，财交旬空，宦囊不免空涩耳。参议：问：亥水子孙剥官，奈何？曰：壬课占官以龙为主，不忌。问：庚日逢丁如何？曰：常占主有祸动，在任则为官星乘马，反主升迁。',
                                'direction': 'mixed',
                                'key_assertions': ['出谷迁乔之象（升迁）', '宦囊不免空涩', '在任逢丁反主升迁'],
                                'timing_claim': None}],
        'outcome_desc': '向来两袖清风，是岁大水，更加脱耗。至辛亥年春迁汉阳，数月又升司马',
        'outcome_original': '案验：向来两袖清风，是岁大水，更加脱耗。至辛亥年春迁汉阳，数月又升司马。',
        'grade_extra': '台账 outcome 为摘录（「是岁大水脱耗；至辛亥年春迁汉阳，数月又升司马」），金标从原页案验全文；正议内提及本命戊辰（金标侧载，题面未单列、卡内年命字段组如实标未单列）。'},
    'BYZ-019': {
        'master_predictions': [{'statement_excerpt': '正议：巳为双女，六合为媒，天空为奴婢，中路必有燕会婚姻事耽延。末传旬空，出旬必到。先锋河魁为鬼克日，亦有风波之惊。然传贵俱顺，此行无恙。但防仆妾别有不利耳。',
                                'direction': 'mixed',
                                'key_assertions': ['中路有婚姻事耽延', '出旬必到', '亦有风波之惊、此行无恙', '防仆妾别有不利'],
                                'timing_claim': '出旬必到'}],
        'outcome_desc': '此张仲远先生迎姐占也。果为甥娶妾，携与同行，以致耽延，亦见风波。出旬清吉。抵署数月后，甥亡妾寡，此戌为寡宿，后乘哭神故也',
        'outcome_original': '案验：此张仲远先生迎姐占也。果为甥娶妾，携与同行，以致耽延，亦见风波。出旬清吉。抵署数月后，甥亡妾寡，此戌为寡宿，后乘哭神故也。',
        'grade_extra': '台账 outcome 为摘录，金标从原页案验全文（含迎姐占的归属句与寡宿注）。'},
}
# 候选三例规格 v1 派生常量：四课格读（候选行课式原文四课格两行配对）、天盘轮转偏移、天将（自课式原文栏位读）
BYZ_DERIVED = {
    'BYZ-078': {'sike': {'一课': '子/壬', '二课': '丑/子', '三课': '亥/戌', '四课': '子/亥'}, 'offset': 1,
                'jiang_by_zhi': {'午': '蛇', '未': '朱', '申': '合', '酉': '勾', '巳': '贵', '戌': '青',
                                 '辰': '后', '亥': '空', '卯': '阴', '寅': '元', '丑': '常', '子': '白'},
                'ot': ''},
    'BYZ-107': {'sike': {'一课': '子/乙', '二课': '申/子', '三课': '酉/丑', '四课': '巳/酉（格读）'}, 'offset': 8,
                'jiang_by_zhi': {'丑': '蛇', '寅': '朱', '卯': '合', '辰': '勾', '子': '贵', '巳': '青',
                                 '亥': '后', '午': '空', '戌': '阴', '酉': '元', '申': '常', '未': '白'},
                'ot': 'R-OT（四课上神格读「巳」与天盘轮转推值「午」差一宫、月将推定值与占月常例不合：候选转录存疑两项照录登记，天盘表以干上/支上双证的轮转值为准）'},
    'BYZ-114': {'sike': {'一课': '申/乙', '二课': '子/申', '三课': '酉/巳', '四课': '丑/酉（格读）'}, 'offset': 4,
                'jiang_by_zhi': {'酉': '蛇', '戌': '朱', '亥': '合', '子': '勾', '申': '贵', '丑': '青',
                                 '未': '后', '寅': '空', '午': '阴', '巳': '元', '辰': '常', '卯': '白'},
                'ot': 'R-OT（四课上神格读「丑」与天盘轮转推值「寅」差一宫：候选转录存疑照录登记，天盘表以干上/支上双证的轮转值为准）'},
    'BYZ-018': {'sike': BYZ_PREP['BYZ-018']['sike'], 'offset': 3, 'jiang_by_zhi': BYZ_PREP['BYZ-018']['jiang_by_zhi'], 'ot': ''},
    'BYZ-019': {'sike': BYZ_PREP['BYZ-019']['sike'], 'offset': 3, 'jiang_by_zhi': BYZ_PREP['BYZ-019']['jiang_by_zhi'], 'ot': ''},
}

for cid in BYZ_SEL:
    dv = BYZ_DERIVED[cid]
    tp_table = {z: f"{zhi_add(z, dv['offset'])}（{dv['jiang_by_zhi'][zhi_add(z, dv['offset'])] }）" for z in ZHI}
    # 推定月将：占时宫天盘支（月将加时口径）
    if cid in BYZ_PREP:
        prep = BYZ_PREP[cid]
        stk = byz_stock[cid]
        chart_text, keming, sanchuan = prep['chart_text'], prep['keming'], prep['sanchuan']
        xunkong = prep['xunkong']
        subject, question, asked_at = stk['subject'], stk['subject'], stk['asked_at']
        page, edition = stk['provenance']['page'], stk['provenance']['edition']
        shi_zhi = asked_at[-2]
        strip_register[cid] = ['master_predictions（金标侧，本席自原页正议转录）', 'outcome/outcome_original（金标侧，本席自原页案验转录）',
                               '台账 outcome 摘录与 grade_note（席位元数据）', 'chart 课名字符串（台账仅存课名，已升全式转录）']
        grade_first = '甲（原页全式可直读，本席回原书页图逐例制备：题面/课式/正议/案验逐项对勘台账相符）'
    else:
        c = dabyz[cid]
        chart_text = c['chart']['课式原文']
        keming, sanchuan = c['chart']['课名'], c['chart']['三传']
        xunkong = c['chart']['旬空']
        subject, question, asked_at = c['subject'], c['question_or_topic'], c['asked_at']
        page, edition = c['provenance'].get('page'), c['provenance'].get('edition')
        shi_zhi = asked_at[-2]
        strip_register[cid] = ['master_predictions（金标侧）', 'outcome/outcome_original（金标侧）', 'grade_note_stock（金标侧）',
                               'outcome_grade_stock/compliance/dedup/grade/grade_evidence（席位元数据）', 'notes（席位元数据）',
                               'chart.月将/旬空（原书未单列、推得注记；规格 v1 下以推定值单列入卡并标来源）',
                               'chart.四课（候选行作「见课式原文四课格」，规格 v1 下以格读独立字段入卡）']
        grade_first = '甲（原页全式可直读，据候选行回原书对勘登记）'
    yuejiang_val = zhi_add(shi_zhi, dv['offset']) + '将'
    atts = {'课式原文': chart_text,
            '四课': dv['sike'],
            '天盘加临表': tp_table,
            '课名': keming,
            '月将': yuejiang_val + '（推定：原书未单列，据天盘轮转与占时以月将加时口径推得）',
            '旬空': xunkong,
            '年命字段组': {'年命干支': '底本未单列', '行年干支': '底本未单列',
                           '年命上神': '不可据（年命干支底本未单列，不臆补）'},
            '三传': sanchuan,
            '三传定位状态': '明载（三传栏逐字，栏列于课式原文）',
            '字段来源登记': '课式原文/课名/三传：底本转录；四课：自课式原文四课格配对格读；天盘加临表：结构化推定（天盘支据四课干上/支上轮转定偏移、天将据课式原文栏位逐宫读，天将与三传栏互证合）；月将/旬空：推定（原书未单列）',
            'chart_complete': True}
    cards[cid] = {
        'id': cid, 'tradition': '六壬',
        'subject': {'name_or_desc': subject},
        'context': {'question': question, 'asked_at': asked_at,
                    'setting': '原书占验课式（全式见附件）', 'attachments': atts},
        'provenance': {'book': '六壬辨疑', 'edition': edition, 'page': page},
        'language': 'zh-Hans'}
    if cid in BYZ_PREP:
        g = BYZ_PREP_GOLD[cid]
        stk = byz_stock[cid]
        grade_note = ('A-low：断验俱全可分离、断先于验。R42 回原书页图（' + page + '，200dpi 渲染直读）逐例对勘相符。'
                      + g['grade_extra']
                      + '；残损自评（规格 v1 第 7 项，只入本字段与封存日志）：R-NM、R-TP、R-YJ。')
        golds[cid] = {
            'id': cid, 'tradition': '六壬', 'master': '张官德（清）',
            'source_work': '《六壬辨疑》正文占验（毕法案录外卷一至五）',
            'subject': subject, 'question_or_topic': question, 'asked_at': asked_at,
            'context_at_prediction': '', 'chart_full': chart_text, 'chart_complete': True,
            'master_predictions': g['master_predictions'],
            'outcome': {'description': g['outcome_desc']},
            'outcome_original': g['outcome_original'],
            'outcome_grade': 'A-low', 'contamination': 'low', 'contamination_rationale': BYZ_RATIONALE,
            'grade_note': grade_note,
            'provenance': {'work': '《六壬辨疑》正文占验（毕法案录外卷一至五）', 'edition': edition, 'page': page},
            'transcription': 'visual', 'license_status': 'in-copyright', 'redistributable': False}
        grade_register[cid] = grade_first
    else:
        c = dabyz[cid]
        gn = c.get('grade_note_stock') or ''
        grade_note = (f"A-low：{gn}；断验俱全可分离、断先于验。R41 回原书对勘相符。"
                      if gn else "A-low：断验俱全可分离、断先于验（原书断语＋案验/验证）；R41 回原书对勘相符、课式自原页全式转录。")
        notes = c.get('notes') or []
        if notes:
            grade_note += ' 注记：' + '；'.join(notes)
        grade_note += '；残损自评（规格 v1 第 7 项，只入本字段与封存日志）：R-NM、R-TP、R-YJ' + ('、' + dv['ot'] if dv['ot'] else '') + '。'
        out_desc = c['outcome']['description']
        orig = (c.get('outcome_original') or '')
        if orig.startswith('案验：'):
            out_desc = orig[len('案验：'):]
        golds[cid] = {
            'id': cid, 'tradition': '六壬', 'master': c['master'], 'source_work': c['source_work'],
            'subject': c['subject'], 'question_or_topic': c['question_or_topic'], 'asked_at': c['asked_at'],
            'context_at_prediction': '', 'chart_full': chart_text, 'chart_complete': True,
            'master_predictions': c['master_predictions'], 'outcome': {'description': out_desc},
            'outcome_grade': 'A-low', 'contamination': 'low', 'contamination_rationale': BYZ_RATIONALE,
            'grade_note': grade_note,
            'provenance': {'work': c['provenance'].get('work'), 'edition': c['provenance'].get('edition'),
                           'page': c['provenance'].get('page')},
            'transcription': 'visual', 'license_status': 'in-copyright', 'redistributable': False}
        grade_register[cid] = grade_first
    residual_register[cid] = 'R-NM（年命未单列）、R-TP（天盘表为结构化推定）、R-YJ（月将/旬空推定）' + ('；' + dv['ot'] if dv['ot'] else '')

# ================= 粹言 5（课盘列回 render 页图逐字转录，本席 R42；承 h17 裁定二体例） =================
CY_VISUAL = {
    'CY-034': {'page_img': 'render/cy-p-162.png（卷六验十九叶，PDF p.162）',
               'columns': '子·亥·戌 ／ 戌·壬·未·申·酉·戌 ／ 子·丑·寅·巳·辰·卯·寅·丑 ／ 戌·午·巳·寅·子·亥',
               'sike_verified': '一课 戌/壬、二课 酉/戌、三课 丑/寅、四课 子/丑 四对之字俱见于刊印列，与复原互证全合',
               'grade': '甲', 'residual': '无未决项：课盘列全录、四课互证全合；原书体例无独立三传栏/天将列'},
    'CY-040': {'page_img': 'render/cy-p-163.png（卷六验廿二叶，PDF p.163）',
               'columns': '午·辰·寅 ／ 申·辛·午·申·戌 ／ 未·酉·卯·辰·寅·丑·子·亥 ／ 酉·申·巳（底行：亥）',
               'sike_verified': '一课 申/辛、二课 午/申、三课 酉/亥、四课 未/酉 四对之字俱见于刊印列，与复原互证全合',
               'grade': '甲', 'residual': '无未决项：课盘列全录、四课互证全合；原书体例无独立三传栏/天将列'},
    'CY-047': {'page_img': 'render/cy-p-165.png（卷六验廿五叶，PDF p.165）',
               'columns': '寅·申·寅 ／ 申·寅·巳·亥·丑 ／ 寅·申·亥·戌·寅·卯·辰 ／ 戌·酉·申（底行：未·午·巳）',
               'sike_verified': '二课 巳/亥、三课 申/寅、四课 寅/申 三对见于刊印列；一课 亥/戊 之戊字在刊印列中形近戌、未能确指，分位以复原互证定',
               'grade': '乙', 'residual': '未决一项：一课下神戊字形近戌未能确指（四课以常法复原为准）；课盘列余字已逐字转录。原书体例无独立三传栏/天将列'},
    'CY-061': {'page_img': 'render/cy-p-169.png（卷六验卅三叶，PDF p.169）',
               'columns': '寅·亥·申 ／ 辰·未·寅·丑·子·亥·戌 ／ 戌·寅·辰·巳·午·未·申 ／ 酉',
               'sike_verified': '一课 寅/戊 之寅、二课 亥/寅、三课 未/戌、四课 辰/未 见于刊印列；一课下神戊字形近戌、未能确指，分位以复原互证定',
               'grade': '乙', 'residual': '未决一项：一课下神戊字形近戌未能确指（四课以常法复原为准）；全书末叶仅上叶、本例完整在叶内。原书体例无独立三传栏/天将列'},
    'CY-010': {'page_img': 'render/cy-p-155.png（卷六验五叶，PDF p.155）',
               'columns': '子·巳·丑·寅·卯·辰 ／ 巳·子·午·巳 ／ 酉·辰·戌·酉·申·未 ／ 巳·戌·卯（盘列中段另见亥字两见、列位未能确指）',
               'sike_verified': '二课 寅/酉、三课 辰/亥、四课 酉/辰 之字见于刊印列；一课下神乙字未能在刊印列中确指，分位以复原互证定（乙亥日午时亥将常法复原：一课 酉/乙、二课 寅/酉、三课 辰/亥、四课 酉/辰）',
               'grade': '乙', 'residual': '未决两项：①一课下神乙字未能确指；②盘列中段亥字两见、列位未能确指。课盘列余字已逐字转录。原书体例无独立三传栏/天将列',
               'sike': {'一课': '酉/乙（辰寄）', '二课': '寅/酉', '三课': '辰/亥', '四课': '酉/辰'},
               'tp_str': '子上巳、丑上午、寅上未、卯上申、辰上酉、巳上戌、午上亥、未上子、申上丑、酉上寅、戌上卯、亥上辰',
               'tp_note': '亥将加午时',
               'xunkong': '申酉空', 'xunkong_note': '推定，底本例头未载、按日干支所属甲戌旬推定'},
}
CY_RES_BASE = 'R-KM（原书无课名）、R-NM（年命未载）、R-TP（天盘为复原值）、R-3C（无独立三传栏）、R-YJ（旬空推定；月将例头明载）'

for cid in CY_SEL:
    vis = CY_VISUAL[cid]
    if cid == 'CY-010':
        m = munong[cid]
        subject, question, asked_at = m['subject'], m['question_or_topic'], m['asked_at']
        例头 = asked_at
        sike = {k: v.split('（')[0] for k, v in vis['sike'].items()}
        tp_table = dict(p.split('上') for p in vis['tp_str'].split('、'))
        tp_note = vis['tp_note']
        yuejiang_val, yuejiang_src = '亥将', '底本例头明载'
        xunkong_val = vis['xunkong'] + '（' + vis['xunkong_note'] + '）'
        prov_page, prov_edition = m['provenance']['page'], m['provenance']['edition']
        strip_register[cid] = ['master_predictions（金标侧）', 'outcome（金标侧）',
                               'grade_note/contamination_rationale（金标侧）', 'holdout_eligible（席位元数据）',
                               '候选文件无行：建卡级材料由本席自 cases-munong.jsonl 台账行＋render 页图转录制备']
        gold_master, gold_source = m['master'], m['source_work']
        gold_preds, gold_outcome = m['master_predictions'], m['outcome']
        gold_rationale, gold_gn0 = m['contamination_rationale'], m['grade_note']
        transcription = m.get('transcription')
    else:
        c = yxs[cid]
        inp, gs = c['input_side'], c['gold_side']
        ch = inp['chart']
        subject, question, asked_at = inp['subject'], inp['question_or_topic'], inp['asked_at']
        例头 = ch['例头原文']
        sike = {}
        for k in ['一课', '二课', '三课', '四课']:
            sike[k] = ch['四课'][k].replace('／', '/').split('（')[0]
        tp_table = dict(p.split('上') for p in ch['天地盘']['天盘加临'].split('、'))
        tp_note = ch['天地盘']['value']
        yuejiang_val, yuejiang_src = ch['月将']['value'], ch['月将']['source']
        xunkong_val = ch['旬空']['value'] + '（来源：推定，' + ch['旬空']['source'] + '）'
        prov_page, prov_edition = inp['provenance']['page'], inp['provenance'].get('edition')
        strip_register[cid] = ['gold_side.master_predictions（金标侧）', 'gold_side.outcome（金标侧）',
                               'gold_side.grade_note/contamination_rationale（金标侧）',
                               'compliance/freshness_check/holdout_eligible_inventory（席位元数据）',
                               'input_side.chart.三传.断语线索（子字段整项不入卡，第一道已拦截、断语只入金标侧）',
                               'input_side.chart.四课.干上核对（席位校验元数据，涉断语内容不入卡）',
                               'input_side.课式成色/残损登记（席位元数据，成色结论已改按 R42 回源转录实况登记）']
        gold_master, gold_source = c['master'], c['source_work']
        gold_preds, gold_outcome = gs['master_predictions'], gs['outcome']
        gold_rationale, gold_gn0 = gs['contamination_rationale'], gs['grade_note']
        transcription = c.get('transcription')
    sike_str = '、'.join(f"{k} {v}" for k, v in sike.items())
    chart_text = (f"例头原文：{例头}。课盘列视觉逐字转录（{vis['page_img']}，列序自右至左、自上而下）：{vis['columns']}。"
                  f"四课（刊印列转录＋复原互证）：{vis['sike_verified']}；复原四课照录：一课 {sike['一课']}、二课 {sike['二课']}、三课 {sike['三课']}、四课 {sike['四课']}。"
                  f"成色：{vis['grade']}（{vis['residual']}）")
    atts = {'课盘原文': chart_text,
            '四课': sike,
            '天盘加临表': tp_table,
            '课名': '底本未载（原书无课名）',
            '月将': yuejiang_val + '（来源：' + yuejiang_src + '）',
            '旬空': xunkong_val,
            '年命字段组': {'年命干支': '底本未载', '行年干支': '底本未载',
                           '年命上神': '不可据（年命底本未载，不臆补）'},
            '三传': '底本课盘列未逐字转录，不臆补',
            '三传定位状态': '无独立三传栏',
            '字段来源登记': '课盘列：本席回 render 页图逐字转录；四课/天盘加临表：复原值（' + tp_note + '，按例头干支/月将/占时常法复原，非转录值，与刊印列互证）；原书无天将列，天盘加临表不带天将；月将/旬空来源见各字段',
            'chart_complete': vis['grade'] == '甲'}
    cards[cid] = {
        'id': cid, 'tradition': '六壬',
        'subject': {'name_or_desc': subject},
        'context': {'question': question, 'asked_at': asked_at,
                    'setting': '原书占验课式（课盘列见附件）', 'attachments': atts},
        'provenance': {'book': '六壬粹言', 'edition': prov_edition, 'page': prov_page},
        'language': 'zh-Hant'}
    res = CY_RES_BASE + ('；R-OT（一课下神干字形近未确指）' if cid in ('CY-047', 'CY-061', 'CY-010') else '')
    grade_note = gold_gn0 + f"；R42 回源页图逐字转录课盘列，成色{vis['grade']}：{vis['residual']}；残损自评（规格 v1 第 7 项，只入本字段与封存日志）：{res}。"
    golds[cid] = {
        'id': cid, 'tradition': '六壬', 'master': gold_master, 'source_work': gold_source,
        'subject': subject, 'question_or_topic': question, 'asked_at': asked_at,
        'context_at_prediction': '', 'chart_full': chart_text, 'chart_complete': vis['grade'] == '甲',
        'master_predictions': gold_preds, 'outcome': gold_outcome,
        'outcome_grade': 'A-low', 'contamination': 'low',
        'contamination_rationale': gold_rationale,
        'grade_note': grade_note,
        'provenance': {'work': gold_source, 'edition': prov_edition, 'page': prov_page},
        'transcription': transcription, 'license_status': 'in-copyright', 'redistributable': False}
    grade_register[cid] = vis['grade'] + f"（R42 回源页图转录：{vis['residual']}）"
    residual_register[cid] = res

# ================= 自校验 + §5 第二道扫描 =================
assert set(cards) == set(ORDER) and set(golds) == set(ORDER)
for cid in ORDER:
    g = golds[cid]
    assert g['outcome_grade'] == 'A-low' and g['contamination'] == 'low', cid
    for k in ['id', 'tradition', 'subject', 'context', 'provenance', 'language']:
        assert k in cards[cid] and cards[cid][k] not in (None, ''), (cid, k)
    for k in ['id', 'tradition', 'master', 'source_work', 'subject', 'question_or_topic', 'asked_at',
              'context_at_prediction', 'master_predictions', 'outcome', 'outcome_grade', 'contamination',
              'contamination_rationale', 'grade_note', 'provenance', 'transcription', 'license_status', 'redistributable']:
        assert k in g, (cid, k)
    if cards[cid]['tradition'] == '六壬':
        at = cards[cid]['context']['attachments']
        for k in ['四课', '天盘加临表', '课名', '月将', '旬空', '年命字段组', '三传', '三传定位状态']:
            assert k in at, (cid, k)
        assert ('课盘原文' in at) or ('课式原文' in at), cid
        assert set(at['四课']) == {'一课', '二课', '三课', '四课'}, cid
        assert len(at['天盘加临表']) == 12, cid

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

for cid in ORDER:
    hits = scan_keys(cards[cid])
    assert not hits, (cid, hits)

scan2 = {}
total_hits = 0
for cid in ORDER:
    ch_hits = [list(h) for h in scan_content(cards[cid])]
    fn_hits = [list(h) for h in scan_field_names(cards[cid])]
    scan2[cid] = {'content_hits': ch_hits, 'fieldname_hits': fn_hits}
    total_hits += len(ch_hits) + len(fn_hits)
assert total_hits == 0, {k: v for k, v in scan2.items() if v['content_hits'] or v['fieldname_hits']}

# 新制备材料第一道补扫（BYZ-018/019、CY-010 的入卡材料，制备期口径）
scan1_new = {}
for cid in ['BYZ-018', 'BYZ-019', 'CY-010']:
    obj = cards[cid]['context']['attachments']
    scan1_new[cid] = {'content_hits': [list(h) for h in scan_content(obj)],
                      'fieldname_hits': [list(h) for h in scan_field_names(obj)]}
    assert not scan1_new[cid]['content_hits'] and not scan1_new[cid]['fieldname_hits'], cid

# ================= 落盘 =================
for cid in ORDER:
    with open(os.path.join(IN_DIR, cid + '.json'), 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in ORDER:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')
read_cards = {cid: json.load(open(os.path.join(IN_DIR, cid + '.json'), encoding='utf-8')) for cid in ORDER}
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
assert {g['id'] for g in read_golds} == set(read_cards) == set(ORDER) and len(read_golds) == 30
sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
sha_sum = subprocess.run(['sha256sum', gold_path], capture_output=True, text=True).stdout.split()[0]
assert sha_lib == sha_sum, (sha_lib, sha_sum)

report = {'round': 'R42', 'seat': 'D4 build/seal (continuation after HOST-RULING-H18-COMPOSITION)',
          'composition': {'T': 30, '测字': ZC_SEL, '断案DA': DA_SEL, '辨疑BYZ': BYZ_SEL, '粹言CY': CY_SEL},
          'gate_recheck': {'holdout3_17_gold_ids': len(used_gold), 'dev9_ids': len(used_dev),
                           'union': len(used_union), 'selected_intersection_with_used_union': 0,
                           'all_A_low': True, 'all_low': True},
          'scan_stage1_candidate_prep': '承前席 build-holdout18-report.json（D3）：31 例已扫，CY-034/040/047/061 四例「三传.断语线索」子字段制备期拦截、整项不入卡；本席新制备三例补扫见 scan_stage1_new_prep',
          'scan_stage1_new_prep': scan1_new,
          'scan_stage2_card_selfcheck': {'method': 'scan_content_markers_r42.py 对 30 张输入卡全字段递归扫描（内容级＋字段名黑名单）',
                                         'per_id': scan2, 'total_hits': total_hits},
          'scan_stage3_host_verify': '主持验封道，非本席执行',
          'da_verify': da_verify,
          'grade_register': grade_register,
          'residual_register': residual_register,
          'strip_register': strip_register,
          'gold_sha256': sha_lib, 'gold_sha256_sha256sum': sha_sum, 'gold_sha256_double_read_match': True,
          'outputs_written': [f'holdout18/inputs/{cid}.json' for cid in ORDER] + ['holdout18/test_gold.jsonl',
                                                                                  'data/holdout18-seal-log.md',
                                                                                  'runs/round42/build-holdout18-report-r42b.json']}
with open(os.path.join(R42, 'build-holdout18-report-r42b.json'), 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

# ================= 封存日志（正式版，整体重写） =================
zc_ids = '、'.join(ZC_SEL)
da_ids = '、'.join(DA_SEL)
byz_ids = '、'.join(BYZ_SEL)
cy_ids = '、'.join(CY_SEL)
grade_lines = '\n'.join(f"- {cid}：{grade_register[cid]}｜残损：{residual_register[cid]}" for cid in ORDER)
seal = f"""# holdout18 封存日志（R42 数据席 D4 续行，2026-10-30）

**本集已建成、已封存（T＝30）。** 本文件整体重写前席 D3 的未封存登记：前席因构成门实核不过（测字新鲜可用 15＜派单构成所需 20）只登记未组集；其后主持落盘裁定 `runs/round42/data-verify/HOST-RULING-H18-COMPOSITION.md` 定案构成（分档基数取新鲜可用数 Z_fresh＝15，适用 PREREG §4.2 第二档 → C＝15、L＝15、T＝30），本席（D4）按裁定在 `runs/round42/` 内新写唯一名续行脚本 `build_holdout18_r42b.py`（不改前席脚本本体）重跑建卡与封存，本文件即本次裁定后重跑的正式封存日志。前席登记件（`runs/round42/build-holdout18-report.json`、`data/holdout18-seal-log.md` 旧版）所载缺口事实与第一道扫描结果仍为本轮证据链一环，不因本文件重写而消失（构建报告互相引用）。
执行口径：PREREG §4.3 建卡封存、§5 验封常例（三道扫描）、§1.2 转录规格 v1（本集为首个全规格验收集，只登记事实、不预设读数含义）；构成定案与 ZC-164 处置承 HOST-RULING-H18-COMPOSITION 第二至四节（PREREG §4.2 分档基数读法勘误并列登记：累计 Z＝35 与新鲜 Z_fresh＝15；勘误不动分档数值、双 50% 上限与零复用限度）。
产物：`holdout18/inputs/` 30 张输入卡；`holdout18/test_gold.jsonl` 30 行金标；构建报告 `runs/round42/build-holdout18-report-r42b.json`。本席只建卡与封存：不作断、不评分、未做 git 操作。
**金标 SHA-256：`{sha_lib}`**（构建脚本 hashlib 输出与封存后 `sha256sum holdout18/test_gold.jsonl` 实测双读一致）。
全集口径：30 例全 A-low、全 low 污染、例级零复用（本席自行复核：holdout3–17 金标 460＋dev9 487、并集 871，选例逐 id 零命中）。

## 一、构成表（裁定写死）

| 来源 | 例数 | 入选 id |
|---|---|---|
| 测字《字触》 | 15 | {zc_ids} |
| 六壬《大六壬断案》DA | 5 | {da_ids} |
| 六壬《六壬辨疑》BYZ | 5 | {byz_ids} |
| 六壬《六壬粹言》慕农 CY | 5 | {cy_ids} |
| 合计 | 30 | 测字 15＝50%（恰上限），六壬 15＝50%；六壬三源各 5（各 ≤ L 的 50%＋1 容差内） |

- 测字 15 例＝留库存 12（ZC-139/143/144/145/146/149/150/154/156/157/158/160，承 holdout17 封存日志 §五）＋本轮补核新增 3（ZC-163/164/165，承 ZC-RECHECK-R42），新鲜可用全池入封、无未选留存。题材：功名 4、生死 3、仕途 3、丧事 1、生死/仕途 1、遇合 1、家宅/灾祸 1（ZC-156 生死/六甲计入生死组旁注）。
- 六壬题材：断案 5 例五题材（求财／买卖经营／出行／行人／疾病）；辨疑 5 例五题材（雇工／失物／军事安危／年将／行人）；粹言 5 例五题材（音信／疾病／公讼／射覆／仕宦）。与 holdout16/17 对照：六壬三源配额由 DA7/BYZ7/CY6 改为 DA5/BYZ5/CY5，辨疑单源占比续降；卷五本轮不用、CY-011 不用（承裁定第三节）。验收结论只对「字触测字＋断案/辨疑/粹言六壬」两总体发言，不外推全体系（PREREG §4.2 限度四）。
- CZ-QX 护栏：本集测字段 n＝15，护栏线不变，n 差异与 SE 变化按 PREREG §3 预留条款登记为可比性限度，结算归验收定稿（本席不结算）。

## 二、逐例成色与残损自评（规格 v1 第 7 项；只入本日志与金标 grade_note，不入输入卡）

{grade_lines}

- ZC-164 逐例标注（承裁定第四节）：判级维持 A-low，倚 ZC-153 先例（梦中答语为对所问的事前直接答语、误读与正解之差即断面本体；承 HOST-RULING-ZC164 前裁不变）；HOST-RULING-ZC164 原「备选末位、非必需不入选」处置以可选池 27 为前提、前提不成立已失效，本例随新鲜 15 例全池入封。验收分段读数时如实登记该例在场，不隐藏、不单独剔除。
- 测字成色总登记：15 例断语/结局视觉转录，置信高 3（ZC-150/158/165）、中高 9（ZC-139/144/145/146/149/154/156/163/164）、中 3（ZC-143/157/160）。
- 断案 5 例全甲：候选行已逐例回 cases_raw 补录全课式，本脚本再复核——三传解析 5/5 与候选行一致、台账断语 6 字窗口 5/5 命中底本（逐例窗口见构建报告 da_verify）。
- 辨疑 5 例全甲（原页全式可直读）：BYZ-078/107/114 据候选行回原书对勘登记；BYZ-018/019 候选文件无行，由本席回原书页图（书页46/47＝PDF58/59，200dpi 渲染）逐例制备建卡级材料（全式线性转录与候选三例同体例），题面/课式与台账（bianyi-stock-r38）相符，正议/案验只入金标侧。BYZ-018/019 金标结局从原页案验全文（台账为摘录，差异见 §六）。
- 粹言 5 例：甲 2（CY-034/040）、乙 3（CY-047/061/010）。五例课盘列均由本席回 render 页图逐字转录（承 h17 裁定二体例）；CY-034/040 自候选行成色乙升甲（课盘列全录、四课互证全合，照 h17 粹言升甲先例）；CY-047/061/010 一课下神干字形近未确指、四课以常法复原为准（逐例未决项见上表）。CY-010 候选文件无行，材料自 cases-munong.jsonl 台账行＋render/cy-p-155.png 转录制备；该例与 CY-009 同在验五叶（本例为叶内第二例、例头「癸未二月乙亥日午时亥将」）。

## 三、转录规格 v1 执行登记（PREREG §1.2，六壬 15 例逐例）

- 七项字段逐卡在场（脚本断言全过）：课盘原文（辨疑/粹言作课式原文/课盘原文，含全式或课盘列转录）／四课独立字段（一课至四课分位 dict）／天盘加临表（12 宫 dict）／课名单列／月将、旬空单列／年命字段组（年命干支、行年干支、年命上神）／三传＋三传定位状态；残损登记字段为第 7 项，落本日志与金标 grade_note、不入卡（承规格原文）。
- 来源标注逐项落卡（字段来源登记）：断案天盘加临表自课盘原文方阵位置解析、经四课链与轮转一致性校验（推定链式校验合，非复原臆造）；断案年命上神标「推定（据天盘）」并给推定链；辨疑四课自课式原文四课格格读、天盘表为结构化推定（天盘支据四课轮转定偏移、天将据课式栏位逐宫读、与三传栏天将互证合）、月将/旬空标推定（原书未单列）、年命上神标「不可据」；粹言四课/天盘表为复原值（标常法复原来源、非转录值）、天将原书无列故加临表不带天将、年命上神标「不可据」；课名底本未载者标「底本未载」（断案 5、粹言 5），辨疑 5 例课名明载。复原值不冒充转录值，逐项已标。

## 四、剥离登记（输入卡卫生）

输入卡只含题面字段 {{id, tradition, subject, context, provenance, language}}；六壬 context 含规格 v1 结构化附件。金标侧字段一律未入卡，构建脚本以 BANNED 字段集全卡递归扫描零残留。逐例剥离项见构建报告 `runs/round42/build-holdout18-report-r42b.json` 之 strip_register（本日志不复制全表，登记位置在此）。同源归纳：
- 测字 15：gold_material.master_prediction、gold_material.outcome、compliance.*、dedup_key、transcription_confidence。
- 断案 5：master_predictions、outcome、grade_note_stock、outcome_grade_stock/compliance/dedup/grade/grade_evidence、notes、chart.四课说明/四课干支校验。
- 辨疑 5：master_predictions、outcome/outcome_original、grade_note_stock（候选三例）、台账摘录与 chart 课名单字符串（BYZ-018/019 制备例）；候选行 chart.四课「见课式原文四课格」与 chart.月将未单列形态经规格 v1 结构化后入卡（格读四课、推定月将/旬空均已标来源，见 §三）。
- 粹言 5：gold_side.master_predictions、gold_side.outcome、gold_side.grade_note/contamination_rationale、compliance/freshness_check/holdout_eligible_inventory、**input_side.chart.三传.断语线索子字段整项不入卡**（CY-034/040/047/061，制备期第一道已拦截、断语只入金标侧，承裁定第五节）、input_side.chart.四课.干上核对（涉断语内容的席位校验元数据）。

## 五、内容级断语扫描（PREREG §5）执行登记

- 第一道（候选材料制备期，前席 D3 已行）：对象 31 例，命中 4 例（CY-034/040/047/061 的「三传.断语线索」子字段，字段名＋内容各 1/例），处置＝整项不入卡（见 §四），明细在前席构建报告。本席新制备三例（BYZ-018/019、CY-010）入卡材料补行第一道同口径扫描：零命中（构建报告 scan_stage1_new_prep）。
- 第二道（建卡自校验，本席）：以 `scan_content_markers_r42.py` 对 30 张输入卡全字段递归扫描（内容级一级/二级标记＋字段名黑名单），**逐卡零命中、合计 0**（逐卡结果在构建报告 scan_stage2_card_selfcheck）。无命中、无退回重建、无剥离存证新增。
- 第三道（主持验封）：非本席执行；开跑验收前主持复扫为 §8 落点，本日志不冒充第三道结论。

## 六、异常与对勘处理登记

1. BYZ-018/019 结局：台账（bianyi-stock-r38）outcome 为摘录，金标从原页案验全文（BYZ-018 补「向来两袖清风」「更加」等原文；BYZ-019 补迎姐归属句与寡宿注），逐字以页图为准，台账摘录不作金标。
2. BYZ-107/114 转录存疑（R-OT）：候选行课式原文四课格读出的四课上神（107「巳」、114「丑」）与天盘轮转推值（午、寅）各差一宫；四课字段照格读入卡并标「（格读）」，天盘加临表以干上/支上双证的轮转值为准，存疑照录于金标 grade_note 与本日志 §二。BYZ-107 另有一项：月将推定值（戌将）与占月（巳月）常例月将不合，同源存疑、一并登记。
3. ZC-139 结局：候选行 outcome 含编辑括注（断结分载说明），金标 outcome.description 取括注前正文、注旨并入 grade_note（承 h17 ZC-159/162 体例）。
4. ZC asked_at 措辞：h17 测字卡 asked_at 含括注长文（内有断语/结局字样），与 §5 第二道零命中要求相冲突，本集统一作「原文未记」，金标同。此为措辞性偏差、已登记，不影响题面信息（三键以 subject/question/所测字为准）。
5. CY-040 课盘列底行「亥」字单列（四课三课下神亥已见于第三列末字，底行为盘阵底行字），转录照录登记。

## 七、与裁定/PREREG 规格的偏差

- 对裁定构成（T＝30）与 PREREG §4.3/§5/§1.2：除 §六.4 一项措辞性偏差外无偏差。构成、选例序、全 A-low、全 low、例级零复用、双 50% 上限、规格 v1 七项、第二道扫描零命中、金标 SHA 双读，均按写死口径执行毕。
- 金标只许评审角在平台全立后的验收轮开封（承 PREREG §4.3），本席未开封他途、未作任何断/评分。
"""
with open(SEAL_LOG, 'w', encoding='utf-8') as f:
    f.write(seal)
print('OK cards=30 gold=30 sha256=', sha_lib)
print('scan2 total hits:', total_hits)
print('da_verify=', json.dumps(da_verify, ensure_ascii=False))
