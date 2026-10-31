import json, pathlib
outdir = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3/runs/round91/predictions')
outdir.mkdir(parents=True, exist_ok=True)

F = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}
def ly(reason):
    return {"changed_main": False, "reserve_used": False, "disputed": False, "reason": reason}

P = {}
# ---------- B01 ----------
P["AS-001"] = dict(confidence=0.62, trigger=dict(F),
 prediction_text="方向：儿子不在主人（master）处，而在母亲自家。systems_used：horary卜卦占星（Lilly古典规则）。具体断语：儿子之主星木星（5宫主）落上升角宫，即落问卜者所在之处，主儿子身在母亲一方/自宅；月亮入相六合4宫主土星（母亲居所之主）亦指居所一线。应期：两主星三合于卡面所载7月25日14时成相，该时点前后当有儿子确切消息或本人现身，时间窗以7月下旬数日计。",
 basis="卡面未标注 tradition 字段，本例据 Lilly 卜卦题面与上升/宫主配置自决为 horary。\n依据：木星为5宫主（子）而居上升，古典卜卦以所问之人之主星落问者宫位主其人在问者处；月亮27°双鱼入相六合土星（4宫主，宅）。应验对象为儿子本人，承受对象与应验对象同一。盘面仅卡面散述星位、无全图，置信因此压低。")
P["AS-002"] = dict(confidence=0.74, trigger=dict(F),
 prediction_text="方向：会致富，且财富可久。systems_used：horary卜卦占星。分项：(1)将富，不靠婚姻自食其力亦可致富；(2)得财之途在自身行业经营与职位声望——火星（2宫主兼福点主）落上升主本人进取得财，木星擢升居角近天顶主贵显助力；(3)应期以年为单位（月亮尚差6°27'合上升主金星，主进程以年计），中年渐盛、非一夕暴发；(4)2宫头与福点俱固定星座，主财能守、致富后可延续。",
 basis="卡面未标注 tradition 字段，此商人问富题按 Lilly 二宫问事的卜卦体裁自决。\n依据：火星2宫主落上升近狮子座轩辕十四旁之角宿、木星擢升于巨蟹角宫近 culminating、月亮（10宫主）离火水相位而入合金星、福点固定。量级核算（R80-REV1现行节）：做功主线为木星擢升角宫助成＋火星2宫主入命两线同向助成，无压制线足以降格，故富取足级而非小康；婚姻非得财主线，致富靠自身与事业。")
P["AS-003"] = dict(confidence=0.65, trigger=dict(F),
 prediction_text="方向：买得成（positive）。systems_used：horary卜卦占星。具体断语：能与卖主成交、购得 Master B. 的房屋，且筹款虽迟但赶得上付款——卖主之星太阳居7宫得金星接纳、7宫主即11宫主（希望）主交易有成，金星入相三合土星（4宫主，房屋本身）主契成；水星（2宫主，本人财）逆行主钱不能按原期调回、须拖延周转，应期以月计，约在钱款原定六个月调回期前后落定成交，卖价可往下谈、不必照卖主最初开价530镑全付。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：太阳（卖主）居7宫受纳、 Venus 入相三合 Saturn（4宫主＝房）、7宫主兼11宫主；逆行水星只压时间不压方向，土星除逆行迟滞外无大凶。初判成交，盘面无可指认翻转触发，终局维持。上升星座度数卡面自注 OCR 残损（note 明言 garbled），不据上升细节加断，置信因此下调。")
P["AS-004"] = dict(confidence=0.72, trigger=dict(F),
 prediction_text="方向：传闻不实（negative）——国王并未攻下剑桥。systems_used：horary卜卦占星。具体断语：各宫头皆变动、月亮落陷无所喜之星座主消息虚浮无根；问者一方（议会方）之上升主擢升有力，对方7宫主入落受困，国王一方并无攻取该城之实据。此为当日即时传闻核验，应期以日计，数日内即见分晓为虚报。",
 basis="卡面未标注 tradition 字段，本例为战时传闻真伪题、据 Lilly 卜卦散述星位自决 horary。\n依据：土星伤10宫头、火星伤7宫头、月亮 cadent、7宫主 entering fall 且受 affliction，与上升主 exaltation 成强弱对照，消息主星弱主传闻不实。无全图，仅据卡面所列证词作断。")
P["AS-005"] = dict(confidence=0.70, trigger=dict(F),
 prediction_text="方向：船还活着、未沉（positive）。systems_used：horary卜卦占星。具体断语：月亮（上升主，船身之主）擢升于金牛居11宫，入相三合7宫太阳、水星且近木星，主船体得救、人员尚存；土星在白羊刑上升主近，主曾遇险受损、被风浪所困而非沉没。方位与消息：船在西班牙沿海一带海面漂航/靠岸待援，消息将随船抵港或来信而至，应期以周计（月亮三合只差数分先成，主消息不远，数周内有确讯）。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：上升巨蟹以其上升度数主船体，月亮为上升主而 exalted、applying trine 太阳水星且近木星，为古典沉船问中主船存之强证；土星刑上升只定受险之量。南交点居9宫主远航有惊，不改存亡方向。")
P["AS-007"] = dict(confidence=0.80, trigger=dict(F),
 prediction_text="方向：Waller 一方得胜、Hopton 败（positive 对问者所问 Waller 方）。systems_used：horary卜卦占星。具体断语：月亮擢升与木星同在、太阳（Waller 军资助之主）居10宫正在擢升正度19°白羊，主 Waller 军势正盛；Hopton 之主星土星焦伤（sub radiis）、入落、无相位、游荡无援，9宫只有火星与南交点主其后援未备。此战当日（3月29日）即分胜负，应期为当日。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：Waller 以上升、月亮、木星、金星为征，Hopton 以7宫主土星为征；一方主星擢升合吉、对方主星 fall＋sub radiis＋peregrine＋无援，强弱悬殊无争议证词。")
P["AS-008"] = dict(confidence=0.66, trigger=dict(F),
 prediction_text="方向：Essex 能取下 Reading（positive），但取法是围困迫降、非强攻破城。systems_used：horary卜卦占星。具体断语：Essex 之星火星虽入落却与月亮互容得力，守将之星土星（4宫主）入落无救，国王之星太阳居7宫固定星座主守方尚能撑持一阵；城中粮弹（木星、金星居5宫一线）有限，撑不到久围。应期以周计，围至4月下旬城方交出（卡面载城于27日交付，与围城进程相合之时段）。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：火星为天蝎上升之主（Essex）与月亮 reception、月亮 void 后入相火星（长升星座折算）主事终成；土星4宫主 fall 主守将弱。年份卡面自注有 1644/1643 印刷歧异（残损旗标：asked_at 注明 OCR 年份与史实围城年份不合），故应期只报月内时段不钉年份。")
P["AS-009"] = dict(confidence=0.58, trigger=dict(F),
 prediction_text="方向：狗找得回（positive）。systems_used：horary卜卦占星。具体断语：往城的西方偏南方位搜寻——狗之主星在西方星座、南象限偏西，且与上升同三方属性主仍在伦敦城内未出城；月亮在风象星座被日光掩，主一时不见踪迹。应期以日计：太阳于次周一入相土星（上升主），主周一前后得狗或得确讯，搜寻窗为数日内。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：6宫及其主主小兽（狗），其主星方位证词指向西偏南、同 triplicity 主未离本城、入相三合6宫头主回归；日月居8宫主藏匿难见。卡面自注多处字形 OCR 残损（note: several glyphs garbled），细节方位只取卡面明述之西方偏南，不再细化街区，置信下调。")
P["AS-010"] = dict(confidence=0.62, trigger=dict(F),
 prediction_text="方向：仆人向西而去，且将被找回/自行返回（positive 于追回）。systems_used：horary卜卦占星。具体断语：水星为本盘仆人之星，居西方星座、南象限，主其人往城西偏南投奔藏匿；月亮在2宫自宫有力、仆星与上升主急趋三合出角宫，主事不拖久、人终回到主人一方。应期以日计，出走后一周内有消息或人回，方位先往西寻。",
 basis="卡面未标注 tradition 字段，此逃仆题据 Lilly 以水星为仆星的卜卦散述自决 horary。\n依据：水星（仆）西方星座南象限定方向；月亮出走时与今同在西方星座主未远；仆星与上升主 hastening to trine 主重逢。无全图，归期只给一周量级。")
P["AS-011"] = dict(confidence=0.74, trigger=dict(F),
 prediction_text="方向：这门婚事能重新撮合并办成（positive）。systems_used：horary卜卦占星。具体断语：木星擢升入相六合土星（7宫主，男方），并把土星之力转交太阳（上升主，女方），中途无 prohibition/frustration 截断，主有人从中撮合、双方重新接上头；月亮与金星、金星与太阳互容主女方体面不失。应期以日计：男方宜于6月19日近午先行一步，土火成相之6月27日前后婚议落定。",
 basis="卡面未标注 tradition 字段，此婚议复燃题据 Lilly 转光（translation of light）卜卦证词自决 horary。\n依据：Jupiter exalted applying sextile Saturn（男）且 transfer 至 Sun（女）、无阻断成相，古典主婚成之强式；月亮 void 后对冲太阳主先僵后通。卡面年份未载，应期只用卡面6月日期。")
P["AS-012"] = dict(confidence=0.82, trigger=dict(F),
 prediction_text="方向：得不到所求的教职/圣俸（negative）。systems_used：horary卜卦占星。具体断语：土星在上升受困直接坏此问；圣俸之星木星（9宫主）与上升主、月亮全无相位，上升主与月亮皆不在9宫，主星之间无转光、无集光、无互容——求职一线全断；月亮离三合而入相对冲水星（3宫主）主空费口舌、徒劳奔走。此事无成期，断为不成，不报应期。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：卡面列 Lilly 自述七项否定证词（无相位、无转光集光、无互容、主星不入9宫、土星 infortuning 上升、金星居7对冲上升），证词同向无一支持成事。部分星符 OCR 残损（note 明言 glyphs garbled），但否定证词为 Lilly 编号明述，不依赖残损字形。")
P["AS-013"] = dict(confidence=0.60, trigger=dict(F),
 prediction_text="方向：赃物可部分追回、贼可指认（positive 于追回一部分）。systems_used：horary卜卦占星。具体断语：贼星取角宫唯一游荡之木星、居7宫头天蝎（水象）——贼是与水上营生/仓囤搬运相关之人（船夫水手一类），非远来生人；赃物之星水星居双鱼（水象）、福点居巨蟹（水象），三证同指货物仍在近水潮湿之处（仓边/船边）未远运。月亮（福点主）六合水星、水星三合福点主尚有追索之线；应期以日计，事发后数日内寻回一部分，其余难全数。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：7宫为盗，角宫 peregrine 木星居7宫头取为贼星为 Lilly 盗问定例；水星2宫主虽 fall/detriment 却在自界、得月亮六合与福点三合，主物有回头之望但受损有亏，故只断部分追回。")
P["AS-014"] = dict(confidence=0.56, trigger=dict(F),
 prediction_text="方向：贼不是主人所疑的女仆，而是个男子；钱难全数追回（negative 于全额追回）。systems_used：horary卜卦占星。具体断语：火星（上升主）与土星（居7宫盗位）各在自界自面，按例不得取为贼星；真正贼星为角宫无尊贵之水星，水星合土星、刑火星，两刑星皆阳性、月亮又在阳性星座近太阳——贼为男性，身份近水星之象（年轻男子/干文书跑腿营生之人，身边近处之人）。水星无尊贵又受两凶夹刑，主钱已散出、至多追回小部分。",
 basis="卡面未标注 tradition 字段，此盗钱题据 Lilly 贼星取舍规则（有界面者不取）自决 horary。\n依据：Mars、Saturn 因 own terms and face 被 Lilly 明文排除，Mercury partile 合 Saturn 刑 Mars 取贼星；阳性证词三重主贼为男，纠正问者疑女仆之误认（应验对象复核：断的是贼之身份，落在水星所指男子，非被疑女子）。无日期，应期不报。")
P["AS-015"] = dict(confidence=0.64, trigger=dict(F),
 prediction_text="方向：丈夫还活着、终将归来（positive 于存亡），但归期迟、且她本人病势沉重未必等得到团圆。systems_used：horary卜卦占星。具体断语：丈夫之星太阳得 hayz 之位、全无 affliction，主其人在海上平安无灾；归期以月计、须待航程走完方回，非数周之事。附断她本人：6宫主土星逆行主旧病反复、火土将成凶相逼近月亮旧位，主她此后病转沉重，此为对她自身之附断，与丈夫存亡方向分开。",
 basis="卡面未标注 tradition 字段，此问海上丈夫题据 Lilly 以太阳为夫星的卜卦散述自决 horary。\n依据：夫星 Sun in hayz free from all affliction 为存亡题决定性证词，卡面自注此点 Lilly 明述无歧义；其余星位卡面自注 OCR 部分残损（positions partly garbled），故归期只给月量级、不钉具体日，置信下调。应验对象复核：存亡断丈夫、病势断妻子本人，两条分主不相混。")
P["AS-204"] = dict(confidence=0.58, trigger=dict(F),
 prediction_text="方向：病在胸腹（乳房与胃一带），属固定难移之沉疴，可治性差、缠绵难愈（negative 于速愈）。systems_used：horary卜卦占星（decumbiture 式病问）。具体断语：6宫受入落之星所伤，上升主刚离土星之刑、土星当时在巨蟹（主胸与胃），月亮居4宫与土星同在，四角皆固定星座主病势已成形、固定不化，非新起急症；纵经调治亦只能缓而难断根，病程以月/年计。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：土星在巨蟹定病位胸胃、6宫 afflicted by planet in fall、四角 fixed 定病之固定性，三证合定病位与难愈。无日期，应期以病程月/年量级表达。")
P["AS-205"] = dict(confidence=0.76, trigger=dict(F),
 prediction_text="方向：病人将死于此病（negative，凶终）。systems_used：horary卜卦占星。具体断语：上升被8宫主之实体临宫所伤，6宫固定受困、6宫主在固定土象忧郁星座，太阳（时光之主）与6宫主土星在固定星座成正对冲，月亮近南交点且在上升受 affliction——生气之星全线受制、无一救应，病为固定忧郁之沉疴（土性积滞），终局主不治。应期以日/周计，图为1645年7月16日，凶终在图后数周内（固定星座主其期以周计）。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：古典病占生死以上升、上升主、月亮受8宫/6宫主凶伤且无吉救为死征，本例四项死征齐备且皆固定星座。上升星座字形卡面自注 OCR 残损不予断言（note 明言 glyph corrupt），断语不依赖该字形。")
P["AS-206"] = dict(confidence=0.54, trigger=dict(F),
 prediction_text="方向：终能嫁给所慕之人，但须过阻滞与体面关、非顺遂即成（positive 而迟）。systems_used：horary卜卦占星。具体断语：问者之星水星逆行且焦伤（under beams），主她自身处于弱势、心虚退缩、名声上有顾虑；对方之星擢升、近六合金星，主男方条件好且另有周旋之人（卡面载其曾与另一人纠缠）；月亮离木星之刑而以三合把光转交水星（上升主），主终有转机接上。两主星仅半六合、宫位虽佳而相位弱，故成婚应期以月计、拖延后成。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：Moon translating Jupiter's light by trine to Mercury（上升主）为成事之桥；Mercury retrograde＋combust 只压过程与等级不翻方向（无翻转触发不改初判之迟成）。图题年份1646、日期 OCR 不可读（残损旗标），应期只给月量级。")
P["AS-207"] = dict(confidence=0.70, trigger=dict(F),
 prediction_text="方向：大主教将死于暴力横死——公开行刑式的刀兵之死（被斩），非囹圄中自然病亡。systems_used：horary卜卦占星。具体断语：以9宫头为其上升（教会之人），其主星土星入落、久逆、居图之12宫（囚禁）主其人困于狱中而势败；月亮离土星入相太阳近8宫头，太阳在火象星座入相对冲火星（其 dispositor），月亮距火星之体仅7°——火星主刀兵刑杀、火象主公开，合定死法为兵刃加身、刑场公开处决。应期以月计，月亮至火星之相位成时为期。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：死法题以当事人主星状态＋8宫一线＋火星相位定死式：土星 fall/retro/12宫主囚败，太阳火象冲火星、月亮趋火星主刀兵。上升度数卡面未给，不据之细化。")
P["AS-208"] = dict(confidence=0.68, trigger=dict(F),
 prediction_text="方向：Prince Rupert 在此战事中得不到荣誉、反居下风，Essex 一方占上风（negative 于 Rupert）。systems_used：horary卜卦占星。具体断语：Rupert 以10宫及其主太阳为征，太阳游荡且入弱（detriment）居固定星座，主其人无地无援、逞勇无功；Essex 之星金星与土星互容、且金星处置 Rupert 之主星，又金星、月亮双双以相位临10宫头，主荣誉与场面归 Essex 一方。Rupert 后局为屡战不利、声望受损而退。应期以月计，本季战局内见分晓。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：贵人以10宫论，Sun peregrine＋detriment 为弱征决定项；Venus（对宫主，Essex）reception 土星且 dispose 太阳，主对方反握其命门。")
P["AS-209"] = dict(confidence=0.58, trigger=dict(F),
 prediction_text="方向分问：(1)国王能弄到爱尔兰援军之事有成象但兵力与祸害有限；(2)王后将南下进军并与国王会合，但声势转衰、难言得利。systems_used：horary卜卦占星。具体断语：国王之星月亮在巨蟹自宫居10宫、增光、无凶伤，主王势自固；11宫（援助）主太阳擢升居7宫趋11宫头、只差6°成正相，主援军之议可成、爱尔兰兵有来路。王后之星土星（4宫主，即10宫之7宫）正换座入白羊入落，月亮距其三合仅差3–4°，主王后进军后与王会合在即（以周/月计），然入落主其军势自此走低、进军得利有限。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：一图两问分主：王以月亮（自宫强）论、援以11宫主太阳擢升趋宫头论、后以土星换座入落论兴衰、三合差度论会合之期。两问方向不同系分主各断，非同一终局并陈。")
# ---------- B02 ----------
P["AS-210"] = dict(confidence=0.68, trigger=dict(F),
 prediction_text="方向：能得到所求的官职/位置（positive）。systems_used：horary卜卦占星。具体断语：月亮居10宫（官位之宫）入相三合土星，土星在上升有擢升之尊、与金星（问者之星）互容，主官位一方接纳问者、事可落定；但11宫主太阳居7宫对冲上升且带南交点，主其所托之『友人』实为虚情假意、暗中作梗，成事靠月亮土星正线而非靠此友。应期以周/月计，月亮三合土星成相之时段为落定窗。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：Moon in 10th applying trine Saturn＋Saturn 与 Venus mutual reception 为求官成事正格；Sun lord11 with Cauda in 7th 只定假友之附断不翻主方向。本图与前图仅差四五分钟（卡面载），星位承前图读法。")
P["AS-211"] = dict(confidence=0.66, trigger=dict(F),
 prediction_text="方向：马找得回（positive），且马往正西方向去了。systems_used：horary卜卦占星。具体断语：马之主星（12宫主）逆行且急趋合问者2宫主（其财物之宫），逆行主回头、合2宫主主马回到主人财物之内；月亮居2宫、2宫头近处两星逆行同主归还之象。方向证词一边倒：12宫星座与马星所在星座皆指西，往 Henley 以西沿路寻访。应期以日计，数日内有马讯或马回。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：lord12 retrograde hastening to conjunction lord2 为失畜回归定式；方位以多证同指（plurality full west）取正西。7宫受 affliction 主或经人手转送，不改可回方向。")
P["AS-212"] = dict(confidence=0.68, trigger=dict(F),
 prediction_text="方向：不是中邪/被巫（negative 于被巫之说），是自然之病，且病情将转好。systems_used：horary卜卦占星。具体断语：月亮趋对冲土星、两星分居6、12宫，确是惹起巫蛊之疑的表象；但上升、上升主、月亮皆未受12宫主之伤，被巫的正证不成立；月亮过土星之冲后即入相上升主，上升主在地平线上趋天顶，主病势过此关口后向上回转、药石终能见功。应期以日计，月亮过冲后数日见转机。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：Lilly 巫蛊题定例须上升/月亮受12宫主 affliction 方成，本例明文三处皆不受伤，故驳巫；Moon applying after opposition to lord of Ascendant 主愈。图题年份1646、日期 OCR 不可读（残损旗标），应期只给日量级。")
P["AS-213"] = dict(confidence=0.60, trigger=dict(F),
 prediction_text="方向：逃犯往正东方向去了，且终将被抓回（positive 于追回）。systems_used：horary卜卦占星。具体断语：逃犯以12宫头射手与木星（居狮子）为征，12宫星座、木星所在星座、天象限、月亮所在星座四证一致指东；月亮近上升、离三合木星而入相对冲太阳且两星皆角，主其行踪终究暴露于光天化日之下、难久藏；木星居8宫主其处境凶险，抓回时或带伤损之虞。应期以日计，东向追缉数日内有获。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：方位四证 unanimously eastward 取东；月亮与太阳角宫对冲主暴露，木星水星成相主消息有路，故断可回。木星居8宫只定其险不改追回方向。")
P["AS-215"] = dict(confidence=0.78, trigger=dict(F),
 prediction_text="方向：Essex 此次西征将以惨败收场、无功而辱（negative）。systems_used：horary卜卦占星（事件图 event figure）。具体断语：上升主土星游荡入落居2宫，南交点坐上升，月亮入弱且离三合土星后入相刑火星（其2、9宫主，军资与远行），福点被7宫主水星（敌方之星）处置——主军资断绝、远征深入敌境而后路被抄，终局为全军受困、被迫缴械投降式的败局，本人蒙羞而还。应期以月计，出征后本季内（数月）败局落定。",
 basis="卡面 tradition＝horary（逐字照录卡面值 horary）。\n依据：事件图以出征时刻论成败：lord Ascendant peregrine＋fall、Cauda in Ascendant、Moon in detriment applying square Mars、Fortune disposed by lord7，五项败征齐备无一吉救，等级取惨败足级（R80-REV1：做功主线为敌方处置福点＋上升主入落两线同向压制，无助成线让位）。")
P["AS-301"] = dict(confidence=0.42, trigger=dict(F),
 prediction_text="方向：2020年世界局势主线为一场自年初暴发的全球性健康危机及其连锁冲击（negative 于世局安稳）。systems_used：西洋占星（mundane 世界占星，无盘面卡面、按公开逐月预测体裁）。逐月骨架：1–2月危机在东亚显形并向外扩散；3–4月全球蔓延、各国封锁、股市与经济急挫为全年最凶段；5–6月第一波缓和但未清；夏秋反复，秋冬（10–12月）第二波再起、疫苗研发传出决定性好消息而局势始见转机。置信低：卡面无任何星盘附件，此为体裁级方向断。",
 basis="卡面 tradition＝astrology（逐字照录卡面值 astrology）。\n残损旗标：attachments 为空、无任何盘面/星位输入，无法回扣星体×宫位×相位逐项作断，只能按 mundane 逐月预测的问题结构给方向与月份骨架，并大幅降置信，不臆补具体星盘。")
P["AS-302"] = dict(confidence=0.58, trigger=dict(F),
 prediction_text="方向：未来六个月（2020年10月至2021年4月）疫情先恶化后转机，疫苗前景明确向好（positive 于疫苗）。systems_used：西洋占星（mundane）。具体断语：秋冬月份病例再冲高、管控收紧为最难段；其间（11–12月）疫苗三期结果与获批消息落定、开始接种；2021年初供应与接种进度慢于预期、病毒变异带来反复，至3–4月随接种铺开局势实质缓和，但疫情不会在六个月内结束。",
 basis="卡面未标注 tradition 字段，此例据 Adams 占星访谈的公开预测体裁自决为西洋 mundane 占星。\n残损旗标：attachments 为空、无盘面输入，断语只能落到问题自带的时间窗（六个月）与疫苗门类，不能回扣具体星象，置信压低。")
P["AS-303"] = dict(confidence=0.38, trigger=dict(F),
 prediction_text="方向：按占者本人（Kumar）一贯的吠陀占星推法落断——第三次世界大战迫在眉睫，将在2024年6月内被触发点燃。systems_used：吠陀占星（vedic，公开预测体裁）。具体断语：其所指认的触发窗在6月中下旬（以6月18日前后数日为最险坐标），由地区战争（俄乌/巴以）外溢、强人政权与恐怖袭击式事件点火，战火先起于既有热点再扩散；时间窗即2024年6月，过期不候。置信低：卡面无盘面，此为对该占者公开断法风格与本题问法的复现式落断。",
 basis="卡面未标注 tradition 字段，此例据『印度诺斯特拉达穆斯』Kumar 以吠陀占星发布三战日期的体裁自决。\n残损旗标：attachments 为空、无出生/事件盘面输入，无法逐项回扣星象；断语按其公开预测的一贯形态（指认具体日期窗）落点，并明确低置信。")
P["AS-304"] = dict(confidence=0.52, trigger=dict(F),
 prediction_text="方向：唐纳德·特朗普赢得2024年美国总统选举（positive 于特朗普）。systems_used：西洋/吠陀混合占星公开预测体裁（卡面仅存 X 帖文来源）。具体断语：选举日（2024年11月5日）前后星象对特朗普一方更有利，哈里斯声势在选前冲高但关键摇摆州落点归特朗普，胜负差距不大、以选举人票定胜负；结果在投票日后数日内明朗，无长期争议拖延。",
 basis="卡面未标注 tradition 字段，此例据其 X 账号占星预测帖的体裁自决。\n残损旗标：attachments 为空、无候选人命盘/选举日盘输入，无法逐项回扣行运，只能按公开预测题给单一赢家方向，置信压低。")
P["AS-305"] = dict(confidence=0.50, trigger=dict(F),
 prediction_text="方向：卡玛拉·哈里斯以极小差距赢得2024年美国总统选举。systems_used：西洋占星（选举日盘＋候选人行运，Astrology King 式公开分析体裁）。具体断语：占者自承两方盘面势均力敌、极难判断，本断只取其天平最后落点：哈里斯在选举日行运略占先机，特朗普盘面强项多在声势而非落点；胜负由少数摇摆州以极小票差决定，计票拖至投票日后数日方全定。",
 basis="卡面未标注 tradition 字段，此例据 Astrology King 网站选举盘分析体裁自决为西洋占星。\n残损旗标：attachments 为空、卡面明载占者自承盘面势均力敌极难判断，故置信压至0.50、断语只给单一方向不加码细节，不臆补盘面。")
P["AS-306"] = dict(confidence=0.56, trigger=dict(F),
 prediction_text="方向：民主党候选人将中途更替——拜登退选、哈里斯接棒；而最终赢家是特朗普。systems_used：吠陀占星（vedic-astrology）。具体断语：2024年6月发断时拜登尚未退选，本断第一层即指其年迈星象不支持其走完选程，夏季（7月前后）退选换人；第二层：接棒者声势虽起，吠陀行运大势仍归特朗普，11月5日选举由特朗普胜出，两段应期分别为2024年夏（换人）与2024年11月（定局）。",
 basis="卡面 tradition＝vedic-astrology（逐字照录卡面值 vedic-astrology）。\n残损旗标：attachments 为空、无拜登/特朗普命盘输入，两段断语按吠陀公开预测体裁与题面所问（含候选人更替）落点，置信压低；两段各有其问面依据（退选问势、胜负问势），非一段外推。")
P["AS-307"] = dict(confidence=0.52, trigger=dict(F),
 prediction_text="方向：受访职业占星师群体多数指向卡玛拉·哈里斯获胜，本断从群体多数落点——哈里斯赢得2024年美国总统选举。systems_used：西洋占星（多位占星师选举盘共识体裁）。具体断语：哈里斯一方盘面在选举日的月亮与行运落点被多数占星师评为更顺，特朗普得势于声量而失于落点；胜负仍近，靠摇摆州小幅差距分出，2024年11月5日后数日定局。",
 basis="卡面 tradition＝astrology（逐字照录卡面值 astrology）。\n残损旗标：attachments 为空、无任何一位占星师的具体盘面输入，断语只能取 HuffPost 专题的问题结构（群体表态赢家）落单一方向，置信压低，不臆造个别人盘面。")
P["BQ-001"] = dict(confidence=0.52, trigger=dict(F),
 prediction_text="方向：父亲寿数已尽、此次复苏只是回光，短期内即逝（negative）。systems_used：周易筮占（蓍筮本宫取断，非纳甲全盘）。具体断语：兑之履，兑为口为言、变乾为天，庚辛日兑宫属金而断语自述『今日庚辛本宫火』克金，主气数被克绝；卧疾三年又昨日气尽，复苏无根。应期以日计：数日内（庚辛日一线）即终，不报愈期。",
 basis="卡面 tradition＝筮占（逐字照录卡面值 筮占）。\n残损旗标：chart_complete=false，原文只记本卦兑、变卦履与断语援引之象（本宫火、兑口、变乾为天等），无六爻全盘；只据已给卦象与病史（卧疾三年、气尽复苏）作断并降置信，不臆补爻位。trigger 按非六爻例三项全 false。")
P["BQ-010"] = dict(confidence=0.60, trigger=ly("初判据父母空亡定败，无动爻材料可构成翻转触发，changed_main=false；无后备取法动用，reserve_used=false；卡面证词单一无对冲，disputed=false。"),
 prediction_text="方向：诉讼败（negative）——官司打不赢。systems_used：六爻纳甲（残盘）。具体断语：蒙之未济，卦终未济主事终不成；父母爻空亡，父母主文书状纸与官府文凭，空亡主证据/文书落空、无凭可恃，讼方在文书一线先输。应期：无确切日期与动爻，应期不钉日，只断此讼无成期、拖亦无益。",
 basis="卡面 tradition＝六爻（逐字照录卡面值 六爻）。\n残损旗标：chart_complete=false，原文只记本卦蒙、变卦未济、父母空亡，无全盘、无确切日期（asked_at 明言未记日）；只据父母空亡与变卦未济作断并降置信。应期三步：尺度无从定日，冲实/填实/逢值三路皆无候选（父母何支空亡卡面未载），明写三路无候选，故不报应期。")
P["BQ-011"] = dict(confidence=0.62, trigger=ly("初判据官鬼冲克世定凶，无化出材料可翻转，changed_main=false；未用后备取法，reserve_used=false；官鬼冲世与财动同向主祸，disputed=false。"),
 prediction_text="方向：官讼大凶、占者败且破财（negative）。systems_used：六爻纳甲（残盘）。具体断语：离之贲，日辰虽扶起而官鬼冲克世爻——官鬼为讼祸之主，冲克世即祸临其身，纵有日辰一时扶持亦挡不住官鬼正冲；财爻又动，财动主破费耗财、且财能生鬼更助讼势。终局为败诉受罚兼破财，应期以日/月计，官鬼值日冲世之期为祸发坐标，残盘无支名不钉具体日。",
 basis="卡面 tradition＝六爻（逐字照录卡面值 六爻）。\n残损旗标：chart_complete=false，原文只记本卦离、变卦贲、官鬼冲克世、财爻动，无全盘；戊子日仅知日辰。应期三步：尺度定为日/月档，冲实一路无空象不取、填实无候选、逢值（官鬼逢值冲世）为与终局同向一路取作主路径，余二路以无候选舍弃；支名未载故只给路径不钉日。")
P["BQ-012"] = dict(confidence=0.66, trigger=ly("鬼爻衰静单一证词定不来，changed_main=false；reserve_used=false；无对冲证词，disputed=false。"),
 prediction_text="方向：倭寇不来（positive 于地方安宁）。systems_used：六爻纳甲（残盘）。具体断语：得噬嗑卦而鬼爻衰静——官鬼为寇盗祸患之主，衰而静主其势弱且不动，弱极不动则寇无来意、边报为虚惊。此问为近事，应期以日计，本旬内无寇至即可验，不来即无期可钉。",
 basis="卡面 tradition＝六爻（逐字照录卡面值 六爻）。\n残损旗标：chart_complete=false，原文只记卦名噬嗑与鬼爻衰静，无全盘；丙子日仅知日辰。应期三步：尺度定日档，鬼衰静则冲实/填实/逢值三路皆无『寇来』候选，与终局（不来）自洽，故只报旬内验期不钉寇期。")
P["BQ-013"] = dict(confidence=0.54, trigger=ly("初判据父母成局主雨续，无子孙发动车晴之据可翻转，changed_main=false；reserve_used=false；动爻成父局证词单一指向雨，disputed=false。"),
 prediction_text="方向：久雨一时难晴，雨还要续下（negative 于即晴）。systems_used：六爻纳甲（残盘）。具体断语：随之咸，五月甲申日得申、子两爻俱动，与日辰申字正合而成父母局——父母主雨云，动而成局、日辰又助局，主雨势正成团、当下无晴象；卦中未见子孙发动车散雨云之据。应期以日计：待父母局被冲散之日（局待冲开）方转晴，残盘无全爻支序，只给『局散之日』路径，窗为数日内。",
 basis="卡面 tradition＝六爻（逐字照录卡面值 六爻）。\n残损旗标：chart_complete=false，原文只记本卦随、变卦咸、申子两爻动成父局，无全盘。应期三步：尺度定日档，候选三路——逢值（父值日）主雨续不取作晴期、填实无空不取、冲实取义为冲散父局之日作转晴主坐标路径；支序未载不钉具体干支日。")
P["BQ-014"] = dict(confidence=0.54, trigger=ly("初判据父母动主风未止，合住应爻只定滞留之量不翻方向，changed_main=false；reserve_used=false；兄父俱动与合应证词同主滞，disputed=false。"),
 prediction_text="方向：飓风当日不会停、行程当日不可行，须滞留待风止后才走得成（negative 于即行）。systems_used：六爻纳甲（残盘）。具体断语：困之震，兄弟、父母俱动——父母主风雨，动则风势正发；兄父合住应爻，应主对方/行程彼端，被合住主动不得、行不得，寓江东返乡之行被风锁在原地。近段（当日）风不止行不成；远段须待父母爻气衰、合被冲开之日方启程，应期以日计、窗为数日内，只给冲开合之路径不钉日。",
 basis="卡面 tradition＝六爻（逐字照录卡面值 六爻）。\n残损旗标：chart_complete=false，原文只记本卦困、变卦震、兄父俱动合应，无全盘。两段式：近段据父动合应断滞留；远段触发为合待日辰冲开（通则路径），卡面无具体支名，故远段只报可成行之路径与日量级窗。应期三步：冲开合一路与终局自洽取之，填实/逢值无候选舍弃。")
P["BQ-015"] = dict(confidence=0.64, trigger=ly("初判据鬼父动克世、财伏定歉，无子孙救应材料，changed_main=false；reserve_used=false；诸证同向主歉，disputed=false。"),
 prediction_text="方向：这一年年景歉收、雨水为患（negative）。systems_used：六爻纳甲（残盘）。具体断语：蒙之中孚，水鬼与应上父母爻俱动伤克世爻——鬼主灾患、父主雨，雨患之灾动而克世，主全年雨水失调有涝患；妻财又伏藏不现，财主五谷收成，伏则谷不出、收成歉薄。量级：财伏加世受双动所克，歉取实歉而非仅平年。应期以年为单位（年时题），雨患集中于水鬼、父爻所主之夏秋雨季，坐标以季月计不钉日。",
 basis="卡面 tradition＝六爻（逐字照录卡面值 六爻）。\n残损旗标：chart_complete=false，原文只记本卦蒙、变卦中孚、水鬼与应父动、财伏，无全盘。功量核算（R80-REV1现行节）：做功线——水鬼动克世（压制）、父动克世兼主雨（压制）、财伏不现（助成线缺位），主线为鬼父双动克世，定带为歉收；无让位依据。应期按年档表达（通则k）。")
P["BQ-016"] = dict(confidence=0.62, trigger=ly("初判据鬼动化金、兄刑克世定乱起，无救应材料可翻转，changed_main=false；reserve_used=false；证词同向主乱，disputed=false。"),
 prediction_text="方向：这一年倭乱会起、地方受扰（negative）。systems_used：六爻纳甲（残盘）。具体断语：困之大过，六三午火官鬼发动——鬼动即寇患发动，非虚惊；鬼化出酉金，化金主兵刃杀伐延续入秋（酉）一线；兄弟带刑克世，兄弟主劫掠耗夺、刑主刑伤，主军民有劫掠伤损之实祸。应期以年为单位：鬼为午火，乱头起于午火当令之夏月，化酉主其势延至秋月酉金之期，坐标以月计。",
 basis="卡面 tradition＝六爻（逐字照录卡面值 六爻）。\n残损旗标：chart_complete=false，原文只记本卦困、变卦大过、六三午火鬼动化酉金，无全盘。应期三步：尺度定年档内取月，候选——逢值（午月鬼值）取作起乱主坐标路径、化出逢值（酉月）作延续坐标入 reasoning 舍作主坐标（主坐标只许一条）、冲实填实无空墓候选舍弃。动化方向：鬼动化酉金，火克金为鬼自化受制之象只调乱之量级（乱起而势不至燎原），不翻乱起方向。")

order_b01 = ["AS-001","AS-002","AS-003","AS-004","AS-005","AS-007","AS-008","AS-009","AS-010","AS-011","AS-012","AS-013","AS-014","AS-015","AS-204","AS-205","AS-206","AS-207","AS-208","AS-209"]
order_b02 = ["AS-210","AS-211","AS-212","AS-213","AS-215","AS-301","AS-302","AS-303","AS-304","AS-305","AS-306","AS-307","BQ-001","BQ-010","BQ-011","BQ-012","BQ-013","BQ-014","BQ-015","BQ-016"]

def write_batch(ids, label):
    for cid in ids:
        d = P[cid]
        rec = {"case_id": cid, "prediction_text": d["prediction_text"], "basis": d["basis"], "confidence": d["confidence"], "trigger": d["trigger"]}
        (outdir / f"{cid}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    # assert per batch
    for cid in ids:
        rec = json.loads((outdir / f"{cid}.json").read_text(encoding="utf-8"))
        assert rec["case_id"] == cid and rec["prediction_text"] and rec["basis"] and 0 <= rec["confidence"] <= 1
        t = rec["trigger"]
        assert set(t) == {"changed_main","reserve_used","disputed","reason"} and all(isinstance(t[k], bool) for k in ("changed_main","reserve_used","disputed"))
    print(label, "written+verified", len(ids))

write_batch(order_b01, "B01")
write_batch(order_b02, "B02")
# trigger counts for liuyao (BQ-010..016)
lys = [c for c in order_b01+order_b02 if P[c]["trigger"]["reason"]]
print("liuyao_with_reason", lys)
for k in ("changed_main","reserve_used","disputed"):
    print(k, sum(1 for c in order_b01+order_b02 if P[c]["trigger"][k]))
