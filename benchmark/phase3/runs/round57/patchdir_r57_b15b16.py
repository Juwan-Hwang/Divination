import json, pathlib
OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round57/predictions")
D = {
"LY-517":"可成（吉）","LY-518":"不成／有害（凶）","LY-519":"可保（吉）","LY-520":"不利（凶）","LY-521":"得利（吉）",
"LY-522":"得利（吉）","LY-523":"难愈（凶）","LY-524":"可用（吉）","LY-525":"难恃（偏凶）","LY-526":"有碍、该日不宜（凶）",
"LY-527":"修补有益、功名有转机（偏吉）","LY-528":"中平可用、非上吉（平偏吉）","LY-529":"中上可用（吉）","LY-530":"不甚平安（偏凶）",
"LY-531":"归（吉）","LY-532":"可愈（吉）","LY-533":"可索而迟得（偏吉）","LY-534":"难准（凶）","LY-535":"可过而迟（偏吉）",
"LY-536":"难愈（凶）","LY-537":"归（吉）","LY-538":"可保（吉）","LY-539":"雨止转晴（吉）","LY-540":"可成（吉）",
"LY-541":"得利（吉）","LY-542":"可葬（偏吉）","LY-543":"当避、避向南方可全（避则吉）",
"LY-601":"可愈（吉）","LY-602":"难得（凶）","LY-603":"可愈而迟（吉）","LY-604":"得救（吉）","LY-605":"难救（凶）",
"LY-606":"凶、难脱","LY-607":"难回生（凶）","LY-608":"可得（吉）","LY-609":"得见（吉）","LY-610":"可升而迟（偏吉）",
"LY-611":"不利（凶）","LY-612":"开成而利薄（偏凶）","LY-613":"产迟有险（偏凶）",
}
for cid, dtext in D.items():
    p = OUT / f"{cid}.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    if not d["prediction_text"].startswith("【方向"):
        d["prediction_text"] = f"" + d["prediction_text"]
    p.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
print("patched", len(D))
