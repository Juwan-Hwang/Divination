# SEALED — holdout7 測試集金標（未開封）

- 封存時間：2026-10-29T19:34:13+08:00（Asia/Shanghai）
- 來源輪次：Phase 3 第五輪擴數（expansion5），新例 LY-701
- 例數：1（合格池 {A 級 ∩ low ∩ 雙完整} 共 1 例，遠不足目標 20–25，如實全取、未放寬標準；
  按 sha256("phase3-round5-20261029:<id>") 十六進制升序取序——合格池全數入選）
- 金標文件：benchmark/phase3/holdout7/test_gold.jsonl
- 金標 SHA-256：1f0b05cf02608eb2542fa5040b35e71cec21164e1a9569e3acd529013030f3c9
- 盲測 inputs：benchmark/phase3/expansion5/inputs/（LY-7xx 逐例一檔）
- 狀態：**未開封**。開封須按 PROTOCOL 預註冊後由評分角執行，並在本文件與
  benchmark/phase3/holdout7-seal-log.md 追加開封記錄。
- 紀律：數據角、修訂角不得讀取 test_gold.jsonl 內容。
- 注意：本集僅 1 例，統計功效近乎為零；是否用作留出驗收由主持角裁斷（見 expansion5/BUILD-REPORT.md 缺口說明）。
