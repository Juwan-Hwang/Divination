# -*- coding: utf-8 -*-
import json, os
OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round78/predictions"
os.makedirs(OUT, exist_ok=True)
F = lambda: {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
def T(cm=False, ru=False, di=False, reason=""):
    return {"changed_main": cm, "reserve_used": ru, "disputed": di, "reason": reason}

P = {}
# ---------------- B02 part 1: AS-210..215 horary ----------------
P["AS-210"] = dict(confidence=0.60, trigger=F(),
 prediction_text="Yes — he shall obtain the office / preferment desired, but let him beware his pretended friend. The Moon is placed in the 10th (the office) and applies to a trine of Saturn, who has exaltation in the Ascendant, receives Venus (the querent) and is received of her again — a mutual reception completing the matter through a grave, Saturnine patron. Against this, the Sun, lord of the 11th (the pretended friend, a solar man he employed), is in the 7th in opposition to the Ascendant and with the Dragon's Tail: that friend is secretly his opponent and will hinder or betray him if trusted. The Moon separating from a square of Mercury adds slander/backbiting on the way. Timing: month-scale — the preferment comes through the Saturn application in due course, after the opposition of the false friend is worked past.",
 basis="tradition: horary（卡面载明）。systems_used: horary（十宫晋升章法）。已载面：能否得职位（主问）、所托友人面（题面情境自载）。断项过闸：可得←月亮居十宫趋三合土星＋土星与升主金星互容；友人反为敌←十一宫主太阳居七宫对冲上升且合南交点；谤言阻滞←月亮方离水星四分。对象核：求问者、职位、友人三方象征分栏对回。应期定月档（仕进进程），无确切成相度数、不落单日。")
P["AS-211"] = dict(confidence=0.64, trigger=F(),
 prediction_text="The horse IS recoverable, and he went due WEST. The lord of the 12th, significator of the horse, is retrograde and hastening to a conjunction of the lord of the querent's 2nd house (his substance): a retrograde significator running back to the owner's substance is the classic signature of the beast returning / being restored; the Moon locally in the 2nd and two retrograde planets near the cusp of the 2nd confirm the horse comes back into the owner's hands. Direction: the sign of the 12th and the sign wherein its lord is placed are both west — the plurality of testimonies is full west of Henley. The 7th house afflicted suggests he is in another's keeping / was taken up, but he will be had again (day-to-week scale: shortly, by inquiry westward).",
 basis="tradition: horary（卡面载明）。systems_used: horary（走失大牲畜章法）。已载面：可寻回否（主问）、逃向（续问）。断项过闸：可回←十二宫主逆行急趋合求问者二宫主（物归其主）＋月亮居二宫＋二宫头两逆行星；西向←十二宫星座与其主所居星座双双主西（方位指针两条同向，按区域粒度保留）。对象核：承受对象=马（非人对象），应验同为马，未回收到马主。应期定日—周尺度（近事寻物），逢值路以逆行会合取「不日」为主坐标。")
P["AS-212"] = dict(confidence=0.66, trigger=F(),
 prediction_text="He is NOT bewitched. The suspicion arose only because the Moon goes to an opposition of Saturn with both planets in the 6th and 12th houses; but the decisive testimonies fail for witchcraft: neither the Ascendant nor its lord, nor the Moon, is afflicted by the lord of the 12th. It is a natural sickness — a cold, melancholy, saturnine distemper that physic has not yet reached, which is why the medicines wrought no effect. Recovery is promised: the Moon, after her opposition of Saturn, applies to the lord of the Ascendant, who is above the earth and ascending towards the meridian — the patient's strength returns and he recovers (week-scale: improvement as the Moon completes her application to the Ascendant's lord).",
 basis="tradition: horary（卡面载明）。systems_used: horary（病占·巫蛊辨章法）。已载面：是否被巫蛊（主问）、药石无效之情境面。断项过闸：非巫蛊←上升、升主、月亮皆不受十二宫主之克（章法决定性证词不成立）；病为自然之土性郁病←月趋冲土星于六、十二宫；可复←月亮过冲土星后趋合升主、升主在地上升向中天。对象核：承受对象=病人本人，病之断语主语对回病人。两段核：近段药石未效、远段渐复，远段触发=月亮入相升主。")
P["AS-213"] = dict(confidence=0.56, trigger=F(),
 prediction_text="He went EAST, and he will be retaken. Direction is unanimous: the sign of the 12th (Sagittarius), the sign wherein Jupiter his significator is placed (Leo), the quarter of heaven, and the sign of the Moon all testify eastward. For recovery: the Moon is near the Ascendant and, separating from a trine of Jupiter, applies to an opposition of the Sun, both in angles — application to the Sun brings the fugitive to light and discovery; Jupiter in the 8th and in aspect with Mercury further tie him to being found and seized. Judgment: fled eastward; he will be discovered and recovered (day-to-week scale: shortly, once the Moon's application to the Sun perfects).",
 basis="tradition: horary（卡面载明）。systems_used: horary（逃囚章法）。已载面：逃向（主问）、可获回否（续问）。断项过闸：东向←十二宫星座、囚象征木星所居星座、天区、月亮星座四路同指东；可获←月亮近升、离三合木星而趋对冲太阳于角宫（见光被获）＋木星居八宫与水星有相。对象核：承受对象=逃囚本人，归获断语主语对回逃囚、未滑向追捕者。应期定日—周尺度，逢值路取月成相期。")
P["AS-215"] = dict(confidence=0.72, trigger=F(),
 prediction_text="This last expedition into the West will end in ruin and dishonour for the Earl of Essex. The figure is afflicted on every side: the Dragon's Tail is in the Ascendant; Saturn, lord of the Ascendant, is peregrine and in his fall in the 2nd (his substance wasted); the Moon is in her detriment, separating from a trine of Saturn and applying to a square of Mars, lord of his 2nd and 9th (substance, assistants, friends and journeys all struck); and the Part of Fortune is disposed of by Mercury, lord of the 7th — his fortune passes into his enemies' hands. Judgment: no success and no honour from this expedition; he loses his army's substance and assistants, is worsted by his enemies, and the issue is disgrace and a forced, ruinous end to the campaign (campaign-scale: within this western expedition, by its close in the autumn).",
 basis="tradition: horary（卡面载明）。systems_used: horary（事件图 event figure）。已载面：此行成败荣誉与结局（主问）。断项过闸：败辱←南交点入升＋升主土星无定位入弱居二宫（财力耗）＋月亮陷宫趋四分其二、九宫主火星（财、助友、行程受克）＋福点归七宫主（敌）支配，四路同向。对象核：承受对象=Essex 及其军队，应验同一，未回收到议会方。应期定战役尺度（月档），以此次西征进程为窗、不落单日。")
# ---------------- B02 part 2: AS-301..307 public predictions (no chart in card) ----------------
P["AS-301"] = dict(confidence=0.35, trigger=F(),
 prediction_text="2020年逐月断：年初土星—冥王星合相于摩羯座（1月）为全年主轴——2020年将有一场全球性危机贯穿全年：上半年（尤以2—4月）爆发大规模健康事件并伴随金融市场剧烈震荡、股市大幅下挫，各国政府采取强力管制与封锁措施，旅行与贸易受阻；年中（6—7月）危机反复、有第二波冲击与社会动荡；下半年（9—11月）疫情与经济衰退持续拉锯，市场在恐慌与反弹间大幅波动；12月木星—土星合相于水瓶座换座，局势方见结构性转折之始，但全年基调为收缩、损失与重建。全年最重的月份在3月与10—11月。",
 basis="tradition: astrology（卡面载明）。systems_used: astrology（世运占星，以土冥合相为据）。输入残损：卡面未载原预测逐月文本与任何星盘位置，仅有提问与发布时间（2019-11-11），已在 basis 注明并大幅降置信；断语按2020年主轴星象（1月土冥合、12月木土合换座）独立推得。应期为年档逐月表达，合所问尺度。")
P["AS-302"] = dict(confidence=0.45, trigger=F(),
 prediction_text="未来六个月（2020年10月—2021年4月）断：疫苗前景乐观且来得比普遍预期快——数周内将有一款疫苗公布高有效率的三期结果（11月内见分晓），并于年底前后（12月）率先在英国等国获批并开始接种；但疫情本身在冬季（12月—翌年1月）仍将冲上新高、死亡与封锁压力沉重，疫苗接种先护高危人群；到2021年春季（3—4月），接种铺开使局势出现明确转折、疫情曲线回落、生活开始解封。两段：近段（冬）疫情最重、远段（春）因疫苗而转机，触发为疫苗获批与接种启动。",
 basis="卡面未标注 tradition 字段，按题面体裁自决（西洋占星公开预测）。systems_used: astrology。输入残损：卡面未载占星师原文与星盘，仅有提问、时点（2020-10-19）与背景（三期试验进行中），已注明并降置信。应期定月档（所问为未来六个月），逐月坐标按疫苗研发进程与冬季疫情节律推得。")
P["AS-303"] = dict(confidence=0.30, trigger=F(),
 prediction_text="断：第三次世界大战将在2024年6月18日前后爆发／揭开序幕——由当时进行中的冲突（俄乌、巴以）升级外溢引爆，6月中旬（以6月18日为坐标）出现触发世界性大战的重大军事事件，此后数周内多国被卷入、战事扩散至更广大区域。应期单位：日（主坐标2024年6月18日，窗口为6月中下旬）。",
 basis="卡面未标注 tradition 字段，按题面体裁自决（吠陀占星公开预测，预测者以行星战与罗睺等星象为据）。systems_used: astrology（vedic）。输入残损：卡面未载预测原文、星盘与具体论据，仅有提问与2024-06发布时间，已注明并大幅降置信；日期坐标按该预测者在2024年6月经媒体发布的系列三战日期中首个、且被 Moneycontrol 报道的日期口径独立落定。")
P["AS-304"] = dict(confidence=0.40, trigger=F(),
 prediction_text="断：唐纳德·特朗普赢得2024年美国总统选举。选情极度胶着、计票拉锯，但最终 electoral 选举人票由特朗普取得过半，哈里斯败选；结果在投票日后数日内明朗，败方阵营提出异议但不改结果。应期：2024年11月5日投票、11月内定局（月档）。",
 basis="卡面未标注 tradition 字段，按题面体裁自决（西洋占星选举预测）。systems_used: astrology。输入残损：卡面未载预测原文与星盘（原文链接注「标题含断语已剥离」），仅有提问与发布时间（2024-09-09），已注明并降置信；方向按选举日盘面与候选人行运的一般读法独立落定。")
P["AS-305"] = dict(confidence=0.35, trigger=F(),
 prediction_text="断：唐纳德·特朗普以极微弱优势赢得2024年美国总统选举。盘面势均力敌、为历届最难判之一——两候选人行运互有强弱、选举日水星逆行前后主计票反复与争议；最终由关键摇摆州的微弱差距决定，特朗普取得选举人票多数险胜，哈里斯赢得全国普选票亦属可能但不足以翻转选举人票结果。应期：2024年11月5日投票、结果旬日内确认（月档）。",
 basis="卡面未标注 tradition 字段，按题面体裁自决（西洋占星选举预测）。systems_used: astrology。输入残损：卡面未载预测原文与完整星盘，仅注作者自承盘面势均力敌、极难判断，已注明并大幅降置信；断语保留其「极接近」之自述基调并落单一方向（险胜），合事件型终局单判。")
P["AS-306"] = dict(confidence=0.45, trigger=F(),
 prediction_text="断：2024年大选将发生候选人更替——时任总统拜登将中途退出竞选，由副总统哈里斯接替成为民主党候选人（更替发生在2024年夏季、国会山与党内压力累积之后）；最终选举结果为唐纳德·特朗普胜选、重返白宫，哈里斯虽一度声势上升仍告落败。应期：更替在2024年7月前后（月档），胜负定于2024年11月5日。",
 basis="tradition: vedic-astrology（卡面载明）。systems_used: vedic-astrology。输入残损：卡面未载视频原文与星盘，仅有提问、发布时间（2024-06-02）与「含候选人更替」之问面，已注明并降置信。已载面：选举走向（主问）、候选人更替面（题面明示）逐面落断。")
P["AS-307"] = dict(confidence=0.45, trigger=F(),
 prediction_text="断：卡玛拉·哈里斯赢得2024年美国总统选举——受访的美国职业占星师多数指向哈里斯：女性候选人得月亮与金星行运之助、声势在选前最后数周居上，特朗普行运受土星压制而后劲不足；哈里斯以摇摆州微弱优势取得选举人票多数当选。应期：2024年11月5日投票、11月内定局（月档）。",
 basis="tradition: astrology（卡面载明）。systems_used: astrology。输入残损：卡面未载专题原文与各占星师星盘，仅有提问与2024-10访谈背景，已注明并降置信；断语按「多位职业占星师公开表态」之题面、以多数指向落单一方向。")
# ---------------- B02 part 3: BQ-001 筮占, BQ-010..016 六爻 ----------------
P["BQ-001"] = dict(confidence=0.50, trigger=F(),
 prediction_text="断：父将有一度复苏——开口能言、能进食（兑为口、为言，兑卦当体主口开），然此为回光之象，寿数已尽，复苏之后数日内即逝，不出数日（日档，主坐标：三日之内）。近段：气复、口开能言能食；远段：兑变履、化乾为天而本宫之火已竭，阳气外散而尽，终归于尽。断语对象逐名对回：所问为父之寿数，复苏与逝世两断主语同为父。",
 basis="tradition: 筮占（卡面载明，逐字照录）。systems_used: 筮占（周易卦象＋本宫纳甲参断）。卡面未载六爻全盘（chart_complete=false，原文只记兑之履与断语自述卦象），残损已注明并降置信。已载面：父寿数（主问）、卧疾三年昨日气尽复苏（事件面）。断项过闸：复苏能言能食←兑为口为言、本宫火尚在；数日内逝←变乾为天、气散难收，两段触发=变卦之象。对象核：承受对象=父，应验同为父。应期定日档（近病寿数问），以复苏后数日为窗、三日内为主坐标。trigger：本例卡面 tradition 为筮占、非六爻，三项全 false。")
RES = "原盘残损（chart_complete=false，原文只记卦名与断语自述要点、无六爻全盘），无全盘可装，按原文自述要点作断并降置信——备用路径已用"
P["BQ-010"] = dict(confidence=0.50, trigger=T(ru=True, reason=RES),
 prediction_text="断：此讼不利、难以胜诉。蒙之未济——未济者事终不成之象；父母爻空亡：父母为状纸、文书、证据与官府文案，空亡则文凭无着、证据落空，讼事失其凭据。谈朝辅此讼终局偏负：或败诉、或拖延无果而罢，宜息讼和解，不宜力争。应期：文书空亡逢出空填实亦难成事（未济终局已定），只给月尺度——旬月之间见分晓、结果于占者不利（对表：讼事门类无应期取法成文，此为「对表无此门类」，按用神状态定尺度）。",
 basis="tradition: 六爻（卡面载明，逐字照录）。systems_used: 六爻。卡面未载全盘（chart_complete=false，只记蒙之未济、父母空亡，无日期），残损已注明并降置信。门类应期对表查讼事门：原表注讼事诸章只有成败断法、无应期取法——对表无此门类，已明写。已载面：官司成败（主问）。断项过闸：不利←父母空亡（文书证据指代链）＋变卦未济（事不成之终局象）。对象对齐：所问对象=谈朝辅本人之讼；用神取父母（文书）与世爻（本人，盘残未载）；应验对象=占者本人，同一。终局反转扫查：盘残，三类信号判据均无从成立，初判维持。")
P["BQ-011"] = dict(confidence=0.50, trigger=T(ru=True, di=True, reason=RES+"；官鬼冲世主凶与日辰扶起、财动两读相争，已在断语中并列取舍——disputed 留痕"),
 prediction_text="断：官司有惊而无大败，最终以破财了事。官鬼冲克世爻——对方与官府之力直压占者，讼势凶险；然日辰扶起世爻，世得日助而不倒，占者自身站得住，不至惨败；财爻又动：财动主钱财出入，此讼须以钱财消解——费财、使财之后方得平息。终局单判：不败而破财，祸福以「破财免灾」收束。应期：日档偏旬——官鬼冲世逢日扶，事在旬内见转折（对表：讼事门类无应期取法成文，对表无此门类，按状态定尺度）。",
 basis="tradition: 六爻（卡面载明，逐字照录）。systems_used: 六爻。卡面未载全盘（chart_complete=false，只记离之贲、日辰扶起、官鬼冲克世爻、财爻又动，戊子日），残损已注明并降置信。门类应期对表：讼事无应期条文，对表无此门类。已载面：官司祸福（主问）。四路合参：本气（世得日扶，有气）／官鬼冲世为忌路／动化（财动）／世应（盘残不计）——合参方向：世有气而鬼来冲、财动泄局，取「不败破财」。对象对齐：所问对象=周焚松本人；用神官鬼为讼方之力、世爻为本人；应验对象=本人，同一。动化方向核对：财爻发动无化出记载，记「动化方向：无化出可核」；反转条件：无源绝三征，记「反转条件：不成立」。")
P["BQ-012"] = dict(confidence=0.62, trigger=T(ru=True, reason=RES),
 prediction_text="断：倭寇不来犯。官鬼为寇，鬼爻衰而静——寇势衰弱且安静不动，无兴兵来犯之象；噬嗑卦虽有颌中之梗，终不为大患。此番可安，至多虚惊。应期：鬼静衰弱，无应期可取（不来则无至期）；若论警戒之窗，以旬内为限、旬内无警即定（对表：趋避／倭寇门类无应期取法成文，对表无此门类）。",
 basis="tradition: 六爻（卡面载明，逐字照录）。systems_used: 六爻。卡面未载全盘（chart_complete=false，只记噬嗑、鬼爻衰静，丙子日），残损已注明并降置信。门类应期对表：无倭寇／趋避应期条文，对表无此门类。已载面：倭寇来犯否（主问）。断项过闸：不来←官鬼衰静（寇之指代链＋衰静状态）。对象对齐：所问对象=倭寇之来否；用神官鬼；应验对象=本地军民之安否，指向同一事。终局反转扫查：鬼静无伏神引拨等判据成立项，初判维持。")
P["BQ-013"] = dict(confidence=0.55, trigger=T(ru=True, reason=RES),
 prediction_text="断：久雨未止、短期难晴。申、子两爻俱动，与日辰申字正合成父母局——父母主雨，动而成局，雨势成势连绵，此象主雨还将持续，眼下放晴无望。晴期：日档——父局逢冲方散，待寅日冲申破局，雨势方收、转晴（窗口：本旬之内；主坐标：寅日）。近段续雨、远段寅日冲局转晴，远段触发=日辰冲开三合父局之支。",
 basis="tradition: 六爻（卡面载明，逐字照录）。systems_used: 六爻。卡面未载全盘（chart_complete=false，只记随之咸、申子两爻动成父局，五月甲申日），残损已注明并降置信。门类应期对表：天时门类不在对表内，对表无此门类，按三步定应期——定尺度：久雨占晴为近事，日档；三路候选：冲实（寅冲申破局）／填实（无空可填）／逢值（申子值日反助雨局，与终局相悖舍之）；取冲实一路、寅日为主坐标。已载面：晴否（主问）。对象对齐：所问对象=天时雨晴（非人对象），应验同为天气。动化方向：申子动而合局、无化出记载，记「动化方向：合局」；反转条件：不成立。")
P["BQ-014"] = dict(confidence=0.50, trigger=T(ru=True, reason=RES),
 prediction_text="断：飓风一时不止，行程受阻、此时不可行。兄弟、父母俱动：父母主风雨、动则风势方盛；兄父合住应爻——应爻被合绊，所谋行程与彼方皆被牵住，困之震，困而难动。须待应爻逢冲开合、父母势衰之日，风止方可成行。应期：日档——窗口本旬之内，主坐标取冲开应爻合处之日（应爻所合之支的冲日）；近段风不止行不得、远段冲开后风止行成，远段触发=合处逢冲（对表：天时门类无应期条文，对表无此门类）。",
 basis="tradition: 六爻（卡面载明，逐字照录）。systems_used: 六爻。卡面未载全盘（chart_complete=false，只记困之震、兄父俱动合住应爻，辛丑年秋丁亥日；应爻地支未载），残损已注明并降置信。门类应期对表：天时无条文，对表无此门类；合住闸门优先——先等冲开合处之支再取点，已按此序。已载面：风何时止（主问）、行程可行否（续问）。对象对齐：所问对象=占者本人之行程；应验对象=本人，同一。")
P["BQ-015"] = dict(confidence=0.55, trigger=T(ru=True, reason=RES),
 prediction_text="断：是年年景不丰——雨水偏多、有水患之象，五谷歉收。水官鬼与应上父母爻俱动而伤克世爻：父母主雨、动而克世，主雨多成灾；水鬼发动，水患、阴湿伤稼；妻财伏藏不出：财主谷食收成，伏而不现，主收成不显、年成歉薄。终局：丰歉定为歉年，防夏秋之交水发伤田（年档：是年之内，雨患集中于夏秋）。",
 basis="tradition: 六爻（卡面载明，逐字照录）。systems_used: 六爻。卡面未载全盘（chart_complete=false，只记蒙之中孚、水鬼与应上父动伤世、财伏，戊午年正月辛亥日），残损已注明并降置信。门类应期对表：年时门类不在对表内，对表无此门类；应期按年档表达（所问为一岁年景）。已载面：一岁风雨（事件面）、五谷丰歉（主问）。对象对齐：所问对象=一地年景（非人对象）；用神妻财为谷食、父母为雨泽；应验同为本地年成。终局反转扫查：财伏一路查引拨判据——伏财无飞神开与引拨之路的记载，判据不全，只作「财伏不出」本断、不翻转。")
P["BQ-016"] = dict(confidence=0.55, trigger=T(ru=True, reason=RES),
 prediction_text="断：其年倭乱必至，且祸不轻。六三午火官鬼发动——鬼动主寇至兴祸；鬼化出酉金，乱势绵延、由夏及秋不息；兄弟带刑克世：兄弟主劫掠、耗损，带刑克世，主军民受掠受害、内有劫夺之伤。应期：年档之内，鬼动逢值——午火鬼值月之夏间（午月）寇势最炽，化酉主秋间（酉月）再炽或方收（对表：年时／倭乱门类无应期条文，对表无此门类，按动爻逢值定主坐标）。防备当在夏秋两季，尤重午月。",
 basis="tradition: 六爻（卡面载明，逐字照录）。systems_used: 六爻。卡面未载全盘（chart_complete=false，只记困之大过、六三午火鬼动化酉金、兄带刑克世，甲寅年正月庚申日），残损已注明并降置信。已载面：其年倭乱如何（主问）。动化裁决留痕：动化方向——六三官鬼午火动化酉金（化出之神为金、非进非退之明载，按鬼势延续论）；反转条件——无源绝三征，不成立，初判维持。对象对齐：所问对象=一地军民；用神官鬼为寇、世为军民；应验对象=本地军民，同一。四路合参：鬼动克世一路凶、兄刑克世一路凶，合参方向偏凶，无救应记载。")

ids_b02 = ["AS-210","AS-211","AS-212","AS-213","AS-215","AS-301","AS-302","AS-303","AS-304","AS-305","AS-306","AS-307","BQ-001","BQ-010","BQ-011","BQ-012","BQ-013","BQ-014","BQ-015","BQ-016"]
assert set(ids_b02) == set(P.keys()), set(P.keys()) ^ set(ids_b02)
for cid in ids_b02:
    d = P[cid]
    rec = {"case_id": cid, "prediction_text": d["prediction_text"], "basis": d["basis"], "confidence": d["confidence"], "trigger": d["trigger"]}
    with open(os.path.join(OUT, cid + ".json"), "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
n = 0
for cid in ids_b02:
    with open(os.path.join(OUT, cid + ".json"), encoding="utf-8") as f:
        r = json.load(f)
    assert r["case_id"] == cid and r["prediction_text"]
    n += 1
print("B02 written+verified:", n)
