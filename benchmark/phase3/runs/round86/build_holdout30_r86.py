# -*- coding: utf-8 -*-
"""holdout30 组集封存构建脚本（R86 组集封存席）。

口径：runs/round86/PREREG.md §4 写死——T=28：六壬 14（三源轮取 DA→CY→BY 承
holdout29 体例、自台账序扣 h29 已取 13 后续取）＋六爻 14（WHY 一轮台账序 10
＋GSZ 建卡口径序 4）；紫微无例。字段白名单对齐 holdout29 输入卡实读。
扫描函数与标记集承 build_holdout29_r85.py（R42 PREREG §5 口径）。
"""
import json, os, re, hashlib, shutil
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R86 = os.path.join(BASE, 'runs/round86')
OUT_DIR = os.path.join(BASE, 'holdout30')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R86, 'build-holdout30-report-r86.json')
PRECHECK_PATH = os.path.join(R86, 'precheck-holdout30-seat-r86.json')

LICENSE_ANCIENT = '古籍文本，内部研究用'
LICENSE_MODERN = '现代版权文本，内部研究用'
INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question',
                'setting', 'provenance', 'redistributable', 'license_status', 'anchors']
GOLD_FIELDS = ['id', 'master_prediction', 'outcome_record', 'tradition',
               'pollution', 'grade', 'grade_note', 'provenance',
               'license_status', 'redistributable']


def load_json(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def load_jsonl(p):
    return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]


# ---------- 载入 ----------
used86 = load_json(os.path.join(R86, 'used-ids-r86.json'))
assert isinstance(used86, list) and len(used86) == 1192, len(used86)
used_set = set(used86)
h29_gold_ids = [json.loads(l)['id'] for l in
                open(os.path.join(BASE, 'holdout29/test_gold.jsonl'), encoding='utf-8') if l.strip()]
assert len(h29_gold_ids) == 27
combined_entries = list(used86) + h29_gold_ids   # 1219 条目（派单口径）
combined_set = set(combined_entries)             # 1192 distinct（h29 27 已在并集内，PREREG 登记）

lr_ledger = load_json(os.path.join(BASE, 'runs/round85/lr-eligible-ledger-r85.json'))
da_pool = {}
for fn in ('cases-a.jsonl', 'cases-b.jsonl'):
    for e in load_jsonl(os.path.join(BASE, 'expansion12/liuren-duanan', fn)):
        da_pool[e['id']] = e
cyj_pool = {e['id']: e for e in load_jsonl(os.path.join(BASE, 'expansion12/liuren-cuiyan/cases-juan5.jsonl'))}
by_pool = {e['id']: e for e in load_jsonl(os.path.join(BASE, 'expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl'))}
why_mining = load_json(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json'))
why_by = {e['provisional_id']: e for e in why_mining['entries']}
why_net = why_mining['counts']['net_eligible_A_low_present']
gsz_mining = load_json(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
gsz_by = {e['provisional_id']: e for e in gsz_mining['entries']}
gsz_card_list = set(gsz_mining['counts']['net_eligible_A_low_present'])
gsz_book_txt = open(os.path.join(BASE, 'runs/round76/gsz-book-r76.txt'), encoding='utf-8').read()

# ---------- 六壬台账序与轮取（口径 B：本集自 DA 起重启轮取，承 h29 体例） ----------
H29_LR = ['DA-025', 'DA-033', 'DA-034', 'DA-035', 'DA-037',
          'CYJ-001', 'CYJ-002', 'CYJ-004', 'CYJ-005',
          'BY-012', 'BY-014', 'BY-015', 'BY-016']
da_seq = [i for i in lr_ledger['六壬/《大六壬断案》'] if i not in H29_LR]
cyj_seq = [i for i in lr_ledger['六壬/《六壬粹言》卷五占验'] if i not in H29_LR]
cy_seq = [i for i in lr_ledger['六壬/《六壬粹言》卷六慕农占验附存'] if i not in H29_LR]
cy_merged = cyj_seq + cy_seq
by_seq = [i for i in lr_ledger['六壬/《六壬辨疑·毕法案录》'] if i not in H29_LR]
yx_seq = [i for i in lr_ledger['六壬/《大六壬预测学》'] if i not in H29_LR]
by_merged = by_seq + yx_seq
srcs = [da_seq, cy_merged, by_merged]
LR_SEL, ptr = [], [0, 0, 0]
while len(LR_SEL) < 14:
    for s in range(3):
        if len(LR_SEL) >= 14:
            break
        LR_SEL.append(srcs[s][ptr[s]])
        ptr[s] += 1
LR_EXPECTED = ['DA-038', 'CYJ-006', 'BY-017', 'DA-041', 'CYJ-007', 'BY-018',
               'DA-042', 'CYJ-008', 'BY-020', 'DA-044', 'CYJ-009', 'BY-021',
               'DA-046', 'CYJ-010']
assert LR_SEL == LR_EXPECTED, LR_SEL
lr_src_counts = Counter('DA' if c.startswith('DA-') else 'CY' if c.startswith(('CYJ-', 'CY-')) else 'BY' for c in LR_SEL)
assert lr_src_counts == {'DA': 5, 'CY': 5, 'BY': 4}, lr_src_counts

# ---------- 六爻选例（台账序） ----------
# WHY 一轮 eligible 未用序：STOCK-RECOUNT-h28 §7（h27 后 27 例）扣 h28 已取 5 例后续取 10
WHY_R1_REST = ['WHY-025', 'WHY-026', 'WHY-027', 'WHY-028', 'WHY-031', 'WHY-032',
               'WHY-033', 'WHY-034', 'WHY-035', 'WHY-036', 'WHY-037', 'WHY-038',
               'WHY-039', 'WHY-040', 'WHY-041', 'WHY-042', 'WHY-043', 'WHY-044',
               'WHY-068', 'WHY-069', 'WHY-070', 'WHY-071']
WHY_SEL = WHY_R1_REST[:10]
WHY_FALLBACK = WHY_R1_REST[10:]
# GSZ 建卡口径未用序（STOCK-RECOUNT-h28 §6，h28 后余 8）取 4
GSZ_REST = ['GSZ-101', 'GSZ-103', 'GSZ-104', 'GSZ-105', 'GSZ-107', 'GSZ-108', 'GSZ-109', 'GSZ-110']
GSZ_SEL = GSZ_REST[:4]
GSZ_FALLBACK = GSZ_REST[4:]

ORDER = LR_SEL + WHY_SEL + GSZ_SEL
assert len(ORDER) == 28 and len(set(ORDER)) == 28

# ---------- 前置核查（三项，落盘） ----------
# 1. 排除对：LY-015／LY-320 不得入集
ly_check = {x: (x in ORDER) for x in ('LY-015', 'LY-320')}
assert not any(ly_check.values())
# 2. 零复用：候选逐一对 1219 条目并集核对
overlap = [c for c in ORDER if c in combined_set]
assert overlap == [], overlap
# 3. id 号段占用：候选不得与既有任何已封集输入卡 id 冲突；且须为池卡既有 id（非新编号）
existing_set_ids = set()
for d in os.listdir(BASE):
    idir = os.path.join(BASE, d, 'inputs')
    if d.startswith('holdout') and os.path.isdir(idir):
        existing_set_ids |= {fn[:-5] for fn in os.listdir(idir) if fn.endswith('.json')}
assert not [c for c in ORDER if c in existing_set_ids], [c for c in ORDER if c in existing_set_ids]
pool_ids = set(da_pool) | set(cyj_pool) | set(by_pool) | set(why_by) | set(gsz_by)
assert all(c in pool_ids for c in ORDER)
precheck = {
    'seat': 'R86 holdout30 组集封存席',
    'exclusion_pair_check': {'checked': ['LY-015', 'LY-320'], 'in_selection': ly_check,
                             'conclusion': '两 id 均不在候选 28 例内（候选 id 空间 DA-/CYJ-/BY-/WHY-/GSZ-，与 LY- 不交叠，逐 id 明核）'},
    'zero_reuse_check': {'basis_entries': len(combined_entries), 'basis_distinct_ids': len(combined_set),
                         'basis_note': 'runs/round86/used-ids-r86.json 1192 条＋holdout29 金标 27 id 条目＝1219 条目；h29 之 27 id 已在 1192 distinct 内（PREREG 开轮登记），distinct 仍 1192',
                         'candidates': ORDER, 'overlap': overlap, 'conclusion': 'overlap 为空集'},
    'id_occupancy_check': {'existing_sealed_input_ids_count': len(existing_set_ids),
                           'conflicts': [], 'all_candidates_are_existing_pool_ids': True,
                           'conclusion': '28 id 均为既有池卡 id 之取用、未入任何已封集，无新编号、无冲突（R84 判例口径）'},
}
with open(PRECHECK_PATH, 'w', encoding='utf-8') as f:
    json.dump(precheck, f, ensure_ascii=False, indent=2)
    f.write('\n')

# ---------- DA 课盘与金标（底本全文 cases_raw 逐字复原） ----------
DA_CHART = {
 'DA-038': {
  'ke_name': '三交课（郑按）',
  'tianpan': '寅合、卯朱、辰蛇、巳贵、丑勾、午后、子青、未阴、亥空、戌虎、酉常、申玄（地盘支→上神天将；原式方阵：合朱蛇贵／寅卯辰巳、勾丑・午后、青子・未阴、亥戌酉申／空虎常玄）',
  'sike': '卯（朱）午、午（后）酉、未（阴）戌、戌（虎）癸（四课格原式：上行卯午未戌／下行午酉戌癸，天将朱后阴虎）',
  'sanchuan': '财庚午（后）、子丁卯（朱）、兄甲子（青）',
  'master_prediction': '邵先生曰：凡四正相交，非死即败。今午加酉，作后发用，午火至酉而无光。天后水又败在酉，既用死败神，则主男女淫奔。今加于宅，主此宅有淫乱不明之事，大不可居。',
  'outcome_record': '占者不听，竟居之。后果公淫其媳，家丑外扬。'},
 'DA-041': {
  'ke_name': '底本未载',
  'tianpan': '酉空、戌虎、亥常、子玄、申龙、丑阴、未勾、寅后、午合、巳雀、辰蛇、卯贵（地盘支→上神天将；原式方阵：空虎常玄／酉戌亥子、龙申・丑阴、勾未・寅后、午巳辰卯／合雀蛇贵；龙＝青龙、雀＝朱雀，底本省字照录）',
  'sike': '未（勾）卯、卯（贵）亥、酉（空）巳、巳（雀）癸（四课格原式：上行未卯酉巳／下行卯亥巳癸，天将勾贵空雀）',
  'sanchuan': '父辛酉（空）、官丑（阴）（原式旁标◎）、财丁巳（雀）（原式旁标⊙）',
  'master_prediction': '邵先生曰：前后左右皆有空坟，穴主山之侧，又是一阴人坟，若不去之，如何葬得？先生曰：此地甚好，以干支上皆贵人，且金局又生日，有何不利？但丑为墓田空亡，则是虚墓；兼有天空，亦是虚坟。须于中陪钱去之，然后可葬，日后必出贵人。最好是水路合星辰，文笔双峰，出人清秀。必是卯龙入首，作乙山辛向也。',
  'outcome_record': '徐向汪家买山，汪兄弟三分，只卖出二分。其长兄一分，故将空棺葬于内。其先前亦有三四个虚冢，皆葬不着。徐乃倍价向汪家长兄买之。庚戌年七月葬妻。壬子年，徐宅三房媳妇，两房得二男。至五六岁聪明，日读百余字，十二岁五经读尽，十六岁入试场，十九岁发科举，二十二岁兄又发举，二十六岁及第，想此地应矣。'},
 'DA-042': {
  'ke_name': '底本未载',
  'tianpan': '卯勾、辰合、巳朱、午蛇、寅青、未贵、丑空、申后、子虎、亥常、戌玄、酉阴（地盘支→上神天将；原式方阵：勾合朱蛇／卯辰巳午、青寅・未贵、空丑・申后、子亥戌酉／虎常玄阴）',
  'sike': '辰（合）午、午（蛇）申、丑（空）卯、卯（勾）戊（四课格原式：上行辰午丑卯／下行午申卯戊，天将合蛇空勾）',
  'sanchuan': '兄癸丑（空）（原式旁标◎）、财辛亥（常）、子己酉（阴）',
  'master_prediction': '邵先生曰：家势退矣。日上勾陈克日，又作空亡，旧事百般，尽牵在己。宅上午作螣蛇带阳刃，主家人争屋，四散分飞。初传丑作天空加卯，主泥土塞门户，妇人腹常疼痛，又有白带。自身主脾泄。末传尽去破败，来年难过，太阴主少妇掌家。',
  'outcome_record': '己卯年果将住宅拆毁，各人四散分居矣。'},
 'DA-044': {
  'ke_name': '底本未载',
  'tianpan': '辰青、巳空、午虎、未常、卯勾、申玄、寅合、酉阴、丑朱、子蛇、亥贵、戌后（地盘支→上神天将；原式方阵：青空虎常／辰巳午未、勾卯・申玄、合寅・酉阴、丑子亥戌／朱蛇贵后）',
  'sike': '亥（贵）子、子（蛇）丑、巳（空）午、午（虎）丁（四课格原式：上行亥子巳午／下行子丑午丁，天将贵蛇空虎）',
  'sanchuan': '官丙子（蛇）、官乙亥（贵）、子甲戌（后）',
  'master_prediction': '邵先生曰：令弟年久而得朝郎，奈后不永。吾丈虽未第，而前程未易量也。此实阴德所至，日后必然位至郎官。曰：此课虽魁渡天门，不作阻隔论。乃六仪扶护，三奇拱秀，小则郎官，大则侍从。因有活人之功，故上天降福，北斗扶身，三光拱照，禄神催逼，即日食禄矣。人见此课，皆谓退连茹不利；殊不知甲戌旬，戌为六仪，戌加亥，亥属乾，乾为天，谓之六仪朝天。亥子丑遁得乙丙丁，谓之三奇拱照。午乃丁禄临干，谓之日禄扶身；且行年并白虎，为催官符使；贵人在三奇之中，而前后拱之；此蛇为吉将，名前一先锋，高甲无疑矣。丁德在亥，戌亥子俱属阴，故知阴德洪大，神明福佑也。亥为上帝，子为紫微，丑为北斗，是以得上天之降福也。',
  'outcome_record': '后贡元庚戌科及第，授吴县尉。辛酉除左司郎官。戊辰升太常寺少卿。己巳二月升大常寺正卿，九月授礼部侍郎。庚午年五月卒于官，享年六十三岁。'},
 'DA-046': {
  'ke_name': '底本未载',
  'tianpan': '申龙、酉勾、戌合、亥雀、未空、子蛇、午虎、丑贵、巳常、辰玄、卯阴、寅后（地盘支→上神天将；原式方阵：龙勾合雀／申酉戌亥、空未・子蛇、虎午・丑贵、巳辰卯寅／常玄阴后；龙＝青龙、雀＝朱雀，底本省字照录）',
  'sike': '戌（合）未、未（空）辰、寅（后）亥、亥（雀）庚（四课格原式：上行戌未寅亥／下行未辰亥庚，天将合空后雀）',
  'sanchuan': '财戊寅（后）、官辛巳（常）、兄申（龙）（原式旁标◎）',
  'master_prediction': '邵先生曰：先失后得，先虚后实。耗废尽了，却得妻财来助起家。因水利中得财，不可不知。若求问功名，不可得也。须是败尽再发，兄弟并星散。所可喜者，妻与子成家，晚年享福有寿，就店房居住。',
  'outcome_record': '应一心只思及第，自后读书不成。家计败尽，方得妻家做酒生理。诸子皆好，日渐丰足，享福寿终。'},
}

# ---------- BY 课盘与金标（原书页图逐字复原，本席 200dpi 渲染读图） ----------
BY_CHART = {
 'BY-017': {
  'ke_name': '进茹空亡',
  'tianpan': '午青、未勾、申合、酉朱、巳空、戌蛇、辰白、亥贵、卯常、寅元、丑阴、子后（地盘支→上神天将；原式方阵：青勾合朱／午未申酉、空巳・戌蛇、白辰・亥贵、卯寅丑子／常元阴后；元＝玄武、龙＝青龙，原书省字照录）',
  'sike': '卯（常）寅、寅（元）丑、酉（朱）申、申（合）丁（四课格原式：上行卯寅酉申／下行寅丑申丁，天将常元朱合）',
  'sanchuan': '财申（合）、财酉（朱）、子戌（蛇）',
  'master_prediction': '正议：此课不以空亡退步论，专看宾主内外。支为主，玄武贼符自上克之，支之二课为内，申酉自外冲之。又干支罗网，三传联茹，重围匪地，无隙可逃。卯酉相冲，门户破败不可以保。',
  'outcome_record': '案验：围久粮空，兵勇自溃，贼匪乘虚而入。而人军兴以来，惟汉中持守年余，皮靴药材食尽，饿莩枕藉，城陷无人可掳，虽睢阳不过如是哀哉。'},
 'BY-018': {
  'ke_name': '进茹空亡',
  'tianpan': '午贵、未后、申阴、酉元、巳蛇、戌常、辰朱、亥白、卯合、寅勾、丑青、子空（地盘支→上神天将；原式方阵：贵后阴元／午未申酉、蛇巳・戌常、朱辰・亥白、卯寅丑子／合勾青空；元＝玄武，原书省字照录）',
  'sike': '丑（青）子、子（空）亥、子（空）亥、亥（白）辛（四课格原式：上行丑子子亥／下行子亥亥辛，天将青空空白）',
  'sanchuan': '父丑（青）、财寅（勾）、财卯（合）',
  'master_prediction': '正议：三传丑寅卯进茹，中末逢空，宜退而不宜进。且正时玄武临门，关墓旬尾发用，必因西方门户之处有贼犯境，故城中闭关，进则无益。然退后，亥子又是脱气，干支乘虚空，亦不可以坐守，惟合干支三传更进一步，便逢辰土建旺，庶可相生。',
  'outcome_record': '案验：本月底上游五百里至袁州颇相安，江西省旋因武宁失守闭城，城外寓处亦毁。'},
 'BY-020': {
  'ke_name': '胎南死气',
  'tianpan': '丑空、寅白、卯常、辰元、子青、巳阴、亥勾、午后、戌合、酉朱、申蛇、未贵（地盘支→上神天将；原式方阵：空白常元／丑寅卯辰、青子・巳阴、勾亥・午后、戌酉申未／合朱蛇贵；元＝玄武，原书省字照录）',
  'sike': '申（蛇）子、子（青）辰、酉（朱）丑、丑（空）戊（四课格原式：上行申子酉丑／下行子辰丑戊，天将蛇青朱空）',
  'sanchuan': '财子（青）、子申（蛇）、兄辰（元）',
  'master_prediction': '正议：子为日财又作日胎，三六相呼，干支相合，主妻有孕，胎逢月内死气，孕必有损，损后复孕，以中传月建助财故也。',
  'outcome_record': '案验：先损复孕已准。'},
 'BY-021': {
  'ke_name': '交车相合・两贵受克・人宅受脱',
  'tianpan': '未蛇、申贵、酉后、戌阴、午朱、亥元、巳合、子常、辰勾、卯青、寅空、丑白（地盘支→上神天将；原式方阵：蛇贵后阴／未申酉戌、朱午・亥元、合巳・子常、辰卯寅丑／勾青空白；元＝玄武，原书省字照录）',
  'sike': '亥（元）酉、酉（后）未、申（贵）午、午（朱）乙（四课格原式：上行亥酉申午／下行酉未午乙，天将元后贵朱）',
  'sanchuan': '官申（贵）、财戌（阴）、父子（常）',
  'master_prediction': '正议：正贵加午，幕贵加戌，俱受克制，不可干贵。以贵人自顾不暇也。乙生午，未生酉，干支俱受上神脱耗，占宅主盗。凡占亦主彼此虚耗，虽交车相合，而未支脱午，支上酉又克日干，外面相关而内怀脱克，不可以利断也。近城内外，俱难久居，须向亥水长生方，再进四百里，方可驻足。',
  'outcome_record': '案验：时居江右城外一月，即赴袁州，其后贼据武宁，逼近省垣。'},
}

# ---------- WHY 断语补录（回原书〔判斷〕段逐字，visual 转录） ----------
WHY_SUPPLEMENT = {
 'WHY-025': ('印刷p48', '〔判斷〕卦中朱雀爻臨父母亥水發動，為火災的信息。亥水對應於西北，西北方向可能將有火災發生。今卦中父母亥水休囚，元神官鬼酉金空亡月破，不會馬上發生。定是在四月五日進入辰月以後官鬼酉金出月合破才會發生。具體地來判斷，四月十二日進入下一旬，官鬼酉金出空，出空一定有大的火災。以六爻應期規律看，既可以應申日，又可以應酉日。甲申日已進下一旬，又為朱雀所臨之爻，休囚逢長生之應，而酉金則是卦中地支實空之日。因此若有火災發生必此二日內。'),
 'WHY-026': ('印刷p49–50', '〔判斷〕卦中官鬼與朱雀同位發動，毫無疑問是火災發生的信息。官鬼申金得月建生扶，又化進神，比前幾日的火災更大。以六爻應期規律來看，用神動而化進，乃應逢值逢合，火災應發生在巳日或巳月。此卦之中官鬼元神妻財戌土月破，本月不會發生，所以當為巳月發生。具體來判斷，乃應元神逢合逢值之日，即戌日或者卯日。'),
 'WHY-027': ('印刷p50', '〔判斷〕妻財酉金得月建生扶，動而化回頭生，財旺生世，財運不錯。但是官鬼亥水臨朱雀在二爻發動，二爻為宅，官鬼與朱雀同動主火災，當慮家中發生火災。'),
 'WHY-028': ('印刷p54', '〔判斷〕以世爻為用神，世爻即為我們生活的地球。世爻不受日月之剋，反得日辰生扶，忌神子孫申金安靜，地球沒有絲毫被毀滅的跡象。因此地球上不會出現外星人入侵，也不會有所謂的一九九九年大劫難發生。《諸世紀》中的預言是不成立的。但是此卦之中官鬼卯木持世發動，且成三合局，官鬼為災害的信息標誌，說明地球雖然沒有被毀滅的現象出現，但卻有自然災害發生。因官鬼旺相成三合局，合有會聚之意，反映出災害集中和多的信息。官鬼臨勾陳發動，勾陳司田土，為地震的信息。同時父母巳火臨朱雀發動，為火災的信息。因此此年當有地震和火災頻繁發生。'),
 'WHY-031': ('印刷p82–83', '〔判斷〕以官鬼為用神。世應相剋婚姻晚。官鬼卯木臨應爻，應為夫位、男性朋友爻位，說明已經有男友。古人云『官鬼臨應必稱心』，自己很喜歡現在的男友。兩個間爻發動，父母午火動生兄弟丑土，兄弟丑土動生忌神子孫，戀愛不順利，家裡有人反對。父母為雙親，兄弟為姐妹，家裡的父母姐妹反對。古書上云『世剋應嫌貧愛富』，是嫌對方的家庭貧困或對方工資不高。世爻入墓於動爻兄弟丑土，入墓為不能自控，主本人沒主見，不能左右自己的婚姻。父母巳火與日相合，故以父母爻來判斷結婚應期。所謂『父母合日定婚期』。因巳火月破，乃應實破，即巳年或巳月。另一父母午火與變爻相合，合處應沖，來年丙子沖開父母午火，綜合來看，應為一九九六年巳月結婚。'),
 'WHY-032': ('印刷p84', '〔判斷〕以妻財爻為用神。乍一看世應相生，夫妻關係很好，但是仔細一看，妻財卯木伏在官鬼午火下，世爻空亡，應斷為夫妻關係不好。求床帳為官鬼午火，雖然兩現，卻都逢空亡，乃是離異或分居的信息。用神不上卦，為妻子不在家之象。再看表示結婚証書的父母辰土被日剋，元神月破，又化回頭剋。乃是離婚之象。父母和日相合，以父母定結婚應期。一九八二年為壬戌年，當為一九八二年結婚。一九九二年為壬申年，一九九三年為癸酉年，皆剋用神，定是這兩年之中的其中一年離婚的。申金在卦中出現，一九九二年離婚的可能性大。月為財爻的沐浴之地，生扶用神，妻子長得漂亮。財爻為木，旺相，個子高。臨玄武，長得很性感。用神伏在官鬼之下，官鬼為別的男人，可以理解為妻子和別的男人有曖昧關係。但官鬼午火月破、空亡，非是真的，乃是一種假象。因此我斷其懷疑老婆有第三者，結果影響了夫妻感情，導致離婚。'),
 'WHY-033': ('印刷p85', '〔判斷〕以官鬼為用神。用神伏在三爻之下，休囚無氣，夫妻緣分薄。用神伏藏，丈夫已不在家。求香閨為亥水，與官鬼同爻伏藏，乃是丈夫離家以後，一個人在家過的信息。父母寅木和日辰相同，以父母爻為判斷結婚的應期。父母寅木安靜，以應期規律看，靜而逢值逢沖，應申年結婚，同時又用神官鬼休囚，申年為用神長生之年，定是申年結婚。一九九二年為壬申年，斷其是在一九九二年結婚的。官鬼亥水與父母寅木相合，父母為結婚証書，說明求測人丈夫有結婚經歷，找的是個二婚的。世爻為巳火，應爻為辰土，辰巳同納巽卦，夫妻二人為同鄉。即古人所謂的『親上加親同一宮』是也。一九九四年為甲戌年，乃剋制官鬼之年，當在一九九四年離婚。'),
 'WHY-034': ('印刷p86–87', '〔判斷〕以妻財爻為用神。妻財伏在父母巳火之下，飛神為用神絕地，說明現在沒有對象。忌神持世，不利婚姻，結婚遲。一九九五年為乙亥助旺用神沖開飛神，此年應有對象。本年丙子與用神地支相同，伏藏逢出現，本年也應有對象可談。下月為亥月，沖開飛神，對象出現。用神為子水，長得圓臉型。從月建來看，用神子水為驛馬，用神又伏在第五爻，五爻為道路，驛馬主快速，對象走路快。臨白虎，性格有點急噪，脾氣不好。因姻緣多遇難成，所以一有機遇一定要抓住。父母巳火與日辰相同，以父母爻定婚期。二〇〇一年為辛巳，應該在二〇〇一年結婚。辛巳年為子孫長生之地，當年結婚生子。卦中官鬼兩動，二爻官鬼卯木為子孫胎地，又為胎兒之爻位，動而生扶父母，父母為結婚証書，乃是先懷孕後結婚之象。'),
 'WHY-035': ('印刷p132', '〔判斷〕以子孫爻為用神。子孫午火伏父母亥水之下，飛來剋伏，為不吉。但飛神被月建剋住，日辰沖開飛神助起伏神，乃有子之象。父母亥水得官鬼酉金生扶，二〇〇〇年庚辰年，合住官鬼酉金，父母入墓難剋子孫，可有孩子。若還沒有二〇〇一辛巳年，沖開飛神必有。'),
 'WHY-036': ('印刷p134', '〔判斷〕以子孫爻為用神。乍一看子孫動化回頭生，乃是將來有子之象，但子孫日月不生，反被日辰剋傷，乃是無根之子孫。再加上元神巳火月破，縱化回頭生也無濟於事。兄弟巳火在世爻，為子孫之元神，月破不能生子孫，卦明明告訴本人人生不下孩子。巳火是被月建沖破的，月為官鬼，官鬼為丈夫，生不下孩子是丈夫的問題。子孫辰土在二爻被日剋傷，二爻為夫位，同時又是應爻，應爻也為夫位，臨白虎，白虎為病，是丈夫有病不能懷孕。二爻為生殖器的爻位，子孫也主生殖器，是丈夫的生殖器有問題。財為精子，空而伏藏，又遇月建亥水為病地，是丈夫的精子有問題。使她不能懷孕。若和丈夫一起生活，一生也不會有孩子。'),
}
assert set(WHY_SUPPLEMENT) == set(WHY_SEL)

# ---------- 资格断言 ----------
eligibility, fallback_log = {}, []


def lr_qual(cid):
    r = (da_pool.get(cid) or cyj_pool.get(cid) or by_pool.get(cid))
    if r is None:
        return False
    ok = (r.get('holdout_eligible') is True and r.get('contamination') == 'low'
          and r.get('outcome_grade') in ('A', 'A-low')
          and r['master_predictions'][0]['statement_excerpt'].strip()
          and r['outcome']['description'].strip() and cid not in used_set)
    if cid.startswith('BY-'):
        ok = ok and r['review']['verdict'] == 'seal' and r['review']['grade_final'] in ('A', 'A-low') \
            and r['review']['contamination_final'] == 'low'
    return bool(ok)


for cid in LR_SEL:
    eligibility[cid] = {'pool_qual': lr_qual(cid), 'pass': lr_qual(cid)}
    assert lr_qual(cid), cid

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
    el['in_book_ben_gua'] = chart['ben_gua'][:2] in gsz_book_txt or chart['ben_gua'] in gsz_book_txt
    el['in_book_asked'] = asked.split('（')[0][:7] in gsz_book_txt.replace(' ', '')
    return el


def gsz_qual(cid):
    e = gsz_by[cid]
    base_ok = (e['grade'] == 'A' and e['pollution'] == 'low'
               and e['anchor_presence'] == 'present' and e['eligible_net'] is True
               and cid in gsz_card_list
               and e['master_prediction'].strip() and e['outcome_record'].strip())
    el = five_elements(cid)
    ok = base_ok and all(el.values())
    eligibility[cid] = {'elements': el, 'base_qual': bool(base_ok), 'pass': bool(ok)}
    return ok


for cid in GSZ_SEL:
    assert gsz_qual(cid), cid


def why_qual(cid):
    e = why_by[cid]
    return (cid in why_net and e['pollution'] == 'low'
            and e['anchor_presence'] == 'present' and not e['anchor_missing']
            and e['outcome_record'].strip())


for cid in WHY_SEL:
    eligibility[cid] = {'ledger_qual': why_qual(cid), 'supplement': cid in WHY_SUPPLEMENT,
                        'pass': why_qual(cid) and cid in WHY_SUPPLEMENT}
    assert why_qual(cid), cid

# ---------- 建卡与金标 ----------
cards, golds = {}, {}
strip_register, field_mapping_notes = {}, {}
leak_notes = []

for cid in LR_SEL:
    r = da_pool.get(cid) or cyj_pool.get(cid) or by_pool.get(cid)
    prov = (f"{r['provenance']['work']}（{r['provenance']['edition']}）·{r['provenance']['page']}"
            f"；底本为用户提供，redistributable=false")
    if cid.startswith('DA-'):
        d = DA_CHART[cid]
        anchors = {'asked_at': r['asked_at'], '课名': d['ke_name'],
                   '天盘': d['tianpan'], '四课': d['sike'], '三传': d['sanchuan'],
                   '课盘原文来源': '底本全文 cases_raw.json 原式照录（天盘方阵／四课格／三传栏）'}
        mp, oc = d['master_prediction'], d['outcome_record']
        gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low；'
                 '课式头四要素 present（R84 核查台账）；课盘经本席回底本全文逐字复原；'
                 '金标断语／结局回底本全文邵先生曰段与应验段逐字照录（池卡摘录为节录，'
                 '不作金标准据）；' + r['grade_note'])
    elif cid.startswith('BY-'):
        d = BY_CHART[cid]
        anchors = {'asked_at': r['asked_at'], '课名': d['ke_name'],
                   '天盘': d['tianpan'], '四课': d['sike'], '三传': d['sanchuan'],
                   '课盘原文来源': '原书页图课盘直录（本席200dpi渲染读图，件存 runs/round86/lr-pages-h30-seat/）'}
        mp, oc = d['master_prediction'], d['outcome_record']
        gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low、'
                 '复核 verdict=seal；课式头四要素 present（R84 核查台账）；课盘与'
                 '正议／案验全文经本席回原书页图逐字复原；池卡摘录为节录，不作金标准据；'
                 + r['grade_note'] + '；复核：' + r['review']['notes'])
    else:
        anchors = {'asked_at': r['asked_at'],
                   '课式头四要素': '年、月、日、时俱载（台账锚点 present 口径，R84 核查台账）',
                   '课盘': '原书有课盘列、池卡未录盘字（holdout12 建集日志 fidelity 登记在案）',
                   'chart_complete': False,
                   'chart_fidelity': '仅干支（复原不能）：原书课盘列在盘、转录底稿未录盘、页图字迹不足以逐字可靠转录；仅录课式头干支，不臆补盘面（承 holdout12 粹言先例）'}
        mp = r['master_predictions'][0]['statement_excerpt']
        oc = r['outcome']['description']
        gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low；'
                 '课式头四要素 present（R84 核查台账）；断语／结局照池卡逐字转录'
                 '（visual 转录，置信度见池卡 grade_note）；课盘 fidelity 降级登记'
                 '见输入卡 anchors；' + r['grade_note'])
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
    golds[cid] = {'id': cid, 'master_prediction': mp, 'outcome_record': oc,
                  'tradition': 'liuren', 'pollution': 'low',
                  'grade': r['outcome_grade'], 'grade_note': gnote,
                  'provenance': prov, 'license_status': LICENSE_ANCIENT,
                  'redistributable': False}
    strip_register[cid] = ['master/master_predictions/outcome/outcome_grade/contamination/'
                           'contamination_rationale/grade_note/holdout_eligible/review'
                           '（池卡管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject/question←池卡 subject/question_or_topic 逐字；'
                                'anchors←asked_at 逐字＋本席回原文复原课盘；'
                                'setting/provenance←池卡 provenance 组写')
    if cid in ('CYJ-006', 'CYJ-009'):
        leak_notes.append({'id': cid, 'note': 'subject 逐字承池卡、含「后知为某人」之占后知悉身份揭示'
                                              '（非所问吉凶结局本身）；承 h29 DA-037「解元」附带登记口径，不改卡面，提请主持验封知悉'})

for cid in WHY_SEL:
    e = why_by[cid]
    ch = e['input_fields']['chart']
    mv = ch.get('moving_lines', ch.get('moving_lines_text'))
    cards[cid] = {
        'id': cid, 'tradition': 'liuyao',
        'subject': '求测者（台账 subject 为空、原书未具名）',
        'context': (f"{e['input_fields']['asked_at']}，{e['input_fields']['question']}"
                    f"；原书{e['source'].split('｜')[1]}"),
        'question': e['input_fields']['question'],
        'setting': '六爻分类占验技法（王虎应著）',
        'provenance': f"{e['source']}；底本为用户经学校图书馆提供之扫描本，redistributable=false",
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': {'asked_at': e['input_fields']['asked_at'],
                    'ben_gua': ch['ben_gua'], 'bian_gua': ch['bian_gua'],
                    'moving_lines': mv,
                    'chart_lines_top_to_bottom': ch['chart_lines_top_to_bottom']}}
    loc, mp = WHY_SUPPLEMENT[cid]
    golds[cid] = {'id': cid, 'master_prediction': mp,
                  'outcome_record': e['outcome_record'],
                  'tradition': 'liuyao', 'pollution': 'low', 'grade': 'A',
                  'grade_note': (f"A（主持口径）；断语台账未单列字段，本轮回原书《六爻分类占验技法》"
                                 f"〔判斷〕段逐字补录（{loc}，扫描本 transcription=visual）；"
                                 f"结局自台账 outcome_record 逐字照录。"),
                  'provenance': e['source'], 'license_status': LICENSE_MODERN,
                  'redistributable': False}
    strip_register[cid] = ['master_prediction（台账未单列、回原书补录件）/outcome_record/'
                           'pollution_note/dedup_check/filters/grade_note（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = 'anchors←台账 input_fields.chart 全列逐字；context←asked_at＋question＋原书章节定位组写'

for cid in GSZ_SEL:
    e = gsz_by[cid]
    ch = e['input_fields']['chart']
    cards[cid] = {
        'id': cid, 'tradition': 'liuyao',
        'subject': '求测者（台账 subject 为空、原书未具名）',
        'context': (f"{e['input_fields']['asked_at']}，{e['input_fields']['question']}"
                    f"；原书{e['source'].split('｜')[1]}"),
        'question': e['input_fields']['question'],
        'setting': '六爻卦例说真（王虎应著）',
        'provenance': f"{e['source']}；底本为用户经学校图书馆提供，redistributable=false",
        'redistributable': False,
        'license_status': LICENSE_MODERN,
        'anchors': {'asked_at': e['input_fields']['asked_at'],
                    'ben_gua': ch['ben_gua'], 'bian_gua': ch['bian_gua'],
                    'chart_lines_top_to_bottom': ch['chart_lines_top_to_bottom']}}
    golds[cid] = {'id': cid, 'master_prediction': e['master_prediction'],
                  'outcome_record': e['outcome_record'],
                  'tradition': 'liuyao', 'pollution': 'low', 'grade': 'A',
                  'grade_note': ('A（主持口径：建卡口径五要素复核全在场——卦名／动爻／世应／'
                                 '六亲纳支／月建日辰俱载、回原书文字层在册）；断语与结局自台账逐字照录。'
                                 + (('台账 grade_note：' + e['grade_note']) if e['grade_note'] else '')),
                  'provenance': e['source'], 'license_status': LICENSE_MODERN,
                  'redistributable': False}
    strip_register[cid] = ['master_prediction/outcome_record/outcome_type/pollution_note/'
                           'dedup_check/filters/grade_note（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = 'anchors←台账 input_fields.chart 全列逐字；context←asked_at＋question＋原书章节定位组写'

for cid in ORDER:
    assert list(cards[cid].keys()) == INPUT_FIELDS, cid
    assert list(golds[cid].keys()) == GOLD_FIELDS, cid
    assert cards[cid]['redistributable'] is False and golds[cid]['redistributable'] is False

# ---------- 扫描函数（承 h29 脚本体例，R42 PREREG §5 标记集） ----------
LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗语', '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '正议', '正議', '验语', '驗语', '占断', '占斷', '线索', '線索']
BANNED_IN_CARD = {'grade_note', 'contamination', 'contamination_rationale', 'outcome', 'outcome_record',
                  'master_prediction', 'master_assertion', 'gold', 'answer', 'holdout_eligible',
                  'review', 'pollution', 'pollution_note', 'anchor_status', 'anchor_presence',
                  'anchor_missing', 'dedup_check', 'filters', 'transcription', 'transcription_confidence',
                  'source', 'grade', 'fail_reason', 'eligible_net', 'outcome_type', 'master',
                  'master_predictions', 'input_fields', 'provisional_id'}


def fragments(text):
    out = set()
    for seg in re.split(r'[。；：！？\n]', text):
        seg = seg.strip(' ，、')
        if len(seg) >= 8:
            out.add(seg)
    flat = re.sub(r'\s+', '', text)
    for i in range(len(flat) - 11):
        out.add(flat[i:i + 12])
    return out


def scan_content(obj):
    hits = []

    def walk(o, path):
        if isinstance(o, dict):
            for k, v in o.items():
                walk(v, path + '/' + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, path + f'[{i}]')
        elif isinstance(o, str):
            for mk in LEVEL1:
                if mk in o:
                    hits.append({'path': path, 'marker': mk, 'level': 1})
            for mk in LEVEL2:
                if mk in o:
                    hits.append({'path': path, 'marker': mk, 'level': 2})
    walk(obj, '')
    return hits


def scan_field_names(obj):
    hits = []

    def walk(o, path):
        if isinstance(o, dict):
            for k, v in o.items():
                for b in FIELD_BLACKLIST:
                    if b in str(k):
                        hits.append({'path': path + '/' + str(k), 'marker': b})
                walk(v, path + '/' + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, path + f'[{i}]')
    walk(obj, '')
    return hits


def banned_key_scan(obj):
    hits = []

    def walk(o, path):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in BANNED_IN_CARD:
                    hits.append({'path': path + '/' + str(k), 'key': k})
                walk(v, path + '/' + str(k))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                walk(v, path + f'[{i}]')
    walk(obj, '')
    return hits


# 扫描①：金标片段对输入卡逐字子串
scan1 = {}
for cid in ORDER:
    card_text = json.dumps(cards[cid], ensure_ascii=False)
    hits_mp = [fr for fr in fragments(golds[cid]['master_prediction']) if fr in card_text]
    hits_oc = [fr for fr in fragments(golds[cid]['outcome_record']) if fr in card_text]
    scan1[cid] = {'master_prediction_hits': hits_mp, 'outcome_hits': hits_oc}
    assert not hits_oc and not hits_mp, (cid, hits_oc[:3], hits_mp[:3])

# 扫描②：内容级标记＋字段名＋禁用键
scan_markers = {}
for cid in ORDER:
    ch, fh, bk = scan_content(cards[cid]), scan_field_names(cards[cid]), banned_key_scan(cards[cid])
    scan_markers[cid] = {'content_hits': ch, 'fieldname_hits': fh, 'banned_key_hits': bk}
    assert not ch and not fh and not bk, (cid, ch, fh, bk)

# ---------- 构成限度断言（PREREG §4 写死） ----------
SOURCE_OF = {}
for cid in ORDER:
    if cid.startswith('DA-'):
        SOURCE_OF[cid] = '《大六壬断案》'
    elif cid.startswith(('CYJ-', 'CY-')):
        SOURCE_OF[cid] = '《六壬粹言》'
    elif cid.startswith(('BY-', 'YX-')):
        SOURCE_OF[cid] = '变易预测（《六壬辨疑·毕法案录》／《大六壬预测学》）'
    elif cid.startswith('WHY-'):
        SOURCE_OF[cid] = '《六爻分类占验技法》'
    else:
        SOURCE_OF[cid] = '《六爻卦例说真》'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)
assert len(ORDER) == 28 and len(ORDER) >= 25
assert trad_counts == {'liuren': 14, 'liuyao': 14}, trad_counts
assert max(trad_counts.values()) == 14  # 14/28 = 50.0%，不逾 50%
assert max(src_counts.values()) <= 10, src_counts
assert all(v <= 6 for k, v in lr_src_counts.items())
assert all(golds[c]['pollution'] == 'low' for c in ORDER)
composition_assertions = {
    'T': 28, 'by_tradition': dict(trad_counts), 'by_source': dict(src_counts),
    'lr_by_source': dict(lr_src_counts),
    'max_single_tradition_share': max(trad_counts.values()) / 28,
    'max_single_source_share': max(src_counts.values()) / 28,
    'non_yijian': 28, 'non_liuyao': 28 - trad_counts['liuyao'], 'pollution_low': 28,
    'used_union_intersection': [], 'all_pass': True}

# ---------- 落盘 ----------
card_bytes = {}
for cid in ORDER:
    p = os.path.join(IN_DIR, f'{cid}.json')
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
        f.write('\n')
    card_bytes[cid] = os.path.getsize(p)
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in ORDER:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')

# ---------- 落盘后回读复扫 ----------
read_cards = {cid: load_json(os.path.join(IN_DIR, f'{cid}.json')) for cid in ORDER}
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
assert {g['id'] for g in read_golds} == set(ORDER) and len(read_golds) == 28
reread = {}
for cid in ORDER:
    card_text = json.dumps(read_cards[cid], ensure_ascii=False)
    g = next(x for x in read_golds if x['id'] == cid)
    oc_hits = [fr for fr in fragments(g['outcome_record']) if fr in card_text]
    mp_hits = [fr for fr in fragments(g['master_prediction']) if fr in card_text]
    assert not oc_hits and not mp_hits, (cid, oc_hits[:3], mp_hits[:3])
    assert not scan_content(read_cards[cid]) and not scan_field_names(read_cards[cid]), cid
    assert not banned_key_scan(read_cards[cid]), cid
    assert list(read_cards[cid].keys()) == INPUT_FIELDS, cid
    reread[cid] = {'outcome_hits': oc_hits, 'master_prediction_hits': mp_hits,
                   'marker_hits': 0, 'banned_key_hits': 0, 'pass': True}

sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
gold_bytes = os.path.getsize(gold_path)

# ---------- 快照：封存时点活 method ＋ 与本轮平台快照对勘 ----------
SNAP_DIR = os.path.join(R86, 'kb-snapshot-holdout30')
if os.path.exists(SNAP_DIR):
    shutil.rmtree(SNAP_DIR)
shutil.copytree(os.path.join(BASE, 'method'), SNAP_DIR)
SNAP_EXCLUDED = []
for fn in sorted(os.listdir(SNAP_DIR)):
    if fn.startswith('METHOD-') and fn.endswith('.md'):
        os.remove(os.path.join(SNAP_DIR, fn))
        SNAP_EXCLUDED.append(fn)
snap_entries = []
for root, dirs, files in os.walk(SNAP_DIR):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        snap_entries.append((os.path.relpath(p, SNAP_DIR),
                             hashlib.sha256(open(p, 'rb').read()).hexdigest()))
SNAP_SHA_PATH = os.path.join(R86, 'kb-snapshot-holdout30-sha256.txt')
with open(SNAP_SHA_PATH, 'w', encoding='utf-8') as f:
    for rel, h in snap_entries:
        f.write(f'{h}  {rel}\n')
snap_list_sha = hashlib.sha256(open(SNAP_SHA_PATH, 'rb').read()).hexdigest()
snap_map = dict(snap_entries)
plat_dir = os.path.join(R86, 'kb-snapshot')
plat_map = {}
for root, dirs, files in os.walk(plat_dir):
    dirs.sort()
    for fn in sorted(files):
        p = os.path.join(root, fn)
        plat_map[os.path.relpath(p, plat_dir)] = hashlib.sha256(open(p, 'rb').read()).hexdigest()
diff_files = [rel for rel in sorted(set(plat_map) | set(snap_map))
              if plat_map.get(rel) != snap_map.get(rel)]

report = {
    'round': 86, 'set': 'holdout30', 'built_by': '组集封存席（R86）',
    'ruling': 'runs/round86/PREREG.md §4（构成写死）＋派单口径（轮取读法 B：本集自 DA 起重启轮取，承 holdout29 体例；与派单字面「续取」读法之别已登记，提请主持验封裁处）',
    'T': 28, 'order': ORDER,
    'lr_rotation': {'source_order': ['DA（断案）', 'CY（粹言 CYJ-后CY-合并台账序）', 'BY（变易 BY-后YX-合并台账序）'],
                    'selected': LR_SEL, 'by_source': dict(lr_src_counts),
                    'rule': '自 lr 台账扣 h29 已取 13 例后余面，三源轮取自 DA 起取 14（承 h29 首轮体例）'},
    'liuyao_selection': {'WHY': WHY_SEL, 'WHY_fallback_unused': WHY_FALLBACK,
                         'GSZ': GSZ_SEL, 'GSZ_fallback_unused': GSZ_FALLBACK},
    'precheck': precheck,
    'fallback_log': fallback_log,
    'leak_note_list': leak_notes,
    'composition_assertions': composition_assertions,
    'eligibility_assertions': eligibility, 'eligibility_all_pass': True,
    'input_field_whitelist': INPUT_FIELDS,
    'input_field_whitelist_basis': 'holdout29 输入卡实读字段集（开工对齐）',
    'strip_register': strip_register, 'field_mapping_notes': field_mapping_notes,
    'gold_supplement': {cid: {'loc': WHY_SUPPLEMENT[cid][0],
                              'source': '原书《六爻分类占验技法》〔判斷〕段逐字补录（扫描本，transcription=visual）'}
                        for cid in WHY_SEL},
    'supplement_count': len(WHY_SEL),
    'lr_gold_recovery': {
        'DA': '金标断语／结局回底本全文（cases_raw）逐字照录；DA-041 两段邵曰拼接（占者问句与缘生谛注不入，登记）；DA-044 内嵌缘生谛注一句（「吾丈，对人的尊称」）剔除（登记）；DA-038 郑按／缘生谛注、DA-042/046 缘生谛注不入',
        'BY': '金标正议／案验与课盘回原书页图全文逐字复原（件存 runs/round86/lr-pages-h30-seat/）；BY-018 案验续释句（盖辰属土…笔墨为生涯也）承 h29 BY-015 先例不入结局、登记；BY-017 附议问答不入断语',
        'CYJ': '断语／结局照池卡摘录逐字（池卡即摘录定本）；课盘 fidelity 降级登记 5 例（chart_complete=false）'},
    'scan1_verbatim_fragment': {
        'method': '每例 master_prediction 与 outcome_record 的特征片段（标点分句整句（≥8字）＋去空白12字滑动窗口全集）对该例输入卡全文本逐字子串扫描；全28例零命中（硬断言）',
        'per_case': scan1},
    'scan_marker_selfcheck': {
        'method': 'R42 PREREG §5 内容级一级/二级标记＋字段名黑名单＋禁用键集对28张输入卡全字段递归扫描（构建脚本内断言道）',
        'per_case': scan_markers,
        'total_hits': sum(len(v['content_hits']) + len(v['fieldname_hits']) + len(v['banned_key_hits']) for v in scan_markers.values())},
    'scan_reread_selfcheck': {
        'method': '落盘后逐卡回读重行片段／标记／禁用键／白名单核，全过', 'per_case': reread},
    'scan2_independent_rescan': '由独立复扫脚本 scan_holdout30_r86.py 执行，结果另行登记于封存日志',
    'scan3_host_rescan': '主持验封道，非本席执行——留位',
    'gold_sha256_hashlib': sha_lib, 'gold_bytes': gold_bytes,
    'card_bytes': card_bytes, 'card_bytes_total': sum(card_bytes.values()),
    'kb_snapshot': {'dir': 'runs/round86/kb-snapshot-holdout30/',
                    'excluded_non_snapshot_files': SNAP_EXCLUDED,
                    'file_count': len(snap_entries),
                    'sha256_list': 'runs/round86/kb-snapshot-holdout30-sha256.txt',
                    'sha256_list_sha256': snap_list_sha,
                    'files': [rel for rel, _ in snap_entries],
                    'diff_vs_round86_platform_snapshot': diff_files},
    'notes': ['WHY-025 台账 asked_at 作「1997年4月27日（卯月甲戌日）」、原书例一作「四月廿日」，卡面承台账逐字、差异登记备核',
              '判读归属：本集为 R86-REV1 判读集预定——本轮修订不立项、无待判读干预，本集判读归属为空缺登记'],
    'outputs_written': [f'holdout30/inputs/{c}.json' for c in ORDER] + ['holdout30/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': 28, 'order': ORDER,
                  'fallback_log': fallback_log,
                  'snapshot_files': len(snap_entries), 'snapshot_excluded': SNAP_EXCLUDED,
                  'diff_vs_platform': diff_files,
                  'gold_sha256_hashlib': sha_lib, 'gold_bytes': gold_bytes,
                  'card_bytes_total': sum(card_bytes.values())}, ensure_ascii=False))
