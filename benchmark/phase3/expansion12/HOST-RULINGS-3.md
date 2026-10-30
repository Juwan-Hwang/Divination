# 主持裁定三：CZ 测字 33 例入封资格生效（2026-10-30）

背景：组集席按派单核对发现，expansion12/online-routes/cases.jsonl 中 CZ-001…033 的 `holdout_eligible` 全为 false——原因为抽例时测字断法章节未建、按 CENSUS-PREREG §二.4 只入储备账。CENSUS-REPORT §一已按「章节前置已解除」将 33 例计入可封存供给，但源文件旗标未翻转，两处口径不一致，组集席停手待裁。

主持核查（盘上实证）：
1. 断法章节已建：`benchmark/phase3/method/references/chinese-cezi.md`（261 行，56 条提炼，HOST-RULINGS-2 §二收束合并在案）。
2. SKILL 路由原未接入（method/SKILL.md 选法表与流程节无测字）——常例（PROTOCOL「新体系入池前置断法章节」：章节＋SKILL 路由与流程节接入，两者俱备才许入盲测轮次）尚差此一环；主持已于本裁定同日补齐：选法表增测字一条、各占法流程增「测字」一条，均指向 chinese-cezi.md（method/ 改动在 R33 冻结快照之前完成，R33 预注册中声明）。

裁定：**CZ-001…033 入封资格自本裁定起生效**（A 16＋A-low 17、全 low、双全，分级以 online-routes/CENSUS-NOTES.md 与 cases.jsonl 原记录为准）。源文件 cases.jsonl 原件不回改（旗标 false 系抽例时点的真实状态，留作历史）；后续组集/建池以本裁定＋CENSUS-REPORT §一为资格准据。组集按原派单规则（N=33、k=8、系统抽样）续行。
