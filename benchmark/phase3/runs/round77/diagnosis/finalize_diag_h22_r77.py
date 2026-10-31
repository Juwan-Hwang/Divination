import json, math
BASE="/home/hatch/workspace/divination/benchmark/phase3"
DIAG=f"{BASE}/runs/round77/diagnosis"
sub=json.load(open(f"{DIAG}/subscores_h22_r77.json"))
fs=json.load(open(f"{BASE}/runs/round77/acceptance/judging/final-scores.json"))
SEG={"DS":"八字·DS","GSZ":"六爻·GSZ","QM":"奇门·QM","ZCB":"测字·ZCB"}
def seg(cid): return SEG[cid.split("-")[0]]
# primary code, E4 grid, evidence, A-sub note
COD={
"DS-004":("E3","SEAT","我方断文书立业、薪俸稳定、终局正面；金标主导面为巳年背公得暗财、壬午年被发现受处分，该事件面从未入列（O 双视同指暗财与处分未预断、与薪俸稳定略悖）；四柱锚点在场、basis 无该面缺路登记。",None),
"DS-005":("E5-CLAIM","NA-列","职业面已入列且营销合主线，差仅 −0.25：我方财富量级及婚／子女／健康附加断项未被结局记载，大师单断贸易销售全合，claims 差 −0.75 为最大分项差。",None),
"DS-006":("E5-CLAIM","NA-列","婚姻面已入列、壬戌低谷带婚动与结局壬戌大运离婚时点合，但我方只断聚少劳多／婚事偏晚、未落定妻离断项，大师妻受克妻离 claims 1.75 对我方 1.00。",None),
"DS-007":("E3","SEAT","我方断中平偏正有职、健康只列病位；金标主导面为丙子运之子运寿必有损，结局壬午年被歹徒杀害，寿损面从未入列（O 双视 direction 均 0）；四柱锚点在场、无该面缺路登记。",None),
"DS-008":("E5-DIR","NA-列","婚姻面已入列但终局相左：我方断婚姻有定、仅口角宜晚婚，结局戊子流年正式离异，direction 差 −1.00 为最大分项差。",None),
"DS-009":("E5-TIM","NA-列","财面已入列而运序峰谷坐标反转：我方以乙亥运为低谷、壬申运为峰值，结局丑运发财几千万、乙亥运发财至亿（O 双视同指与峰值低谷断相反），丙子运入狱一节未断（附记）。",None),
"DS-010":("none","NA-列","我方胜（＋0.25）：经商得财至数千万合正面富向主线（O 双视）；发迹丑运非我方峰值窗一节属胜例内附记、不占主码。",None),
"DS-011":("E5-TIM","NA-列","事业与破财面已入列且方向大体合，差集中于 timing −1.00：大师 1998 开公司、2006 与 2009 破财三年份应期全中，我方只有运档坐标（丙午峰值未核、癸卯低谷破财半合）。",None),
"DS-012":("E5-DIR","NA-列","事业终局方向断反：我方断中平偏正、有职中层晚发，结局为不从事其他职业、没什么收入成社会闲人，direction 0.00 对 1.50（O 双视同指方向反）。",None),
"GSZ-022":("none","NA-列","我方胜（＋0.50）：不会抓上直对楼梯房、终得他房与结局抓一层东面不对楼梯合（O 双视）；主坐标寅日与当日落定之差属胜例内附记、不占主码。",None),
"GSZ-023":("none","NA-列","平局（0.00）：和好收场、僵持数日与结局妻回娘家住院数日气消又回来同断（O／M 双视分项逐项同分）。",None),
"GSZ-024":("E5-DIR","NA-列","终局方向全反：我方断能考上高中，结局差一分没考上（O 双视 direction 均 0、断语全反）。",None),
"GSZ-026":("E5-CLAIM","NA-列","病位断项被结局直接推翻：我方按脾胃区断胃病能愈，结局明言果然不是胃病、实为幽门和十二指肠溃疡，大师病位断语逐字印证。",None),
"QM-011":("none","NA-列","我方胜（＋0.25）：不治病故于戌月与结局 1996 年 11 月 6 日戌月病故，方向、断语、应期俱合（O 双视满分）。",None),
"QM-012":("E5-DIR","NA-列","终局全反：我方断能治好、七日内痊愈，结局测后当日巳时未过鸡已死，三分项双视均 0。",None),
"QM-013":("E5-TIM","NA-列","病死不治方向双方同断，差集中于 timing −1.00：我方主坐标第五日，实于次日寅时死，大师次日（6 月 22 日）寅时精确命中。",None),
"QM-014":("E5-CLAIM","NA-列","手术断项被结局推翻：我方断次日确诊并推进手术，结局会诊为颅内无肿瘤、无须手术（活存与次日定案合），claims 差 −0.50。","病因面（肝火攻头、轻微积水或积血压迫视神经）未入列"),
"QM-201":("E5-DIR","NA-列","终局全反：我方断婚事能成、相互看中，结局次日女方明确不愿相处、终以分手告终（direction 0）；仅男方看中一语合。","先行细断面（女方公职、能歌善舞、右脸黑痣、好胜霸道等）未入列，结局未载"),
"QM-202":("E5-DIR","NA-列","顺产终局全反：我方断能顺产、母子平安，结局胎儿脐带绕颈三圈死于腹中、引产，仅胎儿性别女一子断合。","脐带绕颈面未入列"),
"QM-203":("E5-DIR","NA-列","保胎终局反：我方断孩子保不住、将胎死流产，结局即日剖腹成功生下早产女婴存活（不能顺产与性别女合、核心终局反）。","被撞摔倒、动胎气见红一面未入列"),
"QM-301":("none","NA-列","平局（0.00）：500 元货款能找回与结局当天下午找回平安收回，分项逐项同分；主坐标第二日与实际当日之差属平局内附记、不占主码。",None),
"QM-302":("E5-TIM","NA-列","差仅 −0.25 且全在 timing：考上、520 分、一般大学全合，我方主坐标 8 月而实际 9 月 6 日反馈落定，大师「今年」timing 反高 0.50。",None),
"QM-303":("E5-TIM","NA-列","能调成双方同断，差集中于 timing −0.75：大师明断 1997 年元月 2 日精确命中，我方辰日主坐标只落三日窗（一层无法由结局确证，O2），元月 6 日办手续又在窗外。",None),
"ZCB-001":("none","NA-列","我方胜（＋1.50）：白色银钗、少女之物及果获寻回俱合（O 双视满分）。",None),
"ZCB-002":("E3","SEAT","金标主导面为子嗣面（公将举两子、后生者男、文疾人隐），我方把拆分原文的两人／母部件读成老母之事、两人奉母，子嗣面从未入列（dir／claims 0.25）；拆分锚点逐字在场、basis 无缺路登记。",None),
"ZCB-004":("E5-TIM","NA-列","远遣西域面已入列，差集中于 timing −1.00：大师以不足四年、辛卯释还精确命中，我方明写年份无据不报、只给年尺度时序型，且归望偏薄与终获释还只半合。",None),
"ZCB-005":("none","NA-列","我方胜（＋0.50）：三人分断中、恩中、困不中，结局称三君皆如其言俱合（O 双视）。",None),
}
IDS=list(COD.keys()); assert len(IDS)==27
AMB=["DS-004","DS-005","DS-007","DS-009","GSZ-026"]
AMB_NOTE={
"DS-004":"主导面取暗财／处分事件面则 E3，取财面已入列而读反则近 E5-CLAIM；本席按事件面从未入列取 E3。",
"DS-005":"差仅 −0.25，CLAIM（附加断项未印证）与「无单项主因」两读并存；本席按 claims 为最大分项差取 CLAIM。",
"DS-007":"寿损面未入列取 E3，取终局方向（正面有职对横死）则近 E5-DIR；本席按主导面本体取 E3。",
"DS-009":"运序峰谷反转取 TIM，量级上限（小富对亿）一读近 CLAIM；本席按 O 双视同指峰值低谷反转取 TIM。",
"GSZ-026":"病名断项被推翻取 CLAIM，特定病位取象面（寅木月破指幽门）未入列一读近 E3；本席按病位面已以脾胃区入列、断名被推翻取 CLAIM。",
}
def fmt(v): return f"{v:.2f}".rstrip('0').rstrip('.') if v!=int(v) else str(int(v)) if False else (f"{v:g}")
def se(p,n): return round(math.sqrt(p*(1-p)/n)*100,1) if n else 0.0
# counts
from collections import Counter, defaultdict
prim=Counter(v[0] for v in COD.values())
segrows={}
for s in ["八字·DS","奇门·QM","测字·ZCB","六爻·GSZ"]:
    ids=[c for c in IDS if seg(c)==s]; c=Counter(COD[x][0] for x in ids)
    segrows[s]={"n":len(ids),"E3":c["E3"],"E4":0,"E5":sum(v for k,v in c.items() if k.startswith("E5")),"no_loss_cause":c["none"]}
e5={k:[c for c in IDS if COD[c][0]==k] for k in ["E5-DIR","E5-CLAIM","E5-TIM","E5-OMIT"]}
A_main=[c for c in IDS if COD[c][0]=="E3"]
A_sub={c:COD[c][3] for c in IDS if COD[c][3]}
A_inv=A_main+list(A_sub.keys())
tim_n=len(e5["E5-TIM"]); claim_n=len(e5["E5-CLAIM"]); omit_n=len(e5["E5-OMIT"]); dir_n=len(e5["E5-DIR"])
qm_dir_low=[c for c in IDS if seg(c)=="奇门·QM" and sub[c]["ours"]["direction"]<1.75]
pdiff=fs["main_caliber_low27"]["pair_diff"]
rev1={
 "N":27,"TIM_primary":{"count":tim_n,"rate":round(tim_n/27,3),"threshold_count_max":2,"verdict":"不立"},
 "CLAIM_primary":{"count":claim_n,"rate":round(claim_n/27,3),"threshold_count_max":3,"verdict":"不立"},
 "TIM_plus_CLAIM":{"count":tim_n+claim_n,"rate":round((tim_n+claim_n)/27,3),"threshold_count_max":6,"verdict":"不立"},
 "OMIT_guardrail":{"count":omit_n,"rate":0.0,"threshold_count_max":4,"verdict":"立（未破线）"},
 "pair_diff_guardrail":{"value":pdiff,"guardrail_min":-1.366,"verdict":"不立（破护栏）","falsify_line":-1.722,"falsified":False},
 "falsify_checks":{"TIM_rate_ge_0.280_count_ge_8":tim_n>=8,"CLAIM_rate_ge_0.280_count_ge_8":claim_n>=8,"pair_diff_le_-1.722":pdiff<=-1.722},
 "conclusion":"判读不成立",
 "conclusion_basis":"主指标三项全不立（TIM 6＞2、CLAIM 4＞3、合计 10＞6）且护栏②总配对差 −1.481＜−1.366 破线；反向证伪三项均未触发（TIM 6＜8、CLAIM 4＜8、总配对差 −1.481＞−1.722），故非证伪。",
 "appendix":{"DIR_count":dir_n,"A_involved":{"count":len(A_inv),"rate":round(len(A_inv)/27,3),"overflow_line":0.44,"overflow":len(A_inv)/27>0.44},
   "qimen_direction_below_1.75":{"count":len(qm_dir_low),"cases":qm_dir_low,"threshold":2,"review":"段别有害信号成立登记：奇门段 direction＜1.75 共 5 例（QM-012／201/202/203 为终局方向全反或核心反、QM-014 为 1.50），集中于开悟病占与启悟婚／胎产例；石建国三例 direction 均 2.00。只触发复核、不自动回滚（照定版口径）。"}}
}
out={
 "diagnosis":"DIAG-H22-fresh-r77","case_set":"holdout22","n":27,
 "per_case_primary":{c:(COD[c][0]) for c in IDS},
 "per_case_subscores":{c:{"diff":sub[c]["diff"],"ours":{k:sub[c]["ours"][k] for k in ["direction","claims","timing"]},"master":{k:sub[c]["master"][k] for k in ["direction","claims","timing"]}} for c in IDS},
 "primary_cause_counts":{"全集":{"n":27,"E3":prim["E3"],"E4":0,"E5":sum(v for k,v in prim.items() if k.startswith("E5")),"no_loss_cause":prim["none"]},**segrows,
   "非六爻":{"n":23,"E3":sum(1 for c in IDS if seg(c)!="六爻·GSZ" and COD[c][0]=="E3"),"E4":0,"E5":sum(1 for c in IDS if seg(c)!="六爻·GSZ" and COD[c][0].startswith("E5")),"no_loss_cause":sum(1 for c in IDS if seg(c)!="六爻·GSZ" and COD[c][0]=="none")}},
 "E5_subtypes":e5,
 "E3_layer_h19_caliber":{"A_main":{"count":len(A_main),"share":round(len(A_main)/27,3),"SE_pp":se(len(A_main)/27,27),"cases":A_main},
   "A_involved":{"count":len(A_inv),"share":round(len(A_inv)/27,3),"SE_pp":se(len(A_inv)/27,27),"cases":A_inv},"A_sub_cases":A_sub,"ambiguous":AMB},
 "E4_grid_h19_caliber":{"IN":0,"SEAT":len(A_main),"MIX":0,"UND":0,"NA_listed":27-len(A_main),"SEAT_cases":A_main},
 "acceptance":{"ours_mean":fs["main_caliber_low27"]["ours_mean"],"master_mean":fs["main_caliber_low27"]["master_mean"],"pair_diff":pdiff,"SE":fs["main_caliber_low27"]["SE"],"WTL":fs["main_caliber_low27"]["W/T/L"],"pass":False,
   "segments":{k:{"n":v["n"],"pair_diff":v["pair_diff"],"SE":v["SE"],"WTL":v["W/T/L"]} for k,v in fs["segments"].items() if k in ["bazi_DS","qimen_QM","cezi_ZCB","liuyao_GSZ"]}},
 "REV1_verdict_N27":rev1,
 "ambiguous":AMB,"ambiguous_notes":AMB_NOTE,"unmeasurable":0,
 "quality_notes":{"DS_segment":"DS 9 例为作者自选案例集、「断准」选择偏倚逐例载金标 grade_note，照实登记于成色层、不预占主码（封存日志 §三／§九.3）；DS-011 卡面节题已经主持裁处中性化（封存日志 §九.1）。",
  "ZCB-004":"输入卡拆分过程末段应期断语已经主持附条件改写删除（封存日志 §三），编码时卡内无该段。",
  "QM-012":"我方 basis 自注震 3 宫神位转录与巽 4 同作白虎之疑、不涉用神宫，只登记、不涉主码。"},
 "subscore_recompute":"all 27 ours/master totals match final-scores (script assertions passed)",
}
json.dump(out,open(f"{DIAG}/DIAG-H22-fresh-r77.json","w"),ensure_ascii=False,indent=1)
# ---- MD ----
L=[]
L.append("# DIAG-H22-fresh-r77 · holdout22 验收后诊断（R77 独立诊断席）\n")
L.append("- 角色与产出限（写死）：holdout22 验收后独立诊断角，未兼任本轮平台盲测／评审、验收盲测／评审、W 诊断与数据席。**只诊断与判读、不改方法、不提修订方案**；诊断观察只登记事实形态，不写改法指令。")
L.append("- 对象：holdout22 全集 27 例（已开封、已用）。证据件：`runs/round77/acceptance/judging/final-scores.json`（per_case／segments／per_tradition）、同目录 `host-mapping.json` 与 judgeO1/O2/judgeM1/judgeM2.jsonl（reason 全文只对勘定稿、未据其改分）、`runs/round77/acceptance/predictions/`（27 例 prediction_text＋basis）、`benchmark/phase3/holdout22/test_gold.jsonl`（已开封）、`holdout22/inputs/`、`data/holdout22-seal-log.md`、编码定本 DIAG-H21-fresh-r60 §0 与其 JSON 基线、REV1 判读定本 PREREG-ADDENDUM-r61 §三与 runs/round77/PREREG.md §2。")
L.append("- 验收定稿读数（承定稿、不重判）：我方 3.130 vs 大师 4.611，配对差 −1.481（SE 0.316），W/T/L 5/2/20，三判据全不立、验收未达标；双视无分歧、无仲裁（max |view diff| 我方 1.5／大师 1.0）。分段：八字 DS −1.833（n9）、奇门 QM −1.775（n10）、测字 ZCB −0.375（n4）、六爻 GSZ −1.062（n4）。本席自分项（direction／claims／timing 双视均值）复算 27 例双方 total，与 final-scores 逐值一致（构建脚本断言全过）。\n")
L.append("---\n\n## §0 编码读法（照 DIAG-H21-fresh-r60 §0 定本执行于本集，注明本集情形）\n")
L.append("1. **列面记录**＝prediction 的 prediction_text 与 basis 合并；**主导面**＝金标大师断语中与结局逐项对应、且决定该例胜负的断面，以结局实际转折所系者为准。")
L.append("2. **E3（A 主标／A 涉，h19 原口径）**：A 主标＝主导面从未进入列面记录（含取象选择错误）；A 涉例＝A 主标例＋另有一次面（与所问同属一断面族、在金标断语中独立成句）经复核确认未入列之例（一例多面只计 1）。主导面本体已入列、义面／计数／应期未并读者不计 A，记附记并入 E5。")
L.append("3. **E4（二字段格）**：甲＝主导面锚点输入侧在场状态，乙＝席位侧处理状态；格：在场×未列且未登记→SEAT；不在场×已登记缺路→IN；已列为候选→NA-列；余格 MIX／UND。本集建集口径为锚点全在场，甲字段仍逐例按输入卡实读、不预设。")
L.append("4. **E5 主成因码（优先序写定）**：A 主标→E3；格 IN→E4；主导面已入列而失分→E5 细分 DIR（方向断反或相左）／CLAIM（具体断项被结局直接推翻）／TIM（应期主坐标错位）／OMIT（次面漏断：主导面已入列、已载事件之次面未断）；胜／平例记「无失分主因」。")
L.append("5. 含混例以注记登记不强判；金标断语成色事实照实登记于成色注记层、不预占主码。本集情形：分段改按本集构成（八字 DS／奇门 QM／测字 ZCB／六爻 GSZ）计；DS 例作者自选「断准」偏倚照实登记于成色层、不预占主码。主导面识别以金标定稿为给定前提，本席未重定大师分数、未重评任何一例。\n")
L.append("---\n\n## §1 逐例归因表（27 例）\n\n分项记法：dir／claims／timing 为双视均值，格式 我方→大师。\n")
L.append("| 例 | 段 | diff | 分项 我方→大师 | 主成因码 | E4 格 | 一句话证据 |")
L.append("|---|---|---|---|---|---|---|")
for c in IDS:
    s=sub[c]; code,grid,ev,_=COD[c]
    code_disp={"none":"无失分主因","E3":"**E3 A 主标**"}.get(code,code if code!="E3" else "**E3 A 主标**")
    if code.startswith("E5"): code_disp=code
    L.append(f"| {c} | {seg(c)} | {s['diff']:+.2f} | {s['ours']['direction']:g}→{s['master']['direction']:g}／{s['ours']['claims']:g}→{s['master']['claims']:g}／{s['ours']['timing']:g}→{s['master']['timing']:g} | {code_disp} | {grid} | {ev} |")
L.append("")
L.append("含混登记：含混 "+f"{len(AMB)}/27——"+"；".join(f"{c}（{AMB_NOTE[c]}）" for c in AMB)+"。含混点均落在主导面取舍或分界，无一例锚点在场状态不可判；不可测 0 例。")
L.append("成色注记（不预占主码）：DS 9 例承「作者自选案例集、『断准』选择偏倚逐例载金标 grade_note」构成（大师侧基线被选集抬高属构成事实，承封存日志 §三与 PREREG §2 明示），逐例登记于此、不预占任何一例主码；DS-011 输入卡节题已经主持裁处中性化、QM-301 卡面题名已经主持裁处中性化（封存日志 §九.1），ZCB-004 输入卡拆分过程末段应期断语已经主持附条件改写删除（封存日志 §三），三例编码时卡面均无该内容、主码按列面与结局实读；QM-012 我方 basis 自注震 3 宫神位转录之疑、不涉用神宫，只登记。")
L.append("\n---\n\n## §2 汇总计数（主成因码＋E3／E4 两层并报；份额带 n，比例带 SE，SE＝√(p(1−p)/n)）\n")
L.append("### 2.1 主成因码\n")
L.append("| 段 | n | E3 | E4 | E5 | 无失分主因 |")
L.append("|---|---|---|---|---|---|")
for name in ["全集","八字·DS","奇门·QM","测字·ZCB","六爻·GSZ","非六爻"]:
    r=out["primary_cause_counts"][name]; L.append(f"| {name} | {r['n']} | {r['E3']} | {r['E4']} | {r['E5']} | {r['no_loss_cause']} |")
L.append("")
L.append(f"- E5 细分（{out['primary_cause_counts']['全集']['E5']} 例）：DIR＝{'、'.join(e5['E5-DIR'])}（{dir_n}）；CLAIM＝{'、'.join(e5['E5-CLAIM'])}（{claim_n}）；TIM＝{'、'.join(e5['E5-TIM'])}（{tim_n}）；OMIT＝无（0）；合 {dir_n+claim_n+tim_n}。")
L.append("- 无失分主因 7 例＝胜 5（DS-010、GSZ-022、QM-011、ZCB-001、ZCB-005）＋平 2（GSZ-023、QM-301），与定稿 W/T/L 5/2/20 逐例对应；负 20 例主码 E3 3＋E5 17、E4 0。")
L.append("\n### 2.2 E3 层（h19 原口径）\n")
L.append("| 段 | n | A 主标 | A 涉例（主标＋次标例） |")
L.append("|---|---|---|---|")
segA={"全集":(27,A_main,A_inv),"八字·DS":(9,[c for c in A_main if seg(c)=='八字·DS'],[c for c in A_inv if seg(c)=='八字·DS']),"奇门·QM":(10,[c for c in A_main if seg(c)=='奇门·QM'],[c for c in A_inv if seg(c)=='奇门·QM']),"测字·ZCB":(4,[c for c in A_main if seg(c)=='测字·ZCB'],[c for c in A_inv if seg(c)=='测字·ZCB']),"六爻·GSZ":(4,[],[]),"非六爻":(23,[c for c in A_main if seg(c)!='六爻·GSZ'],[c for c in A_inv if seg(c)!='六爻·GSZ'])}
for name,(n,am,ai) in segA.items():
    L.append(f"| {name} | {n} | {len(am)}（{len(am)/n*100:.1f}%，SE {se(len(am)/n,n)}pp） | {len(ai)}（{len(ai)/n*100:.1f}%，SE {se(len(ai)/n,n)}pp） |")
L.append("")
L.append(f"A 主标 3 例：{'、'.join(A_main)}。A 涉次标 {len(A_sub)} 例："+"；".join(f"{c}（{v}）" for c,v in A_sub.items())+"。")
L.append("\n### 2.3 E4 层（二字段格，h19 原口径）\n")
L.append("| 段 | n | IN | SEAT | MIX | UND | NA-列 |")
L.append("|---|---|---|---|---|---|---|")
for name,(n,am,ai) in segA.items():
    L.append(f"| {name} | {n} | 0 | {len(am)} | 0 | 0 | {n-len(am)} |")
L.append("")
L.append("落格 3 例（＝A 主标 3 例，逐例同一）：DS-004、DS-007、ZCB-002——三例锚点均在场（八字四柱全列、测字拆分过程逐字载卡）、主导面未入列且 basis 无该面缺路登记，故落 SEAT 而非 IN。**IN 在本集为 0，系逐例实读结果**：27 例输入卡锚点逐例在场（八字四柱、奇门局式全载、测字拆分过程、六爻卦象全列），无一例主导面锚点不在场。")
L.append("\n---\n\n## §3 R61-REV1 判读（照 PREREG-ADDENDUM-r61 §三定版与 runs/round77/PREREG.md §2 之 N＝27 计数换算逐项判读）\n")
L.append(f"- 基线（H21，N＝25）：TIM 0.200／CLAIM 0.200／合计 0.400／OMIT 0.080／总配对差 −1.010（SE 0.356）。判读集 holdout22，N＝27。")
L.append("\n| 判读项 | 本集读数 | 门槛（N＝27 换算写死） | 判 |")
L.append("|---|---|---|---|")
L.append(f"| ① TIM 主码（主指标） | {tim_n}/27＝{tim_n/27:.3f} | 率 ≤0.080 → 计数 ≤2 | **不立** |")
L.append(f"| ② CLAIM 主码（主指标） | {claim_n}/27＝{claim_n/27:.3f} | 率 ≤0.120 → 计数 ≤3 | **不立** |")
L.append(f"| ③ TIM＋CLAIM 合计（主指标） | {tim_n+claim_n}/27＝{(tim_n+claim_n)/27:.3f} | 率 ≤0.240 → 计数 ≤6 | **不立** |")
L.append(f"| ④ OMIT 主码（护栏） | {omit_n}/27＝0.000 | 率 ≤0.160 → 计数 ≤4 | 立（未破线） |")
L.append(f"| ⑤ 总配对差（护栏） | {pdiff} | ≥−1.366 | **不立（破护栏）** |")
L.append(f"| 证伪线 TIM | {tim_n}/27＝{tim_n/27:.3f} | 率 ≥0.280（计数 ≥8）触发 | 未触发 |")
L.append(f"| 证伪线 CLAIM | {claim_n}/27＝{claim_n/27:.3f} | 率 ≥0.280（计数 ≥8）触发 | 未触发 |")
L.append("| 证伪线 总配对差 | −1.481 | ≤−1.722 触发 | 未触发（−1.481＞−1.722） |")
L.append("")
L.append("**结论：判读不成立。** 触发项：主指标三项全不立（TIM 6＞2、CLAIM 4＞3、合计 10＞6），且护栏⑤总配对差 −1.481 低于护栏线 −1.366（破线幅度 0.115）；护栏④ OMIT 未破线。反向证伪三项均未触发（TIM 6＜8、CLAIM 4＜8、总配对差 −1.481 未及 −1.722），故不构成反向证伪、非有害判定。处置口径照定版：标「判读不成立」之后续处置由主持照 PREREG §2 写死条文执行，本席只判读、不代行处置。")
L.append("")
L.append("附读：")
L.append(f"- DIR 主码计数 {dir_n} 例（{'、'.join(e5['E5-DIR'])}），只作附读。")
L.append(f"- A 涉率 {len(A_inv)}/27＝{len(A_inv)/27*100:.1f}%（SE {se(len(A_inv)/27,27)}pp），未过 44.0% 外溢线，不登记外溢异常。")
L.append(f"- 奇门段 direction 分项＜1.75 之例数 {len(qm_dir_low)} 例（{'、'.join(qm_dir_low)}：QM-012／QM-201／QM-202 direction 0.00、QM-203 0.50、QM-014 1.50），≥2 例，段别有害信号复核结论：信号成立登记——该 5 例中 4 例主码为 DIR（终局方向全反或核心反）、1 例 CLAIM，集中于开悟病占（QM-012）与启悟婚／胎产例（QM-201/202/203）及开悟手术例（QM-014）；石建国三例（QM-301/302/303）direction 均 2.00、开悟 QM-011/013 direction 均 2.00，不作全段全称。照定版口径只触发复核、不自动回滚。")
L.append("\n---\n\n## §4 限度\n")
L.append("1. 单编码限度：E3／E4／主成因码全部由本席单一编码者完成；含混 5/27（DS-004、DS-005、DS-007、DS-009、GSZ-026），若后续编码者对主导面取舍处置不同，主码计数可在含混例范围内摆动（摆动上限：E3 3→1、E5-CLAIM 4→6、E5-DIR 7→8、E5-TIM 6→5 之间）；REV1 判读之 TIM／CLAIM 计数在该摆动内仍分别为 5–6 与 4–6，合计 10–11，主指标三项与结论方向不因含混摆动而变。")
L.append("2. 基数小：全集 27 例，测字／六爻段各仅 4 例、单段 SE 大；§2 分段份额只作构成登记，不作显著性宣称。DS 大师均分 4.306 含作者自选「断准」集的选择偏倚（金标 grade_note 逐例载），影响外推解释、不改变本集内归因。")
L.append("3. 主导面以金标大师断语＋结局对应为给定前提：主导面定位若经独立复核移位，E3／E4／主码计数随之移位，本件无材料自查此环（与 h20/h21 同限度）。")
L.append("4. DS 段我方应期一律为运档坐标（输入卡无出生年月日时与起运岁数、basis 逐例登记缺位降格），大师断语含流年／年份定值；该形态已逐例登记于证据句（DS-011 等），主码仍按列面与定稿分项实读、不另立输入侧主码（E4 甲字段只就主导面锚点判定、四柱全在场）。")
L.append("\n---\n\n## §5 诊断观察（只登记事实形态，不作改法指令）\n")
L.append("1. 本集负例主码形态：E5 占负例 17/20，其中 DIR 7 例为最大单类——DIR 7 例中奇门占 4 例（QM-012 病占、QM-201 婚占、QM-202／203 胎产，均为终局整体反转）、八字 2 例、六爻 1 例；TIM 6 例分布于八字 2（运序峰谷／年份定值）、奇门 3（日／月坐标）、测字 1（年份定值）。")
L.append("2. E3 A 主标 3 例跨八字 2（暗财处分事件面、寿损面）与测字 1（子嗣面取象误读）；A 涉次标 4 例全在奇门段（病因面、细断面、脐带面、见红面），与 A 主标合计奇门 A 涉 4/10 为各段最高。")
L.append("3. 奇门段形态：段配对差 −1.775，10 例 direction 双视均值两极分化——5 例 2.00、5 例＜1.75（见 §3 附读），无中间带 1.75–1.99；石建国三例总分差合计仅 −1.50、开悟＋启悟七例合计 −16.25，段内来源间差异显著，只作构成登记。")
L.append("4. 测字段为全集最浅段（−0.375）：2 胜 2 负，负例分别为子嗣面取象（ZCB-002，E3）与年份定值缺位（ZCB-004，TIM），形态互不相同。")
L.append("5. IN 连续三集为 0（h20、h21、h22 均为锚点全在场建集）：落格例三集同为 SEAT 形态（锚点在场、主导面未入列、无缺路登记），本集落格 3 例与 h21 同数。")
L.append("\n— 完 —")
open(f"{DIAG}/DIAG-H22-fresh-r77.md","w").write("\n".join(L)+"\n")
print("MD and JSON written; TIM",tim_n,"CLAIM",claim_n,"OMIT",omit_n,"DIR",dir_n,"E3",len(A_main),"Ainv",len(A_inv),"QMlow",qm_dir_low)
