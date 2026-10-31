# -*- coding: utf-8 -*-
"""WHY 页图半页裁切（R89 封存席转录辅助）：spread PNG -> 单印刷页 PNG。
页序承 R88 实测：PDF 页 n 之右半＝印刷 2n-2、左半＝印刷 2n-1。"""
from PIL import Image
import os
D = '/home/hatch/workspace/divination/benchmark/phase3/runs/round89/why-pages-h33-seat'
for n in (63, 64, 65, 85, 86, 87, 88, 89, 90, 91, 97):
    p = os.path.join(D, f'spread-{n}-{n:03d}.png')
    if not os.path.exists(p):
        print('MISSING', p)
        continue
    im = Image.open(p)
    W, H = im.size
    right = im.crop((int(W * 0.50), 0, W, H))
    left = im.crop((0, 0, int(W * 0.50), H))
    right.save(os.path.join(D, f'p{2 * n - 2}.png'))
    left.save(os.path.join(D, f'p{2 * n - 1}.png'))
    print(p, im.size, '->', 2 * n - 2, 2 * n - 1)
