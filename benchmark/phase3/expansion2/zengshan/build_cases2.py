# -*- coding: utf-8 -*-
"""Phase 3 expansion2 — 《增刪卜易》第二輪增補建檔腳本（數據角）。
源文件：sources/chinese/zengshan-buyi-wikisource.txt（維基文庫本，本地已存）。
紀律：斷語/應驗節錄以行號切取原文並逐條斷言為原文子串；訛字照錄、notes 注明。
卦名原文未直書者以程序按裝卦爻象推得本卦/變卦並注明，不作手算訂正。"""
import json, re

SRC = "/home/hatch/workspace/divination/sources/chinese/zengshan-buyi-wikisource.txt"
raw_lines = open(SRC, encoding="utf-8").read().splitlines()
def L(n):
    return raw_lines[n-1].replace("<br>", "").strip()
FULL = "\n".join(L(i+1) for i in range(len(raw_lines)))

def seg(n, a=None, b=None):
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
            if "⚊" in s or "⚋" in s:
                out.append(s)
    return out

POS = ["上爻", "五爻", "四爻", "三爻", "二爻", "初爻"]
def moving(chart_lines):
    res = []
    groups = [chart_lines[i:i+6] for i in range(0, len(chart_lines), 6)]
    for g in groups:
        for i, row in enumerate(g):
            left = row.split("　")[0]
            if "○" in left or "ㄨ" in left:
                name = re.split(r"[○ㄨ⚊⚋]", left)[0]
                sym = "○" if "○" in left else "ㄨ"
                res.append(f"{POS[i]}{name}{sym}動")
    return "、".join(res) if res else "無動爻（靜卦）"

# --- hexagram derivation from chart lines (bottom-up yin/yang) ---
TRI = {(1,1,1):"乾",(0,0,0):"坤",(1,0,0):"震",(0,1,1):"巽",(0,1,0):"坎",(1,0,1):"離",(0,0,1):"艮",(1,1,0):"兌"}
HEX = {
("乾","乾"):"乾為天",("乾","坤"):"天地否",("乾","震"):"天雷無妄",("乾","巽"):"天風姤",("乾","坎"):"天水訟",("乾","離"):"天火同人",("乾","艮"):"天山遁",("乾","兌"):"天澤履",
("坤","乾"):"地天泰",("坤","坤"):"坤為地",("坤","震"):"地雷復",("坤","巽"):"地風升",("坤","坎"):"地水師",("坤","離"):"地火明夷",("坤","艮"):"地山謙",("坤","兌"):"地澤臨",
("震","乾"):"雷天大壯",("震","坤"):"雷地豫",("震","震"):"震為雷",("震","巽"):"雷風恆",("震","坎"):"雷水解",("震","離"):"雷火豐",("震","艮"):"雷山小過",("震","兌"):"雷澤歸妹",
("巽","乾"):"風天小畜",("巽","坤"):"風地觀",("巽","震"):"風雷益",("巽","巽"):"巽為風",("巽","坎"):"風水渙",("巽","離"):"風火家人",("巽","艮"):"風山漸",("巽","兌"):"風澤中孚",
("坎","乾"):"水天需",("坎","坤"):"水地比",("坎","震"):"水雷屯",("坎","巽"):"水風井",("坎","坎"):"坎為水",("坎","離"):"水火既濟",("坎","艮"):"水山蹇",("坎","兌"):"水澤節",
("離","乾"):"火天大有",("離","坤"):"火地晉",("離","震"):"火雷噬嗑",("離","巽"):"火風鼎",("離","坎"):"火水未濟",("離","離"):"離為火",("離","艮"):"火山旅",("離","兌"):"火澤睽",
("艮","乾"):"山天大畜",("艮","坤"):"山地剝",("艮","震"):"山雷頤",("艮","巽"):"山風蠱",("艮","坎"):"山水蒙",("艮","離"):"山火賁",("艮","艮"):"艮為山",("艮","兌"):"山澤損",
("兌","乾"):"澤天夬",("兌","坤"):"澤地萃",("兌","震"):"澤雷隨",("兌","巽"):"澤風大過",("兌","坎"):"澤水困",("兌","離"):"澤火革",("兌","艮"):"澤山咸",("兌","兌"):"兌為澤"}
def derive(chart_lines):
    names = []
    groups = [chart_lines[i:i+6] for i in range(0, len(chart_lines), 6)]
    for g in groups:
        if len(g) != 6:
            names.append(None); continue
        ben, bian, has_move = [], [], False
        for row in reversed(g):  # rows are top-to-bottom; bottom line first
            left = row.split("　")[0]
            if "⚊" in left or "○" in left: y = 1
            else: y = 0
            ben.append(y)
            if "○" in left: bian.append(0); has_move = True
            elif "ㄨ" in left: bian.append(1); has_move = True
            else: bian.append(y)
        lo = TRI[tuple(ben[0:3])]; up = TRI[tuple(ben[3:6])]
        name = HEX[(up, lo)]
        if has_move:
            lo2 = TRI[tuple(bian[0:3])]; up2 = TRI[tuple(bian[3:6])]
            name = name + "之" + HEX[(up2, lo2)]
        names.append(name)
    return names

ED = "維基文庫本（錄入者整理本，未排版/未校對，見 pending 校勘說明）"
URL = "https://zh.wikisource.org/wiki/增刪卜易"
CAST = "六爻納甲（銅錢搖卦，原書只記月日與卦象）"

CASES = []
def C(**kw): CASES.append(kw)

# ================= 卷之二（理論章占例，第一輪未收） =================
C(id="LY-401", opener=285, q="占後遇功名", asked="午月癸卯日（初占）；寅月丙辰日（再占）",
  gua="初占：艮為山之風地觀（卦名原文未直書，據裝卦推得；李我平按語亦稱艮之觀卦）；再占：地澤臨（靜卦）",
  page="卷之二·月破章第二十七", chart=[(287,292),(298,303)],
  stmt=[(294,"斷曰﹕","果於七月"),(305,"予曰﹕聞得士民保畱","果於甲子年")],
  out=[(294,"果於七月","予彼時"),(305,"果於甲子年",None)],
  direction="mixed", timing=True,
  setting="現任官員占問後來功名際遇；降級後再占前程",
  assertions=["官星寅木持世被申金動爻克，今年七月必有凶、成仇家之非","子水元神破而化空，接續相生無用，斷降級離任而非去位","再占斷子年仍以原品起用；辰年子水入墓、有克無生，禍更甚"],
  comment="兩占合斷例（跨數年應驗鏈）：初占應七月成非、冬至月降級；再占應甲子年起用、辰年三月得罪。卦名初占原文未直書，據裝卦推得艮之觀，與原文李我平按語「艮之觀卦」互證。")
C(id="LY-402", opener=472, q="占自陳何如", asked="酉月甲辰日",
  gua=None, page="卷之二·進神退神章第二十九", chart=[(474,479)],
  stmt=[(481,"斷曰﹕","果於次年")], out=[(481,"果於次年革職拿問",None)],
  direction="negative", timing=True,
  setting="占自陳（向上申辯）之後果",
  assertions=["世化回頭之克，官化退神，子孫化進神，三爻皆非吉象","斷大凶之兆"],
  comment="卦名原文未直書，據裝卦推得並注明於 attachments。")
C(id="LY-403", opener=496, q="占本年冬今得關差否", asked="戌月癸亥日",
  gua="水澤節之水天需", page="卷之二·進神退神章第二十九", chart=[(498,503)],
  stmt=[(505,"丑土官動化進神許丑日必得","果得於丑日")], out=[(505,"果得於丑日","古以動日月")],
  direction="positive", timing=True, setting="占本年冬季能否得關差",
  assertions=["丑土官爻動化進神，許丑日必得"], comment="")
C(id="LY-404", opener=507, q="占功名始得出仕否", asked="未月丁卯日",
  gua="天火同人之澤火革", page="卷之二·進神退神章第二十九", chart=[(509,514)],
  stmt=[(516,"予許辰年出仕","果於辰年")], out=[(516,"果於辰年得選","豈可謂之")],
  direction="positive", timing=True, setting="占功名，問何時始得出仕",
  assertions=["子孫戌土動而化退神，不克官","辰年沖去戌土，許辰年出仕"],
  comment="")
C(id="LY-405", opener=540, q="占病", asked="戌月癸未日",
  gua="乾為天之澤天夬", page="卷之二·進神退神章第二十九", chart=[(542,547)],
  stmt=[(549,"斷曰﹕","果卒於丑月")], out=[(549,"果卒於丑月",None)],
  direction="negative", timing=True, setting="占病吉凶",
  assertions=["久病逢沖莫治，父爻持世，妙藥難醫","世化退神乃精神命脈漸漸消枯之象，防沖破未土之時"], comment="")
C(id="LY-406", opener=562, q="占父母近病", asked="卯月癸酉日",
  gua="澤地萃之天地否", page="卷之二·進神退神章第二十九", chart=[(564,569)],
  stmt=[(571,"斷曰﹕","果於甲戌")], out=[(571,"果於甲戌出空卽愈","此乃父爻")],
  direction="positive", timing=True, setting="占父母近病吉凶",
  assertions=["未土父母動化進神，戌值旬空，近病逢空即愈","許次日（甲戌出空）退災"], comment="")
C(id="LY-407", opener=573, q="占病", asked="辰月癸丑日",
  gua="澤水困之雷水解", page="卷之二·進神退神章第二十九", chart=[(575,580)],
  stmt=[(582,"斷曰﹕","後卒於六月")], out=[(582,"後卒於六月","應未月者")],
  direction="negative", timing=True, setting="占病吉凶",
  assertions=["世爻寅木旬空，酉金忌神搖於五位，此時逢空，出空一定遭傷","應未月世爻入墓而死"],
  comment="")
C(id="LY-408", opener=584, q="占妻母病", asked="辰月乙丑日",
  gua="澤雷隨之天地否", page="卷之二·進神退神章第二十九", chart=[(586,591)],
  stmt=[(593,"斷曰﹕","果卒於甲戌日")], out=[(593,"果卒於甲戌日","乃戌土")],
  direction="negative", timing=True, setting="占妻母（岳母）之病",
  assertions=["子水父爻動化未土回頭克父母，未土又化進神克父","須防戌日"], comment="")
C(id="LY-409", opener=595, q="占出行（出）", asked="申月乙卯日",
  gua="水雷屯之水澤節", page="卷之二·進神退神章第二十九", chart=[(597,602)],
  stmt=[(604,"斷曰﹕","後至亥月")], out=[(604,"後至亥月方行由燕至粵","予曰﹕途中安否")],
  direction="positive", timing=True, setting="占出行可否、何時成行",
  assertions=["世臨寅木動化進神，本合當行，因月破目下未必能行","出月方可，應亥月（破而逢合之月）成行"], comment="")
C(id="LY-410", opener=606, q="占兄何日歸來", asked="辰月己未日",
  gua="天澤履之兌為澤", page="卷之二·進神退神章第二十九", chart=[(608,613)],
  stmt=[(615,"斷曰﹕","後至戌月")], out=[(615,"後至戌月方回","乃應實破")],
  direction="positive", timing=True, setting="占兄歸期",
  assertions=["兄動化退，已有歸志，因戌逢月破、在外諸事未遂","斷六月可望（實際戌月方回，應期不合，如實收錄）"],
  comment="原文占日作「辰月已未日」，「已」為「己」之形訛，asked_at 據干支常例作己未，原文照錄於此注。斷語許六月、實際戌月回，應期落空之例如實收錄。")
C(id="LY-411", opener=628, q="占官府升否（衙役代占）", asked="卯月丙寅日",
  gua="雷水解之澤水困", page="卷之二·進神退神章第二十九", chart=[(630,635)],
  stmt=[(637,"斷曰﹕","後報升於巳月")], out=[(637,"後報升於巳月","應巳月者")],
  direction="positive", timing=True, setting="衙役占其官府升遷否",
  assertions=["官動化進神，秋來得令必遷（實際報升於巳月）"],
  comment="斷語許秋來得令必遷、實際報升於巳月，應期不合如實收錄。")
C(id="LY-412", opener=650, q="占母路隔千里何時來", asked="未月丁丑日",
  gua="火天大有之水風井", page="卷之二·進神退神章第二十九", chart=[(652,657)],
  stmt=[(659,"斷曰﹕","果於次年")], out=[(659,"果於次年三月妹至","此乃兄弟化空")],
  direction="mixed", timing=True, setting="占母隔千里何時來；求測者自言有妹無弟",
  assertions=["初爻子水化丑父、子丑合，被合不來；未父化進神亦應不來","未土生酉金兄爻、兄化退合世，斷父母必不來、兄弟必來（應於妹）"], comment="")
C(id="LY-413", opener=703, q="占會試能連捷否", asked="戌月甲寅日",
  gua=None, page="卷之二·隨鬼入墓章第三十", chart=[(705,710)],
  stmt=[(712,"斷曰﹕","果然如是")], out=[(712,"果然如是",None)],
  direction="positive", timing=True, setting="占會試能否連捷",
  assertions=["世爻隨官入三墓，明歲辰年沖開墓庫、發榜之期又遇辰月","斷不獨連登、定中狀元"],
  comment="應驗句為「果然如是」總括式，惟其所驗證的斷語含連登、狀元、辰年辰月三項具體內容，依第一輪 LY-226「果得及第」判 A 的先例收為 A 級並在此標明成色。卦名原文未直書，據裝卦推得。")
C(id="LY-414", opener=714, q="占病（壬申命）", asked="申月己丑日",
  gua="雷風恆（靜卦）", page="卷之二·隨鬼入墓章第三十", chart=[(716,721)],
  stmt=[(723,"因世爻旺相","果起牀於未日")], out=[(723,"果起牀於未日","古法以墓")],
  direction="positive", timing=True, setting="占病，病者壬申命；病中不思湯藥、昏昏沉沉",
  assertions=["世爻旺相，隨鬼入墓非真","許未日愈（沖開丑墓之日）"], comment="")
C(id="LY-415", opener=725, q="占已定重罪可蒙赦免否", asked="未月戊辰日",
  gua=None, page="卷之二·隨鬼入墓章第三十", chart=[(727,732)],
  stmt=[(734,"明歲酉年定蒙赦免","果於次年")], out=[(734,"果於次年辰月蒙赦而出","予因屢試")],
  direction="positive", timing=True, setting="占已定重罪之人可否蒙赦免",
  assertions=["世爻隨鬼入動墓又化墓，予斷為吉：日月生世、丑墓月破，破網容易出","斷明歲酉年定蒙赦免（實際次年辰月赦出，年份合、月份為辰月）"],
  comment="卦名原文未直書，據裝卦推得。")
C(id="LY-416", opener=762, q="占迎請父王靈柩允否", asked="辰月甲戌日",
  gua="初占：（卦名原文未直書，據裝卦推得）；再占：澤火革之水火既濟", page="卷之二·隨鬼入墓章第三十", chart=[(764,769),(775,780)],
  stmt=[(771,"予曰﹐此隔靴搔癢也","再請一卦"),(782,"予曰﹕此正前卦相合","後應申月")],
  out=[(782,"後應申月所請準﹐酉歲迎靈而歸","兩卦皆是獨發")],
  direction="positive", timing=True, setting="占迎請父王靈柩是否允准",
  assertions=["父爻持世被寅木克制，身不能動、靈亦不能動，必待沖開寅木之年月","再占世化申金回頭生，應申月蒙恩；眼下月破萬萬不能"], comment="兩占合斷例。")
C(id="LY-417", opener=808, q="占女病", asked="寅月庚戌日",
  gua=None, page="卷之二·獨發章第三十一", chart=[(810,815),(819,824)],
  stmt=[(817,"予以卦土爲子孫","命伊母再占一卦"),(826,"予曰﹕寅日大愈","果於寅日")],
  out=[(826,"果於寅日全愈","此𨿽應前卦")],
  direction="positive", timing=True, setting="占女病吉凶；母代占，後命母再占一卦合斷",
  assertions=["子孫土雖休囚，得巳午火動生、未土化進、辰土化回頭生，許寅日當愈（不敢竟斷，命再占）","再占亥水子孫化寅木空亡，近病逢空即愈、出空之日，與前卦相合，斷寅日大愈"], comment="兩占合斷例；兩卦卦名原文均未直書，據裝卦推得。")
C(id="LY-418", opener=835, q="占求財", asked="未月庚子日",
  gua="風天小畜（靜卦）", page="卷之二·兩現章第三十二", chart=[(837,842)],
  stmt=[(844,"應臨月建之財以克世","卻得於辰土")], out=[(844,"卻得於辰土出空之日","此乃捨其")],
  direction="positive", timing=True, setting="占求財，問何時到手",
  assertions=["應臨月建之財克世，許必得","斷次日辛丑沖動未財得財（實際得於辰土出空之日，應期不合，如實收錄）"], comment="斷語應期（次日辛丑）與實際（辰日出空）不合，原文以「捨不空用旬空」自釋，如實收錄。")
C(id="LY-419", opener=857, q="母占子何日脫厄", asked="亥月丙午日",
  gua="雷地豫之雷澤歸妹", page="卷之二·兩現章第三十二", chart=[(859,864)],
  stmt=[(866,"予見卦中三現子孫","果脫厄於巳年")], out=[(866,"果脫厄於巳年","此乃卦中")],
  direction="positive", timing=True, setting="母占子何日脫厄",
  assertions=["子孫三現俱生世，午逢日建而靜，兩爻巳火逢月破","許巳年脫厄（實破之年），合前二卦同斷"], comment="原文自記此斷合前二卦（本人自占、弟占兄皆應巳年）而決，非單卦獨立斷。")
C(id="LY-420", opener=924, q="占鄉試", asked="巳月壬子日",
  gua="水地比（靜卦）", page="卷之二·星煞章第三十三", chart=[(926,931)],
  stmt=[(933,"巳月父爻當月建","子年占")], out=[(933,"果於卯年登科","卯年者")],
  direction="positive", timing=True, setting="子年占鄉試",
  assertions=["父爻當月建文星旺，獨嫌官星持世、卯木旬空","許卯科方得遂意（太歲填實不空）"], comment="")
C(id="LY-421", opener=982, q="占官運", asked="未月庚寅日",
  gua=None, page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，維基文庫本此段未標章名）", chart=[(984,989)],
  stmt=[(991,"斷曰﹕","果於巳年")], out=[(991,"果於巳年被論﹐宦囊消索","此乃世逢合")],
  direction="mixed", timing=True, setting="占官運（仕途前程）",
  assertions=["世臨亥水得太歲拱扶、酉金有生意、世化回頭生又得日合，仕途平坦","惟防巳年太歲沖害刑申，有蹭蹬榮歸、宦囊一空之虞"],
  comment="卦名原文未直書，據裝卦推得。")
C(id="LY-422", opener=1099, q="占年運", asked="未月戊辰日",
  gua=None, page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1101,1106)],
  stmt=[(1108,"斷曰﹕","卯年占")], out=[(1108,"卒於午年","應午年者")],
  direction="negative", timing=True, setting="卯年占年運（終身運限）",
  assertions=["世爻子水三合水局，不宜日月克世、世化回頭克、動爻辰土又克，世休囚無氣","應午年世臨歲破之年卒"],
  comment="卦名原文未直書，據裝卦推得。")
C(id="LY-423", opener=1112, q="占妻病", asked="午月癸丑日",
  gua=None, page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1114,1119)],
  stmt=[(1121,"予曰卯日財空","果於次日")], out=[(1121,"果於次日退災﹐不藥而愈","亦不獨此")],
  direction="positive", timing=True, setting="占妻病；來人言病起三月（已三月）",
  assertions=["卯日財空，明日出空必定退災","亥水子孫獨發克去世爻之鬼，應明日寅日（寅亥合起子孫）"],
  comment="卦名原文未直書，據裝卦推得。")
C(id="LY-424", opener=1205, q="占月令（本月運限）", asked="辰月乙未日",
  gua="地天泰之雷火豐", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1207,1212)],
  stmt=[(1214,"世爻辰土﹐月建助之","然此後至辛丑日")], out=[(1214,"此後至辛丑日尙亦見其凶非","應解救者")],
  direction="mixed", timing=True, setting="占本月月令吉凶",
  assertions=["世爻辰土得月建助、丑土動化回頭生扶助，世旺有扶可敵寅木鬼動"], comment="斷語僅及世旺可敵，其後辛丑日見凶非（觸怒上司幾危殆、幸得解救）為原文追記的具體事件，應驗與斷語吉凶並存，如實收錄。")
C(id="LY-425", opener=1232, q="占候選何時得缺", asked="戌月甲寅日",
  gua="風雷益之水山蹇（原文作益變騫）", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1234,1239)],
  stmt=[(1241,"斷曰﹕","果然在第二年")], out=[(1241,"果然在第二年寅月沒有中榜","正如神告")],
  direction="negative", timing=True, setting="占候選何時得缺",
  assertions=["世爻臨月破，又有寅日傷克、卯木克世，有克無生","世爻變出官星其實是變鬼，功名無望"], comment="")
C(id="LY-426", opener=1243, q="占開店貿易", asked="巳月壬申日",
  gua=None, page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1245,1250)],
  stmt=[(1252,"斷曰﹕","果於八月")], out=[(1252,"果於八月﹐因子賭博送官﹐子受杖刑而死","此應酉金")],
  direction="negative", timing=True, setting="占開店貿易得利否",
  assertions=["財臨月破，子動生財亦生之不起；世與子孫一同變鬼","斷營運難圖，今秋必因子女以致官非"],
  comment="卦名原文未直書，據裝卦推得。")
C(id="LY-427", opener=1298, q="占父任雲南何時得信", asked="戌月丙子日",
  gua="地澤臨（靜卦）", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1300,1305)],
  stmt=[(1307,"占信者﹐朱雀巳火父母爲用神","後果無音訊")], out=[(1307,"後果無音訊﹐四年知父而遇害矣",None)],
  direction="negative", timing=True, setting="占父任雲南，何時得音信",
  assertions=["朱雀巳火父母為用神，日辰子水克巳火、巳火又墓於戌月，音信茫然之兆"], comment="應驗時點為「四年後知父遇害」，屬 bounded 追記。")
C(id="LY-428", opener=1311, q="占關差得否", asked="丑月庚子日",
  gua="地天泰之地火明夷", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1313,1318)],
  stmt=[(1320,"占官差以官鬼爲用","卽於壬寅日得差")], out=[(1320,"卽於壬寅日得差","豈可謂之")],
  direction="mixed", timing=True, setting="占關差得否",
  assertions=["官鬼寅木克世、世爻空（原文以此質疑「用克世勿作凶看」之說）"],
  comment="本例斷語與應驗同段敘述：得差在壬寅日、次年三月死於中途，兩段應驗俱見原文同句後段（outcome 節錄含死於中途全句）。")
C(id="LY-429", opener=1348, q="占病", asked="卯月甲申日",
  gua="地山謙之水山蹇", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1350,1355)],
  stmt=[(1357,"斷曰﹕","果於丁亥日")], out=[(1357,"果於丁亥日全愈","豈知卯木"),(1357,"後至巳月亥逢月破",None)],
  direction="mixed", timing=True, setting="占病吉凶",
  assertions=["亥水子孫長生於申日，世遇日建逢生，雖化戌土之克，春令土衰有殺無妨（斷先愈）"], comment="應驗分兩段：丁亥日全愈（近應）；巳月亥逢月破、巳火生助戌土，復病而死（遠應），俱見原文同段。")
C(id="LY-430", opener=1363, q="占掣籤何處（抽籤分發何地）", asked="午月庚寅日（初占）；甲午日（再占）",
  gua="初占：山天大畜之風澤中孚；再占：地澤臨之水澤節", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1365,1370),(1376,1381)],
  stmt=[(1372,"斷曰﹕","改日竭誠再占"),(1383,"予曰此與前卦","後果於七月")],
  out=[(1383,"後果於七月",None)],
  direction="negative", timing=True, setting="占掣籤將分發何處、能否到任",
  assertions=["世臨寅木官星，必得東缺（非廣東即山東）","子水財臨月破動化絕，財為養命之源又為祿，財絕是無財無祿，恐不能到任","再占亥水財爻被回頭克，不獨難以到任，還妨秋令危災"], comment="兩占合斷例；結局為七月得瀉疾、服藥過度竟渴死，未到任。")
C(id="LY-431", opener=1498, q="占主人目下災悔否（家人代占防害）", asked="卯月戊戌日",
  gua="水地比之澤山咸", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1502,1507)],
  stmt=[(1509,"此卦若以本人念","至申日聞信")], out=[(1509,"至申日聞信﹐有人往上司揭告﹐被人勸阻﹐訟之未成","若以家人占主")],
  direction="positive", timing=True, setting="現任官府命家人代占主人目下有無災悔",
  assertions=["若以本人之念斷：子孫克世、克去身邊之鬼，災可解","若以家人占主斷（父母為用）：父空墓於戌日、卯官難擋疊疊之金，秋來有險厄——原文自記實際應在本人之念"], comment="代占取用之爭的成例；原文自記應驗歸於「官府自己之念」一路，如實收錄兩路斷法與歸屬說明。")
C(id="LY-432", opener=1513, q="占功名（先代尊長占病、本人占功名，兩念反應）", asked="辰月癸未日",
  gua="初卦：天風姤之風水渙；後卦：天澤履（靜卦）", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1515,1520),(1524,1529)],
  stmt=[(1531,"若以前卦﹐斷子病者","後卦竟應")], out=[(1531,"五月高遷","後卦竟應"),(1533,"次日卽愈",None)],
  direction="positive", timing=True, setting="其人欲占功名，先命代占尊長之病；本人自占功名另得一卦。原文主旨為兩卦反應（前卦應功名、後卦應子病）",
  assertions=["前卦若斷子病必死，實際應功名：午火官動生世、世動官興，五月高遷","後卦應父占子病：申金子孫得日月生，次日即愈"],
  comment="斷驗同段敘述的反應成例，斷語自分析文字中節錄。")
C(id="LY-433", opener=1537, q="占功名（父命子占將來有功名否）", asked="午月辛酉日",
  gua="澤地萃之天山遁", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1539,1544)],
  stmt=[(1546,"此卦乃是父占子也","此子未年而死")], out=[(1546,"此子未年而死","未年死子者"),(1546,"夫應七月傷妻","予今亦曾")],
  direction="negative", timing=True, setting="父命十五歲子占將來有功名否；原文自記此實為父之念、是父占子",
  assertions=["表面斷法：官星持世、父化進神，功名有望","正斷：此乃父占子，父動克子只傷妻——斷子未年死、夫七月傷妻"], comment="與 LY-320（卜筮正宗第十七問同型案例）為同型不同例：占時、卦象、應驗年份均不同，非同例重複，互見於去重記錄。")
C(id="LY-434", opener=1548, q="占流年（實問援例成否）", asked="未月癸亥日",
  gua="艮為山（靜卦）", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1550,1555)],
  stmt=[(1557,"予曰﹕此卦官星持世","果於申日")], out=[(1557,"果於申日文書實收俱到","應申日者")],
  direction="positive", timing=True, setting="其人已往軍前援例，托言占流年，實問援例成否",
  assertions=["官星持世、長生於亥日，業已成矣；亥水為財，財旺生官","應申日（寅木官星靜而逢沖之日）文書到"], comment="與《卜筮正宗》第十八問所載同型案例（果壬申日文書收到）為同型不同例，互見去重記錄；本例應驗作「申日」未記干支全稱。")
C(id="LY-435", opener=1559, q="占何時得財（閒問古窖）", asked="未月丙辰日",
  gua="澤山咸之澤風大過", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1563,1568)],
  stmt=[(1570,"予曰﹕卦中鬼變子孫","果死於亥日")], out=[(1570,"果死於亥日","彼問﹕何所問得財")],
  direction="negative", timing=True, setting="其人閒問家中常見白影、必有古窖，何時得財；其小女方出花（痘疹）",
  assertions=["卦中鬼變子孫，目下子女不利","小女出花，須防亥日（午火鬼化亥水子）"], comment="占此應彼成例：所問為財，應驗在子女。")
C(id="LY-436", opener=1570, q="占本月月令", asked="酉月甲辰日",
  gua="天山遁之天風姤", page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1572,1577)],
  stmt=[(1579,"世爻午火動化亥水回頭克","占月令而現壽元")], out=[(1579,"世辰年占卦﹐在午年子月而死","占月令而現壽元")],
  direction="negative", timing=True, setting="辰年占本月月令",
  assertions=["世爻午火動化亥水回頭克（原文以此斷壽元）"], comment="占近應遠成例：占月令而現壽元，應於午年子月。斷語簡略，應驗時點明確。")
C(id="LY-437", opener=1583, q="占小廝病", asked="巳月己未日",
  gua=None, page="卷之二·增刪黃金策千金賦章第三十四（章界據通行本體例判定，同上）", chart=[(1585,1590)],
  stmt=[(1592,"予曰﹕此卦不應小廝病","果於七月")], out=[(1592,"果於七月﹐被論革職","此占他而應我")],
  direction="negative", timing=True, setting="占小廝（僕役）之病；占者本人為官",
  assertions=["此卦不應小廝病，而應占者本人今秋功名有礙","世臨卯木之官化申金子孫回頭克，諸事須慎"],
  comment="原文占日作「巳月已未日」，「已」為「己」之形訛，asked_at 作己未並注明。卦名原文未直書，據裝卦推得。占他應我成例。")

# ================= 卷之二·天時章（天氣類，斷語+果驗俱全者） =================
C(id="LY-438", opener=784, q="占防漲水沖去麥子（兼問陰晴）", asked="午月甲申日",
  gua=None, page="卷之二·獨發章第三十一", chart=[(786,791)],
  stmt=[(793,"予曰﹕爾憂麥被水沖","果於卯日")], out=[(793,"果於卯日大晴",None)],
  direction="positive", timing=True, setting="友人憂漲水沖去麥子，執卦來問；時昨日丙戌",
  assertions=["子孫發動克去身邊之鬼，憂非、應晴，決不漲水","卯日必大晴（動而逢合之日晴）"],
  comment="卦名原文未直書，據裝卦推得。")
C(id="LY-439", opener=1693, q="占本日陰晴", asked="午月丁亥日",
  gua="天山遁之天地否（原文作逐之否，逐為遁之形訛）", page="卷之二·天時章第三十五", chart=[(1695,1700)],
  stmt=[(1702,"予曰﹕申金兄爻爲云","果一日陰雲")], out=[(1702,"果一日陰雲申時而見日色﹐次日卯時大晴",None)],
  direction="positive", timing=True, setting="占本日陰晴",
  assertions=["申金兄爻為雲，化卯木財爻，是由雲霧中變出日色之象"], comment="")
C(id="LY-440", opener=1706, q="因連日雪占何日晴", asked="子月己亥日",
  gua="風地觀之水地比", page="卷之二·天時章第三十五", chart=[(1708,1713)],
  stmt=[(1715,"斷曰﹕","果於次日")], out=[(1715,"果於次日卯時﹐云開日出","此子水者")],
  direction="positive", timing=True, setting="連日雪，占何日晴",
  assertions=["兩爻火鬼暗動，今日還是陰天","卯木財爻化出子孫子水，明日卯時必晴"], comment="")
C(id="LY-441", opener=1719, q="占本日陰晴", asked="辰月己卯日",
  gua="水雷屯之地澤臨", page="卷之二·天時章第三十五", chart=[(1721,1726)],
  stmt=[(1728,"斷曰﹕","果於戌時")], out=[(1728,"果於戌時﹐星辰無光","若以一日之煙霧")],
  direction="mixed", timing=True, setting="占本日陰晴",
  assertions=["寅木子孫化進神，今日大晴","五爻戌土鬼動，戌亥時必主黑雲"], comment="")
C(id="LY-442", opener=1753, q="因連日雨占何日晴", asked="午月乙卯日",
  gua=None, page="卷之二·天時章第三十五", chart=[(1755,1760)],
  stmt=[(1762,"予曰﹕今日酉時必見紅輪西墮","果於酉時")], out=[(1762,"果於酉時忽然天開﹐見日色。次日迷雲而雨",None)],
  direction="mixed", timing=True, setting="連日雨、本日亦雨，占何日晴",
  assertions=["六爻酉父化子，今日酉時落日（晴）","初爻卯木化辰鬼，明朝辰日必是陰雲"],
  comment="卦名原文未直書，據裝卦推得。")
C(id="LY-443", opener=1807, q="久雪占晴", asked="丑月戊辰日",
  gua="澤雷隨之震為雷", page="卷之二·天時章第三十五", chart=[(1809,1814)],
  stmt=[(1816,"斷曰﹕","果於酉時")], out=[(1816,"果於酉時霧散天開","凡得父化退神")],
  direction="positive", timing=True, setting="久雪占晴",
  assertions=["鬼化退神，雨（雪）將止"], comment="")
C(id="LY-444", opener=1856, q="因晴占何日雨", asked="辰月癸卯日",
  gua="水山蹇（靜卦）", page="卷之二·天時章第三十五", chart=[(1858,1863)],
  stmt=[(1865,"予曰﹕戌臨月破﹐如何有雨﹖陰雲而已","果於次日")], out=[(1865,"果於次日常見陰雲",None)],
  direction="negative", timing=True, setting="因久晴占何日雨",
  assertions=["戌父臨月破，如何有雨，陰雲而已"], comment="應驗為次日陰雲而無雨，與斷語合。")
C(id="LY-445", opener=1869, q="占何日雨（三占合斷）", asked="未月丙午日",
  gua="初占：離為火之火山旅；二占：離為火（靜卦，原文未附裝卦）；三占：艮為山之地山謙", page="卷之二·天時章第三十五", chart=[(1871,1876),(1880,1885)],
  stmt=[(1878,"斷曰﹕卯木父動臨於旬空","再占一卦"),(1887,"斷曰﹕甲寅日陰雲﹐乙卯日必雨﹐辰日而又晴矣","果於寅日")],
  out=[(1887,"果於寅日云卯日大雨辰日大晴","所以動則不爲空")],
  direction="positive", timing=True, setting="占何日有雨，連占三卦合斷",
  assertions=["初占卯木父動臨旬空，斷己酉不雨則卯日必雨","三占寅木鬼動值旬空，出空之日必天變；合前卦斷寅日陰雲、卯日必雨、辰日又晴"], comment="三占合斷例；二占原文未附裝卦，attachments 只錄初占、三占裝卦並注明。")
C(id="LY-446", opener=1891, q="占何日雨", asked="戌月丙午日",
  gua="坎為水之水風井", page="卷之二·天時章第三十五", chart=[(1893,1898)],
  stmt=[(1900,"予曰﹕非也","果於酉日")], out=[(1900,"果於酉日天變﹐戌日而雨","午火財爻墓於戌")],
  direction="positive", timing=True, setting="占何日有雨；或疑財動主旱無雨",
  assertions=["財爻化出酉父，酉日當有雨；因日建與午火，必待戌日午火入墓方雨"],
  comment="原文占題作「如戌日丙午日占何日雨」，首字「日」疑為「月」之訛，asked_at 作戌月丙午日並注明。")
C(id="LY-447", opener=1915, q="占何日晴", asked="午月乙卯日",
  gua="火地晉之雷澤歸妹", page="卷之二·天時章第三十五", chart=[(1917,1922)],
  stmt=[(1924,"斷曰﹕","果雨旬日")], out=[(1924,"果雨旬日",None)],
  direction="negative", timing=True, setting="占何日晴",
  assertions=["父鬼疊見，乃連朝風雨之象（次日又占仍鬼父同動）"], comment="")
C(id="LY-448", opener=1926, q="占何日雨（連占合斷）", asked="未月甲午日",
  gua="水雷屯之風澤中孚", page="卷之二·天時章第三十五", chart=[(1928,1933)],
  stmt=[(1935,"大旱望云雷","果然兩月不雨")], out=[(1935,"果然兩月不雨",None)],
  direction="negative", timing=True, setting="大旱占何日雨，連日再占合斷",
  assertions=["父爻不動、子孫重疊化進神，疑入墓之日雨；他日再占仍無父動鬼動，斷知其旱"], comment="連占合斷例；應驗為兩月不雨。")
C(id="LY-449", opener=1939, q="占何日晴", asked="辰月庚寅日",
  gua="風地觀之地風升", page="卷之二·天時章第三十五", chart=[(1941,1946)],
  stmt=[(1948,"斷曰﹕","果於次日")], out=[(1948,"果於次日晴還又雨",None)],
  direction="mixed", timing=True, setting="占何日晴",
  assertions=["卯木財現，明日必晴","卦得內外反吟，晴而還雨"], comment="")
C(id="LY-450", opener=2015, q="占甲午日臨造此日有雨否", asked="辰月癸巳日",
  gua=None, page="卷之二·天時章第三十五", chart=[(2017,2022)],
  stmt=[(2024,"予曰﹕應時日看","果於本日")], out=[(2024,"果於本日申時雨","彼﹕又是如何"),(2024,"果於次日大晴",None)],
  direction="mixed", timing=True, setting="預占甲午日營造之日有雨否（問指定日天氣）",
  assertions=["父動，今日申戌時無雨者明日必有雨（實際本日申時雨）","父化退神，雨不久，明日必晴"],
  comment="原文占日作「辰日癸巳日」，首字疑為「月」之訛，asked_at 作辰月癸巳日並注明。卦名原文未直書，據裝卦推得。")

# ================= 卷之三、卷之四補遺（第一輪名額外取捨者中斷驗俱全者） =================
C(id="LY-451", opener=2441, q="占夢（前夫叫去已隨去）", asked="午月丁亥日",
  gua=None, page="卷之三·趨避章第四十", chart=[(2443,2448)],
  stmt=[(2450,"斷曰﹕","果於九月")], out=[(2450,"果於九月成癆﹐臘月而死",None)],
  direction="negative", timing=True, setting="婦人夢見已故前夫叫她、已隨去，占此夢吉凶",
  assertions=["世爻亥水臨日辰，豈當重重土克","今冬防厄"],
  comment="卦名原文未直書，據裝卦推得。")
C(id="LY-452", opener=2535, q="占通鄉避亂（往何方避）", asked="巳月丙戌日",
  gua="乾為天之火天大有", page="卷之三·趨避章第四十", chart=[(2537,2542)],
  stmt=[(2544,"予曰﹕非此議論","後果從北來")], out=[(2544,"後果從北來﹐放火燒村而去﹐房屋稻穀盡成灰燼","乃申金兄動")],
  direction="positive", timing=False, setting="兵亂時通鄉人占往何方避亂；眾議往北（子孫水方）為吉",
  assertions=["兄動化進神乃破財之象，午火得令生世，往南避之為吉（非北）"], comment="應驗為賊兵果從北來燒村，南避者免；應驗無具體日月時點，timing_explicit 記 false。")
C(id="LY-453", opener=2645, q="占兄弟還有（有無）", asked="未月辛丑日",
  gua="水火既濟之澤火革", page="卷之三·兄弟章第四十二", chart=[(2647,2652)],
  stmt=[(2654,"予曰﹕兄弟𨿽有﹐必不得濟","後果異母有出")], out=[(2654,"後果異母有出﹐父亡而撫之","予曰﹕撫其成人")],
  direction="mixed", timing=False, setting="占兄弟還有否；求測者已有一弟得顛狂之癥",
  assertions=["兄弟雖有必不得濟；亥水兄持世、申父動生，此一位得濟之弟尚未生","應爻子水兄弟臨空不得力；斷必有異母所生之弟"],
  comment="")
C(id="LY-454", opener=2863, q="占道考", asked="亥月丙戌日",
  gua="雷火豐之澤火革", page="卷之三·童試章第四十九", chart=[(2865,2870)],
  stmt=[(2872,"父母持世化進神","果取案首")], out=[(2872,"果取案首",None)],
  direction="positive", timing=False, setting="占道考（考試）名次",
  assertions=["父母持世化進神，日建作官生世，文章愈出愈奇、後勝於前","定蒙首選"], comment="")
C(id="LY-455", opener=2883, q="占歲考", asked="申月乙巳日",
  gua="澤風大過之火風鼎", page="卷之三·歲科考章第五十", chart=[(2885,2890)],
  stmt=[(2892,"斷曰﹕","後果取超等")], out=[(2892,"後果取超等補稟",None)],
  direction="positive", timing=False, setting="占歲考等第",
  assertions=["亥水父爻持世得申月生、巳日沖為暗動；未土財動生酉金、酉官生世，接續相生","斷篇篇華錦、財生官旺優等"], comment="")
C(id="LY-456", opener=3034, q="占缺得否", asked="申月己亥日",
  gua="水風井之水澤節", page="卷之三·鄉試章第五十五（升選候補附）", chart=[(3036,3041)],
  stmt=[(3043,"斷曰﹕","後果另選別人")], out=[(3043,"後果另選別人",None)],
  direction="negative", timing=False, setting="占此缺（職位）得否",
  assertions=["內卦巳酉丑合成官局而生應爻、不來生世，所謂出現無情","官生應爻，此缺一定不得"], comment="")
C(id="LY-457", opener=3542, q="占往楚買豆得利否", asked="午月戊子日",
  gua="地澤臨（靜卦）", page="卷之四·往何方買賣章第七十五", chart=[(3544,3549)],
  stmt=[(3551,"斷﹕亥水財爻休囚於外","後果中間人作獘")], out=[(3551,"後果中間人作獘","此乃指其地")],
  direction="positive", timing=True, setting="占往楚地買豆得利否（指其地而占）",
  assertions=["亥水財爻休囚於外，楚地豆子必賤","子水日建生世，必能得厚利；但間爻兄弟月生日合，耗費錢多"], comment="應驗含中間人作弊告官、誤一個月的具體情節與最終得厚利，時點為「誤了一個月」。")
C(id="LY-458", opener=3846, q="占母在外何時來", asked="酉月戊申日",
  gua="火山旅之艮為山", page="卷之四·行人章第九十四", chart=[(3848,3853)],
  stmt=[(3855,"只可斷用神伏藏也﹐克而不來﹐六合沖亦不來","後果在外平安")], out=[(3855,"後果在外平安",None)],
  direction="negative", timing=False, setting="占母在外何時來（原文辨明：此問來否、非問平安）",
  assertions=["用神伏藏受克，不來；六合沖亦不來"], comment="應驗為母在外平安而未歸，與斷語「不來」合。")
C(id="LY-459", opener=3911, q="自占登舟一路平安否", asked="戌月丙戌日",
  gua="山風蠱之巽為風", page="卷之四·舟行章第九十二", chart=[(3913,3918)],
  stmt=[(3920,"見其化出巳火子孫","果泊五日")], out=[(3920,"果泊五日﹐巳日天晴得風順矣","自此始悟")],
  direction="mixed", timing=True, setting="野鶴自占：由江右登舟，一路平安否",
  assertions=["子水父動應子日風雨（占後自悟）","化出巳火子孫，知巳日方晴、得順風"], comment="本例斷語為行程中（戊子日風雨後）據卦自悟，非登舟時預斷，原文如實敘明；作為應期自悟例收錄並標明成色。")

# ================= emit =================
import pathlib
outdir = pathlib.Path(__file__).parent
inputs, answers, roster = [], [], []
for c in CASES:
    cl = chart(c["chart"])
    assert len(cl) in (6, 12), f'{c["id"]} chart rows {len(cl)}'
    derived = derive(cl)
    gua = c["gua"] if c["gua"] else "之".join(x for x in derived if x) + "（卦名原文未直書，據裝卦推得）"
    stmt_text = " ".join(seg(*s) if isinstance(s, tuple) else seg(s[0], s[1], s[2]) for s in c["stmt"])
    out_text = " ".join(seg(s[0], s[1], s[2]) for s in c["out"])
    inp = {"id": c["id"], "tradition": "liuyao",
           "subject": {"name_or_desc": "求測者（原書多未具名）", "gender": None},
           "context": {"question": c["q"], "asked_at": c["asked"], "setting": c["setting"],
                       "attachments": {"casting_method": CAST, "hexagram": gua,
                                       "moving_lines": moving(cl), "chart_lines_top_to_bottom": cl}},
           "provenance": {"book": "《增刪卜易》", "edition": ED, "url": URL, "page": c["page"]},
           "language": "zh-Hant"}
    ans = {"id": c["id"], "master_predictions": [{"master": "野鶴老人", "tradition": "liuyao", "date": c["asked"],
            "statement_excerpt": stmt_text, "source": f"《增刪卜易》{c['page']} {URL}",
            "direction": c["direction"], "key_assertions": c["assertions"]}],
           "outcome": {"description": out_text, "verified_by": "《增刪卜易》原書自載應驗"},
           "provenance": {"book": "《增刪卜易》", "edition": ED, "url": URL, "page": c["page"]},
           "license_status": "public-domain", "redistributable": True, "language": "zh-Hant",
           "notes": {"tags": ["phase3-expansion2"], "comment": c["comment"], "cross_ref": None}}
    inputs.append(inp); answers.append(ans)
    roster.append({"id": c["id"], "tradition": "liuyao", "source": "zengshan2",
                   "outcome_record": out_text, "contamination": "low",
                   "contamination_reason": "清初民間占例，求測者多未具名，非著名歷史人物／事件，結局無從以常識先驗得知（據 expansion2/zengshan/GRADING.md 污染口徑）。",
                   "timing_explicit": bool(c["timing"])})
with open(outdir/"inputs.jsonl", "w", encoding="utf-8") as f:
    for r in inputs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(outdir/"answers.jsonl", "w", encoding="utf-8") as f:
    for r in answers: f.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(outdir/"roster-part.jsonl", "w", encoding="utf-8") as f:
    for r in roster: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"cases: {len(CASES)}")
for c, a in zip(CASES, answers):
    print(c["id"], "| derived:", derive(chart(c["chart"])), "| stmt:", a["master_predictions"][0]["statement_excerpt"][:40], "| out:", a["outcome"]["description"][:40])
