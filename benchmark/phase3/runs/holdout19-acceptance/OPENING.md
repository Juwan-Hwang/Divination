# holdout19 开封记录（R52）

- 开封时点：R52 平台判读定稿后（2026-10-31，Asia/Shanghai）。
- 开封条件（R52 PREREG §3 写死：平台三项全立之轮即开；开封前置三项全数留痕后才许分发）：
  1. 平台三项全立 ✔ —— (a) 全集配对差 −1.221（SE 0.106，n=487，线 −1.371，余量 +0.150）；(b) 分科护栏四线全立（八字全集 −0.155／线 −0.449，余量 +0.294；natal +0.740／线 +0.290，余量 +0.450；horary −0.540／线 −0.760，余量 +0.220；六壬 dev8 −2.472／线 −2.600，余量 +0.128）；(c) 六爻 dev8 单轮 −1.914（SE 0.134，n=246，线 −1.93，余量 +0.016，熔断线 −2.255 未触）。归因护栏：BZ-FY 未触发（−0.155 ＞ −0.816）；六壬合并段（n=30）−1.975 ＞ −2.550、继续恶化登记未触发。源：runs/round52/final-scores.json（analysis_r52），平台定稿提交 c36a984c。平台全立计数更新为 14 轮。
  2. 验收快照 ✔ —— runs/round52/kb-snapshot-acceptance 自活 method/（benchmark/phase3/method）生成，主持以 SHA-256 逐文件验与活 method/ 及 runs/round52/kb-snapshot 三方全等（20 文件、零差异）。
  3. 内容级断语复扫 ✔ —— 主持以本轮新写脚本 runs/round52/scan_holdout19_accept_r52.py（标记集逐字承 R42 PREREG §5：一级 13 项＋二级 9 项＋字段名黑名单，并与 R42 脚本常量断言全等）对 holdout19/inputs/ 25 卡全字段复扫，输出「accept-scan r52: 25 cards, total hits = 0」。
  4. 金标 SHA 主持独立复核 ✔ —— sha256sum holdout19/test_gold.jsonl ＝ `ed29f3a855bbb73980e4d79552842dab268af2941087489b97dc52c6e6349d8b`，与封存值（data/holdout19-seal-log.md）全文一致。
- XJ47-047 裁定（R51 定、R52 PREREG §2 重述，开封轮执行）：验收主口径从严作 **mid**——低污染子集主口径 n＝24（剔除 XJ47-047）；封存口径 low、n＝25 双读并报；两读分歧以主口径为准。封存件一字未动。
- 验收口径（R52 PREREG §3，照 R42 PREREG §8）：三判据——(i) 我方均分 ＞ 大师均分；(ii) 低污染子集配对胜多于负；(iii) 低污染子集配对差为正。主口径 n＝24 判定、封存口径 n＝25 并报。双匿名包（我方/大师）双视评审、|Δtotal|≥3 仲裁替代均值（承 analyze 既例代码规则）。结论只对本集 25 例总体发言、不外推全体系。
- 批次：runs/round52/batches-accept.json（A1＝9、A2＝8、A3＝8，id 排序轮转分批、梦占/非梦占混合）；验收预测落 runs/holdout19-acceptance/predictions/，方法＝验收快照，冻结盲测提示逐字套用。
- CZ-QX：本集无测字例，不结算，同档计数维持 4。
