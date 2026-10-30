# R51 PREREG ADDENDUM-1（轮内留痕件，不改预注册口径）

## 一、B14 盲测席隔离自报（主持核算：影响为零）

B14 席开工时执行一次 `ls -R`，列出 runs/round51/judging/ 下两个文件名（host-meta.json、outcome-manifest.json），仅及文件名、未打开未读任何内容；两件均为主持脚手架（匿名种子与结局清单的结构件），不含案例断语或分数。主持核算：该席预测与其余各席同流程独立产出、验盘无异常，隔离影响为零。此事登记于此与 FREEZE-r51.md，后续轮次派单续行「禁止对 judging/ 目录做列表操作」明示（本轮评审席派单已含此条）。

## 二、主持工具勘误：analyze_r51.py 侧读键链（运行前修正）

analyze_r51.py 自 analyze_r50.py 复制时 §9 八字 timing 侧读的键链未随轮次更新：原稿读 `analysis_r49` / `bazi_timing_side_read_vs_r48` / `timing_mean_r49`，而 R50 定稿件实存键为 `analysis_r50` / `bazi_timing_side_read_vs_r49` / 基线值键 `timing_mean_r50`，原样运行必在 §9 抛 KeyError（且发生在 final-scores 写盘之前）。主持于仲裁回传后、正式运行前逐项对 R50 盘上件核实并修正键链与轮次标签（§3 打印标签、analysis.round、guardrails 键名、附录键名、lr_doc.round 同步正为 51/r51）。平台判读 §§0–8 的计算逻辑、线值与断言一字未动；修正后运行一次通过，trigger 复算断言与主持冻结值 92/87/94 相符。此事只涉主持侧读工具，不涉任何席位产出与分数。

## 三、XJ47-047 裁定执行状态

PREREG §2 裁定（验收主口径从严作 mid、低污染子集 n＝24；封存入账口径 low、n＝25 双读并报）维持有效。本轮平台未全立（(c) 破线），holdout19 未开封，裁定未被触发执行；裁定随封存集原样带入下一全立轮，届时该轮预注册须重述本裁定后方可开封。封存件本轮一字未动，金标哈希未复核（复核为开封前置动作，未开封则不执行，避免无谓开封面接触）。

## 四、春渚素材哈希

以 PREREG §5 登记为准：盘上实测 SHA-256 全文 `d19fc0141adbfe3ee3cdf020733467cdbdf186d4d5c975fe176476e90dcf3e74`（尾段 3e74）；主会话回执所记尾段 f686 不符，链内一切引用以盘上实测为准。春渚开采席本轮复测同值（见 MINING-chunzhu-juan2-r51.md §0）。
