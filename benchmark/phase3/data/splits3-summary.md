# Phase 3 splits3 劃分匯總（數據角，落盤即凍結）

算法（嚴格按任務書執行）：僅對 92 例新 A 級案例劃分——按 tradition × contamination 分層，層內按 sha256("phase3-20261029:"+id) 十六進制升序排序，每 10 例取排序後第 3、6、9 位入 holdout3（約 30%），其餘入 dev-add；層內不足 3 例全入 dev-add。dev3 = dev2 76 例（照 splits2.json 的 dev2 清單）+ dev-add。

新案例池：三路擴數共 94 例，其中 A 級 92 例入池；**B 級 LY-302、LY-303（《卜筮正宗》路，應驗與斷語同句／僅「後果驗」自述、不可分離）已排除**，不入 roster3、不入任何 split。

| tradition | contamination | n（新A級） | dev-add | holdout3 |
|---|---|---|---|---|
| horary | high | 5 | 4 | 1 |
| horary | low | 10 | 7 | 3 |
| liuyao | low | 77 | 54 | 23 |
| **合計（新）** |  | **92** | **65** | **27** |

新 A 級分體系：liuyao 77、horary 15；分污染：low 87、high 5；timing_explicit=true 84 例。

## 總數

- dev3：141 例（dev2 沿用 76 + dev-add 65）；分體系（含 dev2 沿用例，按 phase2 roster 的 tradition 計）：{'astrology': 3, 'bazi': 21, 'fengshui': 2, 'horary': 21, 'liuren': 1, 'liuyao': 82, 'meihua': 6, 'vedic-astrology': 2, 'yijing': 3}
- holdout3：27 例（目標 25–35，達標）；分體系：{'horary': 4, 'liuyao': 23}；分污染：{'high': 1, 'low': 26}
- dev-add 分體系：{'horary': 11, 'liuyao': 54}；分污染：{'low': 61, 'high': 4}

## holdout3 清單

AS-201、AS-202、AS-203、AS-214、LY-201、LY-209、LY-213、LY-214、LY-223、LY-224、LY-225、LY-226、LY-229、LY-233、LY-236、LY-238、LY-239、LY-247、LY-248、LY-256、LY-257、LY-258、LY-308、LY-310、LY-313、LY-316、LY-317

## dev-add 清單

AS-204、AS-205、AS-206、AS-207、AS-208、AS-209、AS-210、AS-211、AS-212、AS-213、AS-215、LY-202、LY-203、LY-204、LY-205、LY-206、LY-207、LY-208、LY-210、LY-211、LY-212、LY-215、LY-216、LY-217、LY-218、LY-219、LY-220、LY-221、LY-222、LY-227、LY-228、LY-230、LY-231、LY-232、LY-234、LY-235、LY-237、LY-240、LY-241、LY-242、LY-243、LY-244、LY-245、LY-246、LY-249、LY-250、LY-251、LY-252、LY-253、LY-254、LY-255、LY-259、LY-301、LY-304、LY-305、LY-306、LY-307、LY-309、LY-311、LY-312、LY-314、LY-315、LY-318、LY-319、LY-320

備註：Lilly 路 GRADING.md 無應驗時點欄，roster3 的 timing_explicit 按 answers 的 outcome 原文是否載有具體日期／相對日／bounded 窗口判定（逐例依據存建池腳本 LILLY_TIMING 表）；其餘兩路照 GRADING.md 逐例欄位。
