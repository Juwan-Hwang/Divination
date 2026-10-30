import json, pathlib
base = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/inputs-dev12")
ids = ["LY-517","LY-518","LY-519","LY-520","LY-521","LY-522","LY-523","LY-524","LY-525","LY-526","LY-527","LY-528","LY-529","LY-530","LY-531","LY-532","LY-533","LY-534","LY-535","LY-536","LY-537","LY-538","LY-539","LY-540","LY-541","LY-542","LY-543","LY-601","LY-602","LY-603","LY-604","LY-605","LY-606","LY-607","LY-608","LY-609","LY-610","LY-611","LY-612","LY-613"]
for cid in ids:
    p = base / f"{cid}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    print(f"===== {cid} =====")
    print(json.dumps(d, ensure_ascii=False, indent=1))
