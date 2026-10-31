# -*- coding: utf-8 -*-
"""R76 S4: dump my 60 cards compactly for reading. Stage 1."""
import json, os
BASE = "/home/hatch/workspace/divination/benchmark/phase3"
IDS = ["LY-242","LY-243","LY-244","LY-245","LY-246","LY-249","LY-250","LY-251","LY-252","LY-253",
"LY-254","LY-255","LY-259","LY-301","LY-304","LY-305","LY-306","LY-307","LY-309","LY-311",
"LY-312","LY-314","LY-315","LY-318","LY-319","LY-320","LY-322","LY-323","LY-324","LY-325",
"LY-328","LY-329","LY-330","LY-331","LY-332","LY-333","LY-335","LY-336","LY-338","LY-339",
"LY-340","LY-342","LY-344","LY-402","LY-403","LY-404","LY-405","LY-406","LY-407","LY-408",
"LY-411","LY-413","LY-415","LY-416","LY-417","LY-418","LY-421","LY-423","LY-424","LY-425"]
out = []
for cid in IDS:
    p = os.path.join(BASE, "inputs-dev12", cid + ".json")
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    ctx = d.get("context", {})
    att = ctx.get("attachments", {}) or {}
    out.append("="*20 + " " + cid)
    out.append("tradition=" + str(d.get("tradition")) + " | system=" + str(d.get("system")))
    out.append("Q: " + str(ctx.get("question")))
    out.append("asked_at: " + str(ctx.get("asked_at")) + " | setting: " + str(ctx.get("setting")))
    for k, v in att.items():
        if k == "chart_lines_top_to_bottom":
            out.append("chart(top->bottom):")
            for line in v:
                out.append("   " + str(line))
        else:
            out.append(str(k) + ": " + str(v))
    # any other top-level keys besides standard
    for k in d.keys():
        if k not in ("id","tradition","system","subject","context","provenance","language"):
            out.append("EXTRA " + k + ": " + json.dumps(d[k], ensure_ascii=False)[:800])
    sub = d.get("subject") or {}
    out.append("subject: " + json.dumps(sub, ensure_ascii=False))
with open(os.path.join(BASE, "runs/round76/dump_r76_s4.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("dumped", len(IDS))
