# -*- coding: utf-8 -*-
"""WHY 页图半页裁切（R88 组集席转录辅助）：spread PNG -> 单印刷页 PNG。
页序实测（PDF p50 spread 读图核）：PDF 页 n 之右半＝印刷 2n-2、左半＝印刷 2n-1。"""
from PIL import Image
import os
D = '/home/hatch/workspace/divination/benchmark/phase3/runs/round88/why-pages-h32-seat'
for n in list(range(50, 64)) + [95, 96]:
    fn = f'spread-{n:03d}.png' if n < 95 else f'spreadx-{n:03d}.png'
    p = os.path.join(D, fn)
    if not os.path.exists(p):
        print('MISSING', p)
        continue
    im = Image.open(p)
    W, H = im.size
    right = im.crop((int(W * 0.50), 0, W, H))
    left = im.crop((0, 0, int(W * 0.50), H))
    right.save(os.path.join(D, f'p{2 * n - 2}.png'))
    left.save(os.path.join(D, f'p{2 * n - 1}.png'))
    print(fn, im.size, '->', 2 * n - 2, 2 * n - 1)
