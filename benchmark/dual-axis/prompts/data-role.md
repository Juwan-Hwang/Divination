# 数据角任务原文（双轴补评·结局可得性分级）

你是 MastersDivination Benchmark「双轴补评」的数据角。角色纪律：你只做结局可得性分级，不作断、不评分、不看任何一轮的预测与分数。

## 背景
本基准原只有一轴评分（与大师原断的一致性）。现新增第二轴「实际应验轴」：预测与案例记录的客观结局的吻合度。轴二的最大风险是拿大师自述充当独立现实标签，所以评审之前必须先由你逐例分级：只有结局有独立客观记录的案例（A 级）才允许评轴二。

## 输入（只许读这两个文件）
- ~/workspace/divination/masters-dataset/data/dev.jsonl（94 例）
- ~/workspace/divination/masters-dataset/holdout/test_gold.jsonl（41 例）
每例含：id、master_predictions（大师断语）、outcome（description + verified_by）、notes 等。

严禁读：benchmark/runs/ 下任何 predictions/、judging/、final-scores（防分级被分数污染）；严禁用你自己的记忆或外部知识替案例补结局——分级只依据条目内 outcome 字段与 verified_by 字段所载的记录形态。

## 分级标准（已预注册，照此执行）
- **A 级**：结局有独立于大师断语的客观记录——
  (a) 史实或带时间戳的公开事件结果（选举官方结果、公开新闻记录、机构批准记录、公开史实等，verified_by 指向条目之外的公开记录）；或
  (b) 案例原文明确记载的实际结果，且与断语文本可分离：即 outcome.description 记载的是具体事件经过（何时、发生了什么、数额/结果如何、求测者实际反馈的事件），其真假不依赖于接受大师的断语或其解释框架。
- **B 级**：结局只有大师（或编集者）自述、或纯书内结局，与大师断语不可分离——例如：outcome 内容本质上是大师自己的命格评语/断语复述（「贵至二品、富有百万」式原注自载而无任何独立事件记录）、只有「果然应验」式断语而无具体事件经过、条目自标 book_internal_only、无结局记载者。
- 拿不准的**从严归 B**，并在理由中标注「从严归 B」。

注意区分：同出于一本书，不自动等于 B——若书中把「后来实际发生了什么」作为独立事件段落记载（有日期、经过、结果），那是 (b) 类 A 级；若所谓结局只是大师/编者在断语里对命主一生的评定本身、或编者一句「验」而无事件，那就是 B。逐例按 outcome 文本的实际形态判，不要按书名一刀切。

## 产出（落盘 + 校验才算交付）
1. ~/workspace/divination/benchmark/dual-axis/grading/outcome-availability.jsonl：135 行，每行一个 JSON：{"id": "...", "grade": "A"|"B", "outcome_record": "<A 级必填：把 outcome.description 原文照录（可节录至足以核对应验的完整程度，不得改写、不得掺入大师断语）；B 级留空字符串>", "verified_by": "<照录>", "reason": "<一至两句分级理由>"}。
2. ~/workspace/divination/benchmark/dual-axis/grading/GRADING-NOTES.md：分级口径执行说明、A/B 计数（按 dev/test 与按 id 前缀体系各一份小计）、从严归 B 的案例清单、你拿不准的边界案例清单及你的处置。
3. 自行用脚本校验：135 行逐行可解析、id 与两个输入文件的并集恰好相等、无重复。

回传：A/B 总数、dev/test 各自 A 级数、从严归 B 例数、边界案例一句话清单。
