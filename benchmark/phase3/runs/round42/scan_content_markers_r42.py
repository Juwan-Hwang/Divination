#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""内容级断语扫描脚本（R42 新写唯一名）。

依据：runs/round42/PREREG.md §5「验封常例升级」——标记集常量逐字复制该节，
脚本头注释引该节节号（§5）。三道扫描共用本脚本：
(1) 候选材料制备期——候选 jsonl 的 input_side 全字段递归字符串扫描（建卡前）；
(2) 建卡自校验——每张输入卡全字段递归字符串扫描，逐卡结果落构建报告；
(3) 主持验封——主持以独立脚本对封存目录全部输入卡复扫（本脚本可供其调用，
    但主持须另行独立执行，不以本席自校验替代）。
字段名黑名单（§5 候选材料制备纪律）：字段名含 断语/断曰/正议/验语/占断/线索·断
者先行拦截，与内容级扫描并行、互不替代。
用法：python3 scan_content_markers_r42.py <file.json|file.jsonl> [...]
输出：每文件一行 JSON（路径、一级/二级命中明细、字段名黑名单命中）。
"""
import json, sys, os

# 一级标记（断语类）——逐字复制 PREREG §5
LEVEL1 = ['断语线索', '断曰', '断語', '正议', '正議', '验语', '驗語',
          '断语：', '斷語：', '占断', '占斷', '大师断', '大師斷']
# 二级标记（结局侧状态措辞）——逐字复制 PREREG §5
LEVEL2 = ['果验', '果然', '果應', '后验', '後驗', '结局', '結局', '应验', '應驗']
# 字段名黑名单片段（PREREG §5：字段名含断语/断曰/正议/验语/占断/线索·断者）
FIELD_BLACKLIST = ['断语', '斷語', '断曰', '斷曰', '正议', '正議', '验语', '驗語',
                   '占断', '占斷', '线索', '線索']


def scan_content(obj, path=''):
    """全字段递归字符串扫描，返回 [(字段路径, 级别, 标记, 命中片段)]。"""
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
                    hits.append((path, lvl, m, obj[max(0, idx - 12):idx + len(m) + 12]))
    return hits


def scan_field_names(obj, path=''):
    """字段名黑名单扫描，返回 [(字段路径, 命中片段)]。"""
    hits = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            for frag in FIELD_BLACKLIST:
                if frag in k:
                    hits.append((f'{path}/{k}', frag))
                    break
            hits += scan_field_names(v, f'{path}/{k}')
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            hits += scan_field_names(v, f'{path}[{i}]')
    return hits


def load_any(p):
    if p.endswith('.jsonl'):
        return [json.loads(l) for l in open(p, encoding='utf-8') if l.strip()]
    return json.load(open(p, encoding='utf-8'))


def main():
    total_l1 = total_l2 = total_fn = 0
    for p in sys.argv[1:]:
        data = load_any(p)
        items = data if isinstance(data, list) else [data]
        for it in items:
            cid = it.get('id', '?') if isinstance(it, dict) else '?'
            ch = scan_content(it)
            fh = scan_field_names(it)
            total_l1 += sum(1 for h in ch if h[1] == 'L1')
            total_l2 += sum(1 for h in ch if h[1] == 'L2')
            total_fn += len(fh)
            print(json.dumps({'file': os.path.basename(p), 'id': cid,
                              'content_hits': [list(h) for h in ch],
                              'fieldname_hits': [list(h) for h in fh]},
                             ensure_ascii=False))
    print(json.dumps({'TOTAL': {'L1': total_l1, 'L2': total_l2, 'fieldname': total_fn}},
                     ensure_ascii=False))


if __name__ == '__main__':
    main()
