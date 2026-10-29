# holdout3 封存日誌

- **組建時間**：2026-10-29T12:37+08:00（Asia/Shanghai）
- **組建角色**：數據角（Phase 3 建池）
- **算法**：僅對 92 例新 A 級案例按 tradition × contamination 分層，層內按 sha256("phase3-20261029:"+id) 十六進制升序，每 10 例取第 3、6、9 位入 holdout3；劃分詳見 benchmark/phase3/data/splits3-summary.md 與 benchmark/phase3/splits3.json，落盤即凍結。
- **例數**：holdout3 共 27 例（AS-201、AS-202、AS-203、AS-214、LY-201、LY-209、LY-213、LY-214、LY-223、LY-224、LY-225、LY-226、LY-229、LY-233、LY-236、LY-238、LY-239、LY-247、LY-248、LY-256、LY-257、LY-258、LY-308、LY-310、LY-313、LY-316、LY-317）。
- **結局封存位置**：benchmark/phase3/holdout3/test_gold.jsonl（同目錄 SEALED.md 注明只許評審角驗收時開封）；holdout3 的盲測 inputs 單獨置於 benchmark/phase3/holdout3-inputs/，不含任何答案字段（核對記錄 benchmark/phase3/data/input-check.txt）。
- **狀態**：**未開封**。自本筆落盤起，holdout3 結局不進入任何給盲測角／修訂角的材料；開封須由評審角於驗收輪在本日誌追加一筆後進行。
- 2026-10-29 输入面清理（未开封）：holdout3 的 27 个 inputs 中 17 例 substantive 泄漏已按 LEAK-CLEANUP-ERRATA 清理（只改 inputs 侧事实叙事、删断语内容）；金标 test_gold.jsonl 清理前后 SHA-256 核对一致、一字未动。本日志所记封存状态不变：结局仍未开封。
