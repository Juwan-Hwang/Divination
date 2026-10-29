任务：担任 MastersDivination Benchmark Phase 2 Round 3 的修订角，执行「回滚验证」修订。工作区 ~/workspace/divination/。严禁查阅任何单例结局/分数/逐例评审材料（runs/*/judging、final-scores.json、roster.jsonl 不许读）。

背景（聚合口径）：Round 2 的 14 项修订（登记在 benchmark/phase2/runs/round2/revision-diff.md）整轮为阴性：总分 −1.8pp，其中六爻应期项不升反降（0.93→0.84），而断语项上升（1.25→1.43）。主持判定：应期「硬序查表」是净负组件；终局单判（通则 l）与对象对齐复述保留。

你要做的（只改 benchmark/phase2/method/）：
1. 撤销硬序：把 SKILL.md 通则（h）③的六爻硬序覆盖句、references/chinese-liuyao-meihua.md「应期三步」第 3 步的硬序表与多状态查表序，恢复为 Round 1 时的条文。Round 1 原文可从 git 取：`git show phase2-round1:benchmark/phase2/method/SKILL.md` 与 `git show phase2-round1:benchmark/phase2/method/references/chinese-liuyao-meihua.md`（只许用这两个命令取方法旧文，不许看其他历史材料）。恢复口径：应期仍走「定档—三路候选—取一舍二并留痕」，主坐标只许一条（保留 R2 的单坐标承诺表述中不依赖硬序的部分：备选只入 reasoning 并注明舍弃理由），但取舍依据恢复为算者按用神状态综合判断并写明理由，不再查表定序。梅花通则句中与硬序绑定的表述同步恢复。
2. 保留不动：通则（l）事件型终局单判、通则（f）/对象对齐表的对象复述条、其余 R2 改动中与硬序无关者。
3. 逐项登记到 benchmark/phase2/runs/round3/revision-diff.md：撤销了哪些条文（对照 R2 登记编号）、恢复后的条文要旨、保留项清单、以及用 `git diff` 自核「method/ 相对 phase2-round2 标签的差异只含本次撤销」的结论。

交付回传：撤销项清单、保留项清单、自核结论。除 method/ 与 revision-diff.md 外不许改任何文件。
