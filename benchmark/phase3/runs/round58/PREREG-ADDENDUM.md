# R58 PREREG 附则：holdout21 选集（验收未达标后续链，2026-10-31 主持写定）

触发：holdout20 验收未达标（三判据全不立），按 PREREG §2 续链；holdout21 构成经 QM 复核补足（非六爻 14 ≥13），按本附则组集封存。选集在本附则写定后由数据席执行，轮内不改。

## 一、选集（T＝25，id 写死）

| 段 | ids | 台账 |
|---|---|---|
| 六爻《六爻卦例说真》 | GSZ-003、GSZ-005、GSZ-009、GSZ-015、GSZ-016、GSZ-017 | runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json |
| 六爻《分类占验技法》二轮 | WHY-072、WHY-073、WHY-074、WHY-075、WHY-078、WHY-079 | runs/round57/digestion/SUPPLY-MINING-wanghuying-r57-r2.json |
| 八字《详批命例精解》 | QW-013、QW-014、QW-015、QW-016、QW-017 | runs/round56/digestion/SUPPLY-MINING-quwei-r56.json（断语经补录件，见 §二） |
| 奇门（杜新会 5＋张志春 3） | QM-001、QM-002、QM-003、QM-004、QM-005、QM-006、QM-007、QM-008 | runs/round56/digestion/SUPPLY-MINING-qimen-r56.json＋runs/round58/digestion/QM-REVIEW-r58.json |

构成复核：六爻 12（48%）／八字 5／奇门 8；非六爻 13；非夷坚 25；单源 ≤6（GSZ 6、WHY 二轮 6、QW 5、QM-杜 5、QM-张 3）；全例 A 级、contamination＝low、锚点在场（QM 经 R58 复核四要件全过；余段 eligible 时已验）。

## 二、QW 断语补录（建集前置，照 holdout20 封存日志 §六先例）

QW 台账无 master_prediction 逐字字段。补录席自源 TXT（incoming/wanted-books-4/详批命例精解_曲炜.txt）按台账 source_ref 定位 QW-013–017 逐例提取作者断语逐字，写 data/holdout21-gold-supplement.md（每条：id、断语逐字、出处行号区间、结局逐字）；任一例断语无法逐字定位 → 回报主持，主持按 QW-018 起顺位替补并在本附则追加替补注记后方可建集。

## 三、建集与验封口径（同 holdout20 定式）

- 资格断言：25 例须在各自台账/QM 复核件中为 eligible（A 级、low、锚点在场、master_prediction 逐字非空——QW 以补录件为准）；与已用 id 全集（dev 池＋holdout2–20＋各 gold）脚本复核零复用。
- 转录规格 v1（同前）：input_side 只含 question/background/chart_anchor（＋八字例 birth 四元组与 sex），禁混 outcome/master_prediction/断语类字段；金标 test_gold.jsonl 含 master_prediction＋outcome＋contamination_grade＋grade＋provenance＋license_status＋redistributable。
- 断语扫描三道：① input_side 逐字子串扫描（断语与结局）；② 语义级抽查 ≥8 例；③ 主持独立复扫。
- 金标 SHA-256 落盘双读一致；封存日志 data/holdout21-seal-log.md（构成、扫描结果、SHA、开封条件）。
- 开封条件（写死）：封存后首个平台全立轮开封，验收快照锚定**封存时点**活 method（建集时由数据席复制 benchmark/phase3/method 至 runs/round58/kb-snapshot-holdout21/ 并在封存日志登记文件清单与逐文件 SHA 摘要）。

## 四、其余

- 选集外合格库存（QM-010、GSZ/WHY/QW 余例等）保留待后续集调用，不预占。
- 本附则不改动 PREREG 本体任何口径；验收判据仍照 R42 PREREG §8。
