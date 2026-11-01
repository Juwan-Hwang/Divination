# VOID-NOTE — R95 平台评审首派全批作废（主持派单事故，R76 型）

## 事实

- R95 平台评审首派 8 席（judgeX1–X4、judgeY1–Y4）回传分数全数 total＝1（每条 direction 0／claims 0／timing 1）、均分 1.0000、通过 0。八席一致自报：本席 block JSONL 中 prediction 四字段（direction／assertions／timing／summary）全部为 null。
- packet 的 prediction 四字段为 null 系建包定式（build_judge_packets 自 R50 体例以 pred.get(k) 取该四键，本链预测文件字段为 prediction_text／basis，故恒为 null——R92/R93/R94 packet 同形态，盘上可验）。
- operative 评审口径（PREREG-r91 §33 验收面明文、平台面历轮同旨；PREREG-r95 §7 亦明文「claims 核验回读路径照定本与历轮口径随单给出」「派单附加条不得收窄定本明文路径（R76 评审事故判例）」）：**claims 核验须经 host-mapping 回读当轮 predictions/<case_id>.json 之 prediction_text 全文逐条核验**。R92–R94 各轮评审均循此路径评分（R94 席位工作件 judgex4_dump.py／judgey1_work.json 等在案）。

## 事故归因

主持首派派单附加条写有「不许读 predictions 原始文件、answers、金标或任何既有分数文件；不许读 host-mapping/host-meta」，与定本明文回读路径直接冲突，属 R76 型「派单附加条收窄定本明文路径」事故——错在主持派单，不在席位（八席均严格执行派单并诚实自报异常）。

## 处置

- 首派 8 件分数文件全批作废，移存本目录（voided-nullpacket-r95/），不入合并与分析。
- 以全新 8 席按修正派单重派：明文给出回读路径（host-mapping 仅限本席 block 内 anon→case 对位；predictions/<case_id>.json 只读 prediction_text 全文）；其余隔离条只就「不读对象」设限（大师基线/金标/他席分数/输入卡），不改动定本评分材料范围。
- 本事故与处置入 ADDENDUM-r95；平台定稿以重派分数为准。
