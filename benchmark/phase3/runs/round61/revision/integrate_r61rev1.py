#!/usr/bin/env python3
"""R61 host tooling: integrate R61-REV1 into the live method per
PREREG-ADDENDUM-r61 s.2 (append-only).

- calibration.md: append new section 6 after section 5 (incl. its
  invalidation registration); body = clauses R61-REV1-1..6 transcribed
  verbatim from revision/PROPOSAL-R61-REV1.md s.2 (programmatic slice,
  no retyping). Section 5 segment hash asserted unchanged.
- SKILL.md: insert the single (n) pointer line right after the (m)
  line; (m) line asserted present verbatim exactly once.
Verification: clause headings 1..6 each exactly once in the appended
block; appended block byte-equal to the proposal slice; section 5
segment sha256 identical pre/post; SKILL diff limited to the one
inserted line.
"""
import hashlib
import re
from pathlib import Path

P3 = Path("/home/hatch/workspace/divination/benchmark/phase3")
PROP = P3 / "runs/round61/revision/PROPOSAL-R61-REV1.md"
CAL = P3 / "method/references/calibration.md"
SKILL = P3 / "method/SKILL.md"

HEADER = ("## 六、应期主坐标二路复推与断项粒度收束核"
          "（R61 干预 R61-REV1，跨体系收束机制）\n\n"
          "（集成登记：提案 runs/round61/revision/PROPOSAL-R61-REV1.md，"
          "主持闸门裁定 runs/round61/PREREG-ADDENDUM-r61.md；自 R62 起算效力。"
          "判读口径定版见增补件 §三：判读集为集成后首个新鲜封存验收集、"
          "N≥20；主指标 TIM ≤0.080／CLAIM ≤0.120／TIM+CLAIM ≤0.240，"
          "护栏 OMIT ≤0.160／总配对差 ≥−1.366，反向证伪与回滚照增补件。）\n\n")
N_LINE = ("- (n) 双核复核：交付前对应期主坐标执行二路复推、对具体断项执行"
          "粒度收束核（正本见 references/calibration.md 第六节，R61-REV1，"
          "自 R62 起算效力）")
M_LINE = ("- (m) 收束复核：交付前执行列面—证据双闸（正本见 "
          "references/calibration.md 第五节，R59-REV1，自 R60 起算效力）")

prop = PROP.read_text(encoding="utf-8")
a = prop.index("**R61-REV1-1")
b = prop.index("### 与现行条文的并列登记")
block = prop[a:b].rstrip() + "\n"
heads = re.findall(r"\*\*(R61-REV1-\d)", block)
assert heads == [f"R61-REV1-{i}" for i in range(1, 7)], heads

cal = CAL.read_text(encoding="utf-8")
assert "## 六、" not in cal, "section 6 already present"
sec5_pre = cal[cal.index("## 五、"):]
h_pre = hashlib.sha256(sec5_pre.encode()).hexdigest()

new_cal = cal.rstrip() + "\n\n" + HEADER + block
CAL.write_text(new_cal, encoding="utf-8")

cal2 = CAL.read_text(encoding="utf-8")
sec5_post = cal2[cal2.index("## 五、"):cal2.index("## 六、")].rstrip() + "\n"
sec5_pre_norm = sec5_pre.rstrip() + "\n"
assert sec5_post == sec5_pre_norm, "section 5 segment changed!"
tail = cal2[cal2.index("## 六、"):]
assert tail == (HEADER + block).rstrip() + "\n" or block in tail
assert cal2.count("R61-REV1-1（触发面") == 1

skill = SKILL.read_text(encoding="utf-8")
assert skill.count(M_LINE) == 1
assert N_LINE not in skill
SKILL.write_text(skill.replace(M_LINE, M_LINE + "\n" + N_LINE), encoding="utf-8")
skill2 = SKILL.read_text(encoding="utf-8")
assert skill2.count(N_LINE) == 1 and skill2.count(M_LINE) == 1
removed = skill2.replace("\n" + N_LINE, "")
assert removed == skill, "SKILL diff beyond the inserted line!"

print("INTEGRATION OK")
print("section5 sha256 pre :", h_pre)
print("section5 sha256 post:", hashlib.sha256(sec5_post.encode()).hexdigest(),
      "(normalized segment, equal content asserted)")
print("clauses integrated: 6/6 verbatim; SKILL (n) line inserted after (m)")
