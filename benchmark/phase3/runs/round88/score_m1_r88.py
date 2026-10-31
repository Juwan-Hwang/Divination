#!/usr/bin/env python3
"""R88 judge M1 (master packet, 28 cases) scoring writer.
Segments appended one at a time; each segment asserted before continuing.
Only reads packet-master.json (the assigned input) to verify anon_id set.
Never touches host-mapping or any other packet/score file.
"""
import json
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round88")
PACKET = BASE / "acceptance" / "judging" / "packet-master.json"
OUT = BASE / "acceptance" / "judging" / "judgeM1.jsonl"

# (anon_id, direction, claims, timing, reason)
SEGMENTS = [
    [
        ("H31M-052d78b7", 2.0, 2.0, 0.0, "携眷寄寓邻地、舟船破损、鸣官见官均与结局吻合；预测断语本身无应期，timing记0。"),
        ("H31M-36766c7d", 2.0, 1.5, 2.0, "亥月乙卯日剖腹产男，日期与平安结局精准命中；入盆一语未被结局记载，claims不给满分。"),
        ("H31M-3d43f4d0", 2.0, 2.0, 0.0, "工作没调动成，主断语完全印证；预测断语本身无应期，timing记0。"),
        ("H31M-52ae3f06", 1.5, 1.0, 0.0, "四月见劫耗印证劫掠方向，但凶手为家人、护救、不能大逞等子断语未被结局记载；预测断语本身无应期，timing记0。"),
        ("H31M-63286ec6", 1.0, 1.0, 0.0, "官讼羁累与阻隔印证，但利于奏对、赴京引见并未发生（旋调松江未赴京）；预测断语本身无应期，timing记0。"),
        ("H31M-72c1b47f", 2.0, 1.5, 2.0, "不赴广南、改岳庙读书、己酉中举、庚戌登科皆验且年份精准；二甲二十一名未被结局记载，claims不给满分。"),
        ("H31M-7518b051", 2.0, 1.5, 2.0, "来岁丁父忧、三十七岁后连任、五十二岁降官闲居八年而死，时间线精准；监司之职等个别细节与结局记载不完全对应，claims不给满分。"),
    ],
    [
        ("H31M-78a13261", 2.0, 2.0, 0.0, "小儿仅呛奶啼哭、并非肺炎，不药而愈方向与断语印证；预测断语本身无应期，timing记0。"),
        ("H31M-7fafad48", 2.0, 1.5, 0.0, "因弟官非逃亡、见火亦为弟所致，兄弟致端与火惊印证；宅昏昧、化解等子断语未被结局记载；预测断语本身无应期，timing记0。"),
        ("H31M-8aa30de8", 1.5, 1.0, 0.0, "次年酉贼破省与防西方之凶方向相合，但屋多人衰、冲关免阻等子断语未被结局印证；预测断语本身无应期，timing记0。"),
        ("H31M-8ce84f81", 2.0, 1.5, 0.0, "怀孕并生女孩印证；第三个孩子之序位未被结局记载，claims不给满分；预测断语本身无应期，timing记0。"),
        ("H31M-9e863514", 2.0, 1.5, 1.5, "数妻相继亡、四年自绛帐显达、遇曹姓荐引、带刑职入六曹大体印证；声名西北、四任、克四妻之数等细节未全被记载，claims与timing不给满分。"),
        ("H31M-a1bef5d3", 1.0, 1.0, 0.0, "行程受阻、贼陷致道路不通印证，但结局明言宜久远之断为误，饷运不继等亦未载；预测断语本身无应期，timing记0。"),
        ("H31M-a63c88ce", 2.0, 1.5, 0.0, "遇贼之时避近处杨家得安，就近为安印证；不可求财一语无结局可核，claims不给满分；预测断语本身无应期，timing记0。"),
    ],
    [
        ("H31M-aeb7b9c9", 1.5, 1.0, 0.0, "怀孕信息印证，但结局为流产，胖小子与子月出生均未实现，所断应期未命中，timing记0。"),
        ("H31M-aee4a7ed", 2.0, 1.5, 2.0, "午时去取果得衣物，时点精准；惟因不合发生争执重改后才取走，到手并非毫无波折，claims不给满分。"),
        ("H31M-b05d2e91", 2.0, 1.5, 2.0, "当月生女孩且难产，本月应期命中；侄女住院、为吉等子断语未被结局明确记载，claims不给满分。"),
        ("H31M-c720bbf9", 2.0, 2.0, 2.0, "本月安全生下女孩，不难产断语全验，本月应期命中。"),
        ("H31M-d0b4bf8e", 2.0, 1.5, 1.5, "两丁服、以弟为子、妻因产亡、死于外州且子不归皆验，四十五岁终亦合；历事三授之数与结局所载多次授职不尽对应，claims与timing不给满分。"),
        ("H31M-d24fe2b1", 2.0, 1.5, 0.0, "鼻癌与手术、维持中（未全愈）印证；呼吸不便、小便困难等子断语未被结局记载；预测断语本身无应期，timing记0。"),
        ("H31M-d73d8e81", 2.0, 2.0, 2.0, "六月十五日丁丑日子时生女孩，所列两日与子丑时辰对应精准命中。"),
    ],
    [
        ("H31M-db602352", 2.0, 2.0, 2.0, "寅月（交节次日）生男孩且难产，凶中有救，月份与诸断语全验。"),
        ("H31M-dcb61247", 2.0, 2.0, 0.0, "钱果在办公室写字台下找到，地点断语精准；预测断语本身无应期，timing记0。"),
        ("H31M-de847485", 2.0, 1.5, 0.0, "兼职权署、得宠、纳妾、欲去不能、遇外路监司恳告得解任皆验；俸增、贪色寻医等子断语未被结局记载；预测断语本身无应期，timing记0。"),
        ("H31M-e0469fa2", 2.0, 2.0, 0.0, "未升迁、丁艰阻、父棺白蚁伤坏、服满得一任而不能终任（病归卒）逐条印证；预测断语本身无应期（仅相对服满），timing记0。"),
        ("H31M-f664f742", 1.0, 1.0, 0.0, "结局仅印证乘轿坠跌致死（覆坠之患），妒忌灭前程、子息、神像、妻疾等众多子断语均未被结局记载；预测断语本身无应期，timing记0。"),
        ("H31M-fcf50885", 2.0, 2.0, 0.0, "查得子宫瘤且服中药而愈，病名与疗法断语全验；预测断语本身无应期，timing记0。"),
        ("H31M-ff003019", 2.0, 1.5, 2.0, "未月果胎动，应期精准，怀孕之象亦由胎动印证；胎儿不动、缺水等前段子断语未被结局单独记载，claims不给满分。"),
    ],
]

ALLOWED = {0.0, 0.5, 1.0, 1.5, 2.0}
FIELDS = {"anon_id", "direction", "claims", "timing", "total", "pass", "reason"}


def check_row(row):
    assert set(row.keys()) == FIELDS, f"field mismatch: {row.keys()}"
    for k in ("direction", "claims", "timing"):
        assert row[k] in ALLOWED, f"{k} out of domain: {row[k]}"
    total = row["direction"] + row["claims"] + row["timing"]
    assert row["total"] == total, f"total mismatch: {row}"
    assert row["pass"] == (total >= 4), f"pass mismatch: {row}"
    assert isinstance(row["reason"], str) and row["reason"]


def main():
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    packet_ids = [c["anon_id"] for c in packet]
    assert len(packet_ids) == 28 and len(set(packet_ids)) == 28

    if OUT.exists():
        raise SystemExit(f"refusing to overwrite existing output: {OUT}")

    written = 0
    seen = []
    with OUT.open("a", encoding="utf-8") as fh:
        for seg in SEGMENTS:
            lines = []
            for anon_id, d, c, t, reason in seg:
                row = {
                    "anon_id": anon_id,
                    "direction": d,
                    "claims": c,
                    "timing": t,
                    "total": d + c + t,
                    "pass": (d + c + t) >= 4,
                    "reason": reason,
                }
                check_row(row)
                lines.append(json.dumps(row, ensure_ascii=False))
                seen.append(anon_id)
            for line in lines:
                fh.write(line + "\n")
            fh.flush()
            written += len(lines)
            # per-segment on-disk assertion
            disk = OUT.read_text(encoding="utf-8").splitlines()
            assert len(disk) == written, f"line count after segment: {len(disk)} != {written}"
            for dl in disk:
                check_row(json.loads(dl))
            print(f"segment ok, cumulative lines={written}")

    disk_rows = [json.loads(l) for l in OUT.read_text(encoding="utf-8").splitlines()]
    assert len(disk_rows) == 28
    assert {r["anon_id"] for r in disk_rows} == set(packet_ids), "anon_id set mismatch vs packet"
    n_pass = sum(1 for r in disk_rows if r["pass"])
    means = {k: sum(r[k] for r in disk_rows) / 28 for k in ("direction", "claims", "timing")}
    print(f"FINAL lines=28 pass={n_pass} means={means} bytes={OUT.stat().st_size}")


if __name__ == "__main__":
    main()
