# -*- coding: utf-8 -*-
"""R89 holdout33 组集封存席构建脚本（唯一名 seal_h33_r89.py）。
构成以 PREREG-ADDENDUM-r89.md（更正版）为准：T=28＝六壬14（DA 7＋BY 7）＋WHY 14。
体例照 holdout32 构建脚本（runs/round88/build_holdout32_r88.py）。
金标「案验复玩文尾」口径：master_prediction 取原卡大师断语全文，
outcome_record 取案验/复玩文尾全文；复盘议论与案验正文同段连写无分界者
整段照录并逐例登记（本轮 BY-043、BY-046 两例；BY-045 案验内占时对话同段照录）。
前置核查 (i)(ii) 本脚本复断言；(iii) 六壬 14 例式盘四课三传实载已逐例开原卡/
原书页图核毕（DA 回底本全文原式、BY 回原书页图，见封存日志 §三）。"""
import json, hashlib, os, shutil

B = '/home/hatch/workspace/divination/benchmark/phase3'
R89 = B + '/runs/round89'
OUT = B + '/holdout33'
os.makedirs(OUT + '/inputs', exist_ok=True)

INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status', 'anchors']
GOLD_FIELDS = ['id', 'master_prediction', 'outcome_record', 'tradition',
               'pollution', 'grade', 'grade_note', 'provenance',
               'license_status', 'redistributable']
LICENSE_ANCIENT = '古籍文本，内部研究用'
LICENSE_MODERN = '现代版权文本，内部研究用'

DA_SEL = ['DA-066', 'DA-067', 'DA-068', 'DA-070', 'DA-072', 'DA-073', 'DA-074']
BY_SEL = ['BY-039', 'BY-041', 'BY-042', 'BY-043', 'BY-044', 'BY-045', 'BY-046']
WHY_SEL = ['WHY-092', 'WHY-093', 'WHY-095', 'WHY-096', 'WHY-098', 'WHY-099',
           'WHY-100', 'WHY-103', 'WHY-104', 'WHY-106', 'WHY-107', 'WHY-108',
           'WHY-109', 'WHY-110']
ORDER = DA_SEL + BY_SEL + WHY_SEL
assert len(ORDER) == 28 and len(set(ORDER)) == 28
assert 'DA-069' not in ORDER and 'BY-040' not in ORDER

# 前置核查 (i)(ii) 复断言
used = set(json.load(open(R89 + '/used-ids-r89.json', encoding='utf-8')))
assert len(used) == 1276 and not (set(ORDER) & used)
assert 'LY-015' not in ORDER and 'LY-320' not in ORDER
assert 'DA-069' in used and 'BY-040' in used

# ---------- 池与台账 ----------
da_pool, by_pool = {}, {}
for fn in ('cases-a.jsonl', 'cases-b.jsonl'):
    for line in open(B + '/expansion12/liuren-duanan/' + fn, encoding='utf-8'):
        r = json.loads(line)
        da_pool[r['id']] = r
for line in open(B + '/expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl',
                 encoding='utf-8'):
    r = json.loads(line)
    by_pool[r['id']] = r
why_by = {}
for fn in ('runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json',
           'runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json'):
    d = json.load(open(B + '/' + fn, encoding='utf-8'))
    for e in d['entries']:
        why_by[e['provisional_id']] = e

# ---------- 资格断言 ----------
def lr_qual(cid):
    r = da_pool.get(cid) or by_pool.get(cid)
    if r is None:
        return False
    ok = (r.get('holdout_eligible') is True and r.get('contamination') == 'low'
          and r.get('outcome_grade') in ('A', 'A-low')
          and r.get('master_predictions') and r.get('outcome', {}).get('description'))
    if cid.startswith('BY-'):
        rv = r.get('review', {})
        ok = ok and rv.get('verdict') == 'seal' and rv.get('grade_final') == 'A-low' \
            and rv.get('contamination_final') == 'low'
    return bool(ok)

def why_qual(cid):
    e = why_by.get(cid)
    if e is None:
        return False
    ch = e['input_fields']['chart']
    return (e.get('pollution') == 'low' and e.get('anchor_presence') == 'present'
            and not e.get('anchor_missing') and bool(e.get('outcome_record'))
            and bool(ch.get('ben_gua')) and bool(ch.get('chart_lines_top_to_bottom')))

for cid in DA_SEL + BY_SEL:
    assert lr_qual(cid), cid
for cid in WHY_SEL:
    assert why_qual(cid), cid

# ---------- DA 课盘与金标（回底本全文 cases_raw.json 复原；转储
# runs/round89/dump-da-raw-h33-r89.txt 在册） ----------
DA_CHART = {
 'DA-066': {
  'ke_name': '四绝',
  'tianpan': '子合、丑朱、寅蛇、卯贵、亥勾、辰后、戌青、巳阴、午玄、未常、申虎、酉空（地盘支→上神天将；原式方阵：合朱蛇贵／子丑寅卯、勾亥・辰后、青戌・巳阴、酉申未午／空虎常玄）',
  'sike': '辰（后）酉、酉（空）寅、丑（朱）午、午（玄）壬（四课格原式：上行辰酉丑午／下行酉寅午壬，天将后空朱玄）',
  'sanchuan': '财甲午（玄）、官辛丑（朱）、父丙申（虎）',
  'master_prediction': '邵先生曰：此课名四绝，且干支自刑，又初中六害，其不利有三。一者居偏室无正位，二者妻宫不利，三者眼不明。因父坟不利，皆是白蚁，左畔已虚空矣。前程非惟不远，又且寿夭。九年将屋基作田园，家破碎，贵贱皆因酒而败也。',
  'outcome_record': '邵闻先生言，欲启父坟。因兄弟众，多不肯行。妻不生子，常有血气。至辛亥年病眼，男女皆因酒败。乙卯年众拆屋，一半作田，一半作园，邵居于店屋。戊午身丧。己未，兄弟启父坟，骸骨皆为蚁食矣。',
  'tail_note': '文尾处置：应验段为止，爱函按不入。课名四绝自断语原文「此课名四绝」。'},
 'DA-067': {
  'ke_name': '底本未载',
  'tianpan': '寅合、卯朱、辰蛇、巳贵、丑勾、午后、子青、未阴、申玄、酉常、戌虎、亥空（地盘支→上神天将；原式方阵：合朱蛇贵／寅卯辰巳、勾丑・午后、青子・未阴、亥戌酉申／空虎常玄）',
  'sike': '申（玄）亥、亥（空）寅、巳（贵）申、申（玄）壬（四课格原式：上行申亥巳申／下行亥寅申壬，天将玄空贵玄）',
  'sanchuan': '财巳（贵）（原式旁标◎）、子壬寅（合）（原式旁标⊙）、兄己亥（空）',
  'master_prediction': '邵先生曰：此课与前课大不同。干支皆受上神之生，学堂加干，贵人发用，尽可取功名。但嫌贵空，又学堂为玄武所滞，非科第中人。日上得申长生，却即去生寅，初巳贵人作财，只运司发解，而不能及第。初任管铜铁，次任管坑冶，三任水船官而止。',
  'outcome_record': '邓果初任铸钱有功。次任坑冶司检踏官。再得明州船场，归家而死。',
  'tail_note': '文尾处置：断语／应验全文照录，爱函按不入。'},
 'DA-068': {
  'ke_name': '底本未载',
  'tianpan': '午龙、未空、申虎、酉常、巳勾、戌玄、辰合、亥阴、子后、丑贵、寅蛇、卯雀（地盘支→上神天将；原式方阵：龙空虎常／午未申酉、勾巳・戌玄、合辰・亥阴、卯寅丑子／雀蛇贵后）',
  'sike': '申（虎）未、未（空）午、未（空）午、午（龙）戊（四课格原式：上行申未未午／下行未午午戊，天将虎空空龙）',
  'sanchuan': '官甲寅（蛇）（原式旁标⊙）、父戊午（龙）、父戊午（龙）',
  'master_prediction': '邵先生曰：司户今无正位，必主上司责罚而别有迁改。寅乃今日之鬼，鬼生午火，午乃今日阳刃煞，且是天鬼，在于中末传，与支上未合，亦忧宅眷人口有死者。',
  'outcome_record': '汪乃饶州人，为衢州司户，起得此课。后果宅中患时气，遂死三人。十月间，因提举检踏常平仓，事露，遂致贬斥。',
  'tail_note': '文尾处置：应验段照录，段中缘生谛注（时气、提举常平司、事露释义）与爱函按不入。'},
 'DA-070': {
  'ke_name': '底本未载',
  'tianpan': '丑蛇、寅朱、卯合、辰勾、子贵、巳青、亥后、午空、未虎、申常、酉玄、戌阴（地盘支→上神天将；原式方阵：蛇朱合勾／丑寅卯辰、贵子・巳青、后亥・午空、戌酉申未／阴玄常虎）',
  'sike': '未（虎）亥、亥（后）卯、申（常）子、子（贵）乙（四课格原式：上行未亥申子／下行亥卯子乙，天将虎后常贵）',
  'sanchuan': '财己未（虎）、兄乙卯（合）、父癸亥（后）',
  'master_prediction': '邵先生曰：此课身坐贵人，又来生日，三传又是木局，乙木生亥旺卯墓未，自墓传旺，自旺传长生，必由穷途渐至荣显至侍从。先丧妻，害眷属。须先纳兄弟一子。后一小妻，大有财物，寿近九十矣。',
  'outcome_record': '刘此时为朝议郎，辛亥丧妻。乙卯丧子，继兄子为子。庚申又娶妻，其时年五十四，妻三十九，携数万贯钱来嫁。后直至吏部侍郎，八十七而终。',
  'tail_note': '文尾处置：断语／应验全文照录；爱函按、缘生谛注（持橐释义）不入。'},
 'DA-072': {
  'ke_name': '底本未载',
  'tianpan': '丑青、寅勾、卯合、辰朱、子空、巳蛇、亥虎、午贵、未后、申阴、酉玄、戌常（地盘支→上神天将；原式方阵：青勾合朱／丑寅卯辰、空子・巳蛇、虎亥・午贵、戌酉申未／常玄阴后）',
  'sike': '丑（青）巳、巳（蛇）酉、寅（勾）午、午（贵）辛（四课格原式：上行丑巳寅午／下行巳酉午辛，天将青蛇勾贵）',
  'sanchuan': '官丁巳（蛇）、父丑（青）（原式旁标◎）、兄辛酉（玄）（原式旁标⊙）',
  'master_prediction': '邵先生曰：官星临日，初传助之，谓之催官符。官星又作贵人，辛藏于戌，主庚戌年及第。嗣后便丁父母服，服满赴任，见禄而终，酉禄加空亡之上故也，止于五十四矣。兄弟相害，因争分居而大生不足。又不得子息力。',
  'outcome_record': '何果庚戌及第，壬子丁母忧，乙卯丁父忧，庚申赴利州推官，辛酉五十三岁八月十四日卒。先是戊午年，兄弟争家财，四次入官，估劄以死。子三人，长十三岁，次者九岁，三者七岁，皆再娶所生。',
  'tail_note': '文尾处置：断语照录，断语末同段缘生谛注（嗣后释义）不入；应验全文照录，爱函按不入。'},
 'DA-073': {
  'ke_name': '底本未载',
  'tianpan': '巳空、午虎、未常、申玄、辰青、酉阴、卯勾、戌后、亥贵、子蛇、丑朱、寅合（地盘支→上神天将；原式方阵：空虎常玄／巳午未申、青辰・酉阴、勾卯・戌后、寅丑子亥／合朱蛇贵）',
  'sike': '巳（空）巳、巳（空）巳、未（常）未、未（常）丁（四课格原式：上行巳巳未未／下行巳巳未丁，天将空空常常）',
  'sanchuan': '兄丁巳（空）、财庚申（玄）、父甲寅（合）',
  'master_prediction': '邵先生曰：此课主来年发解，只是不及第。又妻为猿怪所迷。四年后移居妻家，因妻家子死，并为一家住。又合主科第，授推官，将满，丧妻。再授财赋官，到任七月，而终于奴婢之手，不见子息。一边动哀，一边子息喜事至。',
  'outcome_record': '童果次年得解，至冬赴省。其家近山，妻为猿怪所迷，终日歌笑不已，邻人记得先生言，治之而愈。四年遂移妻家居；七年，妻父止一子而亡，遂与童共居。戊辰科，童果及第，授南安州司李，任满妻叶氏亡。再授临安楼务官，到任七月，二子归秋试。童死，只有五六奴婢措置后事。及子息来扶丧，次子得第七名解矣。',
  'tail_note': '文尾处置：断语照录，断语末同段缘生谛注（发解、及第释义）不入；应验照录，应验末缘生谛注（赴省、楼务释义）与爱函按不入。'},
 'DA-074': {
  'ke_name': '底本未载',
  'tianpan': '卯朱、辰合、巳勾、午青、寅蛇、未空、丑贵、申虎、酉常、戌玄、亥阴、子后（地盘支→上神天将；原式方阵：朱合勾青／卯辰巳午、蛇寅・未空、贵丑・申虎、子亥戌酉／后阴玄常）',
  'sike': '子（后）寅、寅（蛇）辰、辰（合）午、午（青）庚（四课格原式：上行子寅辰午／下行寅辰午庚，天将后蛇合青）',
  'sanchuan': '官壬午（青）（原式旁标⊙）、父庚辰（合）、财戊寅（蛇）',
  'master_prediction': '邵先生曰：日上发传，退入支上，又是顾祖，末又见本命入宅。须是差出，经过乡里而有是非，寅为支马故主经过，又是本命，主自蒙差出，而后经乡里也；不然须是有甚不到处。不合日上退归本命入宅，为蛇所扰，又是共屋人之事也。',
  'outcome_record': '主簿族大房多，因争分家财，遂告至台部。十一月文书下，令知州差人押归，分折了再赴任。陈被押归，分未及半，因房产又入状监司，奏罢关押，始分成。',
  'tail_note': '文尾处置：断语照录，断语末同段缘生谛注（差出、共屋人释义）不入；应验照录，应验末缘生谛注（分折了释义）与爱函按不入。底本式头注「课同120」。'},
}
assert set(DA_CHART) == set(DA_SEL)

# ---------- BY 课盘与金标（回原书页图逐字复原；200dpi 通读＋300dpi
# 疑字/课盘裁切复核，件存 runs/round89/lr-pages-h33-seat/） ----------
# 原书天将「元」＝玄武省字，照录并于方阵注标明（承 h31/h32 注法）；
# BY-042 四课将名第三字原书作「玄」全字，照录并注。
BY_CHART = {
 'BY-039': {
  'ke_name': '末助初传二贵皆空初遭夹克',
  'tianpan': '未勾、申合、酉朱、戌蛇、午青、亥贵、巳空、子后、丑阴、寅元、卯常、辰白（地盘支→上神天将；原式方阵：勾合朱蛇／未申酉戌、青午・亥贵、空巳・子后、辰卯寅丑／白常元阴；元＝玄武，原书省字照录）',
  'sike': '巳（空）卯、卯（常）丑、亥（贵）酉、酉（朱）丁（四课格原式：上行巳卯亥酉／下行卯丑酉丁，天将空常贵朱）',
  'sanchuan': '财酉（朱）、官亥（贵）、子丑（阴）',
  'master_prediction': '初传酉贵旬空，中传亥贵坐空，如考试已经蒙推荐被人挽越，误报同名之人，是是虚喜而已。此课占财夹克，初去不利，并遭口舌，中有凑合之巧，末助初财，又逢天喜，终局更佳，但所得终无实象耳。',
  'outcome_record': '正时未加巳，土中有火，支上木土，支阴见火，断为掘煤之事。果初不见碳，后始有获。',
  'tail_note': '文尾处置：正议／案验全文照录。「是是虚喜」与案验「碳」经 300dpi 页图复核为原书字形，照录不改。'},
 'BY-041': {
  'ke_name': '闭口卦体鬼临三四',
  'tianpan': '寅合、卯朱、辰蛇、巳贵、丑勾、午后、子青、未阴、申元、酉常、戌白、亥空（地盘支→上神天将；原式方阵：合朱蛇贵／寅卯辰巳、勾丑・午后、青子・未阴、亥戌酉申／空白常元；元＝玄武，原书省字照录）',
  'sike': '辰（蛇）未、未（阴）戌、巳（贵）申、申（元）壬（四课格原式：上行辰未巳申／下行未戌申壬，天将蛇阴贵元）',
  'sanchuan': '财巳（贵）、子寅（合）、禄亥（空）',
  'master_prediction': '丑时作闭口，无情者不得逞刁。绝神发用，利于了结，不可深交。鬼临三四，为蜮不止一人。然坐而不动，以受干上之生，彼自无能为也。初财逢劫，破耗已见，无庸追悔，中传六合生财，外有贵人相助，以补其空。',
  'outcome_record': '此因初交不慎，被其拖累，其事未终，将有骗局，理亏自止，贵人之助亦验。',
  'tail_note': '文尾处置：正议／案验全文照录；案验后「问／曰」课理问答非本案断验，不入。'},
 'BY-042': {
  'ke_name': '太阳照武末助初传催官使者交车相合',
  'tianpan': '戌朱、亥合、子勾、丑青、酉蛇、寅空、申贵、卯白、辰常、巳元、午空、未后（地盘支→上神天将；原式方阵：朱合勾青／戌亥子丑、蛇酉・寅空、贵申・卯白、未午巳辰／后空元常；元＝玄武，原书省字照录）',
  'sike': '亥（合）午、午（阴）丑、巳（玄）子、子（勾）己（四课格原式：上行亥午巳子／下行午丑子己，天将合阴玄勾；四课将名第三字原书作「玄」全字，与他处省字「元」并存，照录）',
  'sanchuan': '父巳（元）、兄戌（朱）、鬼卯（白）',
  'master_prediction': '玄武乘巳，巳为太阳，名太阳照武。末传虎乘干鬼，为催官使者。三传巳戌卯，又曰铸印。此课利于干官擒贼。然水遭夹克，铸印不成。禄马逢空，有名无实。且交车合而上下冲，合中必破。初传夹克，亦不由己，尚以恬静为安。但末助初生，恐有文书相催耳。',
  'outcome_record': '秋季楚北胡中丞传檄敦请入幕，县禀远行。张观察复信寄陕西相邀，自揣蹇劣不堪录用，而兴安诸徒维系亦切，遂婉谢之，后数月中丞丁忧。',
  'tail_note': '文尾处置：正议／案验全文照录。'},
 'BY-043': {
  'ke_name': '干支禄马三传递生日禄临支宾主相刑',
  'tianpan': '寅合、卯勾、辰青、巳空、丑朱、午白、子蛇、未常、申元、酉阴、戌后、亥贵（地盘支→上神天将；原式方阵：合勾青空／寅卯辰巳、朱丑・午白、蛇子・未常、亥戌酉申／贵后阴元；元＝玄武，原书省字照录）',
  'sike': '寅（合）巳、巳（空）申、亥（贵）寅、寅（合）丙（四课格原式：上行寅巳亥寅／下行巳申寅丙，天将合空贵合）',
  'sanchuan': '禄巳（空）、官寅（合）、财亥（贵）',
  'master_prediction': '日马加干，日禄加支，为富贵课。兼以三传递生，正贵入传课，必售无疑。日临支而克支，为赘婿，寄考之象也。干支相刑，有德化之，虽小有言，无碍于考，然终不免俯就于人。而发用空上逢空，亦难成实。不如寅木长生为父母之邦，与正贵相合，仍归本籍为妙。',
  'outcome_record': '本年寄籍，众口沸腾，已经调和，县府考起，院试报罢。次年亦如之。戊午年回籍入泮，时年二十四岁，两贵拱年故也。此课不从赘婿长生着想，而况干为外，支为家，则误矣。',
  'tail_note': '文尾处置：同段照录——案验段尾「两贵拱年故也……则误矣」为复盘议论与案验正文同段连写无分界，整段照录。书自注原断着眼有误，断/验俱全可分离（池卡复核 notes 同口径）。'},
 'BY-044': {
  'ke_name': '干支禄马',
  'tianpan': '申合、酉勾、戌贵、亥空、未朱、子白、午蛇、丑常、寅元、卯阴、辰后、巳贵（地盘支→上神天将；原式方阵：合勾贵空／申酉戌亥、朱未・子白、蛇午・丑常、巳辰卯寅／贵后阴元；元＝玄武，原书省字照录）',
  'sike': '寅（元）亥、亥（空）申、巳（贵）寅、寅（元）壬（四课格原式：上行寅亥巳寅／下行亥申寅壬，天将元空贵元）',
  'sanchuan': '财巳（贵）、父申（合）、禄亥（空）',
  'master_prediction': '问：日马加干，日禄加支，又作六合，两贵夹拱丑命，正贵逢太岁发用，此真富贵课也，况日禄加支而受生，此房应大利于人。曰：课名遥克，马逢月建，主动而远寻也。干上寅脱我，支申作长生，是宜去此而就彼也。参议：问：日禄归支，岂非反桴乎？曰：遥克用在二课，又名近射，远而不远也。况四下生上，外吉内凶，不可回家。申支长生在中传，末传日禄遇旬空，是宜中途而止也。问：课名富贵何兆？曰：弹射力轻，辰加丑，主藏名。又逢日墓临命，富贵不显，子旺而生太岁，禄空而冲太岁，不利身而利后人。贵人作财，巳为四数，当有顶戴四人寄书相迎，仍以舌耕为业。正时酉鸡生日，巳火贵人发传，丑日三合，家丁必来。巳为荆楚，两贵拱命，本省虽有贵人远引，末传旬空，恋生不能就。',
  'outcome_record': '癸丑日兴安旧寓家丁果携生监四人书到次日甲寅即行。冬季湖北中丞、观察俱有信邀，未就。癸亥年贼至兴安，携眷归家，无以为生，仍设砚于中途西南方。',
  'tail_note': '文尾处置：断语＝正议全文＋参议问答（占时答问、属原断）并入，grade_note 登记；案验全文照录。'},
 'BY-045': {
  'ke_name': '干支禄马闭口卦体',
  'tianpan': '寅合、卯朱、辰蛇、巳贵、丑勾、午后、子青、未阴、申元、酉常、戌白、亥空（地盘支→上神天将；原式方阵：合朱蛇贵／寅卯辰巳、勾丑・午后、青子・未阴、亥戌酉申／空白常元；元＝玄武，原书省字照录）',
  'sike': '申（元）亥、亥（空）寅、巳（贵）申、申（元）壬（四课格原式：上行申亥巳申／下行亥寅申壬，天将元空贵元）',
  'sanchuan': '财巳（贵）、子寅（合）、禄亥（空）',
  'master_prediction': '日禄加支，日马加干，为富贵课，兼之太岁、天诏加命，必主升迁。但四课不全，未能满任。正贵旬空，幕贵闭口，贼符游都加干二课，印绶逢岁月二破，必因贼到而逃往家乡。盖天空主逃亡而干神又归支也。',
  'outcome_record': '时拟次日摄篆，余曰：发用逢空，出旬方可。曰：已奉札矣。奉札亦不行。果至乙巳日到任，次年春贼至，弃官逃于家。',
  'tail_note': '文尾处置：正议全文照录；案验全文照录——案验内「余曰／曰」为占时次日对话，与案验正文同段连写，整段照录。天盘方阵与课例四十八（BY-041）同式，原书页图直核照录。'},
 'BY-046': {
  'ke_name': '传遇三奇互旺皆旺前后引从首尾相见',
  'tianpan': '午合、未勾、申青、酉空、巳朱、戌白、辰蛇、亥常、子元、丑阴、寅后、卯贵（地盘支→上神天将；原式方阵：合勾青空／午未申酉、朱巳・戌白、蛇辰・亥常、卯寅丑子／贵后阴元；元＝玄武，原书省字照录）',
  'sike': '戌（白）酉、酉（空）申、丑（阴）子、子（元）壬（四课格原式：上行戌酉丑子／下行酉申子壬，天将白空阴元）',
  'sanchuan': '官丑（阴）、子寅（后）、子卯（贵）',
  'master_prediction': '三传乙丙丁，兼丑为旬奇发用，酉为日奇加支，真三奇格也。初末引从丑命，两贵夹拱卯年，初传天喜，中末丁驿二马，原为迁移吉象。然干支皆旺，首尾相见，现在却不能迁，即暂有所出，亦去而复来，惟待卯年丁马冲破支网，始可动，亦不在下埠。',
  'outcome_record': '卯年寅月自江西至湖南，又走荆襄，至谷城，历郫阳，后馆于秦之兴安府。屡蒙大宪拔擢，无才应聘，福甚薄矣。何奇之有？但以流离之子，委琐不堪，而诸生济济，自各府县来者，当以数百里计。庸夫得此，亦颇不辱，鸿飞十年，又应一旬周遍之义，神明指示昭然，初念不及此，而事后始知也。',
  'tail_note': '文尾处置：同段照录——案验后半复盘议论（「何奇之有」以下）与案验正文同段连写无分界，整段照录。'},
}
assert set(BY_CHART) == set(BY_SEL)

# ---------- WHY 断语补录（回原书〔判斷〕段逐字，visual 转录；
# 页图 runs/round89/why-pages-h33-seat/，150dpi 通读＋跨页缝/疑字裁切复核） ----------
WHY_SUPPLEMENT = {
 'WHY-092': ('印刷p124–125', '〔判斷〕官運：以官鬼為用神。世在第五爻，五爻為領導的爻位，世爻臨之，再加上官鬼旺相，為有官之象。但三爻官鬼酉金動化回頭剋，又是丟官之象。故斷其原有官職，現在沒有了。財運：以妻財為用神。乍一看，財爻持世，日月俱是財星，財爻很旺，當斷其財運好才對。但子孫午火伏藏，日月不生，又被父母子水發動剋之，財源枯竭，初爻妻財丑土月破日破，是無財之象。父母子水雖然不旺，但得官鬼酉金生助，官鬼為政府，臨勾陳，古為衙門，今為派出所，公安局，是政府部門斷了他的財源。初爻為事物的開端，財爻臨之月破，是一起步就破了財。臨青龍，青龍為酒色，破財與此有關。所以我斷其今年開始經商，但剛一開始就被公安局斷了其財路，一定是做的不正當生意。', '分节标题（官運／財運）为原书〔判斷〕内结构，照录。'),
 'WHY-093': ('印刷p126', '〔判斷〕本人安危：以世爻為用神。世爻得月生扶，又有動爻發動生之，子孫持世，無災之象。不過元神動而化退，生世爻力量減弱，有輕微的病。世在第五爻，五爻為五官，金為牙，應有牙痛。財運：以財爻為用神。用神雖然伏藏，但日辰幫扶，忌神衰，且動而化退，財運尚可。世爻為財爻元神，靜而不動，只有發動才能成連續相生，減忌神之剋，因此本人為奔波，辛苦求財。家屬的安危：妻財為妻子，月剋，忌神發動剋之，又代表疾病的官鬼臨應，應為妻位，妻子會生病。二爻為子宮，臨勾陳，勾陳為腫塊，肌瘤，妻子會得子宮肌瘤。', '分节标题（本人安危／財運／家屬的安危）为原书〔判斷〕内结构，照录。'),
 'WHY-095': ('印刷p128', '〔判斷〕本人安危：以世爻為用神。世爻被日月剋傷不吉。世在三爻，三爻為胃，土也主胃，忌神在二爻為腸，本年要得腸胃病。財運：以財爻為用神。財爻雖然持世，但被日月剋傷，元神又不上卦。財運不佳。工作：以官鬼為用神。官鬼酉金月破日破，事業運氣也不好。', '分节标题（本人安危／財運／工作）为原书〔判斷〕内结构，照录。'),
 'WHY-096': ('印刷p129', '〔判斷〕本人安危：以世爻為用神。世爻得月建生扶為旺相。但忌神動而剋世，不吉。卦在震宮，震為足，世在二爻又為足的爻位，本年不是腿腳受傷就是腿腳得病。財運：以財爻為用神。財爻持世，得月生扶為旺相，官鬼為工作，動而長生財爻，工資收入不錯。但子孫空亡，忌神寅木發動，想發大財很難。官運：以官鬼為用神。官鬼得日辰比扶動化進神，看似工作蒸蒸日上，晉昇之象，然而，官鬼臨應應為他人，與己何干？官鬼在第五爻，五爻為領導，乃是領導有變動之象。', '分节标题（本人安危／財運／官運）为原书〔判斷〕内结构，照录。'),
 'WHY-098': ('印刷p168–169', '〔判斷〕以父母為用神。父母午火在二爻，入墓於日辰。日為兄弟，兄弟為牆壁，說明是一個被圍牆圍著的房子。主卦六沖，不能藏風聚氣。子孫申金在三爻和勾陳一起發動剋世，三爻為門，申與西南相對，勾陳為修造、建築，西南方向有建築施工影響自己的官運。月為妻財絕地，日剋妻財，妻財子水入墓於暗動之爻兄弟辰土為休囚。卦中雖有子孫發動連續相生，但子孫申金空亡，妻財原本無根，必因風水不好而破財。妻財子水臨五爻被剋，五爻為道路，白虎主交通事故，乃因交通事故破財。', ''),
 'WHY-099': ('印刷p169–170', '〔判斷〕以父母為用神，二爻為宅爻。父母巳火伏在二爻之下，乃是宅下伏宅，房子重疊的信息。說明所測的房子是帶有地下室的。二爻與日相合，父母巳火與月相合，合為重疊之象，房子上有房子，是樓房的信息。二爻月破，但與日相合月破被解，因此房子原有裂縫，後來進行修理過。父母休囚，房子不是新的。應爻發動化出父母午火，應為他人，父母主房子，是別人住過騰出來的房子。白虎臨官鬼在二爻發動，內卦反吟，住房風水不好。宅爻臨白虎動而剋應爻，官鬼和白虎都主疾病，應為他人，受剋，原來的住戶一定病災連連不斷。應也為妻位，住此房子，不利於妻子。', ''),
 'WHY-100': ('印刷p170–171', '〔判斷〕以父母為用神，同時參看二爻。卦中不見火，父母酉金臨玄武，玄武主暗中、暗淡，火為光明，說明現在住的地方光線不好，很少能見到太陽。二爻官鬼丑土剋五爻兄弟亥水，二爻為宅，五爻為人，此房住人不利。官鬼持世，臨騰蛇，官鬼為煩惱，騰蛇為坐臥不安，說明住此房子，人常常心煩意亂，不安定。官鬼在二爻臨朱雀，朱雀為口舌，住此房，口舌官司難免。妻財午火休囚不上卦，飛神絕之，家中不見妻子，老婆離家出走。妻財臨午火，事情發生在午月。地火明夷為坎宮，坎為水，為尿，為血液。妻財伏在三爻被飛神剋之，日辰剋之，三爻為子宮的爻位，老婆有婦科病，月經不調。', ''),
 'WHY-103': ('印刷p173–174', '〔判斷〕以父母為用神參看二爻。初爻父母辰土發動化回頭剋，臨勾陳，勾陳主建築工程，飯店有被拆的危險。五爻發動剋二爻，五爻為路，二爻為店，又為父母之元神，怕是因拓寬馬路飯店被拆。外卦反吟，反吟有反復之意，此店不光經營過飯店，還應經營過別的。妻財卯木伏藏雖得月生，但被兄弟發動剋制，子孫空亡又入日墓，此店很難經營獲利。應臨二爻為應入飛宅，此店不是有人要租就是有人要買。一定要抓住機遇把店轉讓出去。', ''),
 'WHY-104': ('印刷p174–175', '〔判斷〕以父母為用神參看二爻。二爻月破，得父母未土動而合破，店面不是很好，曾修補過。臨朱雀，朱雀為口，卦在兌宮，兌也為口，所經營的店與飲食有關。父母臨應爻，應為他人，店屬於別人，是租來的。妻財卯木雖然伏藏，但得月生扶，飛神空亡，空下伏神易於引拔，同時子孫亥水暗動生之，此店收入還可以。但應上父母未土發動，使財爻入墓，出租店的人要租金要的很緊。目下未土空亡，明年丁丑沖實未土，房價必漲。到時必很難再經營下去。', ''),
 'WHY-106': ('印刷p177–178', '〔判斷〕以父母為用神，參看二爻。父母子水伏於世爻之下所問房子是自己的私產。臨白虎，白虎主道路，房子緊鄰路邊。父母子水月破，房子有裂縫，不是很新。二爻為宅爻，暗動生世上妻財，此宅利於財運。子孫巳火暗動於五爻官鬼申金相合，五爻為尊位，領導的爻位，子孫代表子女，五爻代表官運，子女中有人當官。臨勾陳，勾陳為衙門，說明是在機關單位工作。三爻為門，空亡，門有空隙，是有柵欄的。臨青龍，大門修得很豪華。卦逢六合，本人交際廣。', ''),
 'WHY-107': ('印刷p178–179', '〔判斷〕以父母為用神，參看二爻。二爻為官鬼，官鬼有政府、公家等意思，住房是從工作單位得到的宿舍。四爻發動合二爻，上合下，為樓房。兄弟戌土臨青龍，發動化出父母，青龍主裝修，父母為房子，說明房子已經裝修。父母巳火空亡，說明還沒有人住。父母在初爻，初爻為一層，臨火，火主二數，房子不是在一層就是在二層。父母為火臨空亡，火為光，光線不足。三爻為門，為臥室，兄弟臨之，其意更強，臨玄武，玄武主暗，是室內照不到陽光的信息。六爻官鬼臨勾陳動而剋三爻兄弟，寅木對應於東北，勾陳為突出，土地的意思，說明東北方向有個土坡擋住了房間的采光。五爻生二爻不吉，官鬼臨白虎居二爻，官鬼和白虎都有疾病的意思，此宅不利於住人，得此房子之人易生疾病。官鬼寅木在六爻發動剋世，六爻為頭，木主痛，定有頭疼病。世在三爻被剋，下伏子孫，子孫主生殖器，臨玄武，玄武主曖昧，難言之隱，生殖器有毛病。初爻父母暗動，初爻為心事，父母主房子，動主變化，有換房子的打算。', ''),
 'WHY-108': ('印刷p179–180', '〔判斷〕以父母爻為用神，兼看二爻。世爻為坐山，父母午火持世，為坐南朝北之宅。二爻臨官鬼，官鬼主公家、政府，所住房子為公家的。財臨日生之，又父母持世，已用錢買下歸自己所有。日辰合二爻宅爻，重疊之象，為樓房。卦得六沖，不吉之象，此宅不宜住人。朱雀臨官鬼寅木入宅，寅木為火長生之地，朱雀又主火災，故斷此宅發生過火災。三爻為門，兄弟臨之，兄弟也主門，三爻與月建作合，又臨勾陳為勾絆之象，斷其門不好用。五爻為人，子孫申金空亡臨白虎，白虎主流產、墮胎，斷其若已生下小孩住進此宅則無事，若未生小孩住進去後，必有流產之事發生。沖卦乃不久之象，二爻為宅受月建之剋，又被卦中子孫申金沖剋，斷此宅已住不久，將要拆掉。卦中沖剋宅爻的六親子孫申金在第五爻，五爻主道路，子孫也主道路，臨白虎，白虎也主道路，故斷此宅拆掉後不是重新蓋樓，而是要擴建馬路，占了此地，將來這座樓所在的位置將變成道路。因申金空亡，斷此事將發生在一九九八戊寅年的申月。', ''),
 'WHY-109': ('印刷p192', '〔判斷〕以妻財為用神。卦中妻財子水兩現，以發動妻財子水為用神。妻財得月生扶，動而化回頭生為旺相。忌神戊土雖然動而剋用，但空亡，剋用神力量減弱，大有治癒的希望。用神為水被剋，水主血液、腎、尿等，官鬼在二爻，二爻為胎位，臨白虎，白虎主流產，忌神臨青龍，青龍主生孩子等，綜合判斷為生孩子引起的尿方面的疾病。', ''),
 'WHY-110': ('印刷p193', '〔判斷〕以世爻為用神。世爻與日相同，月建不剋為旺相。但元神休囚，仇神獨發，疾病難以下治癒。仇神動而化出官鬼，神兆機於動，此是判斷病因的關鍵。二爻為宅，亥水為西北，臨玄武，玄武主陰氣，是住房西北方向有陰氣入宅引起的。具體病症的判斷，仇神動剋元神，元神在四爻，四爻為心臟的爻位，午火又主心臟，是心慌。妻財伏藏，食欲不振。', '「疾病難以下治癒」为原书字形，照录不改。'),
}
assert set(WHY_SUPPLEMENT) == set(WHY_SEL)

# ---------- 建卡与金标 ----------
cards, golds = {}, {}
strip_register, field_mapping_notes = {}, {}

for cid in DA_SEL + BY_SEL:
    r = da_pool.get(cid) or by_pool.get(cid)
    prov = (f"{r['provenance']['work']}（{r['provenance']['edition']}）·{r['provenance']['page']}"
            f"；底本为用户提供，redistributable=false")
    if cid.startswith('DA-'):
        d = DA_CHART[cid]
        anchors = {'asked_at': r['asked_at'], '课名': d['ke_name'],
                   '天盘': d['tianpan'], '四课': d['sike'], '三传': d['sanchuan'],
                   '课盘原文来源': '底本全文 cases_raw.json 原式照录（天盘方阵／四课格／三传栏）'}
        gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low；'
                 '课式头四要素 present（R84 核查台账）；课盘经本席回底本全文逐字复原；'
                 '金标断语／结局回底本全文邵先生曰段与应验段逐字照录（池卡摘录为节录，'
                 '不作金标准据）；' + d['tail_note'] + r['grade_note'])
    else:
        d = BY_CHART[cid]
        anchors = {'asked_at': r['asked_at'], '课名': d['ke_name'],
                   '天盘': d['tianpan'], '四课': d['sike'], '三传': d['sanchuan'],
                   '课盘原文来源': '原书页图课盘直录（本席200dpi渲染读图、课盘与疑字300dpi裁切复核，件存 runs/round89/lr-pages-h33-seat/）'}
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
    strip_register[cid] = ['master/master_predictions/outcome/outcome_grade/contamination/'
                           'contamination_rationale/grade_note/holdout_eligible/review'
                           '（池卡管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = ('subject/question←池卡 subject/question_or_topic 逐字；'
                                'anchors←asked_at 逐字＋本席回原文复原课盘；'
                                'setting/provenance←池卡 provenance 组写')

for cid in WHY_SEL:
    e = why_by[cid]
    ch = e['input_fields']['chart']
    anch = {'asked_at': e['input_fields']['asked_at']}
    for k, v in ch.items():
        anch[k] = v
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
        'anchors': anch}
    loc, mp, extra = WHY_SUPPLEMENT[cid]
    head = '断语台账原录为要旨摘录，本轮回原书《六爻分类占验技法》〔判斷〕段逐字补录全文'
    gnote = (f"A（主持口径）；{head}（{loc}，扫描本 transcription=visual）；"
             f"结局自台账 outcome_record 逐字照录，并与原书應驗情況核对相合。"
             + (extra if extra else ''))
    golds[cid] = {'id': cid, 'master_prediction': mp,
                  'outcome_record': e['outcome_record'],
                  'tradition': 'liuyao', 'pollution': 'low', 'grade': 'A',
                  'grade_note': gnote,
                  'provenance': e['source'], 'license_status': LICENSE_MODERN,
                  'redistributable': False}
    strip_register[cid] = ['master_prediction（台账原录为要旨摘录、回原书补录件）/outcome_record/'
                           'pollution_note/dedup_check/filters/grade_note（台账管理与金标侧字段，不入输入卡）']
    field_mapping_notes[cid] = 'anchors←台账 input_fields.chart 全列逐字；context←asked_at＋question＋原书章节定位组写'

for cid in ORDER:
    assert list(cards[cid].keys()) == INPUT_FIELDS, cid
    assert list(golds[cid].keys()) == GOLD_FIELDS, cid
    assert cards[cid]['redistributable'] is False and golds[cid]['redistributable'] is False

# ---------- 落盘 ----------
for cid in ORDER:
    with open(f'{OUT}/inputs/{cid}.json', 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=1)
        f.write('\n')
lines = [json.dumps(golds[cid], ensure_ascii=False) for cid in ORDER]
gold_bytes = ('\n'.join(lines) + '\n').encode('utf-8')
with open(OUT + '/test_gold.jsonl', 'wb') as f:
    f.write(gold_bytes)
sha = hashlib.sha256(gold_bytes).hexdigest()

# ---------- 封存快照（method 活树 21 件；METHOD-* 登记件不入） ----------
SNAP = R89 + '/kb-snapshot-holdout33'
os.makedirs(SNAP + '/references', exist_ok=True)
os.makedirs(SNAP + '/tools', exist_ok=True)
snap_files = ['SKILL.md', 'VALIDATION.md', 'VERIFY-LOG.txt']
snap_files += ['references/' + fn for fn in sorted(os.listdir(B + '/method/references'))]
snap_files += ['tools/' + fn for fn in sorted(os.listdir(B + '/method/tools'))]
assert len(snap_files) == 21, snap_files
sha_lines = []
for rel in snap_files:
    src = B + '/method/' + rel
    dst = SNAP + '/' + rel
    shutil.copyfile(src, dst)
    h_src = hashlib.sha256(open(src, 'rb').read()).hexdigest()
    h_dst = hashlib.sha256(open(dst, 'rb').read()).hexdigest()
    assert h_src == h_dst, rel
    sha_lines.append(f'{h_dst}  {rel}')
with open(R89 + '/kb-snapshot-holdout33-sha256.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sha_lines) + '\n')

report = {
 'set': 'holdout33', 'round': 89,
 'n_cards': len(ORDER), 'n_gold_lines': len(lines),
 'gold_sha256_build': sha, 'gold_bytes': len(gold_bytes),
 'order': ORDER,
 'snapshot_files': snap_files,
 'strip_register': strip_register,
 'field_mapping_notes': field_mapping_notes,
 'limits': {'tradition_liuren': 14 / 28, 'tradition_liuyao': 14 / 28,
            'source_max_share': 14 / 28, 'non_yijian': 28, 'non_liuyao': 14,
            'all_low': True},
}
with open(R89 + '/holdout33-build-report-r89.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=1)
    f.write('\n')
print('cards:', len(ORDER), 'gold lines:', len(lines))
print('gold sha256 (build):', sha)
print('gold bytes:', len(gold_bytes))
print('snapshot files:', len(snap_files), 'all sha equal')
