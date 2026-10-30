#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 56 judge Y block3 scoring.
Source file finding: every row's prediction object is entirely null
(direction/assertions/timing/summary all null) and there is no
prediction_text field at all. With no reported assertions, per the
frozen rubric (unreported items earn no points) every row scores 0.
Outcome-side doubts are noted per-row with a trailing 自報 clause.
"""
import json

BASE = "prediction 四欄均為 null、無 prediction_text，無任何斷語可與結局比對，未報項不給分。"

SCORES = [
    ("P3-84fcc40a", 0, BASE + " 自報：結局混載卦理推斷，斷語與結局不可分離。"),
    ("P3-852b83be", 0, BASE),
    ("P3-857e34eb", 0, BASE + " 自報：結局僅殘句，所指與所問對應不明。"),
    ("P3-85bc272a", 0, BASE),
    ("P3-8637be3b", 0, BASE),
    ("P3-86535a23", 0, BASE),
    ("P3-86cae3cb", 0, BASE),
    ("P3-86fe6a7c", 0, BASE),
    ("P3-8712d27e", 0, BASE + " 自報：結局僅「果然如是」總承，無事實內容可核。"),
    ("P3-87abed70", 0, BASE + " 自報：結局混載卦理評論，斷語與結局不可分離。"),
    ("P3-87ceb12b", 0, BASE),
    ("P3-88b4f5cb", 0, BASE),
    ("P3-8a6dfb6e", 0, BASE),
    ("P3-8af5ecfa", 0, BASE),
    ("P3-8b15ecbc", 0, BASE),
    ("P3-8b65828c", 0, BASE),
    ("P3-8b68d108", 0, BASE),
    ("P3-8bebbde9", 0, BASE + " 自報：結局為對話式反問，未載明確事實結果。"),
    ("P3-8c5b00f8", 0, BASE),
    ("P3-8d8e07c5", 0, BASE + " 自報：結局混載世爻卦理推斷，斷語與結局不可分離。"),
    ("P3-8dec7bc2", 0, BASE),
    ("P3-8e5ca381", 0, BASE),
    ("P3-8e6f9daa", 0, BASE),
    ("P3-8f64f8a0", 0, BASE),
    ("P3-8fd1c3af", 0, BASE),
    ("P3-9033027f", 0, BASE),
    ("P3-9042ed02", 0, BASE + " 自報：結局原文以逗號收尾似未完，且標注稱本人安危未明。"),
    ("P3-904dc3d4", 0, BASE),
    ("P3-907f6197", 0, BASE),
    ("P3-90b3184a", 0, BASE),
    ("P3-90be1a62", 0, BASE),
    ("P3-90e6e2ec", 0, BASE),
    ("P3-9126a73a", 0, BASE),
    ("P3-914fe269", 0, BASE),
    ("P3-91785ebc", 0, BASE),
    ("P3-93784ac0", 0, BASE),
    ("P3-93cb476f", 0, BASE),
    ("P3-93f927b6", 0, BASE + " 自報：結局自注繫獄年數原書與史載有出入。"),
    ("P3-941c839a", 0, BASE),
    ("P3-945ffb26", 0, BASE),
    ("P3-94668cf7", 0, BASE + " 自報：編者注稱日時細項未逐字復核。"),
    ("P3-9469cea9", 0, BASE),
    ("P3-94ae2a78", 0, BASE),
    ("P3-94b9ac37", 0, BASE),
    ("P3-94e3dc54", 0, BASE),
    ("P3-9514f0ad", 0, BASE),
    ("P3-952eabfe", 0, BASE + " 自報：結局疾病部分僅以「all which was true」總承，無具體事實。"),
    ("P3-95bf6cd6", 0, BASE),
    ("P3-961d7c80", 0, BASE),
    ("P3-966606b4", 0, BASE),
    ("P3-971d6f45", 0, BASE),
    ("P3-97683dda", 0, BASE + " 自報：標注稱結局僅載死亡斷面，所問財福面無對應記錄。"),
    ("P3-9788b4e0", 0, BASE),
    ("P3-98bb4f16", 0, BASE + " 自報：結局混載卦理解說，斷語與結局不可分離。"),
    ("P3-99b66f4e", 0, BASE),
    ("P3-9b39fd83", 0, BASE),
    ("P3-9b7e5c5e", 0, BASE),
    ("P3-9ba3a720", 0, BASE),
    ("P3-9c6ff479", 0, BASE),
    ("P3-9cc063b7", 0, BASE),
    ("P3-9cd0198a", 0, BASE),
    ("P3-9cdce4a9", 0, BASE),
    ("P3-9dc8a227", 0, BASE),
    ("P3-9dec5a85", 0, BASE),
    ("P3-9e421a18", 0, BASE),
    ("P3-9ec44089", 0, BASE),
    ("P3-9ef03076", 0, BASE),
    ("P3-9f83156a", 0, BASE),
    ("P3-a020566f", 0, BASE),
    ("P3-a06c14e2", 0, BASE),
    ("P3-a072c743", 0, BASE),
    ("P3-a0804237", 0, BASE),
    ("P3-a13f017a", 0, BASE),
    ("P3-a18a975f", 0, BASE),
    ("P3-a1c26278", 0, BASE),
    ("P3-a2d5c07b", 0, BASE),
    ("P3-a2dfdc80", 0, BASE),
    ("P3-a4362d13", 0, BASE),
    ("P3-a5e3e6ab", 0, BASE),
    ("P3-a6e26772", 0, BASE),
    ("P3-a700e64f", 0, BASE),
    ("P3-a72c99b1", 0, BASE),
    ("P3-a77a0a29", 0, BASE),
    ("P3-a77cda2d", 0, BASE),
    ("P3-a795ff93", 0, BASE + " 自報：標注稱結局對應大師改斷面，非原問斷面。"),
    ("P3-a7e9b366", 0, BASE),
    ("P3-a90796fd", 0, BASE),
    ("P3-a9a8577b", 0, BASE),
    ("P3-aa1d3c4f", 0, BASE),
    ("P3-ab9b1c3d", 0, BASE),
    ("P3-ac7996f4", 0, BASE),
    ("P3-ad1e22ad", 0, BASE),
    ("P3-ad478b45", 0, BASE),
    ("P3-ad525ee4", 0, BASE),
    ("P3-adcd67b1", 0, BASE),
    ("P3-ae14038c", 0, BASE),
    ("P3-ae2e2a30", 0, BASE),
    ("P3-ae5bd123", 0, BASE + " 自報：結局僅「後果然」總承，無事實內容可核。"),
    ("P3-aee78bc2", 0, BASE),
    ("P3-af55c88a", 0, BASE + " 自報：標注稱兩占合載、死亡歸屬未明。"),
    ("P3-af58c360", 0, BASE),
    ("P3-af8b1d7a", 0, BASE + " 自報：標注稱後斷應驗僅以「果如言」總承、原文已剝離。"),
    ("P3-b141f611", 0, BASE),
    ("P3-b1883d8b", 0, BASE),
    ("P3-b194589f", 0, BASE),
    ("P3-b27c1b9f", 0, BASE),
    ("P3-b2c4f663", 0, BASE),
    ("P3-b40770e2", 0, BASE),
    ("P3-b43b1dba", 0, BASE),
    ("P3-b45b8c86", 0, BASE),
    ("P3-b4bd35ae", 0, BASE + " 自報：結局自注晚年敗落細節來源未備、待另核。"),
    ("P3-b512288c", 0, BASE),
    ("P3-b5b63ef7", 0, BASE + " 自報：結局自注年份有 1643 與 OCR 作 1644 之出入。"),
    ("P3-b5c21cda", 0, BASE),
    ("P3-b6752a1c", 0, BASE),
    ("P3-b752c726", 0, BASE),
    ("P3-b781bad2", 0, BASE + " 自報：標注稱當年脫險信息僅以標注形式承接。"),
    ("P3-b8fa6218", 0, BASE),
    ("P3-b925effe", 0, BASE),
    ("P3-ba1c0126", 0, BASE),
    ("P3-babebb3f", 0, BASE),
    ("P3-bbc962a4", 0, BASE),
]

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/scoresY-block3.jsonl"
SRC = "/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/judgeY-block3.jsonl"


def main():
    src_ids = []
    with open(SRC, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                src_ids.append(json.loads(line)["anon_id"])
    my_ids = [a for a, _, _ in SCORES]
    assert my_ids == src_ids, "anon_id order/set mismatch vs source"
    with open(OUT, "w", encoding="utf-8") as f:
        for anon_id, score, note in SCORES:
            f.write(json.dumps({"anon_id": anon_id, "score": score, "note": note},
                               ensure_ascii=False) + "\n")
    print(f"wrote {len(SCORES)} rows -> {OUT}")


if __name__ == "__main__":
    main()
