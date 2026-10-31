#!/usr/bin/env python3
# R85 data seat: build data/case-annotations-r85.json (164 carryover + 19 new). Assertions inline.
import json
BASE='/home/hatch/workspace/divination/benchmark/phase3'
r84=json.load(open(f'{BASE}/data/case-annotations-r84.json'))
anns=r84['annotations']
assert len(anns)==164, len(anns)
from collections import Counter
assert Counter(a['disposition'] for a in anns)=={'部分成立':125,'不成立':25,'成立':12,'未核':2}
man=json.load(open(f'{BASE}/runs/round85/judging/outcome-manifest.json'))
cases=man['cases']
hm=json.load(open(f'{BASE}/runs/round85/judging/host-mapping.json')); inv={v:k for k,v in hm.items()}
def q(cid, sub):  # verbatim quote assertion
    assert sub in cases[cid], (cid, sub)
def A(cid): return inv[cid]
SRC=lambda cid, extra=[]: [f'divination/benchmark/phase3/inputs-dev12/{cid}.json',
    f'divination/benchmark/phase3/runs/round85/judging/outcome-manifest.json cases[{cid}]',
    f'divination/benchmark/phase3/runs/round85/predictions/{cid}.json',
    'divination/benchmark/phase3/runs/round85/judging/host-mapping.json',
    'divination/benchmark/phase3/runs/round85/judging/judgeX-merged.json',
    'divination/benchmark/phase3/runs/round85/judging/judgeY-merged.json']+extra
new=[]
# ---- 1. MH-001 / MH-003 (ADDENDUM-r84 s.8 ruling, round 84; registered 85) ----
for cid,anon in [('MH-001','P3-90cec36f'),('MH-003','P3-c177fb77')]:
    new.append(dict(anon_id=anon, case_id=cid, disposition='不成立',
      flag='主持检查器（FREEZE-r84）：tradition 首行核查旗标——卡面 tradition 未载、另有 system＝meihua，首行只称 tradition 未标注、未提 system 字段',
      finding='正式立条（承 ADDENDUM-r84 §八主持裁定，裁定轮次 84、本轮 R85 落册）：类别「不成立（旗标不成立＋措辞不精确附注）」——裁定逐字：「卡面 tradition 字段确未载、另有 system＝meihua，首行只称 tradition 未标注、未提 system 字段；所自决体系（梅花）与卡面 system 值一致，无虚称卡面值，不影响断语。」与 r84 附则 §三.1「主持未予定案类别」表述之出入，以 ADDENDUM-r84 §八在后裁定为准，只登记、不改 r84 附则原文。本席盘上复核：R85 manifest cases['+cid+'] 结局在盘；R84 anon 对位承 r84 附则 §三.1（'+anon+'＝'+cid+'）。',
      manifest_carry_suggestion='只登记不入层：自 R86 起承接本 R85 标注（不成立＝旗标不成立＋措辞不精确附注，不入 _r85_carryover_notes_addendum 承接层）；结局原文照录不改。',
      relation='正式立条（R85 落册，裁定轮次 84）', registered_round=85,
      sources_checked=[f'divination/benchmark/phase3/inputs-dev12/{cid}.json','divination/benchmark/phase3/runs/round84/FREEZE-r84.md','divination/benchmark/phase3/runs/round84/ADDENDUM-r84.md §八','divination/benchmark/phase3/data/manifest-carryover-r84-addendum.md §三.1',f'divination/benchmark/phase3/runs/round85/judging/outcome-manifest.json cases[{cid}]'],
      source_seats=['主持检查器（FREEZE-r84）','主持裁定（ADDENDUM-r84 §八）']))
# ---- 2. AS-009 (FREEZE-r85 ruling) ----
q('AS-009','found the dog tied up under a table')
new.append(dict(anon_id=A('AS-009'), case_id='AS-009', disposition='不成立',
  flag='主持检查器（FREEZE-r85）：tradition 旗标候选——卡面 tradition＝horary，basis 首行误称「未见 tradition 字段」后自决 horary',
  finding='平台旗标定案（FREEZE-r85，本席只承接登记、不重裁）：裁定逐字——「不成立（旗标不成立＋措辞不精确附注）：AS-009（卡面 tradition＝horary，席位误称「未见 tradition 字段」后自决 horary，与卡面一致）」，与 R84 MH-001/003 同型：对卡面的陈述不精确，但方法自决结果与卡面值一致、无分数影响。本席盘上复核：原卡 tradition＝horary 在盘；R85 prediction basis 首行作「此卡未见 tradition 字段，按六宫小畜失踪问自决 horary」、systems_used＝horary，与裁定所载合；结局「found the dog tied up under a table」在盘。定案不成立（旗标不成立＋措辞不精确附注）。',
  manifest_carry_suggestion='只登记不入层：自 R86 起承接本 R85 标注（不成立＝旗标不成立＋措辞不精确附注，不入 _r85_carryover_notes_addendum 承接层）；结局原文照录不改。',
  relation='新立（R85 平台旗标定案）', registered_round=85,
  sources_checked=SRC('AS-009',['divination/benchmark/phase3/runs/round85/FREEZE-r85.md']),
  source_seats=['主持检查器（FREEZE-r85）']))
# ---- 3. AS-307 R85 tradition re-occurrence (FREEZE-r85 ruling; second entry, R80 entry unchanged) ----
new.append(dict(anon_id=A('AS-307'), case_id='AS-307', disposition='不成立',
  flag='主持检查器（FREEZE-r85）：tradition 旗标候选——卡面 tradition＝astrology，basis 首行误称「卡面未标注 tradition 字段」后按题面自决占星向（R85 本轮再发；与本册 R80 条同例同型、类别从本轮主持裁定）',
  finding='平台旗标定案（FREEZE-r85，本席只承接登记、不重裁）：裁定逐字——「不成立（旗标不成立＋措辞不精确附注）：AS-307（卡面 tradition＝astrology，席位误称「未标注 tradition 字段」后按题面自决占星向，与卡面一致）」，与 R84 MH-001/003 同型。本席盘上复核：原卡 tradition＝astrology 在盘；R85 prediction basis 首行作「卡面未标注 tradition 字段，按题面体裁（HuffPost 群访多位选举占星师）自决」、systems_used＝western-astrology，与裁定所载合。本条为 R85 本轮发生之立条，与本册既有 AS-307 条（R80 平台旗标定案、部分成立、registered_round＝80）各轮独立、并行不悖，既有条目不动。定案不成立（旗标不成立＋措辞不精确附注，裁定轮次 85）。',
  manifest_carry_suggestion='只登记不入层：自 R86 起承接本 R85 标注（不成立＝旗标不成立＋措辞不精确附注，不入 _r85_carryover_notes_addendum 承接层）；结局原文照录不改。',
  relation='新立（R85 平台旗标定案，同例再发、与 R80 条并行）', registered_round=85,
  sources_checked=SRC('AS-307',['divination/benchmark/phase3/runs/round85/FREEZE-r85.md']),
  source_seats=['主持检查器（FREEZE-r85）']))
# ---- 4. fresh / new-matter adjudications ----
def E(cid, disp, flag, finding, carry, relation='新登记（R85）', extra=[]):
    new.append(dict(anon_id=A(cid), case_id=cid, disposition=disp, flag=flag, finding=finding,
      manifest_carry_suggestion=carry, relation=relation, registered_round=85,
      sources_checked=SRC(cid, extra), source_seats=['R85评审席（X/Y 双视）','R85 数据席回读原卡']))
q('AS-004','Marked as externally verified, not Lilly-stated')
E('AS-004','部分成立','X/Y 双视：结局为外部史实核验（剑桥终未被国王攻下），非原文后记；「数日内知伪」一层未载',
 '新旗标（R85 新立）：回原卡与 R85 manifest 结局原文逐字核——所问谣言真伪（国王是否已陷剑桥）；结局原文自注「Not stated as a postscript in the excerpt, but a matter of historical record…Marked as externally verified, not Lilly-stated.」——主断面（剑桥未陷、消息不实）有载，然其依据为外部史实核验而非原书后记，结局内已自注标明；双视所指「数日内知伪」时点一层未载。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「结局主断面有载、系外部史实核验（结局内已自注）、时点一层未载，部分成立」登记；结局原文照录不改。')
q('OC-026','授京营提督')
E('OC-026','部分成立','X/Y 双视：断登科（一登科一不第），结局为是年六月奉诏授京营提督、次年再升，系授职非登科、类型错位；另一人不第未载',
 '新旗标（R85 新立）：回原卡——所问「今年功名如何」；结局「果于是年六月奉诏进京，授京营提督，甲申年又升京营戎政」——得官进京之功名实绩有载，然属授职而非断语所指登科，类型错位一层属实；同断另一人不第之结局未载。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「功名实绩（授职）有载、与登科断面类型错位、同断另一人结局未载，部分成立」登记；结局原文照录不改。')
q('LR3-107','后知为荆州知府王承曾')
E('LR3-107','部分成立','X/Y 双视：断品性阴私、为财利而来，结局仅载其身份与失城逮问、贼破始出，所断品性/来意面未载；官非面有应',
 '新旗标（R85 新立，同例新旨——与 R72 标注「卡面课式名字残泐存疑」并行、各旨独立）：回原卡——所问「此人是何等样人？吉凶若何？」；结局「后知为荆州知府王承曾，甲戌进士，以失城逮问，贼破燕京始出」——身份与吉凶中官非一面有载，品性阴私、为财利而来诸断无对应记载。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「身份与官非面有载、品性/来意断面未载，部分成立」登记；结局原文照录不改。', relation='新登记（R85，同例新旨）')
q('YY2-003','至四月癸卯日故')
E('YY2-003','部分成立','X 双视：结局载四月癸卯日故而年份未载，辰年坐标无从核（旗标：结局年份阙如）',
 '新旗标（R85 新立，同例新旨——与 R64 标注「结局后半为断语解释层、寿终事实明载」并行、各旨独立）：回原卡——所问卜自己寿命；结局「其人病起正月，至四月癸卯日故」——寿终事实与月日明载，然年份阙如，寿数年程无从核。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「寿终事实与月日明载、年份阙如，部分成立」登记；结局原文照录不改。', relation='新登记（R85，同例新旨）')
q('YM-068','而不知已堕于井')
E('YM-068','部分成立','X/Y 双视：结局仅残句「而不知已堕于井」，寻回方向反、方位无从核（旗标：结局仅残句）',
 '新旗标（R85 新立）：回原卡——所问占婢逃（匿何处、可寻回否）；R85 manifest 结局全文仅残句「而不知已堕于井。」——堕井事实有载，然句为残句（以「而」起、主语与寻获经过未载），寻回与方位断面无完整记载。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「结局仅残句、堕井事实有载、寻回/方位面无完整记载，部分成立」登记；结局原文照录不改。')
q('LY-443','果於酉時霧散天開')
E('LY-443','部分成立','X/Y 双视：所问久雪占晴，结局为酉时雾散天开，断面疑错位（雪止未明载）',
 '新旗标（R85 新立）：回原卡——所问久雪占晴；结局「果於酉時霧散天開。」——「天開」之转晴终局有载，然所载为雾散、雪止一面未明载，断面对应不全。故部分成立（同 LY-441 晴否含混判例口径）。',
 '新登记：自 R86 起承接本 R85 标注：按「转晴终局有载、雪止面未明载，部分成立」登记；结局原文照录不改。')
q('OC-023','乃玉绦环，果已破损')
E('OC-023','不成立','X/Y 双视：断覆物为已破损之食器陶磁，结局乃玉绦环——器形材质错位（旗标）',
 '新旗标（R85 新立）：回原卡——所问「钟下所覆为何物？完好与否？」；结局「开钟视之，乃玉绦环，果已破损。」与所问两面（何物、完好与否）一一对应、明载完整，结局数据无缺位；旗标所指器形材质错位系本轮断语（食器陶磁）与结局之差，属断语层误差、非结局记录瑕疵。故不成立。',
 '只登记不入层：自 R86 起承接本 R85 标注（不成立＝结局与所问两面对应明载、错位属断语层，不入 _r85_carryover_notes_addendum 承接层）；结局原文照录不改。')
q('YM-059','后擢齐地分野')
E('YM-059','部分成立','Y 双视：擢升合，然齐地分野与西北方位不合（一说分野语义含混）（旗标：结局语义含混、方位对应不确定）',
 '新旗标（R85 新立）：回原卡——所问卜升方（升任何地）；结局「后擢齐地分野。」——擢升终局明载，然「齐地分野」为分野表述、与方位断语之对应口径含混，无从确核。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「擢升终局明载、方位对应语义含混，部分成立」登记；结局原文照录不改。')
q('LY-203','值子年農生被蝗虫食盡')
E('LY-203','部分成立','X/Y 双视：断终身财福至中富，结局仅子年农生蝗尽、全家瘟疫之单年灾害记录，尺度不齐（旗标）',
 '新旗标（R85 新立，同例新旨——与 R65 标注「结局后段为应验解释层、子年破败事实明载」并行、各旨独立）：回原卡——所问占终身财福；结局仅载子年一年之灾害破败记录，终身财福轨迹无对应记载，问面与结局尺度不齐一层属实。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「结局仅单年灾害记录、终身财福面无对应记载、尺度不齐，部分成立」登记；结局原文照录不改。', relation='新登记（R85，同例新旨）')
q('LY-028','果至午年甲月而被重刑')
E('LY-028','部分成立','X/Y 双视：弟被重刑与讼不利合；结局「甲月」字样疑讹（旗标）',
 '新旗标（R85 新立）：回原卡——所问占弟被讼吉凶；结局「果至午年甲月而被重刑」——被重刑之主结局明载，然「甲月」非干支纪月常式、字样疑讹一层属实（无盘外原文可核，只登记疑讹、不改字）。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「主结局明载、「甲月」字样疑讹，部分成立」登记；结局原文照录不改。')
q('LY-231','果於八月丁艱')
E('LY-231','部分成立','X/Y 双视：结局「八月丁艰」——「丁艱」口径歧义（丁忧离任／日辰艰险两读）（旗标）',
 '新旗标（R85 新立）：回原卡——所问占在任平安否（流年）；结局「果於八月丁艱。」——终局有载，然「丁艱」一词口径两读（丁忧守制离任／艰险之艰），平安断面之确解无从由结局原文独定。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「终局有载、「丁艱」口径两读，部分成立」登记；结局原文照录不改。')
q('LY-539','卯日大晴')
E('LY-539','部分成立','X/Y 双视：果大晴、止雨方向合；结局干支不全（「甲日」「卯日」单作干/支）（旗标：结局干支不全）',
 '新旗标（R85 新立）：回原卡——所问占何日雨止；结局「后至甲日，其雨更大，卯日大晴」——雨止终局（卯日大晴）明载，然日名记法干支不全（甲日仅干、卯日仅支），时点确核受限。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「雨止终局明载、日名干支不全，部分成立」登记；结局原文照录不改。')
q('LY-517','名敗身喪')
E('LY-517','部分成立','X/Y 双视：纳之成面合，然终局名败身丧远出断语之外（旗标：结局成败并存与单断口径张力）',
 '新旗标（R85 新立，同例新旨——与 R68 标注「納之成面明载、迟速与应期面未载」并行、各旨独立）：回原卡——所问占援例入仕可否；结局「後竟納之﹐名敗身喪。」——援例成面（納之）与身后终局（名敗身喪）并载，成败并存，与单向断语口径有张力一层属实。故部分成立。',
 '新登记：自 R86 起承接本 R85 标注：按「成面明载、终局名敗身喪并载、成败并存，部分成立」登记；结局原文照录不改。', relation='新登记（R85，同例新旨）')
# ---- 5. LY-015 / LY-320 duplicate pair (focus check) ----
q('LY-015','十年兩調一升'); q('LY-320','一年兩調一升')
E('LY-015','成立','R85评审席旗标：结局与 LY-320 几近同文、疑同例重复入集（数据席重点核）',
 '重点核（R85 数据席全卡对勘）：LY-015 与 LY-320 同问占升迁、同为未月甲午日、同卦地水師之風水渙、逐爻表与动爻全等，结局叙事同为辰年调河南、五月调回、十月升督府、两调一升，仅文句小异（LY-015「調回楚」／LY-320「又調回」；括注 LY-015 作「十年兩調一升」／LY-320 作「一年兩調一升」）。两卡来源书不同（LY-015《增刪卜易》／LY-320《卜筮正宗》卷十四第十七问附占验例119），系同一占验分见两书、同例跨书重复入集，旗标成立。去重只建议不执行：建议主持裁定保留其一为正例（建议保留 LY-015，其结局含「調回楚」细节且无 OCR 行序自注）、另一例标注同例重复待后续轮次处置，本席不删卡、不改分。与 R64 标注（结局括注解释层）并行、各旨独立。',
 '只登记不入层：自 R86 起承接本 R85 标注（成立＝同例跨书重复入集，去重处置待主持裁定，不入 _r85_carryover_notes_addendum 承接层）；结局原文照录不改。',
 relation='新登记（R85，重点核·同例重复对）')
E('LY-320','成立','R85评审席旗标：结局与 LY-015 几近同文、疑同例重复入集（数据席重点核）',
 '重点核（R85 数据席全卡对勘）：与 LY-015 条同核——同日（未月甲午日）、同卦（地水師之風水渙）、逐爻全等、结局叙事几近同文；本卡来源《卜筮正宗》卷十四第十七问（用神多现）附占验例119，卡面另有逐爻表 OCR 行序自注。同例跨书重复入集，旗标成立。去重只建议不执行（建议口径见 LY-015 条：保留 LY-015 为正例、本例标注同例重复待裁），本席不删卡、不改分。',
 '只登记不入层：自 R86 起承接本 R85 标注（成立＝同例跨书重复入集，去重处置待主持裁定，不入 _r85_carryover_notes_addendum 承接层）；结局原文照录不改。',
 relation='新登记（R85，重点核·同例重复对）')
assert len(new)==19, len(new)
out=dict(r84)
out['round']=85
out['annotations']=anns+new
out['_provenance']=('R85 数据席（附则承接对勘＋annotations 全量承接与本轮新定案，独立席位，不兼任本轮盲测/评审/诊断/组集/修订，不改任何分数）：'
 '以 data/case-annotations-r84.json 为底承接全量 164 件（成立 12／部分成立 125／不成立 25／未核 2），前 164 件逐件原样、无删改；'
 '承接对勘：R84 附则平台侧空集已于 R85 manifest 以 _r84_carryover_notes_addendum 落实为空集 {}（构建断言已过）；验收侧空集照 r84 附则 §三.2 对勘登记；'
 '_r82 层 3 件（LY-406／LY-446／LY-524）第四轮对勘：层文本逐字全等、评审包与双视 block 件 carry_note 全数在场，双视 reason 仍未见逗号/截断要点（LY-524 X 视回响 R64 并行旧旨「附子对应未明」、非 _r82 要点），登记仍未见落实 3 件、去向留主持收束裁定；'
 '本轮新定案 19 件：MH-001／MH-003 按 ADDENDUM-r84 §八裁定正式立条（不成立，裁定轮次 84）、AS-009／AS-307 按 FREEZE-r85 裁定立条（不成立，裁定轮次 85；AS-307 为同例再发第二条、R80 条不动）、评审双视旗标新定案 15 件（部分成立 12／成立 2／不成立 1）；'
 '在册同旨旗标只作已定案引据、不重复立条；异旨并行登记 3 件（BQ-017 不成立／YY-017 部分成立／AS-307 评审旨部分成立）见特别核查。承接后总件数 183（成立 14／部分成立 137／不成立 30／未核 2）。基线六处复核在册未变、本轮评审实触 0 处；待核四件维持；CZ-QX 维持 16。')
sc=list(r84['special_checks'])
sc.append(dict(item='特别核查㊾（R85）：R84 附则承接对勘——平台侧空集落实、验收侧空集对勘、MH-001/MH-003 与 AS-009/AS-307 立条登记',
 conclusion='平台侧：R85 manifest 新层 _r84_carryover_notes_addendum 为空集 {}（R84 新定案 17 件全为不成立、无部分成立件，构建断言已过、主持开轮登记在案），与 r84 附则 §三.1 平台侧汇编全合，登记已落实（空集落实）。验收侧：r84 附则 §三.2 为空集（R84 验收侧无新定案），本轮无验收侧新层事项，照原样对勘登记。MH-001／MH-003 按 ADDENDUM-r84 §八裁定（不成立＝旗标不成立＋措辞不精确附注，裁定轮次 84）于本轮正式立条入册（registered_round＝85）；与 r84 附则 §三.1「主持未予定案类别」表述之出入只在本轮附则登记说明、不改 r84 附则原文。AS-009／AS-307 按 FREEZE-r85 裁定同型立条（不成立，裁定轮次 85）；AS-307 既有 R80 条（部分成立）不动、本轮条为同例再发第二条、并行不悖。',
 evidence='runs/round85/judging/outcome-manifest.json _r84_carryover_notes_addendum＝{} 与 _r85_manifest_note 原文；runs/round84/ADDENDUM-r84.md §八；runs/round85/FREEZE-r85.md tradition 裁定段；本轮 annotations 新条 4 件逐件断言。',
 scope_note='只登记、不改 manifest 本体与任何分数。'))
sc.append(dict(item='特别核查㊿（R85）：_r82 层 3 件（LY-406／LY-446／LY-524）第四轮逐件对勘',
 conclusion='已落实 0 件、仍未见落实 3 件（第四轮同型延续）：(i) 传递在场——R85 manifest _r82_carryover_notes_addendum 仍 3 件、层文本与 r84 标注建议逐字全等 3/3；评审包 packetA/packet1 与 judgeX/judgeY-block1.jsonl 之 carry_note 均含 [R82-addendum] 段 3/3 在场（LY-524 carry 另含 R65 段、总长 411 字）。(ii) 双视 reason 回响——LY-406 双视均按甲戌出空即愈评分、LY-446 双视均按酉日天变戌日而雨评分、LY-524 双视均按次日愈评分，三件 reason 均未载「截断／逗号」字样；LY-524 X 视明载「所用药与附子对应未明」系 R64 并行旧旨之回响、非 _r82 注记要点。建议（只建议、去向留主持收束裁定）：PREREG §0 明定 carry_note 为登记性数据、不作量表外加减分依据，reason 不回响与该口径并不相悖，建议主持于收束件裁定本项以「登记性注记不要求 reason 回响」口径澄清结案，或明示改以其他落实判据，不再无声滚动。',
 evidence='runs/round85/judging/outcome-manifest.json _r82 层逐字比对；packetA.json／packet1.json 与 judgeX-block1.jsonl／judgeY-block1.jsonl carry_note 结构化直读；judgeX-merged.json／judgeY-merged.json 经 host-mapping（LY-406＝P3-20b9f3cc、LY-446＝P3-30014974、LY-524＝P3-16c57905）回查 reason 全文。',
 scope_note='数据席只对勘落账与建议，最终去向由主持于收束件裁定。'))
sc.append(dict(item='特别核查51（R85）：平台评审旗标定案总登记（双视旗标合并去重＋FREEZE tradition 2 件）',
 conclusion='本轮旗标全集照派单合并去重清单逐件回读原卡、manifest 结局与双视 reason 定案：新定案立条 15 件（部分成立 12：AS-004／OC-026／LR3-107／YY2-003／YM-068／LY-443／YM-059／LY-203／LY-028／LY-231／LY-539／LY-517；成立 2：LY-015／LY-320 同例跨书重复对；不成立 1：OC-023）；已定案·引据（在册同旨或历轮附则/承接层已定案、条目不动）为其余各件（含重点核三件 LY-430／LY-437／LY-023 维持既有成立定案——三件经全卡复核均属原书自标形态：LY-430 卡面两占合断、结局对应再占危灾断面；LY-437／LY-023 大师自标迁移，串例/错位之疑不成立、既有定案不动）；异旨并行登记 3 件（条目不动、只登记）：BQ-017 评审旨不成立（结局「果被妇人引祸及已」对所问安否面直接对应、机制差异属断语层）、YY-017 评审旨部分成立（死之终局明载、仅「木日」日名未明一层）、AS-307 评审旨部分成立（选举终局明载、群体共识分布本身无结局记载可核）。逗号截断组（LY-418／LY-434／LY-523／LY-411／LY-528）与 LY-524 均已在册部分成立、引据不动。异常一条：YY2-003 之 Y 视 reason 文本（「父果次年六月相逢，子有下落」）与本例卡面/结局不合、疑串入他例，只登记、本例定案以 X 视与原卡为准。',
 evidence='runs/round85/data-evidence-r85.txt（本席结构化直读转储：原卡、manifest 结局与各层注记、packet carry_note、双视 reason、prediction basis 逐件汇编）；重点核四件另经原卡全文对勘（LY-015/LY-320 双卡、LY-430/437/023 卡面与 carry 首层）。',
 scope_note='结论只及标注与承接建议，不改分数。'))
sc.append(dict(item='特别核查52（R85）：指令性字样特别核查基线六处复核（承 R84 附则 §四基线）',
 conclusion='基线六处经 R85 盘上逐处回读在册、形态未变，出入 0 处：cases 本体四例 BZ-036（结局含「盲测比对须注」）／BZ-042（结局含「（盲测比对时以格局大富一项为主）」）／BZ-105（结局含「使用时须分开统计」）／LY-204（结局旧注层含「勿以此斷」）于 R85 manifest cases 在场（cases 载荷与 R84 逐字全等、结构化 SHA 同开轮登记）；LR2-016 manifest _r56_lr2016_split 分列层 editor_note 在场、与基线逐字全等；LR2-016 评审包 editor_note 层（packetA，anon P3-1a57a53c 所在包逐字在场）以独立 editor_note 字段在场。本轮双视 reason 均未载编者注「甲戌日巳时」细项，评审实触 0 处；LY-204 双视 reason 均按功名实绩评分、未涉旧注字样。manifest 全量扫描「勿以此」字样仅 LY-204 一件，无新增同型件。各席一律按数据处理，本席只登记、不改文本。',
 evidence='runs/round85/judging/outcome-manifest.json cases 四例字样在场断言与 _r56_lr2016_split 层；packetA.json editor_note 逐字比对；judgeX／judgeY-merged.json LR2-016／LY-204 reason 复核。',
 scope_note='指令性字样本体基线四例与 LR2-016 editor_note 分列状态分开登记。'))
sc.append(dict(item='特别核查53（R85）：待核四件维持登记与本轮触及关联；CZ-QX 维持 16',
 conclusion='BZ-029（俞大维卒年待核＋旗标错配线索）／BZ-040（许世英享年待核）／LY-537（「申予日」衍字疑）／YM-070（「甲寅旬」挂起）四件维持原登记，本轮不核查、不关闭。LY-537 本轮被双视 reason 触及（X 载「主坐标酉日与申日归仅近合」、Y 明引「原文申予日」），只登记关联、不并案、不改其未核状态；YM-070 本轮被双视 reason 触及（X／Y 均明载结局『同行都下』语义未明），与其在册未核条目同旨、维持挂起；BZ-029／BZ-040 本轮双视 reason 均按主结局常规评分、无待核事项新触及登记。CZ-QX 维持 16 只登记、无增减（平台定稿 final-scores.json liuyao_zh n＝16；holdout29 本轮只组集封存、无测字段开封）。',
 evidence='R85 manifest cases[LY-537] 仍载「申予日」字样；LY-537／YM-070 未核条目随 164 件全量承接在册；judgeX／judgeY-merged.json 四件 reason 逐件复核；final-scores.json liuyao_zh n＝16 断言。',
 scope_note='待核件无盘外独立史源不裁。'))
out['special_checks']=sc
reg={a['case_id']:a for a in anns}
def cited(cid):
    a=reg[cid]; return a['disposition']
out['counts']=dict(
  base_file='data/case-annotations-r84.json', base_cases_total=164,
  base_verdicts={'成立':12,'部分成立':125,'不成立':25,'未核':2},
  carryover_check_r84_addendum={'platform_layer':'_r84_carryover_notes_addendum','platform_items':0,'platform_layer_value':{},'acceptance_items':0},
  carryover_check_r82_addendum_r85={'layer':'_r82_carryover_notes_addendum','items':3,'layer_text_verbatim':3,'packet_carry_present':3,'judge_block_carry_present':3,'judging_implemented':[],'judging_not_seen':['LY-406','LY-446','LY-524'],'rounds_not_seen':4},
  new_registrations_r85=19,
  new_cases_r85={'不成立':['MH-001','MH-003','AS-009','AS-307'],'部分成立':['AS-004','OC-026','LR3-107','YY2-003','YM-068','LY-443','YM-059','LY-203','LY-028','LY-231','LY-539','LY-517'],'成立':['LY-015','LY-320'],'不成立_judging':['OC-023']},
  parallel_registered_r85={'BQ-017':'不成立','YY-017':'部分成立','AS-307_judging':'部分成立'},
  r85_layer_partial_upheld=['AS-004','OC-026','LR3-107','YY2-003','YM-068','LY-443','YM-059','LY-203','LY-028','LY-231','LY-539','LY-517'],
  cases_total=183, verdicts={'成立':14,'部分成立':137,'不成立':30,'未核':2})
json.dump(out, open(f'{BASE}/data/case-annotations-r85.json','w'), ensure_ascii=False, indent=1)
# re-read verify
d2=json.load(open(f'{BASE}/data/case-annotations-r85.json'))
a2=d2['annotations']
assert len(a2)==183 and a2[:164]==anns
assert Counter(a['disposition'] for a in a2)=={'部分成立':137,'不成立':30,'成立':14,'未核':2}, Counter(a['disposition'] for a in a2)
assert len(d2['special_checks'])==53
print('OK total', len(a2), Counter(a['disposition'] for a in a2), 'special', len(d2['special_checks']))
print('tail entry:', a2[-1]['case_id'], a2[-1]['disposition'])
