# -*- coding: utf-8 -*-
"""Phase 3 expansion2 分池与封存脚本（数据角）。
- 合并 expansion2/zengshan 与 expansion2/bushi 两路新例（84 例，全部 A 级、低污染）。
- 分池：仅 tradition×contamination 一层（liuyao×low），层内按 sha256("phase3-round2-20261029:"+id)
  十六进制升序，每 10 例取第 3、6、9 位入 holdout4，余入 dev-add。
- 单文件 inputs 投影为 phase3 统一格式（id/tradition/subject/context/provenance/language），无任何答案字段。
- holdout4 金标按 holdout3/test_gold.jsonl 的 schema 转换封存；落盘后本脚本不再读它。"""
import json, hashlib, pathlib, subprocess

P3 = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
E2 = P3 / "expansion2"

def load(p):
    return [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]

z_in = {r["id"]: r for r in load(E2/"zengshan/inputs.jsonl")}
z_an = {r["id"]: r for r in load(E2/"zengshan/answers.jsonl")}
b_in = {r["id"]: r for r in load(E2/"bushi/inputs.jsonl")}
b_an = {r["id"]: r for r in load(E2/"bushi/answers.jsonl")}
roster = load(E2/"zengshan/roster-part.jsonl") + load(E2/"bushi/roster-part.jsonl")
inputs = {**z_in, **b_in}; answers = {**z_an, **b_an}
assert len(roster) == 84 and len(inputs) == 84 and len(answers) == 84, (len(roster), len(inputs), len(answers))
assert all(r["contamination"] == "low" and r["tradition"] == "liuyao" for r in roster)

# roster4-additions（按 id 排序）
roster_sorted = sorted(roster, key=lambda r: r["id"])
with open(P3/"roster4-additions.jsonl", "w", encoding="utf-8") as f:
    for r in roster_sorted: f.write(json.dumps(r, ensure_ascii=False) + "\n")

# 分池
ids = [r["id"] for r in roster_sorted]
ordered = sorted(ids, key=lambda i: hashlib.sha256(f"phase3-round2-20261029:{i}".encode()).hexdigest())
holdout4 = [i for pos, i in enumerate(ordered, start=1) if pos % 10 in (3, 6, 9)]
dev_add = [i for i in ids if i not in set(holdout4)]
print(f"holdout4: {len(holdout4)}  dev_add: {len(dev_add)}")
assert 25 <= len(holdout4) <= 35

# 单文件 inputs（统一投影）
def project(r):
    return {"id": r["id"], "tradition": r.get("tradition", r.get("system")), "subject": r["subject"],
            "context": r["context"], "provenance": r["provenance"], "language": r["language"]}
(P3/"holdout4-inputs").mkdir(exist_ok=True)
for i in dev_add:
    (P3/f"inputs/{i}.json").write_text(json.dumps(project(inputs[i]), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for i in holdout4:
    (P3/f"holdout4-inputs/{i}.json").write_text(json.dumps(project(inputs[i]), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

# splits4.json
s3 = json.load(open(P3/"splits3.json", encoding="utf-8"))
splits4 = {
  "algorithm": "仅对 expansion2 新增 84 例 A 级案例划分：按 tradition × contamination 分层（本轮仅 liuyao × low 一层），层内按 sha256(\"phase3-round2-20261029:\"+id) 十六进制升序，每 10 例取排序后第 3、6、9 位入 holdout4，余入 dev-add。dev4 = dev3 全部 141 例 + dev-add；holdout4 独立列明，与 holdout3 无交集。落盘即冻结。",
  "dev4": s3["dev3"] + dev_add,
  "holdout4": holdout4,
  "dev_add_new": dev_add,
  "sources": {"dev3_from": "benchmark/phase3/splits3.json", "additions": "benchmark/phase3/roster4-additions.jsonl"},
}
with open(P3/"splits4.json", "w", encoding="utf-8") as f:
    json.dump(splits4, f, ensure_ascii=False, indent=1)

# dev-add answers（dev-new-answers 格式：expansion answers + tradition + source_route）
route = {r["id"]: r["source"] for r in roster_sorted}
with open(E2/"dev-add-answers.jsonl", "w", encoding="utf-8") as f:
    for i in dev_add:
        a = dict(answers[i]); a["tradition"] = "liuyao"; a["source_route"] = route[i]
        f.write(json.dumps(a, ensure_ascii=False) + "\n")

# holdout4 金标（holdout3 gold schema）
gold = []
for i in holdout4:
    a = answers[i]; mp0 = a["master_predictions"][0]
    gold.append({
      "id": i,
      "master_predictions": [{
        "master": mp0["master"], "system": "liuyao",
        "verdict": mp0["statement_excerpt"],
        "reasoning_points": mp0["key_assertions"],
        "outcome": a["outcome"]["description"],
        "source": {"book": a["provenance"]["book"], "chapter": a["provenance"]["page"], "url": a["provenance"]["url"]},
      }],
      "license_status": a["license_status"], "redistributable": a["redistributable"],
      "tradition": "liuyao", "source_route": route[i],
      "outcome": a["outcome"],
    })
gold_path = P3/"holdout4/test_gold.jsonl"
with open(gold_path, "w", encoding="utf-8") as f:
    for g in gold: f.write(json.dumps(g, ensure_ascii=False) + "\n")
sha = hashlib.sha256(open(gold_path, "rb").read()).hexdigest()
now = subprocess.run(["date", "+%Y-%m-%dT%H:%M:%S+08:00"], env={"TZ": "Asia/Shanghai", "PATH": "/usr/bin:/bin"}, capture_output=True, text=True).stdout.strip()
print("seal time:", now); print("gold sha256:", sha); print("holdout4 ids:", "、".join(holdout4))

(P3/"holdout4/SEALED.md").write_text(f"""# SEALED — holdout4 金标封存说明

- 本目录 `test_gold.jsonl` 为 holdout4 共 {len(holdout4)} 例的完整金标（master_predictions + outcome），组建时间 {now}（Asia/Shanghai）。
- **只许评审角在 Phase 3 验收轮开封时读取**；盲测角、修订角、数据角在本文件落盘后均不得再读。
- 开封须在 `benchmark/phase3/holdout4-seal-log.md` 追加一笔（时间、依据、开封人角色、范围）后方可进行。
- 金标 SHA-256：`{sha}`。
- 封存状态以 seal log 为准；本文件落盘时状态为「未开封」。
""", encoding="utf-8")

(P3/"holdout4-seal-log.md").write_text(f"""# holdout4 封存日志

- **组建时间**：{now}（Asia/Shanghai）
- **组建角色**：数据角（Phase 3 第二轮扩数建池）
- **算法**：仅对 expansion2 新增 84 例 A 级案例按 tradition × contamination 分层（本轮仅 liuyao × low 一层），层内按 sha256("phase3-round2-20261029:"+id) 十六进制升序，每 10 例取第 3、6、9 位入 holdout4；划分详见 benchmark/phase3/splits4.json，落盘即冻结。
- **例数**：holdout4 共 {len(holdout4)} 例（{'、'.join(holdout4)}）。
- **金标 SHA-256**：`{sha}`
- **结局封存位置**：benchmark/phase3/holdout4/test_gold.jsonl（同目录 SEALED.md 注明只许评审角验收时开封）；holdout4 的盲测 inputs 单独置于 benchmark/phase3/holdout4-inputs/，不含任何答案字段（核对记录 benchmark/phase3/expansion2/input-check2.txt）。
- **状态**：**未开封**。自本笔落盘起，holdout4 结局不进入任何给盲测角／修订角的材料；开封须由评审角于验收轮在本日志追加一笔后进行。
""", encoding="utf-8")
print("sealed OK")
