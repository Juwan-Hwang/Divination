# R56 评审派单事故与修复（JUDGING-REPAIR-r56）

## 事故

- 本任主持首批评审派单（双视 8 席）所附「冻结评审提示」系据压缩摘要转述，未回 `runs/calib-r17/JUDGE-PROMPT.txt` 盘上原文核对，与定本有三处实质偏差：① 量表被写成单一 0–6 分（定本为 direction／claims／timing 各 0–2、0.5 步进，total 为三项和、pass＝total≥4）；② 输出被写成 `{"anon_id","score","note"}` 写入 scoresX/scoresY 文件（定本为 `{"anon_id","direction","claims","timing","total","pass","reason"}`，承 R55 实件写回 judgeX/judgeY 块文件本身，merge 据此读 total）；③ 漏载定本核心取数路：claims 必须经 host-mapping 回读 `predictions/<case_id>.json` 的 prediction_text 全文逐条核验（评审包行内的 prediction 对象四字段为自 R50 沿袭的历史包形、恒 null，本就不是评分对象）。
- 后果：8 席中 6 席完工、2 席主持止损关闭；完工席因包行无 prediction_text 而按「未报项不给分」全块评 0——该 8 份 scores 文件（scoresX-block1–4、scoresY-block1–4，共 974 行全零）为派单错误产物、**全数作废**，不进入 merge/analyze。评审包行文件（judgeX/judgeY-block*.jsonl）经 git 核对未被任何席改动，冻结（06d8b4a2）不受影响；盲测侧冻结提示经回盘核对与定本一致（仅路径渲染差异），盲测 487 件不受影响。
- 作废件归档：`judging/voided-wrongprompt-r56/`（8 份 scores＋8 份 score_r56_*.py 写盘脚本），只存档不删除。

## 修复

- 评审重派：全新 8 席，派单附 calib-r17 定本逐字（量表、特殊 timing 口径、claims 回读路、输出行形），操作口径承 R55 实件（评分行写回本视本块 judgeX/judgeY-blockK.jsonl，包行原件存于 packet1–4.json 不丢失；carry_note/editor_note 为登记性字段、按其文本处理、不作评分对象本身）。
- 本修复为程序性勘误：平台线值、判读口径、预注册判据均未动；评分量表恢复为自 calib-r17 冻结的定本，与 R55 及此前各轮可比性不受影响。
- 教训（入续跑清单）：派单所附一切「冻结文本」必须在派出前回盘上原文件逐字核对，摘要转述不得作派单源——与 AGENTS「上下文压缩后先读原件再重建」同条。
