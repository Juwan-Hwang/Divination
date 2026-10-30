# R37 判语卫生（评审侧）剥离日志（PREREG §6）

- 底本：runs/round36/judging/outcome-manifest.json（487 例，overlay 16 条已生效、构建前后逐字自验 16/16）。
- 规格：data-verify/strip-spec_r37.json（数据角制备，79 子串全部唯一命中自验）；执行脚本 build_outcome_manifest_r37.py（机械执行，逐例断言子串恰命中一次、残余非空）。
- 结果：72 例全数处置——机械剥离 71 例＋主持裁决 1 例；与 overlay 16 条交集为空集（无先后冲突例）。
- 剥离内容存于新 manifest 的 stripped_tail 字段（judging/outcome-manifest.json），原结局文字除剥离子串外一字未动；既有各轮分数不回改。

## 主持裁决：LR2-024（规格 ESCALATE 件）

- 底本全文：「已而果然。原文以「已而果然」承「七月必死」之断（应验句紧承断语末句、所指唯一），七月死期为本课结局。」
- 裁决：执行规格候选子句剥离——剥子串「原文以「已而果然」承「七月必死」之断（应验句紧承断语末句、所指唯一），」，残余「已而果然。七月死期为本课结局。」
- 理由：整句剥离后残余仅「已而果然。」——本身即无事件内容的裁决短承，判语污染更甚且结局记录被毁；候选剥离已去除预判对应关系的元注记主体（承断语/所指唯一的对应性断言），残余中「为本课结局」属出处结构陈述、非相合裁决，事件（七月死期）保全优先。此为例外裁决，仅此一例，后续轮次同型例须先经预注册或数据角审计口径处理，不援引本裁决为通例。

## 逐例登记

| 例 | 型 | 处置 | 剥离字数 |
|---|---|---|---|
| AS-002 | A(a) | stripped | 48 |
| AS-015 | A(a) | stripped | 44 |
| AS-204 | A(a) | stripped | 18 |
| AS-211 | A(a) | stripped | 69 |
| AS-302 | A(a) | stripped | 32 |
| AS-305 | A(a) | stripped | 13 |
| BQ-001 | A(a) | stripped | 49 |
| BZ-021 | A(a) | stripped | 58 |
| BZ-022 | A(a) | stripped | 31 |
| BZ-023 | A(a) | stripped | 17 |
| BZ-024 | A(a) | stripped | 14 |
| BZ-026 | A(a) | stripped | 7 |
| BZ-028 | A(a) | stripped | 20 |
| BZ-031 | A(a) | stripped | 51 |
| BZ-032 | A(a) | stripped | 11 |
| BZ-033 | A(a) | stripped | 14 |
| BZ-034 | A(a) | stripped | 17 |
| BZ-037 | A(a) | stripped | 8 |
| BZ-038 | A(a) | stripped | 7 |
| BZ-039 | A(a) | stripped | 7 |
| BZ-040 | A(a) | stripped | 41 |
| BZ-104 | A(a) | stripped | 9 |
| BZ-302 | A(a) | stripped | 9 |
| BZ-303 | A(a) | stripped | 45 |
| LR2-013 | A(b) | stripped | 22 |
| LR2-014 | A(b) | stripped | 16 |
| LR2-015 | A(b) | stripped | 18 |
| LR2-016 | A(a) | stripped | 14 |
| LR2-017 | A(b) | stripped | 17 |
| LR2-018 | A(b) | stripped | 42 |
| LR2-019 | A(a) | stripped | 19 |
| LR2-020 | A(a) | stripped | 76 |
| LR2-021 | A(b) | stripped | 26 |
| LR2-022 | A(b) | stripped | 25 |
| LR2-023 | A(b) | stripped | 27 |
| LR2-024 | A(b) | host-ruling-candidate-strip | 35 |
| LR3-002 | A(a) | stripped | 54 |
| LR3-004 | A(b) | stripped | 38 |
| LR3-006 | A(b) | stripped | 34 |
| LR3-008 | A(b) | stripped | 45 |
| LR3-010 | A(a) | stripped | 34 |
| LR3-101 | A(a) | stripped | 41 |
| LR3-104 | A(a) | stripped | 23 |
| LR3-107 | A(b) | stripped | 48 |
| LR3-110 | A(a) | stripped | 50 |
| LR3-114 | A(a) | stripped | 52 |
| LR3-116 | A(a) | stripped | 65 |
| MH-001 | A(b) | stripped | 25 |
| OC-001 | A(a) | stripped | 36 |
| OC-004 | A(a) | stripped | 13 |
| OC-006 | A(a) | stripped | 19 |
| OC-007 | A(a) | stripped | 16 |
| OC-008 | A(a) | stripped | 18 |
| OC-010 | A(a) | stripped | 41 |
| OC-012 | A(a) | stripped | 10 |
| OC-013 | A(a) | stripped | 24 |
| OC-015 | A(a) | stripped | 57 |
| OC-016 | A(a) | stripped | 22 |
| OC-017 | A(a) | stripped | 13 |
| OC-018 | A(a) | stripped | 28 |
| OC-019 | A(a) | stripped | 13 |
| OC-020 | A(a) | stripped | 13 |
| OC-021 | A(a) | stripped | 23 |
| OC-022 | A(a) | stripped | 21 |
| OC-023 | A(a) | stripped | 70 |
| OC-024 | A(b) | stripped | 18 |
| OC-025 | A(a) | stripped | 6 |
| OC-026 | A(b) | stripped | 14 |
| OC-027 | A(b) | stripped | 10 |
| OC-028 | A(b) | stripped | 10 |
| OC-029 | A(b) | stripped | 12 |
| OC-030 | A(b) | stripped | 25 |
