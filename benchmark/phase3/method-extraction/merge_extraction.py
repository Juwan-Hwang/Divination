#!/usr/bin/env python3
"""Assemble extraction drafts into method chapters (host merge tooling).
新增 blocks are appended verbatim under a dated supplement header; 冲突 blocks
go to a juxtaposition register (unresolved, both sides kept); 已涵盖 blocks are
indexed only (no duplication). Counts are asserted against draft reports.
"""
import re, sys

P3 = 'benchmark/phase3'

def parse_items(path, prefix):
    text = open(path, encoding='utf-8').read()
    parts = re.split(r'(?m)^(### ' + prefix + r'-\d+.*)$', text)
    items = []
    for i in range(1, len(parts), 2):
        header, body = parts[i], parts[i + 1]
        # body runs to the next ### or ## header
        body = re.split(r'(?m)^#{2,3} ', body)[0].rstrip()
        rel = ''
        for line in body.splitlines():
            if '与现章关系' in line:
                rel = line
                break
        val = rel.split('：', 1)[-1].replace('*', '').strip() if rel else ''
        if val.startswith('冲突') or '〔冲突〕' in header:
            kind = 'conflict'
        elif val.startswith('已涵盖'):
            kind = 'covered'
        elif val.startswith('新增'):
            kind = 'new'
        else:
            kind = 'UNKNOWN'
        items.append({'header': header.strip(), 'body': body, 'kind': kind, 'rel': rel})
    return items

def supplement(items, group_name):
    out = []
    new = [x for x in items if x['kind'] == 'new']
    conf = [x for x in items if x['kind'] == 'conflict']
    cov = [x for x in items if x['kind'] == 'covered']
    unk = [x for x in items if x['kind'] == 'UNKNOWN']
    assert not unk, [x['header'] for x in unk]
    out.append(f'### {group_name}·新增条目（{len(new)} 条）\n')
    for x in new:
        out.append(x['header'] + '\n' + x['body'] + '\n')
    if conf:
        out.append(f'### {group_name}·冲突并列登记（{len(conf)} 条，未裁决）\n')
        for x in conf:
            out.append(x['header'] + '\n' + x['body'] + '\n')
    if cov:
        out.append(f'### {group_name}·已涵盖索引（{len(cov)} 条，不重复入章）\n')
        for x in cov:
            out.append(f'- {x["header"][4:]}——{x["rel"].split("：", 1)[-1].strip()}\n')
    return ''.join(out), (len(new), len(cov), len(conf))

HDR = ('\n\n---\n\n## 增补编：断法提炼批次入账（2026-10-30）\n\n'
       '本编条目由断法提炼批次自用户到货原典提炼入账（草稿存 benchmark/phase3/method-extraction/，'
       '汇总见 EXTRACTION-REPORT.md）。只做知识入账：未按任何分数取舍，**不宣称增益**，效力待后续预注册轮次验证。'
       '「冲突并列登记」诸条两说并存未裁决：作断遇之，须在 basis 写明取舍与所据。\n\n')

# liuyao chapter
l1 = parse_items(f'{P3}/method-extraction/l1/DRAFT.md', 'L1')
l2 = parse_items(f'{P3}/method-extraction/l2/DRAFT.md', 'L2')
s1, c1 = supplement(l1, '甲组（易冒／断易天机／黄金策）')
s2, c2 = supplement(l2, '乙组（易隐／卜筮全书／易林补遗／火珠林）')
print('L1 new/cov/conf:', c1, 'L2:', c2)
assert c1 == (49, 17, 14), c1
assert c2 == (55, 7, 10), c2
ch = f'{P3}/method/references/chinese-liuyao-meihua.md'
with open(ch, 'a', encoding='utf-8') as f:
    f.write(HDR + s1 + '\n' + s2)

# bazi chapter (append at file end; header scopes it to 上篇八字)
b1 = parse_items(f'{P3}/method-extraction/b1/DRAFT.md', 'B1')
s3, c3 = supplement(b1, '八字组（滴天髓阐微／子平真诠）')
print('B1 new/cov/conf:', c3)
assert c3 == (54, 10, 5), c3
ch2 = f'{P3}/method/references/chinese-bazi-ziwei.md'
with open(ch2, 'a', encoding='utf-8') as f:
    f.write(HDR.replace('本编条目', '本编条目（八字部分）') + s3 +
            '\n> 紫微部分增补见 `chinese-ziwei.md`（《紫微斗数全书》整章提炼，同批入账）。\n')
print('merge done')
