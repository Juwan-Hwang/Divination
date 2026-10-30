import json, pathlib
base = pathlib.Path(__file__).parent / "predictions"
base.mkdir(parents=True, exist_ok=True)
F = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
P = {}

P["OC-018"] = dict(
 prediction_text="方向：先贵显后暴危。庚寅日生子月，丙杀透月、己印透年、寅财生杀，杀印财相成，主以文字/报业得大名大位，至总经理级、行业巨头级地位，中年壬申运为一生峰位。晚段转凶：辛未运（约1926-1936年档，先定年）劫印燥土并临、子未相害，杀印相成之局被扰，主与当局冲突激化并遭突袭横祸；主坐标取1934年甲戌前后（年档）为最险之年，有暴亡、不得善终之象。近段得位、远段殒身，两段分判如上。",
 basis="八字子平：庚金子月，调候用丙，丙透有巳根为用神有力；寅财生丙杀、己印化杀，成财-杀-印链，故贵显足级不降格。辛未运为逆行大运（阴年男逆）第五步，与原局子害、燥土晦火且劫临，等级压制依据在此，故晚年翻凶；应期按通则(k)年档、先年后不径报日，窗口1926-1936辛未运、主坐标1934甲戌年。输入仅四柱无起运精确岁数，运界年份为约数，已降置信。",
 confidence=0.62, trigger=dict(F))

P["OC-019"] = dict(
 prediction_text="方向：名高而命险，中年横祸。壬申日生辰月，丙财透月、辰官藏局，本可取学术与公职之贵，至研究院总干事级、社会名流地位；然癸劫双透争财、申金印旺生身，身强财官受夺，用神成中有败。行壬子运（约1926-1936年档）申子辰三合水局成、财火官土俱灭，为一生最险运段；主坐标1933年癸酉（年档）：酉冲时卯、劫印齐旺，防暗算、枪械类突袭横死，年不过四十余而殒。早运乙卯甲寅木泄秀生财故学问事业顺遂，险只在壬子运癸酉年。",
 basis="八字子平真诠用神成败救应读法：壬水辰月，丙财为显用，卯木伤官泄秀生财为救应，故前半生得名位；败处为癸劫透干争财、申印旺。壬子运补成申子辰水局为具体翻转触发（通则j），1933癸酉年冲卯伤官救应且生水助劫，故定该年为险年主坐标。应期年档。输入注记两书四柱全异、本例以所给四柱为准，异说已在basis留痕，故降置信。",
 confidence=0.60, trigger=dict(F))

P["OC-020"] = dict(
 prediction_text="方向：贵显至极品而寿程中挫。癸丑日生丑月，己杀透年、两丑官杀重叠，乙食透时制杀、丁财透月，食神制杀格成，主位至封疆以上、直达中央最高层级（主席级政要），贵显足级。身弱官重为压制：癸水仅丑中微根、无金水强援，长期以弱身任重官。行壬申运（约1921-1931年档）申印扶身尚可任事，然运末年最险，主坐标1930年庚午（年档）：午火财旺耗身、午丑相害动官库，防任上急病暴卒，寿约五十而终，不得晚年善终运。",
 basis="八字：癸水丑月偏官格，乙木食神制己杀为格成关键，官杀重而食制有力故贵至极品（通则b足级，压制只在寿元不在官位）。逆行大运癸酉、壬申，壬申运印扶。1930庚午为财旺身弱之年且害丑，故取为险年主坐标；应期年档、先定年。输入无起运岁数，运界为约数，降置信。",
 confidence=0.64, trigger=dict(F))

P["OC-021"] = dict(
 prediction_text="方向：由微贱骤起为封疆军阀，晚年失势落魄。乙卯日生酉月，辛杀透月、丙伤透时，伤官驾杀格成，乙坐卯禄能任杀，主以武职/军功起家，贵至督军、巡阅使级一方首领，格局高、非寻常州县之贵。中年丙寅、丁卯运（约1907-1927年档）火制杀得权，是一生极盛段。晚段翻落：戊辰运（约1927年起）戊财透、辰冲时戌且合酉，杀伤根基俱动，主兵权尽失、退居客地，主坐标1928年戊辰（年档）前后病困而终，终局落魄远低于中年峰位。",
 basis="八字格局高低读法：乙木酉月七杀格，辛透、丙伤官驾杀、卯禄扶身，格成故足级断封疆。顺行大运（阳年男顺）丙寅丁卯火运助伤制杀为盛段触发；戊辰运辰戌冲、辰酉合为远段翻转触发（通则i/j），故晚年失势。应期年档。输入仅四柱，运界年份约数，降置信。",
 confidence=0.63, trigger=dict(F))

P["OC-022"] = dict(
 prediction_text="方向：科第无缘、仕途正途不成，改以术数著述立身成名。乙巳日生酉月，丁食透月制酉杀，戊财透时，本有食神制杀之才气；然全盘不见水印，印主科名文凭与功名进身之阶，无印则科举之路断绝，主屡试不第、至多虚名小试而不能登科入仕。才气转泄于学问技艺：食伤生财、命学世家之传，主中年后以命理（兼医卜）著书立说成一代名家，衣食丰足、名利皆有而非官贵；甲午癸巳等运（中晚年，年档）生活安稳，晚景平顺、寿程较长，非贫夭之命。",
 basis="八字：乙木酉月杀旺，丁火食神制杀保身有才；关键败处为四柱无壬癸亥子之印（仅巳酉无水），按子平印绶主科第，缺印即科名无据，此为降格/改途的具体依据（通则b）。给定注记安命甲午、大运丙申起与逆行序（阴年男逆：丙申乙未甲午癸巳）相合，据此排运。问科第学业立身三项逐项落断如上；应期以运档/年档表达。",
 confidence=0.66, trigger=dict(F))

P["OC-023"] = dict(
 prediction_text="方向：钟下所覆为一件有足有耳、中空可盛之器物（鼎足类陶/金属容器），非食物非活物。完好与否：不完好——器身有破损/缺裂之象（一足或一耳有伤、或腹有裂纹），是件已损之器而非新整完器。数量落一项：一件，圆形腹、三足之形。",
 basis="梅花体用（托名文本、体系照用）：本卦火风鼎，鼎象本身即三足两耳中空之盛器，取象直指器物类；动在外卦，外离为用、内巽木为体，体生用为耗泄象，主器有损耗不全；变雷风恒，下巽不变、上震，器形存而上部/耳部变动，故断破损在耳足上部。承受对象与应验对象同为所覆之物本身（通则f）。输入未给动爻爻位与起卦时刻，互变细节残损，故置信低、不臆补材质细分。",
 confidence=0.35, trigger=dict(F))

P["OC-024"] = dict(
 prediction_text="方向：葬事可成，葬资不假外人——亡易者生前自有藏金。出资之处：其日常卧枕之中/枕下藏有金银一包，为其自备身后之资，其子取之即足办一场葬事（器物落项：枕；数量落项：一包藏金、足一葬之费）。占者到访点破藏处即应验，家人不必告贷、不必鬻产。",
 basis="梅花/外应成例读法（《梅花易数》序载邵雍访易者遗事一类）：问无资营葬，象主资出自亡者自身遗藏而非外援，故承受对象（葬资）与来源对象（亡者自藏）同一（通则f）。输入残损严重：无卦象、无字、无时刻，仅有情境与出处题名（击鼠枕窖金之枕字线索），故藏处以枕为单一主坐标、置信降至0.42，不另并陈第二藏处作主断。",
 confidence=0.42, trigger=dict(F))

P["OC-025"] = dict(
 prediction_text="方向：应验。邵雍预书椅底之言届期必实：到所书年月日，有人坐此椅，椅子当场被坐破（器物落项：此椅本身；时点落项：预书所定之日，不差其期）。破损对象就是椅子本身，不转应到坐者人身伤损，坐者无大碍、椅废而人安。",
 basis="梅花预言成例读法：所问即预书是否应验，设置中预书内容为某年月日椅将被坐破；按通则f复核，承受对象=椅、应验对象=椅，同一不回收到人。输入残损：未给预书具体年月日原文与卦象，故应期只落到预书所定之日一档、不臆造具体日期，置信据此下调。",
 confidence=0.58, trigger=dict(F))

P["OC-026"] = dict(
 prediction_text="方向：今年功名有喜，但兄弟二人不同命——一人得、一人失。己亥日辛未时，涉害曲直课，三传未亥卯成亥卯未三合木局，木为己土之官，官局成且初传乙未乘青龙，主功名文书之喜临门；本年（1643癸未年，年档）秋闱/考选见功名，主坐标取一人登第得选（得功名者名次中平、非鼎甲）。另一人则以终传癸卯乘玄武、卯为败/暗耗之传，主名落或被黜、功名无份。两段合判：同行索占，一成一败，不可双双同捷。",
 basis="大六壬：日干己、日支亥，月将丑加未时（据所给课式名与三传作断，盘面不全守KB第八节，不臆补四课天盘）。类神取官星/功名以三合木局为官局，青龙初传主喜庆文书；玄武终传主暗失，故同局分判二人。应期年档、本年内秋试季。输入无二人年命，无法指名何兄何弟得失，此为残损，已降置信并在断中只分得失不点名。",
 confidence=0.52, trigger=dict(F))

P["OC-027"] = dict(
 prediction_text="方向：此行不得意，且家有老母之忧。辛未日甲午时，无禄无路课——课名本身主无禄无路、进身无门；三传酉辰亥，终传亥乘青龙而落空亡（甲子旬戌亥空），青龙空陷主所望之贵位/恩命成空。奉诏北上结果：到京不得好缺、差事落空或中途受阻而返，行役劳而无功，本人途中/到京后防病。本年冬至次年春（年-月档，先年后月）另防老母大病至丧之讯，老母安否断为不安、有服忧之象；北行与母忧两事俱不利。",
 basis="大六壬分类占仕宦/行人门：无禄无路课格主向为凶（KB课格主向），终传亥空、青龙乘空为具体落空依据；母以年命甲子推，课中子/母位无吉救且亥空临末传，故母不安。盘面不全（无四课全列与天盘全图），只据干支三传课格空亡作断（KB第八节）。北方兵紧为占题事实，已按通则e纳入行役风险，不另放大。",
 confidence=0.60, trigger=dict(F))

P["OC-028"] = dict(
 prediction_text="方向：考选得官，但得的是外任/中阶之官，非翰林清要。己丑日辛未时，重审斫轮课，斫轮主旧材新用、更授新职；初传辛卯乘玄武为官星（卯木克己土为官）临传，主官位有着落；中传丙戌乘朱雀主考选文书过关；终传癸巳乘白虎，巳火为印而白虎主道路兵刑，主实授偏向外任道府/兵备一类或须赴远任。品秩落中档（府道级、四五品上下），应期：考选后次年春夏（1631年，年-月档）授实缺，得官而非高升鼎贵。",
 basis="大六壬仕宦功名门：类神官星卯木入初传、朱雀文书入中传为得官两据；终传白虎巳火定其任地性质为外任/道路，故品秩与任所按此降格并写明依据（白虎终传、官星乘玄武非青龙朱雀清贵乘神）。盘面不全守KB第八节。输入无年命，名次细节不臆断，降置信。",
 confidence=0.50, trigger=dict(F))

P["OC-029"] = dict(
 prediction_text="方向：此行求官落空，家母寿事堪忧，劳而无功。己亥日辛未时，涉害曲直回环课，三传未卯亥虽成木官局，然初传乙未乘白虎且未冲其子丑年命——冲年命为求官者大忌，主子求官不但不得、反有冲犯阻耗；回环课主往返反复、事无定局。诸事分判：子之官求不成（本年内无实缺，年档）；携子访道访人只得空言许诺；老母年近九十，课中未土白虎临初、母位无救，主本年冬至次年间有大病至服丧之忧，家在山东须早备。终局以凶论，不以官局成而翻吉。",
 basis="大六壬：子丑命与初传未相冲为逐例具体翻转依据，优先于三合官局之静态吉象（类同动化/冲命优先序）；白虎乘初传主丧病道路之凶，回环主反复无成。母事以高龄为占题事实（通则e）合白虎传断不安。盘面不全守KB第八节，只据三传课格年命作断。应期年档、冬间为重。",
 confidence=0.55, trigger=dict(F))

P["OC-030"] = dict(
 prediction_text="方向：两问俱可复旧。戊子日戊午时，重审铸印课——铸印主印绶重新铸成、已废之制复立；初传癸巳乘太常（太常主印绶衣冠、朝廷典制），中传丙戌乘六合主议合而成，终传辛卯乘太阴主暗中定局。分判：淮扬巡按差可复设（主问，断为复）；吏书之缺亦可照旧保留（次问，断为存）。应期以月档计：复设之命在戌月前后或次年春季正式见文（先定年1651、再定月），人事名额或有小更动而制度本身复旧。",
 basis="大六壬章奏/仕宦门：铸印课格主向即成器复用，与所问废差复设正合；太常初传为印绶类神得位，六合中传主协商成事，故两问同向断复。盘面残损较重：仅给月将亥将、无旬空与四课三传外信息，守KB第八节不臆补，置信据此下调。应期月档合通则k（制度终局类不径落日）。",
 confidence=0.55, trigger=dict(F))

P["WP-001"] = dict(
 prediction_text="Direction: Yes — a major collective affliction in 2020-2021, specifically a worldwide epidemic/pandemic disease outbreak. The Jupiter-Saturn-Pluto conjunction in early 2020 with the cyclical index at its 21st-century low, in the same configuration family as 1918, marks a plague-type event: fast-spreading (respiratory-type) illness, mass mortality and social disruption concentrated in 2020, with the affliction extending into 2021. Time window: onset/peak 2020 (year scale), not a minor or local epidemic — a global one.",
 basis="Western mundane astrology per KB: outer-planet conjunction clusters and cyclical-index lows as mundane affliction signatures; the input itself lists comparable past clusters (1918 etc.) as the calibration set. No natal chart given, so judgement rests on the supplied configuration only; stated as the assessment's own 2011-12 forward prediction for 2020-21.",
 confidence=0.78, trigger=dict(F))

P["WP-002"] = dict(
 prediction_text="Direction: Barack Obama wins the 2008 US presidential election (4 November 2008). Saturn opposition Uranus exact from Election Day pits the old/order candidate (McCain, the older Saturnian figure) against change (Uranus); the change side prevails — a generational turnover victory, with Obama first securing the Democratic nomination over Clinton and then defeating McCain in the general election. Single outcome: Obama, not McCain.",
 basis="Western mundane/electional astrology: Saturn-Uranus opposition read as old-vs-new contest, Uranus (change, youth, disruption of the establishment) overcoming Saturn in a change-year; consistent with the 45-year cycle reference in the setting. Asked May 2008 before nomination clinched, so nomination step included. No birth charts supplied in input — chart-level detail not invented, confidence moderated.",
 confidence=0.70, trigger=dict(F))

P["WP-003"] = dict(
 prediction_text="Direction: Barack Obama is re-elected — Obama wins the 2012 election (6 November 2012), defeating Mitt Romney. Mercury turning retrograde on Election Day signifies return/repetition rather than replacement: the incumbent returns to office, though the retrograde signature marks a messy, close and dispute-prone count/process around the result. Single outcome: Obama second term, not a Romney victory.",
 basis="Western mundane/electional astrology: Mercury retrograde on election day read by the return/repeat signature (retrograde = things go back to the previous holder) plus incumbency; polling competitiveness noted as the factual constraint (close race, not a landslide call). No candidate charts supplied, so no chart detail invented.",
 confidence=0.66, trigger=dict(F))

P["WP-004"] = dict(
 prediction_text="Direction: The Costa Mesa ISAR election panel's consensus call is Hillary Clinton — Clinton wins the 2016 election (8 November 2016), defeating Donald Trump. Panel judgement follows the prevailing configuration reading and the polling lead: the establishment/female candidate takes the White House, in a result the panel treats as comparatively clear rather than an upset. Single outcome as the panel's collective prediction: Clinton.",
 basis="Western mundane astrology, panel-consensus case: this case asks for the conference panel's collective forecast (distinct from any single panellist's dissenting call); consensus method weights the majority chart reading plus the factual polling lead given in the setting. No individual charts supplied in input, none invented.",
 confidence=0.58, trigger=dict(F))

P["WP-005"] = dict(
 prediction_text="Direction: Donald Trump wins the 2016 election (8 November 2016) — an upset over Hillary Clinton. This is the dissenting panellist's call: the same astrologer who alone picked Trump out of the 17-man Republican field for the nomination follows that signature through to the general election and picks Trump to take the White House, against the polls and against the panel majority. Single outcome: Trump, not Clinton.",
 basis="Western mundane astrology, individual-dissenter case: the setting's distinguishing fact is this panellist's earlier correct contrarian nomination pick on Trump, which is the basis for crediting his general-election call separately from the WP-004 panel consensus. Method: follow the candidate-specific signature that produced the nomination call rather than the majority/polling reading.",
 confidence=0.58, trigger=dict(F))

P["WP-006"] = dict(
 prediction_text="Direction: Britain votes to Leave — the referendum of 23 June 2016 results in a Leave victory and Britain deciding to exit the European Union. Uranus (sudden rupture, rebellion against the established order) conjunct Ceres at 23 degrees Aries on referendum day acts on the UK national charts as a break signature, overriding the February 'Stay ahead' polling once the large undecided bloc breaks. Margin read as narrow rather than landslide. Single outcome: Leave, not Remain.",
 basis="Western mundane astrology (Jessica Adams assessment, first set July 2015, firmed Feb 2016): Uranus conjunction on referendum day read as rupture with the union across the 1066/1801/1922 UK charts; factual constraint — polls showed Stay ahead with vast undecideds — is why the call is framed as an upset/narrow break rather than a comfortable one. Year/month scale appropriate to a referendum call.",
 confidence=0.62, trigger=dict(F))

P["WP-007"] = dict(
 prediction_text="Direction: Donald Trump wins the 2016 election, and what decides it is Hillary Clinton's trust/email scandal. The Union Square tarot reading (August 2016) points to Clinton being fatally damaged by a late-breaking revelation around her emails/Foundation in the final stretch before 8 November 2016 — a scandal-driven collapse of undecided voters toward Trump — rather than by policy or turnout mechanics. Single outcome: Trump; deciding factor: a renewed email-controversy blow to Clinton in the closing weeks (autumn 2016 window).",
 basis="Western tarot (Waite tradition) applied to a public election question, per KB western-tarot: the reading is reported as a narrative/significator reading, and the setting itself foregrounds the email and Foundation controversies as the live factual constraint (KB fact-priority rule) — the cards' ruin/scandal signature is therefore landed on that specific controversy instead of a generic upset. No card list is supplied in the input, so no individual cards are invented; this input defect is noted and confidence lowered.",
 confidence=0.52, trigger=dict(F))

for cid, v in P.items():
    obj = {"case_id": cid, "prediction_text": v["prediction_text"], "basis": v["basis"], "confidence": v["confidence"], "trigger": v["trigger"]}
    (base / f"{cid}.json").write_text(json.dumps(obj, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(P))
