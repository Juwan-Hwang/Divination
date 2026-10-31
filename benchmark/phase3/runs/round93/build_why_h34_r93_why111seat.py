# -*- coding: utf-8 -*-
"""R93 holdout34 WHY 族建卡（分族席 why111seat）：WHY-111/112/114/115。
体例照 holdout33 封存日志 §六与 runs/round89/seal_h33_r89.py WHY 段：
输入卡字段白名单与金标字段序照 h33；anchors 全列＝台账 input_fields.chart
全键逐字；断语回原书《六爻分类占验技法》〔判斷〕段逐字补录（繁体照录，
页图 runs/round93/why-pages-h34-seat/ 与 why-pages-h34-seat-b/ 通读＋
why-pages-h34-why111seat/ 裁切复核）；结局自台账 outcome_record 逐字照录
并与原书應驗情況逐例核对。只写本族产物：holdout34/inputs/<id>.json×4、
gold-frag-why-r93.jsonl、build-frag-why-r93.json。不写封存日志。"""
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
LICENSE_MODERN = '现代版权文本，内部研究用'
SEL = ['WHY-111', 'WHY-112', 'WHY-114', 'WHY-115']

why_by = {}
for fn in ('runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json',
           'runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json'):
    d = json.load(open(B + '/' + fn, encoding='utf-8'))
    for e in d['entries']:
        why_by[e['provisional_id']] = e

# ① 台账资格复核（逐例硬断言）
for cid in SEL:
    e = why_by.get(cid)
    assert e is not None, cid
    ch = e['input_fields']['chart']
    assert e.get('pollution') == 'low', cid
    assert e.get('anchor_presence') == 'present', cid
    assert not e.get('anchor_missing'), cid
    assert bool(e.get('outcome_record')), cid
    assert bool(ch.get('ben_gua')) and bool(ch.get('chart_lines_top_to_bottom')), cid

# ② 断语补录（回原书〔判斷〕段逐字，visual 转录；loc=印刷页位，
# extra=文尾/字形/核对登记，outcome_check=结局核对结论）
SUPP = {
 'WHY-111': {
  'loc': '印刷p194',
  'pages': '印刷p194（why-pages-h34-seat/crop-p194-right.png）',
  'mp': '〔判斷〕以世爻為用神。雖然日月不剋世爻，但世爻不得日月生扶為休囚。卦中元神妻財子水發動，但月建絕之，日辰沖之為日破，生用神的力量不大。妻財主呼吸、飲食，破而難生用神，所以不是哮喘就是飲食難以下咽。斷其原因，官鬼臨青龍，青龍乃是宴會、飲酒的信息，是因喝酒引發的疾病。另外妻財動化官鬼也是表示因飲食而得病。官鬼臨青龍，臨近應爻，應為他處，是別人家喝酒得的病。',
  'extra': '',
  'outcome_check': '相合'},
 'WHY-112': {
  'loc': '印刷p194-196',
  'pages': '印刷p194-196（why-pages-h34-seat/crop-p194-right.png、crop-p195-left.png、crop-p196-right.png；判斷段在p195，crop-p195-judge.png 复核）',
  'mp': '〔判斷〕不管是誰搖卦，最初的意念是由那個女的發出的，所以以子孫為用神。子孫申金月生日剋，力量相當。卦中忌神父母巳火獨發，其兒子的病不輕。此卦元神有二，一為兄弟丑土在三爻空亡，三爻為床，空不生用神，她的兒子睡覺不安穩。另一元神兄弟戌土在六爻月破，六爻為頭，臨朱雀，主胡言亂語，說明她兒子頭腦不清，胡言亂語。查其病因，二爻官鬼臨螣蛇，螣蛇主怪異，二爻宅，家宅不安之象。初爻父母巳火為忌神，臨勾陳動而化官鬼，父母主建築，勾陳主修繕，巳火對應於二〇〇一年辛巳，此年定是改造過房子。乃由風水變化引起的疾病。父母午火在四爻，世在五爻，故斷其房子，不是第四層就是第五層。動爻化出的寅木增強了忌神的力量，家裡應該還有老虎的工藝品。',
  'extra': '判斷段至「家裡應該還有老虎的工藝品。」止；其後陳先生核實安排敘述（p195左欄）非斷語，不入。',
  'outcome_check': '年份一處不合（原书應驗情況作「二〇〇一年搬到五層」，台账 outcome_record 作「2000年」），餘相合；结局仍按台账逐字照录，差异登记于此'},
 'WHY-114': {
  'loc': '印刷p198-199',
  'pages': '印刷p198-199（why-pages-h34-seat-b/p198.png、p199.png；p198左欄 crop-p198-left.png／crop-p198-farleft.png 复核，判斷尾跨頁至p199首欄）',
  'mp': '〔判斷〕以世爻為用神。世爻被日月剋傷，休囚無氣不吉。忌神臨六爻動而剋世，六爻為頭，臨白虎主血，離宮卦，為低血壓。另一忌神子孫丑土臨二爻剋用神，丑為財庫，才為屎尿，墓庫臨子孫為腸，生殖器，世臨朱雀主炎症，斷其有腸炎。又丑為肝在而爻剋世，有肝病：世爻臨水被剋，有肝腹水。二爻也主腿，臨青龍主痛，有腿痛的毛病。',
  'extra': '「才為屎尿」「丑為肝在而爻剋世」为原书字面，照录不改。判斷段跨印刷p198-199，中缝以p199首欄复核拼接。',
  'outcome_check': '相合'},
 'WHY-115': {
  'loc': '印刷p199-200',
  'pages': '印刷p199-200（why-pages-h34-seat-b/p199.png、p200.png；p199判斷欄 crop-p199-judge.png 复核）',
  'mp': '〔判斷〕卦中財動化退，初爻為心事，動而化出財爻，必是問錢財之事。其答道：她原來是商店的售貨員，因把東西賒給顧客，顧客不還錢，於是單位扣發她的工資來頂債。子孫持世，官鬼空亡入墓，乃是退休之象，斷其已經退休。答：已經退休。世爻子孫絕於日，又被父母子水動而剋傷，無力生財爻，斷單位扣了的工資很難要回來。父母子水動化回頭剋，月建又剋，六爻妻財戌土也動而來剋，剋多生少，陽主父，斷其父親已經不在人世。答：已經於一九八九年去世。我補充說一九八九年為己巳，為父母絕地之故。六爻戌土動而使世爻入墓，六爻為頭，入木為眩暈之象，世臨午火被日剋傷，火在四爻為心臟，臨蛇為心慌。二爻為元神，被日合住，不能生用，兄弟為木主風，二爻為腿，斷其腿部有風亂竄。答：本人有頭暈、高血壓、心慌、腿上有風竄來竄去。她又提出給她母親斷病。因剛才以父母子水為父看，卦中只有一個父母爻，故不可再用父母爻看其母。以六親轉換原理，我剋者為財看，子孫午火即可當做其母親。當場有人反對說，世爻和母親同是一爻，這不是亂倫嗎？難道她也是她父親的老婆？我說，世爻和轉換來的母親的爻位相同，正好說明她和她母親長得很像。此是斷病，不是斷婚姻，斷婚姻就不可這樣看了。問之，果然長得像母親。子孫午火受剋，斷其母有嚴重的心臟病。用神入墓於戌土，斷其母親曾於一九九四年甲戌住院。二爻兄弟寅木為元神，被日合住不能生用，斷其母腿已經變形，不能走路。一九九二年壬申，一九九三年癸酉，一九九四年甲戌，一九九五年乙亥，一九九六年丙子，皆對用神不利，所以斷其母親身體一年不如一年。答：所斷皆驗。',
  'extra': '原书無獨立應驗情況段，斷語與課堂核實對話交錯行文，判斷段全文照录（含答語）；「入木為眩暈之象」为原书字面，照录不改。台账 transcription_confidence=medium，本席视觉转录逐欄复核。',
  'outcome_check': '相合（台账 outcome_record 为原书判断段内对话核实摘录，逐项与原书核对相合）'},
}
assert set(SUPP) == set(SEL)

cards, golds = {}, {}
strip_register, field_mapping_notes = {}, {}
verbatim_pages = {}
for cid in SEL:
    e = why_by[cid]
    ch = e['input_fields']['chart']
    anch = {'asked_at': e['input_fields']['asked_at']}
    for k, v in ch.items():
        anch[k] = v
    cards[cid] = {
        'id': cid, 'tradition': 'liuyao',
        'subject': e['subject'] if e['subject'] else '求测者（台账 subject 为空、原书未具名）',
        'context': (f"{e['input_fields']['asked_at']}，{e['input_fields']['question']}"
                    f"；原书{e['source'].split('｜')[1]}"),
        'question': e['input_fields']['question'],
        'setting': '六爻分类占验技法（王虎应著）',
        'provenance': f"{e['source']}；底本为用户经学校图书馆提供之扫描本，redistributable=false",
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': anch}
    s = SUPP[cid]
    head = '断语台账原录为要旨摘录，本轮回原书《六爻分类占验技法》〔判斷〕段逐字补录全文'
    if cid == 'WHY-112':
        gnote = (f"A（主持口径）；{head}（{s['loc']}，扫描本 transcription=visual）；"
                 f"结局自台账 outcome_record 逐字照录，并与原书應驗情況核对：{s['outcome_check']}。"
                 + s['extra'])
    else:
        gnote = (f"A（主持口径）；{head}（{s['loc']}，扫描本 transcription=visual）；"
                 f"结局自台账 outcome_record 逐字照录，并与原书應驗情況核对{s['outcome_check']}。"
                 + (s['extra'] if s['extra'] else ''))
    golds[cid] = {'id': cid, 'master_prediction': s['mp'],
                  'outcome_record': e['outcome_record'],
                  'tradition': 'liuyao', 'pollution': 'low', 'grade': 'A',
                  'grade_note': gnote,
                  'provenance': e['source'], 'license_status': LICENSE_MODERN,
                  'redistributable': False}
    strip_register[cid] = ['master_prediction（台账原录为要旨摘录、回原书补录件）/outcome_record/'
                           'pollution_note/dedup_check/filters/grade_note（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('anchors←台账 input_fields.chart 全列逐字；'
                                'context←asked_at＋question＋原书章节定位组写；'
                                + ('subject←台账 subject 逐字' if e['subject'] else
                                   'subject 台账为空、原书未具名，组写'))
    verbatim_pages[cid] = s['pages']

for cid in SEL:
    assert list(cards[cid].keys()) == INPUT_FIELDS, cid
    assert list(golds[cid].keys()) == GOLD_FIELDS, cid
    assert cards[cid]['redistributable'] is False and golds[cid]['redistributable'] is False

for cid in SEL:
    with open(f'{OUT}/inputs/{cid}.json', 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=1)
        f.write('\n')
with open(R93 + '/gold-frag-why-r93.jsonl', 'w', encoding='utf-8') as f:
    for cid in SEL:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')

report = {
 'built_ids': SEL,
 'stop_items': [],
 'verbatim_pages': verbatim_pages,
 'field_mapping_notes': field_mapping_notes,
 'strip_register': strip_register,
 'notes': [
  'WHY-112 结局年份差异：原书應驗情況「二〇〇一年搬到五層」vs 台账 outcome_record「2000年」；金标结局按工序③台账逐字照录，差异已登记于该例 grade_note，主持封存时请裁是否订正台账。',
  'WHY-115 无独立應驗情況段，结局为判断段内对话核实摘录（台账原样）。',
  '资格复核：4/4 pollution=low、anchor_presence=present、anchor_missing 为假（台账作空串）、outcome_record 非空。'],
}
with open(R93 + '/build-frag-why-r93.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('built:', SEL)
