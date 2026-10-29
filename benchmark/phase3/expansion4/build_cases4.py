#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MastersDivination Benchmark · Phase 3 第四輪擴數（expansion4）建檔腳本（數據角）

來源：
  1. 《增刪卜易》卷之一 —— 2026-10-29 經維基文库主頁線上渲染讀取正文
     （本地 dump sources/chinese/zengshan-buyi-wikisource.txt 的卷一只有
      {{/子頁}} 轉入標籤、無正文）。節錄自渲染頁逐字錄入，本腳本以
      「卦象推導名 == 原文所記卦名」與結構斷言校驗。
  2. 《卜筮正宗》第十八問答第七、八問續收 4 例 —— 華夏大易學社（cnddy.com）
     在線全本在線讀（只讀不存檔），https://www.cnddy.com/1759.html
     沿用前輪口徑：雙不完整、只入 dev 級、逐爻裝卦表不錄不虛構。

去重：三鍵指紋（月日干支＋全裝卦逐爻行（左側本卦爻）＋斷語首句/結局首句）
      對全部既有記錄（masters-dataset、benchmark 歷輪 inputs/answers/cases、
      holdout3/4/5 之 inputs）程序比對；卜筮新例無逐爻表，另做
      「卦名＋占問關鍵詞＋結局首句（繁簡雙查）」比對並人工覆核映射。
      本腳本另掃既有池內部（按 id 去重後）指紋碰撞，只登記不處置。

劃分：合格池＝｛A 級 ∩ low ∩ 雙完整｝（本輪 24 例，不足 25，如實全取），
      按 sha256("phase3-round4-20261029:"+id) 十六進制升序即 holdout6 順序；
      其餘新例為 dev-add。
      金標只寫 benchmark/phase3/holdout6/test_gold.jsonl（封存，未開封）。
      本腳本絕不讀取任何 holdout 的 test_gold.jsonl。
冪等：可重跑，產物一致（時間戳除外）。
"""
import hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]          # ~/workspace/divination
P3 = ROOT / "benchmark" / "phase3"
OUTDIR = P3 / "expansion4"
H6DIR = P3 / "holdout6"
ROUND_TAG = "phase3-round4-20261029"

# ---------------------------------------------------------------- 卦象推導（照 expansion3/build_cases3.py 原件）
TRI = {(1,1,1):"乾",(1,1,0):"兌",(1,0,1):"離",(1,0,0):"震",
       (0,1,1):"巽",(0,1,0):"坎",(0,0,1):"艮",(0,0,0):"坤"}
_HEX_ROWS = {
"乾": {"乾":"乾爲天","坤":"天地否","震":"天雷无妄","巽":"天風姤","坎":"天水訟","離":"天火同人","艮":"天山遯","兌":"天澤履"},
"坤": {"乾":"地天泰","坤":"坤爲地","震":"地雷復","巽":"地風升","坎":"地水師","離":"地火明夷","艮":"地山謙","兌":"地澤臨"},
"震": {"乾":"雷天大壯","坤":"雷地豫","震":"震爲雷","巽":"雷風恆","坎":"雷水解","離":"雷火豐","艮":"雷山小過","兌":"雷澤歸妹"},
"巽": {"乾":"風天小畜","坤":"風地觀","震":"風雷益","巽":"巽爲風","坎":"風水渙","離":"風火家人","艮":"風山漸","兌":"風澤中孚"},
"坎": {"乾":"水天需","坤":"水地比","震":"水雷屯","巽":"水風井","坎":"坎爲水","離":"水火既濟","艮":"水山蹇","兌":"水澤節"},
"離": {"乾":"火天大有","坤":"火地晉","震":"火雷噬嗑","巽":"火風鼎","坎":"火水未濟","離":"離爲火","艮":"火山旅","兌":"火澤睽"},
"艮": {"乾":"山天大畜","坤":"山地剝","震":"山雷頤","巽":"山風蠱","坎":"山水蒙","離":"山火賁","艮":"艮爲山","兌":"山澤損"},
"兌": {"乾":"澤天夬","坤":"澤地萃","震":"澤雷隨","巽":"澤風大過","坎":"澤水困","離":"澤火革","艮":"澤山咸","兌":"兌爲澤"}}
HEX = {}
for _up, _row in _HEX_ROWS.items():
    for _lo, _nm in _row.items():
        HEX[(_up, _lo)] = _nm
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

# ------------------------------------------------------------ 既有記錄載入（去重用）
def iter_jsonl(p):
    try:
        with open(p, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    yield json.loads(line)
    except FileNotFoundError:
        return

def load_existing():
    recs = {}
    pats = ["masters-dataset/**/inputs.jsonl", "masters-dataset/**/answers.jsonl",
            "benchmark/**/inputs.jsonl", "benchmark/**/answers.jsonl",
            "benchmark/**/cases.jsonl", "benchmark/**/roster.jsonl",
            "benchmark/phase3/data/*.jsonl"]
    for pat in pats:
        for p in sorted(ROOT.glob(pat)):
            if "expansion4" in str(p) or "holdout6" in str(p):
                continue                      # 不把本輪產物當既有
            assert "test_gold" not in p.name  # 紀律：不讀任何金標
            for r in iter_jsonl(p):
                rid = r.get("id")
                if rid and rid not in recs:
                    recs[rid] = r
    # holdout3/4/5 與歷輪 inputs 為逐例一檔
    for d in [ROOT/"benchmark/phase3/expansion/inputs",
              ROOT/"benchmark/phase3/expansion2/inputs",
              ROOT/"benchmark/phase3/expansion3/inputs",
              ROOT/"benchmark/phase3/holdout3-inputs",
              ROOT/"benchmark/phase3/holdout4-inputs",
              ROOT/"benchmark/phase3/inputs"]:
        if d.is_dir():
            for p in sorted(d.glob("*.json")):
                r = json.loads(p.read_text(encoding="utf-8"))
                if r.get("id") and r["id"] not in recs:
                    recs[r["id"]] = r
    return recs

PUNC = "，。；：、．·…—「」『』（）()？！?! " 
def norm(s):
    return "".join(c for c in (s or "") if c not in PUNC)
# 繁→簡粗映射（只用於卜筮跨輪比對的輔助鍵，不作判定唯一依據）
T2S = str.maketrans({"斷":"断","曰":"曰","果":"果","於":"于","後":"后","麼":"么",
                     "這":"这","裡":"里","醫":"医","時":"时","還":"还","來":"来",
                     "麼":"么","為":"为","麼":"么","麼":"么"})
def fp_chart(rec):
    hx = rec.get("hexagram") or {}
    rows = []
    for cast in [hx] + (rec.get("extra_casts") or []):
        for ln in (cast.get("chart_lines") or []):
            rows.append(ln.split("　")[0])
    return tuple(rows)

def outcome_head(rec):
    oc = rec.get("outcome") or {}
    txt = oc.get("description") or ""
    m = re.split(r"[。；]", txt)
    return norm(m[0])[:16] if m else ""

# ---------------------------------------------------------------- 增刪卷一案例
# 欄位: subj, caster, question, asked, chapter, category, direction,
#        gua_expected(原文所記), chart(list 或 None), stmt, out, gnote, comment, [sixgods]
Z = []
def z(*a, **k):
    Z.append(a)

z("父親近病吉凶","一人","占父近病","辰月戊申日","用神元神忌神仇神章第九","疾病","positive",
  "乾爲天之風天小畜",
  ["父母戌土⚊世　妻財卯木⚊","兄弟申金⚊　　官鬼巳火⚊","官鬼午火○　　父母未土⚋",
   "父母辰土⚊應　父母辰土⚊","妻財寅木⚊　　妻財寅木⚊","子孫子水⚊　　子孫子水⚊"],
  "此卦辰土未土戌土三重父母爻，當擇其旺者而用之，今辰土父母臨月建，卽用辰土爲用神，目下病重者，乃因申日沖寅木而暗動，木動以克辰土。午火𨿽動化出未土，午與未合，午未相合不生辰土，所以此辰土單受寅木之克，不得午火之生，故此病體沈重，須待丑日沖去未土而午火無合，其土災退。",
  "果於丑日起牀。",
  "卷一首收例；三重父母取用之例，斷語與結局可分離。", "")

z("求財","一人","占求財","酉月辛亥日","元神忌神衰旺章第十","財運","positive",
  "兌爲澤之雷水解",
  ["父母未土⚋世　父母戌土⚋","兄弟酉金○　　兄弟申金⚋","子孫亥水⚊　　官鬼午火⚊",
   "父母丑土⚋應　官鬼午火⚋","妻財卯木⚊　　父母辰土⚊","官鬼巳火○　　妻財寅木⚋"],
  "予曰：神兆機於動，予從來不言散，正因巳火化空，所以目下不見，待甲寅日出空而相見。寅木之財以生官，官來生世，",
  "果於寅日早見木日得財。",
  "結局句「早見木日」文句疑有訛亂，照維基文库渲染頁原文錄入、不改字。", "")

z("自占病吉凶","野鶴老人自占","自占病","巳月乙未日","元神忌神衰旺章第十","疾病","negative",
  "澤風大過之火風鼎",
  ["妻財未土ㄨ　　子孫巳火⚊","官鬼酉金○　　妻財未土⚋","父母亥水⚊世　官鬼酉金⚊",
   "官鬼酉金⚊　　官鬼酉金⚊","父母亥水⚊　　父母亥水⚊","妻財丑土⚋應　妻財丑土⚋"],
  "自占病世爻亥水爲用神，被未土忌神動而克水，幸得酉金元神亦動，忌神未土反生元神之酉金，金生亥水，接續相生，化凶而爲吉。其如亥水月沖日克，值月破而被克，𨿽有生扶生之不起，如樹無根，寒谷不回春也。",
  "果卒於癸卯日，應卯日者沖去元神之日也。",
  "自占例；元神雖動而用神月破，斷凶，結局明確。", "")

z("兄已判重罪能否得救","弟","占兄已得重罪，得蒙救否","卯月己卯日","五行相生章第十一","官非","positive",
  "地雷復之震爲雷",
  ["子孫酉金⚋　　兄弟戌土⚋","妻財亥水⚋　　子孫申金⚋","兄弟丑土ㄨ應　父母午火⚊",
   "兄弟辰土⚋　　兄弟辰土⚋","官鬼寅木⚋　　官鬼寅木⚋","妻財子水⚊世　妻財子水⚊"],
  "兄弟爻爲用神，丑土兄動日月克之，明現大罪難脫，幸得兄爻丑土化午火父母回頭相生，斷曰：速速行之。父母化兄爻相生爲吉，",
  "後蒙恩免死。",
  "結局有事件（蒙恩免死）但無具體時點，grade_note 註明。", "")

z("父官事已擬重罪","一人","占父官事已擬重罪","卯月戊寅日","五行相克章第十二","官非","negative",
  "澤地萃之天火同人",
  ["父母未土ㄨ　　父母戌土⚊","兄弟酉金⚊應　兄弟申金⚊","子孫亥水⚊　　官鬼午火⚊",
   "妻財卯木ㄨ　　子孫亥水⚊","官鬼巳火⚋世　父母丑土⚋","父母未土ㄨ　　妻財卯木⚊"],
  "外卦未土父母，卯月克之，內卦亥卯未合成木局又相克制，月克日刑全無助，",
  "果至重刑。",
  "結局句簡短（果至重刑）但為獨立「果」字應驗記載、事件明確，列 A 級邊界例並註明。",
  "與下一例同日同家事、不同占者不同卦，前輪先例許同日異案並存。")

z("兄官事吉凶","妹","妹占兄官事","卯月戊寅日","克處逢生章第十三","官非","positive",
  "天地否之天水訟",
  ["父母戌土⚊應　父母戌土⚊","兄弟申金⚊　　兄弟申金⚊","官鬼午火⚊　　官鬼午火⚊",
   "妻財卯木⚋世　官鬼午火⚋","官鬼巳火ㄨ　　父母辰土⚊","父母未土⚋　　妻財寅木⚋"],
  "申金兄爻爲用神，巳火鬼動，刑克申金，重罪定矣。幸喜辰日沖動戌土父母暗動生申，克處逢生，若有父母可以救之，",
  "後因父年八十，援例恩畱免死。",
  "與上一例同日（卯月戊寅日）同家事：上一例占父官事、本例妹占其兄，卦象用神皆不同。", "")

z("弟患癌症臨危","一人","占弟癌症已臨危","辰月丙申日","克處逢生章第十三","疾病","positive",
  "水火既濟之澤火革",
  ["兄弟子水⚋應　官鬼未土⚋","官鬼戌土⚊　　父母酉金⚊","父母申金ㄨ　　兄弟亥水⚊",
   "兄弟亥水⚊世　兄弟亥水⚊","官鬼丑土⚋　　官鬼丑土⚋","子孫卯木⚊　　子孫卯木⚊"],
  "月建辰土𨿽克亥水，兄弟賴申日以生之，又得動爻相生，臨危有救，",
  "果於本日酉時遇名醫救活也，至己亥日以全生。",
  "「癌症」為原書用語，照錄。", "")

z("求財何日得","一人","占求財","寅月庚戌日","月將章第十六","財運","positive",
  "火天大有",
  ["官鬼巳火⚊應","父母未土⚋","兄弟酉金⚊","父母辰土⚊世","妻財寅木⚊","子孫子水⚊"],
  "寅木財爻爲用神，財爻克世，此財必得，但目下尙空，要到甲寅日出空可得。",
  "果於甲寅得之。",
  "與既有 LY-417（女病）同日不同案，已核。", "")

z("謁貴見否","一人","占謁貴","酉月丙寅日","月將章第十六","求見","positive",
  "山風蠱之山水蒙",
  ["兄弟寅木⚊應　兄弟寅木⚊","父母子水⚋　　父母子水⚋","妻財戌土⚋　　妻財戌土⚋",
   "官鬼酉金○世　子孫午火⚋","父母亥水⚊　　妻財辰土⚊","妻財丑土⚋　　兄弟寅木⚋"],
  "世臨月建之官，定得面見，但被午火回頭之克，須待子日沖去午火方得拜謁，",
  "果得見於丙子日，故曰逢傷亦傷卻有待時之用。",
  "", "")

z("官之升遷","一人","占官之升遷","寅月丙申日","月將章第十六","功名","positive",
  "艮爲山之山雷頤",
  ["官鬼寅木⚊世　官鬼寅木⚊","妻財子水⚋　　妻財子水⚋","兄弟戌土⚋　　兄弟戌土⚋",
   "子孫申金○應　兄弟辰土⚋","父母午火⚋　　官鬼寅木⚋","兄弟辰土ㄨ　　妻財子水⚊"],
  "寅木官星持世臨月建而旺相，𨿽被申日沖克，喜申子辰合成水局，以生官，不獨無害，定然三月高遷，",
  "果於三月升任云南太守，卽升者乃因爻得水局生扶，應三月者辰土出空之月也，應云南者，世與官星皆在六爻之故耳。",
  "", "")

z("弟被訟吉凶","一人","占弟被訟吉凶","午月丁未日","月將章第十六","官非","negative",
  "澤水困之雷風恆",
  ["父母未土⚋　　父母戌土⚋","兄弟酉金○　　兄弟申金⚋","子孫亥水⚊應　官鬼午火⚊",
   "官鬼午火ㄨ　　兄弟酉金⚊","父母辰土⚊　　子孫亥水⚊","妻財寅木⚋世　父母丑土⚋"],
  "酉金兄爻爲用神，午月克之，未日生之，可以相敵，但不宜又動出午火相克，予曰：酉金兄爻化退神，今歲辰年太歲相合，自是無妨恐，退至申年而無路矣，",
  "果於本年下獄至申年而重刑。",
  "結局跨年（本年下獄、申年重刑），屬長程應驗梗概，事件明確。", "")

z("開鋪面吉凶","一人","占開鋪面","寅月丁酉日","月將章第十六","事業","negative",
  "艮爲山之地火明夷",
  ["官鬼寅木○世　子孫酉金⚋","妻財子水⚋　　妻財亥水⚋","兄弟戌土⚋　　兄弟丑土⚋",
   "子孫申金⚊應　妻財亥水⚊","父母午火⚋　　兄弟丑土⚋","兄弟辰土ㄨ　　官鬼卯木⚊"],
  "世臨寅木得令，當時目下開張，卽許熱鬧，獨嫌日辰克世，世化回頭之克，生少克多，又是六沖卦，不吉。予曰：鬼在身邊須防疾病，夥伴從此變心，受其累。",
  "果於六月疾至，八月夥計盜盡。鳴之於官，分文不復。",
  "", "")

z("妹臨產吉凶","一人","占妹臨產吉凶","午月戊辰日","月將章第十六","生產","positive",
  "火地晉",
  ["官鬼巳火⚊","父母未土⚋","兄弟酉金⚊世","妻財卯木⚋","官鬼巳火⚋","父母未土⚋應"],
  "酉金兄爻爲用神，月令克之，日建生之，許之無礙，卯日卯時必生，",
  "果於次日卯時生，母子平安，應卯時者，酉金與辰日相合。",
  "", "")

z("兄病吉凶","一人","占兄病","申月甲辰日","六神章第十八","疾病","positive",
  "水雷屯之震爲雷",
  ["兄弟子水⚋　　官鬼戌土⚋","官鬼戌土○應　父母申金⚋","父母申金ㄨ　　妻財午火⚊",
   "官鬼辰土⚋　　官鬼辰土⚋","子孫寅木⚋世　子孫寅木⚋","兄弟子水⚊　　兄弟子水⚊"],
  "子水兄爻爲用神，卦中忌神、元神同動，土動生申，申金動而生子水，月建又生子水，",
  "至戊申日沈屙復起，其可謂之蛇動死，虎動主喪耶？",
  "結局以反問句帶出（沈屙復起＝沉疴痊癒），事件明確；原文裝卦行帶六神欄（自上而下：元武、白虎、勾陳、媵蛇、朱雀、靑龍），錄入按通例只取爻行、六神欄記於此。",
  "")

z("出門與嫁女","一人","占出門","申月丙子日","六合章第十九","出行","negative",
  "地火明夷之雷山小過",
  ["父母酉金⚋　　官鬼戌土⚋","兄弟亥水⚋　　父母申金⚋","官鬼丑土ㄨ世　妻財午火⚊",
   "兄弟亥水⚊　　父母申金⚊","官鬼丑土⚋　　妻財午火⚋","子孫卯木○應　官鬼辰土⚋"],
  "世動破，予曰：合住必有事阻，不能動身。予曰：卯木子孫申月絕之，子日刑之，且動而變鬼，恐嫁之不及矣。",
  "後因病重，此人未去，女死辰日，夫應不去者，世動而逢合也，女死辰日者，卯木子孫變辰土之故也。",
  "一卦兩事：本問出門，旁及同人嫁女；結局兩事皆有記載。", "")

z("兩村爭田水","一人","占兩村因田水撕打","卯月丁巳日","六合章第十九","爭訟","positive",
  "離爲火之坤爲地",
  ["兄弟巳火○世　妻財酉金⚋","子孫未土⚋　　官鬼亥水⚋","妻財酉金○　　子孫丑土⚋",
   "官鬼亥水○應　父母卯木⚋","子孫丑土⚋　　兄弟巳火⚋","父母卯木○　　子孫未土⚋"],
  "內卦爲我村，亥卯未合成木局，外卦爲人村，巳酉丑合金局來克木，幸衰金不克旺木，不足畏也。況系六沖卦變六沖，有人解散必不成訟，",
  "後果勸散。",
  "", "")

z("出外經商貿易財運","一人","占出外經商貿易，財運如何","午月丙辰日","六沖章第二十","財運","positive",
  "雷風恆之雷地豫",
  ["妻財戌土⚋應　妻財戌土⚋","官鬼申金⚋　　官鬼申金⚋","子孫午火⚊　　子孫午火⚊",
   "官鬼酉金○世　兄弟卯木⚋","父母亥水○　　子孫巳火⚋","妻財丑土⚋　　妻財未土⚋"],
  "世爻酉金化卯相沖及反復之卦，幸辰日合之，沖中逢合，又得戌土爲財，暗動生世，𨿽則反復不常，卻有財利。",
  "果此人去而復反者三次，中途發財。",
  "《卜筮正宗》第十一問同案版本無結局（已於前輪剔除登記），本例為《增刪卜易》有結局版本；與既有 LY-227（鄉試）同日不同案，已核。", "")

z("子久出不歸生死","一人","占子久出不歸，生死如何","酉月乙未日","六沖章第二十","親屬","positive",
  "坤爲地",
  ["子孫酉金⚋世","妻財亥水⚋","兄弟丑土⚋","官鬼卯木⚋應","父母巳火⚋","兄弟未土⚋"],
  "世持子孫以臨月建，未日生之，𨿽是六沖之卦，此子必歸。",
  "果於子年建功卯年得意而歸，此應靜而逢沖之驗也。",
  "結局跨年梗概（子年建功、卯年歸），事件明確。", "")

z("父出外一載無音信","一人","占父出外一載無音","丑月丁酉日","動散章第二十三","親屬","positive",
  "風水渙之坎爲水",
  ["父母卯木○　　官鬼子水⚋","兄弟巳火⚊世　子孫戌土⚊","子孫未土⚋　　妻財申金⚋",
   "兄弟午火⚋　　兄弟午火⚋","子孫辰土⚊應　子孫辰土⚊","父母寅木⚋　　父母寅木⚋"],
  "卯木父爻發動而生世，又化子水回頭生許之，在外平安。世空者還至交春卽歸，",
  "果於二月得意而回。",
  "", "")

z("長輩功名","來人（代卜）","來人不言所事，代卜長輩功名","卯月辛巳日","卦變生克墓絕章第二十四","功名","negative",
  "巽爲風之乾爲天", None,
  "功名須要親占，代占難取用神，從不敢斷，幸此卦而易見，巽木化乾金，卽爲化回頭克，爲絕卦也，不必問名，壽命不長，",
  "果於削職後七月而終。",
  "原文僅記月日與卦名（巽卦變乾卦），未列逐爻裝卦表 → chart_complete=false，只入 dev 級。占問為功名、大師改斷壽命並明言，照錄。與既有 LY-502（自陳）同日不同案，已核。", "")

z("主病吉凶","一人","占主病","午月丙寅日","卦變生克墓絕章第二十四","疾病","negative",
  "離爲火之坎爲水", None,
  "離火變坎水，回頭來克，但因午月火旺，許之冬令必危。",
  "果卒於九月丁亥日，應亥日者，坎水之絕地也。",
  "原文僅記月日與卦名（離卦變坎卦），未列逐爻裝卦表 → chart_complete=false，只入 dev 級。", "")

z("升遷","一人","占升遷","卯月己亥日","反伏章第二十五","功名","positive",
  "地澤臨之風澤中孚",
  ["子孫酉金ㄨ　　官鬼卯木⚊","妻財亥水ㄨ應　父母巳火⚊","兄弟丑土⚋　　兄弟未土⚋",
   "兄弟丑土⚋　　兄弟丑土⚋","官鬼卯木⚊世　官鬼卯木⚊","父母巳火⚊　　父母巳火⚊"],
  "世臨卯木月建之官，又長生於亥日，世與官星同臨旺地，許之卽升，",
  "果於本月聞報升山東，未及一載復任江西，應本月升者卯官而值月令升山東者，官臨卯木，復任江西者，外卦反伏，去之而復反也。",
  "", "")

z("父外任平安","一人","占父外任平安","申月癸巳日","反伏章第二十五","親屬","mixed",
  "天風姤之雷風恆",
  ["父母戌土○　　父母戌土⚋","兄弟申金○　　兄弟申金⚋","官鬼午火⚊應　官鬼午火⚊",
   "兄弟酉金⚊　　兄弟酉金⚊","子孫亥水⚊　　子孫亥水⚊","父母丑土⚋世　父母丑土⚋"],
  "巳火日辰生父母，當許在任平安，獨憂卦得伏吟，乃是不祥之象，任上必有事故，不得意以呻吟也。予曰：伏吟欲歸而不能，辰年可歸，",
  "後知苗獨作亂，地方不祥，驚險異常，寅年占卦，辰年缺歸，午年又官者，",
  "原文作「申月癸巳占」，月日干支俱全（「日」字省），month_day_complete 按干支俱全計 true 並註明。結局為任上梗概＋歸期/再官的時期性記錄（沿 expansion3 時期梗概收例先例），方向 mixed（人事平安而任上多故、歸期延宕）。", "")

z("求財（兩占合斷）","一人","占求財","辰月乙卯日","旬空章第二十六","財運","negative",
  "風火家人之山火賁＋火澤睽之山澤損",
  ["兄弟卯木⚊　　兄弟寅木⚊","子孫巳火○應　父母子水⚋","妻財未土⚋　　妻財戌土⚋",
   "父母亥水⚊　　父母亥水⚊","妻財丑土⚋世　妻財丑土⚋","兄弟卯木⚊　　兄弟卯木⚊",
   "父母巳火⚊　　官鬼寅木⚊","兄弟未土⚋　　妻財子水⚋","子孫酉金○世　兄弟戌土⚋",
   "兄弟丑土⚋　　兄弟丑土⚋","官鬼卯木⚊　　官鬼卯木⚊","父母巳火⚊應　父母巳火⚊"],
  "丑財持世遇旬空，𨿽有巳火之生，巳火又化回頭之克，不能生丑土之財，此財旣無生扶當主難求。竟斷曰：財無气矣，不必勞心。",
  "後果全無。",
  "同日同人先後兩占（家人之賁、睽之損）合斷一事，兩卦全錄（12 行）。與既有 LY-210（占壽）同日不同案，已核。", "")

z("遠行求財（兩占）","一人","占遠行求財","子月辛亥日","旬空章第二十六","財運","positive",
  "山天大畜＋地火明夷之雷火豐",
  ["官鬼寅木⚊","妻財子水⚋應","兄弟戌土⚋","兄弟辰土⚊","官鬼寅木⚊世","妻財子水⚊",
   "父母酉金⚋　　官鬼戌土⚋","兄弟亥水⚋　　父母申金⚋","官鬼丑土ㄨ世　妻財午火⚊",
   "兄弟亥水⚊　　兄弟亥水⚊","官鬼丑土⚋　　官鬼丑土⚋","子孫卯木⚊應　子孫卯木⚊"],
  "世逢寅木，子月亥日俱作財神而生世，有喜。斷曰：此卦與前卦相同，此行大有財發。彼曰：去得成否？予曰：甲寅日世爻出空之日，準行無疑，",
  "果於乙卯日起程，後到彼地，寅卯月間，諸事順心，滿載而歸。",
  "前一占爲靜卦大畜、後一占明夷之豐，兩占同斷遠行求財，兩卦全錄（12 行）。", "")

# 【剔除登記】午月己卯日占妻病「震之豐」例（生旺墓絕章第又二十六）不收：
# 維基文库本所記卦名與所錄裝卦表自相矛盾——裝卦僅上爻戌土ㄨ動，推導為震之噬嗑，
# 且變卦逐爻納甲干支（下子寅辰、上酉未巳）亦合噬嗑而非豐；原文名「豐」須三爻辰土動方成。
# 疑未校對轉錄之誤，寧缺勿濫，剔除並於 BUILD-REPORT 登記（不改字遷就）。

# ---------------------------------------------------------------- 卜筮正宗續收（dev 級）
# 欄位: subj, question, qno, category, direction, gua, palace, kongwang, stmt, out, gnote
B = []
def b(*a):
    B.append(a)

b("子病吉凶","占子病","第七問","疾病","negative","澤風大過","震宮","午未",
  "午火子孫伏世爻亥父之下，月建生助亥水克之，目下用神旬空，不受其克，甲午日難逃矣．",
  "果死於午日午時，此謂伏無提拔也．",
  "第七問前輪未收；斷語（甲午日難逃）與結局（果死於午日午時）可分離，A 級具體應驗。")

b("父近病吉凶","占父近病","第七問","疾病","negative","地雷復之火雷噬嗑","坤宮","辰巳",
  "巳火父母為用神，值旬空．日辰拱之，近病逄空不死，但不利於六合卦．六合即死，予思用空，六合可以相敵，不宜世忌神暗動，外卦巳酉丑合成金局，助水克之．此病必凶．凶在何日？答曰：己亥日克沖巳火，還在旬空，不妨恐危於出旬，辛亥日也．",
  "果至其日而死，此應出旬又被沖克也．",
  "第七問前輪未收（前輪所收父近病例為增刪同名異案與本書他問）；斷語點名辛亥日、結局果至其日而死，A 級。")

b("訟事勝負","占訟事","第八問","官非","negative","地天泰","坤宮","戌亥",
  "爻逄六合，官事必審，不宜戌建沖世，乃是月破．卯日克世，必輸無疑，",
  "果被杖責，此應日克月破故耳．",
  "第八問前輪未收；斷語（必輸無疑）與結局（果被杖責）可分離，A 級。")

b("墳地風水吉凶","占墳地風水","第八問","風水","positive","澤山咸","兌宮","子丑",
  "日辰臨青龍持世，來龍由左而來，龍虎皆有氣，必然環抱．第嫌應上未土臨月破，應為照山，世前一位為朝案，喜亥水得申日生之，必有朝水，宜取水作朝，不宜取山作向．間爻為明堂，旺相必闊大．",
  "彼曰：一一果然，葬可好否？予曰：依予取水作朝，棄山作向，許必大發，彼果依斷，葬後即如所言．",
  "當場驗證型＋葬後梗概（沿 expansion3 LY-528/537 當場驗證型收例先例，本輪明示此口徑優先於 expansion2 對同類之排除）；第八問前輪未收。")

CONTAM_Z = ("清初民間占例（野鶴老人自占及輯錄）；求測者多未具名、非著名歷史人物或事件，"
            "結局無從以常識先驗得知。")
CONTAM_B = ("明末清初民間占例（王洪緒輯錄其師楊廣含傳授及自占驗）；求測者多未具名、"
            "非著名歷史人物或事件，結局無從以常識先驗得知。")
Z_URL = "https://zh.wikisource.org/wiki/增刪卜易"
B_URL = "https://www.cnddy.com/1759.html"
CAST = "六爻納甲（銅錢搖卦，原書只記月日與卦象）"

def build_z(cid, t):
    (subj, caster, question, asked, chapter, cat, direction, gua_exp,
     chart, stmt, out, gnote, comment) = t
    rec = {
        "id": cid, "tradition": "六爻",
        "master": "野鶴老人（《增刪卜易》）",
        "source_work": "增刪卜易",
        "subject": subj, "caster_or_relation": caster, "question": question,
        "category": cat, "asked_at": asked, "casting_method": CAST,
    }
    if chart is None:
        names = gua_exp.split("之")
        rec["hexagram"] = {
            "original_name": names[0], "changed_name": names[1],
            "palace": "原文未記", "kongwang": "原文未記",
            "chart_lines": [], "chart_note": "原文僅記月日與卦名、未列逐爻裝卦表，逐爻表不錄不虛構。",
            "moving_lines_text": "原文未記"}
        rec["chart_complete"] = False
        rec["completeness_basis"] = ("月日干支原文俱全（month_day_complete=true）；原文未列逐爻裝卦表，"
                                     "chart_complete=false。斷語、結局逐字照錄。")
    else:
        assert len(chart) % 6 == 0
        casts = [chart[i:i+6] for i in range(0, len(chart), 6)]
        derived = derive(chart)
        exps = gua_exp.split("＋")
        assert len(derived) == len(exps), (cid, derived, exps)
        hx = []
        for ci, cl in enumerate(casts):
            assert derived[ci] == exps[ci], (cid, derived[ci], exps[ci])
            nmov = sum(1 for ln in cl if "○" in ln.split("　")[0] or "ㄨ" in ln.split("　")[0])
            hx.append({"name": derived[ci], "chart_lines": cl, "moving": nmov})
        main = hx[0]
        names = main["name"].split("之")
        rec["hexagram"] = {
            "original_name": names[0],
            "changed_name": names[1] if len(names) > 1 else None,
            "chart_lines": casts[0]}
        if len(casts) > 1:
            rec["extra_casts"] = [{
                "original_name": h["name"].split("之")[0],
                "changed_name": h["name"].split("之")[1] if "之" in h["name"] else None,
                "chart_lines": c} for h, c in zip(hx[1:], casts[1:])]
        rec["chart_complete"] = True
        rec["completeness_basis"] = ("月日干支原文俱全（month_day_complete=true）；裝卦表逐爻照錄線上渲染頁，"
                                     "卦名經推導與原文所記相符（chart_complete=true）。斷語、結局逐字照錄。")
    rec["month_day_complete"] = True
    rec["provenance"] = {"work": "增刪卜易", "edition": "維基文库本（錄入者整理本，未排版/未校對）",
                         "page": "卷之一·" + chapter, "url": Z_URL, "language": "zh-Hant"}
    rec["master_predictions"] = [{
        "statement_excerpt": stmt, "direction": direction,
        "key_assertions": [], "timing_claim": None, "source_language": "zh-Hant"}]
    rec["outcome"] = {"description": out, "direction": direction, "source_language": "zh-Hant"}
    rec["outcome_grade"] = "A"
    rec["contamination"] = "low"
    rec["contamination_rationale"] = CONTAM_Z
    rec["grade_note"] = gnote
    rec["comment"] = comment
    rec["holdout_eligible"] = bool(rec["chart_complete"])
    return rec

def build_b(cid, t):
    (subj, question, qno, cat, direction, gua, palace, kw, stmt, out, gnote) = t
    names = gua.split("之")
    rec = {
        "id": cid, "tradition": "六爻",
        "master": "王洪緒（輯，《卜筮正宗》）",
        "source_work": "卜筮正宗",
        "subject": subj, "caster_or_relation": "一人", "question": question,
        "category": cat, "asked_at": "原書未記月日（十八問答體例）", "casting_method": CAST,
        "hexagram": {
            "original_name": names[0],
            "changed_name": names[1] if len(names) > 1 else None,
            "palace": palace, "kongwang": kw, "chart_lines": [],
            "chart_note": ("在線本裝卦表為雙欄排版經 OCR 轉錄後行序錯亂，逐爻裝卦未能可靠還原；"
                           "本條只錄可由卦名、卦宮、空亡與斷語互證的資訊，逐爻表不錄。"),
            "moving_lines_text": "見斷語節錄所涉動爻（在線本裝卦表不可靠，未逐爻還原）"},
        "month_day_complete": False, "chart_complete": False,
        "completeness_basis": ("十八問答體例不記月日干支（month_day_complete=false）；在線本裝卦表 OCR 錯亂、"
                               "逐爻不可還原（chart_complete=false）。只入 dev 級。"),
        "provenance": {"work": "卜筮正宗",
                       "edition": "華夏大易學社（cnddy.com）在線全本（據通行本錄入，頁面字形為簡體，節錄照頁面；在線讀、未存檔）",
                       "page": "十八問答·" + qno, "url": B_URL, "language": "zh-Hans"},
        "master_predictions": [{
            "statement_excerpt": stmt, "direction": direction,
            "key_assertions": [], "timing_claim": None, "source_language": "zh-Hans"}],
        "outcome": {"description": out, "direction": direction, "source_language": "zh-Hans"},
        "outcome_grade": "A", "contamination": "low",
        "contamination_rationale": CONTAM_B,
        "grade_note": gnote, "comment": "",
        "holdout_eligible": False,
    }
    return rec

def zkey(rec):
    """曾刪例（繁體）指紋：月日＋逐爻行左側＋結局首句。"""
    return (rec["asked_at"], fp_chart(rec))

def main():
    now = __import__("subprocess").run(
        ["date", "+%Y-%m-%dT%H:%M:%S+08:00"], env={"TZ": "Asia/Shanghai", "PATH": "/usr/bin:/bin"},
        capture_output=True, text=True).stdout.strip()
    existing = load_existing()
    print(f"既有記錄（按 id 去重）: {len(existing)}")

    # ---- 既有池內部指紋碰撞掃描（只登記，不處置）----
    seen_fp = {}
    internal_dups = []
    for rid, r in sorted(existing.items()):
        fp = (r.get("asked_at"), fp_chart(r))
        if fp[1]:
            if fp in seen_fp and seen_fp[fp] != rid:
                internal_dups.append((seen_fp[fp], rid, fp[0]))
            else:
                seen_fp[fp] = rid
    print("既有池內部（月日＋裝卦）指紋碰撞:", internal_dups)

    # ---- 建新例 ----
    cases = []
    nid = 600
    for t in Z:
        nid += 1
        cases.append(build_z(f"LY-{nid}", t))
    for t in B:
        nid += 1
        cases.append(build_b(f"LY-{nid}", t))
    print(f"新例: {len(cases)}（增刪卷一 {len(Z)}＋卜筮續收 {len(B)}）")

    # ---- 去重斷言 ----
    exist_fp = {}
    for rid, r in existing.items():
        fp = (r.get("asked_at"), fp_chart(r))
        if fp[1]:
            exist_fp.setdefault(fp, rid)
    exist_out_heads = {}
    for rid, r in existing.items():
        h = outcome_head(r)
        if len(h) >= 6:
            exist_out_heads.setdefault(h, rid)
            exist_out_heads.setdefault(h.translate(T2S), rid)
    for c in cases:
        fp = zkey(c)
        if fp[1]:
            assert fp not in exist_fp, f"去重碰撞（月日＋裝卦）: {c['id']} vs {exist_fp.get(fp)}"
        h = outcome_head(c)
        assert h not in exist_out_heads, f"去重碰撞（結局首句）: {c['id']} vs {exist_out_heads.get(h)}"
        # 本輪內部互查
        for o in cases:
            if o is not c and o["asked_at"] == c["asked_at"] and fp_chart(o) and fp_chart(o) == fp_chart(c):
                raise AssertionError(f"本輪內部重複: {c['id']} vs {o['id']}")
    print("去重斷言通過（月日＋裝卦指紋、結局首句繁簡雙查、本輪內部互查）。")

    # ---- 劃分 ----
    eligible = [c for c in cases if c["holdout_eligible"]]
    eligible.sort(key=lambda c: hashlib.sha256(f"{ROUND_TAG}:{c['id']}".encode()).hexdigest())
    holdout = eligible[:25]
    hids = {c["id"] for c in holdout}
    print(f"合格池 {len(eligible)} 例；holdout6 取 {len(holdout)} 例"
          + ("（不足 25，如實全取、不放寬標準）" if len(eligible) < 25 else ""))
    devadd = [c for c in cases if c["id"] not in hids]

    def inp(c):
        return {"id": c["id"], "tradition": c["tradition"], "subject": c["subject"],
                "context": {"caster_or_relation": c["caster_or_relation"],
                            "question": c["question"], "category": c["category"],
                            "asked_at": c["asked_at"], "casting_method": c["casting_method"],
                            "hexagram": c["hexagram"]},
                "provenance": c["provenance"], "language": c["provenance"]["language"]}

    def ans(c):
        return {"id": c["id"], "master": c["master"], "source_work": c["source_work"],
                "master_predictions": c["master_predictions"], "outcome": c["outcome"],
                "outcome_grade": c["outcome_grade"], "contamination": c["contamination"],
                "contamination_rationale": c["contamination_rationale"],
                "grade_note": c["grade_note"]}

    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR / "inputs").mkdir(exist_ok=True)
    with open(OUTDIR / "cases.jsonl", "w", encoding="utf-8") as f:
        for c in cases:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    for c in cases:
        (OUTDIR / "inputs" / f"{c['id']}.json").write_text(
            json.dumps(inp(c), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with open(OUTDIR / "dev-add-answers.jsonl", "w", encoding="utf-8") as f:
        for c in sorted(devadd, key=lambda x: x["id"]):
            f.write(json.dumps(ans(c), ensure_ascii=False) + "\n")

    H6DIR.mkdir(parents=True, exist_ok=True)
    gold_path = H6DIR / "test_gold.jsonl"
    with open(gold_path, "w", encoding="utf-8") as f:
        for c in holdout:
            f.write(json.dumps(ans(c), ensure_ascii=False) + "\n")
    gold_sha = hashlib.sha256(gold_path.read_bytes()).hexdigest()

    sealed = f"""# SEALED — holdout6 測試集金標（未開封）

- 封存時間：{now}（Asia/Shanghai）
- 來源輪次：Phase 3 第四輪擴數（expansion4），新例 LY-601–LY-{600+len(cases)}
- 例數：{len(holdout)}（合格池 {{A 級 ∩ low ∩ 雙完整}} 共 {len(eligible)} 例，不足 25，如實全取、未放寬標準；
  按 sha256("{ROUND_TAG}:<id>") 十六進制升序取序——合格池全數入選）
- 金標文件：benchmark/phase3/holdout6/test_gold.jsonl
- 金標 SHA-256：{gold_sha}
- 盲測 inputs：benchmark/phase3/expansion4/inputs/（LY-6xx 逐例一檔）
- 狀態：**未開封**。開封須按 PROTOCOL 預註冊後由評分角執行，並在本文件與
  benchmark/phase3/holdout6-seal-log.md 追加開封記錄。
- 紀律：數據角、修訂角不得讀取 test_gold.jsonl 內容。
"""
    (H6DIR / "SEALED.md").write_text(sealed, encoding="utf-8")
    seal_log = f"""# holdout6 封存日誌

## {now} 封存（數據角，expansion4）
- 新例總數：{len(cases)}（《增刪卜易》卷一 {len(Z)} 例＋《卜筮正宗》續收 {len(B)} 例）
- 合格池（A∩low∩雙完整）：{len(eligible)} 例 → holdout6 {len(holdout)} 例（不足 25，全取，不放寬標準）
- dev-add：{len(devadd)} 例（答案存 expansion4/dev-add-answers.jsonl）
- 排序鍵：sha256("{ROUND_TAG}:<id>") 十六進制升序
- 金標：benchmark/phase3/holdout6/test_gold.jsonl
- 金標 SHA-256：{gold_sha}
- 狀態：未開封
"""
    (P3 / "holdout6-seal-log.md").write_text(seal_log, encoding="utf-8")

    # ---- inputs 泄漏自檢 ----
    bad = []
    for c in cases:
        p = OUTDIR / "inputs" / f"{c['id']}.json"
        t = p.read_text(encoding="utf-8")
        for kw in ["master_predictions", "outcome", "statement_excerpt", "key_assertions",
                   "果於", "果于", "後果", "后果", "斷曰", "断曰"]:
            if kw in t:
                bad.append((c["id"], kw))
    assert not bad, f"inputs 泄漏: {bad}"
    print("inputs 泄漏自檢: CLEAN")
    print(f"holdout6: {len(holdout)} 例，金標 SHA-256 = {gold_sha}")
    print(f"dev-add: {len(devadd)} 例: {[c['id'] for c in sorted(devadd, key=lambda x: x['id'])]}")
    print(f"內部重複登記（僅通報）: {internal_dups}")

if __name__ == "__main__":
    main()
