#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R79 holdout24 组集修订席：执行主持三项卡面裁处（QM-308 / QM-309 / QM-206）。
方式：对指定卡做原文字符串删除（保留其余字节格式），改前/改后均以结构化
比对断言核验——除指定字段外其余字段与改前逐字全等（deep equality），
指定字段须与预期值逐字全等；任一断言不过即中止、不写盘（先验后写）。
DS-019 / QM-207 为纯登记项，本脚本不触碰其卡。金标文件不触碰。
显式文件清单，无通配、无删除操作。
"""
import copy
import json
import os
import sys

BASE = '/home/hatch/workspace/divination/benchmark/phase3'
INPUTS = os.path.join(BASE, 'holdout24/inputs')

T308 = '「出走的妻子能平安回家」'
T308_BARE = '出走的妻子能平安回家'
CH308 = '行人走失预测'
T309 = '「弟弟有病手术后全愈」'
T309_BARE = '弟弟有病手术后全愈'
CH309 = '人体疾病预测'
Q206_KEEP = '求測者未明言來意，只說「最近我遇到了麻煩事，如果不說，你能測出來嗎？」'
Q206_DROP = '；劉自局中斷其女兒離家出走之事並斷歸期（書名節題為「為陳志勝預測女兒出走實例」）。'


def load(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    return raw, json.loads(raw)


def check_others_equal(before, after, changed_fields, cid):
    assert set(before.keys()) == set(after.keys()), f'{cid}: 字段集变化'
    for k in before:
        if k not in changed_fields:
            assert after[k] == before[k], f'{cid}: 非指定字段 {k} 被改动'
    return True


def main():
    report = {}

    # ---------- QM-308 ----------
    p308 = os.path.join(INPUTS, 'QM-308.json')
    raw_b, obj_b = load(p308)
    assert obj_b['setting'].count(T308) == 1, 'QM-308 setting 目标字样计数 != 1'
    assert obj_b['provenance'].count(T308) == 1, 'QM-308 provenance 目标字样计数 != 1'
    assert raw_b.count(T308) == 2, 'QM-308 全卡目标字样计数 != 2'
    raw_a = raw_b.replace(T308, '')
    obj_a = json.loads(raw_a)
    exp_setting = obj_b['setting'].replace(T308, '')
    exp_prov = obj_b['provenance'].replace(T308, '')
    assert obj_a['setting'] == exp_setting, 'QM-308 setting 改后值不合预期'
    assert obj_a['provenance'] == exp_prov, 'QM-308 provenance 改后值不合预期'
    assert CH308 in obj_a['setting'] and CH308 in obj_a['provenance'], 'QM-308 章节题未保留'
    assert T308_BARE not in raw_a, 'QM-308 例题字样改后仍残留'
    check_others_equal(obj_b, obj_a, {'setting', 'provenance'}, 'QM-308')
    report['QM-308'] = {
        'bytes_before': len(raw_b.encode('utf-8')),
        'bytes_after': len(raw_a.encode('utf-8')),
        'setting_before': obj_b['setting'], 'setting_after': obj_a['setting'],
        'provenance_before': obj_b['provenance'], 'provenance_after': obj_a['provenance'],
    }

    # ---------- QM-309 ----------
    p309 = os.path.join(INPUTS, 'QM-309.json')
    raw_b, obj_b = load(p309)
    assert obj_b['setting'].count(T309) == 1, 'QM-309 setting 目标字样计数 != 1'
    assert obj_b['provenance'].count(T309) == 1, 'QM-309 provenance 目标字样计数 != 1'
    assert raw_b.count(T309) == 2, 'QM-309 全卡目标字样计数 != 2'
    raw_a = raw_b.replace(T309, '')
    obj_a = json.loads(raw_a)
    exp_setting = obj_b['setting'].replace(T309, '')
    exp_prov = obj_b['provenance'].replace(T309, '')
    assert obj_a['setting'] == exp_setting, 'QM-309 setting 改后值不合预期'
    assert obj_a['provenance'] == exp_prov, 'QM-309 provenance 改后值不合预期'
    assert CH309 in obj_a['setting'] and CH309 in obj_a['provenance'], 'QM-309 章节题未保留'
    assert T309_BARE not in raw_a, 'QM-309 例题字样改后仍残留'
    check_others_equal(obj_b, obj_a, {'setting', 'provenance'}, 'QM-309')
    report['QM-309'] = {
        'bytes_before': len(raw_b.encode('utf-8')),
        'bytes_after': len(raw_a.encode('utf-8')),
        'setting_before': obj_b['setting'], 'setting_after': obj_a['setting'],
        'provenance_before': obj_b['provenance'], 'provenance_after': obj_a['provenance'],
    }

    # ---------- QM-206 ----------
    p206 = os.path.join(INPUTS, 'QM-206.json')
    raw_b, obj_b = load(p206)
    assert obj_b['question'] == Q206_KEEP + Q206_DROP, 'QM-206 question 改前值与裁处规格不合'
    assert raw_b.count(Q206_DROP) == 1, 'QM-206 全卡待删后段计数 != 1'
    raw_a = raw_b.replace(Q206_DROP, '')
    obj_a = json.loads(raw_a)
    assert obj_a['question'] == Q206_KEEP, 'QM-206 question 改后值 != 写定保留值'
    assert obj_a['setting'] == obj_b['setting'], 'QM-206 setting 被改动（裁处写定不动）'
    assert obj_a['provenance'] == obj_b['provenance'], 'QM-206 provenance 被改动（裁处写定不动）'
    check_others_equal(obj_b, obj_a, {'question'}, 'QM-206')
    report['QM-206'] = {
        'bytes_before': len(raw_b.encode('utf-8')),
        'bytes_after': len(raw_a.encode('utf-8')),
        'question_before': obj_b['question'], 'question_after': obj_a['question'],
        'setting': obj_b['setting'], 'provenance': obj_b['provenance'],
    }

    # 全部先验断言通过后才写盘
    writes = []
    # 重新计算三卡改后原文并写盘（与上方先验同一变换）
    for cid, path, transform in (
        ('QM-308', p308, lambda r: r.replace(T308, '')),
        ('QM-309', p309, lambda r: r.replace(T309, '')),
        ('QM-206', p206, lambda r: r.replace(Q206_DROP, '')),
    ):
        with open(path, encoding='utf-8') as f:
            cur = f.read()
        new = transform(cur)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new)
        writes.append(cid)

    # 写盘后复断言：自盘上重读，与报告中改后值逐字核对
    for cid, path in (('QM-308', p308), ('QM-309', p309), ('QM-206', p206)):
        _, obj_disk = load(path)
        rep = report[cid]
        if cid in ('QM-308', 'QM-309'):
            assert obj_disk['setting'] == rep['setting_after'], f'{cid} 盘上 setting 复核不合'
            assert obj_disk['provenance'] == rep['provenance_after'], f'{cid} 盘上 provenance 复核不合'
        else:
            assert obj_disk['question'] == rep['question_after'], 'QM-206 盘上 question 复核不合'
        assert len(open(path, 'rb').read()) == rep['bytes_after'], f'{cid} 盘上字节数复核不合'

    report['_assertions'] = 'PASS: 三卡除指定字段外其余字段与改前逐字全等（结构化 deep-equality 断言，先验后写、写后自盘复核）'
    report['_written'] = writes
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def load_text(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    sys.exit(main())
