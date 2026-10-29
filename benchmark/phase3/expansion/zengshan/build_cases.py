# -*- coding: utf-8 -*-
import json, re, io, sys

SRC = "/home/hatch/workspace/divination/sources/chinese/zengshan-buyi-wikisource.txt"
raw_lines = open(SRC, encoding="utf-8").read().splitlines()
def L(n):  # 1-indexed, stripped of <br>
    return raw_lines[n-1].replace("<br>", "").strip()
FULL = "\n".join(L(i+1) for i in range(len(raw_lines)))

def seg(n, a=None, b=None):
    """verbatim substring of line n between markers a (inclusive) and b (exclusive); whole line if none"""
    s = L(n)
    if a is not None:
        i = s.index(a); s = s[i:]
    if b is not None:
        j = s.index(b); s = s[:j]
    assert s and s in FULL, f"seg fail line {n}: {s[:40]}"
    return s

def chart(ranges):
    out = []
    for (a, b) in ranges:
        for n in range(a, b+1):
            s = L(n)
            if ("⚊" in s or "⚋" in s) and ("⚊" in s or "⚋" in s):
                out.append(s)
    return out

POS = ["上爻", "五爻", "四爻", "三爻", "二爻", "初爻"]
def moving(chart_lines, total_groups=1):
    """derive moving lines from first 6 chart rows (per group of 6)"""
    res = []
    groups = [chart_lines[i:i+6] for i in range(0, len(chart_lines), 6)]
    for gi, g in enumerate(groups):
        for i, row in enumerate(g):
            left = row.split("　　")[0]
            if "○" in left or "ㄨ" in left:
                name = re.split(r"[○ㄨ⚊⚋]", left)[0]
                sym = "○" if "○" in left else "ㄨ"
                res.append(f"{POS[i]}{name}{sym}動")
    return "、".join(res) if res else "無動爻（靜卦）"

ED = "維基文库本（錄入者整理本，未排版/未校對，見 pending 校勘說明）"
URL = "https://zh.wikisource.org/wiki/增刪卜易"
ERA = "清初（書成於清初，李文輝增刪）"
CAST = "六爻納甲（銅錢搖卦，原書只記月日與卦象）"

CASES = []
def C(**kw): CASES.append(kw)

# ---------- 卷之三 ----------
C(opener=2101, q="占終身財福", asked="戌月辛亥日", gua="水地比之風地觀", page="卷之三·終身財福章第三十七",
  chart=[(2103,2108)], stmt=(2110, "斷曰﹕", None), out=(2110, "丑年占卦﹐果至卯年立業成家", None),
  direction="positive", timing=True,
  setting="問終身財福；丑年占卦",
  assertions=["世爻雖空，月建合之、亥日生之","子水財爻動而生世","斷卯年一定成家"],
  comment="")
C(opener=2142, q="占財福", asked="寅月乙巳日", gua="地天泰（卦名原文未直書，據所附裝卦推得）", page="卷之三·終身財福章第三十七",
  chart=[(2144,2149)], stmt=(2151, "予曰﹕卦中官父兩旺", "伊曰﹕予知不能"), out=(2151, "後果於寅年醫好富翁﹐厚贈讀書。午年一榜", None),
  direction="positive", timing=True,
  setting="求測者在庠，因家寒意欲行醫，問財福如何；野鶴見卦中官父兩旺，反斷其將來成名",
  assertions=["卦中官父兩旺","斷寅年必有際遇、午未年定登金榜","應寅年者寅年而實空，應午年發者世爻值年月"],
  comment="卦名原文未直書，據裝卦六爻陰陽推得地天泰；原文未附變卦")
C(opener=2200, q="占財福", asked="午月丙子日", gua="地火明夷之雷火豐", page="卷之三·終身財福章第三十七",
  chart=[(2202,2207)], stmt=(2209, "世臨白虎化出旺財生世", "戌年占卦"), out=(2209, "值子年農生被蝗虫食盡﹐全家瘟疫﹐六畜亦瘟", None),
  direction="negative", timing=True,
  setting="問財福；世臨白虎化出旺財生世，其人目不識丁、農生度日",
  assertions=["世臨白虎，化出旺財生世","占時子日沖其午火，午火值月建可相敵","遇子年增其沖克，所以破敗"],
  comment="斷語與應驗同段敘述，節錄以占時沖克之理為斷、子年災變為驗")
C(opener=2215, q="占財福（再占問功名出仕）", asked="酉月壬辰日", gua="初占：雷風恆（靜卦）；再占：火風鼎之火天大有（原文作噬嗑變否卦，據裝卦訂正，見 notes）", page="卷之三·終身財福章第三十七",
  chart=[(2217,2222),(2228,2233)], stmt=(2235, "予曰﹕世爻未土之財變出申金之官", "果於卯年"), out=(2235, "果於卯年援例入臨﹐巳年初任兵馬卽加納縣令﹐未年再位江南", None),
  direction="positive", timing=True,
  setting="生意人占財福，野鶴以前卦財生官旺勸其問名，命再占合斷",
  assertions=["前卦財旺生官，世臨月建之官，辰日沖動戌土之財暗動生世","後卦世臨未土逢空，實空之年必出仕","斷以財變官、援例成名"],
  comment="再占卦名原文作「噬嗑變否卦」，與所附裝卦不合：裝卦上離下巽為鼎、世爻未土ㄨ變申金，上離下乾為大有，故卦名據裝卦訂正並在此注明，裝卦照原文錄入不改")
C(opener=2237, q="占終身財福", asked="巳月己丑日", gua="雷澤歸妹之地澤臨", page="卷之三·終身財福章第三十七",
  chart=[(2239,2244)], stmt=(2246, "予曰﹕世臨日建月建生身", "果於午年"), out=(2246, "果於午年保舉﹐𨿽非科甲﹐身爲科裏之官", None),
  direction="positive", timing=True,
  setting="問終身財福，自言功名之念已滅；野鶴見官父兩旺，反斷其顯貴中舉",
  assertions=["卦中財福不旺，而官父兩旺","世臨日建月建生身，必主顯貴中舉","斷巳午年富貴逼人"],
  comment="")
C(opener=2271, q="占終身財福", asked="卯月癸未日", gua="水火既濟之水山蹇（原文作革之家人，據裝卦訂正，見 notes）", page="卷之三·終身財福章第三十七",
  chart=[(2273,2278)], stmt=(2280, "應外卦世與日月同爲三合", "果至巳月"), out=(2280, "果至巳月而生惡瘡﹐卒於酉月", None),
  direction="negative", timing=True,
  setting="問終身財福；世與日月三合，外卦以為吉，野鶴獨斷世爻變鬼化回頭克，須防不測",
  assertions=["世與日月同為三合，外卦以為吉卦","不宜世爻變鬼又化回頭之克，上爻未土又克","斷今年五月沖開其合、或是酉月沖開卯木，須防不測"],
  comment="卦名原文作「革之家人」，與所附裝卦不合：裝卦本卦上坎下離為既濟、變卦上坎下艮為蹇，故卦名據裝卦訂正並在此注明，裝卦照原文錄入不改")
C(opener=2293, q="占終身功名有無", asked="辰月乙未日", gua="地火明夷之雷火豐", page="卷之三·終身功名有無章第三十八",
  chart=[(2295,2300)], stmt=(2302, "此卦丑土官星持世﹐化出午火﹐財旺生官", "黃堂古法"), out=(2302, "卯年占卦﹐巳年援例連連加納﹐官至府佐﹐未年出仕﹐戌年升任", None),
  direction="positive", timing=True,
  setting="求測者原是武蔭、已任裨官，因病告退，問將來還有功名否",
  assertions=["丑土官星持世，化出午火","財旺生官","古法以動而逢沖謂之散，此係未沖世爻之丑土，不見其散"],
  comment="")
C(opener=2306, q="占終身功名有無", asked="戌月戊辰日", gua="山風蠱（靜卦）", page="卷之三·終身功名有無章第三十八",
  chart=[(2308,2313)], stmt=(2315, "予曰﹕官星持世日月生﹐豈曰無官﹖", "後此人"), out=(2315, "後此人亦未食糧﹐竟隨營破寨﹐奮勇當先﹐主帥嘉之﹐卽以官。不出五載﹐建奇功﹐官至元戎將軍", None),
  direction="positive", timing=True,
  setting="問終身功名有無；日月作財生世，白虎臨金官持世，野鶴斷入武途可以立功",
  assertions=["日月作財生世，白虎臨金官持世","入文途必以援例，入武途可以立功","官星持世而得日月生，斷必有官"],
  comment="應驗時點為「不出五載」的 bounded 記載")
C(opener=2361, q="占壽元（原題未直書，據壽元章與斷語補）", asked="申月己卯日", gua="山澤損之地雷復", page="卷之三·壽元章第三十九",
  chart=[(2363,2368)], stmt=(2370, "予曰﹕若是父爻鬼動", "果終於未年七月"), out=(2370, "果終於未年七月", None),
  direction="negative", timing=True,
  setting="壽元章占例，問公之壽；卦中多鬼搖發",
  assertions=["若是父爻鬼動，壽則不久；今多鬼搖發，反為不礙","今年太歲在子，還享八年之福","斷至未年是其時：未年鬼多入墓，又是世逢年破"],
  comment="占題原文未直書，據本章（壽元章）與斷語「公之壽」補題並在此注明")
C(opener=2374, q="占壽", asked="辰月乙卯日", gua="風澤中孚之風天小畜（原文作中孚之暌，據裝卦訂正，見 notes）", page="卷之三·壽元章第三十九",
  chart=[(2376,2381)], stmt=(2383, "予曰﹕世爻未土﹐月拱日克", "後卒於戌年"), out=(2383, "後卒於戌年。應在巳火入墓之年", None),
  direction="negative", timing=True,
  setting="問壽元；世爻未土月拱日克，巳火動而生世",
  assertions=["世爻未土月拱日克，可以敵之","反不宜巳火動而生世","今歲太歲在申，斷恐亥年不利"],
  comment="斷語原指亥年不利，實際卒於戌年，原文自釋為應在巳火入墓之年——斷驗年份不合之例如實收錄，不迴避；卦名原文作「中孚之暌」，所附變卦裝卦上巽下乾為小畜，據裝卦訂正並注明")
C(opener=2387, q="占壽", asked="寅月己酉日（原文作「已酉日」，已、己形訛，照錄並注）", gua="山地剝之天地否（原文作剝之無妄，據裝卦訂正，見 notes）", page="卷之三·壽元章第三十九",
  chart=[(2389,2394)], stmt=(2396, "斷曰﹕世化申金回頭之生", "果卒於卯年"), out=(2396, "果卒於卯年﹐乃應戌土逢合之年而克世也", None),
  direction="negative", timing=True,
  setting="問壽元；世化申金回頭生，戌土未土動而克世",
  assertions=["世化申金回頭之生","不宜寅月沖破，又嫌戌土未土動而克而無生","斷須防卯歲"],
  comment="原文占日作「寅月已酉日」，「已」為「己」之形訛，asked_at 據干支常例作己酉並注明；卦名原文作「剝之無妄」，所附變卦裝卦上乾下坤為否，據裝卦訂正並注明")
C(opener=2403, q="占索債得否（兼問成非否）", asked="卯月丙寅日", gua="風雷益之風澤中孚", page="卷之三·趨避章第四十",
  chart=[(2405,2410)], stmt=(2412, "予見此卦﹐本日日辰動化進神克世", "彼必欲去"), out=(2412, "今早四隻大船橫渡﹐行至江心﹐忽起暴風﹐盡覆沒", None),
  direction="negative", timing=True,
  setting="漢口；求測者欲渡江索債，因屢取不得欲與之廝鬧，野鶴見卦斷辰時出空被克必有危亡之禍，苦留之過辰時",
  assertions=["本日日辰動化進神克世","世爻落空，辰時出空，被日月動爻之克","斷必有危亡之禍，留之過此時辰"],
  comment="趨避例：本人因被留而倖免，應驗為當日江船覆沒事件；裝卦初爻原文有缺字符號，照錄")
C(opener=2418, q="占夢（一身之血入河洗之）", asked="丑月戊子日", gua="風雷益之風澤中孚", page="卷之三·趨避章第四十",
  chart=[(2420,2425)], stmt=(2427, "予曰﹕血乃財也", "彼曰﹕年歲逼如何遠去﹖"), out=(2427, "不意果於正月亥日宿於妾房﹐被賊明火入室﹐席卷一空﹐身受木器所傷", None),
  direction="negative", timing=True,
  setting="求測者夢一身之血入河洗之，占其兆；野鶴斷破財兼防木害，勸出外避、勿貪幼婦，其人以年歲逼未能遠去",
  assertions=["血乃財也，洗去者破財之兆","元武發動化進神，克世克財不獨劫財，還防身遭木害","世與木爻皆在內卦，出外可避；巽為少女，勿貪幼婦"],
  comment="")
C(opener=2463, q="占防患", asked="巳月庚辰日（初占）；再占、三占均乙酉日（原文未重記月，承初占巳月）", gua="初占：澤天夬（靜卦）；再占：天風姤（原文作無妄，據裝卦訂正，見 notes）；三占：水澤節之水風井（原文作節之坎，據裝卦訂正，見 notes）", page="卷之三·趨避章第四十",
  chart=[(2465,2470),(2476,2481),(2487,2492)], stmt=(2494, "予曰甲寅日則事結矣", "果結於甲寅日"), out=(2494, "果結於甲寅日", None),
  direction="positive", timing=True,
  setting="占防患，前後三占：初占、再占世臨子孫值旬空，斷事不結、反覆；三占乃斷結期",
  assertions=["初占世臨子孫值旬空，事之不結，終日憂煎","再占世臨午火子孫又值旬空，事又反覆不結","三占世下巳火變寅木子孫又值旬空，幸卦遇六沖，斷甲寅日事結"],
  comment="三占合斷例，前兩占斷語見原文 2472、2483 行；再占卦名原文作「無妄」，裝卦上乾下巽為姤；三占變卦原文作「坎」，裝卦上坎下巽為井——均據裝卦訂正並注明，裝卦照原文錄入")
C(opener=2498, q="占流年", asked="寅月丁卯日", gua="風雷益之火澤睽", page="卷之三·趨避章第四十",
  chart=[(2500,2505)], stmt=(2507, "予曰﹕今秋必有險厄", "此人竟未出門"), out=(2507, "捱至七月初七﹐又得凶夢﹐初八卽往東行二十八里﹐地震房塌﹐人口被傷﹐獨伊得免", None),
  direction="mixed", timing=True,
  setting="問流年吉凶；野鶴斷今秋險厄、宜往外避",
  assertions=["今秋必有險厄：寅木動爻臨月建化進神克世","六七月衰墓之時，防土木之厄","宜往外方可避：目下去宜往西方，六七月去宜往東方"],
  comment="")
C(opener=2511, q="占僕人為禍否", asked="未月丙子日", gua="雷水解之雷地豫（原文作解之震，據裝卦訂正，見 notes）", page="卷之三·趨避章第四十",
  chart=[(2513,2518)], stmt=(2520, "予曰﹕不獨此人﹐還有附從者", "果依語而行"), out=(2520, "未去之婦而曰﹕彼二人原欲害主而逃﹐今因外出﹐不能相害", None),
  direction="negative", timing=True,
  setting="此公知僕役變心、意欲處治而尚無實迹，故占之；野鶴斷另有附從者，勸其出外自能免禍",
  assertions=["世臨辰土，兩重寅木傷之","斷不獨此人，還有附從者","未月乃木之墓、七月乃木之絕，此兩月乃露之月，宜出外免禍"],
  comment="卦名原文作「解之震」，所附變卦裝卦上震下坤為豫，據裝卦訂正並注明")
C(opener=2552, q="占定何罪", asked="未月癸亥日", gua="風澤中孚之水澤節（原文作中孚變臨，據裝卦訂正，見 notes）", page="卷之三·趨避章第四十",
  chart=[(2554,2559)], stmt=(2561, "斷曰﹕木鬼臨白虎﹐絞罪定矣", "果議絞罪"), out=(2561, "果議絞罪﹐後蒙駁番撥活罪", None),
  direction="mixed", timing=False,
  setting="問已定何罪；木鬼臨白虎，世臨月建",
  assertions=["木鬼臨白虎，絞罪定矣","幸世臨月建，木鬼雖動又被酉金回頭之克","外卦反覆，雖定絞罪，終有改刑"],
  comment="卦名原文作「中孚變臨」，所附變卦裝卦上坎下兌為節，據裝卦訂正並注明；原文「駁番」疑為「駁翻」之訛，照錄")
C(opener=2572, q="先占父壽、又占母壽", asked="丑月庚子日", gua="初占父壽：天風姤（靜卦）；又占母壽：雷天大壯之雷地豫（原文作大壯之升，據裝卦訂正，見 notes）", page="卷之三·父母壽元章第四十一",
  chart=[(2574,2579),(2583,2588)], stmt=(2590, "斷曰﹕前卦兩現父母", "若以古法"), out=(2590, "癸酉年占至乙巳年三十餘載﹐復遇其人而問曰﹕尊翁健否﹖答曰﹕甚健。問及堂﹐答曰﹕果終於子年", None),
  direction="mixed", timing=True,
  setting="同日分占父母壽元：先占父壽得姤，又占母壽得大壯之升；三十餘載後復遇其人核驗",
  assertions=["前卦兩現父母，取月建丑土為用神，旺於子日又與日合，斷父蒂固根深、大椿永茂","後卦午火父母動被日沖、初爻子水又動，午火有克無生","因初爻子水化出丑土貪合不來克火，斷防丙子年"],
  comment="母壽變卦原文作「升」，所附變卦裝卦上震下坤為豫，據裝卦訂正並注明；應驗中「子年」承斷語丙子年")
C(opener=2592, q="占父壽", asked="巳月乙酉日", gua="天雷無妄（原文作巽之姤，據裝卦訂正，見 notes）", page="卷之三·父母壽元章第四十一",
  chart=[(2594,2599)], stmt=(2601, "斷曰﹕亥水父臨月破", "果終於本年冬至日"), out=(2601, "果終於本年冬至日﹐應子日者沖去午火而未土以克亥水", None),
  direction="negative", timing=True,
  setting="問父親壽元；亥水父臨月破又被未土相傷",
  assertions=["亥水父臨月破，又被未土相傷","酉日沖動卯木克土，土旺木衰","斷不惟不許長年，且無長月"],
  comment="題面卦名原文作「巽之姤卦」，與所附裝卦全不合：裝卦本卦上乾下震為無妄且無動爻（妻財未土ㄨ在裝卦中為靜爻符號之誤植，變卦欄與本卦全同），據裝卦訂正並注明；此例裝卦與卦名矛盾較大，使用時請注意")
C(opener=2634, q="占弟兄和好否、得濟否", asked="申月丙辰日", gua="火天大有之乾為天", page="卷之三·兄弟章第四十二",
  chart=[(2636,2641)], stmt=(2643, "予曰﹕弟兄𨿽多﹐有一位屬猴者得濟", "後一年又登申榜"), out=(2643, "彼曰﹕果有金弟屬猴﹐克曾功一第﹐餘三人皆從別業﹐可見數之責驗如此﹐後一年又登申榜", None),
  direction="positive", timing=True,
  setting="問兄弟和好與得濟否；弟兄臨月建，未土爻動相生又化出兄爻",
  assertions=["弟兄臨月建，未土爻動以相生，又化出兄爻","神化於動，動而變出以臨月建，自是超群拔類","斷弟兄雖多，有一位屬猴者得濟"],
  comment="原文「克曾功一第」語意欠通，疑有訛字，照錄；「數之責驗」疑為「數之徵驗」，照錄")

# ---------- 卷之三（續） ----------
C(opener=2688, q="占夫妻偕老否", asked="巳月丁未日", gua="天雷無妄之風地觀", page="卷之三·夫婦章第四十三",
  chart=[(2690,2695)], stmt=(2697, "滿盤俱是財爻", "果此公美妾十餘"), out=(2697, "正夫人賢而無妒﹐夫妻同庚而生﹐妻活八旬有一﹐夫年八十二歲", None),
  direction="positive", timing=False,
  setting="問夫妻能否偕老；滿盤俱是財爻，世爻變出之未土與世相合為正妻",
  assertions=["世爻變出之未土與世爻相合，此未土之財乃正妻","未土臨日建遇月生扶","斷不獨偕老，且許賢比周南"],
  comment="")
C(opener=2721, q="占子嗣", asked="申月辛卯日", gua="地雷復（靜卦）", page="卷之三·子嗣章第四十四",
  chart=[(2723,2728)], stmt=(2730, "斷曰﹕身帶吉而子扶", "果於次年六月"), out=(2730, "果於次年六月父子相逢", None),
  direction="positive", timing=True,
  setting="求測者三十七歲有子、已十八，因亂失散，至今無所出，問子嗣；野鶴斷失散之子將歸",
  assertions=["身帶吉而子扶，日建沖動上爻子孫而生世","明現子從六爻動來生世，此子見歸","斷明歲申辰與酉金相合，定然得意而歸"],
  comment="本卦為靜卦，上爻子孫酉金為日建沖動（暗動），原文如此")
C(opener=2749, q="占子易養否", asked="亥月丙辰日", gua="天風姤之火山旅", page="卷之三·子嗣章第四十四",
  chart=[(2751,2756)], stmt=(2758, "亥水子孫臨月建五爻", "豈知子爻變鬼"), out=(2758, "死於次年五月", None),
  direction="negative", timing=True,
  setting="問子是否易養；亥水子孫臨月建、兄動相生，表面極旺，野鶴獨斷子爻變鬼主凶",
  assertions=["亥水子孫臨月建五爻，兄動以相生，旺莫旺於此","丙日以亥為貴人，貴莫貴於此","豈知子爻變鬼，斷主不保"],
  comment="")
C(opener=2782, q="占本經能發否（連占易經、書經）", asked="酉月丙子日", gua="初占：風雷益之風地觀；再占易經：天火同人（靜卦）；三占書經：雷火豐之離為火", page="卷之三·治經章第四十六",
  chart=[(2784,2789),(2793,2798),(2802,2807)], stmt=(2809, "旺父持世﹐官動生之", "果於子科中魁"), out=(2809, "果於子科中魁", None),
  direction="positive", timing=True,
  setting="問本經能否發達，初占斷宜改經；再占易經又斷宜再更；三占書經，斷此經相宜、下科高發",
  assertions=["初占旺官合世，嫌初爻文章動化回頭克，宜改經","再占易經旺官持世、父臨月破，宜再更之","三占書經旺父持世、官動生之，斷下科壬子沖去午火，管許高發"],
  comment="三占合斷例；前兩占斷語分見原文 2791、2800 行")
C(opener=2834, q="占子從師（從此師可否）", asked="寅月戊午日", gua="火山旅之離為火（卦名原文未直書，據所附裝卦推得）", page="卷之三·延師章第四十七",
  chart=[(2836,2841)], stmt=(2843, "子動化克﹐不宜從之", None), out=(2843, "後因師責﹐逃至橋頭﹐跌折右足", None),
  direction="negative", timing=False,
  setting="為子占從師可否；子孫動而化克，野鶴斷不宜從之，求測者不聽",
  assertions=["子孫辰土動而化父母卯木，子動化克","斷不宜從之"],
  comment="卦名原文未直書，據裝卦爻象推得火山旅之離為火，動爻為初爻子孫辰土")
C(opener=2947, q="占會試", asked="卯月甲申日", gua="艮為山之風雷益", page="卷之三·鄉試章第五十五",
  chart=[(2949,2954)], stmt=(2956, "寅木旺官持世", "果得及第"), out=(2956, "果得及第", None),
  direction="positive", timing=False,
  setting="問會試能否及第；寅木旺官持世，申日沖之為暗動，日辰會成財局生世",
  assertions=["寅木旺官持世，申日沖之暗動","日辰會成財局，不惟不克世爻，反來生世","斷一定高捷"],
  comment="")
C(opener=2970, q="占鄉試", asked="午月丙辰日", gua="初占：兌為澤（靜卦，六沖）；再占：地澤臨之地水師", page="卷之三·鄉試章第五十五",
  chart=[(2972,2977),(2983,2988)], stmt=(2990, "此卦官星持世", "果得成名"), out=(2990, "果得成名", None),
  direction="positive", timing=False,
  setting="問鄉試；初占得兌卦六沖，世父皆旺，野鶴不敢決之命再占，再占官星持世、父旺，與前卦相合乃許吉",
  assertions=["初占六沖，世父皆逢旺地，不敢決之，請再占","再占官星持世，初爻官生父旺，與前卦相合","許之吉兆"],
  comment="兩占合斷例；初占斷語分見原文 2979 行")
C(opener=3055, q="占得差否", asked="申月戊寅日", gua="澤天夬（靜卦）", page="卷之三·鄉試章第五十五（升選候補附）",
  chart=[(3057,3062)], stmt=(3064, "斷曰﹕子孫持世﹐此差不得", "中途而死者世爻空也"), out=(3064, "不出三日得差﹐行至中途而死", None),
  direction="negative", timing=True,
  setting="問能否得差；子孫持世且世爻旬空，初斷不得",
  assertions=["初斷子孫持世、世空，此差不得","三日之內得差者，子孫未出空也","中途而死者，世爻空也"],
  comment="本例初斷與結果表面相反，原文隨即自釋（子孫未出空故得差、世空故中途死），斷語與自釋一併節錄、如實收錄")
C(opener=3068, q="占升遷", asked="寅月乙未日", gua="水地比之風地觀", page="卷之三·鄉試章第五十五（升選候補附）",
  chart=[(3070,3075)], stmt=(3077, "斷曰﹕卯木旺官持世", "果得升於亥月"), out=(3077, "果得升於亥月", None),
  direction="positive", timing=True,
  setting="問升遷；卯木旺官持世，子水財動相生",
  assertions=["卯木旺官持世，子水財動相生","財爻墓於未日，幸世反得助，無妨","斷必得升"],
  comment="")
C(opener=3079, q="占何日補官", asked="戌月辛酉日", gua="水山蹇之水天需", page="卷之三·鄉試章第五十五（升選候補附）",
  chart=[(3083,3088)], stmt=(3090, "寅木財爻生助午火之鬼", "果得升於冬月"), out=(3090, "果得升於冬月。應冬月者﹐辰土化子水空亡﹐十一月則不空矣", None),
  direction="positive", timing=True,
  setting="問何日補官；寅木財爻生助午火官鬼克世，為助鬼傷身之象，幸辰土生申金、午火貪生忘克",
  assertions=["寅木財爻生助午火之鬼，火鬼克世，乃助鬼傷身","幸辰土生申金，午火貪生忘克","斷今年冬月必升"],
  comment="占題在原文 3079 行（又如戌月辛酉日占何日補官），卦名原文續記於 3081 行「得蹇之需」")
C(opener=3135, q="占在任平安否（流年）", asked="寅月壬午日", gua="山雷頤之火雷噬嗑", page="卷之三·在任吉凶章第五十七",
  chart=[(3137,3142)], stmt=(3144, "予曰﹕財休囚得午火生之﹐自身不妨﹐須防孝服", "果於八月丁艱"), out=(3144, "果於八月丁艱", None),
  direction="negative", timing=True,
  setting="在任者占流年平安，自憂世爻變鬼；野鶴斷自身不妨、須防孝服",
  assertions=["財休囚得午火（日建）生之，自身不妨","午日沖動子水，父母被戌土財爻克，世化官空","斷八九月必見孝服"],
  comment="原文占題作「如寅月壬午占在任平安否」，「壬午」後缺「日」字，asked_at 補足並在此注明")
C(opener=3230, q="出具文伸枉保全功名", asked="丑月丙辰日", gua="雷天大壯之澤天夬", page="卷之三·面聖上書章第六十二",
  chart=[(3232,3237)], stmt=(3239, "父母持世﹐月建文書生旺﹐但不宜子動傷官", "果蒙上臺題保"), out=(3239, "果蒙上臺題保﹐未勞準行﹐八月削職", None),
  direction="negative", timing=True,
  setting="出具文書伸冤以保全功名；父母持世、月建文書生旺，唯子孫申金動而傷官",
  assertions=["父母持世，月建文書生旺","不宜子動傷官","斷七八月申金得令之秋，功名壞矣"],
  comment="")
C(opener=3313, q="占可能鼎甲否（會試後指占）", asked="卯月甲申日", gua="水澤節之山水蹇", page="卷之三·功名到何品級章第六十六",
  chart=[(3315,3320)], stmt=(3322, "斷曰﹕古以蹇爲不吉﹐予重用神", "公曰﹕此數暗含我機"), out=(3322, "至甲辰科殿試﹐果得首唱傳臚", None),
  direction="positive", timing=True,
  setting="占者先經占會試許之必中，又問可能鼎甲否，指其事而占；野鶴斷中鼎甲但非今科",
  assertions=["世臨巳火，卯月生之，申日合青龍持世","世爻變出辰土之官","斷乃辰年之鼎甲，非今科之鼎甲"],
  comment="本例緊承同章前例之後，原文以「卯月甲申日得節之蹇」起例，占者身份原文未明言，setting 據上下文記為會試占者指占鼎甲")
C(opener=3328, q="占父何時起用", asked="卯月壬辰日", gua="風水渙之澤天夬", page="卷之三·子占父功名章第六十七",
  chart=[(3330,3335)], stmt=(3337, "內卦寅木父母旺而化出子水之官", "後終於未年"), out=(3337, "果應於寅年", None),
  direction="positive", timing=True,
  setting="子占父何時起用；內卦寅木父母旺而化出子水之官",
  assertions=["內卦寅木父母旺而化出子水之官","許寅年仍以原品起用","上爻卯木父動化未，謂之空墓以待死，終於實墓之年"],
  comment="應驗主句為「果應於寅年」；同段另記「後終於未年」為次級應驗，一併見於原文 3337 行")
C(opener=3374, q="占借貸", asked="未月丁卯日", gua="火地晉（靜卦）", page="卷之三·求財章第六十八",
  chart=[(3376,3381)], stmt=(3383, "斷曰﹕𨿽則兄爻持世無財", "果得財"), out=(3383, "果得財﹐應辰日者﹐世動逢合之日也", None),
  direction="positive", timing=True,
  setting="問借貸能否得財；兄爻持世、卦中無財，唯卯日即是財星、應爻未土旺而生世",
  assertions=["兄爻持世無財，但喜卯日即是財星","應爻未土旺而生世","斷明日必獲"],
  comment="本例在求財章內，來人所問為借貸，question 據原文作占借貸")
C(opener=3385, q="占求財", asked="巳月丁巳日", gua="水火既濟之水風渙", page="卷之三·求財章第六十八",
  chart=[(3387,3392)], stmt=(3394, "斷曰﹕若逢久遠之財有否﹐則無財", "果於次日送來"), out=(3394, "果於次日送來", None),
  direction="positive", timing=True,
  setting="問求財；野鶴分斷久遠之財無、目下之財明日必得",
  assertions=["兄臨世爻日破月破，不克變出之財","日月俱作財來沖世，只因應爻逢空","斷明日戊午沖實，定送財來"],
  comment="")

# ---------- 卷之四 ----------
C(opener=3426, q="占出行謁見貴人", asked="申月丁卯日", gua="天火同人（靜卦）", page="卷之四·謁貴求財章第六十九",
  chart=[(3428,3433)], stmt=(3435, "斷曰﹕官星持世而空﹐出亥日得見", "果於出空之日見官"), out=(3435, "果於出空之日見官﹐財利得意", None),
  direction="positive", timing=True,
  setting="出行謁見貴人，問能否得見；官星持世而旬空",
  assertions=["官星持世而空","斷出亥日（出空之日）得見","官府財利如心，月建財爻生世之故"],
  comment="")
C(opener=3498, q="占何時得價（囤貨）", asked="子月己丑日", gua="雷澤歸妹之澤為兌", page="卷之四·囤貨賣貨章第七十三",
  chart=[(3500,3505)], stmt=(3507, "斷曰﹕卯木財爻子月生之", "果於正月勃然大長"), out=(3507, "果於正月勃然大長﹐此乃財爻被克待沖去克神之月", None),
  direction="positive", timing=True,
  setting="囤貨問何時得價；卯木財爻得子月生而有根，目下被申金動而克制",
  assertions=["卯木財爻子月生之，財有根蒂","目下不得價者，被申金動而克制","斷待寅月沖去申金，其價必漲"],
  comment="")
C(opener=3511, q="占脫貨於何時", asked="寅月己酉日", gua="山火賁（靜卦）", page="卷之四·囤貨賣貨章第七十三",
  chart=[(3513,3518)], stmt=(3520, "斷曰﹕亥水財爻﹐酉日生之﹐寅月合之﹐目下正及時也", "果去"), out=(3520, "果去﹐不數日﹐得價出脫", None),
  direction="positive", timing=True,
  setting="問貨於何時可脫；亥水財爻得酉日生、寅月合，求測者聞某處得價欲移貨往賣，野鶴勸速行",
  assertions=["亥水財爻酉日生之、寅月合之，目下正及時","世爻暗動，身動方可出脫","斷速宜行之"],
  comment="")
C(opener=3574, q="占借貸", asked="未月丁卯日", gua="兌為澤之震為雷", page="卷之四·借貸章第七十七",
  chart=[(3576,3581)], stmt=(3583, "斷曰﹕兌卦屬金變震卦屬木", "果於辰日"), out=(3583, "果於辰日", None),
  direction="positive", timing=True,
  setting="問借貸；卯木財爻化退、酉金兄動亦化退，幸財臨日辰旺而不退",
  assertions=["金克木為財，卯木財爻化退神、酉金兄動亦化退神","幸得財臨日辰，旺而不退","斷明日辰日合住酉爻必得"],
  comment="原文應驗句止於「果於辰日」，句似未完，照錄不補")
C(opener=3610, q="占鵪鶉（鬥鵪鶉勝負）", asked="巳月戊申日", gua="風山漸之巽為風", page="卷之四·博戲章第八十",
  chart=[(3612,3617)], stmt=(3619, "斷曰﹕子孫持世以臨日辰", "果於早勝"), out=(3619, "果於早勝﹐午時又大敗破財", None),
  direction="mixed", timing=True,
  setting="以鵪鶉相鬥占勝負；子孫持世臨日辰，父爻動而化亥水制之，唯亥水月破",
  assertions=["子孫持世以臨日辰，父爻雖動，亥水制之","獨不宜亥為月破，雖可制火","斷今日巳午時切不可斗：巳午時午火父母得令必克子孫"],
  comment="")
C(opener=3642, q="自占婚", asked="子月癸酉日", gua="雷風恆之火風鼎", page="卷之四·婚姻章第八十二",
  chart=[(3644,3649)], stmt=(3651, "斷曰﹕酉官持世", "果於次日巳時允婚"), out=(3651, "果於次日巳時允婚﹐夫妻白頭相守﹐兒女成行", None),
  direction="positive", timing=True,
  setting="男子自占婚；酉官持世，戌土財爻動而生世，世應相生",
  assertions=["酉官持世，戌土財爻動而生世，又得世應相生","戌土雖值旬空，動不為空","斷明日出空之日求之必允"],
  comment="")
C(opener=3653, q="女家代占婚", asked="寅月丙午日", gua="地澤臨之水火既濟", page="卷之四·婚姻章第八十二",
  chart=[(3655,3660)], stmt=(3662, "卯木旺官持世﹐其婚必成", "後果聘定於四月"), out=(3662, "後果聘定於四月﹐未及成婚被賊兵劫去﹐應巳月者亥水逢月破也", None),
  direction="negative", timing=True,
  setting="女家代占男；卯木旺官持世主婚成，然財爻被回頭克又逢丑土之克，不能生官",
  assertions=["女家占男以官為用，卯木旺官持世，其婚必成","財被回頭克又逢丑土之克，不能生卯木之官","斷男女不能相合相生，婚雖成終有他變"],
  comment="")
C(opener=3680, q="占夫妻不和將來如何", asked="巳月己亥日", gua="水天需之澤風大過", page="卷之四·婚姻章第八十二",
  chart=[(3682,3687)], stmt=(3689, "斷曰﹕女占夫﹐不宜子孫持世", "果於次年寅月休妻"), out=(3689, "果於次年寅月休妻﹐此人六月再取彼婦", None),
  direction="negative", timing=True,
  setting="女占夫、夫妻不和，問將來如何；子孫持世為克夫之象，應爻為夫而逢子丑作合",
  assertions=["女占夫不宜子孫持世，乃克夫之象，幸寅木子水相生不能傷之，所以不和","應爻為夫，應逢子丑作合，夫已有外遇，水木相生兩人情密","斷兩人不是姻緣，雖不能死別，必有生離"],
  comment="")
C(opener=3728, q="占何命者有子（因有妾多，問何命之女有子）", asked="申月丁丑日", gua="澤火革之澤天夬", page="卷之四·此婚子嗣有無章第八十三",
  chart=[(3730,3735)], stmt=(3737, "斷曰﹕卯木子孫絕於申月", "公曰﹕不孝有三"), out=(3737, "嗣後施濟貧寒﹐全人夫婦﹐修橋砌路﹐施藥施棺﹐連生二子", None),
  direction="mixed", timing=False,
  setting="求測者妾多無子，問何命之女能有子；野鶴斷其命元無子、與女命無干，勸多積陰德，兼看八字同斷無子",
  assertions=["卯木子孫絕於申月，鬼變子孫又逢月破","斷公命無子，與女命何干","八字純陽包陰、兵權顯赫，亦主無子；勸多積陰德以培之"],
  comment="斷驗關係特殊：大師斷無子，求測者嗣後行善積德而連生二子，原文以陰功釋其轉變——斷語、勸善與結果俱為原文自載，如實收錄並標 mixed")
C(opener=3765, q="占孕男女（兼問妻孕平安）", asked="辰月戊辰日", gua="雷山小過之雷地豫", page="卷之四·胎孕章第八十七",
  chart=[(3767,3772)], stmt=(3774, "兄爻𨿽動﹐不克變出之財爻", "果於壬申日生女"), out=(3774, "果於壬申日生女﹐產母平安", None),
  direction="positive", timing=True,
  setting="問妻孕平安兼孕之男女；野鶴先正分占之法，幸此卦兩事俱現",
  assertions=["兄爻雖動，不克變出之財爻，艸正坐艸無虞（產母平安）","卦中陽動變陰，必然主女","神兆機於動，先重動爻，不以小過陰包陽斷男"],
  comment="原文「艸正坐艸」語意欠通，疑有訛字，照錄")
C(opener=3857, q="占僕人何日回", asked="亥月甲子日", gua="澤火革之澤天夬", page="卷之四·行人章第九十四",
  chart=[(3859,3864)], stmt=(3866, "世空者速至﹐此人來矣﹐巳日必到", None), out=(3866, "果於巳日到", None),
  direction="positive", timing=True,
  setting="問僕人何日回；此卦若問在外吉凶主不歸，今問歸期則以世空速至斷之",
  assertions=["問歸期不以用神有病斷","世空者速至","斷巳日必到，應巳日者沖空之日，巳火又是財爻"],
  comment="斷語全句見原文 3866 行前段「此卦若問僕人在外之吉凶者…巳火又是財爻」，節錄取其要句")
C(opener=3868, q="占伯何日來", asked="未月戊戌日", gua="水雷屯之澤雷隨", page="卷之四·行人章第九十四",
  chart=[(3870,3875)], stmt=(3876, "父母爲用神﹐克世者速至﹐七月必到", "應亥月者父母化出之爻也"), out=(3876, "後於亥月方到", None),
  direction="positive", timing=True,
  setting="問伯父何日來；父母為用神而克世，初斷七月必到",
  assertions=["父母為用神，克世者速至","初斷七月必到","實際亥月方到，原文自釋應亥月者父母化出之爻"],
  comment="斷語原指七月必到，實際亥月方到——斷驗月份不合之例如實收錄，原文自釋附於斷語節錄")
C(opener=3878, q="占父遠去何日回", asked="丑月庚午日", gua="天澤履（靜卦）", page="卷之四·行人章第九十四",
  chart=[(3880,3885)], stmt=(3887, "斷曰﹕今日乃是午日﹐午火父爻克世爻﹐今日必到", None), out=(3887, "果於申時到", None),
  direction="positive", timing=True,
  setting="問遠行之父何日回；占日即午日，午火父爻克世",
  assertions=["今日乃是午日，午火父爻克世爻","用神克世，斷今日必到"],
  comment="")
C(opener=3900, q="占夫在外還往他省去否（兼問何日到）", asked="亥月甲子日", gua="雷天大壯之澤風大過", page="卷之四·行人章第九十四",
  chart=[(3902,3907)], stmt=(3909, "斷曰﹕妻占夫官爲用神", "或曰﹕用爻有病"), out=(3909, "果於巳日到", None),
  direction="positive", timing=True,
  setting="妻占夫在外是否還往他省；官為用神被申金動克，日月生扶夫爻",
  assertions=["妻占夫官為用神，申動克之，寅木夫爻受克不往他處去","日月生扶，夫生世爻必有歸志，不日必回","斷巳日必到，應巳日者合住申金之日"],
  comment="")
C(opener=3958, q="占子近病", asked="申月庚寅日", gua="雷風恆之雷水解", page="卷之四·疾病章第九十九",
  chart=[(3960,3965)], stmt=(3967, "斷曰﹕鬼變子孫﹐夭折之兆", "辰年占卦至午年出花而死"), out=(3967, "果在出空之日而愈", None),
  direction="mixed", timing=True,
  setting="問子近病；官鬼酉金動而變子孫午火，本為夭折之兆，幸子孫值旬空",
  assertions=["鬼變子孫，夭折之兆","幸得子孫值旬空，近病即愈","斷恐其難過午年"],
  comment="應驗分兩段：近病果在出空之日而愈（主應驗）；原文同句續記「辰年占卦至午年出花而死」為遠期應驗，一併見於原文 3967 行")
C(opener=3975, q="占子病", asked="申月壬子日", gua="天山遯（靜卦）", page="卷之四·疾病章第九十九",
  chart=[(3977,3982)], stmt=(3984, "斷曰﹕令郎今日卽愈", "果於本日愈"), out=(3984, "果於本日愈", None),
  direction="positive", timing=True,
  setting="問子病；官鬼午火持世為憂疑之象，子日沖去憂心",
  assertions=["官鬼持世，憂也","今日子日沖去憂心","斷今日即愈"],
  comment="")
C(opener=4119, q="子占父病喫人參好否", asked="寅月丁卯日", gua="澤地萃之澤山咸（原文作萃之否，據裝卦爻象核算變卦為咸，見 notes）", page="卷之四·醫卜往治章第一百零四",
  chart=[(4121,4126)], stmt=(4128, "予非此斷", "果於雞鳴蘇醒"), out=(4128, "果於雞鳴蘇醒﹐次日不藥而愈", None),
  direction="positive", timing=True,
  setting="府中老先生仆倒狂言不知人事，醫者議用人參提氣，又慮痰上難治，子占父病問喫人參好否",
  assertions=["父爻未土動化戌土，父戌旬空","斷人參莫用、藥亦莫服","斷明日辰日沖空即愈"],
  comment="卦名原文作「萃之否卦」：本卦澤地萃與裝卦合；變卦裝卦上兌下艮為咸，與原文卦名「否」不合——此為全卷覆核中唯一卦名與裝卦不合之例，卦名並記兩說，裝卦照原文錄入不改")
C(opener=4143, q="因楊梅瘡占醫好否（此醫可用否）", asked="申月癸卯日", gua="天澤履之天地否", page="卷之四·醫卜往治章第一百零四",
  chart=[(4145,4150)], stmt=(4152, "斷曰﹕此醫不可用之", "不聽"), out=(4152, "卯辰日服藥還保平常﹐巳日忽然變癥", "其病如常"),
  direction="negative", timing=True,
  setting="患楊梅瘡，問某醫可用否；子孫申金持世而應爻卯木、巳火克世，求測者不聽仍延此醫",
  assertions=["子孫持世，應為醫人","應爻與巳火克申金，又有卯木生火，世爻雖旺","斷巳日一定添災"],
  comment="應驗分兩段：巳日變癥、服解藥至申日其病如常，俱見原文 4152 行")
C(opener=4327, q="占衙宇後溝從後流宜否、修溝之後何如", asked="戌月己亥日", gua="初占：火風鼎（靜卦）；再占修溝後：火雷噬嗑之天雷無妄", page="卷之四·占衙宇章第一百十六",
  chart=[(4329,4334),(4340,4345)], stmt=(4347, "斷曰﹕未土財化申金官﹐未年一定高升", "應申年者"), out=(4347, "後於申年升任", None),
  direction="positive", timing=True,
  setting="一官連任不得升遷疑衙宇不利，諸所疑俱占不現爻，又卜後溝從後流宜否；初占斷即此處不宜、宜改東流，再占修溝後功名",
  assertions=["初占斷即此處（後溝）不宜，宜改往東流，虎鬼持世之故","再占未土財化申金官","斷未年一定高升"],
  comment="初占應驗「後開溝見許多屍體白骨」見原文 4336 行；再占斷未年高升、實際申年升任，原文自釋「應申年者，值官之年也」——斷驗年份不合之例如實收錄")
C(opener=4372, q="占地（此地可用否）", asked="寅月戊午日", gua="山雷頤之天雷無妄", page="卷之四·尋地章第一百十九",
  chart=[(4374,4379)], stmt=(4381, "斷曰﹕世爻戌土", "後竟葬之"), out=(4381, "後竟葬之﹐辰年下葬﹐酉年孫中亞魁﹐及至子年﹐次孫又登鄕榜", None),
  direction="positive", timing=True,
  setting="占墳地可用否；世爻戌土春休囚，化出午火子孫回頭生世，日月世爻成三合",
  assertions=["世爻戌土春天休囚，化出午火子孫回頭生世","日月世爻成三合，青龍戲水以化長生，水源極遠","斷死者安而生者樂、子孫昌盛"],
  comment="")
C(opener=4395, q="占地（此地可用否）", asked="卯月戊子日", gua="巽為風之地風升", page="卷之四·尋地章第一百十九",
  chart=[(4397,4402)], stmt=(4404, "世爲穴﹐世臨月建﹐日辰生之﹐是爲吉也", "後竟葬之"), out=(4404, "四年之內﹐二男一女﹐相繼而亡﹐自身又得半身不遂之疾", None),
  direction="negative", timing=True,
  setting="占墳地可用否；世臨月建日辰生本為吉，唯外卦反吟、世與子孫俱受沖克，野鶴斷不宜用，地主已買成仍葬之",
  assertions=["世為穴，世臨月建、日辰生之，是為吉也","但不宜外卦反吟，世被酉金沖克、子孫被亥水沖克","斷不宜用之"],
  comment="")
C(opener=4458, q="占穴（點穴）", asked="未月乙巳日", gua="雷天大壯（靜卦）", page="卷之四·點穴章第一百二十四",
  chart=[(4460,4465)], stmt=(4467, "予曰﹕世在四爻﹐穴在中段", "東家尙疑"), out=(4467, "此公次年開府﹐兩公郎五年之內俱登甲榜", None),
  direction="positive", timing=True,
  setting="此地屢掘逢石無處導穴，央野鶴到冢下點穴；世在四爻斷穴在中段、午火持世斷枯焦紅花處，設灑錢禱告之法驗之",
  assertions=["世在四爻，穴在中段","午火持世，穴在草木枯焦、有野花紅色之處","斷掘之必逢土穴"],
  comment="原文同段另記即時應驗「果得原錢於紅花之下，掘之周圍僅有丈予，皆泥土也，予皆石塊」（「丈予」「予皆」疑為「丈餘」「餘皆」之訛，照錄），outcome 取其遠期應驗句")
C(opener=4502, q="占以父柩附葬祖塋", asked="子月丙申日", gua="地雷復之坤為地", page="卷之四·新亡附葬祖塋章第一百三十",
  chart=[(4504,4509)], stmt=(4511, "斷曰﹕世爻被克﹐不宜附葬之", "後仍附葬"), out=(4511, "數月後", None),
  direction="mixed", timing=True,
  setting="問以父柩附葬祖塋可否；世爻子水被克，斷不宜附葬，求測者仍附葬之",
  assertions=["世爻被克，斷不宜附葬","後仍附葬，腰疼欲死，命道安土神則吉，果於安墳而愈","化六沖不久之象，斷目下雖不遷改、終有遷改"],
  comment="原文應驗段「數月後不斷曰﹕腰疼欲死」語意欠通，疑有訛字，照錄；outcome 為原文 4511 行應驗全段")

# ---------- patches：卦名一律以原文題面為準（爻象程序覆核全合），撤回手算改名 ----------
PATCH = {
 2142: dict(gua="雷天大壯（靜卦；卦名原文未直書，據所附裝卦推得）", comment="卦名原文未直書，據裝卦六爻陰陽推得雷天大壯（靜卦）"),
 2215: dict(gua="初占：雷風恆（靜卦）；再占：火雷噬嗑之天地否", comment=""),
 2271: dict(gua="澤火革之風火家人", comment=""),
 2374: dict(gua="風澤中孚之火澤睽", comment="斷語原指亥年不利，實際卒於戌年，原文自釋為應在巳火入墓之年——斷驗年份不合之例如實收錄，不迴避"),
 2387: dict(gua="山地剝之天雷無妄", asked="寅月己酉日", comment="原文占日作「寅月已酉日」，「已」為「己」之形訛，asked_at 據干支常例作己酉，原文占題照錄於此注"),
 2463: dict(gua="初占：澤天夬（靜卦）；再占：天雷無妄（靜卦）；三占：水澤節之坎為水", comment="三占合斷例，前兩占斷語見原文 2472、2483 行；再占、三占原文只記乙酉日，月份承初占巳月"),
 2511: dict(gua="雷水解之震為雷", comment=""),
 2552: dict(gua="風澤中孚之地澤臨", comment="原文「駁番」疑為「駁翻」之訛，照錄"),
 2572: dict(gua="初占父壽：天風姤（靜卦）；又占母壽：雷天大壯之地風升", comment="應驗中「子年」承斷語丙子年"),
 2592: dict(gua="巽為風之天風姤", comment=""),
}
for c in CASES:
    if c["opener"] in PATCH:
        c.update(PATCH[c["opener"]])

# ---------- assembly ----------
def moving2(chart_lines):
    res = []
    groups = [chart_lines[i:i+6] for i in range(0, len(chart_lines), 6)]
    for g in groups:
        for i, row in enumerate(g):
            left = [p for p in re.split(r"　+", row) if p][0]
            if "○" in left or "ㄨ" in left:
                name = re.split(r"[○ㄨ⚊⚋]", left)[0]
                sym = "○" if "○" in left else "ㄨ"
                res.append(f"{POS[i]}{name}{sym}動")
    return "、".join(res) if res else "無動爻（靜卦）"

inputs, answers, grading_rows = [], [], []
for idx, c in enumerate(CASES):
    cid = f"LY-{201+idx}"
    ch = chart(c["chart"])
    assert len(ch) % 6 == 0 and len(ch) >= 6, (cid, len(ch))
    sn, sa, sb = c["stmt"]
    excerpt = seg(sn, sa, sb)
    on, oa, ob = c["out"]
    if ob:
        desc = seg(on, oa, ob) + ob
    else:
        desc = seg(on, oa, None)
    assert desc in FULL
    mv = moving2(ch)
    tags = ["phase3-expansion"] + (["應期明確"] if c["timing"] else [])
    inputs.append({
        "id": cid, "system": "liuyao", "master": "野鶴老人", "era": ERA,
        "subject": {"name_or_desc": "求測者（原書多未具名）", "gender": None},
        "context": {"question": c["q"], "asked_at": c["asked"], "setting": c["setting"],
                    "attachments": {"casting_method": CAST, "hexagram": c["gua"], "moving_lines": mv,
                                    "chart_lines_top_to_bottom": ch}},
        "provenance": {"book": "《增刪卜易》", "edition": ED, "url": URL, "page": c["page"]},
        "license_status": "public-domain", "redistributable": True, "language": "zh-Hant",
        "notes": {"tags": tags, "comment": c["comment"], "cross_ref": None},
    })
    answers.append({
        "id": cid,
        "master_predictions": [{"master": "野鶴老人", "tradition": "liuyao", "date": c["asked"],
                                 "statement_excerpt": excerpt, "direction": c["direction"],
                                 "key_assertions": c["assertions"], "reasoning_points": c["assertions"],
                                 "source": f"《增刪卜易》{c['page']} {URL}"}],
        "outcome": {"description": desc, "verified_by": "《增刪卜易》原書自載應驗"},
        "provenance": {"book": "《增刪卜易》", "edition": ED, "url": URL, "page": c["page"]},
        "license_status": "public-domain", "redistributable": True, "language": "zh-Hant",
        "notes": {"comment": c["comment"], "cross_ref": None},
    })
    grading_rows.append((cid, c))

OUT = "/home/hatch/workspace/divination/benchmark/phase3/expansion/zengshan"
with io.open(f"{OUT}/inputs.jsonl", "w", encoding="utf-8") as f:
    for r in inputs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
with io.open(f"{OUT}/answers.jsonl", "w", encoding="utf-8") as f:
    for r in answers: f.write(json.dumps(r, ensure_ascii=False) + "\n")

n = len(CASES); nt = sum(1 for c in CASES if c["timing"])
nv3 = sum(1 for c in CASES if c["page"].startswith("卷之三")); nv4 = n - nv3
print(f"cases={n} vol3={nv3} vol4={nv4} timing={nt} ids=LY-201..LY-{200+n}")

lines_md = []
lines_md.append("# GRADING — 《增刪卜易》卷三、卷四六爻案例增補（Phase 3 數據角）\n")
lines_md.append(f"收錄 **{n} 例**（LY-201–LY-{200+n}）：卷之三 {nv3} 例、卷之四 {nv4} 例；結局可得性 **A 級 {n} 例、B 級 0 例**；污染分層 **低 {n} 例、高 0 例**；應驗時點明確 **{nt} 例**。\n")
lines_md.append("## 分級口徑\n")
lines_md.append("- **A**：原文明確記載可與斷語分離的實際結果事件（果……／後……等追記句），本批全數為 A。")
lines_md.append("- **B**：只有大師自述式應驗、不可分離——本批不收（篩選時剔除，見篩選日誌）。")
lines_md.append("- **污染**：本批皆清初民間占例、求測者多未具名、結局無從以常識先驗得知，一律低污染；無著名歷史人物／事件例，故高污染 0 例。")
lines_md.append("- **應驗時點明確**：應驗追記含具體日／月／年／時辰（如「果於巳日到」「果至卯年立業成家」），或斷語給出 bounded 窗口而應驗落在窗內（如「不出五載」）。\n")
lines_md.append("## 逐例登記\n")
lines_md.append("| id | 章 | 所問 | 占時 | 級 | 污染 | 時點明確 | 備註 |")
lines_md.append("|---|---|---|---|---|---|---|---|")
for cid, c in grading_rows:
    note = c["comment"][:60] if c["comment"] else ""
    lines_md.append(f"| {cid} | {c['page']} | {c['q']} | {c['asked']} | A | 低 | {'是' if c['timing'] else '否'} | {note} |")
lines_md.append("\n## 卦象覆核方法（防手算誤改）\n")
lines_md.append("全部裝卦曾以程序按爻位陰陽（⚊/○為陽、⚋/ㄨ為陰，動爻翻轉得變卦）逐例覆算本卦／變卦名，與原文題面卦名逐一對照：59 例中 58 例全合；唯一不合為 LY-253（原文 4119 行）變卦卦名「否」與裝卦（咸）不合，已在該例 notes 並記兩說、裝卦照錄不改。另 LY-202、LY-225 兩例原文未直書卦名，據裝卦推得並已注明。覆核中曾發現手算誤判多例（如巽之姤、解之震、中孚之臨皆原文正確），故卦名字段一律以原文題面為準，不作手算「訂正」。\n")
lines_md.append("## 篩選日誌\n")
lines_md.append("逐章通讀卷之三（身命章第三十六至求財章第六十八）、卷之四（謁貴章第六十九至新亡附葬祖塋章第一百三十）全文，識別候選占例 **105 則**（多卦合占按一例計），收錄 **59 則**，棄 **46 則**。棄因分類：")
lines_md.append("- 無應驗追記、或只有理論評註無結果事件：9 則（如占壽中孚例只有「二十年後再占」之約、家宅乾之小畜例純為駁古法、占何時得地例斷後無果句）")
lines_md.append("- 月日干支缺損或訛損、四要素之占時不全：7 則（如寅月癸女日、卯月戌辰日、寅月亥日無干、酉日戊寅日等）")
lines_md.append("- 卦名原文未書且推定不穩、或多卦鏈過長不合單例 schema：6 則（如醫卜往治五卦鏈、品級章多卦混敘例）")
lines_md.append("- 斷驗混敘不可分離（相當於 B 級）：6 則（如祖母痰堵例先報已逝後救活、歲考泰卦例斷驗同段、舟行蠱之巽例途中悟卦追敘）")
lines_md.append("- 終身泛斷、應驗為一生梗概不可分離核驗：7 則（終身財福章中段多例屬此）")
lines_md.append("- 四要素俱全但應期與資訊較弱、名額內取捨：11 則")
lines_md.append("\n另：与已收 LY-001–LY-036 按（占時＋卦象）逐一比對，無重複收錄（同主題如占父何日回、占升遷者，占時與卦象皆不同，為不同占例）。\n")
lines_md.append("## 錄入紀律\n")
lines_md.append("斷語與應驗逐字節錄自維基文库本（源文件 sources/chinese/zengshan-buyi-wikisource.txt），建檔腳本以行號切取原文並逐條斷言節錄為原文子串；訛字照錄、於 notes 注明，不擅改。裝卦照原文錄入（含原文缺字符號）。建檔腳本：build_cases.py（同目錄）。\n")
with io.open(f"{OUT}/GRADING.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines_md) + "\n")
print("written inputs/answers/GRADING")
