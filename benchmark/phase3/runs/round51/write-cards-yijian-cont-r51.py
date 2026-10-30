#!/usr/bin/env python3
# R51 数据席写卡脚本 · 《夷坚志》余面续检（YJ4-001…011）
# 逐卡 passage/断语/结局均逐字取自本地 work-yijian-r50/yijian-text-lines.txt 对应行（R50 落盘件）。
# 断言：计数=11 对；JSON 可解析；输入侧字段白名单恰 9 键；输入侧断语/结局关键词组零命中；
# passage 为条内连续原文切片且断语/结局逐字含于 passage。
import json, os, re, sys

BASE = os.path.expanduser("~/workspace/divination")
SRC = BASE + "/benchmark/phase3/runs/round50/digestion/work-yijian-r50/yijian-text-lines.txt"
OUT = BASE + "/benchmark/phase3/runs/round51/digestion/cards-mining-yijian-r51"
URL = "https://www.hugbear.net/hugbear/viewinfobook555.html"
LIC = "古典文本公有领域；在线转录站条款未明，内部研究用"
WL = {"id", "tradition", "subject", "context", "question", "setting", "provenance", "redistributable", "license_status"}

raw = open(SRC, encoding="utf-8", errors="replace").read().splitlines()
def content(i):
    l = raw[i - 1]
    m = re.match(r"^\d+\t(.*)$", l)
    return m.group(1) if m else l.strip()

# 条目边界：题行集合（复用 R51 初筛解析 /tmp/entries2.json 的 fl_title）+ 卷标头行
entries = json.load(open("/tmp/entries2.json", encoding="utf-8"))
starts = sorted(e["fl_title"] for e in entries)
hdrs = [i for i in range(132, 2482) if re.match(r"^夷坚[甲乙丙丁]志卷第.*事$", content(i).strip())]
bounds = sorted(set(starts + hdrs + [2482]))
def full_body(fl):
    nxt = min(b for b in bounds if b > fl)
    return "".join(content(i) for i in range(fl + 1, nxt)), nxt - 1

def prov(chunk_vol, title, fl, fend, with_trans):
    vol = re.search(r"卷.+", chunk_vol).group(0)
    s = (f"《夷坚志》·{chunk_vol}·{title}（hugbear 页内标头位次为{vol} chunk）；"
         f"在线全文实取 hugbear 全文单页，本地文本行 L{fl}–{fend}"
         f"（benchmark/phase3/runs/round50/digestion/work-yijian-r50/yijian-text-lines.txt） {URL}；"
         f"访问日期 2026-10-30（R50 实取落盘），R51 于 2026-10-31 回读本地落盘件逐字核")
    if with_trans:
        s += "；transcription=online-verbatim"
    return s

CARDS = []
def add(**kw):
    CARDS.append(kw)

WANG = ("丙志卷十七", "王铁面", 1787)
WANGP = prov("丙志卷十七", "王铁面", 1787, 1788, False)
WANGG = prov("丙志卷十七", "王铁面", 1787, 1788, True)
WANGBODY, _ = full_body(1787)

add(id="YJ4-001", tradition="xiangshu", fl=1787,
    subject="周元特，权兵部侍郎；相者王廷（三衢人，善相人，不妄许与，士大夫目为王铁面）",
    context="干道三年王廷至临安。周元特欲求去，邀王廷至局中相见，同席有户部郎中莫子蒙、金部郎中何希深。",
    question="周元特去留与迁转如何？",
    setting="南宋干道三年·临安；相术（相人）",
    provenance=WANGP, gold_provenance=WANGG,
    notes="本卡自《王铁面》整条剥离周元特一案（同条局中段三案并载：周元特、莫子蒙、何希深同段受相、结局同段并记，三卡 passage 同段、断语与结局各取本案句）。R50 曾将本条以「法术叙事」首段判读带过，本轮全文精读复核为相术连载，详见 MINING-yijian-cont-r51.md §2 C-1。",
    master="王廷", source="《夷坚志》·丙志卷十七·王铁面（hugbear 页内标头位次为卷十七 chunk）",
    statement="冬季当迁。异时典州未晚也。",
    outcome="元特以十一月拜吏部。又二年乃为太平州。皆如其言。",
    p_start="周元特权兵部侍郎", p_end="皆如其言。",
    grade_reason="断语具名（王廷）可逐字录，含迁转时窗（冬季）与后典州两项断面；结局为独立事件文本（十一月拜吏部、二年后为太平州），逐项对应；可剥离成卡。",
    contam="2026-10-31 以「王铁面 王廷 相人 周元特 冬季当迁 夷坚志」检索零个案命中（返回全为明代同号异人页与无关页）；王廷、周元特均无独立条目。",
    forbid=["冬季当迁", "拜吏部", "太平州", "典州"])

add(id="YJ4-002", tradition="xiangshu", fl=1787,
    subject="莫子蒙，户部郎中；相者王廷（王铁面）",
    context="干道三年，周元特邀王廷至局中相见，莫子蒙适在坐，请王廷相。",
    question="莫子蒙迁转如何？",
    setting="南宋干道三年·临安；相术（相人）",
    provenance=WANGP, gold_provenance=WANGG,
    notes="本卡自《王铁面》整条剥离莫子蒙一案（同段并载说明同 YJ4-001）。断语「更一月」与结局除职在八月之时距出入照原文逐字，金标不粉饰。",
    master="王廷", source="《夷坚志》·丙志卷十七·王铁面（hugbear 页内标头位次为卷十七 chunk）",
    statement="更一月、莫郎中当带职帅边。",
    outcome="子蒙以八月除直徽猷阁帅淮东。",
    p_start="周元特权兵部侍郎", p_end="皆如其言。",
    grade_reason="断语具名可逐字录，含带职、帅边两项具体断面；结局为独立事件文本（八月除直徽猷阁帅淮东，带职与帅边逐项对应）；时距「更一月」与八月之出入照实入卡（承 YJ3-005 出入照录先例）；可剥离成卡。",
    contam="2026-10-31 以「王廷 王铁面 莫子蒙 带职帅边 何希深 福建提刑 夷坚」检索零个案命中（返回全为无关人物页）；莫子蒙无独立条目。",
    forbid=["带职帅边", "徽猷阁", "帅淮东", "更一月"])

add(id="YJ4-003", tradition="xiangshu", fl=1787,
    subject="何希深（何逢原），金部郎中，入蜀十年持使者节、还朝未半年；相者王廷（王铁面）",
    context="干道三年，周元特邀王廷至局中相见，何希深适在坐，请王廷相。",
    question="何希深迁转与休咎如何？",
    setting="南宋干道三年·临安；相术（相人）",
    provenance=WANGP, gold_provenance=WANGG,
    notes="本卡自《王铁面》整条剥离何希深一案（同段并载说明同 YJ4-001）。断语两层：席间明断作监司，复密谓周元特言其明年禄尽，两层并录于 statement_excerpt。",
    master="王廷", source="《夷坚志》·丙志卷十七·王铁面（hugbear 页内标头位次为卷十七 chunk）",
    statement="何郎中当作监司。何公明年禄尽。岂特一去邪。",
    outcome="希深出为福建提刑。次年卒。",
    p_start="周元特权兵部侍郎", p_end="皆如其言。",
    grade_reason="断语具名可逐字录，含作监司与明年禄尽两项断面；结局为独立事件文本（出为福建提刑、次年卒），两断面逐项对应；可剥离成卡。",
    contam="2026-10-31 以「王廷 王铁面 莫子蒙 带职帅边 何希深 福建提刑 夷坚」检索零个案命中（返回全为无关人物页）；何希深无独立条目。",
    forbid=["作监司", "禄尽", "福建提刑", "次年卒"])

add(id="YJ4-004", tradition="xiangshu", fl=1787,
    subject="徐吉卿（徐嚞），侍郎，绍兴三十一年以宫观居衢；相者王廷（王铁面），与吉卿同为衢人",
    context="绍兴三十一年，徐吉卿宫观在衢，王廷见之而相。",
    question="徐吉卿复出之事如何？",
    setting="南宋绍兴三十一年·衢州；相术（相人）",
    provenance=WANGP, gold_provenance=WANGG,
    notes="本卡自《王铁面》整条剥离徐吉卿一案。断语含召用时窗（六十日）与两项验征（骨肉凶讣、登高颠坠），结局逐项载于 passage_full。",
    master="王廷", source="《夷坚志》·丙志卷十七·王铁面（hugbear 页内标头位次为卷十七 chunk）",
    statement="公从今六十日当召用。一月后得五百里外骨肉间凶讣。继有登高颠坠之厄。则吾言应矣。",
    outcome="已而吉卿长女嫁马希言者。卒于临安。吉卿因省先茔。登山而跌。碍树间不至损。会朝廷择使出疆。趣召之。日月皆吻合。",
    p_start="徐吉卿嚞侍郎", p_end="日月皆吻合。",
    grade_reason="断语具名可逐字录，含召用时窗（六十日）与凶讣、颠坠两项验征断面；结局为独立事件文本（长女卒于临安、省茔登山而跌、朝廷趣召），逐项对应；可剥离成卡。",
    contam="2026-10-31 以「徐吉卿 王廷 六十日当召用 登高颠坠 夷坚志」检索零个案命中（返回全为诗词与无关页）；徐吉卿无独立条目。",
    forbid=["六十日", "召用", "凶讣", "颠坠", "登山而跌", "趣召"])

add(id="YJ4-005", tradition="xiangshu", fl=1787,
    subject="毛钦望，镇江通判；相者王廷（王铁面）",
    context="干道三年王廷见洪迈之岁，尝至镇江，见通判毛钦望而相。",
    question="毛钦望仕历终局如何？",
    setting="南宋干道三年·镇江；相术（相人）",
    provenance=WANGP, gold_provenance=WANGG,
    notes="本卡自《王铁面》整条剥离毛钦望一案（镇江段与金山主僧案同段并载，两卡 passage 同段、断语结局各取本案句）。",
    master="王廷", source="《夷坚志》·丙志卷十七·王铁面（hugbear 页内标头位次为卷十七 chunk）",
    statement="君终任造朝。得一虚名郡守。",
    outcome="钦望秩满得全州。不及赴而致仕。",
    p_start="其见予之岁。尝至镇江", p_end="不及赴而致仕。",
    grade_reason="断语具名可逐字录，含终任造朝、得虚名郡守两项断面；结局为独立事件文本（秩满得全州、不及赴而致仕，与「虚名」逐字对应）；可剥离成卡。",
    contam="2026-10-31 以「王铁面 毛钦望 虚名郡守 全州 金山主僧 夷坚」检索零个案命中（返回全为明代同号异人页与无关页）；毛钦望无独立条目。",
    forbid=["虚名郡守", "得全州", "致仕", "造朝"])

add(id="YJ4-006", tradition="xiangshu", fl=1787,
    subject="镇江金山寺主僧（原文未具名，以描述立卡）；相者王廷（王铁面）",
    context="干道三年王廷至镇江，金山寺主僧方入院，王廷见之而相。",
    question="主僧近日行止吉凶如何？",
    setting="南宋干道三年·镇江金山寺；相术（相人）",
    provenance=WANGP, gold_provenance=WANGG,
    notes="本卡自《王铁面》整条剥离金山主僧一案（镇江段同段并载说明同 YJ4-005）。对象原文未具名，以描述立卡（承 YJ3-004、YJ2-012 先例）。断语两层：即日游行二百里，及行前复决「至彼且复来、来之日有小惊恼然不关身」，并录于 statement_excerpt。",
    master="王廷", source="《夷坚志》·丙志卷十七·王铁面（hugbear 页内标头位次为卷十七 chunk）",
    statement="即日游行二百里。至彼且复来。来之日有小惊恼。然不关身也。",
    outcome="甫二日。方务德自建康遣信招之。遂行。求决于廷。廷曰、至彼且复来。来之日有小惊恼。然不关身也。及归。方弛担。而西津火。寺之僦舍十余家焚焉。",
    p_start="其见予之岁。尝至镇江", p_end="不及赴而致仕。",
    grade_reason="断语具名可逐字录，含行程（二百里）、往返与归途小惊恼不关身三项断面；结局为独立事件文本（方务德遣信招行、归时西津火焚僦舍十余家而人无恙），逐项对应；可剥离成卡。",
    contam="2026-10-31 以「王铁面 毛钦望 虚名郡守 全州 金山主僧 夷坚」检索零个案命中（返回全为无关页）；主僧无名、无独立条目。",
    forbid=["二百里", "惊恼", "不关身", "西津火", "僦舍"])

add(id="YJ4-007", tradition="xiangshu", fl=1787,
    subject="王浚明之妻宋氏；相者王廷（王铁面），王浚明过姑苏时见廷请相",
    context="王廷过姑苏见王浚明，王浚明请相，妻宋氏窥于屏间闻之。",
    question="王浚明伉俪安危如何？",
    setting="南宋·姑苏；相术（相人）",
    provenance=WANGP, gold_provenance=WANGG,
    notes="本卡自《王铁面》整条剥离王浚明妻一案。原文「见王浚明□曰」有一转录缺字方框，在王浚明答语处、非断语与结局核心句，passage_full 照录。结局句首「果」为叙事衔接、其下腹痛卧疾而亡为具体事件，非确认式零内容。",
    master="王廷", source="《夷坚志》·丙志卷十七·王铁面（hugbear 页内标头位次为卷十七 chunk）",
    statement="将罹伉俪之戚。自此贤合虽小疾。亦宜善为之防。",
    outcome="未几、果以腹痛卧疾。讫不起。",
    p_start="又过姑苏。见王浚明", p_end="讫不起。",
    grade_reason="断语具名可逐字录，含伉俪之戚与妻小疾宜防两项断面；结局为独立事件文本（妻宋氏未几以腹痛卧疾而亡），对应明确；可剥离成卡。",
    contam="2026-10-31 以「王浚明 王廷 伉俪之戚 贤合 小疾 夷坚志」检索零个案命中（返回全为同名异人页与无关页）；王浚明无独立条目。",
    forbid=["伉俪之戚", "贤合", "腹痛", "讫不起"])

YEYI_P = prov("丙志卷五", "叶议秀才", 1428, 1429, False)
YEYI_G = prov("丙志卷五", "叶议秀才", 1428, 1429, True)
add(id="YJ4-008", tradition="xiangshu", fl=1428,
    subject="叶议，处州青田秀才，家贫母老，侨寄萧山尉家；相者三衢柴生，能相手纹、谈祸福",
    context="绍兴二年，叶议相依潘绂、闾丘观二尉，日饭尉家、夜寝僧舍；柴生至，视叶议手纹而相。",
    question="叶议近时祸福如何？",
    setting="南宋绍兴二年·萧山；相术（相手纹）",
    provenance=YEYI_P, gold_provenance=YEYI_G,
    notes="本卡自《叶议秀才》整条剥离柴生相手纹一案。条内后段女巫通鬼、盗自言见鬼诸段为死后附带叙事，不属断语与结局核心，未入 passage_full（passage 迄叶议被杀句止），如实登记。",
    master="柴生", source="《夷坚志》·丙志卷五·叶议秀才（hugbear 页内标头位次为卷五 chunk）",
    statement="君色殊不佳。法当杀人。否则为人所杀。近三日事尔。切勿妄出。",
    outcome="越三日薄暮。二尉留与饮。中夕醉归。同室僧已寝。一盗在外。尾其后以入。发箧有声。僧觉之。潜起。将取杖击盗。正与盗遇。盗以刃伤僧。僧绝叫而走。叶熟睡。闻呼声。蹶然起。盗适当前。叶急持其袂。盗虑不得脱。掣其肘曰。放我。不然。将杀汝。叶醉甚。持之愈急。盗恐众至。乃剚刃而去。叶即死。",
    p_start="时三衢柴生", p_end="叶即死。",
    grade_reason="断语具名（柴生，能相手纹）可逐字录，含杀人/为人所杀二择断面与三日时窗；结局为独立事件文本（越三日夜盗入、叶持盗袂被剚刃而死），二择后项与时窗逐项对应；可剥离成卡。",
    contam="2026-10-31 以「叶议秀才 柴生 相手纹 法当杀人 三日 夷坚志」检索零个案命中（返回全为现代新闻噪声）；叶议、柴生均无独立条目。",
    forbid=["法当杀人", "为人所杀", "三日事", "剚刃", "叶即死"])

MAO_P = prov("丁志卷六", "和州毛人", 2042, 2043, False)
MAO_G = prov("丁志卷六", "和州毛人", 2042, 2043, True)
MAO_NOTE = "占者毛人兄弟原文无姓名，以条题「和州毛人」为标识（遍体长黑毛、皆善相术、尝召赴京师），(i) 具名性弱于具姓名者，本席以条目主角具位判过并在此明示，留主持复核。"
add(id="YJ4-009", tradition="xiangshu", fl=2042,
    subject="黄达如，和州通判；相者为和州毛人兄弟（遍体长黑毛，皆善相术，尝召赴京师）",
    context="宣和中，黄达如邀毛人兄弟问相，大毛人相之。",
    question="黄达如官位所至与子嗣如何？",
    setting="北宋宣和中·和州；相术（相人）",
    provenance=MAO_P, gold_provenance=MAO_G,
    notes="本卡自《和州毛人》整条剥离黄达如主案（同条子女寿数案另立 YJ4-010，两卡 passage 同段）。" + MAO_NOTE,
    master="和州毛人（大毛人）", source="《夷坚志》·丁志卷六·和州毛人（hugbear 页内标头位次为卷六 chunk）",
    statement="可至大夫与州。生六子。其半得官。",
    outcome="是后二十余年。黄仕历御史郎。官至朝请大夫。知徽州而卒。六子。三入官。",
    p_start="通判黄达如邀问相", p_end="恰二十七岁。",
    grade_reason="断语可逐字录，含官至大夫与州、生六子半入官三项具体断面；结局为独立事件文本（二十余年后官至朝请大夫知徽州、六子三入官），逐项对应；可剥离成卡。",
    contam="2026-10-31 以「和州毛人 相术 黄达如 六子 钱数 寿 夷坚志」检索零个案命中（返回全为术数通书与无关页）；黄达如、毛人均无独立条目。",
    forbid=["大夫与州", "六子", "得官", "朝请大夫", "知徽州", "三入官"])

add(id="YJ4-010", tradition="xiangshu", fl=2042,
    subject="黄达如之长子、长女、次女；相者为和州毛人兄弟",
    context="宣和中，黄达如邀毛人问相毕，呼子女出见，逐一问寿，毛人以钱数报寿。",
    question="黄氏子女寿数如何？",
    setting="北宋宣和中·和州；相术（相人）",
    provenance=MAO_P, gold_provenance=MAO_G,
    notes="本卡自《和州毛人》整条剥离子女寿数一案（与 YJ4-009 同条异问，三键不撞）。断语中长子是否有官一问毛人摇首示意、无文字断语，未入断面；本卡断面只取三人寿钱数。长女封邑一问毛人不对、亦未入断面。" + MAO_NOTE,
    master="和州毛人（大毛人）", source="《夷坚志》·丁志卷六·和州毛人（hugbear 页内标头位次为卷六 chunk）",
    statement="黄呼长子出见。问有官否。摇其首。问寿几何。曰。将钱来。数至四十四钱。顾其弟曰。是么。弟曰。是。即与之。又相长女。问有封邑否。不对。问寿得五十三钱。相次女得二十七钱。",
    outcome="长子长女享年。如所得钱之数。次女以绍兴甲子岁。从其夫祝生赴衡山尉。溺死于江。恰二十七岁。",
    p_start="通判黄达如邀问相", p_end="恰二十七岁。",
    grade_reason="断语可逐字录，含长子四十四、长女五十三、次女二十七三项寿数断面（以钱数报寿为原文占式）；结局为独立事件文本（长子长女享年如钱数、次女二十七岁溺死于江），逐项对应；可剥离成卡。",
    contam="2026-10-31 以「和州毛人 相术 黄达如 六子 钱数 寿 夷坚志」检索零个案命中（返回全为术数通书与无关页）；黄氏子女均无独立条目。",
    forbid=["四十四", "五十三", "二十七", "享年", "溺死"])

YE_P = prov("丁志卷六", "叶德孚", 2060, 2061, False)
YE_G = prov("丁志卷六", "叶德孚", 2060, 2061, True)
add(id="YJ4-011", tradition="ming", fl=2060,
    subject="叶德孚，建安人，得将仕郎、参选；占者蜀人韩慥，以问命为业",
    context="绍兴八年叶德孚获乡荐、结婚宗室，得将仕郎；明年参选，以七月二日谒韩慥问命。",
    question="叶德孚前程如何？",
    setting="南宋绍兴九年七月；禄命（问命）",
    provenance=YE_P, gold_provenance=YE_G,
    notes="本卡自《叶德孚》整条剥离韩慥问命一案。占者韩慥与 R50 只登记《汤史二相》条为同一人（彼条对象为著名宰相判 high 只登记），本案对象叶德孚冷僻，三键（占者＋对象＋所问）不撞。断语两层：初谒言前程俟过立秋别论，复诣明言过不得立秋；statement_excerpt 取复诣决断层，初谒层并载于 passage_full。输入侧背景止于初谒问命，叶氏家世叙事中涉祖母者为条首背景、与断语结局无涉，未入输入卡以免冗载。",
    master="韩慥", source="《夷坚志》·丁志卷六·叶德孚（hugbear 页内标头位次为卷六 chunk）",
    statement="记得此月初曾看前一命。但过不得立秋。此日不死。吾不谈命。",
    outcome="竟以立秋日死。",
    p_start="明年参选。以七月二日。谒蜀人韩慥问命", p_end="竟以立秋日死。",
    grade_reason="断语具名（韩慥）可逐字录，含死期时点（过不得立秋）之决断断面；结局为独立事件文本（竟以立秋日死），时点逐字对应；可剥离成卡。",
    contam="2026-10-31 以「韩慥 叶德孚 立秋 问命 夷坚志」检索零个案命中（返回全为同名异人页与无关页）；叶德孚无独立条目。",
    forbid=["立秋", "不谈命", "过不得", "呕血"])

os.makedirs(OUT, exist_ok=True)
assert len(CARDS) == 11, len(CARDS)
bodies = {}
for c in CARDS:
    body, _ = full_body(c["fl"])
    bodies[c["id"]] = body
    i0 = body.index(c["p_start"]); i1 = body.index(c["p_end"]) + len(c["p_end"])
    passage = body[i0:i1]
    assert c["statement"].replace("。", "。") is not None
    # 断语核心分句与结局须逐字含于 passage（statement 为多句拼接时逐句验）
    for seg in [s for s in re.split(r"(?<=。)", c["statement"]) if s]:
        assert seg in passage, (c["id"], seg)
    assert c["outcome"] in passage, (c["id"], "outcome")
    inp = {"id": c["id"], "tradition": c["tradition"], "subject": c["subject"],
           "context": c["context"], "question": c["question"], "setting": c["setting"],
           "provenance": c["provenance"], "redistributable": False, "license_status": LIC}
    assert set(inp.keys()) == WL, (c["id"], set(inp.keys()))
    blob = json.dumps(inp, ensure_ascii=False)
    for f in c["forbid"]:
        assert f not in blob, (c["id"], f)
    gold = dict(inp)
    gold["provenance"] = c["gold_provenance"]
    gold["record_status"] = "candidate-r51-mining"
    gold["notes"] = c["notes"]
    gold["transcription"] = "online-verbatim"
    gold["master_predictions"] = [{"master": c["master"], "date": None, "tradition": c["tradition"],
        "direction": None, "key_assertions": [], "source": c["source"], "statement_excerpt": c["statement"]}]
    gold["outcome"] = {"description": c["outcome"], "verified_by": "原文结局文本（逐字）"}
    gold["passage_full"] = passage
    gold["grade_suggestion"] = "A"
    gold["grade_reason"] = c["grade_reason"]
    gold["contamination_suggestion"] = "low"
    gold["contamination_reason"] = c["contam"]
    for name, obj in [(f"{c['id']}-input.json", inp), (f"{c['id']}-gold.json", gold)]:
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
    print(c["id"], "passage_len", len(passage), "OK")
# 复验：盘上 JSON 全可解析 + 输入白名单
n = 0
for fn in sorted(os.listdir(OUT)):
    if fn.endswith(".json"):
        json.load(open(os.path.join(OUT, fn), encoding="utf-8")); n += 1
        if fn.endswith("-input.json"):
            d = json.load(open(os.path.join(OUT, fn), encoding="utf-8"))
            assert set(d.keys()) == WL, fn
print("files parsed:", n, "== 22 expected")
assert n == 22
print("ALL ASSERTIONS PASSED")
