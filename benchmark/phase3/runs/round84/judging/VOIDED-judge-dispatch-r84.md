# R84 评审首派作废登记（主持派单事故，R76 判例同型）

## 事件

R84 主持首派双视评审 8 席时犯两处派单错误：

1. **提示路径写错**：派单写 `runs/round84/JUDGE-PROMPT.txt`，盘上定本实际在 `runs/round84/prompts/JUDGE-PROMPT-verbatim.txt`（席位自行定位到定本，未致误读）。
2. **附加条收窄定本明文路径（主因）**：冻结评审提示定本明文写定「claims 必须经 host-mapping 回读 predictions/\<case_id\>.json 的 prediction_text 全文逐条核验，不得只看摘要」；主持派单却自加「严禁打开 host-mapping 与 predictions 原件」，与定本直接冲突。评审块 jsonl 的 prediction 四字段本就全为 null（设计如此，预测全文走定本路径回读），席位在禁读条下无从核验，只能记 0。

## 影响与处置

- X3、Y3 两席已按禁读条产出全 0 分件（各 122 行），两席均在回传中明确旗标「证据受限下的记 0、建议重发重评」，未冒充实质评分——席位无责，事故在主持派单。
- 该两件已改名存档：`judgeX-block3-scores.VOIDED-dispatch-defect.jsonl`、`judgeY-block3-scores.VOIDED-dispatch-defect.jsonl`（只增不删，不计入任何聚合）。
- 在跑的 X1、X2、X4、Y2、Y4 五席已由主持关闭止损；其中 X1、X2、X4、Y4 在关闭前已落盘全 0 分件，已一并改名存档（`judgeX-block1/2/4-scores.VOIDED-dispatch-defect.jsonl`、`judgeY-block4-scores.VOIDED-dispatch-defect.jsonl`），不计入任何聚合；Y2 席在禁读条下拒绝臆造评分、未写盘，并明文给出二选一解阻路径，处置正确、特予登记。作废件共 6 件（X1–X4 中 X3 含在内、Y3、Y4；Y1 首派未派出、Y2 未写盘）。
- Y1 席首派时因平台数据库连接池/锁超时三次未派出成功，与本事故无关，含在重派内。
- **全批重派**：8 席按定本明文路径重派——读块 jsonl 取 outcome_record，经 host-mapping.json 解 anon_id→case_id，回读 predictions/\<case_id\>.json 的 prediction_text 全文逐条核验 claims，余口径照定本。派单不再附加任何收窄定本路径的禁读条（host-meta.json、outcome-manifest.json、anon-seed.txt 与评分无关，不读即可，不作禁令式收窄表述之外的额外限制）。

## 判例归档

- 与 R76「自拟隔离条致 974 行伪零分、全批作废重派」同型；R76 后立规矩「派单附加条不得收窄冻结定本明文路径」已在册，本轮主持未遵，照实登记。重派派单已回读定本全文逐条对齐后发出。
