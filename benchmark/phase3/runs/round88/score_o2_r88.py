#!/usr/bin/env python3
"""R88 acceptance judge O2 (second view), ours packet only, 28 cases.
Scores per frozen rubric: direction/claims/timing each 0-2 step 0.5,
total=sum, pass=total>=4. Outcome with no verifiable time point ->
timing=1 with note in reason. Writes judgeO2.jsonl in 4 appended segments
of 7 with assertions after each segment.
"""
import json
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3/runs/round88")
PACKET = BASE / "acceptance" / "judging" / "packet-ours.json"
OUT = BASE / "acceptance" / "judging" / "judgeO2.jsonl"

# (anon_id, direction, claims, timing, reason)
ROWS = [
    ("H31O-01ab0367", 1, 1, 1, "往行遇贼劫而避杨家颇安，有惊无大祸一面合，不成行或折返未被结局证实，破财亦未载；应期未日无从与四月初八对核，结局无可核时点"),
    ("H31O-0741328c", 0.5, 0.5, 0, "果不能赴广南任、仅授潭州岳庙，后己酉中举庚戌登科，非所断武职末路一任位不高任不久；应期巳年与己酉庚戌不合"),
    ("H31O-12d9d65f", 0, 0.5, 0, "初授抚州教官仅起点合，其后屡迁至司农少卿淮西总领，止于教职十五年无升迁全翻；应期十五年止局不合"),
    ("H31O-1c716404", 2, 1.5, 0, "结局称果如所测、胎动实现，胎儿平安方向合；原神生扶等子断语未被结局逐条记载不给满分；应期卯日与未月胎动不合"),
    ("H31O-1d878e94", 2, 1.5, 0, "本月安全生下女孩，能产与性别女均合；伏藏受压等子断语未被结局逐条记载不给满分；应期主坐标午月不合，实际本月庚子日巳时产"),
    ("H31O-29054a97", 2, 1.5, 1, "马上回办公室在写字台下找回一百元，钱寻回方向合；线索落点等子断语未被结局逐条记载不给满分；结局仅言马上、无干支日期，结局无可核时点"),
    ("H31O-35840ea8", 1, 1, 0, "四月见劫耗与虚惊耗损一面相涉，但家宅安稳吉多于凶未被结局证实；应期主坐标亥月与四月不合"),
    ("H31O-3a60f30b", 0, 1, 1, "先因案件羁累迟滞一节合，但终局不能进京、改调松江且不待引见，进京得遂落定全翻；结局无月份日期，结局无可核时点"),
    ("H31O-49278fa1", 1, 1, 0, "当月生下女孩，生产与性别合，但生时难产与顺利生产相悖；应期窗口申酉月不合，实际当月辛未日产"),
    ("H31O-4a894774", 1.5, 1, 2, "亥月剖腹产下，生产保全与产程不顺之惊合，惟性别断女误为男孩；应期主坐标亥月正合"),
    ("H31O-51cf034f", 2, 1.5, 2, "子月生下女孩，生女终局合；回头生等子断语未被结局逐条记载不给满分；应期主坐标子月正合"),
    ("H31O-5eeda1d8", 0.5, 0.5, 1, "结局为弟屡见官非逃亡见火，年运先虚后安小有所得终无大失不合，仅虚惊火扰一面相涉；结局无可核时点（仅言前一日），结局无可核时点"),
    ("H31O-602985b9", 0.5, 1, 1, "阻服未升迁一程合，但服满后授黄州推官，不再迁转之断翻，病归卒一节与运尽相涉；结局仅载十二月无年份干支，结局无可核时点"),
    ("H31O-7f7a0769", 1.5, 0.5, 1, "果为恶性癌症、病重方向合，但癌在鼻不在肝胆，癌种定位误；结局无时点，结局无可核时点"),
    ("H31O-80f8f738", 2, 1.5, 1, "查得子宫瘤在下腹盆腔区、服中药而愈，良性可治方向合；病势缠绵等子断语未被结局逐条记载不给满分；结局无可核时点"),
    ("H31O-8c1aca9e", 2, 1.5, 1, "小儿仅呛奶啼哭、疑肺炎结果不是，病无实根可愈合；反复缠绵等子断语未被结局逐条记载不给满分；结局无时点，结局无可核时点"),
    ("H31O-9607ab37", 0, 0, 0, "徐屡授岳州尉浑州尉复州司户提学干官东莞县令终于任上，终身无做官之断全翻；其后仕进持续，应期局定之说不合"),
    ("H31O-9761d2b3", 0.5, 0.5, 0, "结局仅携眷至天门寄寓、未证回省，次年货船被抢与惊扰一面相涉；应期本旬子日回省与次年二月情节不合"),
    ("H31O-b16dbb7c", 0, 0, 0, "壬戌年二月坠轿折足而死，无升迁得任记录，前程有成官至中品全翻；应期迁转落定不合"),
    ("H31O-b4ac871c", 0, 1, 0, "工作没调动成、后内退，调得成之终局翻；单位处境与迟滞一节结局称正如所测；应期酉月调成不合"),
    ("H31O-bd9dd94c", 2, 1.5, 0, "果信不能通，终局合；机关难明等子断语未被结局逐条记载不给满分；结局自注原断宜为久远者则误，本旬丑日短档应期不合"),
    ("H31O-c5209c90", 0, 0, 1, "医院检查发现怀孕并流产，未怀孕之断全翻；结局无时点，结局无可核时点"),
    ("H31O-d033997b", 1.5, 1.5, 0, "生男孩且难产，保胎生产男与有惊合；冲合解绊等子断语未被结局逐条记载不给满分；应期戌亥月不合，实际二月五日产"),
    ("H31O-d5de0d3a", 1, 0.5, 0.5, "午月生下女孩，生产一节合但性别断男误、顺利生产未被结局证实；应期主坐标丑月误、仅丁丑日丑字一面相涉"),
    ("H31O-dc842d83", 1, 1, 0, "次年贼破省黄陂失守，任运耗失凶象一面合且更重，宅广人衰无迁擢未被结局记载；应期一年内戌月与次年酉不合"),
    ("H31O-f0003e66", 0, 0.5, 0, "徐得县令正任后历通判知州御史吏部侍郎，无正官终老教职全翻，仅中途任诸王府教授一节相涉；应期六年定局不合"),
    ("H31O-fb6db324", 1.5, 1, 1, "龚终局满替得归、无正式升转，与宜守无成大体合，但曾权署主簿一节与止于县尉相悖，受贿被论告与谋迁反滞合；结局无年份时点，结局无可核时点"),
    ("H31O-ffc78672", 1.5, 1, 1, "午时取衣、修改后取走，取衣可成合而争执非所断、裁缝会到仅部分合；结局仅载午时无日干支，结局无可核时点"),
]

packet = json.loads(PACKET.read_text(encoding="utf-8"))
assert isinstance(packet, list) and len(packet) == 28, f"packet n={len(packet)}"
packet_ids = [c["anon_id"] for c in packet]
assert [r[0] for r in ROWS] == packet_ids, "anon order/set mismatch with packet"

def check(rec, lineno):
    assert set(rec.keys()) == {"anon_id", "direction", "claims", "timing", "total", "pass", "reason"}, rec
    for k in ("direction", "claims", "timing"):
        v = rec[k]
        assert 0 <= v <= 2 and (v * 2) == int(v * 2), (k, v)
    assert rec["total"] == rec["direction"] + rec["claims"] + rec["timing"], rec
    assert rec["pass"] == (rec["total"] >= 4), rec
    assert isinstance(rec["reason"], str) and rec["reason"], rec

records = []
for anon, d, c, t, reason in ROWS:
    rec = {"anon_id": anon, "direction": d, "claims": c, "timing": t,
           "total": d + c + t, "pass": (d + c + t) >= 4, "reason": reason}
    check(rec, len(records) + 1)
    records.append(rec)

# segmented append: 4 segments x 7, truncate-by-open('w') only at start on fresh file
assert not OUT.exists(), "output already exists; refusing to overwrite"
written = 0
for seg in range(4):
    chunk = records[seg * 7:(seg + 1) * 7]
    assert len(chunk) == 7
    with OUT.open("a", encoding="utf-8") as f:
        for rec in chunk:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    written += 7
    lines = OUT.read_text(encoding="utf-8").splitlines()
    assert len(lines) == written, f"seg {seg}: lines={len(lines)} expected={written}"
    for i, line in enumerate(lines):
        check(json.loads(line), i + 1)
    print(f"segment {seg + 1}: cumulative lines={len(lines)} OK")

lines = OUT.read_text(encoding="utf-8").splitlines()
assert len(lines) == 28
final = [json.loads(x) for x in lines]
assert [r["anon_id"] for r in final] == packet_ids
npass = sum(1 for r in final if r["pass"])
means = {k: round(sum(r[k] for r in final) / 28, 4) for k in ("direction", "claims", "timing")}
print(f"FINAL lines=28 pass={npass} means={means} bytes={OUT.stat().st_size}")
