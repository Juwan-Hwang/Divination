# -*- coding: utf-8 -*-
"""Round55 B20 blind predictions writer (this batch only)."""
import json, os

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round55/predictions"
os.makedirs(OUT, exist_ok=True)

TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

P = {}

P["OC-018"] = {
 "prediction_text": "方向：贵显而带横险——一生以财与名望成巨头之业（报业经营致富、名重一时），地位至社会名流/行业首脑级，非官贵正途之极品；晚年行运转凶，有横祸寿关。格局量级区间：下限为富而有名（依据：财星卯寅两见成势、杀印相生有名位之托）—上限为行业巨头/名流领袖（依据：月令伤官当权、丙杀透而己印化杀生身，成中有救，非清贵纯官之格，上限止于名望财业一途）。逐运（阴年男逆行，自月柱丙子逆排；起运岁数卡面无生辰不可精算，年龄为约数）：乙亥运平（财伤并见，少年家业未振）；甲戌运平偏吉（甲财透、戌为火库，经营起步）；癸酉运吉（癸伤生财、酉金助身任财，事业扩张之始）；壬申运吉（申金得地助身、壬水生财链成，为一生高峰运段，报业版图与声望在此运登顶）；辛未运凶（辛劫争财、未土晦火填杀而子未相害，财名两途起争端，运末为转折带）；庚午运凶（午火七杀冲月令子水伤官，杀旺攻身、伤官见杀无印之运干可化，主横祸）。终局：寿关在辛未运末至庚午运初交运带，主坐标落在甲戌年一带（约1934年、54岁前后）：甲木财透生杀、戌土引动火势，杀重身泄，主遭人暗害/横死之险，不得善终高寿。子女/承继：时柱辛巳，官杀在时、巳中庚金有根，子女有而承继之势弱于创业之势，家业在其身后难守其盛。病位：病字为丙火七杀与子水伤官相战，火主心血、水主肾膀胱，晚年防心脑血管急症，但首要之厄为横祸而非久病。破财之因：劫财辛金与财星相争，因同业/政争与人事倾轧耗财招祸，非经营失算。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字（子平，立春换年、节气换月）。\n四柱：己卯 丙子 庚寅 辛巳，庚金日主生子月。特格扫描：从格未命中（庚有巳中长生根、辛劫透、己印生，不合无根无扶四据）；专旺未命中；寒极未命中（丙巳火有根可暖）。主线：①格局——月令子水伤官当权，丙火七杀透月干，伤官见杀为成中有败；年干己土正印化杀生身、时干辛金助身为救应，格成而带病。②用神——印（己土）与比劫为救，状态得力中等。③定性——常规格，调候冬金喜火暖而不喜火旺攻身。病药链：病＝丙火七杀（月干，病型破格，冬月无根但得寅巳木火之根党）；药＝己土正印（年干，以化法去病，有根于寅巳戊土，得力中等）；扶抑取向＝喜印比扶身任财杀，忌财生杀太过与杀冲令。峰值运三核对：壬申运①申为庚金临官得地满足②运干壬水食神泄秀生财、与局中财链呼应满足③否决清单(i)壬不合绊用神己(ii)申不冲印根(iii)壬非忌神透出——满足3项，定为峰值；辛未运否决(ii)未冲巳、(i)未合己，但未土填杀害子、方向逆主线，列低运。否决三条核查（壬申运）：①运干合绊用神：未命中；②运支冲克用神之根：未命中；③运干透忌神且通根：未命中。应期：尺度定年档（问一生地位与晚年行运，先运后年）；三路候选——运年触发（庚午运午冲子）、合冲引动（甲戌年戌引火势、财生杀）、值年值月（丙丁火杀值年），取合冲引动一路为主坐标（甲戌年一带），余二路舍：值年路只定年内轻重不单独成寿关、运年触发之午冲子在庚午运内与甲戌交运带合看不另立。残损注明：卡面只给四柱，无公历生辰、出生地与大运原排，起运岁数不可精算，年龄与年份为按运序推得之约数，置信据此降档。",
 "confidence": 0.52,
}

P["OC-019"] = {
 "prediction_text": "方向：显达而横夭——命主以学术/干事之才居研究院总干事级要职，名位清显至厅局级学术领袖，但行运有暴烈横关，中年遭横祸凶死，不得寿终。格局量级区间：下限为清贵有职（依据：申金印根护身、丙财透有俸禄之源）—上限为学术机构首长级（依据：辰月杂气、官杀土藏而不透，贵气藏多于透，财格为主、官格未纯，上限不及政枢极品）。逐运（阴年男逆行，自月柱丙辰逆排，年龄约数）：乙卯运平（伤官见官之象萌，少年聪敏而多口舌）；甲寅运平偏吉（伤官生财，学业游历有成）；癸丑运吉（癸劫助身、丑土印库藏金，任职立名之运）；壬子运凶（壬比子水劫旺成势，子卯相刑、子辰半合而水势泛溢，劫财夺财破格，又子水冲动午外之火无据，唯水旺金寒、刑冲交加为此运定性）；辛亥运未及论寿（已殁于前运）。终局险年：壬子运内癸酉年（约1933年、40岁前后）为主坐标——酉金冲时支卯木伤官，伤官被冲而官杀辰土得金泄后转克之链乱，子卯刑与卯酉冲同岁叠见，主横祸：遭暗杀/枪刃之害暴死，非病终。子女/承继：时柱癸卯，食伤在时而官杀为子女星藏辰，子女缘薄或身后承继无人接其位。病位：病字为辰丑湿土官杀与过旺之水，土主脾胃、水主肾与血，然终局之厄为横祸先于病厄。破财之因：两癸劫财透干、子运劫旺，因同僚争竞与人事倾轧耗名耗财，并引横祸，非经营之失。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字（子平）。\n四柱：癸巳 丙辰 壬申 癸卯，壬水日主生辰月。注记：卡面自注他书另载全异四柱、本例以本卡为准，已按卡面断。特格扫描：从格未命中（壬有申长生强根、两癸助、申印生）；专旺未命中；寒湿偏枯未命中（三月非冬令、巳丙火有暖）。主线：①格局——辰月杂气，丙火偏财透月干为财格之象，癸劫两透争财破格，巳中戊杀、辰中戊杀藏而攻身为病；②救应——日支申金偏印长生根，化劫生身、泄杀之气，为格之救；③定性——常规格，身有根可任财，喜印比、忌劫旺夺财与刑冲伤官。病药链：病＝癸水劫财（年时两透，病型太过兼破格，根在申子）；药＝申金印星（日支，以化法泄劫生身，得令根深、得力）；扶抑取向＝喜印比护身任财，忌子水劫运与卯酉冲。峰值运三核对：癸丑运①丑中辛金印有根、癸水得库②运干癸为比助非用神透出只半应③否决(i)癸不合丙财用神干？丙财为格神，癸与丙无合绊，(ii)丑不冲申印根，(iii)癸劫非忌透而通根丑——劫通根一项近忌，峰值只记次峰；全程各运均≤2项且无满格之运，相对以癸丑为次峰、无极盛峰值。否决三条核查（癸丑运）：①未命中；②未命中；③癸为劫财忌神而丑为其库根，记部分命中，故只称次峰不称峰值。应期：尺度年档；三路——运年触发（壬子运水劫成势）、合冲引动（癸酉年酉冲卯、子卯刑）、值年（酉金印值年本为救路，但冲伤官在先，救不及），取合冲引动为主坐标癸酉年，余路舍：值年路方向与终局相悖、运年触发只定运段不定年。残损：无公历生辰与大运原排，年份年龄为约数，置信降档。",
 "confidence": 0.5,
}

P["OC-020"] = {
 "prediction_text": "方向：贵至极品而寿不满——食神制杀成格，命主贵显至国民政府主席级/政枢最高层，为本批贵气最重之造；但身弱杀重、财生杀为病，中年后运入财杀引动之年主暴病而终，寿约五十。格局量级区间：下限为方面大员（依据：食神制杀成格、两卯食神有根）—上限为国家最高名位（依据：杀格得制、印藏丑中辛金可化杀，制化两全之象容此级；压低依据：癸水日主无强根、丁财透生杀，贵成而身不耐久，故寿与贵不两全，不压贵级而压寿数）。逐运（阴年男逆行，自月柱丁丑逆排，年龄约数）：丙子运吉（子水扶身、丙财有子制其流，少年顺遂）；乙亥运大吉（乙食神得亥生、亥水扶身任杀，制杀得力，青年发贵之基）；甲戌运平偏凶（甲伤生丁财、戌土杀库填实，财杀攻身，仕途起伏带险）；癸酉运吉（癸比扶身、酉金印星化杀生身，位望隆盛）；壬申运吉中藏凶（壬劫申印扶身任杀登峰，此运内得最高名位；然申子外火无根，庚午年财杀齐到为运内寿关）；辛未运不及。终局：高峰在壬申运（约44–53岁段），主位在此运坐定；险年主坐标庚午年（约1930年、50岁前后）——午中丁财己杀同到，财生杀攻弱身、午冲运支子外无解（按：冲去扶身之水势），主急病暴终，病在心脑（火土压水，主脑溢血/中风类急症）。子女/承继：时柱乙卯食神，男命以官杀为子女星，杀在年、月支丑而被制，子女有而承其位者无，家声在其身后转衰。病位病名：病字为丑己七杀与丁火财（月柱），土主脾胃、火主心脑，终局病位以心脑血管急症为断。破财之因：财星丁火在本造非破财之主，耗损之因在财生杀——因位高与政事耗神耗财，非产业失利。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字（子平）。\n四柱：己卯 丁丑 癸丑 乙卯，癸水日主生丑月。特格扫描：从官杀未命中（癸有丑中癸根、卯木食神两根成党制杀，日主有自立之路，不合从杀四据）；专旺未命中；寒极近似而未立（冬月而丁火透、卯木可生火，火有出路）。主线：①格局——丑月己土七杀透年干为七杀格，时干乙木食神透、两卯为根，食神制杀成格；②病——月干丁火偏财生杀助杀，财党杀为成中之败；③救应——乙卯食神制杀为主救，丑中辛金印星化杀为次救，制化并行故贵显。病药链：病＝丁火偏财（月干，病型破格，生杀太过，根在午外无、借卯木为源）；药＝乙木食神（时干，以制法去杀之势，两卯强根，得力）；扶抑取向＝喜食伤制杀、印比扶身，忌财杀同到之运年。峰值运三核对：壬申运①申中壬水日主得长生、辛印有根，用神乙木于申无根——①以扶身之印比得地记满足②运干壬劫扶身、申印化杀呼应救应记满足③否决(i)壬不合乙(ii)申不冲卯食根（申卯无冲）(iii)壬非忌神——满足3项定峰值；乙亥运同为3项候选而先到，然乙亥在青年只立基，运序在前——按同分以先到为峰之规，乙亥与壬申同满足3项并列，乙亥称峰值之基、壬申为位望之峰（名位落点以后运为准，留痕并列）。否决三条核查（壬申运）：①未命中；②未命中；③未命中。应期：尺度年档；三路——运年触发（壬申运扶身登峰）、合冲引动（庚午年午火财杀攻身）、值年（辛金印值年路在本运后段不及），登峰取运年触发、寿关取合冲引动庚午年为主坐标，值年路舍（时点已过终局）。残损：无公历生辰与大运原排，年份年龄约数，置信降档。",
 "confidence": 0.55,
}

P["OC-021"] = {
 "prediction_text": "方向：一时封疆、晚节衰落——命主以武力起家，贵显至督军/巡阅使、统两广之封疆级军阀首领，权势煊赫于中年；然格有财生杀、伤官被合之病，晚运财杀攻禄，失势闲居，终以衰病老终，寿近古稀。格局量级区间：下限为武职方面之员（依据：丙火伤官制杀、乙木坐卯禄有根可任杀）—上限为封疆军阀首领（依据：酉月辛杀当令成势、食伤午丙制杀得局，武贵之格容此级；压低依据：丙辛相合伤官被绊、戊财生杀，制杀不纯，故其贵为草莽兵权之贵、非文治功名之贵，且晚年必失其势）。逐运（阳年男顺行，自月柱辛酉顺排，年龄约数）：壬戌运平（壬印化杀、戌库收火，少年平顺）；癸亥运吉（印星得地扶身，学武从戎起家）；甲子运吉（甲劫助身、子印化杀，兵权渐握）；乙丑运平偏吉（乙比坐丑财库，扩军聚财而丑酉合金助杀，权与险并进）；丙寅运大吉（丙伤制杀、寅为乙木长生又藏丙火，制杀得力，为一生高峰前段，兵权登峰）；丁卯运吉（丁食卯禄，食神制杀而禄根固守，督粤督桂之盛在此运，然卯酉冲贯穿运内，盛中带战）；戊辰运凶（戊财透生杀、辰冲戌火库又辰酉合金，财杀齐攻禄根，失势下野之运）；己巳运不及或余烬。终局：戊辰运内戊辰/己巳年一带（约1928年前后、69岁前后）为终局坐标——财杀攻身、禄根被合冲，主失位后衰病而终。子女/承继：时柱丙戌，男命官杀为子女星，辛杀在月、戌中辛余，子女有而不能承其兵权基业，身后家业星散。病位：病字为辛金七杀（月柱），金主肺与筋骨、又主兵刃旧伤，晚年防肺病与旧伤宿疾。破财之因：戊土财星生杀——因养兵争战与失势耗尽资财，因兵而富、亦因兵而耗。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字（子平）。\n四柱：戊午 辛酉 乙卯 丙戌，乙木日主生酉月、坐卯禄。特格扫描：从官杀未命中（乙坐卯禄强根、午丙食伤成党制杀，有自立与制杀之路）；专旺未命中（酉金当令克木）；燥热近夏秋之交而未成极（午戌火土、酉金有气、水虽缺而金可生水之源在局外，不立燥极）。主线：①格局——酉月辛金七杀透月干为七杀格，丙火伤官透时、午火食神在年，食伤制杀成格；②病——年干戊土正财生杀助杀、丙辛合绊伤官，制杀之力被牵；③救应——乙坐卯禄自强、午戌火局助制。病药链：病＝戊土正财（年干，病型破格，生杀太过，根在午戌）；药＝丙火伤官（时干，以制法制杀，得午戌火根，得力而受丙辛合牵制记半力）；扶抑取向＝喜食伤制杀、比劫助身，忌财杀同旺之运。峰值运三核对：丙寅运①寅为乙木长生得地、用神丙火寅中藏而得生，记满足②运干丙即药神透出呼应，记满足③否决(i)丙运干与原局辛杀相合为合药之疑——丙辛合在本运为运干合杀非合用神干，用神为丙本身，记未命中（合杀反助制杀之局）(ii)寅不冲酉杀根、冲申与局无涉(iii)丙非忌神——满足3项定峰值；丁卯运①卯禄得地②丁食呼应③卯冲酉杀根——卯酉冲所冲为杀根非用神之根（用神根在午戌），记未命中，满足3项并列，先到丙寅为峰值、丁卯称次峰。否决三条核查（丙寅运）：①未命中；②未命中；③未命中。应期：尺度年档；三路——运年触发（丙寅丁卯运制杀登峰）、合冲引动（戊辰运辰冲戌、辰酉合助杀攻禄）、值年（戊己财值年助杀为终局触发同路），终局取合冲引动为主、坐标落戊辰运戊辰己巳年带，值年路并入不另立。残损：无公历生辰与大运原排，年份年龄约数，置信降档。",
 "confidence": 0.55,
}

P["OC-022"] = {
 "prediction_text": "方向：科第无缘、术业成名——命主功名科举屡试不第，终身不入仕途正途；转以命学/术数著述立身，成为一代命师，名望高而官位无，立身之路在著书授业与为人论命。断语依据落点：四柱印星（水）全然不见，科名之凭缺位，此为屡试不第之主断；食伤两巳一丁火势成局、制杀有象而印不化杀，故聪明才学无所附丽于功名，只能泄为著述技艺。逐运（卡面自注大运丙申起，逆行序：丙申、乙未、甲午、癸巳、壬辰、辛卯、庚寅、己丑；年龄约数）：丙申运平偏凶（丙伤、申冲时支寅根，少年多动荡）；乙未运凶于科第（乙比未土财库，考试期逢财土晦火、无印入运，赴试无成）；甲午运凶于科第而艺日进（甲劫午火食伤旺极，屡试不第于此运坐实，然术数著述之技在此运大成）；癸巳运吉（癸水偏印终于透运——印星迟到，不为功名而为著述立名之凭，《命理探原》一系著述成名在此运段）；壬辰运吉（壬印辰库，名望隆盛、授业著书之峰）；辛卯运平（辛杀卯比，晚年名在而身稍劳）；庚寅运平（寅根得地，安享晚名）。应期：科第绝望以乙未、甲午两运为窗（约16–35岁应试期），主坐标甲午运（伤官旺而无印，功名之门在此运关闭）；成名以癸巳运为窗（约36–45岁），主坐标癸印透运之首段，著述问世立名。子女/承继：时柱戊寅，食伤为著述之星在局中旺，门生/著述承其学者众，胜于子嗣承继。病位：病字为酉金七杀与过旺之火，火主心目、金主肺，防心目之疾。破财之因：戊财透而身弱不任大财，一生财在清贵之财（著述授业之入），不聚大富。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：八字（子平）。\n四柱：辛巳 丁酉 乙巳 戊寅，乙木日主生酉月。卡面自注：安命甲午、大运丙申起，已从其注排运（阴年男逆行与月柱丁酉逆排丙申合）。特格扫描：从格未命中（乙有寅根、巳火食伤成党）；专旺未命中；燥热未立极（巳酉金在、寅木有气）。主线：①格局——酉月辛金七杀年透、丁火食神月透，食神制杀之格；②病——印星水全缺：杀无印化、食神无印制衡之正途，功名凭据（印绶文书）缺位为全造第一病；戊财生杀为次病；③救应——寅根自立、巳火食伤泄秀，救在技艺不在功名。病药链：病＝印星缺位与戊土正财（时干，病型破格，生杀，根在巳寅）；药＝巳丁食伤（以制法制杀、泄秀成著述，得两巳一丁成势，得力）；扶抑取向＝喜食伤泄秀成名、运逢印星癸壬为迟到之凭据运（只成著述名望、不成科第）。峰值运三核对：壬辰运①辰为水库印根之地、乙木于辰有余气②运干壬正印透出呼应缺位之凭③否决(i)壬不合丁食神？壬与丁有合（丁壬合）——运干壬合原局丁火食神（药神），记(i)命中之疑；然丁为药而壬合丁为印合食、化木助身，于著述立名反成合局，惟按否决条文面记命中，壬辰取消峰值资格记伪峰；癸巳运①巳非印根、癸无根于巳，①不满足②癸印透呼应记满足③癸不合戊？癸戊合为合财非合用神干，(ii)巳不冲药根(iii)癸非忌神——满足2项（②③），定癸巳为峰值（次高而无否决者优先于伪峰）。否决三条核查（癸巳运）：①运干合绊用神：未命中；②运支冲克用神之根：未命中；③运干透忌神且通根：未命中。应期：尺度年档（问一生立身，先运后年）；三路——运年触发（癸巳运印透）、合冲引动（丙申运申冲寅为早年动荡）、值年（壬癸印值运年），成名取运年触发癸巳运为主坐标，科第窗取乙未甲午两运（食伤旺无印），值年路与触发同源不另立。残损：无公历生辰、出生地，起运岁数按卡注运序推、年龄约数，置信降档。",
 "confidence": 0.58,
}

P["OC-023"] = {
 "prediction_text": "方向：所覆之物为一面圆形铜镜类明器，且不完好——镜有缺破之损。具体断语：①物品（对象）：圆而明亮的金属镜面之物，互卦乾金为圆为金、离火为明为照，两象合指铜镜；体巽木为其柄/框之木质部分或置放之木托。②完好与否（对象同上）：不完好——互卦见兑，兑为毁折、为缺口，变卦恒之上爻由阳变阴，器之上沿/镜边有缺破一处，非完璧。③数量：一件（一面），非成对成组。应期：此为当场射覆、无应期纵深，验物即在启钟当下（日档即时，不适用两段式）。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：梅花易数（体用射覆，托名邵雍、明以降通行本，著录存疑照实标注）。\n卡面卦象：火风鼎变雷风恒。动爻推定：鼎（下巽上离）与恒（下巽上震）仅上爻异，故上爻动；动在上卦，上卦离为用、下卦巽为体。体用：体巽木、用离火，体生用为耗泄之象（物之光泽/完好被泄损，与缺破断相合）。互卦：二三四爻成乾、三四五爻成兑——乾金圆而离明主镜，兑主毁折缺口主不完好；变震为动、恒为久置，主此物为久置之旧器而非新物。爻辞核对：鼎上九『鼎玉铉，大吉』辞主吉，只调节量级（物虽损而非全毁、仍可辨认为完整器形），不翻转兑毁折之缺破定性（合梅花量级与辞义分工）。事实优先：占题只给卦象与射覆场景，无时令外应可对，时令一路无据已注明。梅花自检：主断语三条各落具体项——物品（铜镜）、对象状态（镜边缺破）、数量（一件），达事象级密度。残损：卡面未给起卦方式、动爻明文与占时，动爻系由本变卦比对推得，已注明为推导，置信降档。",
 "confidence": 0.34,
}

P["OC-024"] = {
 "prediction_text": "方向：葬资有着落，不必举债——易者生前已自备身后之资，藏金于窖（地下窖藏之处），其家依来访秀士（邵雍）之指点掘窖得金，金数足以营葬，丧事由此办成。具体断语：①物品/对象：所出者为窖藏之金（金银之属），非向外借贷、非他人赙赠。②人物：得金与主持其事者为易者家人，托付对象为如约来访的年轻秀士。③结果：葬事办成，易者得葬，遗书预言（来访者可托身后事）应验。应期：来访后即时掘藏办丧，日档/旬内之事，无远段纵深，一段终局。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：梅花易数成例形态（《梅花易数》序载邵雍事，托名文本著录照实）。\n输入残损（重点注明）：卡面未给任何卦象、起卦数字、时间或外应数据，无盘可据，不得臆补卦象；本断只据卡面自带信息作有限判断——provenance题名自带『击鼠枕窖金』，其中『窖金』即窖藏之金一线，与context『其家正苦于无资营葬』『遗书预言来访秀士可托身后事』两项事实合参：预言既指人、必同时指资，资之所在以题名窖金为据。承受对象与应验对象同一：断的是易者身后葬资，应验落在易者之家掘藏得金办葬，未回收到访者本人财运。量级守恒：所问为一家丧葬小事，断语只落葬资一层，不放大为访者仕途荣辱。置信因无卦象大幅降档，本断为据题面事实与序题之推断，非据卦推断，已如实标注。",
 "confidence": 0.42,
}

P["OC-025"] = {
 "prediction_text": "方向：应验——预书之事届期坐实。具体断语：①事件（对象）：到期之日，有来访之客坐此椅，椅当即被坐破（椅足/椅面折断），非朽坏自塌、非无人时自损。②应验点：坐破之年月日与椅底预书所记年月日相合，预言以日期对验为据。③人物：坐破者为外来之客/访者，非邵雍家人日常使用所致。应期：以预书所记之年月日为唯一主坐标（卡面未载其具体日期，日期原文无据、不臆报），届期即验，日档定点。此问为单点应验之问、无近远两段，不适用两段式。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：梅花易数成例形态（《梅花易数》序『置椅坐破』，托名文本著录照实）。\n输入残损（重点注明）：卡面未给卦象、预书原文与所记年月日，无盘可据，不臆补日期与卦象。本断据卡面事实作有限判断：context明言邵雍预先在椅底写下某年月日椅子将被坐破的预言、届期验之——此问本身即验谶之问，断语落『届期客坐而破、日期合』为该成例形态之主断；承受对象（椅）与应验对象（椅被客坐破）同一，未转断到坐者人身祸福（量级守恒：小事只断小验，不放大为坐者灾伤）。置信因无卦象与日期原文降档。",
 "confidence": 0.45,
}

P["OC-026"] = {
 "prediction_text": "方向：今年功名不就——两客（昆弟二人）今年应试/求功名皆无成，榜上无名，白跑一趟求名之行。具体断语：①功名线（对象：两客）：三传亥卯未成曲直木局，纯官鬼克己土日干，官势成局而身休囚不任，又父母（文书）火不入三传、朱雀不乘传，文书凭据一路无据——功名压身而文凭不到，主不第。②牵连线：初传未乘青龙有一线喜气（或得荐送/入场之便），中传亥乘螣蛇主考前惊疑虚耗，末传卯乘玄武主结果暗昧落空，终以落第收束。③应期：月档——本年秋冬放榜/定名之期见分晓，主坐标取卯月/卯日一带（末传卯逢值）为落名定期之窗，窗内主坐标为卯支逢值之期；功名终局为不成，不因青龙初传翻案。回乡安居读书、待来年再图为其出路（曲直木局逢明年火运年泄木生身之年方有转机，此为余地非本年断）。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（指南系）。\n盘面（卡面已给）：1643年正月初四己亥日辛未时，月将丑将，甲午旬辰巳空；课式涉害、曲直；三传乙未（青龙）、己亥（螣蛇）、癸卯（玄武）。指代链：日干己土为占者/两客之身，日支亥为对方与事体。课格：三传亥卯未三合木局为曲直格（指南卷二：举直错枉），然三合只为一象、仍回三传分论（卷三下三合章总戒）。类神（仕宦/考试门，指南卷三第十五、十三章）：官鬼为功名本体——木局即官鬼成局克干，官旺身弱（己土正月休囚）；父母为文书试卷——火不入传，按取用层LR-QY-2：文书不入传只降权不作存在否决，然本课亦无四课概要可凭类（盘面未给四课），文书面记无据，与官局克身同向，故终局定不第而非仅降量级。旺衰：正月木旺、未亥卯皆得令气，青龙初传吉将乘未土（己之比）力薄。应期三路（月档，仕宦迁转/榜期月档）：①逢值——末传卯逢值；②逢冲合——亥卯未合局已成、合处在卯；③出空填实——辰巳空不临三传，此路无候选（理由：空亡未落传位）。取逢值卯支为主坐标，合局路与之同支不另立、出空路无据舍。盘面不全守第八节：无天盘全图、四课全列、年命（两客年命未给，行年路无据已注明），细断降档。两段式：本问只问今年功名一程，无远段盘面触发，远段只作余地语、非终局，终局单判为不成。",
 "confidence": 0.55,
}

P["OC-027"] = {
 "prediction_text": "方向：此行不得意——奉诏北上终成空行/虚行：或行至中途差命有变、或到京而不遂所愿，无新迁之喜，所得意处落空。具体分判：①差行线（对象：方替夫本人）：课式无禄、无路为凶格（四上克下、无禄无依之属），末传亥乘青龙而落甲子旬空（刖足之空），喜庆恩宠之将落空主终局无果；官鬼（职分本体）火不入三传，此行无新职可得。②身体线（对象：本人）：官鬼火不入传、白虎不乘传，病源一路无据，本人身体无性命之厄，唯行途劳顿惊扰（中传辰乘太阴主暗昧迟滞）。③老母线（对象：其母，甲子年生）：母以父母土为类——日支未土、中传辰土太阴入传而生辛金日干，母体根基尚在、太阴主暗助，断老母无大碍，唯有小疾/挂念之忧，不至寿关；母年命子水与末传空亥比邻，忧在虚惊非实祸。应期：月档偏近——本旬内（甲子旬）行止难定，出空填实之期（转入甲戌旬、亥支得实，约十日后）为主坐标：届时差命虚实定案，主差行落空/改命不行。近段（旬内）为命下待行而多变，远段（出空后）为不行或行而无功，两段同向收束为不得意。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（指南系）。\n盘面（卡面已给）：1642年冬月初五辛未日甲午时，月将丑将，甲子旬戌亥空；课式无禄、无路；三传癸酉（六合）、戊辰（太阴）、亥（青龙，空）。指代链：日干辛金为本人，日支未为宅/对方，母以父母类神（土）与母年命甲子分看（指南第五节干支年命总纲、男女分推与代占定位）。课格：无禄（卷二凶格：四上克下、无禄无依）、无路同主行无出路；末传空按第三节空亡分位为刖足——事无果而终。类神：仕宦门官鬼火不入传（LR-QY-2：不入传降权，合无禄格与末空同向方定无新迁）；出行门日干辛金冬月泄于水、驿马未在卡面标明（神煞未给，只按已给传课断，不臆补马位）；疾病门虎鬼无据，本人安危只断无大厄、不作细病位断（第八节细断降档）。三传链：酉金（辛之比、癸食）—辰土（印）—亥水（伤、青龙空），递泄至空，势泄而终空。应期三路（月档内近程）：①出空填实——末传亥出旬得实，约十日后甲戌旬；②逢值——酉辰逢值只主行程枝节；③逢冲合——六合初传主合而无成期之实。取①为主坐标（落空者先取出空填实，第七节取期优先序第1位），②③舍（与终局虚行方向不合/只主枝节）。盘面不全：四课全列、天盘、母年命上神未给，母线只据父母入传与年命干支大势，置信降档。",
 "confidence": 0.5,
}

P["OC-028"] = {
 "prediction_text": "方向：得官——入觐考选必得授官，且为成器之迁。具体断语：①得官线（对象：朱西崑）：课式斫轮（卯发用、中戌末巳，印绶俱全、木就金斫成器之格）主迁转成官；初传卯木正官乘玄武、中传戌乘朱雀（文书）、末传巳乘白虎（印火），官印文书三者俱入传，官星得印生扶之链成（卯生巳火、巳戌火土相生），考选得官无疑。②官之量级与性质：官星卯木冬月休囚、乘玄武主暗昧，量级只至中下——断得文职系统之官，约县级正佐/州县一级文官（七品上下），非台阁显要；得官过程带暗线（玄武乘官：有人情打点/暗荐之助，非全凭明考）。③应期：月档——迁期干年支月推，官星卯逢值为主坐标：来春卯月（二月一带）定授/到任，窗口为冬末至春季。近段（觐见考选）顺、远段（定授）成，两段同向，终局单判为得官。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（指南系）。\n盘面（卡面已给）：1630年冬月十四己丑日辛未时，月将寅将，甲申旬午未空；课式重审、斫轮；三传辛卯（玄武）、丙戌（朱雀）、癸巳（白虎）。指代链：日干己土为占者，日支丑为宅/朝廷事体。课格：斫轮两说并存（卷二卯发用中戌末巳印绶俱全、大全卯加申成器），盘面课式名已给、从盘面，其主向同为成器迁转。类神（仕宦门）：官鬼卯木为官职本体入初传，得中末火土印星回生（父母为印绶文书：丙火透中传干、朱雀乘戌主文书音信），官印相生链可述，为一级据可定主线；白虎末传主道路催行（鬼曜逢虎号催官之速至一面，合旺衰：巳火冬月有气、为印非病源，本课问仕宦不作病断）。旺衰：卯木冬月休而得月将寅木之气相助，量级据此压至中下（通则b：降格依据＝官星休囚乘玄武，已写明）。应期三路（月档，仕宦迁转月档）：①逢值——卯逢值（卯月）；②逢冲合——卯戌合在中传，主文书合就、为成期辅据；③出空填实——午未空不临传，此路无候选。取①为主坐标，②同向作辅不另立，③无据舍。盘面不全守第八节：四课、天盘、年命未给，官阶只给量级区间不给确职名，置信降档。",
 "confidence": 0.52,
}

P["OC-029"] = {
 "prediction_text": "方向：一课多占、逐事分判——①子求官线（对象：其子，丑命）：在此地随父求官不成，宜回山东本省取功名——干神归支、传将逆行之象主回乡方成，留此无功。②方所兵动线（对象：山东其家所在方所）：三传纯官鬼成曲直木局、白虎初传乘未、贼符将星克干之势，主山东有兵动之警，冬月间有攻城陷邑之事，家在彼处者须预避。③母寿线（对象：其母，年近九十）：寿止八十九——发用乙未与地盘己字合断为八九之数，母寿关在近岁（本年至明年之间），为诸事中最急者，宜速归侍奉送终。④失盗线（对象：其子之物）：将有失盗，所盗者为郎君（其子）之物；课传回环，贼去而复来——目今先失、三日后贼复来再图，须严防，失物难全追回。⑤客至线（对象：占者处）：顷刻/须臾有客至（三客，内有杨姓者）——此线取象据成例形态，注文无据已在basis注明，只作即时小验。应期各从其门：客至即时（日档内时级）、失盗目今与三日后（日档）、兵动冬月（月档）、子功名回乡后以年档论、母寿近岁（年档内）。全课终局不以一吉凶统之：求官一线在他乡为负、回乡转正；家门一线以母寿与兵动、失盗三凶为重。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（指南系），一课多占走本篇第六节第13条逐事分门。\n盘面（卡面已给）：1642年十月初二己亥日辛未时，月将丑将，甲午旬辰巳空；课式涉害、曲直、回环；三传乙未（白虎）、癸卯（六合）、己亥（天后）；卡面自注其子丑命、母年近九十、家在山东。逐事取象（与本篇第13条成例形态对读，本课即该条所据占验三十五同盘）：(a)子求官——干神归支、传将逆行，断回东省取功名（仕宦门）；(b)兵动——三传纯官鬼（亥卯未曲直木局纯官）、白虎乘初传、贼符将星克干，方所以日支亥分野指山东（兵斗门：干攻支守、虎鬼克支）；(c)母寿——发用合字数断『八九』为成例专法（非父母行年通法），母年命未给，除此专法外不别推寿数，已守其界；(d)失盗——玄武脱气居丑命定所盗属其子、回环格定贼去复来（失物/贼盗门加回环格义：成事吉散事凶、去而复返）；(e)客至——成例只记断语未注取象，依第13条『此事取法查无注文，不立条』，本席只录其断、不臆补取象，置信单独最低。指代链复核（通则f）：母寿断承受对象为其母、子物断承受对象为其子、兵动承受对象为山东方所，三者各归其位未相回收。应期分档依第七节第4条：即时/日档/月档/年档各从其门，已逐事写入prediction。盘面不全：天盘全图、四课全列未给，除成例专法已载者外不臆补神煞与年命上神。",
 "confidence": 0.62,
}

P["OC-030"] = {
 "prediction_text": "方向：两问皆可——①巡按差可复（对象：淮扬巡按差）：课式铸印（戌加巳发用、乘太常）主印绶复铸、有官必迁，钦差占得铸印主复任巡按之象，淮扬巡按差将复设。②吏书缺可照旧（对象：吏书之缺）：中传戌乘六合与末传卯相合（卯戌合），末传卯木官星乘太阴主暗中照旧——吏书缺存续照旧，或由原人/按旧例补任，不至废革。应期：月档——铸印格冲破应在咫尺之格义加以月计，主坐标取巳月（初传巳逢值，四月一带）为复差定案之期，窗口为本年春末至夏初；吏书一线随巡按复设同窗落定。近段（二三月）为议复未定，远段（巳月）为复设坐实，两段以铸印发用为远段触发（巳戌印绶入传），终局单判两问皆成。",
 "basis": "卡面未标注 tradition/system 字段；实际所用体系：大六壬（指南系），章奏·钦差门（本篇第六节第12条）。\n盘面（卡面已给）：1651年二月初十戊子日戊午时，月将亥将（卡面只给月将、无旬空记载，空亡一路无据已注明）；课式重审、铸印；三传癸巳（太常）、丙戌（六合）、辛卯（太阴）。课格：铸印构成戌加巳发用更乘太常（卷二：有官必迁；无官反主官非口舌——本问为官缺复设之问、属有官之问，从迁复一面）；第12条钦差细断明载铸印课占钦差主复任巡按之象（成例胡尹二兄铸印复巡按，与本课同源形态）。类神：官鬼卯木为差缺本体入末传乘太阴（暗昧照旧），父母巳火印绶入初传乘太常（印绶迁拜之将），印官两见、巳生戌、戌合卯，复设之链可述；六合中传主合就。指代链：代占官缺事，日干戊土为占问二人/所问之事，日支子为淮扬事体，断语承受对象为巡按差与吏书缺两事体本身，未回收到占者个人仕途。应期三路（月档）：①逢值——初传巳逢值（巳月）；②逢冲合——卯戌合主合就、为辅；③出空填实——卡面无旬空记载，此路无候选（理由：空亡未给）。取①为主坐标，②同向作辅，③无据舍。盘面不全守第八节：四课、天盘、年命未给，细断只落差缺存废一层，不臆断具体人选姓名。",
 "confidence": 0.6,
}

P["WP-001"] = {
 "prediction_text": "Direction: Yes — a major collective affliction: a worldwide pandemic in 2020–2021. Specific claims: (1) The affliction is an epidemic disease on a global scale — a respiratory/influenza-type pandemic — not merely war or economic crisis; it erupts as the Jupiter–Saturn–Pluto conjunction becomes exact in early 2020 and dominates the 2020–2021 period. (2) Severity is exceptional for the century: mass illness and death, collective confinement/disruption of ordinary life, matching the cyclical index standing at its lowest reading of the 21st century and the past-cluster parallels (1918 above all). Timing: onset/peak window 2020, extending through 2021; main coordinate early 2020 (the exact conjunction).",
 "basis": "Card face carries no tradition/system field; system actually used: Western mundane astrology (classical/modern mundane, per method western-astro chapter: outer-planet cycles and conjunctions as mundane signatures).\nCard-given configuration only (no natal data needed for mundane): Jupiter–Saturn–Pluto conjunction exact early 2020; five outer planets within ~100 degrees; cyclical index at 21st-century low; card itself supplies the historical parallel set 1918/1954/1968/1982 — of these 1918, 1954 (Asian flu era cluster as cited) and 1968 are influenza pandemic years, which fixes the affliction type by the card's own analogy rather than by free association. Saturn–Pluto = mass hardship/mortality signature, Jupiter amplifies scale to worldwide. No full chart/ephemeris data is given on the card, so no house/sign-level detail is asserted; timing is stated at year scale (per timing-scale rule: far-period collective events take year/month units, main coordinate early 2020 from the exact conjunction given on the card).",
 "confidence": 0.68,
}

P["WP-002"] = {
 "prediction_text": "Direction: Barack Obama wins the 2008 US presidential election. Specific claims: (1) The winner is the challenger/change candidate, Obama, defeating John McCain — the Saturn–Uranus opposition exact from Election Day (4 November 2008) breaks for Uranus: the old-guard, older establishment candidate (Saturn) loses to the insurgent 'change' candidate. (2) Obama first secures the Democratic nomination over Hillary Clinton (he already leads and does not collapse), then wins the general election. Timing: decided on Election Day, 4 November 2008 (single-day event scale).",
 "basis": "Card face carries no tradition/system field; system actually used: Western mundane/electional astrology (per method western-astro chapter, modern planets admitted as supplementary signatures and labelled as such).\nCard-given data only: asked 20 May 2008; Obama leads Clinton for the nomination, McCain is presumptive Republican nominee; Saturn–Uranus opposition begins on Election Day, last seen ~45 years earlier (the mid-1960s upheaval cycle). Reading: Saturn signifies age, incumbency, the establishment — embodied by the septuagenarian McCain; Uranus signifies rupture and generational change — embodied by Obama's explicit change candidacy. An opposition culminating exactly on the decision day is read as the change pole prevailing in a close structural contest, not as a status-quo hold. No birth charts or election-day chart are given on the card, so no state-level or margin claims are made; confidence reduced accordingly. This is a single-point question; no near/far two-stage split applies beyond nomination-then-general sequence noted in the prediction.",
 "confidence": 0.6,
}

P["WP-003"] = {
 "prediction_text": "Direction: Barack Obama wins again — he is re-elected in the 2012 US presidential election, defeating Mitt Romney. Specific claims: (1) The incumbent holds the White House; the competitive polling does not translate into a change of president. (2) The Mercury retrograde beginning on Election Day (6 November 2012) marks counting friction — slow/confused tallies and disputed details in places — but does not overturn or steal the result; no 2000-style reversal of the outcome. Timing: decided 6 November 2012, with result clarity within the following days (day scale).",
 "basis": "Card face carries no tradition/system field; system actually used: Western mundane/electional astrology (method western-astro chapter).\nCard-given data only: asked May 2012; incumbent Obama vs presumptive nominee Romney; competitive polls; Mercury retrograde begins on election day itself. Reading: incumbency is the Saturnian continuity pole and no card-given configuration displaces it (unlike a challenger-favouring outer-planet trigger, none is supplied); Mercury retrograde on election day is read, per the tradition this report works in, as a signature of recounts, communication breakdowns and delayed counts — a process affliction, not an outcome reversal, unless other signatures concur, and none are given. No charts are supplied on the card, so margin/state detail is not asserted and confidence is reduced. Single-point event; no two-stage split applies.",
 "confidence": 0.58,
}

P["WP-004"] = {
 "prediction_text": "Direction: Hillary Clinton wins the 2016 US presidential election — this is the forecasting panel's consensus call. Specific claims: (1) The international astrology conference panel in Costa Mesa (October 2016) settles, in its majority, on Clinton as the winner over Donald Trump, in line with the polling lead she holds through October. (2) The panel's call is for a Clinton victory in the 8 November 2016 election (not merely a popular-vote win). Timing: election day, 8 November 2016 (day scale).",
 "basis": "Card face carries no tradition/system field; system actually used: Western mundane/electional astrology as practised by the conference panel described on the card (method western-astro chapter).\nCard-given data only: asked October 2016 at the ISAR Costa Mesa election panel; Clinton vs Trump; most polls favour Clinton. Reading: the question's subject is the panel's forecast; with no charts, transits or panel split supplied on the card, the only card-supported reading of a forecasting panel convened amid a consistent polling lead is that its consensus follows the continuity/favourite signature and names Clinton. No individual dissenting panellist is described on this card (contrast discipline: none imported from other cards). No chart data given, so no margin or electoral-college detail is asserted; confidence reduced for the missing panel-vote breakdown on the card face.",
 "confidence": 0.52,
}

P["WP-005"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election — this is the call of the one panel astrologer singled out on the card. Specific claims: (1) The astrologer who, when 17 Republicans still contested the nomination, picked Trump to become the Republican nominee follows through and names Trump to win the presidency itself. (2) Trump defeats Hillary Clinton on 8 November 2016 despite Clinton leading most polls — an upset victory, against the panel/polling consensus. Timing: election day, 8 November 2016 (day scale).",
 "basis": "Card face carries no tradition/system field; system actually used: Western mundane/electional astrology (method western-astro chapter).\nCard-given data only: October 2016, same Costa Mesa panel context; the card's distinguishing fact is that one panellist had already called Trump's nomination correctly against a 17-candidate field — an established against-consensus track record on this exact subject. Reading: the question is anchored to that astrologer's forecast (the card supplies no other distinguishing subject); a reader who read Trump's rise correctly at the nomination stage, against the field, is read as holding the same line at the general-election stage rather than reverting to the polling favourite. No charts or quotes are given on the card, so the astrologer is not named and no margin detail is asserted; confidence reduced accordingly.",
 "confidence": 0.52,
}

P["WP-006"] = {
 "prediction_text": "Direction: Yes — Britain votes to leave the European Union in the referendum of 23 June 2016. Specific claims: (1) The Leave side wins the referendum despite February 2016 newspaper polls showing 'Stay' ahead with many undecideds — the undecided bloc breaks disproportionately to Leave on the day. (2) The result is a rupture/shock outcome (a sudden severing of a decades-old bond), not a narrow status-quo hold. Timing: referendum day, 23 June 2016 (day scale); the assessment was first published 5 July 2015 and firmed on 22 February 2016, i.e. the Leave call precedes the vote by over a year/at least four months.",
 "basis": "Card face carries no tradition/system field; system actually used: Western mundane astrology (UK national charts tradition; method western-astro chapter).\nCard-given data only: referendum date 23 June 2016 just announced; polls show Stay ahead with vast 'not sure' numbers; charts available are the UK 1066/1801/1922 charts; on referendum day Uranus and Ceres conjunct at 23 degrees Aries. Reading: Uranus is the rupture/separation signature and its conjunction exact on polling day, in Aries (assertion of separate identity), is read as the break prevailing over the status quo; Ceres adds the severing-from-the-nourishing-body motif. Polls are treated as the weaker signal against the day-configuration, per the mundane tradition this assessment works in — and the 'not sure' mass is exactly the population a late Uranian break moves. Full UK chart data and transits are not reproduced on the card, so no vote percentage is asserted; confidence reduced for that gap. Single-point event; no two-stage split applies.",
 "confidence": 0.5,
}

P["WP-007"] = {
 "prediction_text": "Direction: Donald Trump wins the 2016 US presidential election, and what decides it is Hillary Clinton's email controversy. Specific claims: (1) Winner: Trump, defeating Clinton on 8 November 2016, against her August polling lead. (2) Deciding factor: the Clinton email affair (with the Clinton Foundation questions attached) — renewed email revelations late in the campaign corrode Clinton's trustworthiness among late-deciding voters and tip the election; the race is decided by scandal-driven defection/distrust, not by policy or turnout machinery. Timing: the decisive turn falls in the final stretch before 8 November 2016 (weeks scale), result on election day.",
 "basis": "Card face carries no tradition/system field; system actually used: Tarot (Rider-Waite-Smith, Waite meanings per method western-tarot chapter) as used by the reader described on the card.\nInput deficiency (stated plainly): the card records that a Manhattan (Union Square Park) tarot reader was consulted and drew cards in August 2016, but the drawn cards, spread and positions are NOT given on the card — no card-by-card Waite reading can be performed, and none is fabricated here. The prediction is therefore made at reduced confidence from the card's own framing facts: the question explicitly asks 'what will decide it', and the only deciding-factor material the card supplies is that Clinton's email controversy and the Clinton Foundation were already live public controversies at the time of the reading; a reading whose decisive card-complex centred on hidden/revealed communications (the tarot complex of concealment-and-exposure) resolves, on the card's facts, to the email affair deciding the race against Clinton. Because the actual draw is missing, no specific card names are asserted. Timing scale: weeks-to-election-day, per the question's own scale.",
 "confidence": 0.42,
}

for cid, rec in P.items():
    rec_out = {
        "case_id": cid,
        "prediction_text": rec["prediction_text"],
        "basis": rec["basis"],
        "confidence": rec["confidence"],
        "trigger": TRIG,
    }
    with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec_out, f, ensure_ascii=False, indent=1)

print("written", len(P))
