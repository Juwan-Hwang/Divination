import json, pathlib
base=pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3")
batches=json.loads((base/"runs/round78/batches.json").read_text())
ids=[]
for b in ["B16","B17","B18"]:
    ids+=batches[b]
for cid in ids:
    d=json.loads((base/f"inputs-dev12/{cid}.json").read_text())
    ctx=d.get("context",{})
    att=ctx.get("attachments",{}) if isinstance(ctx,dict) else {}
    out={
      "id":cid,
      "tradition":d.get("tradition"),
      "system":d.get("system"),
      "question":ctx.get("question"),
      "asked_at":ctx.get("asked_at"),
      "setting":ctx.get("setting"),
      "hexagram":att.get("hexagram"),
      "method_detail":att.get("method_detail"),
      "casting":att.get("casting_method"),
      "date":att.get("date_ganzhi"),
      "kong":att.get("空亡") or d.get("空亡"),
      "moving":att.get("moving_lines"),
      "hidden":att.get("hidden_lines"),
      "lines":att.get("chart_lines_top_to_bottom"),
      "chart_note":att.get("chart_note"),
      "subject":d.get("subject"),
      "extra_keys": [k for k in att.keys()],
      "ctx_other": {k:v for k,v in ctx.items() if k not in ("question","asked_at","setting","attachments")},
      "top_other": {k:v for k,v in d.items() if k not in ("context","subject","notes","provenance")},
    }
    # also include any other attachment fields
    for k,v in att.items():
        if k not in ("hexagram","method_detail","casting_method","date_ganzhi","空亡","moving_lines","hidden_lines","chart_lines_top_to_bottom","chart_note"):
            out[f"att_{k}"]=v
    print(json.dumps(out,ensure_ascii=False))
