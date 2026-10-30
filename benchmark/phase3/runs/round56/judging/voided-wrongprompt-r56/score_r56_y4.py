#!/usr/bin/env python3
# Round56 judgeY block4 scoring
# Source inspection: every line's prediction object has direction/assertions/timing/summary all null,
# and there is no prediction_text field. With no concrete assertion to compare against outcome_record,
# per rules (unreported items get no points) all scores are 0.
import json, pathlib

SRC = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/judgeY-block4.jsonl")
OUT = pathlib.Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/scoresY-block4.jsonl")

GENERIC = "预测各字段均为null、无具体断语可与结局核对，故0分；自报：预测文本缺失，无法作应验比对。"

# anon_id -> note (all score 0). Special notes flag outcome-side issues in addition to missing prediction.
NOTES = {
    "P3-bbd80599": GENERIC,
    "P3-bbf9c520": GENERIC,
    "P3-bcc1cce0": GENERIC,
    "P3-bcc8816d": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局自注为回溯断验且系求测者自述，预测文本亦缺失。",
    "P3-be207416": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局句末附应期解释、断语与结局混杂，且预测文本缺失。",
    "P3-beea24bb": GENERIC,
    "P3-bf5893af": GENERIC,
    "P3-c09cc757": GENERIC,
    "P3-c155e71a": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌占者对话与断语、预测与结局不可分离。",
    "P3-c1c7ae7a": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局句末附断理解释、断语与结局混杂，且预测文本缺失。",
    "P3-c29cf367": GENERIC,
    "P3-c2f0ae45": GENERIC,
    "P3-c3502e45": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌得差与中途死之解释、预测与结局不可分离。",
    "P3-c3f9d23e": GENERIC,
    "P3-c4320d31": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局为书内自述的求测方口头反馈、无第三方记录，且预测文本缺失。",
    "P3-c434753a": GENERIC,
    "P3-c5513fcf": GENERIC,
    "P3-c65f4083": GENERIC,
    "P3-c6f06b53": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局称旁验不属本例、承接注称补官仅间接对应未明载。",
    "P3-c8317718": GENERIC,
    "P3-c8f87278": GENERIC,
    "P3-c9158813": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌占者取用解释与问答、预测与结局不可分离。",
    "P3-ca11369d": GENERIC,
    "P3-ca34a1c9": GENERIC,
    "P3-ca4f9ef6": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局句末以征验语收束、断语与结局混杂，且预测文本缺失。",
    "P3-ca7fdb92": GENERIC,
    "P3-cae8db28": GENERIC,
    "P3-cdbae30c": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：承接注称得缺仅以总承语带过、未明名，结局成色不足。",
    "P3-cf0343b9": GENERIC,
    "P3-cfe8e325": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌升迁与复任之断理解释、预测与结局不可分离。",
    "P3-d07175d6": GENERIC,
    "P3-d09a30f3": GENERIC,
    "P3-d10b3b96": GENERIC,
    "P3-d11fc22e": GENERIC,
    "P3-d16455bf": GENERIC,
    "P3-d192b8df": GENERIC,
    "P3-d192f5fa": GENERIC,
    "P3-d21b7d99": GENERIC,
    "P3-d24d1be8": GENERIC,
    "P3-d36b8a73": GENERIC,
    "P3-d388874c": GENERIC,
    "P3-d3ba9e0c": GENERIC,
    "P3-d41b69cf": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局句末附成就缘由解释、断语与结局混杂，且预测文本缺失。",
    "P3-d458096f": GENERIC,
    "P3-d471c4bd": GENERIC,
    "P3-d4a663ec": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌升任月份与云南之断理解释、预测与结局不可分离。",
    "P3-d4ab2b8c": GENERIC,
    "P3-d53e1712": GENERIC,
    "P3-d558307f": GENERIC,
    "P3-d5a0d5f7": GENERIC,
    "P3-d73d4eff": GENERIC,
    "P3-d7fedd27": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局句末附应期解释、断语与结局混杂，且预测文本缺失。",
    "P3-d8375d76": GENERIC,
    "P3-d93d7b8e": GENERIC,
    "P3-d974e65a": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局自注非原文后记、系外部史实核验而非原载结局。",
    "P3-d9937932": GENERIC,
    "P3-d9f3d5d7": GENERIC,
    "P3-dcb64464": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：承接注称间接验证例、终身功名断语无对应结局事件。",
    "P3-dd4eb325": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌死期推理解释、预测与结局不可分离。",
    "P3-dd9fdd5b": GENERIC,
    "P3-dddffa45": GENERIC,
    "P3-df0d63cc": GENERIC,
    "P3-dfae5f6b": GENERIC,
    "P3-dfddf2c7": GENERIC,
    "P3-dfe074f4": GENERIC,
    "P3-e028f477": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局句末附三刑补字解释、断语与结局混杂，且预测文本缺失。",
    "P3-e059a804": GENERIC,
    "P3-e122293f": GENERIC,
    "P3-e161dce9": GENERIC,
    "P3-e1ea02bd": GENERIC,
    "P3-e225f571": GENERIC,
    "P3-e231681c": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：承接注称两占合断、结局仅对应再占危灾断面而另一断面无记载。",
    "P3-e359f1db": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局后半为取用通则解说、与具体结局混杂不可分离。",
    "P3-e3a656a3": GENERIC,
    "P3-e47efba4": GENERIC,
    "P3-e4bb303a": GENERIC,
    "P3-e5fbf351": GENERIC,
    "P3-e61ec6f5": GENERIC,
    "P3-e677a78d": GENERIC,
    "P3-e81277b3": GENERIC,
    "P3-e8a607b0": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：承接注称趋避例、索债本问在原书中本无结局记载。",
    "P3-ea40b5b4": GENERIC,
    "P3-eb1c6a10": GENERIC,
    "P3-ebaadaab": GENERIC,
    "P3-ec495ea1": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局为书内自述且无气象记录佐证、以果然应验语收束。",
    "P3-ec87652a": GENERIC,
    "P3-ecf94947": GENERIC,
    "P3-ed45c630": GENERIC,
    "P3-ed5d37cd": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌占者自陈断期偏差、断语与结局混杂，且预测文本缺失。",
    "P3-edefb599": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌占者多段断语与对话、预测与结局不可分离。",
    "P3-f04bbebc": GENERIC,
    "P3-f2e94935": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌终命推理解释、预测与结局不可分离。",
    "P3-f2f3d134": GENERIC,
    "P3-f36815d1": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局为多段引文拼合且含日期误印标注、成色混杂。",
    "P3-f49d0c9d": GENERIC,
    "P3-f56b3f21": GENERIC,
    "P3-f58be719": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：承接注称升迁结果未直接记载、结局对应第二断防刑狱断面。",
    "P3-f5bb7a77": GENERIC,
    "P3-f5c40007": GENERIC,
    "P3-f65886cd": GENERIC,
    "P3-f7697c67": GENERIC,
    "P3-f7f36fa9": GENERIC,
    "P3-f93a8830": GENERIC,
    "P3-fa2aa5c1": GENERIC,
    "P3-fa97f7d0": GENERIC,
    "P3-faae2b82": GENERIC,
    "P3-fb0da62a": GENERIC,
    "P3-fb73c25b": GENERIC,
    "P3-fc287e7b": GENERIC,
    "P3-fc48f0e9": GENERIC,
    "P3-fca98859": GENERIC,
    "P3-fcc2b449": GENERIC,
    "P3-fd6b3633": GENERIC,
    "P3-fd750d86": GENERIC,
    "P3-fd8b90c9": GENERIC,
    "P3-fe50d4db": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局后半为六冲六合通则解说、与具体结局混杂不可分离。",
    "P3-feefc6b9": GENERIC,
    "P3-fef507d6": GENERIC,
    "P3-ff205585": GENERIC,
    "P3-ff600ee6": "预测各字段均为null、无具体断语可与结局核对，故0分；自报：结局内嵌未去与死期之断理解释、预测与结局不可分离。",
    "P3-ffcc793c": GENERIC,
}

def main():
    src_ids = []
    with SRC.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                src_ids.append(json.loads(line)["anon_id"])
    assert set(src_ids) == set(NOTES.keys()), f"id mismatch: missing={set(src_ids)-set(NOTES)} extra={set(NOTES)-set(src_ids)}"
    assert len(src_ids) == len(NOTES), "duplicate ids in source"
    with OUT.open("w", encoding="utf-8") as out:
        for aid in src_ids:
            out.write(json.dumps({"anon_id": aid, "score": 0, "note": NOTES[aid]}, ensure_ascii=False) + "\n")
    print(f"wrote {len(src_ids)} lines to {OUT}")

if __name__ == "__main__":
    main()
