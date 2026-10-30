#!/usr/bin/env python3
# Round 56 judge Y block1 scoring.
# Finding: every source line has prediction = {direction: None, assertions: None,
# timing: None, summary: None} and no prediction_text field at all.
# With no prediction assertions to compare against the outcome, no direction /
# specific-item / timing credit can be established -> score 0 for every line.
# Outcome-side doubts are appended to the note as 「自报：...」 without changing scores.
import json

BASE = "prediction四字段皆null且无prediction_text，无可核断语可与结局比对，应验一致性无据，记0分"
D = "；自报：结局以「果」字断语式自证应验、断语与结局不可分离"
A = "；自报：结局以「應」字断语式自证、断语与结局不可分离"
R = "；自报：结局嵌入占断推演、断语与结局不可分离"
S1 = "；自报：结局自述断语与结局同载于断语段落、断语与结局不可分离"

# (anon_id, self-report suffix) in exact source order; score is 0 for all.
ENTRIES = [
    ("P3-003b3418", D),
    ("P3-005280bd", S1),
    ("P3-00dc5635", D),
    ("P3-0143787b", "；自报：结局称原书已自注此节为既验之事、断语与结局不可分离"),
    ("P3-018a3d4b", R),
    ("P3-01c07f5f", D),
    ("P3-01e3481b", D),
    ("P3-0249fa8e", D),
    ("P3-0264d004", ""),
    ("P3-03bbaf01", D),
    ("P3-04161335", ""),
    ("P3-049fb164", ""),
    ("P3-0605ecfd", "；自报：结局仅载死亡、所问终身财福面无独立记载（carry_note已标）"),
    ("P3-06383757", ""),
    ("P3-067f7add", "；自报：结局以「属实」自证、断语与结局不可分离"),
    ("P3-08496a2f", "；自报：结局以「果」字断语式自证且病断面结局缺位、部分细项原文未逐项复核"),
    ("P3-0853e41f", ""),
    ("P3-0866c552", "；自报：结局为旁及官非断面、开店贸易得利面无独立记载（carry_note已标）"),
    ("P3-08781833", D),
    ("P3-094e5758", ""),
    ("P3-0aff3018", D),
    ("P3-0b6f646d", D),
    ("P3-0bbb2de6", ""),
    ("P3-0c1f6b0c", "；自报：结局仅一句「果一一無錯」自证、无具体结局内容可核"),
    ("P3-0c7a1ce4", ""),
    ("P3-0d6970f8", A),
    ("P3-0dc01222", "；自报：结局仅「后果然」三字、无具体结局内容可核且属断语式自证"),
    ("P3-0dc4d9d2", D),
    ("P3-0e38394f", ""),
    ("P3-0e83a011", ""),
    ("P3-0f0365df", ""),
    ("P3-0fcdee67", D),
    ("P3-0fe27431", R),
    ("P3-10570ec9", S1),
    ("P3-10b8c0ae", ""),
    ("P3-11646c1c", D),
    ("P3-1169e52a", ""),
    ("P3-1170fd6f", ""),
    ("P3-13845a2d", R),
    ("P3-13bb30bd", D),
    ("P3-14487d3b", D),
    ("P3-14d32646", D),
    ("P3-15309526", ""),
    ("P3-176fe2fc", D),
    ("P3-18692de4", ""),
    ("P3-18faea6e", D),
    ("P3-198a2b72", ""),
    ("P3-1999ea2e", R),
    ("P3-19a380a1", D),
    ("P3-1ab3414c", D),
    ("P3-1adfaf10", ""),
    ("P3-1b257c29", ""),
    ("P3-1bf0b312", D),
    ("P3-1d0443c2", D),
    ("P3-1ea46e8f", ""),
    ("P3-1eb14970", D),
    ("P3-1ec8ec97", D),
    ("P3-1eee60cd", ""),
    ("P3-1fa16314", A),
    ("P3-200c90d4", A),
    ("P3-20519132", ""),
    ("P3-212c0c10", D),
    ("P3-213544a6", ""),
    ("P3-21b3e21b", D),
    ("P3-221ab57c", D),
    ("P3-22d8e205", D),
    ("P3-23323706", ""),
    ("P3-23677a67", "；自报：结局仅止于占后半日即时记载、养蜂终局未载（carry_note已标）"),
    ("P3-23793db5", D),
    ("P3-23912aaf", ""),
    ("P3-2464740c", ""),
    ("P3-248e3b70", ""),
    ("P3-24f24a8c", R),
    ("P3-252b1f5f", ""),
    ("P3-2611a889", D),
    ("P3-26c9d71e", "；自报：结局仅「後果全無」四字、无具体所指可核且属断语式措辞"),
    ("P3-26ed52ce", D),
    ("P3-26f85d51", ""),
    ("P3-272e9d90", ""),
    ("P3-27f5f037", ""),
    ("P3-29543457", D),
    ("P3-29c05d7a", ""),
    ("P3-29c50b3e", R),
    ("P3-2af3591e", S1),
    ("P3-2b5c5cab", D),
    ("P3-2ba0d2f3", "；自报：结局仅载死亡断面、所问功名面无对应记载且结局嵌入断语推演（carry_note已标）"),
    ("P3-2bf71cf2", D),
    ("P3-2c2667ae", D),
    ("P3-2c9904b7", D),
    ("P3-2cbf8400", D),
    ("P3-2df5a8d5", D),
    ("P3-2fb23f6d", D),
    ("P3-301ceb7a", D),
    ("P3-30aca65b", D),
    ("P3-3106cf4c", ""),
    ("P3-31993f47", ""),
    ("P3-31ccb244", D),
    ("P3-31e65266", "；自报：结局仅载平安、未载来否结果、答非所问一面（carry_note已标）"),
    ("P3-32617982", D),
    ("P3-32990c94", ""),
    ("P3-33cd18e5", ""),
    ("P3-34349353", ""),
    ("P3-3607dd50", ""),
    ("P3-3639633a", "；自报：结局称应期为本人亲历自证、断语与结局不可分离"),
    ("P3-368c3ee9", "；自报：结局对应同条再问遍游、主问具体断面无独立记载（carry_note已标）"),
    ("P3-36a50634", D),
    ("P3-3762b19d", D),
    ("P3-37679a8a", "；自报：结局以「果然」自证且仅余七月死期一语、断语与结局不可分离"),
    ("P3-3822d63a", D),
    ("P3-38f0b3c1", D),
    ("P3-3917d7d0", "；自报：结局叙事内嵌占者断语对话、断语与结局不可分离"),
    ("P3-3a8e221b", ""),
    ("P3-3af59fd6", ""),
    ("P3-3c43df42", ""),
    ("P3-3c6e3454", D),
    ("P3-3cefc3ba", D),
    ("P3-3d53ae3c", D),
    ("P3-3d7ab254", ""),
    ("P3-3e2fe950", D),
    ("P3-3e58c3b1", D),
    ("P3-3e66e497", ""),
    ("P3-402945a3", ""),
]

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/scoresY-block1.jsonl"
SRC = "/home/hatch/workspace/divination/benchmark/phase3/runs/round56/judging/judgeY-block1.jsonl"


def main():
    src_ids = []
    with open(SRC, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                src_ids.append(json.loads(line)["anon_id"])
    my_ids = [a for a, _ in ENTRIES]
    assert my_ids == src_ids, "anon_id order/content mismatch vs source"
    with open(OUT, "w", encoding="utf-8") as f:
        for anon_id, suffix in ENTRIES:
            rec = {"anon_id": anon_id, "score": 0, "note": BASE + suffix}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {len(ENTRIES)} lines to {OUT}")


if __name__ == "__main__":
    main()
