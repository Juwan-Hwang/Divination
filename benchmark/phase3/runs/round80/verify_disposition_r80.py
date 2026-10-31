#!/usr/bin/env python3
"""R78-REV1 证伪处置验合（R80 判读处置席，独立角）：断言全过才算处置成立。

主持判读（已定，本脚本不重判）：R78-REV1 于 holdout24（N＝27）判读证伪
（DIR 证伪线触发），照写死条款删 SKILL (o) 指针回滚＋calibration 第七节
条文标失效存档。数值出处 runs/round80/acceptance/DIAG-H24.md §4 与
judging/final-scores-h24.json。

验合面（只读活 method 与 runs/round80/kb-snapshot-holdout25，不读预测/评分）：
1. 活 method 与封存快照在快照文件集上差异恰为 SKILL.md 与
   references/calibration.md 两文件，其余逐件 SHA-256 全等；
2. SKILL.md 与快照件差异恰为删去 (o) 指针一行（活件＝快照件删该行，
   其余逐字全等），(p) 指针保留；
3. calibration.md 与快照件差异恰为第七节内新增失效登记一段（删去该段
   后逐字全等；第八节等其余部分全等），登记段须含判读写死数值全文；
4. 六壬章 chinese-liuren.md 与快照 SHA 全等。
"""
import hashlib
import pathlib
import re
import sys

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
METHOD = BASE / 'method'
SNAP = BASE / 'runs/round80/kb-snapshot-holdout25'


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def rel_files(root: pathlib.Path):
    return sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file())


def main() -> int:
    # ---------- 1. 差异文件集恰为两文件，其余 SHA 全等 ----------
    snap_files = rel_files(SNAP)
    method_files = rel_files(METHOD)
    # 活 method 侧多出者只许是集成登记件（METHOD-INTEGRATION-*.md），不属知识库快照比对面
    extras = [f for f in method_files if f not in snap_files]
    assert all(re.fullmatch(r'METHOD-INTEGRATION-r\d+\.md', f) for f in extras), f'非登记件多出文件: {extras}'
    missing = [f for f in snap_files if f not in method_files]
    assert not missing, f'活 method 缺失快照文件: {missing}'

    differing = []
    for rel in snap_files:
        if sha_bytes((METHOD / rel).read_bytes()) != sha_bytes((SNAP / rel).read_bytes()):
            differing.append(rel)
    assert differing == ['SKILL.md', 'references/calibration.md'], f'差异文件集不符: {differing}'
    print(f'[1] OK 差异恰为两文件: {differing}；其余 {len(snap_files) - 2} 件 SHA-256 全等；活侧多出仅集成登记件: {extras}')

    # ---------- 2. SKILL.md 差异恰为删去 (o) 一行 ----------
    skill_live = (METHOD / 'SKILL.md').read_text(encoding='utf-8')
    skill_snap = (SNAP / 'SKILL.md').read_text(encoding='utf-8')
    snap_lines = skill_snap.split('\n')
    o_lines = [ln for ln in snap_lines if ln.startswith('- (o) ')]
    assert len(o_lines) == 1, f'快照 SKILL.md 中 (o) 指针行数异常: {len(o_lines)}'
    o_line = o_lines[0]
    assert 'R78-REV1' in o_line and '第七节' in o_line, f'(o) 指针行内容异常: {o_line}'
    o_idx = snap_lines.index(o_line)
    stripped = snap_lines[:o_idx] + snap_lines[o_idx + 1:]
    assert '\n'.join(stripped) == skill_live, 'SKILL.md 非「快照删去 (o) 一行」精确形态（其余部分非逐字全等或留有空行残迹）'
    live_lines = skill_live.split('\n')
    assert not any(ln.startswith('- (o) ') for ln in live_lines), '活 SKILL.md 仍残留 (o) 指针'
    p_lines_live = [ln for ln in live_lines if ln.startswith('- (p) ')]
    assert len(p_lines_live) == 1 and 'R80-REV1' in p_lines_live[0], '(p) 指针未保留或内容异常'
    assert live_lines.index(p_lines_live[0]) == o_idx, '(p) 指针未落在原 (o) 行位置（删除未整行或有移位）'
    print(f'[2] OK SKILL.md＝快照件删去 (o) 指针一行（原第 {o_idx + 1} 行），其余逐字全等、无空行残迹；(p) 指针保留不动')

    # ---------- 3. calibration.md 差异恰为第七节新增失效登记一段 ----------
    cal_live = (METHOD / 'references/calibration.md').read_text(encoding='utf-8')
    cal_snap = (SNAP / 'references/calibration.md').read_text(encoding='utf-8')
    live_cal_lines = cal_live.split('\n')
    reg_lines = [ln for ln in live_cal_lines if ln.startswith('**失效登记（R80 判读，')]
    assert len(reg_lines) == 1, f'活 calibration.md 中 R80 失效登记段行数异常: {len(reg_lines)}'
    reg = reg_lines[0]
    reg_idx = live_cal_lines.index(reg)
    # 定点：登记段必须位于第七节内（第七节标题之后、第八节标题之前），且前后为空行
    sec7_idx = next(i for i, ln in enumerate(live_cal_lines) if ln.startswith('## 七、'))
    sec8_idx = next(i for i, ln in enumerate(live_cal_lines) if ln.startswith('## 八、'))
    assert sec7_idx < reg_idx < sec8_idx, '失效登记段不在第七节内'
    assert live_cal_lines[reg_idx - 1] == '' and live_cal_lines[reg_idx + 1] == '', '失效登记段前后空行形态异常'
    # 登记段必含项（照主持判读结论与 DIAG-H24 §4 写死数值）
    required = [
        'runs/round80/acceptance/DIAG-H24.md §4',
        'holdout24', 'N＝27',
        'DIR 主码率 0.370（10/27，线 ≤0.100）', '证伪线 ≥0.340',
        'TIM＋CLAIM 名义 0.519（14/27）／实质 0.444（12/27，线 ≤0.370）',
        'OMIT 主码率 0.000（0/27）', '护栏未破',
        '总配对差 −0.935', '≥−1.837', '≤−2.193',
        '判读**证伪**', 'DIR 证伪线触发',
        'SKILL (o) 指针照证伪条款删除回滚',
        '自 R81 起标失效存档、不再强制执行，原文保留备查',
        '后续修订须基于再下一份聚合诊断另行提案、另立编号',
    ]
    for item in required:
        assert item in reg, f'失效登记段缺少必含项: {item}'
    # 删去登记段（登记行＋其后空行）后逐字还原快照——第八节等其余部分全等由此一并断言
    stripped_cal = live_cal_lines[:reg_idx] + live_cal_lines[reg_idx + 2:]
    assert '\n'.join(stripped_cal) == cal_snap, 'calibration.md 删去失效登记段后与快照不逐字全等'
    print(f'[3] OK calibration.md＝快照件＋第七节失效登记一段（第 {reg_idx + 1} 行，{len(reg)} 字符），删去该段后逐字还原快照；第八节等其余部分全等；登记段必含项 {len(required)} 项全在')

    # ---------- 4. 六壬章冻结 ----------
    lr_live = sha_bytes((METHOD / 'references/chinese-liuren.md').read_bytes())
    lr_snap = sha_bytes((SNAP / 'references/chinese-liuren.md').read_bytes())
    assert lr_live == lr_snap, '六壬章与快照 SHA 不等（冻结被破）'
    print(f'[4] OK 六壬章 chinese-liuren.md SHA 全等: {lr_live}')

    print('ALL CHECKS PASSED')
    return 0


if __name__ == '__main__':
    sys.exit(main())
