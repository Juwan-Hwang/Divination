#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""R93 holdout34 建卡·紫微族小席：只建本族 12 例（ZW-017..023, ZW-028..032）。
数据源（只读点名件）：round91 BATCH1、round92 BATCH2-XZS、round93 REVIEW-XZS7、
round93 BATCH3-ZJ、BATCH3-SUMMARY；盘面缺项回原书页图补录（见各 grade_note）。
体例：输入卡字段白名单与金标字段序照 holdout33-seal-log §六；
紫微卡格式对 holdout29/inputs/ ZW 卡实读。
"""
import json
from pathlib import Path

BASE = Path("/home/hatch/workspace/divination/benchmark/phase3")
OUT_DIR = BASE / "holdout34" / "inputs"
FRAG = BASE / "runs" / "round93" / "gold-frag-ziwei-r93.jsonl"
REPORT = BASE / "runs" / "round93" / "build-frag-ziwei-r93.json"

CARD_KEYS = ["id", "tradition", "subject", "context", "question", "setting",
"provenance", "redistributable", "license_status", "anchors"]
GOLD_KEYS = ["id", "master_prediction", "outcome_record", "tradition", "pollution",
"grade", "grade_note", "provenance", "license_status", "redistributable"]
QUESTION = "就此命盘求测（原书命例体例，无独立问句原文载录）"
CONTEXT = "紫微命例实批；命盘锚点载于 anchors"
LICENSE = "现代版权文本，内部研究用"

CASES = [
dict(
id="ZW-017",
subject="女命，甲申年四月初九丑时，木三局",
setting="《钦天四化紫微斗数命理学》（许铨仁讲述）·A10案例1（书p.26）",
provenance="《钦天四化紫微斗数命理学》（许铨仁讲述）·A10案例1（书p.26）；底本为用户自寻提供（紫微替代包 incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "甲申年四月初九丑时，女命",
"局": "木三局（原盘未直标局名，据命宫大限起岁3岁读出）",
"命宫": "命宫在辰，天同坐命",
"紫微落宫": "紫微在酉（奴仆宫）",
"四化锚点": "大运疾厄宫壬干化忌武曲入本命父母宫、忌冲本命疾厄宫；大运奴仆宫太阳生年忌又自化禄成双忌",
},
master_prediction="［命宫］代表这十年的命宫。［大疾］代表这十年身体健康位。（壬）［大疾33-42］化忌·武曲入［本父］；［大疾］忌冲［本疾］。理则五：同类宫职用冲体，必见凶象。为什么是39岁？因为她是甲申年的，从申宫开始数，不管是男生还是女生，顺数。理则：位法位，象法象的原则。奴仆宫，是论断寿元的关键。大运奴仆宫，生年忌又自化禄，谓之双忌。",
outcome_record="这位女士芳龄39岁，得子宫癌病逝了。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH1-r91 §3.5 四滤全过、锚点在场、low污染；断语／结局据登记件§3.2逐字转录（transcription=visual，置信度文字面0.97／盘面0.93），断语以右侧文字面原断全文为限、结局以标题句为限，两者分立；局数原盘未直标，据命宫大限起岁3岁读出为木三局，已于输入卡anchors注明；讲授回溯实录，断语与已发生事件俱在书内、具体可分离（A-low）。",
leak=["子宫癌", "病逝", "39岁"],
),
dict(
id="ZW-018",
subject="女命，戊子年九月申时，水二局",
setting="《钦天四化紫微斗数命理学》（许铨仁讲述）·A10案例2（书p.27）",
provenance="《钦天四化紫微斗数命理学》（许铨仁讲述）·A10案例2（书p.27）；底本为用户自寻提供（紫微替代包 incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "戊子年九月申时，女命",
"局": "水二局（原盘未直标局名，据命宫大限起岁2岁读出）",
"命宫": "命宫在寅，廉贞、文昌坐命",
"紫微落宫": "紫微在戌（财帛宫）",
"四化锚点": "大运夫妻宫紫微自化权、权带破耗，大夫飞化忌冲本夫；后段大运夫妻宫天机生年忌＋巨门自化禄构成双忌",
},
master_prediction="理则：（1）有自化，一定有变化。（2）旧有的结束，崭新的开始。（3）有时间观念。理则：位法位，象法象的原则。大运夫妻宫变成流年夫妻宫。理则：自化权或者视同自化权，带有变化中带破耗。（壬）［大夫22-31］化忌冲［本夫］。理则五：同类宫职用冲体，必见凶象。婚姻亮红灯，变化中带破耗。因为大夫自化权，权带破耗。象就是气，就是自化权的气。气讲往来。所以这种变化中带破耗感应在29岁。34岁走到大运夫妻宫，走到发射宫。天机生年忌+巨门自化禄，构成双忌，二倍的凶，结果论。",
outcome_record="25才结婚，29岁离婚；34岁结婚，36岁离婚。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH1-r91 §3.5 四滤全过、锚点在场、low污染；断语／结局据登记件§3.3逐字转录（transcription=visual，置信度文字面0.95／盘面0.93；一处语序句置信约0.85、不涉判定项，未入本金标），断语以右侧文字面原断为限、结局以标题四事件句为限，两者分立；下图疾厄格多载天姚一星之两图出入不涉主星与断语，照登记件注记；局数原盘未直标，据命宫大限起岁2岁读出为水二局；讲授回溯实录（A-low）。",
leak=["结婚", "离婚"],
),
dict(
id="ZW-019",
subject="男命，丙戌年8月申时（日数原书未标），土五局",
setting="《紫微斗数命运分析》（徐曾生著）·第25章四化飞星活用例解主例（书pp.241–250）",
provenance="《紫微斗数命运分析》（徐曾生著）·第25章例解主例（书pp.241–250）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "丙戌年8月申时，男（日数原盘未标，照实登记）",
"局": "土五局",
"命宫": "命宫在丑，天相坐命",
"紫微落宫": "紫微在未（迁移宫）",
"四化锚点": "本命事业宫紫府朝垣格；廉贞化忌、巨门文曲是非之星、同类相冲；本命疾厄化忌入大限疾厄、双层忌星",
},
master_prediction="本命事业宫紫府朝垣格，释其富贵；大限、流年以廉贞化忌、巨门文曲是非之星、同类相冲逐步推演；看疾厄大限盘以本命疾厄化忌入大限疾厄、大限疾厄累积双层忌星的凶力推演。",
outcome_record="这位先生曾是叱咤一时的大富翁，在甲子年开始崩溃，一发不可收拾，结果于乙丑年因所开支票无法兑现，正月即依违反票据法被捕入狱。该命例于七十六年因癌症在监狱内吐血而亡。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH2-XZS-r92（XZS-08）四滤全过、锚点在场、low污染；结局据登记件逐字引文（书p.242章首叙事＋p.248后记）照录、以结局正文为限，断语据登记件断语要点以原断推演为限组录，与结局分立（A-low：作者回溯解说已发生且经报纸报导之事件）；命宫地支与紫微落宫登记件未载，经本席回原书p.241本命盘图300dpi补录（命宫在丑、天相坐命，紫微在未；页图存runs/round93/supply/pages-xzs-h34-ziwei-r93/，transcription=visual，置信高）；日数原盘未标、不臆补。",
leak=["入狱", "崩溃", "癌症", "吐血", "支票", "票据法"],
),
dict(
id="ZW-020",
subject="阴男，癸巳年11月3日丑时，水二局",
setting="《紫微斗数命运分析》（徐曾生著）·第28章命例（取自楚皇著作，书p.270）",
provenance="《紫微斗数命运分析》（徐曾生著）·第28章命例（取自楚皇著作，书p.270）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "癸巳年11月3日丑时，阴男（原盘另标「42年」）",
"局": "水二局",
"命宫": "命宫在亥，无正曜（空宫）",
"紫微落宫": "紫微在寅（田宅宫）",
"四化锚点": "本命财帛化忌冲命宫；大限财帛丁干巨门自化忌；大限事业化忌入本命事业宫冲大限命宫；自化忌主漏出、流失",
},
master_prediction="本命财帛化忌冲命宫，大限财帛在丁巳宫丁干巨门自化忌，大限事业化忌入本命事业宫冲大限命宫，自化忌为漏出、流失之象。",
outcome_record="依据书中所载，此人从事建筑业，二十九岁辛酉年时被倒一百萬。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH2-XZS-r92（XZS-12）四滤全过、锚点在场、low污染；结局据登记件逐字引文（书p.270）照录、以结局正文为限（引文后半「原书未解说，现在来分析看看」为编述语、不入结局），断语据登记件断语要点以原断为限组录，与结局分立；转引他书已发生事实、本书作者回溯解说（A-low）；transcription=visual，置信高。",
leak=["被倒", "建筑业", "辛酉", "一百萬"],
),
dict(
id="ZW-021",
subject="阴女，丁酉年11月卯时（日数原书未标），土五局",
context="紫微命例实批（31岁求测，命例主人在日本开礼品店）；命盘锚点载于 anchors",
setting="《紫微斗数命运分析》（徐曾生著）·第19章案例一（书pp.180–183）",
provenance="《紫微斗数命运分析》（徐曾生著）·第19章案例一（书pp.180–183）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "丁酉年11月卯时，阴女（日数原盘未标，照实登记）",
"局": "土五局",
"命宫": "命宫在酉，无正曜（空宫）",
"紫微落宫": "紫微在辰（疾厄宫，紫微天相）",
"四化锚点": "流日子时福德宫内坐太阳、太阴；贪狼化忌入流时田宅宫冲福德宫（同类相冲）",
},
master_prediction="「你昨晚子时，是不是为了头发的事，在伤脑筋。」解析：31岁（丁卯年），流日子时的福德宫内坐太阳、太阴（天干（癸）贪狼化忌入流时田宅宫冲流月福德宫，因为已知是烦恼事，故以福德宫为显象宫），符合同类相冲的条件；太阳（头部）、太阴（头发），是为了头发的事而烦心。",
outcome_record="命例主人前一日晚上十一时许，由礼品店坐电车回家途中反覆思量：头发已经好几天没洗了，不太好，回去马上洗，等弄干已很晚了，明天一大早要赶去大师处，可能会睡眠不足；第二天到大师处，命盘一排开，大师第一句话就说中其心中所想，当场就把命例主人吓呆了。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH2-XZS-r92（XZS-05）四滤通过、法项挂起后经ZIWEI-REVIEW-XZS7-r93复评通过（断法演示型登记D5-19-05／06／08）；断语据复评件锚点回读（书p.180逐字在场）与原书p.181解析面照录，结局据原书p.180「事情的缘由」叙事正文照录、以结局正文为限，断语（大师当场第一句话）与结局（命主前夜思量之事与当场确认）文本分立、非同文；当场断中、命主即时确认型（A-low）；命宫地支与紫微落宫登记件未逐载，经本席回原书p.181盘图300dpi补录（命宫在酉、无正曜，紫微在辰；页图存runs/round93/supply/pages-xzs-h34-ziwei-r93/，transcription=visual，置信高）；日数原盘未标、不臆补；断者为长住日本之另一位大师（非徐曾生），照登记件登记。",
leak=["头发", "伤脑筋", "吓呆", "洗了"],
),
dict(
id="ZW-022",
subject="阴女，癸酉年12月辰时（日数原书未标），木三局",
setting="《紫微斗数命运分析》（徐曾生著）·第26章命盘十六（书pp.257–258）",
provenance="《紫微斗数命运分析》（徐曾生著）·第26章命盘十六（书pp.257–258）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "癸酉年12月辰时生，阴女（日数原盘未标，照实登记）",
"局": "木三局",
"命宫": "命宫在酉，廉贞、破军坐命",
"紫微落宫": "紫微在巳（财帛宫，紫微七杀）",
"四化锚点": "杀破狼格局（财帛宫紫微七杀、事业宫武曲贪狼擎羊）；大限财帛天同化忌入大限命宫，大限命宫廉贞化禄、破军化权入本命宫",
},
master_prediction="她的命盘，财帛宫坐，事业宫坐，三合是的格局，故而医生、助产士的行业适合。大限走到子限时（三十三—四十二岁）：大限的财帛在庚申，天同化忌又入大限命宫。大限命宫甲子，廉贞化禄，破军化权入本命宫。因大限命宫和田宅宫重叠，故房地产会增加（当然本造有其他条件配合—大限命宫甲子，表示财帛化禄和权都同挤入大限命宫，表示会为赚钱而在家中忙得不可开支，因禄权同宫，所以赚钱应该在很自然，没有刻意强求的状况下，成就其事业的。",
outcome_record="这位女士在民国五十四年至六十三年间当密医，赚了五、六栋房子。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH2-XZS-r92（XZS-10）四滤通过、法项挂起后经ZIWEI-REVIEW-XZS7-r93复评通过（断法登记D5-26-01／02／04）；结局据登记件逐字引文（书p.257）与复评件锚点回读照录、以结局正文为限，断语据原书p.258正文逐字照录、以原断为限，两者分立；已发生事实回溯解说（A-low）；命宫地支与紫微落宫登记件未逐载，经本席回原书p.258命盘十六盘图补录（命宫在酉、廉贞破军坐命，紫微在巳；transcription=visual，置信高）；日数原盘未标、不臆补。",
leak=["密医", "五、六栋", "五十四年"],
),
dict(
id="ZW-023",
subject="阳男，甲戌年12月13日巳时，金四局",
setting="《紫微斗数命运分析》（徐曾生著）·第28章命例一（书pp.276–279）",
provenance="《紫微斗数命运分析》（徐曾生著）·第28章命例一（书pp.276–279）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "甲戌年12月13日巳时，阳男",
"局": "金四局",
"命宫": "命宫在申，七杀坐命",
"紫微落宫": "紫微在寅（迁移宫，紫微天府）",
"四化锚点": "杀破狼格局；生年四化化禄入夫妻、化权入官禄、化科入福德；以子女宫为合伙人代表宫",
},
master_prediction="命盘排出来是杀破狼的格局，生年天干四化之化禄入夫妻，化权入官禄，化科入福德，三吉化星有入照本命三方，是属于具有事业雄心之格局，但是杀破狼格的人大多早年辛勤，成败不一。以事业宫当命宫、本命子女宫为合伙人代表宫：子女宫为做生意的交友宫，合伙人帮我赚钱迹象。",
outcome_record="这位先生曾经多次独资创业，但是屡做屡败，后来因为资金不足，不得不与朋友合伙，结果开始赚钱，并有余钱置产购屋。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH2-XZS-r92（XZS-13）四滤通过、法项挂起后经ZIWEI-REVIEW-XZS7-r93复评通过（断法登记D5-28-07／10／08／11）；结局据登记件逐字引文（书p.276）与复评件锚点回读照录、以结局正文为限，断语据原书p.276–277正文与复评件回读（子女宫立向、合伙人帮我赚钱迹象）以原断为限组录，两者分立；已发生事实回溯解说（A-low）；命宫地支与紫微落宫登记件未逐载，经本席回原书p.276命例一盘图补录（命宫在申、七杀坐命，紫微在寅；transcription=visual，置信高）。",
leak=["屡做屡败", "置产购屋", "多次独资创业"],
),
dict(
id="ZW-028",
subject="女命，庚子年12月子时（日数原书未标），火六局",
setting="《紫微斗数命理学正解》（许铨仁著）·第五章第三节案例一（书pp.227–232）",
provenance="《紫微斗数命理学正解》（许铨仁著）·第五章第三节案例一（书pp.227–232，另第三章书pp.103–108同例理则示例）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "民国49年生，庚子年12月子时，女命（日数原盘未标，照实登记）",
"局": "火六局",
"命宫": "命宫在丑（己丑），无十四主星（天魁坐守）",
"紫微落宫": "紫微在戌（子女宫，紫微天相）",
"四化锚点": "生年化禄、化科在迁移宫，生年化权在奴仆宫，生年化忌在官禄宫；大运夫妻宫与本命子女宫叠宫、流年命宫与大运夫妻宫叠宫",
},
master_prediction="生年化禄、化科在迁移宫；生年化权在奴仆宫；生年化忌在官禄宫（天同）。大运夫妻宫与本命子女宫叠宫、流年命宫与大运夫妻宫叠宫而引爆；第三章以理则（七）「A宫＋B宫＝禄＋生年忌」等式推演婚变。",
outcome_record="（一）民國七十二年，芳齡二十四歲步上地毯，結婚了。（二）隔年，二十五歲，竟而離婚矣。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH3-ZJ-r93（ZJ-01）四滤全过、锚点在场、low污染，主持汇编收口续编ZW-028（ZIWEI-SUPPLY-BATCH3-SUMMARY-r93 §三）；结局据登记件摘要記述逐字照录（书p.227，中间数字词个别字置信0.85、事件与年份年龄无疑）、以结局正文为限，断语据登记件作者断语要点以原断为限组录，与摘要分立；讲授回溯实录（A-low）；盘面经登记件裁剪复核转录（crops-zhengjie-r93/），transcription=visual；日数原盘未标、不臆补。",
leak=["結婚", "離婚", "二十四歲", "二十五歲", "七十二年"],
),
dict(
id="ZW-029",
subject="女命，壬辰年6月子时（日数原书未标），水二局",
setting="《紫微斗数命理学正解》（许铨仁著）·第五章第三节案例二（书pp.231–237）",
provenance="《紫微斗数命理学正解》（许铨仁著）·第五章第三节案例二（书pp.231–237）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "民国41年生，壬辰年6月子时，女命（日数原盘未标，照实登记）",
"局": "水二局",
"命宫": "命宫在未（丁未），太阳、太阴坐命",
"紫微落宫": "紫微在戌（田宅宫，紫微天相）",
"四化锚点": "命宫太阳太阴自化禄出；夫妻宫宫干乙使太阴化忌冲命宫；22–31大运命宫与本命夫妻宫重叠",
},
master_prediction="命宫太阳太阴同坐，个性中庸，恋爱观保守，而自化禄出；夫妻宫宫干乙使太阴化忌冲命宫；行运22–31大运命宫与本命夫妻宫重叠引爆。",
outcome_record="女壬年生，卅一歲紅杏出牆，終告與夫他離，人隨桃花而去矣；剖析文内复述：終告於31歲時離婚矣。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH3-ZJ-r93（ZJ-02）四滤全过、锚点在场、low污染，主持汇编收口续编ZW-029；结局据登记件摘要記述（逐字大意）与剖析文内复述句照录、以结局正文为限，断语据登记件作者断语要点以原断为限组录，与摘要分立；讲授回溯实录（A-low）；摘要题下「心素」二字疑为命主化名标记（置信0.7）、不入卡；transcription=visual；日数原盘未标、不臆补。",
leak=["紅杏出牆", "離婚", "桃花而去"],
),
dict(
id="ZW-030",
subject="女命，丁酉年5月卯时（日数原书未标），金四局",
setting="《紫微斗数命理学正解》（许铨仁著）·第五章第三节案例四（书pp.244–248）",
provenance="《紫微斗数命理学正解》（许铨仁著）·第五章第三节案例四（书pp.244–248，§三总语书p.248复述）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "民国46年生，丁酉年5月卯时，女命（日数原盘未标，照实登记）",
"局": "金四局",
"命宫": "命宫在卯（癸卯），空宫（无十四主星）",
"紫微落宫": "紫微在亥（财帛宫，紫微七杀）",
"四化锚点": "命宫宫干癸使贪狼化忌入官禄；本宫自化忌与双忌叠宫；命宫化忌冲夫妻宫",
},
master_prediction="命宫宫干癸使贪狼化忌入官禄（夫妻宫之事业宫位读法）、本宫自化忌与双忌叠宫理则；书248总语：命宫化忌冲夫妻宫，其夫先天定数已定。",
outcome_record="民國七十一年，嚴×女士，芳齡27歲，先生逝矣。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH3-ZJ-r93（ZJ-04）四滤全过、锚点在场、low污染，主持汇编收口续编ZW-030；结局据登记件摘要記述逐字照录（书p.244）、以结局正文为限——摘要「逝」前一字登记件标注单字置信低（视读为「瘋」、疑为「病」之形近误读），本金标只取「先生逝矣」无疑部分、不臆补该字；断语据登记件作者断语要点与书p.248总语以原断为限组录，与摘要分立；半匿名私命（A-low）；transcription=visual；日数原盘未标、不臆补。",
leak=["逝矣", "嚴", "七十一年", "27歲"],
),
dict(
id="ZW-031",
subject="男命，辛丑年2月午时（日数原书未标），火六局",
setting="《紫微斗数命理学正解》（许铨仁著）·第六章第二节案例一（书pp.257–262）",
provenance="《紫微斗数命理学正解》（许铨仁著）·第六章第二节案例一（书pp.257–262）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "民国50年生，辛丑年2月午时，男命（日数原盘未标，照实登记）",
"局": "火六局",
"命宫": "命宫在酉（丁酉），无十四主星（右弼、火星、禄存坐守）",
"紫微落宫": "紫微在卯（迁移宫，紫微贪狼）",
"四化锚点": "终身交通安全三宫位（命、迁、疾）组合；大运命宫宫干丙使天机化权飞至奴仆宫；流年命宫走至生年科之宫位",
},
master_prediction="终身交通安全三宫位（命、迁、疾）剖析；大运命宫（16–25）宫干丙使天机化权直系化飞至奴仆宫、视同自化权与自化权之解；22岁流年命宫走至生年科之宫位引爆。",
outcome_record="（一）本命造係男命，民國五十年生，騎機車發生車禍時，為國立交通大學學生。（二）民國七十一年，廿二歲時不幸發生車禍，手臂斷了而致殘疾。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH3-ZJ-r93（ZJ-05）四滤全过、锚点在场、low污染，主持汇编收口续编ZW-031；结局据登记件摘要記述逐字照录（书p.257）、以结局正文为限，断语据登记件作者断语要点以原断为限组录，与摘要分立；讲授回溯实录（A-low）；盘面经登记件剖析页单宫小图与盘面互证；transcription=visual；日数原盘未标、不臆补。",
leak=["車禍", "殘疾", "交通大學", "手臂斷"],
),
dict(
id="ZW-032",
subject="男命，乙巳年3月巳时（日数原书未标），土五局",
setting="《紫微斗数命理学正解》（许铨仁著）·第六章第二节案例二（书pp.263–266）",
provenance="《紫微斗数命理学正解》（许铨仁著）·第六章第二节案例二（书pp.263–266）；底本为学校图书馆件（incoming/wanted-books-6），redistributable=false",
anchors={
"birth": "民国54年生，乙巳年3月巳时，男命（日数原盘未标，照实登记）",
"局": "土五局",
"命宫": "命宫在亥（丁亥），紫微、七杀坐命",
"紫微落宫": "紫微在亥（命宫）",
"四化锚点": "命、迁、疾三宫位组合象；大运大命化忌入本疾；流年命宫走至子宫（太阴血光之星）",
},
master_prediction="命、迁、疾三宫位组合象；大运（15–24）大命化忌入本疾，20岁流年命宫走至子宫（太阴血光之星），须特别留意血光之灾。",
outcome_record="（一）翁×輝（苗栗人），18歲離鄉，出外謀生。（二）20歲時發生車禍，左腿骨折，開刀縫了數拾針。",
grade_note="入账口径：ZIWEI-SUPPLY-BATCH3-ZJ-r93（ZJ-06）四滤全过、锚点在场、low污染，主持汇编收口续编ZW-032；结局据登记件摘要記述（逐字大意，姓名首字与个别字置信0.8、事件无疑）照录、以结局正文为限，断语据登记件作者断语要点以原断为限组录，与摘要分立；半匿名私命（A-low）；盘面经登记件单宫小图互证；transcription=visual；日数原盘未标、不臆补。",
leak=["車禍", "骨折", "離鄉", "翁"],
),
]

FIELD_NOTES = [
"输入卡字段序与白名单照holdout33-seal-log §六、卡面排版对holdout29/inputs/ ZW卡实读：id, tradition, subject, context, question, setting, provenance, redistributable, license_status, anchors；金标字段序：id, master_prediction, outcome_record, tradition, pollution, grade, grade_note, provenance, license_status, redistributable。",
"tradition全例=ziwei；pollution全例=low；grade全例=A-low；redistributable全例=false；license_status全例=现代版权文本，内部研究用（照登记件来源登记）。",
"subject组写＝性别＋干支年月时＋局数（日数原书未标者逐例注明）；question全例照holdout29紫微卡体例组写（原书命例体例、无独立问句原文载录）；context全例=紫微命例实批；命盘锚点载于anchors（ZW-021另注31岁求测背景）。",
"anchors键组＝birth／局／命宫／紫微落宫／四化锚点：birth、局数、命宫主星以登记件转录为准；登记件缺载项回原书页图补录——ZW-019命宫在丑·天相坐命、紫微在未（原书p.241盘图300dpi，页图存runs/round93/supply/pages-xzs-h34-ziwei-r93/）；ZW-021命宫在酉·无正曜、紫微在辰（原书p.181盘图300dpi，同目录）；ZW-022命宫在酉·廉贞破军、紫微在巳（原书p.258盘图）；ZW-023命宫在申·七杀、紫微在寅（原书p.276盘图）；ZW-017／018局数原盘未直标，据命宫大限起岁读出（起岁＝局数：ZW-017命宫大限3–12→木三局、ZW-018命宫大限2–11→水二局），已于各卡anchors注明读法。",
"金标编例：结局以案验／结局正文为限（ZW-017标题句、ZW-018标题四事件句、ZW-019章首叙事＋后记、ZW-020摘要引文正文、ZW-021事情的缘由叙事、ZW-022结局句、ZW-023结局句、ZW-028／029／030／031／032摘要記述），断语以原断全文为限（ZW-017／018／022／023据逐字转录面照录，其余据登记件断语要点／总语以原断为限组录）；复玩文尾、附议、编注不入。",
"锚点核（工序①）逐例结论：12例断语均在登记件逐字或要点在场、且与结局文本分立，无断语与结局同文／互串例，stop_items为空。",
"provenance照登记件来源登记：ZW-017／018《钦天四化紫微斗数命理学》（许铨仁讲述）；ZW-019–023《紫微斗数命运分析》（徐曾生著，学校图书馆件）；ZW-028–032《紫微斗数命理学正解》（许铨仁著，学校图书馆件）。",
]

STRIP_COMMON = ["master_prediction（大师断语）→只入金标分片、不入输入卡",
"outcome_record（结局）→只入金标分片、不入输入卡",
"grade／grade_note／pollution→只入金标分片、不入输入卡",
"盘面逐宫全录未入卡：anchors只取birth／局／命宫／紫微落宫／四化锚点五项"]

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    built, gold_lines = [], []
    strip_register = {}
    for c in CASES:
        card = {
            "id": c["id"], "tradition": "ziwei",
            "subject": c["subject"],
            "context": c.get("context", CONTEXT),
            "question": QUESTION,
            "setting": c["setting"],
            "provenance": c["provenance"],
            "redistributable": False,
            "license_status": LICENSE,
            "anchors": c["anchors"],
        }
        assert list(card.keys()) == CARD_KEYS, (c["id"], list(card.keys()))
        blob = json.dumps(card, ensure_ascii=False)
        for w in c["leak"]:
            assert w not in blob, f"LEAK {c['id']}: {w}"
        gold = {
            "id": c["id"],
            "master_prediction": c["master_prediction"],
            "outcome_record": c["outcome_record"],
            "tradition": "ziwei",
            "pollution": "low",
            "grade": "A-low",
            "grade_note": c["grade_note"],
            "provenance": c["provenance"],
            "license_status": LICENSE,
            "redistributable": False,
        }
        assert list(gold.keys()) == GOLD_KEYS
        (OUT_DIR / f"{c['id']}.json").write_text(
            json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        gold_lines.append(json.dumps(gold, ensure_ascii=False))
        built.append(c["id"])
        strip_register[c["id"]] = list(STRIP_COMMON)
    strip_register["ZW-021"] = list(STRIP_COMMON) + ["断者身份（长住日本之另一位大师）只登记于金标grade_note、不入卡面"]
    strip_register["ZW-029"] = list(STRIP_COMMON) + ["摘要题下「心素」二字（疑命主化名标记，置信0.7）未入卡、未入金标"]
    strip_register["ZW-030"] = list(STRIP_COMMON) + ["摘要「逝」前一字（单字置信低）未入任何产物、不臆补"]
    FRAG.write_text("\n".join(gold_lines) + "\n", encoding="utf-8")
    report = {
        "built_ids": built,
        "stop_items": [],
        "field_mapping_notes": FIELD_NOTES,
        "strip_register": strip_register,
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("built:", len(built), built)
    print("gold lines:", len(gold_lines))

if __name__ == "__main__":
    main()
