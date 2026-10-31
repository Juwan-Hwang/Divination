# -*- coding: utf-8 -*-
"""R93 holdout34 WHY 族小席构建脚本（唯一名 build_why_h34_r93.py）。
构成照 PREREG-ADDENDUM-r93.md：WHY-111、WHY-112、WHY-114、WHY-115。
体例照 holdout33 封存日志 §六（字段白名单/金标字段序/WHY 卡组写口径，
承 runs/round89/seal_h33_r89.py）；断语回原书《六爻分类占验技法》〔判斷〕段
逐字补录（页图 runs/round93/why-pages-h34-seat/ 与 why-pages-h34-seat-b/，
双页扫描本右半＝印刷2n-2、左半＝2n-1）；结局自台账 outcome_record 逐字照录
并与原书應驗情況逐例核对。产物：holdout34/inputs/<id>.json×4＋
runs/round93/gold-frag-why-r93.jsonl＋runs/round93/build-frag-why-r93.json。"""
import json, hashlib, os

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

# ---------- 台账 ----------
why_by = {}
for fn in ('runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json',
           'runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json'):
    d = json.load(open(B + '/' + fn, encoding='utf-8'))
    for e in d['entries']:
        why_by[e['provisional_id']] = e

# ---------- 资格复核（工序①） ----------
def why_qual(cid):
    e = why_by.get(cid)
    if e is None:
        return False
    ch = e['input_fields']['chart']
    return (e.get('pollution') == 'low' and e.get('anchor_presence') == 'present'
            and not e.get('anchor_missing') and bool(e.get('outcome_record'))
            and bool(ch.get('ben_gua')) and bool(ch.get('chart_lines_top_to_bottom')))

for cid in SEL:
    assert why_qual(cid), cid

# ---------- 断语补录（工序②；回原书〔判斷〕段逐字，visual 转录，繁体照录） ----------
SUPPLEMENT = {
 'WHY-111': {
  'pages': '印刷p194',
  'confidence': 'high',
  'master_prediction': '〔判斷〕以世爻為用神。雖然日月不剋世爻，但世爻不得日月生扶為休囚。卦中元神妻財子水發動，但月建絕之，日辰沖之為日破，生用神的力量不大。妻財主呼吸、飲食，破而難生用神，所以不是哮喘就是飲食難以下咽。斷其原因，官鬼臨青龍，青龍乃是宴會、飲酒的信息，是因喝酒引發的疾病。另外妻財動化官鬼也是表示因飲食而得病。臨近應爻，應為他處，是別人家喝酒得的病。',
  'extra': '',
  'outcome_check': '相合：原书應驗情況（一九九三年此人幫朋友蓋房，在朋友家因喝酒過度而引起肺部化膿，最後發展成哮喘病）与台账 outcome_record 逐字对应（简繁之别除外）。'},
 'WHY-112': {
  'pages': '印刷p194–196',
  'confidence': 'high',
  'master_prediction': '〔判斷〕不管是誰搖卦，最初的意念是由那個女的發出的，所以以子孫為用神。子孫申金月生日剋，力量相當。卦中忌神父母巳火獨發，其兒子的病不輕。此卦元神有二，一為兄弟丑土在三爻空亡，三爻為床，空不生用神，她的兒子睡覺不安穩。另一元神兄弟戌土在六爻月破，六爻為頭，臨朱雀，主胡言亂語，說明她兒子頭腦不清，胡言亂語。查其病因，二爻官鬼臨螣蛇，螣蛇主怪異，二爻宅，家宅不安之象。初爻父母巳火為忌神，臨勾陳動而化官鬼，父母主建築，勾陳主修繕，巳火對應於二〇〇一年辛巳，此年定是改造過房子。乃由風水變化引起的疾病。父母午火在四爻，世在五爻，故斷其房子，不是第四層就是第五層。動爻化出的寅木增強了忌神的力量，家裡應該還有老虎的工藝品。陳先生並不知道此女的實際情況，但有一點可以肯定，他今年為此女兒子工作調動調風水時，曾讓她家放了一個老虎的工藝品，於是要求化解。我說你和她核實完我斷的結果看與她家相符與否？然後再化解。',
  'extra': '判斷段末核實前敘事段（「陳先生並不知道此女的實際情況……然後再化解」）位于〔判斷〕標題下、〔應驗情況〕標題前，與判斷同段連寫，整段照錄。',
  'outcome_check': '一处字面差异登记：台账 outcome_record 作「2000年搬到五层」，原书應驗情況（印刷p196）作「二〇〇一年搬到五層」；结局照台账逐字照录不改，余文（整修、今年卯月發瘋、自言自語、神仙下凡、調理而愈）逐字对应。'},
 'WHY-114': {
  'pages': '印刷p198–199',
  'confidence': 'medium-high',
  'master_prediction': '〔判斷〕以世爻為用神。世爻被日月剋傷，休囚無氣不吉。忌神臨六爻動而剋世，六爻為頭，臨白虎主血，離宮卦，為低血壓。另一忌神子孫丑土臨二爻剋用神，丑為財庫，才為屎尿，墓庫臨子孫為腸，生殖器，世臨朱雀主炎症，斷其有腸炎。又丑為肝在而爻剋世，有肝病：世爻臨水被剋，有肝腹水。二爻也主腿，臨青龍主痛，有腿痛的毛病。',
  'extra': '判斷跨印刷p198 三欄＋p199 首欄，經中縫帶放大裁切逐欄復核拼接（頁圖 why-pages-h34-seat-b/zoom-114-*）；「才為屎尿，墓庫臨子孫為腸」與「在而爻」均為原書字面，照錄不改並登記。',
  'outcome_check': '相合：原书應驗情況（所斷疾病皆驗，她說肝腹水已經好了。其他病還沒治好）与台账 outcome_record 逐字对应（简繁之别除外）。'},
 'WHY-115': {
  'pages': '印刷p199–200',
  'confidence': 'high',
  'master_prediction': '〔判斷〕卦中財動化退，初爻為心事，動而化出財爻，必是問錢財之事。其答道：她原來是商店的售貨員，因把東西賒給顧客，顧客不還錢，於是單位扣發她的工資來頂債。子孫持世，官鬼空亡入墓，乃是退休之象，斷其已經退休。答：已經退休。世爻子孫絕於日，又被父母子水動而剋傷，無力生財爻，斷單位扣了的工資很難要回來。父母子水動化回頭剋，月建又剋，六爻妻財戌土也動而來剋，剋多生少，陽主父，斷其父親已經不在人世。答：已經於一九八九年去世。我補充說一九八九年為己巳，為父母絕地之故。六爻戌土動而使世爻入墓，六爻為頭，入墓為眩暈之象，世臨午火被日剋傷，火在四爻為心臟，臨蛇為心慌。二爻為元神，被日合住，不能生用，兄弟為木主風，二爻為腿，斷其腿部有風亂竄。答：本人有頭暈、高血壓、心慌、腿上有風竄來竄去。她又提出給她母親斷病。因剛才以父母子水為父看，卦中只有一個父母爻，故不可再用父母爻看其母。以六親轉換原理，我剋者為財看，子孫午火即可當做其母親。當場有人反對說，世爻和母親同是一爻，這不是亂倫嗎？難道她也是她父親的老婆？我說，世爻和轉換來的母親的爻位相同，正好說明她和她母親長得很像。此是斷病，不是斷婚姻，斷婚姻就不可這樣看了。問之，果然長得像母親。子孫午火受剋，斷其母有嚴重的心臟病。用神入墓於戌土，斷其母親曾於一九九四年甲戌住院。二爻兄弟寅木為元神，被日合住不能生用，斷其母腿已經變形，不能走路。一九九二年壬申，一九九三年癸酉，一九九四年甲戌，一九九五年乙亥，一九九六年丙子，皆對用神不利，所以斷其母親身體一年不如一年。答：所斷皆驗。',
  'extra': '本例原书无獨立〔應驗情況〕段，核實以對話（答：…）交錯于〔判斷〕內，整段照錄；台账 outcome_record 為對話摘錄編合，结局照台账逐字照录，与原书判斷內答語逐項相合（退休／父一九八九年去世／母一年不如一年／本人頭暈高血壓心慌腿風竄）。',
  'outcome_check': '相合（口径见 extra：无獨立應驗段，以判斷內答語逐項核对）。'},
}
assert set(SUPPLEMENT) == set(SEL)

# ---------- 建卡与金标 ----------
cards, golds = {}, {}
strip_register, field_mapping_notes = {}, {}
verbatim_pages, outcome_checks = {}, {}

for cid in SEL:
    e = why_by[cid]
    s = SUPPLEMENT[cid]
    ch = e['input_fields']['chart']
    anch = {'asked_at': e['input_fields']['asked_at']}
    for k, v in ch.items():
        anch[k] = v
    subj = e['subject'] if e.get('subject') else '求测者（台账 subject 为空、原书未具名）'
    cards[cid] = {
        'id': cid, 'tradition': 'liuyao',
        'subject': subj,
        'context': (f"{e['input_fields']['asked_at']}，{e['input_fields']['question']}"
                    f"；原书{e['source'].split('｜')[1]}"),
        'question': e['input_fields']['question'],
        'setting': '六爻分类占验技法（王虎应著）',
        'provenance': f"{e['source']}；底本为用户经学校图书馆提供之扫描本，redistributable=false",
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': anch}
    gnote = (f"A（主持口径）；断语台账原录为要旨摘录，本轮回原书《六爻分类占验技法》"
             f"〔判斷〕段逐字补录全文（{s['pages']}，扫描本 transcription=visual，"
             f"转录置信度 {s['confidence']}）；结局自台账 outcome_record 逐字照录，"
             f"并与原书應驗情況逐例核对：{s['outcome_check']}"
             + (s['extra'] if s['extra'] else ''))
    golds[cid] = {'id': cid, 'master_prediction': s['master_prediction'],
                  'outcome_record': e['outcome_record'],
                  'tradition': 'liuyao', 'pollution': 'low', 'grade': 'A',
                  'grade_note': gnote,
                  'provenance': e['source'], 'license_status': LICENSE_MODERN,
                  'redistributable': False}
    strip_register[cid] = ['master_prediction（台账原录为要旨摘录、回原书补录件）/outcome_record/'
                           'pollution_note/dedup_check/filters/grade_note（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('anchors←台账 input_fields.chart 全列逐字（键序 ben_gua/bian_gua/'
                                'moving_lines/chart_lines_top_to_bottom/fu_shen，fu_shen 空值照录）；'
                                'context←asked_at＋question＋原书章节定位组写；'
                                + ('subject←台账 subject 逐字（本例非空）' if e.get('subject')
                                   else 'subject 台账为空、原书未具名，组写'))
    verbatim_pages[cid] = s['pages']
    outcome_checks[cid] = s['outcome_check']

for cid in SEL:
    assert list(cards[cid].keys()) == INPUT_FIELDS, cid
    assert list(golds[cid].keys()) == GOLD_FIELDS, cid
    assert cards[cid]['redistributable'] is False and golds[cid]['redistributable'] is False
    assert golds[cid]['pollution'] == 'low'

# ---------- 落盘 ----------
for cid in SEL:
    with open(f'{OUT}/inputs/{cid}.json', 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=1)
        f.write('\n')
lines = [json.dumps(golds[cid], ensure_ascii=False) for cid in SEL]
frag_bytes = ('\n'.join(lines) + '\n').encode('utf-8')
with open(R93 + '/gold-frag-why-r93.jsonl', 'wb') as f:
    f.write(frag_bytes)
sha = hashlib.sha256(frag_bytes).hexdigest()

report = {
 'set': 'holdout34', 'round': 93, 'seat': 'WHY 族小席',
 'built_ids': SEL,
 'stop_items': [],
 'n_cards': len(SEL), 'n_gold_lines': len(lines),
 'gold_frag_sha256_build': sha, 'gold_frag_bytes': len(frag_bytes),
 'verbatim_pages': verbatim_pages,
 'transcription_confidence': {c: SUPPLEMENT[c]['confidence'] for c in SEL},
 'outcome_checks': outcome_checks,
 'field_mapping_notes': field_mapping_notes,
 'strip_register': strip_register,
 'page_images': 'runs/round93/why-pages-h34-seat/（前席备件，只读复用）＋'
                'runs/round93/why-pages-h34-seat-b/（本席新裁：p198–p201 半页与 zoom 复核件）',
}
with open(R93 + '/build-frag-why-r93.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('cards:', len(SEL), 'gold lines:', len(lines))
print('gold frag sha256 (build):', sha)
print('gold frag bytes:', len(frag_bytes))
