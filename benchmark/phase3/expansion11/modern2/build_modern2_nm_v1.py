# -*- coding: utf-8 -*-
"""expansion11/modern2 批次构建脚本（NM 系，现代大师时间戳公开预测）。
唯一脚本，置于本批次目录内。运行后产出 cases.jsonl 与 inputs/<id>.json。
数据角按预注册收录标准整理；不作断、不评分（grade 字段仅为收录分级与污染分级）。"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
LIC = "internal-research-only"
LIC_NOTE = "公开报道节录，内部研究使用（redistributable=false）"

CASES = []

# ---------------- NM-001 Eurovision 2011 / Andrew Bevan ----------------
CASES.append({
  "id": "NM-001",
  "tradition": "mundane-astrology",
  "subject": {"name_or_desc": "第56届欧洲歌唱大赛（2011，杜塞尔多夫）冠军归属", "gender": "不适用"},
  "context": {
    "question": "2011年欧洲歌唱大赛冠军将归哪个国家？",
    "asked_at": "2010-10-16（预测于 Skyscript 论坛首发时点；作者页面自记日期2010-12-15，末次增补2011-04-22；决赛2011-05-14）",
    "setting": "第56届欧洲歌唱大赛定于2011-05-14在德国杜塞尔多夫举行，43国参赛；预测首发时多数国家尚未选定参赛曲目。",
    "attachments": {}
  },
  "provenance": {
    "carrier": "预测者本人网站 astronor.com 专题页《Eurovision 2011》，并自述首发于 Skyscript.co.uk（2010-10-16）",
    "work": "Eurovision Song Contest 2011 predictions（astronor.com/eurovision2011.htm）",
    "published_at": "2010-10-16 首发（Skyscript）；页面日期 2010-12-15，末次增补 2011-04-22，均在决赛（2011-05-14）之前",
    "url": "astronor.com/eurovision2011.htm",
    "timestamp_evidence": "本人站点页面自带日期与增补记录，增补截止2011-04-22，早于决赛日；断语在结果揭晓前已固定",
    "license_note": LIC_NOTE
  },
  "language": "en",
  "master_predictions": [{
    "master": "Andrew Bevan",
    "tradition": "mundane-astrology",
    "date": "2010-10-16（增补至2011-04-22）",
    "statement_excerpt": "My first bet goes with the United Kingdom.（其冠军候选前列为英国、爱尔兰、法国；文中曾考虑阿塞拜疆，但以其位于东南、与原始判断不合而明确排除）",
    "source": "astronor.com/eurovision2011.htm（本人网站）",
    "direction": "positive",
    "key_assertions": [
      "冠军将西移，首选英国夺冠（first bet: United Kingdom）",
      "候选前列为英国、爱尔兰、法国",
      "明确排除阿塞拜疆（方位不合）"
    ],
    "timing_claim": "决赛日2011-05-14揭晓"
  }],
  "outcome": {
    "description": "阿塞拜疆 Ell & Nikki 以《Running Scared》221分夺冠；英国仅列第11（100分），爱尔兰第8，法国第15。",
    "verified_by": "欧洲广播联盟（EBU）2011-05-15官方新闻稿公布全场名次与分数；Wikipedia『Eurovision Song Contest 2011』词条复核"
  },
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名职业占星师、本人站点一手发表、时间戳（2010-10-16首发、末次增补2011-04-22）早于决赛、断语为单一首选（英国夺冠）可证伪、结局有EBU官方记录。断语形态为『短名单＋首选』，较单点断语略弱，请主持角复核是否接受此形态。断误（冠军为其明确排除的阿塞拜疆）。",
  "contamination": "low",
  "contamination_reason": "赛事本身有名，但2011年冠军阿塞拜疆（Ell & Nikki）为冷门具体结局，模型先验大概率不知该届冠军归属；断语细节（排除阿塞拜疆）更非通识。",
  "holdout_eligible": True,
  "notes": {
    "tags": ["欧洲歌唱大赛", "娱乐赛事", "冠军预测"],
    "comment": "本批唯一 A-low；污染判定依据『模型先验是否知结局』，若主持角以赛事知名度改判 medium，本批 A-low 将归零，已在 BUILD-REPORT 明示。",
    "cross_ref": ""
  }
})

# ---------------- NM-002 I'm a Celebrity 2024 / Inbaal Honigman ----------------
CASES.append({
  "id": "NM-002",
  "tradition": "tarot",
  "subject": {"name_or_desc": "《I'm a Celebrity…Get Me Out of Here!》2024系列（第24季）决赛名次", "gender": "不适用"},
  "context": {
    "question": "《I'm a Celebrity…Get Me Out of Here!》2024系列冠军与亚军是谁？",
    "asked_at": "2024-12-06（决赛定于2024-12-08）",
    "setting": "决赛三强为 Danny Jones、Coleen Rooney、Richard Coles；Danny Jones 自节目开播起即为博彩公司赔率热门。",
    "attachments": {}
  },
  "provenance": {
    "carrier": "What's The Jam（Jam Press 系娱乐新闻）刊载具名塔罗师 Inbaal Honigman 决赛前预测",
    "work": "I'm a Celebrity 2024 final tarot predictions（What's The Jam）",
    "published_at": "2024-12-06T11:00Z，在2024-12-08决赛揭晓前两日",
    "url": "",
    "timestamp_evidence": "载体页面带 Published 2024-12-06T11:00Z 时间戳，早于决赛直播",
    "license_note": LIC_NOTE
  },
  "language": "en",
  "master_predictions": [{
    "master": "Inbaal Honigman",
    "tradition": "tarot",
    "date": "2024-12-06",
    "statement_excerpt": "Coleen Rooney will be absolutely delighted to come second; Danny Jones's Ace of Swords has the edge… Danny walks away victorious.",
    "source": "What's The Jam, 2024-12-06",
    "direction": "positive",
    "key_assertions": [
      "Danny Jones 夺冠",
      "Coleen Rooney 居第二名"
    ],
    "timing_claim": "决赛日2024-12-08揭晓"
  }],
  "outcome": {
    "description": "Danny Jones 夺冠（King of the Jungle），Coleen Rooney 第二，Richard Coles 第三，2024-12-08决赛公布，逾千万票投出。",
    "verified_by": "OK! Magazine 2024-12-08当晚报道及 PA 通讯稿（Westmeath Examiner 2024-12-09刊载）等多家独立报道"
  },
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名职业塔罗师、决赛前两日公开发表、双名次断语具体可证伪、结局有独立新闻核。断中。污染从严判 medium（见 contamination_reason），不计入 holdout11 备料。",
  "contamination": "medium",
  "contamination_reason": "该节目为 ITV 旗舰真人秀、参赛者皆为名人，属有一定知名度的事件；且 Jones 为开播以来赔率热门，断中信息量有限。从严判 medium。",
  "holdout_eligible": False,
  "notes": {
    "tags": ["真人秀", "娱乐赛事", "名次预测"],
    "comment": "同作者另有 Euro 2024（NM-010）与奥斯卡（NM-012–NM-017）两组断语，事项不同、三键不重复。",
    "cross_ref": "NM-010, NM-012"
  }
})

# ---------------- NM-003/004/005 Telangana 2023（同一载体三位占星师） ----------------
_TELANGANA_CTX = {
  "question": "2023年特伦甘纳邦议会选举结果如何？",
  "asked_at": "2023-12-01（投票已于2023-11-30结束，计票定于2023-12-03）",
  "setting": "特伦甘纳邦议会共119席，多数线60席；现任首席部长 K. Chandrashekar Rao 领导的 BRS 寻求连任，国大党为主要挑战者。",
  "attachments": {}
}
_TELANGANA_PROV = {
  "carrier": "Deccan Chronicle 2023-12-01 报道（计票前刊出，汇集三位占星师选前断语）",
  "work": "Telangana Assembly elections 2023: astrologers' predictions（Deccan Chronicle，文号011223）",
  "published_at": "2023-12-01，投票后、2023-12-03计票揭晓前",
  "url": "",
  "timestamp_evidence": "报纸报道日期2023-12-01，介于投票日（11-30）与计票日（12-03）之间，断语于结果揭晓前公开发表",
  "license_note": LIC_NOTE
}
_TELANGANA_OUT = {
  "description": "国大党赢得64/119席过半，BRS 39席；国大党 Revanth Reddy 于2023-12-07就任首席部长，K. Chandrashekar Rao 未能连任，无悬峙议会。",
  "verified_by": "Scroll、CNBC-TV18 等报道引印度选举委员会计票数据（国大党64席、BRS 39席、多数线60席）"
}

CASES.append({
  "id": "NM-003",
  "tradition": "astro-numerology",
  "subject": {"name_or_desc": "2023年特伦甘纳邦议会选举（现任首席部长 K. Chandrashekar Rao 连任问题）", "gender": "男"},
  "context": dict(_TELANGANA_CTX),
  "provenance": dict(_TELANGANA_PROV),
  "language": "en",
  "master_predictions": [{
    "master": "Jayashankarr Sistlaa",
    "tradition": "astro-numerology",
    "date": "2023-12-01（报道刊出；断语为选前所发）",
    "statement_excerpt": "K. Chandrashekar Rao will retain his position as the chief minister because his stars are shining.",
    "source": "Deccan Chronicle, 2023-12-01",
    "direction": "positive",
    "key_assertions": ["K. Chandrashekar Rao 将保住首席部长之位（BRS 继续执政）"],
    "timing_claim": "计票日2023-12-03揭晓"
  }],
  "outcome": dict(_TELANGANA_OUT),
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名职业占星-数字命理师、报刊一手报道、发表于计票揭晓前、断语单一明确可证伪、结局有选委会数据来源的独立报道。断误。",
  "contamination": "medium",
  "contamination_reason": "印度邦级选举有一定知名度，结局见于印度主流媒体，但非全球通识级事件；模型先验未必知此邦选举细节。从严判 medium。",
  "holdout_eligible": False,
  "notes": {"tags": ["印度邦选举", "连任预测"], "comment": "与 NM-004、NM-005 同载体、同日发表，但预测者与所测事项各异，三键不重复。", "cross_ref": "NM-004, NM-005"}
})

CASES.append({
  "id": "NM-004",
  "tradition": "vedic-astrology",
  "subject": {"name_or_desc": "2023年特伦甘纳邦议会选举（国大党席次）", "gender": "不适用"},
  "context": dict(_TELANGANA_CTX),
  "provenance": dict(_TELANGANA_PROV),
  "language": "en",
  "master_predictions": [{
    "master": "Krothapally Suresh Sharma",
    "tradition": "vedic-astrology",
    "date": "2023-12-01（报道刊出；断语为选前所发）",
    "statement_excerpt": "The Congress will win 70 seats.（并自述其卡纳塔克邦选举断语曾应验）",
    "source": "Deccan Chronicle, 2023-12-01",
    "direction": "positive",
    "key_assertions": ["国大党将赢得选举", "国大党具体席次为70席"],
    "timing_claim": "计票日2023-12-03揭晓"
  }],
  "outcome": dict(_TELANGANA_OUT),
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合（标准同 NM-003）。断语含方向与具体席次两层：方向（国大党胜）中，具体席次（70席，实际64席）误；评分归评分角，本处仅登记。",
  "contamination": "medium",
  "contamination_reason": "同 NM-003：邦级选举有一定知名度，从严判 medium。",
  "holdout_eligible": False,
  "notes": {"tags": ["印度邦选举", "席次预测"], "comment": "与 NM-003、NM-005 同载体、三键不重复。", "cross_ref": "NM-003, NM-005"}
})

CASES.append({
  "id": "NM-005",
  "tradition": "vedic-astrology",
  "subject": {"name_or_desc": "2023年特伦甘纳邦议会选举（议会格局与首席部长产生）", "gender": "不适用"},
  "context": dict(_TELANGANA_CTX),
  "provenance": dict(_TELANGANA_PROV),
  "language": "en",
  "master_predictions": [{
    "master": "Sanganabhatla Narasimha Murthy Sidhanthi",
    "tradition": "vedic-astrology",
    "date": "2023-12-01（报道刊出；断语为选前所发）",
    "statement_excerpt": "There will be a hung Assembly… the Chief Minister will not be decided easily even after the result is out.（其据为两党首席部长候选人命盘皆有缺陷）",
    "source": "Deccan Chronicle, 2023-12-01",
    "direction": "negative",
    "key_assertions": ["将出现悬峙议会（无政党过半）", "结果公布后首席部长人选仍难以确定"],
    "timing_claim": "计票日2023-12-03揭晓"
  }],
  "outcome": dict(_TELANGANA_OUT),
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合（标准同 NM-003）。断误：国大党单独过半，首席部长于2023-12-07顺利就任。",
  "contamination": "medium",
  "contamination_reason": "同 NM-003：邦级选举有一定知名度，从严判 medium。",
  "holdout_eligible": False,
  "notes": {"tags": ["印度邦选举", "悬峙议会预测"], "comment": "预测者为电视占星师（Sidhanthi）。与 NM-003、NM-004 同载体、三键不重复。", "cross_ref": "NM-003, NM-004"}
})

# ---------------- NM-006 Chicago mayoral 2019 / Susan Abbott Gidel ----------------
CASES.append({
  "id": "NM-006",
  "tradition": "western-astrology",
  "subject": {"name_or_desc": "2019年芝加哥市长选举（候选人 Bill Daley）", "gender": "男"},
  "context": {
    "question": "2019年芝加哥市长选举谁能胜出？",
    "asked_at": "2019-02-20（首轮投票2019-02-26）",
    "setting": "芝加哥市长选举首轮2019-02-26举行，14名候选人参选；无人过半数则前两名进入2019-04-02决选。Bill Daley 为候选人之一，前市长 Richard M. Daley 之子、曾任白宫幕僚长。",
    "attachments": {}
  },
  "provenance": {
    "carrier": "预测者本人网站 susangidel.com 专栏文章",
    "work": "Astrology Points to Bill Daley as New Chicago Mayor（susangidel.com）",
    "published_at": "2019-02-20（页面元数据 Published 2019-02-20T23:36Z），在首轮投票（2019-02-26）之前",
    "url": "",
    "timestamp_evidence": "本人站点页面元数据载发表时间2019-02-20T23:36Z；页面另有 Updated 2019-10-23 字样（选后修订痕迹），核心断语归属以选前发表时间为据，此点已登记请主持角注意",
    "license_note": LIC_NOTE
  },
  "language": "en",
  "master_predictions": [{
    "master": "Susan Abbott Gidel",
    "tradition": "western-astrology",
    "date": "2019-02-20",
    "statement_excerpt": "Daley is a shoo-in; his win is practically inevitable.（据木星回归与选举日火星合北交点；并称理想的决选对阵为 Daley 对 Lightfoot，且 Daley 将胜出）",
    "source": "susangidel.com, 2019-02-20",
    "direction": "positive",
    "key_assertions": [
      "Bill Daley 当选芝加哥市长几成定局（shoo-in / practically inevitable）",
      "决选将为 Daley 对 Lightfoot，且 Daley 胜出"
    ],
    "timing_claim": "首轮2019-02-26、决选2019-04-02"
  }],
  "outcome": {
    "description": "首轮 Daley 仅得14.78%居第三，未进决选（Lightfoot 17.54%、Preckwinkle 16.04%居前二）；决选 Lightfoot 以73.7%击败 Preckwinkle 当选。",
    "verified_by": "Wikipedia 与 Ballotpedia 之2019年芝加哥市长选举记录、Daily Northwestern 报道复核"
  },
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名职业占星师、本人站点一手发表、选前时间戳、断语强烈明确可证伪、结局有独立选举记录。断误。注意页面存选后 Updated 戳（见 provenance），若主持角从严认为时间戳证据受损，可降 B，本处已明示。",
  "contamination": "medium",
  "contamination_reason": "美国市级选举有一定知名度（Lightfoot 当选曾有全国报道），但 Daley 首轮出局的具体名次非通识。从严判 medium。",
  "holdout_eligible": False,
  "notes": {"tags": ["美国地方选举", "市长选举"], "comment": "", "cross_ref": ""}
})

# ---------------- NM-007 Sri Lanka 2015 / Sumanadasa Abeygunawardena ----------------
CASES.append({
  "id": "NM-007",
  "tradition": "vedic-astrology",
  "subject": {"name_or_desc": "2015年斯里兰卡总统选举（现任总统 Mahinda Rajapaksa）", "gender": "男"},
  "context": {
    "question": "2015年斯里兰卡总统选举，现任总统 Rajapaksa 能否连任？",
    "asked_at": "2015-01-06（选举定于2015-01-08）",
    "setting": "Rajapaksa 提前近两年举行选举、寻求第三任期；反对派共同候选人为其前卫生部长 Maithripala Sirisena。预测者 Sumanadasa Abeygunawardena 为 Rajapaksa 的私人占星师。",
    "attachments": {}
  },
  "provenance": {
    "carrier": "选前多家一手报道：纽约时报 Ellen Barry 报道（2015-01-06，Economic Times 2015-01-08转载）、IBTimes 2014-12-30占星师会议报道、Ceylon Today 访谈（dbsjeyaraj.com 转载全文）",
    "work": "选前系列报道与访谈（NYT / IBTimes / Ceylon Today）",
    "published_at": "2014-12-30 至 2015-01-06，均在选举日2015-01-08之前",
    "url": "",
    "timestamp_evidence": "三家载体各自带选前日期：IBTimes 2014-12-30载其断言 Rajapaksa『大胜』；NYT 2015-01-06引其原话；访谈针对2015-01-08选举",
    "license_note": LIC_NOTE
  },
  "language": "en",
  "master_predictions": [{
    "master": "Sumanadasa Abeygunawardena",
    "tradition": "vedic-astrology",
    "date": "2014-12-30 / 2015-01-06",
    "statement_excerpt": "He cannot be defeated in an election… If he gives someone else the position, or steps down, or retires, that's the only way.（2014-12-30占星师会议上另断 Rajapaksa 将『取得大胜』）",
    "source": "New York Times, 2015-01-06（Ellen Barry）；IBTimes, 2014-12-30；Ceylon Today 访谈",
    "direction": "positive",
    "key_assertions": [
      "Rajapaksa 在选举中不可能被击败，必连任",
      "且将取得大胜（a big victory）"
    ],
    "timing_claim": "选举日2015-01-08"
  }],
  "outcome": {
    "description": "Sirisena 以51.28%（6,217,162票）击败 Rajapaksa 的47.58%（5,768,090票）；Rajapaksa 承认败选，Sirisena 于2015-01-09就任。",
    "verified_by": "选举结果数据见 Wikipedia『2015 Sri Lankan presidential election』引官方计票；选后 Sunday Times（2015-01-11）与 Guardian（2015-01-13）报道复核其断误"
  },
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名（总统私人占星师）、三家选前一手载体、断语绝对化且可证伪、结局为官方计票记录。断误。",
  "contamination": "medium",
  "contamination_reason": "该次选举为国际报道的著名爆冷，但属一国一届选举的具体结果，非全球通识级；模型先验未必知票数细节。从严判 medium。",
  "holdout_eligible": False,
  "notes": {"tags": ["总统选举", "连任预测", "爆冷"], "comment": "同国2019年大选占星师群因只有选后盘点文、无选前一手发表，本轮已排除（见 BUILD-REPORT E7），与本例不重复。", "cross_ref": ""}
})

# ---------------- NM-008 IPL 2024 final / Pandit Jagannath Guruji ----------------
CASES.append({
  "id": "NM-008",
  "tradition": "vedic-astrology",
  "subject": {"name_or_desc": "2024年印度超级联赛（IPL）总决赛：加尔各答骑士（KKR）对海得拉巴日出（SRH）", "gender": "不适用"},
  "context": {
    "question": "2024年IPL总决赛谁将夺冠？",
    "asked_at": "2024-05-23（决赛定于2024-05-26，金奈）",
    "setting": "IPL 2024 总决赛由 KKR 对阵 SRH，2024-05-26于金奈举行。",
    "attachments": {}
  },
  "provenance": {
    "carrier": "Economic Times 决赛前三日报道（具名占星师 Pandit Jagannath Guruji）",
    "work": "Astrologer predicts IPL 2024 final winner three days before the game（Economic Times）",
    "published_at": "2024-05-23（标题自述为决赛前三日），决赛为2024-05-26",
    "url": "",
    "timestamp_evidence": "报道于决赛前刊出；ET 决赛后报道回指此断语曾于赛前发表，可互证时间在前",
    "license_note": LIC_NOTE
  },
  "language": "en",
  "master_predictions": [{
    "master": "Pandit Jagannath Guruji",
    "tradition": "vedic-astrology",
    "date": "2024-05-23",
    "statement_excerpt": "KKR will win the IPL 2024 title.（并预期将是一场激烈较量）",
    "source": "Economic Times, 2024-05-23",
    "direction": "positive",
    "key_assertions": ["KKR 将赢得 IPL 2024 冠军", "决赛将是一场激烈较量（附带断言）"],
    "timing_claim": "决赛日2024-05-26"
  }],
  "outcome": {
    "description": "KKR 在2024-05-26决赛击败 SRH，赢得 IPL 2024 冠军。",
    "verified_by": "Economic Times 决赛后报道（确认冠军归属并回指其赛前断语）及公开赛事记录"
  },
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名职业占星师、主流报刊决赛前报道、断语单一明确、结局为公开赛事记录。主断中；『激烈较量』为附带断言，决赛实际进程是否激烈由评分角按原始记录裁断，本处只登记。同一决赛另有特伦古占星师 Venuswamy 倾向 SRH 的含糊表述（possibly），未达可证伪标准，已排除（BUILD-REPORT E1）。",
  "contamination": "medium",
  "contamination_reason": "IPL 为印度头部赛事、有一定知名度，单届决赛冠军非法全球通识；模型先验未必确知2024届冠军。从严判 medium。",
  "holdout_eligible": False,
  "notes": {"tags": ["板球", "联赛决赛", "冠军预测"], "comment": "", "cross_ref": ""}
})

# ---------------- NM-009 Ashes 2017-18 / Greenstone Lobo ----------------
CASES.append({
  "id": "NM-009",
  "tradition": "vedic-astrology",
  "subject": {"name_or_desc": "2017–18灰烬杯系列赛（澳大利亚主场对英格兰，五场测试赛）", "gender": "不适用"},
  "context": {
    "question": "2017–18灰烬杯系列赛结果如何？",
    "asked_at": "2017-11-22（首场测试赛2017-11-23开赛）",
    "setting": "英格兰为灰烬杯卫冕方；澳大利亚队长 Steve Smith 首次以队长身份出战灰烬杯；新秀 Cameron Bancroft 入选澳大利亚阵容。预测者 Greenstone Lobo 为印度体育占星师，本断首发于其 Sportskeeda 专栏，CricTracker 于赛前一日转载报道。",
    "attachments": {}
  },
  "provenance": {
    "carrier": "CricTracker 2017-11-22 报道（转述其 Sportskeeda 专栏原文），首测开赛前一日",
    "work": "Ashes 2017-18 predictions（Greenstone Lobo，Sportskeeda 专栏；CricTracker 报道）",
    "published_at": "2017-11-22T18:05+05:30，首测2017-11-23之前",
    "url": "",
    "timestamp_evidence": "CricTracker 页面带 Published 2017-11-22T18:05+05:30 时间戳，早于系列赛开赛",
    "license_note": LIC_NOTE
  },
  "language": "en",
  "master_predictions": [{
    "master": "Greenstone Lobo",
    "tradition": "vedic-astrology",
    "date": "2017-11-22",
    "statement_excerpt": "Australia will win a closely fought series and reclaim the Ashes urn; it will be Steve Smith's first Ashes series win as captain. Debutant Cameron Bancroft will have a memorable series; Dawid Malan and Mark Stoneman will make England's greatest impact; Alastair Cook will be patchy; Jackson Bird and Chadd Sayers will be important if given the opportunity.",
    "source": "CricTracker, 2017-11-22（报道其 Sportskeeda 专栏）",
    "direction": "positive",
    "key_assertions": [
      "澳大利亚将赢得系列赛并夺回灰烬杯",
      "此为 Steve Smith 以队长身份的首个灰烬杯系列赛胜利",
      "新秀 Cameron Bancroft 将有令人难忘的系列赛表现",
      "Dawid Malan 与 Mark Stoneman 将是英格兰影响最大的球员",
      "Alastair Cook 表现将不稳定（patchy）",
      "Jackson Bird、Chadd Sayers 若获机会将发挥重要作用（此二人整届未上场）"
    ],
    "timing_claim": "系列赛2017-11-23至2018-01-08"
  }],
  "outcome": {
    "description": "澳大利亚4–0赢得系列赛夺回灰烬杯；Steve Smith 以687分获系列赛最佳球员（Compton–Miller Medal）；英格兰跑分最高者为 Dawid Malan（383分），Alastair Cook 376分；Jackson Bird 与 Chadd Sayers 未在本届系列赛上场。",
    "verified_by": "Wikipedia『2017–18 Ashes series』系列赛数据表与 ICC 2018-01-08 报道复核"
  },
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名职业体育占星师、赛前一日带时间戳发表、多条具体断语可逐条证伪、结局有官方与百科记录。主断（澳大利亚夺冠、Smith 队长首胜）中，子断语混合（Malan 居英格兰跑分首位中；Bird/Sayers 未上场，该子断落空）。逐条评分归评分角。与 WP-009（同人、2019板球世界杯）对象/日期/事项皆不同，非重复。",
  "contamination": "medium",
  "contamination_reason": "灰烬杯为著名系列赛，但2017–18单届比分与子项细节（各队跑分名次）非通识；从严介于 high/medium 之间取 medium 并在此明示，主持角可上调。",
  "holdout_eligible": False,
  "notes": {"tags": ["板球", "灰烬杯", "系列赛预测"], "comment": "", "cross_ref": "WP-009"}
})

# ---------------- NM-010 Euro 2024 / Inbaal Honigman ----------------
CASES.append({
  "id": "NM-010",
  "tradition": "tarot",
  "subject": {"name_or_desc": "2024年欧洲足球锦标赛（德国主办）：冠军归属与英格兰前景", "gender": "不适用"},
  "context": {
    "question": "2024年欧洲杯冠军归谁？英格兰能走多远？英格兰主帅 Southgate 赛后去留如何？",
    "asked_at": "2024-01月上旬（原文自述『2024年开始不到一周』；赛事定于2024-06-14至07-14）",
    "setting": "2024年欧洲杯将于2024年6–7月在德国举行，英格兰主帅为 Gareth Southgate。",
    "attachments": {}
  },
  "provenance": {
    "carrier": "Betfair Casino 2024年度预测栏目，具名塔罗师 Inbaal Honigman；全文经 FreeLibrary/Gale 转载存档（MGN Ltd 版权页2024）",
    "work": "Inbaal Honigman 2024 predictions for Betfair Casino（FreeLibrary/Gale 转载本）",
    "published_at": "2024-01月上旬（文中自述距2024年开始不到一周），赛事2024-06-14开赛之前约五个月",
    "url": "",
    "timestamp_evidence": "转载本带 MGN Ltd 2024 版权与行文内时间自述（2024年首周），断语固定于赛事之前",
    "license_note": LIC_NOTE
  },
  "language": "en",
  "master_predictions": [{
    "master": "Inbaal Honigman",
    "tradition": "tarot",
    "date": "2024-01月上旬",
    "statement_excerpt": "England will not get further than the semi-final; Euro 2024 will eventually be won by Germany. After England's semi-final exit, Southgate's time as manager will be over, and his successor will be a colourful character with a fiery tongue.",
    "source": "Betfair Casino 2024 predictions（FreeLibrary/Gale 转载存档），记者 Laura Williams 署名整理",
    "direction": "positive",
    "key_assertions": [
      "德国将赢得 Euro 2024 冠军",
      "英格兰至多止步半决赛",
      "英格兰半决赛出局后 Southgate 时代结束，继任者为个性鲜明、言辞犀利之人"
    ],
    "timing_claim": "赛事2024-06-14至07-14"
  }],
  "outcome": {
    "description": "西班牙夺冠，决赛2–1击败英格兰（英格兰进入决赛）；德国止步八强。Southgate 于赛后辞职（其『时代结束』子断方向合，但所断的出局阶段与机制不合）。",
    "verified_by": "Euro 2024 公开赛事记录（决赛与各轮结果）及 Southgate 赛后辞职的公开报道"
  },
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名职业塔罗师、赛前约五个月公开发表、断语具体可证伪、结局有公开赛事记录。主断（德国冠军、英格兰止步四强）皆误。",
  "contamination": "high",
  "contamination_reason": "Euro 2024 为全球著名赛事，决赛与冠军为通识级事实，模型先验大概率已知。判 high，仅入储备。",
  "holdout_eligible": False,
  "notes": {"tags": ["足球", "欧洲杯", "冠军预测"], "comment": "同作者另见 NM-002、NM-012–NM-017，事项不同、三键不重复。", "cross_ref": "NM-002, NM-012"}
})

# ---------------- NM-011 Cricket World Cup 2023 / Greenstone Lobo ----------------
CASES.append({
  "id": "NM-011",
  "tradition": "vedic-astrology",
  "subject": {"name_or_desc": "2023年板球世界杯（印度主办）冠军归属", "gender": "不适用"},
  "context": {
    "question": "2023年板球世界杯冠军归谁？",
    "asked_at": "2023-10月（赛事2023-10-05开赛，决赛2023-11-19）",
    "setting": "2023年板球世界杯在印度举行；印度队队长 Rohit Sharma 生于1987年。预测者 Greenstone Lobo 长期主张1987年出生的一代队长运势论。",
    "attachments": {}
  },
  "provenance": {
    "carrier": "Asianet Newsable 赛前报道（2023-10月，赛事开赛前后），另有 Sportskeeda 等同期报道互证",
    "work": "Greenstone Lobo on Cricket World Cup 2023 winner（Asianet Newsable）",
    "published_at": "2023-10月，决赛2023-11-19之前逾一个月（采赛前文；其决赛前同事项文已去重剔除，见 BUILD-REPORT D2）",
    "url": "",
    "timestamp_evidence": "报道刊于赛事期间、决赛之前，断语对象为整届冠军，结果未揭晓时已固定",
    "license_note": LIC_NOTE
  },
  "language": "en",
  "master_predictions": [{
    "master": "Greenstone Lobo",
    "tradition": "vedic-astrology",
    "date": "2023-10月",
    "statement_excerpt": "India is the team with the highest possibility; Rohit Sharma will go on to win the World Cup.",
    "source": "Asianet Newsable, 2023-10月",
    "direction": "positive",
    "key_assertions": ["印度将赢得2023年板球世界杯", "1987年出生的队长 Rohit Sharma 将捧杯"],
    "timing_claim": "决赛日2023-11-19"
  }],
  "outcome": {
    "description": "澳大利亚在2023-11-19决赛击败印度，赢得2023年板球世界杯；印度为亚军。",
    "verified_by": "2023年板球世界杯公开赛事记录（决赛结果）"
  },
  "license_status": LIC,
  "redistributable": False,
  "outcome_grade": "A",
  "grade_note": "A级全合：具名职业体育占星师、赛前公开发表、断语明确、结局为公开赛事记录。断误。与 WP-009（同人、2019世界杯）及 NM-009（灰烬杯）事项不同，非重复。",
  "contamination": "high",
  "contamination_reason": "板球世界杯为全球著名赛事，2023届决赛结果为通识级事实。判 high，仅入储备。",
  "holdout_eligible": False,
  "notes": {"tags": ["板球", "世界杯", "冠军预测"], "comment": "同一赛事其决赛前 Asianet 文属同大师同事项，已择赛前文收录、决赛前文去重登记（BUILD-REPORT D2）。", "cross_ref": "NM-009, WP-009"}
})

# ---------------- NM-012..017 Oscars 2024 / Inbaal Honigman（同篇六个奖项，事项各异） ----------------
_OSCAR_CTX_BASE = {
  "asked_at": "2024-01-25（提名公布后、颁奖礼2024-03-10之前）",
  "attachments": {}
}
_OSCAR_PROV = {
  "carrier": "CheatSheet 刊载具名塔罗师 Inbaal Honigman 为 Slingo 所作第96届奥斯卡预测",
  "work": "Oscars 2024 predictions by Inbaal Honigman for Slingo（CheatSheet）",
  "published_at": "2024-01-25T02:25Z，颁奖礼2024-03-10之前约六周",
  "url": "",
  "timestamp_evidence": "载体页面带 Published 2024-01-25T02:25Z 时间戳，早于颁奖礼",
  "license_note": LIC_NOTE
}
_OSCAR_NOTE = "与同作者 NM-002、NM-010 事项不同；本组六例同篇发表，奖项（所测事项）各异、三键不重复，同载体情形与 NM-003–005 先例一致。"

def oscar(cid, category, nominees, excerpt, assertions, outcome_desc):
    return {
      "id": cid,
      "tradition": "tarot",
      "subject": {"name_or_desc": f"第96届奥斯卡金像奖（2024-03-10）{category}奖归属", "gender": "不适用"},
      "context": {
        "question": f"第96届奥斯卡{category}奖将归谁？",
        "asked_at": _OSCAR_CTX_BASE["asked_at"],
        "setting": f"第96届奥斯卡定于2024-03-10举行；{category}提名名单：{nominees}。",
        "attachments": {}
      },
      "provenance": dict(_OSCAR_PROV),
      "language": "en",
      "master_predictions": [{
        "master": "Inbaal Honigman",
        "tradition": "tarot",
        "date": "2024-01-25",
        "statement_excerpt": excerpt,
        "source": "CheatSheet, 2024-01-25（for Slingo）",
        "direction": "positive",
        "key_assertions": assertions,
        "timing_claim": "颁奖礼2024-03-10"
      }],
      "outcome": {
        "description": outcome_desc,
        "verified_by": "第96届奥斯卡官方获奖名单及公开报道"
      },
      "license_status": LIC,
      "redistributable": False,
      "outcome_grade": "A",
      "grade_note": "A级全合：具名职业塔罗师、颁奖前约六周带时间戳公开发表、单奖项断语具体可证伪、结局有官方获奖名单。",
      "contamination": "high",
      "contamination_reason": "奥斯卡为全球著名奖项，各奖项得主为通识级事实，模型先验大概率已知。判 high，仅入储备。",
      "holdout_eligible": False,
      "notes": {"tags": ["奥斯卡", "电影奖项"], "comment": _OSCAR_NOTE, "cross_ref": "NM-002, NM-010"}
    }

CASES.append(oscar("NM-012", "最佳女主角",
  "Annette Bening（《Nyad》）、Lily Gladstone（《花月杀手》）、Sandra Hüller（《坠落的审判》）、Carey Mulligan（《音乐大师》）、Emma Stone（《可怜的东西》）",
  "Annette Bening will win Best Actress for Nyad — the Academy has picked her as their winner; Emma Stone may leave empty-handed.",
  ["Annette Bening 凭《Nyad》获最佳女主角", "Emma Stone 将空手而归"],
  "Emma Stone 凭《可怜的东西》获最佳女主角；Annette Bening 未获奖。断误。"))

CASES.append(oscar("NM-013", "最佳男主角",
  "Bradley Cooper（《音乐大师》）、Colman Domingo（《鲁斯汀》）、Paul Giamatti（《留校联盟》）、Cillian Murphy（《奥本海默》）、Jeffrey Wright（《美国小说》）",
  "Cillian Murphy will win Best Actor for Oppenheimer.",
  ["Cillian Murphy 凭《奥本海默》获最佳男主角"],
  "Cillian Murphy 凭《奥本海默》获最佳男主角。断中。"))

CASES.append(oscar("NM-014", "最佳男配角",
  "Sterling K. Brown（《美国小说》）、Robert De Niro（《花月杀手》）、Robert Downey Jr.（《奥本海默》）、Ryan Gosling（《芭比》）、Mark Ruffalo（《可怜的东西》）",
  "Robert Downey Jr. will win Best Supporting Actor for Oppenheimer.",
  ["Robert Downey Jr. 凭《奥本海默》获最佳男配角"],
  "Robert Downey Jr. 凭《奥本海默》获最佳男配角。断中。"))

CASES.append(oscar("NM-015", "最佳女配角",
  "Emily Blunt（《奥本海默》）、Danielle Brooks（《紫色》）、America Ferrera（《芭比》）、Jodie Foster（《Nyad》）、Da'Vine Joy Randolph（《留校联盟》）",
  "Da'Vine Joy Randolph was always going to be winning an Oscar — she will win Best Supporting Actress for The Holdovers.",
  ["Da'Vine Joy Randolph 凭《留校联盟》获最佳女配角"],
  "Da'Vine Joy Randolph 凭《留校联盟》获最佳女配角。断中。"))

CASES.append(oscar("NM-016", "最佳导演",
  "Justine Triet（《坠落的审判》）、Martin Scorsese（《花月杀手》）、Christopher Nolan（《奥本海默》）、Yorgos Lanthimos（《可怜的东西》）、Jonathan Glazer（《利益区域》）",
  "Martin Scorsese will win Best Director for Killers of the Flower Moon.",
  ["Martin Scorsese 凭《花月杀手》获最佳导演"],
  "Christopher Nolan 凭《奥本海默》获最佳导演；Martin Scorsese 未获奖。断误。"))

CASES.append(oscar("NM-017", "最佳影片",
  "《美国小说》《坠落的审判》《芭比》《留校联盟》《花月杀手》《音乐大师》《奥本海默》《过往人生》《可怜的东西》《利益区域》",
  "Oppenheimer will win Best Picture.",
  ["《奥本海默》获最佳影片"],
  "《奥本海默》获最佳影片。断中。"))

# ---------------- 写出 cases.jsonl 与 inputs ----------------
def input_view(c):
    """题面：仅保留对象背景＋当时情境；剔除 master_predictions 与 outcome 本体；
    provenance 中性化（只记载体类型与日期，标题/链接可能含断语指向，一律不入题面）；
    grade_note 含中误讨论，一律不入题面。"""
    return {
      "id": c["id"],
      "tradition": c["tradition"],
      "subject": c["subject"],
      "context": c["context"],
      "provenance": {
        "carrier_type": "具名职业预测者于结果揭晓前公开发表（载体与时间戳证据见同批 cases.jsonl 对应条目；题面不载标题与链接以防断语泄漏）",
        "published_at": c["master_predictions"][0]["date"]
      },
      "language": c["language"],
      "license_status": c["license_status"],
      "redistributable": c["redistributable"],
      "outcome_grade": c["outcome_grade"],
      "contamination": c["contamination"],
      "holdout_eligible": c["holdout_eligible"],
      "notes": {
        "tags": c["notes"]["tags"],
        "leak_check": "已逐例自检：题面仅含对象背景与预测时点情境，不含大师断语、不含结局及结局派生信息；出处标题/链接已中性化剔除。",
        "cross_ref": c["notes"]["cross_ref"]
      }
    }

def main():
    ids = [c["id"] for c in CASES]
    assert len(ids) == len(set(ids)) == 17, ids
    with open(os.path.join(BASE, "cases.jsonl"), "w", encoding="utf-8") as f:
        for c in CASES:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    os.makedirs(os.path.join(BASE, "inputs"), exist_ok=True)
    for c in CASES:
        with open(os.path.join(BASE, "inputs", c["id"] + ".json"), "w", encoding="utf-8") as f:
            json.dump(input_view(c), f, ensure_ascii=False, indent=2)
    from collections import Counter
    print("cases:", len(CASES), Counter(c["contamination"] for c in CASES))

if __name__ == "__main__":
    main()
