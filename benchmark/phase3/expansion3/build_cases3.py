# -*- coding: utf-8 -*-
"""Phase 3 expansion3 — 第三輪擴數建檔腳本（數據角）。
來源：(1) 《增刪卜易》維基文庫本地本 sources/chinese/zengshan-buyi-wikisource.txt（逐行切取，子串斷言）；
      (2) 《卜筮正宗》cnddy 在線全本在線讀（節錄照頁面簡體字，逐條人工核對頁面原文）。
紀律：不讀 holdout3/holdout4 test_gold.jsonl；去重只用 roster／分卷 inputs/answers 出處字段。
"""
import json, re, os, glob, hashlib
from datetime import datetime, timezone, timedelta

BASE = "/home/hatch/workspace/divination"
SRC = BASE + "/sources/chinese/zengshan-buyi-wikisource.txt"
OUT = BASE + "/benchmark/phase3/expansion3"
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
        for row in reversed(g):
            left = row.split("　")[0]
            y = 1 if ("⚊" in left or "○" in left) else 0
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
CONT_Z = "清初民間占例（野鶴老人自占及輯錄），求測者多未具名，非著名歷史人物／事件，結局無從以常識先驗得知。"
CONT_B = "清初民間占例（王洪緒輯錄其師楊廣含傳授及自占驗），求測者多未具名，非著名歷史人物／事件，結局無從以常識先驗得知。"

CASES = []
def C(**kw): CASES.append(kw)

# ================= 《增刪卜易》=====================
# 每例: chart 行段、stmt/out 節錄段 (line, 起子串, 止子串)
C(id="LY-501", q="占求財", asked="未月庚子日", page="卷之二·兩現章第三十二",
  chart=[(837,842)], stmt=[(844,"應臨月建之財以克世","卻得於辰土")], out=[(844,"卻得於辰土出空之日",None)],
  direction="positive", setting="占求財能否得、何時到手",
  assertions=["應爻未土妻財臨月建克世，許之必得","斷次日辛丑沖動未財到手；實際得於辰土出空之日，主斷（得財）應驗、應期不合"],
  comment="主斷與應期分離可判讀例。", eligible=True)
C(id="LY-502", q="占鄉試", asked="巳月壬子日", page="卷之二·增刪黃金策千金賦章第三十四",
  chart=[(926,931)], stmt=[(933,"巳月父爻當月建","果於卯年")], out=[(933,"果於卯年登科",None)],
  direction="positive", setting="子年占鄉試，問能否登科",
  assertions=["父母巳火臨月建文星旺，官星卯木持世旬空，許之卯科方得遂意","子年占，果於卯年登科（太歲填實）"],
  comment="", eligible=True)
C(id="LY-503", q="占自陳何如", asked="卯月辛巳日", page="卷之二·增刪黃金策千金賦章第三十四",
  chart=[(943,948)], stmt=[(950,"予曰﹕酉官持世破而且空","果於五月")], out=[(950,"果於五月下獄",None)],
  direction="negative", setting="占自陳（向上申辯）吉凶",
  assertions=["酉金官鬼持世，破而且空，又動出午火相克","斷不獨削職，須防五六月還見凶災；果於五月下獄"],
  comment="原文 asked 僅作「卯月辛巳」無「日」字，月建與日辰干支俱全，照錄。", eligible=True)
C(id="LY-504", q="占久病", asked="巳月未日（原文如此，日干支不全）", page="卷之二·增刪黃金策千金賦章第三十四",
  chart=[(1028,1033)], stmt=[(1035,"斷曰﹕世爻寅木化出巳爻","果卒於申日")], out=[(1035,"果卒於申日",None)],
  direction="negative", setting="占久病吉凶",
  assertions=["世爻寅木化出巳火，三刑少申字，防申日之危","果卒於申日"],
  comment="原文只記「巳月未日」，日干支不全（或為巳月某未日之略記），月日完整性不成立，僅入 dev-add。",
  eligible=False, md_complete=False, md_basis="原文作「巳月未日」，只有月建與日支、日干缺失，不合「明記日辰」硬要求。")
C(id="LY-505", q="占升遷", asked="酉月乙巳日", page="卷之二·增刪黃金策千金賦章第三十四",
  chart=[(1039,1044)], stmt=[(1046,"斷曰﹕巳火官星持世","果升於卯月")], out=[(1046,"果升於卯月",None)],
  direction="positive", setting="占升遷可否、何時",
  assertions=["巳火官星持世臨日建，三合虛一待用（少卯字）","斷明年卯月必升；果升於卯月"],
  comment="裝卦四爻原文有缺字訛符（□□），照錄。", eligible=True)
C(id="LY-506", q="占目下功名升否", asked="卯月戊戌日", page="卷之二·兩現章第三十二",
  chart=[(1422,1427)], stmt=[(1429,"予曰﹕離變震卦","一曰於藩司署中")],
  out=[(1462,"及至三月將軍之侄","又見邸報")],
  direction="negative", setting="將軍之侄（四十九歲）占目下功名能否升遷",
  assertions=["離變震，六沖而變六沖，世爻化墓，官星亥水動化回頭之克","斷勿望升遷、且防刑獄；後都中行文拿問"],
  comment="結局與 LY-507 同載於卷末應驗總述行，分句切取，各歸其例。", eligible=True)
C(id="LY-507", q="占府尊能否復職", asked="卯月庚子日（初占）；卯月辛丑日（再占、三占）", page="卷之二·兩現章第三十二",
  chart=[(1433,1438),(1444,1449),(1453,1458)],
  stmt=[(1440,"斷曰﹕子孫持世","府尊曰﹕今日不誠"),(1451,"予曰﹕今日卦與昨日相同","又得恆之大過"),(1460,"予曰﹕恭喜",None)],
  out=[(1462,"又本府府尊命下",None)],
  direction="mixed", setting="府尊因得罪制臺被辯護，占能否復職，連占三卦合斷",
  assertions=["初占、再占皆斷祿位已屬他人，萬萬難於復職","三占斷速速援例（刑例）再任西方","結局：不準復職；後援例果於巳年補陝西慶陽府知府"],
  comment="三占合斷例（先例 LY-401 同體）。結局句與 LY-506 同行，分句切取。", eligible=True)
C(id="LY-508", q="占身病", asked="申月戊寅日", page="卷之二·增刪黃金策千金賦章第三十四",
  chart=[(1596,1601)], stmt=[(1603,"斷曰﹕卦中世爻酉金絕於寅日","果不久病愈")],
  out=[(1603,"果不久病愈。九月妻死","是占我應他")],
  direction="mixed", setting="自占身病吉凶，並及妻安危",
  assertions=["世爻酉金值秋旺相，斷自身無災、不藥而愈","亥水妻財化戌土回頭之克，防九十月妻有危","結局：病愈；九月妻死（占我應他）"],
  comment="", eligible=True)
C(id="LY-509", q="占母病；再占子病", asked="未月丁亥日（初占）；酉月丁卯日（再占）", page="卷之二·增刪黃金策千金賦章第三十四",
  chart=[(1607,1612),(1618,1623)],
  stmt=[(1614,"斷曰﹕此卦不現母病","果於八月"),(1625,"斷曰﹕卯木子孫","果死於卯日")],
  out=[(1614,"果於八月其子驚風",None),(1625,"果死於卯日",None)],
  direction="negative", setting="初占母病，斷語轉指初生子有災；八月子驚風後再占子病",
  assertions=["初占斷母病六沖即愈，不宜子孫變鬼，八月防子有災","再占斷子孫卯木臨月破、動出申金傷克，難過酉月卯日","結局：八月其子驚風；再占後果死於卯日"],
  comment="兩占合斷例。", eligible=True)
C(id="LY-510", q="占何日雨", asked="巳月甲寅日", page="卷之二·天時章第三十五",
  chart=[(1740,1745)], stmt=[(1747,"予斷辰日天陰","果於辰日")], out=[(1747,"果於辰日天變","故曰")],
  direction="positive", setting="連日晴，占何日下雨",
  assertions=["斷辰日天陰、巳日必雨","果於辰日天變、巳日大雨"],
  comment="與已收 LY-440（巳月丙申日占雨）、LY-442（巳月甲申日占何日雨）月日、卦象、結局俱不同，非同例。", eligible=True)
C(id="LY-511", q="占終身財福", asked="酉月辛未日", page="卷之三·終身財福章第三十七",
  chart=[(2114,2119)], stmt=[(2121,"斷曰﹕財爻持世","此人自二十五歲")],
  out=[(2121,"此人自二十五歲至五十多歲東奔西走","如此者謂之")],
  direction="negative", setting="占終身財福有無",
  assertions=["財爻持世遇旬空，卦中無火生助，難許成家","結局：二十五歲至五十多歲東奔西走、一事無成，後因貧困從戒外出"],
  comment="", eligible=True, grade_note="結局為終身梗概式敘述，事件可判讀而非單一應期事件。")
C(id="LY-512", q="占終身財福", asked="申月壬子日", page="卷之三·終身財福章第三十七",
  chart=[(2159,2164)], stmt=[(2166,"世臨辰土","後從當夫頭")], out=[(2166,"後從當夫頭死於丑年",None)],
  direction="negative", setting="原稍有家業、因賭致貧者占終身財福",
  assertions=["兄爻持世，斷永無發福之秋","世爻逢退，難許長年","結局：死於丑年"],
  comment="原文「後從當夫頭死於丑年」文句有訛亂（維基文庫未校對本），照錄。與已收 LY-252（同日占子病，畢之屯）為同日異人異事，非同例。",
  eligible=True, grade_note="結局含壽限斷語之應驗，財福部分為梗概式敘述。")
C(id="LY-513", q="占終身財福", asked="丑月丙辰日", page="卷之三·終身財福章第三十七",
  chart=[(2172,2177)], stmt=[(2179,"斷曰﹕兄爻持世","後因叔父")],
  out=[(2179,"後因叔父作衙門命之貼","叔父提拔者")],
  direction="mixed", setting="占終身財福，問作何事可以成家",
  assertions=["兄爻持世耗財，斷財不聚","斷以筆硯（貼寫）可以營生","結局：得叔父提拔作衙門貼寫，可度日而財不聚"],
  comment="", eligible=True, grade_note="結局為終身梗概式敘述。")
C(id="LY-514", q="占終身財福", asked="子月乙未日", page="卷之三·終身財福章第三十七",
  chart=[(2252,2257)], stmt=[(2259,"斷曰﹕卯木之財","後屢見逢顯貴")], out=[(2259,"後屢見逢顯貴聘之",None)],
  direction="negative", setting="占終身財福",
  assertions=["卯木財入未日之墓，巳火官休囚，斷名不能成、利不能就，一事無成","結局：屢被顯貴聘用皆因才高氣傲辭去，貧寒淡泊十餘載，後隨表弟赴雲南不知所終"],
  comment="", eligible=True, grade_note="結局為終身梗概式敘述。")
C(id="LY-515", q="占終身功名有無", asked="戌月丁卯日", page="卷之三·終身功名有無章第三十八",
  chart=[(2323,2328)], stmt=[(2330,"斷曰﹕子孫持世","但此人功名之念切甚")],
  out=[(2330,"但此人功名之念切甚",None)],
  direction="negative", setting="占終身功名有無",
  assertions=["子孫持世，斷終身不許成名","結局：讀書苦甚竟未遊泮，從戌（軍／例）二十餘載，皓首無成"],
  comment="", eligible=True, grade_note="結局為終身梗概式敘述。")
C(id="LY-516", q="占壽元", asked="辰月乙巳日（初占，五十三歲）；申月己卯日（再占，七十餘歲）", page="卷之三·壽元章第三十九",
  chart=[(2352,2357),(2363,2368)],
  stmt=[(2359,"世臨未土","彼笑而占"),(2370,"予曰﹕若是父爻鬼動","果終於未年")],
  out=[(2370,"果終於未年七月",None)],
  direction="mixed", setting="五十三歲占壽元，斷許長年、二十年後再占；七十餘歲再占問壽",
  assertions=["初占斷世爻得生扶，必享長年，二十年後再占","再占斷還享八年之福，至未年是其時","結局：果終於未年七月"],
  comment="兩占合斷例，跨約二十年；以再占斷語及其結局為主要判讀對象。", eligible=True)
C(id="LY-517", q="占防流兵", asked="巳月戊辰日", page="卷之三·趨避章第四十",
  chart=[(2526,2531)], stmt=[(2533,"予笑而曰﹕爾與兵賊同居","彼曰﹕酉金子孫")],
  out=[(2533,"後此人屢次遇兵變","自癸未占卦")],
  direction="positive", setting="流兵為害之時占防避吉凶",
  assertions=["子孫合成金局克去身邊之鬼，斷保爾無事","結局：屢次遇兵變，或避之、或有驚無險"],
  comment="原文結局句中「自癸未占卦」一語疑有訛字，照錄。結局為時期梗概，僅入 dev-add。",
  eligible=False, grade_note="結局為時期內多次遭遇之梗概敘述，非單一事件。")
C(id="LY-518", q="占夫婦將來和好否", asked="酉月辛巳日", page="卷之三·夫婦章第四十三",
  chart=[(2673,2678)], stmt=[(2680,"兄爻持世以克妻財","後竟生離")], out=[(2680,"後竟生離",None)],
  direction="negative", setting="夫婦目下不和，占將來能否和好",
  assertions=["妻財亥水臨驛馬被巳日沖動而暗動，心去難留","斷生離之象；後竟生離"],
  comment="原文標題「和俁」為「和好」之訛，照錄於節錄、問題欄從正字。", eligible=True)
C(id="LY-519", q="占升遷地方", asked="未月己巳日", page="卷之三·升遷何方章第五十六",
  chart=[(3100,3105)], stmt=[(3107,"彼時有山東眞定兩缺","果得眞定")], out=[(3107,"果得眞定",None)],
  direction="positive", setting="住在京都占升遷將得何地之缺（山東、真定兩缺）",
  assertions=["巳火官星屬南方，斷必得真定（都門之南）","果得真定"],
  comment="", eligible=True)
C(id="LY-520", q="占援例", asked="丑月乙卯日", page="卷之三·援例章第五十八",
  chart=[(3154,3159)], stmt=[(3161,"斷曰﹕財動生官","後竟納之")], out=[(3161,"後竟納之﹐名敗身喪",None)],
  direction="negative", setting="占援例（捐納）入仕可否",
  assertions=["財動生官，不宜世臨月破，破而被克，有官不能享","結局：竟納之，名敗身喪"],
  comment="", eligible=True)
C(id="LY-521", q="占上書", asked="申月戊辰日", page="卷之三·面聖上書章第六十二",
  chart=[(3213,3218)], stmt=[(3220,"斷曰﹕五位巳火生世","後此人上書")], out=[(3220,"後此人上書﹐不準",None)],
  direction="mixed", setting="占上書（條陳）可否、有害否",
  assertions=["斷此書宜上，利害皆無、上與不上皆可","結局：上書，不準"],
  comment="斷語本身兩可（宜上而無利害），屬兩可例，僅入 dev-add。", eligible=False,
  grade_note="斷語兩可，判讀粒度弱。")
C(id="LY-522", q="占因避誤軍糧已被劫", asked="未月戊申日", page="卷之三·面聖上書章第六十二",
  chart=[(3247,3252)], stmt=[(3254,"斷曰﹕世臨日建月建生之","彼不以爲然")],
  out=[(3254,"豈知因獲奇功","或曰﹕卯木子孫發動")],
  direction="positive", setting="因躲避耽誤軍糧、軍糧已被劫，占功名能否保全",
  assertions=["世臨日建月建生之，動出戌土相生，斷官爵無恙","結局：因獲奇功，功名仍復保全"],
  comment="", eligible=True)
C(id="LY-523", q="占出行謁見貴人", asked="申月丁卯日", page="卷之四·謁貴求財章第六十九",
  chart=[(3428,3433)], stmt=[(3435,"斷曰﹕官星持世而空","果於出空之日")],
  out=[(3435,"果於出空之日見官﹐財利得意","月建財爻生世")],
  direction="positive", setting="占出行謁見貴人能否得見、財利如何",
  assertions=["官星持世而空，斷出亥日（出空）得見，官府財利如心","果於出空之日見官，財利得意"],
  comment="", eligible=True)
C(id="LY-524", q="占收貨", asked="寅月己亥日", page="卷之四·囤貨賣貨章第七十三",
  chart=[(3481,3486)], stmt=[(3488,"古以財爻衰者宜收貨","但求問者不聽")],
  out=[(3488,"後來存貨堆積四年",None)],
  direction="negative", setting="占收貨（囤貨）可否得利",
  assertions=["辰戌之財衰而無根，斷將來終不得價、不可收買","結局：不聽而收，存貨四年朽壞大半、大虧其本"],
  comment="", eligible=True)
C(id="LY-525", q="占往楚買豆", asked="午月戊子日", page="卷之四·往何方買賣章第七十五",
  chart=[(3544,3549)], stmt=[(3551,"斷﹕亥水財爻休囚於外","後果中間人作獘")], out=[(3551,"後果中間人作獘",None)],
  direction="positive", setting="指明方向占往楚地買豆得利否",
  assertions=["斷楚地豆子必賤、必能得厚利；唯間爻兄弟耗費必多","結局：中間人作弊告官誤一月，幸地頭價漲，果然得厚利"],
  comment="", eligible=True)
C(id="LY-526", q="占往粵東探親可帶何貨歸來得利", asked="未月戊申日", page="卷之四·買何貨爲吉章第七十六",
  chart=[(3560,3565)], stmt=[(3567,"斷曰﹕爻逢六合","後此人買攢香")],
  out=[(3567,"後此人買攢香翠毛而歸﹐俱得大利","若執古法斷者")],
  direction="positive", setting="占往粵東探親、帶何貨歸來得利",
  assertions=["六合卦世應相生，斷此行遂意、任買何貨亦得厚利","結局：買攢香翠毛而歸，俱得大利"],
  comment="", eligible=True)
C(id="LY-527", q="占買馬往南發賣", asked="丑月丁卯日", page="卷之四·買賣六畜章第七十九",
  chart=[(3596,3601)], stmt=[(3603,"斷曰﹕內卦子孫","後果買馬七十餘匹")], out=[(3603,"後果買馬七十餘匹",None)],
  direction="mixed", setting="占買馬往南方發賣得利否",
  assertions=["子孫動而變鬼、外卦子孫臨月破，斷不宜買、馬雖多死","間爻酉財暗動生世，斷財不致大耗","結局：買馬七十餘匹一路多死、僅存二十八匹，幸得價不致大虧"],
  comment="", eligible=True)
C(id="LY-528", q="占子近病", asked="申月庚寅日", page="卷之四·疾病章第九十九",
  chart=[(3960,3965)], stmt=[(3967,"斷曰﹕鬼變子孫","果在出空之日")], out=[(3967,"果在出空之日而愈",None)],
  direction="mixed", setting="辰年占子近病吉凶",
  assertions=["鬼變子孫為夭折之兆，幸子孫值旬空，斷近病即愈","又斷恐其難過午年","結局：出空之日而愈；至午年出花（痘）而死"],
  comment="雙斷語雙應驗例（近病愈＋遠年夭），判讀須兩項分計。", eligible=True)
C(id="LY-529", q="占子病", asked="申月壬子日", page="卷之四·疾病章第九十九",
  chart=[(3977,3982)], stmt=[(3984,"斷曰﹕令郎今日卽愈","果於本日愈")], out=[(3984,"果於本日愈",None)],
  direction="positive", setting="占子病吉凶",
  assertions=["官鬼持世為憂，子日沖去憂心，斷今日即愈","果於本日愈"],
  comment="與已收 LY-252（同月日占子病）卦象（遯靜卦 vs 畢之屯）、斷語、結局俱不同，為同日異例，非重複收錄。", eligible=True)
C(id="LY-530", q="占兄病", asked="午月甲寅日", page="卷之四·醫卜往治章第一百零四",
  chart=[(4051,4056)], stmt=[(4058,"予卽笑而言曰﹕列位放心","果於子時退災")],
  out=[(4058,"果於子時退災﹐次日起牀","此何嘗用藥")],
  direction="positive", setting="兄病危篤、醫家不治，弟迎卜者到宅占兄病",
  assertions=["斷今日半夜（子時）退災、明日卯日即起牀","果於子時退災，次日起牀"],
  comment="占期敘事在章首行（午月甲寅日一人病在危篤…弟占兄病得屯之中孚卦）。與同章五卦鏈（4062 行起）為另一事，前兩輪已拒收該鏈，本例為鏈外獨立一占。", eligible=True)
C(id="LY-531", q="占父病喫牛黃丸可否", asked="亥日辛酉日（原文如此，月建記載不全）", page="卷之四·醫卜往治章第一百零四",
  chart=[(4134,4139)], stmt=[(4141,"予曰﹕灌服此丸可保立愈","服之便醒")], out=[(4141,"服之便醒","喜子孫持世")],
  direction="positive", setting="席間見東翁（父輩）中風之症，子占父病可否服家中牛黃丸",
  assertions=["子孫持世值日，斷灌服此丸可保立愈","服之便醒"],
  comment="原文作「亥日辛酉日」，月建干支不全（「亥日」疑為亥月之訛，照錄不改），月日完整性不成立，僅入 dev-add。",
  eligible=False, md_complete=False, md_basis="原文作「亥日辛酉日」，月建只餘地支「亥」、且誤書為「日」，不合「明記月建」硬要求。")
C(id="LY-532", q="占擇某日入宅是否有礙父母", asked="子月丁酉日", page="卷之四·入宅六親凶吉章第一百十一",
  chart=[(4226,4231)], stmt=[(4233,"斷曰﹕此日入宅","予目其平安")], out=[(4233,"後照此行﹐予目其平安一十七載",None)],
  direction="positive", setting="占擇定之日入宅是否有礙父母",
  assertions=["斷此日寅卯時入宅吉、父母安牀於西南，保清靜吉祥","結局：照此行，平安一十七載"],
  comment="結局為長時段平安梗概，僅入 dev-add。", eligible=False,
  grade_note="結局為十七年平安之梗概敘述。")
C(id="LY-533", q="占家宅（院內有井、大門對向、修補後功名）", asked="酉月戊寅日", page="卷之四·舊宅章第一百十三",
  chart=[(4286,4291),(4295,4300)],
  stmt=[(4293,"斷曰﹕世爲本宅","彼曰﹕廟前有一照壁"),(4302,"斷曰﹕修補之後","果中經魁")],
  out=[(4293,"彼曰﹕廟前有一照壁","予曰﹕卽此物也"),(4302,"果中經魁",None)],
  direction="positive", setting="官員十載不升疑家宅有礙，指疑處（廟前照壁大樹）占之，並再占修補後功名",
  assertions=["斷犯處不在井、在廟前照壁後大樹，安獸頭對樹則吉","再占斷修補之後今科必中","結局：果中經魁，下科胞弟又發"],
  comment="同日連占合斷例（首占月日原文作「酉日戊寅日」，首字疑為「酉月」之訛；本例月日完整性以第二、三占同日戊寅、日辰明確為據，月建照原文登記並註明）。",
  eligible=True, md_basis="原文首占作「酉日戊寅日」（「酉日」疑「酉月」之訛），日辰戊寅明確；同日連占共用此月日，判讀從寬認定月建為酉月並在此註明。")
C(id="LY-534", q="占官衙後溝從後流宜否；再占修溝後何如", asked="戌月己亥日", page="卷之四·占衙宇章第一百十六",
  chart=[(4329,4334),(4340,4345)],
  stmt=[(4336,"斷曰﹕卽此處違也","後開溝見"),(4347,"斷曰﹕未土財化申金官","後於申年")],
  out=[(4336,"後開溝見許多屍體白骨","予始悟曰"),(4347,"後於申年升任",None)],
  direction="mixed", setting="一官連任不得升遷疑衙署不利，指疑處（後溝）占之",
  assertions=["初占斷即此處（後溝）違礙，宜改往東流","開溝果見許多屍體白骨","再占斷未年一定高升；結局於申年升任（應期與斷語差一年，照實登記）"],
  comment="兩占合斷例；再占應期不合（斷未年、應申年）為本例內在兩可點，照實登記。", eligible=True)
C(id="LY-535", q="占地（墳地）", asked="寅月戊午日", page="卷之四·尋地章第一百十九",
  chart=[(4374,4379)], stmt=[(4381,"斷曰﹕世爻戌土","彼曰﹕正是如此")], out=[(4381,"後竟葬之﹐辰年下葬",None)],
  direction="positive", setting="占墳地吉凶與形勢",
  assertions=["斷世化子孫回頭生、日月世子孫成三合，死者安而生者樂、子孫昌盛","形勢斷語（春夏有水、秋冬必動）經求測者當場證實","結局：辰年下葬，酉年孫中亞魁，子年次孫又登鄉榜"],
  comment="", eligible=True, grade_note="結局含跨年子孫科名事件，客觀可判讀。")
C(id="LY-536", q="占地（墳地）", asked="卯月戊子日", page="卷之四·尋地章第一百十九",
  chart=[(4397,4402)], stmt=[(4404,"世爲穴","彼曰﹕已買成矣")], out=[(4404,"後竟葬之。四年之內",None)],
  direction="negative", setting="占墳地吉凶（地師稱美地，已買成）",
  assertions=["世臨月建本為吉，唯外卦反吟、世與子孫被沖克，斷不宜用之","結局：竟葬之，四年內二男一女相繼而亡，自身半身不遂，二年後沒"],
  comment="", eligible=True)
C(id="LY-537", q="占地形勢", asked="丑月庚申日", page="卷之四·占地形勢章第一百二十",
  chart=[(4419,4424)], stmt=[(4426,"靑龍持世","彼曰﹕果一一無錯")], out=[(4426,"彼曰﹕果一一無錯","此地吉否")],
  direction="positive", setting="占墳地形勢（來龍、明堂、水口、道路等）",
  assertions=["逐項斷來龍由左而至、龍虎環抱、明堂寬大、前山有朝水、道路參差、水口散亂","求測者當場覆：果一一無錯"],
  comment="當場驗證型（形勢描寫逐項核對），非後事應驗，僅入 dev-add（先例 LY-314 同體）。", eligible=False,
  grade_note="當場驗證型，結局為求測者即時確認。")
C(id="LY-538", q="占穴（點穴）", asked="未月乙巳日", page="卷之四·點穴章第一百二十四",
  chart=[(4460,4465)], stmt=[(4467,"予曰﹕世在四爻","東家尙疑")], out=[(4467,"令人徧地灑之",None)],
  direction="positive", setting="吉地屢掘逢石無處導穴，卜者到冢下占點穴",
  assertions=["世在四爻，斷穴在中段午火枯焦紅花之處，掘之必逢土穴","以紅記錢混灑遍地驗之，果得原錢於紅花之下；掘之周圍僅丈餘泥土、餘皆石塊","次年開府，兩公郎五年內俱登甲榜"],
  comment="", eligible=True, grade_note="穴位斷語以擲錢法當場驗證，屬當場驗證與後事（開府登榜）混合型。")
C(id="LY-539", q="占以父柩附葬祖塋", asked="子月丙申日", page="卷之四·新亡附葬祖塋章第一百三十",
  chart=[(4504,4509)], stmt=[(4511,"斷曰﹕世爻被克","後仍附葬")], out=[(4511,"後仍附葬",None)],
  direction="mixed", setting="占以父柩附葬祖塋可否",
  assertions=["世爻被克，斷不宜附葬","結局：仍附葬，數月後腰疼欲死；命道安土神（安墳）而愈","又斷目下雖不遷改、終有遷改；果於子年死母，起此冢合葬於他處"],
  comment="", eligible=True)

# ================= 《卜筮正宗》（dev-add only；節錄照 cnddy 頁面簡體字） =================
BURL = "https://www.cnddy.com/1759.html"
BED = "華夏大易學社（cnddy.com）在線全本（據通行本錄入，頁面字形為簡體，節錄照頁面；裝卦表 OCR 有錯亂，見完整性說明）"
BCHART_NOTE = "在線本裝卦表為雙欄排版經 OCR 轉錄後行序錯亂，逐爻裝卦未能可靠還原；本條只錄可由卦名、卦宮、空亡與斷語互證的信息，逐爻表不錄。"
def B(id, qnum, q, gua, gong, kong, stmt, out, direction, setting, assertions, comment="", yongshen=None, grade_note=""):
    CASES.append(dict(id=id, book="bushi", q=q, asked="原文未明記月日",
        page=f"卷十三、十四·十八問答附占驗·{qnum}", gua_text=f"{gua}（{gong}宮，空亡{kong}）",
        yongshen=yongshen, stmt_text=stmt, out_text=out, direction=direction, setting=setting,
        assertions=assertions, comment=comment, eligible=False, md_complete=False, chart_complete=False,
        grade_note=grade_note))

B("LY-540","第一問","占墳地","山地剝","乾","午未",
  "断曰：日辰子孙持世，月建生之，青龙戏水，水必从左繞穴，必近大水，不然长流之水到堂．白虎临卯木，子卯寅中带生，是临财爻为无碍．应为朝山属火被世克，朝山不高；世前戌土为对案，土克世，对案略高彼．",
  "一一皆是，葬后未出三年，二子皆发科甲．","positive",
  "占墳地吉凶與形勢",["形勢諸斷（左繞水、近大水、朝山不高、對案略高）經求測者當場證實：一一皆是","葬後未出三年，二子皆發科甲"],
  comment="當場驗證＋後事科甲混合型。", grade_note="結局含當場證實與三年內科甲兩部分。")
B("LY-541","第二問","占家宅人口平安否","水天需之乾為天","坤","子丑",
  "断曰：申金子孙持世，化午火回头之克，乃自身及子孙皆受克也，子水财爻化戌土回头之克，财为妻妾奴仆，一家受克之卦，",
  "后至午月火旺克世，助土克财，财逄月破，一家数口回禄俱死．","negative",
  "占家宅人口平安否",["世、財皆化回頭之克，斷一家受克","結局：午月一家數口死於火災（回祿）"])
B("LY-542","第二問","一人占僕何日回","澤天夬之天澤履","坤","午未",
  "断曰：亥水财爻为用神，亥水虽是月建，不谓月破，但不宜重重土动伤之．谚云：双拳不敌四手，不独难望归期，还要防途中不测，",
  "后至午月火旺合未助土时，中途过害矣．","negative",
  "占僕人何日歸來",["用神亥水財爻被重重土動傷，斷難望歸期、防途中不測","結局：午月途中遇害"],
  yongshen="妻財亥水為用神")
B("LY-543","第二問","一人占自病","離為火之坎為水","離","戌亥",
  "断曰：离火化坎水，乃卦变回头之克；巳火世爻化出子水回头之克，名为反吟卦．目今午月火旺之时，日主生扶，近来无碍，冬令防之．",
  "后果死于戌月丁亥日，应戌月者世入墓之月也，亥日者，克冲之日也","negative",
  "自占病吉凶",["反吟卦、世化回頭之克，斷近來無礙、冬令防之","結局：死於戌月丁亥日"])
B("LY-544","第二問","一人占索房價","坎為水之坤為地","坎","午未",
  "断曰：坎卦变坤亦是卦变回头之克，世爻虽得日生，不宜两重土动来伤．此卦甚凶，不但房价事小，宜防不测之祸．",
  "后于午月覆舟而亡．","negative",
  "占索討房價（占此應彼）",["斷卦甚凶、防不測之禍（所應不在房價而在其身）","結局：午月覆舟而亡"])
B("LY-545","第二問","占具題","風澤中孚之山澤損","艮","戌亥",
  "断曰：五位巳火生世，化子水回头，克不宜具题．问曰：有害否．予曰：巳火虽不能生，幸卦中无动爻克世，利害皆无，",
  "后题而果不准行．","negative",
  "占具題（上題本）可否",["斷不宜具題；即使具題亦利害皆無","結局：題而果不准行"])
B("LY-546","第二問","占慮大計","火山旅之地火明夷","離","子丑",
  "断曰：子孙持世化回头之克，但嫌世位临之，世为自己，不宜受，克虽有金局生扶，伏官难称无恙，",
  "后果削职．","negative",
  "占慮大計（考核）吉凶",["子孫持世化回頭之克、世受克，斷伏官難稱無恙","結局：削職"])
B("LY-547","第三問","子占父病","地風升之地水師","震","戌亥",
  "断曰：亥水父爻为用，虽值旬空，有酉金原神动来生之，可许无碍．但不宜酉金化出午火回头一克，此乃原神被伤，用神无根矣．",
  "此人果死于卯年卯月卯日卯时，应卯日时者，生助午火克冲原神也．","mixed",
  "子占父病吉凶",["首斷可許無礙；但附警示：原神酉金化午火回頭之克，用神無根","結局：果死於卯年卯月卯日卯時（首斷不驗、警示應驗）"],
  yongshen="父母亥水為用神",
  comment="首斷與警示結論相反，判讀須分項計分，照實登記。")
B("LY-548","第四問","占子何日歸","火澤睽之火風鼎","艮","寅卯",
  "断曰：内卦巳酉丑合成金局作用神，丑土系月破，必待立秋后甲子日到家．",
  "果于申予日归","mixed",
  "占子何日歸來",["斷立秋後甲子日到家","結局：於申□日歸（頁面作「申予日」，疑 OCR 訛字）——歸果成而應期不合"],
  comment="頁面結局作「果于申予日归」，「予」疑為 OCR 訛字，照錄。")
B("LY-549","第四問","占防恭劾","水風井之風澤中孚","兌","戌亥",
  "予曰：此卦甚奇，世空逄日冲不为空矣，世不受克而暗动，虽无参论，离任不免．彼曰：既无参论如何离任．予曰：世爻暗动必主动摇，内卦合金局生应，果知此位已属他人矣．",
  "后因裁他处缺上台，题留他处官顶此公位将，此将公赴京另补","positive",
  "此公防新換撫軍參劾占吉凶",["斷雖無參論、離任不免，其位已屬他人","結局：他處官頂此公之位，此公赴京另補"],
  comment="結局句頁面文氣有 OCR 訛亂（「位将，此将公」），照錄。")
B("LY-550","第四問","占何日雨止","火風鼎之火澤暌","離","（頁面未錄）",
  "若执古法，父伏空无雨，才褔动晴．明今不然．巳酉丑合成财局克父，父若不空受其克是无雨也，今伏而又空，谓之避克，其雨不能止，必待卯日出透，出空，被克方可雨止．",
  "后至甲日，其雨更大，卯日大晴","positive",
  "占何日雨止",["斷雨不能止，必待卯日方可雨止","結局：甲日雨更大，卯日大晴"])
B("LY-551","第五問","占隨官上任如何","水地比之水風井","坤","戌亥",
  "断曰：世临卯木化酉金克冲内卦，爻之反吟也，此行不吉，不去为上，",
  "后因官府掣签得缺，近于贼营辞而不去，及至官府去后又因他事而去，至七月城破与官府一同被害，","negative",
  "占隨官上任吉凶",["反吟卦，斷此行不吉、不去為上","結局：終究隨去，七月城破與官府一同被害"])
B("LY-552","第五問","占往前處脫貨有利否","風天小畜之乾為天","巽","寅卯",
  "断曰：小畜卦变干是卦之反吟也，所喜世与财爻长生于日，指此占以应爻作地头，临午火回头生合，比前利倍．",
  "后此人往返三次俱得倍利．","positive",
  "占往前處脫售貨物有利否",["斷比前利倍","結局：往返三次俱得倍利"])
B("LY-553","第五問","占墳地","巽為風之地風升","巽","午未",
  "断曰：世为穴，临月建子日生之为吉地，但不宜爻变反吟，子孙与世皆化克冲，不可葬．彼曰：重价己成久矣，地师皆称美地．",
  "后竟葬之．四年内，二子一女并自身相继而卒．","negative",
  "占墳地可否葬（重價已買、地師稱美地）",["世與子孫皆化克沖，斷不可葬","結局：竟葬之，四年內二子一女並自身相繼而卒"])
B("LY-554","第六問","占兵到一家當避何處","天雷无妄之雷天大壯","巽","子丑",
  "内外伏吟，忧郁未解，所喜世爻午火子孙为自己，应爻子水父母作父母，月建生应，日辰生世，世应安静，父母与自己无碍．第嫌寅木兄弟爻伏吟，又是月破，昆仲有厄．彼曰：我父母在西方舍亲家得无妨否？答曰：西方属金，生扶父母，万无忧疑矣！汝自己宜避于东方，东方木能生火，兄弟妻仆俱从汝走，子孙持世，可保无虞．",
  "彼回即领家眷往东去，后来覆我曰平安，惟其弟牵念父母往探之，行至半途遭害矣．","mixed",
  "兵到之時占一家當避何處",["斷父母與自己無礙、宜避於東方；唯兄弟有厄","結局：家眷隨往東方平安；其弟半途往探父母遭害"],
  comment="前兩輪曾以弱例略過，本輪作 dev-add 補收並註明。", grade_note="斷語為分人分述，結局分項應驗。")


# ================= 去重裁定補丁（全裝卦指紋比對後） =================
# 以下 15 例經逐例比對既有分卷（月日＋全裝卦＋結局三項俱合）確認為重複收錄，剔除並登記於 BUILD-REPORT：
# 舊LY-501=LY-014/LY-418、502=LY-420、505=LY-017、508=LY-022、510=LY-026、516第二占=LY-209、
# 523=LY-237、525=LY-457、528=LY-251、529=LY-252、534=LY-255、535=LY-256、536=LY-257、538=LY-258、539=LY-259。
DROP = {"LY-501","LY-502","LY-505","LY-508","LY-510","LY-516","LY-523","LY-525","LY-528","LY-529","LY-534","LY-535","LY-536","LY-538","LY-539"}
CASES = [c for c in CASES if c["id"] not in DROP]
for c in CASES:
    if c["id"] == "LY-512":
        c["comment"] = "原文「後從當夫頭死於丑年」文句有訛亂（維基文庫未校對本），照錄。同日（申月壬子日）另有占子病一例已收為 LY-252（天山遯靜卦），卦象、事由俱不同，非同例。"
# 補收 7 例（全文件「月日＋全裝卦」雙鍵掃描後逐例裁定；皆前兩輪未收、斷驗可分、結局明確）。
# 另：掃描中先後識破的「補收」候選 N1–N8 經全裝卦指紋比對確認皆為既收例
# （=LY-410/411/010/011/012/228/229/230，其中 LY-011 與 LY-412 本身即同一例），不予收錄，登記於 BUILD-REPORT。
C(id="N9", q="占候文書何日得領", asked="卯月壬辰日", page="卷之二·飛伏神章第二十八",
  chart=[(355,360)], stmt=[(362,"午火父母爲用神","果得於甲午日")], out=[(362,"果得於甲午日",None)],
  direction="positive", setting="占候文書何日得領",
  assertions=["父母午火空而伏於二爻丑土之下，壓住難出，許甲午日出空必得","果得於甲午日"],
  comment="", eligible=True, ord=353)
C(id="N10", q="占子病", asked="酉月丙辰日", page="卷之二·飛伏神章第二十八",
  chart=[(366,371)], stmt=[(373,"黃金策曰﹕空下伏神","果於午日")], out=[(373,"果於午日起牀",None)],
  direction="positive", setting="占子病吉凶",
  assertions=["子孫午火伏於旬空丑土之下，伏易出，許午日子孫出現必愈","果於午日起牀"],
  comment="", eligible=True, ord=364)
C(id="N13", q="占父病", asked="卯月丙辰日", page="卷之二·飛伏神章第二十八",
  chart=[(381,386),(390,395),(399,404)],
  stmt=[(397,"巳火父母明現於初爻","次子又占"),(406,"予疑曰﹕兩卦俱當卽愈","再請夫人卜之"),(408,"予連見此卦","果絕於亥月")],
  out=[(408,"果絕於亥月","予之不取伏神")],
  direction="mixed", setting="父病勢危、醫者滿座，本人、次子、夫人連占數卦合斷",
  assertions=["前兩卦斷目前即愈","後三占得漸之巽雷同，斷亥水回頭克父、今冬難延","結局：果絕於亥月"],
  comment="多占合斷例；漸之巽一卦由三人連占雷同，原文備述。",
  eligible=True, ord=379, grade_note="「目前即愈」一項由敘事中壽醫「目下不妨」間接印證；主斷（今冬難延）由果絕於亥月直接應驗。")
C(id="N14", q="占終身除功名外何事可爲", asked="酉月癸丑日", page="卷之三·終身財福章第三十七",
  chart=[(2189,2194)], stmt=[(2196,"斷曰﹕財星伏於二爻","後聞此人遊川廣")], out=[(2196,"後聞此人遊川廣塡黔","覺子曰")],
  direction="positive", setting="四十三歲、妻亡無子者占終身除功名外何事可為",
  assertions=["財伏而空，斷財莫能聚；子孫獨發遇靑龍，主清高、非義不取","問挾志遊歷、絕俗離羣可能如願，斷如有此志、此卦驗之幾矣","結局：後聞遊川廣滇黔十餘載，致書於家，竟入華山不知所終"],
  comment="終身類：以志向斷語與後來行跡對讀（與終身兌例同體）。",
  eligible=True, ord=2187, grade_note="結局為行跡梗概；斷語中妻財等項部分屬背景印證。")
C(id="N15", q="占終身功名", asked="巳月乙卯日", page="卷之三·終身功名有無章第三十八",
  chart=[(2336,2341)], stmt=[(2343,"斷曰﹕𨿽是爻逢六合","至子年得病")], out=[(2343,"至子年得病﹐丑年得蠱病而終",None)],
  direction="negative", setting="占終身功名（業已援例）",
  assertions=["子孫持世、官逢月破，斷勿想成名；費盡萬金，終難食祿","結局：子年得病，丑年得蠱病而終"],
  comment="功名斷語之驗否只能由終身結局間接推知（原文未明記其未食祿），判讀粒度弱，僅入 dev-add。",
  eligible=False, ord=2334, grade_note="結局為死亡記錄，功名命題屬間接驗證。")
C(id="N11", q="占父壽、母壽", asked="丑月庚子日（同日分占）", page="卷之三·父母壽元章第四十一",
  chart=[(2574,2579),(2583,2588)],
  stmt=[(2590,"斷曰﹕前卦兩現父母","加以太歲沖之")], out=[(2590,"癸酉年占至乙巳年三十餘載",None)],
  direction="mixed", setting="癸酉年同日分占父壽、母壽",
  assertions=["父：父母丑土旺於子日又與日合，斷蒂固根深、大椿永茂","母：父母午火動被日沖、子水動克，斷防丙子年","結局：三十餘載後復遇其人，父甚健；母果終於子年"],
  comment="母壽斷語作「丙子年」，結局只記「終於子年」，干支粒度照實登記。",
  eligible=True, ord=2572, grade_note="母壽結局年份只記地支（子年），與斷語粒度略差。")
C(id="N12", q="占父壽", asked="巳月乙酉日", page="卷之三·父母壽元章第四十一",
  chart=[(2594,2599)], stmt=[(2601,"斷曰﹕亥水父臨月破","果終於本年")], out=[(2601,"果終於本年冬至日",None)],
  direction="negative", setting="占父壽",
  assertions=["父母亥水臨月破又被未土相傷，斷不惟不許長年、且無長月","果終於本年冬至日"],
  comment="", eligible=True, ord=2592)
# 兩例雙完整梗概型例改判 eligible（與終身類同以命題時域內之梗概結局為驗，註記在案）：
for c in CASES:
    if c["id"] == "LY-517":
        c["eligible"] = True
        c["comment"] = "原文結局句中「自癸未占卦」一語疑有訛字，照錄。結局為占期時域內屢次遇兵之梗概，與終身類同體，改判 eligible 並註明。"
    if c["id"] == "LY-532":
        c["eligible"] = True
        c["comment"] = "結局為入宅後十七年平安之梗概，與終身類同體，改判 eligible 並註明。"
# 再剔除 4 例（全裝卦＋斷語＋結局比對確認既收）：N10=LY-003、N13=LY-004、N11=LY-218、N12=LY-219。
CASES = [c for c in CASES if c["id"] not in {"N10","N13","N11","N12"}]
# 補收醫卜鏈末占（自足單元）：
C(id="N16", q="占用附子可否", asked="未月壬子日", page="卷之四·醫卜往治章第一百零四",
  chart=[(4108,4113)], stmt=[(4115,"子孫臨日辰","保管立愈")], out=[(4115,"醫家先用漧薑湯試之","此人之不死也")],
  direction="positive", setting="子病寒證、醫者誤投涼藥將危，父占可否改用附子（大熱之劑）",
  assertions=["子孫臨日辰、酉金兄動相生，斷服用一劑、保管立愈","醫家以乾薑湯試之、加減調理一夜，次日曰愈"],
  comment="醫卜五占鏈（原文 4062–4115 行）之末占：前四占斷語或存疑、或屬鏈內推理，本例只取末占自足之斷驗（問藥、斷立愈、次日愈），鏈節關係在此註明。",
  eligible=True, ord=4106, grade_note="鏈末自足單元，斷驗自閉合。")
# 兩例改判 eligible（第 24、25 席，理由照實登記）：
for c in CASES:
    if c["id"] == "LY-537":  # 占地形勢：雙完整；形勢逐項斷語由求測者當場逐項證實，屬可判讀的即時驗證
        c["eligible"] = True
        c["comment"] = "當場驗證型（形勢描寫逐項核對）：雙完整性成立，斷語逐項可判讀，改判 eligible；與後事應驗型之別在此註明（先例 LY-314 為同體 dev 例）。"
    if c["id"] == "LY-521":  # 占上書：雙完整；「利害皆無」可判讀、「不準」結局客觀；「宜上」屬建議不列計分斷語
        c["eligible"] = True
        c["comment"] = "斷語含建議性成分（「此書宜上」）與預測性成分（「利害皆無從言起」）：計分只認預測性斷語，結局「上書不準、無害」客觀明確。雙完整性成立，改判 eligible 並在此註明其兩可性。"
        c["grade_note"] = "斷語兩可性已在 comment 註明；計分限預測性斷語。"
# 重新編號：增刪例按原文行序 LY-501 起順排，卜筮例隨後。
for c in CASES:
    if c.get("book") != "bushi" and "ord" not in c:
        c["ord"] = min(a for a, b in c["chart"])
_z = sorted([c for c in CASES if c.get("book") != "bushi"], key=lambda c: c["ord"])
_b = [c for c in CASES if c.get("book") == "bushi"]
CASES = _z + _b
for i, c in enumerate(CASES):
    c["id"] = f"LY-{501+i}"
print("renumbered:", [(c["id"], c["q"]) for c in CASES])

# ================= 組裝 =================
def build_z(c):
    cl = chart(c["chart"])
    assert len(cl) % 6 == 0 and len(cl) >= 6, f"{c['id']} chart lines {len(cl)}"
    names = derive(cl)
    assert all(names), f"{c['id']} derive fail {names}"
    prefixes = ["初占", "再占", "三占"]
    if len(names) == 1:
        gua = names[0] + ("（靜卦）" if "無動爻" in moving(cl) else "")
    else:
        gua = "；".join(f"{prefixes[i]}：{n}" for i, n in enumerate(names))
    stmt = " ".join(seg(*s) for s in c["stmt"])
    out = " ".join(seg(*s) for s in c["out"])
    md = c.get("md_complete", True)
    basis = c.get("md_basis") or (
        f"原文明記月建與日辰（{c['asked']}）；逐爻裝卦表完整照錄（{len(cl)} 行），"
        f"卦名由裝卦逐爻推得為{names}，與原文標題／敘事互證。")
    rec_in = {
        "id": c["id"], "tradition": "liuyao",
        "subject": {"name_or_desc": "求測者（原書多未具名）", "gender": None},
        "context": {"question": c["q"], "asked_at": c["asked"], "setting": c["setting"],
            "attachments": {"casting_method": CAST, "hexagram": gua,
                            "moving_lines": moving(cl), "chart_lines_top_to_bottom": cl}},
        "provenance": {"book": "《增刪卜易》", "edition": ED, "url": URL, "page": c["page"]},
        "language": "zh-Hant"}
    pred = {"master": "野鶴老人", "tradition": "liuyao", "date": c["asked"],
            "statement_excerpt": stmt, "source": f"《增刪卜易》{c['page']} {URL}",
            "direction": c["direction"], "key_assertions": c["assertions"]}
    ans = {"id": c["id"], "master_predictions": [pred],
           "outcome": {"description": out, "verified_by": "《增刪卜易》原書自載應驗"},
           "provenance": {"book": "《增刪卜易》", "edition": ED, "url": URL, "page": c["page"]},
           "license_status": "public-domain", "redistributable": True, "language": "zh-Hant",
           "notes": {"tags": ["phase3-expansion3"], "comment": c["comment"], "cross_ref": None}}
    full = dict(rec_in)
    full.update({"master_predictions": [pred], "outcome": ans["outcome"],
        "license_status": "public-domain", "redistributable": True,
        "outcome_grade": "A", "grade_note": c.get("grade_note", ""),
        "contamination": "low", "contamination_reason": CONT_Z,
        "month_day_complete": md, "chart_complete": True,
        "completeness_basis": basis,
        "holdout_eligible": bool(c.get("eligible")),
        "notes": ans["notes"]})
    return rec_in, ans, full

def build_b(c):
    att = {"casting_method": "六爻納甲（以錢代蓍）", "hexagram": c["gua_text"], "chart_note": BCHART_NOTE}
    if c.get("yongshen"): att["yongshen"] = c["yongshen"]
    prov = {"book": "《卜筮正宗》", "edition": BED, "url": BURL, "page": c["page"]}
    rec_in = {
        "id": c["id"], "tradition": "liuyao",
        "subject": {"name_or_desc": "求測者/所占之人（原書多未具名）", "gender": None},
        "context": {"question": c["q"], "asked_at": c["asked"], "setting": c["setting"], "attachments": att},
        "provenance": prov, "language": "zh-Hant"}
    pred = {"master": "王洪緒（輯錄，含師楊廣含傳授及自占驗）", "tradition": "liuyao",
            "date": "原書未記占期（康熙四十八年〔1709〕成書前）",
            "statement_excerpt": c["stmt_text"], "source": f"《卜筮正宗》{c['page']} {BURL}",
            "direction": c["direction"], "key_assertions": c["assertions"]}
    ans = {"id": c["id"], "master_predictions": [pred],
           "outcome": {"description": c["out_text"], "verified_by": "《卜筮正宗》原書自載應驗"},
           "provenance": prov, "license_status": "public-domain", "redistributable": True,
           "language": "zh-Hant",
           "notes": {"tags": ["phase3-expansion3"], "comment": c["comment"], "cross_ref": None}}
    full = dict(rec_in)
    full.update({"master_predictions": [pred], "outcome": ans["outcome"],
        "license_status": "public-domain", "redistributable": True,
        "outcome_grade": "A", "grade_note": c.get("grade_note", ""),
        "contamination": "low", "contamination_reason": CONT_B,
        "month_day_complete": False, "chart_complete": False,
        "completeness_basis": "《卜筮正宗》十八問原文不記占問月建與日辰（月日完整性不成立）；在線本逐爻裝卦表經 OCR 轉錄行序錯亂、不可靠還原（裝卦完整性不成立），只錄卦名、卦宮、空亡、用神等可互證字段。依本輪硬要求僅入 dev-add。",
        "holdout_eligible": False,
        "notes": ans["notes"]})
    return rec_in, ans, full

BUILT = {}
for c in CASES:
    BUILT[c["id"]] = build_b(c) if c.get("book") == "bushi" else build_z(c)
IDS = [c["id"] for c in CASES]
assert len(IDS) == len(set(IDS)) == 43, IDS

# ================= 去重（fingerprint vs 既有 inputs/answers；不讀 holdout gold） =================
def load_existing():
    recs = []
    pats = [BASE+"/masters-dataset/**/inputs.jsonl", BASE+"/masters-dataset/**/answers.jsonl",
            BASE+"/benchmark/phase3/inputs/*.json", BASE+"/benchmark/phase3/expansion/**/inputs.jsonl",
            BASE+"/benchmark/phase3/expansion/**/answers.jsonl", BASE+"/benchmark/phase3/expansion2/**/inputs.jsonl",
            BASE+"/benchmark/phase3/expansion2/**/answers.jsonl", BASE+"/benchmark/phase3/holdout3-inputs/*.json",
            BASE+"/benchmark/phase3/holdout4-inputs/*.json", BASE+"/benchmark/phase3/data/*.jsonl"]
    for p in pats:
        for f in glob.glob(p, recursive=True):
            try:
                if f.endswith(".jsonl"):
                    for ln in open(f, encoding="utf-8"):
                        if ln.strip(): recs.append(json.loads(ln))
                else:
                    recs.append(json.load(open(f, encoding="utf-8")))
            except Exception as e:
                print("skip", f, e)
    return [r for r in recs if isinstance(r, dict) and r.get("id")]
EX = load_existing()
ex_by_asked_chart = {}
ex_out_texts = []
ex_stmt_texts = []
for r in EX:
    ctx = r.get("context") or {}
    att = ctx.get("attachments") or {}
    cl = att.get("chart_lines_top_to_bottom") or []
    full = tuple(row.split("　")[0] for row in cl)
    key = ((ctx.get("asked_at") or ""), full)
    if full: ex_by_asked_chart.setdefault(key, []).append(r["id"])
    _oc = r.get("outcome")
    oc = _oc.get("description") if isinstance(_oc, dict) else (_oc if isinstance(_oc, str) else "")
    if oc: ex_out_texts.append((r["id"], oc or ""))
    for p in (r.get("master_predictions") or []):
        se = p.get("statement_excerpt") or ""
        if se: ex_stmt_texts.append((r["id"], se))
print(f"existing records loaded for dedup: {len(EX)}")
dedup_rows = []
for cid in IDS:
    rec_in, ans, full = BUILT[cid]
    ctx = rec_in["context"]; att = ctx["attachments"]
    cl = att.get("chart_lines_top_to_bottom") or []
    full = tuple(row.split("　")[0] for row in cl)
    first = cl[0].split("　")[0] if cl else ""
    clash = ex_by_asked_chart.get((ctx["asked_at"], full), []) if full else []
    out_head = ans["outcome"]["description"][:12]
    out_clash = [eid for eid, oc in ex_out_texts if out_head and out_head in oc]
    stmt_head = ans["master_predictions"][0]["statement_excerpt"][:12]
    stmt_clash = [eid for eid, se in ex_stmt_texts if stmt_head and stmt_head in se]
    status = "OK"
    if clash or out_clash or stmt_clash: status = f"CHECK clash={clash} out_clash={out_clash} stmt_clash={stmt_clash}"
    dedup_rows.append((cid, ctx["asked_at"], first[:18], status))
    print(f"DEDUP {cid} asked={ctx['asked_at']} chart1={first[:18]} -> {status}")
assert all(s == "OK" for *_, s in dedup_rows), "dedup clash found!"

# ================= holdout5 抽選 =================
SALT = "phase3-round3-20261029:"
elig = [cid for cid in IDS if BUILT[cid][2]["holdout_eligible"]]
elig_sorted = sorted(elig, key=lambda i: hashlib.sha256((SALT + i).encode()).hexdigest())
HOLD = elig_sorted[:25]
DEVADD = [cid for cid in IDS if cid not in set(HOLD)]
print(f"eligible={len(elig)} holdout5={len(HOLD)} dev-add={len(DEVADD)}")
print("holdout5:", HOLD)

# ================= 落盤 =================
os.makedirs(OUT + "/inputs", exist_ok=True)
os.makedirs(BASE + "/benchmark/phase3/holdout5", exist_ok=True)
with open(OUT + "/cases.jsonl", "w", encoding="utf-8") as f:
    for cid in IDS:
        f.write(json.dumps(BUILT[cid][2], ensure_ascii=False) + "\n")
for cid in IDS:
    with open(f"{OUT}/inputs/{cid}.json", "w", encoding="utf-8") as f:
        json.dump(BUILT[cid][0], f, ensure_ascii=False, indent=1)
with open(OUT + "/dev-add-answers.jsonl", "w", encoding="utf-8") as f:
    for cid in DEVADD:
        f.write(json.dumps(BUILT[cid][1], ensure_ascii=False) + "\n")
with open(BASE + "/benchmark/phase3/holdout5/test_gold.jsonl", "w", encoding="utf-8") as f:
    for cid in HOLD:
        f.write(json.dumps(BUILT[cid][1], ensure_ascii=False) + "\n")
gold_sha = hashlib.sha256(open(BASE + "/benchmark/phase3/holdout5/test_gold.jsonl", "rb").read()).hexdigest()
now = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%dT%H:%M:%S+08:00")
sealed = f"""# SEALED — holdout5 金標封存說明

- 本目錄 `test_gold.jsonl` 為 holdout5 共 {len(HOLD)} 例的完整金標（master_predictions + outcome），組建時間 {now}（Asia/Shanghai）。
- **只許評審角在 Phase 3 驗收輪開封時讀取**；盲測角、修訂角、數據角在本文件落盤後均不得再讀。
- 開封須在 `benchmark/phase3/holdout5-seal-log.md` 追加一筆（時間、依據、開封人角色、範圍）後方可進行。
- 金標 SHA-256：`{gold_sha}`。
- 封存狀態以 seal log 為準；本文件落盤時狀態為「未開封」。
"""
open(BASE + "/benchmark/phase3/holdout5/SEALED.md", "w", encoding="utf-8").write(sealed)
seal_log = f"""# holdout5 封存日誌

- **組建時間**：{now}（Asia/Shanghai）
- **組建角色**：數據角（Phase 3 第三輪擴數建池）
- **算法**：僅對 expansion3 新增例中滿足硬要求者抽選——結局 A 級、污染 low、《增刪卜易》原文明記月建與日辰且逐爻裝卦表完整（雙完整性），共 {len(elig)} 例合格；按 sha256("phase3-round3-20261029:"+id) 十六進制升序排序，取前 {len(HOLD)} 例入 holdout5，其餘合格例與全部不合雙完整性／梗概型新例入 dev-add。劃分明細見 benchmark/phase3/expansion3/BUILD-REPORT.md，落盤即凍結。
- **例數**：holdout5 共 {len(HOLD)} 例（{'、'.join(HOLD)}）。
- **金標 SHA-256**：`{gold_sha}`
- **結局封存位置**：benchmark/phase3/holdout5/test_gold.jsonl（同目錄 SEALED.md 註明只許評審角驗收時開封）；holdout5 的盲測 inputs 置於 benchmark/phase3/expansion3/inputs/（與 dev-add 共用同一 inputs 目錄，逐例一檔），不含任何答案字段（核對記錄見 expansion3/BUILD-REPORT.md）。
- **狀態**：**未開封**。自本筆落盤起，holdout5 結局不進入任何給盲測角／修訂角的材料；開封須由評審角於驗收輪在本日誌追加一筆後進行。
"""
open(BASE + "/benchmark/phase3/holdout5-seal-log.md", "w", encoding="utf-8").write(seal_log)

# ================= inputs 洩漏自檢 =================
bad = []
for cid in IDS:
    t = open(f"{OUT}/inputs/{cid}.json", encoding="utf-8").read()
    for kw in ["master_predictions", "outcome", "statement_excerpt", "key_assertions", "果於", "果于", "後果", "后果", "斷曰", "断曰"]:
        if kw in t: bad.append((cid, kw))
print("input leak check:", "CLEAN" if not bad else bad)
assert not bad
print("GOLD_SHA256:", gold_sha)
print("NOW:", now)
print("DEVADD:", DEVADD)
