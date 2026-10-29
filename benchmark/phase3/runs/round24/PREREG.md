# Round 24 预注册（2026-10-29，零改动基线轮，新池 dev8）

- 目的：方法零改动（现行 R21 版，与 round23/method-used 逐字相同），在新池 dev8（412 例＝dev7 334＋holdout8 已用 28＋expansion7 dev-add 50）上建立基线，为后续平台判定（须再一轮零改动复现对照）与干预轮立对照点。本轮不作平台宣称。
- 大师基线：data/master-baseline-dev8.json（412/412 覆盖，均分 4.626、pass 330/412；建构记录见 data/master-baseline-dev8-BUILD.md）。
- 分组：runs/round24/batches.json 新编 25 批（dev8 id 排序、每批 17 例、末批 4 例）。盲测输入只读 benchmark/phase3/inputs8/<case_id>.json；方法只读 runs/round24/kb-snapshot。盲测/评审冻结提示逐字使用（runs/calib-r17 的 BLIND-PROMPT.txt / JUDGE-PROMPT.txt 口径，路径按本轮 inputs8 与 round24 替换，主持不附加额外禁令）。
- 评审：build_packets.py（已补 roster8-additions 读取）产 packetA/packetB，主持切半 4 份、双评审 8 文件（judgeA-part1＝A1＋A2 拼接、judgeA-part2、judgeB 同理）；分歧规则 |Δ(claims+timing)|≥2 或 pass 不一致 → 仲裁；merge_scores.py 对 master-baseline-dev8.json 出 final-scores。
- 重点分段（预先声明，不作事后挑选）：全集配对差；low/high 分段；新入池段（holdout8-used 28、expansion7 50，其中六壬 LR2 与易隐/卜筮全书六爻为 holdout8 诊断点名的缺口段）；分体系 liuyao/liuren/bazi/horary 等。
- 轴一旁报：不单独跑，同前。

*主持角，2026-10-29*
