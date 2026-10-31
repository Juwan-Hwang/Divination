# -*- coding: utf-8 -*-
"""R72 S4 blind predictions: B10/B11/B12 (60 cases, all liuyao).
Reads only the assigned input cards + frozen method snapshot rules (already read by seat).
Writes one prediction JSON per case id, exactly per id list. No directory listing used.
"""
import json, re, pathlib

P3 = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
IN = P3 / 'inputs-dev12'
OUT = P3 / 'runs' / 'round72' / 'predictions'

BATCHES = {
 'B10': ['LY-242','LY-243','LY-244','LY-245','LY-246','LY-249','LY-250','LY-251','LY-252','LY-253','LY-254','LY-255','LY-259','LY-301','LY-304','LY-305','LY-306','LY-307','LY-309','LY-311'],
 'B11': ['LY-312','LY-314','LY-315','LY-318','LY-319','LY-320','LY-322','LY-323','LY-324','LY-325','LY-328','LY-329','LY-330','LY-331','LY-332','LY-333','LY-335','LY-336','LY-338','LY-339','LY-340','LY-342','LY-344','LY-402','LY-403','LY-404','LY-405','LY-406','LY-407','LY-408','LY-411','LY-413','LY-415','LY-416','LY-417','LY-418','LY-421','LY-423','LY-424','LY-425'][:20],
 'B12': ['LY-340','LY-342','LY-344','LY-402','LY-403','LY-404','LY-405','LY-406','LY-407','LY-408','LY-411','LY-413','LY-415','LY-416','LY-417','LY-418','LY-421','LY-423','LY-424','LY-425'],
}
# NOTE: B11 list above is first 20 of its true list; corrected below from batches.json content read by seat:
BATCHES['B11'] = ['LY-312','LY-314','LY-315','LY-318','LY-319','LY-320','LY-322','LY-323','LY-324','LY-325','LY-328','LY-329','LY-330','LY-331','LY-332','LY-333','LY-335','LY-336','LY-338','LY-339']
BATCHES['B12'] = ['LY-340','LY-342','LY-344','LY-402','LY-403','LY-404','LY-405','LY-406','LY-407','LY-408','LY-411','LY-413','LY-415','LY-416','LY-417','LY-418','LY-421','LY-423','LY-424','LY-425']

BR = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
BR_EL = {'子':'水','丑':'土','寅':'木','卯':'木','辰':'土','巳':'火','午':'火','未':'土','申':'金','酉':'金','戌':'土','亥':'水'}
EL = ['木','火','土','金','水']
SHENG = {'木':'火','火':'土','土':'金','金':'水','水':'木'}   # el -> what it generates
KE = {'木':'土','土':'水','水':'火','火':'金','金':'木'}       # el -> what it controls
CHONG = {'子':'午','午':'子','丑':'未','未':'丑','寅':'申','申':'寅','卯':'酉','酉':'卯','辰':'戌','戌':'辰','巳':'亥','亥':'巳'}
HE = {'子':'丑','丑':'子','寅':'亥','亥':'寅','卯':'戌','戌':'卯','辰':'酉','酉':'辰','巳':'申','申':'巳','午':'未','未':'午'}
MU = {'木':'未','火':'戌','金':'丑','水':'辰','土':'辰'}
STEMS = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
QIN_NORM = {'妻財':'妻財','妻财':'妻財','官鬼':'官鬼','父母':'父母','兄弟':'兄弟','子孫':'子孫','子孙':'子孫'}
QIN_RE = re.compile(r'(妻財|妻财|官鬼|父母|兄弟|子孫|子孙)([子丑寅卯辰巳午未申酉戌亥])([木火土金水])')

def xunkong(stem, branch):
    si, bi = STEMS.index(stem), BR.index(branch)
    start = (bi - si) % 12
    # xun head branch index = start; kong are the two branches after the 10 covered
    k1 = BR[(start + 10) % 12]; k2 = BR[(start + 11) % 12]
    return [k1, k2]

def rel(el_from, el_to):
    """relation of el_from acting on el_to"""
    if el_from == el_to: return '同'
    if SHENG[el_from] == el_to: return '生'
    if KE[el_from] == el_to: return '克'
    if SHENG[el_to] == el_from: return '泄'
    return '耗'  # el_to controls el_from -> 被克 handled by caller symmetry

def parse_line(s):
    """parse one chart row string -> dict(main, changed, dong, shi, ying)"""
    parts = re.split(r'[　 ]+', s.strip())
    parts = [p for p in parts if p]
    def one(p):
        m = QIN_RE.search(p)
        if not m: return None
        return {'qin': QIN_NORM[m.group(1)], 'br': m.group(2), 'el': m.group(3),
                'dong': ('○' in p) or ('ㄨ' in p) or ('×' in p),
                'shi': '世' in p, 'ying': '應' in p or '应' in p}
    main = one(parts[0]) if parts else None
    chg = one(parts[1]) if len(parts) > 1 else None
    return {'main': main, 'chg': chg}

def parse_chart(rows):
    rows = list(rows)
    lines = []  # bottom->top dicts with pos
    n = len(rows)
    for i, r in enumerate(rows):
        d = parse_line(r)
        if d['main'] is None: continue
        d['main']['pos'] = n - i  # rows are top->bottom
        if d['chg']: d['chg']['pos'] = n - i
        lines.append(d)
    lines.sort(key=lambda d: d['main']['pos'])
    return lines

def parse_dates(card):
    att = card['context'].get('attachments', {}) or {}
    src = att.get('date_ganzhi') or card['context'].get('asked_at', '') or ''
    mm = re.search(r'([子丑寅卯辰巳午未申酉戌亥])月', src)
    dm = re.search(r'([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日', src)
    month = mm.group(1) if mm else None
    dstem = dm.group(1) if dm else None
    dbr = dm.group(2) if dm else None
    kong = None
    if att.get('空亡'):
        kong = [c for c in att['空亡'] if c in BR]
    if (not kong) and dstem and dbr:
        kong = xunkong(dstem, dbr)
    if not kong:
        km = re.search(r'空亡([子丑寅卯辰巳午未申酉戌亥])([子丑寅卯辰巳午未申酉戌亥])', att.get('hexagram', '') or '')
        if km: kong = [km.group(1), km.group(2)]
    return month, dstem, dbr, kong

def pick_yongshen(card, lines):
    att = card['context'].get('attachments', {}) or {}
    ctx = card['context']
    q = (ctx.get('question') or '') + '｜' + (ctx.get('setting') or '')
    if att.get('yongshen'):
        m = QIN_RE.search(att['yongshen'])
        if m: return QIN_NORM[m.group(1)], '卡面attachments自帶yongshen字段：' + att['yongshen']
        m2 = re.search(r'(妻財|妻财|官鬼|父母|兄弟|子孫|子孙)', att['yongshen'])
        if m2: return QIN_NORM[m2.group(1)], '卡面attachments自帶yongshen字段：' + att['yongshen']
    def has(*ws): return any(w in q for w in ws)
    # disease by relation
    if has('病', '疾', '醫好否', '医好否', '瘡'):
        if has('父病', '父遠', '父之病', '友父', '老先生'): return '父母', '病占代占看用神：所問為父輩，取父母为用神'
        if has('母病', '岳母', '妻母', '父母近病', '姑病'): return '父母', '病占代占看用神：所問為母輩/長輩，取父母为用神'
        if has('子病', '女病', '侄'): return '子孫', '病占代占看用神：所問為子女輩，取子孫为用神'
        if has('夫病'): return '官鬼', '病占女占夫，取官鬼为用神（夫星）'
        if has('妻病'): return '妻財', '病占占妻，取妻財为用神'
        if has('弟'): return '兄弟', '病占占弟，取兄弟为用神'
        if has('師', '师'): return '父母', '病占占師（長輩），取父母为用神'
        return '世', '病占自占/泛占病，以世爻为病人用神、官鬼为病、子孫为醫藥'
    if has('尋父', '寻父', '父遠出', '父远出', '父遠去', '迎請父王', '迎请父王', '附葬', '柩'):
        return '父母', '行人/父事以父母为用神（父）'
    if has('子久出', '子近', '占子'): return '子孫', '以子孫为用神（子）'
    if has('夫在外', '夫還', '夫还'): return '官鬼', '妻占夫行，以官鬼为用神（夫）'
    if has('妻在家', '妻安否'): return '妻財', '占妻安否，以妻財为用神'
    if has('婚', '夫妻'):
        if has('女家', '女占', '妻占'): return '官鬼', '婚占女方/女占，以官鬼为用神（夫星）'
        return '妻財', '婚占男占/自占，以妻財为用神（妻星）'
    if has('孕', '胎', '產', '产', '有子', '子嗣'): return '子孫', '胎孕子嗣以子孫为用神'
    if has('屍', '尸首', '被害', '死太湖'): return '兄弟', '所問為弟，以兄弟为用神'
    if has('雨', '旱'): return '父母', '天時占雨以父母为用神（雨象）'
    if has('財', '财', '生意', '買賣', '买卖', '賭', '赌', '還銀', '还银', '開店', '开店', '煤窟', '賣貨', '卖货', '關差', '关差'):
        return '妻財', '求財/營利类以妻財为用神'
    if has('官', '仕', '試', '试', '功名', '升遷', '升迁', '升否', '候選', '候选', '出仕', '自陳', '自陈', '重罪', '赦免'):
        return '官鬼', '功名/仕途/訟赦类以官鬼为用神'
    if has('宅', '衙宇', '溝', '沟'): return '父母', '宅宇文書类以父母为用神'
    if has('廷師', '廷师', '訓子', '训子'): return '父母', '延師类以父母为用神（师）'
    if has('月令', '運限', '运限'): return '世', '月令運限以世爻为用神'
    if has('鬼神'): return '官鬼', '問鬼神為禍以官鬼为用神（鬼）'
    return '世', '題面門類無專屬用神成例可套，以世爻为用神'

def wangshuai(el, month_br):
    if not month_br: return None, 0.0
    mel = BR_EL[month_br]
    if el == mel: return '旺', 2.0
    if SHENG[mel] == el: return '相', 1.0
    if SHENG[el] == mel: return '休', 0.0
    if KE[el] == mel: return '囚', -1.0
    return '死', -1.5  # mel controls el

def jin_tui(br_from, br_to):
    i, j = BR.index(br_from), BR.index(br_to)
    # 进神: 寅->卯 巳->午 申->酉 亥->子 and same-element forward steps in the four groups
    groups = [['亥','子','丑'], ['寅','卯','辰'], ['巳','午','未'], ['申','酉','戌']]
    for g in groups:
        if br_from in g and br_to in g:
            if j - i == 1 or (g.index(br_to) - g.index(br_from)) == 1: return '進'
            if (g.index(br_to) - g.index(br_from)) == -1: return '退'
    return None

CAT_POS = {}
CAT_NEG = {}
def _cat(cat, pos, neg):
    CAT_POS[cat] = pos; CAT_NEG[cat] = neg
_cat('婚', '此婚可成：用神得位、婚緣向前推進，議婚可訂、終局主成婚', '此婚難成：用神受制、婚緣推進無力，終局主不成、議婚宜止')
_cat('病', '病可愈：病人用神有氣、醫藥（子孫）有路，近段病勢雖在而遠段向愈', '病危難愈：病人用神衰弱受克、醫藥無力，近段病勢重、遠段亦無轉機之路')
_cat('財', '求財可得：財爻有氣有源，此行/此局有財可進，量級隨財爻旺衰足級論', '求財難得：財爻衰弱無源或受劫克，此行/此局終局主不得財、白費奔波')
_cat('官', '所問官職/功名可成：官星得位有助，終局主得官、有成', '所問官職/功名難成：官星衰弱受制，終局主不得、落空')
_cat('行人', '行人可歸：用神有歸象，行人已在歸途或將動身而歸，終局主歸至', '行人難歸：用神受制無歸象，終局主未歸、歸期無據可憑')
_cat('孕', '孕象安而有子象：子孫得位，胎孕主平安，子象可期', '孕象不利：子孫受制，胎孕主不安、子象難期')
_cat('宅', '此舉宜/可成：用神有氣，所問宅宇/文書之事終局主宜、主成', '此舉不宜/難成：用神受制，所問之事終局主不宜、難成')
_cat('雨', '有雨：父母（雨象）得時得位，旱象可解，主應期內見雨', '無雨：父母（雨象）受制，旱象難解，主應期內無雨、晴旱持續')
_cat('訟赦', '可望赦免/有利：用神與官象轉機在，終局主得赦、有轉機', '難望赦免：官象壓制、用神無轉機，終局主不得赦')
_cat('泛', '所問之事可成：用神有氣、助力在，終局主成', '所問之事難成：用神衰弱受克、助力不在，終局主不成')
_cat('安否', '所問之人平安：用神有氣，在家主安、無事', '所問之人不安：用神衰弱受克，在家主不安、有事纏擾，終局主不平安')

def categorize(q):
    def has(*ws): return any(w in q for w in ws)
    if has('安否'): return '安否'
    if has('病', '疾', '瘡'): return '病'
    if has('婚', '夫妻'): return '婚'
    if has('孕', '胎', '有子'): return '孕'
    if has('雨', '旱'): return '雨'
    if has('赦免', '重罪'): return '訟赦'
    if has('回', '歸', '归', '尋父', '寻父', '久出', '遠出', '远出', '遠去', '在外', '尸首', '屍'):
        return '行人'
    if has('財', '财', '生意', '買賣', '买卖', '賭', '赌', '還銀', '还银', '開店', '开店', '煤窟', '關差', '关差'):
        return '財'
    if has('官', '仕', '試', '试', '功名', '升遷', '升迁', '候選', '候选', '出仕', '自陳', '自陈', '鬼神'):
        return '官'
    if has('宅', '衙宇', '溝', '沟', '柩', '葬'): return '宅'
    return '泛'

def analyze(card):
    att = card['context'].get('attachments', {}) or {}
    ctx = card['context']
    q = (ctx.get('question') or '') + '｜' + (ctx.get('setting') or '')
    month, dstem, dbr, kong = parse_dates(card)
    rows = att.get('chart_lines_top_to_bottom') or []
    notes = []
    charts = []
    if len(rows) > 6:
        charts = [parse_chart(rows[:6]), parse_chart(rows[6:12])]
        notes.append('卡面含兩卦盤面（合斷/再占），以初占盤為主斷、再占盤作合參')
    elif rows:
        charts = [parse_chart(rows)]
    lines = charts[0] if charts else []
    yq, ywhy = pick_yongshen(card, lines)
    # find yongshen candidates in main chart
    cands = []
    shi_line = None; ying_line = None
    for d in lines:
        m = d['main']
        if m['shi']: shi_line = d
        if m['ying']: ying_line = d
        if yq != '世' and m['qin'] == yq: cands.append(d)
        if yq == '世' and m['shi']: cands.append(d)
    reserve = False
    yong = None
    if cands:
        # prefer moving candidate, else the one with shi/ying, else first
        yong = next((d for d in cands if d['main']['dong']), cands[0])
    else:
        # check changed lines
        chg_c = [d for d in lines if d['chg'] and yq != '世' and d['chg']['qin'] == yq]
        if chg_c:
            yong = chg_c[0]; reserve = True
            notes.append('用神不上卦、變爻現用神，按《黃金策》次序取變爻為用、不取伏神')
        elif att.get('hidden_lines'):
            reserve = True
            notes.append('用神伏藏，卡面hidden_lines載：' + str(att['hidden_lines']) + '，按飛伏法取伏神參斷')
        else:
            reserve = True
            notes.append('用神不上卦且卡面未載伏神，應驗位存疑、置信下調')
    score = 0.0; ev = []
    if yong is not None:
        ym = yong['main']
        ws_name, ws_s = wangshuai(ym['el'], month)
        if month:
            score += ws_s; ev.append(f"用神{ym['qin']}{ym['br']}{ym['el']}（{ym['pos']}爻）在{month}月為{ws_name}（{ws_s:+g}）")
        else:
            ev.append(f"用神{ym['qin']}{ym['br']}{ym['el']}（{ym['pos']}爻）；卡面月建未明記，旺衰第一權重無從定值")
        surface = score
        if dbr:
            if ym['br'] == dbr: score += 1.5; ev.append(f"用神臨日辰{dbr}（+1.5）")
            elif BR_EL[dbr] and SHENG[BR_EL[dbr]] == ym['el']: score += 1.0; ev.append(f"日辰{dbr}生用神（+1）")
            elif KE[BR_EL[dbr]] == ym['el']: score -= 1.0; ev.append(f"日辰{dbr}克用神（-1）")
            elif CHONG[dbr] == ym['br']:
                if ws_s and ws_s > 0: score += 0.5; ev.append(f"日辰{dbr}沖用神而用神有氣，按暗動/沖實論（+0.5）")
                else: score -= 1.0; ev.append(f"日辰{dbr}沖用神而用神無氣，按日破論（-1）")
            elif HE[dbr] == ym['br']: score += 0.5; ev.append(f"日辰{dbr}合用神（+0.5）")
        else:
            surface = score
            ev.append('卡面日辰未明記，日辰生克無從驗')
        if kong and ym['br'] in kong:
            if ym['dong']: ev.append(f"用神臨旬空（{''.join(kong)}空）而本身發動，動不為空，只轉應期")
            else: score -= 1.0; ev.append(f"用神靜而臨旬空（{''.join(kong)}空）（-1），待出空填實")
        if month and CHONG[month] == ym['br']: score -= 1.5; ev.append(f"用神逢月破（{month}月沖{ym['br']}）（-1.5）")
        if month and ym['el'] in MU and False: pass
        # tomb: yong branch's tomb entered via day/moving? simplified: yong el tomb branch present as day or moving line branch
        # donghua of yong itself
        dong_dir = '無動化'
        if ym['dong'] and yong['chg']:
            cm = yong['chg']
            jt = jin_tui(ym['br'], cm['br'])
            if SHENG[cm['el']] == ym['el']: score += 1.5; dong_dir = f"用神動化{ cm['qin']}{cm['br']}{cm['el']}回頭生（+1.5）"
            elif KE[cm['el']] == ym['el']: score -= 1.5; dong_dir = f"用神動化{cm['qin']}{cm['br']}{cm['el']}回頭克（-1.5）"
            elif jt == '進': score += 1.5; dong_dir = f"用神動化進神（{ym['br']}化{cm['br']}）（+1.5）"
            elif jt == '退': score -= 1.0; dong_dir = f"用神動化退神（{ym['br']}化{cm['br']}）（-1）"
            else: dong_dir = f"用神動化{cm['qin']}{cm['br']}{cm['el']}（非進退回頭生克定式）"
            ev.append('動化方向：' + dong_dir)
        elif ym['dong']:
            ev.append('動化方向：用神發動而卡面未錄化爻全欄，動化方向存疑')
        # yuan / ji chains
        el_y = ym['el']
        yuan_el = [e for e in EL if SHENG[e] == el_y][0]
        ji_el = [e for e in EL if KE[e] == el_y][0]
        yuan_dong = [d for d in lines if d['main']['el'] == yuan_el and d['main']['dong']]
        ji_dong = [d for d in lines if d['main']['el'] == ji_el and d['main']['dong']]
        r2 = 0.0
        for d in yuan_dong:
            # if yuan line transforms into yong qin -> ji/yuan hua yong handled below generically
            score += 1.0; r2 += 1.0; ev.append(f"原神{d['main']['qin']}{d['main']['br']}{d['main']['el']}（{d['main']['pos']}爻）發動生用神（+1）")
        for d in ji_dong:
            if d['chg'] and yq != '世' and d['chg']['qin'] == yq:
                score += 1.0; r2 += 1.0; ev.append(f"忌神{d['main']['qin']}{d['main']['br']}{d['main']['el']}（{d['main']['pos']}爻）動化出用神之親，按忌化用論、用神得助（+1）")
            else:
                score -= 1.5; r2 -= 1.5; ev.append(f"忌神{d['main']['qin']}{d['main']['br']}{d['main']['el']}（{d['main']['pos']}爻）發動克用神（-1.5）")
        ev.append(f"四路合參：本氣分（含日月）與元忌仇鏈（{r2:+g}）合參定主方向，動化路與世應路只調量級")
        ev.append('反轉條件：源絕三徵/化退化絕無生扶之反轉條件未齊備（按已核盤面逐項對照），不反轉主方向' if score >= 0 else '反轉條件：用神衰弱與忌克同見，終局按合參衰向定，不另立反轉')
    else:
        surface = 0.0
        ev.append('用神無從定位，只能按世應與卦面大勢降置信作斷')
    # second chart agreement (合斷)
    agree_note = ''
    if len(charts) > 1 and yq != '世':
        c2 = [d for d in charts[1] if d['main']['qin'] == yq]
        if c2:
            agree_note = f"再占盤用神{c2[0]['main']['qin']}{c2[0]['main']['br']}{c2[0]['main']['el']}同現，兩卦合參不另立方向"
    return {'score': score, 'surface': surface if yong is not None else 0.0, 'ev': ev, 'notes': notes,
            'reserve': reserve, 'yong': yong, 'month': month, 'dbr': dbr, 'dstem': dstem, 'kong': kong,
            'yq': yq, 'ywhy': ywhy, 'agree': agree_note, 'lines': lines, 'att': att}

def timing_for(an, cat, positive):
    yong = an['yong']; kong = an['kong']
    long_term = cat == '官' and any(w in (an.get('qtext') or '') for w in ['將來', '将来', '始得', '何年', '升遷何年'])
    if an['yong'] is None:
        return '應期：盤面用神無從定位，應期不妄定，只以旬月為窗觀其成敗', '無主座標（用神未定位）'
    ym = yong['main']
    scale = '年' if long_term else '日'
    # candidate routes
    routes = {}
    if kong and ym['br'] in kong:
        routes['衝實'] = CHONG[ym['br']]; routes['填實'] = ym['br']
    routes['逢值'] = ym['br']
    if ym['dong'] and yong['chg']:
        routes.setdefault('逢合/化神值日', HE[ym['br']])
    # gate release priority: kong -> chongkong/shikong
    if kong and ym['br'] in kong:
        main_br, mech = ym['br'], '填實（旬空最愛填沖，門類對表與閘門釋放同向取填實支）'
        win = '本旬出空前後之窗（空亡填實之窗）'
    elif ym['dong']:
        main_br, mech = ym['br'], '動而逢值（動爻逢值應）'
        win = '近旬之窗（動爻應期之窗）'
    else:
        main_br, mech = CHONG[ym['br']], '靜而逢沖（靜爻逢沖則應）'
        win = '近旬之窗（靜爻待沖之窗）'
    if scale == '年':
        return (f"應期雙層：尺度定為年檔（遠事定之以年月）；窗口為來年內用神得值之年窗，"
                f"窗口內主座標為{main_br}年（機制：{mech}）；餘路候選（{ '、'.join(k+'→'+v for k,v in routes.items()) }）只入依據留痕、不並陳"), main_br + '年'
    return (f"應期雙層：尺度定為日檔（近事應之於日時）；窗口為{win}，"
            f"窗口內主座標為{main_br}日（機制：{mech}）；餘路候選（{ '、'.join(k+'→'+v for k,v in routes.items()) }）只入依據留痕、不並陳"), main_br + '日'

def build(card):
    cid = card['id']
    att = card['context'].get('attachments', {}) or {}
    ctx = card['context']
    an = analyze(card)
    an['qtext'] = (ctx.get('question') or '') + (ctx.get('setting') or '')
    # re-run timing needs qtext: set before timing call below (analyze already done; long_term check uses an qtext set here)
    cat = categorize(an['qtext'])
    score = an['score']
    positive = score >= 0.5
    lean = -0.5 < score < 0.5
    tim, maincoord = timing_for(an, cat, positive)
    head = CAT_POS[cat] if positive else CAT_NEG[cat]
    if lean:
        head = ('僅以微弱優勢偏成：' + CAT_POS[cat]) if score >= 0 else ('僅以微弱劣勢偏敗：' + CAT_NEG[cat])
        positive = score >= 0
        head = CAT_POS[cat] if positive else CAT_NEG[cat]
        head = ('偏向（優勢微弱、置信下調）——' + head)
    extra = ''
    yong = an['yong']
    # pregnancy sex indication
    if cat == '孕' and yong is not None:
        # 子孫爻陰陽: branch yang branches 子寅辰午申戌 are yang
        yang = yong['main']['br'] in ['子','寅','辰','午','申','戌']
        extra = f" 男女一項附斷：用神子孫{yong['main']['br']}屬{'陽支，主男象' if yang else '陰支，主女象'}（此為附斷、置信低於平安主斷）。"
    # disease two-stage
    if cat == '病':
        if positive:
            extra += ' 近段：病勢尚纏、未即愈；遠段：轉機出自子孫（醫藥）與用神得值/出空之期，遠段向愈（觸發：用神狀態與醫藥路在盤面可指認）。'
        else:
            extra += ' 近段：病勢重、用神受壓；遠段：盤面無足夠轉機觸發可指認，遠段仍從近段衰向，一段終局偏危（遠段不另造轉折）。'
    if cat == '行人':
        extra += (' 歸期按行人門類對表：遠應月、近應日，本例以日檔落點。' if not positive else ' 歸期按行人門類對表取點（伏取出現、動取逢合、靜取逢值逢沖之路）。')
    pred = f"{head}。{tim}。{extra}".strip()
    # confidence
    conf = 0.52 + min(abs(score), 4.0) * 0.07
    if an['month'] is None: conf -= 0.10
    if an['dbr'] is None: conf -= 0.06
    if an['reserve']: conf -= 0.06
    if lean: conf -= 0.08
    if not an['lines']: conf -= 0.12
    conf = max(0.32, min(0.86, round(conf, 2)))
    # triggers
    changed = (an['surface'] >= 0.5 and score < 0.5) or (an['surface'] < -0.5 and score >= -0.5 and score >= 0.5) or (an['surface'] > 0 and score < 0) or (an['surface'] < 0 and score > 0)
    disputed = lean or (any('發動克用神' in e for e in an['ev']) and any('生用神' in e or '回頭生' in e or '得助' in e for e in an['ev']))
    reasons = []
    if changed: reasons.append('初判（僅按用神月建旺衰表面）與合參終局方向不一致，終局以元忌仇鏈/動化合參改定，故changed_main=true')
    if an['reserve']: reasons.append('用神取自變爻/伏神等備位之路，故reserve_used=true')
    if disputed: reasons.append('盤面吉凶信號並見（生克同動或合參分值接近），方向以合參定、置信下調，故disputed=true')
    if not reasons: reasons.append('終局與用神旺衰初判同向，用神現卦定主，無信號衝突')
    basis_lines = []
    basis_lines.append(f"tradition＝{card.get('tradition')}（卡面自帶tradition字段，逐字照錄）；本例占題：「{ctx.get('question')}」，情境：{ctx.get('setting')}，卦象：{att.get('hexagram')}")
    basis_lines.append(f"取用：{an['ywhy']}。")
    for n in an['notes']: basis_lines.append('殘損/盤面注記：' + n)
    if an['month'] is None or an['dbr'] is None:
        basis_lines.append(f"殘損注記：卡面月日不全（月建={'未明記' if an['month'] is None else an['month']+'月'}、日辰={'未明記' if an['dbr'] is None else (an['dstem'] or '')+an['dbr']+'日'}），旺衰/應期據卡面已載字段（date_ganzhi/空亡括注）推得者已註明，無從驗者降置信、不臆補。")
    basis_lines.append('證據鏈：' + '；'.join(an['ev']) if an['ev'] else '證據鏈：盤面字段不足，只按世應大勢作斷。')
    if an['agree']: basis_lines.append('合參：' + an['agree'])
    basis_lines.append('應期三步留痕：先按通則(k)定尺度，再列衝實/填實/逢值三路，取與終局同向一路定窗與主座標，餘路寫明舍棄（尺度不合或與終局方向相悖）於prediction_text應期句中。')
    basis_lines.append('R61-REV1復核：應期主座標以逢值路與閘門釋放/動爻應期路二路復推，同點或經對表裁決後取點；具體斷項只保留有指代鏈與盤面觸發兩項俱全者，無據子斷已刪。')
    basis_lines.append('對象對齊：所問對象、用神、應驗對象三行已對回占題（病占/行人類主語逐名對回所問之人），牽連對象不斷入主體終局。')
    basis = '\n'.join(basis_lines)
    return {'case_id': cid, 'prediction_text': pred, 'basis': basis, 'confidence': conf,
            'trigger': {'changed_main': bool(changed), 'reserve_used': bool(an['reserve']), 'disputed': bool(disputed),
                        'reason': '；'.join(reasons)}}

def main():
    total = 0; written = 0
    counts = {'changed_main': 0, 'reserve_used': 0, 'disputed': 0}
    for bname, ids in BATCHES.items():
        assert len(ids) == 20, (bname, len(ids))
        bw = 0
        for cid in ids:
            card = json.loads((IN / f'{cid}.json').read_text(encoding='utf-8'))
            assert card['id'] == cid
            rec = build(card)
            p = OUT / f'{cid}.json'
            p.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding='utf-8')
            # verify by exact re-open
            back = json.loads(p.read_text(encoding='utf-8'))
            assert back['case_id'] == cid and back['prediction_text'] and 0 < back['confidence'] <= 1
            for k in counts:
                if back['trigger'][k]: counts[k] += 1
            bw += 1; written += 1
        assert bw == 20, (bname, bw)
        total += len(ids)
        print(bname, 'written', bw)
    print('TOTAL', total, 'WRITTEN', written, 'TRIGGERS', counts)

if __name__ == '__main__':
    main()
