#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
铜钱起卦（周易六爻）— cast_iching.py

方法：三枚铜钱掷六次，自下而上成卦（传统规则）。
  每枚铜钱：字（反面）记 2，背（正面/花）记 3 —— 本脚本以加密随机模拟，
  每枚取 2 或 3，三枚求和：
    6 = 老阴（动爻，阴变阳）  ×
    7 = 少阳（静爻）          —
    8 = 少阴（静爻）          - -
    9 = 老阳（动爻，阳变阴）  ○
随机源：secrets（操作系统 CSPRNG），不用 random、不用可预测种子。
用法：python3 cast_iching.py ["所问何事"]
输出：逐爻结果、本卦名、动爻、变卦名（无动爻则无变卦）。
"""
import sys
import secrets

# 八卦：爻位自下而上，1=阳，0=阴
TRIGRAMS = {
    (1, 1, 1): "乾",
    (1, 1, 0): "兑",
    (1, 0, 1): "离",
    (1, 0, 0): "震",
    (0, 1, 1): "巽",
    (0, 1, 0): "坎",
    (0, 0, 1): "艮",
    (0, 0, 0): "坤",
}

# 64 卦（文王卦序）：(卦名, 上卦, 下卦)
HEXAGRAM_ORDER = [
    ("乾", "乾", "乾"), ("坤", "坤", "坤"), ("屯", "坎", "震"), ("蒙", "艮", "坎"),
    ("需", "坎", "乾"), ("讼", "乾", "坎"), ("师", "坤", "坎"), ("比", "坎", "坤"),
    ("小畜", "巽", "乾"), ("履", "乾", "兑"), ("泰", "坤", "乾"), ("否", "乾", "坤"),
    ("同人", "乾", "离"), ("大有", "离", "乾"), ("谦", "坤", "艮"), ("豫", "震", "坤"),
    ("随", "兑", "震"), ("蛊", "艮", "巽"), ("临", "坤", "兑"), ("观", "巽", "坤"),
    ("噬嗑", "离", "震"), ("贲", "艮", "离"), ("剥", "艮", "坤"), ("复", "坤", "震"),
    ("无妄", "乾", "震"), ("大畜", "艮", "乾"), ("颐", "艮", "震"), ("大过", "兑", "巽"),
    ("坎", "坎", "坎"), ("离", "离", "离"), ("咸", "兑", "艮"), ("恒", "震", "巽"),
    ("遁", "乾", "艮"), ("大壮", "震", "乾"), ("晋", "离", "坤"), ("明夷", "坤", "离"),
    ("家人", "巽", "离"), ("睽", "离", "兑"), ("蹇", "坎", "艮"), ("解", "震", "坎"),
    ("损", "艮", "兑"), ("益", "巽", "震"), ("夬", "兑", "乾"), ("姤", "乾", "巽"),
    ("萃", "兑", "坤"), ("升", "坤", "巽"), ("困", "兑", "坎"), ("井", "坎", "巽"),
    ("革", "兑", "离"), ("鼎", "离", "巽"), ("震", "震", "震"), ("艮", "艮", "艮"),
    ("渐", "巽", "艮"), ("归妹", "震", "兑"), ("丰", "震", "离"), ("旅", "离", "艮"),
    ("巽", "巽", "巽"), ("兑", "兑", "兑"), ("涣", "巽", "坎"), ("节", "坎", "兑"),
    ("中孚", "巽", "兑"), ("小过", "震", "艮"), ("既济", "坎", "离"), ("未济", "离", "坎"),
]

TRIGRAM_LINES = {name: bits for bits, name in TRIGRAMS.items()}

def hexagram_name(lines_bottom_up):
    """lines_bottom_up: 6 个 0/1，自下而上。返回 (卦序, 卦名, 上卦, 下卦)"""
    lower = tuple(lines_bottom_up[0:3])
    upper = tuple(lines_bottom_up[3:6])
    lower_name = TRIGRAMS[lower]
    upper_name = TRIGRAMS[upper]
    for idx, (name, up, low) in enumerate(HEXAGRAM_ORDER, start=1):
        if up == upper_name and low == lower_name:
            return idx, name, upper_name, lower_name
    raise ValueError("卦象不在 64 卦表内")

def toss_line():
    """掷三枚铜钱一次，返回 (和值, 爻值 0/1, 是否动爻)"""
    total = sum(secrets.choice((2, 3)) for _ in range(3))
    if total == 6:   # 老阴，动，阴变阳
        return total, 0, True
    if total == 7:   # 少阳，静
        return total, 1, False
    if total == 8:   # 少阴，静
        return total, 0, False
    # total == 9     # 老阳，动，阳变阴
    return total, 1, True

LINE_LABEL = {6: "老阴 ×（动）", 7: "少阳 —（静）", 8: "少阴 - -（静）", 9: "老阳 ○（动）"}
LINE_DRAW = {(1, False): "━━━━━━━", (0, False): "━━━ ━━━",
             (1, True): "━━━━━━━ ○", (0, True): "━━━ ━━━ ×"}
POS_NAME = ["初爻", "二爻", "三爻", "四爻", "五爻", "上爻"]

def main():
    question = sys.argv[1] if len(sys.argv) > 1 else "（未填写所问何事）"
    print("周易铜钱起卦（secrets 加密随机，三钱六掷，自下而上）")
    print(f"所问：{question}")
    print("-" * 48)
    lines, changed, moving = [], [], []
    tosses = []
    for i in range(6):
        total, val, is_moving = toss_line()
        tosses.append((i, total, val, is_moving))
        lines.append(val)
        changed.append(1 - val if is_moving else val)
        if is_moving:
            moving.append(i + 1)
    # 自上而下打印卦画（观感与传统卦图一致），标注爻位
    for i in range(5, -1, -1):
        _, total, val, is_moving = tosses[i]
        print(f"{POS_NAME[i]}  {LINE_DRAW[(val, is_moving)]:<12} 和={total}  {LINE_LABEL[total]}")
    print("-" * 48)
    idx, name, up, low = hexagram_name(lines)
    print(f"本卦：第{idx}卦 {name}（上{up}下{low}）")
    if moving:
        c_idx, c_name, c_up, c_low = hexagram_name(changed)
        print(f"动爻：第{'、'.join(str(m) for m in moving)}爻")
        print(f"变卦：第{c_idx}卦 {c_name}（上{c_up}下{c_low}）")
        print(f"记作：{name} 之 {c_name}")
    else:
        print("动爻：无（静卦，看本卦卦辞与彖象）")
        print("变卦：无")

if __name__ == "__main__":
    main()
