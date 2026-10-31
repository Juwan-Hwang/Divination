#!/usr/bin/env python3
# R76 方法集成席脚本：测字（字触补）+ 八字（段氏理象学）两件入章；奇门因 DIGEST 源文件截断未执行（见回传）。
# 方式：从 DIGEST 原文逐条提取 → 只增尾附 → 写后自目标文件附章区重提取逐条比对（diff 为空才算过）。
import re, sys, hashlib, pathlib

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
DIG = BASE / 'runs/round76/digestion'
REF = BASE / 'method/references'

def lines_of(p):
    return p.read_text(encoding='utf-8').split('\n')

def extract(lines, pat):
    return [l for l in lines if re.match(pat, l)]

def ids_of(items, pat):
    return [re.match(pat, l).group(1) for l in items]

failures = []
def check(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        failures.append(msg)

# ---------- 1. 测字：字触补 ----------
zcb_src = lines_of(DIG / 'DIGEST-zichubu-r76.md')
zcb_items = extract(zcb_src, r'^- \*\*(ZCB-M\d+) ')
zcb_ids = ids_of(zcb_items, r'^- \*\*(ZCB-M\d+) ')
check(zcb_ids == [f'ZCB-M{i:02d}' for i in range(1, 13)], f'测字 ZCB-M 条数/编号齐全: {len(zcb_items)} {zcb_ids}')
# 冲突表整表（含表头与分隔行）原文提取：自 '| 编号 |' 行起至 ZB-C5 行为止
tbl_start = next(i for i, l in enumerate(zcb_src) if l.startswith('| 编号 |'))
tbl_rows = []
for l in zcb_src[tbl_start:]:
    if not l.startswith('|'):
        break
    tbl_rows.append(l)
zb_ids = [re.match(r'^\| (ZB-C\d) ', l).group(1) for l in tbl_rows if re.match(r'^\| ZB-C\d ', l)]
check(zb_ids == [f'ZB-C{i}' for i in range(1, 6)], f'测字 ZB-C 冲突齐全: {zb_ids}')
check(len(tbl_rows) == 7, f'测字冲突表行数（表头+分隔+5）: {len(tbl_rows)}')

cezi_path = REF / 'chinese-cezi.md'
cezi_orig = cezi_path.read_text(encoding='utf-8')
check('字触补提炼（R76 入章）' not in cezi_orig, '测字章尚无 R76 承接节（防重复入章）')
cezi_add = (
    '\n## 十二、字触补提炼（R76 入章）\n\n'
    '来源：《字触补》（清·桑灵直编，《四库未收书辑刊》陆辑第拾捌册）断法提炼，DIGEST-zichubu-r76.md（runs/round76/digestion/）ZCB-M01–M12 与冲突并列登记 ZB-C1–C5，照原文转录；效力自 R77 起算，本节与既有各节并列登记、不改既有口径。\n\n'
    + '\n'.join(zcb_items)
    + '\n\n### 冲突并列登记（ZB-C1–C5）\n\n'
    + '\n'.join(tbl_rows)
    + '\n'
)
cezi_path.write_text(cezi_orig + cezi_add, encoding='utf-8')
cezi_new = cezi_path.read_text(encoding='utf-8')
check(cezi_new.startswith(cezi_orig), '测字章既有正文一字未动（新文本以原文为前缀）')
app = cezi_new[len(cezi_orig):]
check(extract(app.split('\n'), r'^- \*\*(ZCB-M\d+) ') == zcb_items, '测字入章 ZCB-M 逐条与 DIGEST 原文 diff 为空')
check([l for l in app.split('\n') if l.startswith('|')] == tbl_rows, '测字入章冲突表逐行与 DIGEST 原文 diff 为空')
print(f'测字新增行数: {cezi_add.count(chr(10))}')

# ---------- 2. 八字：段氏理象学 ----------
ds_src = lines_of(DIG / 'DIGEST-duanshi-r76.md')
ds_items = extract(ds_src, r'^- \*\*(D\d+) ')
ds_ids = ids_of(ds_items, r'^- \*\*(D\d+) ')
check(ds_ids == [f'D{i}' for i in range(1, 41)], f'八字 D 条数/编号齐全: {len(ds_items)}')
k_items = extract(ds_src, r'^- \*\*(K\d) ')
k_ids = ids_of(k_items, r'^- \*\*(K\d) ')
check(k_ids == [f'K{i}' for i in range(1, 9)], f'八字 K 冲突齐全: {k_ids}')

bazi_path = REF / 'chinese-bazi-ziwei.md'
bazi_orig = bazi_path.read_text(encoding='utf-8')
check('段氏理象学提炼附章（R76）' not in bazi_orig, '八字章尚无段氏附章（防重复入章）')
bazi_add = (
    '\n## 附章：段氏理象学提炼附章（R76）\n\n'
    '来源：《段氏理象学》（段建业，2011 年中国商业出版社，ISBN 978-7-5044-7457-5）断法提炼，DIGEST-duanshi-r76.md（runs/round76/digestion/）D1–D40 与冲突并列登记 K1–K8，照原文转录；效力自 R77 起算。K6 裁定（PREREG-ADDENDUM-r76 §二第 3 项）：本书为正式出版文本，其提炼以「段氏一家之说」名义入本附章，不改本章正文的收录总则条文，两说并列。\n\n'
    + '\n'.join(ds_items)
    + '\n\n### 冲突并列登记（K1–K8）\n\n'
    + '\n'.join(k_items)
    + '\n'
)
bazi_path.write_text(bazi_orig + bazi_add, encoding='utf-8')
bazi_new = bazi_path.read_text(encoding='utf-8')
check(bazi_new.startswith(bazi_orig), '八字章既有正文一字未动（新文本以原文为前缀）')
app2 = bazi_new[len(bazi_orig):]
check(extract(app2.split('\n'), r'^- \*\*(D\d+) ') == ds_items, '八字入章 D1–D40 逐条与 DIGEST 原文 diff 为空')
check(extract(app2.split('\n'), r'^- \*\*(K\d) ') == k_items, '八字入章 K1–K8 逐条与 DIGEST 原文 diff 为空')
print(f'八字新增行数: {bazi_add.count(chr(10))}')

print('RESULT:', 'ALL PASS' if not failures else f'{len(failures)} FAILURES')
sys.exit(1 if failures else 0)
