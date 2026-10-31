# METHOD-INTEGRATION-r78 · R78-REV1 集成记录（主持验合）

- 提案：runs/round78/diagnosis/REVISION-PROPOSAL-r78.md；闸门：runs/round78/diagnosis/REV-GATE-r78.md（五项全过）；集成席：独立席位执行、回传后主持逐路径实查代记（承 R74 判例）。
- 集成内容（只增并列）：
  1. `references/calibration.md` 末尾新增第七节「主断方向双路对决前置裁决（R78 干预 R78-REV1）」（R78-REV1-1～-6），逐字自提案 §2.1 草案经文件间复制路径落盘。
  2. `SKILL.md` 作断通则 (n) 后新增 (o) 指针一行，逐字自提案 §2.2。
- 哈希（盘上实测全文）：calibration 改前 0bdafabcdb0cbb6012cb2c3b4ee20b0bb67e30e34c95a929853df56c6ddb6402（21,225 字节）→ 改后 a0858ca4c51a73bd4760b10e6ab761e7b810c05864958bd88a60e82cd468d691（25,223 字节）；SKILL 改前 b8901a1ad9880fb2fb24434757da68825b893227618113f66468b3f6dbb02cc0（39,905 字节）→ 改后 bd3550b5196a532368e9500d4a2d374e49bb71e8e1d13248e11f60c69bbdd63（40,076 字节）。活文件 SHA 与集成席回传逐一全等。
- 主持验合：活 method 与 runs/round78/kb-snapshot 逐件比对，差异恰为上述两文件；SKILL diff 恰增 (o) 一行、删 0 行；calibration diff 增 32 行、删 0 行且为纯后缀追加（快照为活文件前缀）；strip-back（删第七节／删 (o) 行）逐字还原快照；余 19 文件全等。
- 效力：自 R79 起算。判读口径以提案 §3 写死值（判读集最早 holdout24、N≥20；主线 DIR 率 ≤0.100；副线 TIM＋CLAIM ≤0.370；护栏总差 ≥−1.837、OMIT ≤0.160；证伪 DIR ≥0.340 或总差 ≤−2.193；附读三位）。
- 锚定关系：holdout23 快照（runs/round78/kb-snapshot-holdout23）于集成前封存，不含第七节；R79 平台快照将含第七节。
