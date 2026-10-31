#!/usr/bin/env python3
# R91 数据席落盘脚本：case-annotations-r91.json + manifest-carryover-r91-addendum.md 配套断言
import json, pathlib, collections, sys
base = pathlib.Path('/home/hatch/workspace/divination/benchmark/phase3')
ann90 = json.load(open(base/'data/case-annotations-r90.json', encoding='utf-8'))
man = json.load(open(base/'runs/round91/judging/outcome-manifest.json', encoding='utf-8'))
hm = json.load(open(base/'runs/round91/judging/host-mapping.json', encoding='utf-8'))
anon_of = {v: k for k, v in hm.items()}
cases = man['cases']

def outcome(cid):
    v = cases[cid]
    assert isinstance(v, str) and v.strip(), cid
    return v

def entry(cid, flag, finding, short, relation=None):
    if relation is None:
        n = sum(1 for a in ann90['annotations'] if a['case_id'] == cid)
        relation = '新登记（该例首条）' if n == 0 else f'同例新旨并行（在册 {n} 条各旨独立、互不覆盖）'
    return {
        'anon_id': anon_of[cid],
        'case_id': cid,
        'disposition': '部分成立',
        'finding': finding,
        'flag': flag,
        'manifest_carry_suggestion': f'平台侧新登记：自 R92 起承接本 R91 标注：按「{short}，部分成立」登记；结局原文照录不改。',
        'relation': relation,
        'registered_round': 91,
        'sources_checked': [
            f'divination/benchmark/phase3/inputs-dev12/{cid}.json',
            f'divination/benchmark/phase3/runs/round91/judging/outcome-manifest.json cases[{cid}]',
            f'divination/benchmark/phase3/runs/round91/predictions/{cid}.json',
        ],
        'source_seats': ['R91 平台盲测席 basis 自报', 'R91 数据席回读原卡'],
    }

new = []

# LY-007 FREEZE 首件
new.append({
    'anon_id': anon_of['LY-007'], 'case_id': 'LY-007', 'disposition': '部分成立',
    'flag': '主持裁定（FREEZE-r91）：卡面实载 tradition=\'liuyao\'，R91 prediction basis 首行误称「卡面未标注 tradition/system 字段」',
    'finding': '主持裁定部分成立（FREEZE-r91 tradition 旗标裁定，本席逐件回读复核）：回原卡——卡面顶层逐字载 tradition＝\'liuyao\'（卡键集 context／provenance／subject／tradition／uid）；R91 prediction basis 首行逐字作「卡面未标注 tradition/system 字段，按题面体裁自决」，与卡面实载不符、措辞不实一层成立。但该例实际作断体系为六爻纳甲（basis 首行自注「六爻纳甲卦盘俱全，用六爻」、systems_used 明载六爻纳甲，与卡面 tradition 一致），无体系误标、无虚构卡面值，不作废不重测（与 R90 AS-009 同型同裁）。R91 manifest 结局逐字载「果得遇於未日」，终局明载可核。故部分成立。该例首条。',
    'manifest_carry_suggestion': '平台侧新登记：自 R92 起承接本 R91 标注：按「卡面实载 tradition＝liuyao、R91 首行误称未标注属措辞不实，注记须分述卡面实载与首行误称、不得沿误称转写；实际作断体系与卡面一致、无体系误标，部分成立」登记；结局原文照录不改。',
    'relation': '新登记（该例首条；平台面新定案第一件，承 FREEZE-r91 裁定）',
    'registered_round': 91,
    'sources_checked': ['divination/benchmark/phase3/inputs-dev12/LY-007.json',
                        'divination/benchmark/phase3/runs/round91/judging/outcome-manifest.json cases[LY-007]',
                        'divination/benchmark/phase3/runs/round91/predictions/LY-007.json',
                        'divination/benchmark/phase3/runs/round91/FREEZE-r91.md'],
    'source_seats': ['主持检查器＋FREEZE-r91 裁定', 'R91 数据席回读原卡'],
})

GROUPS = [
    ('G7', ['LY-027','LY-028','LY-029','LY-030','LY-031','LY-032','LY-033','LY-034','LY-035'],
     'R91 平台 basis 留痕：卡面 chart_note 自注装卦表 OCR 行序错乱、逐爻未能可靠还原、逐爻表不录（残损类）',
     '回原卡——卡面 chart_note 逐字自注装卦表经 OCR 转录行序错乱、逐爻装卦未能可靠还原、逐爻表不录、本条只录可互证资讯，残损一层属实；R91 basis 逐字照实登记、只据卦名／用神／空亡／动爻立论并降置信，不臆补逐爻；R91 manifest 结局逐字载「{OUT}」，终局明载可核。故部分成立。',
     '卡面 chart_note 自注 OCR 行序错乱、逐爻未能可靠还原、逐爻表不录，已照实登记、只据可互证资讯立论；终局明载'),
    ('G10', ['LY-304','LY-305','LY-306','LY-307','LY-309','LY-311'],
     'R91 平台 basis 留痕：卡面 chart_note 自注装卦表 OCR 错乱经校正本补录（残损类）',
     '回原卡——卡面 chart_note 自注装卦表 OCR 错乱、经校正本补录，残损一层属实；R91 basis 逐字照实登记、以卡面用神／动爻字段为准作断并降置信；R91 manifest 结局逐字载「{OUT}」，终局明载可核。故部分成立。',
     '卡面 chart_note 自注 OCR 错乱经校正本补录、已照实登记以卡面字段为准；终局明载'),
    ('G11', ['LY-312','LY-314','LY-315','LY-318','LY-319','LY-320','LY-323','LY-325','LY-328','LY-329','LY-330','LY-331','LY-333','LY-335','LY-336','LY-340','LY-342'],
     'R91 平台 basis 留痕：卡面 chart_note 自注装卦表 OCR 行序错乱、逐爻表不录，空亡／伏神为推算复原（残损类）',
     '回原卡——卡面 chart_note 逐字自注装卦表 OCR 行序错乱、逐爻表不录，空亡／伏神为推算复原 grades，残损一层属实；R91 basis 逐字照实登记并降置信、不以推算复原冒充直载；R91 manifest 结局逐字载「{OUT}」，终局明载可核。故部分成立。',
     '卡面 chart_note 自注 OCR 行序错乱、逐爻表不录，空亡／伏神推算复原已照实登记；终局明载'),
    ('G12', ['LY-402','LY-403','LY-404','LY-405','LY-406','LY-407','LY-408','LY-411','LY-413','LY-415','LY-418','LY-421','LY-424','LY-425'],
     'R91 平台 basis 留痕：卡面 attachments 未载 yongshen 与空亡字段（残损类）',
     '回原卡——卡面 attachments 逐项核：只有 casting_method／hexagram／moving_lines／chart_lines_top_to_bottom，未载 yongshen 与空亡字段，缺载一层属实；R91 basis 逐字照实登记、空亡按旬空规则推得并注明、用神按所问自取，不冒充卡面直载；R91 manifest 结局逐字载「{OUT}」，终局明载可核。故部分成立。',
     '卡面 attachments 未载 yongshen 与空亡字段、已照实登记按规则推补；终局明载'),
    ('G15', ['LY-531','LY-532','LY-533','LY-534','LY-535','LY-536','LY-538','LY-539','LY-540','LY-541','LY-542','LY-543','LY-627','LY-628','LY-629'],
     'R91 平台 basis 留痕：卡面 chart_note 自注装卦表 OCR 行序错乱、逐爻装卦未能可靠还原（残损类）',
     '回原卡——卡面 chart_note 逐字自注装卦表为双栏排版经 OCR 转录行序错乱、逐爻装卦未能可靠还原，残损一层属实；R91 basis 逐字照实登记、逐爻只按卡面所录行序作断并降置信，空亡／伏神推算复原面照实注明；R91 manifest 结局逐字载「{OUT}」，终局明载可核。故部分成立。',
     '卡面 chart_note 自注 OCR 行序错乱、逐爻未能可靠还原，已照实登记按所录行序作断；终局明载'),
    ('G16', ['LY-601','LY-604','LY-605','LY-606','LY-607','LY-608','LY-609','LY-610','LY-611','LY-612','LY-613'],
     'R91 平台 basis 留痕：卡面 notes.completion_grade 自注 palace／kongwang（部分例并 hidden_lines）为推算复原（自注类）',
     '回原卡——卡面 notes.completion_grade 逐项载 palace（宫）与 kongwang（空亡）为「推算复原」（原书未另标）、余项为「直载」，自注一层属实；R91 basis 逐字照实登记此 grades、按卡面盘面作断，不以推算复原冒充原书直载；R91 manifest 结局逐字载「{OUT}」，终局明载可核。故部分成立。',
     '卡面 completion_grade 自注宫／空亡为推算复原、已照实登记；终局明载'),
]
for gname, ids, flag, ftmpl, short in GROUPS:
    for cid in ids:
        out = outcome(cid)
        new.append(entry(cid, flag, ftmpl.replace('{OUT}', out), short))

# G11 special members
SPECIAL_G11 = {
 'LY-322': ('卡面「应上巳火」用神文字与爻位标注不合一面已由在册 R79 条登记、本条不重裁；本条只裁 OCR／推算复原面：',
            '卡面 chart_note 自注 OCR 行序错乱、逐爻表不录，空亡推算复原已照实登记（用神文字不合面在册 R79 条并行）；终局明载'),
 'LY-324': ('另卡面 hexagram 逐字载卦名页面作「震为木」、自注疑为「震为雷」之误，此卡面自注旗标一并属实；',
            '卡面 chart_note 自注 OCR 行序错乱、逐爻表不录，空亡／伏神推算复原已照实登记；卦名括注「震为木」疑误卡面已自注；终局明载'),
 'LY-339': ('另复占空亡一面：卦名括注作寅卯与复占丁卯日旬空规则不合，卡面补录以规则推得戌亥为准、basis 照实登记从补录值，此卡面不合旗标一并属实（两卦合断／OCR 面已由在册 R86 条登记、本条只裁空亡括注面）；',
            '复占空亡括注（寅卯）与丁卯日旬空规则不合、卡面补录戌亥为准已照实登记；终局明载'),
 'LY-344': ('另题面一面：卡面 setting 逐字自注页面占题「占子久出何日冲」之「冲」疑为「回」之误，此卡面自注旗标一并属实；',
            '卡面 chart_note 自注 OCR 行序错乱、逐爻表不录，空亡／伏神推算复原已照实登记；题面「冲」疑「回」卡面已自注；终局明载'),
}
for cid, (extra, short) in SPECIAL_G11.items():
    out = outcome(cid)
    finding = ('回原卡——卡面 chart_note 逐字自注装卦表 OCR 行序错乱、逐爻表不录，空亡为推算复原，残损一层属实；'
               + extra +
               f'R91 basis 逐字照实登记并降置信；R91 manifest 结局逐字载「{out}」，终局明载可核。故部分成立。')
    new.append(entry(cid, 'R91 平台 basis 留痕：卡面 chart_note 自注装卦表 OCR 行序错乱、逐爻表不录，空亡／伏神为推算复原，另含卡面自注旗标（残损类＋卡面不合类）', finding, short))

SINGLES = [
 ('DT-001', 'R91 平台 basis 留痕：卡面未给变卦全盘、化神方向未载（残损类）',
  '回原卡——卡面 hexagram 只载本卦「雷水解」、逐爻为本卦六行，未载变卦全盘与化神方向，缺载一层属实；R91 basis 逐字照实登记此限、降置信；R91 manifest 结局逐字载「以后果无事（父病无事）。」，终局明载可核。故部分成立。',
  '卡面未给变卦全盘、化神方向未载，已照实登记；终局明载'),
 ('DT-002', 'R91 平台 basis 留痕：卡面动爻原文以本宫飞伏语叙述、动爻组读法有歧（卡面不合类）',
  '回原卡——卡面 moving_lines 逐字载动爻原文以本宫飞伏语叙述（本宫巳火兄动、本宫亥水鬼动）、语涉飞伏换算、图解本整理为蒙之升，读法有歧一层属实；R91 basis 逐字照实登记、按卡面所列现卦爻位为准作断并留 disputed 痕；R91 manifest 结局逐字载「后果于九月己卯日巳时生男，母子俱得平安。」，终局明载可核。故部分成立。与在册 R87 DT-004 条同型同旨、各自独立。',
  '卡面动爻原文飞伏叙述、读法有歧，已照实登记按现卦爻表为准；终局明载'),
 ('AS-011', 'R91 平台 basis 留痕：卡面年份未载（残损类）',
  '回原卡——卡面 asked_at 逐字作「June of an unstated year」，年份未载属实；R91 basis 逐字照实登记、应期只用卡面 6 月日期；卡面盘面关键位置实载，R91 manifest 结局为长文实载（以「Confirmed in the text」起、逐项载复核结果），终局明载可核。故部分成立。',
  '卡面年份未载（asked_at 自载 unstated year）、已照实登记；终局明载'),
 ('AS-207', 'R91 平台 basis 留痕：卡面未给上升度数（残损类）',
  '回原卡——卡面 attachments note 逐字载「the ascending degree is not given in the prose and is not asserted here」，上升度数未给属实；R91 basis 逐字照实登记、不据度数细化；其余关键位置卡面散文实载，R91 manifest 结局逐字载「\'He was beheaded about the tenth of January following.\'」，终局明载可核。故部分成立。',
  '卡面未给上升度数（note 明言）、已照实登记不据之细化；终局明载'),
 ('MH-001', 'R91 平台 basis 留痕：卡面未载动爻爻辞（残损类）',
  '回原卡——卡面 attachments 只有 casting_method／method_detail／hexagram，未载动爻爻辞，缺载一层属实；R91 basis 逐字照实登记「爻辞未引」、只走体用一路；R91 manifest 结局逐字载「次晚果有鄰女折花墮地傷股」，终局明载可核。故部分成立。与在册 R85 条（tradition 首行旨）各旨独立并行。',
  '卡面未载动爻爻辞、已照实登记只走体用一路；终局明载'),
 ('MH-002', 'R91 平台 basis 留痕：卡面未载动爻爻辞（残损类）',
  '回原卡——卡面 attachments 只有 casting_method／method_detail／hexagram，未载动爻爻辞，缺载一层属实；R91 basis 逐字照实登记、未引辞作断、只走体用生克一路；R91 manifest 结局逐字载「次日午時，果有貴官觀牡丹，二馬相齧，群至花間馳驟，花盡為之踐毀」，终局明载可核。故部分成立。另注：本例 tradition 旗标候选经 FREEZE-r91 裁定不成立（首行逐字照录卡面 tradition＝meihua），与本条各旨独立。',
  '卡面未载动爻爻辞、已照实登记只走体用一路；终局明载'),
 ('MH-003', 'R91 平台 basis 留痕：卡面未载爻辞（残损类）',
  '回原卡——卡面 attachments 只有 casting_method／method_detail／hexagram，未载爻辞，缺载一层属实；R91 basis 逐字照实登记「未引辞」；R91 manifest 结局逐字载「聞之，果借斧」，终局明载可核。故部分成立。与在册 R85 条（tradition 首行旨）各旨独立并行。',
  '卡面未载爻辞、已照实登记；终局明载'),
 ('OC-010', 'R91 平台 basis 留痕：卡面注明原书未附大运表（残损类）',
  '回原卡——卡面 birth note 逐字载「原书未附大运表」，大运表缺载属实；R91 basis 逐字照实登记、运程只定方向不报起运岁数；四柱实载，R91 manifest 结局逐字载溥仪 1932 年出任伪满洲国执政、1934 年称帝、1945 年被俘、1967 年卒等事，终局明载可核。故部分成立。',
  '卡面注明原书未附大运表、已照实登记运程只定方向；终局明载'),
 ('OC-013', 'R91 平台 basis 留痕：卡面仅注八岁起运、无大运干支表（残损类）',
  '回原卡——卡面 birth note 只载「八岁起运」、未载大运干支表，缺载一层属实；R91 basis 逐字照实登记、运段只定方向；四柱实载，R91 manifest 结局逐字载周信芳盛名终身、1975 年卒于上海，终局明载可核。故部分成立。',
  '卡面仅注八岁起运、无大运干支表，已照实登记；终局明载'),
 ('OC-015', 'R91 平台 basis 留痕：卡面注明生庚据西报传略译演、来源为二手传略（自注类）',
  '回原卡——卡面 birth note 逐字载「韦氏据西报传略译生庚演造」，生庚来源为二手传略一层属实且卡面自注；R91 basis 逐字照实登记、置信据此下调；四柱实载，R91 manifest 结局逐字载乔治五世事历（1891 年患伤寒、1910 年登基等），终局明载可核。故部分成立。',
  '生庚据西报传略译演、二手来源卡面已自注并降置信；终局明载'),
 ('OC-019', 'R91 平台 basis 留痕：卡面注明他书另载全异四柱、本例以徐乐吾书为准（卡面不合类）',
  '回原卡——卡面 birth note 逐字载「韦千里《千里命稿》另载癸巳 甲寅 壬辰 庚子，两书所载全异，本例以徐乐吾书为准」，两书四柱全异一层属实且卡面自注出处与取舍；R91 basis 逐字照实登记、按卡面指定口径作断、未混用异造；本例四柱（癸巳 丙辰 壬申 癸卯）实载，R91 manifest 结局明载可核。故部分成立。与在册 R84／R89 两条（tradition 首行旨、不成立）各旨独立并行。',
  '他书另载全异四柱、卡面已自注以徐乐吾书为准；终局明载'),
 ('OC-030', 'R91 平台 basis 留痕：卡面仅载月将、未载旬空（残损类）',
  '回原卡——卡面 attachments 载课式／三传／月将（亥将），未载旬空，缺载一层属实；R91 basis 逐字照实登记「三传不判空亡」；R91 manifest 结局逐字载「未几，工科上疏题复巡按差，巡方官复设；吏书缺未复。」，终局明载可核。故部分成立。',
  '卡面未载旬空、已照实登记三传不判空亡；终局明载'),
 ('YM-035', 'R91 平台 basis 留痕：卡面自注占日承前例、原文未重记占日（自注类）',
  '回原卡——卡面 asked_at 逐字载「丑建甲寅旬乙卯日（与前例同日，原文『复一人亦占』未重记占日）」，占日承前例一层属实且卡面自注；R91 basis 逐字照实登记、按卡面自注采用乙卯日并留痕；盘面实载，R91 manifest 结局逐字载「及次年二月始痘。」，终局明载可核。故部分成立。',
  '占日承前例、卡面已自注并照实登记采用；终局明载'),
 ('YM-055', 'R91 平台 basis 留痕：占年之具体年份卡面未载（残损类）',
  '回原卡——本例问发迹何年，卡面 asked_at 只载「酉建甲寅旬壬戌日」、未载占问具体年份，缺载一层属实；R91 basis 逐字照实登记、应期只能落支年并降置信；盘面实载，R91 manifest 结局逐字载「丑年发甲是也。」，终局明载可核。故部分成立。另注：本例 tradition 旗标候选经 FREEZE-r91 裁定不成立（首行另述他字段未载、非 tradition），与本条各旨独立。',
  '占年具体年份卡面未载、已照实登记应期只落支年；终局明载'),
 ('YM-063', 'R91 平台 basis 留痕：卡面未载行程远近（残损类）',
  '回原卡——本例占弟兄归期，卡面 question／setting／attachments 逐项核均未载行程远近，缺项一层属实；R91 basis 逐字照实登记此缺项、按行人门远应月取月档并降置信；盘面实载，R91 manifest 结局逐字载「后遇丁丑，冲动未爻，其弟乃还。」，终局明载可核。故部分成立。另注：本例 tradition 旗标候选经 FREEZE-r91 裁定不成立，与本条各旨独立。',
  '卡面未载行程远近、已照实登记并降置信；终局明载'),
 ('YY2-005', 'R91 平台 basis 留痕：空亡卡面未载、按旬空规则推算（残损类）',
  '回原卡——卡面 attachments 逐项核未载空亡字段，空亡未载属实；R91 basis 逐字照实登记空亡按庚辰日甲戌旬推得申酉、注明推算非卡面原文；盘面实载，R91 manifest 结局逐字载「后于子日成就，盖文书旺于子，且冲破午胎也。」，终局明载可核。故部分成立。另注：本例 tradition 旗标候选经 FREEZE-r91 裁定不成立，与本条各旨独立。',
  '空亡卡面未载、推算已照实注明；终局明载'),
 ('LY-253', 'R91 平台 basis 留痕：卡面自注变卦名有原文／核算出入（卡面不合类）',
  '回原卡——卡面 hexagram 逐字载「澤地萃之澤山咸（原文作萃之否，據裝卦爻象核算變卦為咸，見 notes）」，变卦名原文与核算出入一层属实且卡面自注；R91 basis 逐字照实登记、以卡面装卦爻象为准读；盘面逐爻实载，R91 manifest 结局逐字载「果於雞鳴蘇醒﹐次日不藥而愈。」，终局明载可核。故部分成立。',
  '变卦名原文／核算出入卡面已自注、以装卦爻象为准；终局明载'),
 ('LY-259', 'R91 平台 basis 留痕：卡面未载伏神栏、伏父为规则推得（残损类）',
  '回原卡——卡面 attachments 逐项核未载伏神／hidden_lines 栏，伏神未载属实；R91 basis 逐字照实登记伏父为按纳甲伏神规则推得并注明；盘面逐爻实载，R91 manifest 结局为长文实载（安坟而愈一节明载），终局明载可核。故部分成立。',
  '卡面未载伏神栏、伏父规则推得已照实注明；终局明载'),
 ('LY-252', 'R91 平台 basis 留痕：卡面未载空亡与伏神栏、皆按规则推得（残损类）',
  '回原卡——卡面 attachments 逐项核未载空亡与伏神栏，缺载一层属实；R91 basis 逐字照实登记皆按干支与纳甲规则推得并降置信；盘面逐爻实载，R91 manifest 结局逐字载本日愈之事实层（结局后半混入断法通则一面已由在册 R75 条登记、本条不重裁），终局明载可核。故部分成立。',
  '卡面未载空亡与伏神栏、规则推得已照实注明；终局明载'),
 ('LY-218', 'R91 平台 basis 留痕：卡面两占并录、chart_lines 两卦并列共 12 行（多卦合卡类）',
  '回原卡——卡面 question 逐字载「先占父壽、又占母壽」，chart_lines_top_to_bottom 共 12 行、两卦并列，两占并录一层属实；R91 basis 逐字照实登记、依卦名与动爻字段分属两卦读取；两占问事分载，R91 manifest 结局逐字载父健、母终于子年两面，终局明载可核。故部分成立。与在册 R75 条（同 prediction 两占方向旨）各旨独立并行。',
  '卡面两占并录、12 行并列已照实登记分属读取；终局明载'),
 ('LY-227', 'R91 平台 basis 留痕：卡面两占并录、再占动爻仅初爻一动（多卦合卡类）',
  '回原卡——卡面 setting 逐字载「問鄉試，前後兩占」，chart_lines 共 12 行、两占并录属实；R91 basis 逐字照实登记、按卦名分属读取；R91 manifest 结局逐字载得成名及再占通则一节（个案事实层明载），终局明载可核。故部分成立。与在册 R75 条各旨独立并行。',
  '卡面两占并录已照实登记分属读取；终局明载'),
 ('LY-255', 'R91 平台 basis 留痕：卡面两占并录（多卦合卡类）',
  '回原卡——卡面 question 逐字载占沟流宜否、又再占修沟之后何如，chart_lines 共 12 行、两占并录属实；R91 basis 逐字照实登记、按卦名分属读取；R91 manifest 结局逐字载「後於申年升任﹐應申年者﹐值官之年也。」，终局明载可核（修沟面未载一面已由在册 R79 条登记、本条不重裁）。故部分成立。',
  '卡面两占并录已照实登记分属读取；终局明载'),
 ('YY-006', 'R91 平台 basis 留痕：卡面未载月建与日辰（残损类）',
  '回原卡——卡面 asked_at 只载「明正统己巳（1449年）」、未载月建与日辰，旺衰日月层缺失属实；R91 basis 逐字照实登记并在 prediction 与 basis 双注、降置信；卦盘逐爻实载，R91 manifest 结局逐字载「后英宗南旋，及锢南内，最后夺门复辟，年月日悉符其占。」，终局明载可核（结局总承粒度面已由在册 R75 条登记、本条不重裁）。故部分成立。另注：本例 tradition 旗标候选经 FREEZE-r91 裁定不成立，与本条各旨独立。',
  '卡面未载月建与日辰、已照实登记并降置信；终局明载'),
 ('LR3-107', 'R91 平台 basis 留痕：卡面自注课式名首字残泐存疑（自注类）',
  '回原卡——卡面 attachments 课式逐字载「退茹（原书课体首字作「鬼」，疑残泐[存疑]）」，课式名首字残泐存疑属实且卡面自注；R91 basis 逐字照实登记、不据课式名加断、只据三传天将作断并降置信；四课／三传实载，R91 manifest 结局逐字载「后知为荆州知府王承曾，甲戌进士，以失城逮问，贼破燕京始出。」，终局明载可核。故部分成立。与在册 R85 条（结局断面旨）各旨独立并行。',
  '课式名首字残泐存疑卡面已自注、不据课式名加断；终局明载'),
 ('BZ-104', 'R91 平台 basis 留痕：卡面无大运、无干支全历（残损类）',
  '回原卡逐项核——卡面未载大运与出生年月日时干支全历，应期只能定年档一层属实（成立面）；但 R91 basis 径称「无出生年月日时干支」一层与卡面不合：卡面 basic_info 与 attachments.pillars 实载四柱「壬子 癸丑 己酉 癸酉」（成立面之反面）。R91 basis 已明写应期限度并降置信；R91 manifest 结局逐字载 1990 年患肝炎住院、骑摩托车撞伤等事（书内自述口头反馈一面已由在册 R79 条登记），终局明载可核。故部分成立。',
  '大运与干支全历未载属实、basis 称无出生干支一层与卡面四柱实载不合；终局明载'),
 ('LY-614', 'R91 平台 basis 留痕：卡面自注原书六神栏本批未录（残损类）',
  '回原卡——卡面 notes.completion_grade source_locator 逐字载「原書裝卦表另載六神欄，本批未錄」，六神栏未录属实且卡面自注；R91 basis 逐字照实登记六神一路无据不入断并降置信；逐爻盘面实载，R91 manifest 结局逐字载「至戊申日沈屙復起，其可謂之蛇動死，虎動主喪耶？」（结局反问收束一面已由在册 R75 条登记、本条不重裁），终局事实层明载可核。故部分成立。',
  '原书六神栏本批未录卡面已自注、六神一路不入断；终局明载'),
]
for cid, flag, finding, short in SINGLES:
    new.append(entry(cid, flag, finding, short))

# ---- assertions ----
ids_new = [e['case_id'] for e in new]
assert len(ids_new) == len(set(ids_new)), 'dup new'
assert len(new) == 103, len(new)
base_anns = ann90['annotations']
assert len(base_anns) == 362
all_anns = base_anns + new
# AS-307 double entry verbatim check
as307 = [a for a in all_anns if a['case_id'] == 'AS-307']
assert len(as307) == 2
verdicts = collections.Counter(a['disposition'] for a in all_anns)
assert verdicts == {'成立': 14, '部分成立': 378, '不成立': 71, '未核': 2}, verdicts

special = list(ann90['special_checks']) + [
 {'item': '（R91）特别核查81：R90 附则承接对勘——平台面 _r90 层 7 件落实验合与 LY-007 承接注记',
  'conclusion': 'runs/round91/judging/outcome-manifest.json 新层 _r90_carryover_notes_addendum 7 件（AS-009／AS-304／AS-306／LY-518／LY-534／LY-626／LR3-010）逐件与 data/case-annotations-r90.json 对应条（registered_round＝90）manifest_carry_suggestion 全文逐字全等（落盘脚本逐件断言全过）：落实 7／维持 0／订正 0，出入 0 件；注记内容与 manifest-carryover-r90-addendum.md §三.1 逐件承接建议逐字对应（含 AS-009 注记须以卡面实载值 horary 回写一条，§二.3）。LY-007 承接注记已按 FREEZE-r91 裁定语写定于本轮新条 manifest_carry_suggestion、自 R92 manifest 起落实。',
  'evidence': 'runs/round91/judging/outcome-manifest.json _r90_carryover_notes_addendum；data/case-annotations-r90.json 七条 manifest_carry_suggestion；data/manifest-carryover-r90-addendum.md §二.3／§三.1；runs/round91/FREEZE-r91.md。',
  'scope_note': '只对勘与登记，不改 manifest 任一侧文本。'},
 {'item': '（R91）特别核查82：平台面旗标定案总登记（新定案 103 条）与承接筛检',
  'conclusion': '平台面新定案 103 条全部分成立（FREEZE 裁定 1：LY-007；盲测席 basis 自报定案 102：OCR／推算复原 groups 76＋ singles 26），逐件回 inputs-dev12 原卡与 R91 manifest 结局原文核对。tradition 旗标候选余 37 件经 FREEZE-r91 裁定全数不成立、只登记不入层（MH-002 首行实逐字照录卡面值、属检查器误报，一并登记）。承接筛检（同旨已在册、不重复立条）与不立条登记见 manifest-carryover-r91-addendum.md §三.4／§三.5。AS-307 双条并行续行、本轮 basis 首行已逐字照录卡面 tradition＝astrology、盘面缺载面与在册 R86 条同旨，不另立第三条。',
  'evidence': 'runs/round91/FREEZE-r91.md；runs/round91/predictions 逐件 basis（487 件全量扫描，扫描件 runs/round91/diagnosis/flag-scan-r91-data-seat.txt）；inputs-dev12 逐件原卡；data/case-annotations-r90.json 在册各条。',
  'scope_note': '结论只及标注与承接建议，不改分数。'},
 {'item': '（R91）特别核查83：紫微供给面首批登记',
  'conclusion': '承 ZIWEI-SUPPLY-BATCH1-r91.md 定案逐项转录：ZW-017／ZW-018 两例 A-low eligible；天纪 P-07 不通过 F②（独立结局不成立、盘面复核已清）；紫微面未用 eligible 实测＝2，距 h34 判据 ≥9 差 7；首批余项 #3／#6／#5／#4 只排期未推进。紫微池 eligible 累计 15 例（ZW-004–ZW-018）。',
  'evidence': 'runs/round91/supply/ZIWEI-SUPPLY-BATCH1-r91.md §二–§五。',
  'scope_note': '只转录登记，不增删供给席结论、不预决组集。'},
 {'item': '（R91）特别核查84：指令性字样基线六处复核',
  'conclusion': '基线六处中 manifest 侧五处经 R91 盘上逐处回读在册、形态未变，出入 0 处：cases 本体四例（BZ-036／BZ-042／BZ-105／LY-204）于 runs/round91/judging/outcome-manifest.json 在场、逐字含基线字样；LR2-016 manifest editor_note 一处于 _r56_lr2016_split 分列层逐字在场。评审包 editor_note 层一处：本席本轮禁读 judging packet 件、未复核该层，只承 R90 在册形态登记、不下在场结论。本轮新增同型件：无。只登记、不改文本。',
  'evidence': 'runs/round91/judging/outcome-manifest.json cases 与 _r56_lr2016_split；data/manifest-carryover-r90-addendum.md §四。',
  'scope_note': '各席一律按数据处理、不作指令。'},
 {'item': '（R91）特别核查85：待核四件维持与 CZ-QX 维持 16',
  'conclusion': '待核四件维持原状、不核查不关闭：BZ-029（俞大维卒年＋旗标错配线索，无新证据；本轮无 R91 prediction 触及新旨）、BZ-040（许世英享年，无新证据；本轮 basis 格局分歧自注只登记触及、维持未核原登记、不入 annotations）、LY-537（「申予日」衍字疑，以未核条目随承接在册；本轮 basis OCR 旗标同旨触及、维持未核）、YM-070（「甲寅旬」出处待核并「都下」语义未明，以未核条目随承接在册；本轮 basis 明载「卡面无残损」、无新证据）。CZ-QX 维持 16：本轮平台集无测字例新结算、同档计数不变，只登记。',
  'evidence': 'data/case-annotations-r90.json LY-537／YM-070 未核条承接；data/manifest-carryover-r90-addendum.md §五.3；runs/round91/predictions BZ-040／LY-537／YM-070 basis。',
  'scope_note': '无盘外独立史源不裁。'},
 {'item': '（R91）特别核查86：验收面占位、并集与已用数登记',
  'conclusion': 'holdout33 验收尚未开封（待平台评审定稿），验收面定案待开封后另行补编（若开封），本轮无验收面新定案。已用并集 1304（runs/round91/used-ids-r91.json 实测 1304 件、与 R90 收束定版逐值相符）；holdout33 封存待开封、holdout34 未组集（紫微面未用 eligible＝2、距判据 ≥9 差 7）。CYJ fidelity 例外 46 件只登记、不充 eligible。',
  'evidence': 'runs/round91/used-ids-r91.json；data/holdout33-seal-log.md；runs/round90/ADDENDUM-r90.md §六。',
  'scope_note': '只登记状态，不复验封存件。'},
]

out = {
 '_provenance': ('R91 数据席（旗标定案流水与承接登记，独立席位，不兼任本轮盲测／评审／诊断／组集／修订，不改方法、不动分数）：'
   '以 data/case-annotations-r90.json 为底承接全量 362 件（成立 14／部分成立 275／不成立 71／未核 2），前 362 件逐件原样、无删改（落盘脚本全等断言验过）；'
   '承接对勘：R91 manifest 新层 _r90_carryover_notes_addendum 7 件（AS-009／AS-304／AS-306／LY-518／LY-534／LY-626／LR3-010）逐件与 r90 条 manifest_carry_suggestion 全文逐字全等、出入 0 件，注记内容与 manifest-carryover-r90-addendum.md §三.1 承接建议逐件对应；'
   '本轮平台面新定案 103 条全部分成立（FREEZE-r91 裁定 LY-007 部分成立为平台面新定案第一件；盲测席 basis 自报定案 102 件：groups 76＋singles 26，逐件回原卡与 R91 manifest 结局原文核对）；tradition 旗标候选余 37 件经 FREEZE-r91 裁定全数不成立、只登记不入 annotations；'
   '合计 465 件（成立 14／部分成立 378／不成立 71／未核 2）。基线六处 manifest 侧五处 R91 盘上复核在册、形态未变，评审包层本轮禁读未复核、只承接登记；CZ-QX 维持 16；待核四件维持；CYJ fidelity 例外 46 件只登记；AS-307 双条并行保留、不合并、本轮不立第三条；'
   '紫微供给首批定案转录登记（ZW-017／ZW-018 A-low eligible、天纪 P-07 不通过 F②、紫微面未用 eligible＝2、距 h34 判据 ≥9 差 7）；已用并集 1304、holdout33 封存待开封（验收面定案待开封后另行补编）、holdout34 未组集。'),
 'round': 91,
 'annotations': all_anns,
 'special_checks': special,
 'counts': {
   'base_file': 'data/case-annotations-r90.json',
   'base_cases_total': 362,
   'base_verdicts': {'成立': 14, '部分成立': 275, '不成立': 71, '未核': 2},
   'carryover_check_r90_addendum': {
     'platform_layer': '_r90_carryover_notes_addendum',
     'platform_items': 7,
     'platform_ids': ['AS-009','AS-304','AS-306','LY-518','LY-534','LY-626','LR3-010'],
     'platform_result': '逐件与 r90 条 manifest_carry_suggestion 全文逐字全等，落实 7／出入 0（层实在 runs/round91/judging/outcome-manifest.json）',
     'acceptance_items_r90': 24,
     'acceptance_status': 'R90 验收面部分成立 24 条照 R83 判例不入 dev 层、本轮无承接件入层，只登记（承 manifest-carryover-r90-addendum.md §三.2）',
   },
   'new_registrations_r91': 103,
   'new_cases_r91': {'部分成立_platform': ids_new},
   'r91_partial_upheld_platform': ids_new,
   'r91_not_upheld_platform_registered_only': 'tradition 旗标候选余 37 件（FREEZE-r91 裁定不成立）＋YM-033／YM-040 卡面旗标不成立 2 件，只登记不入 annotations',
   'acceptance_side_r91': 'holdout33 尚未开封（待平台评审定稿），验收面无新定案；定案待开封后另行补编（若开封）',
   'baseline_instructional_strings': {'items': 6, 'result': 'manifest 侧五处 R91 盘上逐处在册、形态未变，出入 0 处；评审包 editor_note 层本轮禁读 packet、未复核，只承 R90 在册形态登记'},
   'czqx_same_tier_count': 16,
   'as307_double_entry': 'R80 部分成立条与 R85 不成立条并行保留、不合并；R91 无 AS-307 新旗标旨、不另立第三条',
   'pending_four': 'BZ-029／BZ-040／LY-537／YM-070 维持原状；BZ-040 本轮 basis 格局分歧自注只登记触及、LY-537 本轮 basis OCR 旗标同旨触及，均维持未核',
   'ziwei_supply_batch1': {'eligible_new': ['ZW-017','ZW-018'], 'grades': 'A-low', 'tianji_P07': '不通过 F②（独立结局不成立）', 'unused_eligible': 2, 'h34_gap': 7},
   'used_union': 1304,
   'cases_total': 465,
   'verdicts': {'成立': 14, '部分成立': 378, '不成立': 71, '未核': 2},
 },
}
# verify carryover verbatim
for a90, a91 in zip(base_anns, all_anns[:362]):
    assert a90 == a91
layer = man['_r90_carryover_notes_addendum']
r90map = {a['case_id']: a['manifest_carry_suggestion'] for a in base_anns if a.get('registered_round') == 90}
for cid, note in layer.items():
    assert note == r90map[cid], cid
dest = base/'data/case-annotations-r91.json'
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print('written', dest, 'total', len(all_anns), 'new', len(new))
print('verdicts', dict(verdicts))
pref = collections.Counter()
for a in all_anns:
    pref[a['case_id'].split('-')[0]] += 1
print('prefix total', dict(sorted(pref.items())))
prefnew = collections.Counter(c.split('-')[0] for c in ids_new)
print('prefix new', dict(sorted(prefnew.items())))
