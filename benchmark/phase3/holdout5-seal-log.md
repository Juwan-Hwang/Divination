# holdout5 封存日誌

- **組建時間**：2026-10-29T16:50:50+08:00（Asia/Shanghai）
- **組建角色**：數據角（Phase 3 第三輪擴數建池）
- **算法**：僅對 expansion3 新增例中滿足硬要求者抽選——結局 A 級、污染 low、《增刪卜易》原文明記月建與日辰且逐爻裝卦表完整（雙完整性），共 25 例合格；按 sha256("phase3-round3-20261029:"+id) 十六進制升序排序，取前 25 例入 holdout5，其餘合格例與全部不合雙完整性／梗概型新例入 dev-add。劃分明細見 benchmark/phase3/expansion3/BUILD-REPORT.md，落盤即凍結。
- **例數**：holdout5 共 25 例（LY-516、LY-514、LY-522、LY-527、LY-504、LY-502、LY-506、LY-505、LY-512、LY-528、LY-518、LY-517、LY-515、LY-501、LY-519、LY-511、LY-507、LY-520、LY-508、LY-526、LY-509、LY-523、LY-521、LY-510、LY-524）。
- **金標 SHA-256**：`c5c2979a94cd45b7827b7d3887d12a472f1689c9910e419e48967840caad927f`
- **結局封存位置**：benchmark/phase3/holdout5/test_gold.jsonl（同目錄 SEALED.md 註明只許評審角驗收時開封）；holdout5 的盲測 inputs 置於 benchmark/phase3/expansion3/inputs/（與 dev-add 共用同一 inputs 目錄，逐例一檔），不含任何答案字段（核對記錄見 expansion3/BUILD-REPORT.md）。
- **狀態**：**未開封**。自本筆落盤起，holdout5 結局不進入任何給盲測角／修訂角的材料；開封須由評審角於驗收輪在本日誌追加一筆後進行。
