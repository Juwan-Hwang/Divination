#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R80 holdout25 探查5（只读）：GSZ 入选例动爻/世应行明细，供封存日志逐例登记。"""
import json, os
BASE = '/home/hatch/workspace/divination/benchmark/phase3'
gsz = json.load(open(os.path.join(BASE, 'runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json'), encoding='utf-8'))
by = {e['provisional_id']: e for e in gsz['entries']}
for cid in ('GSZ-049', 'GSZ-050', 'GSZ-052', 'GSZ-053', 'GSZ-054', 'GSZ-055',
            'GSZ-058', 'GSZ-059', 'GSZ-060', 'GSZ-061', 'GSZ-068'):
    ch = by[cid]['input_fields']['chart']
    lines = ch['chart_lines_top_to_bottom']
    moving = [ln.strip() for ln in lines if '动' in ln]
    shi = [ln.strip() for ln in lines if '世' in ln]
    ying = [ln.strip() for ln in lines if '应' in ln]
    print(cid, '| 本', ch.get('ben_gua'), '变', ch.get('bian_gua'), '| 动爻:', '；'.join(moving),
          '| 世:', '；'.join(shi), '| 应:', '；'.join(ying))
