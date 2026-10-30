#!/usr/bin/env python3
# R48 数据席（测字普查·乙）: ZC 判级集逐例摘要提取（只读四台账 jsonl，禁止触碰 predictions/judging/final-scores）
import json
from pathlib import Path

ROOT = Path("/home/hatch/workspace/divination")
OUT = ROOT / "benchmark/phase3/runs/round48/digestion/work-cezi-r48/zc-entries-summary-r48.json"
FILES = [
    ROOT / "benchmark/phase3/runs/round38/data-verify/zichu-cases-r38.jsonl",
    ROOT / "benchmark/phase3/runs/round39/data-verify/zichu-j3-cases-r39.jsonl",
    ROOT / "benchmark/phase3/runs/round41/data-verify/zc-candidates-r41.jsonl",
    ROOT / "benchmark/phase3/runs/round42/data-verify/zc-candidates-r42.jsonl",
]
USED = set()
for v in ["006 014 016 017 022 023 024 025 028 030 036 039 049 054 061 062 064 066 068 069",
          "070 071 075 077 079 081 082 083 084 085 090 091 092 093 097 108 118 123 125 133",
          "072 073 130 134 135 136 137 138 140 141 142 147 148 151 152 153 155 159 161 162",
          "139 143 144 145 146 149 150 154 156 157 158 160 163 164 165"]:
    USED |= {f"ZC-{x}" for x in v.split()}
assert len(USED) == 75

rows = []
for path in FILES:
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        comp = r.get("compliance") or {}
        grade = r.get("outcome_grade") or comp.get("outcome_grade")
        contam = r.get("contamination") or comp.get("contamination")
        elig = r.get("holdout_eligible")
        if elig is None:
            elig = comp.get("holdout_eligible")
        prov = r.get("provenance") or {}
        ctx = r.get("context") or {}
        inp = r.get("input_material") or {}
        gold = r.get("gold_material") or {}
        char = (ctx.get("attachments") or {}).get("character_written") or inp.get("character_or_omen") or ""
        subj = (r.get("subject") or {}).get("name_or_desc") or inp.get("subject") or ""
        ques = ctx.get("question") or inp.get("question") or ""
        pred = ""
        mp = r.get("master_predictions") or []
        if mp:
            pred = mp[0].get("statement_excerpt", "")
        if not pred:
            pred = gold.get("master_prediction", "")
        outc = (r.get("outcome") or {}).get("description", "") or gold.get("outcome", "")
        rows.append(dict(id=r["id"], grade=grade, contamination=contam, eligible=elig,
                         used=r["id"] in USED, book=prov.get("book", ""), page=prov.get("page", ""),
                         char=str(char), subject=str(subj), question=str(ques),
                         pred=str(pred)[:70], outcome=str(outc)[:70],
                         topic=r.get("topic_tag", "")))
rows.sort(key=lambda d: int(d["id"].split("-")[1]))
assert len(rows) == 165 and rows[0]["id"] == "ZC-001" and rows[-1]["id"] == "ZC-165"
OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"[assert ok] ZC 摘要 165 条 -> {OUT}")
for r in rows[:3]:
    print(r["id"], r["grade"], r["contamination"], r["used"], "|", r["book"], "|", r["page"], "|", r["char"][:20], "|", r["subject"][:30])
