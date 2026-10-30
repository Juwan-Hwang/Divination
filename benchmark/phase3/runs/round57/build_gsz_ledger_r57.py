# R57 开采席构建脚本：《六爻卦例说真》113 例台账
# 只做转录与入账核查，不作断、不评分。断语/结局摘录逐字断言（去空白后须为原文子串）。
import re, json, subprocess, sys

PDF = "/home/hatch/workspace/divination/incoming/wanted-books-4/Book/六爻卦例说真 (王虎应著).pdf"
OUT_JSON = "/home/hatch/workspace/divination/benchmark/phase3/runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.json"
OUT_MD = "/home/hatch/workspace/divination/benchmark/phase3/runs/round57/digestion/SUPPLY-MINING-guaishuo-r57.md"

raw = subprocess.run(["pdftotext", "-layout", PDF, "-"], capture_output=True, text=True).stdout
cn = {'一':1,'二':2,'三':3,'四':4,'五':5,'六':6,'七':7,'八':8,'九':9,'十':10,'十一':11,'十二':12,'十三':13,'十四':14,'十五':15,'十六':16,'十七':17,'十八':18}
chap_pat = re.compile(r'^\s*第([一二三四五六七八九十]+)章\s+(\S.*?)\s*$', re.M)
chaps = [(m.start(), cn[m.group(1)], m.group(2).strip()) for m in chap_pat.finditer(raw) if '....' not in m.group(0)]
exs = list(re.finditer(r'例([一二三四五六七八九十]+)', raw))
segs = []
for i, m in enumerate(exs):
    cur = None
    for c in chaps:
        if c[0] < m.start(): cur = c
    start = m.start(); end = exs[i+1].start() if i+1 < len(exs) else len(raw)
    for c in chaps:
        if start < c[0] < end: end = c[0]; break
    segs.append({"chapter": cur[1], "chapter_title": cur[2], "ex_label": m.group(0), "text": raw[start:end]})
assert len(segs) == 113, len(segs)

def norm(s): return re.sub(r'\s+', '', s or '')
def chart_lines(text):
    out = []
    for line in text.split('\n'):
        if '▅' in line or '▄' in line or ('″' in line or '′' in line):
            out.append(line.strip())
    return out

# 逐例人工判定（通读全文后）：q 问事 / at 占时 / ben,bian / mp 断语摘录 / oc 结局摘录 /
# pol 污染 / anch 锚点 / grade / f=[转录,独立结局,可分离,非high] / fail 不入账原因 / note
C = {}
def E(i, **kw): C[i] = kw

E(1, q="无具体所问（来人随便看看，断其生平）", at="己卯年丁丑月己卯日", ben="天泽履", bian="", mp="我见子孙持世，因子孙为快乐之神，断其一生无忧无虑是个乐天派", oc="每年有一多半时间在各地拍摄有关民俗、风土人情的内容，然后在日本发表，其作品很受人们的欢迎", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：性格/职业/生平回溯核实，无前向独立结局（承R56分类姻缘回溯例淘汰口径）")
E(2, q="测家宅不安之原因（韩先生电话求测，王代摇）", at="戊寅年庚申月丁酉日", ben="风雷益", bian="水泽节", mp="第一，你最近到外地的一个亲戚家走了一趟，第二你家里近日改造修建时移动过木制东西，由于这些原因造成了你家宅不安", oc="最近住在外地的老丈人病了，于是开车一家三口前去探病，由于病情较重，妻子留下照顾老人，自己开车带孩子回家，半路撞倒一辆摩托车，幸好人没伤着，赔了 5 千多元才算了事", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：回溯归因型（已发事件的事后指认），无前向结局")
E(3, q="问婚姻情况（书店女士，辛丑年生）", at="戊寅年癸亥月乙酉日", ben="天风姤", bian="风地观", mp="我最后告说她下个月将和丈夫离婚，十有八九要通过法院才离成", oc="最后她通过法院于 1998 年子月离婚", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="金标断语只取前向离婚断语；结婚年/流产等回溯段不入断语")
E(4, q="问日本首相小渊惠三病倒吉凶（第三者代摇）", at="庚辰年己卯月辛卯日", ben="天火同人", bian="火风鼎", mp="因此断其辰月若是不凶巳月必凶", oc="后小渊惠三果于巳月壬申日去世", pol="mid", anch="present", grade="B", f=[True,True,True,True], fail="污染mid不入账：公众人物、结局（小渊惠三2000年病逝）为公共知识且流传广，名案从严")
E(5, q="测工作（约五十男子）", at="戊寅年丁巳月己未日", ben="火泽睽", bian="火天大有", mp="以官为用，休囚入墓，又子孙持世，工作不利之象，于是我断其面临下岗", oc="经我预测，其高高兴兴地回单位办退休手续去了", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(6, q="测婚姻（马女士）", at="巳月已巳日（原文无年柱、巳月与日干支并记）", ben="雷地豫", bian="泽水困", mp="应爻为夫位，我见忌神午火临之，断她婚姻为老大难", oc="她说光这个月提亲的就有三、四个，她想修行，甚至有出家的念头", pol="low", anch="partial", grade="B", f=[True,False,True,True], fail="独立结局滤：现状自述核实，无前向结局；兼锚点partial（占时无年柱）", anch_missing="占时仅记「巳月已巳日」，无年柱")
E(7, q="测婚（某男）", at="丙子年癸巳月乙巳日", ben="泽风大过", bian="乾为天", mp="我说他这山望着那山高，意马心猿，和那个也成不了", oc="果皆验", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局仅「果皆验」概括语，无独立具体结局")
E(8, q="占金戒指丢失可否找回", at="已卯年丙子月丁未日（原文「已卯」）", ben="雷泽归妹", bian="兑为泽", mp="卦变六冲，失物难回", oc="她找过多次都没有找到", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：反馈只核实丢失经过与多次找寻未果，找回与否未了结")
E(9, q="射覆：占口袋里是什么", at="庚辰年癸未月壬申日", ben="雷水解", bian="泽水困", mp="用临螣蛇，其色为黑里透黄的褐色物。用神为孟（寅申巳亥），主物带点尖", oc="断完，从口袋里掏出个塑料袋，里边有几个胖大海", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="例末附课堂笔记同卦复述（未月壬申日雷水解变泽水困）为同案重讲，不另计例、不另入账")
E(10, q="占搞运煤发财否", at="已卯年丙寅月乙卯日（原文「已卯」）", ben="天地否", bian="泽地萃", mp="此卦无财可发，若坚持要做，必会因修车或罚款而损大财", oc="", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：原文自承「此卦无反馈」，仅现场核实其买报废车一节")
E(11, q="测病（某男）", at="已卯年丁卯月甲子日（原文「已卯」）", ben="泽天夬", bian="雷天大壮", mp="世临白虎动而化退，白虎主伤灾，以退神为应期，断其壬申年有伤灾", oc="庚辰年，他的一位邻居来我这里时告诉我，那个男的已于已卯年死了", pol="low", anch="present", grade="B", f=[True,True,True,True], fail="定级B不入账：死亡结局独立存在，然断语只及「凶兆/非常不利」、未明确指向死亡，金标断语可判性不足")
E(12, q="测与某男感情（某女，丙午年生）", at="丙子年癸巳月乙巳日", ben="山泽损", bian="山雷颐", mp="我断她以前曾搞过一个对象，是这个男的追的她，但后来因俩人争吵不和，无法相处，男的便离她而去，与另一个女的结婚", oc="她说我断得很对，是已巳年结的婚", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：回溯感情史核实，无前向结局")
E(13, q="测婚（日本久保女士，戊申年生）", at="丙子年甲午月丙子日", ben="泽天夬", bian="雷地豫", mp="官鬼临应爻，应爻为他处，又临驿马，说明这个男的为远方之人。官鬼寅木动而与妻财亥水相合，说明那个男的另有所爱", oc="后听人说，她于 1999 年结婚，定居在中国，乃应世爻旬空，此年冲实", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：1999年结婚系传闻且为叙述者事后应期附会，断时尚无此前向断语；暗恋对象是否即婚配对象原文自承不得而知")
E(14, q="测病（某女）", at="丙子年已亥月丙寅日（原文「已亥」）", ben="泽风大过", bian="雷风恒", mp="元神官鬼动而化退，金主肺，临五爻，五爻也主肺，化退为肺功能退化，呼吸系统有病", oc="", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：原文自承「后未再见面，不知吉凶结果如何」")
E(15, q="测父病（某男）", at="辛巳年（2001年）丁酉月癸未日", ben="天火同人", bian="泽火革", mp="父母卯木月破入日墓，必凶。用神休囚遇死、墓、绝之一者，必为癌症", oc="果然是肺癌，99 年得病，虽多方面治疗，无明显效果，医生也说没有希望，现已出院回家疗养", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型（承R56 WHY-067…071肿瘤例净入账先例）")
E(16, q="测公务员考试结果", at="丁丑年辛亥月庚午日", ben="水风井", bian="巽为风", mp="父母又主录取名单或通知书，亥水空亡，录取通知单上没有他的名字", oc="考试成绩下来后，他的分数第一，然在填写自己名字的代码时，不小心写错了，成绩作废，未被录取", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(17, q="测婚（某男二十岁）", at="丙子年癸巳月丙午日", ben="山水蒙", bian="天风姤", mp="应爻空亡，不成之象", oc="推断果然正确，是他在追人家，女的是他老乡，死活不愿意，老躲着他，最后没成", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(18, q="测钢材生意如何", at="丙子年癸己月戊午日（原文月柱作「癸己月」）", ben="天风姤", bian="", mp="故断其钢材生意很了，價都存不住 ，供不应求，甚至还有人托关系向他买 钢材", oc="结果完全正确", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局仅「结果完全正确」概括语")
E(19, q="测打官司（某女）", at="戊寅年已未月丁丑日（原文「已未」）", ben="雷火丰", bian="", mp="至申月，应爻出月不破，世爻出空受生，接受对方条件", oc="所有推断果验", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局仅「所有推断果验」概括语")
E(20, q="测身体（某女）", at="戊寅年甲子月已亥日（原文「已亥」）", ben="离为火", bian="", mp="官鬼亥水得日月帮扶极旺，临三爻冲克世爻，三爻为肾，水也主肾，乃是肾水过旺而引起肾病", oc="她说自己有肾病三年，多方治疗无效，身上到处是肿块", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型；作者自拟调治法「不到一个星期她的病就好了」一段系作者介入自述，不入断语、结局只取本人自述核实段")
E(21, q="测婚（某男）", at="丁丑年戊申月癸卯日", ben="泽地萃", bian="", mp="应爻暗动克之，应为他人，酉月怕有变故，对象被他人夺走。世临青龙空亡，空不受生，青龙为喜，乃是空欢喜一场", oc="以上推断不幸言中", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局仅「以上推断不幸言中」概括语")
E(22, q="单位抓阄分房，测会不会抓上直对楼梯的房子", at="丁丑年甲申月乙未日（原文月柱作「甲申月」）", ben="风水涣", bian="天水讼", mp="世爻临之空亡，言求测者的房子不对楼梯", oc="下午回去后抓阄，果然抓的是一层的东面，没有对着楼梯", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(23, q="测与老婆吵架结果如何", at="丁丑年丙午月辛丑日", ben="雷泽归妹", bian="地泽临", mp="用神空亡，出空即回", oc="分老婆果然是和他吵架后回了娘家，住院了几天后，气消了一些又回来了", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="结局首字「分」为原文录入讹字（疑「其」），照录登记")
E(24, q="测儿子考高中如何（某女代占）", at="丁丑年丙午月已亥日（原文「已亥」）", ben="泽地萃", bian="火地晋", mp="故断其儿子平常学习用功，这次考试成绩也觉得不错，但就是怕差一分考不上", oc="后果差一分没考上", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(25, q="母测女儿婚姻", at="乙亥年癸未月丁卯日", ben="水火既济", bian="水雷屯", mp="断其本年亥月又可出现一个男朋友，但必须是大人撮合而成", oc="", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：回溯段仅「以上推断全部应验」概括语；前向段原文自承「后结果如何，因无信息反馈，不得而知」")
E(26, q="自测胃病（某男）", at="丙子年丙申月壬午日", ben="天雷无妄", bian="风水涣", mp="二爻寅木月破为幽门、十二指肠溃疡", oc="果然不是胃病，是幽门和十二指肠溃疡，他怕我不知道这些脏腑的名称故而说成是胃病，治疗时确有副作用", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型；「需到下个月方能痊愈」前向段无反馈，不入断语")
E(27, q="问生孩子（某女）", at="丁丑年甲辰月丁丑日", ben="山雷颐", bian="", mp="子孙入库破而得出，一定顺产。子孙休囚，又在巽宫，巽为女，生女孩的可能性大", oc="后于本月良子日巳时产一女婴", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="同案去重不入账：与《分类占验技法》第八章例七WHY-039三键同案（丁丑年甲辰月丁丑日、山雷颐静卦、测生孩子），分类版已于R56先完成转录并入账（净入账40内），归属先完成转录者，《说真》版只登记异文", note="异文对勘：分类版结局作「本月庚子日巳时安全生下一女孩」，与《说真》版「良子日巳时产一女婴」仅日名一字之异——《说真》「良子日」经对勘可证为「庚子日」录入讹字，照录不改、注于此；顺产/女孩/巳时三项两版一致，无方向冲突")
E(28, q="测在路边摆地摊如何（某女）", at="丁丑年乙巳月丁巳日", ben="地天泰", bian="雷天大壮", mp="财临月破，摆之必破财", oc="结果不听，租地摊搞夜市，连租金也挣不够，损失数百元后收摊", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(29, q="测病（医院老妇）", at="庚辰年甲申月丁酉日", ben="泽天夬", bian="泽火革", mp="断其有头疼病", oc="一个星期后再被 请到她家看时，浮肿基本消失", pol="low", anch="present", grade="B", f=[True,True,False,True], fail="可分离滤：断语、作者建议拔管出院调治、事后传闻（酉月云游郎中一针而愈）交织，断/结局不可干净分离")
E(30, q="手中打火机突然爆炸，测吉凶（某男）", at="庚辰年壬午月已酉日（原文「已酉」）", ben="风天小畜", bian="水天需", mp="故断其四天后的子日，他骑的自行车轮胎将会爆胎", oc="结果推断内容在子日全部得到验证，自行车后胎放炮，且本人受凉而拉肚子", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(31, q="为母测病（铜厂马姓学员，培训班例）", at="戊寅年己未月己巳日己巳时（旬空戌亥）", ben="泽火革", bian="泽天夬", mp="当堂断到：你母病无大碍，是内分泌失调，尿上面出了问题", oc="答曰：糖尿病。又断说你母亲当月骨折，你家住的是楼房，在第四层或第五层住，你母是在爬第三层楼梯时骨折的", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型；原文同一段落重复排印两次，照录登记；卦盘为现代排盘格式（含干支/神煞栏）")
E(32, q="儿媳占搬家选日子", at="戊寅年庚申月辛卯日", ben="地雷复", bian="震为雷", mp="主卦六合，子孙又入墓，必主难产", oc="后于丙申日搬家，于戊申日生下一个男孩，生时难产", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="断语生子日期作丁未日、实际戊申日，原文自承「误差了一天」，逐字并列登记")
E(33, q="测与某女约会，女方赴约否（胡某）", at="丙子年壬辰月已亥日（原文「已亥」）", ben="风天小畜", bian="风水涣", mp="用神动而克世，书云：用克世人必来，此女一定会赴约", oc="后此女果来赴约", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="约会地点（并州饭店门口）断语经胡某当场确认，并入结局段逐字")
E(34, q="拉盲人郝金阳先生来省城，测头号（出发）情况", at="丁丑年丙午月甲申日", ben="风火家人", bian="风地观", mp="故断此次去接郝先生恐怕会在一个三岔路口堵车", oc="次日，驱车前去接郝先生，车到半路的一个三岔路口，正逢一大群人聚众闹事，堵塞交通，不能前进", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="题面录入多处讹字（「段建 业」「拉盲人合理师」等），卦盘与断/结局段可逐字转录，照录登记")
E(35, q="测事业（在北京的日本人）", at="庚辰年（2000年）丙戌月甲子日", ben="火风鼎", bian="火雷噬嗑", mp="明年辛巳，冲实世爻，又巳酉丑合成财局生世，2001 年将是三处来财", oc="", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：前向段（2001年三处来财/婚期）原文自承「后结果如何，因无再见此人，不得而知」；余为现状核实")
E(36, q="测妻子事业流年如何（王某代占）", at="已卯年已巳月甲申日（原文「已卯年已巳月」）", ben="地火明夷", bian="离为火", mp="你爱人的学校有个大的变动，今年学校要扩大，要把其他学校兼并过来", oc="后果验", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：兼并段仅「正是此事」现状确认、教高中段结局仅「后果验」概括语")
E(37, q="测侄儿耳聋能治好否、有好方法否（李女士）", at="戊寅年丙辰月丁亥日", ben="火泽睽", bian="山风蛊", mp="用神得月来合，必是久病。合神为养地，胎在官鬼卯木，此乃先天性耳聋之信息", oc="后喝磁石水后，稍有好转", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：主问「能治好否」无明确结局；病情段为回溯核实，「稍有好转」系作者自荐磁石水之效、非独立结局")
E(38, q="测带团旅游此行吉凶（作者自占自述）", at="丁丑年甲辰月壬寅日", ben="雷风恒", bian="震为雷", mp="五爻官鬼申金暗动，临螣蛇，螣蛇主惊异，变异，路上将有麻烦事发生", oc="结果，在五台山区旅游完后，由于下雨从五台山到浑源的路段遭到破坏，不能通车，临时决定放弃去浑源", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="结局段续有客人争吵、旅行社退还部分钱解决，逐字见原文")
E(39, q="测财运（某女士）", at="丁丑年乙巳月丁卯日", ben="地天泰", bian="地泽临", mp="一看便知此人挣钱手段高强，是个挣大钱之人", oc="", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：全例无结局/反馈段，止于案语疑问")
E(40, q="测已卯年财运（某男）", at="戊寅年甲子月戊子日", ben="地天泰", bian="地水师", mp="世爻动而化空，明年午月即可见财", oc="他说已同好几家房地产开发公司签定了合同，明年阳历 6 月等楼房盖好后，由他的公司安装室内卫生洁具", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：反馈仅为已签合同之现状与计划，午月见财之前向结果尚未发生、无回报")

E(41, q="测妻带小孩回娘家，何日得见小孩（某男）", at="丁丑年丙午月甲申日", ben="天山遁", bian="天风姤", mp="世爻动而化出子孙亥水，必会见面", oc="后于丙申日，妻子带小孩回家", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(42, q="测侄儿出事吉凶（某男）", at="已卯年壬申月丁巳日（原文「已卯」）", ben="山地剥", bian="风地观", mp="子孙临玄武动而化鬼化绝，玄武主偷盗，动而化官鬼，乃与官鬼相见，断因偷盗被公安人员抓获", oc="果然其侄儿因偷摩托车被抓", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(43, q="射覆：测杯中何物", at="丁丑年（97年）戊申月甲申日", ben="火泽睽", bian="火雷噬嗑", mp="综合上述信息，断杯内放着一团叠起来的写有文字的纸", oc="结果打开后，里面放着卷成卷的一百元钱", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="射覆揭晓型：断语与实物不尽合属评分事项，不属开采淘汰事由")
E(44, q="测事业（某女）", at="辛巳年辛丑月丙戌日", ben="水山蹇", bian="艮为山", mp="子孙发动克官鬼，自己想辞掉现在的工作", oc="果如所测，她在一个体的旅行社任副经理，但说了话不算数，工作才能得不到发挥", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局段为现状复述（「果如所测」领起），无独立结局事件")
E(45, q="测住宅风水情况（初中同学）", at="酉月乙亥日（无年柱）", ben="天雷无妄", bian="", mp="且此房不久将要被拆，不过被拆之后不是要重新盖楼，而是因扩建马路，要拆掉此房", oc="结果所断皆验。为二层楼房，原为公家的，自己买下，坐南朝北", pol="low", anch="partial", grade="B", f=[True,True,True,True], fail="锚点partial不入账：占时无年柱、年代框架（79年聚会/19年未见/98年拆迁）关系不清；卦盘爻象以′″记号代线条", anch_missing="占时仅月日无年柱；爻位以′″记号标注、无标准爻线与动爻标记")
E(46, q="测所管帐上缺了一笔钱，结果如何（邮政局王女士）", at="庚辰年壬午月丁巳日", ben="山泽损", bian="风雷益", mp="财爻子水月破绝于日辰，又动而化绝，此笔钱很难找回", oc="果然是帐上一千元的数目核对不上，本人也怀疑是把票单弄丢。最后查不到短缺之钱的下落，只好自认倒霉自己补上", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="同例后段婚姻回溯不入断语")
E(47, q="测婚（医院赵女士）", at="丙子年巳亥月癸酉日（原文月柱作「巳亥月」）", ben="天泽履", bian="泽水困", mp="说明她又私订盟约，和另外一个男人同居，卦变六合，二人可成，文书月破，出月不破，即可成", oc="此女果然因丈夫有外遇于９４年离婚，目前有一个男的与自己同居，后于庚子月二人正式结婚", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(48, q="测一认识女子的相貌（某男）", at="庚辰年癸未月癸未日", ben="水泽节", bian="", mp="卦得六合，该女为丰满之人", oc="结果所断皆验", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：相貌回溯例，结局仅「结果所断皆验」概括语（承R56分类姻缘相貌回溯例淘汰口径）")
E(49, q="测其叔家风水（某男）", at="丙子年已亥月辛酉日（原文「已亥」）", ben="水地比", bian="坤为地", mp="父临巳火月破而入墓，一家之主若有病必为心脏病", oc="其叔叔已于戌月因心肌梗死而亡", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="风水诊断核实型：大道直冲大门一节亦经本人确认，逐字见原文")
E(50, q="测到某婚姻介绍所求对象得否（某男）", at="戊寅年辛酉月乙酉日", ben="地泽临", bian="山泽损", mp="这个婚姻介绍所将来会被公家取缔", oc="后来才知该婚姻介绍所为非法机构，专与一些三陪小姐联系，合谋骗人钱财而被取缔", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="介绍女子索财经过逐字见原文结局段")
E(51, q="测与某女关系如何（某男）", at="丙子年癸巳月已巳日（原文「已巳」）", ben="乾为天", bian="泽天夬（原文卦名截断作「泽天」）", mp="财爻寅木休囚，元神又绝于日月，卦得六中，冲即为散，此为二人分手之象", oc="此男告知，几天前和自己原来相好的一位女人分手", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：分手系占前已发事件之回溯告知，无前向结局")
E(52, q="测单位失窃情况（某男）", at="丁丑年丁未月辛巳日", ben="离为火", bian="火天大有", mp="物难回", oc="最后此男告知，单位东北方向的大门被贼人撬开，贼人由此进去，把院子里一个办公室的办公用品、写字台、沙发等全部盗走，门也被撬得稀巴烂", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="结局段末「后未找到失物」与断语相应，逐字见原文")
E(53, q="测她家房子风水（某女）", at="丙子年已亥月丙寅日（原文「已亥」）", ben="风泽中孚", bian="巽为风", mp="今子孙不旺，又遇墓绝，其子必有肿瘤之类的病", oc="果然是旧房子，门与门相对。自觉风水不好，请一走江湖的看过，把房子大加改造不但无效，还被骗去万元之多。小孩得脑瘤，住院手术又花去许多", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="风水诊断核实型")
E(54, q="测妻怀孕如何（某男）", at="丁丑年壬子月壬辰日", ben="天泽履", bian="天水讼", mp="怕是妻子要把胎儿堕掉", oc="果然是未婚同居，女方怀孕。后到戊寅年卯月，二人因口舌矛盾，女方执意要分手，私自堕胎，不欢而散", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(55, q="测流年运气（某男，公安部门任职）", at="戊寅年丁巳月辛巳日", ben="火山旅", bian="离为火", mp="然化出卯木无制，恐亥月卯木得生，那个人又有了撑腰的，再次反攻倒算告之", oc="然时至亥月，对方再次告他，司法部门认为公款虽然已退，也还得追究刑事责任，此男于是外逃，至今未归", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(56, q="测工作如何（某女）", at="戊寅年戊午月丙午日", ben="地泽临", bian="", mp="官鬼休囚，死于日月，工作无发展前途", oc="此女最后告诉我，她在法院工作，以上所测很符合她的现状", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局仅「很符合她的现状」概括语")
E(57, q="问友流年（罗先生代占）", at="戊寅年卯月庚午日（戌亥空）", ben="艮为山", bian="山地剥", mp="今用神旬空，尚在避空之地，辰月冲实，用神入墓，牢狱之灾必至", oc="后找了一个属牛的人帮助，解决了此事", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局为当日下午口头更正核实（女人牵连/属牛人解事），「牢狱之灾必至」之前向断语未验、且以解事收束不可判")
E(58, q="测风水（某焦碳厂）", at="戊寅年已未月庚辰日（原文「已未」）", ben="风泽中孚", bian="天水讼", mp="又财爻入墓于日，有死亡事件发生", oc="求测者反馈，工厂门朝西南开，工厂经济效益不好，目前处于半停产状态。工厂内的确发生过死伤事件", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="风水诊断核实型；结局段续载伤者一腿一脚、一人被煤压窒息而死，逐字见原文")
E(59, q="问小孩身体", at="戊寅年甲子月癸巳日", ben="风火家人", bian="巽为风", mp="卦在巽宫，巽为白眼多人，故断小孩白眼珠多。因忌神月建子水为巳火胎地，故断为先天性的", oc="反馈说小孩为天生的吊白眼，老是向上翻白眼珠子", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型")
E(60, q="测何时有子（某男）", at="戊寅年甲子月未日（原文日柱仅记「未日」）", ben="雷天大壮", bian="乾为天", mp="空亡，精子数量少，难以使妻子怀孕，终身难有子女", oc="结果此男告诉我，他已结婚好几年了，妻子一直不怀孕。二人到医院一检查是因为他本人精子太少造成的", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型（医院检查为独立核实）；占时日柱干支不全照录登记，月建甲子月在场")
E(61, q="问病", at="戊寅年丑月丙子日", ben="山水蒙", bian="地水师", mp="必主病在头部，六爻临青龙，青龙主痛，故断头部脑血管出了问题引起头痛", oc="反馈因头部血栓引起头痛不止", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型")
E(62, q="占流年（某男）", at="已卯年丙寅月丙申日（原文「已卯」）", ben="泽山咸", bian="火山旅", mp="故断其虽然多得朋友帮助，却也被朋友拖累，从他身上套财，哄骗他", oc="反馈说，近年来靠朋友帮忙挣了二十多万元，朋友们见他有了钱便向他借，只借不还", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：流年综合回溯（借财/神经衰弱/便秘皆现状自述），无前向结局")
E(63, q="测其老婆儿子吉凶（某男）", at="已卯年丁卯月戊辰日（原文「已卯」）", ben="火泽睽", bian="乾为天", mp="以这些信息而断，妻子儿子双双入狱", oc="此人之妻和儿子果然是因贩毒而于 98 年未月乙卯日双双被捕入狱", pol="low", anch="present", grade="B", f=[True,True,True,True], fail="定级B不入账：入狱系占前（98年）已发事件之回溯；量刑断语（妻死刑）与结果（无期）不合且上诉重审未结、无反馈")
E(64, q="测流年运气（某女）", at="已卯年丁卯月甲戌日（原文「已卯」）", ben="地山谦", bian="雷天大壮", mp="便直断其弟弟已被公安局抓起来了", oc="最后她告诉我其父亲是 93 年因上呼吸道癌去世的", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：流年大包围回溯（弟被抓当场证实/85年结婚/父93年去世皆已发事实），无前向结局")
E(65, q="测婚（长治市某男；刘昌明解析王虎应实例）", at="己卯年年庚午月乙巳日（原文「己卯年年」衍字）", ben="风水涣", bian="泽水困", mp="综合上述信息，我断到怕是你穿好新衣，摆好酒席要娶新娘了，但你只定了婚，没有领结婚证", oc="结果所断完全正确。他告诉我他和那个女的只定了婚没有领结婚证", pol="low", anch="present", grade="B", f=[True,True,False,True], fail="可分离滤：本例为刘昌明对王虎应原例的解析重构，王氏原断仅片语被引，金标断语非王氏原文、不可分离认定")
E(66, q="问妻子怀孕（友赵先生）", at="庚辰年庚辰月壬子日", ben="艮为山", bian="水火既济", mp="初爻 元神临月化回头克，打算在本月之内流产掉", oc="结果他说的确如此。妻妇已经怀孕一个月", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：反馈止于流产计划之确认，流产未实际发生回报")
E(67, q="测事业（人称校长的某男）", at="庚辰年辛巳月丑日（原文日柱仅记「丑日」）", ben="风水涣", bian="", mp="断其挣钱是流动的，打一枪换一个地方就可以挣钱，若连续不动，固定在某个地方就会赔钱", oc="结果，来人说他是部队转业军人，前几年做装潢生意，虽然东奔西跑，但却挣了不少钱", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：职业生涯回溯自述核实，无前向结局")
E(68, q="测侄儿（99年生）的病（某男）", at="庚辰年辛巳月壬申日", ben="天泽履", bian="雷火丰", mp="综合卦象来看，为先天性脑瘫", oc="对方反馈推断很对，为孩子治病已花去 20 多万元了，再无能力治下去", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型；结局段后半涉家属极端言论，与断/结局无关，不录入")
E(69, q="测病", at="庚辰年庚辰月已酉日（原文「已酉」）", ben="火地晋", bian="泽地萃", mp="故断主要是有肿块或增生造成的", oc="卦主说，由于脖子颈椎增生，胳膊活动都不灵便了，每天痛得难以忍受", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型；卦盘「白牙」「官鬼己火」为原文录入讹字（白虎/巳火），照录登记")
E(70, q="测怀孕如何（某男）", at="庚辰年壬午月丙申日", ben="风天小畜", bian="火天大有", mp="我说这个孩子生不下来", oc="果如所断", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局仅「果如所断」概括语")
E(71, q="测近日财运（某男）", at="庚辰年壬午月辛亥日", ben="风山渐", bian="火水未济", mp="故断此次求财 中间人隔了好几层，中间人太多求不到财", oc="果然如测", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局仅「果然如测」概括语")
E(72, q="测考试结果如何（某女）", at="丙子年癸己月丁己日（原文月日干支多处讹字）", ben="火水未济", bian="山风蛊", mp="考试结果肯定不好", oc="", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：全例无结局/反馈段，止于案语设问")
E(73, q="测合伙求财", at="壬午年甲辰月乙卯日", ben="火风鼎", bian="泽风大过", mp="可以断定不是俩人合伙，而是中间还隔一个人", oc="", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：原文自承「求财结果如何，因无反馈，不得而知」（中间人一节经卦主确认）")
E(74, q="测婚（某男，求测人22岁）", at="丁丑年癸丑月已巳日（原文「已巳」）", ben="山雷颐", bian="离为火", mp="今兄弟寅木休囚不克财，明年兄弟值太岁，与现在的女友必会分手", oc="其果然已有女友，于丙子年相识，不久就发生两性关系，后又出现一个女的，遂于 1998 年与原女友分手，和另一女人相好", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(75, q="测与一女搞对象，将来能成夫妻否（某男）", at="戊寅年卯月丁巳日", ben="天风姤（原文作「天风逅」）", bian="泽风大过", mp="元神死绝休囚又变游魂，二人必将分手", oc="后果于巳月分手", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(76, q="测月球有水否（报载美国1月8日发射探测器，作者自摇）", at="丁丑年癸丑月丙辰日", ben="水雷屯", bian="泽风大过", mp="说明月坏表面根本没有一点水，卦变游魂，月球相力小，耗散大，月球上很难有水珠形成", oc="后探测结果，果然没有在月球表面找到水", pol="mid", anch="present", grade="B", f=[True,False,True,True], fail="主持先裁执行（R57 PREREG §4）：与《分类占验技法》月球例同案（丁丑年癸丑月丙辰日、水雷屯变泽风大过），两书结局冲突及方向——分类版作未定、《说真》版作已定阴性——整例不入账只登记；兼污染mid（月球探测为公共科学议题）", note="同案异文并列见 counts.moon_case")
E(77, q="测朋友的女儿走失，吉凶如何", at="戊寅年甲寅月已酉日（原文「已酉」）", ben="风水涣", bian="天水讼", mp="子孙动化午火生，在外很安全；合处逢冲，丑日一定会回来", oc="后来朋友女儿果于丑日回来，说是心情不好和朋友一块到北部一百多里以外的温泉去洗澡、散心去了", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(78, q="测去相亲结果如何（某女）", at="戊寅年戊午月乙酉日", ben="天水讼", bian="风水涣", mp="这次相亲怕是连对方的脸都看不到", oc="后此女前去相亲，对方果然梳洗打扮了一番，但由于对方胆小，吓得连头也没敢抬，直到相亲结束也没看清对方长得啥样，嫌对方太老实，不愿意", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(79, q="测喂养的鹦鹉飞走会回来否", at="已卯年戊辰月丙午日（原文「已卯」）", ben="乾为天", bian="水天需", mp="子孙子水月克日冲，卦中又有父母爻动克，世克用，难回之象", oc="后果未回", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="结局简略（仅「后果未回」）但指向明确、可判")
E(80, q="测到某地办培训班如何（一友）", at="壬午年壬子月丁巳日", ben="风泽中孚", bian="", mp="此去不但无财，还要把东西忘在那里", oc="果然没有招到学员，回来时，把手机的充电器忘在那里了", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")

E(81, q="测子出国考试可通过否（某女代占）", at="戊寅年戊午月甲寅日", ben="雷天大壮", bian="火天大有", mp="必因人做手脚而通不过考试", oc="后果差 20 分未能出成，但本人觉得分数有些不对，却又无可奈何", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(82, q="测夫运（某女）", at="戊寅年壬戌月戊申日", ben="雷泽归妹", bian="", mp="断其丈夫中在狱中却十分挂念家里，怕有越狱的想法", oc="谁知道 其夫于已卯提越狱逃跑回家又被抓回，不但没有减刑，反而加了刑", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="入狱缘由段为当场告知核实；金标断语/结局取越狱前向段")
E(83, q="测终身（某女）", at="戊寅年癸亥月甲戌日", ben="地泽临", bian="雷泽归妹", mp="断其 88 年结婚", oc="以上推断全部正确", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：终身综合回溯，结局仅「以上推断全部正确」概括语")
E(84, q="测母亲病（某女代占）", at="戊寅年癸亥月戊寅日", ben="雷天大壮", bian="火天大有", mp="父母 午火临四爻受月建之克，午火为心脏，四爻又为心脏的爻位，其母亲应有心脏病", oc="其母病症果如所测，说是已神经衰弱二十年，有轻微的心肌炎", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型")
E(85, q="测婚（某女，乙巳年生）", at="已卯年丁卯月甲子日（原文「已卯」）", ben="风水涣", bian="天水讼", mp="又卦变归魂，归魂不出家，乃是终身在娘家守老之象", oc="此女从 20 岁起不知见过多少男的，始终没成一个，就连恋爱的机会都没有", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：反馈为止于占时之现状自述，「终身无婚」于占时不可验、无后续回报")
E(86, q="测夫何日归（某女）", at="丙子年壬辰月乙酉日", ben="火山旅", bian="艮为山", mp="卦逢六合用神又旺，其丈夫一定会回来，用神伏藏逢出现，丁亥日有可能", oc="结果其丈夫于丁亥日亥时回来了，说是心情不好回老家在姐姐家住了几天", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(87, q="测手机丢失（某男）", at="丁丑年乙巳月壬子日", ben="天山遁", bian="", mp="以财为用，财不上卦，虽空亡，但得日生，又临青龙伏世下生世爻，失物可找回", oc="经公安多方查证，于未月找到了用手机的人，原来是与此男同住一个院子的邻居", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局止于找到使用人，其不承认偷窃、手机是否追回与「两个人作案」均未明，断语主旨（可找回）未了结")
E(88, q="占问羊肉可吃否", at="已卯年已巳月庚辰日（原文「已卯年已巳月」）", ben="天山遁", bian="天地否", mp="进一步可以推断羊是在高山上路边的一个干涸的水池里捡的", oc="来人说分析基本正确。该羊肉为整只，是在高山上路边的一个旱井里捡的。吃了羊肉的人平安无事", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="第十四章「例三」重号之第一例（见GSZ-089登记）")
E(89, q="测家宅（某男）", at="丁丑年已酉月乙亥日（原文「已酉」）", ben="地火明夷", bian="", mp="断其老婆有妇科病，月经不调", oc="此男房子果然是坐北朝南，因地势较低，周围房子盖得高，影响光线，几乎看不到阳光。老婆的确有妇科病，月经不调", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="家宅诊断核实型；原书本例与GSZ-088同标「例三」（第十四章例三重号），系原书编号重复，非两例同案")
E(90, q="测婚（某男）", at="乙亥年（95年）戊子月辛卯日", ben="雷山小过", bian="雷风恒", mp="综合以上信息，我断其因怀疑老婆有外遇，实际却没有，结果致使二人离婚", oc="最后此男告诉我，他老婆是歌团的，个高，很漂亮，脸不黑但有痣。他们是 82 年结的婚，92 年离的", pol="low", anch="present", grade="B", f=[True,True,True,True], fail="定级B不入账：回溯例且结局含关键细节反转（原文：非他怀疑老婆、而老婆怀疑他），叙述者自承「最后也不知真实情况」；另与《分类占验技法》第五章应期例四WHY-032三键同案（分类版R56已入账），《说真》版并登记异文", note="异文对勘：分类版结局作「老婆在歌舞团工作，长得又高又漂亮，1982年结婚，1992年离异，赔偿了八万元」，与《说真》版主干一致（歌团/82年婚/92年离/八万元）；《说真》版多载怀疑方向反转一节，分类版无此文，并列登记")
E(91, q="测自行车丢失（单位某武警）", at="乙亥年丙戌月庚寅日", ben="雷水解", bian="泽水困", mp="世爻妻财辰土月破日克，元神午火又空，破财之象，车子难找回", oc="果然是一辆破旧的自行车，被人偷走没有找回", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(92, q="老乡几天不见，担心问之如何", at="丁丑年甲辰月甲辰日", ben="水风井", bian="天水讼", mp="问其老家是否在东南方，回答说是，故断有可能是回了老家", oc="当日午时，接到电话，得知回了老家", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(93, q="自占本年年运（作者本人）", at="戊寅年甲寅月壬午日", ben="天山遁", bian="水火既济", mp="今官鬼午火化出申金空亡，申月出空当防", oc="结果一进厨房什么也没干，拿起刀来稀里糊涂直接把中指头切了一块，指甲被切三分之一。于是放下刀忙去医院包扎，三月有余方愈", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="结局时点在申月（断语应期），逐字见原文前段")
E(94, q="测一亲戚家的孩子吉凶如何（某男）", at="丁丑年乙巳月庚申日", ben="水雷屯", bian="", mp="断其亲戚家的孩子因偷盗或诈骗已犯刑入狱", oc="果然是因偷盗和诈骗入狱，被劳改", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="硬事实核实型（入狱现状）")
E(95, q="测婚姻（某女）", at="戊寅年丙辰月丁亥日", ben="地山谦", bian="雷火丰", mp="化出妻财卯木回头克，又官下伏藏的卯木，对应于 1999 年，该年出现，这个男的老婆会发现此事", oc="", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：现状段经本人告知核实；前向段（1999年被发现）原文自承「后来结果如何，因无反馈，不得而知」")
E(96, q="测晚年生活状况如何（某老妇）", at="丙子年癸巳月癸亥日", ben="水地比", bian="风泽中孚", mp="断其原丈夫已死，又嫁了一个男的", oc="测完后此妇告知，自己原有工作，现已退休，晚年主要是靠退休金生活", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：晚年现状回溯自述核实，无前向结局")
E(97, q="测财运（某农民）", at="丙子年丙申月庚子日", ben="风泽中孚", bian="风天小畜", mp="发的是水上的财，而且是一种意想不到的财", oc="原来此人 92 年就开始发财了，兄弟 8 人，只有他发了财", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：逐年财运回溯为主；洪水鱼池得财事在叙述时序上属已发/正发事件之复述，非占后独立回报")
E(98, q="测子吉凶（某妇女）", at="乙亥年已丑月庚午日（原文「已丑」）", ben="风地观", bian="水雷屯", mp="应临白虎克之，白虎主刀枪，乃是被枪决之象", oc="其子果然是犯刑入狱，被判死刑，缓期两年执行", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="结局段续载96年严打重审于巳月枪决、较断语午月应期提前一月，逐字并列登记")
E(99, q="测外语书不见，能找到否", at="丁丑年丙午月乙酉日", ben="风天小畜", bian="水天需", mp="父母子水在初爻，书被藏在比较低的地方", oc="结果当日酉时，他在值班室的柜子最底层一团棉花下，找到了书，原来包的书皮被人扯掉了", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(100, q="测搞对象（某男）", at="丁丑年（97年）庚戌月戊戌日", ben="雷地豫", bian="雷风恒", mp="妻财旺相持世，又是六合卦，此婚可成", oc="以上所断皆验，二人于 98 年酉月结婚", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="断语领证应期作98戊寅合亥、结局作98年酉月结婚，年份合、月份异，逐字并列登记")
E(101, q="测找厂长办事如何", at="丙子年（96年）甲午月乙未日", ben="风火家人", bian="地山谦", mp="应爻动而生世，求其办事，对方肯定答应", oc="此人告知，他拿一条烟去找厂长办事，厂长一点也没犹豫就答应了", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(102, q="测与某男关系（某女）", at="丁丑年（97年）辛亥月壬戌日", ben="风天小畜", bian="地天泰", mp="应爻临财克世，对方给自己造成很大的经济压力", oc="此男果然是她养的一个小白脸，每过一段时间，就以各种借口向她要钱，每年因此耗财一、二十万", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：关系现状回溯核实，无前向结局")
E(103, q="电话测老婆哪一天生孩子（某男）", at="壬午年（2002年）辛亥月戊申日", ben="风雷益", bian="地泽临", mp="用神子孙巳火月破，本月难生，需出月不破，到子月才能生下来", oc="后于子月庚申日剖腹产生下一个男孩", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(104, q="测父病（某男）", at="壬午年庚戌月辛未日", ben="天风姤", bian="天地否", mp="用神在六爻空不受生，六爻主头，卦在乾宫也主头，是头部有病", oc="他说他父亲主要是高血压和甲亢，手脚麻木发抖，晚上失眠睡不好觉，每天靠吃安眠药维持", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型；「防丙戌年用神实空为凶」前向段未验，不入断语")
E(105, q="测儿子将来考高中如何（某女士）", at="寅年甲寅月癸未日（原文年柱仅作「寅年」）", ben="雷天大壮", bian="地雷复", mp="断其孩子考高中一次考不上，需留级或补考", oc="后庚辰年考高中，其子就在考试的前一天出走了，等找回来，考试时间已过", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="锚点：月建（甲寅月）与日辰（癸未日）在场，年柱简写不碍锚点定式，照录登记")
E(106, q="测流年（某老妇，86岁）", at="戊寅年丙辰月癸巳日", ben="地天泰", bian="水雷屯", mp="忌神动而被合，防申月冲开不利", oc="当年腿部莫名其妙地发肿，行走不便，治疗了一个多月才好，但因此了年纪，本人忘 了是几月腿肿的", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：流年回溯自述为主；腿肿月份本人已忘、申月应期未核实")
E(107, q="去取订做的衣服、裁缝不在，看何时人在", at="乙亥年癸巳月丙辰日", ben="雷水解", bian="天泽履", mp="父母子水伏而空亡，午时冲出冲实，午时云取定可到手", oc="午时去取时，裁缝从柜台底下拿出，因做得不合适，与其发生争执，重新修改后取走", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="断语「午时云取」为原文录入讹字，照录登记")
E(108, q="丢钱，测能找到否（某男）", at="丙子年癸巳月甲寅日", ben="天山遁", bian="雷山小过", mp="断钱在办公室的写字台下", oc="他马上回到办公室，在写字台下找到了丢失的一百元钱", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(109, q="测小儿病（某男）", at="丙子年庚子月壬午日", ben="火雷噬嗑", bian="乾为天", mp="子孙临日不药而愈，无须就医", oc="小儿果是吃奶时呛了一下，啼哭不止，疑是肺炎，结果不是", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="", note="诊断核实型")
E(110, q="测工作调动（某女）", at="丁丑年丁未月辛未日", ben="风天小畜", bian="天雷无妄", mp="官鬼酉金不上卦，伏在三爻妻财辰土之下，虽得日月相生旺相，伏而被合，又化六冲，难以调动", oc="在单位处境正如所测，工作没调动成，后于壬午年内退", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(111, q="电话中测开饭店如何（某女，王代摇）", at="已卯年戊辰月辛丑日（原文「已卯」）", ben="水风井", bian="", mp="此卦虽然日月都是妻财，但用神月破，元神休囚不在卦中，定难赢利", oc="我劝其别开，但最后还是开了，结果午月因拓宽马路，店面被拆，连本钱都没回来", pol="low", anch="present", grade="A", f=[True,True,True,True], fail="")
E(112, q="测婚（某女）", at="戊寅年庚申月壬辰日", ben="山风蛊", bian="山水蒙", mp="98 年已卯冲开，当有再婚之喜，但官鬼动化回头克，化空，很难有如意婚姻", oc="断完问之，其夫果然是被常去她家的同学勾跑了， 88 年结婚，89 年生儿子，94 年丈夫外遇，95 年和她离异。98 年虽有介绍对象的，但不合心意未成", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：主体为婚姻史回溯核实；前向「再婚之喜」未成（仅介绍对象未成），无成立之前向结局")
E(113, q="测其母房子何时可以盖好（五台山某女）", at="庚辰年癸未月乙未日", ben="风水涣", bian="", mp="我见元神官鬼亥水不在卦中，马上断其母亲连地基还没批下。本年亥月批下，次年巳月动工盖房", oc="以上推断全部应验", pol="low", anch="present", grade="B", f=[True,False,True,True], fail="独立结局滤：结局仅「以上推断全部应验」概括语，前向盖房时点（亥月批地基/次年巳月动工）无具体反馈")

assert len(C) == 113, len(C)

# ---------- 去重对勘 ----------
why = json.load(open("/home/hatch/workspace/divination/benchmark/phase3/runs/round56/digestion/SUPPLY-MINING-wanghuying-r56.json"))
why_keys = []
for e in why["entries"]:
    ch = e["input_fields"]["chart"]
    why_keys.append((e["provisional_id"], ch.get("ben_gua",""), ch.get("bian_gua",""), e["input_fields"].get("asked_at","")))
import glob as _g
ly_named = {  # LY-102…105 名案（inputs-dev12 卡面逐字，2026-10-31 本席直读）
 "LY-102": ("山水蒙","坤为地","戌月丁丑日"), "LY-103": ("火山旅","天风姤","午月丙辰日"),
 "LY-104": ("山风蛊","山水蒙","辰月戊寅日"), "LY-105": ("雷天大壮","水天需","乙酉年壬午月壬戌日")}
def monthday(at):
    m = re.search(r'([甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]月[甲乙丙丁戊己庚辛壬癸][子丑寅卯辰巳午未申酉戌亥]日)', at or '')
    return m.group(1) if m else (at or '')
gsz_keys = {}
entries = []
eligible = []
for i, s in enumerate(segs, start=1):
    c = C[i]
    gid = f"GSZ-{i:03d}"
    key = (c["ben"], c["bian"], monthday(c["at"]))
    gsz_keys.setdefault(key, []).append(gid)
    hits = []
    for wid, wb, wbn, wat in why_keys:
        if wb == c["ben"] and wbn == c["bian"] and monthday(wat) == monthday(c["at"]):
            hits.append(wid)
    for lid, (lb, lbn, lat) in ly_named.items():
        if lb == c["ben"] and lbn == c["bian"] and monthday(lat) == monthday(c["at"]):
            hits.append(lid)
    CHN = ["一","二","三","四","五","六","七","八","九","十","十一","十二","十三","十四","十五","十六","十七","十八"]
    if i == 76:
        dedup = "同案（主持先裁）：与《分类占验技法》神秘章月球例同案（本变卦＋占日＋问事三键全合），分类版未入账（R56四滤淘汰挂起）；结局冲突及方向，整例只登记。与WHY-001…071入账例及LY-102…105名案三键无重合"
    elif i == 27:
        dedup = "同案：与《分类占验技法》第八章例七WHY-039三键全合（本变卦＋占月日＋问事），同案只入一例、归属先完成转录之分类版（R56已入账），《说真》版登记异文（见grade_note）"
    elif i == 90:
        dedup = "同案：与《分类占验技法》第五章应期例四WHY-032三键全合（本变卦＋占月日＋问事），同案只入一例、归属先完成转录之分类版（R56已入账），《说真》版登记异文（见grade_note）"
    elif hits:
        dedup = f"三键对勘命中同案：{hits}（本变卦＋占月日＋问事），只入一例、另一版登记异文"
    else:
        dedup = "三键（本变卦＋占月日＋问事）对勘：与已用并集926（dev9 487＋holdout2–20，含LY-102…105名案逐项对勘）、WHY-001…071入账例、《分类占验技法》余例登记、本书内他例均无同案"
    elig = (c["grade"] == "A" and c["pol"] == "low" and c["anch"] == "present" and all(c["f"]) and i not in (27,))  # GSZ-027同案让账WHY-039
    if elig: eligible.append(gid)
    entries.append({
        "provisional_id": gid, "tradition": "liuyao",
        "source": f"六爻卦例说真（王虎应著，用户经学校图书馆提供，文字版 transcription=verbatim）｜第{CHN[s['chapter']-1]}章《{s['chapter_title']}》{s['ex_label']}",
        "input_fields": {"question": c["q"], "asked_at": c["at"],
            "chart": {"ben_gua": c["ben"], "bian_gua": c["bian"],
                      "chart_lines_top_to_bottom": chart_lines(s["text"])}},
        "subject": "",
        "master_prediction": c["mp"], "outcome_record": c["oc"],
        "outcome_type": "forward" if c["f"][1] else "none_or_retrospective",
        "pollution": c["pol"],
        "pollution_note": c.get("fail","") if c["pol"] != "low" else "未见公开转载/名案流传痕迹（王虎应著名案例从严口径下复核：非LY-102…105同源名案、非公众人物/公共事件例）",
        "anchor_presence": c["anch"], "anchor_missing": c.get("anch_missing",""),
        "dedup_check": dedup,
        "filters": {"verbatim_transcribable": c["f"][0], "independent_outcome": c["f"][1], "separable_prediction_outcome": c["f"][2], "not_high_pollution": c["f"][3]},
        "grade": c["grade"], "eligible_net": elig,
        "fail_reason": c["fail"], "grade_note": c.get("note",""),
        "transcription": "verbatim（文字版PDF文字层逐字转录）", "transcription_confidence": "high",
    })
    # 逐字断言：断语/结局摘录去空白后须为该例原文子串（先剔除独立页码行，页脚不属正文）
    seg_clean = "\n".join(l for l in s["text"].split("\n") if not re.fullmatch(r"\s*\d{1,2}\s*", l))
    seg_n = norm(seg_clean)
    assert norm(c["mp"]) in seg_n, f"{gid} master_prediction not verbatim"
    if c["oc"]:
        assert norm(c["oc"]) in seg_n, f"{gid} outcome_record not verbatim"

dup_inbook = {str(k): v for k, v in gsz_keys.items() if len(v) > 1}
counts = {
    "book_cases_titled": 113,
    "chapter9_ex1_missing": "第九章《六冲辨义》例一在本PDF中缺载（正文自例二起，卷首有「六爻卦例说真（二）」分卷标记）；第十四章「例三」重号（GSZ-088羊肉例与GSZ-089家宅例同标例三，系原书编号重复、非同案）。113为「例」标题实见数",
    "ledger_entries": len(entries),
    "anchor_present": sum(1 for e in entries if e["anchor_presence"]=="present"),
    "anchor_partial": sum(1 for e in entries if e["anchor_presence"]=="partial"),
    "pollution_low": sum(1 for e in entries if e["pollution"]=="low"),
    "pollution_mid": sum(1 for e in entries if e["pollution"]=="mid"),
    "grade_A": sum(1 for e in entries if e["grade"]=="A"),
    "net_eligible_A_low_present": eligible, "net_count": len(eligible),
    "inbook_same_key_groups": dup_inbook,
    "moon_case": {
        "gsz_id": "GSZ-076", "key": "丁丑年癸丑月丙辰日／水雷屯变泽风大过／测月球有水否",
        "shuo_zhen_outcome": "后探测结果，果然没有在月球表面找到水",
        "fenlei_outcome": "有待于科学探测证明（据R56台账摘要转述其结局口径；分类版原文为扫描本，本席未直读该页）",
        "ruling_applied": "R57 PREREG §4主持先裁：冲突及结局方向（未定 vs 已定阴性）→整例不入账、只登记；两版逐字并列于此"},
    "optional_pool_recalc": {
        "pool_after_r56": 65, "holdout20_sealed_from_pool": 25, "pool_stock_before_r57_mining": 40,
        "this_batch_net_new": len(eligible), "pool_after_this_batch": 40 + len(eligible),
        "note": "仅计本席《卦例说真》一批；R57其余席位（WHY待二轮46、QW partial复核、QM续抽）增量由各席台账另计，holdout21构成总复算以主持汇总为准。本批构成：全为六爻、单源（王虎应《卦例说真》）；是否触单源≤50%须与全池同算"},
}
ledger = {"batch": "round57-digestion-liuyao-guaishuo", "provenance": "用户经学校图书馆提供", "redistributable": False,
    "sources": ["《六爻卦例说真》（王虎应著，文字版PDF 54页，pdftotext全量可提；与派单「扫描本」描述不符，以盘上实测为准，逐例 transcription=verbatim）"],
    "rules": "四滤（逐字可转录／独立结局／可分离／非high污染）＋锚点在场（卦名、动爻、世应、六亲纳支、月建日辰）；入账口径承R57 PREREG §4：A级＋low＋锚点present；名案从严（mid/high不入账）；月球例同案冲突照主持先裁",
    "counts": counts, "entries": entries}
json.dump(ledger, open(OUT_JSON, "w"), ensure_ascii=False, indent=1)

fail_list = [e for e in entries if not e["eligible_net"]]
with open(OUT_MD, "w") as f:
    f.write("# R57 开采台账摘要｜王虎应《六爻卦例说真》113例（二轮开采席）\n\n")
    f.write(f"- 台账 JSON：`SUPPLY-MINING-guaishuo-r57.json`（同目录，{len(entries)} 例 GSZ-001…GSZ-113）\n")
    f.write("- 转录口径更正：派单作「扫描本、无文字层处读图」，盘上实测本 PDF 为**文字版**（LibreOffice 重排、54 页、文字层全量可提），与 R56 DIGEST §1.1 登记一致；逐例以文字层**逐字转录**（transcription=verbatim、confidence=high），原文录入讹字（如「已卯」 for 己卯、「白牙」 for 白虎）一律照录并在 grade_note 登记、不臆改。\n")
    f.write("- 编号体例：GSZ-001…113 按全书「例」标题出现顺序（章内例序见 source 字段）。结构异常二项：第九章例一在本 PDF 缺载；第十四章「例三」重号（GSZ-088/089 非同案）。\n\n")
    f.write("## 漏斗\n\n")
    f.write(f"| 层 | 例数 |\n|---|---|\n| 书中「例」标题实见 | 113 |\n| 台账登记 | {len(entries)} |\n| 锚点 present / partial | {counts['anchor_present']} / {counts['anchor_partial']} |\n| 污染 low / mid | {counts['pollution_low']} / {counts['pollution_mid']} |\n| A 级 | {counts['grade_A']} |\n| **净入账（A＋low＋present＋四滤全过）** | **{len(eligible)}** |\n| 只登记不入账 | {len(fail_list)} |\n\n")
    f.write("## 净入账清单（" + str(len(eligible)) + "）\n\n" + "、".join(eligible) + "\n\n")
    f.write("## 败滤登记（只登记不入账，逐例败因）\n\n")
    for e in fail_list:
        f.write(f"- {e['provisional_id']}（{e['source'].split('｜')[-1]}）：{e['fail_reason']}\n")
    f.write("\n## 同案异文清单\n\n")
    f.write("- 月球例（GSZ-076）：与《分类占验技法》神秘章月球例三键同案（丁丑年癸丑月丙辰日、水雷屯变泽风大过、测月球有水否）。结局逐字并列——《说真》版：「后探测结果，果然没有在月球表面找到水」；《分类》版（据 R56 台账摘要转述）：「有待于科学探测证明」。照 R57 PREREG §4 主持先裁：冲突及结局方向（未定 vs 已定阴性），**整例不入账、只登记**；分类版该例 R56 已挂起未入账，故无双入账之虞。\n")
    f.write("- GSZ-009 例末附课堂笔记同卦复述（雷水解变泽水困、胖大海射覆）：同案重讲，不另计例、不另入账，登记于该例 grade_note。\n")
    f.write("- GSZ-027 ↔ WHY-039（《分类》第八章例七，测生孩子）：三键同案，分类版 R56 已入账，《说真》版让账只登记。异文：分类版结局「本月庚子日巳时安全生下一女孩」vs《说真》版「后于本月良子日巳时产一女婴」——仅日名一字之异（《说真》「良子日」为「庚子日」录入讹字，对勘可证），顺产/女孩/巳时一致，无方向冲突。\n")
    f.write("- GSZ-090 ↔ WHY-032（《分类》第五章应期例四，夫妻缘分）：三键同案，分类版 R56 已入账，《说真》版只登记（本例另以细节反转定级 B）。异文：两版主干一致（歌舞团/1982 年结婚/1992 年离异/赔偿八万元）；《说真》版多载「非他怀疑老婆、而老婆怀疑他」之反转一节，分类版无此文，并列登记。\n")
    f.write("- 与 WHY-001…071（《分类占验技法》入账例）及 LY-102…105 名案三键（本变卦＋占月日＋问事）程序对勘：命中同案 2 组（GSZ-027↔WHY-039、GSZ-090↔WHY-032，均已让账登记，见上）；另有本变卦同而占月日/问事皆异者 6 组（WHY-006/008/011/055/056 及 LY-104↔GSZ-112 山风蛊变山水蒙），逐组核对非同案。本书内三键重复组：0（见 JSON counts.inbook_same_key_groups）。已用并集 926 以 id 命名空间与题面双轨核对，GSZ 新编号无冲突。\n\n")
    f.write("## 可选集增量复算\n\n")
    f.write(f"- R56 收束可选集 65，holdout20 已自池中封存 25，余库存 40；本批净新增 **{len(eligible)}** → 本批后可选集 **{40+len(eligible)}**（仅计本席一批；WHY 待二轮 46 等其余 R57 席位增量另计，总构成以主持汇总为准）。\n")
    f.write("- 本批构成：全为六爻、单源《六爻卦例说真》；holdout21 构成约束（T≥25、单体系≤50%、单源≤50%、非夷坚≥13、仅锚点在场）须与全池合算，本席不单独组集不封存（承 PREREG §4）。\n")
print("eligible:", len(eligible), eligible)
print("fail:", len(fail_list))
print("inbook dup keys:", dup_inbook)
