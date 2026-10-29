# master-baseline-dev8 建构记录（2026-10-29）

构成：master-baseline-dev7.json（334 例，原样）＋holdout8 验收混编定稿的大师段（28 例，src=holdout8-acceptance，取 holdout8-acceptance/judging/final-scores.json 的 pairs.master.total）＋expansion7 dev-add 50 例新建（src=dev8-baseline-build）。
dev-add 口径：冻结量表（direction/claims/timing 各 0–2、0.5 步进；断语无应期 timing 记 0、结局无可核时点记 1，均注明），双评审独立（A 席均分 5.26、pass 49/50；B 席均分 5.22、pass 47/50）＋分歧 2 例仲裁（D8B-015/YY-022、D8B-048/YY-023：pass 不一致触发；两例 outcome 均为「后果然」总括，仲裁采 B 席读法——未被结局逐条记载的子断语不得给满分，claims 1.5、total 3.5）。非分歧例取双评审分项均值，分歧例以仲裁分为定稿。逐例分项存 data/dev8-baseline-build/part-new.jsonl；原始评审与仲裁存同目录 judgeA/judgeB/arbitration jsonl、disputes.json、arbitration-packet.json。
dev-add 50 例大师均分 5.230、pass 47/50；holdout8 段大师均分 4.036、pass 19/28；dev8 全集（412 例）大师基线均分 4.626、pass 330/412。
master-baseline-dev8.json 仅存 {total, src}，供 merge_scores.py 配对用。
