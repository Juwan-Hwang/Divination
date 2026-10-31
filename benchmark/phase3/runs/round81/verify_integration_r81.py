#!/usr/bin/env python3
"""R81-REV1 集成验合（独立集成席）：断言全过才算集成成立。

验合面（只读活 method、runs/round81/kb-snapshot 与提案正本，不读 judging/ 与金标）：
1. 活 method 与 kb-snapshot 在快照文件集（21 文件）上差异恰为 SKILL.md 与 references/calibration.md 两文件，其余逐件 SHA-256 全等；
2. strip-back 精确：calibration.md 删去新增第九节后与快照件逐字全等；SKILL.md 删去 (q) 指针一行后与快照件逐字全等；
3. 新增条文与提案 §四条文段逐字比对（自提案文件抽取该段，断言包含且为 calibration 后缀全文）；
4. 六壬章 chinese-liuren.md 与快照件 SHA 全等（冻结零改动）。
"""
import hashlib
import pathlib
import re
import sys

BASE = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
METHOD = BASE / 'method'
SNAP = BASE / 'runs/round81/kb-snapshot'
PROPOSAL = BASE / 'runs/round81/revision/PROPOSAL-R81-REV1.md'


def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def rel_files(root: pathlib.Path):
    return sorted(p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file())


def main() -> int:
    # ---------- 1. 差异文件集恰为两文件，其余 SHA 全等 ----------
    snap_files = rel_files(SNAP)
    assert len(snap_files) == 21, f'快照文件集应为 21 件，实得 {len(snap_files)}: {snap_files}'
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
    print(f'[1] OK 快照文件集 21 件；差异恰为两文件: {differing}；其余 {len(snap_files) - 2} 件 SHA-256 全等；活侧多出仅集成登记件: {extras}')

    # ---------- 提案 §四条文段抽取（第九节全文） ----------
    prop = PROPOSAL.read_text(encoding='utf-8')
    start = prop.index('## 九、初判方向锚定')
    boundary = prop.index('\n\n---\n', start)
    section = prop[start:boundary]
    assert section.startswith('## 九、初判方向锚定与变更门槛核')
    assert section.endswith('不改五段格式。')
    assert 'R81-REV1-7' in section
    assert '涉测字段' not in section, '提案层「涉测字段相容陈述」误入条文段'
    assert '六壬章冻结自证' not in section, '提案层「六壬章冻结自证」误入条文段'
    assert '（集成登记：提案 runs/round81/revision/PROPOSAL-R81-REV1.md' in section

    # (q) 指针一行自提案 §四拟文抽取
    q_lines = [ln for ln in prop.splitlines() if ln.startswith('- (q) ')]
    assert len(q_lines) == 1, f'提案 (q) 指针行数异常: {len(q_lines)}'
    q_line = q_lines[0]

    # ---------- 2+3. calibration strip-back 与逐字比对 ----------
    cal_live = (METHOD / 'references/calibration.md').read_text(encoding='utf-8')
    cal_snap = (SNAP / 'references/calibration.md').read_text(encoding='utf-8')
    assert section in cal_live, 'calibration.md 未包含提案 §四条文段'
    suffix = '\n' + section + '\n'
    assert cal_live == cal_snap + suffix, 'calibration.md 非「快照＋空行＋第九节后缀」精确形态（纯后缀追加）'
    stripped_cal = cal_live[:-len(suffix)]
    assert stripped_cal == cal_snap, 'calibration strip-back 后与快照不逐字全等'
    assert cal_live.count('## 九、初判方向锚定与变更门槛核') == 1, '第九节出现次数异常'
    print(f'[2] OK calibration 为纯后缀追加，strip-back 逐字还原快照；新增第九节 {len(section)} 字符 / {section.count(chr(10)) + 1} 行，与提案 §四抽取段逐字一致且为文件后缀')

    # ---------- 2. SKILL strip-back ----------
    skill_live = (METHOD / 'SKILL.md').read_text(encoding='utf-8')
    skill_snap = (SNAP / 'SKILL.md').read_text(encoding='utf-8')
    live_lines = skill_live.split('\n')
    assert live_lines.count(q_line) == 1, 'SKILL.md 中 (q) 指针行数异常'
    q_idx = live_lines.index(q_line)
    p_idx = next(i for i, ln in enumerate(live_lines) if ln.startswith('- (p) '))
    assert q_idx == p_idx + 1, '(q) 指针未紧接 (p) 之后'
    del live_lines[q_idx]
    assert '\n'.join(live_lines) == skill_snap, 'SKILL strip-back 后与快照不逐字全等'
    print('[3] OK SKILL strip-back 逐字还原快照；(q) 指针紧接 (p) 之后一行，逐字同提案 §四拟文')

    # ---------- 4. 六壬章冻结 ----------
    lr_live = sha_bytes((METHOD / 'references/chinese-liuren.md').read_bytes())
    lr_snap = sha_bytes((SNAP / 'references/chinese-liuren.md').read_bytes())
    assert lr_live == lr_snap, '六壬章与快照 SHA 不等（冻结被破）'
    print(f'[4] OK 六壬章 chinese-liuren.md SHA 全等（冻结零改动）: {lr_live}')

    print('ALL CHECKS PASSED')
    return 0


if __name__ == '__main__':
    sys.exit(main())
