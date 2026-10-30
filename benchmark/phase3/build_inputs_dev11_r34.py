# -*- coding: utf-8 -*-
"""
build_inputs_dev11_r34.py — 组 inputs-dev11（R34 预注册 §6.③ 数据卫生·口径切换立项）

底本 benchmark/phase3/inputs-dev10/（487 件 .json，逐字复制），仅按
benchmark/phase3/input-audit/CORRECTIONS.md 对 6 例落改：
  LY-006、LY-010、LY-105、YY2-001、YY2-002、YY2-005。
纠正值以 CORRECTIONS.md 表格为准绳；字段级细节以 input-audit/verify-V1.json、
verify-V2.json、verify-V3.json 对应例证据值为准。本脚本先做两源一致性断言，
再以「原文文本级替换」落改（每处旧文本须在文件内恰出现 1 次），保 6 个改动
文件内未改字段逐字不变；其余 481 件字节复制。
自验：文件数、与 inputs-dev10 逐文件 SHA-256 比对（恰 6 件不同）、6 件的
JSON 深比对差异路径恰为声明字段、改后字段值与证据值逐项相等。
不改 inputs-dev10 与任何既有原件；产出仅 inputs-dev11/ 与其内 BUILD-MANIFEST.md。
口径切换登记见产出 BUILD-MANIFEST.md：自 R35 起输入口径为 inputs-dev11、
一切合读池资格重置、R33/R34 合读关系终止于 R34；本切换只作数据卫生、不包装增益。
"""
import hashlib
import json
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE / "inputs-dev10"
DST = BASE / "inputs-dev11"
AUDIT = BASE / "input-audit"

CHANGED_IDS = ["LY-006", "LY-010", "LY-105", "YY2-001", "YY2-002", "YY2-005"]

# ---- 声明的落改（old_text -> new_text，原文文本级；均取自 CORRECTIONS/verify 证据）----
# LY-006：moving_lines 补「上爻子孫巳火○動」，动位 [1,4,5]->[1,4,5,6]（CORRECTIONS 表 + V1）
LY006_OLD = "初爻父母子水○、四爻官鬼酉金○、五爻妻財未土ㄨ（世）動"
LY006_NEW = "初爻父母子水○、四爻官鬼酉金○、五爻妻財未土ㄨ（世）動、上爻子孫巳火○動"
# LY-010：moving_lines「五爻父母未土ㄨ（世）」改「上爻父母未土ㄨ（世）」，动位 [1,5]->[1,6]（CORRECTIONS 表 + V1）
LY010_OLD = "五爻父母未土ㄨ（世）"
LY010_NEW = "上爻父母未土ㄨ（世）"
# LY-105：attachments.空亡「寅卯」改「子丑」（CORRECTIONS 表 + V1）
LY105_OLD = '"空亡": "寅卯"'
LY105_NEW = '"空亡": "子丑"'

def chart_block(lines):
    inner = ",\n".join(f'        "{s}"' for s in lines)
    return f'"chart_lines_top_to_bottom": [\n{inner}\n      ]'

# YY2-001：chart_lines 全 6 爻按水澤節（坎宫一世）标准装卦（V2 corrected_chart_top_to_bottom）
YY2001_OLD = ["官鬼丁丑土", "父母丁酉金", "妻财丁巳火 应", "父母戊申金", "官鬼戊辰土", "子孙戊寅木 世"]
YY2001_NEW = ["兄弟戊子水", "官鬼戊戌土", "父母戊申金 应", "官鬼丁丑土", "子孙丁卯木", "妻财丁巳火 世"]
# YY2-002：chart_lines 全 6 爻按地水師（坎宫歸魂）标准装卦（V2 corrected_chart_top_to_bottom）
YY2002_OLD = ["妻财戊午火 应", "官鬼戊戌土", "兄弟戊子水", "子孙乙卯木 世", "妻财乙巳火", "官鬼乙未土"]
YY2002_NEW = ["父母癸酉金 应", "兄弟癸亥水", "官鬼癸丑土", "妻财戊午火 世", "官鬼戊辰土", "子孙戊寅木"]
# YY2-005：chart_lines 上三爻改（下三爻不变）：六爻官鬼癸酉金、五爻父母癸亥水、四爻妻财癸丑土 世（CORRECTIONS 表 + V3）
YY2005_OLD = ["兄弟乙卯木", "子孙乙巳火", "妻财乙未土 世", "官鬼辛酉金", "父母辛亥水", "妻财辛丑土 应"]
YY2005_NEW = ["官鬼癸酉金", "父母癸亥水", "妻财癸丑土 世", "官鬼辛酉金", "父母辛亥水", "妻财辛丑土 应"]

REPLACEMENTS = {
    "LY-006": [(LY006_OLD, LY006_NEW)],
    "LY-010": [(LY010_OLD, LY010_NEW)],
    "LY-105": [(LY105_OLD, LY105_NEW)],
    "YY2-001": [(chart_block(YY2001_OLD), chart_block(YY2001_NEW))],
    "YY2-002": [(chart_block(YY2002_OLD), chart_block(YY2002_NEW))],
    "YY2-005": [(chart_block(YY2005_OLD), chart_block(YY2005_NEW))],
}

# 改后语义期望（深比对用）
EXPECTED_FIELDS = {
    "LY-006": ("moving_lines", LY006_NEW),
    "LY-010": ("moving_lines", "初爻官鬼巳火○、上爻父母未土ㄨ（世）動"),
    "LY-105": ("空亡", "子丑"),
    "YY2-001": ("chart_lines_top_to_bottom", YY2001_NEW),
    "YY2-002": ("chart_lines_top_to_bottom", YY2002_NEW),
    "YY2-005": ("chart_lines_top_to_bottom", YY2005_NEW),
}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def deep_diff(a, b, path=""):
    out = []
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        for k in sorted(set(a) | set(b)):
            out += deep_diff(a.get(k), b.get(k), f"{path}.{k}")
    elif isinstance(a, list):
        if len(a) != len(b):
            out.append(path)
        else:
            for i, (x, y) in enumerate(zip(a, b)):
                out += deep_diff(x, y, f"{path}[{i}]")
    elif a != b:
        out.append(path)
    return out


def check_evidence_consistency():
    """CORRECTIONS.md 与 verify-V1/V2/V3 两源一致性断言；不一致即停手。"""
    corr = (AUDIT / "CORRECTIONS.md").read_text(encoding="utf-8")
    for cid in CHANGED_IDS:
        assert cid in corr, f"CORRECTIONS.md 未载 {cid}"
    v1 = {c["id"]: c for c in json.loads((AUDIT / "verify-V1.json").read_text(encoding="utf-8"))["cases"]}
    v2 = {c["id"]: c for c in json.loads((AUDIT / "verify-V2.json").read_text(encoding="utf-8"))["cases"]}
    v3 = {c["id"]: c for c in json.loads((AUDIT / "verify-V3.json").read_text(encoding="utf-8"))["cases"]}
    # LY-006 / LY-010 / LY-105（V1）
    s = v1["LY-006"]["discrepancies"][0]["source_value"]
    assert "上爻子孫巳火○" in s and "[1,4,5,6]" in s and "上爻子孫巳火○動" in corr, "LY-006 两源不一致"
    s = v1["LY-010"]["discrepancies"][0]["source_value"]
    assert "上爻" in s and "[1,6]" in s and "上爻父母未土ㄨ（世）" in corr, "LY-010 两源不一致"
    s = v1["LY-105"]["discrepancies"][0]["source_value"]
    assert s.startswith("子丑") and "「子丑」" in corr, "LY-105 两源不一致"
    # YY2-001 / YY2-002（V2 corrected_chart 与本脚本声明逐字相等；CORRECTIONS 指向 V2）
    assert v2["YY2-001"]["corrected_chart_top_to_bottom"] == YY2001_NEW, "YY2-001 与 V2 corrected_chart 不一致"
    assert v2["YY2-002"]["corrected_chart_top_to_bottom"] == YY2002_NEW, "YY2-002 与 V2 corrected_chart 不一致"
    # YY2-005（V3 三条 source_value 与 CORRECTIONS 表三值对应）
    sv = [d["source_value"] for d in v3["YY2-005"]["discrepancies"]]
    assert "妻财癸丑土 世" in sv[0] and "父母癸亥水" in sv[1] and "官鬼癸酉金" in sv[2], "YY2-005 与 V3 不一致"
    assert "癸丑" in corr and "癸亥" in corr and "癸酉" in corr, "YY2-005 与 CORRECTIONS 不一致"


def main() -> None:
    check_evidence_consistency()

    src_files = sorted(SRC.glob("*.json"))
    assert len(src_files) == 487, f"底本 {len(src_files)} 件"

    if DST.exists():
        shutil.rmtree(DST)
    DST.mkdir(parents=True)
    for p in src_files:
        shutil.copyfile(p, DST / p.name)

    # 落改：原文文本级替换，每处旧文本恰出现 1 次
    for cid, reps in REPLACEMENTS.items():
        p = DST / f"{cid}.json"
        text = p.read_text(encoding="utf-8")
        for old, new in reps:
            assert text.count(old) == 1, f"{cid}：旧文本出现 {text.count(old)} 次（须恰 1 次）"
            text = text.replace(old, new)
        p.write_text(text, encoding="utf-8")

    # 自验 1：文件数与文件名集
    out_files = sorted(DST.glob("*.json"))
    assert len(out_files) == 487, f"产出 {len(out_files)} 件"
    assert [p.name for p in out_files] == [p.name for p in src_files], "文件名集与底本不一致"

    # 自验 2：逐文件 SHA-256 比对——恰 6 件不同、其余 481 件逐字一致
    diff_ids, same_n = [], 0
    for p in out_files:
        if sha(p.read_bytes()) != sha((SRC / p.name).read_bytes()):
            diff_ids.append(p.stem)
        else:
            same_n += 1
    assert sorted(diff_ids) == sorted(CHANGED_IDS), f"diff 集 {sorted(diff_ids)} != 声明 6 例"
    assert same_n == 481, f"逐字一致 {same_n} 件（须 481）"

    # 自验 3：6 件 JSON 深比对——差异路径恰为声明字段；改后值与证据期望逐项相等
    diff_paths = {}
    for cid in CHANGED_IDS:
        a = json.loads((SRC / f"{cid}.json").read_text(encoding="utf-8"))
        b = json.loads((DST / f"{cid}.json").read_text(encoding="utf-8"))
        paths = deep_diff(a, b)
        field, expected = EXPECTED_FIELDS[cid]
        att_b = b["context"]["attachments"]
        assert att_b[field] == expected, f"{cid}：改后 {field} 与证据期望不符"
        assert paths and all(field in x for x in paths), f"{cid}：差异路径越界 {paths}"
        diff_paths[cid] = paths

    # ---- BUILD-MANIFEST.md（体例同 inputs-dev10/BUILD-MANIFEST.md）----
    md = []
    md.append("# inputs-dev11 · BUILD-MANIFEST（R34 §6.③ 数据卫生·口径切换，数据角交付 2026-10-30）")
    md.append("")
    md.append("- 底本：`benchmark/phase3/inputs-dev10/`（487 件 `.json`）；产出：本目录 487 件 `.json`＋本清单。")
    md.append("- 组集脚本：`benchmark/phase3/build_inputs_dev11_r34.py`（本批唯一新脚本，保留在案）。")
    md.append("- 立项依据：`benchmark/phase3/runs/round34/PREREG.md` §6.③（与方法轮分离的数据卫生立项，R34 分析定稿后执行）；纠正准绳：`benchmark/phase3/input-audit/CORRECTIONS.md`（6 例 A 类定案）；字段级证据：`input-audit/verify-V1.json`（LY-006、LY-010、LY-105）、`verify-V2.json`（YY2-001、YY2-002）、`verify-V3.json`（YY2-005）。构建前已断言 CORRECTIONS 与三份 verify 证据值逐项一致、无冲突。")
    md.append("- 落改方式：逐字复制底本后，仅对下 6 例作原文文本级替换（每处旧文本在文件内恰出现 1 次才许替换）；6 个改动文件内未改字段逐字不变，其余 481 件与底本逐字（SHA-256）一致。")
    md.append(f"- diff（vs inputs-dev10）：**6 例**，全部落在 CORRECTIONS 声明集内；其余 **481 例**逐字一致。")
    md.append("")
    md.append("## 6 例逐例 diff（字段 · 旧值 · 新值 · 证据文件）")
    md.append("")
    md.append(f"- LY-006 · 字段 `context.attachments.moving_lines` · 旧值「{LY006_OLD}」· 新值「{LY006_NEW}」· 补「上爻子孫巳火○動」、动位 [1,4,5]→[1,4,5,6] · 证据：CORRECTIONS.md 表 LY-006 行＋verify-V1.json（源本盘面与断语「巳火子動而生世」互证）· 改后 SHA-256 前 12 位 {sha((DST / 'LY-006.json').read_bytes())[:12]}（底本 {sha((SRC / 'LY-006.json').read_bytes())[:12]}）。")
    md.append(f"- LY-010 · 字段 `context.attachments.moving_lines` · 旧值「初爻官鬼巳火○、五爻父母未土ㄨ（世）動」· 新值「初爻官鬼巳火○、上爻父母未土ㄨ（世）動」· 动位 [1,5]→[1,6] · 证据：CORRECTIONS.md 表 LY-010 行＋verify-V1.json（源本盘面未土ㄨ世在上爻）· 改后 SHA-256 前 12 位 {sha((DST / 'LY-010.json').read_bytes())[:12]}（底本 {sha((SRC / 'LY-010.json').read_bytes())[:12]}）。")
    md.append(f"- LY-105 · 字段 `context.attachments.空亡` · 旧值「寅卯」· 新值「子丑」· 证据：CORRECTIONS.md 表 LY-105 行＋verify-V1.json（卡面 setting 自载「壬戌日（子丑空）」、壬戌属甲寅旬空子丑）· 改后 SHA-256 前 12 位 {sha((DST / 'LY-105.json').read_bytes())[:12]}（底本 {sha((SRC / 'LY-105.json').read_bytes())[:12]}）。范围注记：本次仅改 `attachments.空亡` 值字段；`notes.completion_grade` 中关于该字段补录依据的历史记录文字未改（属补录过程记录、非输入字段）。")
    md.append(f"- YY2-001 · 字段 `context.attachments.chart_lines_top_to_bottom`（全 6 爻，自上而下）· 旧值 {'／'.join(YY2001_OLD)} · 新值 {'／'.join(YY2001_NEW)} · 按水澤節（坎宫一世）标准装卦逐爻改 · 证据：CORRECTIONS.md 表 YY2-001 行（纠正值见 V2）＋verify-V2.json `corrected_chart_top_to_bottom`（与新值逐字相等、脚本已断言）· 改后 SHA-256 前 12 位 {sha((DST / 'YY2-001.json').read_bytes())[:12]}（底本 {sha((SRC / 'YY2-001.json').read_bytes())[:12]}）。")
    md.append(f"- YY2-002 · 字段 `context.attachments.chart_lines_top_to_bottom`（全 6 爻，自上而下）· 旧值 {'／'.join(YY2002_OLD)} · 新值 {'／'.join(YY2002_NEW)} · 按地水師（坎宫歸魂）标准装卦逐爻改 · 证据：CORRECTIONS.md 表 YY2-002 行（纠正值见 V2）＋verify-V2.json `corrected_chart_top_to_bottom`（与新值逐字相等、脚本已断言）· 改后 SHA-256 前 12 位 {sha((DST / 'YY2-002.json').read_bytes())[:12]}（底本 {sha((SRC / 'YY2-002.json').read_bytes())[:12]}）。")
    md.append(f"- YY2-005 · 字段 `context.attachments.chart_lines_top_to_bottom`（仅上三爻，自上而下为六爻／五爻／四爻）· 旧值 兄弟乙卯木／子孙乙巳火／妻财乙未土 世 · 新值 官鬼癸酉金／父母癸亥水／妻财癸丑土 世（下三爻 官鬼辛酉金／父母辛亥水／妻财辛丑土 应 不变）· 上卦坤误按内卦序装、改按外卦序癸酉亥丑 · 证据：CORRECTIONS.md 表 YY2-005 行＋verify-V3.json 三条 discrepancies（四爻妻财癸丑土 世、五爻父母癸亥水、六爻官鬼癸酉金）· 改后 SHA-256 前 12 位 {sha((DST / 'YY2-005.json').read_bytes())[:12]}（底本 {sha((SRC / 'YY2-005.json').read_bytes())[:12]}）。")
    md.append("")
    md.append("## 口径切换登记")
    md.append("")
    md.append("- 自 **R35** 起，输入口径为 **inputs-dev11**（本目录）；inputs-dev10 口径终止于 R34。")
    md.append("- **一切合读池资格重置**：R33/R34 依「inputs-dev10 与前轮逐字不变」成立的合读关系**终止于 R34**，不延伸至 inputs-dev11；R35 起任何合读资格须按新口径另行预注册声明。")
    md.append("- 本切换**只作数据卫生、不包装增益**：6 例均为输入转录/复原错误的勘误落改，非方法改进；其收益上限约 +0.10 且存疑（R34 PREREG §6.③ 在案），不得引作方法增益证据。")
    md.append("- 本立项与方法轮分离：未改动 `method/` 与任何 `runs/` 目录，未改动 inputs-dev10 任何文件；本轮（R34）一切读数与判据不受本切换影响。")
    md.append("")
    md.append("## 自验")
    md.append("")
    md.append("- 文件数：inputs-dev11 内 `.json` **487** 件＋本清单 `BUILD-MANIFEST.md` 1 件；文件名集与 inputs-dev10 逐一相等。")
    md.append("- 逐文件比对方法：对 inputs-dev10 与 inputs-dev11 同名 `.json` 逐一计算 SHA-256 全等判定（脚本 `build_inputs_dev11_r34.py` 自验 2）。结果：**恰 6 件不同**（即上 6 例）、**其余 481 件逐字一致**。")
    md.append("- 字段级核对：6 件改后经 JSON 深比对，差异路径恰落在声明字段内（LY-006/LY-010 为 `moving_lines`、LY-105 为 `空亡`、YY2 三例为 `chart_lines_top_to_bottom`），无越界改动；改后值与 CORRECTIONS/verify 证据值逐项相等（构建前两源一致性断言＋构建后语义断言均通过）。")
    md.append("- 与 CORRECTIONS.md 逐条对应：6 行表格（LY-006、LY-010、LY-105、YY2-001、YY2-002、YY2-005）与上 diff 登记一一对应，无遗漏、无额外例。")
    md.append("")
    (DST / "BUILD-MANIFEST.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"files={len(out_files)} diff={len(diff_ids)} same={same_n}")
    for cid in CHANGED_IDS:
        print(cid, "diff_paths=", diff_paths[cid])


if __name__ == "__main__":
    main()
