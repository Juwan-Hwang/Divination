# master-baseline-dev9 建构记录（2026-10-30）

构成：master-baseline-dev8.json（412 例，原样）＋dev9 新增 75 例新建（src=dev9-baseline-build，易冒 56＋断易天机 7＋六壬续抽 LR3 12）。
口径：冻结量表（direction/claims/timing 各 0–2、0.5 步进；断语无应期 timing 记 0、结局无可核时点记 1，均注明），双评审独立（A 席均分 4.900、B 席均分 4.887，两席高度一致）＋分歧 7 例仲裁（pass 不一致或 claims+timing 和差 ≥2 触发：D9B-018/020/021/022/028/029/034，仲裁定分 4.0/3.0/3.5/3.0/3.5/3.0/4.0）。非分歧例取双评审分项均值，分歧例以仲裁分为定稿。逐例分项存 data/dev9-baseline-build/part-new.jsonl；原始评审与仲裁存同目录 judgeA/judgeB/arbitration jsonl、disputes.json、packet*.json、host-key.json。
新增 75 例大师均分 4.860、pass 65/75；分来源：易冒 5.107（n=56，pass 49）、断易天机 4.286（n=7，pass 7）、LR3-chen1 4.100（n=5）、LR3-chen2 4.000（n=7）。
dev9 全集（487 例）大师基线均分 4.662。
master-baseline-dev9.json 仅存 {total, src}，供 merge_scores.py 配对用。
