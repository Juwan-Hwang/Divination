# -*- coding: utf-8 -*-
"""R93 holdout34 建卡·BY 族小席构建脚本（唯一名 build_by_h34_r93.py）。
构成（PREREG-ADDENDUM-r93 定版，precheck_h34_r93.py 台账复算续位）：
BY-047、BY-048、BY-049、BY-050、BY-051、BY-053（BY-052 资格断言未过，不在构成）。
体例照 holdout33 封存日志 §六：输入卡字段白名单与金标字段序同 h33；
BY 卡格式对 holdout33/inputs/BY-044.json 实读。
金标编例：断语＝正议全文（BY-050 正议问答属原断并入，照 BY-044 参议先例登记）；
结局＝案验正文（附议不入：BY-048、BY-050；无复玩文尾例）。
课盘与正议/案验全文回原书页图逐字复原：页图 runs/round93/lr-pages-h34-seat/
（by-192..196.png，本席通读＋课盘裁切放大复核 runs/round93/h34-by-crops-r93/）。
原书天将「元」＝玄武省字，照录并于方阵注标明（承 h33 注法）。"""
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

ORDER = ['BY-047', 'BY-048', 'BY-049', 'BY-050', 'BY-051', 'BY-053']
assert 'BY-052' not in ORDER

pool = json.load(open(R93 + '/h34-pool-dump-r93.json', encoding='utf-8'))
used = set(json.load(open(R93 + '/used-ids-r93.json', encoding='utf-8')))
assert len(used) == 1304

# ---------- 资格复核（逐例硬断言） ----------
for cid in ORDER:
    r = pool[cid]
    assert r.get('holdout_eligible') is True, cid
    assert r.get('contamination') == 'low', cid
    assert r.get('outcome_grade') in ('A', 'A-low'), cid
    assert r.get('master_predictions'), cid
    assert r.get('outcome', {}).get('description'), cid
    rv = r.get('review', {})
    assert rv.get('verdict') == 'seal', cid
    assert rv.get('grade_final') == 'A-low', cid
    assert rv.get('contamination_final') == 'low', cid
    assert cid not in used, cid

# ---------- 课盘与金标（回原书页图逐字复原） ----------
CHART = {
 'BY-047': {
  'ke_name': '课传俱贵干神归支',
  'tianpan': '未勾、申合、酉朱、戌蛇、午青、亥贵、巳空、子后、丑阴、寅元、卯常、辰白（地盘支→上神天将；原式方阵：勾合朱蛇／未申酉戌、青午・亥贵、空巳・子后、辰卯寅丑／白常元阴；元＝玄武，原书省字照录）',
  'sike': '酉（朱）未、未（勾）巳、亥（贵）酉、酉（朱）丁（四课格原式：上行酉未亥酉／下行未巳酉丁，天将朱勾贵朱）',
  'sanchuan': '财酉（朱）、官亥（贵）、子丑（阴）',
  'master_prediction': '课传五贵，而末传又是贵人本家，此例邵子名为遍地贵人，无所依倚之状。虽举荐者多，终属无益。况干神归支，正宜回家静守。',
  'outcome_record': '时省中多有挽留，决意归去。嗣后贼兵复至，官吏一空。',
  'chart_check': '合格：原书书p180（PDF p192，页图 by-192.png）课盘方阵／四课格／三传栏三件俱在，本席通读＋裁切放大复核（h34-by-crops-r93/crop-by047.png）逐字转录。',
  'tail_note': '文尾处置：正议／案验全文照录，无附议、复玩文尾。'},
 'BY-048': {
  'ke_name': '昼夜贵加三传递生',
  'tianpan': '卯贵、辰后、巳阴、午元、寅蛇、未常、丑朱、申白、酉空、戌青、亥勾、子合（地盘支→上神天将；原式方阵：贵后阴元／卯辰巳午、蛇寅・未常、朱丑・申白、子亥戌酉／合勾青空；元＝玄武，原书省字照录）',
  'sike': '未（常）酉、酉（空）亥、酉（空）亥、亥（勾）癸（四课格原式：上行未酉酉亥／下行酉亥亥癸，天将常空空勾）',
  'sanchuan': '鬼未（常）、财巳（阴）、子卯（贵）',
  'master_prediction': '凡幕贵加年命发用，占考得中，占仕升迁，如此课，巳加未年，乘丁驿二马入传，又得卯贵助之，必膺两贵保举，未土遥克发用，支神加干，未月定有好音到门。正时戌印乘龙，初传未绶乘常，俱得相气，亦荣升之象。',
  'outcome_record': '令似现任户部主事，六月来报，果升员外郎。',
  'chart_check': '合格：原书书p180（PDF p192，页图 by-192.png）课盘方阵／四课格／三传栏三件俱在，本席通读＋裁切放大复核（h34-by-crops-r93/crop-by048.png）逐字转录。四课二三两课同作酉（空）亥，原书格内照录。',
  'tail_note': '文尾处置：正议／案验全文照录；案验后附议（书p181页首「凡幕贵加年命为林下贵人……故以升官论」）为附议，不入断语。'},
 'BY-049': {
  'ke_name': '昼夜贵加',
  'tianpan': '卯朱、辰蛇、巳贵、午后、寅合、未阴、丑勾、申元、酉常、戌白、亥空、子青（地盘支→上神天将；原式方阵：朱蛇贵后／卯辰巳午、合寅・未阴、勾丑・申元、子亥戌酉／青空白常；元＝玄武，原书省字照录）',
  'sike': '卯（朱）巳、巳（贵）未、酉（常）亥、亥（空）癸（四课格原式：上行卯巳酉亥／下行巳未亥癸，天将朱贵常空）',
  'sanchuan': '财巳（贵）、子卯（朱）、鬼丑（勾）',
  'master_prediction': '勾陈克日，考必攻讦。然卯木子孙制鬼，攻之无嫌。正时贵德临支发用，中传幕贵助之，必得两贵提携。神将俱逆，先有所阻，后必有成。巳为四数，名数应在第四，本届岁考不济，巳年科考准进。',
  'outcome_record': '县考攻落，学院作主书考，名数、年分亦准。',
  'chart_check': '合格：原书书p181（PDF p193，页图 by-193.png）课盘方阵／四课格／三传栏三件俱在，本席通读＋裁切放大复核（h34-by-crops-r93/crop-by049.png）逐字转录。',
  'tail_note': '文尾处置：正议／案验全文照录，无附议、复玩文尾。'},
 'BY-050': {
  'ke_name': '昼夜贵加虚一待用',
  'tianpan': '卯勾、辰青、巳空、午白、寅合、未常、丑朱、申元、酉阴、戌后、亥贵、子蛇（地盘支→上神天将；原式方阵：勾青空白／卯辰巳午、合寅・未常、朱丑・申元、子亥戌酉／蛇贵后阴；元＝玄武，原书省字照录）',
  'sike': '丑（朱）卯、卯（勾）巳、卯（勾）巳、巳（空）丁（四课格原式：上行丑卯卯巳／下行卯巳巳丁，天将朱勾勾空）',
  'sanchuan': '子丑（朱）、官亥（贵）、财酉（阴）',
  'master_prediction': '问：课传五阴，昏迷之象？曰：三传逆朝于干，由暗投明也。初丑末酉，自衰传旺也。时逢日禄，命上长生，皆阳将也。辰命乘青龙作太阳临午，又日丽中天之象，未可昏迷论也。荆州分野在午，命坐生方，此去可以得志。问：贵人坐空受制，奈何？曰：初空末助，先虚后实，官星乘马，退则陷空受克，进则出空受生，且天空乘巳会卯，为铸印。支加干，印来就我，巳逢丁岁二马，又为马上佩印，三传从革，虚一待用，不惟差事无伤，并能补缺。问：补何缺？曰：下克上，必下署上职，初传逢空，出旬乃动。',
  'outcome_record': '丑月果以候补府署粮道，因差得缺，马上佩印也。时楚北未复，制军驻襄阳，着委员送印到荆，印来就我也。酉日接印，应巳酉丑局也。',
  'chart_check': '合格：原书书p181-182（PDF p193-194，页图 by-193.png／by-194.png）课盘方阵／四课格／三传栏三件俱在（课盘全在书p181），本席通读＋裁切放大复核（h34-by-crops-r93/crop-by050.png）逐字转录。四课二三两课同作卯（勾）巳（干上神与支同为巳），原书格内照录。',
  'tail_note': '文尾处置：断语＝正议全文（跨书p181-182，正议内「问／曰」问答属原断，照 BY-044 参议并入先例并载）；案验全文照录；案验后附议（「此课若泥类神……邵子所以贵心易也」）不入。'},
 'BY-051': {
  'ke_name': '贵人蹉跌所筮不入将逢内战',
  'tianpan': '酉勾、戌合、亥朱、子蛇、申青、丑贵、未空、寅后、卯阴、辰元、巳常、午白（地盘支→上神天将；原式方阵：勾合朱蛇／酉戌亥子、青申・丑贵、空未・寅后、午巳辰卯／白常元阴；元＝玄武，原书省字照录）',
  'sike': '子（蛇）申、申（青）辰、辰（元）子、子（蛇）庚（四课格原式：上行子申辰子／下行申辰子庚，天将蛇青元蛇）',
  'sanchuan': '父辰（元）、禄申（青）、子子（蛇）',
  'master_prediction': '昼贵坐夜方，夜贵坐昼方，名贵人蹉跌。如此课，丑加酉，未加卯是也。占事主参差不一，难与图成。禄空全脱，课传内战，丑命贵人乘丁加于岁墓死神之方，行年又逢夜贵加之，是身入夜台之兆也。两贵虽不入传，仍凭类神及年命上神之。',
  'outcome_record': '刘秀谷兄时在宜春城内领袖乡勇，相见莫逆，旋邀卜吉，佳城未就，遯以无病，捐馆后得一穴，家人不能用。',
  'chart_check': '合格：原书书p182（PDF p194，页图 by-194.png）课盘方阵／四课格／三传栏三件俱在，本席通读＋裁切放大复核（h34-by-crops-r93/crop-by051.png）逐字转录。',
  'tail_note': '文尾处置：正议／案验全文照录，无附议、复玩文尾。'},
 'BY-053': {
  'ke_name': '两贵受克干支受脱',
  'tianpan': '未蛇、申贵、酉后、戌阴、午朱、亥元、巳合、子常、丑白、寅空、卯青、辰勾（地盘支→上神天将；原式方阵：蛇贵后阴／未申酉戌、朱午・亥元、合巳・子常、辰卯寅丑／勾青空白；元＝玄武，原书省字照录）',
  'sike': '酉（后）未、未（蛇）巳、申（贵）午、午（朱）乙（四课格原式：上行酉未申午／下行未巳午乙，天将后蛇贵朱）',
  'sanchuan': '官申（贵）、财戌（阴）、父子（常）',
  'master_prediction': '未土财爻乘丁，似宜动谋，然蛇主惊恐，未生酉鬼，求财得祸，且两贵受克，贵人自有忧烦，何能为力？喜日上子孙制鬼，可免于难耳。',
  'outcome_record': '时郧县受荐未请，旋往河口邦办公局。八月土匪滋事，仍是逃难。幸依亲处，眷口得全耳。',
  'chart_check': '合格：原书书p184（PDF p196，页图 by-196.png）课盘方阵／四课格／三传栏三件俱在，本席通读＋裁切放大复核（h34-by-crops-r93/crop-by053.png）逐字转录。',
  'tail_note': '文尾处置：正议／案验全文照录，无附议、复玩文尾。'},
}
assert set(CHART) == set(ORDER)

# ---------- 建卡与金标 ----------
cards, golds = {}, {}
chart_check, tail_disposition = {}, {}
strip_register, field_mapping_notes = {}, {}

for cid in ORDER:
    r = pool[cid]
    d = CHART[cid]
    prov = (f"{r['provenance']['work']}（{r['provenance']['edition']}）·{r['provenance']['page']}"
            f"；底本为用户提供，redistributable=false")
    anchors = {'asked_at': r['asked_at'], '课名': d['ke_name'],
               '天盘': d['tianpan'], '四课': d['sike'], '三传': d['sanchuan'],
               '课盘原文来源': '原书页图课盘直录（本席读图通读、课盘裁切放大复核，页图存 runs/round93/lr-pages-h34-seat/、裁切件存 runs/round93/h34-by-crops-r93/）'}
    gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low、'
             '复核 verdict=seal；课式头四要素 present（R84 核查台账）；课盘与'
             '正议／案验全文经本席回原书页图逐字复原；池卡摘录为节录，不作金标准据；'
             + d['tail_note'] + r['grade_note'] + '；复核：' + r['review']['notes'])
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
    golds[cid] = {'id': cid, 'master_prediction': d['master_prediction'],
                  'outcome_record': d['outcome_record'],
                  'tradition': 'liuren', 'pollution': 'low',
                  'grade': r['outcome_grade'], 'grade_note': gnote,
                  'provenance': prov, 'license_status': LICENSE_ANCIENT,
                  'redistributable': False}
    chart_check[cid] = d['chart_check']
    tail_disposition[cid] = d['tail_note']
    strip_register[cid] = ['master/master_predictions/outcome/outcome_grade/contamination/'
                           'contamination_rationale/grade_note/holdout_eligible/review'
                           '（池卡管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject/question←池卡 subject/question_or_topic 逐字；'
                                'anchors←asked_at 逐字＋本席回原书页图复原课盘；'
                                'setting/provenance←池卡 provenance 组写')

for cid in ORDER:
    assert list(cards[cid].keys()) == INPUT_FIELDS, cid
    assert list(golds[cid].keys()) == GOLD_FIELDS, cid
    assert cards[cid]['redistributable'] is False and golds[cid]['redistributable'] is False
    assert golds[cid]['pollution'] == 'low'

# ---------- 落盘 ----------
for cid in ORDER:
    with open(f'{OUT}/inputs/{cid}.json', 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=1)
        f.write('\n')
lines = [json.dumps(golds[cid], ensure_ascii=False) for cid in ORDER]
with open(R93 + '/gold-frag-by-r93.jsonl', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

report = {
 'set': 'holdout34', 'round': 93, 'family': 'BY',
 'built_ids': ORDER,
 'stop_items': [],
 'chart_check': chart_check,
 'tail_disposition': tail_disposition,
 'field_mapping_notes': field_mapping_notes,
 'strip_register': strip_register,
 'notes': ['页图目录实存为 runs/round93/lr-pages-h34-seat/（派单所指 '
           'runs/round93/h34-precheck-extract-r93/lr-pages-h34-seat/ 不存在），本席复用实存目录页图 by-192..196.png。',
           'BY-052 不在构成内（资格断言未过，承派单与 precheck 复算），本席未建。'],
}
with open(R93 + '/build-frag-by-r93.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('built:', ORDER)
print('gold lines:', len(lines))
