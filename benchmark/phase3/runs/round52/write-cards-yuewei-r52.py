#!/usr/bin/env python3
"""R52 yuewei mining: write YW5-001..003 candidate pairs (inputs/gold separated).
Input cards: fields EXACTLY the R52 whitelist {id, tradition, subject, context,
question, setting, provenance, redistributable, license_status}.
Input-side content scan (task R52 marker sets) must be zero-hit before writing:
 L1: 断语线索 断曰 斷語 正议 正議 验语 驗語 断语： 斷語： 占断 占斷 大师断 大師斷
 L2: 果验 果然 果應 后验 後驗 结局 結局 应验 應驗
Field-name blacklist = any field outside the whitelist (asserted by key equality).
"""
import json, os

OUT = "/home/hatch/workspace/divination/benchmark/phase3/runs/round52/digestion/cards-mining-yuewei-r52"
os.makedirs(OUT, exist_ok=True)

WHITELIST = ["id", "tradition", "subject", "context", "question", "setting",
             "provenance", "redistributable", "license_status"]
L1 = ["断语线索", "断曰", "斷語", "正议", "正議", "验语", "驗語", "断语：", "斷語：",
      "占断", "占斷", "大师断", "大師斷"]
L2 = ["果验", "果然", "果應", "后验", "後驗", "结局", "結局", "应验", "應驗"]

PROV = ("《阅微草堂笔记》·卷十二·槐西杂志二(5)；在线全文实取 arteducation 分页站"
        "卷十二(5) https://www.arteducation.com.tw/guwen/bookv_17127.html；"
        "transcription=online-verbatim；访问日期 2026-10-31")
LIC = "古典文本公有领域；在线转录站条款未明，内部研究用"

cards = []

# ---------- YW5-001 李鹭汀六壬占妾三夫案 ----------
inp1 = {
    "id": "YW5-001",
    "tradition": "liuren",
    "subject": "李鹭汀（鬻古器者）之妾",
    "context": ("许文木言，康熙末年，鬻古器者李鹭汀为许文木父执辈，善六壬，惟晨起自占一课，"
                "而不肯为人卜，自言才得康节六七分。年五十余无子，惟蓄一妾。一日许父造访，"
                "闻其妾泣且絮语相诘，又闻鹭汀力辩所言为真实语、非戏语，许父乃叩问反目之故。"),
    "question": "李鹭汀以当日晨课所占告其妾者为何？其课所示妾之姻缘归宿为何？",
    "setting": "清·康熙末年；李鹭汀晨起自占六壬一课，许父造访时以课语告妾",
    "provenance": PROV,
    "redistributable": False,
    "license_status": LIC,
}
gold1 = dict(inp1)
gold1.update({
    "record_status": "candidate-r52-mining",
    "notes": ("同条另有鹭汀占仙人扶竹杖来访一子案，应验落在雕竹纯阳像求售，属谐谑式应验、"
              "建议 B，只登记于 MINING-yuewei-cont-r52.md，不并入本卡。"),
    "master_predictions": [{
        "master": "李鹭汀（鬻古器者，许文木父执）",
        "date": None,
        "tradition": "liuren",
        "direction": None,
        "key_assertions": [],
        "source": "《阅微草堂笔记》·卷十二·槐西杂志二",
        "statement_excerpt": ("今日占课，有二客来市古器，一其前世夫，尚有一夕缘；"
                              "一其后夫，结好当在半年内，并我为三，生在一堂矣。"),
    }],
    "outcome": {
        "description": "越半载鹭汀果死，妾鬻于一翰林家，嫡不能容，过一夕即遣出，再鬻于一中书舍人家，乃相安云。",
        "verified_by": "原文结局文本（逐字；独立事件，非确认式）",
    },
    "passage_full": ("许文木言，康熙末年，鬻古器李鹭汀，其父执也，善六壬，惟晨起自占一课，而不肯为人卜。"
                     "曰：多泄未来，神所恶也。有以康节比之者，曰：吾才得六七分耳。尝占得某日当有仙人扶竹杖来，"
                     "饮酒题诗而去，焚香候之，乃有人携一雕竹纯阳像求售，侧倚一贮酒壶卢，上刻朝游北海一诗也。"
                     "康节安有此失乎。年五十余无子，惟蓄一妾，一日，许父造访，闻其妾泣，且絮语曰：此何事而以戏人，"
                     "其试我乎？又闻鹭汀力辩曰：此真实语，非戏也。许父叩反目之故，鹭汀曰：事殊大奇，今日占课，"
                     "有二客来市古器，一其前世夫，尚有一夕缘；一其后夫，结好当在半年内，并我为三，生在一堂矣。"
                     "吾以语彼，彼遽恚怒，数定无可移，我不泣而彼泣，我不讳而彼讳之，岂非痴女子哉。"
                     "越半载鹭汀果死，妾鬻于一翰林家，嫡不能容，过一夕即遣出，再鬻于一中书舍人家，乃相安云。"),
    "grade_suggestion": "A",
    "grade_reason": ("断语逐字可录且多项具体（二客同堂、一为前世夫仅一夕缘、一为后夫半年内结好）；"
                     "结局为独立事件文本：鹭汀越半载死、妾鬻翰林家过一夕即遣出（应一夕缘）、"
                     "再鬻中书舍人家相安（应后夫），逐项对应。单注：后夫结好时点自占课日计，"
                     "鹭汀之死已在越半载，时限一项略宽，主持可据此降 B，本席照实登记。"),
    "contamination_suggestion": "low",
    "contamination_reason": ("2026-10-31 以「李鹭汀 六壬 妾 前世夫」检索，零个案命中（返回仅本书通论维基页与无关页）；"
                             "占者为鬻古器市井术者、对象为其无名之妾，无名人无名案；三键（李鹭汀／许文木／二客）"
                             "对 masters-dataset 与历轮台账 grep 零命中，净新。"),
})
cards.append((inp1, gold1))

# ---------- YW5-002 卢暉吉推郭氏寿案 ----------
inp2 = {
    "id": "YW5-002",
    "tradition": "ming",
    "subject": "侍姬郭氏（纪昀侍姬）",
    "context": ("侍姬郭氏，其父大同人，流寓天津。郭氏年十三归纪昀，生数子皆不育，惟一女适德州卢荫文。"
                "卢荫文之父卢暉吉（暉吉观察）善星命，曾为郭氏推命论寿数。"),
    "question": "卢暉吉为郭氏推命，所论寿数上限为何？",
    "setting": "清·乾隆间；卢暉吉以星命为纪昀侍姬郭氏推寿数",
    "provenance": PROV,
    "redistributable": False,
    "license_status": LIC,
}
gold2 = dict(inp2)
gold2.update({
    "record_status": "candidate-r52-mining",
    "notes": "同条后段郭氏祈签关帝一案另建 YW5-003，两卡断面互不相含。",
    "master_predictions": [{
        "master": "卢暉吉（暉吉观察，卢荫文之父）",
        "date": None,
        "tradition": "ming",
        "direction": None,
        "key_assertions": [],
        "source": "《阅微草堂笔记》·卷十二·槐西杂志二",
        "statement_excerpt": "暉吉善星命，尝推其命寿不能四十。",
    }],
    "outcome": {
        "description": "果三十七而卒。",
        "verified_by": "原文结局文本（逐字；具体享年，非确认式套语）",
    },
    "passage_full": ("侍姬郭氏，其父大同人，流寓天津，生时其母梦鬻端午彩符者，买得一枝，因以为名，"
                     "年十三归余，生数子，皆不育，惟一女，适德州卢荫文，暉吉观察子也。"
                     "暉吉善星命，尝推其命寿不能四十，果三十七而卒。"),
    "grade_suggestion": "A",
    "grade_reason": "断语逐字可录（寿不能四十，上限明确）；结局「三十七而卒」为具体数值、独立可核，非确认式泛语。",
    "contamination_suggestion": "low-mid",
    "contamination_reason": ("从严：对象为纪昀侍姬，其早卒事在纪昀生平叙事脉络内，按名人关联口径自 mid 起评；"
                             "但 2026-10-31 以「卢暉吉 推命 郭氏 寿不能四十」及姓名键检索均零个案命中，"
                             "占者卢暉吉冷僻、无独立条目，个案本身不见于通论，据冷门性证据降一档至 low-mid；"
                             "入账与否候主持终裁（照台账口径 low-mid 只登记不入账）。"),
})
cards.append((inp2, gold2))

# ---------- YW5-003 郭氏祈签关帝、邱二田解签案 ----------
inp3 = {
    "id": "YW5-003",
    "tradition": "qian",
    "subject": "侍姬郭氏（纪昀侍姬）",
    "context": ("纪昀在西域时，侍姬郭氏已病瘵。郭氏祈签于关帝，问尚能与纪昀相见否；"
                "时门人邱二田在寓闻之，曾就签语有所评断。"),
    "question": "郭氏祈签所问为何？邱二田就签语所下评断为何？",
    "setting": "清·乾隆间；纪昀在西域，郭氏病中于关帝前祈签问相见，邱二田在寓解签",
    "provenance": PROV,
    "redistributable": False,
    "license_status": LIC,
}
gold3 = dict(inp3)
gold3.update({
    "record_status": "candidate-r52-mining",
    "notes": ("tradition 代码「qian」为签占暂定码：既有卡 tradition 代码集（至 R51）未见签占先例，"
              "请主持定码后回填。同条前段卢暉吉推命一案另建 YW5-002。"),
    "master_predictions": [{
        "master": "邱二田（纪昀门人；签为郭氏自祈于关帝）",
        "date": None,
        "tradition": "qian",
        "direction": None,
        "key_assertions": [],
        "source": "《阅微草堂笔记》·卷十二·槐西杂志二",
        "statement_excerpt": ("得一签曰：喜鹊檐前报好音，知君千里有归心，绣帏重结鸳鸯带，叶落霜雕寒色侵。"
                              "（邱二田解）见则必见，然末句非吉语也。"),
    }],
    "outcome": {
        "description": ("后余辛卯六月还，姬病良已，至九月，忽转剧，日渐沈绵，遂以不起。"
                        "（纪昀后题其遗事诗注：姬以三月三十日亡。）"),
        "verified_by": "原文结局文本（逐字；相见与病卒两项独立事件）",
    },
    "passage_full": ("余在西域时，姬已病瘵，祈签关帝，问尚能相见否？得一签曰：喜鹊檐前报好音，"
                     "知君千里有归心，绣帏重结鸳鸯带，叶落霜雕寒色侵。谓余即当以秋冬归，意甚喜，"
                     "时门人邱二田在寓闻之，曰：见则必见，然末句非吉语也。后余辛卯六月还，姬病良已，"
                     "至九月，忽转剧，日渐沈绵，遂以不起。"),
    "grade_suggestion": "A",
    "grade_reason": ("签诗逐字可录、解者邱二田具名且判语逐字（见则必见、末句非吉语）；"
                     "结局两项独立对应：辛卯六月还而相见（应必见）、九月病转剧遂不起（应末句非吉）。"),
    "contamination_suggestion": "low-mid",
    "contamination_reason": ("从严两点：对象同 YW5-002（纪昀侍姬）自 mid 起评；签诗本身为关帝灵签通行签文"
                             "（今通行本第七十一签，签文文本广见流传）——但签文只在金标侧，输入侧不含；"
                             "本案问事、邱二田解语与结局组合 2026-10-31 检索零个案命中，据此降一档至 low-mid；"
                             "入账与否候主持终裁。"),
})
cards.append((inp3, gold3))

# ---------- scan & write ----------
for inp, gold in cards:
    assert list(inp.keys()) == WHITELIST, f"{inp['id']}: input fields off-whitelist: {list(inp.keys())}"
    text = json.dumps(inp, ensure_ascii=False)
    hits = [m for m in L1 + L2 if m in text]
    assert not hits, f"{inp['id']}: input-side marker hits {hits}"
    for name, obj in [(f"{inp['id']}-input.json", inp), (f"{inp['id']}-gold.json", gold)]:
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
print("OK: input scan zero-hit for", [i["id"] for i, _ in cards])
print("written:", sorted(os.listdir(OUT)))
