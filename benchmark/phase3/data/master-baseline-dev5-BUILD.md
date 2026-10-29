# master-baseline-dev5 建构记录（2026-10-29）

构成：dev4 基线（benchmark/phase3/data/master-baseline-dev4.json）限于 dev5∩dev4 的 199 例（排除 LY-412），加 expansion3 新增 18 例（LY-503、513、525、529–543）由独立基线建构角新建。
新 18 例口径：与 master-baseline-dev4-BUILD.md 的新例口径同源——轴二量表（direction/claims/timing 各 0–2、0.5 步进）；断语无任何应期信息 timing 记 0 并注明；断语有应期但结局无可核时点记 1 并注明。逐例分项与依据存 master-baseline-dev5-part-new.jsonl。
新 18 例结果：大师均分 4.111（pass 14/18），分项 direction 1.889 / claims 1.833 / timing 0.389（14 例 timing 记 0，其中 13 例为断语本体无应期信息）。
dev5 全集大师基线：n=217，均分 4.915，pass 191/217。
文件：master-baseline-dev5.json 仅存 {total, src}（与 dev4 基线同构，供 merge_scores.py 配对用）；新例分项细节以 part-new.jsonl 为准。
