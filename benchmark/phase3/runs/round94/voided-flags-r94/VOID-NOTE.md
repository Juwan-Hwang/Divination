# VOID-NOTE — R94 tradition 旗标作废件（2026-11-01 主持裁定）

主持验盘（verify_predictions_host_r94.py）tradition 旗标候选 5 件，逐件回读卡面（inputs-dev12）＋预测首行裁定：

| case | 卡面实况 | 预测首行 | 裁定 |
|---|---|---|---|
| AS-301 | tradition='astrology' | 「卡面未标注 tradition 字段」 | **真虚称成立**——陈述与卡面字段在场事实直接矛盾。作废重测（承 R79 LY-022 判例）。 |
| AS-307 | tradition='astrology' | 「卡面未标注 tradition 字段」 | **真虚称成立**——同上。作废重测。 |
| LY-036 | tradition 缺、system='liuyao' | 「卡面未标注 tradition 字段…（卡面亦未载 system 字段）」 | **真虚称成立（system 条款）**——tradition 条款属实，system 条款与卡面矛盾。作废重测。 |
| BZ-021 | tradition/system 均缺 | 「卡面未标注 tradition 字段，按题面体裁自决（八字）」 | 旗标不成立——陈述属实，检查器误报，登记在案。 |
| LY-221 | tradition='liuyao' | 「卡面 tradition＝liuyao（逐字照录）」 | 旗标不成立——首行已逐字照录，检查器因全角等号未检出，登记在案。 |

本目录三件为作废原件，只增不删、保留备查；重测件由新席按冻结 BLIND 定本重写至 predictions/。
claim 声明组候选 0 件。
另登记两件零影响隔离接触自报（不作废）：B12 席校验脚本以 glob 解析 predictions 目录全部 LY-*.json 仅取 case_id 过滤（未读他批正文）；B23 席曾对 predictions 目录执行一次 `ls | head` 仅见文件名（未打开内容）。均诚实自报、影响为零，入 ADDENDUM-r94。
