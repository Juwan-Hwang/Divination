# -*- coding: utf-8 -*-
"""R96 holdout35 封存建卡席脚本（唯一名 build_h35_r96.py）。
构成（主持定版逐 id，ZIWEI-SUPPLY-SUMMARY-r96 §六）：
紫微14 ZW-024,025,026,027,033,034,035,036,037,038,039,044,045,046
六壬14 DA-082,083,085,086,087,088,090 + BY-054,055,056,057,058,060,061。T=28。
体例承 holdout34：卡字段白名单 INPUT_FIELDS、金标字段序 GOLD_FIELDS（h34 §六）。
DA 金标回 cases_raw.json 程序化提取（解析器承 build_da_h34_r93.py，已对 h33/h34 复现验证）；
BY 课盘/正议/案验回原书页图逐字转录（页图 runs/round96/h35-by-pages-r96/、裁切 h35-by-crops-r96/）；
ZW 据点名登记件逐字转录/组录（逐例 grade_note 登记口径）。
"""
import json, os, hashlib, io, shutil

B = '/home/hatch/workspace/divination/benchmark/phase3'
R96 = B + '/runs/round96'
OUT = B + '/holdout35'
os.makedirs(OUT + '/inputs', exist_ok=True)

INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status', 'anchors']
GOLD_FIELDS = ['id', 'master_prediction', 'outcome_record', 'tradition',
               'pollution', 'grade', 'grade_note', 'provenance',
               'license_status', 'redistributable']
LIC_A = '古籍文本，内部研究用'
LIC_M = '现代版权文本，内部研究用'

ZW_IDS = ['ZW-024','ZW-025','ZW-026','ZW-027','ZW-033','ZW-034','ZW-035',
          'ZW-036','ZW-037','ZW-038','ZW-039','ZW-044','ZW-045','ZW-046']
DA_IDS = ['DA-082','DA-083','DA-085','DA-086','DA-087','DA-088','DA-090']
BY_IDS = ['BY-054','BY-055','BY-056','BY-057','BY-058','BY-060','BY-061']
ALL = DA_IDS + BY_IDS + ZW_IDS
assert len(ALL) == 28 and len(set(ALL)) == 28

# ---- id 集断言：零复用对 used-ids-r96（1333） ----
used = json.load(open(R96 + '/used-ids-r96.json', encoding='utf-8'))
assert len(used) == 1333 and len(set(used)) == 1333
assert not (set(ALL) & set(used)), set(ALL) & set(used)
assert 'LY-015' not in ALL and 'LY-320' not in ALL
# ---- 台账续位复算断言 ----
led = json.load(open(B + '/runs/round85/lr-eligible-ledger-r85.json', encoding='utf-8'))
da_led = led['六壬/《大六壬断案》']; by_led = led['六壬/《六壬辨疑·毕法案录》']
def cont(lst, anchor, n, used_set):
    i = lst.index(anchor); out = []
    for x in lst[i+1:]:
        if x not in used_set:
            out.append(x)
            if len(out) == n: break
    return out
assert cont(da_led, 'DA-081', 7, set(used)) == DA_IDS, cont(da_led, 'DA-081', 7, set(used))
assert cont(by_led, 'BY-053', 7, set(used)) == BY_IDS, cont(by_led, 'BY-053', 7, set(used))

cards, golds = {}, {}
register = {}  # 逐例登记（来源/资格/整段照录等）供建卡报告

# ================= DA =================
pool = {}
for fn in ('cases-a.jsonl', 'cases-b.jsonl'):
    for line in open(B + '/expansion12/liuren-duanan/' + fn, encoding='utf-8'):
        r = json.loads(line); pool[r['id']] = r
bypool = {}
for line in open(B + '/expansion12/liuren-bianyi-yuce/cases-reviewed.jsonl', encoding='utf-8'):
    r = json.loads(line); bypool[r['id']] = r
raw_by_n = {e['n']: e for e in json.load(open(
    B + '/expansion12/liuren-duanan/scratch-archive/cases_raw.json', encoding='utf-8'))}

OUTCOME_MARK = {
 'DA-082': '后辛亥年大水', 'DA-083': '盖判院欲来年冬赴任',
 'DA-085': '方后果授温州乐清尉', 'DA-086': '何上舍发解后',
 'DA-087': '毛巨富', 'DA-088': '王当年十月丁母忧', 'DA-090': '赵果与判官不足'}
TAIL_NOTE = {
 'DA-082': '文尾处置：断语／应验全文照录，爱函按与又按不入。',
 'DA-083': '文尾处置：断语照录，爱函按不入。断语中「四绝」为格称、非「课名」明载，课名记底本未载。',
 'DA-085': '文尾处置：断语照录，断语末缘生谛注（特达、下稍释义）不入；应验全文照录，爱函按不入。',
 'DA-086': '文尾处置：断语／应验全文照录，爱函按不入。',
 'DA-087': '文尾处置：断语全文照录；应验照录，应验末缘生谛注（夤缘释义）不入，爱函按不入。池卡 subject 作「毛主簿」、底本原文作「毛主薄」，卡面从池卡。',
 'DA-088': '文尾处置：断语／应验全文照录，爱函按不入。断语中「闭口」为格称、非「课名」明载，课名记底本未载。',
 'DA-090': '文尾处置：断语照录，断语末缘生谛注（火阁、中堂、下稍、权释义及联系方式字样）不入；应验照录，应验末缘生谛注（间牒释义）不入，爱函按不入。注内联系方式字样按数据处理、不入卡不入金标。'}

GEN = set('青勾合朱蛇贵后空虎常玄阴'); BR = set('子丑寅卯辰巳午未申酉戌亥'); KIN = set('财官父兄子')
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
    L = [lines[s + i].split() for i in range(6)]
    assert len(L[0]) == 4 and len(L[4]) == 4 and len(L[5]) == 4
    assert all(len(x) == 1 and x in BR for x in L[4])
    assert all(len(x) == 1 and x in GEN for x in L[5])
    assert len(L[2]) == 9 and len(L[3]) == 9
    top_g, top_b = L[0], L[1][0:4]
    sike_g, sc1 = L[1][4:8], L[1][8:11]
    l2g, l2b = L[2][0][0], L[2][0][1]
    r2b, r2g = L[2][1][0], L[2][1][1]
    l3g, l3b = L[3][0][0], L[3][0][1]
    r3b, r3g = L[3][1][0], L[3][1][1]
    upper, sc2 = L[2][2:6], L[2][6:9]
    lower, sc3 = L[3][2:6], L[3][6:9]
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
        kin, sb, g = row; mark = ''
        if '◎' in g: mark = '（原式旁标◎）'; g = g.replace('◎', '')
        if '⊙' in g: mark = '（原式旁标⊙）'; g = g.replace('⊙', '')
        assert len(g) == 1 and g in GEN, row
        return f'{kin}{sb}（{g}）{mark}'
    return tianpan, sike, '、'.join([sc(sc1), sc(sc2), sc(sc3)])

def strip_note(seg):
    k = seg.find('缘生谛：')
    if k >= 0:
        assert seg[:k].endswith(('。', '也。', '矣。')), seg[:k]
        return seg[:k]
    return seg

def extract_gold(lines, s, cid):
    body = ''.join(l.strip() for l in lines[s + 6:])
    body = body.split('\x0c')[0].split('爱函按')[0].split('又按')[0]
    i = body.find('邵先生曰'); j = body.find(OUTCOME_MARK[cid])
    assert i >= 0 and j > i, cid
    pred = strip_note(body[i:j]); out = strip_note(body[j:])
    assert '缘生谛' not in pred and '爱函按' not in pred, cid
    assert '缘生谛' not in out and '爱函按' not in out, cid
    assert pred.startswith('邵先生曰：') and pred in body and out in body, cid
    return pred, out

for cid in DA_IDS:
    r = pool[cid]
    assert r.get('holdout_eligible') is True and r.get('contamination') == 'low' \
        and r.get('outcome_grade') in ('A', 'A-low') and r.get('master_predictions') \
        and r.get('outcome', {}).get('description'), cid
    e = raw_by_n[int(cid.split('-')[1])]
    lines = e['raw'].split('\n'); s = locate_chart(lines)
    assert s is not None, cid
    tianpan, sike, sanchuan = parse_chart(lines, s)
    pred, out = extract_gold(lines, s, cid)
    prov = (f"{r['provenance']['work']}（{r['provenance']['edition']}）·"
            f"{r['provenance']['page']}；底本为用户提供，redistributable=false")
    cards[cid] = {'id': cid, 'tradition': 'liuren', 'subject': r['subject'],
        'context': r['context_at_prediction'] if r['context_at_prediction'] else
                   f"占验例（{r['source_work']}）；占时与课式载于 anchors",
        'question': r['question_or_topic'],
        'setting': f"{r['source_work']}（{r['master']}）；{r['provenance']['page']}",
        'provenance': prov, 'redistributable': False, 'license_status': LIC_A,
        'anchors': {'asked_at': r['asked_at'], '课名': '底本未载',
                    '天盘': tianpan, '四课': sike, '三传': sanchuan,
                    '课盘原文来源': '底本全文 cases_raw.json 原式照录（天盘方阵／四课格／三传栏）'}}
    gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low；'
             '课式头四要素 present（R84 核查台账）；课盘经本席回底本全文逐字复原；'
             '金标断语／结局回底本全文邵先生曰段与应验段逐字照录（池卡摘录为节录，'
             '不作金标准据）；' + TAIL_NOTE[cid] + r['grade_note'])
    golds[cid] = {'id': cid, 'master_prediction': pred, 'outcome_record': out,
                  'tradition': 'liuren', 'pollution': 'low',
                  'grade': r['outcome_grade'], 'grade_note': gnote,
                  'provenance': prov, 'license_status': LIC_A, 'redistributable': False}
    register[cid] = 'DA：来源 cases_raw.json n=%s＋池卡 cases-a/b.jsonl 资格断言全过（eligible/low/A-low）；课盘三件程序化转录断言在场；金标为底本正文子串（脚本断言）' % cid.split('-')[1]

# ================= BY =================
BYCH = {
'BY-054': {'ke': '魁度天门 旺禄临身',
 'tp': '辰蛇、巳贵、午后、未阴、卯朱、申元、寅合、酉常、戌白、亥空、子青、丑勾（地盘支→上神天将；原式方阵：蛇贵后阴／辰巳午未、朱卯・申元、合寅・酉常、丑子亥戌／勾青空白；元＝玄武，原书省字照录）',
 'sk': '丑（勾）寅、寅（合）卯、亥（空）子、子（青）癸（四课格原式：上行丑寅亥子／下行寅卯子癸，天将勾合空青）',
 'sc': '鬼丑（勾）、禄子（青）、兄亥（空）',
 'mp': '问：魁度天门，旺禄临身，似不宜动。曰：现在逃兵，何禄可守？三传润下，宜于下行。丑能刑戌，木能克土，亦无所隔。退茹有相联而退之象。再退一步逢申酉之生，即父母之邦，退而受生可也，况青龙得水，能奋万里之翼，六合为门，作子孙制鬼，如何不行？问：寅木死气，何能制戌虎？且妨子孙不利。曰：三传属水以助子孙，死化为生，何不利之有？但勾陈发用，不免迟滞，出旬破关，未日冲丑，方能启行，宜坐以待之，上路必有退回之船，且得贵财相助。',
 'oc': '果因汉中城陷，船户相联而下，未日得开，贵财亦应此课。',
 'tail': '文尾处置：断语＝正议＋参议全文照录（参议问答属原断，照 BY-044 参议并入先例）；案验照录，案验末「以干支上神与三传格例断者也」为收束语、不入结局。'},
'BY-055': {'ke': '罡塞鬼户 脱上逢脱',
 'tp': '未勾、申合、酉朱、戌蛇、午青、亥贵、巳空、子后、丑阴、寅元、卯常、辰白（地盘支→上神天将；原式方阵：勾合朱蛇／未申酉戌、青午・亥贵、空巳・子后、辰卯寅丑／白常元阴；元＝玄武，原书省字照录）',
 'sk': '未（勾）巳、巳（空）卯、亥（贵）酉、酉（朱）丁（四课格原式：上行未巳亥酉／下行巳卯酉丁，天将勾空贵朱）',
 'sc': '财酉（朱）、官亥（贵）、子丑（阴）',
 'mp': '游都乘马加支，贼必过境。然支上脱气，又乘天空，只是虚声动摇，人民争出，城内却无事。初财遭夹克，不过迁移耗财而已。辰为天罡，寅为鬼户，辰加寅，则鬼户杜塞，不致破城。初传旬尾，末传关神，闭关则不免也。',
 'oc': '四月初八日贼兵犯境，城内争逃，后却无事。',
 'tail': '文尾处置：正议／案验全文照录；案验后附议（支为宅问答二段）不入。'},
'BY-056': {'ke': '两蛇夹墓',
 'tp': '戌蛇、亥朱、子合、丑勾、酉贵、寅青、申后、卯空、辰白、巳常、午元、未阴（地盘支→上神天将；原式方阵：蛇朱合勾／戌亥子丑、贵酉・寅青、后申・卯空、未午巳辰／阴元常白；元＝玄武，原书省字照录）',
 'sk': '戌（蛇）巳、巳（常）子、卯（空）戌、戌（蛇）丙（四课格原式：上行戌巳卯戌／下行巳子戌丙，天将蛇常空蛇）',
 'sc': '禄巳（常）、子戌（蛇）、父卯（空）',
 'mp': '戌为日墓，乘蛇加巳，巳属蛇，故为两蛇夹墓，主有惊危之事。然时逢天罡，戌为月破，其凶可散。但卯木文书乘天空，不免谣言动众耳。课名回环，去者仍回本处。游都落空坐克，可无忧也。',
 'oc': '此因探报不实，人皆惊走，后却无事。',
 'tail': '文尾处置：正议／案验全文照录，无附议、复玩文尾。'},
'BY-057': {'ke': '所谋多拙 初遭夹克',
 'tp': '午蛇、未贵、申后、酉阴、巳朱、戌元、辰合、亥常、子白、丑空、寅青、卯勾（地盘支→上神天将；原式方阵：蛇贵后阴／午未申酉、朱巳・戌元、合辰・亥常、卯寅丑子／勾青空白；元＝玄武，原书省字照录）',
 'sk': '辰（合）卯、卯（勾）寅、辰（合）卯、卯（勾）甲（四课格原式：上行辰卯辰卯／下行卯寅卯甲，天将合勾合勾）',
 'sc': '财辰（合）、子巳（朱）、子午（蛇）',
 'mp': '墓贵空上逢空，正贵逢墓，干支罗网，初遭夹克，决不能中。',
 'oc': '柏香，吾畏友，楚之志士也。心企古人，学期远到，乡试经魁。年甫二十四岁，再赴礼闱，报罢半途染病，至舅家而卒。',
 'tail': '文尾处置：正议全文照录；结局取案验正文至「至舅家而卒」止，案验后段回课语（查此课云云）与感叹（寿少颜子一岁、聊附寄痛）不入，逐例登记于此。'},
'BY-058': {'ke': '天罗自裹 虎乘遁鬼 干墓并关',
 'tp': '戌合、亥朱、子蛇、丑贵、酉勾、寅后、申青、卯阴、辰元、巳常、午白、未空（地盘支→上神天将；原式方阵：合朱蛇贵／戌亥子丑、勾酉・寅后、青申・卯阴、未午巳辰／空白常元；元＝玄武，原书省字照录）',
 'sk': '申（青）卯、卯（阴）戌、午（白）丑、丑（贵）庚（四课格原式：上行申卯午丑／下行卯戌丑庚，天将青阴白贵）',
 'sc': '禄申（青）、父丑（贵）、鬼午（白）',
 'mp': '本命作日墓加干，为天网自裹，主作事糊涂，自招其悔。卯木财空，青龙折足，岂可贸易？况干墓并关，虎乘遁鬼，不惟道路梗滞，并受惊危。喜德禄乘马，太阳加年，破财而人清吉，幸矣。',
 'oc': '是年借本贸易，竟折其半，而上下兵变，携眷流离，苦不堪言，人口无伤。',
 'tail': '文尾处置：正议／案验全文照录；案验后「胶鬲遭乱」一段为附议感叹，不入。正议「天网自裹」照原书页图字形录（课名题作「天罗自裹」）。三传栏首二行旁注「日」「马」为年命标记、不入三传正文。'},
'BY-060': {'ke': '用破身心 传财化鬼 三传递生 交车相合',
 'tp': '酉贵、戌后、亥阴、子元、申蛇、丑常、未朱、寅白、卯空、辰青、巳勾、午合（地盘支→上神天将；原式方阵：贵后阴元／酉戌亥子、蛇申・丑常、朱未・寅白、午巳辰卯／合勾青空；元＝玄武，原书省字照录）',
 'sk': '子（元）申、申（蛇）辰、丑（常）酉、酉（贵）丙（四课格原式：上行子申丑酉／下行申辰酉丙，天将元蛇常贵）',
 'sc': '财酉（贵）、子丑（常）、禄巳（勾）',
 'mp': '两贵坐克，中末空亡，支上岁破，日禄坐空，日马长生投墓，课传毫无益处，所谓用破身心无所归是也。丑命上乘丁马，仍以远行为高。',
 'oc': '此处系贸易之所，毫无知音。越二日戊午遂行，不久，贼过，已成灰烬。',
 'tail': '文尾处置：正议／案验全文照录；案验后问曰段（交车相合问答）为附议，不入。'},
'BY-061': {'ke': '华盖覆日 辛日逢丁 彼此猜忌',
 'tp': '寅勾、卯合、辰朱、巳蛇、丑青、午贵、子空、未后、申阴、酉元、戌常、亥白（地盘支→上神天将；原式方阵：勾合朱蛇／寅卯辰巳、青丑・午贵、空子・未后、亥戌酉申／白常元阴；元＝玄武，原书省字照录）',
 'sk': '酉（元）子、子（空）卯、辰（朱）未、未（后）辛（四课格原式：上行酉子辰未／下行子卯未辛，天将元空朱后）',
 'sc': '子子（空）、父未（后）、子子（空）',
 'mp': '亥卯未日以未为华盖，是三合墓神也。华盖覆日，凡占昏昧，问病主憸憸之状。天后逢空，而干支相害，害者阻也，未者胃也，乃脾胃不纳饮食之象。午鬼虽空而时上白虎乘丁，病难治矣。',
 'oc': '时抱噎症，百药不效，未月身故。',
 'tail': '文尾处置：正议全文照录；结局取案验正文首段，案验后段身世感叹（嫂自二十一岁守志云云）不入，逐例登记于此。三传初末两传同作子子（空），原书照录。'},
}
for cid in BY_IDS:
    r = bypool[cid]; d = BYCH[cid]
    assert r.get('holdout_eligible') is True and r.get('contamination') == 'low' \
        and r.get('outcome_grade') in ('A', 'A-low') and r.get('master_predictions') \
        and r.get('outcome', {}).get('description'), cid
    rv = r.get('review', {})
    assert rv.get('verdict') == 'seal' and rv.get('grade_final') == 'A-low' \
        and rv.get('contamination_final') == 'low', cid
    prov = (f"{r['provenance']['work']}（{r['provenance']['edition']}）·"
            f"{r['provenance']['page']}；底本为用户提供，redistributable=false")
    cards[cid] = {'id': cid, 'tradition': 'liuren', 'subject': r['subject'],
        'context': f"占验例（{r['source_work']}）；占时与课式载于 anchors",
        'question': r['question_or_topic'],
        'setting': f"{r['source_work']}（{r['master']}）；{r['provenance']['page']}",
        'provenance': prov, 'redistributable': False, 'license_status': LIC_A,
        'anchors': {'asked_at': r['asked_at'], '课名': d['ke'], '天盘': d['tp'],
                    '四课': d['sk'], '三传': d['sc'],
                    '课盘原文来源': '原书页图课盘直录（本席读图通读、课盘裁切放大复核，页图存 runs/round96/h35-by-pages-r96/、裁切件存 runs/round96/h35-by-crops-r96/）'}}
    gnote = ('入账口径：池卡 holdout_eligible=true、contamination low、A-low、复核 verdict=seal；'
             '课式头四要素 present（R84 核查台账）；课盘与正议／案验全文经本席回原书页图逐字复原；'
             '池卡摘录为节录，不作金标准据；' + d['tail'] + r['grade_note'] + '；复核：' + rv.get('notes', ''))
    golds[cid] = {'id': cid, 'master_prediction': d['mp'], 'outcome_record': d['oc'],
                  'tradition': 'liuren', 'pollution': 'low',
                  'grade': r['outcome_grade'], 'grade_note': gnote,
                  'provenance': prov, 'license_status': LIC_A, 'redistributable': False}
    register[cid] = 'BY：来源原书页图（%s）逐字转录；池卡资格字段 holdout_eligible=true、contamination=low、outcome_grade=A-low、review.verdict=seal/grade_final=A-low/contamination_final=low（台账/池件断言全过）；课盘三件读图复原' % r['provenance']['page']

# ================= ZW =================
Q_ZW = '就此命盘求测（原书命例体例，无独立问句原文载录）'
CTX_ZW = '紫微命例实批；命盘锚点载于 anchors'
CTX_CM = '紫微命例实批（局部盘）；命盘锚点载于 anchors（仅实载宫星，空白宫不补）'
PROV_XZS = '《紫微斗数命运分析》（徐曾生著）·{s}；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false'
PROV_ZJ = '《紫微斗数命理学正解》（许铨仁著）·{s}；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false'
PROV_CM = '蔡明宏《紫微六玄经脉——钦天四化秘仪在华山》·{s}；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false'

ZWCASES = [
dict(id='ZW-024', subject='男命，庚寅年4月巳时（日数原书未标），火六局',
 setting='《紫微斗数命运分析》（徐曾生著）·第29章命例E（书pp.290–292）',
 prov=PROV_XZS.format(s='第29章命例E（书pp.290–292）'), context=CTX_ZW,
 anchors={'birth': '庚寅年4月 日巳时，男（日数原盘未标，照实登记）', '局': '火六局',
  '命宫': '命宫在辰（戊干），天梁、天刑坐命', '紫微落宫': '紫微在财帛宫',
  '四化锚点': '本命官禄宫坐忌又自化忌成双忌冲对宫夫妻；大限夫妻化忌冲大限命宫；流年夫妻化忌冲大限夫妻（D5-29-16 图注四点）'},
 mp='一、本命官禄坐忌又自化忌成双忌，冲到对宫夫妻。二、夫妻宫坐巨门，被官禄宫之自化忌冲到，已有变动之意。三、大限夫妻化忌冲大限命宫，该大限夫妻关系也有变化。综合前述，命与限的夫妻都冲动了，一定会有变化。四、流年进入夫妻宫，被官禄宫的双忌冲到，且流年夫妻宫化忌冲大限夫妻，因此该年离婚。但流年夫妻有化科坐守，会拖延一下。',
 oc='33岁闹离婚；34岁离婚。因子女之事，夫妻感情恶化而闹离婚。',
 gn='入账口径：ZIWEI-REVIEW-XZS7-r93 复评通过（XZS-14→ZW-024，四滤全过、锚点回读置信高、断法 D5-29-16/D5-29-15 在册）；断语取原盘图注四点逐字（书p.290，DIGEST-5 D5-29-16 转录在场）；结局据盘侧注「33岁闹离婚」「34岁离婚」与书p.292 子女线结尾（D5-29-16 转录）组录、以结局正文为限；命宫地支据盘图宫干戊读定（本席回原书页图，页图存 runs/round96/h35-xzs-pages-r96/）；讲授回溯实录（A-low）；transcription=visual。',
 reg='ZW-024：来源 ZIWEI-REVIEW-XZS7-r93 §三.4＋ZIWEI-SUPPLY-BATCH2-XZS-r92 XZS-14 条＋DIGEST-5 D5-29-16；原书页图 PDF151 回读'),
dict(id='ZW-025', subject='阴女，己丑年8月卯时（日数原书未标），土五局',
 setting='《紫微斗数命运分析》（徐曾生著）·第29章命例H（书pp.300–303）',
 prov=PROV_XZS.format(s='第29章命例H（书pp.300–303）'), context=CTX_ZW,
 anchors={'birth': '己丑年8月 日卯时，阴女（日数原盘未标，照实登记）', '局': '土五局',
  '命宫': '命宫在申，禄存坐命', '紫微落宫': '紫微在未（兄弟宫，紫微七杀）',
  '四化锚点': '本命交友宫乙亥，乙干天机化禄入夫妻、天梁化权入夫妻、紫微化科入兄弟、太阴化忌入迁移宫即冲命宫；28岁流年（D5-29-21）'},
 mp='本命交友宫乙干四化：天机化禄入夫妻宫，天梁化权入夫妻宫，紫微化科入兄弟宫，太阴化忌入迁移宫即冲命宫。天机化禄和天梁化权皆飞入夫妻宫，表示朋友和我夫妻宫有关系，关系非常强烈，亦是外遇命格。大限交友与我夫妻发生链结，巨门主暗昧不明，故是同居关系。流年28岁，本命交友飞出禄权在迁移照命宫、大限交友飞出禄权在迁移照流年命宫，故出外遇。',
 oc='此造原拥有美满家庭，丈夫是殷实商人。命造不甘寂寞红杏出墙了，离家出走与情夫同居，当情夫厌腻了，便弃她而去，只好自己赁屋独居。',
 gn='入账口径：ZIWEI-REVIEW-XZS7-r93 复评通过（XZS-17→ZW-025，四滤全过、锚点回读置信高、断法 D5-29-21/D5-29-19/D5-29-22 在册）；断语据 DIGEST-5 D5-29-21 逐字要点组录；结局据复评件书p.302 主锚点叙事逐字照录、以结局正文为限；命宫/紫微落宫经本席回原书 H-1 盘图读定（命宫庚干在申、紫微七杀在兄弟宫未，页图存 runs/round96/h35-xzs-pages-r96/）；讲授回溯实录（A-low）；transcription=visual。',
 reg='ZW-025：来源 ZIWEI-REVIEW-XZS7-r93 §三.5＋BATCH2-XZS XZS-17 条＋DIGEST-5 D5-29-21；原书页图 PDF156 回读'),
dict(id='ZW-026', subject='男命，丁丑年3月戌时（日数原书未标），水二局',
 setting='《紫微斗数命运分析》（徐曾生著）·第30章图三命例（书pp.312–313）',
 prov=PROV_XZS.format(s='第30章图三命例（书pp.312–313）'), context=CTX_ZW,
 anchors={'birth': '丁丑年3月 日戌时，男命（日数原盘未标，照实登记）', '局': '水二局',
  '命宫': '命宫在午（丙干），天梁、左辅、禄存坐命', '紫微落宫': '紫微在卯（子女宫，紫微贪狼）',
  '四化锚点': '本命夫妻化禄权科入12–21大限的三合方内；本命夫妻坐甲辰，廉贞化禄入父母宫、破军化权入交友宫（D5-30-08）'},
 mp='本命夫妻化禄权科入12--21大限的三合方内，21岁恰在三方的顶点，故该年结婚。本命夫妻坐甲辰，廉贞化禄入父母宫、破军化权入交友宫；大限夫妻坐丁未，干丁四化星全入本命盘三合内，巨门化忌入本命夫妻宫为忌入；流年步入酉年时已达适婚年龄，流年夫妻坐丁未、干丁四化全入本命三合、巨门化忌入本命夫妻为忌入，故辛酉年（21岁）完成终身大事。',
 oc='本命造很早就结婚了，21岁结婚。',
 gn='入账口径：ZIWEI-REVIEW-XZS7-r93 复评通过（XZS-19→ZW-026，四滤全过、锚点回读置信高、断法 D5-30-08/D5-30-05/D5-30-06 在册）；断语首句为原书图注逐字、余据 D5-30-08 逐字要点组录；结局据原书p.312 正文与盘侧注「21岁结婚」组录、以结局正文为限；命宫/紫微落宫经本席回原书图三盘图以宫干校验读定（命宫丙干在午、子女宫癸干在卯，页图存 runs/round96/h35-xzs-pages-r96/）；讲授回溯实录（A-low）；transcription=visual。',
 reg='ZW-026：来源 ZIWEI-REVIEW-XZS7-r93 §三.6＋BATCH2-XZS XZS-19 条＋DIGEST-5 D5-30-08；原书页图 PDF162 回读'),
dict(id='ZW-027', subject='女命，民国45年（丙申年）7月19日酉时（农历6月12日），木三局',
 setting='《紫微斗数命运分析》（徐曾生著）·第32章例二（书pp.340–342）',
 prov=PROV_XZS.format(s='第32章例二（书pp.340–342）'), context=CTX_ZW,
 anchors={'birth': '阳女，民国45年丙申年，国历7月19日17时，农历6月12日酉时；四柱丙申・乙未・丁亥・己酉',
  '局': '木三局（命主禄存、身主天梁；生年四化：天同禄／天机权／文昌科／廉贞忌）',
  '命宫': '命宫在戌（戊戌），3–12岁宫（软件打印盘图读定）',
  '紫微落宫': '软件打印盘小字密集，复评件附项未逐载紫微落宫，照实登记不臆补；盘面全字段（阳女、丙申、木三局、生年四化、命宫岁段）经复评件 300dpi 复核逐字可读',
  '四化锚点': '婚姻曲线15–43岁婚姻指数处于负数区（D5-32-13）；43–52岁大限夫妻宫坐天机（化权）、天梁、陀罗（D5-32-14）'},
 mp='在婚姻指数低／次低时段决定结婚，往往有所托非人、爱不对人等缺憾，即在婚姻曲线低的时段结婚，结婚当下就播下婚姻失败种子；15–43岁婚姻指数曲线都处于负数区，此种曲线结构下婚姻多半存在不稳定因素，适当时机来到就爆发使婚姻破裂。婚姻指数由40岁到41岁间下降幅度达25点，代表该段期间有非常重大感情转折，在曲线降幅大的时段下决定，往往会造成遗憾事件。',
 oc='命例主人在一家妇产科担任护士，与院内医师恋爱，于二十四岁结婚。决定离婚是在四十一岁，而于四十二岁签署离婚证书确定。',
 gn='入账口径：ZIWEI-REVIEW-XZS7-r93 复评通过（XZS-25→ZW-027，四滤全过、盘面 300dpi 附项复核成立、断法 D5-32-13/D5-32-14 在册）；断语据 D5-32-13 逐字要点组录；结局据复评件书pp.340–341 回读逐字组录、以结局正文为限；盘面联系方式栏不转录、不入卡（承复评件处置）；命宫在戌经本席回原书p.342 软件打印盘图读定（页图存 runs/round96/h35-xzs-pages-r96/）；讲授回溯实录（A-low）；transcription=visual。',
 reg='ZW-027：来源 ZIWEI-REVIEW-XZS7-r93 §三.7＋DIGEST-5 附项/D5-32-13；原书页图 PDF176–177 回读'),
dict(id='ZW-033', subject='男命，庚子年1月巳时（日数原书未标），水二局',
 setting='《紫微斗数命理学正解》（许铨仁著）·第六章案例三（书pp.267–271）',
 prov=PROV_ZJ.format(s='第六章案例三（书pp.267–271）'), context=CTX_ZW,
 anchors={'birth': '民国49年生，庚子年1月 日巳时，男命（日数原盘未标，照实登记）', '局': '水二局',
  '命宫': '命宫在酉（乙酉），天刑、文曲、羊刃', '紫微落宫': '紫微在午（子女宫）',
  '四化锚点': '命宫宫干乙使天梁化权飞至迁移宫、视同自化权；大运（12–21）自化忌与20岁流命走至未宫叠宫引爆'},
 mp='命宫天刑、文曲、羊刃三星个性刚直，羊刃为血光之星主受伤。命宫宫干乙使天梁化权飞至迁移宫，视同自化权。大运（12–21）自化忌与20岁流命走至未宫之叠宫引爆。',
 oc='（一）小时候常碰伤、撞伤，左手曾骨折。（二）20岁时骑机车，发生车祸致脑震荡，尚幸终能化险为夷。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH3-ZJ-r93（ZJ-07）四滤全过、锚点在场、low污染，主持汇编收口续编 ZW-033（ZIWEI-SUPPLY-BATCH3-SUMMARY-r93 §三）；结局据登记件摘要記述逐字照录、以结局正文为限，断语据登记件作者断语要点以原断为限组录，与摘要分立；讲授回溯实录（A-low）；盘面经登记件裁剪复核转录（crops-zhengjie-r93/），transcription=visual；日数原盘未标、不臆补。',
 reg='ZW-033：来源 ZIWEI-SUPPLY-BATCH3-ZJ-r93 ZJ-07 条＋BATCH3-SUMMARY §三续编（ZJ-07→ZW-033）'),
dict(id='ZW-034', subject='男命，丁酉年3月戌时（日数原书未标），水二局',
 setting='《紫微斗数命理学正解》（许铨仁著）·第六章案例四（书pp.272–278）',
 prov=PROV_ZJ.format(s='第六章案例四（书pp.272–278）'), context=CTX_ZW,
 anchors={'birth': '民国46年生，丁酉年3月 日戌时，男命（日数原盘未标，照实登记）', '局': '水二局',
  '命宫': '命宫在午（丙午），天机、左辅、禄存', '紫微落宫': '紫微在未（父母宫，紫微破军）',
  '四化锚点': '迁移宫巨门生年忌重叠、来因宫（疾厄）巨门化忌；大运（22–31）大运命宫与大运迁移宫干组合太阳化忌交会；命宫化忌冲疾厄宫'},
 mp='迁移宫巨门生年忌重叠，来因宫（疾厄）巨门化忌。大运（22–31）大运命宫、大运迁移宫干组合太阳化忌交会。命宫化忌冲疾厄宫之交通安全读法。',
 oc='※民国73年，28岁遭车祸压断双腿。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH3-ZJ-r93（ZJ-08）四滤全过、锚点在场、low污染，主持汇编收口续编 ZW-034（ZIWEI-SUPPLY-BATCH3-SUMMARY-r93 §三）；结局据登记件摘要記述逐字照录（摘要仅一行、事件具体）、以结局正文为限，断语据登记件作者断语要点以原断为限组录，与摘要分立；讲授回溯实录（A-low）；盘面经登记件裁剪复核转录，transcription=visual；日数原盘未标、不臆补。',
 reg='ZW-034：来源 ZIWEI-SUPPLY-BATCH3-ZJ-r93 ZJ-08 条＋BATCH3-SUMMARY §三续编（ZJ-08→ZW-034）'),
dict(id='ZW-035', subject='男命，丙午年6月申时（日数原书未标），木三局',
 setting='《紫微斗数命理学正解》（许铨仁著）·第六章案例五（书pp.275–278）',
 prov=PROV_ZJ.format(s='第六章案例五（书pp.275–278）'), context=CTX_ZW,
 anchors={'birth': '民国55年生，丙午年6月 日申时，男命（日数原盘未标，照实登记）', '局': '木三局',
  '命宫': '命宫在亥（己亥），太阴、铃星', '紫微落宫': '紫微在午（疾厄宫）',
  '四化锚点': '大运命宫（13–22）行至引爆点、本命之重象权力决定流年应数；疾厄宫为父母宫之位，13–22岁段宜特别留意交通事故'},
 mp='大运命宫（13–22）行至引爆点、本命之重象权力决定流年应数。疾厄宫为父母宫之位、13–22岁段宜特别留意交通事故。',
 oc='蔡×宏小弟，于民国70年，年仅16岁时，骑摩托车，被自用轿车撞，肋骨皆断，不幸惨死。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH3-ZJ-r93（ZJ-09）四滤全过、锚点在场、low污染，主持汇编收口续编 ZW-035（ZIWEI-SUPPLY-BATCH3-SUMMARY-r93 §三）；结局据登记件摘要記述（逐字大意，个别字置信0.8、事件与年份年龄无疑）照录、以结局正文为限，断语据登记件作者断语要点以原断为限组录，与摘要分立；讲授回溯实录（A-low）；盘面经登记件裁剪复核转录，transcription=visual；登记件盘面兄弟宫与父母宫同为戊戌系本书盘式宫干并列印行所致、不涉命宫与紫微落宫；日数原盘未标、不臆补。',
 reg='ZW-035：来源 ZIWEI-SUPPLY-BATCH3-ZJ-r93 ZJ-09 条＋BATCH3-SUMMARY §三续编（ZJ-09→ZW-035）'),
dict(id='ZW-036', subject='男命，丙年生（天同节例三）',
 setting='蔡明宏《紫微六玄经脉——钦天四化秘仪在华山》·例三（PDF p.189，印p.172）',
 prov=PROV_CM.format(s='例三（PDF p.189，印p.172）'), context=CTX_CM,
 anchors={'birth': '丙年生，男命（原书仅载生年干与性别，照实登记）',
  '实载范围': '局部盘：十二宫方格框架在场，标字5格/12，实载星曜天同、贪狼、巨门、天机4星；空白宫不补',
  '命宫': '命宫格实载贪狼（丙干）',
  '四化锚点': '子女宫天同生年禄、无自化；本官禄宫坐庚，天同化忌入子女宫构成禄忌；天同→巨门在父母宫、天同→贪狼在命宫'},
 mp='来因宫在命宫，与自己有关。（1）天同星在子女，天同有生年禄，没有自化。（2）既然没有自化，只好用化忌来平衡。（3）本官禄宫坐庚，天同星化忌入子女宫，构成禄、忌，代表此命主上班为宜或有一份工作可做。（4）天同→巨门：巨门在父母，代表工作地点在公家或大公司的工作环境。（5）天同→贪狼：贪狼在命宫，代表他本人很自立，独立性强也有才华。',
 oc='命主本人打从学校毕业后，就在公家机关上班，迄今都有一份安定工作。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH5-CM-r96 定版（CM-11）四滤全过、局部锚点、low污染，主持汇编续编 ZW-036（ZIWEI-SUPPLY-SUMMARY-r96 §一）；断语/结局据 rate-chunk-3-r96.md CM-11 逐字转录（transcription=visual，正文置信0.96/盘图0.93），结局只取评定件所引原句、不扩写；局部锚点逐例标明实载宫星范围、空白宫不补；讲授回溯实录（A-low）。ZW-036 无特殊注（承派单）。',
 reg='ZW-036：来源 ZIWEI-SUPPLY-BATCH5-CM-r96 CM-11 行＋rate-chunk-3-r96.md CM-11 节逐字转录；SUMMARY-r96 编号 CM-11→ZW-036'),
dict(id='ZW-037', subject='女命，癸年生（太阴节演员排练（1））',
 setting='蔡明宏《紫微六玄经脉——钦天四化秘仪在华山》·演员排练（1）（PDF p.201，印p.184）',
 prov=PROV_CM.format(s='演员排练（1）（PDF p.201，印p.184）'), context=CTX_CM,
 anchors={'birth': '癸年生，女命（原书仅载生年干与性别，照实登记）',
  '实载范围': '局部盘：标字4格/12，实载星曜破军、武曲、太阴、天机4星；空白宫不补',
  '命宫': '命宫格宫干癸（星名未标）',
  '四化锚点': '癸天干在命宫，太阴化科在子女；太阴所在宫位坐庚，庚会使太阴再自化科；第三大限子女宫变成大限的疾厄'},
 mp='癸天干在命宫，太阴化科在子女，代表有子女之命。太阴所在宫位，坐庚，庚会使太阴再自化科，代表生产子女要特别小心，恐有灾厄。当大限走入第三大限时，子女宫会变成大限的疾厄。为什么会有灾厄的现象。｛癸天干的太阴化科。庚天干的太阴化科。｝同时交会的宫位要特别小心，这两个天干的会合，正如月亮看不到的那一面→背面。都会有一种劫难发生。',
 oc='此人真的在生产时发生意外。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH5-CM-r96 定版（CM-12）四滤全过、局部锚点、low污染，主持汇编续编 ZW-037（ZIWEI-SUPPLY-SUMMARY-r96 §一）；断语/结局据 rate-chunk-3-r96.md CM-12 逐字转录（transcription=visual，正文置信0.96/盘图0.93），结局只取评定件所引原句、意外细节原书未载不扩写；局部锚点逐例标明实载范围、空白宫不补；栏目名「演员排练」为教学栏目名、非名人例；讲授回溯实录（A-low）。',
 reg='ZW-037：来源 BATCH5 CM-12 行＋rate-chunk-3-r96.md CM-12 节；SUMMARY-r96 编号 CM-12→ZW-037'),
dict(id='ZW-038', subject='男命，癸年生（太阴节演员排练（2））',
 setting='蔡明宏《紫微六玄经脉——钦天四化秘仪在华山》·演员排练（2）（PDF p.202上，印p.185）',
 prov=PROV_CM.format(s='演员排练（2）（PDF p.202上，印p.185）'), context=CTX_CM,
 anchors={'birth': '癸年生，男命（原书仅载生年干与性别，照实登记）',
  '实载范围': '局部盘：标字4格/12，实载星曜太阴、天机、破军、武曲4星；空白宫不补',
  '命宫': '命宫格宫干戊（星名未标）',
  '四化锚点': '癸天干，破军化禄又自化禄在交友；太阴化科在财帛；福德宫坐庚，又化科入财帛，构成太阴化科在癸、庚会合中'},
 mp='癸天干，破军化禄又自化禄在交友。太阴化科在财帛。福德宫坐庚，又化科入财帛，构成太阴化科在癸、庚会合中。太阴星的重点，在宫位论，指太阴在什么宫位为主。',
 oc='此人曾被朋友损财过，失了一笔大财。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH5-CM-r96 定版（CM-13）四滤全过、局部锚点、low污染，主持汇编续编 ZW-038（ZIWEI-SUPPLY-SUMMARY-r96 §一）；断语/结局据 rate-chunk-3-r96.md CM-13 逐字转录（transcription=visual，正文置信0.96/盘图0.93），结局只取评定件所引原句、金额原书未载不扩写不估数；局部锚点逐例标明实载范围、空白宫不补；讲授回溯实录（A-low）。',
 reg='ZW-038：来源 BATCH5 CM-13 行＋rate-chunk-3-r96.md CM-13 节；SUMMARY-r96 编号 CM-13→ZW-038'),
dict(id='ZW-039', subject='男命，辛年生（太阳节例二）',
 setting='蔡明宏《紫微六玄经脉——钦天四化秘仪在华山》·例二（PDF p.223，印p.206）',
 prov=PROV_CM.format(s='例二（PDF p.223，印p.206）'), context=CTX_CM,
 anchors={'birth': '辛年生，男命（原书仅载生年干与性别，照实登记）',
  '实载范围': '局部盘（节录示意盘）：仅田宅宫、子女宫、命宫3格标字；田宅宫太阳、太阴同宫（宫干辛）；空白宫不补',
  '命宫': '命宫格仅宫位标记（星名未标）',
  '四化锚点': '辛年生，太阳在田宅，权自化权；对宫为子女宫，像似家庭性的工作'},
 mp='辛年生，太阳在田宅，权自化权。此命主的事业在家里开工厂。对宫为子女宫，像似家庭性的工作；换言之，原本此工作是父亲（田属家族）传下来的，现由子女后代（命主）在经营。何以说？太阳权自化权，有承续解。除非自己结束。',
 oc='此命主的事业在家里开工厂。原本此工作是父亲（田属家族）传下来的，现由子女后代（命主）在经营。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH5-CM-r96 定版（CM-18）四滤全过、局部锚点、low污染，主持汇编续编 ZW-039（ZIWEI-SUPPLY-SUMMARY-r96 §一）；断语/结局据 rate-chunk-4-r96.md CM-18 逐字转录（transcription=visual，正文置信0.96/盘图0.94），结局只取评定件所引原句、不扩写；整段照录登记：本例断语与结局同段连写无分界，结局二句同见于断语段内，照金标编例整段口径登记于此；局部锚点逐例标明实载范围、空白宫不补；讲授回溯实录（A-low）。',
 reg='ZW-039：来源 BATCH5 CM-18 行＋rate-chunk-4-r96.md CM-18 节；SUMMARY-r96 编号 CM-18→ZW-039；同段连写整段登记例'),
dict(id='ZW-044', subject='男命，辛巳年生（命例三）',
 setting='蔡明宏《紫微六玄经脉——钦天四化秘仪在华山》·命例三（PDF pp.535–540，印pp.518–523）',
 prov=PROV_CM.format(s='命例三（PDF pp.535–540，印pp.518–523）'), context=CTX_ZW,
 anchors={'birth': '辛巳年生，男命（盘注大命62～71）',
  '实载范围': '全盘锚点：十二宫宫名、宫干、星曜实载齐备',
  '命宫': '命宫癸干，天同坐命', '紫微落宫': '紫微在交友宫（戊干，右弼、天相、紫微）',
  '全盘': '命宫天同（癸）；父母宫天府、武曲（甲）；福德宫太阴、太阳（乙）；田宅宫贪狼（丙）；兄弟宫左辅、破军（壬）；夫妻宫无主星（辛）；官禄宫巨门、天机（丁）；交友宫右弼、天相、紫微（戊）；子女宫廉贞（庚）；财帛宫文曲、文昌（辛）；疾厄宫七杀（庚）；迁移宫天梁（己）',
  '四化锚点': '辛干四化标记：巨门禄在官禄、太阳权在福德、文曲科在财帛、文昌忌在财帛；来因宫在夫妻宫，向心禄入官禄宫；官禄宫与财帛宫自化科、忌串联'},
 mp='此命盘也是属于来因宫自化的命例，且是双边自化。（1）辛年生，来因宫在夫妻宫，一个向心禄入官禄宫。直觉的，就是婚后必须创业。为什么？官禄宫与财帛宫有自化科、忌，并串联，也象征夫妻要共事（一起经营）。（2）来因宫用神是化禄，则用神就取禄、忌组。禄、忌全部在三合，代表事业是自己创业的，不须与人合作。（3）官禄宫有三象，即其中少了化权，由丁天干转化权入命宫，法生年权太阳在福德，代表此工作是由自己（本人）创业的，而天同星，解释为一种服务业的性质。财帛宫也是有三象，其中少了化禄，由辛天干转化禄与生年巨门化禄同一颗，代表在生意往来上的财务都是由太太在处理的（巨门禄在官禄）。（5）当官禄宫与财帛宫都有串联时，并且现象又平衡，大抵在赚钱上都很平稳而不错。（6）终归此命盘的人，婚后的重心都放在工作事业上，较劳碌之命。另类分析（2）：己天干中有天梁自化科，代表物相。（4）天梁科串联右弼，当大限在第四大限（寅宫），右弼变成大限的财帛宫，表示第四大限开始，生意就走入佳境。（5）丙在田宅，廉贞化忌入子女，法生年忌在财帛。（6）疾厄宫也坐庚，所以从事的行业做到第六大限，也不会改行，并且依然会经营的不错。',
 oc='命造本人从第三大限开始做到现在。此命盘的本人，是位中医师。第四大限就赚钱，并也开了店。此命造直到现在还是开业经营中。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH5-CM-r96 定版（CM-73）四滤全过、全盘锚点、low污染，主持汇编续编 ZW-044（ZIWEI-SUPPLY-SUMMARY-r96 §一）；断语据 rate-chunk-15-r96.md CM-73 逐字转录组录（transcription=visual，正文置信0.96/盘图0.90；原书编号自（3）径接（5），照录不补）；结局只取评定件所引原句四处组录、不扩写（PDF p.542 页首无题一段归属未裁、不作本例结局依据，承评定件登记）；讲授回溯实录（A-low）。',
 reg='ZW-044：来源 BATCH5 CM-73 行＋rate-chunk-15-r96.md CM-73 节逐字转录；SUMMARY-r96 编号 CM-73→ZW-044；全盘锚点'),
dict(id='ZW-045', subject='男命，丙戌年7月子时（日数原书未标），火六局',
 setting='《紫微斗数命理学正解》（许铨仁著）·第八章第一节案例（书pp.306–313）',
 prov=PROV_ZJ.format(s='第八章第一节案例（书pp.306–313）'), context=CTX_ZW,
 anchors={'birth': '民国35年生，丙戌年7月 日子时，男命（日数原盘未标，照实登记）', '局': '火六局',
  '命宫': '命宫在申（丙申，6–15）', '紫微落宫': '紫微在卯（疾厄宫，紫微贪狼）',
  '四化锚点': '大财双忌冲本命主大破财；天地数：庚之数是7决定目、戌宫宫干戊数是5、化科之数是3，5＋3＝8决定数（ZZ-M134）'},
 mp='大财双忌冲本命，主凶，主破财；此破耗之气纳集在本迁，其宫干庚之数是7决定目，表7位数，即百万元也。戌宫宫干戊数是5，唯戌干又化科到对宫（右弼星），视同加法，而化科之数是3，故5＋3＝8决定数。合解答案是8百万元。',
 oc='亿万富翁，于民国七十一年（壬戌年），37岁。合伙失败，被友冒领八百多万元。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH6-ZJ-UNLOCK-r96 复评通过（ZJ-10，四滤全过、锚点在场、决定性断法天地数已入册 ZZ-M134）并对 BATCH3-ZJ 原页复核，主持汇编续编 ZW-045（ZIWEI-SUPPLY-SUMMARY-r96 §一/§三）；断语据 BATCH6 §二书310 引文组录、以原断为限；结局据 BATCH6 §四案面复核摘要逐字照录、以结局正文为限；讲授回溯实录（A-low）；transcription=visual；日数原盘未标、不臆补。',
 reg='ZW-045：来源 BATCH3-ZJ ZJ-10 条＋BATCH6-ZJ-UNLOCK-r96 §二/§四原页复核引文对勘；SUMMARY-r96 编号 ZJ-10→ZW-045'),
dict(id='ZW-046', subject='女命，甲戌年10月亥时（日数原书未标），水二局',
 setting='《紫微斗数命理学正解》（许铨仁著）·第八章第二节案例（书pp.314–320，盘面书p.317）',
 prov=PROV_ZJ.format(s='第八章第二节案例（书pp.314–320，盘面书p.317）'), context=CTX_ZW,
 anchors={'birth': '民国25年生，甲戌年10月 日亥时，女命（日数原盘未标，照实登记）', '局': '水二局',
  '命宫': '命宫在子（丙子），武曲、天府坐命', '紫微落宫': '紫微在辰（官禄宫，紫微天相）',
  '四化锚点': '生年禄在财帛宫；生年忌又自化禄；逆行运大运命宫坐生年禄（大命与本财宫职重叠），禄入大命成万象归一元反格（ZZ-M135）'},
 mp='生年禄在财帛宫（六内宫），尤其是生年忌又自化禄，更主不利解。但因她走逆行运，大运命宫会坐到生年禄（大命与本财宫职重叠），配合生年忌又自化禄，禄入大命，即万象归一元之理则，变成反格，而得财。如果，生年忌又自化忌，那损财更严重，会形成损财又负债，纵然走逆行运，亦枉然无用矣。',
 oc='坤造年42～51行大运，赚大钱，于美国开餐厅与朋友合伙。',
 gn='入账口径：ZIWEI-SUPPLY-BATCH6-ZJ-UNLOCK-r96 复评通过（ZJ-11，四滤全过、锚点在场、决定性断法万象归一元已入册 ZZ-M135；②附注经 BATCH6 裁定为 A-low、不升 A）并对 BATCH3-ZJ 原页复核，主持汇编续编 ZW-046（ZIWEI-SUPPLY-SUMMARY-r96 §一/§三）；断语据 BATCH6 §二书318 引文逐字照录、以原断为限；结局据 BATCH6 §四案面复核摘要逐字照录、以结局正文为限；讲授回溯实录（A-low）；transcription=visual；日数原盘未标、不臆补。',
 reg='ZW-046：来源 BATCH3-ZJ ZJ-11 条＋BATCH6-ZJ-UNLOCK-r96 §二/§四原页复核引文对勘；SUMMARY-r96 编号 ZJ-11→ZW-046'),
]
assert [c['id'] for c in ZWCASES] == ZW_IDS
for c in ZWCASES:
    cid = c['id']
    cards[cid] = {'id': cid, 'tradition': 'ziwei', 'subject': c['subject'],
                  'context': c['context'], 'question': Q_ZW, 'setting': c['setting'],
                  'provenance': c['prov'], 'redistributable': False,
                  'license_status': LIC_M, 'anchors': c['anchors']}
    golds[cid] = {'id': cid, 'master_prediction': c['mp'], 'outcome_record': c['oc'],
                  'tradition': 'ziwei', 'pollution': 'low', 'grade': 'A-low',
                  'grade_note': c['gn'], 'provenance': c['prov'],
                  'license_status': LIC_M, 'redistributable': False}
    register[cid] = c['reg'] + '；资格断言：pollution=low、锚点在场、grade=A-low（登记件在册）'

# ================= 落盘 + 组装 + 快照 =================
assert set(cards) == set(ALL) and set(golds) == set(ALL)
for cid in ALL:
    assert list(cards[cid].keys()) == INPUT_FIELDS, cid
    assert list(golds[cid].keys()) == GOLD_FIELDS, cid
    assert golds[cid]['pollution'] == 'low' and golds[cid]['redistributable'] is False
    assert golds[cid]['master_prediction'].strip() and golds[cid]['outcome_record'].strip()
    # 输入卡泄漏自检：结局关键串不得入卡（逐例粗检：outcome 全文不得为卡面子串）
    blob = json.dumps(cards[cid], ensure_ascii=False)
    assert golds[cid]['outcome_record'] not in blob, cid
    with io.open(f'{OUT}/inputs/{cid}.json', 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=1); f.write('\n')

gold_path = OUT + '/test_gold.jsonl'
with io.open(gold_path, 'w', encoding='utf-8') as f:
    for cid in ALL:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')
gold_bytes = open(gold_path, 'rb').read()
gold_sha = hashlib.sha256(gold_bytes).hexdigest()
assert len(gold_bytes.decode('utf-8').strip().split('\n')) == 28

# 快照：自 method/ 当前活版整目录复制（体例承 h34：快照树＝SKILL/VALIDATION/VERIFY-LOG/references/tools 共21件，METHOD-* 根件不入）
SRC = B + '/method'; SNAP = OUT + '/kb-snapshot'
snap_files = []
for root, dirs, files in os.walk(SRC):
    dirs.sort()
    for fn in sorted(files):
        rel = os.path.relpath(os.path.join(root, fn), SRC).replace(os.sep, '/')
        if rel.startswith('METHOD-'):
            continue
        snap_files.append(rel)
assert len(snap_files) == 21, snap_files
sha_lines = []
for rel in snap_files:
    data = open(os.path.join(SRC, rel), 'rb').read()
    dst = os.path.join(SNAP, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, 'wb') as f: f.write(data)
    sha_lines.append('%s  %s' % (hashlib.sha256(data).hexdigest(), rel))
with io.open(OUT + '/kb-snapshot-sha256.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sha_lines) + '\n')

# 快照差异：holdout35 快照 vs 平台快照 runs/round96/kb-snapshot 逐件对勘
PLAT = R96 + '/kb-snapshot'
plat_files = []
for root, dirs, files in os.walk(PLAT):
    for fn in files:
        plat_files.append(os.path.relpath(os.path.join(root, fn), PLAT).replace(os.sep, '/'))
assert sorted(plat_files) == sorted(snap_files), (plat_files, snap_files)
diffs = []
for rel in snap_files:
    a = open(os.path.join(SNAP, rel), 'rb').read()
    b = open(os.path.join(PLAT, rel), 'rb').read()
    if a != b: diffs.append(rel)

report = {'set': 'holdout35', 'round': 96, 'ids': ALL,
          'composition': {'ziwei': ZW_IDS, 'da': DA_IDS, 'by': BY_IDS},
          'cards_written': 28, 'gold_lines': 28, 'gold_sha256': gold_sha,
          'gold_bytes': len(gold_bytes), 'snapshot_files': snap_files,
          'snapshot_diff_vs_platform_r96': diffs, 'register': register,
          'id_assert': '28 id 与主持定版逐字对撞一致；对 used-ids-r96.json（1333）交集为空；台账续位复算 DA/BY 与定版逐 id 全等'}
with io.open(R96 + '/holdout35-build-frag-r96.json', 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=1); f.write('\n')
print('cards 28, gold sha256:', gold_sha)
print('snapshot diffs vs platform:', diffs)
print('BUILD OK')
