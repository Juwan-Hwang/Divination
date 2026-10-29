# schema.json 的 id 正则修订建议（Round 18 数据角旁线，2026-10-29，只登记不擅改）

- 边界：本文件只提建议，**未修改 masters-dataset/schema.json**；采纳与否、采用哪一版，等主持角与主会话裁定。采纳时请同步 SCHEMA.md 第 10 行的 id 前缀说明表（文案与规则同改的既有规矩）。

## 1. 现状

masters-dataset/schema.json 中 `id` 字段现行定义：

```json
"id": {"pattern": "^(LY|MH|ZY|BZ|ZW|TR|AS|RN|NM|QM|LR)-[0-9]{2,}$", "type": "string"}
```

即：仅允许「白名单大写双字母前缀 + 连字符 + 至少 2 位数字」一种形态。

## 2. 全库盘点（2026-10-29 实测）

扫描 masters-dataset 全部 jsonl（chinese-divination、chinese-natal、western、modern-masters 四个源卷的 inputs/answers，及 data/dev.jsonl、data/test_inputs.jsonl、holdout/test_gold.jsonl），共 **205 个 distinct id，其中 72 个不匹配现行正则**，不匹配的全是已入集的真实条目，不是假想形态：

| 形态 | 例 | 数量（distinct） | 所在文件 |
|---|---|---|---|
| 西方卷描述性 slug（小写、多段、含年份与单词） | `lilly-nativity-1616-merchant`、`lilly-horary-1634-purchase-houses` 等 | 16 | western/inputs.jsonl、answers.jsonl；其中 `lilly-nativity-1616-merchant` 已入 data/test_inputs.jsonl 与 holdout/test_gold.jsonl（即 test 集，且在 Round 18 inputs 中） |
| 中方命理卷小写词干 + 3 位数字 | `wei-023`、`ren-001`、`xu-001`、`ziwei-001`、`sanming-001` | 46（wei 23、ren 16、xu 3、ziwei 3、sanming 1） | chinese-natal/inputs.jsonl、answers.jsonl；其中 `wei-023` 已入 data/dev.jsonl |
| 现代大师卷单字母 + 2 位数字、无连字符 | `C01`…`C10` | 10 | modern-masters/inputs.jsonl、answers.jsonl |
| 大写前缀 + 数字（现行形态） | `LY-018`、`BZ-041`、`AS-303` 等 | 133 | 各卷及池文件 |

补充两点盘点事实：

- **数字位数不是问题**：短 id `LY-01`、`LY-03`（早期 seed 例，见 data/dev.jsonl 与 data/test_inputs.jsonl；与 `LY-001`、`LY-003` 是**不同条目**，如 LY-01 为「候文書，何日得領？」source_id 作 `seed:LY-01`，LY-001 为「占將來有官否」）与三位 id 并存，但现行 `[0-9]{2,}` 对 2 位、3 位都放行，二者均合规。修订时**不可收紧为恰好 3 位**，否则会误伤 LY-01/LY-03 这类既有 id。
- 现行白名单中 TR、RN、NM、QM 四个前缀目前全库无实际 id（SCHEMA.md 第 10 行有卷别定义），属预留，不建议因此删除。
- modern-masters/predictions.jsonl 另有 `P01`…`P12`，那是预测文件自身的编号、非案例 id，未计入上表；是否纳入 schema 适用范围，请主持角一并裁定（见第 4 节待决项）。

## 3. 现正则为何不匹配（逐因）

1. **前缀白名单写死且仅大写双字母**：`lilly-`、`ren-`、`wei-`、`xu-`、`ziwei-`、`sanming-` 这些已入集词干不在名单内，且为小写，`[A-Z]` 口径下永不命中。
2. **尾段限定纯数字**：slug 形态尾段含英文单词与四位年份（如 `-1616-merchant`），`-[0-9]{2,}$` 无法覆盖。
3. **强制连字符**：`C01` 类无连字符形态被排除。
4. 后果是当下的、非理论的：对 data/test_inputs.jsonl、data/dev.jsonl 跑 schema 校验，现在就会在已入池的真实条目（`lilly-nativity-1616-merchant`、`wei-023`）上报错。

## 4. 建议正则（方案 A，推荐）

按已入集的四种形态做锚定 alternation，各形态内部仍保持严格，不放宽到「任意字符串」：

```
^(?:(?:LY|MH|ZY|BZ|ZW|TR|AS|RN|NM|QM|LR)-[0-9]{2,}|(?:ren|wei|xu|ziwei|sanming)-[0-9]{3}|C[0-9]{2}|lilly-[a-z0-9]+(?:-[a-z0-9]+)+)$
```

- 已实测：全库 205 个 distinct 案例 id **全部通过**；反例 `LY-1`、`XX-001`、`ren-01`、`C123`、`lilly-`、`ly-001` 等均被拒。
- 影响面：**不需要改名任何既有 id**，splits.json 的键、各轮 inputs 文件名、dev/test 池均不受影响；改后对四源卷与三个池文件做全量校验应零报错。
- 日后新增卷别词干时，往 alternation 里加一支即可，形态边界保持显式可审。

被否方案（方案 B，仅记录）：把正则放宽为通式 `^[A-Za-z][A-Za-z0-9]*(-[A-Za-z0-9]+)*$`。虽一劳永逸，但等于放弃 id 形态校验（错拼前缀、异形编号都放行），与「编号一经发布不得复用/更改」的稳定性要求相悖，不推荐。

待决项（请主持角裁定）：modern-masters/predictions.jsonl 的 `P01`…`P12` 若也被视为应受 schema 约束的 id，需在方案 A 中再加一支 `P[0-9]{2}`；若其定位是预测文件内部序号，则维持范围外，并在 SCHEMA.md 注明 schema 只管案例 id。

## 5. 采纳时的同步项（建议）

1. schema.json 按方案 A 替换 `id.pattern`（本文件不执行）；
2. SCHEMA.md 第 10 行 id 说明补登已入集词干：`ren-`、`wei-`、`xu-`、`ziwei-`、`sanming-`（中方命理卷来源词干）、`C`（现代大师卷）、`lilly-`（西方卷 Lilly 描述性 slug），并注明 LY 卷内 2 位 seed id（LY-01/LY-03）与 3 位 id 并存、不得互改；
3. 改后跑一次全库校验（四源卷 inputs/answers + dev/test_inputs/test_gold 共 205 个 distinct id）留痕，再行发布。

—— 数据角（Round 18 旁线），2026-10-29。本文件只增不改；本轮未修改 schema.json 及任何既有数据文件。
