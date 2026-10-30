#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R50 数据席（组集数据席）：按 PREREG-ADDENDUM-1 裁定组建并封存 holdout19。

裁定：runs/round50/PREREG-ADDENDUM-1.md（构成写死：非梦占 13＋梦占 12＝T25；
YJ2-007 附条件改写；四限度；本轮只组集封存、不开封）。
配套口径：runs/round47/PREREG.md §5（验封常例与转录规格 v1 照行）、
runs/round42/PREREG.md §1.2（转录规格 v1 字段集）＋§5（内容级断语扫描三道）。

内容级断语扫描标记集：逐字复制 runs/round42/PREREG.md §5 常量（见下方
LEVEL1/LEVEL2/FIELD_BLACKLIST，脚本头注释引节号＝R42 PREREG §5）。
本席执行第一道（候选材料 input_side 制备期扫描）与第二道（建卡自校验逐卡
扫描）；第三道（主持验封）非本席执行，报告中留位。

回退规则（主持预授权，仅梦占侧）：梦占 12 例中恰 1 例无法逐字建卡（断语或
结局无逐字文本）→ 剔除该例、非梦占按编号最小补 YJ2-008、构成改 T＝26；
无法建卡 ≥2 例 → 本脚本中止报主持，不自改构成。

只建卡与封存：不作断、不评分、不开封验收、不做 git 操作。
零复用复核只对已用集 id 集（禁打开已封存集金标正文做内容比对）：已用 id
来源＝phase2/splits2.json 之 holdout2（29）＋holdout3–18 各 test_gold.jsonl
仅取 id 字段（490）＋data/master-baseline-dev9.json 键集 dev9（487），
并集 901（与 R47 PREREG §1⑥「已用并集 901 id」登记合）。
"""
import json, hashlib, os, subprocess, sys

BASE = os.path.expanduser('~/workspace/divination/benchmark/phase3')
ROOT = os.path.expanduser('~/workspace/divination')
R50 = os.path.join(BASE, 'runs/round50')
OUT_DIR = os.path.join(BASE, 'holdout19')
IN_DIR = os.path.join(OUT_DIR, 'inputs')
os.makedirs(IN_DIR, exist_ok=True)
REPORT_PATH = os.path.join(R50, 'build-holdout19-report-r50.json')

# ---------- 内容级断语扫描标记集（逐字复制 R42 PREREG §5） ----------
# 一级标记（断语类）——逐字复制 PREREG §5
LEVEL1 = ['断语线索', '断曰', '斷語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
# 二级标记（结局侧状态措辞）——逐字复制 PREREG §5
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
# 字段名黑名单片段（PREREG §5：字段名含断语/断曰/正议/验语/占断/线索·断者）
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '斷曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']


def scan_content(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            hits += scan_content(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_content(v, f'{path}[{i}]')
    elif isinstance(obj, str):
        for lvl, markers in (('L1', LEVEL1), ('L2', LEVEL2)):
            for m in markers:
                idx = obj.find(m)
                if idx >= 0:
                    hits.append([path, lvl, m, obj[max(0, idx - 12):idx + len(m) + 12]])
    return hits


def scan_field_names(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            for frag in FIELD_BLACKLIST:
                if frag in k:
                    hits.append([f'{path}/{k}', frag])
                    break
            hits += scan_field_names(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_field_names(v, f'{path}[{i}]')
    return hits


def load_json(p):
    return json.load(open(p, encoding='utf-8'))


# ---------- 门：例级零复用复核（只对 id 集） ----------
h2_ids = set(load_json(os.path.join(ROOT, 'benchmark/phase2/splits2.json'))['holdout2'])
h3_18_ids = set()
for i in range(3, 19):
    p = os.path.join(BASE, f'holdout{i}/test_gold.jsonl')
    for line in open(p, encoding='utf-8'):
        if line.strip():
            h3_18_ids.add(json.loads(line)['id'])  # 只取 id，不作内容比对
dev9_ids = set(load_json(os.path.join(BASE, 'data/master-baseline-dev9.json')).keys())
used_union = h2_ids | h3_18_ids | dev9_ids
assert len(h2_ids) == 29 and len(h3_18_ids) == 490 and len(dev9_ids) == 487, \
    (len(h2_ids), len(h3_18_ids), len(dev9_ids))
assert len(used_union) == 901, len(used_union)

# ---------- 构成（ADDENDUM-1 写死） ----------
NON_DREAM = ['SS-001', 'SS-005', 'YJ2-005', 'YJ2-006', 'YJ2-007', 'YJ2-009', 'YJ2-010',
             'YJ3-001', 'YJ3-002', 'YJ3-003', 'YJ3-004', 'YJ3-005', 'YW3-001']
DREAM = ['XJ47-047', 'XJ47-092', 'XJ47-289', 'XJ47-373', 'XJ47-386', 'XJ47-442',
         'XJ47-500', 'XJ47-502', 'LK-058', 'LK-046', 'LK-054', 'YZ-C019']
FALLBACK_POOL = ['YJ2-008', 'YJ2-011', 'YJ2-012', 'YJ2-013']  # 编号最小者优先
CARD_DIRS = {
    'SS': 'runs/round48/digestion/cards-mining-sanshu',
    'YJ2': 'runs/round49/digestion/cards-mining-yijian-r49',
    'YJ3': 'runs/round50/digestion/cards-mining-yijian-r50',
    'YW3': 'runs/round50/digestion/cards-mining-yuewei-r50',
}


def card_dir(cid):
    for pref in ('YJ2', 'YJ3', 'YW3', 'SS'):
        if cid.startswith(pref):
            return os.path.join(BASE, CARD_DIRS[pref])
    raise KeyError(cid)


INPUT_FIELDS = ['id', 'tradition', 'subject', 'context', 'question', 'setting',
                'provenance', 'redistributable', 'license_status']
GOLD_EXTRA = ['master_predictions', 'outcome', 'passage_full',
              'grade_suggestion', 'grade_reason',
              'contamination_suggestion', 'contamination_reason']
BANNED_IN_CARD = {'grade_note', 'grade_suggestion', 'grade_reason', 'contamination',
                  'contamination_suggestion', 'contamination_reason',
                  'contamination_rationale', 'outcome', 'outcome_grade',
                  'master_predictions', 'passage_full', 'record_status', 'notes',
                  'master', 'seal_eligible', 'holdout_eligible', 'review'}


def banned_key_scan(obj, path=''):
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in BANNED_IN_CARD:
                hits.append(f'{path}/{k}')
            hits += banned_key_scan(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += banned_key_scan(v, f'{path}[{i}]')
    return hits


# ---------- 梦占 12 例：自登记全文建卡（逐字文本一律照登记件，不臆补） ----------
# 玄解 8：runs/round47/digestion/REGISTER-xuanjie-mengzheng-r47.md 各例精读小节
# 类考 3：runs/round46/digestion/DIGEST-leikao-r46.md §2.3 行＋
#         runs/round47/digestion/NEARPOOL-review-r47.md 复议节（污染以降 low 为准）
# 逸旨 1：runs/round47/digestion/RECHECK-yz-c019-r47.md（逐字复核件）
XJ_PROV = ('《夢林玄解》·{vol}；底本 incoming/wanted-books-3/Book/'
           '梦林玄解 (（宋）邵雍，（明）陈士元).pdf，PDF {pages}；transcription=visual；'
           '登记件 runs/round47/digestion/REGISTER-xuanjie-mengzheng-r47.md')
LK_PROV = ('《夢占類考》（明·張鳳翼輯，萬曆乙酉信陽王氏梓行本）·{part}；底本 '
           'incoming/wanted-books-3/Book/梦占类考 (（明）张凤翼辑).pdf，{pages}；'
           'transcription=visual；登记件 runs/round46/digestion/DIGEST-leikao-r46.md '
           '§2.3＋runs/round47/digestion/NEARPOOL-review-r47.md 复议节')
DREAM_LICENSE = '古典文本公有领域；底本为用户经学校图书馆提供之扫描本，内部研究用'

DREAM_DATA = {
    'XJ47-047': {
        'subject': '陳奇，初被召',
        'context': '陳奇初被召，夜夢星墜壓腳，醒後告人問此夢。',
        'question': '此夢主何吉凶？',
        'setting': '陳奇初被召時；夢占（自占，醒後告人）',
        'provenance': XJ_PROV.format(vol='卷三十星斗類', pages='1062–1063'),
        'master': '陳奇本人（自占）',
        'source': '《夢林玄解》卷三十星斗類「星墜壓腳」',
        'statement_excerpt': '星則好風，星則好雨，夢星壓腳，必無善徵。',
        'outcome': '後竟以造謗書見枉，遂至于大戮。謚忠肅。',
        'passage_full': '陳奇初被召，夜夢星墜壓腳，明日告人曰：星則好風，星則好雨，夢星壓腳，必無善徵。後竟以造謗書見枉，遂至于大戮，謚忠肅。',
        'grade_suggestion': 'A',
        'grade_reason': '自占逐字、結局獨立詳載（REGISTER 精讀判 A）；結局「謗」字 R47 登記待核，R48 回原頁復核讀定（runs/round48/data-verify/XJ47-chars-recheck-r48.md §1），斷語與 passage_full 以 R48 原頁欄文逐字為準（R47 登記斷語作「夢星墜壓腳」，原頁欄文作「夢星壓腳」，異文在此登記）。',
        'contamination_suggestion': 'low',
        'contamination_reason': '入賬口徑承 R47 主持核查（A＋low）。口徑衝突標旗：玄解登記作「宋人陳奇，冷僻」判 low；類考復議件 NEARPOOL-review-r47.md LK-039 節證同案（陳奇星墜壓腳，類考標出處北史）傳主陳奇有《北史》《魏書》本傳與百科專條、結局謗書案為其傳主幹，污染維持 mid——兩登記件口徑不一致，本卡污染字段照入賬裁定作 low，衝突如實提請主持知悉。',
    },
    'XJ47-092': {
        'subject': '黃芸（黃主事，江西豐城人），應舉士人',
        'context': '黃芸夜夢鄰火將延，戴斗登山避之，堂上有冠冕者四座待之。',
        'question': '此夢主何吉凶？於功名主何應？',
        'setting': '明·江西豐城；應舉前後夜夢，夢占（自占，「竊詳」自解）',
        'provenance': XJ_PROV.format(vol='卷三十山水類', pages='1074–1075'),
        'master': '黃芸本人（自占）',
        'source': '《夢林玄解》卷三十山水類「戴斗登山」',
        'statement_excerpt': '火者，文明之象；斗者，魁也，戴斗者，魁在頭上也；赤馬者，丙午也；鹿者，祿也。',
        'outcome': '是秋鄉薦，黃中詩經亞魁，甲辰進士，丙午授南京刑部主事……後甲辰會試果中一百四十六名……年三十四授南京按察司，成化丙午年郎（即）赤馬之應也。',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '自占長文逐字、結局跨年詳載（REGISTER 精讀判 A）；結局為登記「逐字要點」（含登記編者括注「（即）」照錄）；斷語兼及赤馬、鹿象（篇內連載諸夢成分），輸入側夢境按登記「夢者/事」首夢原文建卡、不補夢境細節；登記件未載全條全文，passage_full 無逐字全文可錄、不臆補，置 null 並在此登記。',
        'contamination_suggestion': 'low',
        'contamination_reason': '明代地方人物，源出地方/家乘文獻（REGISTER 精讀判 low）。',
    },
    'XJ47-289': {
        'subject': '王徽（字尚文，南京錦衣衛人），應試士人',
        'context': '景泰丙子鄉試前，王徽夜夢登高梯三次，第三次墜梯。',
        'question': '此夢主何吉凶？於功名主何應？',
        'setting': '明·景泰丙子鄉試前，南京；夢占（自占）',
        'provenance': XJ_PROV.format(vol='卷三十二科第類', pages='1131'),
        'master': '王徽本人（自占）',
        'source': '《夢林玄解》卷三十二科第類「三塲之兆」',
        'statement_excerpt': '自謂：此必三塲之兆。',
        'outcome': '巴（既）而領鄉薦，連中會試，尋聞母訃，不與廷試，始悟墜梯之夢……迨揭曉，中一十八名，廷試名在二甲第三，兩度皆奇驗。',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '自占逐字、結局詳載且墜梯應於丁憂一節非復述斷語（REGISTER 精讀判 A）；結局為登記「逐字要點」（「巴（既）」為登記讀法括注照錄）；篇內第二夢（入試院見榜名）無斷語、未入本卡；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '明人，冷僻（REGISTER 精讀判 low）。',
    },
    'XJ47-373': {
        'subject': '錢山（字靜夫，滁州人），會試士人',
        'context': '錢山會試畢，夜夢手舉一傘，同舍傅恕在座，以夢告之。',
        'question': '此夢主何吉凶？於名次主何應？',
        'setting': '明·會試畢；夢占（同舍傅恕占）',
        'provenance': XJ_PROV.format(vol='卷三十三家伙類', pages='1157'),
        'master': '傅恕（同舍，江西臨江縣人）',
        'source': '《夢林玄解》卷三十三家伙類「手舉一傘」',
        'statement_excerpt': '吾鄉曾夢舉傘者，人或占云：當中第六名也。君當應此兆。蓋傘字五人，今夢舉傘者，在五人之下故也。',
        'outcome': '迨揭曉，果符前占……後果觀政刑部，授南臺御史。',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '斷語逐字（REGISTER 精讀判 A；斷語含轉述鄉占成分，精讀註明如上）；結局逐字（含省略號為登記原文節錄形態）；篇末附第二夢（卸頭取髮）未入本卡；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '明人，冷僻（REGISTER 精讀判 low）。',
    },
    'XJ47-386': {
        'subject': '曾崇志之父（僉憲）',
        'context': '曾崇志之父夢澡浴之後，胸前隱隱生獅牙紋，以夢告子曾崇志。',
        'question': '此夢主何吉凶？於仕途主何應？',
        'setting': '明；夢占（子曾崇志為父占）',
        'provenance': XJ_PROV.format(vol='卷三十三門梁類', pages='1160–1161'),
        'master': '曾崇志',
        'source': '《夢林玄解》卷三十三門梁類「梁傾桁」（主案：父夢獅牙紋）',
        'statement_excerpt': '大人行當君內臺矣。獅牙乃風憲花樣，不衣于外，而生于內，是在內也。',
        'outcome': '巴（已）而陞僉都御史……果驗。',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '斷語逐字（含申說，REGISTER 精讀判 A）；結局逐字（「巴（已）」為登記讀法括注照錄，末「果驗」為原文自載）；篇內另附曾氏自夢銀章、梁傾桁二事未入本卡；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '明人，冷僻（REGISTER 精讀判 low）。',
    },
    'XJ47-442': {
        'subject': '柳凌，汝州刺史',
        'context': '柳凌夜夢一人呈案，言其欠柴一千七百束。韋正貫時應舉，柳留之為署軍事判官，以夢問之。',
        'question': '此夢主何吉凶？',
        'setting': '唐·汝州刺史任上；夢占（韋正貫占）',
        'provenance': XJ_PROV.format(vol='卷三十三柴薪類', pages='1176'),
        'master': '韋正貫',
        'source': '《夢林玄解》卷三十三柴薪類「欠柴一千七百束」',
        'statement_excerpt': '柴薪，木也；公得非不久乎。',
        'outcome': '月餘，柳卒……唯官中欠柴一千七百束，方省柳前夢。',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '斷語逐字、結局含數字獨立覆核（REGISTER 精讀判 A）；結局為登記「逐字要點」；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '唐人冷僻（REGISTER 精讀判 low）。',
    },
    'XJ47-500': {
        'subject': '阮登炳，應試士人',
        'context': '阮登炳夜夢前科狀元毛自知乘獨角青牛，以火照交于其身上。',
        'question': '此夢主何吉凶？於阮登炳功名主何應？',
        'setting': '清·科場；夢占（自解）',
        'provenance': XJ_PROV.format(vol='卷三十四六畜類', pages='1190'),
        'master': '阮登炳本人（自解）',
        'source': '《夢林玄解》卷三十四六畜類「獨角青牛」',
        'statement_excerpt': '青牛，年庚也；火照交身上，乃登炳之義；花甲告周，將代毛自知矣。',
        'outcome': '後乙丑，果狀元及第。',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '自解逐字、結局獨立（REGISTER 精讀判 A）；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '清人科場條，冷僻（REGISTER 精讀判 low）。',
    },
    'XJ47-502': {
        'subject': '林誌，會試士人',
        'context': '林誌會試時，夜夢人牽馬一匹過其前。',
        'question': '此夢主何吉凶？於功名主何應？',
        'setting': '明·會試時；夢占（自占）',
        'provenance': XJ_PROV.format(vol='卷三十四六畜類', pages='1190–1191'),
        'master': '林誌本人（自占）',
        'source': '《夢林玄解》卷三十四六畜類「牽馬過前」',
        'statement_excerpt': '牽馬在前，予祿至矣。',
        'outcome': '傳臚，狀元乃馬鐸，公居第二。',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '自占逐字、文本完整；自解祿至而名次為人所先，斷語與結局有落差，精讀如實記（REGISTER 精讀判 A）；結局為登記「逐字要點」；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '明人，冷僻（REGISTER 精讀判 low）。',
    },
    'LK-058': {
        'subject': '李伯怜',
        'context': '李伯怜夜夢洗白馬，以夢問占者梅伯成。',
        'question': '此夢主何吉凶？所憂之事如何？',
        'setting': '夢占（梅伯成占，反語斷法）；時代原文未標',
        'provenance': LK_PROV.format(part='卷三走獸部', pages='抽樣頁 PDF p90/100/110 區間（逐例頁位登記未單列）'),
        'master': '梅伯成',
        'source': '《夢占類考》卷三走獸部「洗白馬」（本條未標出處）',
        'statement_excerpt': '凡郵人好反語：洗白馬，濕白米也；君所憂，或有風水之虞乎',
        'outcome': '數日弟至，果曾於渭河中覆舟',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '斷語具名逐字、結局獨立事件文本（DIGEST-leikao-r46 A 預判，主持 R47 核查入賬）；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '原判 low（DIGEST-leikao-r46）；標誌語句冷僻、夢者無獨立條目。',
    },
    'LK-046': {
        'subject': '張宅，敦煌郡主簿',
        'context': '張宅夜夢走馬上山，還繞舍三周，但見松柏墓門。',
        'question': '此夢主何吉凶？',
        'setting': '夢占（解者類考本條未具名）；時代原文未標',
        'provenance': LK_PROV.format(part='卷一地理部', pages='抽樣頁 PDF p30'),
        'master': '解者（類考本條未具名）',
        'source': '《夢占類考》卷一地理部「走馬上山」（原書標出處僅「史」一字，含糊）',
        'statement_excerpt': '松柏，墓門象也；三周，三棘也；後三年必有大禍',
        'outcome': '宅果以（譖）反伏誅',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '斷語逐字、結局獨立（DIGEST-leikao-r46 A 預判，主持 R47 復議核查入賬）；結局「（譖）」為登記待核讀法括注照錄；同案另見《夢林玄解》（XJ47-081，索統斷版）未入選本集，不構成集內復用；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '原判 low-mid，R47 復議以冷門性新證據（標誌短語精確檢索零命中、傳主無任何獨立條目、無類書著錄）降 low（NEARPOOL-review-r47.md LK-046 節，復議後口徑），主持採納入賬。',
    },
    'LK-054': {
        'subject': '李權，宋士子',
        'context': '李權夜夢入張氏之松，虎頭洲上。',
        'question': '此夢主何吉凶？於功名主何應？',
        'setting': '宋；夢占（自解）',
        'provenance': LK_PROV.format(part='卷三走獸部', pages='抽樣頁 PDF p90/100/110 區間（逐例頁位登記未單列）'),
        'master': '李權本人（自解）',
        'source': '《夢占類考》卷三走獸部「虎頭洲」（本條未標出處）',
        'statement_excerpt': '虎頭，虎榜頭也',
        'outcome': '俄而登科',
        'passage_full': None,
        'grade_suggestion': 'A',
        'grade_reason': '自解逐字、結局獨立（DIGEST-leikao-r46 A 預判（弱，自解），主持 R47 復議核查入賬；弱點在判級面、與污染面無關，NEARPOOL 註明）；登記件未載全條全文，passage_full 置 null、不臆補。',
        'contamination_suggestion': 'low',
        'contamination_reason': '原判 low-mid，R47 復議以故事與傳主雙零命中、類考未標出處無流傳通道降 low（NEARPOOL-review-r47.md LK-054 節，復議後口徑），主持採納入賬。',
    },
    'YZ-C019': {
        'subject': '索充，晉人',
        'context': '索充夜夢天上有二棺落其前，以夢問索紞。',
        'question': '此夢主何吉凶？',
        'setting': '晉；夢占（索紞占）；源書引《晉書》',
        'provenance': ('《夢占逸旨》·卷六篇十三（棺椁喪葬類）；底本 incoming/wanted-books-3/Book/'
                       '梦占逸旨 (（明）陈士元纂).pdf，印刷頁 55＝PDF 頁 60；transcription=visual；'
                       '登記件 runs/round47/digestion/RECHECK-yz-c019-r47.md'),
        'master': '索紞',
        'source': '《夢占逸旨》卷六篇十三「索充夢棺」（引《晉書》）',
        'statement_excerpt': '棺者，職也，當有京師貴人舉君。二棺者，□□。',
        'outcome': '再遷（綱目句：「夢二棺落天上，而索充再遷」）',
        'passage_full': '夢二棺落天上，而索充再遷。晉書曰：索充夢天上有二棺落充前，以問索紞。紞曰：「棺者，職也，當有京師貴人舉君。二棺者，□□。」',
        'grade_suggestion': 'A',
        'grade_reason': 'R47 回源逐字復核後主持裁定入賬（A＋low 維持）；限度兩項如實登記：①斷語尾二字原頁欄末漫漶未讀定、標 □□ 掛起不臆補；②結局在本頁僅有綱目級「再遷」二字、引文段未另載獨立結局句（RECHECK-yz-c019-r47.md §四）。passage_full 由綱目句與源書引文兩段逐字登記拼接（全例完整落印刷頁 55 一頁內）。',
        'contamination_suggestion': 'low',
        'contamination_reason': '入賬口徑承 R47 主持裁定（low 維持）。',
    },
}


# ---------- 梦占逐字建卡门（回退规则执行点） ----------
buildability = {}
for cid in DREAM:
    d = DREAM_DATA[cid]
    ok_stmt = bool(d['statement_excerpt'].strip())
    ok_out = bool(d['outcome'].strip())
    buildability[cid] = {'statement_verbatim_present': ok_stmt,
                         'outcome_verbatim_present': ok_out,
                         'buildable': ok_stmt and ok_out}
unbuildable = [c for c in DREAM if not buildability[c]['buildable']]
fallback_triggered = False
fallback_case = None
dream_final = list(DREAM)
non_dream_final = list(NON_DREAM)
if len(unbuildable) >= 2:
    print(json.dumps({'ABORT': '梦占无法逐字建卡 ≥2 例，停工回传主持',
                      'unbuildable': unbuildable}, ensure_ascii=False))
    sys.exit(2)
if len(unbuildable) == 1:
    fallback_triggered = True
    fallback_case = unbuildable[0]
    dream_final.remove(fallback_case)
    add = FALLBACK_POOL[0]
    assert add == 'YJ2-008'
    non_dream_final.append(add)

ORDER = non_dream_final + dream_final
T = len(ORDER)
assert T == (26 if fallback_triggered else 25), T
assert len(set(ORDER)) == T
assert all(cid not in used_union for cid in ORDER), '选例与已用并集相交（零复用门）'
assert all(cid not in used_union for cid in FALLBACK_POOL), '回退池与已用并集相交'

# ---------- YJ2-007 附条件改写（转录规格 v1：输入侧纯背景） ----------
YJ2007_OLD_CONTEXT = '邵南至婺，范之才喜甚。邵南通夕细推之后，复谒屏人而语，催其遣健步者出城迎取文书。'
YJ2007_NEW_CONTEXT = '邵南至婺州，時范之才守婺州，邵南為其客，范之才喜其至。范之才以拜命之事問邵南，邵南通夕細推之。'

# ---------- 建卡 ----------
cards, golds = {}, {}
strip_register, scan_stage1, gold_deviations = {}, {}, []

for cid in ORDER:
    if cid in DREAM_DATA and cid in dream_final:
        d = DREAM_DATA[cid]
        input_side = {'id': cid, 'tradition': 'mengzhan', 'subject': d['subject'],
                      'context': d['context'], 'question': d['question'],
                      'setting': d['setting'], 'provenance': d['provenance'],
                      'redistributable': False, 'license_status': DREAM_LICENSE}
        # 第一道：候选材料 input_side 全字段递归扫描（内容级＋字段名黑名单）
        scan_stage1[cid] = {'content_hits': scan_content(input_side),
                            'fieldname_hits': scan_field_names(input_side),
                            'source': '登记件自建 input_side（本脚本 DREAM_DATA）'}
        card = dict(input_side)
        strip_register[cid] = ['（自登记建卡，无候选卡管理字段；斷語/結局/判級/污染/'
                               '三鍵等登記側內容一律不入輸入卡，只入金標）']
        gold = dict(input_side)
        gold['master_predictions'] = [{
            'master': d['master'], 'date': None, 'tradition': 'mengzhan',
            'direction': None, 'key_assertions': [], 'source': d['source'],
            'statement_excerpt': d['statement_excerpt']}]
        gold['outcome'] = {'description': d['outcome'],
                           'verified_by': '原文結局文本（逐字，據登記件）'}
        gold['passage_full'] = d['passage_full']
        gold['grade_suggestion'] = d['grade_suggestion']
        gold['grade_reason'] = d['grade_reason']
        gold['contamination_suggestion'] = d['contamination_suggestion']
        gold['contamination_reason'] = d['contamination_reason']
        gold['grade_note'] = d['grade_reason'] + '｜污染：' + d['contamination_reason']
        cards[cid], golds[cid] = card, gold
        continue

    dpath = card_dir(cid)
    cand_in = load_json(os.path.join(dpath, f'{cid}-input.json'))
    cand_gold = load_json(os.path.join(dpath, f'{cid}-gold.json'))
    # 第一道：候选材料 input_side（候选输入卡全字段）递归扫描
    scan_stage1[cid] = {'content_hits': scan_content(cand_in),
                        'fieldname_hits': scan_field_names(cand_in),
                        'source': os.path.relpath(os.path.join(dpath, f'{cid}-input.json'), BASE)}
    stripped = [k for k in cand_in if k not in INPUT_FIELDS]
    gold_only = [k for k in cand_gold if k not in INPUT_FIELDS]
    strip_register[cid] = ([f'{k}（管理字段，剥离）' for k in stripped] +
                           [f'{k}（金标侧，不入输入卡）' for k in gold_only])
    card = {k: cand_in[k] for k in INPUT_FIELDS}
    if cid == 'YJ2-007':
        assert cand_in['context'] == YJ2007_OLD_CONTEXT, cand_in['context']
        card['context'] = YJ2007_NEW_CONTEXT
    cards[cid] = card

    gold = {k: cand_gold[k] for k in INPUT_FIELDS}
    for k in GOLD_EXTRA:
        gold[k] = cand_gold[k]
    if cid == 'YJ2-007':
        gold['context'] = cand_in['context']  # 金标侧保留原卡 context 全文（封存侧）
    if cid == 'YW3-001':
        assert cand_gold['grade_suggestion'] == 'B'
        gold['grade_suggestion'] = 'A'
        gold['grade_reason'] = (cand_gold['grade_reason'] +
                                '；主持 R50 复核改判 A（承 PREREG-ADDENDUM-1 §一 YW3-001 备注：'
                                '台账 supply-ledger-r50-rest.jsonl），本卡金标以改判为准、'
                                '原候选卡 B 级原文并存于此句之前。')
        gold_deviations.append('YW3-001 金标 grade_suggestion 由候选卡 B 改为主持改判 A（ADDENDUM-1），grade_reason 尾部并记改判出处')
    golds[cid] = gold

assert set(cards) == set(ORDER) and set(golds) == set(ORDER)

# 输入卡字段白名单断言＋禁用键递归零残留
for cid in ORDER:
    assert list(cards[cid].keys()) == INPUT_FIELDS, (cid, list(cards[cid].keys()))
    assert not banned_key_scan(cards[cid]), (cid, banned_key_scan(cards[cid]))
    assert golds[cid]['master_predictions'][0]['statement_excerpt'].strip(), cid
    assert golds[cid]['outcome']['description'].strip(), cid

# ---------- 第二道：建卡自校验逐卡扫描 ----------
scan_stage2 = {}
for cid in ORDER:
    ch = scan_content(cards[cid])
    fh = scan_field_names(cards[cid])
    scan_stage2[cid] = {'content_hits': ch, 'fieldname_hits': fh}
    assert not ch and not fh, (cid, ch, fh)  # 任一命中即中止，不交付

# 第一道处置登记：命中只许落在将被整项剥离的管理字段（notes/record_status）
stage1_disposition = {}
for cid in ORDER:
    hits = scan_stage1[cid]['content_hits'] + scan_stage1[cid]['fieldname_hits']
    paths = sorted({h[0].split('/')[1] if h[0].startswith('/') and len(h[0].split('/')) > 1 else h[0]
                    for h in hits})
    stage1_disposition[cid] = {
        'hit_fields': paths,
        'disposition': ('命中字段均为管理字段（notes），整项剥离不入卡；剥离后第二道复扫零命中放行'
                        if hits else '零命中')}

# ---------- 落盘 ----------
for cid in ORDER:
    with open(os.path.join(IN_DIR, f'{cid}.json'), 'w', encoding='utf-8') as f:
        json.dump(cards[cid], f, ensure_ascii=False, indent=2)
        f.write('\n')
gold_path = os.path.join(OUT_DIR, 'test_gold.jsonl')
with open(gold_path, 'w', encoding='utf-8') as f:
    for cid in ORDER:
        f.write(json.dumps(golds[cid], ensure_ascii=False) + '\n')

read_cards = {fn[:-5]: load_json(os.path.join(IN_DIR, fn)) for fn in os.listdir(IN_DIR) if fn.endswith('.json')}
read_golds = [json.loads(l) for l in open(gold_path, encoding='utf-8') if l.strip()]
assert set(read_cards) == set(ORDER) and len(read_cards) == T
assert {g['id'] for g in read_golds} == set(ORDER) and len(read_golds) == T
# 落盘后复扫（第二道对盘上文件重行）
for cid in ORDER:
    assert not scan_content(read_cards[cid]) and not scan_field_names(read_cards[cid]), cid

sha_lib = hashlib.sha256(open(gold_path, 'rb').read()).hexdigest()
sha_sum = subprocess.run(['sha256sum', gold_path], capture_output=True, text=True).stdout.split()[0]
assert sha_lib == sha_sum

# ---------- 构成统计 ----------
from collections import Counter
SOURCE_OF = {}
for cid in ORDER:
    if cid in ('SS-001', 'SS-005') or cid.startswith(('YJ2', 'YJ3')):
        SOURCE_OF[cid] = '夷坚志'
    elif cid.startswith('YW3'):
        SOURCE_OF[cid] = '阅微草堂笔记'
    elif cid.startswith('XJ47'):
        SOURCE_OF[cid] = '夢林玄解'
    elif cid.startswith('LK'):
        SOURCE_OF[cid] = '夢占類考'
    elif cid.startswith('YZ'):
        SOURCE_OF[cid] = '夢占逸旨'
trad_counts = Counter(cards[c]['tradition'] for c in ORDER)
src_counts = Counter(SOURCE_OF[c] for c in ORDER)

report = {
    'round': 50, 'set': 'holdout19', 'built_by': '组集数据席（R50）',
    'ruling': 'runs/round50/PREREG-ADDENDUM-1.md',
    'T': T, 'order': ORDER,
    'composition': {
        'non_dream': non_dream_final, 'dream': dream_final,
        'by_source': dict(src_counts), 'by_tradition': dict(trad_counts),
        'dream_share': f"{len(dream_final)}/{T} = {len(dream_final) / T:.1%}",
        'yijian_share': f"{src_counts['夷坚志']}/{T} = {src_counts['夷坚志'] / T:.1%}",
    },
    'fallback': {'triggered': fallback_triggered,
                 'removed_case': fallback_case,
                 'buildability': buildability,
                 'note': ('梦占 12 例断语与结局均有登记逐字文本（逐例见 buildability 与各卡 '
                          'grade_note 之限度登记：XJ47-092/289/442/502 结局为登记「逐字要點」、'
                          'YZ-C019 断语尾二字 □□ 挂起且结局仅纲目级二字——均属有逐字文本而 '
                          '成色受限，非「无逐字文本」，不构成回退触发）'
                          if not fallback_triggered else
                          f'回退触发：{fallback_case} 无法逐字建卡，剔除并以 YJ2-008 补入，T＝26')},
    'zero_reuse_recheck': {
        'holdout2_ids': 29, 'holdout3_18_gold_ids': 490, 'dev9_ids': 487,
        'used_union': 901, 'method': '只对 id 集（phase2/splits2.json、holdout3–18 '
        'test_gold.jsonl 仅取 id 字段、data/master-baseline-dev9.json 键集）；未打开任何已封存集金标正文做内容比对',
        'selected_hit_count': 0,
        'fallback_pool_hit_count': 0},
    'input_field_whitelist': INPUT_FIELDS,
    'strip_register': strip_register,
    'yj2_007_rewrite': {
        'rule': 'ADDENDUM-1 附条件：输入侧按转录规格 v1 改写为纯背景（去掉原卡 context 中断语指向成分）',
        'before_context_input_side': YJ2007_OLD_CONTEXT,
        'after_context_input_side': YJ2007_NEW_CONTEXT,
        'note': '被改原文（before）原样留存于此与金标侧 context；改写只及输入卡 context，subject/question/setting/provenance 不动'},
    'gold_deviations': gold_deviations,
    'scan_stage1_candidate_prep': scan_stage1,
    'scan_stage1_disposition': stage1_disposition,
    'scan_stage2_card_selfcheck': scan_stage2,
    'scan_stage2_total_hits': sum(len(v['content_hits']) + len(v['fieldname_hits'])
                                  for v in scan_stage2.values()),
    'scan_stage3_host_verify': '主持验封道，非本席执行——留位：主持以独立脚本对 holdout19/inputs/ 全部输入卡复扫，零命中方许封存日志落「验封通过」',
    'markers_source': '标记集逐字复制 runs/round42/PREREG.md §5（LEVEL1/LEVEL2/FIELD_BLACKLIST，见脚本头注释）',
    'gold_sha256': sha_lib, 'gold_sha256_sha256sum': sha_sum,
    'gold_sha256_double_read_match': sha_lib == sha_sum,
    'outputs_written': [f'holdout19/inputs/{c}.json' for c in ORDER] +
                       ['holdout19/test_gold.jsonl'],
}
with open(REPORT_PATH, 'w', encoding='utf-8') as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'OK': True, 'T': T, 'fallback_triggered': fallback_triggered,
                  'stage2_total_hits': report['scan_stage2_total_hits'],
                  'gold_sha256': sha_lib}, ensure_ascii=False))
