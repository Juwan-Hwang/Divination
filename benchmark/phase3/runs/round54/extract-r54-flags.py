import json, pathlib, sys
base = pathlib.Path.home() / "workspace/divination/benchmark/phase3"
def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

mapping_pairs = [
 ("P3-03d05d10","LR3-112"),("P3-071c8c12","AS-015"),("P3-0cacdd18","BQ-001"),("P3-1f388a29","LY-426"),
 ("P3-20ec5663","AS-210"),("P3-26c91e10","LR3-107"),("P3-3446c2fd","LY-011"),("P3-3056d752","LY-620"),
 ("P3-3efec437","BQ-023"),("P3-41a254e2","LR3-101"),("P3-4b9f3826","OC-026"),("P3-5821c078","LY-506"),
 ("P3-5d2b7172","OC-029"),("P3-5e199cfa","LY-504"),("P3-62d15b3b","LY-508"),("P3-6ceeff0f","LY-623"),
 ("P3-7c998ca0","LY-533"),("P3-98d80157","LY-458"),("P3-9f93f9ca","BQ-025"),("P3-a7f97569","LR2-023"),
 ("P3-a84dca42","LY-430"),("P3-b34a586a","LY-513"),("P3-b4594a3b","LY-212"),("P3-9ac5a8db","LY-433"),
 ("P3-b6fc52d8","LR2-020"),("P3-bd88c89c","LY-510"),
 ("P3-c43a7f24","LY-629"),("P3-c5c90843","LY-205"),("P3-d081b2d4","LY-206"),("P3-dbd02581","LY-023"),
 ("P3-dc7dc0f6","LY-203"),("P3-eb47d7b7","LY-436"),("P3-ef32f68b","LY-222"),("P3-f271e700","LY-220"),
 ("P3-f9ec0167","LY-615"),("P3-fcbb56a9","LY-437"),
]
block = int(sys.argv[1]) if len(sys.argv)>1 else 1
chunk = mapping_pairs[(block-1)*9:block*9] if block<=4 else mapping_pairs
# blocks in task are 8,8,10,10; handle custom slices via second arg
if len(sys.argv)>3:
    s,e = int(sys.argv[2]), int(sys.argv[3])
    chunk = mapping_pairs[s:e]

man = load(base/"runs/round54/judging/outcome-manifest.json")
cases = man.get("cases", {})
tails = man.get("stripped_tail", {})

for anon, cid in chunk:
    inp = load(base/"inputs-dev12"/f"{cid}.json")
    pred = load(base/"runs/round54/predictions"/f"{cid}.json")
    ctx = inp.get("context", {})
    print(f"\n===== {anon} -> {cid} =====")
    print("SUBJECT:", json.dumps(inp.get("subject",{}), ensure_ascii=False))
    print("QUESTION:", ctx.get("question",""))
    print("SETTING:", ctx.get("setting",""))
    # attachments keys only plus short values if string short
    att = ctx.get("attachments", {})
    if isinstance(att, dict):
        print("ATTACH_KEYS:", list(att.keys()))
    print("PROVENANCE:", json.dumps(inp.get("provenance",{}), ensure_ascii=False)[:500])
    print("PREDICTION:", pred.get("prediction_text",""))
    print("OUTCOME:", cases.get(cid, "<MISSING>"))
    if cid in tails:
        print("STRIPPED_TAIL:", tails[cid])
