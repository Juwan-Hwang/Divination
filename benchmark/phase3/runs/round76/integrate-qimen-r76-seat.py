#!/usr/bin/env python3
# R76 方法集成席（奇门一件）：chinese-qimen.md 末尾新增附章「R76 三书提炼附章」。
# 规格：PREREG-ADDENDUM-r76 §二第 2 项；效力自 R77 起算；只转录、不裁决；既有正文一字不改、只增尾附。
# 方式：从三份 DIGEST 原文逐条提取 → 按源小节分三次 append（每次回读验尾）→ 写后自附章区重提取逐条比对（diff 为空才算过）。
import re, sys, pathlib

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
DIG = BASE / 'runs/round76/digestion'
TARGET = BASE / 'method/references/chinese-qimen.md'

failures = []
def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        failures.append(msg)

def lines_of(p):
    return p.read_text(encoding='utf-8').split('\n')

# ---------- 源提取 ----------
# 开悟之门：条文为单段行 **KW-Mxx ……；冲突为单段行 **C-KWx ……；KW-M26 补记为补全节内 "- KW-M26 补记……" 行。
kw_src = lines_of(DIG / 'DIGEST-kaiwu-r76.md')
kw_items = [l for l in kw_src if re.match(r'^\*\*KW-M\d+ ', l)]
kw_ids = [re.match(r'^\*\*(KW-M\d+) ', l).group(1) for l in kw_items]
check(kw_ids == [f'KW-M{i:02d}' for i in range(1, 35)], f'开悟 KW-M 条数/编号齐全: {len(kw_items)}')
kw_buji = [l for l in kw_src if l.startswith('- KW-M26 补记')]
check(len(kw_buji) == 1, f'开悟 KW-M26 补记行: {len(kw_buji)}')
kw_conf = [l for l in kw_src if re.match(r'^\*\*C-KW\d ', l)]
kw_conf_ids = [re.match(r'^\*\*(C-KW\d) ', l).group(1) for l in kw_conf]
check(kw_conf_ids == [f'C-KW{i}' for i in range(1, 5)], f'开悟 C-KW 冲突齐全: {kw_conf_ids}')

# 奇门启悟：条文/冲突为块——标题行 **QW-Mxx ……／**QW-Cx …… 后随连续 "- " 条身行；
# QW-M07 条身截断行 "...[truncated 6739 chars]" 不以 "- " 起，不入块（与补全节「截断处不续写」口径一致）。
qw_src = lines_of(DIG / 'DIGEST-qiwu-r76.md')
def blocks(lines, head_pat):
    out = []  # 每块为行列表 [标题行, 条身行...]
    i = 0
    while i < len(lines):
        if re.match(head_pat, lines[i]):
            blk = [lines[i]]
            j = i + 1
            while j < len(lines) and lines[j].startswith('- '):
                blk.append(lines[j]); j += 1
            out.append(blk); i = j
        else:
            i += 1
    return out
qw_items = blocks(qw_src, r'^\*\*QW-M\d+ ')
qw_ids = [re.match(r'^\*\*(QW-M\d+) ', b[0]).group(1) for b in qw_items]
check(qw_ids == [f'QW-M{i:02d}' for i in range(1, 23)], f'启悟 QW-M 条数/编号齐全: {len(qw_items)}')
qw_conf = blocks(qw_src, r'^\*\*QW-C\d ')
qw_conf_ids = [re.match(r'^\*\*(QW-C\d) ', b[0]).group(1) for b in qw_conf]
check(qw_conf_ids == [f'QW-C{i}' for i in range(1, 7)], f'启悟 QW-C 冲突齐全: {qw_conf_ids}')

# 石建国：条文为单行 "- **SG-Mxx ……",冲突为单行 "- **C-SGx ……"。
sg_src = lines_of(DIG / 'DIGEST-shijianguo-r76.md')
sg_items = [l for l in sg_src if re.match(r'^- \*\*SG-M\d+ ', l)]
sg_ids = [re.match(r'^- \*\*(SG-M\d+) ', l).group(1) for l in sg_items]
check(sg_ids == [f'SG-M{i:02d}' for i in range(1, 33)], f'石建国 SG-M 条数/编号齐全: {len(sg_items)}')
sg_conf = [l for l in sg_src if re.match(r'^- \*\*C-SG\d ', l)]
sg_conf_ids = [re.match(r'^- \*\*(C-SG\d) ', l).group(1) for l in sg_conf]
check(sg_conf_ids == [f'C-SG{i}' for i in range(1, 6)], f'石建国 C-SG 冲突齐全: {sg_conf_ids}')

if failures:
    print('SOURCE CHECK FAILED, abort before any write'); sys.exit(1)

orig = TARGET.read_text(encoding='utf-8')
check('R76 三书提炼附章' not in orig, '奇门章尚无 R76 附章（防重复入章）')
if failures:
    print('PRECHECK FAILED, abort'); sys.exit(1)

def append_step(step_name, add_text):
    """append 一段,回读验:既有内容为前缀、文件尾恰为本段尾行。"""
    before = TARGET.read_text(encoding='utf-8')
    TARGET.write_text(before + add_text, encoding='utf-8')
    after = TARGET.read_text(encoding='utf-8')
    check(after.startswith(before), f'{step_name}: 追加后既有内容一字未动（前缀校验）')
    check(after == before + add_text, f'{step_name}: 文件内容恰为原内容＋本段')
    tail_expected = add_text.rstrip('\n').split('\n')[-1]
    tail_actual = after.rstrip('\n').split('\n')[-1]
    check(tail_actual == tail_expected, f'{step_name}: 回读验尾 OK（尾行: {tail_actual[:40]}…）')
    print(f'{step_name}: 新增行数 {add_text.count(chr(10))}')
    return add_text.count('\n')

total_added = 0

# ---------- 第一段:附章首 + 口径注 + 开悟之门小节 ----------
kw_paras = []
for l in kw_items:
    kw_paras.append(l)
    if l.startswith('**KW-M26 '):
        kw_paras.append(kw_buji[0])  # 补记随 M26 附后（补记行本身已注明「补记（不改正文，仅登记原书全文）」）
add1 = (
    '\n## 附章：R76 三书提炼附章\n\n'
    '口径注（照 PREREG-ADDENDUM-r76 §二第 2 项）：本附章为 R76 三书提炼转录，效力自 R77 起算；本附章与正文默认口径冲突处以正文为准、附章只并列登记——排局默认拆补法（启悟「茅山道人法为永久规范」只并列登记、不改默认）、天禽寄宫默认寄坤二（启悟个人规范并列）、生克层级维持既有 SQ 口径（启悟异说并列）。既有正文一字不改。\n\n'
    '### 开悟之门（张志春《开悟之门》，KW-M01–M34＋冲突 C-KW1–C-KW4）\n\n'
    '来源：《开悟之门》（张志春著，新疆人民出版社 2004 年 6 月第 1 版，ISBN 7-288-08782-8）断法提炼，DIGEST-kaiwu-r76.md（runs/round76/digestion/）KW-M01–M34（KW-M27–M34 与冲突 C-KW1–C-KW4 在原文件「补全节」内，入章以补全节文本为源）与 KW-M26 补记，照原文转录；页码为印刷页（正文印刷页＝PDF 页−28）。\n\n'
    + '\n\n'.join(kw_paras)
    + '\n\n#### 冲突并列登记（C-KW1–C-KW4）\n\n'
    + '\n\n'.join(kw_conf)
    + '\n'
)
total_added += append_step('第一段·开悟之门', add1)

# ---------- 第二段:奇门启悟小节 ----------
qw_paras = []
for b in qw_items:
    qw_paras.append('\n'.join(b))
    if b[0].startswith('**QW-M07 '):
        qw_paras.append('（注：QW-M07 條身在原 DIGEST 落盤時截斷於上行，補全節明定截斷處不續寫、自 QW-M08 起補；本附章照原樣轉錄，不臆補。）')
add2 = (
    '\n### 奇门启悟（刘文元《奇門啟悟》，QW-M01–M22＋冲突 QW-C1–C6）\n\n'
    '来源：《奇門啟悟》（劉文元著，天府書屋（滾石出版）繁體版）断法提炼，DIGEST-qiwu-r76.md（runs/round76/digestion/）QW-M01–M22（QW-M08–M22 与冲突 QW-C1–C6 在原文件「補全節」内，入章以補全節文本為源），照原文转录；页码为印刷页。\n\n'
    + '\n\n'.join(qw_paras)
    + '\n\n#### 冲突并列登记（QW-C1–C6）\n\n'
    + '\n\n'.join('\n'.join(b) for b in qw_conf)
    + '\n'
)
total_added += append_step('第二段·奇门启悟', add2)

# ---------- 第三段:石建国小节 ----------
add3 = (
    '\n### 石建国（《奇门遁甲最新实例解析》，SG-M01–M32＋冲突 C-SG1–C-SG5）\n\n'
    '来源：《奇门遁甲最新实例解析》（石建国著，建筑与风水杂志社（中国神秘文化大系），ISBN 988-98339-8-0）断法提炼，DIGEST-shijianguo-r76.md（runs/round76/digestion/）SG-M01–M32 与冲突 C-SG1–C-SG5，照原文转录；页码为书内印刷页。\n\n'
    + '\n'.join(sg_items)
    + '\n\n#### 冲突并列登记（C-SG1–C-SG5）\n\n'
    + '\n'.join(sg_conf)
    + '\n'
)
total_added += append_step('第三段·石建国', add3)

# ---------- 写后总验合:自附章区重提取逐条比对 ----------
new = TARGET.read_text(encoding='utf-8')
check(new.startswith(orig), '总验:既有正文一字未动（新文本以原文为前缀）')
app = new[len(orig):]
app_lines = app.split('\n')

app_kw = [l for l in app_lines if re.match(r'^\*\*KW-M\d+ ', l)]
check(app_kw == kw_items, '入章 KW-M01–M34 逐条与 DIGEST 原文 diff 为空')
app_buji = [l for l in app_lines if l.startswith('- KW-M26 补记')]
check(app_buji == kw_buji, '入章 KW-M26 补记与 DIGEST 补全节原文 diff 为空')
# 补记位置:M26 条之后、M27 条之前
i26 = app_lines.index(kw_items[25]); ib = app_lines.index(kw_buji[0]); i27 = app_lines.index(kw_items[26])
check(i26 < ib < i27, 'KW-M26 补记位置在 M26 之后、M27 之前')
app_kw_conf = [l for l in app_lines if re.match(r'^\*\*C-KW\d ', l)]
check(app_kw_conf == kw_conf, '入章 C-KW1–C-KW4 逐条与 DIGEST 原文 diff 为空')

app_qw = blocks(app_lines, r'^\*\*QW-M\d+ ')
check(app_qw == qw_items, '入章 QW-M01–M22 逐块（标题＋条身）与 DIGEST 原文 diff 为空')
app_qw_conf = blocks(app_lines, r'^\*\*QW-C\d ')
check(app_qw_conf == qw_conf, '入章 QW-C1–C6 逐块（标题＋条身）与 DIGEST 原文 diff 为空')

app_sg = [l for l in app_lines if re.match(r'^- \*\*SG-M\d+ ', l)]
check(app_sg == sg_items, '入章 SG-M01–M32 逐条与 DIGEST 原文 diff 为空')
app_sg_conf = [l for l in app_lines if re.match(r'^- \*\*C-SG\d ', l)]
check(app_sg_conf == sg_conf, '入章 C-SG1–C-SG5 逐条与 DIGEST 原文 diff 为空')

print(f'附章新增行数合计: {total_added}')
print('RESULT:', 'ALL PASS' if not failures else f'{len(failures)} FAILURES')
sys.exit(1 if failures else 0)
