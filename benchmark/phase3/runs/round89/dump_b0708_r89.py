import json, os
P3 = "/home/hatch/workspace/divination/benchmark/phase3"
ids = ['LY-009','LY-01','LY-010','LY-011','LY-012','LY-013','LY-014','LY-015','LY-016','LY-017','LY-018','LY-019','LY-021','LY-022','LY-023','LY-024','LY-025','LY-026','LY-027','LY-028','LY-029','LY-030','LY-031','LY-032','LY-033','LY-034','LY-035','LY-036','LY-102','LY-103','LY-104','LY-105','LY-202','LY-203','LY-204','LY-205','LY-206','LY-207','LY-208','LY-210']
out = []
for i in ids:
    d = json.load(open(f"{P3}/inputs-dev12/{i}.json"))
    trad = d.get("tradition", d.get("system", "UNSET"))
    ctx = d.get("context", {})
    att = ctx.get("attachments", {}) or {}
    lines = att.get("chart_lines_top_to_bottom") or att.get("lines_top_to_bottom") or ctx.get("lines_top_to_bottom") or []
    out.append(f"===== {i} | tradition_field={trad}")
    out.append(f"Q: {ctx.get('question','')} | asked_at: {ctx.get('asked_at','')} | setting: {ctx.get('setting','')}")
    out.append(f"hex: {att.get('hexagram','')} | moving: {att.get('moving_lines','')} | kong: {att.get('空亡','')} | hidden: {att.get('hidden_lines','')} | date: {att.get('date_ganzhi','')}")
    for L in lines:
        out.append("  " + str(L))
    extra = {k: v for k, v in att.items() if k not in ("hexagram","moving_lines","chart_lines_top_to_bottom","lines_top_to_bottom","casting_method","空亡","hidden_lines","date_ganzhi")}
    if extra:
        out.append("  extra_att: " + json.dumps(extra, ensure_ascii=False)[:600])
    out.append("")
open(f"{P3}/runs/round89/cards_b0708_r89.txt","w").write("\n".join(out))
print("wrote", len(ids))
