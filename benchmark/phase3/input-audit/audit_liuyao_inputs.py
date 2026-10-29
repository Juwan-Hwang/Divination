# -*- coding: utf-8 -*-
"""
audit_liuyao_inputs.py — 六爻输入机械一致性普查（input-audit 试点，规则照 PREREG.md §2 冻结清单）

范围：inputs-dev10 中 (c) 子集 246 例（host-meta tradition=liuyao ∧ 见于 master-baseline-dev8）。
两种卦面格式：
  A（增删卜易系）：「六亲+地支+五行+爻符」双栏（本卦/变卦），动爻以 ○/ㄨ 代爻符。
  B（易隐系）：「六亲+纳甲天干+地支+五行」单栏，动以（动）标，卦名见 hexagram 文本——
     以卦名定爻符（卦名表引 tools/cast_iching.py 的 HEXAGRAM_ORDER 为在仓权威表），
     干支/六亲/世应/化出逐项与推得对核（同一 R1–R6 规则的格式 B 实现）。
产出：census.json（逐例逐条标记）＋ CENSUS.md（汇总）。只产标记、不产结论。
运行：python3 audit_liuyao_inputs.py（cwd=benchmark/phase3）
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

P3 = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
ROOT = P3.parent.parent

# ---------- 卦名表（引在仓 tools/cast_iching.py） ----------
sys.path.insert(0, str(ROOT / 'tools'))
from cast_iching import HEXAGRAM_ORDER, TRIGRAMS as _TRI_BY_BITS  # noqa: E402

_S2T_TRI = {'兑': '兌', '离': '離'}


def _tri_trad(n):
    return _S2T_TRI.get(n, n)


TRI_BITS = {_tri_trad(name): bits for bits, name in _TRI_BY_BITS.items()}
BITS_TRI = {v: k for k, v in TRI_BITS.items()}
HEXAGRAM_ORDER_T = [(name, _tri_trad(up), _tri_trad(low)) for name, up, low in HEXAGRAM_ORDER]
HEX_BY_UD = {(up, low): name for name, up, low in HEXAGRAM_ORDER_T}  # (上,下)->卦名(简)
TRI_ELEM_CHAR = {'乾': '天', '坤': '地', '震': '雷', '巽': '风', '坎': '水',
                 '離': '火', '艮': '山', '兌': '泽'}
T2S = str.maketrans({'歸': '归', '無': '无', '訟': '讼', '節': '节', '漸': '渐', '頤': '颐',
                     '觀': '观', '豐': '丰', '剝': '剥', '復': '复', '隨': '随', '蠱': '蛊',
                     '臨': '临', '賁': '贲', '謙': '谦', '壯': '壮', '晉': '晋', '濟': '济',
                     '恆': '恒', '過': '过', '離': '离', '兌': '兑', '為': '为', '風': '风',
                     '澤': '泽', '遯': '遁', '孫': '孙', '財': '财', '應': '应', '動': '动'})


def simp(s):
    return (s or '').translate(T2S)


def full_name(name, up, low):
    if up == low:
        return f"{up}为{TRI_ELEM_CHAR[up]}"
    return f"{TRI_ELEM_CHAR[up]}{TRI_ELEM_CHAR[low]}{name}"


FULL2UD = {}
for name, up, low in HEXAGRAM_ORDER_T:
    FULL2UD[full_name(name, up, low)] = (up, low)
    FULL2UD[name] = (up, low)  # 短名兜底（有歧义时靠出现顺序，见 parse_hexagram_text）

# ---------- 基础表 ----------
NAJIA = {
    '乾': (('子', '寅', '辰'), ('午', '申', '戌')),
    '坤': (('未', '巳', '卯'), ('丑', '亥', '酉')),
    '震': (('子', '寅', '辰'), ('午', '申', '戌')),
    '巽': (('丑', '亥', '酉'), ('未', '巳', '卯')),
    '坎': (('寅', '辰', '午'), ('申', '戌', '子')),
    '離': (('卯', '丑', '亥'), ('酉', '未', '巳')),
    '艮': (('辰', '午', '申'), ('戌', '子', '寅')),
    '兌': (('巳', '卯', '丑'), ('亥', '酉', '未')),
}
NAJIA_STEM = {'乾': ('甲', '壬'), '坤': ('乙', '癸'), '震': ('庚', '庚'), '巽': ('辛', '辛'),
              '坎': ('戊', '戊'), '離': ('己', '己'), '艮': ('丙', '丙'), '兌': ('丁', '丁')}
BRANCH_ELEM = {'子': '水', '丑': '土', '寅': '木', '卯': '木', '辰': '土', '巳': '火',
               '午': '火', '未': '土', '申': '金', '酉': '金', '戌': '土', '亥': '水'}
PALACE_ELEM = {'乾': '金', '坤': '土', '震': '木', '巽': '木',
               '坎': '水', '離': '火', '艮': '土', '兌': '金'}
STAGES = [('本宮', 6, frozenset()), ('一世', 1, frozenset({1})), ('二世', 2, frozenset({1, 2})),
          ('三世', 3, frozenset({1, 2, 3})), ('四世', 4, frozenset({1, 2, 3, 4})),
          ('五世', 5, frozenset({1, 2, 3, 4, 5})), ('游魂', 4, frozenset({1, 2, 3, 5})),
          ('歸魂', 3, frozenset({5}))]


def build_palace_map():
    m = {}
    for pal, tri in TRI_BITS.items():
        pure = tri + tri
        for name, shi, flips in STAGES:
            bits = tuple(b ^ (1 if (i + 1) in flips else 0) for i, b in enumerate(pure))
            assert bits not in m
            m[bits] = (pal, shi)
    assert len(m) == 64
    return m


PALACE_MAP = build_palace_map()
GEN = {'金': '水', '水': '木', '木': '火', '火': '土', '土': '金'}
CTL = {'金': '木', '木': '土', '土': '水', '水': '火', '火': '金'}


def qin_relation(pal_elem, line_elem):
    if line_elem == pal_elem:
        return '兄弟'
    if GEN[pal_elem] == line_elem:
        return '子孫'
    if GEN[line_elem] == pal_elem:
        return '父母'
    if CTL[pal_elem] == line_elem:
        return '妻財'
    return '官鬼'


def derive_chart(bits):
    lower = BITS_TRI[bits[0:3]]
    upper = BITS_TRI[bits[3:6]]
    pal, shi = PALACE_MAP[bits]
    pe = PALACE_ELEM[pal]
    lines = {}
    for pos in range(1, 7):
        tri = lower if pos <= 3 else upper
        seq = NAJIA[tri][0] if pos <= 3 else NAJIA[tri][1]
        stem = NAJIA_STEM[tri][0] if pos <= 3 else NAJIA_STEM[tri][1]
        br = seq[(pos - 1) % 3]
        el = BRANCH_ELEM[br]
        lines[pos] = {'branch': br, 'elem': el, 'qin': qin_relation(pe, el), 'stem': stem}
    return {'lower': lower, 'upper': upper, 'palace': pal, 'shi': shi,
            'ying': shi + 3 if shi <= 3 else shi - 3, 'lines': lines}


# ---------- 格式 A ----------
SEG_RE = re.compile(
    r'^(父母|兄弟|子孫|子孙|妻財|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([金木水火土])([⚊⚋○ㄨ×])(世|應|应)?$')
PAREN_RE = re.compile(r'（[^）]*）|\([^)]*\)')


def norm_qin(q):
    return q.replace('孙', '孫').replace('财', '財')


def parse_segment_a(seg):
    m = SEG_RE.match(seg.strip())
    if not m:
        return None
    qin, br, el, sym, mark = m.groups()
    return {'qin': norm_qin(qin), 'branch': br, 'elem': el, 'sym': sym,
            'mark': mark.replace('应', '應') if mark else None}


def parse_chart_line_a(raw):
    paren = bool(PAREN_RE.search(raw))
    cleaned = PAREN_RE.sub('', raw)
    parts = [p for p in re.split(r'[　 ]+', cleaned) if p]
    if len(parts) == 1:
        left = parse_segment_a(parts[0])
        return {'left': left, 'right': None, 'paren': paren} if left else None
    if len(parts) == 2:
        left, right = parse_segment_a(parts[0]), parse_segment_a(parts[1])
        if left and right:
            return {'left': left, 'right': right, 'paren': paren}
    return None


def sym_bit(sym):
    return 1 if sym in ('⚊', '○') else 0


def sym_moving(sym):
    return sym in ('○', 'ㄨ', '×')


def shi_ying_flags(marks_shi, marks_ying, base, prefix=''):
    flags = []
    if marks_shi and marks_shi != [base['shi']]:
        flags.append(('R5', 'hard', f"{prefix}世标记位于 {marks_shi}，推得世位 {base['shi']}"))
    if marks_ying and marks_ying != [base['ying']]:
        flags.append(('R5', 'hard', f"{prefix}應标记位于 {marks_ying}，推得應位 {base['ying']}"))
    if not marks_shi and not marks_ying:
        flags.append(('R5', 'soft', f"{prefix}世應俱未标"))
    elif not marks_shi:
        flags.append(('R5', 'soft', f"{prefix}世未标"))
    elif not marks_ying:
        flags.append(('R5', 'soft', f"{prefix}應未标"))
    return flags


def audit_group_a(lines_td):
    flags = []
    lines_bu = list(reversed(lines_td))
    bits = tuple(sym_bit(p['left']['sym']) for p in lines_bu)
    moving = {i + 1 for i, p in enumerate(lines_bu) if sym_moving(p['left']['sym'])}
    base = derive_chart(bits)
    changed_bits = tuple(b ^ (1 if (i + 1) in moving else 0) for i, b in enumerate(bits))
    changed = derive_chart(changed_bits)
    pal_elem = PALACE_ELEM[base['palace']]
    for pos in range(1, 7):
        p = lines_bu[pos - 1]
        left = p['left']
        exp = base['lines'][pos]
        if left['branch'] != exp['branch'] or left['elem'] != exp['elem']:
            flags.append(('R2/R3', 'hard',
                          f"{pos}爻 本卦侧所书 {left['qin']}{left['branch']}{left['elem']}，推得 {exp['qin']}{exp['branch']}{exp['elem']}"))
        elif left['qin'] != exp['qin']:
            flags.append(('R4', 'hard',
                          f"{pos}爻 本卦侧六亲所书 {left['qin']}，推得 {exp['qin']}（{left['branch']}{left['elem']}）"))
        right = p['right']
        if right is not None:
            cexp = changed['lines'][pos]
            cqin = qin_relation(pal_elem, cexp['elem'])
            exp_sym = '⚊' if changed_bits[pos - 1] == 1 else '⚋'
            if right['sym'] != exp_sym:
                flags.append(('R1', 'hard', f"{pos}爻 变卦侧爻符所书 {right['sym']}，推得 {exp_sym}"))
            if right['branch'] != cexp['branch'] or right['elem'] != cexp['elem']:
                flags.append(('R2/R3', 'hard',
                              f"{pos}爻 变卦侧所书 {right['qin']}{right['branch']}{right['elem']}，推得 {cqin}{cexp['branch']}{cexp['elem']}"))
            elif right['qin'] != cqin:
                flags.append(('R4', 'hard',
                              f"{pos}爻 变卦侧六亲所书 {right['qin']}，推得 {cqin}（{cexp['branch']}{cexp['elem']}）"))
    if moving and all(p['right'] is None for p in lines_bu):
        flags.append(('R1', 'soft', '有动爻而卦面无变卦栏'))
    flags += shi_ying_flags(
        [i + 1 for i, p in enumerate(lines_bu) if p['left']['mark'] == '世'],
        [i + 1 for i, p in enumerate(lines_bu) if p['left']['mark'] == '應'], base)
    return flags


POS_WORD = {'初': 1, '二': 2, '三': 3, '四': 4, '五': 5, '上': 6}
MV_RE = re.compile(r'([初二三四五上])爻(父母|兄弟|子孫|子孙|妻財|妻财|官鬼)([子丑寅卯辰巳午未申酉戌亥])([金木水火土])([○ㄨ])')


def audit_r6_a(moving_text, lines_td):
    if len(lines_td) != 6:
        return None
    lines_bu = list(reversed(lines_td))
    chart_mv = {}
    for i, p in enumerate(lines_bu):
        if sym_moving(p['left']['sym']):
            chart_mv[i + 1] = (p['left']['qin'], p['left']['branch'])
    flags = []
    entries = {}
    for m in MV_RE.finditer(moving_text or ''):
        entries[POS_WORD[m.group(1)]] = (norm_qin(m.group(2)), m.group(3))
    if '無動爻' in (moving_text or '') and not entries:
        if chart_mv:
            flags.append(('R6', 'hard', f"moving_lines 称無動爻，卦面动爻位于 {sorted(chart_mv)}"))
        return flags
    if not entries:
        return None
    if set(entries) != set(chart_mv):
        flags.append(('R6', 'hard',
                      f"moving_lines 动位 {sorted(entries)} 与卦面动位 {sorted(chart_mv)} 不一致"))
    else:
        for pos in entries:
            if entries[pos] != chart_mv[pos]:
                flags.append(('R6', 'hard',
                              f"{pos}爻 moving_lines 作 {entries[pos]}，卦面作 {chart_mv[pos]}"))
    return flags


# ---------- 格式 B（易隐系） ----------
SEG_B_RE = re.compile(
    r'^(父母|兄弟|子孙|子孫|妻财|妻財|官鬼)([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])([金木水火土])'
    r'\s*(?:[（(](动)([？?])?[）)])?\s*(世|应|應)?\s*(?:[（(](动)([？?])?[）)])?$')
PALACE_PREFIX_RE = re.compile(r'([乾坤震巽坎离艮兑])宫')


def parse_segment_b(seg):
    m = SEG_B_RE.match(seg.strip().translate(T2S))
    if not m:
        return None
    qin, stem, br, el, mv1, unc1, mark, mv2, unc2 = m.groups()
    return {'qin': norm_qin(simp(qin)), 'stem': stem, 'branch': br, 'elem': el,
            'moving': bool(mv1 or mv2), 'uncertain': bool(unc1 or unc2),
            'mark': mark.replace('应', '應') if mark else None}


def parse_hexagram_text(text):
    """-> (base_ud, changed_ud, palace_prefix) ；ud=(上,下) 或 None"""
    t = simp(text)
    parts = t.split('之', 1)
    found = []
    for part in parts:
        hit = None
        for fname, ud in FULL2UD.items():
            if fname in part and len(fname) >= 2:
                if hit is None or len(fname) > len(hit[0]):
                    hit = (fname, ud)
        found.append(hit[1] if hit else None)
    pals = PALACE_PREFIX_RE.findall(t)
    pal = pals[0] if pals else None
    if pal == '兑':
        pal = '兌'
    elif pal == '离':
        pal = '離'
    return found[0], (found[1] if len(found) > 1 else None), pal


def bits_of_ud(ud):
    up, low = ud
    return TRI_BITS[low] + TRI_BITS[up]


MV_B_RE = re.compile(
    r'([初二三四五上])爻(父母|兄弟|子孙|妻财|官鬼)([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])([金木水火土])动化'
    r'(父母|兄弟|子孙|妻财|官鬼)([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])([金木水火土])')


def audit_group_b(lines_td, hex_text, moving_text):
    """lines_td: 6 条 parse_segment_b 结果（自上而下）。返回 (flags, applicable)"""
    base_ud, changed_ud, pal_prefix = parse_hexagram_text(hex_text or '')
    if base_ud is None:
        return None
    bits = bits_of_ud(base_ud)
    base = derive_chart(bits)
    lines_bu = list(reversed(lines_td))
    moving = {i + 1 for i, p in enumerate(lines_bu) if p['moving']}
    flags = []
    if pal_prefix and pal_prefix != base['palace']:
        flags.append(('R4', 'hard',
                      f"hexagram 文本宫名 {pal_prefix}宫 与卦名推得 {base['palace']}宫 不符"))
    # R1' 动变一致
    if changed_ud is not None:
        derived_changed = tuple(b ^ (1 if (i + 1) in moving else 0) for i, b in enumerate(bits))
        if derived_changed != bits_of_ud(changed_ud):
            flags.append(('R1', 'hard',
                          f"动爻 {sorted(moving)} 推得变卦与文本变卦名不符"))
    elif moving:
        flags.append(('R1', 'soft', '有（动）标记而 hexagram 文本无变卦名'))
    changed = None
    if changed_ud is not None:
        changed = derive_chart(bits_of_ud(changed_ud))
    pal_elem = PALACE_ELEM[base['palace']]
    for pos in range(1, 7):
        p = lines_bu[pos - 1]
        exp = base['lines'][pos]
        if p['stem'] != exp['stem'] or p['branch'] != exp['branch'] or p['elem'] != exp['elem']:
            flags.append(('R2/R3', 'hard',
                          f"{pos}爻 所书 {p['qin']}{p['stem']}{p['branch']}{p['elem']}，推得 {exp['qin']}{exp['stem']}{exp['branch']}{exp['elem']}"))
        elif p['qin'] != exp['qin']:
            flags.append(('R4', 'hard',
                          f"{pos}爻 六亲所书 {p['qin']}，推得 {exp['qin']}（{p['branch']}{p['elem']}）"))
    flags += shi_ying_flags(
        [i + 1 for i, p in enumerate(lines_bu) if p['mark'] == '世'],
        [i + 1 for i, p in enumerate(lines_bu) if p['mark'] == '應'], base)
    # R6' 动化文本互核
    if isinstance(moving_text, str) and changed is not None:
        entries = {}
        for m in MV_B_RE.finditer(simp(moving_text)):
            pos = POS_WORD[m.group(1)]
            entries[pos] = {'from': (norm_qin(m.group(2)), m.group(3), m.group(4)),
                            'to': (norm_qin(m.group(6)), m.group(7), m.group(8))}
        for pos, e in entries.items():
            lp = lines_bu[pos - 1]
            if pos not in moving:
                flags.append(('R6', 'hard', f"moving_lines 称 {pos}爻 动化，卦面该爻无（动）标记"))
                continue
            if e['from'] != (lp['qin'], lp['stem'], lp['branch']):
                flags.append(('R6', 'hard',
                              f"{pos}爻 动化文本本侧作 {e['from']}，卦面作 {(lp['qin'], lp['stem'], lp['branch'])}"))
            cexp = changed['lines'][pos]
            exp_to = (qin_relation(pal_elem, cexp['elem']), cexp['stem'], cexp['branch'])
            if e['to'] != exp_to:
                flags.append(('R6', 'hard',
                              f"{pos}爻 动化文本化出作 {e['to']}，推得 {exp_to}"))
        text_pos = set(entries)
        if text_pos and text_pos != moving:
            flags.append(('R6', 'hard',
                          f"moving_lines 动化位 {sorted(text_pos)} 与卦面动位 {sorted(moving)} 不一致"))
    return flags


# ---------- R7 空亡 ----------
STEMS = '甲乙丙丁戊己庚辛壬癸'
BRANCHES = '子丑寅卯辰巳午未申酉戌亥'


def xunkong(day_gz):
    s = STEMS.index(day_gz[0])
    b = BRANCHES.index(day_gz[1])
    head = (b - s) % 12
    covered = {(head + k) % 12 for k in range(10)}
    return {BRANCHES[i] for i in range(12) if i not in covered}


def audit_r7(card):
    att = card.get('context', {}).get('attachments', {}) or {}
    kw = att.get('空亡')
    if not kw:
        return []
    date_txt = att.get('date_ganzhi') or card.get('context', {}).get('asked_at') or ''
    m = re.findall(r'([甲乙丙丁戊己庚辛壬癸])([子丑寅卯辰巳午未申酉戌亥])日', date_txt)
    if not m:
        return []
    day = m[-1][0] + m[-1][1]
    exp = xunkong(day)
    written = {ch for ch in kw if ch in BRANCHES}
    if written and written != exp:
        return [('R7', 'hard', f"空亡所书 {''.join(sorted(written))}，{day}日推得 {''.join(sorted(exp))}")]
    return []


def main():
    meta = json.load(open(P3 / 'runs/round31/judging/host-meta.json'))
    master8 = json.load(open(P3 / 'data/master-baseline-dev8.json'))
    cards = {}
    for p in (P3 / 'inputs-dev10').glob('*.json'):
        c = json.loads(p.read_text(encoding='utf-8'))
        cards[c.get('id') or p.stem] = c
    ids246 = sorted(c for c in meta if meta[c]['tradition'] == 'liuyao' and c in master8)
    assert len(ids246) == 246, len(ids246)

    results = {}
    for cid in ids246:
        card = cards[cid]
        att = card.get('context', {}).get('attachments', {}) or {}
        rec = {'flags': [], 'status': 'ok'}
        cl = att.get('chart_lines_top_to_bottom')
        if not cl:
            rec['status'] = 'no_chart'
            rec['flags'] = [{'rule': r, 'severity': s, 'detail': d} for r, s, d in audit_r7(card)]
            results[cid] = rec
            continue
        # 格式判别：首行可解析者为准
        fmt = None
        if parse_chart_line_a(cl[0]) is not None:
            fmt = 'A'
        elif parse_segment_b(cl[0]) is not None:
            fmt = 'B'
        rec['format'] = fmt
        if fmt is None or len(cl) % 6 != 0:
            rec['status'] = 'unparseable'
            rec['unparseable_lines'] = cl[:3]
            rec['flags'] = [{'rule': r, 'severity': s, 'detail': d} for r, s, d in audit_r7(card)]
            results[cid] = rec
            continue
        all_flags = []
        if fmt == 'A':
            parsed = [parse_chart_line_a(ln) for ln in cl]
            if any(p is None for p in parsed):
                rec['status'] = 'unparseable'
                rec['unparseable_lines'] = [cl[i] for i, p in enumerate(parsed) if p is None][:3]
                rec['flags'] = [{'rule': r, 'severity': s, 'detail': d} for r, s, d in audit_r7(card)]
                results[cid] = rec
                continue
            groups = [parsed[i:i + 6] for i in range(0, len(parsed), 6)]
            for gi, g in enumerate(groups):
                for rule, sev, det in audit_group_a(g):
                    all_flags.append({'rule': rule, 'severity': sev,
                                      'detail': (f"第{gi + 1}卦 " if len(groups) > 1 else '') + det})
            r6 = audit_r6_a(att.get('moving_lines') if isinstance(att.get('moving_lines'), str) else None, parsed)
            if r6:
                all_flags += [{'rule': r, 'severity': s, 'detail': d} for r, s, d in r6]
        else:  # B
            parsed = [parse_segment_b(ln) for ln in cl]
            if any(p is None for p in parsed):
                rec['status'] = 'unparseable'
                rec['unparseable_lines'] = [cl[i] for i, p in enumerate(parsed) if p is None][:3]
                rec['flags'] = [{'rule': r, 'severity': s, 'detail': d} for r, s, d in audit_r7(card)]
                results[cid] = rec
                continue
            groups = [parsed[i:i + 6] for i in range(0, len(parsed), 6)]
            if len(groups) > 1:
                rec['status'] = 'unparseable'
                rec['unparseable_lines'] = ['多组卦面（格式 B 多卦卡未纳入本轮实现）']
                rec['flags'] = [{'rule': r, 'severity': s, 'detail': d} for r, s, d in audit_r7(card)]
                results[cid] = rec
                continue
            bf = audit_group_b(groups[0], att.get('hexagram'), att.get('moving_lines'))
            if bf is None:
                rec['status'] = 'unparseable'
                rec['unparseable_lines'] = ['hexagram 文本卦名不可解析']
                rec['flags'] = [{'rule': r, 'severity': s, 'detail': d} for r, s, d in audit_r7(card)]
                results[cid] = rec
                continue
            all_flags += [{'rule': r, 'severity': s, 'detail': d} for r, s, d in bf]
            if any(p['uncertain'] for p in parsed):
                rec['uncertain_marks'] = True
        all_flags += [{'rule': r, 'severity': s, 'detail': d} for r, s, d in audit_r7(card)]
        rec['flags'] = all_flags
        results[cid] = rec

    json.dump(results, open(OUT / 'census.json', 'w'), ensure_ascii=False, indent=1)

    st = Counter(r['status'] for r in results.values())
    fmt_c = Counter(r.get('format') for r in results.values())
    hard_cases = {c for c, r in results.items() if any(f['severity'] == 'hard' for f in r['flags'])}
    soft_cases = {c for c, r in results.items() if any(f['severity'] == 'soft' for f in r['flags'])} - hard_cases
    rule_hard = Counter()
    rule_soft = Counter()
    nflags_hard = 0
    for r in results.values():
        for f in r['flags']:
            if f['severity'] == 'hard':
                rule_hard[f['rule']] += 1
                nflags_hard += 1
            else:
                rule_soft[f['rule']] += 1
    lines = ['# 六爻输入机械核查普查（CENSUS）', '',
             '- 范围：(c) 子集 n＝246（inputs-dev10）',
             f"- 状态分布：{dict(st)}；格式分布：{dict(fmt_c)}",
             f"- 硬标记：{nflags_hard} 条，涉 {len(hard_cases)} 例",
             f"- 仅软标记涉例：{len(soft_cases)} 例",
             f"- 硬标记按规则：{dict(rule_hard)}",
             f"- 软标记按规则：{dict(rule_soft)}", '',
             '## 硬标记涉例清单', '']
    for c in sorted(hard_cases):
        fl = [f for f in results[c]['flags'] if f['severity'] == 'hard']
        lines.append(f"- {c}（{len(fl)} 条）：")
        for f in fl:
            lines.append(f"  - [{f['rule']}] {f['detail']}")
    (OUT / 'CENSUS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f"cases=246 status={dict(st)} formats={dict(fmt_c)} hard_flags={nflags_hard} hard_cases={len(hard_cases)} soft_only={len(soft_cases)}")
    print('hard by rule:', dict(rule_hard), '| soft by rule:', dict(rule_soft))


if __name__ == '__main__':
    sys.exit(main())
