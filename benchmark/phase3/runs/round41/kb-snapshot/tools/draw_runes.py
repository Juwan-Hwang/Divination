#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
卢恩抽符 — draw_runes.py（Elder Futhark 长者富萨克，24 符文）
随机源：secrets（CSPRNG），不用 random / 可预测种子。
用法：
  python3 draw_runes.py        # 默认抽 1 根
  python3 draw_runes.py 3      # 抽 3 根（过去/现在/未来，即三诺恩阵）
说明：约半数符文图形可倒置，抽到可逆符文时以 secrets 定正/逆（merkstave）；
不可逆符文（图形上下对称者）只记正位。
"""
import sys
import secrets

# (符文, 名, 音, 本义/关键词, 是否可逆)
RUNES = [
    ("ᚠ", "Fehu", "F", "家畜/财富、流动资产", True),
    ("ᚢ", "Uruz", "U", "原牛、原始力量/健康", True),
    ("ᚦ", "Thurisaz", "Th", "巨人/荆棘、防御与冲击", True),
    ("ᚨ", "Ansuz", "A", "神（奥丁）、讯息/智慧", True),
    ("ᚱ", "Raidho", "R", "骑行/旅程、节奏", True),
    ("ᚲ", "Kenaz", "K", "火炬、知识/洞见", True),
    ("ᚷ", "Gebo", "G", "礼物、交换/伙伴关系", False),
    ("ᚹ", "Wunjo", "W", "喜悦、和谐", True),
    ("ᚺ", "Hagalaz", "H", "冰雹、自然力/突变", False),
    ("ᚾ", "Nauthiz", "N", "需要、匮乏/韧性", True),
    ("ᛁ", "Isa", "I", "冰、静止/停顿", False),
    ("ᛃ", "Jera", "J/Y", "年/收成、周期回报", False),
    ("ᛇ", "Eihwaz", "Ei", "紫杉、坚韧/生死之间", False),
    ("ᛈ", "Perthro", "P", "骰盅（义未确）、命运/未知", True),
    ("ᛉ", "Algiz", "Z", "麋鹿/莎草、守护", True),
    ("ᛊ", "Sowilo", "S", "太阳、成功/能量", False),
    ("ᛏ", "Tiwaz", "T", "提尔神、正义/牺牲", True),
    ("ᛒ", "Berkano", "B", "桦树、生长/新生", True),
    ("ᛖ", "Ehwaz", "E", "马、信任/协作前进", True),
    ("ᛗ", "Mannaz", "M", "人、自我/社会关系", True),
    ("ᛚ", "Laguz", "L", "水/湖、直觉/流动", True),
    ("ᛜ", "Ingwaz", "Ng", "英格神、孕育/潜能", False),
    ("ᛞ", "Dagaz", "D", "白昼、突破/觉醒", False),
    ("ᛟ", "Othala", "O", "祖产/家园、传承", True),
]

POSITIONS_3 = ["过去 / 根源", "现在 / 状况", "未来 / 倾向"]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if n not in (1, 3):
        print("只支持抽 1 或 3 根")
        sys.exit(1)
    pool = list(RUNES)
    drawn = []
    for _ in range(n):
        idx = secrets.randbelow(len(pool))
        drawn.append(pool.pop(idx))  # 不放回抽取
    print(f"卢恩抽符（Elder Futhark 24，secrets 抽取，抽 {n} 根）")
    print("-" * 48)
    for i, (glyph, name, sound, meaning, reversible) in enumerate(drawn):
        pos = POSITIONS_3[i] if n == 3 else "指引"
        if reversible and secrets.randbelow(2) == 1:
            ori = "逆位 merkstave（义偏阻塞/反面）"
        else:
            ori = "正位"
        print(f"【{pos}】{glyph} {name}（音 {sound}）— {meaning}｜{ori}")


if __name__ == "__main__":
    main()
