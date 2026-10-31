# -*- coding: utf-8 -*-
"""holdout31 组集封存构建脚本（R87 组集封存席）。

口径：runs/round87/PREREG.md §5＋PREREG-ADDENDUM-r87.md 构成定版——T=28：
六壬 14（源序 DA→CY→BY 轮取、读法 B 自 DA 起重启；CY 源经常规 eligible
为 0 自动无取，实成 DA 7＋BY 7）＋六爻 14（WHY 台账序续取 10＋GSZ-107、
108、109、110 四例尽取）。锚点以盘体实载为准（CYJ 专项复核裁定乙）。
字段白名单对齐 holdout30 输入卡实读。扫描函数与标记集承 build_holdout30_r86.py
（R42 PREREG §5 口径）。
"""
import json, os, re, hashlib, shutil
from collections import Counter

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
R87 = os.path.join(BASE, 'runs/round87')
OUT_DIR = os.path.join(BASE, 'holdout31')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R87, 'build-holdout31-report-r87.json')
PRECHECK_PATH = os.path.join(R87, 'precheck-holdout31-seat-r87.json')

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
used87 = load_json(os.path.join(R87, 'used-ids-r87.json'))
assert isinstance(used87, list) and len(used87) == 1220, len(used87)
used_set = set(used87)
assert len(used_set) == 1220
precheck = load_json(PRECHECK_PATH)

lr_ledger = load_json(os.path.join(BASE, 'runs/round85/lr-eligible-ledger-r85.json'))
da_pool = {}
for fn in ('cases-a.jsonl', 'cases-b.jsonl'):
    for e in load_jsonl(os.path.join(BASE, 'expansion12/liuren-duanan', fn)):
        da_pool[e['id']] = e
by_pool = {e['id']: e for e in load_jsonl(os.path.join(BASE, 'expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl'))}
why_mining = load_json(os.path.join(BASE, 'runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json'))
why_by = {e['provisional_id']: e for e in why_mining['entries']}
why_net = why_mining['counts']['net_eligible_A_low_present']
gsz_mining = load_json(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'))
gsz_by = {e['provisional_id']: e for e in gsz_mining['entries']}
gsz_card_list = set(gsz_mining['counts']['net_eligible_A_low_present'])
gsz_book_txt = open(os.path.join(BASE, 'runs/round76/gsz-book-r76.txt'), encoding='utf-8').read()

# ---------- 六壬台账序与轮取（读法 B：自 DA 起重启；CY 常规 eligible 为 0 自动无取） ----------
da_seq = [i for i in lr_ledger['六壬/《大六壬断案》'] if i not in used_set]
by_seq = [i for i in lr_ledger['六壬/《六壬辨疑·毕法案录》'] if i not in used_set]
LR_SEL, _di, _bi = [], 0, 0
while len(LR_SEL) < 14:
    LR_SEL.append(da_seq[_di]); _di += 1
    if len(LR_SEL) >= 14:
        break
    LR_SEL.append(by_seq[_bi]); _bi += 1
LR_EXPECTED = ['DA-047', 'BY-022', 'DA-048', 'BY-023', 'DA-050', 'BY-024', 'DA-051',
               'BY-025', 'DA-054', 'BY-027', 'DA-055', 'BY-028', 'DA-057', 'BY-030']
assert LR_SEL == LR_EXPECTED, LR_SEL
assert LR_SEL == precheck['selection']['liuren_wheel']
lr_src_counts = Counter('DA' if c.startswith('DA-') else 'BY' for c in LR_SEL)
assert lr_src_counts == {'DA': 7, 'BY': 7}, lr_src_counts

# ---------- 六爻选例（台账序） ----------
WHY_SEL = precheck['selection']['why']
assert WHY_SEL == ['WHY-037', 'WHY-038', 'WHY-039', 'WHY-040', 'WHY-041',
                   'WHY-042', 'WHY-043', 'WHY-044', 'WHY-068', 'WHY-069']
WHY_FALLBACK = ['WHY-070', 'WHY-071']  # 一轮余序（未触发）
GSZ_SEL = precheck['selection']['gsz']
assert GSZ_SEL == ['GSZ-107', 'GSZ-108', 'GSZ-109', 'GSZ-110']
GSZ_FALLBACK = []  # 建卡口径余序至 GSZ-110 尽取、无同源递补余位（未触发）

ORDER = LR_SEL + WHY_SEL + GSZ_SEL
assert ORDER == precheck['selection']['order']
assert len(ORDER) == 28 and len(set(ORDER)) == 28

# ---------- 前置核查对勘（precheck 件已落盘，本处只复断言） ----------
assert precheck['exclusion_pair_check']['in_selection'] == {'LY-015': False, 'LY-320': False}
assert precheck['zero_reuse_check']['overlap'] == []
assert precheck['id_occupancy_check']['conflicts'] == []
assert precheck['lr_remaining_recount']['regular_eligible_total'] == 170
assert precheck['why_remaining_recount']['remaining_total'] == 42
pool_ids = set(da_pool) | set(by_pool) | set(why_by) | set(gsz_by)
assert all(c in pool_ids for c in ORDER)

# ---------- DA 课盘与金标（底本全文 cases_raw 逐字复原，本席自 raw 原式转录） ----------
DA_CHART = {
 'DA-047': {
  'ke_name': '涉三渊课',
  'tianpan': '未空、申虎、酉常、戌玄、午青、亥阴、巳勾、子后、辰合、卯朱、寅蛇、丑贵（地盘支→上神天将；原式方阵：空虎常玄／未申酉戌、青午・亥阴、勾巳・子后、辰卯寅丑／合朱蛇贵）',
  'sike': '申（虎）午、午（青）辰、酉（常）未、未（空）戊（四课格原式：上行申午酉未／下行午辰未戊，天将虎青常空）',
  'sanchuan': '子壬申（虎）、兄戌（玄）（原式旁标◎）、财甲子（后）（原式旁标⊙）',
  'master_prediction': '邵先生曰：涉三渊课，主跋涉奔波，劳力无成。干支上午与未合，出身甚妙，历事三授，两丁上服。申为子孙，居午火阳刃上，而受下克，且乘白虎，主难为子息。中传同类为兄弟，加子息上，日后当以弟为子。末传妻爻坐空，天后秽神加之，妻因产亡。戊辰干支皆东南神，辛卯命又是东方，三传反流入西方，那更涉三渊，陷于西北，必主死于外州。传既不回，故子亦不能归也。四十五六岁，行年到子丑，为过三渊之外，然而落空，虽过得此年，亦不济事也。',
  'outcome_record': '徐二十五上铨试中，当年授岳州尉。二十七丁父忧。二十九授浑州尉。三十丁母忧。三十三授复州司户，当年冬赴任。三十四妻因产亡，止有四女，遂以小弟为子。任满再授广西提学干官，又授广州东莞县令。四十五终于任上，继子遂家于彼而不归。'},
 'DA-048': {
  'ke_name': '底本未载',
  'tianpan': '申合、酉朱、戌蛇、亥贵、未勾、子后、午青、丑阴、巳空、辰虎、卯常、寅玄（地盘支→上神天将；原式方阵：合朱蛇贵／申酉戌亥、勾未・子后、青午・丑阴、巳辰卯寅／空虎常玄）',
  'sike': '申（合）巳、巳（空）寅、亥（贵）申、申（合）丙（四课格原式：上行申巳亥申／下行巳寅申丙，天将合空贵合）',
  'sanchuan': '财壬申（合）、官亥（贵）（原式旁标◎）、父丙寅（玄）（原式旁标⊙）',
  'master_prediction': '邵先生曰：申本时临日，为日所克，又丙为夫，申为妻。既从日上发用，空亡又临妻宫，目下主克妻；亥数四，主克四妻。仲冬子息亦克，以六合不得地也。申为西南之金，到巳之炉冶上，必有声名于西北也。申乘今日之马，干又坐本命之马而得长生，主为官至老不倦也。宅上丙火受寅而生，不可以外内言也。年将四旬必遇曹姓人而显官，亦终于六曹。亥乃月将，不论空亡，但时少迟耳。月将贵人入传，四年之后，便显自绛帐，从此达于天庭。又寅来生身，十一月天马天在寅，寅临天门，玄归本家为黑煞，黑煞为刑职，中传既有天门，末寅又在天门上，以天见天，必出疆见诸侯，然后入奉天子。处六曹中带刑职者，黑煞之故也。寅申巳亥为四维，主代天子而守四方，必四任也。',
  'outcome_record': '徐君当年服满从吉，得江州德化县令，次年二月赴任，五月丧妻杨氏。庚戌正月再娶李氏。辛亥年宣抚使刘大中保举，得诸王府教授，李氏又亡，又娶毛氏，此应中传之亥，自绛帐而入绛帐，从此达于天庭也。果然四年自诸王教授，出为饶州通判，丁母忧，服满得宣州通判。是时知州曹泳，乃秦太师上客，曹赴京，因荐之，徐随赴召。毛氏又卒，再娶江氏，转知江阴州军，召为监察御史，又除殿中侍御史，七月除吏部侍郎，出作奉使兼枢密院承旨，年八十六矣。'},
 'DA-050': {
  'ke_name': '铸印乘轩课',
  'tianpan': '戌朱、亥合、子勾、丑青、酉蛇、寅空、申贵、卯虎、未后、午阴、巳玄、辰常（地盘支→上神天将；原式方阵：朱合勾青／戌亥子丑、蛇酉・寅空、贵申・卯虎、未午巳辰／后阴玄常）',
  'sike': '丑（青）申、申（贵）卯、巳（玄）子、子（勾）己（四课格原式：上行丑申巳子／下行申卯子己，天将青贵玄勾）',
  'sanchuan': '父辛巳（玄）、兄甲戌（朱）、官己卯（虎）',
  'master_prediction': '邵先生曰：吾兄心术多，且又毒，以鼠忌羊头上，鸡惊犬吠喉。凡所行所为，皆为妒忌之心，好闻是非，好谈人短，所以灭前程也。大凡七煞元辰，若占前程多主妒忌，常占多主事体切害。初传破碎乘玄武，又是驿马，主面东指西，走南奔北，多图多觅之人。身宅虽皆有贵人，而子作勾陈，申作空亡，谓之指空话空。己以巳为父母，加妻宫，为妻所制，又乘马与破碎，是踪迹不定，不在父母之旁，一不足也。子息倚身，为身所克，子息难得，二不足也。申犯空亡，作夜贵加宅，是神像破损，香火不安，三不足也。妻临身宫，上下夹克，若非不和，便多疾病，四不足也。铸印乘轩之课，巳作玄武加子，上火下水，玄武为贼，谓之走范。卯作白虎加戌，谓之破模。虎伤卯，又为坠轩，故主功名不成。且防覆坠骑乘之患也。',
  'outcome_record': '后至壬戌年二月，因争役乘轿入城，坠而折足，血气上攻而死。'},
 'DA-051': {
  'ke_name': '底本未载',
  'tianpan': '午青、未空、申虎、酉常、巳勾、戌玄、辰合、亥阴、卯朱、寅蛇、丑贵、子后（地盘支→上神天将；原式方阵：青空虎常／午未申酉、勾巳・戌玄、合辰・亥阴、卯寅丑子／朱蛇贵后）',
  'sike': '辰（合）卯、卯（朱）寅、未（空）午、午（青）戊（四课格原式：上行辰卯未午／下行卯寅午戊，天将合朱空青）',
  'sanchuan': '兄庚辰（合）、父辛巳（勾）、父壬午（青）',
  'master_prediction': '邵先生曰：干支皆天罗阳刃，四课发传，归于日上，主目下赴任。但值罗刃，主不终任。来岁行年到地盘亥上见子，即凑今日之地网，必阻父服。三十七岁到寅上见卯，即是今日支辰，自三十七岁后迤逦赴任，绵绵不断，一气十五年，合作监司之职。十五年后入午，天罗阳刃，必降官闲住；再八年，连前十五年，共二十三年而寿阻。',
  'outcome_record': '叶二甲二名高中，授抚州教官。己酉年八月上任，庚戌年四月丁父忧。三十七岁得国学录。三十八岁召试馆职高中，得除国子监丞。四十一岁除太常寺丞。四十四岁迁工部待郎。四十六岁迁尚书都官郎中。四十九岁除司农少卿。五十一岁发淮西总领兼少卿，当年又兼淮西运使。五十二岁上，因支军粮交争，降三级，停见任，自此闲居八年死。'},
 'DA-054': {
  'ke_name': '登三天',
  'tianpan': '未朱、申蛇、酉贵、戌后、午合、亥阴、巳勾、子玄、辰青、卯空、寅虎、丑常（地盘支→上神天将；原式方阵：朱蛇贵后／未申酉戌、合午・亥阴、勾巳・子玄、辰卯寅丑／青空虎常）',
  'sike': '辰（青）寅、寅（虎）子、酉（贵）未、未（朱）丙（四课格原式：上行辰寅酉未／下行寅子未丙，天将青虎贵朱）',
  'sanchuan': '子庚辰（青）、兄壬午（合）、财申（蛇）（原式旁标◎）',
  'master_prediction': '邵先生曰：登三天，本主升迁之象，但嫌登不过关。关者，日干是也。既不过关，难以升迁。若跳过，则又进锐退速。白虎入宅乘父母，目下必因丁艰而阻。且主父母棺内白蚁食坏，以致不利子孙，遂成灾咎。服满之后，虽得一任差遣，恐不能终任矣。',
  'outcome_record': '知丞乃机宜之弟，课象主服不利，彼此相同，果因阻服未升迁。及举母棺，欲与父合葬，因起父坟视之，尽为泥水白蚁伤坏，遂不敢葬。续有堪舆人，言此地本吉，因葬高露风不利，若葬低便发。知丞又来占，极断其不可，而知丞不听，竟合葬焉。及服满，授黄州推官，赴任数月，因病假归，十二月卒。'},
 'DA-055': {
  'ke_name': '底本未载',
  'tianpan': '巳朱、午蛇、未贵、申后、辰合、酉阴、卯勾、戌玄、寅青、丑空、子虎、亥常（地盘支→上神天将；原式方阵：朱蛇贵后／巳午未申、合辰・酉阴、勾卯・戌玄、寅丑子亥／青空虎常）',
  'sike': '辰（合）辰、辰（合）辰、申（后）申、申（后）庚（四课格原式：上行辰辰申申／下行辰辰申庚，天将合合后后）',
  'sanchuan': '兄申（后）（原式旁标◎⊙）、财戊寅（青）、官辛巳（朱）',
  'master_prediction': '邵先生曰：将仕之禄，乃虚禄也。夫武职兵权，惟要金盛，无金何武？此课无武有文，今任必不赴，必改岳庙之职，就彼处宜读书取科第。己酉中举；来年庚戌及第，二甲二十一名。',
  'outcome_record': '赵不信，后果不能赴广南任，遂授潭州岳庙，因邀数人同读书，己酉投国子监中举，庚戌年登科。'},
 'DA-057': {
  'ke_name': '伏吟课',
  'tianpan': '巳朱、午合、未勾、申青、辰蛇、酉空、卯贵、戌虎、寅后、丑阴、子玄、亥常（地盘支→上神天将；原式方阵：朱合勾青／巳午未申、蛇辰・酉空、贵卯・戌虎、寅丑子亥／后阴玄常）',
  'sike': '午（合）午、午（合）午、亥（常）亥、亥（常）壬（四课格原式：上行午午亥亥／下行午午亥壬，天将合合常常）',
  'sanchuan': '兄乙亥（常）、财壬午（合）、兄丙子（玄）',
  'master_prediction': '邵先生曰：此课本身，现在戴禄，又作太常，必有兼职之事，俸禄亦增，若论升转则未。盖支干自刑，日后因得宠，遂做不廉之事。又因纳一美妾，贪色寻医而治。欲解任不能，幸遇一外路监司经过，为公恳告，遂得解任。但伏吟时下未发，只等替时自见耳。',
  'outcome_record': '龚因主簿坏去，遂权署其职。得太守宠，遂旁若无人。又纳一妾，颇多淫乐。其后龚尉满替，因前看验事受贿，被人论告，欲去不能，州县又不与批结。遂求湖北运司胡某，胡向与龚父交好，又与太守是往日同寅官，因经过见太守，为龚力恳，遂准放行，乃得归也。'},
}
assert set(DA_CHART) == {c for c in LR_SEL if c.startswith('DA-')}

# ---------- BY 课盘与金标（原书页图逐字复原，本席 140dpi 渲染读图、课盘 250dpi 裁切复核） ----------
BY_CHART = {
 'BY-022': {
  'ke_name': '上下皆合・闭口卦体',
  'tianpan': '寅青、卯勾、辰合、巳朱、丑空、午蛇、子白、未贵、亥常、戌元、酉阴、申后（地盘支→上神天将；原式方阵：青勾合朱／寅卯辰巳、空丑・午蛇、白子・未贵、亥戌酉申／常元阴后；元＝玄武，原书省字照录）',
  'sike': '申（后）亥、亥（常）寅、申（后）亥、亥（常）甲（四课格原式：上行申亥申亥／下行亥寅亥甲，天将后常后常）',
  'sanchuan': '财丑（贵）、父亥（常）、父亥（常）',
  'master_prediction': '正议：干支上神皆作六合，占主二人同心。又八专课，如八家共井、同力合作之象。交车长生，宜在此处结宾主、谋生理，以为久远之计。若占行程，阳主超进，岁日二马原是动象，奈发用逢空，亥作闭口，动必有阻，亦进茹空亡宜退步之例也。两贵坐狱，二马交克，干支丑财旬空，必饷运不继，官兵失利，贼复壅塞，致道路不通耳。',
  'outcome_record': '案验：果信不能通，次年春自袁州回到长沙，闻贼又陷本省，致阻行程，其后袁州亦失，而原断宜为久远者则误矣。盖阴神俱克干支，为左右猷城之象。八专彼此相同，是楚与袁皆不能安也。二马并冲，自当远颺，不可以坐而受生之例泥之。且长生作闭口，是父母之邦不通也。'},
 'BY-023': {
  'ke_name': '自支传干・闭口卦体',
  'tianpan': '寅青、卯勾、辰合、巳朱、丑空、午蛇、子白、未贵、亥常、戌元、酉阴、申后（地盘支→上神天将；原式方阵：青勾合朱／寅卯辰巳、空丑・午蛇、白子・未贵、亥戌酉申／常元阴后；元＝玄武，原书省字照录；本例天盘与课例二十四原式同式，经 250dpi 裁切复核）',
  'sike': '寅（青）巳、巳（朱）申、申（后）亥、亥（常）甲（四课格原式：上行寅巳申亥／下行巳申亥甲，天将青朱后常）',
  'sanchuan': '子巳（朱）、禄寅（青）、父亥（常）',
  'master_prediction': '正议：初传支上神，末传干上神，为自支传干，占事皆起于人。支神克日，上见劫煞，必家有凶人为首劫掠。子孙太阳，其护救亦在家人也。后临干鬼，巳作闭口，不能大逞其凶。',
  'outcome_record': '案验：四月见劫耗，所指亦准。'},
 'BY-024': {
  'ke_name': '庚日逢丁',
  'tianpan': '午青、未空、申白、酉常、巳勾、戌元、辰合、亥阴、卯朱、寅蛇、丑贵、子后（地盘支→上神天将；原式方阵：青空白常／午未申酉、勾巳・戌元、合辰・亥阴、卯寅丑子／朱蛇贵后；元＝玄武，原书省字照录）',
  'sike': '寅（蛇）丑、丑（贵）子、戌（元）酉、酉（常）庚（四课格原式：上行寅丑戌酉／下行丑子酉庚，天将蛇贵元常）',
  'sanchuan': '财寅（蛇）、财卯（朱）、父辰（合）',
  'master_prediction': '正议：干乘羊刃遁丁克日，每因兄弟致起争端，且摇动不定，难安常业，墓神加支，宅亦昏昧，蛇朱相乘，三传生起正时午火，必有火烛之惊。幸寅为月德，支属子水，可以化解。',
  'outcome_record': '案验：果因弟屡见官非，逃亡数次，前一日见火，亦为弟所致。'},
 'BY-025': {
  'ke_name': '庚日逢丁',
  'tianpan': '寅蛇、卯朱、辰合、巳勾、丑贵、午青、子后、未空、亥阴、戌元、酉常、申白（地盘支→上神天将；原式方阵：蛇朱合勾／寅卯辰巳、贵丑・午青、后子・未空、亥戌酉申／阴元常白；元＝玄武，原书省字照录）',
  'sike': '午（青）酉、酉（常）子、寅（蛇）巳、巳（勾）庚（四课格原式：上行午酉寅巳／下行酉子巳庚，天将青常蛇勾）',
  'sanchuan': '鬼午（青）、财卯（朱）、子子（后）',
  'master_prediction': '正议：比用课，移远就近，纵不到家，亦在邻县。常乘丁马，眷属必行，但卯为舟车，逢酉冲破。青龙克日，财爻助鬼见朱，官符逢勾，恐有见官之事。',
  'outcome_record': '案验：下流贼退，携眷至天门寄寓。次年二月汉中货船到紫阳破坏，被人抢夺，鸣官。'},
 'BY-027': {
  'ke_name': '水日逢丁',
  'tianpan': '卯朱、辰蛇、巳贵、午后、寅合、未阴、丑勾、申元、子青、亥空、戌白、酉常（地盘支→上神天将；原式方阵：朱蛇贵后／卯辰巳午、合寅・未阴、勾丑・申元、子亥戌酉／青空白常；元＝玄武，原书省字照录）',
  'sike': '丑（勾）卯、卯（朱）巳、酉（常）亥、亥（空）癸（四课格原式：上行丑卯酉亥／下行卯巳亥癸，天将勾朱常空）',
  'sanchuan': '鬼丑（勾）、兄亥（空）、父酉（常）',
  'master_prediction': '正议：勾朱相会，定有官讼。丁马作财，岁逢天空，利于奏对。但逆间课，不无阻隔耳。',
  'outcome_record': '案验：先因下员案件羁累，不能进京。旋奉檄调松江府，并不待赴京引见。'},
 'BY-028': {
  'ke_name': '传财化鬼・辛日逢丁',
  'tianpan': '酉青、戌勾、亥合、子朱、申空、丑蛇、未白、寅贵、午常、巳元、辰阴、卯后（地盘支→上神天将；原式方阵：青勾合朱／酉戌亥子、空申・丑蛇、白未・寅贵、午巳辰卯／常元阴后；元＝玄武，原书省字照录）',
  'sike': '卯（后）亥、亥（白）未、午（常）寅、寅（贵）辛（四课格原式：上行卯亥午寅／下行亥未寅辛，天将后白常贵）',
  'sanchuan': '子亥（合）、财卯（后）、父未（白）',
  'master_prediction': '正议：课上有鬼，三传会财以生之，为传财化鬼格。切不可求财。如此课，三传亥卯未，第二课与正时见巳午是也。且辛日逢丁，游都加干，动必遇贼。比用课以舍远就近为安。',
  'outcome_record': '案验：四月初八，贼劫株树潭时避杨家，颇安，离城仅五里耳。'},
 'BY-030': {
  'ke_name': '屋宅宽广・魁度天门・六爻现卦',
  'tianpan': '辰合、巳勾、午青、未空、卯朱、申白、寅蛇、酉常、丑贵、子后、亥阴、戌元（地盘支→上神天将；原式方阵：合勾青空／辰巳午未、朱卯・申白、蛇寅・酉常、丑子亥戌／贵后阴元；元＝玄武，原书省字照录）',
  'sike': '戌（玄）亥、亥（阴）子、卯（朱）辰、辰（合）戊（四课格原式：上行戌亥卯辰／下行亥子辰戊，天将玄阴朱合；原式天将行末另标「关」字）',
  'sanchuan': '兄戌（元）、子酉（常）（原式旁标游）、子申（白）（原式旁标都）',
  'master_prediction': '正议：三传戌酉申，全备西方，脱戊干之土，生子支之水，占家宅主屋多人衰。此闲官星，魁度天门，得日上辰土冲关，可免阻隔。然辰命上见卯官，三传会子孙克之，非吉象也。游都作虎，玄武劫财，须防西方肃杀之凶。',
  'outcome_record': '案验：次年酉贼破省，黄陂失守。'},
}
assert set(BY_CHART) == {c for c in LR_SEL if c.startswith('BY-')}

# ---------- WHY 断语补录（回原书〔判斷〕段逐字，visual 转录） ----------
WHY_SUPPLEMENT = {
 'WHY-037': ('印刷p135', '〔判斷〕以子孫爻為用神。子孫子水伏在初爻父母未土之下，飛神發動剋用神，不吉。幸好飛神空亡，又有日辰制服，古書云：『空下伏神，易於引拔。』用神伏而得出。午月飛神逢合不剋伏神，沖出伏神，孩子將於午月出生。沖處逢合，合處逢沖，午月子日出生必應丑時，丑日出生必應子時。六月十四日為丙子日，十五日為丁丑日，孩子一定是在這兩日出世。判斷孩子的性別，子孫爻休囚，又是陰爻發動，當生女孩。同時本卦陰卦變陰卦，也為生女孩的信息。'),
 'WHY-038': ('印刷p135–136', '〔判斷〕以子孫爻為用神。子孫巳火伏於五爻父母子水之下，飛剋伏不吉。但飛神安靜，元神發動生之，乃是凶中有救。看本人安危，以世爻看之。世爻與日月五行相同，旺相為吉。子孫日月相合為難產的資訊，元神月破，寅月實破，生助用神，為寅月生。子孫為陽爻，休囚，陽爻發動，為生男孩。'),
 'WHY-039': ('印刷p136', '〔判斷〕以子孫爻為用神。子孫巳火伏在五爻父母子水之下，飛來剋伏，用神又不旺相，但不受日月之剋，飛神反被日月剋制，飛神自顧無暇，無力剋伏，無妨。世爻為求測者，子孫墓庫臨世，為腹中懷孕之象。今月建沖破，肚開生孩子之象。本月即生。臨白虎，白虎主臨盆，也是即要生孩子之資訊。子孫休囚，在巽宮，巽為陰卦，當生女孩。子孫墓庫被月沖破，破墓易出，不會難產。'),
 'WHY-040': ('印刷p137', '〔判斷〕侄女和嬰兒都屬子孫爻，但卦中只有一個子孫爻，若以一個子孫爻來同時判斷嬰兒和侄女的吉凶，顯然不很合適。此時就要把六親加以活用。假如以子孫酉金為嬰兒，兄弟丑土為子孫墓庫，為懷孕嬰兒的人，所以把兄弟丑土即可以理解為其侄女。今子孫墓庫月破，是本月要生孩子的資訊。子孫酉金得月生扶，為吉。子孫為陰爻，又在陰卦，當生女孩。兄弟辰土動合子孫為難產，兄弟丑土入墓於辰土，乃侄女住院之資訊。'),
 'WHY-041': ('印刷p137–138', '〔判斷〕以子孫為用神。子孫亥水得日月生扶，孩子平安無事。用神化進神，乃孩子入盆之象。出生日期應在亥月。大凡用神化進神，進神逢值之日即為應期。所以孩子出生應在乙卯日。'),
 'WHY-042': ('印刷p138', '〔判斷〕以子孫為用神。子孫酉金旺相臨世是懷孕的標誌。子孫臨世為胎。用神生世，是孩子尋母之象。子水為孩子之原神，原神子水空亡，孩子缺水，所以胎兒不動。子水空亡待出空填實之日，孩子當動。本月是午月，子水出空填實在未月，當為未月胎動。'),
 'WHY-043': ('印刷p139', '〔判斷〕以子孫為用神。用神不上卦，子孫子水伏在飛神父母亥水下，飛來生伏是吉兆，是懷孕的信息。用神伏藏，所以以前月經不正常，一般測懷孕，子孫伏藏都是停經而來測的。子孫化回頭生說明孩子強壯有力，一經出生必然是個胖小子。而子孫不上卦，應該還有很長時間才顯示出來。子孫逢空，出空在子月，子孫的出空之日也是子水出現之時，因此會在子月出生。'),
 'WHY-044': ('印刷p140', '〔判斷〕以子孫為用神。子孫子水持世，動而化回頭生，是已經懷孕的資訊。子孫所臨之爻為陰，不得日月生扶為休囚，卦中四個爻發動，多爻發動看靜爻，兩個靜爻都是陰爻，子孫所臨之爻為陰，第三個孩子也是女的。'),
 'WHY-068': ('印刷p188', '〔判斷〕卦雖是我搖，但她本人求測，以世爻為用神。世在三爻臨勾陳被二爻官鬼午火剋制，三爻為子宮的爻位，世爻又是子孫的長生之地，是生孩子的地方，子宮的信息很強。勾陳為腫脹之物，但世爻得日幫扶為旺相，所以斷其是子宮瘤。官鬼為忌神，子孫剋官，臨水為中醫，所以斷其服中藥可治。'),
 'WHY-069': ('印刷p188–189', '〔判斷〕自己測病以世爻為用神。世爻不得日月生扶且空亡為休囚。五爻元神臨勾陳動而化絕，月建又是其墓庫，癌症無疑。五爻為五官的爻位，山火賁在艮宮，艮為鼻子，脾胃、手背等方面的疾病，結合爻為判斷為鼻癌。妻財在五爻動而化絕是鼻涕流不出，呼吸不便的信息。三爻元神妻財亥水也被日月剋傷，動而化墓，不能生用，妻財主尿，入墓不生用，是小便困難的信息。世臨白虎，白虎主刀，是做手術的信息。但用神休囚，很難完全治愈。'),
}
assert set(WHY_SUPPLEMENT) == set(WHY_SEL)

# ---------- 资格断言（承 h30 §三断言集，按本集源面适配） ----------
eligibility, fallback_log = {}, []


def lr_qual(cid):
    r = (da_pool.get(cid) or by_pool.get(cid))
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
    eligibility[cid] = {'pool_qual': lr_qual(cid), 'pass': lr_qual(cid),
                        'chart_source': '底本全文 cases_raw 原式（DA）' if cid.startswith('DA-')
                                        else '原书页图课盘直录（BY）'}
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
    r = da_pool.get(cid) or by_pool.get(cid)
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
    else:
        d = BY_CHART[cid]
        anchors = {'asked_at': r['asked_at'], '课名': d['ke_name'],
                   '天盘': d['tianpan'], '四课': d['sike'], '三传': d['sanchuan'],
                   '课盘原文来源': '原书页图课盘直录（本席140dpi渲染读图、课盘250dpi裁切复核，件存 runs/round87/lr-pages-h31-seat/）'}
        mp, oc = d['master_prediction'], d['outcome_record']
        gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low、'
                 '复核 verdict=seal；课式头四要素 present（R84 核查台账）；课盘与'
                 '正议／案验全文经本席回原书页图逐字复原；池卡摘录为节录，不作金标准据；'
                 + r['grade_note'] + '；复核：' + r['review']['notes'])
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

# ---------- 扫描三道：标记与字段名扫描（承 R42 PREREG §5 口径，复用 h30 扫描函数） ----------
LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗语', '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '正议', '正議', '验语', '驗语', '占断', '占斷', '线索', '線索']
BANNED_IN_CARD = {'grade_note', 'contamination', 'contamination_rationale', 'outcome',
                  'outcome_record', 'master_prediction', 'master_assertion', 'gold', 'answer',
                  'holdout_eligible', 'review', 'pollution', 'pollution_note', 'anchor_status',
                  'anchor_presence', 'anchor_missing', 'dedup_check', 'filters', 'transcription',
                  'transcription_confidence', 'source', 'grade', 'fail_reason', 'eligible_net',
                  'outcome_type', 'master', 'master_predictions', 'input_fields', 'provisional_id'}


def all_strings(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from all_strings(v)
    elif isinstance(o, list):
        for v in o:
            yield from all_strings(v)
    elif isinstance(o, str):
        yield o


def all_keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield k
            yield from all_keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from all_keys(v)


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


content_hits, fieldname_hits, banned_hits, frag_hits = {}, {}, {}, {}
for cid in ORDER:
    card = cards[cid]
    ch = [mk for s in all_strings(card) for mk in LEVEL1 + LEVEL2 if mk in s]
    fh = [b for k in all_keys(card) for b in FIELD_BLACKLIST if b in str(k)]
    bk = [k for k in all_keys(card) if k in BANNED_IN_CARD]
    text = json.dumps(card, ensure_ascii=False)
    fg = [fr for fr in fragments(golds[cid]['master_prediction']) if fr in text] + \
         [fr for fr in fragments(golds[cid]['outcome_record']) if fr in text]
    content_hits[cid], fieldname_hits[cid] = ch, fh
    banned_hits[cid], frag_hits[cid] = bk, fg
    assert not ch and not fh and not bk and not fg, (cid, ch[:3], fh[:3], bk[:3], fg[:3])
leak_notes.append('构建道：28 卡一级＋二级标记零命中、字段名污染词零命中、禁用键零命中、'
                  '金标断语与结局逐句片段对卡面子串扫描零命中（扫描函数与标记集逐字承 '
                  'build_holdout30_r86.py；落盘回读道与独立复扫道另见报告与 '
                  'scan-holdout31-rescan-r87.json）。')

# ---------- 限定核验 ----------
cnt = Counter(golds[c]['tradition'] for c in ORDER)
assert len(ORDER) == 28 and cnt == {'liuren': 14, 'liuyao': 14}, cnt
src_counts = {'DA': lr_src_counts['DA'], 'BY': lr_src_counts['BY'],
              'WHY': 10, 'GSZ': 4}
assert all(v <= 14 for v in src_counts.values())                    # 单源 ≤50%
yizhi = [c for c in ORDER if c.startswith('YZ-')]
non_yizhi = 28 - len(yizhi)
assert non_yizhi >= 13
assert cnt['liuren'] + 0 >= 13                                      # 非六爻侧＝六壬 14
assert all(golds[c]['pollution'] == 'low' for c in ORDER)
composition = {'T': 28, 'tradition_counts': dict(cnt),
               'tradition_shares': {'liuren': 0.5, 'liuyao': 0.5},
               'source_counts': src_counts,
               'source_share_max': 0.357,  # WHY 10/28
               'non_yiji_count': non_yizhi, 'non_liuyao_count': 14,
               'non_liuyao_min_required': 13, 'anchor_present_only': True,
               'pollution_low_only': True}

# ---------- 写盘 ----------
for cid in ORDER:
    with open(os.path.join(IN_DIR, cid + '.json'), 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
        f.write('\n')
gold_text = '\n'.join(json.dumps(golds[c], ensure_ascii=False) for c in ORDER) + '\n'
with open(os.path.join(OUT_DIR, 'test_gold.jsonl'), 'w', encoding='utf-8') as f:
    f.write(gold_text)
gold_sha = hashlib.sha256(gold_text.encode('utf-8')).hexdigest()
gold_bytes = len(gold_text.encode('utf-8'))

# ---------- 落盘回读扫描道 ----------
r_content, r_field, r_banned, r_frag = {}, {}, {}, {}
reread = {}
for cid in ORDER:
    card = json.load(open(os.path.join(IN_DIR, cid + '.json'), encoding='utf-8'))
    reread[cid] = card
    ch = [mk for s in all_strings(card) for mk in LEVEL1 + LEVEL2 if mk in s]
    fh = [b for k in all_keys(card) for b in FIELD_BLACKLIST if b in str(k)]
    bk = [k for k in all_keys(card) if k in BANNED_IN_CARD]
    text = json.dumps(card, ensure_ascii=False)
    fg = [fr for fr in fragments(golds[cid]['master_prediction']) if fr in text] + \
         [fr for fr in fragments(golds[cid]['outcome_record']) if fr in text]
    r_content[cid], r_field[cid], r_banned[cid], r_frag[cid] = ch, fh, bk, fg
    assert list(card.keys()) == INPUT_FIELDS and card == cards[cid]
    assert not ch and not fh and not bk and not fg
gold_lines = open(os.path.join(OUT_DIR, 'test_gold.jsonl'), encoding='utf-8').read().splitlines()
assert len(gold_lines) == 28
for line, cid in zip(gold_lines, ORDER):
    g = json.loads(line)
    assert g['id'] == cid and list(g.keys()) == GOLD_FIELDS

# ---------- 封存快照（活 method/ ＋与平台快照对勘） ----------
SNAP31 = os.path.join(R87, 'kb-snapshot-holdout31')
if os.path.isdir(SNAP31):
    shutil.rmtree(SNAP31)
shutil.copytree(os.path.join(BASE, 'method'), SNAP31)
for fn in os.listdir(SNAP31):
    if fn.startswith('METHOD-') and fn.endswith('.md'):
        os.remove(os.path.join(SNAP31, fn))


def file_hashes(root):
    out = {}
    for dp, _, fns in os.walk(root):
        for fn in fns:
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, root)
            out[rel] = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    return out


snap_hashes = file_hashes(SNAP31)
with open(os.path.join(R87, 'kb-snapshot-holdout31-sha256.txt'), 'w', encoding='utf-8') as f:
    for rel in sorted(snap_hashes):
        f.write(f"{snap_hashes[rel]}  {rel}\n")
assert len(snap_hashes) == 21, sorted(snap_hashes)
platform = file_hashes(os.path.join(R87, 'kb-snapshot'))
assert set(platform) == set(snap_hashes)
snap_diff = sorted(rel for rel in snap_hashes if snap_hashes[rel] != platform[rel])
assert snap_diff == ['SKILL.md', 'references/calibration.md'], snap_diff

report = {
 'set': 'holdout31', 'round': 87,
 'ruling': 'PREREG-ADDENDUM-r87.md 构成定版（PREREG.md §5 写死口径＋CYJ 专项复核主持裁定乙·锚点以盘体实载为准）',
 'adjudication': '本集为 R87-REV1（calibration 第十二节）判读集（集成先于封存、快照含集成集）；开封条件＝封存后首个平台全立轮（最早 R88）',
 'order': ORDER,
 'selection': {'liuren_wheel': LR_SEL, 'why': WHY_SEL, 'gsz': GSZ_SEL},
 'eligibility': eligibility,
 'fallback_triggered': fallback_log,
 'composition': composition,
 'strip_register': strip_register,
 'field_mapping_notes': field_mapping_notes,
 'why_supplement_matched': {cid: True for cid in WHY_SEL},
 'leak_notes': leak_notes,
 'scan_build_pass': {'content_hits_total': sum(len(v) for v in content_hits.values()),
                     'fieldname_hits_total': sum(len(v) for v in fieldname_hits.values()),
                     'banned_key_hits_total': sum(len(v) for v in banned_hits.values()),
                     'gold_fragment_hits_total': sum(len(v) for v in frag_hits.values())},
 'scan_reread_pass': {'content_hits_total': sum(len(v) for v in r_content.values()),
                      'fieldname_hits_total': sum(len(v) for v in r_field.values()),
                      'banned_key_hits_total': sum(len(v) for v in r_banned.values()),
                      'gold_fragment_hits_total': sum(len(v) for v in r_frag.values())},
 'gold_sha256': gold_sha, 'gold_bytes': gold_bytes, 'gold_lines': 28,
 'snapshot': {'dir': SNAP31, 'files': len(snap_hashes),
              'sha_list': os.path.join(R87, 'kb-snapshot-holdout31-sha256.txt'),
              'vs_platform_diff': snap_diff,
              'vs_platform_note': ('与平台快照 runs/round87/kb-snapshot 逐件对勘，差异恰为 '
                                   '{SKILL.md, references/calibration.md} 两文件（本轮 R87-REV1 '
                                   '集成：calibration 第十二节＋SKILL (t) 指针）')},
 'lr_gold_recovery': ('DA 七例课盘与金标自底本全文 cases_raw.json 原式逐字复原（邵先生曰段'
                      '与应验段全录、缘生谛编注剔除）；BY 七例课盘与正议／案验全文自原书页图'
                      '逐字复原（140dpi 渲染读图、课盘 250dpi 裁切复核；BY-022 案验段复玩'
                      '分析文尾照录承 h30 DA-038 例、BY-027 案验后复玩段与附议不入、逐项见'
                      '封存日志）；WHY 十例断语回原书〔判斷〕段逐字补录、结局自台账逐字；'
                      'GSZ 四例五要素回原书文字层复核全过、断语与结局自台账逐字'),
 'notes': ('判读归属：本集为 R87-REV1（calibration 第十二节）判读集。供给面：「本集为存量内'
           '最后一集」口径不适用——本集系 expansion 池台账存量＋r56/r57 台账存量组集；'
           '封存后六壬常规 eligible 余面 156（＝170－14，含 YX 3 不入轮取源序）、CYJ/CY '
           'fidelity 例外未用余面 46 例、WHY 资格余面 32、GSZ 建卡口径名单已尽取。'
           '前置核查三项结论见 precheck-holdout31-seat-r87.json（排除对不交叠、零复用'
           '交集为空、id 号段零冲突）。递补：同源台账序递补链全程未触发。'),
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'gold_sha256': gold_sha, 'gold_bytes': gold_bytes,
                  'order': ORDER, 'snapshot_files': len(snap_hashes),
                  'snapshot_diff': snap_diff}, ensure_ascii=False))
