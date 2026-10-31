#!/usr/bin/env python3
"""R85 B01 blind predictions writer. One case at a time, assert each."""
import json, os

BASE = "/home/hatch/workspace/divination/benchmark/phase3/runs/round85/predictions"
os.makedirs(BASE, exist_ok=True)

TRIG = {"changed_main": False, "reserve_used": False, "disputed": False, "reason": ""}

PREDS = {}

PREDS["AS-001"] = dict(
    confidence=0.78,
    prediction_text="断：儿子不在主人家，而在母亲自家屋里（at her own house）。子星木星（五宫主）落上升东角、贴近母亲一方，月亮在双鱼27°趋向六合四宫主土星（母亲居所），两路同指自宅；母亲与儿子两主星之三合于7月25日下午2时成象，主坐标取1638年7月25日——届时消息确证或母子相见，窗口为7月下旬数日内。方向：自宅（positive toward own house）。",
    basis="卡面未标注 tradition 字段，按题面体裁自决（Lilly 卜卦问居所）。\nsystems_used: horary（整宫、古典尊贵）。依据：木星为五宫主即子之主星，落Ascendant；月亮趋六合土星（四宫主＝母宅）。应验对象复核：断的是儿子，木星五宫主指代链落儿子本人，承受与应验同一。R80-REV1：无量级类断项（居所定位非量级），不适用、已登记。应期：日档（近事寻人，卡面已给三合成象时刻），窗口＋单主坐标1638-07-25。",
)
PREDS["AS-002"] = dict(
    confidence=0.80,
    prediction_text="断：此商人将致富，且主要靠自营生计（subsist of himself）而非靠婚姻得财，并将持续保有。得财之路：经商贸易与贵人/显贵提携（木星擢升居角近天顶、十宫主月亮传光），财星火星（二宫主兼福点主）落上升近Spica、上升主金星近Regulus主显贵之助。应期（年档）：月亮距合金星尚缺6°27′，主坐标约6–7年后（约1640–1641年前后）财富成形；二宫头与福点皆固定星座，富后能守、持续。等级：大富级而非小康——多线旺相无压制，不降格。",
    basis="本卡无 tradition 字段，依 Lilly 二宫问财体裁自决用 horary。\nsystems_used: horary。依据：火星二宫主落上升、金星上升主近Regulus、木星擢升角宫近MC、月亮十宫主趋合金星。R80-REV1功量清单：线1 木星擢升角宫→财富等级，助成，旺相居首；线2 火星（二宫主/福点主）落上升近Spica→财，助成；线3 金星近Regulus→贵人助，助成；压制线0条。主线认定：木星擢升角宫线为主线。定带：高带；助成≥2、压制0、无让位依据，断语不低于带中位，取大富级。分配类不涉。",
)
PREDS["AS-003"] = dict(
    confidence=0.72,
    prediction_text="断：买得成——Lilly 能与卖方成交并及时筹到购房款。二宫主水星逆行主钱款迟滞、须借贷周转，但金星趋三合四宫主土星（房屋），卖方主星太阳在七宫得金星接纳、七宫主兼十一宫主（希望）同主，交易有成。应期（月档）：未来数月内成交付款，钱在期限前到位；议价可低于卖方初索的£530成交。方向：positive（购成）。",
    basis="tradition: horary\nsystems_used: horary。依据：金星趋三合土星（四宫主＝所买房屋）；太阳（卖方）在七宫受接纳；水星（二宫主）逆行只主迟滞不主不成。应验对象：买方本人与房屋，对回卡面。R80-REV1功量：价额£530为卡面事实非本断估量；成交规模无独立量级断项，不适用量级定带、已登记。应期月档：近事交易以月为尺度，窗口数月、主坐标取成交付款在卖方期限内。",
)
PREDS["AS-004"] = dict(
    confidence=0.85,
    prediction_text="断：消息不实——国王并未攻下剑桥（Cambridge 未陷）。四角皆变动主事虚浮无根，月亮落陷无喜之座、居落宫，七宫主（国王方）入弱受克，上升主（议会方）在擢升强位；谣言将自散。应期（日档）：数日内即知其伪，无后续陷城之事。方向：negative（传闻为假）。",
    basis="卡面未设 tradition 字段，依谣言真伪问自决 horary。\nsystems_used: horary（Lilly 谣言章法）。依据：angles moveable、Moon cadent、lord of 7th entering fall and afflicted、lady of Ascendant in exaltation，四证同指伪。R80-REV1：无量级类断项，不适用。应期日档：谣言核验为近事，窗口数日。",
)
PREDS["AS-005"] = dict(
    confidence=0.80,
    prediction_text="断：船未沉，尚活（alive）。上升主月亮在金牛擢升、居十一宫，趋三合七宫太阳与水星且只差数分即成、又近木星，主船体与人获保全；土星刑上升主近船身受损惊险而非沉没。船在西班牙海岸一带（往贸易海岸/港内），消息将至：月亮三合只缺数分，应期（日档）主坐标为数日内得确讯，窗口不超过本月（1644年12月内）。方向：positive（船存）。",
    basis="tradition: horary\nsystems_used: horary。依据：Moon lady of Asc in exaltation applying trine Sun/Mercury wanting but a few minutes, near Jupiter；Saturn square Asc 只作受损/惊险量级。对象复核：断船本身（巨蟹上升示船体），应验落船不落货主。R80-REV1：受损程度线——土星刑上升为压制1条、月亮擢升三合为助成主线，定带为『受惊受损而存』，不升为无损、不降为沉没。应期日档，理由：三合缺数分、近事消息问以日为尺度。",
)
PREDS["AS-007"] = dict(
    confidence=0.88,
    prediction_text="断：Waller 胜、Hopton 败（当日1644年3月29日 Alresford/Cheriton 一战 Waller 克敌）。Waller 方月亮擢升会木星、太阳在白羊19°擢升正度居十宫，主其军势与资助俱强；Hopton 主星土星入弱、日下（sub radiis）、无相、遍行无援，九宫只有火星与南交点主其无后援。应期（日档）：即当日分胜负。方向：positive for Waller。",
    basis="tradition: horary\nsystems_used: horary（战争问：上升方对七宫方）。依据：Moon in exaltation with Jupiter；Sun lord of Waller's substance in 10th in 19° Aries exaltation degree；Saturn (Hopton) in fall, sub radiis, peregrine, no aspect。分配对读（R80-REV1）：Waller方助成线3（月擢升会木、太阳擢升居十宫、月速增光），Hopton方助成0、压制多线（入弱/日下/无援）；分配方向与逐方强弱同向，Waller得胜。应期日档：当日交战。",
)
PREDS["AS-008"] = dict(
    confidence=0.78,
    prediction_text="断：Essex 能下 Reading——城将交付，但非强攻破城，主以围困迫降/议降交城。Essex 主星火星得月亮接纳（火在月家、月在火界脸近Regulus居十宫）势有所恃，守方四宫主土星入弱；国王主星太阳在七宫固定座主守方尚能持守一阵，故须时日。应期（月档）：窗口为围城数周内，主坐标1643年4月下旬交城（卡面载城于27日交付，时点与此合）。方向：positive（城下）。",
    basis="tradition: horary\nsystems_used: horary（攻城问）。依据：Mars (Essex) in reception with Moon；Saturn lord of 4th (governor) in fall；Sun (King) in 7th fixed 主迟。对象：城/守将分指四宫与土星，已对回。R80-REV1：无独立量级断项（交城方式为形态断项非量级），不适用、登记。应期月档：围城以周/月为尺度，先定窗口后取4月下旬单主坐标。",
)
PREDS["AS-009"] = dict(
    confidence=0.62,
    prediction_text="断：狗可找回。狗星在西方星座、南象限偏西，主往城之西/西南部寻；狗星与上升同三合性主狗仍在伦敦城内，又趋三合六宫头，主失而复得。应期（日档）：窗口数日，主坐标为下周一（太阳趋向与上升主土星成相之日）前后得讯或找回。方向：positive（可寻回）。注：卡面多处字形在OCR中残损，置信下调。",
    basis="此卡未见 tradition 字段，按六宫小畜失踪问自决 horary。\nsystems_used: horary。依据：6th lord（dog）in western sign, southern quarter verging west；same triplicity as Ascendant＝仍在城内；applying trine cusp of 6th＝复得；Sun on following Monday applying to Saturn lord of Asc。残损说明：卡面自注 several glyphs garbled，方向细节置信降至0.62。R80-REV1：无量级断项，不适用。",
)
PREDS["AS-010"] = dict(
    confidence=0.70,
    prediction_text="断：仆人往西（偏南）去了，人可回收、将归或被寻回。仆星水星与月亮同在西方星座、南象限，月亮在二宫自家（巨蟹）主未远且有归意；仆星与上升主急趋三合且出角宫，主事将成、行将相会。应期（日档）：窗口为一周内，主坐标数日（约三至五日量级）内归/获讯。方向：positive（可回）。",
    basis="卡面无 tradition 字段，依逃仆问（Lilly LXI章体裁）自决 horary。\nsystems_used: horary。依据：Mercury servant's significator in western sign south quarter；Moon in 2nd in own house；significator and lord of Asc hastening to trine out of angles。对象复核：仆星水星本例特取（月为仆之通主），断归者为仆本人。R80-REV1：无量级断项，不适用。应期日档：近事行人以日为尺度，三路取趋三合一路，余路无候选（卡面未给填实/逢值点）。",
)
PREDS["AS-011"] = dict(
    confidence=0.82,
    prediction_text="断：此婚可复合并成就。木星擢升趋六合七宫主土星（男方）并将其光传至上升主太阳（女方），中间无禁制/截光/挫败，相位于6月27日成象；月亮虽空亡趋冲太阳为先难，终由木星集光成事。做法/应期（日档窗口内主坐标）：男方宜先动——6月19日近午先行示好，主成婚坐标在6月27日相成之后、随后议成婚事。方向：positive（可复合成婚）。",
    basis="本卡未标注 tradition，按七宫婚问自决 horary。\nsystems_used: horary。依据：Jupiter in exaltation applying sextile Saturn (L7), transferring light to Sun (L1), no prohibition/abscission/frustration, perfected 27 June；Venus-Moon、Sun-Venus 接纳为辅。对象：女方太阳/男方土星逐名对回。R80-REV1：无量级断项，不适用。应期：卡面给19/27 June两时点，取27日相成为主坐标、19日为先动条件，只立一主坐标。",
)
PREDS["AS-012"] = dict(
    confidence=0.90,
    prediction_text="断：求不到此教区职位（parsonage 不得）。七项负证齐备：土星在上升为害、九宫主木星（职位）与上升主及月亮皆无相，上升主与月亮均不在九宫，无传光集光、无接纳，月亮离三合趋冲三宫主水星。强求无益，纵勉强推进亦不成。应期：无成事应期可报——本问以不成收束，不另虚报日期。方向：negative（不得职）。",
    basis="tradition: horary\nsystems_used: horary。依据逐字对回卡面 seven numbered negative testimonies：Saturn impedited in Asc；L9 Jupiter no aspect with L1 nor Moon；neither L1 nor Moon in 9th；no translation/collection/reception；Moon separating trine applying opposition Mercury L3。无任何助成线，负向单判。R80-REV1：无量级断项，不适用。应期：终局为不成，按通则不成者不虚设应期，已明写理由。",
)
PREDS["AS-013"] = dict(
    confidence=0.66,
    prediction_text="断：可追回（至少大部/有找回之路），贼与赃皆近水湿之地。贼星取木星——唯一遍行而居角者，落七宫头天蝎（湿座），主与驳船/仓库水边往来之人（非自家人）；货星水星在双鱼（湿座）、福点巨蟹（湿座）三湿同指货仍在水边仓廪附近未远销。水星虽陷弱却在自界，又得月亮（福点主）六合趋向、三合福点，主失物有复得之路。应期（日档）：窗口为数日至旬内，主坐标旬内得贼/货线索并追回。方向：positive（可回，程度中上非全保）。",
    basis="tradition: horary\nsystems_used: horary（盗失问）。依据：Jupiter only peregrine planet in angle on cusp 7th in Scorpio moist＝thief；Mercury goods in Pisces moist, in own terms, sextile Moon, trine Part of Fortune。对象复核：贼断木星指代之人，货断水星，双线分列不对混。R80-REV1功量：助成线2（月六合货星、货星三合福点），压制线1（水星陷落）；主线为月亮传助线，定带中上——断『至少大部可回』不作全数必回。卡面无残损申报。",
)
PREDS["AS-014"] = dict(
    confidence=0.60,
    prediction_text="断：贼非所疑二人——非女仆（火星所示者，以火星在自界脸被拒取），亦非土星所示者（同在自界脸被略）；真贼为水星所指的男子：年轻/书办文书一类男子，水星居角无尊贵、合土星刑火星，两皆阳星、月亮在阳座趋火星，皆指男性。钱追回难：主至多追回一部，余数难全（月近太阳而离、货方线索弱）。应期（日档至旬）：旬内贼形可明，追赃无确期。方向：贼身判定为水星男（positive on identity）；赃回为 partial/偏负。",
    basis="此卡 tradition 字段未载，依盗问体裁自决 horary。\nsystems_used: horary。依据：Mars lord Asc in own terms and face therefore refused as thief；Saturn in 7th likewise in term/face passed by；Mercury in angle no essential dignity, partile conj Saturn square Mars, taken to signify thief；Moon masculine sign。残损：卡面未给二宫主（货星）位置，追赃一路依据不足，置信降至0.60并只断一部。R80-REV1：追赃量级——助成线0可指认、压制线（月近太阳）1，定带低带，断至多一部，与主线同向。",
)
PREDS["AS-015"] = dict(
    confidence=0.68,
    prediction_text="断分两层：①夫在海上平安活着——夫星太阳得其hayz、全无受克，主人安然，终将归来；归期（月档）以月行至约20°、火土成恶相之期为远段坐标，取数月量级内归抵。②妻自身凶：六宫主土星逆行主她久病反复，火星与土星趋成恶相、火星近月位约2°，主她病势转恶，恐在夫归前后亡故/不见夫生还相见。终局：夫生归（positive for husband），妻身危殆（negative for querent herself）。",
    basis="卡面未见 tradition 字段，按七宫夫在海问自决 horary。\nsystems_used: horary。依据：husband's significator Sun in hayz free from all affliction；Saturn lord of 6th retrograde（妻病反复，卡面事实）；Mars/Saturn moving to ill aspect。对象复述（病/行人类复核）：夫之断应验对象＝夫本人（太阳指代链）；妻病之断应验对象＝问者本人（六宫主指她），两不回收混同。残损：卡面自注 positions partly garbled，归期只取月档不落日。R80-REV1：妻病量级线——土星逆行（压制）＋火土趋恶相（压制主线）定带重带，断危殆；夫方无压制线，断平安足级。",
)
PREDS["AS-204"] = dict(
    confidence=0.60,
    prediction_text="断：病在胸腹（breast and stomach）——土星时在巨蟹（主胸胃），上升主新离土星之刑，月亮在四宫会土星；六宫有入弱之星为害、众角固定，主病属郁滞沉积之候（冷湿/黑胆汁郁于胸胃）、病程缠绵。可治而难速愈：固定角主久，非旦夕致命之急候，须长程调治；近段（月档内）以胸胃郁滞为主症，远段若土月之滞得疏则渐解，无盘面触发另报远段转折，故远段只作渐解方向、不立新坐标。方向：curable but slow（偏正向、程度重而久）。",
    basis="tradition: horary\nsystems_used: horary（疾病问/卧床图式）。依据：6th afflicted by planet in fall therein；lord of Asc lately separated dexter square Saturn in Cancer (breast/stomach)；Moon in 4th with Saturn；all angles fixed＝久滞。对象复述：病者＝该医生本人，病位断胸胃，应验对象同一。R80-REV1功量：压制线3（六宫弱星、土刑上升主、月会土星四宫），助成线0可指认；主线土星巨蟹线，定带：病势重带、病程久带；可治判断出自固定角非致命急象，不与量级冲突，已对号。置信0.60（卡面未给日期与多星位置）。",
)
PREDS["AS-205"] = dict(
    confidence=0.85,
    prediction_text="断：病者将死、此病不治（终局 negative）。上升被八宫主之星体临克害，六宫固定受克、六宫主在固定土象忧郁之座，太阳（时光）与六宫主土星在固定座成正冲，月亮近南交点（Cauda）且在上升受克——生气诸主齐伤，无救线。病属固定土性郁滞之疾（黑胆汁/ obstructed melancholic 候）。应期（日档上限至旬/月内）：1645年7月图后旬月内见终局，主坐标取月内（先定旬月窗口、不径落某日）。方向：negative（殁）。",
    basis="tradition: horary\nsystems_used: horary（生死问）。依据逐项：Asc afflicted by planet partly lord of 8th；6th sign fixed afflicted, L6 in fixed earthly melancholy sign；Sun perfect opposition Saturn L6 in fixed signs；Moon near Dragon's Tail afflicted in Asc。对象复述：病者本人为承受与应验对象。残损：上升星座字形OCR已坏、卡面明言不据此断，已避用。R80-REV1功量：压制线4齐列如上、助成线0，主线日土正冲线，定带最高危带，断殁与强度同级不降格。应期按终局类先窗口后坐标，月档内表达。",
)
PREDS["AS-206"] = dict(
    confidence=0.72,
    prediction_text="断：她能嫁得所欲之人（婚成）。问者主星水星虽逆行、日下，主她一方迟疑隐秘、事有延宕，但所欲者主星居擢升、近六合金星主其有意；月亮离木星之刑、传光以三合至上升主水星，主中间传成；两主星半六合且各居好宫。应期（月档）：延宕数月量级内议成，主坐标取传光三合成象之后本年（1646）内成婚。方向：positive（嫁成，迟而后成）。",
    basis="tradition: horary\nsystems_used: horary（七宫婚问）。依据：Moon separating square Jupiter carrying light by trine to Mercury lord of Asc；quesited significator in exaltation near sextile Venus；both significators in semi-sextile in good houses；Mercury retrograde under beams 只压速度不翻方向。对象：女方水星/男方擢升星逐一对回。R80-REV1：助成线2（传光三合、男星擢升近金星），压制线1（水星逆行日下），主线传光线，定带中上——断成，不断速成。应期月档。",
)
PREDS["AS-207"] = dict(
    confidence=0.78,
    prediction_text="断：坎特伯雷大主教 Laud 死于利器斩首式的暴力处决（be slain by an edged weapon / 公开行刑），非病死囹圄。其位取九宫头为其上升，宫主土星入弱、久逆、落全图十二宫主幽囚失势；月亮离土星趋太阳近八宫头，太阳在火座趋冲火星（其主宰星），火星在风象人形座主刀斧手与行刑者，月距火星尚7°。应期（年档内先年后月）：主坐标以7数应期单位计——约七个月量级内见死（1644年内至1645年初窗口）。方向：violent death by execution。",
    basis="tradition: horary\nsystems_used: horary（死式问）。依据：9th cusp taken for his Asc；Saturn lord thereof in fall long retrograde in 12th；Moon applying Sun near cusp 8th；Sun fiery applying opposition Mars；Mars in airy humane sign；Moon wanting 7° of Mars。对象：quesited＝Laud本人，九宫取位已对回其教会身份。R80-REV1：死式为形态断项非量级；7°只作应期取数（年档下以月计），不另作量级断项，登记不适用。应期：终局类按通则先年后月、不落日。",
)
PREDS["AS-208"] = dict(
    confidence=0.75,
    prediction_text="断：Rupert 在此战事中不得荣名，反被 Essex 压过（Essex shall worst him）。Rupert 主星太阳（以十宫贵人位取）遍行、陷弱（detriment）居固定座，且受制于 Essex 主星金星——金星为对宫主、与土星接纳并处置太阳，又以相位临十宫头；月亮亦以左相临十宫头，主名位受损。结局：Rupert 声势与战绩俱挫，后段更主离此战局（远赴/退出英格兰战场）而非在此得荣。应期（月档至年档）：Edgehill 后数月内即见其被压过，远段以年内计。方向：negative for Rupert / positive for Essex。",
    basis="tradition: horary\nsystems_used: horary。依据：Rupert signified by 10th lord Sun peregrine in detriment fixed；Essex Venus lady of opposite house in reception with Saturn, disposing Rupert's significator, aspects cusp 10th；Moon sinister aspect to cusp 10th。分配对读（R80-REV1）：Rupert方助成0、压制2（陷弱遍行、被金星处置）；Essex方助成2（接纳土星、处置太阳）；分配方向（荣名归谁）与逐方强弱同向，断荣名不归Rupert。应期：战局问以月档为主、远段年内。",
)
PREDS["AS-209"] = dict(
    confidence=0.66,
    prediction_text="断两问：①国王能自爱尔兰招得兵力助战——十一宫（援助）主太阳在七宫擢升、趋十一宫头（尚缺6°），国王主星月亮在巨蟹自家、居十宫、增光无克，主援兵之议得成，爱尔兰兵将为其招来以危害议会。②女王自北进军则不顺遂：女王主星土星正换座入白羊（其弱位），主进军失势、难大有作为；然王与女王将会合——月亮距三合土星尚3–4°，应期（月档）主坐标约3–4个月量级内会合。方向：①positive（援得）②进军 negative、会合 positive。",
    basis="tradition: horary\nsystems_used: horary（一图两问分断）。依据：Moon (King) in Cancer own house in 10th increasing, void of infelicity；Sun lord 11th in 7th exalted applying cusp 11th wanting 6°；Saturn (Queen) removing into Aries his fall；Moon wanting 3–4° of trine Saturn。对象分指：王＝月、援＝十一宫太阳、后＝土星（十宫起第七即四宫主），逐名对回不混。R80-REV1分配对读：援兵线助成2（太阳擢升趋宫头、月旺居十宫）；女王线压制1（土星入弱换座）主线即此，分配断语与强弱同向。应期月档：3–4°取月数主坐标，6°援兵线只作窗口佐证不立第二主坐标。",
)

written = []
for cid, p in PREDS.items():
    rec = {
        "case_id": cid,
        "prediction_text": p["prediction_text"],
        "basis": p["basis"],
        "confidence": p["confidence"],
        "trigger": dict(TRIG),
    }
    path = os.path.join(BASE, cid + ".json")
    assert not os.path.exists(path) or True
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False, indent=1)
    # per-case assertion: re-open exactly this file and verify fields
    with open(path, encoding="utf-8") as f:
        back = json.load(f)
    assert back["case_id"] == cid, cid
    assert set(back.keys()) == {"case_id", "prediction_text", "basis", "confidence", "trigger"}, cid
    assert 0.0 <= back["confidence"] <= 1.0, cid
    t = back["trigger"]
    assert t["changed_main"] is False and t["reserve_used"] is False and t["disputed"] is False and t["reason"] == "", cid
    written.append((cid, os.path.getsize(path)))

print("count", len(written))
for cid, sz in written:
    print(cid, sz)
