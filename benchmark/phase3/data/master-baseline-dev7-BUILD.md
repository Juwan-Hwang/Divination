# master-baseline-dev7 建构记录（2026-10-29）

构成：master-baseline-dev6.json（248 例）＋holdout6 验收混编定稿的大师段（23 例，src=holdout6-acceptance）＋dev-add 63 例新建（expansion6-new 34＋legacy 29）。
dev-add 口径：冻结量表（direction/claims/timing 各 0–2、0.5 步进；断语无应期 timing 记 0、结局无可核时点记 1，均注明），混编无关、双评审独立＋分歧 3 例仲裁（D7B-LY-010/OC-005/OC-013）。逐例分项存 data/dev7-baseline-build/part-new.jsonl；原始评审与仲裁存同目录 judgeA/judgeB/arbitration jsonl。
dev-add 63 例大师均分 3.829；dev7 全集（334 例）大师基线均分 4.585、pass 264/334。
master-baseline-dev7.json 仅存 {total, src}，供 merge_scores.py 配对用。
