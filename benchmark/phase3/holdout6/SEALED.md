# SEALED — holdout6 測試集金標（未開封）

- 封存時間：2026-10-29T18:34:19+08:00（Asia/Shanghai）
- 來源輪次：Phase 3 第四輪擴數（expansion4），新例 LY-601–LY-629
- 例數：23（合格池 {A 級 ∩ low ∩ 雙完整} 共 23 例，不足 25，如實全取、未放寬標準；
  按 sha256("phase3-round4-20261029:<id>") 十六進制升序取序——合格池全數入選）
- 金標文件：benchmark/phase3/holdout6/test_gold.jsonl
- 金標 SHA-256：f0efd8a947e00714cfea169ea78d7600dba9bb7ad0dcd2beb2d35f9b1ad0417a
- 盲測 inputs：benchmark/phase3/expansion4/inputs/（LY-6xx 逐例一檔）
- 狀態：**未開封**。開封須按 PROTOCOL 預註冊後由評分角執行，並在本文件與
  benchmark/phase3/holdout6-seal-log.md 追加開封記錄。
- 紀律：數據角、修訂角不得讀取 test_gold.jsonl 內容。
