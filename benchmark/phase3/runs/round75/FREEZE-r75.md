# FREEZE-r75 — R75 盲测冻结记录

（主持角，2026-10-31。预注册：runs/round75/PREREG.md；匿名种子 20261081。本件冻结后方许构建评审包。）

## 一、验盘（主持盘上复算）

- verify_predictions_host_r75.py：487/487 全在盘，缺失 0、额外 0、结构坏件 0（case_id/prediction_text/basis/confidence/systems_used/trigger 结构全检通过）。
- 六爻 trigger 主持复算：changed_main＝24、reserve_used＝42、disputed＝69；与十席回传分项和逐值全等（24/42/69）。
- 方法零改动：kb-snapshot 21 件 SHA-256 与 round74 快照逐件全等。

## 二、tradition 检查与裁定（承 R74 覆盖缺口判例）

- check_tradition_host_r75.py 初检：direct 365、none-labelled 98、flags 24；声明组数加扫：声明组 0、冲突组 0。
- flags 24 件逐件裁定：首行均明写卡面未载/未见 tradition 字段（如实注明），主持逐件回读卡面定案——24/24 卡面确无 tradition/system 字段（MP-002/004/006/008/010/012/014/016/018、OC-003/007/010/012/015/017/021/025/028、WP-001/002/003/004/006/007）。全数属检查器关键词覆盖缺口，裁定不成立为席位错误，不作废不重测，实效归 none-labelled。
- 实效分布：direct 365 / none-labelled 122 / flags 0——与 R74 冻结实效分布（365/122/0）逐值相同，跨轮可比性成立。

## 三、本轮隔离与自报事项登记（详见 ADDENDUM-r75）

- BZ-019 卡面 setting 内嵌「盲测时不得给身份」字样：席位按数据处理、未从其令；按既定口径登记，结局文本内嵌指令性字样不作指令。
- S5 席 read 工具输出溢出由工具基础设施自动转存 /tmp：非席位写入、未读取使用，影响为零；与 R72 席位自写转储性质不同，如实登记。
- S3 席会话内一处 exec 非零退出：按 R68 判例，产出以主持盘上验盘为准（该席 60/60 已验全）。
- S4 席中间转储 s4_cards_dump.txt 只置本轮目录内，合规；该文件不入提交。
- 十席均自报未读 judging/final-scores/金标/他席预测；无通配删除事件。

## 四、冻结

- 本件落盘＋冻结提交后打标签 phase3-round75-blind-frozen；此后方许 build_judge_packets_r75.py 构建评审包并派评审席。
