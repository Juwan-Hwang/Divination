# R44 派单记录（主持自记；体例承 R43）

## 前置（主持自办，数据议程）

- 数据议程四项由主持自办并落 data-verify/DATA-AGENDA-R44.md（核账脚本 account_reviewed_r44.py、reconcile_by_r44.py）：① 账外待核库存 110 行（BY/YX 107＋LR3 3）定性待对勘、不计供给，natal 未用 72 行 eligible 全 False 关闭；② LY-436 回源裁定旗标不成立；③ incoming/Book.7z 与第一批解压 20 件全等、无新增；④ 卷五回叶对勘 0/55 触发型顺延。预注册检查点 a0d1e965。

## 平台盲测 25 席（批次沿 R43 batches.json 逐字，487 例）

提示结构承 R43 定式（kb 路径白名单＝runs/round44/kb-snapshot、路径写全 benchmark/phase3/ 前缀、trigger 三布尔原文＋主持注记随单附、回传格式）；B05 条款：回传不作落盘证据，冻结前主持逐批按 batches.json id 清单验盘，缺件全新席补测、复验全过才许冻结。

- B01 79f8ffa3（20）｜B02 e2a1721f（20）｜B03 dc4a7f4d（20）｜B04 cbfaf169（20）｜B05 d138e8b7（20）
- B06 10e4335c（20）｜B07 9ed50c1e（20）｜B08 2ce79988（20）｜B09 ddf82b7d（20）｜B10 a1dd25ab（20）
- B11 1c1c84ff（20）｜B12 4f575219（20）｜B13 2e24144f（20）｜B14 c30c1376（20）｜B15 7de9076a（20）
- B16 21178eac（20）｜B17 b9570d63（20）｜B18 18e06ad8（20）｜B19 4b25cab6（20）｜B20 d31a4514（20）
- B21 a457f6d0（启动期数据库错误未执行）→ 补测 15400d1e（20）｜B22 a751d1bd（20）｜B23 67a7f9a8（20）｜B24 c0d0914b（20）｜B25 9dc5157f（7）

25/25 批回传、逐批自验全过。主持验盘（verify_predictions_host_r44.py）：487/487 落盘、missing 0、bad 0、trigger 终校 changed_main 53／reserve_used 57／disputed 75（R43 为 62/49/100；trigger 语义无成文定义，计数差异只作附读、不作方法信号）。

写位自纠专项复核（冻结前主持执行）：B25 席自报 ZY-002 内容一度误写 ZY-003 文件名下、ZY-004 人名字形一度写错，均自纠重写；主持复核三件内容与各自 inputs-dev12 输入对位（ZY-002＝屯初九毕万建侯、ZY-003＝艮穆姜东宫、ZY-004＝屯之比立元孙圉），对位属实、三件以正确内容冻结。本轮无 B05 型缺件事件（B21 首席启动失败系基础设施错误、未执行任何工作，补测席全新接单，不构成内容事件）。

冻结：本提交、标签 phase3-round44-blind-frozen。outcome-manifest 由 build_outcome_manifest_r44.py 生成（487 键集与 R43 全等、overlay 16/16 逐字合并、承 R43 manifest outcomes 逐字）；评审包由 build_judge_packets_r44.py 生成（anon 种子 20261045；块 [122,122,122,121]；host-meta 承 R43 验键集）。
