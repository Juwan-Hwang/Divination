# -*- coding: utf-8 -*-
"""R93 holdout34 DA 族小席构建脚本（唯一名 build_da_h34_r93.py）。
构成：DA-075..DA-081（《大六壬断案》7 例，PREREG-ADDENDUM-r93.md 定版、续位经
precheck_h34_r93.py 复算）。体例照 holdout33 封存日志 §六与 seal_h33_r89.py 的
DA 字段映射：输入卡字段白名单 INPUT_FIELDS、金标字段序 GOLD_FIELDS。
课盘解析器已对 holdout33 已封 7 例（DA-066/067/068/070）逐字复现验证通过
（天盘／四课／三传与封存卡全等）；金标断语／结局由本脚本回 cases_raw.json
原式后正文程序化提取（邵先生曰段→应验段），编注（缘生谛注、爱函按）按
逐例 tail_note 登记剥离，断语／结局剥离后须为底本正文的子串（脚本硬断言）。"""
import json, os

B = '/home/hatch/workspace/divination/benchmark/phase3'
R93 = B + '/runs/round93'
OUT = B + '/holdout34'
os.makedirs(OUT + '/inputs', exist_ok=True)

INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status', 'anchors']
GOLD_FIELDS = ['id', 'master_prediction', 'outcome_record', 'tradition',
               'pollution', 'grade', 'grade_note', 'provenance',
               'license_status', 'redistributable']
LICENSE_ANCIENT = '古籍文本，内部研究用'

SEL = ['DA-075', 'DA-076', 'DA-077', 'DA-078', 'DA-079', 'DA-080', 'DA-081']
NUM = {cid: int(cid.split('-')[1]) for cid in SEL}

# 应验段起始标记（底本正文逐字）与逐例文尾处置登记
OUTCOME_MARK = {
 'DA-075': '徐辛亥赴任',
 'DA-076': '钱乃奉议郎',
 'DA-077': '时自二十三上',
 'DA-078': '陈生当年果不中',
 'DA-079': '后入试，果聚众相争',
 'DA-080': '徐于三月间',
 'DA-081': '何当年乳母死',
}
KE_NAME = {cid: '底本未载' for cid in SEL}
KE_NAME['DA-075'] = '乱首'
TAIL_NOTE = {
 'DA-075': '文尾处置：断语＝邵先生曰当面语＋退而告门人语＋门人问故三段全文照录'
           '（池卡 grade_note 登记断语本体为邵公退后告门人之语、与当面勉廉洁之语'
           '分离，本轮照「邵先生曰全文」口径整段收录三段）；应验段照录，应验末'
           '缘生谛注（申文、所持释义）不入；本案底本无爱函按段。'
           '课名「乱首」自断语原文「此课名乱首」。',
 'DA-076': '文尾处置：断语照录，断语末缘生谛注（及瓜释义）不入；应验照录，'
           '应验末缘生谛注（奉议郎、通判释义）与爱函按不入。'
           '断语首「无禄课」为格称、非「课名」明载，课名记底本未载。',
 'DA-077': '文尾处置：断语照录，断语末缘生谛注（守、监庙、药院释义）不入；'
           '应验照录，应验末缘生谛注（和剂局、乃岳释义）与爱函按不入。',
 'DA-078': '文尾处置：断语／应验全文照录，爱函按不入。'
           '断语中「铸印格」「贵人课」为格称、非「课名」明载，课名记底本未载。',
 'DA-079': '文尾处置：断语全文照录；应验照录，应验末缘生谛注（罢斥释义）与'
           '爱函按不入。断语首「上门乱首」为格称、非「课名」明载，课名记底本未载。',
 'DA-080': '文尾处置：断语照录，断语末缘生谛注（荣卫释义）不入；应验全文照录，'
           '爱函按不入。断语中「真闭口」为格称、非「课名」明载，课名记底本未载。',
 'DA-081': '文尾处置：断语／应验全文照录，爱函按不入。',
}

# ---------- 数据源 ----------
pool = json.load(open(R93 + '/h34-pool-dump-r93.json', encoding='utf-8'))
raw_by_n = {e['n']: e for e in json.load(open(
    B + '/expansion12/liuren-duanan/scratch-archive/cases_raw.json',
    encoding='utf-8'))}

# ---------- 资格复核 ----------
def qual(cid):
    r = pool.get(cid)
    if r is None:
        return False
    return (r.get('holdout_eligible') is True and r.get('contamination') == 'low'
            and r.get('outcome_grade') in ('A', 'A-low')
            and bool(r.get('master_predictions'))
            and bool(r.get('outcome', {}).get('description')))

# ---------- 式盘实载核（回 cases_raw 原式：方阵／四课格／三传栏三件） ----------
GEN = set('青勾合朱蛇贵后空虎常玄阴')
BR = set('子丑寅卯辰巳午未申酉戌亥')
KIN = set('财官父兄子')

def locate_chart(lines):
    for i in range(len(lines) - 5):
        t = lines[i].split()
        if len(t) == 4 and all(len(x) == 1 and x in GEN for x in t):
            t2 = lines[i + 1].split()
            if len(t2) >= 11 and all(x in BR for x in t2[0:4]) \
                    and all(x in GEN for x in t2[4:8]) and t2[8] in KIN:
                return i
    return None

def parse_chart(lines, s):
    """照 h33 转录法：天盘（方阵读序）／四课（列序）／三传（行序）。"""
    L = [lines[s + i].split() for i in range(6)]
    assert len(L[0]) == 4 and len(L[4]) == 4 and len(L[5]) == 4
    assert all(len(x) == 1 and x in BR for x in L[4])
    assert all(len(x) == 1 and x in GEN for x in L[5])
    assert len(L[2]) == 9 and len(L[3]) == 9
    assert len(L[2][0]) == 2 and len(L[2][1]) == 2
    assert len(L[3][0]) == 2 and len(L[3][1]) == 2
    top_g, top_b = L[0], L[1][0:4]
    sike_g, sc1 = L[1][4:8], L[1][8:11]
    l2g, l2b = L[2][0][0], L[2][0][1]
    r2b, r2g = L[2][1][0], L[2][1][1]
    l3g, l3b = L[3][0][0], L[3][0][1]
    r3b, r3g = L[3][1][0], L[3][1][1]
    upper, sc2 = L[2][2:6], L[2][6:9]
    lower, sc3 = L[3][2:6], L[3][6:9]
    assert all(len(x) == 1 and x in BR | set('甲乙丙丁戊己庚辛壬癸') for x in upper + lower)
    assert sc1[0] in KIN and sc2[0] in KIN and sc3[0] in KIN
    bot_b, bot_g = L[4], L[5]
    tianpan = '、'.join(
        [f'{top_b[i]}{top_g[i]}' for i in range(4)]
        + [f'{l2b}{l2g}', f'{r2b}{r2g}', f'{l3b}{l3g}', f'{r3b}{r3g}']
        + [f'{bot_b[i]}{bot_g[i]}' for i in range(3, -1, -1)])
    fang = (f"{''.join(top_g)}／{''.join(top_b)}、{l2g}{l2b}・{r2b}{r2g}、"
            f"{l3g}{l3b}・{r3b}{r3g}、{''.join(bot_b)}／{''.join(bot_g)}")
    tianpan += f'（地盘支→上神天将；原式方阵：{fang}）'
    sike = '、'.join(f'{upper[i]}（{sike_g[i]}）{lower[i]}' for i in range(4))
    sike += (f"（四课格原式：上行{''.join(upper)}／下行{''.join(lower)}，"
             f"天将{''.join(sike_g)}）")

    def sc(row):
        kin, sb, g = row
        mark = ''
        if '◎' in g:
            mark = '（原式旁标◎）'
            g = g.replace('◎', '')
        if '⊙' in g:
            mark = '（原式旁标⊙）'
            g = g.replace('⊙', '')
        assert len(g) == 1 and g in GEN, row
        return f'{kin}{sb}（{g}）{mark}'

    sanchuan = '、'.join([sc(sc1), sc(sc2), sc(sc3)])
    check = {'fangzhen': True, 'sike_grid': True, 'sanchuan_col': True,
             'chart_line_index': s,
             'detail': '方阵6行（天将顶行／支顶行／中二行左右将支／支底行／天将底行）、'
                       '四课格（天将行＋上行＋下行各4列）、三传栏3行（六亲＋干支＋天将）'
                       '经 token 模式断言俱在'}
    return tianpan, sike, sanchuan, check

def strip_note(seg):
    k = seg.find('缘生谛：')
    if k >= 0:
        assert seg[:k].endswith(('。', '也。', '矣。')), seg[:k]
        return seg[:k]
    return seg

def extract_gold(lines, s, cid):
    body = ''.join(l.strip() for l in lines[s + 6:])
    body = body.split('\x0c')[0].split('爱函按')[0]
    i = body.find('邵先生曰')
    j = body.find(OUTCOME_MARK[cid])
    assert i >= 0 and j > i, cid
    pred = strip_note(body[i:j])
    out = strip_note(body[j:])
    assert '缘生谛' not in pred and '爱函按' not in pred, cid
    assert '缘生谛' not in out and '爱函按' not in out, cid
    assert pred.startswith('邵先生曰：') and pred in body and out in body, cid
    return pred, out

# ---------- 逐例工序 ----------
cards, golds = {}, {}
stop_items, chart_check = [], {}
strip_register, field_mapping_notes = {}, {}

for cid in SEL:
    if not qual(cid):
        stop_items.append({'id': cid, 'reason': '资格复核不过（holdout_eligible/'
                           'contamination/grade/master_predictions/outcome 任一不合）'})
        continue
    e = raw_by_n.get(NUM[cid])
    if e is None:
        stop_items.append({'id': cid, 'reason': 'cases_raw.json 无此案号'})
        continue
    lines = e['raw'].split('\n')
    s = locate_chart(lines)
    if s is None:
        stop_items.append({'id': cid, 'reason': '式盘实载核不过：原式未检出方阵／'
                           '四课格／三传栏三件俱在的课盘块'})
        chart_check[cid] = {'fangzhen': False, 'sike_grid': False,
                            'sanchuan_col': False}
        continue
    try:
        tianpan, sike, sanchuan, chk = parse_chart(lines, s)
        pred, out = extract_gold(lines, s, cid)
    except AssertionError as ex:
        stop_items.append({'id': cid, 'reason': f'式盘/金标提取断言失败：{ex}'})
        chart_check[cid] = {'fangzhen': False, 'sike_grid': False,
                            'sanchuan_col': False}
        continue
    chart_check[cid] = chk
    r = pool[cid]
    assert r['asked_at'] in e['raw'], cid
    prov = (f"{r['provenance']['work']}（{r['provenance']['edition']}）·"
            f"{r['provenance']['page']}；底本为用户提供，redistributable=false")
    anchors = {'asked_at': r['asked_at'], '课名': KE_NAME[cid],
               '天盘': tianpan, '四课': sike, '三传': sanchuan,
               '课盘原文来源': '底本全文 cases_raw.json 原式照录（天盘方阵／四课格／三传栏）'}
    cards[cid] = {
        'id': cid, 'tradition': 'liuren',
        'subject': r['subject'],
        'context': r['context_at_prediction'] if r['context_at_prediction'] else
                   f"占验例（{r['source_work']}）；占时与课式载于 anchors",
        'question': r['question_or_topic'],
        'setting': f"{r['source_work']}（{r['master']}）；{r['provenance']['page']}",
        'provenance': prov,
        'redistributable': False,
        'license_status': LICENSE_ANCIENT,
        'anchors': anchors}
    gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low；'
             '课式头四要素 present（R84 核查台账）；课盘经本席回底本全文逐字复原；'
             '金标断语／结局回底本全文邵先生曰段与应验段逐字照录（池卡摘录为节录，'
             '不作金标准据）；' + TAIL_NOTE[cid] + r['grade_note'])
    golds[cid] = {'id': cid, 'master_prediction': pred,
                  'outcome_record': out,
                  'tradition': 'liuren', 'pollution': 'low',
                  'grade': r['outcome_grade'], 'grade_note': gnote,
                  'provenance': prov, 'license_status': LICENSE_ANCIENT,
                  'redistributable': False}
    strip_register[cid] = ['master/master_predictions/outcome/outcome_grade/contamination/'
                           'contamination_rationale/grade_note/holdout_eligible/transcription'
                           '（池卡管理与金标侧字段，不入输入卡）',
                           '金标侧剥离：缘生谛注、爱函按（编注与案验续释，不入断语/结局；'
                           '逐例处置见 grade_note 文尾处置）']
    field_mapping_notes[cid] = ('subject/question←池卡 subject/question_or_topic 逐字；'
                                'anchors.asked_at←池卡 asked_at 逐字（与底本式头核对相合）；'
                                'anchors.课名←' + KE_NAME[cid] +
                                ('（自断语原文「此课名乱首」）' if cid == 'DA-075'
                                 else '（底本无「课名」明载）') +
                                '；anchors 天盘/四课/三传←本席回底本全文 cases_raw.json '
                                '原式程序化转录（解析器对 holdout33 封存 DA 卡逐字复现验证）；'
                                'setting/provenance←池卡 provenance 组写；'
                                '金标 master_prediction/outcome_record←底本正文邵先生曰段/'
                                '应验段程序化提取，剥离后为底本正文子串（脚本断言）')

built = [cid for cid in SEL if cid in cards]
for cid in built:
    assert list(cards[cid].keys()) == INPUT_FIELDS, cid
    assert list(golds[cid].keys()) == GOLD_FIELDS, cid
    assert cards[cid]['redistributable'] is False
    assert golds[cid]['redistributable'] is False and golds[cid]['pollution'] == 'low'

# ---------- 落盘 ----------
for cid in built:
    with open(f'{OUT}/inputs/{cid}.json', 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=1)
        f.write('\n')
frag_path = R93 + '/gold-frag-da-r93.jsonl'
with open(frag_path, 'w', encoding='utf-8') as f:
    for cid in built:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')

report = {
 'set': 'holdout34', 'round': 93, 'family': 'DA（《大六壬断案》）',
 'built_ids': built,
 'stop_items': stop_items,
 'chart_check': chart_check,
 'field_mapping_notes': field_mapping_notes,
 'strip_register': strip_register,
 'gold_frag': 'runs/round93/gold-frag-da-r93.jsonl',
 'gold_frag_lines': len(built),
 'order': built,
}
report_path = R93 + '/build-frag-da-r93.json'
with open(report_path, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('built:', built)
print('stop_items:', stop_items)
print('gold frag lines:', len(built))
