#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
塔罗抽牌 — draw_tarot.py（Rider-Waite-Smith 体系，78 张）
随机源：secrets（CSPRNG）洗牌与定正逆位，不用 random / 可预测种子。
用法：
  python3 draw_tarot.py          # 默认抽 3 张（过去/现在/未来）
  python3 draw_tarot.py 1        # 抽 1 张（今日指引）
  python3 draw_tarot.py 10       # 抽 10 张（凯尔特十字）
"""
import sys
import secrets

MAJOR = [
    "愚者 The Fool", "魔术师 The Magician", "女祭司 The High Priestess",
    "皇后 The Empress", "皇帝 The Emperor", "教皇 The Hierophant",
    "恋人 The Lovers", "战车 The Chariot", "力量 Strength",
    "隐士 The Hermit", "命运之轮 Wheel of Fortune", "正义 Justice",
    "倒吊人 The Hanged Man", "死神 Death", "节制 Temperance",
    "恶魔 The Devil", "高塔 The Tower", "星星 The Star",
    "月亮 The Moon", "太阳 The Sun", "审判 Judgement", "世界 The World",
]
SUITS = ["权杖 Wands", "圣杯 Cups", "宝剑 Swords", "星币 Pentacles"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
         "侍从 Page", "骑士 Knight", "王后 Queen", "国王 King"]


def full_deck():
    deck = list(MAJOR)
    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{suit}·{rank}")
    return deck  # 22 + 4*14 = 78


SPREADS = {
    1: ["指引"],
    3: ["过去 / 根源", "现在 / 状况", "未来 / 倾向"],
    10: ["现状", "挑战（横牌）", "根源 / 潜意识", "过去", "目标 / 显意识",
         "近未来", "自我态度", "环境 / 他人", "希望与恐惧", "结果倾向"],
}


def secure_shuffle(deck):
    """Fisher-Yates，随机数全部来自 secrets。"""
    d = list(deck)
    for i in range(len(d) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        d[i], d[j] = d[j], d[i]
    return d


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    if n not in SPREADS:
        print("只支持抽 1 / 3 / 10 张")
        sys.exit(1)
    deck = secure_shuffle(full_deck())
    print(f"塔罗抽牌（Rider-Waite，secrets 洗牌，共 78 张，抽 {n} 张）")
    print("-" * 48)
    for pos, card in zip(SPREADS[n], deck[:n]):
        orientation = "正位" if secrets.randbelow(2) == 0 else "逆位"
        print(f"【{pos}】{card}（{orientation}）")


if __name__ == "__main__":
    main()
