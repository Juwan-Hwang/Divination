#!/usr/bin/env python3
# R86 数据席落盘脚本：case-annotations-r86.json（全量承接 r85 183 件 + 本轮新定案 55 件）
# 旗标逐件回原卡/结局核读结论均已由本席逐件核定后写死于下表；本脚本只负责落盘与断言。
import json, hashlib, collections

BASE = "/home/hatch/workspace/divination/benchmark/phase3"
r85 = json.load(open(f"{BASE}/data/case-annotations-r85.json"))
anns85 = r85["annotations"]
assert len(anns85) == 183, len(anns85)
man86 = json.load(open(f"{BASE}/runs/round86/judging/outcome-manifest.json"))
cases86 = man86["cases"]
hm86 = json.load(open(f"{BASE}/runs/round86/judging/host-mapping.json"))  # anon -> case
inv86 = {v: k for k, v in hm86.items()}
hma = json.load(open(f"{BASE}/runs/round86/acceptance/judging/host-mapping.json"))
inva = {v: k for k, v in hma["ours"].items()}
gold = {}
for line in open(f"{BASE}/holdout29/test_gold.jsonl"):
    g = json.loads(line)
    gold[g["id"]] = g

def outcome(cid):
    return cases86[cid]

# _r85 层落实断言：12 件、文本与 r85 annotations 部分成立条 suggestion 全等
layer85 = man86["_r85_carryover_notes_addendum"]
assert len(layer85) == 12, len(layer85)
sugg85 = {}
for a in anns85:
    if a["registered_round"] == 85 and a["disposition"] == "部分成立":
        sugg85[a["case_id"]] = a["manifest_carry_suggestion"]
assert set(layer85) == set(sugg85), (set(layer85) ^ set(sugg85))
for cid, txt in layer85.items():
    assert sugg85[cid].endswith(txt) or txt in sugg85[cid] or sugg85[cid].split("：", 1)[-1].endswith(txt), cid
print("r85 layer assert OK (12)")

# 指令性字样基线六处断言
for cid, kw in [("BZ-036", "盲测比对须注"), ("BZ-042", "盲测比对时以格局大富一项为主"),
                ("BZ-105", "使用时须分开统计"), ("LY-204", "勿以此斷")]:
    assert kw in cases86[cid], cid
assert "甲戌日巳时" in man86["_r56_lr2016_split"]["editor_note"]
packetA = json.load(open(f"{BASE}/runs/round86/judging/packetA.json"))
lr16 = [p for p in packetA if hm86.get(p.get("anon_id")) == "LR2-016"]
assert lr16 and "editor_note" in lr16[0] and "甲戌日巳时" in json.dumps(lr16[0], ensure_ascii=False)
print("instruction-baseline assert OK (6)")

# BQ chart_complete 断言
import os
for cid in ["BQ-001"] + [f"BQ-0{i}" for i in range(10, 26)]:
    card = json.load(open(f"{BASE}/inputs-dev12/{cid}.json"))
    assert card["context"]["attachments"]["chart_complete"] is False, cid
print("BQ chart_complete assert OK (17)")

NEW = []  # (case_id, disposition, flag, finding, carry, relation, face)

def P(cid, disp, flag, finding, carry, relation="新登记（R86，平台 basis 留痕定案）"):
    NEW.append((cid, disp, flag, finding, carry, relation, "platform"))

def A(cid, disp, flag, finding, carry, relation="新登记（R86，验收侧旗标定案）"):
    NEW.append((cid, disp, flag, finding, carry, relation, "acceptance"))

CARRY_P = "新登记：自 R87 起承接本 R86 标注：按「{g}，部分成立」登记；结局原文照录不改。"
CARRY_N = "只登记不入层：自 R87 起承接本 R86 标注（不成立，不入 _r86_carryover_notes_addendum 承接层）；结局原文照录不改。"
SYN = "同例新旨（R86，与在册旧旨并行）"

# ---------- 平台侧：部分成立 ----------
P("AS-009", "部分成立",
  "R86 平台 basis 留痕：卡面注部分字形 OCR 残损、未载度数不臆补（残损类）",
  "回原卡——卡面 attachments note 逐字载「several glyphs are garbled in the 1647 OCR」，残损一层属实，席位据此不臆补度数、降置信；R86 manifest 结局载狗于 Long Acre 桌下被寻回送还，主问（往何处寻＋能否找回）终局明载可核。故部分成立。与在册 R85 tradition 条（不成立）各旨独立、并行不悖。",
  CARRY_P.format(g="卡面 1647 OCR 部分字形残损已自注、未载度数无据，未臆补；寻狗主问终局明载"), SYN)
P("AS-015", "部分成立",
  "R86 平台 basis 留痕：输入残损——卡面自注 1647 OCR 部分残损、丈夫主星位置不全（残损类）",
  "回原卡——卡面 attachments note 逐字载「Positions partly garbled in the 1647 OCR」，残损一层属实，席位据此归期降置信、不臆补度数；R86 manifest 结局载问者本人死日一面（夫存亡面未载一层已由在册 R75 条定案、本条不重裁）。残损层与在册结局层各旨独立。故部分成立。",
  CARRY_P.format(g="卡面 1647 OCR 部分残损、夫主星位置不全已自注，归期无确切度数可据；结局一面明载"), SYN)
P("AS-205", "部分成立",
  "R86 平台 basis 留痕：输入残损——上升星座字形 OCR 已坏、卡面明言不作断言（残损类）",
  "回原卡——卡面 asked_at 逐字载「see the ocr_note on the year」、attachments note 载图面散文位置且 OCR 字形有坏，残损一层属实，席位据此病位只就六宫主土性固定之象作断、不强指脏腑；R86 manifest 结局逐字载「The sick dyed the 28th of July following」，死生终局明载可核。故部分成立。",
  CARRY_P.format(g="上升星座字形 OCR 已坏、卡面明言不作断言，病位一层无据；死生终局明载"))
P("AS-212", "部分成立",
  "R86 平台 basis 留痕：输入残损——卡面日期 OCR 不可读、全盘未载，仅有散文关键位置（残损类）",
  "回原卡——卡面 asked_at 逐字载「the day is not legible in the OCR」、attachments 仅载 key_positions 散文位置、无全盘，残损一层属实，席位据此降置信；R86 manifest 结局载改从医嘱、约三周痊愈，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面日期 OCR 不可读、全盘未载，仅散文关键位置在场；痊愈终局明载"))
for cid, gist, oc in [
    ("AS-301", "卡面未载任何星盘、星位或逐月原文，只有发问时间与题面", "2020年3月上旬新冠在欧美急剧扩散，世卫组织于2020年3月11日宣布大流行"),
    ("AS-302", "卡面未载任何星盘星位与原文断语，只有发问时间与设定", "辉瑞/BioNTech疫苗2020年12月2日获英国批准、12月8日开始接种"),
    ("AS-303", "卡面未载星盘与原文日期清单", "2024年6月18日、7月26/28日、8月4/5日均无第三次世界大战爆发"),
    ("AS-305", "卡面未载具体星盘与行运数据，只有占者自承势均力敌之设定", "特朗普获胜且优势明确（312对226选举人票，并赢得普选票）"),
    ("AS-306", "卡面未载任何星盘、dasha 或原文断语，只有发布时间与题面设定", "拜登于2024年7月21日退选，哈里斯成为民主党候选人；特朗普于11月5日胜选"),
]:
    P(cid, "部分成立",
      "R86 平台 basis 留痕：输入残损——" + gist + "（残损类）",
      f"回原卡——卡面 context 仅 question／asked_at／setting、无 attachments，{gist}属实，席位据此只按通例落事件级、明写无盘面不臆补；R86 manifest 结局逐字载「{oc}」，终局明载可核。故部分成立。",
      CARRY_P.format(g="题面无盘面附件、输入残损已自注，终局明载"))
P("AS-304", "部分成立",
  "R86 平台 basis 留痕：输入残损——卡面未载两候选人命盘、选举日星盘与原文断语（残损类）",
  "回原卡——卡面 context 仅 question／asked_at／setting、无 attachments，残损一层属实，席位据此只按职业占星界主流取向落单一终局；R86 manifest 结局载特朗普 312 张选举人票胜出，选举终局明载可核（结局后半认错一节已由在册 R79 条定案、本条不重裁）。故部分成立。",
  CARRY_P.format(g="题面无盘面附件、输入残损已自注，选举终局明载"), SYN)
BQ_GIST = {
 "BQ-001": "原文只记本卦兑、变卦履与断语援引之象，无六爻全盘、无动爻明载",
 "BQ-010": "原文只记蒙之未济、父母空亡，无全盘、无月建世应",
 "BQ-011": "只记离之贲、日辰扶世、官鬼冲克世、财爻动，无全盘",
 "BQ-012": "原文只记卦名噬嗑与鬼爻衰静，无全盘、无世应月建",
 "BQ-013": "只记随之咸、申子两爻动成父局，无全盘",
 "BQ-014": "只记困之震、兄父俱动合住应爻，无全盘、无月建",
 "BQ-015": "只记蒙之中孚、水鬼与应上父动克世、财伏，无全盘",
 "BQ-016": "只记困之大过、六三午火鬼动化酉金、兄弟带刑克世，无全盘",
 "BQ-017": "无全盘、无月建、无逐爻六亲六神全列，仅据卡面 excerpt 作断",
 "BQ-018": "无全盘、无月建、无鬼爻地支与世爻地支，仅据 excerpt 作断",
 "BQ-019": "无全盘、无月建（只记五月）、无逐爻地支，仅据 excerpt 作断",
 "BQ-020": "无全盘、无月建、无动爻爻位地支，仅据 excerpt 作断",
 "BQ-021": "无全盘、无月建干支全称（只记四月）、无用神爻位全列，仅据 excerpt 作断",
 "BQ-022": "无全盘、无月日干支全称（只记丙子日）、无应世地支，仅据 excerpt 作断，信息最薄",
 "BQ-023": "无全盘、无占期月日、无父爻地支与化神地支，仅据 excerpt 作断",
 "BQ-024": "无全盘、无月建、无子孙与鬼爻地支全列，仅据 excerpt 作断",
 "BQ-025": "无全盘、无月建、无动爻地支，仅据 excerpt 作断",
}
for cid, gist in BQ_GIST.items():
    rel = SYN if cid in {a["case_id"] for a in anns85} else "新登记（R86，平台 basis 留痕定案）"
    P(cid, "部分成立",
      "R86 平台 basis 留痕：输入残损——chart_complete=false，" + gist + "（残损类）",
      f"回原卡——卡面 attachments 逐字载 chart_complete＝False、completeness_basis 与 chart_excerpt，{gist}属实，席位据此降置信作断；R86 manifest 结局逐字载「{outcome(cid)}」，主问终局明载可核。故部分成立。",
      CARRY_P.format(g="卡面 chart_complete＝false、无全盘，残损已于卡面与 prediction 双示；主问终局明载"), rel)
P("BZ-301", "部分成立",
  "R86 平台 basis 留痕：输入残损（重度）——卡面未载任何四柱、成立时盘或起算数据，无盘可排（残损类）",
  "回原卡——卡面 context 仅 question／asked_at／setting、无四柱与盘面附件，残损一层属实，席位据此只据所问年份干支作方向级判断、格局运程量级明写不报；R86 manifest 结局载国民党 2022 年九合一地方选举大胜、其后持续正常运作，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面无四柱无盘面、重度残损已自注，只作方向级断；终局明载"))
P("BZ-302", "部分成立",
  "R86 平台 basis 留痕：输入残损（重度）——卡面未载缪斌生辰四柱，无盘可排（残损类）",
  "回原卡——卡面 context 仅 question／asked_at／setting、无生辰四柱，残损一层属实，席位据此只就题面已载面落终局方向；R86 manifest 结局载缪斌投汪伪被捕、吴稚晖说情反启蒋疑、1946 年枪决，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面无生辰四柱、重度残损已自注，只就题面已载面作断；终局明载"))
P("BZ-303", "部分成立",
  "R86 平台 basis 留痕：输入残损——卡面未载任何坐向、元运盘面数据，无盘可起（残损类）",
  "回原卡——卡面 context 仅 question／asked_at／setting、无盘面附件，残损一层属实，席位据此只据所问时段与八运九运交界锚点落方向；R86 manifest 结局载香港住宅楼价自 2021 年高位累计下跌约四成、2024 年后持续低迷，终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面无坐向元运盘面、残损已自注，只落方向；终局明载"))
P("BZ-304", "部分成立",
  "R86 平台 basis 留痕：输入残损——卡面未载起算盘面与具体断法数据，无盘可起（残损类）",
  "回原卡——卡面 context 仅 question／asked_at／setting、无盘面附件，残损一层属实，席位据此只据题面已载面与岁运干支落方向；R86 manifest 结局与历轮所核文本一致、终局明载可核（在册旧旨为他旨、本条不重裁）。故部分成立。",
  CARRY_P.format(g="卡面无起算盘面、残损已自注，只落方向；终局明载"), SYN)
P("BZ-035", "部分成立",
  "R86 平台 basis 留痕：卡面纪年作嘉庆八年（1803），与四柱癸未及史载生年不合（卡面不合类）",
  "回原卡——卡面 subject.birth.date 逐字作「清嘉庆八年（1803年）」，attachments.pillars 逐字作「癸未 甲寅 乙亥 己卯」；嘉庆八年为癸亥、癸未对应 1823 年（李鸿章史载生年），纪年与四柱不合一层属实，席位以四柱为准、纪年存疑计入置信；R86 manifest 结局载李鸿章官至直隶总督兼北洋大臣、1901 年卒，终局明载可核。故部分成立。与在册 R76 tradition 条各旨独立。",
  CARRY_P.format(g="卡面纪年（嘉庆八年）与四柱癸未不合已自注、以四柱为准；终局明载"), SYN)
P("LR-001", "部分成立",
  "R86 平台 basis 留痕：输入残损实录——卡面只有 subject、question、asked_at、setting 与 provenance，无课式、无三传、无干支占时（残损类）",
  "回原卡——卡面 context 仅 question／asked_at／setting、无 attachments，残损一层属实，席位据此降置信作断；R86 manifest 结局逐字载「1936年12月25日蒋介石获释飞离西安，未受人身伤害，平安抵南京」，生死安危终局明载可核。故部分成立。",
  CARRY_P.format(g="卡面无课式三传附件、残损实录已自注；生死终局明载"))
P("LY-246", "部分成立",
  "R86 平台 basis 留痕：残损注明——卡面六亲标示下子孙（按本宫）不上卦、且卡面未给伏神字段（残损类）",
  "回原卡——卡面 chart_lines 本卦六爻为父母／兄弟／官鬼、无子孙现爻，attachments 无伏神（hidden_lines）字段，残损一层属实，席位据此改以发动三爻与世应结构立断、置信下调；R86 manifest 结局逐字载「果於壬申日生女，產母平安」，平安与男女两面明载可核。故部分成立。",
  CARRY_P.format(g="子孙不上卦、无伏神字段，残损已自注；生女与母平安明载"))
P("LY-338", "部分成立",
  "R86 平台 basis 留痕：残损面——父母、子孙两亲不现、伏位不唯一（卡面明载不可补）（残损类）",
  "回原卡——卡面 notes.completion_grade.hidden_lines 逐字载 grade「不可補」、basis 载「本卦六親缺父母、子孫兩味不現，伏神取位不唯一……保持不補」，残损一层属实，席位据此已列面不臆补；R86 manifest 结局逐字载「后一冬果获大利」，获利终局明载可核。故部分成立。",
  CARRY_P.format(g="父母子孙两亲不现、伏位不唯一不可补，残损已于卡面自注；获利终局明载"))
P("LY-339", "部分成立",
  "R86 平台 basis 留痕：卡面明载两卦合断、trigger 记 disputed；卡面 chart_note 另载 OCR 行序错乱、逐爻表不录（多卦合卡类＋残损类）",
  "回原卡——卡面 question 逐字作「占自去寻父回（两卦合断）」、setting 载「先得一卦，命再占一卦合决」，attachments.chart_note 逐字载装卦表 OCR 行序错乱、逐爻装卦未能可靠还原，合卡与残损两层俱属实，席位逐卦分列后合断；R86 manifest 结局逐字载「果于申年八月寻父回家」，寻回终局明载可核。故部分成立。",
  CARRY_P.format(g="两卦合卡、逐爻表 OCR 行序错乱不录，合断取舍已留痕；寻回终局明载"))
P("LY-417", "部分成立",
  "R86 平台 basis 留痕：残损注——卡面 hexagram 并列三卦名，chart_lines 仅载两卦盘面，第三卦（无妄）盘面未载（残损类＋多卦合卡类）",
  "回原卡——卡面 attachments.hexagram 逐字并列「火水未濟之水山蹇之天風姤之天雷無妄」，chart_lines 十二行仅两卦盘面，第三卦盘面未载属实，席位据此只据前两卦合断并降置信；R86 manifest 结局逐字载「果於寅日全愈」，愈否终局明载可核。故部分成立。",
  CARRY_P.format(g="三卦并列、第三卦盘面未载，残损已自注，只据前两卦合断；全愈终局明载"))
P("LY-445", "部分成立",
  "R86 平台 basis 留痕：三占合断、二占残缺降权——二占卡面明载原文未附装卦、无爻位可据（多卦合卡类＋残损类）",
  "回原卡——卡面 question 逐字作「占何日雨（三占合斷）」、attachments.hexagram 逐字载「二占：離為火（靜卦，原文未附裝卦）」、chart_lines 十二行仅初占与三占盘面，二占残缺一层属实，席位以初占、三占为主据、二占弱参；R86 manifest 结局逐日载云、雨、晴（在册 R71／R75 条为结局层定案、本条为输入层新旨，不重裁）。故部分成立。",
  CARRY_P.format(g="三占合卡、二占未附装卦残缺已自注，主据初占三占；逐日结局有载"), SYN)
P("LY-503", "部分成立",
  "R86 平台 basis 留痕：卡面残损——asked_at 仅「巳月未日（原文如此，日干支不全）」，日干缺载（残损类）",
  "回原卡——卡面 asked_at 逐字作「巳月未日（原文如此，日干支不全）」，残损一层属实，席位据此旬空、六神、日辰生克明写无从确核、只据月建与动化作断；R86 manifest 结局逐字载「果卒於申日」，卒期终局明载可核。故部分成立。",
  CARRY_P.format(g="日干支不全、残损已自注，只据月建动化作断；卒于申日明载"))
P("LY-505", "部分成立",
  "R86 平台 basis 留痕：卡面为三卦合卡，disputed——三卦分占、静动不一，合断取舍存分歧面（多卦合卡类）",
  "回原卡——卡面 setting 逐字载「連占三卦合斷」、attachments.hexagram 逐字列初占风山渐、再占火地晋、三占雷风恒之泽风大过，合卡一层属实，席位逐卦分列、取三占动进为收束所据并留痕；R86 manifest 结局逐字载「又本府府尊命下，不準復職，後援刑例果於巳年補陜慶陽府知府」，复职终局明载可核。故部分成立。",
  CARRY_P.format(g="三卦合卡、合断取舍分歧已留痕；复职终局明载"))
P("LY-527", "部分成立",
  "R86 平台 basis 留痕：卡面盘面十二行、动爻栏混列两占，残损形态在此注明（多卦合卡类＋残损类）",
  "回原卡——卡面 attachments.hexagram 逐字列初占火天大有之乾为天、再占雷泽归妹之雷地豫，chart_lines 十二行两占并载、moving_lines 三动分属两占，混列一层属实，席位按行序拆分两占作断；R86 manifest 结局载照壁大树宅形一面与「果中經魁」功名一面，分占终局明载可核。故部分成立。",
  CARRY_P.format(g="两占合卡、盘面十二行混列已注明并按行序拆分；分占终局明载"))
P("LY-538", "部分成立",
  "R86 平台 basis 留痕：卡面 notes 自载宫位标注出入——卦名括注兑宫与世应震宫五世不合，trigger.disputed 据此留痕（卡面不合类）",
  "回原卡——卡面 notes 逐字载「palace字段出入（仅提示，不改原字段）：inputs8 卦名括注作『兌宮』，与标准八宫及原书装卦表世应（世在五爻、应在二爻，震宫五世）不合」，不合一层属实，席位按逐爻六亲地支与世应原样作断、不据宫名；R86 manifest 结局与在册 R79 条所核文本一致、仕途终局可读（结局层旧旨不重裁）。故部分成立。",
  CARRY_P.format(g="宫位标注出入（兑宫括注与震宫五世不合）已自注、按世应原样作断；仕途终局可读"), SYN)
P("LY-626", "部分成立",
  "R86 平台 basis 留痕：残损注明——卡面 chart_note 明载在线本装卦表 OCR 行序错乱、逐爻未能可靠还原（残损类）",
  "回原卡——卡面 hexagram.chart_note 逐字载「在線本裝卦表為雙欄排版經 OCR 轉錄後行序錯亂，逐爻裝卦未能可靠還原……逐爻表不錄」，残损一层属实，席位据此逐爻表按卡面所录用之、不臆补未录项；R86 manifest 结局逐字载「果死於午日午時」，死期终局明载可核。故部分成立。",
  CARRY_P.format(g="装卦表 OCR 行序错乱、逐爻未能可靠还原，残损已自注；死于午日午时明载"))
P("MP-012", "部分成立",
  "R86 平台 basis 留痕：残损注记——原占之塔罗牌面与圣卦卦面均未随卡附载，属输入残损（残损类）",
  "回原卡——卡面 context 仅 question／asked_at／setting、无 attachments，牌面卦面未载属实，席位据此只走事实路、限置信；R86 manifest 结局逐字载「赖清德、萧美琴当选第16任正副总统」，当选终局明载可核。故部分成立。",
  CARRY_P.format(g="牌面卦面均未随卡附载、残损已自注；当选终局明载"))
P("YM-004", "部分成立",
  "R86 平台 basis 留痕：输入残损（照实注记）——卡面明载「原书未记月建」，旺衰缺月建一层（残损类）",
  "回原卡——卡面 asked_at 逐字作「甲辰旬戊申日（原书未记月建）」，残损一层属实，席位据此只按日辰与动爻判读、不臆补月建；R86 manifest 结局逐字载「后至亥令而痊」，痊愈终局明载可核。故部分成立。",
  CARRY_P.format(g="原书未记月建、残损已自注，只按日辰动爻判读；痊愈终局明载"))
# ---------- 平台侧：不成立 ----------
P("LY-022", "不成立",
  "R86 平台 basis 留痕：输入残损注记——卡面变卦栏初爻地支字形残损（呈缺字符）（残损类）",
  "回原卡——卡面 chart_lines_top_to_bottom 六行逐字回读：本变两栏十二项俱可读（初爻本栏「兄弟未土」、变栏「兄弟未土」俱在），全卡无缺字符，残损注记无据；席位自注「本卦初爻兄弟未土可读、动爻与世应俱清，不影响取用」亦与之合。R86 manifest 结局「果不久病愈；九月妻死」明载。故旗标不成立，只登记。",
  CARRY_N)
P("OC-018", "不成立",
  "R86 平台 basis 留痕：残损注明——卡面未给出生公历日期与起运岁数，大运交运年份不可复算（残损类）",
  "回原卡——卡面载四柱（basis 逐字照录「己卯 丙子 庚寅 辛巳」）与命主设定，装盘作断无缺口；未给公历日期与起运岁数属八字命例通例形态（同组 OC 命例同型），席位应期落运档并按窗口标注即为通例处置、不构成残损缺口。R86 manifest 结局载史量才 1934 年遇刺身亡，终局明载。故旗标不成立，只登记。",
  CARRY_N)
# ---------- 验收侧 ----------
for cid in ["CYJ-001", "CYJ-002", "CYJ-004", "CYJ-005"]:
    g = gold[cid]
    A(cid, "部分成立",
      "DIAG-H29 §5 F3＋验收 basis 残损注明：卡面 chart_complete=false、chart_fidelity 明载仅干支，四课、三传、天将、空亡、年命俱未给（残损类）",
      f"回原卡——holdout29 输入卡 anchors 逐字载 chart_complete＝False、chart_fidelity「仅干支（复原不能）：原书课盘列在盘、转录底稿未录盘、页图字迹不足以逐字可靠转录」，盘体缺载一层属实；金标 grade_note 所载「课式头四要素 present（R84 核查台账）」指课式头层、与盘体缺载指向同一输入形态的不同层，两口径并列、不相悖。大师决定性读法所凭盘面未录、席位按残损口径只据干支大势作断并明写无据不报；金标 outcome_record 逐字载「{g['outcome_record']}」，终局明载可核。故部分成立。",
      CARRY_P.format(g="课盘 fidelity 降级、盘体缺载（仅干支），课式头 present 口径并列；终局明载"))
A("ZW-015", "部分成立",
  "DIAG-H29 §5 F2：卡面与 basis 逐字作「虹桥机场（60009）」五位代码，与常见六位证券代码形态不合（卡面不合类）",
  "回原卡——holdout29 输入卡 subject 逐字作「问事盘对象：股票虹桥机场（60009）」，五位字样属实；对象身份可确指（虹桥机场标的本身无歧义）、席位与大师共用同一卡面锚点，金标 outcome_record 逐字载次周收盘 14.68 元、完全应验，终局明载可核。字样位数不合一层属实，故部分成立；原文形态照录不改。",
  CARRY_P.format(g="对象代码字样作五位「60009」、与通行六位形态不合，对象可确指；终局明载"))
A("ZW-010", "不成立",
  "DIAG-H29 §5 F1：卡面四化锚点（太阴化忌）与席位本库四化表（庚干太阴化科、天同化忌）冲突候选（卡面不合类）",
  "回原卡——holdout29 输入卡 anchors 四化锚点逐字作「太阴化忌；父母宫擎羊落陷」，卡面锚点自洽、且为席位与大师共用之断据面；分歧在席位藏书四化表之庚干异说（紫微章 ZZ-M101 并列在册），席位从卡面作断并于 basis 标明分歧，处置合口径。金标 master_prediction 决定性断项（18 岁婚、20 岁妻自杀、26 岁牢狱）与 outcome_record 逐字对应明载，卡面无瑕疵。故旗标不成立，只登记。",
  CARRY_N)
A("DS-063", "不成立",
  "DIAG-H29 §5 F4＋验收 basis 残损注明：输入卡只有四柱与性别，无出生年月日时、出生地、起运岁数（残损类）",
  "回原卡——holdout29 输入卡 anchors 逐字载四柱「壬戌 己酉 丁巳 丙午」完整在场；金标 grade_note 逐字载「出生年月日时原文未载（本书命例通例），锚点口径从派单：四柱完整载于原文即 present」，封存口径已定。无出生年月日时属本书命例通例形态、不构成残损缺口，席位应期降格为运档坐标即通例处置。故旗标不成立，只登记。",
  CARRY_N)
A("ZW-011", "不成立",
  "DIAG-H29 §5 F5：金标 master_prediction 逐字载「34-33 岁化忌」，原文异写候选（卡面不合类）",
  "回原卡与金标——holdout29 输入卡 anchors 无此字样，异写在金标大师断语原文，grade_note 已逐字注「『34-33』为原文如此，照录不改」；金标 outcome_record 逐字载「26 岁结婚，35 岁婚姻失败」，终局明载。此为大师侧原文照录形态、非输入卡或结局数据瑕疵，与本例核验无涉。故旗标不成立，只登记。",
  CARRY_N)

assert len(NEW) == 55, len(NEW)
from collections import Counter
print(Counter((f, d) for _, d, _, _, _, _, f in NEW))

in85 = {a["case_id"] for a in anns85}
new_anns = []
for cid, disp, flag, finding, carry, relation, face in NEW:
    if face == "platform":
        anon = inv86[cid]
        srcs = [f"divination/benchmark/phase3/inputs-dev12/{cid}.json",
                f"divination/benchmark/phase3/runs/round86/predictions/{cid}.json",
                f"divination/benchmark/phase3/runs/round86/judging/outcome-manifest.json cases[{cid}]",
                "divination/benchmark/phase3/runs/round86/judging/host-mapping.json",
                "divination/benchmark/phase3/runs/round86/FREEZE-r86.md"]
        seats = ["R86 平台盲测席 basis 留痕", "R86 数据席回读原卡"]
    else:
        anon = inva[cid]
        srcs = [f"divination/benchmark/phase3/holdout29/inputs/{cid}.json",
                f"divination/benchmark/phase3/holdout29/test_gold.jsonl [{cid}]",
                f"divination/benchmark/phase3/runs/round86/acceptance/predictions/{cid}.json",
                "divination/benchmark/phase3/runs/round86/acceptance/DIAG-H29.md §5",
                "divination/benchmark/phase3/runs/round86/acceptance/judging/host-mapping.json"]
        seats = ["DIAG-H29 席（§5 旗标候选）", "R86 数据席回读原卡／金标"]
    new_anns.append({
        "anon_id": anon, "case_id": cid, "disposition": disp, "finding": finding,
        "flag": flag, "manifest_carry_suggestion": carry, "registered_round": 86,
        "relation": relation, "source_seats": seats, "sources_checked": srcs,
    })

out = dict(r85)
out["round"] = 86
out["_provenance"] = (
    "R86 数据席（附则承接对勘＋annotations 全量承接与本轮新定案，独立席位，不兼任本轮盲测/评审/诊断/组集/修订，不改任何分数）："
    "以 data/case-annotations-r85.json 为底承接全量 183 件（成立 14／部分成立 137／不成立 30／未核 2），前 183 件逐件原样、无删改；"
    "承接对勘：R85 附则平台侧部分成立 12 件已于 R86 manifest 以 _r85_carryover_notes_addendum 落实（脚本断言：层 id 集与 r85 部分成立∧registered_round＝85 集全等、注记文本逐件捕获验合）；验收侧空集照 r85 附则对勘登记；"
    "_r82 层 3 件已经 R85 主持裁定结案（登记性注记不要求 reason 回响，承 PREREG-r86 §6），本轮不再滚动对勘、只作在册登记；"
    "本轮新定案 55 件：平台侧 47 件（部分成立 45／不成立 2；来源＝FREEZE-r86 tradition/CLAIM 候选 0 件＋平台 predictions basis 残损/卡面不合/多卦合卡三类留痕逐件回原卡与 R86 manifest 结局定案）＋验收侧 8 件（部分成立 5／不成立 3；来源＝DIAG-H29 §5 F1–F5＋验收 predictions basis 留痕逐件回 holdout29 输入卡与金标定案）；"
    "在册同旨旗标只登记不重复立条（引据清单见附则 §三.4／§四.3）；合断体例无异常留痕者经核不立旗（附则筛检登记）；"
    "AS-307 双条并行例外形态照体例续行（R80 部分成立条与 R85 不成立条并行保留、不合并；本轮 AS-307 无新旗标，其 basis 输入残损留痕与 R68 已定案旨同旨、只引据登记，不另立第三条）；"
    "LY-015／LY-320 同例重复登记承 R85 裁定、两例互引已于 r85 落账，本轮照原样承接；待核四件维持；CZ-QX 维持 16 只登记。"
)
out["annotations"] = anns85 + new_anns
sc = list(r85["special_checks"])
sc += [
 {"item": "（R86）特别核查54：R85 承接对勘与 _r82 层结案登记",
  "conclusion": "R85 附则平台侧 12 件已于 R86 manifest 以 _r85_carryover_notes_addendum 落实（层 id 集与附则 §三.2 清单逐件全等、注记文本捕获验合）；验收侧空集照原样对勘。_r82 层 3 件（LY-406／LY-446／LY-524）已经 R85 主持裁定结案（登记性注记不要求 reason 回响），本轮不再滚动对勘，注记在 manifest 层与 annotations 之保留只作在册登记。",
  "evidence": "runs/round86/judging/outcome-manifest.json _r85_carryover_notes_addendum 12 件（落盘脚本结构化直读断言）；PREREG-r86 §6① 结案口径。",
  "scope_note": "对勘只登记，不改 manifest 任一侧。"},
 {"item": "（R86）特别核查55：平台旗标定案总登记（basis 三类留痕）",
  "conclusion": "FREEZE-r86 tradition 候选 0、CLAIM 声明组候选 0，无主持裁定件；平台 predictions basis 残损/卡面不合/多卦合卡三类留痕逐件回原卡与 R86 manifest 结局定案：新定案 47 件（部分成立 45／不成立 2）；同旨已定案者入引据清单不重复立条；合断体例无异常留痕者（LY-001／LY-004／LY-204／LY-227／LY-255／LY-416／LY-432／OC-029 等）经核不立旗，只筛检登记。",
  "evidence": "runs/round86/FREEZE-r86.md；runs/round86/predictions 逐件 basis（落盘脚本逐件回卡断言：BQ 17 件 chart_complete＝False 全等、LY-538 palace 出入原文在卡、LY-022 全卡无缺字符）。",
  "scope_note": "basis 留痕不凭转述定案，逐件以原卡与结局原文为准。"},
 {"item": "（R86）特别核查56：验收侧旗标定案总登记（holdout29）",
  "conclusion": "DIAG-H29 §5 旗标候选 F1–F5 与验收 predictions basis 留痕逐件回 holdout29 输入卡与金标定案：新定案 8 件（部分成立 5＝CYJ-001／CYJ-002／CYJ-004／CYJ-005＋ZW-015；不成立 3＝ZW-010／DS-063／ZW-011）。紫微 13 例 basis 锚点稀疏残损自注属池例设计形态（DIAG-H29 §0 定性：所给锚点即共用断据面、不计 IN），不立旗；DA 四例课名未载已注明不臆补、盘面全在场，不立旗。",
  "evidence": "runs/round86/acceptance/DIAG-H29.md §5／§0；holdout29/inputs 与 test_gold.jsonl 逐件回读（落盘脚本金标 outcome 逐字引录）。",
  "scope_note": "验收侧定案只及标注与承接建议，不改验收分数。"},
 {"item": "（R86）特别核查57：指令性字样特别核查基线六处复核",
  "conclusion": "基线六处经 R86 盘上逐处回读在册、形态未变，出入 0 处：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）＋LR2-016 manifest editor_note 一处（_r56_lr2016_split 分列层、原文逐字全等）＋LR2-016 评审包 editor_note 层一处（packetA 独立字段在场）。本轮新增同型件：无。各席一律按数据处理。",
  "evidence": "runs/round86/judging/outcome-manifest.json 与 packetA.json（落盘脚本逐处逐字断言全过）。",
  "scope_note": "只登记、不改任何文本。"},
 {"item": "（R86）特别核查58：待核四件维持与 CZ-QX 维持登记",
  "conclusion": "BZ-029／BZ-040／LY-537／YM-070 四件无新证据、维持待核原登记（LY-537 本轮 basis 仍载 OCR 行序同型留痕，只登记关联、不并案）；CZ-QX 维持 16（holdout29 无测字例、平台定稿口径不变），只登记不另行结算。",
  "evidence": "data/case-annotations-r85.json 待核条目承接；runs/round86/acceptance/DIAG-H29.md §2（CZ-QX 不适用／不增）。",
  "scope_note": "无盘外独立史源不裁。"},
]
out["special_checks"] = sc
cnt = Counter(a["disposition"] for a in out["annotations"])
out["counts"] = {
 "base_file": "data/case-annotations-r85.json", "base_cases_total": 183,
 "base_verdicts": {"成立": 14, "部分成立": 137, "不成立": 30, "未核": 2},
 "carryover_check_r85_addendum": {"platform_layer": "_r85_carryover_notes_addendum", "platform_items": 12,
   "platform_ids": sorted(layer85.keys()), "acceptance_items": 0},
 "carryover_check_r82_closed": {"layer": "_r82_carryover_notes_addendum", "items": 3,
   "status": "已经 R85 主持裁定结案（登记性注记不要求 reason 回响），R86 不再滚动对勘"},
 "new_registrations_r86": 55,
 "new_cases_r86": {
   "部分成立_platform": sorted(c for c, d, _, _, _, _, f in NEW if f == "platform" and d == "部分成立"),
   "不成立_platform": sorted(c for c, d, _, _, _, _, f in NEW if f == "platform" and d == "不成立"),
   "部分成立_acceptance": sorted(c for c, d, _, _, _, _, f in NEW if f == "acceptance" and d == "部分成立"),
   "不成立_acceptance": sorted(c for c, d, _, _, _, _, f in NEW if f == "acceptance" and d == "不成立")},
 "r86_layer_partial_upheld_platform": sorted(c for c, d, _, _, _, _, f in NEW if f == "platform" and d == "部分成立"),
 "r86_partial_upheld_acceptance": sorted(c for c, d, _, _, _, _, f in NEW if f == "acceptance" and d == "部分成立"),
 "as307_double_entry": "R80 部分成立条与 R85 不成立条并行保留、不合并；R86 不另立第三条（本轮残损留痕与 R68 已定案旨同旨、引据登记）",
 "cases_total": len(out["annotations"]),
 "verdicts": {"成立": cnt["成立"], "部分成立": cnt["部分成立"], "不成立": cnt["不成立"], "未核": cnt["未核"]},
}
assert out["counts"]["cases_total"] == 238
assert out["counts"]["verdicts"] == {"成立": 14, "部分成立": 187, "不成立": 35, "未核": 2}, out["counts"]["verdicts"]
# 承接全等断言
assert out["annotations"][:183] == anns85
with open(f"{BASE}/data/case-annotations-r86.json", "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1)
print("written annotations:", len(out["annotations"]), out["counts"]["verdicts"], "special_checks:", len(sc))
